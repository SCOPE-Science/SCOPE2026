---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification checks and limits

The self-contained Python 3 program `verify_rank_one_products.py` uses exact arithmetic and enumerates all matrices as possible target products. It checks every predicted fiber, the number of available idempotents, and the total number of ordered products. The sample fields are \(\mathbb F_2\), \(\mathbb F_3\), \(\mathbb F_4\) (implemented by the relation \(z^2+z+1=0\)), and \(\mathbb F_5\).

A stored exact replay covers eighteen combinations across \(n=2,3,4\) and \(r=1,2,3,4\), ending with `VERIFY_OK`. The complete tested set is recorded in the program, and the direct output is in `verification_output.txt`. Run `python3 verify_rank_one_products.py` to reproduce. These finite checks are independent of the general symbolic argument only insofar as they enumerate products directly; they do not prove the infinite field/dimension/length quantifiers. The proof provides that justification by an exact three-eigenspace transition matrix with integer combinatorial interpretation.

No external independent validation or audit has been performed.

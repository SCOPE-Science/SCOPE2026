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

# Reproducibility and checks

Run `python3 verify_joint_squarezero.py` using only the Python 3 standard library.

The script constructs all matrices in dimensions two to four for designated fields, checks the square-zero equation by direct multiplication, computes ordinary ranks of both ordered products, and compares the full observed four-rank table with the closed formula. The test cases are \((n,q)=(2,2),(3,2),(4,2),(3,3),(3,4)\). The field of four elements is implemented as the quotient by the irreducible polynomial \(t^2+t+1\) over \(\mathbb F_2\), not as integers modulo four.

It also checks the complete rank sums against products of independent square-zero populations, the symmetry under exchange of the two operators, exact support, and the maximal-rank diagonal specialization for \(1\leq n\leq11\), with \(q=2,3,4,5,7\). These are finite checks. The unrestricted theorem is established by the proof in RESULT.md, not by extrapolation from the tested cases.

Expected final line: `VERIFY_OK_SQUAREZERO_BIDIRECTIONAL_PRODUCT_RANKS`.

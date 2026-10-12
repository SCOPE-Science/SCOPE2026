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

# Verification notes

The script `verify_super_leafbundles.py` uses the Python 3 standard library. Its `direct` routine creates the leaf-extended adjacency list, enumerates each candidate selected subset, and tests the original super domination predicate for each omitted vertex. Its `formula` routine independently evaluates the proposed boundary-subset polynomial and sums exact coefficients. It also computes connected components and tests the proposed minimum-set product and the high-degree coefficient relation.

Observed result: `VERIFY_OK {'instances': 1150, 'direct_subsets': 2435884, 'random_seed': 271828}`. All labeled simple graphs on up to four original vertices and multiplicities one or two were checked; seeded random cases on five and six original vertices were added. Every pair of integer coefficient distributions matched, along with the two stated coefficient identities. The complete output is in `verification_output.txt`.

To reproduce, put the two supplied files in the same directory and run `python3 verify_super_leafbundles.py`. The program needs no external modules or external files. No execution of other packages or previously produced logs is assumed. Finite enumeration is limited to the exact domains above, and is **not** a proof for arbitrary graph orders; the independent general bijection in `RESULT.md` supplies that proof. This is a self-reviewed result; no independent audit has been performed.

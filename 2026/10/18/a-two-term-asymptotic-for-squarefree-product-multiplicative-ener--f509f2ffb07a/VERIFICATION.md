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

# Verification

The supplied `verify.py` runs two independent exact arithmetic procedures: enumerate all ordered monic input pairs, multiply over a finite field, filter common products by squarefreeness using gcd with the formal derivative, and sum squared multiplicities; independently, count squarefree pairwise-coprime component quadruples by assigning every irreducible of admissible degree to at most one of four degree slots. Möbius inversion supplies the exact number of degree-\(d\) irreducibles. The computations cover all \(n=0,\ldots,7\) for \(q=2\), all \(n=0,\ldots,3\) for \(q=3\), and all \(n=0,1,2\) for \(q=5\): 15 test cases in total. The executable reports `VERIFY_OK` if and only if these finite checks agree.

This exhaustive verification is finite. The proof for arbitrary prime powers and degrees rests on formal Euler-product coefficient extraction and holomorphic analytic tail bounds in `RESULT.md`. In particular, these experiments do not establish the two-term asymptotic by themselves.

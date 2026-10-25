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

Execute `python3 verify.py` in the directory containing the accompanying `verify.py` and `certificate.txt`. The verifier is Python standard-library only and should print `VERIFY_OK`; compare its complete stdout with `certificate.txt`.

## Checks performed

The program constructs each bipartite two-cycle bouquet without relying on a graph-theory library and enumerates every vertex-retention subset for the nine configurations \((4,4)\), \((4,6)\), \((4,8)\), \((6,6)\), \((4,10)\), \((6,8)\), \((4,12)\), \((6,10)\), and \((8,8)\). It recomputes the final \(2\)-core by repeated removal of vertices of current degree less than two. For each possible initial subset size and output size, it checks the exact integer coefficient in the Bernstein expansion of the proposed probability law; these checks certify the complete probability polynomials for the tested graph instances, not just evaluations at chosen \(p\). It also checks the guild degree sequences for paired sizes, exact rational factorization identities, and the direction of both comparisons at rational probabilities on either side of \(1/\sqrt 2\). Total tested initial subsets: 119,424.

## Analytical checks and limits

For the universal all-even-length result, the proof does **not** extrapolate from those nine cases. The essential analytic steps are that the \(2\)-core of a two-cycle bouquet after node deletion comprises precisely its intact original cycles, and that the balancing difference is a polynomial whose at-most-two positive roots are constrained by Descartes' rule. The endpoint root at one is simple; a sign change forces exactly one other positive root. These mathematical arguments cover every pair of admissible even lengths and every real \(0<p<1\). Finite enumerations cannot certify external priority, and no independent scientific validation has occurred.

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

The lower bound was checked from the dual curvature characterization before imposing symmetry on the weight. After normalizing \(\min_e w_e=1\), the feasible test function on a clique edge yields
\[
q\le (p-1)D\left(1+\frac{2D}{p-2}\right),
\]
so every admissible weight has distortion at least the displayed root (and at least \(1\)).

For the candidate optimizer, the three edge types have curvatures
\[
\frac{2}{(p-1)s+q},\qquad
\frac{s+p-1}{s+p-2},\qquad
\frac{2(p-1)s^2+(p-1)(p-2)s-q(p-2)}{((p-1)s+q)(s+p-2)}.
\]
The first two are positive and the third is nonnegative by the defining quadratic inequality for \(s\). The coefficient analysis in the proof verifies that the stated dual values are actual infima, not merely evaluations at one test function.

`verify.py` checks these formulas for \(600\) pairs \((p,q)\) with \(3\le p\le12\) and \(1\le q\le60\), and independently enumerates normalized dual potentials for \(20\) small clique-edge cases. Its expected terminal line is:

`ALL CHECKS PASSED; parameter_pairs=600; brute_dual_cases=20; max_p=12; max_q=60`

These finite checks are not used to infer the universal theorem.

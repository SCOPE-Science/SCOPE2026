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

The proof is analytic and does not depend on an external certificate.

Checks performed:

- Continued-fraction parity: consecutive denominators are coprime, so every four consecutive denominators contain at least two odd members.
- Old-distance upper bound: the two odd denominators among the last four convergents before \(2k-1\) provide two values among \(\delta_{A,1},\ldots,\delta_{A,k}\) bounded by \(\pi/q_{n-2}\).
- New-distance lower bound: best approximation at the convergent immediately below \(2k+1\), combined with the standard lower convergent-error estimate, gives \(\delta_{A,k+1}=\Omega(1/(k(\log k)^2))\) under \(a_j\le j^2\).
- Forbidden-window scale: the source inequalities for \(F_{A,+}\) and \(F_{A,-}\), uniformly on a compact rotation interval, give \(O((\log k)^{12}/k^2)\), which is asymptotically smaller than the new-distance lower bound.
- Cylinder mass: the exact child/parent ratio is \((1+r)/((m+r)(m+1+r))\); summing children with \(m>M\) telescopes to at most \(2/(M+1)\). Thus the restrictions \(a_j\le j^2\) leave positive measure for sufficiently deep starting cylinders.
- Parameter map: \(A'(\gamma)=4\pi^2\tan^2(\pi\gamma)\sec^2(\pi\gamma)>0\), so positive measure is preserved up to a positive local factor on the chosen compact cylinder.

Limits: the result inherits the geometric hypotheses and the definitions of the admissible set from arXiv:2605.00299v1. No independent audit has been performed.

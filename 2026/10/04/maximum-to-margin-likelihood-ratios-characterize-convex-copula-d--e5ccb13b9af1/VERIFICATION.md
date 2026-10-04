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

The finding is analytic; no finite enumeration or simulation is used as proof.

## Replayed checks
1. **Maximum law.** From Sklar's identity, \(G_M(x)=\Delta(F(x))\).
2. **Diagonal regularity.** The standard copula-diagonal characterization gives \(0\le\Delta(v)-\Delta(u)\le d(v-u)\). Hence \(\Delta\) is absolutely continuous, \(q=\Delta'\) exists almost everywhere, \(0\le q\le d\), and \(\int_0^1q=1\).
3. **Density ratio.** The chain rule gives \(g_M=q(F)f\), so \(g_M/f=q\circ F\) almost everywhere.
4. **Likelihood-ratio equivalence.** Convexity of \(\Delta\) is equivalent to a nondecreasing derivative representative. Since \(F\) is increasing, this is equivalent to monotonicity of \(g_M/f\). Conversely the uniform-margin case has density ratio exactly \(q\), so likelihood-ratio order forces convexity.
5. **Information identity.** Substitution \(u=F(x)\) gives \(D_\phi=\int_0^1\phi(q(u))\,du\).
6. **Lower bound.** Jensen yields \(D_\phi\ge\phi(1)=0\).
7. **Upper bound.** Since \(q\in[0,d]\), the endpoint chord inequality for convex \(\phi\) gives \(D_\phi\le(1-1/d)\phi(0)+(1/d)\phi(d)\).
8. **Sharpness.** For \(\Delta(u)=u\), \(q=1\). For \(\Delta(u)=\max\{du-d+1,0\}\), \(q\) is zero on a set of measure \(1-1/d\) and \(d\) on a set of measure \(1/d\). These attain the lower and upper bounds for strictly convex generators; for the upper bound, uniqueness of the displayed diagonal is asserted only within the diagonally convex class.
9. **Kullback–Leibler specialization.** With \(\phi(t)=t\log t\) and \(0\log0=0\), the upper endpoint is \(\log d\). For independence, direct integration of \(q(u)=du^{d-1}\) gives \(\log d-(d-1)/d\).

## Limits
The likelihood-ratio formulation requires the stated regular continuous margin so that a common density ratio on an interval is available. The result identifies only the copula diagonal. The reverse Kullback–Leibler divergence is not covered by the finite bound and can be infinite at the lower Fréchet–Hoeffding extremal diagonal. The closest inaccessible likelihood-ratio-order paper remains an originality risk, not a correctness issue.

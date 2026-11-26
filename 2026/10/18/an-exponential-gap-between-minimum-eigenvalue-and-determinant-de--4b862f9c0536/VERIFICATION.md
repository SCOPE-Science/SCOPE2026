---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Set t=pi*rho^2, a_k=t^k/k!, and p_k=a_k/sum(a). The Gram diagonal is (m+1)p_k; the centered regular polygon makes the Gram diagonal by Fourier orthogonality. The Rayleigh bounds on the two extremes and Hadamard give the three fixed-radius optima. Equality for the condition ratio requires equality in both Rayleigh bounds. The least a_k is an endpoint, so equality for the lower Rayleigh bound makes an endpoint basis vector an eigenvector and forces all angular power sums of orders 1 through m to vanish; Hadamard equality does so directly. Newton identities then force a rotated regular polygon. For t<T_m the least diagonal is the last one and increases strictly after normalization (logarithmic derivative (m-mu)/t), while for t>T_m the first one decreases strictly. For the condition ratio below T_m, the maximum is over k<m (a_m<a_0) and each a_k/a_m decreases; above T_m the maximum is over k>0 and each a_k/a_0 increases. This includes m=1. The optimal determinant has logarithmic derivative (m+1)(m/2-mu)/t; mu' is positive variance divided by t and its limits are 0 and m. At T_m the symmetric endpoint terms agree; the geometric means of the outer factorial pairs are strictly smaller than the means of the retained inner pairs, proving a_k>a_{m-k} for 1<=k<m/2. This gives strict separation for m>=3 and equality for m=1,2. For the asymptotic put b=a_m/sum(a). Then mu=t(1-b) and mu'=1-b(1+m-mu). A Poisson Chernoff bound gives b exponentially small uniformly for m/2<=t<=0.6m, so mu'=1+o(1) there, mu(0.6m)>m/2 eventually, and the root displacement is asymptotic to (m/2)b(m/2). Stirling yields the stated displacement and T_m=m/e+log(2*pi*m)/(2e)+o(1). The modal term at floor(t) is asymptotic to exp(t)/sqrt(2*pi*t) in both cases, and a_0 is the minimum at both optimum radii; their quotient gives exactly the stated prefactor and exponential rate. The proof's sign convention on the Gram off-diagonal phase is conjugated relative to the customary evaluation matrix; conjugation leaves every spectral and equality argument unchanged.

## originality

PASS

The supported distinct claim is the sharp determinant-versus-least-eigenvalue/conditioning comparison, including the unique determinant radius, strict separation for all m>=3, and the sharp exponential relative conditioning loss. There is substantial exact overlap of the least-eigenvalue and conditioning component with a separately indexed, weighted theorem, which is credited rather than treated as novel in isolation. The weighted theorem does not supply the distinct determinant half or the comparison. Relative catalogue dates are not proof of priority.

## value

PASS

A natural exactly solvable square design class separates volume from worst-case stability without comparing different node counts or normalizations. The angles are forced to agree for all objectives, while changing only the optimal radius causes a quantified exponential loss, not just a finite-degree inequality. The all-degree optimizer comparison and asymptotic prefactor are useful even though the E/condition component also appears in a broader theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.

---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Independently, on the unit circle P_s(z)=0 is equivalent to c z + a conjugate(z)=−s b. This real-linear equation is invertible when Δ=|c|²−|a|²≠0, giving the unique candidate z=−sB/Δ. Thus a circle root exists exactly at T and is simple because the other root has modulus |a/c|≠1. The count is constant on each open interval avoiding T; at zero both root moduli are sqrt(|a/c|), and for large s the middle term dominates on the circle, giving exactly one interior root. For the law write b=ρe^(iψ), d=e^(2iψ)conjugate(c), D=d−a and S=d+a. D,S are conditionally independent circular Gaussians of variance 2 with conditional law independent of b. Then Δ=Re(S conjugate(D)), |B|=ρ|D|, and Z=Re(S conjugate(D)/|D|) is standard real normal with conditional law independent of D and b. Hence T=|Z|/ρ with ρ² unit exponential independent of Z. This also proves the stated null exclusions and the independent fair sign. The Gaussian integral gives the CDF, and its density is constant to leading order near zero and asymptotic to 2/s³ at infinity; the advertised beta integral yields exactly −1<q<2, the mean and divergent second moment. Solving the CDF equation gives the median, and the root-count law gives its stated mean and variance.

## originality

PASS

Credit the deterministic Schur test, the mean count, and the standard folded Student t distribution as known tools or consequences, not as novel results. The distinct contribution is identifying that distribution as the threshold of the entire realized holomorphic quadratic root-count path (and the resulting exact fixed-amplitude count probabilities). The strongest available nearby statements did not provide that identification.

## value

PASS

The quadratic is the first case with competing zero-, one-, and two-inside-root counts. Following a single realization under amplitude variation gives an exact path, not only a stability probability. The law gives a precise probability of crossing by a prescribed amplitude and shows that the random crossing scale has a finite mean but no finite variance, features not visible in the constant mean root count.

The dated certificate retains the supplied scientific assessment, sources and limitations.

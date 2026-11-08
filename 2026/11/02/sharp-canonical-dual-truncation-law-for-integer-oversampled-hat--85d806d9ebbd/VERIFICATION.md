---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

Independently reconstructed the Zak diagonalization of the integer-modulation Gabor operator for g=(1−|x|)_+, translations k/q, q>=2, modulation m. The scalar multiplier is Φ=q−2c_q(t)+2c_q(t)cos(2πω) with c_q piecewise quadratic and q strict nondegenerate maxima. Its reciprocal has Fourier coefficients (−r_q(t))^|n|/Δ_q(t), where Δ=√[q(q−4c)] and r=(q−Δ)/(q+Δ). Multiplying by Zg(t,ω)=(1−t)+te^{2πiω} yields γ_q(t+n)=(−r)^n[1−t(1+r)]/Δ. Laplace expansion at the q maxima yields I_n∼E_q R_q^(2n)/√n with positive E_q; reflection symmetry and a geometrically weighted tail yield 2E_q/(1−R_q²). Domain fixed q>=2, n→∞; no uniform-q bound. I independently numerically integrated cells at n=25,80,250 for q=2,3,4,7. Ratios to asymptotic tend to unity, e.g q2: 0.9967864,0.9990145,0.9996866; q3: 0.9961467,0.9988089,0.9996202. Finite quadrature is not proof of the asymptotic.

## originality

PASS

PASS qualified for explicit sharp cellwise L² canonical-dual tail and truncation constant at every integer q>=2; not for frame bounds, Zak diagonalization or qualitative exponential decay. A highly relevant 1996 Janssen integer-redundancy/minimal-dual paper was inaccessible in full, so its precise formula coverage remains material residual risk.

## value

PASS

An exact canonical minimum-energy dual can have a sharp intrinsic infinite tail even when other compactly supported duals exist. The optimal exponential factor and n^(-1/2) saddle prefactor, plus exact leading truncation error, are independently useful for controlled spatial truncation. The specific fixed-integer oversampling family and rate are natural rather than arbitrarily chosen.

The dated certificate retains the supplied scientific assessment, sources and limitations.

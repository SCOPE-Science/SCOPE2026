---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

The unnormalised axial transform is H(t)=4∫₀¹(1−x⁴)^{1/4}cos(tx)dx; the endpoint at x=1 has amplitude √2(1−x)^{1/4}, yielding C=4√2Γ(5/4), phase t−5π/8 and t^{−5/4}. The quartic disk area is 4Γ(5/4)^2/Γ(3/2); independent gamma calculation confirms (5/2)C²/(2|K|)=5√π and 4/3 times this is 20√π/3. For near-axis angle θ, the quartic stationary-point scaling μ=θ t^{3/4} gives the uniform t^{−5/4}(1+|μ|)^{−1/3} decay. Fixed nonaxis directions have smooth positive-curvature stationary-phase decay t^{−3/2} with nonzero leading mean square, causing p=3 divergence. At p=5/2 the μ≈1 cutoff t≈|θ|^{−4/3} gives log angular factor 4/3 and the stated coefficient; the uniform large-μ tail is integrable after s=|θ|t^{3/4}. For 5/2<p<3, the local bound ρ_p²≲|θ|^{−8(p−5/2)/(3p)} has exponent <1, so four measure-zero infinite rays still allow finite planar area. These analytic estimates establish the three exact phases for all p, not just the finite diagnostic sample. The displayed endpoint/beta constant and exponents were checked independently.

## originality

PASS

PASS best of knowledge: general Fourier-mean-body theory brackets the quartic disk but does not calculate its isolated-flat-direction phase diagram, sharp residue or critical angular horn. Classical finite-type techniques are prior inputs, not claimed new.

## value

PASS

The quartic disk is a canonical strictly convex finite-type body just outside the strictly-positive-curvature class. Its Fourier-mean radial operator undergoes an unexpected middle regime with four infinite yet finite-area logarithmic/power horns; exact index 5/2 and sharp constants quantify the first curvature-degenerate transition. These are concrete natural geometric-analysis invariants, not routine substitution of a previously covered curvature theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.

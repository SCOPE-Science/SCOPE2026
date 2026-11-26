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

Inverting the four modes gives the heat weights (A,B,C,B)=((1+2q+q⁴)/4,(1−q⁴)/4,(1−2q+q⁴)/4,(1−q⁴)/4) for q=e^(−t), with row sum one. Only C can be negative for t>0; 4C=(1−q)(1−q−q²−q³) has the asserted simple interior threshold. When C≥0 both heat stages preserve the cube, and the exact scalar flow does as well since its squared denominator minus z² is e^(−2ρ)(1−z²). When t<θ, C<0 and A>A(θ)=q*>1/2. For the impulse e_0 the first heat stage has signs +,+,−,+, all nonzero. Taking the exact reaction flow to its sign limit makes the opposite composition coordinate converge to C+2B−A=1−2A<0; the strict limit ensures failure already at a finite ρ for each such t. For ρ=0 the map is H_(2t) with nonnegative threshold t=θ/2, including equality. Below θ/2 the derivative of the composition at zero is e^ρ H_(2t); its strictly negative opposite component on e_0 gives arbitrarily small failing inputs for each fixed finite ρ. This does not assert the intermediate-regime threshold for each fixed ρ. Independent replay `python3 /workspace/independent_reproduction.py 4` used the full matrix exponential, giving H_(2t)e_0 opposite +0.07419904 but opposite split output −0.08922606 at e^(−t)=0.6 and ρ=log(100), and gives a small-amplitude failure below θ/2. The analytic sign limits, not these finite checks, prove the universal quantifiers.

## originality

PASS

Li already studies effective maximum principles and counterexamples for the same Fourier-collocation Allen–Cahn Strang scheme. Credit that direct precedent and the prior general phenomenon of eventual linear positivity. The supported distinct claim is the exact four-node nonnegative-cube cutoff uniform over all reaction strengths, with the sharp factor-of-two distinction from the full heat map. Neither the prior effective bound nor the closest indexed linear positivity results supply this exact finite nonlinear classification.

## value

PASS

The four-point grid is the first standard periodic Fourier grid with a negative off-diagonal Laplacian entry (two and three nodes are Metzler). The complete cutoff at that minimal size diagnoses a real failure mode: even a nonnegative full heat kernel can give a negative split result after strong pointwise reaction. That quantified distinction is useful for interpreting maximum-principle tests in a canonical spatial discretization; it is not a claim about accuracy, unconditional stability, or positivity between nodes.

The dated certificate retains the supplied scientific assessment, sources and limitations.

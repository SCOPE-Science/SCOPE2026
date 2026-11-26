---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The class exit rates from a particular ordered pair, not just an average, are 2α from A and 2β from B to D; from D the rates into A, B and absorption are p, q and κ as given. At each visit to D there is positive chance κ/(α+β) of absorption on the next jump; no-jump events ensure positive survival at any finite time. First-step equations give the three stated rational transforms with common denominator det(sI−Q). For −Q the reversible weights π_D=1, π_A=p/(2α), π_B=q/(2β) give the positive quadratic form p(x_A−x_D)^2+q(x_B−x_D)^2+κx_D^2. For unequal rates the secular function is strictly decreasing between poles with opposite signs across each root bracket, giving the strict interlacing. For equal rates the middle eigenvalue is 2α and its residue cancels in all three laws. Residue division by λ_j gives D all positive nonzero survival coefficients (at least two), hence a strictly negative hazard derivative. In a slow starting part the survival after factoring out exp(−λ1 t) is positive, increasing and strictly concave, so its log is strictly concave and the hazard increases. In a fast starting part the derivative, up to positive factors, is a strictly negative constant plus two positive decreasing exponentials. It starts positive because Q²1 gives h′_A(0)=2ακ (or h′_B(0)=2βκ) and ends negative, so there is exactly one positive critical time. The leading residue is positive in all cases. The limiting positive λ1 is the smallest eigenvalue of −Q as explicitly defined in the proof, not an eigenvalue of Q with that sign. Frozen verify.py and VERIFICATION.md were inspected, not run. Their recorded 426 rational identities and 18 numerical shape samples are corroboration, not the general proof.

## originality

PASS

The supported distinct contribution is the strict monotone/one-peak classification under unequal location-dependent rates, with exact threshold α=β for arbitrary m,n≥2. Existing equal-rate meeting laws, general backward methods, and differently meaningful collision rates were credited rather than treated as new.

## value

PASS

The statistic answers how the prospective encounter risk changes with elapsed nonencounter time, which a mean or limiting decay rate cannot determine. A unique peak in just the faster starting part, with a kinetic equality threshold independent of both part sizes, is a structural classification over a natural graph family and nontrivial parameter range.

The dated certificate retains the supplied scientific assessment, sources and limitations.

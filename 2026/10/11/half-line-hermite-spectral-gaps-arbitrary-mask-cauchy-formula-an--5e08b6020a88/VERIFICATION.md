---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

Normalized Hermite boundary values are u_a=psi_{2a}(0), v_b=psi′_{2b+1}(0), from Rodrigues formulas. Green/Wronskian identity applied to oscillator energies 4a+1 and 4b+3 yields the centered positive-halfline block B_{ab}=u_a v_b/(2b+1-2a); same-parity centered blocks vanish. Distinct even/odd energy labels imply nonzero scaled Cauchy maximal minors and rank r=min(e,o). Singular-value pairing gives exactly |e-o| midpoint modes and nonzero-gap product as sum of squared maximal Cauchy minors; nonzero analytic Hermite polynomials cannot vanish on either open halfline, so all concentration eigenvalues are strictly inside (0,1). For contiguous 2m levels a single Cauchy determinant yields D_m=product_{j=0}^{m-1}Gamma(j+1)^2/[Gamma(j+1/2)Gamma(j+3/2)]; Barnes-G recurrence and large-z expansion give limit sqrt(pi) G(1/2)^2 times m^{-1/4}. Independent mpmath/numpy calculation m=1..5 matched exact determinant vs gamma products to <4e-16; this does not substitute for the proof.

## originality

PASS

Reviewed equivalent Gaussian Hankel determinant / parity of positive GUE eigenvalue counts, not just Hermite vocabulary. Its–Krasovsky and Charlier derive large-n asymptotics for jump parameter beta in the strict |Re beta|<1/4 strip; a true sign jump corresponds to beta=1/2 and is outside these stated theorems. Charlier–Deaño works with nonnegative real jump s∈[0,1], excluding s=-1. None of these read results supplies finite arbitrary-mask Cauchy minors. However known exact GUE index-parity expectations or endpoint extensions might reproduce lowpass Barnes formula, a real unclosed originality risk. The all-mask feature remains separately significant and no covering comparison was found.

## value

PASS

The oscillator and centered halfline are canonical spectral/spatial coordinates. Every finite sparse selection of Hermite modes has an exact transition eigenspace and collective off-center gap product; in the physically natural lowpass regime this invariant has a sharp quarter-power decay with Barnes constant. This answers a motivated spectral concentration question and is not a finite table entry, even if the Cauchy and Barnes identities used are classical.

The dated certificate retains the supplied scientific assessment, sources and limitations.

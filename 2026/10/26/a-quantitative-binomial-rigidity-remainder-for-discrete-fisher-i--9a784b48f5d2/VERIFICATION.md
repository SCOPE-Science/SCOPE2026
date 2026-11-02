---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

PASS: The score sigma_i=2-4 p_i^{-1}sum_{u<=i}(-1)^(i-u)p_u satisfies endpoint identities -2,+2 for balanced positive laws; direct convolution rearrangement gives E[s_X|X+Y]=E[t_Y|X+Y]=sigma_{X+Y}(f*g). The gap equals E Var(a s_X+b t_Y|X+Y). Expanding each fiber variance into positive pair terms and retaining adjacent (i,j-1),(i-1,j) gives a coefficient f_i f_{i-1}g_jg_{j-1}/h_{i+j-1} at least c=(min f)^2(min g)^2. Centering score increments (sum_i delta s_i=sum_j delta t_j=4) gives exactly n a² E_f+m b² E_g+16mn(a/m-b/n)². Vanishing forces all increments affine and a/m=b/n; the adjacent mass recurrence uniquely gives the balanced binomial laws. Under tau_f<=2/m, each relevant positive score-ratio factor is >=2/m and the log ratio between f_i/B_i steps is bounded by m tau_f; accumulating and normalizing gives TV<=min(1,(e^(m² tau_f)-1)/2), analogously for g. Independently derived exact symbolic perturbation deficit (10/3)eps²-(376/3)eps⁴+O(eps⁶) for m=n=2, while TV=|eps|, confirming optimal local exponent 1/2; a separate exact rational example verifies the three-part inequality. The coefficient c is small and no dimension-free statement is made.

## originality

PASS

PASS, qualified: Ball–Gárgyán 2026 introduce exactly this balanced discrete score, prove the unquantified convolution information inequality and characterize binomial extremizers of an associated Cramér–Rao inequality. The nonnegative adjacent-pair quantitative remainder, explicit TV closeness from score increments, and optimal square-root deficit exponent were not identified in the materially read sections of their primary paper. Nishiyama and Gibilisco–Isola use different discrete information frameworks. The adjacent-edge estimate is elementary once the prior variance identity is known, but the connected quantitative inverse theorem is a natural new consequence; an implicit earlier stability estimate remains possible.

## value

PASS

PASS: Stability of equality in an information inequality is a standard mathematically motivated gap, not just a rephrased nonnegative deficit. The result identifies the exact extremizers, quantitatively forces both score sequences toward affine increments, bounds total variation to balanced binomial laws, and gives a sharp local square-root exponent while transparently retaining mass-sensitive constants.

The dated certificate retains the supplied scientific assessment, sources and limitations.

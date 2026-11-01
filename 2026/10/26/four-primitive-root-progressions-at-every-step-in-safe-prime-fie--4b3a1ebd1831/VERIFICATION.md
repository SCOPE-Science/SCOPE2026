---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

For safe p>=11, multiplicative order p−1=2q shows primitive roots are precisely quadratic nonresidues except -1, the sole order-2 nonresidue. The character class of four consecutive nonresidues has count B_p=[p−10−4chi_p(2)+S_p]/16: reflection t→−3−t exchanges square/non-square patterns since chi_p(-1)=−1; odd character sums vanish, each distinct quadratic pair sum is −1, and correcting the four zeros gives the -10−4chi2 constant. Scaling x=dt maps all prescribed steps to one of two equal sign-class counts; deleting progressions containing -1 gives exactly E_p(d)<=4. Weil’s degree-4 quadratic character sum bound |S_p|<=3sqrt(p) gives B_p>(p−14−3sqrt p)/16>4 for p>=113. For safe p<113 the finite list 5,7,11,23,47,59,83,107 is complete and all x,d were exhaustively checked; min counts 0,0,0,0,1,1,1,4. The universal part follows from the Weil inequality and finite exhaustive cutoff, not extrapolation from higher sample primes.

## originality

PASS

Jarso–Trudgian proves the four-CONSECUTIVE (unit-difference) primitive-root question and exact exceptions. Carella 2019/2022 Section 15.1 treats any *fixed tuple of distinct offsets* for sufficiently large p with asymptotic error; that does not provide a uniform finite bound simultaneously for every nonzero d in F_p nor the sharp safe-prime threshold 47. This claim strengthens quantification from fixed d to every field step and provides an exact count with an explicit exceptional -1 correction. The unit-step d=1 specialization is already known at the existence level and is not advertised as new.

## value

PASS

Uniform existence of four primitive roots at every prescribed nonzero additive step is a natural strengthening of the classic consecutive-primitive-root question. The sharp least safe-prime cutoff, exact dependence on step and a complete certified finite exceptional range are substantive arithmetic facts; not merely a sample count.

The dated certificate retains the supplied scientific assessment, sources and limitations.

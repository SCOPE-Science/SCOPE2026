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

## Analytic checks

1. For \(F_u(h)=\|u+h\|^p\) and \(p>1\), convexity gives one-sided directional derivatives; the triangle inequality gives the upper bound \(p\|u\|^{p-1}\) for unit directions. The direction \(u/\|u\|\) attains it when \(u\ne0\); when \(u=0\), the directional derivative equals zero. Hence equality of norm-power germs up to a constant identifies component radii.
2. After equal radii are known, the constant difference vanishes at zero; Steinhaus separation of equal-radius distinct vectors then excludes unequal components. This is valid for every real Banach space.
3. For any index family, varying one coordinate of the \(\ell_p\)-sum gives a constant difference of the corresponding component's \(p\)-th-power norms. Absolute convergence is the only summability input.
4. For finite families, a failure of uniform positivity produces a pair with identical norm germs in an ultrapower. The ultrapower of a finite \(\ell_p\)-sum identifies isometrically with the finite sum of ultrapowers; uniform positivity in each component implies ordinary Steinhaus separation in its ultrapower. This contradicts Check 3.
5. For the reverse uniform implication, \(s\mapsto(s^p+t)^{1/p}\) is \(1\)-Lipschitz on \([0,\infty)\), so a pair in a single coordinate has exactly its original pointwise separation modulus in the whole sum.
6. The \(p=1\) and \(p=\infty\) witnesses in RESULT.md have open perturbation neighborhoods on which the two norms agree exactly; rational grid diagnostics were also run but are not the proof.

## Limits and evidence

The result is analytic and does not rely on empirical extrapolation, numerical optimization, or external proof certification. The first public version of the 2013 source is dated 26 February 2013. The 2026 source poses a stronger quantitative direct-sum modulus question, and the theorem here does not establish a universal modulus constant. The statement covers real Banach spaces, arbitrary index sets for ordinary \((S)\), and only finite index sets for uniform \((S)\).

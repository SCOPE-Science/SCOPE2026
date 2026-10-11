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
# Verification and reproducibility

The theorem is proved analytically. To reproduce the central checks, choose any nonzero vector in the first block to obtain the exact norms \(\|I_Y-D_\varepsilon\|=\varepsilon\) and \(\|D_\varepsilon^{-1}\|=(1-\varepsilon)^{-1}\); choose unit vectors in blocks with index tending to infinity to obtain \(\|D_\varepsilon\|=1\). For any fixed nonzero vector, choose a norm-one functional supporting its nonzero diagonal image. The \(1\)-unconditional multiplier property gives absolute convergence of its coordinate evaluations and a strict coefficientwise inequality, hence no norm attainment. Because the operator is invertible, its image of the closed unit ball is closed; applying a norm-one projection preserves this exact closed image. These checks cover real and complex scalars and every admissible block dimension.

Reproducible concrete family: in \(L_p(0,1)\) for \(1\le p<\infty\), use the dyadic intervals \(E_n=(2^{-n},2^{1-n}]\). Multiplication by the step function taking value \(1-\varepsilon/n\) on \(E_n\) has norm one, inverse norm \((1-\varepsilon)^{-1}\), and exact distance \(\varepsilon\) from identity. Every nonzero function has strictly decreased norm, while functions supported on late intervals asymptotically saturate the operator norm.

No numerical computation, automated proof certification, or independent external audit is asserted. Unconditionality is an explicit hypothesis; the conclusion is not asserted for arbitrary Schauder decompositions or for infinite \(\ell_\infty\)-products.

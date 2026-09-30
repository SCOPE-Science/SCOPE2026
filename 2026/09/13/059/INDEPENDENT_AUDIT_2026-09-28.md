# Independent audit — SCOPE-20260913-059

Date: 2026-09-28 (UTC)  

## Disposition: PASSED

### Correctness
The proof checks. The semicircle logarithmic integral is log(sigma)-1/2, so Delta(s1)=e^-1/2 and Delta(s1+s2)=sqrt(2)e^-1/2. Multiplicativity gives Delta(p1)=sqrt(2)/e>0. The Brown logarithmic-potential identity at zero then rules out any atom at zero, since positive mass at z=0 would force the extended integral of log|z| to be -infinity. The record correctly leaves the punctured support-gap radius unresolved.

### Originality
This is a clean instance-specific consequence of standard Fuglede–Kadison and Brown-measure machinery, not a new general method. A targeted search found no source treating exactly p1=s1^2+s1s2, but the proof is sufficiently direct that priority should be described conservatively as limited.

### Scientific value
The exact atom mass answers one component of the target and supplies a useful determinant check, but it does not address the harder local support geometry near zero.

### Sources checked
- Fuglede and Kadison, Determinant theory in finite factors: https://doi.org/10.2307/1969645 — Foundational multiplicative determinant used in the factorization p1=s1(s1+s2).
- Haagerup and Schultz, Brown measures of unbounded operators affiliated with a finite von Neumann algebra: https://arxiv.org/abs/math/0605251 — Brown-measure/log-determinant framework; the present operator is bounded and lies in the classical setting.

### Limitations
- No positive support-gap radius is proved or disproved.
- The stored artifact path in the prose uses the historical output/artifacts prefix although the repository file is under artifacts/; this does not affect the theorem.

# Scientific review — alternating-grid BDF3 parasitic spectrum

## Correctness — PASS
The claim concerns the homogeneous, interpolation-defined third-order BDF recurrence on strictly alternating positive widths, with a **fixed** width ratio. Differentiating the cubic at its newest node gives the two explicit matrices in `RESULT.md`. Their two-step product has exactly stated trace and determinant. Three fully factored positive rational expressions satisfy the strict quadratic Schur conditions after scaling eigenvalues by five; no finite enumeration is used to conclude the universal bound. The limiting trace \(-1/5\) and determinant zero prove optimality; summability of the resulting differences proves convergence of the original solution. Two independent symbolic formulations and rational-parameter checks completed using `verify.py`.

Boundary qualification: both widths must be strictly positive, and the ratio is fixed throughout repeated alternations. The strict multiplier bound holds for every finite ratio, whereas the supremum is approached only in singular ratio limits. Norm-wise transient control is not uniform in the ratio. No theorem is asserted for general meshes or nonzero differential-equation right-hand sides.

## Originality — PASS, qualified
Full-text comparison with Li–Liao (2022), especially coefficients (1.1)–(1.5), Theorem 3.1, remarks and numerical examples, finds a sufficient general-mesh step-ratio bound near \(2.553\). This does not imply unconditional stability on fixed alternating meshes with an arbitrarily large ratio at infinitely many positions. Full-text comparison with Söderlind–Fekete–Faragó (2018), especially Theorem 5.1 and BDF3 specialization, finds a smooth-grid condition requiring neighboring step ratios to approach one, not the present alternating setting. Published prior-record and literature searches on alternating BDF3, reciprocal-ratio products, Floquet monodromy, and the sharp constant \(1/5\) did not reveal an exact covering statement.

The specialized earlier papers of Guglielmi–Zennaro (2001) and Skeel–Jackson (1983) provide relevant general-matrix-product or Nordsieck stability theory. Their accessible abstracts describe restricted mesh policies rather than the present unrestricted two-cycle formula, but their complete texts could not be inspected. An equivalent older calculation remains a genuine priority risk; this qualification is not a claim of independent novelty certification.

## Value — PASS
General variable-step BDF3 stability conditions are strongly sensitive to adjacent-ratio restrictions. The theorem isolates a natural, implementable counterpoint: compensation across alternating long and short steps guarantees geometric parasitic damping regardless of the magnitude of either reciprocal ratio. The exact sharp constant \(1/5\) is a structural two-step rate, not an arbitrary sampled invariant, and distinguishes the asymptotic spectrum from potentially large within-period transients. Its applicability and limits are determined explicitly.

## Closest sources and limits
Li and Liao, *Stability of variable-step BDF2 and BDF3 methods*, arXiv:2201.00527v1 (2022); Söderlind, Fekete and Faragó, *On the zero-stability of multistep methods on smooth nonuniform grids* (2018); Guglielmi and Zennaro, *On the zero-stability of variable stepsize multistep methods: the spectral radius approach* (2001); Skeel and Jackson, *The stability of variable-stepsize Nordsieck methods* (1983). See `RESULT.md` for references and exact boundaries. The finite checker supports, but does not replace, the analytical proof.

Self-review: passed. Independent audit: not yet performed.

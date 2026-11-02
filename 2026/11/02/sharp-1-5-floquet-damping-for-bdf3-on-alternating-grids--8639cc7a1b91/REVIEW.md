# Self-review

## Correctness

**PASS.** The four-node cubic interpolation construction uniquely determines two coefficient triples. Direct multiplication yields the reduced quadratic factor of the two-step monodromy. Three strict Schur--Jury inequalities reduce to polynomials with positive coefficients, establishing \(|z|<1/5\) for every \(r>0\), not merely enumerated ratios. Both singular endpoint limits are \(\{0,-1/5\}\) and prove optimality of the constant. The reciprocal discriminant identity and Descartes' rule prove the mode transition and its uniqueness. The exact symbolic checker reproduces the critical identities from interpolation data. Zero-stability follows from power boundedness of one fixed three-dimensional monodromy and boundedness of its one-step phases for each fixed \(r\).

## Originality

**PASS on inspected material, with residual risk.** The closest relevant published spectral-radius paper is Guglielmi--Zennaro (online 2000), whose available abstract describes a general ratio-bound approach. Its full text was inaccessible, which leaves a specific possible undocumented periodic-grid comparison. Li--Liao's accessible 2022 theorem addresses ratios bounded by approximately \(2.553\) almost everywhere, and Söderlind--Fekete--Faragó (2018) analyze smooth grids with ratios approaching one. None of the material inspected states or implies the sharp all-positive-ratio two-periodic \(1/5\) disk, or the discriminant transition. Absence from searched indexes is not a uniqueness certificate.

## Mathematical value

**PASS.** Alternating ratios are a natural stress test for variable-step multistep methods. The theorem proves an unexpectedly stable entire unbounded-ratio family beyond available general sufficient ratio conditions, giving the exact optimal parasitic damping constant and a nontrivial real/complex spectral phase transition. It reveals why unrestricted one-step jump size alone is not a necessary instability criterion. Its scope is explicitly limited to homogeneous zero stability, not full perturbed stability.

## Closest literature and limitations

See Guglielmi--Zennaro (2000/2001), Li--Liao (2022), and Söderlind--Fekete--Faragó (2018) in `RESULT.md`. The inaccessible full text of Guglielmi--Zennaro is the leading originality risk. Uniform-in-r transient bounds, arbitrary switching, A-stability, and inhomogeneous stability are outside the result.

Self-review: passed. Independent audit: not yet performed.

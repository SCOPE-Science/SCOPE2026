# Same-model review

Same-model review: passed. Cross-model review: not yet performed.

## Correctness

**Verdict: PASS.**

The argument reduces the upper bound to the componentwise uniform-submajorization estimate proved in Theorem 3.2 of Huang--Pliev--Sukochev--Xu and combines the component estimates by finite iteration of their Proposition 3.1. The loss introduced by finite iteration is arbitrary and disappears in the norm limit. The Russo--Dye reduction is valid because the generalized derivation is bounded into the symmetric ideal.

For the lower bound, the atomic type-I-infinity counterpart of the construction underlying Lemma 4.2 is applied independently on each factor. The cited paper explicitly states that its atomic case follows by the same argument. Taking the direct sum of the component partial isometries preserves the contraction bound. Additivity of distribution functions over a finite disjoint union shows that dilation commutes with the merged rearrangement. Equation (4) of the cited paper then yields the factor (N-1)/(N+1), which tends to one.

Stress tests are consistent: for one summand the theorem reduces to Huang--Pliev--Sukochev--Xu Theorem 1.1; for positive implementers it reduces to their properly-infinite non-factor formula; and the explicit two-summand rank-one example directly verifies the claimed strict gap between center-local and global cross-center pairing.

## Originality

**Verdict: PASS, to the best of our knowledge.**

The closest source is Huang--Pliev--Sukochev--Xu (2026). Its exact self-adjoint theorem is stated for infinite semifinite factors, while its exact non-factor theorem assumes positive implementers. Remark 4.3 says that the factor hypothesis cannot simply be dropped and gives an abelian obstruction, but it does not state a finite-center replacement formula. The paper's general Theorem 3.2 supplies a global upper bound, not the center-local exact expression established here.

Searches using “generalized derivation”, “finite direct sum”, “finite-dimensional center”, “atomic center”, “central summand”, “symmetric ideal/space”, and equivalent norm-formula terminology did not locate the center-local theorem or the explicit cross-center sharpness mechanism. Earlier center-valued derivation formulas found in the literature concern inner derivations or different targets and do not imply the generalized two-implementer formula here.

The primary 2026 paper was inspected in the sections containing its introduction and main theorems, uniform-submajorization machinery, factor lower estimate, factor-hypothesis remark, and finite/infinite direct-sum discussion. The complete texts of Fialkow (1979) and Fialkow--Loebl (1984) were not inspected; their scope and relevance were checked through the 2026 source and accessible bibliographic material. They remain the principal residual originality risk. No inaccessible source produced concrete evidence that the present finite-center formula is already covered.

## Value

**Verdict: PASS.**

The result identifies a sharp implication boundary left open by the factor/non-factor split in the recent exact norm theorem. It gives a reusable rule for finite atomic centers—local spectral sign matching followed by global rearrangement—and an elementary two-summand example explaining why the naive global factor expression fails. The mechanism applies to arbitrary symmetrically normed sequence spaces rather than only Schatten classes.

## Limitations

The theorem is restricted to finite direct sums of infinite type-I factors and self-adjoint compact implementers. The proof does not establish the analogous statement for infinitely many central summands, and no failure claim is made there. The literature search is necessarily non-exhaustive, with the two older norm-ideal papers above representing the most relevant uninspected full texts.

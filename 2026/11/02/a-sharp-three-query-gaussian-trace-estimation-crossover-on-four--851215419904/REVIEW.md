# Independent mathematical audit

## correctness

PASS

Conditioning on q=Ag/||Ag|| makes trace(H++) unbiased and variance twice the expected squared Frobenius norm of (I-qq^T)A(I-qq^T). Projector algebra gives 3+2(lambda-1)u+(lambda-1)^2u² for u=w/(lambda² z+w), chi-square(1)/chi-square(3) ratios. The beta angular integral yields Eu=(2lambda+1)/(lambda+1)^2 and Eu²=(lambda²+3lambda+1)/(lambda+1)^3. Direct SymPy differentiation independently checked the resulting rational variance difference and negative derivative of the ratio, and numerical root verification gave 4.56842704056585. Descartes sign changes prove uniqueness for all lambda>0; lambda=1, scale s>0, conjugation and lambda→infinity treated explicitly. Sampling is not a proof and is not used here.

## originality

PASS

Meyer–Musco–Musco–Woodruff original Hutch++ paper provides the query allocation algorithm and general PSD sample complexity, while Persson–Cortinovis–Kressner discuss spectrum-dependent allocation and Gaussian variance. Their inspected Algorithm 1 and introductory formulas do not state the exact 4D one-spike three-query quintic crossover. Search of Resultary did not find an equivalent. Risk remains that a closed special-case moment follows implicitly from general variance bounds or overlooked low-rank formulas.

## value

PASS

Smallest matrix dimension d=4 where three queries do not already permit deterministic complete-basis trace evaluation. The exact crossover quantifies a genuine benchmark at fixed compute budget; its monotone spectral dependence and counterintuitive flat-spectrum loss are useful estimator-allocation information rather than a cosmetic substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.

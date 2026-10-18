# Review of the binary adjacent-pair collision law

## Correctness
PASS. The exact Fourier integral follows from the bijection between the full ordered-pair profile and the two loop counts plus the telescoping endpoint flag. The transfer matrix has precisely two peripheral spectral points; at both, the dominant projection and covariance Hessian give the same Gaussian contribution. The determinant \(1/16\), endpoint weight \(3/8\), and factor two from the peripheral points yield \(3/(4\pi)\). Direct exhaustive spectra and an independent run-composition formula agree for all words through length \(17\), with exact mass sums through length \(800\). A fixed-length census alone would not establish the limit; the explicit spectral-gap argument does.

## Originality
PASS against the checked record, subject to residual risk. Jacquet–Knessl–Szpankowski enumerate cyclic types; Karhumäki–Saarela–Zamboni retain extra unigram information; Gabrys–Milenkovic describe the same ordered linear spectrum but do not state the sharp collision probability. A particularly close published note, *Exact binary two-multispectrum code size and singleton classification*, supplies full finite ambiguity-class formulas; squaring and summing them in principle determines each finite collision probability. **Those formulas are prior work and are not claimed as new.** The new contribution assessed here is the explicit leading asymptotic constant, with a full nontrivial two-peak spectral derivation. The possibility that this precise asymptotic has already been worked out as an unindexed consequence remains an identifiable risk.

## Value
PASS. This is the natural probability that length-two ordered reads from two unrelated fair binary words are indistinguishable. It supplies the leading constant for the expected ambiguity and collision Rényi entropy. Because the number of feasible spectra is quadratic but the collision probability decays only linearly, the result quantifies the strong inhomogeneity of ambiguity-class sizes, not a routine re-count of profile types.

## Scope and limits
Fair binary i.i.d. words, complete uncorrupted adjacent-pair multispectra, linear not cyclic. No general alphabet or source distribution theorem, and no independently performed audit.

Self-review: passed. Independent audit: not yet performed.

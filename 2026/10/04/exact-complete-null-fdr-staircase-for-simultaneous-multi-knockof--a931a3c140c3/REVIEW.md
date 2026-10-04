# Review
## Correctness
PASS. The threshold algebra was reconstructed directly from the published simultaneous multi-knockoff FDP estimator. Under the complete null, the published conditional-uniformity lemma turns decreasing-gap winner labels into iid increments \(+1\) and \(-r\). Because the walk is upward skip-free, nonempty selection is exactly a first hit of level \(r\). The Raney count gives the finite formula, and the bounded harmonic equation gives the infinite-feature root law. Exact rational enumeration in `verify.py` independently checks finite cases and boundary locations.

Risk: the formula assumes positive pairwise-distinct gaps. Ties can change which prefixes are reachable and are excluded from the claim.

## Originality
PASS. The closest source, Gimenez and Zou, supplies the uniform-label lemma, threshold, FDR-control proposition, and detection threshold, but its inspected main text and supplementary proof do not state an exact complete-null finite-feature FDR, a Raney/Catalan first-passage law, or the limiting root formula. Targeted searches using multi-knockoff, complete-null, exact FDR, first-passage, Catalan, Raney, and Selective SeqStep terminology found control theorems and related multiple-competition methods rather than this statement. Emery and Keich analyze a different multiple-knockoff construction.

Risk: the first-passage enumeration is classical once the procedure is reduced to a skip-free random walk, so an equivalent consequence could appear in competition-based multiple-testing work under different notation.

## Value
PASS. The source emphasizes that simultaneous knockoffs reduce the detection threshold from \(\lceil1/q\rceil\) to \(\lceil1/(q\kappa)\rceil\). The exact law quantifies the calibration consequence of that design choice: at fixed nominal level, detection threshold one can make the global-null FDR bound asymptotically sharp, while larger thresholds remain substantially conservative. This is a natural finite-sample invariant of the published procedure and supplies exact benchmarks for simulation, implementation checks, and comparisons of admissible \((\kappa,r)\) choices.

Same-model review: passed. Independent audit: not yet performed.

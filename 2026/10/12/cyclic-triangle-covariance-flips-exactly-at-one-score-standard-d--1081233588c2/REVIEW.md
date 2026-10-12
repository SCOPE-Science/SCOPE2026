# Review

## Correctness

PASS. Conditioning on one vertex outdegree leaves all edges among the other vertices independent and fair. This gives the exact conditional cyclic-triangle mean and the quadratic score-imbalance correction. Vertex exchangeability then proves the master covariance identity.

The two-vertex score-class probability is computed by conditioning on their shared edge, and the cyclic-triangle variance follows because distinct cyclic-triangle indicators are pairwise independent even when the triangles share one edge. The local central-limit profile is a direct substitution into the exact correlation formula.

## Originality

PASS, with a specific residual risk. The classical full text of Beineke--Harary explicitly gives the deterministic score-sequence formula for cyclic triangles, but not a random covariance with score-class counts. Barbour--Godbole--Qian use the same independent fair random-tournament model for different statistics. Andersson treats asymptotic counts of fixed digraphs, which includes cyclic triangles marginally but does not make the moving degree-class statistic a fixed subgraph count.

Targeted searches for score-class/cyclic-triangle covariance, outdegree-class covariance, and the one-standard-deviation sign rule found no matching statement. Andersson's full text was not accessible, so possible implicit overlap there is retained as a risk rather than dismissed.

## Value

PASS. Vertex scores and cyclic triangles are canonical local and global measures of tournament balance. The theorem identifies an exact finite sign phase at the natural score standard deviation, not an arbitrary parameter slice, and the master identity explains the phase structurally through squared score imbalance.

The local-limit profile quantifies the effect on the natural central score scale and shows that the sign transition is stable asymptotically rather than a finite-size coincidence.

Self-review: passed. Independent audit: not yet performed.


Exact replay: `VERIFY_OK tournaments=33864 conditional_checks=18 covariance_checks=18 variance_checks=22 sign_checks=18 master_checks=12`.

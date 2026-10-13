# Review

## Correctness

PASS. For a fixed vertex \(j\), conditioning on indegree zero means that all \(n\) independent images avoid \(j\). The images of the other \(n-1\) vertices are therefore independent uniform choices from the remaining \(n-1\) labels, and \(j\) itself cannot lie on a cycle. This proves the Palm identity without an asymptotic approximation.

The cyclic-point tail law follows from the exact count of rooted forests with a fixed root set. The matrix-tree determinant gives that count directly, and the resulting point probabilities telescope to the displayed tails. Those tails strictly increase with mapping size, which proves the entire monotone-transform sign statement.

## Originality

PASS, with a bounded residual risk from older local-structure literature. The closest full inspected source is Hansen--Jaworski's exchangeable-indegree paper. It studies exactly the same functional-digraph object, gives the cyclic-point distribution in a much broader indegree model, and its coding algorithm explicitly deletes zero-indegree vertices. Later in the same full article it discusses expected numbers of zero-indegree vertices in constrained mapping models. The inspected text does not state a mixed law between the total zero-indegree count and the cyclic-point count.

The companion local-properties paper has verified primary classification \(60C05\) and treats predecessor/successor distributions. Drmota's correlation paper concerns distance strata from the cyclic set, which are not the zero-indegree fringe statistic.

## Value

PASS. Zero-indegree vertices are the removable fringe of a functional digraph, while cyclic vertices form its persistent core. The result gives an exact finite bridge between these two canonical layers: size-biasing by fringe size performs a one-vertex dimension reduction on the core law.

The threshold identities show that the conclusion is stronger than one covariance number. Every increasing cyclic-core diagnostic is negatively correlated with the zero-indegree count, with exact finite threshold covariances.

Self-review: passed. Independent audit: not yet performed.


Exact replay: `VERIFY_OK mappings_checked=873612 distribution_checks=28 tail_checks=28 mean_z_checks=6 palm_checks=27 threshold_covariance_checks=21 covariance_checks=6`.

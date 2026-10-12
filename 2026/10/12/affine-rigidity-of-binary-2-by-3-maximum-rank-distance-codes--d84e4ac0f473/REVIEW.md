# Review: Affine rigidity of binary 2 by 3 maximum-rank-distance codes

## Correctness
PASS. Row puncturing gives the analytic bound \(|C|\le8\). The embedded verifier exhausts the entire \(64\)-matrix graph and finds exactly \(384\) equality cases. A second route enumerates all \(1395\) three-spaces of \(\mathbb F_2^6\), obtaining exactly \(48\) linear MRD spaces, equal to the zero-containing clique census. Their \(384\) affine cosets reproduce every maximum. The natural group sizes \(6\) and \(168\), the single orbit of size \(48\), and stabilizer \(21\) are recomputed directly.

## Originality
PASS with stated residual bibliographic risk. Delsarte’s full paper supplies the rank metric, Singleton bound, and linear Singleton-system constructions, but not this unrestricted binary \(2\times3\) equality classification. Later nonlinear-MRD literature shows that non-affine equality cases exist in broader settings, so affinity is not implied by the general MRD property. Targeted searches for binary \(2\times3\) MRD, nonlinear/affine aliases, exact counts \(384\) and \(48\), and bilinear-form Singleton-system classifications found no statement implying the claim.

## Value
PASS. MRD equality cases are the rank-metric analogue of MDS equality cases, and nonlinear MRD phenomena are known in general. Proving that the smallest rectangular binary instance at distance \(2\) has no nonlinear extremizer is a structural rigidity fact, not merely a recomputation of the Singleton number. The complete count and one-orbit classification give a reusable small-parameter benchmark.

## Closest literature and limitations
The closest foundational source is Delsarte (1978), which proves the bound and constructs linear equality cases. Cossidente–Marino–Pavese (2016) and Otal–Özbudak (2018) document nonlinear/non-additive MRD phenomena in broader parameter ranges. The present result is finite, and an obscure unindexed small-parameter enumeration remains a bibliographic risk.

Self-review: passed. Independent audit: not yet performed.

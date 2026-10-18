# Independent mathematical audit

## correctness

PASS

For each simple unweighted cycle C_n (n>=3), graph-state bipartite entropy in bits is the F_2 rank of the S-by-S^c cut-adjacency matrix. If not every edge crosses the cut, maximal crossing-edge runs are disjoint alternating paths; an L-edge path contributes exactly ceil(L/2) to cut rank. A four-state parity transfer T(z,t) records membership cardinality z and rank t, with one unique closed walk whenever a noncrossing edge exists. On even n=2m, the two all-alternating membership patterns have matrix I+P over F2 with rank m-1, while the cyclic transfer trace spuriously contributes four weight z^m t^m; replacement gives E_n(z,t)=tr(T^n)+1_(even n)*2 z^(n/2)t^(n/2-1)(1-2t). The univariate eigenvalues 0,1,(1±sqrt(1+8t))/2 and dominant-eigenvalue expansion derive the exact odd/even means, variance 2n/27+O(n²2^-n), and CLT for UNCONDITIONED uniform subsets. Independently enumerated all 2^n vertex subsets for each n=3..15 and computed binary cut ranks; the direct generating function matched the transfer/run formula, including C12 balanced histogram (12,96,306,386,124). This finite corroboration is not the all-n proof.

## originality

PASS

Sakib’s complete 2025 ResearchGate-hosted manuscript defines the same conditional entropy statistic and provides exact cut-rank histograms for graphs of size at most 12, including cycle C12; it does not prove an all-n bivariate transfer enumerator. Nguyen–Oum’s full primary paper covers unconditional average cut-rank on general graphs and structural results, but a first moment does not determine conditional fixed-k distributions. Hein et al. establish the graph-state rank/Schmidt correspondence, which is credited. The particularly relevant published Resultary cycle graphical-group theorem was opened in full: its 3-state transfer enumerates ranks of full antisymmetric edge-weighted matrices over F_q, yielding partial analogous run methods and potentially some unconditioned rank expressions, but no binary bipartition cut rank marked jointly by |S|. Thus the full bivariate claim is not dominated, with acknowledged analogue and possible prior recurrences.

## value

PASS

The exact joint cut-cardinality / entanglement law for every cycle C_n computes all conditional entropy histograms, their Shannon heterogeneity and unrestricted asymptotic fluctuations, extending a specific finite graph-state invariant introduced and measured in 2025. The four-state transfer and parity-cycle correction answer a motivated exact counting question. It does not demonstrate enhanced circuit performance or a balanced-cut CLT.

The dated certificate retains the supplied scientific assessment, sources and limitations.

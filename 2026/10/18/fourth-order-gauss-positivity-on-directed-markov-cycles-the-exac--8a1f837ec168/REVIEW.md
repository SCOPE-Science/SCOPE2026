# Scientific review: fourth-order Gauss positivity on directed Markov cycles

## Correctness

**PASS.** The proof fixes the row-generator convention and strictly positive cycle rates. The directed passage-time formula supplies an explicit group inverse \(G\) and establishes \(QG=GQ=I-\Pi\), \(\pi G=0\), and \(G\mathbf1=0\). Restricting the rational Padé map to the nonstationary subspace yields \(T(h)=I+12G/h+O(h^{-2})\). For every cycle with at least four states, the sum of the forward-neighbor entries of \(G\) is the strictly negative nonadjacent-pair sum. The three-state zero-sum exception forces equal rates, and exact circulant calculations establish sufficiency. The two-state spectral calculation verifies the remaining case. Four-state numerators and a one-positive-root sign argument give the sharp uniform cutoff. An exact rational/symbolic verification program corroborates 406 independent assertions, but is not taken as proof of the infinite-family result.

## Originality

**PASS, with a residual literature risk.** Zappavigna, Colaneri, Kirkland and Shorten (2010; 2012) established Padé positivity failures and sufficient timestep conditions, and the 2012 work explicitly describes a cyclic-feedback Metzler matrix (equation 18). Its illustrated fourth-order failure specializes that matrix to an eight-dimensional **open nilpotent chain**, not an irreducible cycle; the inspected results do not classify all positive rates and all step sizes on conservative cycles. Classical group-inverse/first-passage relations are treated as prior methods. The contribution assessed here is the exact all-step equivalence, heterogeneous-triangle rigidity, all-dimensional nonadjacent-pair obstruction and exact uniform-four-cycle frontier. Other numerical positivity investigations of Laplacian graphs or different Runge–Kutta maps do not entail this all-rate directed-cycle classification. Searches cannot exclude an equivalent unindexed result, particularly in earlier numerical analysis theses and positivity-preserving discretization literature.

## Value

**PASS.** Directed-cycle generators are a canonical irreducible, nonreversible transport model; preservation of stochastic nonnegativity is a physical constraint on a numerical transition matrix. The theorem gives a complete and sharp answer for the entire rate-labeled class, isolates a fragile homogeneous three-state exception, and identifies a universal graph-structural mechanism for the failure, quantified by nonadjacent-pair holding-time products. The first failing uniform cycle also has an exact finite timestep cutoff. This is a motivated structural classification rather than an arbitrary finite example or generic positivity counterexample.

## Evidence and limits

The public manuscripts of Zappavigna et al. (2010), https://mural.maynoothuniversity.ie/id/eprint/2195/ , and Zappavigna et al. (2012), https://mural.maynoothuniversity.ie/id/eprint/3761/ , were consulted, including the cyclic-feedback model, the nilpotent eight-state example, and positivity sufficient conditions in the latter. Rossi, Colaneri and Shorten (2011), DOI 10.1109/TAC.2011.2161028, concerns polyhedral Lyapunov preservation rather than the stated transition-entry classification. The bound for general cycles is eventual sign loss; the complete positivity interval is characterized only for the equal-rate four-cycle. Formal independent mathematical validation and a guaranteed exhaustive literature survey have not been performed.

Self-review: passed. Independent audit: not yet performed.

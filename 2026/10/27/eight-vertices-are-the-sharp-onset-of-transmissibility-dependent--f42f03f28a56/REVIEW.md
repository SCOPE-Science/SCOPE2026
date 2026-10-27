# Scientific review

## Correctness — PASS

The probabilistic identity \(\mathbb E[Z_v]=1+W_v(p)/(n-1)\) follows by unique paths and independent percolation. Prüfer enumeration visits every labelled tree of orders two through eight; center-rooted canonical codes merge precisely the isomorphism classes, and their count is independently matched against \(1,1,2,3,6,11,23\). Each universal-optimality test uses a sufficient exact integer nonnegativity identity valid at **all** real \(0<p<1\), not a parameter grid. For each of two exception types the candidate optimum sets at exact rational \(p=1/2\) and \(p=9/10\) are disjoint, conclusively proving the absence of a universal optimizer. Explicit tree polynomials yield unique sharp thresholds. The package-contained `verify.py` was executed successfully. The computational proof is bounded to \(n\le8\) only.

## Originality — PASS, provisionally

Holme's full-text continuous-time Markov SIR analysis includes vaccination-related node rankings; after matching per-edge transmissibility, its **mean** tree objective agrees with independent-bond Reed–Frost despite dependence in higher-dimensional outbreak laws. Its enumeration stops at seven vertices and does not establish the first eight-vertex crossover or classify the two new exception types. Hall–Siebert's inspected full-text rooted-tree Markov SIR/SEIR theorem gives node-state probabilities without optimal single-vertex deletion rankings. Hosoya–Wiener tree-polynomial formulas give a broader computational language but not, on accessible evidence, the eight-vertex vaccination switching classification. Published mathematical-record searches using epidemic vaccination, deletion polynomial, tree and transmissibility aliases identified no covering theorem. The exact finite classification is assessed as original under available literature, not independently priority-certified.

## Value — PASS

The optimum vaccine target is typically chosen under uncertainty about per-contact transmissibility. The first possible failure of a transmissibility-independent best target is a natural structural cutoff: it quantifies when the intuitive heuristic “vaccinate the same critical tree vertex” ceases to be valid. Two distinct tree topologies and exact thresholds illustrate a meaningful choice between isolating a high-degree hub and severing an internal connector. Finite but complete size-eight census and all-parameter certificates matter even without extending to infinite families.

## Scope and remaining risks

The result does not cover graphs with cycles, nonuniform infection sources, dependent outgoing contacts, multiple removed vertices or more than eight vertices. Priority uncertainty remains from literature on distance-polynomial graph vulnerability and node deletion not located in full text; the 2007 weighted Hosoya–Wiener paper was accessible at abstract level but its publisher-hosted PDF was not retrieved. Computational reproducibility and a self-review are not independent audit.

Self-review: passed. Independent audit: not yet performed.

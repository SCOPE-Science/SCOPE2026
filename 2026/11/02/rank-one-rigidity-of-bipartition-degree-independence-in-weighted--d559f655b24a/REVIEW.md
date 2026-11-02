# Scientific review

## Correctness (C): PASS

The theorem is for all finite \(a,b\ge2\) with strictly positive real \(w_{ij}\); degrees are ordinary edge counts. Every hub event has positive mass and exactly the stated attachment structure. Conditional leaf choices factor by column, giving the degree means, and summing them proves the inverse identity. Independence of full side-degree vectors makes all conditional means independent of the hub, forcing equal normalized columns. Rank-one sufficiency follows from the explicitly derived weighted matrix-tree generating polynomial, which factorizes into two shifted multinomial generating functions. The exact-rational standalone checker enumerates spanning trees across fourteen small weighted cases; this is support, not a substitute for the general proof.

## Originality (O): PASS, qualified

The closest inspected source is Fita Sanmartín–Schnörr–Hamprecht, arXiv:2409.13472v1, particularly its introduction, degree-moment theorem and covariance appendix. Its arbitrary-graph covariance formulas address first and second moments and do not state a matrix-rank characterization of independence between *entire* bipartition degree vectors. Dong–Ge, arXiv:2103.05294v1, proves forest-constrained counts in the unweighted complete bipartite graph, not the positive-weight converse. The Fischer–Fischer 2019 accessible first-page preview addresses the number of attainable degree sequences and does not contain the relevant probabilistic statement; its remaining pages were not accessible for full inspection. Broad literature searches and mathematical research-record comparisons did not reveal equivalent coverage. The classical bicolored Prüfer enumerator already proves rank-one sufficiency; this is openly credited. The claim-to-prior implication comparison leaves the positive-weight necessity and exact conditional recovery as distinct. Hidden earlier weighted-tree literature remains a priority risk.

## Value (V): PASS

This is a natural complete classification, valid for arbitrary part sizes and *all* positive edge-weight arrays, of exactly when a familiar stochastic independence phenomenon survives heterogeneity. The constructive necessity is stronger than observing an example of lost independence: a finite collection of conditional degree means exactly recovers normalized edge preferences, and gives a concrete statistical witness against factorization. It addresses structural probabilistic identifiability rather than an arbitrary numerical case; the result could guide model diagnostics and dependence calculations in Gibbs spanning trees.

## Scope and remaining limits

Positivity and both part sizes at least two are indispensable. The theorem does not identify column scales or say pairwise uncorrelated degrees suffice. It is not a theorem for noncomplete graphs or for all tree measures. Historical priority is assessed by best available material, not proven by absence from searches. Independent verification is outstanding.

Self-review: passed. Independent audit: not yet performed.

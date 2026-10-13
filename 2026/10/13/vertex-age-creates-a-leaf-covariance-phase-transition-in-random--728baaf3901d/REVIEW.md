# Review

## Correctness

PASS. The parent choices in a random recursive tree are independent. Conditioning on \(P_j=v\) destroys the leaf event at \(v\), protects every other earlier vertex from being selected at time \(j\), and is independent of later-born leaf indicators. Summing these exact contributions gives the local formula, and summing potential children gives the harmonic aggregate formula.

The finite sign theorem follows from an explicit positive second discrete difference, together with the endpoint signs. The macroscopic limit follows from the harmonic tail. Exact exhaustive enumeration through \(n=9\) and an independent rational threshold replay agree with every displayed identity.

## Originality

PASS, with a residual risk from older joint-distribution literature. Addario-Berry--Eslava provides the closest inspected full source for labeled/high-degree behavior in the same model; it reviews degree-profile results but does not discuss leaves or terminal vertices.

Najock--Heyde is the classical source for terminal-vertex counts, while Drmota--Hwang studies sign changes among level-profile correlations and Janson studies global degree-count covariance. None of the accessible statements retains the deterministic birth label and pairs its outdegree with the total leaf count.

The strongest novelty is not a marginal moment: it is the local \(j=2v\) sign law and the induced single birth-time threshold at a nontrivial constant fraction of the growth horizon.

## Value

PASS. Vertex degree and leaf count are canonical local and global observables of recursive-tree growth. The result identifies the mechanism by which a single attachment has two competing effects on the final leaves and shows that their balance reverses exactly at twice the vertex's birth time.

Summing that local mechanism produces a natural macroscopic phase boundary at approximately \(28.47\%\) of the growth horizon. This gives a structural explanation of how vertex age controls dependence with a global tree-shape statistic.

Self-review: passed. Independent audit: not yet performed.


Exact replay: `VERIFY_OK trees_checked=46233 leaf_mean_checks=8 local_cov_checks=84 aggregate_cov_checks=36 convexity_checks=123747 threshold_checks=494 asymptotic_checks=26`.

# Scientific review

## Correctness — PASS

The controlled process is defined on finite labeled complete rooted regular trees, with independent uniform offers sampled with replacement. The strictly increasing radial Bellman solution proves global optimality even against history-dependent policies; the exact first-difference recurrence and finite expectation formula are independently checked. For positive drift, the sum of independent downward-level passage times and a uniformly exponentially integrable coupling to the infinite biased walk yield the Gaussian limit, including variance \(4pq/(p-q)^3\). For outward drift, the leaf-to-leaf/root excursion renewal decomposition and exact rare-success probability give the mean and exponential limit. The checker reproduces 3,481 exact and analytic-consistency assertions. A finite checker is not the source of the infinite-horizon proof.

## Originality — PASS, qualified

The original power-of-choice walk literature already specifies the with-replacement model, general hitting-time methods and the outward-drift obstruction for an infinite four-regular tree. The present statement does not assert discovery of the drift observation. Its contribution is the fixed-branching all-offer integer threshold combined with exact finite-height optimal expectation and Gaussian-versus-exponential limit laws for leaf-to-root passage. A full-text review of the relevant open-access source and comparison of accessible indexed findings revealed no implication-equivalent result; neither a database search nor a finite paper selection proves historical uniqueness. Standard one-dimensional birth-death theory can be used to derive the formula, and independently published variants remain a residual priority risk.

## Value — PASS

Root targeting on regularly branching search spaces is a natural benchmark for the exact cost of local choice. The integer choice threshold separates \(\Theta(h)\) and \(\Theta((q/p)^h)\) expected search durations; because the number of vertices is exponential in \(h\), this distinguishes logarithmic from polynomial search in network size. The associated Gaussian versus rare-excursion exponential laws identify fundamentally different uncertainty and tail mechanisms. The classification is exact for every fixed integer branching factor and offer count; it is not merely a small numerical example or a reparameterization of a single previously stated bound.

## Closest literature and limitations

Georgakopoulos, Haslegrave, Sauerwald and Sylvester (arXiv:1911.05170; DOI:10.1017/S0963548321000183) provide the underlying walk model and qualitative regular-tree drift observation, but not the compared finite-height expectation and paired depth-dependent weak limits. Related indexed tree-coupling and graph-indexed-walk results concern different processes or target quantities. The theorem is restricted to known-root complete regular trees and independent uniform with-replacement choices; priority remains qualified, and external audit has not been completed.

Self-review: passed. Independent audit: not yet performed.

# Independent mathematical audit

## correctness

PASS

Read the full RESULT.md and verify_spectrum.py in the actual record. Enumerating all 24^4 choices of four permutation rows and enforcing column distinctness yields precisely 576 indexed squares. Inspecting each of the 36 possible row/column intercalates gives a 144-by-432 incidence B with degrees 12 and 4 (1728 edges). The exact integer identity BB^T=12I+2H, H 18-regular with entrywise annihilator H(H+6I)(H+2I)(H-6I)(H-18I)=0 and traces (144,0,2592,10368,176256), determines H eigenvalue multiplicities (-6:15,-2:81,0:8,6:39,18:1). Thus A has zero mult 318 and paired eigenvalues sqrt(8) mult81, sqrt(12) mult8, sqrt(24) mult39, sqrt(48) mult1, proving displayed characteristic polynomial. Degree normalization A/sqrt(48) yields lazy gap (1-1/sqrt(2))/2. Independent freshly written checker enumerated all 576, checked every exact polynomial residual, all-pair BFS diameter=6, degree counts, traces. This is finite exhaustive proof because order is fixed, unlike an extrapolation.

## originality

PASS

Best-of-knowledge PASS for complete labeled adjacency spectrum and exact lazy-walk gap, not for 576 count or 432:144 degree partition. Wanless classified a quotient on isotopy/main classes. Davis explicitly considers the SAME labeled 576-vertex graph but accessible record reports degree classes and Laplacian top eigenspace, not the full spectrum. Its actual spectral_branch.pdf was inaccessible, so priority remains materially qualified.

## value

PASS

A complete characteristic polynomial and sharp degree-biased lazy-walk spectral gap of a canonical finite move graph are natural exact Markov-chain / algebraic invariants useful for sampling and understanding connectedness; 576 labeled states form a nontrivial graph, not an arbitrary slice or known 16-vertex Latin-square graph. The degree partition itself is prior known, not claimed new.

The dated certificate retains the supplied scientific assessment, sources and limitations.

# Independent mathematical audit

## correctness

PASS

Read the complete 5×20 binary generator column list and independently computed all 32 codewords. They are distinct; among 31 nonzero messages exactly 30 have two zero cyclic 3-windows and one (message 14) has none; thus d3=18 and linear dimension=5. Each cyclic triple of columns has rank3, with exactly three nonzero annihilating messages. Universally, a length n dimension5 binary generator with d3≥n−2 has at most 62 zero windows across nonzero messages, while each position supplies ≥3; hence 3n≤62 and n≤20. At n20,d18 the three-symbol Singleton d3≤n−2 and Griesmer 7n≥Σ_{j=0}^4 ceil(4d3/2^j)=140 are attained.

## originality

PASS

The binary b-symbol Griesmer bound already implies the n≤20 upper cutoff; the new ingredient is an explicit binary linear [20,5,18] three-read code attaining it with a complete 31-word certificate. Resultary search found related pair-metric codes and 3-read families with other parameters, not the same witness; targeted exact parameter searches found no positive match. Full primary construction tables were inaccessible and remain a real prior-implication risk; acceptance is best-of-knowledge for the exact attaining example.

## value

PASS

Dimension-five binary 3-read Singleton-optimal maximal length is a natural extremal construction question. General upper bounds alone do not construct a code. A finite explicit generator at the sharp n=20 boundary with complete weight distribution and equality in two bounds closes that concrete existence gap; this is not an arbitrary narrow sample or known-table recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.

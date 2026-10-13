# Self-review

## Correctness
PASS. The non-overlapping grain definition is reconstructed from the inspected primary source. The packaged verifier uses two independent constructions of allowed grain patterns and error balls, a complete maximal-clique census, a separate branch-and-bound maximum-clique computation, and a separate increasing-order enumeration of all ten-cliques. All agree on maximum size \(10\), exactly \(16\) labeled maxima, and common core \(\{001100,011001,100110,110011\}\).

## Originality
PASS. The closest inspected exact-parameter source is Kashyap--Zémor's finite-bound table, which lists lower bound \(10\) and upper bound \(16\) for length \(6\), two grains. Thus it leaves the equality unresolved. published-finding corpus and web searches over exact parameter, channel aliases, and the value \(10\) found no prior equality census. Residual risk is an obscure or unindexed enumeration.

## Value
PASS. Closing an explicit published finite gap at a canonical small parameter is mathematically motivated, and the full equality census plus the common four-word core gives structural information useful for testing constructions and bounds.

## Closest literature and limitations
The foundational 2010 model paper gives the channel and general bounds. The 2013 upper-bound paper treats precisely the same non-overlapping model and leaves \(10\le M(6,2)\le16\). The result here is finite and does not extend to overlapping grains or other values of \(n,t\).

Self-review: passed. Independent audit: not yet performed.

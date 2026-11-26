# The full elementary coefficient vector of the directed circular square on eight vertices

## Finding

Let \(C_{8,2}\) have vertex set \(\mathbb Z/8\mathbb Z\) and directed arcs \(i\to i+1\) and \(i\to i+2\) for every \(i\), with all indices cyclic. For a proper coloring \(\kappa\) of the underlying undirected graph, let \(\operatorname{asc}(\kappa)\) count arcs whose destination has the larger color. Define
\[
X(\mathbf x;t)=\sum_{\kappa} t^{\operatorname{asc}(\kappa)}\prod_{v} x_{\kappa(v)}.
\]
The full elementary expansion is \(X=\sum_{\lambda\vdash 8}c_\lambda(t)e_\lambda\), with the following coefficient lists (in order of increasing degree, starting at the displayed degree):

| \(\lambda\) | Start degree | Consecutive coefficients |
|---|---:|---|
| \((8)\) | 3 | \(8,64,224,456,616,672,616,456,224,64,8\) |
| \((7,1)\) | 5 | \(32,136,208,208,208,136,32\) |
| \((6,2)\) | 6 | \(24,64,64,64,24\) |
| \((5,3)\) | 6 | \(8,48,80,48,8\) |
| \((4,4)\) | 6 | \(4,40,80,40,4\) |

All unlisted coefficients are zero. The lists are nonnegative and unimodal and satisfy \(c_\lambda(t)=t^{16}c_\lambda(t^{-1})\).

## Proof and replay

Any stable set has at most two vertices: if it had three, all three cyclic gaps between successive members of the triple would be at least three, requiring at least nine vertices. The stable pairs are precisely the nonedges of the undirected circular square (cyclic distance three or four). Each proper coloring using exactly colors \(1,\ldots,k\) has an ordered partition into singleton and stable-pair blocks. Choose the least remaining vertex and either make it a singleton or match it to one stable partner still remaining. This enumerates each undirected color-class partition exactly once. Order the resulting blocks in all possible ways and count ascents on the 16 specified arcs. For each ordered size sequence this gives the exact coefficient polynomial for its monomial on \(x_1,\ldots,x_k\). Ordered colors with gaps give the same polynomials because only relative order affects ascents.

For a monomial with \(d\) squared colors and \(s=8-2d\) singleton colors, the coefficient of that monomial in \(e_{8-b}e_b\) is \(\binom{s}{b-d}\), zero outside the binomial's range. The doubled colors must appear in both factors, and one chooses \(b-d\) of the singleton colors for the second factor. Set \(e_0=1\) for \(b=0\). For \(d=4,3,2,1,0\) use the monomial with the doubled colors first to solve for \(c_{(8-d,d)}\) by backward substitution; the coefficient of this unknown is one at each step. The checker compares the result with the direct coloring counts for all 34 ordered exponent sequences on consecutive colors, not just the five used for substitution. Exponents of three or more cannot occur on either side. Thus the matching polynomials verify the full identity, including symmetry and all 17 zero elementary terms.

Run `python3 check_c82.py` with the Python 3 standard library. It examines 106 color-class partitions and 136488 ordered partitions, derives all five polynomials, and checks equality with the displayed lists, all monomial comparisons, and the shape assertions.

## Prior coverage and scope

This graph is Ellzey's \(\vec G^c_{8,3}\). Ellzey had already tested the circular-indifference conjecture (which includes e-positivity and e-unimodality) by computer for this graph as part of the remaining cases with \(n\le8\). The contribution here is the explicit individual coefficient polynomials and their short replay, not the first e-positivity test for this instance or for higher directed powers. The general row-sum identity does not separate \((7,1),(6,2),(5,3),(4,4)\), and specializing at \(t=1\) loses the ascent grading. The circular square on eight vertices is the first to have nonedges at two different cyclic distances (three and four) and the last before stable triples appear at order nine. Its full vector is thus a check for ascent-weighted formulas that must account for more than one kind of stable pair, while the color-class enumeration still reduces to matchings. The computation is for this graph, not an all-order e-positivity or unimodality theorem.

- B. Ellzey, *A directed graph generalization of chromatic quasisymmetric functions*, [arXiv:1709.00454](https://arxiv.org/abs/1709.00454), §6 (prior computer test, family definition and row sums).
- P. Alexandersson and G. Panova, *LLT polynomials, chromatic quasisymmetric functions and graphs with cycles*, [arXiv:1705.10353](https://arxiv.org/abs/1705.10353), circular unit-arc formulation and Proposition 28.

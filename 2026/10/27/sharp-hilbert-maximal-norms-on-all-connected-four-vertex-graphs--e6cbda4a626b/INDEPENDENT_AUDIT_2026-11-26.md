# Independent mathematical audit

## correctness

PASS

Because the maximal operator uses |f|, each choice of one of the distinct normalized ball rows per vertex gives a nonnegative linearization A and the squared output norm is the maximum of ||A|f|||² over those choices. Nonnegative top eigenvectors of AᵀA give equality in the optimization over input moduli, so the squared operator norm is the maximum top Gram eigenvalue. An independently written fraction-arithmetic replay rebuilt the balls via all-pairs distances and checked all 385 matrices. For the path, cycle, star, complete graph, diamond and paw, respectively, it checked 142,79,53,12,35,53 nonwinning Gram matrices by strict Sylvester minors; the 2,2,1,4,1,1 winners have the stated characteristic polynomials and exceed their rational barriers. Replay and exact output: branches/0e3353d6-7f1c-46d5-8713-0654f213edad/replay_record4.py and replay_record4_full.txt in the same directory; I inspected the code and output. The supplied verifier is separate and was not executed. In the path/paw form the rows are one high-coordinate singleton, two copies of its three-vertex average and one two-vertex average with the remaining coordinate; the cycle/diamond rows are two high singletons and averages on the highs plus each individual low. These forms give the claimed paired Gram spectra by permutations. Solving the low-coordinate equations gives a=1/(4Λ−1), c=2/(9Λ−4) and the stated three t values. Each winner has a connected Gram support and hence a unique positive Perron ray. Distinct winning row patterns for a graph have distinct high-coordinate sets; if a distinct averaging ball tied at an extremizer, the alternate choice would also have to be winning with the same Perron ray, which is impossible. This checks all extremizers, the listed distinct balls, and invariance under phase. The additional claim that the operator determines the graph follows because every ball row is exposed by a positive input peaked on the outer shell of that ball and lower outside; the resulting exposed row set identifies the smallest nonsingleton ball and thus the neighbors of each vertex.

## originality

PASS

Credit the exact star and complete constants, the known K_4 extremizer profile and star witness, and the directly overlapping indexed P_4 and C_4 determinations as component coverage. The distinct remaining statement is an all-six sharp Hilbert classification with the paw and diamond equality cases and the exact nonisomorphic Hilbert-norm coincidences. The four-vertex ℓ¹ precedent concerns a different optimization problem.

## value

PASS

Order four is the first connected order with six structural types, including both four-edge types and a complete-minus-edge graph. A natural Hilbert norm separates four levels but cannot distinguish two pairs of nonisomorphic operators. Knowing precisely which pairs coincide, why their winning matrices match, and which inputs exhaust equality gives information beyond an isolated norm computation or a table in another exponent.

The dated certificate retains the supplied scientific assessment, sources and limitations.

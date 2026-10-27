# Scientific review: exact producer-count distributions on rook networks

## Correctness

PASS. The actual best response to the parity of active **other** neighbors yields the necessary-and-sufficient matrix identity \(x_{ij}=1+r_i+c_j\) over \(\mathbb F_2\). Summation gives compatible parity-vector constraints; each parity case is exhaustively solved with an injective reconstruction of every equilibrium. Counting these vectors proves each polynomial coefficient, total, minimum, and its multiplicity, including the odd-odd corner argument. The uniform-selection expectation follows from marginal parity symmetry. An independent plain-Python checker evaluated \(314{,}512\) actual profiles and checked closed-neighborhood ranks on \(81\) rectangles. Finite checks were not used as an infinite proof.

## Originality

PASS for the exact full producer-count weight enumerator and all-dimension extremal multiplicity statement, with the cited prior-work limits. Gilboa–Nisan already place parity games in polynomial time through binary linear equations. Peters–Goldwasser–Young already establish the even-even invertible rook-product case (2017, Proposition 3.1), and Curtis–Earl–Livingston–Shader provide general Cartesian-product nullity methods. Batal gives the known odd-domination equivalent condition. These facts are not novel here. In the inspected original papers none supplies the four-case coefficients \([z^j]P_{m,n}(z)\) that distinguish how many producers each equilibrium has. Generic rank/nullity results provide totals, not their Hamming-weight distribution. The standard *ordinary* domination polynomial of the rook graph is a different invariant. The 2001 odd-domination article was not inspected in complete primary full text, so the chance of an equivalent indexed or unindexed enumerator remains a residual risk. Published-record semantic searches found no direct covering claim; absence from such searches is not a uniqueness proof.

## Mathematical value

PASS. The activity distribution, not just one feasible equilibrium or the rank, is a natural statistic of strategic public-goods provision. The polynomial simultaneously determines exact equilibrium multiplicity at every attainable production level, the sparsest-production welfare boundary and its count, and uniform equilibrium-selection expected production. The sharp parity-regime discontinuities persist for arbitrarily large complete-row/complete-column networks. The objective is a complete classification of a motivated natural network family, rather than an arbitrary finite subcase.

## Scope and remaining risks

The alternating strict parity response is a deliberately specific game. No dynamical convergence or general economic efficiency is asserted. The proof is self-contained but independent expert validation has not occurred. Nonindexed parity-domination and coding-theory enumerators are a remaining bibliographic risk, and a direct equivalent formula there would supersede any originality assessment.

Self-review: passed. Independent audit: not yet performed.

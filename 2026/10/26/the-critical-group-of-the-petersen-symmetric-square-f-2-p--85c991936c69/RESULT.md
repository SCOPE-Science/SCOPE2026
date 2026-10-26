# The critical group of the Petersen symmetric square \(F_2(P)\)

## Finding
Let \(P=KG(5,2)\) be the Petersen graph and \(T=F_2(P)\) its graph of two indistinguishable, noncolliding tokens. The critical group of \(T\) is
\[
K(T)\cong (\mathbb Z/2\mathbb Z)^8\oplus(\mathbb Z/4\mathbb Z)^2
\oplus\mathbb Z/28\mathbb Z\oplus\mathbb Z/1596\mathbb Z
\oplus\mathbb Z/38304\mathbb Z\oplus(\mathbb Z/191520\mathbb Z)^3.
\]
The number of spanning trees of \(T\), which also counts its recurrent chip-firing states relative to any fixed sink, is exactly
\[
\tau(T)=49,253,533,675,382,566,432,014,336,000.
\]
The Laplacian characteristic polynomial is
\[
\chi_{L(T)}(x)=x(x-7)^6(x-6)^6(x-5)^4(x-3)^5(x-2)^5
(x^2-13x+32)^4(x^2-13x+38)^5.
\]
The critical group statement, rather than the eigenvalue list alone, is the principal new claim.

## Assumptions and scope
All graphs are finite, simple and unweighted. The ten vertices of \(P\) are the two-subsets of \(\{0,1,2,3,4\}\), with edges joining disjoint subsets. Vertices of \(T\) are the \(\binom{10}{2}=45\) unordered pairs \(\{u,v\}\) of distinct vertices of \(P\). The configurations \(\{u,v\}\) and \(\{u,w\}\) are adjacent in \(T\) precisely when \(vw\) is an edge of \(P\) and \(u\notin\{v,w\}\). These adjacency conditions completely define \(T\); no other collisions or moves are permitted.

Write \(L=D-A\) for the combinatorial Laplacian of \(T\). Its connectedness is checked by exhaustive breadth-first search in the standalone verifier. The critical group \(K(T)\) is the finite cokernel of any reduced Laplacian obtained by deleting one row and the corresponding column of \(L\). Its invariant-factor description is independent of the deleted vertex.

## Proof
**1. State graph and reduced matrix.** Enumerate the ten Kneser vertices lexicographically, and then enumerate their 45 distinct unordered pairs lexicographically. Two configurations are joined when their symmetric difference is one Petersen edge. There are 15 configurations occupying the endpoints of an edge of \(P\), each with degree four in \(T\); the other 30 configurations have degree six. Hence the hand-checkable degree count gives
\[
|E(T)|=(15\cdot4+30\cdot6)/2=120.
\]
The adjacency construction and breadth-first search in `verify.py` check all 45 vertices and all 120 edges. Form the integer matrix \(M\) by deleting the last row and column of the resulting \(45\times45\) Laplacian. It is \(44\times44\) and nonsingular.

**2. The integer determinant and spectrum.** Fraction-free Bareiss elimination gives
\[
\det(M)=2^{36}3^9 5^3 7^6 19^5
=49,253,533,675,382,566,432,014,336,000.
\]
Independently, the verifier calculates the exact 45-degree characteristic polynomial of \(L\) using Newton identities applied to \(\operatorname{tr}(L^j)\) for all integers \(1\le j\le45\). Its coefficients equal exactly the polynomial displayed above. In particular, the coefficient of \(x\) is \(45\det(M)\), as required by the matrix-tree theorem; this supplies a separate integer identity for the determinant and spanning-tree count.

**3. Prime-primary Smith factors.** Only the five primes dividing \(\det M\) can occur. For a prime \(p\) with \(e=v_p(\det M)\), work over the finite ring \(\mathbb Z/p^{e+1}\mathbb Z\). In each remaining submatrix choose an entry of smallest \(p\)-adic valuation \(a\), move it to the top-left position by row and column permutations, and apply elementary row and column additions to clear its column and row. This is legitimate because every remaining entry is divisible by \(p^a\), while the unit part of the pivot is invertible modulo \(p^{e+1-a}\). The operations are reductions of invertible integer elementary operations. The diagonal valuations obtained, in ascending order, are therefore exactly the local Smith valuations below; no unseen valuation can exceed \(e\), since their sum is already \(e\).

| Prime \(p\) | Valuation \(0\) | Valuation \(1\) | Valuation \(2\) | Valuation \(5\) |
|---|---:|---:|---:|---:|
| \(2\) | 28 | 8 | 4 | 4 |
| \(3\) | 39 | 1 | 4 | 0 |
| \(5\) | 41 | 3 | 0 | 0 |
| \(7\) | 38 | 6 | 0 | 0 |
| \(19\) | 39 | 5 | 0 | 0 |

All local lists have length 44. The code asserts that the sum of the valuations for each prime agrees with the corresponding exponent in the determinant. Aligning these ascending local lists positionwise gives 28 unit invariant factors followed, in divisibility order, by
\[
\underbrace{2,\ldots,2}_{8},\quad4,4,28,1596,38304,191520,191520,191520.
\]
The factors form a divisor chain, and their product equals \(\det M\). Since elementary integer row and column operations preserve cokernels, this proves the displayed decomposition of \(K(T)\).

## Verification
Run `python3 verify.py` using Python 3 and its standard library; no data downloads or third-party packages are needed. The program reconstructs \(P\) and \(T\) from their set-theoretic definitions, asserts the degree and connectivity counts, computes the reduced determinant by exact Bareiss elimination, computes the characteristic polynomial by exact Newton identities and matrix powers, and independently computes local Smith valuations modulo the necessary prime powers. Every entry and pivot is checked in exact integer arithmetic. On success it prints `VERIFY_OK` and the nonunit invariant factors. The exact computation is over all 44 rows and columns, rather than an empirical sample.

## Relationship to prior work
Audenaert, Godsil, Royle and Rudolph introduced the symmetric-square construction and studied adjacency-spectral invariants and strongly regular graphs. Fabila-Monroy and collaborators developed the token-graph interpretation, including connectivity and reconfiguration parameters. Ducey, Gerhard and Watson computed critical groups for rook graphs and their complements; Ducey, Hill and Sin treated the base Kneser graph \(KG(n,2)\) itself. Dalfó and collaborators established important general Laplacian-spectral relationships for token graphs. These results motivate and inform the construction, but none of the inspected relevant statements specifies the integral Smith factors for \(F_2(KG(5,2))\). The critical group of the ten-vertex base graph is not the critical group of its 45-vertex symmetric square; neither the eigenvalues nor the spanning-tree count alone determine the Smith invariant-factor decomposition.

## Limitations
The theorem classifies one natural finite token graph and does not prove an all-graph or all-Kneser-family formula. The factorization is exact by the included finite computation; a conceptual representation-theoretic derivation of each prime-primary summand remains desirable. The comparison with published literature cannot rule out unpublished or unindexed earlier computations.

## References
- K. Audenaert, C. Godsil, G. Royle and T. Rudolph, *Symmetric Squares of Graphs*, arXiv:math/0507251, first posted 12 July 2005, https://arxiv.org/abs/math/0507251.
- R. Fabila-Monroy, D. Flores-Peñaloza, C. Huemer, F. Hurtado, J. Urrutia and D. R. Wood, *Token Graphs*, arXiv:0910.4774, first posted 25 October 2009, https://arxiv.org/abs/0910.4774.
- J. Ducey, J. Gerhard and N. Watson, *The Smith and Critical Groups of the Square Rook's Graph and its Complement*, arXiv:1507.06583, first posted 23 July 2015, https://arxiv.org/abs/1507.06583.
- J. Ducey, I. Hill and P. Sin, *The Critical Group of the Kneser Graph on 2-Subsets of an n-Element Set*, arXiv:1707.09115, first posted 28 July 2017, https://arxiv.org/abs/1707.09115.
- C. Dalfó et al., *On the Laplacian Spectra of Token Graphs*, arXiv:2012.00808, first posted 1 December 2020, https://arxiv.org/abs/2012.00808.

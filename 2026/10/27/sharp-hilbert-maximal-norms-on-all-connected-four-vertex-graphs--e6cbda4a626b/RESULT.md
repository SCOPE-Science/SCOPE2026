# Sharp Hilbert maximal norms on all connected four-vertex graphs

## Finding

Let \(G\) be any connected simple graph on exactly four vertices, with graph distance, counting measure and its centered graph-ball maximal operator
\[
(M_G f)(v)=\max_{r\in\{0,1,2,3\}}\frac{1}{|B_G(v,r)|}\sum_{w\in B_G(v,r)}|f(w)|.
\]
The exact sharp strong Hilbert norm \(\|M_G\|_{\ell^2\to\ell^2}\) takes precisely four values on the six isomorphism classes:

| Graph | Squared sharp norm \(\|M_G\|_{2\to2}^2\) | Numerical norm |
| --- | --- | --- |
| Star \(K_{1,3}\) | \(1+\sqrt{3}/2\) | \(1.366025403784\ldots\) |
| Path \(P_4\) and paw (triangle with one pendant edge) | \(\Lambda\), largest root of \(36z^3-78z^2+35z-4=0\) | \(1.266333300269\ldots\) |
| Cycle \(C_4\) and diamond \(K_4\setminus e\) | \((7+2\sqrt{10})/9\) | \(1.216760513291\ldots\) |
| Complete graph \(K_4\) | \((7+\sqrt{13})/8\) | \(1.151387818866\ldots\) |

Here \(\Lambda=1.603600027370\ldots\) is uniquely determined by \(\Lambda>79/50\). Thus two pairs of **nonisomorphic** graphs have exactly the same sharp Hilbert maximal norm, even though the centered maximal operators themselves determine the underlying graph.

Every nonzero norm-attaining input is characterized, up to graph automorphism, positive scaling and arbitrary coordinatewise real signs or complex phases, by its coordinatewise modulus as follows. Put
\[
 a=\frac{1}{4\Lambda-1},\qquad c=\frac{2}{9\Lambda-4},\qquad
 t_C=\frac{2}{9\Lambda_C-1},\quad
 t_S=\frac{1}{4\Lambda_S-1},\quad
 t_K=\frac{3}{16\Lambda_K-9},
\]
where \(\Lambda_C=(7+2\sqrt{10})/9\), \(\Lambda_S=1+\sqrt{3}/2\), and \(\Lambda_K=(7+\sqrt{13})/8\). All parameters above are strictly between zero and one. The respective modulus patterns are:

| Graph and vertex order | Modulus pattern |
| --- | --- |
| Path \(1-2-3-4\) | \((a,1,c,c)\) or its reversal |
| Paw: hub \(0\), triangle neighbors \(1,2\), pendant \(3\) | \((1,c,c,a)\) |
| Cycle \(0-1-2-3-0\) | \((1,t_C,1,t_C)\), with opposite high vertices |
| Diamond: universal vertices \(0,1\), nonadjacent vertices \(2,3\) | \((1,1,t_C,t_C)\) |
| Star: center \(0\) | \((1,t_S,t_S,t_S)\) |
| Complete graph: distinguished vertex \(0\) | \((1,t_K,t_K,t_K)\) |

At every such extremizer, each optimal **distinct averaging ball** is uniquely determined by its vertex. With the vertex orders just given, the minimum integer radii realizing the optimal balls are \((1,0,1,2)\) for the path, \((0,1,1,1)\) for the paw, \((0,1,0,1)\) for the cycle, \((0,0,1,1)\) for the diamond, \((0,1,1,1)\) for the star and \((0,1,1,1)\) for the complete graph. Graph automorphisms transport these patterns. Radii larger than the graph diameter may represent the same ball; such redundant radii are not considered distinct.

## Assumptions and scope

All graphs are finite, undirected, unweighted, simple and connected, with four vertices. Distances are shortest-path edge counts. Norms use counting measure on vertices (equivalently uniform probability, since domain and codomain have the same number of vertices). The operator acts on real or complex functions and takes absolute values before averaging. The paw has edges \(01,02,12,03\); the diamond has all edges on \(\{0,1,2,3\}\) except \(23\). In the path, vertices are ordered \(1,2,3,4\); other graphs use \(0,1,2,3\).

## Proof

**1. Exact finite linearization.** Given any input \(f\), replace it by \(|f|\) without affecting either the output or its input norm. At each vertex \(v\) there is a finite set of distinct normalized graph-ball averaging rows \(a_{v,r}\). Selecting one row independently at each vertex produces a nonnegative stochastic matrix \(A\). Pointwise maximization and nonnegativity give the identity
\[
 \|M_G f\|_2^2=\max_A\|A|f|\|_2^2.
\]
The two finite maxima and the supremum over nonnegative inputs commute. Because \(A^\mathsf{T}A\) is nonnegative symmetric, one of its top eigenvectors may be chosen nonnegative. Therefore
\[
 \|M_G\|_{2\to2}^2=\max_A\lambda_{\max}(A^\mathsf{T}A).
\]
This argument is valid whether or not some individual averaging radii tie.

**2. Exhaustive rational comparison.** Every connected four-vertex simple graph is one of the six classes listed: two trees (path and star), two four-edge graphs (cycle and paw), the five-edge diamond or the complete graph. Number the distinct ball-average rows by increasing radius, starting with index zero. The possible row counts, numbers of selection matrices, rational separation barriers and all winning row-index patterns are:

| Graph | Row-option counts | Selections | Barrier \(q_G\) | Winning patterns |
| --- | --- | ---: | --- | --- |
| Path | \((4,3,3,4)\) | 144 | \(79/50\) | \((1,0,1,2)\), \((2,1,0,1)\) |
| Cycle | \((3,3,3,3)\) | 81 | \(29/20\) | \((0,1,0,1)\), \((1,0,1,0)\) |
| Star | \((2,3,3,3)\) | 54 | \(7/4\) | \((0,1,1,1)\) |
| Complete | \((2,2,2,2)\) | 16 | \(33/25\) | all four permutations of \((0,1,1,1)\) |
| Diamond | \((2,2,3,3)\) | 36 | \(29/20\) | \((0,0,1,1)\) |
| Paw | \((2,3,3,3)\) | 54 | \(79/50\) | \((0,1,1,1)\) |

For each of the 374 nonwinning matrices, all four leading principal minors of \(q_G I-A^\mathsf{T}A\) are strictly positive. This is an **exact rational finite assertion** proven by the complete enumerator in `verify.py`, which reconstructs every graph distance and normalized row directly from the edge list, evaluates the minors via the permutation formula and checks all cases with integer-rational arithmetic. Sylvester's criterion therefore proves that all 374 nonwinning squared singular values lie strictly below their listed barriers. The remaining 11 matrices are exactly the listed winning patterns. None is inferred from a numerical optimization: the code checks exact characteristic coefficients and the negative final determinant at its corresponding barrier. The minimum of each leading-minor column over all nonwinners in each graph is separately printed by the program, giving an additional reproducible certificate of strictness.

**3. Winning characteristic polynomials and algebraic norms.** For the listed winning averaging matrices, direct multiplication yields the following complete characteristic polynomials \(\det(zI-A^\mathsf{T}A)\):
\[
\begin{array}{ll}
\text{path/paw}:&z(36z^3-78z^2+35z-4)/36,\\
\text{cycle/diamond}:&(z-1)(9z-1)(9z^2-14z+1)/81,\\
\text{star}:&(4z-1)^2(4z^2-8z+1)/64,\\
\text{complete}:&z^2(16z^2-28z+9)/16.
\end{array}
\]
Moreover, the two paired coincidences are structural: after independent permutations of input columns and output rows, the winning path and paw matrices become identical (one singleton row, one two-vertex average, and two copies of a three-vertex average), and the winning cycle and diamond matrices become identical (two singleton rows and two distinct three-vertex averages). Thus each paired group has the same **entire singular-value multiset** of winning matrices, not merely the same largest singular value. The largest root in each case is strictly above the relevant rational barrier, whereas every other row selection has spectral radius below it. For the cubic, its derivative is \((6z-7)(18z-5)\), strictly positive above \(79/50\); the cubic has negative value \(-44499/31250\) there and positive value at \(z=2\). Thus \(\Lambda\) is uniquely the root above the barrier. The quadratic radicals follow immediately.

**4. Equality cases.** The matrices \(A^\mathsf{T}A\) for the winners have connected positive-entry support and thus simple Perron eigenvalues and a unique strictly positive top eigenvector ray. For path/paw, substitution of \(a=1/(4\Lambda-1)\) and \(c=2/(9\Lambda-4)\) into the eigenvector equation reduces its remaining coordinate to \(36\Lambda^3-78\Lambda^2+35\Lambda-4=0\). For cycle/diamond the remaining eigenvector condition is \(9\Lambda_C^2-14\Lambda_C+1=0\); for star it is \(4\Lambda_S^2-8\Lambda_S+1=0\); for complete it is \(16\Lambda_K^2-28\Lambda_K+9=0\). These give exactly the patterns stated above. For path/paw, \(0<a,c<1/4\) follows from \(\Lambda>79/50\); comparing each listed ball average with every other radius is then strict. In the remaining graphs the comparisons among distinct balls are strict because \(0<t_S,t_C,t_K<1\). Hence each Perron vector truly activates the listed radius pattern, not merely a formal linearization. Every maximizing input selects a winning matrix and must lie on its Perron ray. Independent coordinate phases or signs do not change \(M_G f\).

## Verification

Run `python3 verify.py` with Python 3's standard library only. It reconstructs all 385 averaging selections from the six graph edge lists, checks strict Sylvester minors for 374 nonwinners, identifies all 11 winners and confirms six exact characteristic polynomials. Its check uses `fractions.Fraction` and the Leibniz determinant formula, not floating point or an eigensolver. The analytical finite-maximization and Perron arguments above supply the universal quantifiers over all real or complex inputs; the program certifies the explicitly finite enumeration.

## Relationship to prior work

Soria and Tradacete, *Best constants for the Hardy-Littlewood maximal operator on finite graphs* (arXiv:1410.6204v1, first posted 2014-10-22), introduce the graph-ball framework and compute the \(\ell^1\) norms of the six connected four-vertex graphs in their Example 2.6; they call the four-vertex **path** \(L_4\). The present \(\ell^2\) constants and the above full Hilbert extremizer classification are different statements and do not follow from their \(\ell^1\) values. González-Riquelme and Madrid, *Sharp Inequalities for maximal operators on finite graphs* (arXiv:2005.03146, first posted 2020-05-06), and *Sharp inequalities for maximal operators on finite graphs, II* (arXiv:2011.02630, first posted 2020-11-05), establish related \(\ell^2\) norms for complete and star graphs, which are therefore **not** independently claimed as new. The new parts are the sharp values and all extremizers for path, paw, cycle and diamond, and their complete four-vertex classification and nonisomorphic norm coincidences.

## Limitations

This result classifies exactly four-vertex unweighted connected graphs, not larger or weighted graphs. It is a finite exact classification, not a general-purpose formula for arbitrary graph order. The finite rational certificate can be inspected or rerun; its proof scope is exactly the finite table of ball-selection matrices. Bibliographic searches and inspection of closest available primary sources did not locate prior coverage of the full classification; unindexed or differently titled literature could exist. No conclusions are asserted for exponents other than \(2\).

## References

1. J. Soria and P. Tradacete, *Best constants for the Hardy-Littlewood maximal operator on finite graphs*, arXiv:1410.6204v1 (2014-10-22), especially Example 2.6, Section 3 and Proposition 3.3. https://arxiv.org/html/1410.6204v1
2. C. González-Riquelme and J. Madrid, *Sharp Inequalities for maximal operators on finite graphs*, arXiv:2005.03146 (2020-05-06), especially Section 3. https://arxiv.org/html/2005.03146v3
3. C. González-Riquelme and J. Madrid, *Sharp inequalities for maximal operators on finite graphs, II*, arXiv:2011.02630 (2020-11-05), especially the introduction and complete/star graph theorems. https://arxiv.org/abs/2011.02630

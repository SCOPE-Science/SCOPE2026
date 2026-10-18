# Odd-independent-set polynomial of circular ladders

## Finding

For every integer \(n\ge3\), let \(P_n=C_n\square K_2\) be the \(n\)-rung circular ladder (prism). Let \(L_n(z)=\sum_{S}z^{|S|}\), where the sum is over all odd independent sets, including the empty set. The exact coefficient \(a_{n,k}=[z^k]L_n(z)\) is as follows:

\[
 a_{n,0}=1,\qquad
 a_{n,k}=\frac{n}{k}\sum_{r=1}^{\min(k,n-2k)}
   2^r\binom{k}{r}\binom{n-2k-1}{r-1}
 \quad (1\le k<n/2).
\]

For even \(n\), the remaining potentially nonzero coefficients are
\[
 a_{n,n/2}=\begin{cases}4,&4\mid n,\\0,&n\equiv2\pmod4,\end{cases}
 \qquad a_{n,n}=2.
\]
All other coefficients vanish. Thus
\[
 \alpha_{\mathrm{od}}(P_n)=
 \begin{cases}n,&n\text{ even},\\ (n-1)/2,&n\text{ odd},\end{cases}
\]
and for every odd \(n\), exactly \(2n\) odd independent sets have the maximum size. For even \(n\) there are exactly two maximum sets of size \(n\); in addition, when \(4\mid n\), there are exactly four sets of size \(n/2\), while when \(n\equiv2\pmod4\), there are no sets of size \(n/2\).

The positive-size support is \(\{1,\ldots,(n-1)/2\}\) for odd \(n\), \(\{1,\ldots,n/2,n\}\) for \(4\mid n\), and \(\{1,\ldots,n/2-1,n\}\) for \(n\equiv2\pmod4\). The odd-independence density consequently changes from exactly \(1/2\) for even \(n\) to \((n-1)/(4n)\) for odd \(n\). These are density values relative to all \(2n\) vertices, not asymptotic limits.

For instance,
\[
 L_5(z)=1+10z+10z^2,\qquad
 L_6(z)=1+12z+24z^2+2z^6.
\]

## Assumptions and scope

The graph is finite, simple, undirected and indexed: its vertices are \((i,b)\) for \(i\in\mathbb Z/n\mathbb Z\) and \(b\in\{0,1\}\); edges join \((i,b)\) to \((i\pm1,b)\) and to \((i,1-b)\). An *odd independent set* \(S\) is independent and satisfies \(|N(v)\cap S|\in\{0,1,3,5,\ldots\}\) for each vertex \(v\notin S\). In this cubic graph the allowable counts are \(0,1,3\). The coefficient count uses labelled graph vertices; it does not quotient by rotations, reflections or layer swaps. Binomial coefficients in the formula have nonnegative integer arguments throughout the stated range.

## Proof

Every rung contains at most one selected vertex. Encode a set by the cyclic word \((s_0,\ldots,s_{n-1})\) over \(\{0,+,-\}\), with zero meaning an empty rung and either sign recording which vertex of the rung is selected.

First suppose rung \(i\) has sign \(+\). By independence, neither of its adjacent rungs can also carry \(+\). The unselected \(-\)-vertex in rung \(i\) sees the selected \(+\)-vertex in its rung plus one selected neighbour for each adjacent rung signed \(-\). Its selected-neighbour count is therefore \(1+t\), with \(t\in\{0,1,2\}\). Odd independence forces \(t=0\) or \(t=2\). The same argument holds after interchanging the signs. Consequently a selected rung has either two adjacent empty rungs or two adjacent selected rungs of the opposite sign. If *any* pair of consecutive rungs is selected, this rule propagates in both directions: all rungs must be selected, their signs must alternate, and \(n\) must be even. Conversely, the two alternating full-rung words for even \(n\) are valid odd independent sets of cardinality \(n\).

All other nonempty valid sets therefore have no consecutive selected rungs. At a selected rung, the selected vertex has no selected neighbour and the other vertex has exactly one. At an empty rung, each vertex has selected neighbours only in the two adjacent rungs. The odd condition fails precisely when *both* neighbouring rungs are selected with the *same* sign. Hence the exact characterization in the non-full case is: selected rungs are nonadjacent, and any two selected rungs separated by exactly one empty rung have opposite signs. No other restriction is needed. This proves the claimed structural classification without finite enumeration.

Fix \(k\ge1\) selected rungs in this non-full case and list them in cyclic order. Let \(g_j\) denote the number of empty rungs between consecutive selected rungs. Each \(g_j\ge1\) and \(\sum_jg_j=n-k\). Put \(L=n-2k\). When \(L>0\), at least one gap is long (\(g_j\ge2\)). Suppose exactly \(r\) gaps are long. Choosing the long-gap positions gives \(\binom{k}{r}\) possibilities, and distributing the \(L\) extra empty rungs among those \(r\) gaps, each receiving at least one, gives \(\binom{L-1}{r-1}\) compositions. Every unit gap \(g_j=1\) imposes opposite signs on its endpoints; a long gap imposes none. Because at least one gap is long, this sign-constraint graph is the disjoint union of exactly \(r\) paths, including isolated vertices as paths, so there are exactly \(2^r\) admissible signings.

Choose an indexed starting selected rung in \(n\) ways and the cyclic gap vector beginning there. Each final selected-rung set with signs is counted exactly \(k\) times, once for each possible starting selected rung. Dividing by \(k\) proves
\[
 a_{n,k}=\frac nk\sum_{r=1}^{\min(k,L)}
 \binom{k}{r}\binom{L-1}{r-1}2^r
 \qquad (1\le k<n/2).
\]
This combinatorial derivation also proves integrality of the displayed rational-looking expression.

If \(L=0\), then \(n=2k\) and every gap is a unit gap. The selected rungs are exactly one of the two parity classes of the cycle. Their signs must alternate around a length-\(k\) cycle, which allows two signings exactly when \(k\) is even and none when \(k\) is odd. Thus \(a_{n,n/2}=4\) if \(4\mid n\) and is zero otherwise. The previously classified full-rung words contribute \(2z^n\) for even \(n\). Including the empty set proves all coefficients and their vanishing statements.

For odd \(n\), full-rung words are impossible, and for each \(1\le k\le(n-1)/2\) the formula has a positive term with \(r=1\). At \(k=(n-1)/2\), \(L=1\), so the coefficient is \(2n\). For even \(n\), full-rung words give the maximum size \(n\), and no independent set can exceed one vertex per rung. The support and density conclusions follow. In particular, the even-order maximum number was already available as a consequence of the previously known fact for odd-regular bipartite graphs; the new statement is the full coefficient classification including the odd-order case.

## Verification

Run `python3 verify_prism_odd_independence.py` in the directory containing the two files. The standard-library program implements three separate specifications: a direct graph-neighbourhood test of all ternary rung words; the closed formula above; and an independently defined nine-state transfer enumeration implementing the local parity constraints. The direct test examines all \(\sum_{n=3}^{11}3^n=265707\) words for \(3\le n\le11\). The transfer and closed-form coefficient arrays agree for every \(3\le n\le100\). The program also checks extremal and parity statements. These bounded checks are corroboration, not proof for unbounded \(n\).

## Relationship to prior work

Caro, Petruševski, Škrekovski and Tuza introduced systematic study of odd independence and established the inequality between odd independence and strong odd colouring, including the equality \(\alpha_{\mathrm{od}}(G)=\alpha(G^2)\) for claw-free graphs [1]. For even \(n\), the circular ladder is bipartite and cubic, so their observation about odd-regular bipartite graphs already yields \(\alpha_{\mathrm{od}}(P_n)=n\). For odd \(n\ge5\), the circular ladder is not claw-free, and those statements do not determine the exact odd-independence number; neither statement enumerates the set sizes.

Their sequel studies products of paths and cycles, including square cylindrical and toroidal grids, and asks for further exact values on grid products [2, Section 6, Problem 27]. It gives a general Cartesian-product lower bound [2, Proposition 6], but no width-two circular-ladder coefficient formula. The present theorem treats the natural first fixed-width cylindrical family and determines the entire enumerator, not only its maximum. Other graph invariants of prism and ladder graphs, including ordinary independence or topological invariants of independence complexes, are not equivalent to this locally parity-constrained enumeration.

## Limitations

The theorem covers the width-two circular ladder only; it does not solve general rectangular, toroidal, or higher-dimensional grid-product questions. It is a direct finite-graph count, not a classification up to automorphisms. The literature comparison is not a proof of global novelty: equivalent transfer formulas in unindexed sources remain possible. No independent external mathematical audit has been performed.

## References

[1] Y. Caro, M. Petruševski, R. Škrekovski, Z. Tuza, *The odd independence number of graphs, I: Foundations and classical classes*, arXiv:2509.20763, first public version 2025-09-25, https://arxiv.org/abs/2509.20763.

[2] Y. Caro, M. Petruševski, R. Škrekovski, Z. Tuza, *The odd independence number of graphs, II: Finite and infinite grids and chessboard graphs*, arXiv:2510.01897, first public version 2025-10-02, https://arxiv.org/abs/2510.01897.

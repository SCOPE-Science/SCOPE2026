# Exact order-four universal-cycle enumeration under tandem-square avoidance

## Finding

Let \(\Sigma\) be a fixed labeled alphabet of size \(q\ge 2\), and let \(\mathcal L_m\) be the set of length-\(m\) words containing no contiguous factor \(abab\), where \(a,b\in\Sigma\) may be equal. A cyclic universal word for \(\mathcal L_m\) is a circular word in which every element of \(\mathcal L_m\) occurs as a cyclic length-\(m\) factor exactly once and no other factor occurs. Cyclic rotations, but not reflections or alphabet permutations, are identified.

**Theorem.** Universal cycles exist for every \(m\le 4\), but for no \(m\ge5\). At order four they have length \(q^4-q^2\); their exact number, for every \(q\ge2\), is

\[
\boxed{U_q=q^{q^3-q^2+q-4}(q-1)^{2(q-1)}
(q^2-2q+2)^{(q-1)(q-2)/2}
((q-2)!)^{q^2}((q-1)!)^{q^3-q^2}.}
\]

In particular, \(U_2=4\) and \(U_3=2{,}708{,}265{,}511{,}157{,}760\). The formula counts individual symbol-labeled universal cycles modulo rotation only; each cycle is primitive because its cyclic four-factors are distinct.

## Assumptions and scope

All words use a finite labeled alphabet of cardinality \(q\ge2\), with unrestricted repetitions except for the explicitly forbidden four-factors. A *tandem square of span two* means any factor \(abab\); importantly, the case \(a=b\), which gives \(aaaa\), is forbidden too. The constraint does **not** forbid general squares of other spans, nor does it require adjacent letters to be distinct. Orders \(m\ge1\) are integers. For \(m=1,2,3\), no word is excluded and ordinary de Bruijn cycles exist. The nontrivial count concerns exactly the fourth order.

## Proof

**1. The fourth-order graph.** Build the directed overlap graph on all \(q^3\) triples \((a,b,c)\), with an edge labeled \(abcd\) from \((a,b,c)\) to \((b,c,d)\), precisely when \(abcd\ne abab\). The forbidden condition is equivalent to \(a=c\) and \(b=d\). There are \(q^2\) forbidden labels, so the graph has \(q^4-q^2\) distinct labeled edges. Both its in- and outdegree at a vertex \((a,b,c)\) are \(q-1\) when \(a=c\), and \(q\) otherwise. Thus it is balanced. A fourth-order universal cycle is exactly an Euler circuit, modulo cyclic choice of its first edge.

Write \(N=q^3\). Let \(A\) be the adjacency matrix of the complete order-three de Bruijn graph and \(J\) the all-ones \(N\)-square matrix. Every three-step walk in the full graph has exactly one realization between each ordered pair of triples, hence \(A^3=J\). Also \(A\mathbf1=q\mathbf1\) and \(\mathbf1^{\mathsf T}A=q\mathbf1^{\mathsf T}\). The full out-Laplacian is \(L_0=qI-A\), whose restriction to the zero-sum subspace has determinant \(q^{N-1}\). The directed matrix-tree theorem therefore gives its common rooted in-arborescence count

\[
t_0=\frac{q^{N-1}}{N}=q^{q^3-4}.
\]

**2. The low-rank deletion.** The \(q\) excluded constant edges \(aaaa\) are loops, so their deletion does not alter a Laplacian. The remaining excluded edges form one two-cycle for every unordered pair \(\{a,b\}\) of distinct alphabet symbols: the two triples \(aba\) and \(bab\) point to each other. Orient each alphabet pair once, and form the \(N\)-by-\(\binom q2\) matrix \(D\) whose column is \(e_{aba}-e_{bab}\). Removal of both directed edges changes the Laplacian by the negative of the corresponding undirected two-vertex Laplacian, giving exactly

\[
L=L_0-DD^{\mathsf T}.
\]

Let \(P=J/N\). On the zero-sum subspace \(L_0\) has inverse

\[
G=\frac1q\left(I+\frac Aq+\frac{A^2}{q^2}-3P\right).
\]

Indeed, direct multiplication using \(A^3=J\) yields \(L_0G=GL_0=I-P\). Let \(B\) be the ordinary oriented vertex-edge incidence matrix of the complete graph \(K_q\), with column \(e_a-e_b\) for each chosen alphabet pair. The shift structure gives the exact identities

\[
D^{\mathsf T}D=2I,\qquad D^{\mathsf T}AD=-2I,\qquad D^{\mathsf T}A^2D=B^{\mathsf T}B,
\]

and \(D^{\mathsf T}PD=0\). To verify the third identity, a two-step path from the triple \(aba\) to \(cdc\) in the full de Bruijn graph exists exactly when \(a=c\), so expanding the signed columns reproduces inner products of the alphabet incidence vectors. Consequently,

\[
D^{\mathsf T}GD=\left(\frac2q-\frac2{q^2}\right)I+\frac1{q^3}B^{\mathsf T}B.
\]

Since \(BB^{\mathsf T}=qI-J_q\), the eigenvalues of \(B^{\mathsf T}B\) are \(q\) with multiplicity \(q-1\), and zero with multiplicity \((q-1)(q-2)/2\). Applying the matrix determinant lemma on the zero-sum subspace,

\[
\begin{aligned}
\frac{t_q}{t_0}&=\det\!\left(I-D^{\mathsf T}GD\right)\\
&=\left(\frac{(q-1)^2}{q^2}\right)^{q-1}
\left(\frac{q^2-2q+2}{q^2}\right)^{(q-1)(q-2)/2}.
\end{aligned}
\]

Thus the rooted arborescence count is the strictly positive integer

\[
\boxed{t_q=q^{q^3-q^2+q-4}(q-1)^{2(q-1)}
(q^2-2q+2)^{(q-1)(q-2)/2}.}
\]

Positivity supplies a spanning in-arborescence. A balanced digraph possessing such an arborescence and with positive degree at every vertex is strongly connected: its condensation is acyclic and balanced, so has only one component. Hence an Euler circuit exists.

**3. Counting the circuits.** By the directed BEST theorem, the number of Euler circuits modulo rotating their **distinct labeled edges** is \(t_q\prod_v(\deg^+(v)-1)!\). Exactly \(q^2\) triple-vertices have their first and third letters equal, each with degree \(q-1\), and the other \(q^3-q^2\) vertices have degree \(q\). Therefore

\[
\prod_v(\deg^+(v)-1)!=((q-2)!)^{q^2}((q-1)!)^{q^3-q^2}.
\]

Multiplying by \(t_q\) gives the displayed formula for \(U_q\). Each allowed four-letter word labels exactly one edge, and is encountered once, so edge-circuits modulo rotation are in bijection with the required cyclic words; no additional division by their length or by the alphabet size is appropriate.

**4. Sharp obstruction for every higher order.** For \(m\ge5\), form the corresponding overlap graph on allowed \((m-1)\)-letter words, whose edges are the allowed \(m\)-letter words. At a valid vertex \(v\), the indegree is \(q-1\) if its **first** three letters form a palindrome \(aba\), otherwise \(q\). Its outdegree is \(q-1\) if its **last** three letters form \(aba\), otherwise \(q\). This follows because adding a letter to a valid word can introduce only one new length-four factor, at the corresponding end.

For every vertex length \(\ell=m-1\ge4\), take the first \(\ell\) letters of the infinite binary word

\[
0100\,1100\,1100\,1100\cdots.
\]

Every length-four factor is one of \(0100\), \(1001\), \(0011\), \(0110\), \(1100\), none a tandem square. The initial three letters are \(010\), but every terminal triple of a prefix of length at least four belongs to \(\{100,001,011,110\}\). Thus the corresponding vertex has indegree \(q-1\) and outdegree \(q\). This imbalance excludes any Euler circuit that uses all allowed edges, proving nonexistence at every \(m\ge5\), even when extra alphabet symbols are present.

## Verification

The standalone `verify.py` constructs the full fourth-order overlap graph, checks every in/outdegree, and calculates exact integral Laplacian cofactors by the fraction-free Bareiss algorithm for \(q=2,3,4\). The respective rooted in-arborescence counts are \(4\), \(10{,}331{,}213{,}040\) and \(57{,}757{,}330{,}472{,}898{,}702{,}105{,}693{,}539{,}794{,}944{,}000\), all agreeing with the theorem. For \(q=2\) it independently exhausts all edge-circuits after fixing a single edge and finds exactly four. It also verifies the imbalance witness for all vertex lengths from \(4\) through \(150\). Run `python3 verify.py` in a Python 3 installation; no third-party modules are used. The finite checks corroborate, but do not replace, the all-parameter algebraic proof.

## Relationship to prior work

Chen, Kitaev and Sun (arXiv:1908.01116, first public in 2019; published 2020) study existence probabilities after removing sets of factors from de Bruijn graphs. Their Theorem 2.1 covers the **existence** of the fourth-order cycles after removing all binary short cycles for alphabets of at least three letters, and their binary order-four table is consistent with existence for two letters. Hence *existence at order four is not claimed as novel*. Their statements do not evaluate the number of Euler circuits for this exact removed family for all alphabets, nor the fixed-forbidden-motif obstruction at orders five and higher. Alhakim (2022) gives preference-function constructions under separative constraints; the paper's term “square-free” at separation one means avoiding equal **adjacent** letters, not the present exclusion of exactly length-four factors \(abab\). Moreno and Matamala's general language-constrained de Bruijn construction studies a lexicographically minimal cycle; no general-purpose constructive existence criterion entails the explicit enumerator here.

Related results about cyclic covers of the *excluded* tandem squares, and about universal cycles over *distinct-letter four-factors*, address different edge sets. Neither count implies the present count by complementation or subtraction of cycle numbers: Euler-tour counts of complementary edge sets are not additive.

## Limitations

The proof is mathematical and has not undergone independent external audit. The result does not count arbitrary square-free cyclic words, de Bruijn cycles omitting other motif families, cycles modulo alphabet relabeling or reversal, or partial coverings. A previously unindexed equivalent formula remains a priority risk, especially within general constrained universal-cycle enumeration literature. The historical literature establishes several general graph criteria and the fourth-order existence; the assessed new component is the **explicit all-alphabet fourth-order enumeration together with the same forbidden-family sharp order cutoff**.

## References

1. H. Z. Q. Chen, S. Kitaev and B. Y. Sun, *On the probability of existence of a universal cycle or a universal word for a set of words*, arXiv:1908.01116 (first public 2019-08-03); published as *Lower Bounds, and Exact Enumeration in Particular Cases, for the Probability of Existence of a Universal Cycle or a Universal Word for a Set of Words*, Mathematics 8 (2020), 778. https://arxiv.org/abs/1908.01116
2. A. M. Alhakim, *Designing preference functions for de Bruijn sequences with forbidden words*, Designs, Codes and Cryptography 90 (2022), 2319–2335. https://doi.org/10.1007/s10623-022-01077-5
3. E. Moreno and M. Matamala, *Minimal de Bruijn Sequence in a Language with Forbidden Substrings*, WG 2004, pp. 168–176; arXiv:0711.1695 (2007). https://arxiv.org/abs/0711.1695
4. The BEST theorem and the directed matrix-tree theorem, standard enumerative graph-theory results; cf. https://debruijnsequence.org/db/graph

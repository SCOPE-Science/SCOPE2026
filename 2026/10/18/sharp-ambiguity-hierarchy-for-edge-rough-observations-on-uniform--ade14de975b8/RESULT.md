# Sharp ambiguity hierarchy for edge rough observations on uniform loose hypercycles

## Finding

**Theorem.** Fix integers \(k\geq3\) and \(r\geq3\). Let \(H_{k,r}\) be the \(k\)-uniform loose hypercycle with distinct core vertices \(v_0,\ldots,v_{r-1}\), mutually disjoint private sets \(W_0,\ldots,W_{r-1}\), each of size \(k-2\), and hyperedges
\[
e_i=\{v_i,v_{i+1}\}\cup W_i\qquad(i\in\mathbb Z/r\mathbb Z).
\]
For every vertex subset \(X\), define the edge rough observation \(\rho(X)=(L(X),U(X))\), where
\[
L(X)=\{e:e\subseteq X\},\qquad U(X)=\{e:e\cap X\ne\varnothing\}.
\]
Thus every edge is recorded as empty, mixed, or full. Put \(B=2^{k-1}-1\).

1. The all-mixed observation \(Q_*=(\varnothing,E(H_{k,r}))\) is realized by exactly \(B^r+(-1)^r\) vertex subsets. It is the **unique** maximum-size observation fiber.
2. The second-largest fiber cardinality is exactly
\[
S_{k,r}=\frac{B^{r-1}+(-1)^{r-1}}2.
\]
Exactly \(2r\) observations attain it: those with a single specified empty or full edge and all remaining edges mixed. Every observation with at least two definite (empty or full) edges has strictly smaller multiplicity.
3. Every fiber is given by the transfer formula in the proof. The number of distinct observations is
\[
|\operatorname{im}\rho|=1+(1+\sqrt2)^r+(1-\sqrt2)^r,
\]
independently of \(k\). Under a uniform random vertex subset, the output min-entropy is
\[
H_\infty(\rho(X))=(k-1)r-\log_2\bigl(B^r+(-1)^r\bigr).
\]
In particular, the largest-to-second-largest multiplicity ratio converges to \(2(2^{k-1}-1)\) as \(r\to\infty\).

## Assumptions and scope

All vertices listed above are distinct except the intentional cyclic repetition \(v_r=v_0\). The private sets contain no core vertices; thus \(|V(H_{k,r})|=(k-1)r\). A *definite* edge is one observed as empty or full; a *mixed* edge intersects both \(X\) and its complement. The statement concerns the exact three-way edge observation induced by a binary vertex subset, not a rough relation obtained from an equivalence relation on the hyperedge set. Fibers are distinguished by labeled-edge observations. The main hypotheses \(k\ge3\) and \(r\ge3\) are essential to the stated hierarchy. When \(k=2\), the local transfer matrix has zero diagonal and the all-mixed status may be unrealizable for odd \(r\), so the theorem is not asserted there.

## Proof

**Local mixed-edge transfer.** Write \(q=2^{k-2}\) and \(B=2q-1\). For a mixed edge with its two core vertices fixed to bits \(a,b\), the private \(k-2\) vertices have \(q\) possible bit strings. If \(a\ne b\), every string gives a mixed edge. If \(a=b\), exactly the single constant string matching \(a\) is forbidden, leaving \(q-1\) choices. Consequently the number of completions across one mixed edge is the corresponding entry of
\[
M=\begin{pmatrix}q-1&q\\q&q-1\end{pmatrix}.
\]
Its eigenvectors \((1,1)\) and \((1,-1)\) have eigenvalues \(B\) and \(-1\), respectively. Hence, for every integer \(\ell\ge0\),
\[
(M^\ell)_{a,b}=\frac{B^\ell+(-1)^\ell}2\ \text{if }a=b,
\qquad
(M^\ell)_{a,b}=\frac{B^\ell-(-1)^\ell}2\ \text{if }a\ne b.
\]
For \(\ell=0\), this gives the identity matrix; for \(\ell\ge1\), every entry is positive because \(B\ge3\).

**Every exact fiber.** Represent an observation by a cyclic status word \(\sigma\in\{0,*,1\}^r\), where \(0\), \(*\), \(1\) mean empty, mixed, full. If all statuses are mixed, summing over cyclic sequences of core bits gives
\[
|\rho^{-1}(\sigma)|=\operatorname{tr}(M^r)=B^r+(-1)^r.
\]
Otherwise list the definite indices in cyclic order as \(i_1,\ldots,i_t\). Define \(i_{t+1}=i_1+r\) in a cyclic lift; choose the lift so \(i_1<\cdots<i_t<i_1+r\). Let \(\ell_j=i_{j+1}-i_j-1\ge0\), and let \(a_j\in\{0,1\}\) be the value forced on both core endpoints by the definite edge \(e_{i_j}\), with \(a_{t+1}=a_1\). The definite edges also uniquely fix all their private vertices. The mixed runs are disjoint in their private vertices and interior core vertices. Therefore
\[
\boxed{\quad |\rho^{-1}(\sigma)|=
\prod_{j=1}^t (M^{\ell_j})_{a_j,a_{j+1}}.\quad}
\]
This formula includes the case of adjacent definite edges: when \(\ell_j=0\), its factor is zero if their forced bits disagree, and one otherwise. Since every matrix entry for positive powers is positive, the status word is realized **if and only if** there is no adjacent cyclic pair of opposite definite statuses \(0,1\).

**The two largest fibers.** With a single definite edge, \(t=1\), the one mixed run has length \(r-1\) and its two forced endpoints have the same bit. The displayed formula gives \(S_{k,r}=(B^{r-1}+(-1)^{r-1})/2\); there are precisely two choices of definite status at each of the \(r\) indices.

For any \(\ell\ge0\), every entry of \(M^\ell\) is bounded above by \(m_\ell=(B^\ell+1)/2\). If \(a,b\ge0\), then
\[
m_a m_b\le m_{a+b},
\]
because this is equivalent to \((B^a-1)(B^b-1)\ge0\). Thus for \(t\ge2\), since \(\sum\ell_j=r-t\),
\[
|\rho^{-1}(\sigma)|\le\prod_jm_{\ell_j}\le m_{r-t}\le\frac{B^{r-2}+1}{2}
<\frac{B^{r-1}+(-1)^{r-1}}2=S_{k,r}.
\]
The strict inequality holds for all \(B\ge3\), \(r\ge3\): after multiplication by two its difference is \(B^{r-2}(B-1)+(-1)^{r-1}-1\ge 2B^{r-2}-2>0\). Finally, the all-mixed fiber exceeds \(S_{k,r}\), since \(B^r-1>(B^{r-1}+1)/2\). Uniqueness and the exact runner-up classification follow.

**Observation count.** The proven admissibility criterion says that neighboring letters \(0\) and \(1\) cannot occur consecutively in the cyclic status word, while every other adjacent pair is allowed. The three-state transition matrix in the order \(0,*,1\) is
\[
T=\begin{pmatrix}1&1&0\\1&1&1\\0&1&1\end{pmatrix}.
\]
For \(r\ge3\), the number of admissible cyclic words is \(\operatorname{tr}(T^r)\). Its eigenvalues are \(1,1+\sqrt2,1-\sqrt2\), yielding the claimed observation count. Since a uniform subset has probability \(2^{-(k-1)r}\) and each observation probability equals its fiber size times that number, the exact min-entropy follows. The ratio limit follows by dividing its numerator and denominator by the appropriate powers of \(B\).

## Verification

The self-contained Python 3 program `verify.py` independently enumerates all subsets of the hypercycle's vertex set and every possible three-symbol observation word. It checks the transfer product against every observed fiber (including unrealized words), exact maximum and runner-up values and counts, total probability mass, and the Pell-type observation count. Verified cases are \(k=3\), \(3\le r\le7\); \(k=4\), \(3\le r\le5\); \(k=5\), \(3\le r\le4\); and \((k,r)=(6,3)\). These comprise \(161600\) explicitly enumerated binary subsets. Run `python3 verify.py` in the directory containing this file. The general theorem rests on the preceding proof, not on finite enumeration.

## Relationship to prior work

Rough approximations and hypergraph formulations are developed by Sarwar (2022), whose construction uses equivalence relations on vertices and hyperedge collections; its rough hypercycle and line-graph theory do not give the present labeled-edge inverse-fiber counts. Cattaneo, Chiaselotti, Ciucci, and Gentile (2016; an earlier preprint was publicly accessible in 2015) connect hypergraphs, formal concept analysis, and rough sets via Boolean information tables and investigate complete uniform hypergraphs and indiscernibility partitions; this is a different observation map. Standard loose-cycle hypergraphs also feature in English, Kostochka, and Zirlin (2023), focused on saturation rather than information loss. Crucially, the **numerical observation-count sequence is already known**: under the substitution \(0,*,1\mapsto1,2,3\), allowable status words are exactly the smooth cyclic words enumerated in Knopfmacher, Mansour, Munagi, and Prodinger (2008), Theorem 3.3, and OEIS A124696. Neither the sequence nor the standard cyclic transfer-matrix technique is claimed as new.

The specific contribution is the complete local transfer description and **sharp first-versus-second inverse-fiber hierarchy simultaneously for all hyperedge ranks \(k\ge3\)**, as well as the identification of the particular rough-observation map with the previously known cyclic-word count. The binary graph-edge case is not a covering theorem: its local matrix has zero diagonal and loses the strict positivity needed here.

## Limitations

The proof addresses only the explicitly defined loose hypercycles and three-level edge observation, not arbitrary hypergraphs, generalized rough relations, nonuniform private-set sizes, or probabilistic vertex weights. The general problem of identifying the largest fibers for arbitrary intersecting hypergraphs remains open here. An independently verified publication-priority determination has not been performed; equivalent descriptions under constraint-satisfaction or transfer-matrix terminology remain a search risk.

## References

1. M. Sarwar, *A Theoretical Investigation Based on the Rough Approximations of Hypergraphs*, Journal of Mathematics (2022), article 1540004, first published 2022-03-07, https://doi.org/10.1155/2022/1540004.
2. G. Cattaneo, G. Chiaselotti, D. Ciucci and T. Gentile, *On the connection of hypergraph theory with formal concept analysis and rough set theory*, Information Sciences 330 (2016), 342–357, https://doi.org/10.1016/j.ins.2015.09.054; publicly available submitted preprint https://boa.unimib.it/retrieve/e39773b2-f7e4-35a3-e053-3a05fe0aac26/HypFINAL.pdf.
3. S. English, A. Kostochka and D. Zirlin, *Saturation for the 3-uniform loose 3-cycle*, Discrete Mathematics 346 (2023), 113504, https://doi.org/10.1016/j.disc.2023.113504.
4. A. Knopfmacher, T. Mansour, A. Munagi and H. Prodinger, *Smooth words and Chebyshev polynomials*, arXiv:0809.0551v1 (2008), especially Theorem 3.3, https://arxiv.org/abs/0809.0551.
5. OEIS Foundation, *A124696: Number of base-3 circular n-digit numbers with adjacent digits differing by 1 or less*, https://oeis.org/A124696; sequence originally submitted by R. H. Hardin in 2006.

# Exact enumeration of two-symbol length-four universal cycles

## Finding

Let \(q\ge2\) be an integer and let \(\Sigma_q\) be a labeled alphabet of size \(q\). Put
\[
\mathcal S_q=\{w\in\Sigma_q^4:|\operatorname{alph}(w)|=2\}.
\]
An **oriented universal cycle** for \(\mathcal S_q\) is a circular word whose cyclic length-four factors, counted with multiplicity, are precisely the elements of \(\mathcal S_q\), each once. Cyclic rotations are identified, whereas reversal and permutations of the alphabet are not.

**Theorem.** Such cycles exist for every \(q\ge2\). Their number is exactly
\[
\boxed{U_q=2^{(q-1)(q+2)}q^{q-2}
7^{\binom{q-1}{2}}\big((q-2)!\big)^q.}
\]
Each cycle has length \(|\mathcal S_q|=7q(q-1)\). In particular,
\[
U_2=16,\qquad U_3=21504,\qquad U_4=23018340352.
\]
For the alphabet \(\{0,1,2\}\), one such circular word is
`000100020022020222111001101011121122121222`.

## Assumptions and scope

All alphabet symbols are distinguished, the cycles have the exact required length, and the windows wrap cyclically. The count does not quotient by alphabet relabeling, reversal, or any other action beyond cyclic rotation. The parameter ranges over every integer \(q\ge2\); no claim is made for \(q=1\) or for different window lengths or support sizes.

## Proof

**1. Restricted overlap graph and its degrees.** The \(q(q-1)/2\) unordered pairs of symbols each contribute \(2^4-2=14\) nonconstant binary four-words, giving \(|\mathcal S_q|=7q(q-1)\). Construct a directed graph \(G_q\) with an edge labeled by every \(abcd\in\mathcal S_q\), from its three-letter prefix \(abc\) to its suffix \(bcd\). The vertices are exactly
\[
A_a=aaa\quad(a\in\Sigma_q),\qquad
B_{ab}=aab,\quad C_{ab}=aba,\quad D_{ab}=abb\quad(a\ne b).
\]
There are \(q+3q(q-1)\) vertices. Each \(A_a\) has incoming and outgoing degree \(q-1\); every other vertex has both degrees equal to \(2\). For distinct \(a,b\), the outgoing transitions are
\[
\begin{aligned}
A_a&\longrightarrow B_{ab},\\
B_{ab}&\longrightarrow C_{ab},D_{ab},\\
C_{ab}&\longrightarrow D_{ba},C_{ba},\\
D_{ab}&\longrightarrow B_{ba},A_b.
\end{aligned}
\]
These rules cover all edges. The route \(A_a\to B_{ab}\to D_{ab}\to A_b\) connects the constant vertices for all ordered pairs \(a\ne b\). Every nonconstant vertex occurs on a directed route from a constant vertex and reaches a constant vertex. Consequently, \(G_q\) is strongly connected and balanced. Its Euler circuits correspond bijectively to the universal cycles under consideration.

**2. A six-vertex block for each unordered symbol pair.** Let \(L\) be the outdegree Laplacian, so \(L_{uv}=-\#\{\text{edges }u\to v\}\) for distinct vertices and diagonal entries are outgoing degrees (loops, if present, are subtracted also; here none occur). Order the nonconstant vertices for a fixed unordered pair \(\{a,b\}\) as
\[
(B_{ab},C_{ab},D_{ab},B_{ba},C_{ba},D_{ba}).
\]
The corresponding block of \(L\) is
\[
X=\begin{pmatrix}
2&-1&-1&0&0&0\\
0&2&0&0&-1&-1\\
0&0&2&-1&0&0\\
0&0&0&2&-1&-1\\
0&-1&-1&0&2&0\\
-1&0&0&0&0&2
\end{pmatrix}.
\]
Direct integer elimination gives \(\det X=28\). With constant-vertex rows ordered \((A_a,A_b)\), the couplings \(U=L_{A,I}\) and \(T=L_{I,A}\) have their only nonzero entries \(U_{1,1}=U_{2,4}=-1\) and \(T_{3,2}=T_{6,1}=-1\), respectively. Exact rational elimination gives
\[
UX^{-1}T=\frac17\begin{pmatrix}3&4\\4&3\end{pmatrix}.
\]
There are no Laplacian connections between internal blocks belonging to different unordered symbol pairs: a length-three vertex containing exactly two symbols only participates in the corresponding pair's four-letter edges. The full internal block is therefore a direct sum of \(\binom q2\) copies of \(X\).

**3. Reduced Laplacian and arborescences.** Eliminating these nonconstant blocks, the Schur complement on the \(q\) constant vertices is
\[
S=(q-1)I_q-\sum_{\{a,b\}}
\frac17\begin{pmatrix}3&4\\4&3\end{pmatrix}_{\{a,b\}}
=\frac47(qI_q-J_q),
\]
where \(J_q\) is the all-ones matrix and each two-by-two block in the sum is embedded in the \(a,b\) coordinates. Fix a root \(A_0\) (the label \(0\) may be chosen on any alphabet). The directed matrix-tree theorem applied to the outdegree Laplacian counts in-arborescences oriented toward \(A_0\) by deleting its row and column. Since \(\det(qI_{q-1}-J_{q-1})=q^{q-2}\), the rooted tree count is
\[
\begin{aligned}
t_q&=28^{\binom q2}\left(\frac47\right)^{q-1}q^{q-2}\\
&=2^{(q-1)(q+2)}7^{\binom{q-1}{2}}q^{q-2}.
\end{aligned}
\]
Both the six-state determinant and the transfer matrix are verifiable by explicit exact-rational elimination; `verification.py` independently recomputes them and the entire cofactor for several values of \(q\).

**4. Counting directed Euler circuits.** Distinguish the edge labeled `0001`, directed out of \(A_0\), after fixing two distinct letters labeled `0` and `1`. Every universal cycle contains that edge exactly once, so choosing it as the first edge gives a unique representative of each rotation class. By the BEST theorem, the number of Euler circuits beginning with this fixed edge equals
\[
t_q\prod_{v\in V(G_q)}(\deg^+(v)-1)!.
\]
Nonconstant vertices have degree two and contribute \(1!=1\). The \(q\) constant vertices have degree \(q-1\), giving \(\big((q-2)!\big)^q\). This proves the asserted formula. Positivity of its factors, together with strong connectivity, also proves existence for every \(q\ge2\). \(\square\)

## Verification

Run `python3 verification.py` using Python 3 and its standard library. It recomputes the six-state determinant \(28\) and the exact transfer matrix, directly enumerates all sixteen binary Euler circuits beginning with the fixed first edge, and independently forms the full restricted overlap-graph Laplacian. Fraction-free integer cofactors for \(q=2,3,4,5,6\) agree exactly with the all-parameter formula. Deterministic Eulerian construction supplies and verifies length-\(7q(q-1)\) cyclic witnesses for \(q=2,3,4\). The observed terminal output is `VERIFY_OK`.

The proof, not these finite tests, establishes the theorem for all \(q\ge2\).

## Relationship to prior work

Gardner and Godbole [1] establish existence for several restricted universal-cycle languages, including onto and augmented-onto words. Their existence conclusions do not enumerate cycles for the exact range-size-two four-word language on arbitrary \(q\). Leitner and Godbole [2] give existence results for non-bijections and near-onto words with different restrictions; these do not yield the present count. Chen, Kitaev, and Sun [3] analyze which small deletions from unrestricted de Bruijn languages permit universal cycles and count sets of deletions, not the number of Euler tours in this structured length-four restricted language. In the binary \(q=2\) case, the selected language is the set of all nonconstant four-words; prior existence results cover this case but do not provide the general alphabet-dependent enumeration.

The main contribution is the exact all-\(q\) tour count, derived from a pairwise six-state Laplacian decomposition and the directed matrix-tree and BEST theorems. Earlier length-three two-symbol universal-cycle counts use a different overlap graph, and enumerations of length-four words using three or four symbols concern nonidentical languages; none of those statements imply this formula without new graph analysis.

## Limitations

Novelty is qualified by the possibility of an unindexed or differently formulated earlier enumeration. This result addresses only oriented cycles modulo rotation for length-four windows with exactly two distinct letters. No uniqueness under relabeling or reversal is claimed. The finite verifier is corroboration, not a proof for infinitely many alphabet sizes; the proof rests on the explicit Laplacian block and established matrix-tree/BEST identities.

## References

1. KB Gardner and Anant Godbole, *Universal Cycles of Restricted Words*, arXiv:1711.07029, first posted November 19, 2017. https://arxiv.org/abs/1711.07029
2. Arielle Leitner and Anant Godbole, *Universal Cycles of Restricted Classes of Words*, arXiv:0808.1309 (2008). https://arxiv.org/abs/0808.1309
3. Herman Z. Q. Chen, Sergey Kitaev, and Brian Y. Sun, *On the probability of existence of a universal cycle or a universal word for a set of words*, arXiv:1908.01116, first posted August 3, 2019; published as *Lower Bounds, and Exact Enumeration in Particular Cases, for the Probability of Existence of a Universal Cycle or a Universal Word for a Set of Words*, Mathematics 8 (2020), 778. https://arxiv.org/abs/1908.01116

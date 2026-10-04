# Fubini orbit profile of the universal homogeneous echeloned space

## Finding
Let \(\mathbf F\) be the unique countable universal homogeneous echeloned space. For \(n\ge 1\), let \(a_n\) be the number of \(\operatorname{Aut}(\mathbf F)\)-orbits on injective ordered \(n\)-tuples. Then
\[
a_n=F_{\binom n2}=\sum_{j=0}^{\binom n2} j!\,S(\binom n2,j),
\]
where \(F_m\) is the \(m\)-th Fubini number (ordered Bell number), equivalently the number of weak orders on an \(m\)-element labeled set, and \(S(m,j)\) is a Stirling number of the second kind.

The first injective orbit counts are
\[
a_1,a_2,a_3,a_4,a_5,a_6=1,1,13,4683,102247563,230283190977853.
\]

If \(b_n\) denotes the number of orbits on all ordered \(n\)-tuples, allowing repeated coordinates, then
\[
b_n=\sum_{k=1}^n S(n,k)F_{\binom k2}.
\]
In particular,
\[
b_1,b_2,b_3,b_4,b_5=1,2,17,4769,102294734.
\]
Finally, the standard asymptotic for the Fubini numbers gives
\[
a_n\sim \frac{(\binom n2)!}{2(\log 2)^{\binom n2+1}}.
\]

## Assumptions and scope
An echeloned space on a set \(X\) is the structure introduced by Gheysens, Pavlica, Pech, Pech, and Schneider: a total preorder on ordered pairs \(X^2\) in which every diagonal pair is least, no off-diagonal pair is tied with the diagonal, and reversing an ordered pair preserves its echelon class. The source proves that the finite echeloned spaces form a Fraïssé class and denotes its countable universal homogeneous limit by \(\mathbf F\).

The statement concerns the automorphism action of that specific Fraïssé limit. Tuple coordinates are ordered. The injective formula counts tuples with pairwise distinct coordinates; the second formula separately accounts for equality patterns.

## Proof
Fix \(n\ge 1\) and label the coordinates by \([n]=\{1,\ldots,n\}\). For an injective tuple \(\bar x=(x_1,\ldots,x_n)\), its induced finite echeloned subspace is completely determined by the relative echelon levels of the unordered pairs
\[
\binom{[n]}2=\{\{i,j\}:1\le i<j\le n\}.
\]
Indeed, all diagonal pairs have the common least echelon level, every off-diagonal pair lies strictly above it, and symmetry identifies \((x_i,x_j)\) with \((x_j,x_i)\). Therefore the remaining information is exactly a total preorder, or weak order, on the \(\binom n2\) labeled unordered pairs.

Conversely, every weak order on \(\binom{[n]}2\) defines a finite echeloned space on \([n]\): put all diagonal ordered pairs in a new least class and assign each off-diagonal ordered pair the rank of its underlying unordered pair. The echelon axioms are immediate. Since \(\mathbf F\) is universal for all finite echeloned spaces, every such weak order occurs on some injective ordered \(n\)-tuple in \(\mathbf F\).

Two injective ordered tuples \(\bar x\) and \(\bar y\) lie in the same automorphism orbit exactly when the coordinate map \(x_i\mapsto y_i\) is an isomorphism between their induced finite subspaces. By homogeneity of \(\mathbf F\), every such finite isomorphism extends to an automorphism. Thus the orbit set is in bijection with weak orders on a labeled set of size \(\binom n2\). A weak order with exactly \(j\) levels is an ordered partition into \(j\) nonempty blocks, counted by \(j!S(\binom n2,j)\). Summing over \(j\) proves the injective formula.

For arbitrary ordered \(n\)-tuples, first fix the equality partition of the \(n\) coordinate positions into \(k\) blocks. There are \(S(n,k)\) such partitions. Choosing a canonical order of the blocks by their least positions identifies the distinct coordinate values with an injective ordered \(k\)-tuple, so each equality partition contributes exactly \(a_k=F_{\binom k2}\) orbits. Summing over \(k\) proves the formula for \(b_n\).

The asymptotic follows by substituting \(m=\binom n2\) into the classical Fubini-number estimate
\[
F_m\sim \frac{m!}{2(\log 2)^{m+1}}.
\]

## Verification
The bundled script `verify.py` computes Stirling and Fubini numbers exactly, checks the displayed injective and repeated-coordinate values, and independently enumerates all rank-surjections representing weak orders on up to six labeled pairs. In particular it brute-force recovers \(F_6=4683\), the \(n=4\) injective orbit count. These finite checks corroborate the arithmetic and the weak-order encoding; the general theorem is established by the Fraïssé-homogeneity proof above, not by finite enumeration.

## Relationship to prior work
The defining paper introduces echeloned spaces, proves that finite echeloned spaces form a Fraïssé class, and constructs the unique countable universal homogeneous limit \(\mathbf F\). It also studies the associated edge-coloured graph and the automorphism group, but targeted inspection of the full text found no tuple-orbit enumeration and no occurrence of “Fubini.”

The combinatorial sequence itself is classical: OEIS A000670 records the Fubini numbers as the numbers of weak orders on labeled sets and gives the same asymptotic. The contribution here is the model-theoretic identification of the complete ordered-tuple orbit profile of \(\mathbf F\) with the subsequence \(F_{\binom n2}\), together with the equality-pattern Stirling transform for noninjective tuples.

Several contemporary orbit-profile results for other homogeneous structures were checked as nearby comparisons. They concern different Fraïssé limits and do not imply the echeloned-space formula.

## Limitations
The originality check used targeted searches of the defining paper, general web literature, and a semantic research index. No covering source was located, but an elementary consequence of homogeneity can exist as folklore, in lecture notes, or under terminology not captured by the searches. The claim is therefore an exact derived invariant of the 2023 construction, not a claim that Fubini numbers or their asymptotics are new.

## References
1. M. Gheysens, B. Pavlica, C. Pech, M. Pech, and F. M. Schneider, *Echeloned Spaces*, arXiv:2312.11141 (first public version 2023-12-18); Forum of Mathematics, Sigma 13 (2025), e89, DOI 10.1017/fms.2025.47.
2. OEIS Foundation Inc., *A000670 — Fubini numbers (ordered Bell numbers)*, accessed 2026-10-01.

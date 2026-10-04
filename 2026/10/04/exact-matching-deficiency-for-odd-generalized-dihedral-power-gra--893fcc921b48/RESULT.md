# Exact matching deficiency for odd generalized dihedral power graphs

## Finding

Let \(A\) be a nontrivial finite abelian group of odd order \(m\), and let
\[
G=\operatorname{Dih}(A)=A\rtimes\langle t\rangle,\qquad t^2=1,\qquad tat=a^{-1}\quad(a\in A).
\]
Then
\[
\mu(\mathcal P(G))=\mu(\mathcal P_e(G))=\frac{m+1}{2}.
\]
In fact, in either graph every maximum matching uses exactly one edge from the coset \(At\) to the identity, saturates every vertex of \(A\), and leaves the other \(m-1\) elements of \(At\) unmatched.

Equivalently, the matching deficiency of either graph is \(m-1\). For noncyclic \(A\), this extends the previously computed ordinary-dihedral case to a genuinely broader generalized-dihedral family.

## Assumptions and scope

The group \(A\) is finite, abelian, nontrivial, and of odd order \(m\). The power graph \(\mathcal P(G)\) has vertex set \(G\), with distinct vertices adjacent when one is a power of the other. The enhanced power graph \(\mathcal P_e(G)\) has the same vertex set, with distinct vertices adjacent when they lie in a common cyclic subgroup.

No claim is made here for generalized dihedral groups with even-order kernel.

## Proof

Write elements of the nontrivial coset as \(at\), with \(a\in A\). Since the action is inversion,
\[
(at)^2=atat=aa^{-1}=1.
\]
Thus every element of \(At\) is an involution.

First consider the power graph. If \(x=at\in At\), then the powers of \(x\) are only \(1\) and \(x\). No element of \(A\) has a power in \(At\), and every other element of \(At\) also has order \(2\). Hence \(x\) is adjacent only to \(1\). Therefore \(\mathcal P(G)\) is obtained from the induced copy of \(\mathcal P(A)\) by attaching all \(m\) vertices of \(At\) as pendant vertices at \(1\).

The same pendant statement holds in the enhanced power graph. If \(x=at\) and \(y\in A\setminus\{1\}\), then
\[
xyx^{-1}=y^{-1},
\]
so \(x\) and \(y\) commute only if \(y=y^{-1}\). Since \(A\) has odd order, that forces \(y=1\). Two distinct elements of \(At\) also cannot commute: their product lies in \(A\), and if two involutions commute then their product has order at most \(2\), hence is \(1\) because \(A\) has odd order; the involutions would then be equal. Since two elements lying in a common cyclic subgroup commute, no vertex of \(At\) is enhanced-adjacent to any vertex other than \(1\). Thus \(\mathcal P_e(G)\) is obtained from \(\mathcal P_e(A)\) by the same \(m\) pendant vertices at \(1\).

Because \(m\) is odd, every \(a\in A\setminus\{1\}\) satisfies \(a\ne a^{-1}\). The inverse pairs
\[
\{a,a^{-1}\}
\]
partition \(A\setminus\{1\}\), and each pair is an edge in both \(\mathcal P(A)\) and \(\mathcal P_e(A)\). Hence \(A\setminus\{1\}\) has a perfect matching of size \((m-1)/2\). Adding one pendant edge \(\{1,t\}\) gives a matching of size
\[
1+\frac{m-1}{2}=\frac{m+1}{2}.
\]

For the upper bound, all \(m\) vertices of \(At\) have the same unique neighbor \(1\), so a matching contains at most one edge incident with \(At\). If it contains no such edge, it has at most \(\lfloor m/2\rfloor=(m-1)/2\) edges inside \(A\). If it contains one such edge, the identity is unavailable and at most \((m-1)/2\) further edges can lie in \(A\setminus\{1\}\). Therefore every matching has size at most \((m+1)/2\), proving equality.

Finally, a maximum matching cannot omit all pendant edges, since that would give at most \((m-1)/2\) edges. Hence it uses exactly one pendant edge. Equality then forces a perfect matching on \(A\setminus\{1\}\), so every vertex of \(A\) is saturated and exactly \(m-1\) coset involutions remain unmatched.

## Verification

The symbolic argument proves the statement for every finite abelian odd-order \(A\). The included exact replay constructs generalized dihedral groups for
\[
A\cong C_3,\ C_5,\ C_9,\ C_3\times C_3,
\]
builds both graphs directly from the group law and cyclic subgroups, checks that every coset involution is pendant at the identity, and computes the exact matching number by exhaustive dynamic programming. It returns `VERIFY_OK`.

## Relationship to prior work

Panda, Dalal, and Kumar computed the matching number of the enhanced power graph of the ordinary dihedral group \(D_{2n}\), obtaining \(\lceil n/2\rceil\). Their family has cyclic rotation kernel. The present statement recovers the odd cyclic case and extends it to every odd-order finite abelian kernel, including noncyclic groups such as \(C_3\times C_3\).

Cameron, Swathi, and Sunitha proved general upper and lower bounds for power-graph matching, proved that odd-order groups have matching number \((|G|-1)/2\), proved equality of the power-graph and enhanced-power-graph matching numbers, and explicitly left a general matching formula as an open problem. For the present family, \(|I(G)|=|O(G)|=m\), so their involution-versus-odd-order obstruction gives no unmatched vertices, whereas the exact deficiency is \(m-1\). Moreover \(C_G(I(G))=\{1\}\), so their centralizer-based construction bound is attained exactly.

Brachter and Kaja study generalized dihedral groups in the different context of chordality of power graphs and record the inversion-action structure, but do not address matching numbers.

## Limitations

The result does not treat even-order kernels, for which the coset need not consist of pendant involutions and the inverse-pair argument changes. The originality assessment is based on targeted database and full-text searches; an unindexed equivalent observation could exist. The finite replay is only a sanity check and is not used as evidence for the infinite theorem.

## References

1. R. P. Panda, S. Dalal, and J. Kumar, “On the enhanced power graph of a group,” *Communications in Algebra* 49 (2021), 1697–1716. arXiv:2001.08932; DOI: 10.1080/00927872.2020.1847289.
2. P. J. Cameron, V. V. Swathi, and M. S. Sunitha, “Matching in power graphs of finite groups,” *Annals of Combinatorics* 26 (2022), 379–391. arXiv:2107.01157; DOI: 10.1007/s00026-022-00576-5.
3. J. Brachter and E. Kaja, “On groups with chordal power graph, including a classification in the case of finite simple groups,” *Journal of Algebraic Combinatorics* 58 (2023), 1095–1124. arXiv:2209.00317; DOI: 10.1007/s10801-023-01262-2.

# The center of reduced power monoids over odd generalized dihedral groups

## Finding
Let \(H\) be a nontrivial finite abelian group of odd order and \(G=H\rtimes\langle s\rangle\), where \(s\) acts on \(H\) by inversion. The full center of the reduced power monoid \(\mathcal P_1(G)\), and not merely its group-conjugacy-invariant part, is classified below. Write the complement of \(A\in\mathcal P_1(G)\) uniquely as
\[
G\setminus A=R\sqcup Ss,\qquad R,S\subseteq H,\quad 1\notin R.
\]
Then \(A\in Z(\mathcal P_1(G))\) precisely in the following disjoint cases:

1. \(S=\varnothing\), with \(R\) **any** subset of \(H\setminus\{1\}\).
2. \(S=aK\) for a subgroup \(K\le H\) and a coset representative \(a\in H\), with \(R\subseteq K\setminus\{1\}\) and \(R=R^{-1}\).

In the second case \(K=SS^{-1}\) is unique. Consequently
\[
\boxed{\bigl|Z(\mathcal P_1(G))\bigr|=2^{|H|-1}+\sum_{K\le H}|H:K|\,2^{(|K|-1)/2}.}
\]
For \(H\cong C_p\), where \(p\) is an odd prime, this becomes \(2^{p-1}+p+2^{(p-1)/2}\). The count distinguishes abelian kernels of the same order: it is \(287\) for \(C_9\) and \(305\) for \(C_3\times C_3\).

## Assumptions and scope
All subsets are finite because \(G\) is finite. Setwise multiplication is \(AB=\{ab:a\in A,\ b\in B\}\). The identity in \(\mathcal P_1(G)\) is \(\{1\}\); elements are exactly subsets containing \(1\). The center means \(Z(\mathcal P_1(G))=\{A\in\mathcal P_1(G):AB=BA\ \forall B\in\mathcal P_1(G)\}\). We use additive notation for \(H\) inside the proof, with \(0\) corresponding to the group identity. Odd order is essential to the step in which multiplication by \(2\) is inverted.

## Proof
**1. Reduction to two-point tests.** For arbitrary \(A,B\in\mathcal P_1(G)\), since \(1\in B\),
\[
AB=A\cup\bigcup_{g\in B}(Ag),\qquad BA=A\cup\bigcup_{g\in B}(gA).
\]
Thus \(A\) is central if and only if \(A\cup Ag=A\cup gA\) for every \(g\in G\): necessity follows from \(B=\{1,g\}\), and sufficiency by taking unions. If \(C=G\setminus A\), right and left multiplication are bijections of \(G\), so this is equivalent to
\[
\tag{1} C\cap Cg=C\cap gC\qquad(g\in G).
\]
This criterion uses only the complement, without assuming that \(A\) is conjugacy invariant.

**2. Rotation tests determine the reflection complement.** Identify elements of \(G\) with pairs \((x,\epsilon)\), for \(x\in H\) and \(\epsilon\in\{0,1\}\), with product
\[
(x,\epsilon)(y,\delta)=(x+(-1)^\epsilon y,\epsilon+\delta\pmod2).
\]
Write \(C=R\sqcup(S\times\{1\})\), suppressing the second coordinate for rotations. When \(g=(k,0)\), its rotation part in (1) agrees automatically because \(H\) is abelian; its reflection part is exactly
\[
\tag{2} S\cap(S-k)=S\cap(S+k)\qquad(k\in H).
\]
If \(S=\varnothing\), (2) imposes no restriction. If \(S\ne\varnothing\), then (2) implies
\[
\tag{3} 2a-b\in S\qquad\text{for every }a,b\in S.
\]
Indeed, put \(k=b-a\) in (2) and test membership at \(a\). Hence each reflection of \(H\) about an element of \(S\), namely \(x\mapsto2a-x\), preserves \(S\). Composing reflections about \(a,b\in S\) gives translation by \(2(a-b)\), so \(S\) is invariant under translations by \(2K\), where \(K=\langle a-b:a,b\in S\rangle\). As \(|H|\) is odd, multiplication by \(2\) is an automorphism of \(H\), and \(2K=K\). Choosing \(a_0\in S\), we have \(S\subseteq a_0+K\) by definition and \(a_0+K\subseteq S\) by translation invariance. Therefore \(S=a_0+K\) is a coset, and \(K\) is uniquely determined. Conversely any coset satisfies (2), because the two intersections are both \(S\) when \(k\in K\) and both empty otherwise.

**3. Reflection tests determine the rotation complement.** With \(g=(k,1)\), equation (1) splits into precisely two set equalities:
\[
\tag{4} R\cap(S-k)=R\cap(k-S),\qquad S\cap(R+k)=S\cap(k-R)\quad(k\in H).
\]
When \(S=\varnothing\), both are automatic; thus every \(R\subseteq H\setminus\{0\}\) is permitted. If \(S=a_0+K\), the first equality in (4), applied at a fixed \(r\in R\), is equivalent to
\[
\mathbf1_S(k+r)=\mathbf1_S(k-r)\qquad\text{for every }k\in H.
\]
It says that translation by \(2r\) preserves \(S\); the stabilizer subgroup of the coset \(a_0+K\) is exactly \(K\). Therefore \(2r\in K\), and, since \(|K|\) is odd, \(r\in K\). Conversely \(R\subseteq K\) implies the first equality in (4). The second equality in (4), applied at any fixed \(t\in S\) and allowing \(k\) to vary, is equivalent to
\[
\mathbf1_R(x)=\mathbf1_R(-x)\qquad\text{for every }x\in H,
\]
namely \(R=-R\). These implications reverse, so conditions (2) and (4) are jointly necessary and sufficient. By step 1 they are exactly the centrality conditions for \(A\).

**4. Enumeration.** If \(S=\varnothing\), there are \(2^{|H|-1}\) choices for \(R\). If \(S\ne\varnothing\), every \(S\) is a unique coset of a unique subgroup \(K\le H\), so for fixed \(K\) there are \(|H:K|\) choices for \(S\). Since \(K\) has odd order, inversion partitions \(K\setminus\{0\}\) into exactly \((|K|-1)/2\) unordered pairs \(\{k,-k\}\). Exactly \(2^{(|K|-1)/2}\) subsets \(R\) are inversion-stable. Multiplication and summation of these disjoint possibilities prove the displayed formula. For \(C_p\), only the trivial and full subgroups occur. For \(C_9\), the subgroup orders are \(1,3,9\), each once; for \(C_3\times C_3\), there are four distinct subgroups of order \(3\), yielding the two numerical values.

## Verification
The accompanying self-contained Python 3 program `verify_general.py` independently enumerates all subsets containing the identity for \(H=C_3,C_5,C_7,C_9,C_3\times C_3\). It tests commutation against every two-point subset \(\{1,g\}\) by direct group multiplication and, separately, tests the coset-based classification and the subgroup-sum count. The reproduced center counts are respectively \(9,25,79,287,305\); the program exits with `VERIFY_OK` when all checks match. These are finite stress tests only; the proof for every finite odd-order abelian \(H\) is in the preceding section.

## Relationship to prior work
The theory of large, finitary, and reduced power monoids is surveyed in Tringali (2026). Tringali and Wen (2026) examine automorphisms of power semigroups of numerical semigroups, a commutative-base setting. Wen, He, and Liu (2026) describe power monoids through Kleisli convolution. The present theorem addresses a different invariant—**the center**—for a noncommutative family, and gives its exact elements and size. Results about automorphism groups, embeddability, or power graphs do not by themselves determine this center. A close general-group paper by Bershadsky and Kublanovsky (2025) primarily studies semigroup embeddability; its full text was not available for comparison, leaving a prior-art risk.

For comparison, in the **unreduced** power monoid \(\mathcal P(G)\) of nonempty subsets, commutation with every singleton \(\{g\}\) forces conjugation invariance, and conversely a conjugation-invariant subset commutes with every subset. The reduced monoid does **not** contain most singletons, and the present larger center is therefore not implied by the unreduced case.

## Limitations
The theorem applies only to finite generalized dihedral groups with abelian odd-order kernel. The even-order and nonabelian-kernel settings are not classified here. The exact center count is a combinatorial-semigroup theorem, not an isomorphism classification of reduced power monoids. Literature comparison cannot exclude an equivalent result in unindexed or inaccessible sources. Verification is self-review and finite computational testing; no independent audit has been performed.

## References
1. S. Tringali, *Power monoids and their arithmetic: a survey*, arXiv:2602.15754 (first posted 17 February 2026).
2. S. Tringali and K. Wen, *On the automorphisms of the power semigroups of a numerical semigroup*, arXiv:2604.26901 (first posted 29 April 2026).
3. H. Wen, J. He, and Y.-Z. Liu, *Kleisli convolution representations of power monoids*, arXiv:2608.27292 (first posted 27 August 2026).
4. S. G. Bershadsky and S. I. Kublanovsky, *On power semigroups of groups*, Semigroup Forum 111 (2025), 543–560, DOI: 10.1007/s00233-025-10594-3 (abstract and accessible preview only; full text not checked).

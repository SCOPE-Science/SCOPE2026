# The Catalan quotient reflects commutation of 0-Hecke idempotents

## Finding

Let \(H_n\) be the type-\(A_n\) 0-Hecke monoid, with simple idempotent generators \(\pi_1,\ldots,\pi_n\). Let \(C_{n+1}\) be the monoid of nondecreasing, regressive maps on \([n+1]\), and let \(\Phi:H_n\to C_{n+1}\) be the homomorphism sending \(\pi_i\) to the map lowering \(i+1\) to \(i\) and fixing the other points. Then \(\Phi\) restricts to a bijection of idempotents and **reflects commutation on them**:
\[
\pi_I\pi_J=\pi_J\pi_I\quad\Longleftrightarrow\quad
\Phi(\pi_I)\Phi(\pi_J)=\Phi(\pi_J)\Phi(\pi_I).
\]
Here \(\pi_I\) denotes the idempotent indexed by \(I\subseteq[n]\), namely the longest element of the standard parabolic subgroup, with the 0-Hecke multiplication. A pair commutes precisely when each consecutive run of \(I\cup J\) is wholly contained in \(I\) or wholly contained in \(J\); its product is then \(\pi_{I\cup J}\). The quotient thus identifies the idempotent commuting graphs and their clique complexes, with the partial product operations on commuting families. In particular, every fixed-arity ordered commuting-tuple count in the Catalan monoid transfers unchanged to \(H_n\). A finite transfer matrix for those counts is given below.

## Assumptions and scope

The integer \(n\ge 0\) counts simple generators, not chain points. At \(n=0\) both monoids are trivial. Function products apply the rightmost map first. Tuple entries may repeat and all pairs of entries must commute. The result is about idempotents and their partially defined commuting products, not commutation reflection for arbitrary elements or an isomorphism of the two monoids.

## Proof

**Idempotents and images.** The idempotents of \(H_n\) are exactly the parabolic longest elements \(\pi_I\) [1]. Write \(\alpha_i=\Phi(\pi_i)\) and \(F_I=\{1\}\cup\{i+1:i\notin I\}\). Every point of \(F_I\) is fixed by all generators in \(I\), hence by \(\Phi(\pi_I)\). For \(i\in I\), left parabolic absorption \(\pi_i\pi_I=\pi_I\) implies that every image point of \(\Phi(\pi_I)\) is fixed by \(\alpha_i\), so \(i+1\) is not an image point. Thus its fixed set is exactly \(F_I\). If \(e\) is a nondecreasing, regressive idempotent, then its image is its fixed set \(F\), which contains 1. For every \(j\), the greatest \(f\in F\) with \(f\le j\) has \(f=e(f)\le e(j)\le j\), and \(e(j)\in F\); therefore \(e(j)=f\). Conversely, that formula defines such an idempotent for every \(F\ni1\). This proves the bijection and the image formula.

**Gate for commutation in the quotient.** Put \(D=F\cap G\). On a gap following a common fixed point \(d\), before the next common fixed point or at the end of the chain, if one of \(F\setminus G\) and \(G\setminus F\) is absent, the corresponding retraction is constant \(d\) there and both compositions send the entire gap to \(d\). Conversely, if both exclusive colors occur, take the first exclusive point of each color and assume the first \(F\)-exclusive point precedes the first \(G\)-exclusive point \(g\). Then \(e_F e_G(g)=e_F(g)>d\), whereas \(e_G e_F(g)=d\) since there is no exclusive \(G\) point before \(g\) in that gap. The reverse order is symmetric. This rederives the known Catalan pair criterion [2].

**Lifting commutation.** In the special case \(F=F_I,G=F_J\), the common fixed points after 1 correspond to indices outside \(I\cup J\). Each nonempty following gap corresponds to one run of \(I\cup J\). The two exclusive colors correspond to membership in exactly one of \(I,J\), with the roles interchanged under the complement convention. Thus when the images commute each run \(B\) of \(I\cup J\) lies in one of \(I,J\). Elements supported on different runs commute, because every generator in one run commutes with every generator in another. On each run, one of the two parabolic factors is the full longest idempotent \(\pi_B\), which absorbs the other on either side. The absorption follows by multiplying along words in the generators of \(B\): all these generators are left and right descents of the longest element. Hence \(\pi_I\pi_J=\pi_J\pi_I=\pi_{I\cup J}\). Preservation of commutation is automatic for the homomorphism. For a pairwise-commuting family, the product of any subfamily is again idempotent and commutes with every remaining entry. Induction shows that products of subfamilies are indexed by the corresponding unions of supports; all their images and all such partial product relations are transported bijectively.

**Constructive consequence for ordered tuples.** For a fixed \(r\ge1\), process the support sets in columns of \(r\) bits, one column per generator. For each unordered pair of entries keep one of three states: no exclusive bit has occurred since the last joint zero, or an exclusive bit has occurred on a specified side. Two zeros reset the state; two ones leave it unchanged. Exactly one one sets or maintains the corresponding side, unless the opposite side was recorded, which rejects the column. The run criterion proves that exactly the ordered pairwise-commuting tuples are accepted. The all-zero state is initial, every reachable state accepts, and there are at most \(3^{\binom r2}\) states. If \(M\) counts accepted symbols per transition, the generating function is \(\mathbf e(I-zM)^{-1}\mathbf1\), where \(\mathbf e\) selects the initial state. Thus it is rational for every fixed \(r\) in both monoids.

For comparison, the Catalan pair series is \(1/(1-4z+2z^2)\) [2]. The exact Catalan triple series, with index shifted to the number of simple generators, is also recorded in rank-refined form in [3]. The support transfer recovers its unweighted specialization: for three entries, record each exclusive-side memory as a directed arc from that side to the other. Up to permuting the entries, the reachable arc configurations are empty, a two-out star, a two-in star and a transitive triangle. The numbers of allowable columns into each of these four orbit types form the matrix
\[
B=\begin{pmatrix}2&3&3&0\\1&2&0&2\\1&2&2&0\\1&1&0&2\end{pmatrix}.
\]
These rows follow by testing the eight sets of ones: delete arcs whose two endpoints are zeros and insert arcs from each one to each zero, rejecting if an inserted arc has a remembered opposite. The orbit sizes are \(1,3,3,6\). The empty state's generating function from \((I-zB)^{-1}\mathbf 1\) is \((1-2z^2+2z^3)/(1-8z+16z^2-12z^3+2z^4)\). This equality is a consistency check and an application of the reflection result, not a claim of distinctness for the standalone Catalan triple formula.

## Verification

The finite transfer and its four-state quotient both give initial triple counts \(1,8,46,254,1390,7592\). The accompanying standard-library `verify.py` checks Catalan/0-Hecke commutation and product matching through six generators, triple counts through five generators by explicit enumeration, and a finite recurrence certificate on the thirteen-state unweighted system. The general reflection and transfer claims are proved above independently of those finite checks.

## Relationship to prior work and limitations

The 0-Hecke/Catalan quotient, the classifications of idempotents, and the pair criterion in the Catalan monoid are established [1,2,4,5]. The Catalan triple specialization appears identically in [3], which gives substantially finer rank information. The finite-automaton argument is a constructive consequence of the pair language. The structural contribution here is the lifting of that language across a noninjective quotient, identifying *all* commuting idempotent configurations and their product operations. The known bijection on idempotents alone does not give that lifting because products of noncommuting idempotents need not be idempotent. The listed sources do not establish historical priority for any of the overlapping exact counts. No claim is made about maximal cliques or small closed-form denominators in higher arity.

## References

1. T. Denton, F. Hivert, A. Schilling and N. M. Thiéry, *On the Representation Theory of Finite J-Trivial Monoids*, [arXiv:1010.3455](https://arxiv.org/abs/1010.3455), §2.5 and Example 3.9.
2. *Common-fixed-point compatibility and product-fiber factorization for Catalan monoid idempotents*, [record 06ff39bf0d33](https://github.com/Resultary/2026/blob/main/2026/10/18/SCOPE-common-fixed-point-compatibility-and-product-fiber-factorization--06ff39bf0d33/RESULT.md), Finding.
3. *Quartic triple-commutation law and joint-rank transfer for Catalan monoids*, [record 494cdd8f9928](https://github.com/Resultary/2026/blob/main/2026/11/22/SCOPE-quartic-triple-commutation-law-and-joint-rank-transfer-for-catal--494cdd8f9928/RESULT.md), Finding.
4. O. Ganyushkin and V. Mazorchuk, *On Kiselman Quotients of 0-Hecke Monoids*, [arXiv:1006.0316](https://arxiv.org/abs/1006.0316), Theorem 1.
5. T. Denton, *Algebraic and Affine Pattern Avoidance*, [arXiv:1303.3767](https://arxiv.org/abs/1303.3767), introduction and Theorem 4.2.

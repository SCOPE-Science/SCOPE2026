# Endomorphism-rank rigidity for finite Boolean cascades with nonsingleton levels

## Finding
Let \(h\ge 2\), and let \(P=A_1\oplus\cdots\oplus A_h\) be an ordinal sum of pairwise disjoint antichains, ordered so that points in \(A_i\) are below points in \(A_j\) exactly when \(i<j\). Write \(n_i=|A_i|\ge2\) and let \(H=\operatorname{Up}(P)\) be the finite Heyting algebra of all upsets.

**Normal-form theorem.** Every Heyting endomorphism \(\Phi:H\to H\) is uniquely the inverse-image operator \(f^{-1}\) of exactly one map of the following two types:

1. **Level-preserving type:** \(f|_{A_1}:A_1\to A_1\) is arbitrary, whereas \(f|_{A_i}\) is a permutation of \(A_i\) for each \(2\le i\le h\).
2. **Initial-collapse type:** for a unique \(j\in\{2,\ldots,h\}\) and a point \(c\in A_j\), \(f(x)=c\) on \(A_1\cup\cdots\cup A_j\), whereas \(f|_{A_i}\) is a permutation of \(A_i\) for each \(i>j\).

In particular, the complete endomorphism count is
\[
|\operatorname{End}(H)|=n_1^{n_1}\prod_{i=2}^h n_i!+\sum_{j=2}^h n_j\prod_{i=j+1}^h n_i!.
\]
Empty products are one. The distinct possible cardinalities of endomorphism images, together with their full multiplicities, are as follows:

* For \(1\le r\le n_1\), the image size is
\[
R_r=1+(2^r-1)+\sum_{i=2}^h(2^{n_i}-1),
\]
with multiplicity
\[
M_r=\binom{n_1}{r}\,r!\,\left\{\begin{matrix}n_1\\r\end{matrix}\right\}\prod_{i=2}^h n_i!,
\]
where the braces denote a Stirling number of the second kind.
* For \(2\le j\le h\), the image size is
\[
Q_j=2+\sum_{i=j+1}^h(2^{n_i}-1),
\]
with multiplicity
\[
N_j=n_j\prod_{i=j+1}^h n_i!.
\]
These image sizes are pairwise distinct across the stated families. Moreover, the number of idempotent Heyting endomorphisms is
\[
\boxed{\sum_{r=1}^{n_1}\binom{n_1}{r}r^{n_1-r}+\sum_{j=2}^h n_j.}
\]
At image size \(R_r\), precisely \(\binom{n_1}{r}r^{n_1-r}\) of the endomorphisms are idempotent. At image size \(Q_j\), precisely \(n_j\) are idempotent. Thus this is also a rank-resolved classification of retractions.

## Assumptions and scope
The poset \(P\) has at least two levels, each containing at least two incomparable points. The carrier points are distinguished when counting maps. An upset is a subset \(U\subseteq P\) satisfying \(x\in U\) and \(x\le y\Rightarrow y\in U\). The operations of \(H\) are \(\cap\), \(\cup\), \(\varnothing\), \(P\), and implication
\[
U\to V=\{x\in P:\uparrow x\cap U\subseteq V\},\qquad \uparrow x=\{y\in P:x\le y\}.
\]
An endomorphism preserves all these operations. Its **image size** is the cardinality of \(\{\Phi(U):U\in H\}\), not the size of the image of \(f\) on worlds. Idempotence means \(\Phi^2=\Phi\).

The nonsingleton hypothesis matters. For the three-element chain \(a<b<c\), the map \(a\mapsto b\), \(b\mapsto c\), \(c\mapsto c\) satisfies the bounded-morphism condition but shifts levels, so the theorem would fail if singleton levels were admitted. No assertion about arbitrary finite Heyting algebras or about all order-preserving poset maps is made.

## Proof
**1. Finite Esakia duality.** A map \(f:P\to P\) defines a Heyting endomorphism \(f^{-1}:U\mapsto f^{-1}(U)\) precisely when it is a bounded morphism, meaning
\[
\tag{1}f(\uparrow x)=\uparrow f(x)\quad\text{for all }x\in P.
\]
This is finite Esakia duality [1, Theorem 2.6]. Explicitly, equation (1) implies order preservation and the implication identity \(f^{-1}(U\to V)=f^{-1}(U)\to f^{-1}(V)\): the latter equivalence at \(x\) follows by substituting \(f(\uparrow x)=\uparrow f(x)\). Conversely, if inverse images preserve implication, the missing back-lifting condition in (1) would distinguish a principal-upset test, so (1) is necessary. Finite upsets separate distinct points; therefore different bounded morphisms yield different algebra endomorphisms.

**2. Each source antichain has a single target level.** Write \(L(y)\) for the target-level index of a point \(y\in P\). Fix \(1\le i<h\) and let \(T_i=A_{i+1}\cup\cdots\cup A_h\). For each \(x\in A_i\), (1) reads
\[
\tag{2}\{f(x)\}\cup f(T_i)=\uparrow f(x).
\]
Suppose two points \(x,y\in A_i\) have \(L(f(x))=k<\ell=L(f(y))\). Every point of \(T_i\) lies above both \(x\) and \(y\), so \(f(T_i)\subseteq\uparrow f(y)\). But by (2) for \(x\), the set \(f(T_i)\) must contain all of \(A_\ell\), since \(\ell>k\). Its intersection with \(A_\ell\) is therefore all of \(A_\ell\). On the other hand, \(\uparrow f(y)\cap A_\ell=\{f(y)\}\). This contradicts \(n_\ell\ge2\). The same conclusion is obvious at the maximal source level, since images of maximal points under (1) are maximal. Thus each \(A_i\) maps wholly to one target level, say \(\ell_i\), and \(\ell_h=h\).

Order preservation forces \(\ell_1\le\cdots\le\ell_h\). Let \(j=\ell_1\). The image \(f(P)\) is an upset by (1). In particular \(f(P)\) contains every point of every level \(A_k\) with \(k>j\), and the sequence \(\ell_1,\ldots,\ell_h\) visits each such \(k\).

**3. No target level above the first may be visited twice.** If \(\ell_i=\ell_s=k\) for \(i<s\), every point of \(A_i\) is below every point of \(A_s\). Their images lie in the same antichain \(A_k\); order preservation makes them equal. Consequently all images in \(f(A_i)\cup f(A_s)\) coincide. Monotonicity of the level indices means all source levels mapping into \(A_k\) form a consecutive interval, whose union must therefore have a singleton image. If \(k>j\), however, the upset property gives \(f(P)\cap A_k=A_k\), containing at least two points: contradiction.

It follows that levels \(j+1,\ldots,h\) are each visited exactly once. Since there are \(h-j\) of them and the source has \(h\) levels, monotonicity of \(\ell_i\) forces
\[
\ell_1=\cdots=\ell_j=j,\qquad \ell_i=i\text{ for }i>j.
\]
If \(j=1\), the first level maps arbitrarily into itself. Each higher level is the only source of the entire target level and hence maps bijectively. If \(j>1\), the first \(j\) source levels all map into the same target antichain; cross-level comparability forces their images to be a single common point \(c\in A_j\). Every higher level again maps bijectively. This proves exhaustiveness and uniqueness of the two forms. Conversely, a direct check of (1) verifies both forms.

**4. Counts and endomorphism image ranks.** In the level-preserving case, there are \(n_1^{n_1}\) bottom-level maps and \(\prod_{i=2}^h n_i!\) choices above. In the initial-collapse case, choose \(j\), the point \(c\in A_j\), and permutations above \(j\), giving \(n_j\prod_{i>j}n_i!\) maps. These cases are disjoint.

Because \(f(P)\) is an upset, restriction \(U\mapsto U\cap f(P)\) maps \(\operatorname{Up}(P)\) surjectively onto \(\operatorname{Up}(f(P))\), and the inverse-image map separates those restrictions. Hence
\[
\tag{3}|\operatorname{Im}(f^{-1})|=|\operatorname{Up}(f(P))|.
\]
For an ordinal sum with level cardinalities \(m_1,\ldots,m_s\), the number of upsets is \(1+\sum_{i=1}^s(2^{m_i}-1)\): a nonempty upset has a unique least occupied level, an arbitrary nonempty subset there, and all higher levels entirely. For a level-preserving map with \(r\) different bottom images, (3) gives \(R_r\). The number of bottom transformations of image size \(r\) is \(\binom{n_1}{r}r!\left\{\begin{matrix}n_1\\r\end{matrix}\right\}\). For an initial-collapse map with index \(j\), its image poset is \(\{c\}\oplus A_{j+1}\oplus\cdots\oplus A_h\), giving \(Q_j\). Since all \(n_i\ge2\), the \(R_r\) increase strictly with \(r\); the \(Q_j\) decrease strictly with \(j\); and \(R_1>Q_2\). This proves the claimed rank distribution without collisions.

**5. Idempotents.** Faithfulness of the inverse-image representation gives \((f^{-1})^2=f^{-1}\iff f^2=f\). In the level-preserving case, all upper permutations must be identities, while a bottom idempotent transformation with \(r\) fixed image points is specified by choosing those \(r\) points and mapping each of the remaining \(n_1-r\) points to one of them. Thus its count is \(\binom{n_1}{r}r^{n_1-r}\). In the collapse case, the upper permutations must again be identities; the constant prefix fixes its selected point \(c\), leaving exactly \(n_j\) idempotents for each \(j\). This proves all formulas.

## Verification
The standalone Python 3 file `verify.py` has no third-party dependencies. Run `python3 verify.py` in the directory containing that file. It exhaustively enumerates all maps of the specified finite carriers for nine parameter vectors, directly tests (1), independently generates the normal-form maps, computes endomorphism-image ranks by acting on every upset, tests implication preservation where stated, and checks the rank/idempotent formulas. The checked parameter vectors are \((2)\), \((3)\), \((2,2)\), \((2,3)\), \((3,2)\), \((2,2,2)\), \((2,3,2)\), \((2,2,3)\), and \((3,2,2)\). The finite checks include the one-level boundary case, although the theorem focuses on at least two levels. Their combined raw map-space size is \(2{,}523{,}822\) candidate functions.

For example, at level sizes \((2,3,2)\), the four endomorphism-image cardinalities are \(2,5,12,14\), with respective multiplicities \(2,6,24,24\) and eight total idempotents.

## Relationship to prior work
Finite Esakia duality and the bounded-morphism condition are standard and explicitly supplied by Bezhanishvili, Bezhanishvili, Moraschini and Stronkowski [1, Section 2, Theorem 2.6]. The same paper [1, Section 3] situates ordinal sums of antichains as the finite duals of Boolean cascades and studies their associated varieties; it does not state this complete endomorphism normal form or image-rank formula in the sections inspected and in the article-wide text search. Bezhanishvili, Carai and Morandi [2] develop a general duality perspective rather than the present count. Neither standard duality itself nor the notion of a Boolean cascade is claimed as original.

Adams, Koubek and Sichler [3] studied endomorphism monoids of general Heyting algebras, including near-rigidity phenomena. The accessible abstract does not give the present rank-resolved finite-cascade formulas, but its complete article was not accessible and remains a priority risk.

Existing mathematical records on order-preserving mapping spaces of weak orders and on their ordinary poset retractions treat a larger/different class of maps. Those statements do not supply the additional exact back-lifting condition (1), its rigidity consequences, or the rank-resolved Heyting endomorphism count. Existing counts of embedded Heyting subalgebras for two-level examples likewise do not count all retraction maps, and do not cover the arbitrary number of nonsingleton levels treated here.

## Limitations
This is an internally checked mathematical argument, not an independent certification or a proof of absolute publication priority. Literature access did not include the body of the directly relevant 1985 Adams–Koubek–Sichler article or every older specialist article on Boolean-cascade endomorphisms; equivalent older formulas may exist. The result assumes every antichain has at least two elements. It does not classify arbitrary finite posets or arbitrary order-preserving maps, whose behaviour may differ markedly. No infinite analogue or asymptotic claim is asserted.

## References
[1] G. Bezhanishvili, N. Bezhanishvili, T. Moraschini and M. Stronkowski, *Profiniteness and representability of spectra of Heyting algebras*, first publicly posted 2021-03-03, arXiv:2103.02530, https://arxiv.org/abs/2103.02530. In particular Sections 2 and 3.

[2] G. Bezhanishvili, L. Carai and P. J. Morandi, *A frame-theoretic perspective on Esakia duality*, Algebra Universalis 84 (2023), article 30, DOI:10.1007/s00012-023-00827-3; https://air.unimi.it/handle/2434/1011749.

[3] M. E. Adams, V. Koubek and J. Sichler, *Endomorphisms and homomorphisms of Heyting algebras*, Algebra Universalis 20 (1985), 167–178, DOI:10.1007/BF01278594. Abstract-level comparison only.

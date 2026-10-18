# Exact coefficient-shape thresholds for two-set Kneser dissociation polynomials

## Finding

Let \(K(n,2)\) denote the Kneser graph whose vertices are the two-element subsets of \([n]\), with two vertices adjacent exactly when their subsets are disjoint. A *dissociation set* is a vertex subset inducing maximum degree at most one. For every integer \(n\ge4\), its complete dissociation polynomial is
\[
D_n(z)=1+\binom n2z+n\big((1+z)^{n-1}-1-(n-1)z\big)+\binom n3z^3+\binom n4\big((1+z)^6-(1+2z)^3\big).
\]
The coefficient sequence, including its nonzero endpoints, is **strictly log-concave** exactly when \(4\le n\le12\), and is **unimodal** exactly when \(n\ne14\). Thus log-concavity fails persistently from order thirteen, but unimodality fails at only one order, fourteen, and returns for every \(n\ge15\).

The complete polynomial counting *inclusion-maximal*, rather than merely maximum, dissociation sets is
\[
M_n(z)=\begin{cases}z^6,&n=4,\\nz^{n-1}+\binom n4z^6,&n\ge5.\end{cases}
\]
For \(n\ge5\), the maximal dissociation sets are exactly the \(n\) full stars and the \(\binom n4\) six-edge families supported on four base labels. In particular, the dissociation complex is pure if and only if \(n\in\{4,7\}\); for \(n\ge9\), maximal-set sizes have the gap \(7,8,\ldots,n-2\).

## Assumptions and scope

All graphs are finite, simple and unlabeled as graph types, but vertex subsets of the specified labeled Kneser graph are counted separately. We write
\[
D_n(z)=\sum_{S\subseteq V(K(n,2)),\,\Delta(K(n,2)[S])\le1}z^{|S|}=\sum_k a_{n,k}z^k.
\]
The maximal-set polynomial uses the same weights but sums only over inclusion-maximal sets. Strict log-concavity means \(a_{n,k}^2>a_{n,k-1}a_{n,k+1}\) for every internal coefficient index between nonzero endpoints. Unimodality means the coefficients first weakly increase and then weakly decrease. The statement concerns \(n\ge4\) and does not assert results about larger-subset Kneser graphs \(K(n,r)\), \(r\ge3\).

## Proof

**Configuration dichotomy.** Regard a selected vertex family as a family of two-element subsets, or edges of the complete graph on \([n]\). If all selected pairs intersect, a family of at least two members is a subfamily of a unique star, unless it contains three pairs \(\{ab,ac,bc\}\). In the latter case these three form the entire family: any further pair disjoint from none of the three is itself among these three. Indeed, after two intersecting pairs \(ab,ac\), a pair not containing \(a\) must equal \(bc\), and no fourth pair meets all three.

If the selected family contains disjoint pairs \(ab,cd\), then they are adjacent vertices of the Kneser graph. Every further selected pair must meet **both** of these pairs, since each already has its permitted one neighbor. Thus every selected pair is one of the six pairs on the four base labels \(a,b,c,d\). Conversely, these six pairs induce three disjoint edges in the Kneser graph; consequently **every** subfamily is a dissociation set. The supporting four-label set is uniquely determined by any disjoint pair contained in the selected family.

**Enumeration.** Empty and singleton intersecting families contribute \(1+\binom n2 z\). Intersecting families with at least two members contained in stars contribute
\[
n\big((1+z)^{n-1}-1-(n-1)z\big).
\]
The exceptional three-pair triangles contribute \(\binom n3z^3\). For each four-label support, select a subset of its six edges that contains at least one disjoint pair. The three Kneser-adjacent pairs form \(3K_2\), so the required generating function is
\[
(1+z)^6-(1+2z)^3.
\]
This yields the stated \(D_n\), without double counting.

**Inclusion-maximal configurations.** A proper subfamily of a star extends by an unused star edge. A triangle extends inside a four-label six-edge family. A nonintersecting family on four labels extends within its six-edge family unless already full. That full family cannot be extended: any pair using a label outside the support is disjoint from at least three of its six members. For \(n\ge5\), the full star is also inclusion-maximal because an outside pair is disjoint from \(n-3\ge2\) star members. For \(n=4\), the unique six-edge family contains every vertex. These observations prove \(M_n\) and the purity and gap assertions.

**Sharp log-concavity threshold.** Direct expansion of the closed formula for the nine orders \(n=4,5,\ldots,12\) gives the following smallest internal determinants \(\min_k(a_{n,k}^2-a_{n,k-1}a_{n,k+1})\), respectively:
\[
21,\ 55,\ 120,\ 231,\ 406,\ 666,\ 1035,\ 1540,\ 2211.
\]
Every entry is positive; these are finite exact arithmetic identities in the displayed polynomial, not statistical evidence. For \(13\le n\le21\), expansion and factorization give
\[
\begin{aligned}
a_{n,5}^2-a_{n,4}a_{n,6}&=\frac{n^2(n-3)^2(n-2)^2(n-1)^2}{86400}H_5(n),\\
H_5(n)&=n^4-88n^3+1541n^2-9020n+19950.
\end{aligned}
\]
For successive orders \(n=13,\ldots,21\), the exact values of \(H_5(n)\) are
\[
-1656,-7350,-15000,-24786,-36864,-51366,-68400,-88050,-110376,
\]
all strictly negative. For \(n\ge22\), another internal determinant is
\[
\begin{aligned}
a_{n,4}^2-a_{n,3}a_{n,5}
&=-\frac{n^2(n-3)(n-2)^2(n-1)^2}{2880}H_4(n),\\
H_4(n)&=11n^3-283n^2+921n-385.
\end{aligned}
\]
Putting \(t=n-22\ge0\) yields \(H_4(n)=11t^3+443t^2+4441t+33>0\). Hence strict log-concavity holds exactly for \(4\le n\le12\), and ordinary log-concavity also fails in all larger orders because the displayed determinants are negative.

**Isolated nonunimodality.** Exact expansion for \(4\le n\le13\) shows that each coefficient sequence is unimodal, with unique mode index \(3\) for orders \(4,5,6\) and mode index \(4\) for orders \(7,8,\ldots,13\). At \(n=14\), three consecutive coefficients are
\[
a_{14,4}=25025,\qquad a_{14,5}=24024,\qquad a_{14,6}=25025,
\]
so unimodality fails. For every \(n\ge15\), the first two coefficients satisfy \(a_{n,1}>a_{n,0}\), while direct subtraction gives the following positive differences:
\[
\begin{aligned}
a_{n,2}-a_{n,1}&=\frac{n(n-3)(n-1)(n+2)}8,\\
a_{n,3}-a_{n,2}&=\frac{n(n-2)(n-1)(13n-47)}{24},\\
a_{n,4}-a_{n,3}&=\frac{n(n-2)(n-1)(n^2-8n+11)}{24},\\
a_{n,5}-a_{n,4}&=\frac{n(n-3)(n-2)(n-1)(n^2-14n-5)}{120},\\
a_{n,6}-a_{n,5}&=\frac{n(n-3)(n-2)(n-1)(n^3-21n^2+128n-390)}{720},\\
a_{n,7}-a_{n,6}&=\frac{n(n-3)(n-2)(n-1)(n^4-29n^3+284n^2-1156n+1470)}{5040}.
\end{aligned}
\]
Each factor not manifestly positive becomes a polynomial with strictly positive coefficients upon replacing \(n\) by \(15+t\), \(t\ge0\); in particular the last two large factors become \(t^3+24t^2+173t+180\) and \(t^4+31t^3+329t^2+1289t+780\). For \(k\ge7\), all coefficients have the ordinary binomial form \(a_{n,k}=n\binom{n-1}{k}\); their tail is unimodal. Therefore the full coefficient sequence is unimodal for every \(n\ge15\).

## Verification

The standalone `verify.py` constructs adjacency from disjoint two-subsets. It tests the dissociation condition by hereditary subset recursion and identifies inclusion-maximal sets by all possible one-vertex extensions; neither decision uses the theorem's structural classification. It exhaustively checks all \(2^{\binom n2}\) vertex subsets for \(n=4,5,6,7\), totaling \(2{,}131{,}008\) subsets, and checks the predicted coefficient-shape results by exact integer arithmetic for \(4\le n\le500\). It prints the output stored in `verification_output.txt`. Finite checks are corroboration; the all-order claims are proved above.

## Relationship to prior work

Brešar and Dravec, *On the dissociation number of Kneser graphs*, arXiv:2108.10801v1 (first public 2021-08-24), proved \(\operatorname{diss}(K(n,2))=\max\{n-1,6\}\) for \(n\ge5\) and in Proposition 2.1 used the same key local observation that any nonindependent dissociation set is supported on four base labels. **Neither the scalar dissociation number nor this four-label localization is claimed as new here.** The additional assertions are the full all-cardinality enumeration, complete maximal-set enumerator, and exact unimodality/log-concavity transitions.

Tu, Li and Du, *Maximal and Maximum Dissociation Sets in General and Triangle-Free Graphs* (arXiv:2103.01402v1), proved general extremal bounds on numbers of maximal dissociation sets, not this exact family-specific enumerator. Tu, Xiao and Lang, *Counting the number of dissociation sets in cubic graphs* (AIMS Mathematics, 2023, DOI:10.3934/math.2023507), proved a universal weighted extremal bound for cubic graphs. It applies to the Petersen member but does not determine the all-order family polynomial. Neither inspected source gives the coefficient transition theorem.

## Limitations

The new enumeration is an explicit consequence of a structural decomposition closely related to Brešar–Dravec's proof; it must not be read as a priority claim for that decomposition. The displayed finite arithmetic table is exhaustive only in the stated finite range; infinite-range shape claims use the polynomial factorizations and positive-coefficient arguments above. Literature searching and full-text examination cannot establish global uniqueness; unindexed equivalents or independent discovery remain possible. No independent scientific audit has been performed.

## References

1. B. Brešar and T. Dravec, *On the dissociation number of Kneser graphs*, arXiv:2108.10801v1, publicly posted 2021-08-24. https://arxiv.org/pdf/2108.10801
2. J. Tu, Y. Li and J. Du, *Maximal and Maximum Dissociation Sets in General and Triangle-Free Graphs*, arXiv:2103.01402v1 (2021). https://arxiv.org/pdf/2103.01402
3. J. Tu, J. Xiao and R. Lang, *Counting the number of dissociation sets in cubic graphs*, AIMS Mathematics 8 (2023), 10021–10032, DOI:10.3934/math.2023507. https://www.aimspress.com/aimspress-data/math/2023/5/PDF/math-08-05-507.pdf

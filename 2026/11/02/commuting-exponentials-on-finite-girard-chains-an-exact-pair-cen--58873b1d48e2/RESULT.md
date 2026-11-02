# Commuting exponentials on finite Girard chains: an exact pair census

## Finding
Let \(A\) be any finite bounded commutative residuated chain with multiplicative unit \(1\), least element \(0\), and product \(\odot\). An **exponential** is a unary operation \(!\) satisfying
\[
!1=1,\quad !a\le a\wedge1,\quad !a\odot !b=!(a\wedge b),\quad !!a=!a.
\]
Set \(E=\{e\in A:0\le e\le1,\ e\odot e=e\}\), and write \(h=|E|\) and \(r=h-2\). Then:

1. Exponentials correspond bijectively to subsets \(S\subseteq E\) containing \(0,1\), by \(!_{S}a=\max\{s\in S:s\le a\wedge1\}\). There are exactly \(2^r\) exponentials.
2. Two exponentials \(!_{S},!_{T}\) commute under functional composition precisely when, between every two consecutive elements of \(S\cap T\), there are no elements of **both** \(S\setminus T\) and \(T\setminus S\). When they commute, their composition equals \(!_{S\cap T}\), hence is again an exponential.
3. The number \(c_r\) of **ordered** commuting pairs is given by
\[
c_0=1,\qquad c_1=4,\qquad c_r=4c_{r-1}-2c_{r-2}\ (r\ge2),
\]
\[
\sum_{r\ge0}c_r z^r=\frac1{1-4z+2z^2},\qquad
c_r=\frac{(2+\sqrt2)^{r+1}-(2-\sqrt2)^{r+1}}{2\sqrt2}.
\]
Thus there are exactly \(4^r-c_r\) noncommuting ordered pairs.

For the standard \(n\)-element nilpotent-minimum chain, \(h=\lfloor n/2\rfloor+1\), so **six elements are the sharp first size admitting noncommuting exponential operations**. At six elements, precisely two of the sixteen ordered pairs fail to commute.

## Assumptions and scope
A finite **bounded commutative residuated chain** is a finite bounded lattice whose order is linear, with a commutative monoid \((A,\odot,1)\) for which \(a\odot b\le c\) iff \(b\le a\to c\). In particular, \(\odot\) is order-preserving, and \(0\) is absorbing. No integrality assumption \(1=\max A\) is made. Every finite Girard chain is covered because it is such a residuated chain with an additional involutive dualizer. The theorem concerns unary operations obeying exactly the four displayed exponential axioms; additional unrelated modalities are not assumed.

For the concrete nilpotent-minimum chain write its carrier as \(\{0,1,\ldots,n-1\}\), with unit \(n-1\), and \(i\odot j=0\) if \(i+j\le n-1\), otherwise \(i\odot j=\min(i,j)\). Its residual exists by monotonicity and it has involution \(i\mapsto(n-1-i)\), so it is a finite Girard chain.

## Proof
**Step 1 (classification).** Let \(!\) obey the four axioms. If \(a\le b\), then \(a\wedge b=a\), hence
\(!a=!a\odot !b\le1\odot !b=!b\), using \(!a\le1\). Thus \(!\) is monotone. By idempotence, its image \(S\) consists exactly of its fixed points. By \(!!a=!a\), the images are fixed; by \(!a\odot!a=!a\), they are multiplicative idempotents not exceeding \(1\). Since \(!0\le0\), \(!0=0\), and \(!1=1\), we have \(\{0,1\}\subseteq S\subseteq E\). For every \(s\in S\) with \(s\le a\wedge1\), monotonicity gives \(s=!s\le!a\); meanwhile \(!a\in S\) and \(!a\le a\wedge1\). Hence \(!a\) is exactly the largest such \(s\).

Conversely fix any \(S\subseteq E\) containing \(0,1\), and define \(!_{S}\) by that largest element. Floors are monotone, deflationary and idempotent, and fix \(1\). For idempotents \(e\le f\le1\), monotonicity of product gives
\[
e=e\odot e\le e\odot f\le e\odot1=e,
\]
so \(e\odot f=e\) and multiplication restricted to \(E\) equals minimum. It follows that \(!_{S}a\odot!_{S}b=\min(!_{S}a,!_{S}b)=!_{S}(a\wedge b)\). Thus all four axioms hold, giving the claimed bijection.

**Step 2 (commutation).** Put \(f=!_{S}\), \(g=!_{T}\). If they commute, \(f\circ g\) is an idempotent, monotone, deflationary map whose fixed points are exactly \(S\cap T\): a fixed point of the composition is \(x=f(g(x))\le g(x)\le x\), forcing \(g(x)=x=f(x)\). Such a map on a chain is necessarily the floor onto its fixed points. Thus commuting forces \(f\circ g=g\circ f=!_{S\cap T}\).

Let \(u<v\) be successive points of \(S\cap T\). If the open interval \((u,v)\) contains points of both \(S\setminus T\) and \(T\setminus S\), choose one from each and suppose first that an \(S\)-only point lies below a \(T\)-only point \(t\). Then \(f(g(t))=f(t)\) lies in \(S\setminus T\), while \(g(f(t))\in T\), proving failure of commutation. The reverse order gives the symmetric argument. Conversely, if each interval contains points from at most one exclusive subset, then in that interval each composition maps every argument strictly below \(v\) to \(u\) (and fixes \(v\)). This proves the criterion and the identity \(f\circ g=!_{S\cap T}\) under commutation.

**Step 3 (enumeration).** The \(r\) interior points of \(E\) are independently marked by one of four statuses: neither subset, only \(S\), only \(T\), or both. The endpoints are always marked both. Between consecutive both-marked points, commutation allows neither-marked points and one of the two exclusive types, but never both exclusive types. For a gap with \(\ell\) interior points, there are \(g_\ell=2^{\ell+1}-1\) admissible markings: \(2^\ell\) with no \(T\)-only mark plus \(2^\ell\) with no \(S\)-only mark, minus the single all-neither marking. With \(G(z)=\sum_{\ell\ge0}g_\ell z^\ell=1/((1-z)(1-2z))\), a word is a sequence of such gaps separated by both-marks. Its generating function is \(G(z)/(1-zG(z))=1/(1-4z+2z^2)\). Coefficient extraction gives the recurrence and the closed formula. There are \((2^r)^2=4^r\) total ordered pairs.

**Step 4 (sharp concrete boundary).** In the nilpotent-minimum chain a nonzero element is idempotent exactly when its index is strictly greater than half the maximal index; hence \(E=\{0\}\cup\{i:2i>n-1\}\), so \(h=\lfloor n/2\rfloor+1\). For \(n\le5\), \(r\le1\) and all pairs commute. At \(n=6\), take \(S=\{0,4,5\}\) and \(T=\{0,3,5\}\). At input \(4\), \(!_{S}(!_{T}(4))=0\), but \(!_{T}(!_{S}(4))=3\), so they do not commute. Here \(r=2\), so \(c_2=14\) out of sixteen pairs commute.

## Verification
Run `python3 checker.py` using Python's standard library. The checker independently enumerates every unary function for the nilpotent-minimum chains of orders \(2\) through \(6\) and tests the four original axioms, comparing accepted maps to the floor-subset classification. It checks the monoid, residual and involution identities. For all abstract ordered idempotent sets of sizes \(2\) through \(9\), it exhaustively compares each pair's commutation with the gap criterion and the recurrence. It reports `ALL_CHECKS_OK functions_examined=50068 commuting_counts=[1, 4, 14, 48, 164, 560, 1912, 6528]`. Finite enumeration checks the implementation and small cases; the proof above establishes the theorem for all finite sizes.

## Relationship to prior work
Aglianò and Nedeljkovic formulate Girard algebra semantics of linear logic and the four girale exponential axioms in arXiv:2610.16804 (initially public October 12, 2026). Their paper develops structural results on Girard subvarieties and finite examples, not the mutual commutation law or its pair census. Kruml and Paseka's 2019 work studies quantic nuclei and conuclei of Girard posets, including fixed-point closure under multiplication (Lemma 3.3); that general theory motivates the fixed-point representation but does not supply the chain-specific two-operator criterion or recurrence. The exact census and the nilpotent-minimum threshold are the additional results claimed here. No assertion of uniqueness in the complete historical literature is made.

## Limitations
This is a finite-chain theorem for the displayed exponential axioms, not a classification of exponentials on arbitrary non-chain Girard algebras. In general noncommuting compositions need not themselves satisfy the exponential axioms. The sequence \(1,4,14,48,\ldots\) may have prior purely combinatorial appearances, which would not by itself establish the stated Girard-chain application; historically equivalent applications remain possible. No machine-verified infinite proof has been performed.

## References
1. P. Aglianò and M. Nedeljkovic, *Linear Logic via algebra I: Girard algebras*, arXiv:2610.16804, first submitted October 12, 2026, https://arxiv.org/abs/2610.16804.
2. D. Kruml and J. Paseka, *Nuclei and conuclei on Girard posets*, EUSFLAT 2019, pp. 289–296, DOI:10.2991/eusflat-19.2019.42, https://download.atlantis-press.com/article/125914812.pdf.

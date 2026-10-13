# Automorphism-orbit spectra of subalgebras in length-six truncated polynomial rings

## Finding
Let \(k=\mathbb F_q\) and \(A=k[t]/(t^6)\). The full group \(G=\operatorname{Aut}_{k\text{-alg}}(A)\) has exactly
\[
\#(\operatorname{Sub}_{k,1}(A)/G)=
\begin{cases}
12,&\operatorname{char} k>3,\\
18,&\operatorname{char} k=3,\\
16+\gcd(3,q-1),&\operatorname{char} k=2.
\end{cases}
\]
Here \(\operatorname{Sub}_{k,1}(A)\) means unital \(k\)-subalgebras, and \(G\) acts by algebra substitution. In characteristic two the number is \(17\) for an odd extension degree and \(19\) for an even extension degree. Every orbit size and its multiplicity are specified below. The known total cardinality \(6+3q+3q^2\) is recalled only as a consistency check, not a novel claim.

## Assumptions and scope
There is no restriction on the finite field beyond \(q\) being a prime power. All subalgebras contain the specified copy of \(k\) and the unit; all automorphisms fix \(k\) pointwise. Each subalgebra is \(k\oplus W\) for a multiplication-closed vector subspace \(W\subset (t)\). An exponent label, such as \((2,4)\), is the set of leading powers in the reduced echelon basis of \(W\) relative to \(t,t^2,t^3,t^4,t^5\). In the following table \(u,v\) range independently over \(k\), and angle brackets denote \(k\)-linear span of the displayed vectors.

| Family | Leading powers | Radical part \(W\) | Number of subalgebras |
| --- | --- | --- | --- |
| \(F_0\) | \(\varnothing\) | \(0\) | \(1\) |
| \(F_1\) | \((1,2,3,4,5)\) | \((t)\) | \(1\) |
| \(F_2\) | \((2,3,4,5)\) | \((t^2)\) | \(1\) |
| \(F_3\) | \((3,4,5)\) | \((t^3)\) | \(1\) |
| \(F_4\) | \((4,5)\) | \((t^4)\) | \(1\) |
| \(F_5\) | \((5)\) | \((t^5)\) | \(1\) |
| \(P_{24}\) | \((2,4)\) | \(\langle t^2+ut^3+vt^5,\ t^4+2ut^5\rangle\) | \(q^2\) |
| \(P_{245}\) | \((2,4,5)\) | \(\langle t^2+ut^3,\ t^4,\ t^5\rangle\) | \(q\) |
| \(P_3\) | \((3)\) | \(\langle t^3+ut^4+vt^5\rangle\) | \(q^2\) |
| \(P_{34}\) | \((3,4)\) | \(\langle t^3+ut^5,\ t^4+vt^5\rangle\) | \(q^2\) |
| \(P_{35}\) | \((3,5)\) | \(\langle t^3+ut^4,\ t^5\rangle\) | \(q\) |
| \(P_4\) | \((4)\) | \(\langle t^4+ut^5\rangle\) | \(q\) |

**Complete orbit-size spectra.** Each bracketed list is a multiset of orbit sizes *within that family*. The six \(F_i\) families each contribute one orbit of size one in all characteristics. Write \(g=\gcd(3,q-1)\).

| Family | \(\operatorname{char} k>3\) | \(\operatorname{char} k=3\) | \(\operatorname{char} k=2\) |
| --- | --- | --- | --- |
| \(P_{24}\) | \([q^2]\) | \([q^2]\) | \([1,\ \underbrace{(q-1)/g,\ldots,(q-1)/g}_{g\text{ terms}},\ q(q-1)]\) |
| \(P_{245}\) | \([q]\) | \([q]\) | \([1,q-1]\) |
| \(P_3\) | \([q^2]\) | \([1,(q-1)/2,(q-1)/2,q(q-1)]\) | \([q^2]\) |
| \(P_{34}\) | \([q^2]\) | \([q,q(q-1)/2,q(q-1)/2]\) | \([q,q(q-1)]\) |
| \(P_{35}\) | \([q]\) | \([1,q-1]\) | \([q]\) |
| \(P_4\) | \([q]\) | \([q]\) | \([1,q-1]\) |

The occurrence of the two equal-size orbit entries is intentional: they are distinguished square classes. If \(q=2\), entries \(q-1=1\) describe distinct singleton orbits, not merged orbits.

## Proof
Write an arbitrary automorphism uniquely as
\[
\phi(t)=at+bt^2+ct^3+dt^4+et^5,
\qquad a\in k^\times,\quad b,c,d,e\in k.
\]
Every such substitution is invertible by successive solution in the degree filtration. In particular, \(|G|=(q-1)q^4\). The radical filtration is characteristic, so its reduced-echelon leading-degree sets are preserved under \(G\).

For subalgebra completeness, let \(W\) be the radical part and choose its monic reduced-echelon basis. If degree one occurs, repeated powers force all five radical degrees. Otherwise closure under products implies that the leading-degree set in \(\{2,3,4,5\}\) is stable under sums less than six. The only possible leading-degree sets are exactly the remaining eleven sets displayed in the first table. Within the set \((2,4)\), squaring \(t^2+ut^3+vt^5\) forces the second vector \(t^4+2ut^5\). For all other sets, reduced-echelon parameters have the displayed independent ranges, and products vanish or stay in the span. This gives all subalgebras uniquely. This explicit enumeration (also appearing in later literature) yields \(6+3q+3q^2\), and serves here only to define the group action's complete domain.

The action is calculated by substituting \(\phi(t)\) into each reduced-echelon basis, dividing each leading coefficient by its nonzero power of \(a\), and eliminating higher pivot columns. For \(P_{24}\), the new parameters obey
\[
U=au+2b/a,\qquad
T=b^2/a^2+2c/a+3ub,
\]
\[
V=a^3v+2d/a+2bc/a^2+3uc+3ub^2/a,
\qquad (u',v')=(U,V-2UT).
\]
The single-parameter families have \(u'=au+2b/a\) for \(P_{245}\), \(u'=au+3b/a\) for \(P_{35}\), and \(u'=au+4b/a\) for \(P_4\). For \(P_3\), direct expansion of \(\phi(t)^3+u\phi(t)^4+v\phi(t)^5\) gives \(u'=au+3b/a\) and an expression for \(v'\) whose coefficient of \(c\) is \(3/a\). For \(P_{34}\), substitution yields \(v'=av+4b/a\) and an expression for \(u'\) whose coefficient of \(c\) is \(3/a\). Thus when the characteristic exceeds three, every parameter family is transitive, giving the column \([q^2]\) or \([q]\).

In characteristic three, the exceptional reduced actions are
\[
P_3:\quad (u',v')=(au,a^2v+ub),
\qquad
P_{34}:\quad (u',v')=(a^2u,av+b/a),
\qquad P_{35}:\quad u'=au.
\]
For \(P_3\), the zero vector, the two square classes in \(\{u=0,v\ne0\}\), and the stratum \(u\ne0\) are the four distinct orbits with sizes shown. In \(P_{34}\), the invariant \(u\) has three classes \(0\), nonzero square, nonzero nonsquare, and \(v\) ranges freely in each. The only other exceptional family is \(P_{35}\), which splits into \(u=0\) and \(u\ne0\). All remaining families are transitive.

In characteristic two, the exceptional reduced actions are
\[
P_{24}:\quad (u',v')=(au,a^3v+u(c+b^2/a)),
\quad P_{245}:\quad u'=au,
\quad P_4:\quad u'=au,
\]
\[
P_{34}:\quad (u',v')=(a^2u+c/a+b^2/a^2+bv,av).
\]
Thus \(P_{24}\) splits into \((u,v)=(0,0)\), the \(g\) nonzero cube classes at \(u=0\), and one orbit at \(u\ne0\). In \(P_{34}\), \(c\) moves \(u\) freely while \(a\) distinguishes \(v=0\) and \(v\ne0\). Each of \(P_{245}\) and \(P_4\) splits into zero versus nonzero parameters; the other two families remain transitive because the coefficients three in their triangular elimination remain invertible. The orbit sizes are the cardinalities of these explicit strata. Their sums give \(q^2\) or \(q\) for each family, and the orbit totals give \(12\), \(18\), and \(16+g\), respectively. Since \(\mathbb F_{2^e}^\times\) is cyclic of order \(2^e-1\), \(g=1\) for odd \(e\) and \(g=3\) for even \(e\). This completes the classification.

## Verification
The standalone `verify.py` constructs finite fields, all twelve parameter families, substitution generators, and full orbit traversals, checking closure and the orbit-size spectra for field sizes \(2,3,4,5,7,8\). It checks respectively \(17,18,19,12,12,17\) orbits. The independent enumeration in `verify_rref.py` walks **every** subspace of the five-dimensional nilpotent radical over field sizes \(2,3,4,5\) and tests closure under multiplication, confirming the complete parameter-list and counts. Both scripts use exact finite arithmetic. These checks corroborate but do not replace the uniform symbolic proof for all prime powers.

## Relationship to prior work
Micale's historical study of order bases for subalgebras of power-series rings provides the general context of describing subalgebras via leading exponents; its online publication date is documented as 31 August 2006. Franco Muñoz's later full-text preprint explicitly lists the **same twelve parameter families** for this algebra in Section 3.1.6 and tabulates the total number over finite fields in Section 4.2. Accordingly neither the classification of the subalgebras as sets nor their total count is asserted to be new. The present claim is their complete orbit decomposition under all substitutions fixing the coefficient field, including each orbit size and the exact arithmetic characteristic jump. Published classifications of truncated *coordinate-cross* algebras have different multiplication and do not imply this orbit decomposition.

## Limitations
This treats exactly truncation exponent six, unital coefficient-field subalgebras, and coefficient-field-linear algebra automorphisms. No claims are made for general truncation exponents, semilinear automorphisms, or arbitrary additive subrings. A historical title concerning order bases was accessed via its abstract and bibliographic page, not its entire paper. A complete search cannot exclude an equivalent orbit classification under another terminology; the finite verification cases are not an infinite proof. There is no independent external validation.

## References
1. V. Micale, *Order Bases of Subalgebras of Power Series Rings*, Communications in Algebra **31** (2003), 1359–1375, DOI: 10.1081/AGB-120017770; publicly dated online 2006-08-31, https://www.tandfonline.com/doi/abs/10.1081/AGB-120017770.
2. F. Franco Muñoz, *The existence of non-thin subalgebras of \(K[x]/x^n\) and related numerical monoids*, arXiv:1812.03576 (first posted December 2018), especially §§3.1.6, 4.2, https://arxiv.org/pdf/1812.03576.
3. J. C. Rosales and P. A. García-Sánchez, *Numerical Semigroups*, Springer, 2009; background for valuation monoids, not a source for the orbit formulas.

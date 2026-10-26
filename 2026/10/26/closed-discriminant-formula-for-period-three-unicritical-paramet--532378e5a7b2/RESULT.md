# Closed discriminant formula for period-three unicritical parameters

## Finding

For every integer \(d\ge2\), let \(f_{d,c}(z)=z^d+c\) and \(P_n(c)=f_{d,c}^{\circ n}(0)\). The period-three dynatomic parameter polynomial is
\[
G_d(c)=\frac{P_3(c)}{P_1(c)}
=c^{d-1}(c^{d-1}+1)^d+1,
\]
a monic polynomial of degree \(N=d^2-1\). Its exact polynomial discriminant is
\[
\boxed{\operatorname{Disc}_c(G_d)=(-1)^{d+1}(d-1)^{d^2-1}
\big((d+1)^{d+1}-d^d\big)^{d-1}.}
\]
Consequently, for every prime \(p\),
\[
v_p(\operatorname{Disc}(G_d))
=(d^2-1)v_p(d-1)
+(d-1)v_p\big((d+1)^{d+1}-d^d\big).
\]
Thus \(p\) divides this discriminant exactly when it divides \(d-1\) or \((d+1)^{d+1}-d^d\).

## Assumptions and scope

The degree \(d\) is any integer at least \(2\), and \(c\) is an indeterminate. The discriminant is the usual polynomial discriminant over \(\mathbb Z\), not a number-field discriminant. In characteristic zero, the roots of \(G_d\) are exactly the parameters for which the critical point \(0\) has exact period \(3\) under \(f_{d,c}\), by the dynatomic construction of Hutz and Towsley. Their finite-characteristic criterion interprets prime divisors of this polynomial discriminant as failures of transversality for the corresponding period-three parameter problem. The present claim computes the discriminant explicitly; it does not reprove their general criterion.

## Proof

Write \(m=d-1\), \(n=d+1\), and
\[
h_d(t)=t(t+1)^d+1,\qquad
R_d=(d+1)^{d+1}-d^d.
\]
Direct iteration gives
\[
P_1(c)=c,\quad P_2(c)=c(c^{d-1}+1),\quad
P_3(c)=c^d(c^{d-1}+1)^d+c,
\]
so \(G_d(c)=h_d(c^m)\) and \(\deg G_d=N=mn=d^2-1\).

Differentiating,
\[
h_d'(t)=(t+1)^{d-1}((d+1)t+1).
\]
Also \(h_d(-1)=1\) and
\[
h_d\!\left(-\frac1{d+1}\right)
=1-\frac{d^d}{(d+1)^{d+1}}.
\]
The product definition of the resultant therefore yields
\[
\operatorname{Res}(h_d,t+1)=(-1)^{d+1},
\]
\[
\operatorname{Res}(h_d,(d+1)t+1)=(-1)^{d+1}R_d.
\]
By multiplicativity of the resultant,
\[
\operatorname{Res}(h_d,h_d')
=(-1)^{(d+1)(d-1)}(-1)^{d+1}R_d=R_d,
\]
because \(d(d+1)\) is even. Since \(h_d\) is monic of degree \(n=d+1\),
\[
\operatorname{Disc}(h_d)=(-1)^{d(d+1)/2}R_d.
\]

Now \(G_d(c)=h_d(c^m)\), \(G_d(0)=1\), and
\[
G_d'(c)=m c^{m-1}h_d'(c^m).
\]
The roots of \(G_d\) are the \(m\)-th roots of the roots of \(h_d\), counted with multiplicity. Applying the product definition and multiplicativity of the resultant gives
\[
\operatorname{Res}(G_d,h_d'(c^m))
=\operatorname{Res}(h_d,h_d')^m=R_d^m
\]
and
\[
\operatorname{Res}(G_d,m c^{m-1})
=m^N(-1)^{N(m-1)}G_d(0)^{m-1}
=m^N(-1)^{N(m-1)}.
\]
Hence
\[
\operatorname{Res}(G_d,G_d')
=m^N(-1)^{N(m-1)}R_d^m.
\]
Using \(\operatorname{Disc}(G_d)=(-1)^{N(N-1)/2}\operatorname{Res}(G_d,G_d')\), the total sign exponent
\[
\frac{N(N-1)}2+N(m-1)
\]
has parity \(d+1\): if \(d\) is odd then \(N\) is even; if \(d\) is even then \(N\) is odd and \((N-1)/2+(m-1)\) is odd. Substituting \(m=d-1\) proves the displayed formula. Since \(d-1>0\) and \(R_d>0\), the discriminant is nonzero. Taking \(p\)-adic valuations gives the stated exact valuation formula.

## Verification

The proof is symbolic and holds for every integer \(d\ge2\). The accompanying `verify.py` uses only the Python standard library to compute exact Sylvester determinants for \(d=2,\ldots,7\) with fraction-free Bareiss elimination and compares them with the closed formula. All seven exact checks pass. The cases \(d=5\) and \(d=7\) reproduce the factorizations reported by Hutz and Towsley for their period-three discriminants:
\[
d=5:\quad 2^{48}\,101^4\,431^4,
\qquad
d=7:\quad 2^{48}\,3^{54}\,19^{12}\,14731^6.
\]
These finite checks are consistency checks only; the proof above establishes the formula for all \(d\ge2\).

## Relationship to prior work

Hutz and Towsley, *Misiurewicz Points for Polynomial Maps and Transversality*, define the exact-period parameter polynomials \(G_d(0,n)\), study \(D_d(0,n)=\operatorname{Disc}(G_d(0,n))\), prove a finite-characteristic criterion linking \(p\mid D_d(0,n)\) to failure of transversality, and give explicit \(n=3\) factorizations for \(d=5\) and \(d=7\). In the inspected full text, they do not state the general closed formula above.

Buff, *On postcritically finite unicritical polynomials*, studies the equivalent period-three polynomial \(h_d(t)=t(t+1)^d+1\) in a transformed parameterization and proves irreducibility results; the inspected text does not give its exact integer discriminant. Goksel, *A note on Misiurewicz polynomials*, studies irreducibility and arithmetic of Misiurewicz polynomials, including the same exact-period family, but does not state the displayed discriminant formula. The present contribution is limited to the explicit period-three discriminant and its valuation consequence. Searches for the exact formula returned no directly covering statement. The composition/resultant method is classical, so an unindexed prior derivation remains possible.

## Limitations

This formula treats only exact period \(3\) for the critical point in the unicritical family \(z^d+c\). It does not give discriminants for periods \(n\ge4\), strictly preperiodic portraits, irreducibility, Galois groups, or number-field discriminants. The bad-prime interpretation uses the previously published transversality criterion rather than establishing a new general criterion. The literature comparison is bounded and does not certify absolute priority. Independent audit has not been performed.

## References

1. B. Hutz and A. Towsley, “Misiurewicz Points for Polynomial Maps and Transversality,” *New York Journal of Mathematics* **21** (2015), 297–319; first public version arXiv:1309.4048v1, posted 2013-09-16. See the unicritical exact-period construction and the section on failure of transversality over finite fields. https://arxiv.org/abs/1309.4048
2. X. Buff, “On postcritically finite unicritical polynomials,” *New York Journal of Mathematics* **24** (2018), 1111–1122. https://nyjm.albany.edu/j/2018/24-54p.pdf
3. V. Goksel, “A note on Misiurewicz polynomials,” *Journal de Théorie des Nombres de Bordeaux* **32** (2020), no. 2, 373–385, DOI 10.5802/jtnb.1126. https://www.numdam.org/item/JTNB_2020__32_2_373_0.pdf

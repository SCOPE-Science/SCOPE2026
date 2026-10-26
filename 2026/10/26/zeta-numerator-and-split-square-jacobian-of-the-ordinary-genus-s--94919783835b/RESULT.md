# Zeta numerator and split-square Jacobian of the ordinary genus-six Artin–Schreier boundary curve

## Finding

Let \(X\) be the smooth projective model over \(\mathbb F_3\) of
\[
y^3-y=x+\frac{1}{x^3-x}.
\]
Its zeta function is \(Z(X,T)=P_X(T)/((1-T)(1-3T))\), where
\[
\boxed{P_X(T)=1+16T^3+118T^6+432T^9+729T^{12}
=(1-T+3T^2)^2(1+T-2T^2+3T^3+9T^4)^2.}
\]
Consequently its Jacobian is \(\mathbb F_3\)-isogenous to
\[
\boxed{\operatorname{Jac}(X)\sim_{\mathbb F_3}E^2\times A^2,}
\]
where \(E\) is the ordinary elliptic isogeny class with Frobenius polynomial \(U^2-U+3\), and \(A\) is an ordinary, simple **over \(\mathbb F_3\)** abelian surface with Frobenius polynomial \(U^4+U^3-2U^2+3U+9\). In particular,
\[
\#\operatorname{Jac}(X)(\mathbb F_3)=P_X(1)=1296.
\]
For all positive integers \(r\) not divisible by \(3\), one also has \(\#X(\mathbb F_{3^r})=3^r+1\).

## Assumptions and scope

All point counts and isogenies are over the indicated finite fields. The smooth projective model exists because the equation is a separable Artin–Schreier extension. The rational function has exactly four distinct simple poles on \(\mathbb P^1_{\mathbb F_3}\), at \(0,1,-1,\infty\), and the cover is totally ramified with exactly one rational point above each pole. The standard genus formula for an Artin–Schreier cover with simple poles gives
\[
g(X)=\frac{3-1}{2}\bigl(4(1+1)-2\bigr)=6.
\]
The result concerns this canonical coefficient-one model over \(\mathbb F_3\). It does not assert the same Frobenius polynomial for every coefficient or for every arithmetic form.

## Proof

**The prime-to-three extension counts.** Write \(f(x)=x+1/(x^3-x)\). For \(t\in\mathbb F_3\), the characteristic-three identity \((x+t)^3-(x+t)=x^3-x\) shows that \(f(x+1)=f(x)+1\). For \(r\) with \(3\nmid r\), the absolute field trace changes by the nonzero element \(r\bmod 3\) under \(x\mapsto x+1\). All nonpole \(x\)-coordinates split into translation orbits of size three, and precisely one member of each orbit satisfies \(\operatorname{Tr}_{\mathbb F_{3^r}/\mathbb F_3}(f(x))=0\). By the additive Hilbert 90/Artin–Schreier trace criterion, exactly those members have three \(y\)-solutions. Accounting for the four points above poles gives
\[
\#X(\mathbb F_{3^r})=4+3\frac{3^r-3}{3}=3^r+1
\qquad(3\nmid r).
\]

**The remaining small extensions.** For \(r=3,6\), use polynomial presentations
\[
\mathbb F_{27}=\mathbb F_3[u]/(u^3+2u^2+1),\qquad
\mathbb F_{729}=\mathbb F_3[v]/(v^6+v^5+v^4+1).
\]
The defining polynomials are irreducible (the attached standalone verifier checks the Frobenius/GCD irreducibility criterion). Enumerating every field element in the standard polynomial basis, skipping the three finite poles and evaluating the absolute trace of \(x+(x^3-x)^{-1}\), produces the exact respective trace-frequency vectors
\[
(24,0,0)\quad\text{and}\quad(222,252,252),
\]
where coordinates count trace values \(0,1,2\). These are finite, exhaustive enumerations over respectively \(27\) and \(729\) elements; the attached dependency-free verification code supplies the complete algorithm, tests polynomial irreducibility and inverses, and cross-checks by enumerating the image of \(y\mapsto y^3-y\) without relying on the trace routine. Including the four ramified points gives
\[
\#X(\mathbb F_{27})=4+3\cdot24=76,\qquad
\#X(\mathbb F_{729})=4+3\cdot222=670.
\]
The six point counts are therefore exactly
\[
\begin{array}{c|rrrrrr}
r&1&2&3&4&5&6\\\hline
\#X(\mathbb F_{3^r})&4&10&76&82&244&670
\end{array}.
\]

**Recovering the entire zeta numerator.** Let \(s_r=3^r+1-\#X(\mathbb F_{3^r})\) be the \(r\)-th sum of Frobenius eigenvalue powers. We have
\[
(s_1,s_2,s_3,s_4,s_5,s_6)=(0,0,-48,0,0,60).
\]
Newton's recurrence \(kc_k=-\sum_{j=1}^k c_{k-j}s_j\), \(c_0=1\), gives \(c_1=c_2=c_4=c_5=0\), \(c_3=16\), and \(c_6=118\). The functional equation for a genus-six curve over \(\mathbb F_3\), namely \(c_{12-j}=3^{6-j}c_j\) for \(0\le j\le6\), forces all remaining coefficients and yields the displayed numerator. Straight integer polynomial multiplication verifies its asserted factorization.

**Isogeny classes and simplicity.** The numerator corresponds to the product of the square of an elliptic Weil polynomial and the square of a quartic Weil polynomial. By the finite-field isogeny theorem (or Honda–Tate classification), these define the stated elliptic and abelian-surface isogeny factors. They are ordinary: the elliptic trace is not divisible by \(3\), and the degree-two numerator coefficient of the surface is \(-2\), also prime to \(3\). The quartic characteristic polynomial
\[
h(U)=U^4+U^3-2U^2+3U+9
\]
is irreducible over \(\mathbb Q\). Indeed it has no integral root among the signed divisors of \(9\). If it factored into monic integer quadratics \((U^2+aU+b)(U^2+cU+d)\), coefficient comparison would give \(a+c=1\), \(bd=9\), \(ac+b+d=-2\), \(ad+bc=3\). When \((b,d)=(3,3)\) or either negative pair, the first three equations have no integral solution for \(a,c\). For \((b,d)=(1,9)\) or \((9,1)\), they force \(\{a,c\}=\{4,-3\}\), giving \(ad+bc\in\{33,-23\}\), not \(3\). Therefore \(h\) is irreducible and its surface is simple over \(\mathbb F_3\). Finally \(P_X(1)=(1-1+3)^2(1+1-2+3+9)^2=1296\).

## Verification

The standalone `verify.py` checks irreducibility of both field presentations, enumerates the absolute-trace frequencies at extension degrees three and six, independently counts the additive-polynomial images at those degrees, constructs the genus-six numerator via Newton identities and functional-equation symmetry, checks polynomial multiplication, and verifies the absence of linear or integral quadratic factors of the quartic. Successful execution prints `VERIFY_OK` together with the counts and final polynomial. The Python program uses only the standard library. Its finite checks prove precisely the finite-field counting assertions used in the proof; the all-extension statement comes from the translation argument, not from extrapolating the finite test.

## Relationship to prior work

Tafazolian (2026), Theorem 1.1(4) and Propositions 8.7–8.8, establishes the exceptional ordinary genus-six Artin–Schreier family and describes its geometric automorphism group. It does not supply the zeta numerator or the \(\mathbb F_3\)-isogeny decomposition calculated here. The earlier zeta computations of Bouw–Ho–Malmskog–Scheidler–Srinivasan–Vincent concern the polynomial family \(y^p-y=xR(x)\) with \(R\) additive, whose Jacobians are supersingular; this is a different class from the four-simple-pole ordinary curve considered here. The general zeta algorithms of Lauder–Wan (2002, 2004) address computational methods, rather than a stated explicit value for this coefficient-one genus-six model. The 2002 paper treats Laurent-polynomial right sides, while the sequel addresses more general Artin–Schreier covers; the sequel was not available for a whole-document comparison. The concrete polynomial and its simple abelian-surface factor have not been located in the primary references and directed literature comparisons; an undiscovered equivalent calculation remains possible.

## Limitations

The isogeny statement is over \(\mathbb F_3\), and simplicity of \(A\) is asserted only over \(\mathbb F_3\), not geometrically. The value \(1296\) is the Jacobian's rational-point **order**, not a classification of its finite group structure. This does not classify other \(\mathbb F_3\)-forms, higher base-field twists, or a universal parameter family. The point-counting code is exhaustive in two explicitly specified finite fields and does not provide an independent proof of the Weil functional equation or Tate's isogeny theorem, which are invoked as standard results. A matching value in an unindexed database or earlier paper remains a possible originality risk.

## References

1. S. Tafazolian, *Sharp bounds and gap phenomena for large p-subgroups of automorphism groups of curves*, arXiv:2610.05539v1 (first posted 2026-10-04), Theorem 1.1 and Propositions 8.7–8.8. https://arxiv.org/html/2610.05539
2. I. Bouw, W. Ho, B. Malmskog, R. Scheidler, P. Srinivasan and C. Vincent, *Zeta Functions of a Class of Artin–Schreier Curves with Many Automorphisms*, 2016, DOI: 10.1007/978-3-319-30976-7_4. Author-available text: https://cspages.ucalgary.ca/~rscheidl/Papers/win3.pdf
3. A. Lauder and D. Wan, *Computing Zeta Functions of Artin–Schreier Curves over Finite Fields*, LMS J. Comput. Math. 5 (2002), 34–55, DOI: 10.1112/S1461157000000681.
4. A. Lauder and D. Wan, *Computing zeta functions of Artin–Schreier curves over finite fields II*, J. Complexity 20 (2004), 331–349.
5. J. Tate, *Endomorphisms of abelian varieties over finite fields*, Invent. Math. 2 (1966), 134–144.

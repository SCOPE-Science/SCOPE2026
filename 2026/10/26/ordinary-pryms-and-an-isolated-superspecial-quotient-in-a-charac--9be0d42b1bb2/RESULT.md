# Ordinary Pryms and an isolated superspecial quotient in a characteristic-seven cyclic-trigonal pencil

## Finding
Let \(k\) be algebraically closed of characteristic \(7\). For every \(a\in k\) with \(a^2\ne4\), let \(C_a\) be the smooth projective curve with function field \(k(x,y)\), where
\[
y^3=x^5+a x^3+x.
\]
The order-two automorphism \(\iota(x,y)=(-x,-y)\) defines a branched double quotient \(Q_a=C_a/\langle\iota\rangle\) of genus \(2\); let \(P_a\) denote the connected Prym kernel of the norm \(J(C_a)\to J(Q_a)\), an abelian surface.

**Theorem.** For every smooth parameter, \(P_a\) is ordinary. The quotient \(Q_a\) is superspecial precisely at \(a^2=-2\), and otherwise ordinary. Accordingly, the Jacobian \(J(C_a)\) has \(7\)-rank
\[
f(J(C_a))=\begin{cases}2,&a^2=-2,\\4,&a^2\ne-2\end{cases}
\qquad(a^2\ne4).
\]
Thus this entire smooth pencil has exactly two Jacobian \(7\)-rank strata, and no member of \(7\)-rank \(0\), \(1\), or \(3\). The two parameter values with \(a^2=-2\) give isomorphic geometric curves via an order-four change of variable.

## Assumptions and scope
All varieties, ranks, and isogenies are over an algebraically closed field of characteristic \(7\). The curve means the smooth projective normalization of the displayed affine equation, not its possibly singular naive plane closure. The smoothness condition is exactly \(a^2\ne4\): the branch polynomial \(f=x(x^4+a x^2+1)\) is squarefree precisely under that condition. The curve has genus \(4\), since the cyclic tame degree-three map to the \(x\)-line is totally ramified at the five roots and at infinity. The involution has precisely the two fixed points \((0,0)\) and the unique point at infinity, so tame Riemann–Hurwitz gives genus \(2\) for its quotient. The quotient has invariant coordinates \(t=x^2\) and \(v=y/x\), satisfying \(t v^3=t^2+a t+1\), interpreted via its smooth projective normalization. The Prym has dimension \(2\).

This pencil naturally exhausts the smooth odd-polynomial subfamily of normalized cyclic trigonal genus-four curves of the form \(y^3=x^5+a x^3+b x\) with \(b\ne0\): an algebraic-closure rescaling of \(x\) and \(y\) makes \(b=1\). The involution, not a numerically selected parameter, motivates the family.

## Proof
**Holomorphic differential basis.** Let \(f=x^5+a x^3+x\). The four forms
\[
\omega_0=\frac{dx}{y},\quad\omega_1=\frac{dx}{y^2},\quad
\omega_2=\frac{x\,dx}{y^2},\quad\omega_3=\frac{x^2\,dx}{y^2}
\]
are regular. At a simple zero of \(f\), \(y\) is a uniformizer and \(dx\) has order \(2\); at infinity, \(v(x)=-3\), \(v(y)=-5\), \(v(dx)=-4\), giving nonnegative orders \(1,6,3,0\), respectively. As the genus is \(4\), these are a basis. The involution fixes \(\omega_0,\omega_2\) and negates \(\omega_1,\omega_3\).

**Cartier calculation.** Since \(7=1+3\cdot2\), write \(x^i dx/y^j=(x^i f^{2j}dx)/y^{7j}\). For the Cartier operator \(\mathcal C\), coefficient extraction yields
\[
\mathcal C(x^i dx/y^j)=\sum_{m\ge1}
\bigl([x^{7m-1-i}]f^{2j}\bigr)^{1/7}\,
\frac{x^{m-1}dx}{y^j}.
\]
Here \([x^n]\) denotes coefficient extraction; this identity holds in the perfect field \(k\). In the ordered basis \((\omega_1,\omega_2,\omega_3)\) for the \(j=2\) forms, the matrix whose entries are the seventh powers of the actual Cartier entries is
\[
B=\begin{pmatrix}
4a&0&1\\
0&(a^2+2)(a^2-4)&0\\
1&0&4a
\end{pmatrix}.
\]
In the \(\omega_0\) direction the corresponding entry is \(a^2+2\). Indeed, the required coefficients come from direct expansion of \(f^2\) and \(f^4\). Entrywise seventh roots leave all zero patterns, determinants, and invertibility unchanged.

**Prym versus quotient.** The invariant two-dimensional block, in the basis \((\omega_0,\omega_2)\), is diagonal with seventh-powered entries
\[
a^2+2,\qquad (a^2+2)(a^2-4).
\]
The anti-invariant block, in the basis \((\omega_1,\omega_3)\), is
\[
B_{-}=\begin{pmatrix}4a&1\\1&4a\end{pmatrix},
\quad\det B_-=16a^2-1=2(a^2-4)\ \text{in }k.
\]
Because \(a^2\ne4\), the anti-invariant Cartier block is invertible for every smooth member. The pullback and norm maps associated to the degree-two cover give a prime-to-seven isogeny \(J(Q_a)\times P_a\to J(C_a)\), whose differential decomposition is the invariant and anti-invariant splitting. Thus \(P_a\) has invertible Cartier operator, hence is an ordinary abelian surface for all such \(a\).

Since \(a^2-4\ne0\), the invariant block is invertible if \(a^2+2\ne0\), and it is the zero matrix if \(a^2=-2\). In the first case \(Q_a\) is ordinary. In the second case its genus-two Jacobian has zero Cartier operator and is superspecial. The prime-to-seven isogeny makes the \(7\)-ranks additive: \(2+2=4\) generically and \(0+2=2\) precisely on the exceptional locus. No intermediate rank is possible. As \(-2\ne4\) in characteristic seven, both exceptional parameters are smooth and occur over the algebraic closure.

Finally choose \(c\in k\) with \(c^2=-1\); then \(c^4=1\). Choose \(d\) with \(d^3=c\). The coordinate change \((x,y)\mapsto(cx,dy)\) identifies \(C_a\) with \(C_{-a}\), so the two roots of \(a^2=-2\) represent one geometric isomorphism class within the pencil.

## Verification
The standalone `artifacts/verify.py` recomputes from integer-coefficient polynomial convolution the coefficient extractions in \(f^2\) and \(f^4\), checking every displayed Cartier block entry modulo \(7\). It enumerates the \(47\) smooth parameters in \(\mathbb F_{49}\), finding exactly two with \(a^2=-2\) and \(45\) with ordinary quotient; it also checks the smoothness criterion on \(\mathbb F_7\) and lists independently enumerated \(\mathbb F_7\)-point counts. Output terminates in `CHECK_OK`. The proof of the statements for **all** algebraically closed-field parameters is symbolic, not inferred from finite enumeration.

## Relationship to prior work
Baldwin–Eilbeck–Gibbons–Ônishi (initial preprint 21 December 2006) study the full cyclic-trigonal genus-four equation and its analytic Abelian functions; that family and the holomorphic-differential description are established background, not claimed new. Kudo–Harashita (initial preprint 5 July 2016) prove the nonexistence of superspecial genus-four curves in characteristic seven, which neither implies the exclusion of intermediate \(7\)-ranks in this pencil nor determines ordinarity of its Prym or the superspeciality of its genus-two quotient. The more recent Sohn (2025) paper concerns the \(a\)-number of genus-four superelliptic curves; its bibliographic description is relevant, but its full text could not be examined. This theorem's asserted contribution is the **simultaneous quotient/Prym decomposition with uniform Prym ordinarity and exact exceptional quotient locus**; it does not assert priority for general Cartier formulas or genus-four \(a\)-number computations.

## Limitations
This is a statement only about the smooth odd-polynomial one-parameter subfamily in characteristic seven, not the whole trigonal locus, all characteristics, singular boundary points, Newton polygons, or arbitrary Prym families. The comparison to prior research is based on the accessible full text and searches listed in the accompanying review, with an explicit unresolved historical-overlap risk from Sohn (2025). All scientific assessments are self-review; no independent validation has been performed.

## References
1. S. Baldwin, J. C. Eilbeck, J. Gibbons, Y. Ônishi, *Abelian Functions for Cyclic Trigonal Curves of Genus Four*, arXiv:math/0612654 (first public 2006-12-21), https://arxiv.org/abs/math/0612654 .
2. M. Kudo and S. Harashita, *Superspecial curves of genus 4 in small characteristic*, arXiv:1607.01114 (first public 2016-07-05), https://arxiv.org/abs/1607.01114 .
3. G. Sohn, *The a-number of superelliptic curves of genus four*, Journal of Applied and Pure Mathematics 7 (2025), 59–66, doi:10.23091/japm.2025.059; bibliographic record and abstract only, https://doi.org/10.23091/japm.2025.059 .

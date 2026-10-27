# Two-versus-three component transition for square-zero centralizers of Jordan type \((n,2)\)

## Finding

Let \(k\) be any field, let \(n\ge4\), and let \(J=J_n(0)\oplus J_2(0)\in M_{n+2}(k)\). Define the **square-zero centralizer locus**
\[
\mathcal X_n(k)=\{X\in M_{n+2}(k):XJ=JX,\ X^2=0\}.
\]
Its reduced affine algebraic variety has precisely **two** irreducible components when \(n\) is even and precisely **three** when \(n\) is odd. Every component has dimension \(\lfloor n/2\rfloor+3\), and all components meet along the same affine subspace of dimension \(\lfloor n/2\rfloor+2\). The descriptions and component assertions hold over every field, including characteristic two (irreducible means geometrically irreducible).

For every prime power \(q\), the exact number of labeled commuting square-zero matrices is
\[
\boxed{\#\mathcal X_n(\mathbb F_q)=
\begin{cases}
q^{n/2+1}(2q^2-1),&n\text{ even},\\
q^{(n+3)/2}(3q-2),&n\text{ odd}.
\end{cases}}
\]
The assertions concern the fixed matrix \(J\), rather than the union over its conjugacy class; no orbit quotient is taken.

## Assumptions and scope

Write \(R_j=k[t]/(t^j)\), identifying the underlying \(k[t]\)-module of \(J\) with \(M=R_n\oplus R_2\), where \(J\) acts as multiplication by \(t\). Any commuting \(k\)-linear operator is uniquely determined by \(a\in R_n\) and \(b,c,d\in R_2\), acting by
\[
X(u,v)=\bigl(au+t^{n-2}bv,\ cu+dv\bigr).
\]
Products involving the second coordinate are read in \(R_2\); the factor \(t^{n-2}\) in the first coordinate gives the unique \(k[t]\)-linear map \(R_2\to R_n\) with parameter \(b\). The ambient centralizer has affine dimension \(n+6\).

To describe component equations, use variables \(B,C,U,V,\delta,x,y\), all in \(k\). The variable \(\delta\) is an invertible linear reparameterization of the coefficient of \(t\) in \(d\). The following normal forms are **reduced-variety** isomorphisms; potentially nonreduced defining schemes are not identified with their reductions.

For \(n=2h\), \(h\ge2\), let
\[
E=V(x^2+BC,\ 2xy+BV+CU,\ \delta B,\delta C)_{\mathrm{red}}
\subseteq\mathbb A^7.
\]
Then \(\mathcal X_{2h}^{\mathrm{red}}\cong\mathbb A^{h-1}\times E\). Its two irreducible components are
\[
E_0=V(B,C,x),\qquad
E_1=V(\delta,x^2+BC,2xy+BV+CU)_{\mathrm{red}}.
\]
Each has dimension four, and their common intersection is \(V(B,C,x,\delta)\cong\mathbb A^3\).

For \(n=2h+1\), \(h\ge2\), let
\[
O=V(BC,\ x^2+BV+CU,\delta B,\delta C)_{\mathrm{red}}
\subseteq\mathbb A^6,
\]
with coordinates \(B,C,U,V,\delta,x\). Then \(\mathcal X_{2h+1}^{\mathrm{red}}\cong\mathbb A^h\times O\). Its three irreducible components are
\[
O_0=V(B,C,x),\qquad
O_B=V(C,\delta,x^2+BV),\qquad
O_C=V(B,\delta,x^2+CU).
\]
Each has dimension three. Every pairwise intersection and their triple intersection equals the common affine plane \(V(B,C,x,\delta)\cong\mathbb A^2\).

## Proof

**1. Centralizer normal form and square equations.** Since \(M=R_n\oplus R_2\), endomorphism blocks are respectively \(R_n\), \(t^{n-2}R_2\), \(R_2\), \(R_2\). Squaring the displayed operator, and using \(n\ge4\) so that \(t^{n-2}=0\) in \(R_2\), gives the four necessary and sufficient identities
\[
a^2+t^{n-2}bc=0\pmod {t^n},\qquad
b(a+d)=c(a+d)=0\pmod {t^2},\qquad d^2=0\pmod {t^2}.
\]
Their constant terms force \(a(0)=d(0)=0\) over *every* field. Thus \(d=t d_1\) in \(R_2\).

**2. Valuation cutoff.** The first identity implies that \(a\) is divisible by \(t^{h-1}\) for \(n=2h\), and by \(t^h\) for \(n=2h+1\). Indeed, if the leading nonzero term of \(a\) has degree \(r\), its square has nonzero leading coefficient in degree \(2r\); this cannot cancel a term of \(t^{n-2}bc\) below degree \(n-2\). Hence \(2r\ge n-2\), giving these integer cutoffs. In particular, \(a\) has zero constant term, and for odd \(n\ge5\) its linear term also vanishes.

**3. Even length.** Put \(n=2h\) and write \(a=t^{h-1}(x+yt+\cdots)\). The coefficients above \(t^h\) are unrestricted: exactly \(h-1\) free scalar parameters. Write \(b=B+Ut\), \(c=C+Vt\). Matching coefficients in the first square equation yields
\[
x^2+BC=0,\qquad 2xy+BV+CU=0.
\]
For \(h\ge3\), the two mixed equations become \(d_1B=d_1C=0\), so take \(\delta=d_1\). For the boundary \(h=2\), they instead become \((x+d_1)B=(x+d_1)C=0\), so take \(\delta=x+d_1\). This change of variables is invertible in all characteristics and yields exactly \(E\).

Any solution with \(B=C=0\) has \(x=0\) and lies in \(E_0\). If \((B,C)\ne(0,0)\), the mixed conditions force \(\delta=0\) and give \(E_1\). To prove \(E_1\) geometrically irreducible, regard it as the two-equation complete intersection
\[
Y=V(x^2+BC,\ 2xy+BV+CU)\subseteq\mathbb A^6.
\]
The first polynomial is irreducible over any algebraic closure, and the second is nonzero in its coordinate domain, so the pair is a regular sequence and every irreducible component of \(Y\) has dimension four. On \(B\ne0\), one solves uniquely for \(C=-x^2/B\) and \(V=-(2xy+CU)/B\), obtaining an irreducible four-dimensional open set. On \(B=0\), the equations force \(x=0\), and then \(CU=0\), so this closed complement has dimension at most three. No four-dimensional component can lie in it. Therefore \(Y\) is irreducible of dimension four; \(E_0\) is plainly affine four-space, and neither component contains the other. Their stated intersection follows directly.

For the point count, \(B=C=0\) forces \(x=0\), leaving \(q^4\) choices of \((y,U,V,\delta)\). Otherwise \(\delta=0\) and the equation \(x^2+BC=0\) has \(q^2-1\) triples \((x,B,C)\) with \((B,C)\ne(0,0)\): precisely \(2(q-1)\) with \(x=0\), and \((q-1)^2\) with \(x\ne0\). The remaining linear equation has \(q^2\) solutions in \((y,U,V)\). Multiplying by the \(q^{h-1}\) freely chosen coefficients of \(a\) gives
\[
q^{h-1}\bigl(q^4+(q^2-1)q^2\bigr)=q^{h+1}(2q^2-1).
\]

**4. Odd length.** Put \(n=2h+1\) with \(h\ge2\) and write \(a=t^h(x+\cdots)\), with exactly \(h\) unrestricted coefficients above \(t^h\). Matching the coefficients of \(t^{2h-1}\) and \(t^{2h}\) in the first square equation gives
\[
BC=0,\qquad x^2+BV+CU=0.
\]
The mixed equations give \(d_1B=d_1C=0\), so take \(\delta=d_1\). This yields \(O\). If \(B=C=0\), then \(x=0\), giving \(O_0\). If \(B\ne0\), then \(C=\delta=0\) and \(x^2+BV=0\); if \(C\ne0\), the symmetric statement holds. Each quadratic cone \(x^2+BV=0\) or \(x^2+CU=0\) is irreducible over every algebraic closure, since these polynomials do not factor into linear factors even in characteristic two. Hence the three displayed components are geometrically irreducible, three-dimensional, distinct, and have exactly the asserted common intersection.

For the point count, the \(B=C=0\) stratum has \(q^3\) points \((U,V,\delta)\). For \(B\ne0,C=0\), there are \((q-1)q^2\) points since \(\delta=0\), \(x,U\) are arbitrary, and \(V=-x^2/B\). The symmetric stratum has the same size. Multiplying by the \(q^h\) free higher coefficients of \(a\) gives
\[
q^h\bigl(q^3+2(q-1)q^2\bigr)=q^{h+2}(3q-2).
\]
All arguments use polynomial equations valid in every characteristic; nowhere is division by \(2\) required. This completes both assertions.

## Verification

The accompanying `check_n2_squarezero.py` enumerates \(k[t]\)-linear block parameters independently of the component argument, checks the square equations and the resulting point counts for \((n,q)=(4,2),(5,2),(6,2),(7,2),(4,3),(5,3),(6,3)\). A second implementation assembles ordinary \((n+2)\times(n+2)\) matrices and tests commutation and squaring directly for \((n,q)=(4,2),(5,2),(4,3)\). Reproduce with `python3 check_n2_squarezero.py`; the expected final marker is `MATRIX_MODEL_CROSSCHECK_OK`.

The coordinate and matrix implementations agree with totals \(56,64,112,128,459,567,1377\), respectively. These finite tests are regression checks rather than an infinite-field proof; the all-field and all-size assertions follow from the preceding symbolic argument. The geometric component analysis uses the reduced locus and is not a proof of reducedness of the original defining ideal.

## Relationship to prior work

Košir and Oblak (`arXiv:0712.2813`, original public posting 2007-12-17) study generic commuting nilpotent matrices and the dense Jordan partition in an entire nilpotent centralizer. Britnell and Wildon (`arXiv:1001.0811`, 2010-01-06), especially Section 4 and Theorem 4.10, classify existence of commuting nilpotent similarity types in specified two-part cases. Both are important antecedents but neither inspected section provides the number or reduced-component equations for the square-zero fiber at a fixed \((n,2)\) Jordan matrix. Bogdanić et al. (`arXiv:2212.08425`, 2022-12-16) treat centralizers of **equal** two-block partitions and possible Jordan types, rather than the unequal-length \((n,2)\) centralizer's square-zero component/point census.

The related fixed-hook case \((n,1)\) has a different parity transition: in odd size its square-zero fiber is irreducible, whereas the present \((n,2)\) fiber has three components. Results for consecutive two-block partitions \((m,m-1)\) concern full nilpotent ranks and do not imply the all-length square-zero count here. General Jordan-type existence assertions cannot determine finite-field fiber cardinalities or numbers of components.

## Limitations

The theorem is for a fixed nilpotent matrix with blocks \((n,2)\) and \(n\ge4\), not arbitrary partitions, conjugacy classes, or complete ordinary-rank distributions. The geometric statements concern the reduced algebraic variety, not the nonreduced parameter scheme. The primary-literature comparison did not rule out every possible prior formula hidden in broader centralizer or Hall-polynomial enumeration frameworks. Independent mathematical review and comprehensive historical publication-priority verification have not been performed.

## References

1. T. Košir and P. Oblak, *On pairs of commuting nilpotent matrices*, arXiv:0712.2813 (first posted 2007-12-17). https://arxiv.org/abs/0712.2813
2. J. R. Britnell and M. Wildon, *On types and classes of commuting matrices over finite fields*, arXiv:1001.0811 (first posted 2010-01-06), especially Section 4. https://arxiv.org/abs/1001.0811
3. D. Bogdanić, A. Đurić, S. Koljančić, P. Oblak, and K. Šivic, *Jordan structures of nilpotent matrices in the centralizer of a nilpotent matrix with two Jordan blocks of the same size*, arXiv:2212.08425 (first posted 2022-12-16). https://arxiv.org/abs/2212.08425

# A rank-preserving bridge from square-zero traceless matrices to primitive image zeta strata

## Finding

Let \(R\) be a finite commutative chain ring of length \(m\ge1\), maximal ideal \((\pi)\), and residue-field size \(q\). Write \(R_\ell=R/(\pi^\ell)\). Define the primitive set \(\mathcal P_\ell=\{Y\in\mathrm{sl}_2(R_\ell):Y\not\equiv0\pmod\pi\}\), and the image exponent \(\rho_\ell(Y)=\log_q|\operatorname{im}(Y:R_\ell^2\to R_\ell^2)|\). Let \(\mathcal N_m=\{X\in\mathrm{sl}_2(R):X^2=0\}\).

**Rank-preserving bridge.** For every \(R\), the map
\[
\Phi_m:\{0\}\sqcup\bigsqcup_{\ell=1}^{m}\{Y\in\mathcal P_\ell:\rho_\ell(Y)\le m\}\longrightarrow\mathcal N_m,
\qquad \Phi_m(Y)=\pi^{m-\ell}\widetilde Y,
\]
is a canonical bijection satisfying \(\rho_m(\Phi_m(Y))=\rho_\ell(Y)\). Here \(\widetilde Y\) is any trace-zero lift of \(Y\) to \(R\); the expression is independent of the lift.

For \(0\le r\le m\), it follows that the number of \(X\in\mathcal N_m\) with image cardinality \(q^r\) depends only on \(q,r\), and not on \(R,m\) beyond \(m\ge r\). Denoting it by \(C_r(q)\), one has
\[
C_0(q)=1,\qquad
\sum_{r\ge0}C_r(q)T^r
=\frac{(1-T)(1-q^2T^2)}{(1-q^2T)(1-q^3T^2)}.
\]
The rational series is the **previously known** two-by-two traceless primitive image-zeta series of Carnevale--Shechter--Voll, Example 1.3 (2017). The finding here is the explicit uniform bridge that transfers those coefficients, without further correction terms, to a nonlinear square-zero matrix locus.

## Assumptions and scope

The ground ring is finite, commutative, local and principal, with linearly ordered ideals. Its characteristic can be even or odd and need not equal the characteristic of the residue field. The image exponent is defined via cardinality, not vector-space rank over a residue field; in mixed characteristic the latter need not be defined. The trace is the ordinary matrix trace over the ring. The bijection is canonical relative to the stipulated uniformizer \(\pi\); changing the uniformizer changes the coordinates, but not the image-size counts. All \(m\ge1\), \(q\) prime powers, and \(0\le r\le m\) are covered. For \(Y\in\mathcal P_\ell\), \(\rho_\ell(Y)\) need not be at most \(m\) unless the stated inequality is imposed.

## Proof

**1. Canonical valuation factorization.** A matrix \(X\in\mathrm{sl}_2(R)\) is uniquely of the form \(\left(\begin{smallmatrix}a&b\\c&-a\end{smallmatrix}\right)\). If nonzero, the minimum valuation of \(a,b,c\) is a unique integer \(s\in\{0,\ldots,m-1\}\). Put \(\ell=m-s\). The map \(R_\ell\to(\pi^s)\subset R\), \(u\mapsto\pi^s\tilde u\), is a well-defined bijection of additive groups: two lifts differ by an element of \((\pi^\ell)\), annihilated by \(\pi^s\). Thus \(X=\pi^s\widetilde Y\) for a **unique** primitive trace-zero \(Y\in\mathrm{sl}_2(R_\ell)\). A trace-zero lift exists by lifting the three entries \(a,b,c\) and setting the fourth entry to \(-a\). This proves well-definedness and injectivity of the displayed map without any choice of coefficient representatives.

**2. Square-zero criterion versus image size.** The Cayley--Hamilton identity for a traceless two-by-two matrix gives \(Y^2=-\det(Y)I\), in all characteristics. Since \(Y\) is primitive, one Smith invariant factor is a unit and the second has valuation \(v\in\{0,\ldots,\ell\}\), where \(v=\ell\) means zero. Consequently \(\rho_\ell(Y)=2\ell-v\). The lifted matrix satisfies \((\pi^s\widetilde Y)^2=0\) if and only if \(\pi^{2s}\det(\widetilde Y)=0\), equivalently \(2s+v\ge m\). Substituting \(s=m-\ell\) makes this **exactly** \(2\ell-v\le m\), or \(\rho_\ell(Y)\le m\). Multiplication by \(\pi^s\) identifies the additive image of \(Y\) in \(R_\ell^2\) with the additive image of \(X\) in \(R^2\), so \(\rho_m(X)=\rho_\ell(Y)\). The zero matrix corresponds only to the isolated base point. Surjectivity and rank preservation follow.

**3. Rank multiplicities and zeta-series identification.** Let \(Q(a,b,c)=a^2+bc\), so \(\det\left(\begin{smallmatrix}a&b\\c&-a\end{smallmatrix}\right)=-Q\). Over \(\mathbb F_q\), exactly \(q^2-1\) nonzero triples satisfy \(Q=0\). Each is a smooth point of the quadratic hypersurface: its gradient \((2a,c,b)\) is nonzero in every characteristic. The primitive triples over \(R_\ell\), categorized by the truncated determinant valuation \(v\), therefore number
\[
N_{\ell,v}=\begin{cases}
(q-1)q^{3\ell-1},&v=0,\\
(q^2-1)(q-1)q^{3\ell-v-3},&1\le v<\ell,\\
(q^2-1)q^{2\ell-2},&v=\ell.
\end{cases}
\]
Indeed, lifting a nonzero smooth root through each successive quotient imposes one nonzero linear equation in three residue-field digits and hence gives \(q^2\) lifts, while the next nonvanishing digit has \(q-1\) choices. The \(v=0\) count is the complement among all primitive triples. By Step 2, a primitive level-\(\ell\) contribution of image exponent \(r\) is exactly \(v=2\ell-r\), so the bijection yields for \(r\ge1\)
\[
C_r(q)=(q^2-1)q^{2r-2}
+\mathbf 1_{2\mid r}(q-1)q^{3r/2-1}
+(q^2-1)(q-1)\sum_{\ell=\lfloor r/2\rfloor+1}^{r-1}q^{\ell+r-3},
\]
with the empty sum equal to zero. The terms arise respectively from \(v=\ell\) (so \(\ell=r\)), \(v=0\) (so \(\ell=r/2\)), and \(0<v<\ell\). They depend on \(r\), not the ambient length, since \(\ell\le r\le m\). A geometric sum, or multiplication of formal power series, gives the stated rational function. Its equality with the earlier two-by-two primitive image-zeta formula is recorded as a consequence of the new correspondence, **not as a novelty claim for the rational coefficients**.

The support of the image exponent is exactly \(0,1,\ldots,m\), because each \(C_r(q)>0\) and \(\rho_m(X)\le m\) for a square-zero endomorphism of the length-\(2m\) module \(R^2\).

## Verification

Run `python3 verify.py` with standard Python 3. The checker directly enumerates all trace-zero square-zero matrices and computes image sizes over \(\mathbb Z/(p^m)\), including lengths through four for \(p=2\), and over \(\mathbb F_p[t]/(t^m)\). It also checks the genuine extension-field chain ring \(\mathbb F_4[t]/(t^2)\). Every computed rank multiplicity agrees with the closed formula, and power-series coefficients match the rational function for \(q=2,3,4,5,7\) through exponent nine. The required success marker is `VERIFY_OK_TRACEZERO_SQUAREZERO_ZETA_BRIDGE`. This exhaustive **finite** corroboration is not the proof of the arbitrary-length statement; Steps 1--3 are the symbolic proof.

## Relationship to prior work

Carnevale, Shechter and Voll, *Enumerating traceless matrices over compact discrete valuation rings* (arXiv:1709.02717), Theorem 1.2, Example 1.3 and §2.2, already calculate the displayed rational image-zeta series for primitive traceless two-by-two matrices via elementary divisors. That is stronger published coverage of the **coefficient formula** considered in isolation. The distinct assertion here is the rank-preserving **canonical bijection** from a finite-level square-zero locus to disjoint truncated primitive-image strata; the inspected sections do not state or imply a map to square-zero matrices. Britnell and Wildon (arXiv:1001.0811) study commuting Jordan types over fields, and Stasinski and Voll (arXiv:1104.1756) provide background on local representation and image-zeta methods. Their inspected discussions do not give this correspondence. The possibility of an earlier equivalent valuation-scaling correspondence under other terminology is a residual bibliographic risk.

## Limitations

Only two-by-two **traceless** matrices over **commutative finite chain rings** are covered. The rational series is not a new formula, and a numerical match alone does not establish a new result; only the proved canonical set-theoretic correspondence is advanced here. No counterpart is proved for larger matrices, nonprincipal Artinian rings, or non-tracezero square-zero loci. The literature comparison is not a claim of absolute historical priority. Independent mathematical audit has not been performed.

## References

- Britnell, J. R., and Wildon, M., *On types and classes of commuting matrices over finite fields*, arXiv:1001.0811, first publicly posted 2010-01-06.
- Stasinski, A., and Voll, C., *Representation zeta functions of nilpotent groups and generating functions for Weyl groups of type B*, arXiv:1104.1756, first posted 2011-04-10.
- Carnevale, A., Shechter, S., and Voll, C., *Enumerating traceless matrices over compact discrete valuation rings*, arXiv:1709.02717, Theorem 1.2, Example 1.3 and §2.2, first posted 2017-09-08.

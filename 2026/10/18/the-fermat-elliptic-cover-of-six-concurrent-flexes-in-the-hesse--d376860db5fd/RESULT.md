# The Fermat elliptic cover of six concurrent flexes in the Hesse quartic family

## Finding
Let \(\omega\) be a primitive cube root of unity, and put
\[
B=\{\gamma\in\mathbf C:\gamma\ne0,\ \gamma^3\ne1\}.
\]
For \(\gamma\in B\), let \(C_\gamma\subset\mathbf P^2_\mathbf C\) be the smooth quartic
\[
4Z(X^3+Y^3)+Z^4-6\gamma XYZ^2-3\gamma^2X^2Y^2=0,
\]
marked by \(p=[0:0:1]\). Its six flexes whose tangent lines pass through \(p\) form a finite étale degree-six incidence cover of \(B\). The unique smooth projective completion of that incidence curve is the elliptic Fermat-type cubic
\[
\mathcal E:\ T^3+W^3-2Z^3=0\ \subset\mathbf P^2_\mathbf C,
\qquad j(\mathcal E)=0,
\]
and the completed parameter morphism is
\[
\pi:\mathcal E\longrightarrow\mathbf P^1_\gamma,\qquad
[T:Z:W]\longmapsto[Z^2:TW].
\]
This is a **Galois cover of degree six with group \(S_3\)**. Explicit deck transformations on \(t=T/W\), \(z=Z/W\) are
\[
\rho(t,z)=(\omega t,\omega^2z),\qquad
\tau(t,z)=(t^{-1},z/t).
\]
The branch values are exactly \(\gamma=0,1,\omega,\omega^2\), with three points of ramification index two over each value and no ramification at \(\infty\). Accordingly each local monodromy permutation on the six flexes has cycle type \((2,2,2)\), and the full geometric monodromy is \(S_3\) acting regularly on six points. Equivalently, the slope parameters of the flex lines have splitting polynomial
\[
(t^3+1)^2-4\gamma^3t^3,
\]
whose splitting field over \(\mathbf C(\gamma)\) is \(\mathbf C(\mathcal E)\).

## Assumptions and scope
The base field is \(\mathbf C\); all curves and morphisms are over \(\mathbf C\). The quartics arise, up to nonzero scalar, from the Hesse cubic \(\phi=X^3+Y^3+Z^3-3\gamma XYZ\) by Chisini's polar construction \(\phi_{ZZ}\phi-\tfrac12\phi_Z^2=0\), as in [1, Corollary 36]. A flex here means a smooth point of the quartic at which its tangent line meets it to *exact* order three. A line through \(p\) is marked by its slope \(t=X/Y\); the two coordinate slopes \(0,\infty\) are treated separately. The incidence curve parameterizes pairs \((\gamma,q)\), not arbitrary flexes of \(C_\gamma\), and the Galois/ramification assertion concerns the completion over the full parameter line. The four finite excluded parameter values correspond to singular quartics, so the ramification at these values is boundary ramification, not flex ramification of a smooth quartic.

## Proof
**1. Smooth parameter locus.** Direct expansion of the polar construction yields the stated quartic. For \(\gamma\ne0\), the only points of \(C_\gamma\) on \(Z=0\) are \([1:0:0]\) and \([0:1:0]\), where \(F_Z=4(X^3+Y^3)\ne0\). In \(Z=1\), let \(u=X/Z\), \(v=Y/Z\), \(w=uv\). At a singular point \(u,v\ne0\) (otherwise the derivatives force \(u=v=0\), which does not lie on the quartic). The two partial derivatives give \(u^3=v^3=a\) and \(2a=\gamma w(1+\gamma w)\). Substitution into the quartic equation gives \((\gamma w-1)^2=0\), hence \(\gamma w=1\), \(a=1\), and \(w^3=u^3v^3=1\). Therefore \(\gamma^3=1\). Conversely, when \(\gamma^3=1\), choosing \(u^3=v^3=1\) and \(uv=\gamma^{-1}\) produces singular points. For \(\gamma=0\), the equation factors as \(Z(4X^3+4Y^3+Z^3)\). Thus the smooth locus is exactly \(B\).

**2. Flex-incidence equations.** On a line \(X=tY\), with \(Y=1\) and \(z=Z/Y\), intersection with the quartic is the polynomial
\[
G_{\gamma,t}(z)=z^4-6\gamma t z^2+4(t^3+1)z-3\gamma^2t^2.
\]
Triple contact is the simultaneous system \(G=\partial_zG=\partial_z^2G=0\). The second derivative gives \(z^2=\gamma t\); inserting this into the first derivative gives \(t^3+1=2z^3\). These two equations automatically make \(G=0\), and \(\partial_z^3G=24z\ne0\) on \(B\), so the contact order is exactly three. At \(t=0\) and \(t=\infty\), the line-intersection polynomial in the analogous coordinate is \(z^4+4z\), with four simple roots, so neither is a flex tangent. The six flex points thus correspond bijectively to solutions
\[
t^3+1=2z^3,\qquad\gamma=z^2/t,
\]
with \(t,z\ne0\). Eliminating \(z\) gives the displayed sextic in \(t\), and \(z=(t^3+1)/(2\gamma t)\) recovers the point uniquely. Its exact discriminant is \(2985984\gamma^9(\gamma^3-1)^3\), nonzero on \(B\), so there are exactly six distinct flex lines and the incidence map over \(B\) is étale.

**3. Completion and Galois action.** Homogenizing the incidence equation gives the nonsingular plane cubic \(\mathcal E\). The projective pair \([Z^2:TW]\) has no base point on \(\mathcal E\): \(Z=T=0\) or \(Z=W=0\) contradicts its cubic equation. The six poles of \(\gamma=Z^2/(TW)\) occur at the three points \(T=0\) and the three points \(W=0\), and all are simple, proving \(\deg\pi=6\). The cubic is a diagonal Fermat cubic after scaling a coordinate, hence \(j(\mathcal E)=0\). Both stated maps preserve \(t^3+1=2z^3\) and \(\gamma=z^2/t\), and satisfy \(\rho^3=\tau^2=1\), \(\tau\rho\tau=\rho^{-1}\). They yield six different automorphisms of the generic fiber and therefore the full degree-six Galois group \(S_3\). In particular the cover is connected and the sextic's splitting field is the function field \(\mathbf C(\mathcal E)\).

**4. Exact branch divisor.** At \(z=0\), the cubic has three points \(t^3=-1\); \(z\) is a local coordinate there and \(\gamma=z^2/t\) has a double zero. Away from \(t z=0\), differentiating the cubic relation gives \(dt=2z^2t^{-2}dz\), whence
\[
\frac{d\gamma}{\gamma}=\frac{2(t^3-z^3)}{zt^3}\,dz.
\]
This vanishes exactly when \(t^3=z^3=1\): there are nine such points, three over each of the three cube roots of unity \(\gamma^3=1\), with simple derivative zero and ramification index two. At the three points \(T=0\) and three points \(W=0\), \(\gamma\) has simple poles, so no branching occurs over \(\infty\). The four branch fibers contribute \(4\cdot3=12\) to the ramification divisor, also agreeing with Riemann--Hurwitz \(2g(\mathcal E)-2=6(-2)+12=0\). Since the Galois action on a generic fiber is regular, a stabilizer of order two swaps the six sheets in three disjoint pairs; this establishes the monodromy cycle type.

## Verification
The standalone script `artifacts/check_flex_cover.py` uses exact SymPy polynomial arithmetic to reproduce the polar-quartic normalization, contact derivative identities, sextic discriminant, group equation invariance, and critical-point reduction. Executing it with Python 3 and SymPy prints `FLEX_INCIDENCE_FERMAT_S3_EXACT_OK`. Its checks corroborate, but do not replace, the global geometric arguments above. No numerical sample is treated as proof of the universal statement.

## Relationship to prior work
Ciliberto--Grassi--Miranda--Verra--Zanardini [1, Theorem 31 and Corollary 36] develop the Chisini quartic, show its six concurrent flex tangents, and give a detailed numeric example. Those are premises, not new claims here. The added statement is the entire varying-parameter flex-incidence cover, its genus-one compactification, splitting field, exact Galois group, and complete geometric branch profile. Chisini's classical treatment [2] supplies the polar construction and much equianharmonic quartic geometry; a prior calculation of this *global incidence monodromy* in that work cannot be excluded without a complete independent historical review.

## Limitations
The theorem concerns this marked Hesse coordinate family, not an intrinsic monodromy computation over an unmarked coarse moduli stack, and it does not classify all flexes of the quartics. Special fibers outside \(B\) do not count as smooth quartics. The exact branch formula is for the natural smooth completion of the incidence cover. The novelty comparison is not exhaustive for the 1916 Italian original and other early equianharmonic-curve literature.

## References
[1] C. Ciliberto, A. Grassi, R. Miranda, A. Verra, A. Zanardini, *Rational elliptic surfaces with six singular double fibres*, arXiv:2602.11725v1 (first publicly posted 2026-02-12), especially Section 3.3, Theorem 31, Corollary 36, Example 37, Remark 38; https://arxiv.org/pdf/2602.11725.

[2] O. Chisini, *Sui fasci di cubiche a modulo costante*, Rendiconti del Circolo Matematico di Palermo **41** (1916), 59--93, as cited and discussed in [1].

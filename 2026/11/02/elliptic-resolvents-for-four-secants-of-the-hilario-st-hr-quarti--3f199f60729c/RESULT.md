# Elliptic resolvents for four-secants of the Hilario–Stöhr quartic pencil

## Finding

For any integer \(r\ge2\), let \(q=2^r\) and \(t\in\mathbb F_q^\times\). Consider the plane quartic

\[
C_t:\quad Z^4+X^2Y^2+X^3Z+t(Y^4+X^2Z^2)=0.
\]

Only *distinct smooth rational intersection points* are counted: intersection multiplicities and the singular point are not included. The line \(X=0\) is among the projective lines but contains no smooth point of the quartic. Let \(s_4(t)\) denote the number of directions of affine lines through \((y,z)=(0,0)\) containing four distinct rational points of \(C_t\). Set

\[
\alpha=t^{1/8},\quad \Delta=1+\alpha^3,\quad e=\Delta/\alpha^4.
\]

The eighth root is the unique one in \(\mathbb F_q\). When \(\Delta\ne0\), the nonsingular projective cubic

\[
E_t:\quad V^2+UV=U^3+\alpha^{-3}U^2+e^3U
\]

is an elliptic curve and the following **exact identity** holds:

\[
\boxed{\#E_t(\mathbb F_q)=6+6s_4(t).}
\]

In this case Hasse's theorem yields \(\left|s_4(t)-(q-5)/6\right|\le\sqrt q/3\). When \(\Delta=0\), equivalently \(t^3=1\), the cubic is singular and the replacement formula is

\[
\boxed{s_4(t)=\begin{cases}(q-2)/6,&r\text{ odd},\\(q-4)/6,&r\text{ even}.\end{cases}}
\]

For \(j\in\{0,1,2,3,4\}\), write \(N_j\) for the number of \(\mathbb F_q\)-projective lines containing exactly \(j\) distinct *smooth* \(\mathbb F_q\)-points of \(C_t\). The complete line-intersection distribution is

\[
\begin{aligned}
N_4&=\frac q4s_4(t),\\
N_3&=0,\\
N_2&=\frac q2\bigl(q-1-3s_4(t)\bigr),\\
N_1&=2q\bigl(1+s_4(t)\bigr),\\
N_0&=1+\frac{q(q-1)}2-\frac{3q}4s_4(t).
\end{aligned}
\]

The source pencil is geometrically rational. The elliptic curve arises instead as a quadratic resolvent of its degree-three map of rational secant directions; there is no claim that the quartic itself has genus one.

## Assumptions and scope

All statements are for every finite field \(\mathbb F_{2^r}\), \(r\ge2\), and every nonzero parameter \(t\). Homogeneous coordinates are \([X:Y:Z]\); on the affine chart \(X=1\) use \(y=Y/X\) and \(z=Z/X\). The unique geometric singular point is \([0:1:t^{1/4}]\), which is rational because the field is perfect. We exclude the exceptional nonintegral member at the parameter at infinity of the pencil and the parameter \(t=0\), which has different tangent geometry.

A *four-secant* is an \(\mathbb F_q\)-rational projective line containing four distinct \(\mathbb F_q\)-rational smooth points. This arithmetic notion does not count multiplicity-four contact at one point or Galois-conjugate intersections. The elliptic formula includes all \(t\) with \(t^3\ne1\), including small fields; no genericity hypothesis is imposed.

## Proof

**1. Rational points as an additive plane set.** In characteristic two the affine equation is

\[
z^4+y^2+z+t(y^4+z^2)=0.
\]

Define \(u=z+y^2\). Its equation is \(tu^2+u=z^4\). The fourth-power and square maps are bijections of \(\mathbb F_q\), so each \(u\in\mathbb F_q\) gives exactly one pair \((z,y)\). In particular the affine curve has exactly \(q\) rational points. With \(\alpha^8=t\), set \(u=w^8\). Taking fourth and then square roots gives the explicit bijective parametrization

\[
\boxed{(y,z)=(w^4+\alpha w^2+w,\ \alpha^2w^4+w^2),\qquad w\in\mathbb F_q.}
\]

Both coordinates are additive (\(\mathbb F_2\)-linear) functions of \(w\). The map is injective: from \((y,z)\) we recover \(w\) uniquely through \(w^8=z+y^2\). Thus the set of \(q\) affine rational points is an \(r\)-dimensional \(\mathbb F_2\)-linear subspace of \(\mathbb F_q^2\). All these points are smooth because \(\partial F/\partial Z=X^3\). The projective line \(X=0\) contains only the unique singular point.

**2. Intersection sizes and direction weights.** For an affine line \(ay+bz=c\) with \((a,b)\ne(0,0)\), substitution yields the additive polynomial equation

\[
(a+b\alpha^2)w^4+(a\alpha+b)w^2+aw=c.
\]

This polynomial cannot vanish identically: if its coefficient of \(w\) is zero, then \(a=0\) and its coefficient of \(w^2\) is \(b\ne0\). Its kernel therefore has size \(1\), \(2\), or \(4\), and every nonempty fiber is a coset of the kernel. Hence no projective line contains exactly three distinct smooth rational points, and every affine line has \(0\), \(1\), \(2\), or \(4\) such points.

A direction has *weight two* if the line of that direction through \((0,0)\) contains four points, i.e. three nonzero additive parameters. Otherwise it has weight one (two points) or zero (only the origin). The nonzero parameters yield \(q-1\) direction incidences. If \(s=s_4(t)\), then there are \(q-1-3s\) directions with two origin-line points and \(2+2s\) directions with only the origin. For any direction with kernel size \(k\), exactly \(q/k\) parallel affine lines meet the point set, each at \(k\) points. Counting the \(q(q+1)\) affine lines and adding the line \(X=0\) (zero smooth points) yields all five displayed formulas for \(N_j\).

**3. The cubic direction map.** For a nonzero parameter \(w\), the point's direction is its affine ratio \(m=y/z\), with \(m=\infty\) when \(z=0\). Cancelling \(w\) gives the separable degree-three rational map

\[
\phi_\alpha(w)=\frac{w^3+\alpha w+1}{\alpha^2w^3+w}.
\]

For finite \(m\), the preimage equation is

\[
A(m)w^3+B(m)w+1=0,
\quad A(m)=1+\alpha^2m,\quad B(m)=m+\alpha.
\]

Assume first \(\Delta\ne0\). At \(m_0=\alpha^{-2}\) the equation becomes linear and has exactly one rational solution; at \(m=\infty\) the denominator vanishes at \(w=0\) and twice at \(w=\alpha^{-1}\), and only the nonzero latter parameter contributes one point. Every other one of the \(q-1\) finite slopes has a separable cubic with \(0\), \(1\), or \(3\) rational roots: a repeated root would satisfy both \(Aw^3+Bw+1=0\) and \(Aw^2+B=0\), an impossibility. Denote the numbers of slopes of these three types by \(h_0,h_1,h_3\). Because there are \(q-1\) nonzero parameters, the two special directions each have one, and \(h_3=s\),

\[
h_0+h_1+h_3=q-1,\qquad h_1+3h_3=q-3,
\quad\text{so}\quad h_0=2+2s.
\]

**4. The quadratic resolvent and its elliptic model.** For a separable cubic \(w^3+pw+v=0\) in characteristic two, let its roots be \(w_1,w_2,w_3\), and set

\[
R=\frac{w_1^2w_2+w_2^2w_3+w_3^2w_1}{v}.
\]

The opposite cyclic expression equals \(R+1\), and the symmetric identities \(w_1+w_2+w_3=0\), \(\sum_{i<j}w_iw_j=p\), \(w_1w_2w_3=v\) imply

\[
R^2+R=1+\frac{p^3}{v^2}.
\]

A three-cycle fixes \(R\), while a transposition exchanges \(R\) with \(R+1\). Thus this Artin–Schreier equation splits over \(\mathbb F_q\) precisely when the cubic has either zero or three rational roots, not when it has exactly one. For the cubic above take \(p=B/A\) and \(v=1/A\), giving

\[
R^2+R=1+\frac{(m+\alpha)^3}{1+\alpha^2m}.
\]

Put \(d=\Delta/\alpha^2\), \(u=m+\alpha+d\), \(x=\alpha^{-4}u\), and replace \(R\) by \(R'=R+\alpha^{-1}(m+\alpha)\). Direct polynomial division in characteristic two transforms this equation into

\[
(R')^2+R'=x+\alpha^{-3}+\frac{e^3}{x}.
\]

With \(V=xR'\), this becomes the displayed Weierstrass equation for \(E_t\). Since \(\Delta\ne0\), one has \(e\ne0\). The partial derivatives show the cubic is nonsingular: \(F_V=x\), and at the only possible affine point with \(x=0\), namely \((0,0)\), one has \(F_x=e^3\ne0\); the point at infinity is smooth as well. Thus it is a genus-one curve with a rational point, i.e. an elliptic curve.

For the \(q-1\) finite slopes excluding \(m_0\), the resolvent has two rational points exactly when the cubic has zero or three rational roots. The smooth projective elliptic curve has additionally exactly two rational points over the two poles of the Artin–Schreier rational function: one above \(m_0\) (\(x=0\)) and one over \(m=\infty\). Therefore

\[
\#E_t(\mathbb F_q)=2(h_0+h_3)+2
=2(2+2s+s)+2=6+6s.
\]

Hasse's elliptic point-count bound gives the stated square-root estimate.

**5. The degenerate parameter.** If \(\Delta=0\), then \(\alpha^3=1\) and the exceptional finite direction \(m=\alpha\) has no finite nonzero parameter. For any other finite slope, setting \(v=\alpha w\) reduces its equation to

\[
v^3+v=\frac{\alpha}{m+\alpha}\ne0.
\]

For any root \(v\notin\{0,1\}\), the other two roots are rational together exactly when the separable quadratic \(U^2+vU+(v^2+1)=0\) splits; equivalently,

\[
\operatorname{Tr}_{\mathbb F_q/\mathbb F_2}(1+v^{-2})=0.
\]

Inversion and the invariance of trace under squaring show there are exactly \(q/2-1\) such roots \(v\) if \(r\) is odd, or \(q/2-2\) if \(r\) is even. Each completely split cubic contributes three roots, so the number of weight-two directions is respectively \((q-2)/6\) or \((q-4)/6\). This proves the exceptional formula and completes the theorem.

## Verification

The self-contained Python program `verify_secants.py` uses exact polynomial-basis arithmetic for \(\mathbb F_{2^r}\), for \(2\le r\le7\). For **all 246 nonzero field parameters across these six degrees**, it verifies the quartic parametrization, the possible direction weights, the exceptional closed formula, and the complete line-count distribution. For each nonexceptional parameter it independently counts points on the displayed Weierstrass cubic and checks the identity \(\#E_t=6+6s_4\). It reports `QUARTIC_FOUR_SECANTS_ELLIPTIC_RESOLVENT_PASS`. These finite tests are corroboration; the preceding argument proves the result for every \(r\ge2\).

## Relationship to prior work

Hilario and Stöhr introduced the pencil in *On regular but non-smooth integral curves*, Section 3, identifying its unique singular point and its striking geometric bitangent behavior (arXiv:2211.16962, first posted November 30, 2022). Their later articles classify the relevant families of quartics and describe their geometric tangent lines (arXiv:2306.08579; arXiv:2409.05464). None of these inspected results supplies this finite-field four-secant spectrum or the genus-one quadratic resolvent of its degree-three direction map. The general theory of Artin–Schreier quadratic extensions and cubic resolvents is used as standard background, not claimed as new. The new content is the explicit reduction and exact arithmetic count for this quartic pencil, including the exceptional parameter and all rational-line intersection numbers.

## Limitations

The theorem counts rational **smooth** intersections, not intersection multiplicities, scheme-theoretic line sections, or geometric secants defined over extension fields. It does not determine the full distribution of four-secants over varying extension fields with the parameter fixed, other than by reapplying the formula. The elliptic curve is auxiliary, not the normalization of the rational quartic. The singular-cubic boundary \(t^3=1\) is handled separately; no elliptic Hasse bound is asserted there. Historical equivalences in uncatalogued literature on characteristic-two linear sets or cubic resolvents have not been exhaustively excluded. There has been no independent mathematical validation.

## References

1. C. Hilario and K.-O. Stöhr, *On regular but non-smooth integral curves*, arXiv:2211.16962, Section 3 (first public preprint 2022-11-30): https://arxiv.org/abs/2211.16962 .
2. C. Hilario and K.-O. Stöhr, *Fibrations by plane quartic curves with a canonical moving singularity*, arXiv:2306.08579, Sections 4–5 (2023): https://arxiv.org/abs/2306.08579 .
3. C. Hilario and K.-O. Stöhr, *Fibrations by plane projective rational quartic curves in characteristic two*, arXiv:2409.05464, Sections 3–4 (2024): https://arxiv.org/abs/2409.05464 .

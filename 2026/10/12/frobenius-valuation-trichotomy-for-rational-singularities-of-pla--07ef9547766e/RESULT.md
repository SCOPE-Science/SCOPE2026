# Frobenius-valuation trichotomy for rational singularities of plane-filling curves

## Finding
Let \(q=p^e\) with \(e\geq1\), and let \(r\geq2\) be divisible by \(p\). For \(k\in\mathbb F_q\), consider the plane-filling curve \(C_{k,r}\subset\mathbb P^2_{\mathbb F_q}\) with homogeneous equation
\[
F=X^r(X^qY-XY^q)+Y^r(Y^qZ-YZ^q)+(Z^r+kX^r)(Z^qX-ZX^q)=0.
\]
Put \(s=p^{v_p(r)}\), \(h=r/s\) (so the reduction of \(h\) in \(\mathbb F_p\) is nonzero), and \(N=r^2+r+1\). Every \(\mathbb F_q\)-rational singular point is uniquely of the form
\[
P_t=[t^r:t^{r+1}:1],\qquad t\in\mathbb F_q^\times,\qquad k=t^{r+1}-t^{-r^2}.
\]
At \(P_t\), write local coordinates \(U=X/Z-t^r\) and \(V=Y/Z-t^{r+1}\). The local multiplicity is **exactly** \(\min(s,q)+1\), with the following complete tangent-cone classification.

**Subfield valuation, \(s<q\).** The point is an ordinary \((s+1)\)-fold point. In the slope coordinate \(V=tUz\), its distinct geometric tangent directions are exactly the \(s+1\) roots of
\[
z^{s+1}-z+t^{-N}=0.
\]
Consequently the local delta invariant is \(s(s+1)/2\); the number of \(\mathbb F_q\)-rational points in the local normalization above \(P_t\) is the number of roots of this displayed polynomial in \(\mathbb F_q\).

**Superfield valuation, \(s>q\).** The point is an ordinary \((q+1)\)-fold point, with initial form
\[
(t^r)^r(U^qV-UV^q).
\]
All \(q+1\) distinct tangent directions, and therefore all local normalization branches, are defined over \(\mathbb F_q\). The local delta invariant is \(q(q+1)/2\).

**Critical valuation, \(s=q\).** Write \(h=r/q\) (viewed modulo \(p\)) and \(\lambda=t^N\in\mathbb F_q^\times\). The point has multiplicity \(q+1\); in the slope coordinate \(V=tUz\), its tangent form is a nonzero scalar multiple of
\[
P_{h,\lambda}(z)=-h+\lambda\bigl((h+1)z-z^q-hz^{q+1}\bigr).
\]
It is ordinary if and only if
\[
h^2+\lambda(h+1)\neq0\quad\text{in }\mathbb F_q.
\]
If equality holds, \(P_{h,\lambda}\) has a root \(z_0=(h+1)/h\) of multiplicity \(q\), and another simple root \(z=-1/h\) when \(h+2\neq0\). If \(h+2=0\), the only root is \(z_0\), of multiplicity \(q+1\). In the ordinary critical case, the rational tangent/branch count is exactly the number of solutions of \(z(1-z)=\lambda^{-1}\) in \(\mathbb F_q\), hence at most two.

All three valuation regimes occur. The rational singularity \([1:1:1]\) is present for \(k=0\). The two exceptional critical tangent patterns are also realized: \((p,q,r,t)=(5,5,5,3)\) gives a fivefold tangent and one simple tangent, while \((3,3,3,1)\) gives one fourfold tangent.

## Assumptions and scope
The ground field is \(\mathbb F_q\), not necessarily a prime field; tangent factors and ordinary-multiple-point assertions are geometric, over an algebraic closure. Only singular points rational over \(\mathbb F_q\) are classified. The theorem does not assert that the whole curve is irreducible or nonsingular away from these points. Where an ordinary multiple point occurs, the local reduced curve has distinct smooth branches; statements about its local normalization refer to those branches.

## Proof
In the chart \(Z=1\), the curve has polynomial
\[
f(x,y)=x^r(x^qy-xy^q)+y^r(y^q-y)+(1+kx^r)(x-x^q).
\]
At every rational point \((a,b)\), all three Frobenius differences vanish. Its two first derivatives there are
\[
f_x(a,b)=1+a^r(k-b),\qquad f_y(a,b)=a^{r+1}-b^r.
\]
Their simultaneous vanishing forces \(a,b\neq0\), and with \(t=b/a\) gives \(a=t^r\), \(b=t^{r+1}\), and \(k=b-a^{-r}=t^{r+1}-t^{-r^2}\). No rational singular point lies on \(Z=0\): at a rational point of that line, the derivative along the line has coefficient \(X^{r+1}\), forcing \(X=0\); then the transverse derivative at \([0:1:0]\) equals \(1\). Thus the parametrization is exhaustive and injective.

Fix one such point and set \(a=t^r\), \(b=t^{r+1}\). Frobenius gives the exact local differences
\[
\begin{aligned}
x^qy-xy^q&=aV-bU+bU^q-aV^q+U^qV-UV^q,\\
y^q-y&=-V+V^q,\\
x-x^q&=U-U^q.
\end{aligned}
\]
The singular-point identities \(b^r=a^{r+1}\) and \(1+ka^r=a^rb\) cancel both their degree-one and degree-\(q\) constant-coefficient contributions. Since \(s=p^{v_p(r)}\), the first nonconstant term of \((a+U)^r\) is \(h a^{r-s}U^s\), and likewise for \((b+V)^r\).

When \(s<q\), the first nonzero homogeneous part is
\[
f_{s+1}=h\bigl(-a^{-s}U^{s+1}+a^{r-s+1}U^sV-b^{r-s}V^{s+1}\bigr).
\]
Substitute \(V=tUz\): by the displayed parametrization this becomes
\[
h t^{-rs}U^{s+1}\bigl[-1+t^N(z-z^{s+1})\bigr].
\]
The derivative of \(z^{s+1}-z+t^{-N}\) is \(z^s-1\). Its only geometric critical point is \(z=1\), where the polynomial equals \(t^{-N}\neq0\). The tangent cone therefore splits into \(s+1\) distinct geometric lines. By the standard ordinary-multiple-point local criterion, the point has that many smooth branches, local delta invariant \(\binom{s+1}{2}\), and rational branches precisely over rational tangent directions.

When \(s>q\), all coefficient variations start in degree greater than \(q\). After the noted cancellations, the first surviving part, in degree \(q+1\), is \(a^r(U^qV-UV^q)\). It has exactly one line for every slope in \(\mathbb P^1(\mathbb F_q)\): this is the ordinary \((q+1)\)-fold case, with \(\binom{q+1}{2}\) as its local delta invariant and \(q+1\) rational branches.

When \(s=q\), coefficient variations contribute in the same degree \(q+1\) as the mixed Frobenius term. Because \(a,b\in\mathbb F_q\), \(a^r=a^h\) and \(b^{r-q}=b^{h-1}\); the initial form is
\[
-h a^{-1}U^{q+1}+(h+1)a^hU^qV-a^hUV^q-hb^{h-1}V^{q+1}.
\]
Putting \(V=tUz\), and using \(t^q=t\), gives \(t^{-h}U^{q+1}P_{h,\lambda}(z)\). Its constant term \(-h\) is nonzero, so the multiplicity is exactly \(q+1\). Its derivative is \(\lambda((h+1)-hz^q)\), with unique critical root \(z_0=(h+1)/h\in\mathbb F_p\). Evaluation gives
\[
P_{h,\lambda}(z_0)=-\frac{h^2+\lambda(h+1)}{h}.
\]
Thus its tangent cone has distinct lines exactly outside the stated equality. At equality, translating \(z=z_0+w\) produces the exact factorization
\[
P_{h,\lambda}(z_0+w)=-\lambda w^q\bigl((h+2)+hw\bigr),
\]
which proves both repeated-root cases. Finally for \(z\in\mathbb F_q\), replace \(z^q\) with \(z\) to obtain \(P_{h,\lambda}(z)=h[-1+\lambda z(1-z)]\). This proves the critical rational tangent-count formula. All calculations hold for every prime power and every permitted exponent.

## Verification
The accompanying `verify.py` implements local polynomial arithmetic modulo primes, computes the truncated expansion of the **actual defining equation** at explicit rational singular points, checks that all lower terms vanish, and compares the full first nonzero homogeneous form with the formulas above. Its fourteen tests cover \(s<q\), \(s=q\), and \(s>q\) in characteristics two, three, five, and seven, including both types of critical repeated tangents. Execute `python verify.py` with the Python standard library. Successful execution prints `VERIFY_OK: exact truncated local coefficient identities and critical multiplicities in 14 cases`. The uniform derivation above, not those fourteen instances, proves the theorem.

## Relationship to prior work
Asgarli and Ghioca, *Plane-filling curves of small degree over finite fields* (arXiv:2307.03072, first submitted July 6, 2023), introduced \(C_{k,r}\) and in Theorem 1.8 established the condition for the absence of rational singularities. Their proof computes first derivatives, but it does not determine tangent cones, branch splitting, the valuation threshold \(s=q\), or the sharp repeated-tangent boundary. Their Conjectures 4.3–4.4 explicitly distinguish exponents prime to the characteristic; the present local theorem addresses the complementary regime without proving or refuting either conjecture.

Homma and Kim classified smooth plane-filling curves of minimum degree \(q+2\) (2013); their degree and smoothness assumptions do not give this higher-degree singularity classification. Earlier work on rational node/cusp splitting for the \(r=2\), odd-characteristic subfamily does not cover \(p\mid r\). The new assertion is the parameter-uniform higher-multiplicity and tangent-collision trichotomy, not the already published rational singular-point parametrization.

## Limitations
No statement is made about singularities defined only over extension fields, global geometric irreducibility, total normalization genus, or the numbers of local branches in the nonordinary critical collision cases. In particular, a repeated tangent direction alone does not determine analytic branch number or delta invariant. The local branch and delta assertions above apply only when the initial homogeneous form is squarefree. Unindexed prior calculations or a general singularity theorem that explicitly subsumes these same family-wide formulas remain a bibliographic priority risk; independent validation has not been performed.

## References
1. Shamil Asgarli and Dragos Ghioca, *Plane-filling curves of small degree over finite fields*, arXiv:2307.03072v1, submitted 2023-07-06. Author-posted complete text: https://personal.math.ubc.ca/~dghioca/papers/0706_plane_filling_curves.pdf .
2. Masaaki Homma and Seon Jeong Kim, *Nonsingular plane filling curves of minimum degree over a finite field and their automorphism groups: Supplements to a work of Tallini*, Linear Algebra and Its Applications 438 (2013), 969–985, DOI 10.1016/j.laa.2012.08.032.

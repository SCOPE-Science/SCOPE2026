# Sharp perimeter-normalized radial moments of centered parallelograms

## Finding

Let \(P\) be a nondegenerate Euclidean parallelogram of perimeter \(L\), area \(A\), and center \(o\). For every real \(p>0\) put
\[
I_p(P)=\int_{\partial P}\|x-o\|^p\,ds.
\]
For **every \(p\ge 2\)** the exact sharp envelope, with \(L\) fixed, is
\[
\boxed{I_p(P)\le \frac{L^{p+1}}{(p+1)4^p}.}
\]
For \(p>2\) the inequality is strict for every nondegenerate parallelogram, but the bound is attained in the Hausdorff-degenerate limit of flattened parallelograms. At \(p=2\) every parallelogram has the same value \(I_2=L^3/48\), a special case of earlier work on planar boundary moments. At fixed lengths of the two half-edge vectors, the moment is strictly maximized by perpendicular vectors when \(0<p<2\), independent of their angle at \(p=2\), and strictly increases with the absolute cosine of their angle when \(p>2\).

Define \(p_{\mathrm c}>2\) uniquely by
\[
\left(\frac{\pi}{2}\right)^{p_{\mathrm c}}=p_{\mathrm c}+1,
\qquad p_{\mathrm c}=3.1529558562\ldots.
\]
For the disk \(B_L\) of perimeter \(L\), centered at its center, \(I_p(B_L)=L^{p+1}/(2\pi)^p\). The sharp **universal disk comparison within the parallelogram family** is therefore
\[
\boxed{I_p(P)\le I_p(B_L)\text{ for every nondegenerate parallelogram }P
\ \Longleftrightarrow\ 0<p\le p_{\mathrm c}.}
\]
For \(p>p_{\mathrm c}\), arbitrarily thin nondegenerate parallelograms violate the disk bound. In particular every parallelogram obeys the unresolved general \(p=3\) disk-moment inequality with a uniform strict factor:
\[
I_3(P)\le \frac{\pi^3}{32}I_3(B_L),\qquad \frac{\pi^3}{32}<1.
\]
Two structural refinements hold. Writing the lengths of the centered half-edge vectors as \(a,b>0\) and their angle as \(\theta\), for \(2<p\le4\),
\[
I_p(P)\le \frac{4}{p+1}(a+b)^{p+1}
-\frac{2p(p-2)}3a^2b^2(a+b)^{p-3}\sin^2\theta.
\]
At the quartic exponent this is an *exact identity*:
\[
\boxed{I_4(P)=\frac{L^5}{1280}-\frac{LA^2}{12}.}
\]

## Assumptions and scope

The parallelogram is the convex hull of \(\pm u\pm v\) in the Euclidean plane, where \(u,v\) are nonparallel vectors, \(a=\|u\|>0\), \(b=\|v\|>0\), and \(\cos\theta=(u\cdot v)/(ab)\in(-1,1)\). Its center, also its arclength centroid, is \(o=0\). Its perimeter and area are \(L=4(a+b)\) and \(A=4ab|\sin\theta|\). Integrals are Euclidean arclength integrals over the once-traversed boundary. Needle configurations appear only as limiting bodies with perimeter counted with multiplicity two; they are not nondegenerate equality cases.

## Proof

**1. Exact reduction.** Two opposite edges are parameterized by \(\pm u+t v\), and the other two by \(\pm v+t u\), for \(-1\le t\le1\). If \(c=\cos\theta\), elementary arclength integration gives
\[
\begin{aligned}
F_p(c):=I_p(P)&=2b\int_{-1}^{1}
(a^2+b^2t^2+2abct)^{p/2}\,dt\\
&\quad+2a\int_{-1}^{1}
(b^2+a^2t^2+2abct)^{p/2}\,dt.
\end{aligned}
\]
The expression is even in \(c\), by replacing \(t\) with \(-t\).

**2. Angular extremum and its exact value.** For \(p>2\), the function \(q\mapsto q^{p/2}\) is strictly convex on the nonnegative half-line; the integrands depend affinely on \(c\). As \(a,b>0\), integration over nonzero \(t\) makes \(F_p\) strictly convex and even on \([-1,1]\). Consequently \(F_p(c)<F_p(1)=F_p(-1)\) for \(-1<c<1\). When \(0<p<2\), strict concavity gives instead the unique maximum at \(c=0\); when \(p=2\), even affine dependence makes \(F_2\) constant.

For the endpoint \(c=1\), suppose without loss of generality \(a\ge b\). Direct integration yields, for every \(p>0\),
\[
\begin{aligned}
F_p(1)&=2b\int_{-1}^1|a+bt|^p\,dt
+2a\int_{-1}^1|b+at|^p\,dt\\
&=\frac{2}{p+1}\Bigl[(a+b)^{p+1}-(a-b)^{p+1}
+(a+b)^{p+1}+(a-b)^{p+1}\Bigr]\\
&=\frac4{p+1}(a+b)^{p+1}.
\end{aligned}
\]
The cancellation makes the flattened-limit answer independent of side-length ratio. Substituting \(L=4(a+b)\) proves the sharp envelope for \(p\ge2\). The endpoint is approachable with both \(a,b\) fixed and \(|c|\uparrow1\). At \(p=2\), affine dependence gives equality for all angles, namely \(I_2=L^3/48\).

**3. The full disk-comparison cutoff.** For \(0<p<2\), Hölder's inequality together with the exact \(p=2\) identity gives
\[
I_p(P)\le L^{1-p/2}I_2(P)^{p/2}
=\frac{L^{p+1}}{48^{p/2}}
<\frac{L^{p+1}}{(2\pi)^p},
\]
because \(2\pi<\sqrt{48}\). For \(p\ge2\), the sharp envelope-to-disk ratio is
\[
R(p)=\frac{(\pi/2)^p}{p+1}.
\]
It is strictly increasing on \([2,\infty)\), because
\[
\frac{d}{dp}\log R(p)=\log(\pi/2)-\frac{1}{p+1}>0.
\]
The inequality follows, for example, from \(\log(\pi/2)>1/3\). We have \(R(3)<1<R(4)\), so there is exactly one cutoff \(p_{\mathrm c}\in(3,4)\). For larger exponents the sharp envelope exceeds the disk value, and continuity in the angle supplies genuine nondegenerate counterexamples. For smaller exponents the disk bound holds; at the cutoff it is strict for nondegenerate parallelograms. Taking \(p=3\) gives the claimed uniform factor \(\pi^3/32\).

**4. Quantitative angular loss.** For \(2<p\le4\), put \(\alpha=p/2\). Every squared norm in the integrands of Step 1 is at most \((a+b)^2\). Since \(\alpha-2\le0\),
\[
\frac{d^2}{dq^2}q^\alpha
=\alpha(\alpha-1)q^{\alpha-2}
\ge\alpha(\alpha-1)(a+b)^{p-4}.
\]
Differentiating under the integrals therefore gives
\[
F_p''(c)\ge\frac{16}{3}\alpha(\alpha-1)a^2b^2(a+b)^{p-3}.
\]
Evenness gives \(F_p'(0)=0\); integrate the curvature bound from \(|c|\) to \(1\) to obtain
\[
F_p(1)-F_p(c)\ge\frac{2p(p-2)}{3}a^2b^2(a+b)^{p-3}(1-c^2).
\]
For \(p=4\), the squared-norm power is quadratic, so the second derivative is constant and this inequality is equality. Using \(A^2=16a^2b^2(1-c^2)\) and \(a+b=L/4\) yields the exact quartic identity.

## Verification

The self-contained standard-library program `check.py` derives the second and fourth moment identities by exact rational polynomial integration. It independently evaluates the edge integrals by Simpson quadrature at nonintegral exponents, checks the quantitative angular remainder, brackets the unique critical exponent, and checks both sides of the disk transition on genuinely nondegenerate examples. Running `python check.py` produces `ALL_CHECKS_PASSED`. Finite computations illustrate the formulas; the universal statements follow from the proof above, not from the numerical tests.

## Relationship to prior work

Dietze, Kachmar and Lotoreichik (arXiv:2311.18413, first publicly posted November 30, 2023) proved disk upper bounds for boundary moments at exponents at most two and formulated the exponent-three inequality as an open conjecture for broad curve classes. Their Proposition 5.3 uses a doubly covered interval to show failure at sufficiently high exponent; it does not give the sharp continuous parallelogram envelope or the complete family-specific threshold.

Csató, Giovagnoli and Roy (arXiv:2608.19851, posted August 20, 2026) recount Sachs's classical second-moment result and prove *lower* sharp bounds for exponents up to two in symmetric convex-curve families. They do not establish this *upper* envelope at exponents greater than two. Their results explain why the exponent-two value is prior knowledge, not a new claim here. Saracco and Stefani (arXiv:2306.07770, posted June 13, 2023) analyze weighted-perimeter monotonicity under inclusion, rather than optimization over equal-perimeter parallelograms. Csató and Giovagnoli (arXiv:2610.11677, posted October 8, 2026) likewise study continuity and inclusion monotonicity, not this moment maximum. The sharp cutoff, the fourth-moment area correction, and the reversal of angular extremizers are the claimed distinctions.

## Limitations

This is a classification **only for Euclidean parallelograms** and their flattening limits. It does not resolve the unrestricted exponent-three conjecture or imply an exponent threshold for general convex curves. The bound is sharp as a supremum, not attained by a nondegenerate parallelogram for exponents strictly exceeding two. Historical priority of these specific formulas has not been independently certified; older sources under different moment or wire-inertia terminology may contain equivalent formulas. No finite-sample or statistical claims are made.

## References

1. C. Dietze, A. Kachmar and V. Lotoreichik, *Isoperimetric inequalities for inner parallel curves*, arXiv:2311.18413, first version November 30, 2023, especially Section 5 and Conjecture 1.4. https://arxiv.org/abs/2311.18413
2. G. Csató, D. Giovagnoli and P. Roy, *Weighted Perimeters and pth Moments of Inertia of Convex Curves and Surfaces*, arXiv:2608.19851, first version August 20, 2026, especially Introduction, Corollary 1.5, and Section 3. https://arxiv.org/abs/2608.19851
3. G. Saracco and G. Stefani, *On the monotonicity of weighted perimeters of convex bodies*, arXiv:2306.07770, first version June 13, 2023. https://arxiv.org/abs/2306.07770
4. G. Csató and D. Giovagnoli, *Continuity and monotonicity of weighted perimeters of convex bodies*, arXiv:2610.11677, first version October 8, 2026. https://arxiv.org/abs/2610.11677

# Strict Bézout-witness monotonicity for translated Euclidean-ball lenses

## Finding
For every integer \(n\ge2\), put \(U=B_2^n\), \(A_a=[0,2a e_1]\), and \(L_a=U\cap(U-2a e_1)\), for \(0<a<1\). Denote the volume of the Euclidean unit ball in dimension \(j\) by \(\kappa_j=\pi^{j/2}/\Gamma(j/2+1)\), with \(\kappa_0=1\). Define the normalized two-auxiliary-body Bézout quotient
\[
R_n(a)=\frac{\kappa_n V_n(U[n-2],A_a,L_a)}{V_n(U[n-1],A_a)\,V_n(U[n-1],L_a)}.
\]
Here \(V_n\) is the symmetric multilinear mixed volume, and \(U[k]\) denotes \(k\) repeated arguments.

**Theorem.** The function \(R_n\) is strictly increasing for \(0<a<1\), and its exact range is
\[
1<R_n(a)<C_n=\frac{n}{n-1}\frac{\kappa_n\kappa_{n-2}}{\kappa_{n-1}^2},
\qquad \lim_{a\downarrow0}R_n(a)=1,\quad \lim_{a\uparrow1}R_n(a)=C_n.
\]
Both endpoint limits are excluded from the domain. Independently, \(C_n\) is the exact optimal coefficient in
\[
\kappa_n V_n(U[n-2],A,B)\le C_n V_n(U[n-1],A)V_n(U[n-1],B)
\]
when \(A\) and \(B\) are **zonoids**, including lower-dimensional ones. Equality is achieved by any pair of mutually orthogonal nondegenerate line segments. Thus the canonical axial-lens witnesses asymptotically approach the sharp coefficient of an independent zonoid inequality.

## Assumptions and scope
A convex body is a nonempty compact convex set, possibly lower dimensional. A zonoid is a Hausdorff limit of finite Minkowski sums of line segments. The lens \(L_a\) has nonempty interior exactly for \(0<a<1\). Its translation by \(a e_1\) is the symmetric lens \(\widetilde L_a=B_2^n(a e_1,1)\cap B_2^n(-a e_1,1)\). Translation invariance makes both lenses interchangeable in mixed volumes. The ambient body is the Euclidean unit ball; no bound for all ambient convex bodies or all non-zonoid auxiliary test bodies is asserted.

## Proof
**1. Axial mixed volumes.** Put \(r=\sqrt{1-a^2}\). The orthogonal projection of \(\widetilde L_a\) onto \(e_1^\perp\) is \(rB_2^{n-1}\). The standard projection identity
\[
n V_n(K_1,\ldots,K_{n-1},[0,e_1])=V_{n-1}(P_{e_1^\perp}K_1,\ldots,P_{e_1^\perp}K_{n-1})
\]
gives, with homogeneous scaling of \(A_a\),
\[
V_n(U[n-1],A_a)=\frac{2a\kappa_{n-1}}n,
\qquad
V_n(U[n-2],A_a,L_a)=\frac{2ar\kappa_{n-1}}n.
\]
Consequently \(R_n(a)=r/M_n(a)\), where \(M_n(a)=V_n(U[n-1],L_a)/\kappa_n\) is the normalized mean support function of the translated symmetric lens.

**2. Exact angular reduction.** For a unit normal \(u\), set \(t=|u_1|\). Maximizing the linear support functional over the intersection of two balls, with the closest ball constraint active, gives
\[
h_{\widetilde L_a}(u)=\begin{cases}r\sqrt{1-t^2},&0\le t\le a,\\1-at,&a\le t\le1.\end{cases}
\]
The two branches agree at \(t=a\). The spherical distribution of \(|u_1|\) has density \(c_n(1-t^2)^{(n-3)/2}\), with \(c_n=2(n-1)\kappa_{n-1}/(n\kappa_n)\). Since the surface area measure of \(U\) is ordinary spherical measure, integration of this support function gives
\[
M_n(a)=c_n\left[r\int_0^a(1-t^2)^{(n-2)/2}\,dt+\int_a^1(1-at)(1-t^2)^{(n-3)/2}\,dt\right].
\]
Hence, after division by \(r\),
\[
R_n(a)^{-1}=c_n\left[\int_0^a(1-t^2)^{(n-2)/2}\,dt+\frac1r\int_a^1(1-at)(1-t^2)^{(n-3)/2}\,dt\right].\tag{1}
\]
The integral is proper in the interior and finite at the endpoints even when \(n=2\), where the weight is integrable.

**3. Strict monotonicity.** Differentiate (1) for \(0<a<1\). The lower and upper moving-endpoint terms cancel exactly, because \((1-a^2)^{(n-2)/2}=r(1-a^2)^{(n-3)/2}\). The remaining derivative is
\[
\frac{d}{da}R_n(a)^{-1}=\frac{c_n}{r^3}\int_a^1(a-t)(1-t^2)^{(n-3)/2}\,dt<0.\tag{2}
\]
The integrand is strictly negative for \(a<t<1\), with a positive integrable weight. Thus \(R_n\) increases strictly. At \(a\downarrow0\), the centered lens tends to \(U\), so \(M_n(a)\to1\), \(r\to1\), and \(R_n(a)\to1\). At \(a\uparrow1\), the second term of (1) vanishes (use \(0\le 1-at\le1-a^2=r^2\) on \([a,1]\)), and
\[
\int_0^1(1-t^2)^{(n-2)/2}\,dt=\frac{\kappa_{n-1}}{2\kappa_{n-2}}.
\]
It follows that \(R_n(a)^{-1}\to c_n\kappa_{n-1}/(2\kappa_{n-2})=C_n^{-1}\). Strict increase from the value \(1\) implies \(C_n>1\).

For concrete dimension checks, the closed forms are
\[
R_2(a)=\frac{\pi\sqrt{1-a^2}}{2\arccos a},\quad C_2=\frac\pi2;
\qquad
R_3(a)=\left(\sqrt{\frac{1-a}{1+a}}+\tfrac12\arcsin a\right)^{-1},\quad C_3=\frac4\pi.
\]

**4. Sharp zonoid coefficient.** For nonzero vectors \(v,w\), two applications of the segment projection identity yield
\[
\begin{split}
V_n(U[n-1],[0,v])&=\frac{\kappa_{n-1}}n\|v\|,\\
V_n(U[n-2],[0,v],[0,w])&=\frac{\kappa_{n-2}}{n(n-1)}\|v\wedge w\|.
\end{split}
\]
Consequently, the quotient of the mixed-volume expressions for these two segments is \(C_n\|v\wedge w\|/(\|v\|\|w\|)\le C_n\), with equality exactly for perpendicular directions. By mixed-volume multilinearity, the inequality extends termwise to finite Minkowski sums of segments. It extends to zonoids by Hausdorff continuity. Orthogonal unit segments attain equality, so the coefficient cannot be lowered. Comparison with the limit in step 3 proves the claimed asymptotic coincidence.

## Verification
The analytic proof establishes all dimensions and all \(0<a<1\); numerical checks do not substitute for steps 1–4. The standalone `verify.py` uses only the Python standard library and non-singular angular substitutions to verify the exact integral expression, strict derivative sign, monotonic samples, sharp endpoint consistency, and the two elementary closed forms in dimensions \(2\) and \(3\). Run `python3 verify.py`; successful output is `VERIFY_OK`.

## Relationship to prior work
Langharst and Wang (2026, arXiv:2609.20380v1) prove that a Bézout inequality tested specifically on \(A=[0,x]\) and \(B=K\cap(K-x)\), for every admissible nonzero displacement, characterizes simplices. Their theorem motivates evaluating the strength of those **canonical witnesses** at a non-simplex, and the proof does not compute an exact Euclidean-ball ratio or its monotonicity.

An earlier published exact mean-width calculation for symmetric two-ball lenses provides the two-branch support function and angular mean-width evaluation used in step 2. Neither the individual decreasing mean-width statement nor the universal simplex characterization states the strict monotonicity of the *mean width divided by transverse radius*, which is the extra property in equation (2), or the exact matching with the zonoid extremal coefficient. The original contribution here is this normalized monotonicity-and-extremal-link theorem, **not** a claim to have discovered the lens support function or its mean width. Averkov and Soprunov (2025) establish a three-dimensional inequality for arbitrary zonoid ambient and auxiliary bodies with a coarser coefficient; their theorem does not determine this all-dimensional Euclidean-ball canonical lens trajectory.

## Limitations
The result applies only to the unit ball with axial overlap lenses and to the separate sharp zonoid restriction. Although the limiting constant is sharp for two zonoid auxiliary bodies, nothing here determines the optimal coefficient for two unrestricted convex auxiliary bodies. No finite positive lens separation attains the limiting constant. Exact lens mean width was previously available, so only the new normalized monotonicity and Bézout interpretation are claimed as an extension. Unindexed earlier derivations of that normalized statement remain a residual originality risk; the independent validation of this calculation has not been carried out.

## References
1. D. Langharst and S. Wang, *The Bézout inequality for mixed volumes characterizes simplices*, arXiv:2609.20380v1, first publicly available 2026-09-17.
2. *Mean width of a symmetric lens in every dimension*, published mathematical research record, 2026. Exact support-function and mean-width formulas as cited above.
3. G. Averkov and I. Soprunov, *An Algebraic-Combinatorial Proof of a Bézout-Type Inequality for Mixed Volumes of Three-Dimensional Zonoids*, *Discrete & Computational Geometry*, first published 2025-05-23, DOI 10.1007/s00454-025-00745-2.
4. R. Schneider, *Convex Bodies: The Brunn–Minkowski Theory*, 2nd ed., Cambridge University Press, 2014, mixed-volume projection identities.

# Complete rotation-number distribution and critical winding-time tails in a polygonally foliated square map

## Finding
For the resonant piecewise-affine square maps of Ostrovski, the invariant outer annulus has a **closed, piecewise-quadratic cumulative distribution for every rotation number**, followed by a sharp reciprocal-rotation tail. Fix an integer \(K\ge3\). With the quantities defined below, set \(d_K=1-2s_K>0\), \(q_N=(1+Nd_K)^{-1}\),
\[
H_K=\sum_{j=0}^{K-1}\det(v_j,v_{j+1})+v_K\mathbin{\cdot}v_0,\qquad W_K=4t_K-2H_K>0.
\]
Under normalized planar Lebesgue area on the invariant outer annulus, the reciprocal rotation number \(\mathcal T_K=1/\rho_K\) obeys, for every integer \(N\ge0\),
\[
\Pr\{\mathcal T_K\ge4(K+N)\}
=\frac{4t_Kq_N-2H_Kq_N^2}{W_K}.
\]
Consequently, with \(D_K=16t_K/(d_KW_K)>0\),
\[
\Pr\{\mathcal T_K>u\}=\frac{D_K}{u}+O_K(u^{-2})\quad(u\to\infty),
\]
\[
\mathbb E[\mathcal T_K^p]<\infty\ \Longleftrightarrow\ 0\le p<1,
\qquad \mathbb E[\min(\mathcal T_K,L)]=D_K\log L+O_K(1).
\]
More precisely, the full continuous rotation-number law is explicit. Put \(r_N=1/[4(K+N)]\). For \(r\in[r_{N+1},r_N]\), define
\[
q(r)=q_{N+1}+\frac{r-r_{N+1}}{r_N-r_{N+1}}(q_N-q_{N+1}).
\]
Then the probability distribution function of the rotation number is **exactly**
\[
\nu_K\{X:\rho_K(X)\le r\}
=\frac{4t_K q(r)-2H_Kq(r)^2}{W_K},
\quad 0<r\le\frac1{4K}.
\]
It extends continuously by zero at \(r=0\) and by one above \(1/(4K)\). In the interior of each interval \((r_{N+1},r_N)\), its density is
\[
\frac{4t_K-4H_Kq(r)}{W_K}\,\frac{4d_K(K+N)(K+N+1)}{(1+Nd_K)(1+(N+1)d_K)}.
\]
It is therefore absolutely continuous on the open rotation-number range, with finite, nonzero limiting density \(D_K\) at zero.

The unnormalized leading coefficient \(C_K=D_KW_K=16t_K/d_K\) has a second, resonant-parameter asymptotic as \(K\to\infty\):
\[
C_K=4K^2-\frac{32}{3}K+\frac{128}{45}+O(K^{-1}).
\]
These are distributions of **inverse rotation numbers**, not distributions of first-return times or of a noninteger physical period.

## Assumptions and scope
Let \(\mathcal S=[0,1]^2\), \(Z=(1/2,1/2)\), and \(R(x,y)=(1-y,x)\). The map \(F_\theta:\mathcal S\to\mathcal S\) is the nine-piece, continuous, area-preserving map defined by the corresponding affine partitions in Ostrovski [1, Section 2]. For each integer \(K\ge3\), select the resonant \(\theta_K\in(0,\pi/4)\) characterized in [1, Lemma 5.2] by \(B_K^K P_4=P_1\), where
\[
t_K=\sin^2\theta_K,\quad s_K=\sin\theta_K\cos\theta_K,\quad
P_4=(t_K,1-s_K),\quad P_1=(s_K,t_K),
\]
and where the corner matrix is
\[
B_K=\frac1{t_K-s_K}\begin{pmatrix}
t_K^2-(1-s_K)^2&(1-2s_K)t_K\\
(2s_K-1)t_K&(2t_K-1)t_K
\end{pmatrix}.
\]
Set \(v_j=B_K^jP_4\) for integers \(0\le j\le K\); in particular \(v_K=P_1\). The established invariant polygon \(\Gamma_K^N\) has \(4(K+N)\) vertices, rotation number \(1/[4(K+N)]\), and quarter-polygon trajectory from \(q_Nv_0\) along \(q_Nv_1,\ldots,q_Nv_K\), then along a straight shear line to \(R(q_Nv_0)\). The shear-line intermediate vertices are collinear and do not affect area. These invariant polygons are nested and bound a fully foliated annulus \(\Omega_K=\operatorname{int}(\mathcal S)\setminus\operatorname{int}(\Gamma_K^0)\) [1, Theorem 5.1 and Corollary 5.4]. Its normalized area probability is \(\nu_K(A)=\operatorname{area}(A\cap\Omega_K)/\operatorname{area}(\Omega_K)\). The function \(\rho_K(X)\) is the rotation number of the unique invariant polygonal circle through \(X\) in this foliation; boundary circles and measure-zero ambiguities may be defined arbitrarily. All asymptotics in \(u\) fix \(K\), and all asymptotics in \(K\) concern only this resonant sequence.

## Proof
**1. Exact vertices.** The shear on the first side is \(A(x,y)=(x+(1-2s_K)y/t_K,y)\). Lemma 5.3 of [1] identifies the intersection of \(\Gamma_K^N\) with \(\overline{E_1P_1}\) as \(Y_N=q_NP_1\). The corner map is linear and \(B_K^KP_4=P_1\), hence its preimage is \(X_N=q_NP_4\). The first \(K\) polygon edges have endpoints \(q_Nv_j\); the next \(N\) shear steps are collinear and end at \(R(q_Nv_0)\). Rotating these edges through the four powers of \(R\) gives the entire Jordan polygon. The orbit itinerary and absence of self-intersections are provided by the invariant-circle construction in [1], not inferred from mere finite iteration.

**2. Shoelace calculation.** For \(q\in(0,1]\), form the closed polygon with quarter vertices \(qv_0,\ldots,qv_K,R(qv_0)\) and their three rotated copies. Write \(\det(a,b)=a_1b_2-a_2b_1\). Summing all oriented edge determinants over the four quarter-turns, using the center \(Z\), yields the area
\[
2q^2\sum_{j=0}^{K-1}\det(v_j,v_{j+1})
+2(qv_K-Z)\mathbin{\cdot}(qv_0-Z)
+2q\det(Z,v_0-v_K).
\]
Here \(\det(a,Jb)=a\cdot b\) for the counterclockwise quarter-turn linear part \(J\). Since \(v_0=(t_K,1-s_K)\), \(v_K=(s_K,t_K)\), we have
\[
2\det(Z,v_0-v_K)-2Z\mathbin{\cdot}(v_0+v_K)=-4t_K,
\]
while \(2Z\cdot Z=1\). Thus
\[
\operatorname{area}(\operatorname{int}\Gamma_K^N)
=1-4t_Kq_N+2H_Kq_N^2.
\]
All noncorner shear vertices lie on already counted straight edges. It follows that the square area *outside* \(\Gamma_K^N\) is exactly \(P_N=4t_Kq_N-2H_Kq_N^2\). At \(N=0\) this is \(W_K\), the positive area of the nonempty outer annulus.

**3. Complete rotation-number law and tail.** The interpolation statement following Theorem 5.1 in [1] proves that between \(\Gamma_K^N\) and \(\Gamma_K^{N+1}\) every invariant circle has the same parallel-edge polygonal pattern, and its rotation number varies linearly with the intersection point \(qP_1\) on the break line. Because this point varies linearly in \(q\), the law \(q=q(r)\) on each interval \([r_{N+1},r_N]\) is exactly the displayed affine formula. The corner vertices for a continuously interpolating invariant circle are \(qv_0,\ldots,qv_K\); its remaining shear segment still lies on the line joining \(qv_K\) and \(R(qv_0)\). Thus the same area polynomial \(4t_Kq-2H_Kq^2\) applies to **every** such level curve, not only the distinguished integer levels. The area lying farther outward corresponds to \(\rho_K\le r\), proving the claimed complete distribution function. Differentiation gives the stated density and \(dq/dr=(q_N-q_{N+1})/(r_N-r_{N+1})\). Since \(dq/dr\to4/d_K\) as \(N\to\infty\), its density tends to \(D_K=16t_K/(d_KW_K)\) at zero.

By [1, Corollary 5.4], rotation numbers decrease monotonically and continuously as invariant circles move from \(\Gamma_K^0\) to the square boundary. Therefore the event \(\mathcal T_K\ge4(K+N)\), modulo zero-area level curves, is precisely the part of \(\Omega_K\) outside \(\Gamma_K^N\). Its probability is \(P_N/W_K\), proving the exact discrete-threshold identity. As \(N\to\infty\),
\[
q_N=\frac1{Nd_K}+O_K(N^{-2}),\quad
P_N=\frac{4t_K}{d_KN}+O_K(N^{-2}),\quad u_N=4(K+N).
\]
Thus \(P_N/W_K=D_K/u_N+O_K(u_N^{-2})\). For real \(u\) between consecutive \(u_N\) values, monotonicity sandwiches the tail between its two exact levels, which differ by \(O_K(u^{-2})\). This proves the continuous-\(u\) expansion. For \(p>0\), the tail formula \(\mathbb E[\mathcal T_K^p]=p\int_0^\infty u^{p-1}\Pr(\mathcal T_K>u)\,du\) establishes the claimed cutoff; \(p=0\) is immediate. The integrated survival identity gives \(\mathbb E[\min(\mathcal T_K,L)]=\int_0^L\Pr(\mathcal T_K>u)du=D_K\log L+O_K(1)\).

**4. Resonant scaling.** Write \(t=t_K=1/2-\delta\), \(s=\sqrt{t(1-t)}\), and \(f=\sqrt{1-4t^2}\). The expanding eigenvalue and the ratio of expanding eigen-coordinates of \(P_1,P_4\) from [1, Appendix, equations (6.2)--(6.4)] are
\[
\lambda(t)=\frac{4t^2-2t+(2s-1)(1+f)}{2(t-s)},\qquad
\Xi(t)=\frac{2ts+t(f-1)}{2t^2+(1-s)(f-1)},\qquad
K=\frac{\log\Xi(t)}{\log\lambda(t)}.
\]
Expanding the displayed algebraic functions for \(\delta\downarrow0\) (both logarithms are positive and the denominators have removable leading-order cancellations) gives
\[
\log\lambda=2\delta^{3/2}+\delta^{5/2}+\frac{11}{4}\delta^{7/2}+O(\delta^{9/2}),
\quad \log\Xi=2\delta^{1/2}+\frac53\delta^{3/2}+\frac{43}{20}\delta^{5/2}+O(\delta^{7/2}).
\]
Long division and inversion therefore give
\[
K=\delta^{-1}+\frac13-\frac7{15}\delta+O(\delta^2),\quad
\delta=K^{-1}+\frac1{3K^2}-\frac{16}{45K^3}+O(K^{-4}).
\]
Finally \(1-2s=1-\sqrt{1-4\delta^2}=2\delta^2+2\delta^4+O(\delta^6)\). Substitute this and \(t=1/2-\delta\) into \(C_K=16t/(1-2s)\) to obtain \(C_K=4K^2-(32/3)K+128/45+O(K^{-1})\), as asserted. Algebraic Taylor series and inversion are valid near the positive real branch \(\delta=0\), with \(K\to\infty\) supplied by [1, Lemma 5.2].

**5. Explicit smallest resonance.** At \(K=3\), \(\theta_3=\pi/8\), \(t_3=(2-\sqrt2)/4\), \(s_3=\sqrt2/4\), and direct multiplication of \(B_3\) yields \(H_3=(5\sqrt2-7)/4\), \(W_3=(11-7\sqrt2)/2\), and \(C_3=8\). Hence the leading conditional tail coefficient is \(D_3=16/(11-7\sqrt2)\), agreeing with the general formulas.

## Verification
Run `python verify.py` from the same directory. It uses standard-library bisection of the resonant equation, direct polygon vertices and a separate shoelace sum, and checks against the formula for \(K\in\{3,4,5,7,10,20\}\) and \(N\in\{0,1,2,7,30,100\}\); it also checks the exact \(K=3\) identities and a finite large-\(K\) asymptotic comparison. The recorded result is `VERIFY_OK 36`. These tests are floating-point consistency checks only. The proof of all \(K,N\), the power-law tail, and the resonant asymptotic is analytical and does not rely on enumerating examples.

## Relationship to prior work
Ostrovski [1, Theorem 5.1, Corollary 5.4, Appendix] supplies the map, polygonal invariant circles, their rotation numbers, the shear-vertex formula, and the implicit resonant parameter equation. Those are credited input, not newly claimed results. The contribution here is their **Lebesgue-area pushforward**: the complete piecewise-quadratic rotation-number law (not just a single polygon area), the reciprocal-winding-time Pareto tail and sharp moment threshold, and its two-scale resonant coefficient. A separate earlier exact area calculation for the innermost polygon supplies only the endpoint normalization and not the full distribution of rotation levels; this overlap is acknowledged rather than counted as novelty. Ostrovski's thesis [2, Chapter 5] treats the same map and geometry without giving this distribution. Lagarias and Rains [3] study a different homogeneous planar piecewise-linear family with invariant rays and a distinct rotation-number problem. Bullett [4] treats a different piecewise-linear twist-map family; complete priority exclusion from that source was not obtained.

## Limitations
The distribution law concerns the distinguished resonant angles and the outer invariant annulus only. The observable is reciprocal circle rotation number, not an individual orbit's first-return time, primitive period, or an ergodic average over a specified section. The tail constant is conditional on normalized annulus area; \(C_K\) denotes the unnormalized leading coefficient. No result is claimed for nonresonant parameters or for points inside \(\Gamma_K^0\). A novelty search does not establish absolute priority; particularly, a corresponding calculation hidden in earlier piecewise-affine dynamics literature remains a risk.

## References
[1] G. Ostrovski, *Dynamics of a Continuous Piecewise Affine Map of the Square*, arXiv:1305.4282v1, first submitted 2013-05-18, Sections 2, 5 and Appendix. https://arxiv.org/html/1305.4282v1

[2] G. Ostrovski, doctoral thesis, 2013, Chapter 5, https://ostrovski.co.uk/data/thesis.pdf

[3] J. C. Lagarias and E. Rains, *Dynamics of a family of piecewise-linear area-preserving plane maps I. Rational rotation numbers*, arXiv:math/0301294, 2003. https://arxiv.org/abs/math/0301294

[4] S. R. Bullett, *Invariant circles for the piecewise linear standard map*, Commun. Math. Phys. 107 (1986), 241--262. Bibliographic comparison only, not a full-text clearance.

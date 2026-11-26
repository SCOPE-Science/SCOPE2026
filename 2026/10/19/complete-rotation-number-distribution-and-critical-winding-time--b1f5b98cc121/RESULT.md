# Exact rotation-number distribution and critical winding-time tails in a polygonally foliated square map

## Finding

Fix a resonant index \(K\ge3\) for Ostrovski's area-preserving piecewise-affine square map. Use the map parameters \(t=t_K\), \(s=s_K\) defined below and put \(d=1-2s>0\), \(h=1-Kd\). The outer invariant annulus has area \(W=2t(2-h)\). Under its normalized area measure, the cumulative law of the rotation number \(\rho\) is exactly
\[
 \Pr\{\rho\le r\}=\frac{x(2+hx)}{(2-h)(1+hx)^2},\qquad x=4r/d,\qquad 0\le r\le 1/(4K).
\]
The CDF is zero below this range and one above it. In its open range it has density
\[
 \frac{8}{d(2-h)}\left(1+\frac{4hr}{d}\right)^{-3}.
\]
In particular, the law is generally rational, not piecewise quadratic: the level-curve coordinate \(q\) is related to rotation number by \(q=4r/(d+4hr)\).

For the reciprocal rotation number \(\mathcal T=1/\rho\), with \(q_N=(1+Nd)^{-1}\) and \(H=th\), the distinguished thresholds obey
\[
 \Pr\{\mathcal T\ge4(K+N)\}=\frac{4tq_N-2Hq_N^2}{W}\quad(N=0,1,\ldots).
\]
For real \(u\ge4K\) the survival probability is given by the CDF above at \(r=1/u\). Thus
\[
 \Pr\{\mathcal T>u\}=D_K/u+O_K(u^{-2}),\qquad D_K=\frac{16t}{dW}>0,
\]
\[
 \mathbb E[\mathcal T^p]<\infty\quad\Longleftrightarrow\quad p<1\quad(p\in\mathbb R),\qquad
 \mathbb E[\min(\mathcal T,L)]=D_K\log L+O_K(1).
\]
The unnormalized leading coefficient along the resonant sequence satisfies
\[
 C_K=D_K W=\frac{16t_K}{d_K}=4K^2-\frac{32}{3}K+\frac{128}{45}+O(K^{-1}).
\]

## Assumptions and scope

Let \(\mathcal S=[0,1]^2\), \(R(x,y)=(1-y,x)\), and \(F_\theta\) be the nine-piece continuous area-preserving map defined in Ostrovski [1, §2]. For \(K\ge3\) select the resonant \(\theta_K\in(0,\pi/4)\) of [1, Lemma 5.2]. Define \(t=\sin^2\theta_K\), \(s=\sin\theta_K\cos\theta_K\), \(P_4=(t,1-s)\), \(P_1=(s,t)\), and
\[
 B=\frac{1}{t-s}\begin{pmatrix}t^2-(1-s)^2&(1-2s)t\\ (2s-1)t&(2t-1)t\end{pmatrix},\qquad v_j=B^jP_4\quad (0\le j\le K).
\]
Here \(v_K=P_1\). The polygon construction and interpolation in [1, §5] supply the outer invariant annulus, the distinguished levels \(q_N\), and the parallel-sided polygonal leaves between them. A leaf is labeled by the intercept \(qP_1\) on the break line, \(0<q\le1\). Its oriented quarter-chain runs through \(qv_0,\ldots,qv_K,R(qv_0)\); its other three chains are obtained by \(R\). Indeed the corner itinerary is the homogeneous iteration by \(B\), so that its departure point \(qP_1\) determines the corner chain; the side of the interpolating polygon is horizontal, joining \(qP_1\) to \(R(qP_4)\). Collinear subdivisions do not change the geometric leaf. Only the geometry and continuity of the circle rotation numbers are used from this interpolation, not an affine interpolation formula for the rotation numbers. The probability excludes the central region inside the \(q=1\) leaf. The square boundary and individual polygonal leaves have planar measure zero.

## Proof

**1. Area in leaf coordinates.** Write \(\det(u,v)=u_1v_2-u_2v_1\). Since \(\det B=1\) and \(Bv_0=(t,s)\), each \(\det(v_j,v_{j+1})=-td\). Also \(v_K\cdot v_0=t\); hence the corner-plus-side coefficient \(\sum_{j=0}^{K-1}\det(v_j,v_{j+1})+v_K\cdot v_0\) is \(H=t(1-Kd)\).

Use area coordinates \((q,z)\) on the strip traversed by one corner edge, with position \(q((1-z)v_j+zv_{j+1})\), \(0<z<1\). The absolute Jacobian is \(qtd\), giving a mass of \(qtd\) on that edge per unit \(dq\). On the side segment use \((q,x_1)\mapsto(x_1,qt)\), with horizontal length \(1-q\), giving mass \(t(1-q)\) per unit \(dq\). Quarter turns preserve these masses. Strips meet only on boundaries of area zero. Thus area disintegrates as \(dq\,d\mu_q\), with total leaf mass
\[
 M(q)=4\big(Kqtd+t(1-q)\big)=4t(1-hq).
\]
The area between the square boundary and the leaf \(q\) is \(\int_0^q M(a)\,da=4tq-2Hq^2\). At \(q=1\) this is \(W>0\).

**2. Rotation number off the distinguished levels.** The map fixes \(q\) and preserves planar area, so it preserves \(\mu_q\) on almost every leaf (test invariance against continuous functions of position and arbitrary functions of \(q\)). This measure is atomless and gives positive mass to each open arc. The oriented cumulative mass divided by \(M(q)\) is a circle coordinate in which the map is a rotation: orientation and preservation of arc masses give a constant displacement modulo one. From \(qv_0\) to its image \(qv_1\) the positively oriented arc is exactly the first corner edge. Its normalized mass gives
\[
 \rho(q)=\frac{qtd}{M(q)}=\frac{dq}{4(1-hq)}.
\]
This identity extends to every interior leaf by continuity. It gives \(\rho(q_N)=1/[4(K+N)]\), including the upper endpoint at \(q_0=1\). It is strictly increasing in \(q\), since \(1-hq>0\) and its derivative is \(d/[4(1-hq)^2]\). Inversion gives \(q=x/(1+hx)\) for \(x=4r/d\). Dividing the area outside this leaf by \(W\) gives \((2q-hq^2)/(2-h)\), the displayed CDF. Differentiation gives the density, with no atoms at either endpoint.

**3. Reciprocal rotation and moments.** In the exact CDF, put \(r=1/u\); the linear coefficient at zero is \(D_K\). The tail-integral formula for nonnegative moments shows finiteness for \(0<p<1\) and divergence for \(p\ge1\). For \(p\le0\), finiteness follows from \(\mathcal T\ge4K>0\). Integrating the tail up to \(L\) proves the truncated first-moment formula.

**4. Resonant asymptotics.** Put \(\delta=1/2-t\), \(f=\sqrt{1-4t^2}\), \(s=\sqrt{t(1-t)}\). From the expanding eigenvalue and eigen-coordinate ratio in [1, Appendix, (6.2)–(6.4)],
\[
 \lambda=\frac{4t^2-2t+(2s-1)(1+f)}{2(t-s)},\qquad
 \Xi=\frac{2ts+t(f-1)}{2t^2+(1-s)(f-1)},\qquad K=\frac{\log\Xi}{\log\lambda}.
\]
As \(K\to\infty\), \(\delta\downarrow 0\). Expanding using \(f=2\sqrt{\delta}\sqrt{1-\delta}\) gives
\[
 \log\lambda=2\delta^{3/2}+\delta^{5/2}+\tfrac{11}{4}\delta^{7/2}+O(\delta^{9/2}),\qquad
 \log\Xi=2\delta^{1/2}+\tfrac53\delta^{3/2}+\tfrac{43}{20}\delta^{5/2}+O(\delta^{7/2}).
\]
Division yields \(K=\delta^{-1}+1/3-(7/15)\delta+O(\delta^2)\), so \(\delta^{-1}=K-1/3+7/(15K)+O(K^{-2})\). Substitution in \(16t/d=4\delta^{-2}-8\delta^{-1}-4+O(\delta)\) proves the stated asymptotic. At \(K=3\), \(\theta_3=\pi/8\), so \(C_3=8\), \(W=(11-7\sqrt2)/2\), and \(D_3=16/(11-7\sqrt2)\).

## Verification

The symbolic area disintegration and invariant arc-mass calculation are the off-node verification. For example, at \(K=3\), \(d=1-1/\sqrt2\) and \(r=1/14\) gives \(q=(1+d/2)^{-1}\) rather than the straight-line interpolation \((1+3d/7)/(1+d)\). These differ by \((30\sqrt2-41)/833\). Since area is strictly increasing in \(q\), the interpolated CDF would be wrong at this value. The accompanying optional finite numerical checks concern distinguished polygon areas and resonant parameter values, not the rotation coordinate between those polygons.

## Relationship to prior work and limitations

Ostrovski [1, §5 and Appendix] supplies the resonant polygonal foliation, distinguished rotation levels and implicit parameter relation. The parenthetical “in fact, linearly” after the proof of Theorem 5.1 is not valid in the break-line intercept: the leaf mass and the mass advanced in one step both depend on that intercept, and their ratio is generally nonlinear. The formula here leaves the distinguished levels and the continuity and monotonicity of Corollary 5.4 intact.

An exact area calculation for the innermost polygon [2] gives the normalization but not the area distribution of rotation numbers. A related calculation [3] also gives the distinguished threshold areas and the leading slow-winding tail. The formula above additionally gives the law between the distinguished levels and the higher-order resonant asymptotic for its leading coefficient. The scope is the resonant sequence and the exterior of the innermost polygon only. The reciprocal rotation number is not a first-return time or an orbit's primitive period. Bibliographic distinction is a best-knowledge assessment, not an absolute priority claim.

## References

[1] G. Ostrovski, *Dynamics of a Continuous Piecewise Affine Map of the Square*, arXiv:1305.4282v1, §§2, 5 and Appendix, https://arxiv.org/abs/1305.4282v1.

[2] *Quadratic vanishing of the unfoliated core in an integrable piecewise-affine square map*, Resultary record 22de24ee92be.

[3] *Exact slow-winding area law for the integrable Ostrovski square map*, Resultary record 9d9a41caf0a3.

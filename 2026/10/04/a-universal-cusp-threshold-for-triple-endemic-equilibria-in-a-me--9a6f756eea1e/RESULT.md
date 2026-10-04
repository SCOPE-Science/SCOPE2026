# A universal cusp threshold for triple endemic equilibria in a media-responsive SIR model

## Finding

For the active-media subsystem of the epidemic model introduced by Wang, Yang, and Yang, define
\[
R:=R_0=\frac{kb}{n}>1,\qquad q:=\frac{m_1a}{b}>0.
\]
Every strictly positive equilibrium satisfies
\[
S^*=\frac{n}{b}e^{m_1I^*},
\]
and the remaining equilibrium condition reduces exactly to
\[
I^*=\frac{a}{b}e^{m_1I^*}
\left(1-\frac{e^{m_1I^*}}{R}\right).
\]
With \(z=e^{m_1I^*}\), this is equivalent to
\[
q=G_R(z):=\frac{\log z}{z(1-z/R)},\qquad 1<z<R.
\]

Let
\[
R_c=4e^{3/2}.
\]
If \(1<R\le R_c\), then \(G_R\) is increasing on \((1,R)\), so there is exactly one regular endemic equilibrium for every \(q>0\).

If \(R>R_c\), there are exactly two points \(1<z_-<z_+<R\) satisfying
\[
1-\frac zR-\left(1-\frac{2z}{R}\right)\log z=0.
\]
The first is a local maximum and the second a local minimum of \(G_R\). Define
\[
q_{\max}=G_R(z_-),\qquad q_{\min}=G_R(z_+).
\]
Then the exact equilibrium count is:
\[
\begin{cases}
1,&0<q<q_{\min},\\
2,&q=q_{\min},\\
3,&q_{\min}<q<q_{\max},\\
2,&q=q_{\max},\\
1,&q>q_{\max}.
\end{cases}
\]
At either two-equilibrium boundary, one equilibrium is double. The two folds meet at the universal cusp
\[
(R,q)=\left(4e^{3/2},2e^{-3/2}\right).
\]

Moreover, if \(z\) is a simple endemic root, then
\[
\det J=
\frac{nI^*b\,z(1-z/R)}{1+m_2nI^*}\,G_R'(z).
\]
Hence the middle branch in the three-equilibrium regime is always a saddle, and the Jacobian determinant vanishes exactly at the folds.

## Assumptions and scope

All biological parameters are positive, \(m_1>0\), \(m_2>0\), and the claim concerns regular equilibria in the active-media region of the model. The source writes \(n=\alpha+\beta+\gamma\). The classification is for endemic equilibria only; it does not claim global convergence for the full piecewise system.

All roots above automatically lie in the active-media region. Indeed, the switching threshold is
\[
S_q=\frac{m_2n-m_1}{bm_2},
\]
whereas an endemic root has \(S^*=nz/b\) with \(z>1\), so
\[
S^*-S_q=
\frac{n(z-1)}{b}+\frac{m_1}{bm_2}>0.
\]

## Proof

Set
\[
G_R(z)=\frac{\log z}{z(1-z/R)}.
\]
Because \(G_R(z)\to0\) as \(z\downarrow1\) and \(G_R(z)\to+\infty\) as \(z\uparrow R\), every positive \(q\) has at least one root.

The sign of \(G_R'\) is the sign of
\[
N_R(z)=1-\frac zR-\left(1-\frac{2z}{R}\right)\log z.
\]
Its derivative is
\[
N_R'(z)=\frac{1+2\log z}{R}-\frac1z.
\]
The function \(z(1+2\log z)\) is strictly increasing for \(z>1\), so \(N_R\) has a unique critical point \(z_0\), necessarily its minimum, characterized by
\[
R=z_0(1+2\log z_0).
\]
Writing \(L=\log z_0\), direct substitution gives
\[
N_R(z_0)=\frac{L(3-2L)}{1+2L}.
\]
Thus the minimum of \(N_R\) is nonnegative exactly when \(L\le3/2\), which is equivalent to
\[
R\le4e^{3/2}.
\]
This proves uniqueness below and at the cusp threshold.

For \(R>4e^{3/2}\), the minimum of \(N_R\) is negative while \(N_R(1)>0\) and \(N_R(R)=\log R>0\). Hence \(N_R\) has exactly two roots \(z_-<z_+\), and \(G_R\) is increasing, then decreasing, then increasing. The horizontal-line intersection count gives the one/two/three/two/one classification above.

At the transition value \(R=4e^{3/2}\), the critical point is \(z=e^{3/2}\). Substitution into \(G_R\) yields
\[
q_c=2e^{-3/2}.
\]
At this point the scalar equilibrium equation has vanishing first and second derivatives but nonzero third derivative, giving the cusp contact.

For the determinant identity, write the active subsystem after the Lambert-\(W\) reduction as
\[
\dot S=aS\left(1-\frac Sk\right)-\frac{W(G_1)}{m_2},
\qquad
\dot I=\frac{W(G_1)}{m_2}-nI.
\]
At an endemic equilibrium, \(W(G_1)=m_2nI^*\). Differentiation gives
\[
\frac1{m_2}\frac{\partial W}{\partial S}
=\frac{nI^*}{S^*(1+m_2nI^*)},
\]
and
\[
\frac1{m_2}\frac{\partial W}{\partial I}-n
=-\frac{nm_1I^*}{1+m_2nI^*}.
\]
Using \(S^*=nz/b\), \(R=kb/n\), and \(q=m_1a/b\), the determinant reduces to
\[
\det J=
\frac{nI^*b}{1+m_2nI^*}
\left[\frac1z-q\left(1-\frac{2z}{R}\right)\right].
\]
At a root \(q=G_R(z)\), the bracket equals
\[
z(1-z/R)G_R'(z),
\]
which proves the stated determinant formula and the saddle character of the middle branch.

## Verification

For the exact parameter choice
\[
a=b=n=1,\qquad k=20,\qquad m_1=\frac{43}{100},\qquad m_2=\frac12,
\]
we have \(R=20>4e^{3/2}\) and \(q=0.43\). The two fold levels are
\[
q_{\min}\approx0.4264916567,
\qquad
q_{\max}\approx0.4339207029,
\]
so the model is in the three-equilibrium regime. The three roots are approximately
\[
z\approx2.9387164522,\quad4.7984225372,\quad7.5275757359.
\]
They correspond to
\[
I^*\approx2.5069137329,\quad3.6471795949,\quad4.6943559129.
\]
For these three equilibria, the trace/determinant pairs are approximately
\[
(-0.1507937862,\,0.0407715562),\quad
(-0.3044542781,\,-0.0197188259),\quad
(-0.5421372511,\,0.0372087525).
\]
Thus the first and third are locally asymptotically stable and the middle one is a saddle. The bundled verification script recomputes the fold levels, three roots, residuals, active-region inequalities, and Jacobian signs.

## Relationship to prior work

Wang, Yang, and Yang (2024), DOI 10.3934/math.2024172, derive the implicit endemic-equilibrium equation used here and state existence for \(R_0>1\), but do not classify the number of positive solutions of that equation. Their local-stability discussion is written around a single labeled endemic point.

Xiao, Zhao, and Tang (2013), DOI 10.3934/mbe.2013.10.445, study the earlier derivative-dependent media model with linear demographic inflow and mortality. In that model the endemic equation is explicitly solvable with the principal Lambert \(W\) function and yields a single endemic equilibrium for \(R_0>1\). The logistic susceptible growth in the 2024 model changes the scalar equilibrium geometry and is exactly what permits the fold pair found here.

Wang et al. (2016), DOI 10.1080/17513758.2016.1181212, already show that a different SIS model with logistic growth and a media-alert threshold can have up to three endemic equilibria and bistability. Therefore the qualitative possibility of media-associated multiplicity is not claimed as new. The present result is the exact root classification, universal cusp threshold, and determinant-slope identity for the specific 2024 Lambert-\(W\) model.

## Limitations

The result classifies endemic equilibria and identifies the middle branch as a saddle. It does not prove global bistability for every parameter point in the three-equilibrium wedge, classify Hopf bifurcations of the outer branches, or analyze optimal-control trajectories. The explicit witness establishes local bistability only.

## References

1. D. Wang, H. Yang, L. Yang, “Research on nonlinear infectious disease models influenced by media factors and optimal control,” AIMS Mathematics 9 (2024), 3505–3520. DOI: 10.3934/math.2024172.
2. Y. Xiao, T. Zhao, S. Tang, “Dynamics of an infectious disease with media/psychology induced non-smooth incidence,” Mathematical Biosciences and Engineering 10 (2013), 445–461. DOI: 10.3934/mbe.2013.10.445.
3. L. Wang, D. Zhou, Z. Liu, D. Xu, X. Zhang, “Media alert in an SIS epidemic model with logistic growth,” Journal of Biological Dynamics 11 (2017), 120–137. DOI: 10.1080/17513758.2016.1181212.

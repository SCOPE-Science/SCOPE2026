# Two-conductance stars: exact heat-Lipschitz norm, slow-edge rigidity and a sharp fixed-size amplification envelope

## Finding
Let \(k\ge2\) be any integer, and let \(0<a<b\). On the star with hub \(o\), one distinguished leaf \(x\), and \(k\) other leaves \(y_1,\ldots,y_k\), assign the edge \(ox\) heat conductance \(a\) and all \(oy_j\) heat conductance \(b\). The vertex measure is counting measure and **all graph-metric edge lengths are one**, regardless of conductance. Write \(L\) for the symmetric conductance Laplacian and \(H_t=e^{-tL}\).

Set
\[
S=2a+(k+1)b,\qquad \Delta=\sqrt{S^2-4(k+2)ab},\qquad
\alpha=\frac{S-\Delta}{2},\quad\beta=\frac{S+\Delta}{2},\quad d=kb-2a.
\]
Then for **every** \(t\ge0\), the exact sharp real operator norm on Lipschitz functions modulo constants is
\[
\boxed{\Lambda(t)=\|H_t\|_{\mathrm{Lip}\to\mathrm{Lip}}=
\frac{(\beta+d)e^{-\alpha t}-(\alpha+d)e^{-\beta t}}{\Delta}.}
\]
For every \(t>0\) the slow edge \(ox\) is the **unique** edge at which the maximizing output gradient is attained. All nonconstant real extremizers at that time are exactly the positive or negative multiples, plus arbitrary constants, of
\[
f(x)=1,\quad f(o)=0,\quad f(y_j)=-1\quad(1\le j\le k).
\]
The sharp profile has exactly one positive-time strict maximum at
\[
\boxed{t_*=\frac1\Delta\log\frac{\beta(\alpha+d)}{\alpha(\beta+d)}.}
\]
For each **fixed** \(k\ge2\), allowing arbitrary \(0<a<b\) and \(t\ge0\) gives the sharp but unattained envelope
\[
\boxed{\sup_{0<a<b,\ t\ge0}\Lambda(t)=2-\frac1{k+1}.}
\]
It is approached when \(b/a\to\infty\) at \(t=(ab)^{-1/2}\). In the smallest covered star (four vertices, \(k=2\)), the limiting amplification is \(5/3\).

## Assumptions and scope
The heat generator acts on real vertex functions by
\[
(Lf)(v)=\sum_{w\sim v}c_{vw}(f(v)-f(w)),\qquad c_{ox}=a,\quad c_{oy_j}=b.
\]
The metric is the unweighted shortest-path distance, not the conductance-resistance metric. Thus
\[
\operatorname{Lip}(f)=\max\bigl\{|f(x)-f(o)|,\max_j|f(y_j)-f(o)|\bigr\}.
\]
The norm refers to the induced linear operator on vertex functions modulo constants. The heat semigroup preserves constants, and each claimed extremizer is understood to have positive input Lipschitz seminorm. The limit \(b/a\to\infty\) does not admit any zero or infinite conductances within an individual member of the family.

## Proof
**Exact intertwining and two rate classes.** Set \(g_x=f(x)-f(o)\), \(g_j=f(y_j)-f(o)\), \(\bar g=k^{-1}\sum_jg_j\), and \(z=-\bar g\). The heat equation gives
\[
\frac{d}{dt}\begin{pmatrix}g_x\\ z\end{pmatrix}
=T\begin{pmatrix}g_x\\ z\end{pmatrix},\qquad
T=\begin{pmatrix}-2a&kb\\a&-(k+1)b\end{pmatrix},\qquad
\frac{d}{dt}(g_j-\bar g)=-b(g_j-\bar g).
\]
The two eigenvalues of \(-T\) are \(0<\alpha<\beta\), with \(\alpha<b<\beta\) because its characteristic polynomial at \(b\) equals \(kb(a-b)<0\). Write
\[
e^{tT}=\begin{pmatrix}A&B\\C&D\end{pmatrix},\qquad E=e^{-bt}.
\]
All four entries are strictly positive for \(t>0\), because the off-diagonal entries of \(T\) are strictly positive. Since initial leaf differences can independently range in \([-1,1]\), the largest output gradient on the slow edge has exact magnitude \(X=A+B\), attained when \(g_x(0)=1\) and every \(g_j(0)=-1\). Solving the two-dimensional system with initial state \((1,1)\) gives
\[
X(t)=\frac{(\beta+d)e^{-\alpha t}-(\alpha+d)e^{-\beta t}}\Delta.
\]

**Every fast edge is strictly smaller.** For a fast leaf \(y_j\), the absolute row sum of its induced gradient operator is
\[
F=C+\frac{D+(k-1)E}{k}+\frac{k-1}{k}|D-E|
=\begin{cases}C+D,&D\ge E,\\ C+D+h(E-D),&D<E,\end{cases}
\qquad h=\frac{2(k-1)}k.
\]
To compare, put \(p=(2k+1)b-3a>0\). Both row sums of \(e^{tT}\) start at one, hence their difference is
\[
\delta(t):=X-(C+D)=\frac p\Delta\bigl(e^{-\alpha t}-e^{-\beta t}\bigr)>0\quad(t>0).
\]
This handles \(D\ge E\). For \(D<E\), it remains to establish \(J(t):=\delta(t)-h(E-D)>0\). Using the explicit \(D\) entry,
\[
J(t)=u e^{-\alpha t}+v e^{-\beta t}-h e^{-bt},\quad
u=\frac{p+h(\beta-(k+1)b)}\Delta,\quad
v=h-u.
\]
Here \(u>0\): indeed the characteristic polynomial of \(-T\) at \(2a\) is \(-kab<0\), so \(\alpha<2a\) and \(\beta>(k+1)b\). Also \(J(0)=0\) and \(J'(0)=3(b-a)>0\). If \(v\le0\), rewrite \(J=u(e^{-\alpha t}-e^{-bt})+v(e^{-\beta t}-e^{-bt})>0\) using \(\alpha<b<\beta\). If \(v>0\), then \(u+v=h>0\), and \(J'(0)>0\) means \((u\alpha+v\beta)/h<b\); strict convexity of the exponential and Jensen's inequality yield \(J(t)>0\) for \(t>0\). Thus \(X>F\) for every \(t>0\). The nonzero slow-edge row coefficients have one positive slow-leaf coefficient and \(k\) negative fast-leaf coefficients. Equality in its \(\ell^\infty\)-row estimate forces precisely the displayed vertex-ramp pattern, proving all equality statements.

**Single peak.** Since \(k\ge2\) and \(b>a\), \(d=kb-2a>0\). Put \(P=(\beta+d)/\Delta=1+(\alpha+d)/\Delta>1\). Then
\[
X(t)=P e^{-\alpha t}-(P-1)e^{-\beta t},\quad X'(0)=d>0,
\]
whereas \(X'(t)<0\) eventually. After division by \(e^{-\alpha t}\), the derivative equation has one strictly decreasing exponential term. Therefore it has exactly one zero, which is the stated \(t_*\), and the peak is strict.

**Sharp fixed-size envelope.** Write \(r=a/b\in(0,1)\). The slow exponential coefficient satisfies
\[
P=\frac12+\frac{3k+1-2r}{2\sqrt{(k+1)^2-4r+4r^2}}<\frac{2k+1}{k+1}.
\]
For clarity, the exact positive difference of squares needed for the final inequality is
\[
(3k+1)^2\big((k+1)^2-4r+4r^2\big)
-(k+1)^2(3k+1-2r)^2
=4kr\big((k-1)(3k+1)+4(2k+1)r\big)>0.
\]
For all finite \(t>0\), \(X(t)<P\); at \(t=0\), \(X(0)=1\). Hence the claimed envelope is never reached. Taking \(b/a\to\infty\) and \(t=(ab)^{-1/2}\) gives \(\alpha t\to0\), \(\beta t\to\infty\), and \(P\to(2k+1)/(k+1)\), which proves sharpness and the four-vertex value \(5/3\).

## Verification
Run `python verify.py` with Python 3 and the standard library. The independent verifier checks the exact full-gradient intertwining \(DQ=BD\) with rational arithmetic, and computes the heat operator directly by uniformization on the **entire** vertex space for 28 parameter-time cases. It compares these independent edge-row norms with the analytic formula, tests strict slow-edge domination and checks seven high-contrast limiting examples. The analytic arguments above prove the statements for all admissible integers, conductances and times; the finite computations only corroborate them. In a separate additional numerical stress test, 90 distinct random parameter-time cases agreed with the closed formula and strict edge ranking.

For example, with \(k=2,a=1,b=3\), the unique peak occurs at \(t_*\approx0.1293921245\), where \(\Lambda(t_*)\approx1.2022839624\). With \(k=2,a=1,b=1000\), the peak is approximately \(1.6608229472\), approaching \(5/3\).

## Relationship to prior work
Ollivier's Markov-chain transport curvature introduces the relevant \(W_1\) framework [1]. Chafaï and Joulin derive gradient intertwinings and sharp curvature formulas for birth-death processes on a line [2]; the present branching star is not a birth-death chain when \(k\ge2\). Münch and Wojciechowski prove general graph-curvature/semigroup gradient equivalences for weighted graphs [3], which do not themselves evaluate this exact all-time profile, its unique edge, or its sharp heterogeneity envelope. The established unweighted star formula is recovered on the boundary \(a=b\), but is not claimed as a new result. The findings here concern all strict two-rate contrasts \(0<a<b\), the equality classification, and a sharp fixed-vertex-count supremum. An unindexed equivalent special calculation cannot be ruled out.

## Limitations
Conductances are symmetric and positive and take exactly two values: one slow leaf and \(k\) equally fast leaves. The metric is independent of the heat conductances. The theorem does not classify arbitrary heterogeneous stars, intrinsic conductance metrics, normalized random-walk generators, or larger tree families. The sharp envelope is a supremum along a singular conductance-ratio limit, not a maximum for any fixed finite weighted star. No claim of independent validation or publication priority is made.

## References
[1] Yann Ollivier, *Ricci curvature of Markov chains on metric spaces*, first publicly posted January 30, 2007; arXiv:math/0701886, https://arxiv.org/abs/math/0701886.

[2] Djalil Chafaï and Aldéric Joulin, *Intertwining and commutation relations for birth-death processes*, first publicly posted November 10, 2010; arXiv:1011.2331, https://arxiv.org/abs/1011.2331.

[3] Florentin Münch and Radosław K. Wojciechowski, *Ollivier Ricci curvature for general graph Laplacians: Heat equation, Laplacian comparison, non-explosion and diameter bounds*, first publicly posted December 4, 2017; arXiv:1712.00875, https://arxiv.org/abs/1712.00875.

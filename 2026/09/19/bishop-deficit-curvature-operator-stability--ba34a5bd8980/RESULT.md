# Bishop volume deficit controls curvature-operator excess

## Statement

Let \((M^n,g)\), \(n\ge 3\), be a complete Riemannian manifold without boundary whose curvature operator satisfies
\[
R\ge \operatorname{Id}
\]
on \(\Lambda^2T^*M\), with the unit sphere normalized by \(R_{\mathbb S^n}=\operatorname{Id}\). Bonnet--Myers implies that \(M\) is compact and \(q:=|\pi_1(M)|<\infty\). Let
\[
\delta_q(M):=\frac{\omega_n}{q}-\operatorname{Vol}(M,g),
\qquad E:=R-\operatorname{Id}\ge0,
\]
where \(\omega_n=\operatorname{Vol}(\mathbb S^n(1))\).

For the normalized Lipschitz--Killing curvature polynomials \(H_j\) used by Ge--Li--Li,
\[
H_0(E)=1,\qquad H_1(E)=\frac{2\operatorname{tr}E}{n(n-1)},
\]
and \(H_j(E)\ge0\) whenever \(E\ge0\). Put \(m=\lfloor n/2\rfloor\). Then
\[
\boxed{
\delta_q(M)
\begin{cases}
=\displaystyle\sum_{j=1}^{m}\binom{n/2}{j}\int_M H_j(E)\,dV_g,& n\ \text{even},\\[2mm]
\ge\displaystyle\sum_{j=1}^{m}\binom{n/2}{j}\int_M H_j(E)\,dV_g,& n\ \text{odd}.
\end{cases}}
\tag{1}
\]
For odd \(n\), the generalized binomial coefficients \(\binom{n/2}{j}\) are positive for \(1\le j\le m\).

### Sharp full-operator \(L^1\) stability

Since \(E\ge0\) and hence \(\|E\|_{S_1}=\operatorname{tr}E\), the first term of (1) gives
\[
\boxed{
\int_M\|R-\operatorname{Id}\|_{S_1}\,dV_g
\le (n-1)\delta_q(M).
}
\tag{2}
\]
Consequently, for every Schatten norm \(S_p\), \(1\le p\le\infty\),
\[
\boxed{
\int_M\|R-\operatorname{Id}\|_{S_p}\,dV_g
\le (n-1)\delta_q(M),
}
\tag{3}
\]
and, for every \(\tau>0\),
\[
\boxed{
\operatorname{Vol}\{x:\|R_x-\operatorname{Id}\|_{S_p}\ge\tau\}
\le \frac{(n-1)\delta_q(M)}{\tau}.
}
\tag{4}
\]
Thus almost-maximal Bishop volume forces the full curvature operator, not merely scalar curvature, to be close to the spherical operator in \(L^1\). The same estimate applies to the pointwise maximal sectional-curvature excess because
\[
0\le \max_{\sigma\subset T_xM}\bigl(K_x(\sigma)-1\bigr)
\le \|E_x\|_{S_\infty}.
\]

If
\[
\varepsilon:=1-\frac{q\operatorname{Vol}(M,g)}{\omega_n}\in[0,1),
\]
then (3) becomes
\[
\boxed{
\frac1{\operatorname{Vol}(M,g)}
\int_M\|R-\operatorname{Id}\|_{S_p}\,dV_g
\le (n-1)\frac{\varepsilon}{1-\varepsilon}.
}
\tag{5}
\]

For each \(2\le j\le m\), (1) also gives
\[
\boxed{
\int_M H_j(E)\,dV_g
\le \frac{\delta_q(M)}{\binom{n/2}{j}}.
}
\tag{6}
\]
In even dimensions the volume deficit is therefore exactly partitioned among the linear curvature-operator excess and all higher nonnegative Lipschitz--Killing excesses.

### A sharp nonlinear concentration law for the curvature floor

Define the local curvature-operator floor excess
\[
a(x):=\lambda_{\min}(E_x)=\lambda_{\min}(R_x)-1\ge0
\]
and
\[
P_n(t):=\sum_{j=1}^{\lfloor n/2\rfloor}\binom{n/2}{j}t^j.
\]
Then
\[
\boxed{
\int_M P_n(a(x))\,dV_g\le\delta_q(M).
}
\tag{7}
\]
When \(n\) is even this becomes the particularly simple sharp estimate
\[
\boxed{
\int_M\left((1+a(x))^{n/2}-1\right)dV_g
\le\delta_q(M).
}
\tag{8}
\]
Consequently,
\[
\boxed{
\operatorname{Vol}\{x:R_x\ge(1+\tau)\operatorname{Id}\}
\le \frac{\delta_q(M)}{P_n(\tau)}
}
\tag{9}
\]
for every \(\tau>0\). In even dimensions,
\[
\boxed{
\operatorname{Vol}\{x:R_x\ge(1+\tau)\operatorname{Id}\}
\le
\frac{\delta_q(M)}{(1+\tau)^{n/2}-1}.
}
\tag{10}
\]
This is a nonlinear localization of the spherical scaling law: a region on which the curvature operator has a uniformly stronger lower bound must occupy correspondingly less volume.

The even-dimensional bound (10) is exactly sharp for every \(\tau>0\). For the round sphere with constant sectional curvature \(k=1+\tau\), the set on the left is all of \(M\), while
\[
\delta_1=\omega_n(1-k^{-n/2}),
\]
and the right side of (10) is exactly \(\omega_nk^{-n/2}=\operatorname{Vol}(M,g_k)\).

Finally, the coefficient \(n-1\) in (2) is also optimal. For \(g_k=k^{-1}g_{\mathbb S^n(1)}\), with \(N=\binom n2\),
\[
\frac{\int\|E\|_{S_1}\,dV_{g_k}}
{\omega_n-\operatorname{Vol}(g_k)}
=
\frac{N(k-1)}{k^{n/2}-1}
\longrightarrow n-1
\qquad(k\downarrow1).
\tag{11}
\]
Hence no smaller universal coefficient can replace \(n-1\), even within constant-curvature metrics.

## Proof

It is enough first to work on the simply connected universal cover. Ge--Li--Li normalize the curvature operator by \(R=\operatorname{Id}+E\) and prove
\[
2\operatorname{tr}E=\operatorname{Scal}-n(n-1)
\]
together with positivity \(H_j(E)\ge0\) for \(E\ge0\).

Assume first that \(n=2m\). Their Pfaffian expansion is
\[
e_g=\frac{2}{\omega_n}\sum_{j=0}^{m}\binom mj H_j(E).
\]
Positive curvature operator implies that the simply connected manifold is diffeomorphic to \(\mathbb S^n\), so Chern--Gauss--Bonnet gives \(\int_M e_g\,dV_g=2\). Therefore
\[
\omega_n
=
\sum_{j=0}^{m}\binom mj\int_M H_j(E)\,dV_g.
\]
Since \(H_0=1\), subtracting \(\operatorname{Vol}(M,g)\) gives the even-dimensional equality in (1).

Now let \(n=2m+1\). For the strict inequality \(R>\operatorname{Id}\), Ge--Li--Li construct a Ricci-expander filling and prove that the limiting Chern--Gauss--Bonnet boundary density is
\[
b_g
=
\frac1{\omega_n}
\sum_{j=0}^{m}\binom{n/2}{j}H_j(E)
\]
and satisfies
\[
\int_M b_g\,dV_g\le1.
\]
Hence
\[
\omega_n-\operatorname{Vol}(M,g)
\ge
\sum_{j=1}^{m}\binom{n/2}{j}\int_M H_j(E)\,dV_g.
\]
For the non-strict hypothesis \(R\ge\operatorname{Id}\), apply the strict statement to \(g_a=ag\), \(0<a<1\), for which
\[
R_{g_a}=a^{-1}R_g>\operatorname{Id},
\]
and pass to \(a\uparrow1\). The curvature polynomials and volume forms converge smoothly, giving the odd-dimensional inequality in (1).

For a general \(M\), \(R\ge\operatorname{Id}\) implies \(\operatorname{Ric}\ge(n-1)g\), so \(q=|\pi_1(M)|<\infty\). Apply the simply connected result to the universal Riemannian cover. Volume and every integral in (1) are multiplied by \(q\); division by \(q\) replaces \(\omega_n\) by \(\omega_n/q\), proving (1) as stated.

The \(j=1\) term is
\[
\binom{n/2}{1}H_1(E)
=
\frac{\operatorname{tr}E}{n-1}.
\]
Dropping all nonnegative terms with \(j\ge2\) gives (2). Since \(E\ge0\), every Schatten norm satisfies \(\|E\|_{S_p}\le\|E\|_{S_1}\), giving (3); Markov's inequality gives (4), and division by volume gives (5). Formula (6) follows by retaining any one nonnegative term in (1).

For the nonlinear curvature-floor estimate, diagonalize \(E_x\). Every eigenvalue is at least \(a(x)\). Ge--Li--Li's eigenform formula is
\[
H_j(E_x)=c_{n,j}\sum_{a_1,\ldots,a_j}
\lambda_{a_1}\cdots\lambda_{a_j}
|\eta_{a_1}\wedge\cdots\wedge\eta_{a_j}|^2,
\]
with \(c_{n,j}>0\). Replacing each \(\lambda_a\) by its lower bound \(a(x)\) and using \(H_j(\operatorname{Id})=1\) gives
\[
H_j(E_x)\ge a(x)^j.
\]
Insert these inequalities into (1) to obtain (7). If \(n\) is even, the binomial theorem gives \(P_n(t)=(1+t)^{n/2}-1\), proving (8). On the superlevel set \(a(x)\ge\tau\), one has \(P_n(a(x))\ge P_n(\tau)\); applying (7) gives (9) and hence (10).

For a round metric of curvature \(k=1+\tau\), \(a\equiv\tau\), \(H_j(E)=\tau^j\), and in even dimensions the exact defect identity becomes the binomial identity
\[
\omega_n-\omega_nk^{-n/2}
=
\omega_nk^{-n/2}\bigl(k^{n/2}-1\bigr),
\]
so (10) is an equality. The trace-norm sharpness calculation in (11) follows from \(E=(k-1)\operatorname{Id}_{\Lambda^2}\) and \(N=n(n-1)/2\).

## Context and relation to known results

Ge, Li and Li proved in September 2026 that, under \(R\ge\operatorname{Id}\),
\[
\int_M\operatorname{Scal}\,dV
\le
2(n-1)\omega_n+(n-1)(n-2)\operatorname{Vol}(M)
\le n(n-1)\omega_n,
\]
with round-sphere rigidity in the simply connected case. Their proof develops the positive \(H_j(E)\) expansion used above. The present statement reorganizes the full expansion as a Bishop-volume-deficit hierarchy, retains the nonlinear terms rather than discarding them, and derives full curvature-operator \(L^1\) stability together with a sharp nonlinear concentration law for regions having a stronger curvature-operator floor. The source paper does not formulate a volume-deficit stability theorem, Schatten-norm estimate, or such concentration bound.

This differs from almost-maximal-volume rigidity under a Ricci lower bound, which gives topological or metric closeness under various hypotheses, and from recent scalar-curvature refinements of Bishop comparison. For example, Kwong's 2026 volume estimate assumes \(\operatorname{Ric}\ge(n-1)g\) and uses scalar-curvature lower information to sharpen the volume bound; it does not give the full curvature-operator \(L^1\) estimate or the higher Lipschitz--Killing defect budget above. The stronger curvature-operator hypothesis here is essential to the positivity mechanism.

## Limitations

- The estimate requires the strong pointwise lower bound \(R\ge\operatorname{Id}\); a Ricci lower bound alone does not make \(R-\operatorname{Id}\) positive semidefinite and does not support the trace-norm argument.
- The result proves \(L^1\) control of curvature-operator magnitude. No higher-\(L^p\) curvature-magnitude estimate is established here without additional geometric input.
- The coefficient \(n-1\) is optimal for the trace-norm estimate and the even-dimensional nonlinear floor bound is exactly sharp on round rescalings, but the individual higher-order bounds (6) are not claimed optimal.
- In odd dimensions (1) is an inequality rather than an exact identity; the missing defect is tied to the nonnegative interior Euler contribution of the Ricci-expander filling.
- This is a structural consequence of the recent Ge--Li--Li curvature-integral theorem and its positive curvature-polynomial expansion, not an independent replacement proof of that theorem.

## References

1. J. Ge, C. Li, R. Li, *Total scalar curvature under a curvature operator lower bound*, arXiv:2609.19851 (2026). https://arxiv.org/abs/2609.19851
2. K.-K. Kwong, *An improved volume bound under Ricci and scalar curvature lower bounds*, arXiv:2608.19196 (2026). https://arxiv.org/abs/2608.19196
3. G. Perelman, *Manifolds of positive Ricci curvature with almost maximal volume*, J. Amer. Math. Soc. 7 (1994), 299--305. https://doi.org/10.2307/2152760
4. L. Chen, X. Rong, S. Xu, *Quantitative Volume Space Form Rigidity Under Lower Ricci Curvature Bound*, arXiv:1604.06986. https://arxiv.org/abs/1604.06986
5. J.-P. Bourguignon, H. Karcher, *Curvature operators: pinching estimates and geometric examples*, Ann. Sci. Éc. Norm. Supér. 11 (1978), 71--92. https://doi.org/10.24033/asens.1340

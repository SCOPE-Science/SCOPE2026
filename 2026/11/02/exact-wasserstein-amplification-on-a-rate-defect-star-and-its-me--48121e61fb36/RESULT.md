# Exact Wasserstein amplification on a rate-defect star and its metastable peak

## Finding

Fix an integer \(r\ge2\) and a rate \(0<\varepsilon\le1\). Let \(S\) be the star with hub \(o\), one distinguished leaf \(w\), and ordinary leaves \(v_1,\ldots,v_r\). Give **every edge geometric length one**. Let \(Q\) be the symmetric continuous-time Markov generator with rate \(\varepsilon\) in both directions across \(ow\), and rate one in both directions across each \(ov_i\). Write \(P_t=e^{tQ}\), and use the fixed unit-edge shortest-path distance in Wasserstein-one transport.

For \(t\ge0\) define
\[
\mathcal C_{r,\varepsilon}(t)=\sup_{\mu\ne\nu}\frac{W_1(\mu P_t,\nu P_t)}{W_1(\mu,\nu)}.
\]
Set
\[
L=r+1,\qquad \Delta=\sqrt{L^2-4\varepsilon(1-\varepsilon)},\qquad
\lambda_\pm=\frac{L+2\varepsilon\pm\Delta}{2},\qquad
A=\frac{\lambda_+-2\varepsilon+r}{\Delta}.
\]
Then \(0<\lambda_-<\lambda_+\), \(A>1\), and the **exact all-time transport amplification** is
\[
\boxed{\mathcal C_{r,\varepsilon}(t)=A e^{-\lambda_-t}-(A-1)e^{-\lambda_+t}.}
\]
For every \(t\), the supremum is attained by the Dirac pair \((\delta_w,\delta_o)\), across the exceptional edge. When \(0<\varepsilon<1\) and \(t>0\), its transport amplification is strictly greater than that of each ordinary-edge Dirac pair; when \(\varepsilon=1\), symmetry makes all edges equivalent.

There is a unique global maximizing time
\[
\boxed{t_*=\frac{1}{\Delta}\log\frac{(A-1)\lambda_+}{A\lambda_-}\ge0,}
\]
which is positive except at \((r,\varepsilon)=(2,1)\), where it is zero. Its exact peak is
\[
\boxed{\mathcal A_r(\varepsilon)=A\left(1-\frac{\lambda_-}{\lambda_+}\right)
\left(\frac{A\lambda_-}{(A-1)\lambda_+}\right)^{\lambda_-/\Delta}.}
\]
Thus \(\mathcal C_{r,\varepsilon}(t)>1\) for sufficiently small positive \(t\) except at \((r,\varepsilon)=(2,1)\), and in that exceptional case \(\mathcal C_{2,1}(t)\le1\) for all times.

For fixed \(r\), define
\[
K_r=\frac{r(r+1)^2}{(2r+1)(r+2)},\qquad
b_r=\frac{(2r+1)(r+2)}{(r+1)^3}.
\]
As \(\varepsilon\downarrow0\),
\[
\boxed{t_* =\frac{\log(K_r/\varepsilon)}{r+1}
+O_r\!\left(\varepsilon\log\frac1\varepsilon\right)}
\]
and
\[
\boxed{\begin{aligned}
\mathcal A_r(\varepsilon)={}&2-\frac1{r+1}-b_r\varepsilon\log\frac1\varepsilon\\
&-\varepsilon\left[b_r(1+\log K_r)+\frac{r(r-1)}{(r+1)^3}\right]
+O_r\!\left(\varepsilon^2\log^2\frac1\varepsilon\right).
\end{aligned}}
\]
In particular, \(\lim_{\varepsilon\downarrow0}\mathcal A_r(\varepsilon)=2-1/(r+1)\), and this limit tends to two as \(r\to\infty\).

## Assumptions and scope

The vertex set is \(\{o,w,v_1,\ldots,v_r\}\), with exactly the \(r+1\) indicated hub-leaf edges. The rate matrix has \(Q(o,w)=Q(w,o)=\varepsilon\), \(Q(o,v_i)=Q(v_i,o)=1\), zero other off-diagonal entries, and diagonal rows summing to zero. The invariant distribution is uniform. Distances do **not** change with jump rates. The time parameter ranges over all \(t\ge0\); the weak-defect expansion fixes \(r\) before sending \(\varepsilon\) to zero. Only Wasserstein order one is considered.

## Proof

**1. Kantorovich duality and the edge-gradient system.** For a real function \(f\), put \(h=f(w)-f(o)\) and \(g_i=f(v_i)-f(o)\). On the unit-edge tree,
\[
\operatorname{Lip}(f)=\max\{|h|,|g_1|,\ldots,|g_r|\}.
\]
Kantorovich--Rubinstein duality therefore identifies \(\mathcal C_{r,\varepsilon}(t)\) with the induced \(\ell_\infty\)-norm of the heat semigroup acting on the \(r+1\) edge gradients. Direct substitution of \(Q\) gives
\[
\dot h=-2\varepsilon h-\sum_{j=1}^r g_j,\qquad
\dot g_i=-\varepsilon h-g_i-\sum_{j=1}^r g_j.
\]
Writing \(\bar g=r^{-1}\sum_jg_j\), the contrasts \(g_i-\bar g\) decay at rate one, and
\[
\frac{d}{dt}\binom{h}{\bar g}=-B\binom{h}{\bar g},\qquad
B=\begin{pmatrix}2\varepsilon&r\\\varepsilon&r+1\end{pmatrix}.
\]
The eigenvalues of \(B\) are \(\lambda_-\) and \(\lambda_+\). Since \(\det B=\varepsilon(r+2)>0\), both are positive.

**2. Explicit gradient rows.** Set \(x=e^{-\lambda_-t}\), \(y=e^{-\lambda_+t}\), \(z=e^{-t}\), and \(d=(x-y)/\Delta\). Let \(H=e^{-tB}\). Its four entries are
\[
\begin{aligned}
H_{11}&=\frac{(\lambda_+-2\varepsilon)x+(2\varepsilon-\lambda_-)y}{\Delta},
&H_{12}&=-rd,\\
H_{21}&=-\varepsilon d,
&H_{22}&=\frac{(\lambda_+-L)x+(L-\lambda_-)y}{\Delta}.
\end{aligned}
\]
The slow-gradient row of the full system has absolute row sum
\[
R_s(t)=H_{11}-H_{12}=A x-(A-1)y.
\]
The ordinary-gradient row has absolute row sum
\[
R_f(t)=\varepsilon d+\frac{r-1}{r}z+\frac{H_{22}}r
+\frac{r-1}{r}|H_{22}-z|.
\]
All diagonal coefficients used here are nonnegative; this is immediate from the displayed formulas and the spectral ordering below.

**3. The exceptional edge dominates at every time.** For \(0<\varepsilon\le1\), the characteristic polynomial of \(B\) is negative at one and at \(L\) when \(\varepsilon<1\), giving \(\lambda_-\le1< L<\lambda_+\) (with \(\lambda_-=1\) at \(\varepsilon=1\)). Also \(\Delta\le L\). Put \(q=(\lambda_+-L)/\Delta\in(0,1)\); then \(H_{22}=qx+(1-q)y\) and \(1-q=(\lambda_+-2\varepsilon)/\Delta\). For \(t>0\) we have \(x\ge z\), with strict inequality when \(\varepsilon<1\).

If \(H_{22}\ge z\), algebra gives
\[
R_s-R_f=\frac{2r+1-3\varepsilon}{\Delta}(x-y)\ge0.
\]
If \(H_{22}<z\), then \(z-H_{22}\le(1-q)(x-y)\), so
\[
\begin{aligned}
R_s-R_f&=\frac{2r+1-3\varepsilon}{\Delta}(x-y)
-\frac{2(r-1)}r(z-H_{22})\\
&\ge \frac{x-y}{\Delta}
\left[(r+1)+\frac1r-\left(1+\frac2r\right)\varepsilon
-\frac{r-1}{r}\Delta\right]\\
&\ge\frac{x-y}{\Delta}\left(1+\frac2r\right)(1-\varepsilon)\ge0.
\end{aligned}
\]
The inequalities are strict for \(0<\varepsilon<1\), \(t>0\), since \(x>z\) or the displayed strictly positive margin applies. For \(\varepsilon=1\) all leaves are symmetric. Hence the induced gradient norm equals \(R_s\) for all \(t\). A maximizing gradient witness is \(h(0)=1\), \(g_j(0)=-1\), corresponding to a one-Lipschitz potential. Duality shows that the Dirac pair on \(ow\) attains the norm.

**4. Exact peak.** The coefficient satisfies \(A>1\) for \(r\ge2\), \(0<\varepsilon\le1\), and
\[
R_s'(0)=r-2\varepsilon\ge0.
\]
The derivative is
\[
R_s'(t)=-A\lambda_-e^{-\lambda_-t}
+(A-1)\lambda_+e^{-\lambda_+t}.
\]
Its sign changes from positive to negative exactly once if \(r>2\varepsilon\); if \(r=2\varepsilon\), then \(r=2,\varepsilon=1\) and it is negative at all positive times. Solving for the zero gives the displayed \(t_*\). Substituting the critical-point identity gives \(\mathcal A_r(\varepsilon)\). This proves uniqueness and the all-time claims.

**5. Small-rate expansion.** Elementary Taylor expansions, at fixed \(r\), give
\[
\begin{aligned}
\Delta&=L-2\varepsilon/L+O_r(\varepsilon^2),\\
\lambda_-&=(r+2)\varepsilon/L+O_r(\varepsilon^2),\\
\lambda_+&=L+r\varepsilon/L+O_r(\varepsilon^2),\\
A&=(2r+1)/L-r(r-1)\varepsilon/L^3+O_r(\varepsilon^2).
\end{aligned}
\]
Consequently the ratio inside the logarithm defining \(t_*\) equals \(K_r/\varepsilon\,[1+O_r(\varepsilon)]\). Expanding the exact peak formula through first order, retaining \(\varepsilon\log(1/\varepsilon)\), gives the displayed asymptotic with remainder \(O_r(\varepsilon^2\log^2(1/\varepsilon))\). No interchange of the \(r\to\infty\) and \(\varepsilon\downarrow0\) limits is used.

## Verification

The companion `CHECKER.py` reconstructs the full Markov generator and matrix exponential independently and computes tree Wasserstein distances directly from leaf marginal discrepancies. It compares every edge Dirac pair against the formula over a grid of sizes, rates and times, checks the unique peak against independent optimization, and verifies the weak-rate expansion. The replay passed 693 finite numerical assertions. These finite tests are supporting evidence; the statements for all integer \(r\ge2\), continuous rate and time ranges follow from the proof above.

For orientation, \(r=2\) and \(\varepsilon=0.1\) give \(t_*\approx0.7600541951\) and \(\mathcal A_2(0.1)\approx1.4367929307\), while \(\mathcal A_2(1)=1\).

## Relationship to prior work

Münch and Wojciechowski establish a general equivalence between graph curvature, heat-semigroup Lipschitz bounds and Wasserstein contraction (Theorem 3.8 of [MW]). This framework motivates studying exact amplification, but does not supply the present defect-star profile or maximizer. Bai, Lin, Lu, Wang and Yau study evolving edge-length Ricci flow on weighted star graphs, proving convergence of those flows to equal weights (Theorem 5 of [BLLWY]); their evolving metric is different from the fixed unit-length geometry and fixed inhomogeneous generator here. Previously obtained exact equal-rate windmill/star formulas recover the boundary \(\varepsilon=1\); a slow-bond path result covers a different graph and only weak-rate peak asymptotics. Neither implies the present all-time, all-rate slow-edge dominance and exact peak on an inhomogeneous star.

## Limitations

The theorem is restricted to finite stars with one exceptional symmetric jump rate no larger than the ordinary rates, with every geometric edge length fixed at one. It does not address multiple distinct defect rates, normalized random walks, varying geometric edge lengths, higher-order Wasserstein distances, or any coupled large-degree/small-rate scaling beyond the displayed fixed-degree expansion. Priority beyond the inspected sources is not established independently; the review is self-review, not external certification.

## References

- [MW] F. Münch and R. K. Wojciechowski, *Ollivier Ricci curvature for general graph Laplacians: Heat equation, Laplacian comparison, non-explosion and diameter bounds*, arXiv:1712.00875v1, first public 2017-12-04. https://arxiv.org/abs/1712.00875
- [BLLWY] S. Bai, Y. Lin, L. Lu, Z. Wang, and S.-T. Yau, *Ollivier Ricci-flow on weighted graphs*, arXiv:2010.01802, first public 2020-10-05. https://arxiv.org/abs/2010.01802
- [V] L. Veysseire, *Coarse Ricci curvature for continuous-time Markov processes*, arXiv:1202.0420, first public 2012-02-02. https://arxiv.org/abs/1202.0420

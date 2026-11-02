# A sharp inverse-square negative-type transition for odd sunlet metrics

## Finding
For each odd integer \(n\ge5\), form the **sunlet** \(S_n=C_n\odot K_1\) by adjoining one private leaf to every vertex of the unit-edge cycle \(C_n\). Give its \(2n\) vertices their unweighted shortest-path metric \(d_n\). Let
\[
\wp_n=\sup\{p\ge0:\ \sum_{x,y\in S_n}\xi_x\xi_y d_n(x,y)^p\le0\quad\text{whenever }\sum_x\xi_x=0\}.
\]
Then \(1<\wp_n\le\log_2 3\), and the sharp asymptotic law along odd orders is
\[
\boxed{\lim_{\substack{n\to\infty\\ n\text{ odd}}}n^2(\wp_n-1)=T
=\frac{2\pi^2}{\gamma+\log(2\pi)-\operatorname{Ci}(2\pi)}
=8.097627356866536\ldots.}
\]
Here \(\gamma\) is Euler's constant and \(\operatorname{Ci}\) is the cosine integral, equivalently \(\gamma+\log u-\operatorname{Ci}(u)=\int_0^u(1-\cos v)\,dv/v\). More precisely, for each fixed \(t<T\), all sufficiently large odd \(n\) have **strict** \((1+t/n^2)\)-negative type; for each fixed \(t>T\), all sufficiently large odd \(n\) fail \((1+t/n^2)\)-negative type, with the obstruction in Fourier frequency \(2\). This last assertion describes the asymptotic transition, not a proof that frequency \(2\) is critical at every finite order.

## Assumptions and scope
The metric is the graph-path metric, not Euclidean chord distance. All quadratic forms use real coefficients with total sum zero. The exponent \(p\) refers to the power \(d_n^p\), so that \(p\)-negative type is equivalent to an isometric Hilbert embedding of \(d_n^{p/2}\). The result concerns every odd integer \(n\ge5\); claims about optimal modes at fixed finite \(n\), even orders, and weighted pendant edges are not made.

Write \(d_r=\min\{r,n-r\}\) for \(0\le r<n\). Relative to cycle vertices first and leaves second, the real distance-power matrix has two circulant layers with first rows
\[
A_r=d_r^p,\qquad B_r=(d_r+1)^p,\qquad
C_r=\begin{cases}0,&r=0,\\(d_r+2)^p,&r\ne0.\end{cases}
\]
For \(1\le k\le(n-1)/2\), define the real Fourier coefficients
\[
a_{n,k}(p)=\sum_{r=0}^{n-1}A_r\cos(2\pi kr/n),\quad
b_{n,k}(p)=\sum_rB_r\cos(2\pi kr/n),\quad
c_{n,k}(p)=\sum_rC_r\cos(2\pi kr/n),
\]
and \(M_{n,k}(p)=\begin{pmatrix}a_{n,k}(p)&b_{n,k}(p)\\b_{n,k}(p)&c_{n,k}(p)\end{pmatrix}\). The zero-frequency coefficient contrast is \(H_n(p)=a_{n,0}(p)+c_{n,0}(p)-2b_{n,0}(p)\). Fourier diagonalization gives the **exact finite-order criterion**: \(S_n\) has \(p\)-negative type if and only if \(H_n(p)\le0\) and all \(M_{n,k}(p)\) are negative semidefinite. This criterion is useful for reproducing numerical examples but is not itself an explicit finite-order formula for \(\wp_n\).

## Proof
**1. Strict negative type at \(p=1\).** Put \(a_{n,k}=a_{n,k}(1)\). The circulant coefficients at this exponent satisfy \(b_{n,k}(1)=a_{n,k}\) and \(c_{n,k}(1)=a_{n,k}-2\) for \(k\ne0\). Since the cyclic second difference of \(r\mapsto d_r\) equals \(+2\) at \(0\), \(-1\) at each of the two antipodal sites, and \(0\) elsewhere, its discrete Fourier transform yields
\[
a_{n,k}=
\begin{cases}
-\dfrac1{4\cos^2(\pi k/(2n))},&k\ \text{even},\\[2mm]
-\dfrac1{4\sin^2(\pi k/(2n))},&k\ \text{odd}.
\end{cases}
\]
Thus \(a_{n,k}\le-1/4\), and
\[
M_{n,k}(1)=a_{n,k}\begin{pmatrix}1&1\\1&1\end{pmatrix}-2\begin{pmatrix}0&0\\0&1\end{pmatrix}
\]
is negative definite. Its largest eigenvalue equals \(a_{n,k}-1+\sqrt{a_{n,k}^2+1}\), uniformly bounded above by \(-\beta\), where \(\beta=(5-\sqrt{17})/4>0\). The zero-frequency contrast is \(H_n(1)=-2\). Hence the finite metric has strict \(1\)-negative type, implying \(\wp_n>1\) by continuity. For \(n\ge5\), each cycle vertex and its three neighbors form an isometric three-leaf star. Its \(p\)-negative type requires \(2^p\le3\), proving \(\wp_n\le\log_2 3\).

**2. Uniform perturbation of the Fourier blocks.** Fix \(t\ge0\) and set \(p=1+t/n^2\). Let \(f(x)=\delta(x)\log\delta(x)\), where \(\delta(x)=\min\{x,1-x\}\) on \([0,1]\) and \(0\log0=0\). This is a continuous, \(1\)-periodic function. Define
\[
F_{n,k}=\frac1n\sum_{r=0}^{n-1}f(r/n)\cos(2\pi kr/n),\qquad
J=\begin{pmatrix}1&1\\1&1\end{pmatrix}.
\]
Uniformly for \(1\le k\le(n-1)/2\), the elementary Taylor expansion of \(z^{1+t/n^2}\) gives, in operator norm,
\[
M_{n,k}(1+t/n^2)
=\left(1+\frac{t\log n}{n^2}\right)M_{n,k}(1)+tF_{n,k}J+E_{n,k},
\qquad\max_k\|E_{n,k}\|\longrightarrow0.
\]
Indeed, for \(\ell=0,1,2\), the difference between \(((d_r+\ell)/n)\log((d_r+\ell)/n)\) and \(f(r/n)\) tends uniformly to zero, including the exceptional zero diagonal of the leaf-leaf block. The total Taylor remainder is \(O_t((\log n)^2/n^2)\) uniformly in Fourier frequency. The same expansion applied to the constant-frequency contrast gives \(H_n(1+t/n^2)=-2+o(1)\), since the common first-order matrix \(J\) vanishes on \((1,-1)\).

Let \(A_k=\int_0^1f(x)\cos(2\pi kx)\,dx=2\int_0^{1/2}x\log x\cos(2\pi kx)\,dx\). Ordinary Riemann sums show \(F_{n,k}\to A_k\) for each fixed positive integer \(k\). More importantly,
\[
\lim_{K\to\infty}\ \limsup_{\substack{n\to\infty\\n\ \mathrm{odd}}}\ \max_{K\le k\le(n-1)/2}|F_{n,k}|=0.
\]
To prove this uniform high-frequency assertion, approximate the continuous periodic \(f\) uniformly by a trigonometric polynomial of degree below \(K\). For \(n>2K\), discrete Fourier orthogonality makes its sampled coefficient exactly zero for every \(K\le k\le(n-1)/2\); the uniform approximation error bounds the remaining coefficients.

**3. Identification of the first unstable asymptotic mode.** At any fixed odd frequency \(k\), \(a_{n,k}\to-\infty\). Because the two large entries of the perturbation are proportional to \(J\), the greatest eigenvalue of
\[
\left(1+\frac{t\log n}{n^2}\right)M_{n,k}(1)+tF_{n,k}J
\]
tends to \(-1\); the vanishing \(E_{n,k}\) does not alter negativity. At fixed even frequency \(k\), instead \(a_{n,k}\to-1/4\), so the full block tends to
\[
B(t,k)=\left(-\frac14+tA_k\right)J-2\begin{pmatrix}0&0\\0&1\end{pmatrix}.
\]
Its determinant is \(1/2-2tA_k\), and its trace is negative whenever the determinant is nonnegative. Thus \(B(t,k)\) is strictly negative definite for \(t<1/(4A_k)\) and has a positive eigenvalue for \(t>1/(4A_k)\).

For every even \(k\ge2\), integration by parts gives
\[
A_k=\frac{\gamma+\log(\pi k)-\operatorname{Ci}(\pi k)}{2\pi^2 k^2}>0.
\]
The expression \(I(u)=\gamma+\log u-\operatorname{Ci}(u)=\int_0^u(1-\cos v)\,dv/v\) satisfies \(I(2\pi)>1\) and \(I'(u)=(1-\cos u)/u\). Therefore \((I(u)/u^2)'<0\) for \(u\ge2\pi\), showing \(A_2>A_4>A_6>\cdots\). The smallest finite-frequency transition occurs at
\[
T=\frac1{4A_2}=\frac{2\pi^2}{\gamma+\log(2\pi)-\operatorname{Ci}(2\pi)}.
\]
Fix \(0\le t<T\); negative \(t\) are covered by the downward monotonicity of strict negative type from exponent \(1\). For any prescribed large \(K\), the finitely many even modes below \(K\) are negative definite for all large odd \(n\), as are the finitely many odd modes. For the remaining frequencies, the uniform negative margin \(\beta\), the high-frequency estimate on \(F_{n,k}\), and \(\max\|E_{n,k}\|\to0\) preserve negative definiteness. The constant-frequency contrast is also negative. Hence \(S_n\) has strict \((1+t/n^2)\)-negative type for all sufficiently large odd \(n\). For \(t>T\), the \(k=2\) limit has a positive eigenvalue, so \(S_n\) fails \((1+t/n^2)\)-negative type eventually. Monotonicity of the negative-type exponent interval then sandwiches \(n^2(\wp_n-1)\) between any two numbers on opposite sides of \(T\), proving the limit.

## Verification
The standalone `verify.py` uses only Python's standard library. It independently evaluates the complete two-layer distance spectrum at odd orders \(5\) through \(101\), checks the exact \(p=1\) Fourier identities, evaluates finite-order critical exponents by bisection, compares the spectral blocks to direct full-distance quadratic forms, and evaluates \(T\) with a separate numerical quadrature of its integral. A successful replay prints `CHECK_OK checks=5337 asymptotic_constant=8.097627356867` and finite-order examples. This finite verification is diagnostic; the proof of the asymptotic and all quantifiers is the analytic argument above.

## Relationship to prior work
The general theory of finite-metric negative type and a determinant criterion for maximal generalized roundness appears in Robertson (2020), while Robertson (2023) relates negative type to Hilbert embeddings and studies specific bipartite/Hamming families. Neither provides an asymptotic exponent for odd sunlets. The present argument exploits their negative-type framework but adds the two-layer sunlet spectral reduction and a uniform-in-frequency singular perturbation calculation. Earlier classifications of vertex-transitive graphs do not directly apply because sunlets have two vertex orbits. Existing calculations involving more than one pendant leaf per pentagon concern a different fixed-cycle family and do not imply this odd-cycle growth law.

## Limitations
The result does not determine \(\wp_n\) exactly for each finite odd \(n\), nor does it prove that Fourier frequency \(2\) is the first obstruction for every finite order (though the supplied finite checks observe it in their tested range). It does not treat even orders, arbitrary pendant multiplicities, edge weights, or second-order correction terms. Historical precedence under an unsearched alternative formulation remains a risk; no independent mathematical audit has been performed.

## References
- Gavin Robertson, *The Maximal Generalised Roundness Of Finite Metric Spaces*, arXiv:2004.10923, first submitted 2020-04-23. https://arxiv.org/abs/2004.10923
- Gavin Robertson, *Negative Type and Bi-lipschitz Embeddings Into Hilbert Space*, arXiv:2309.16070, first submitted 2023-09-27. https://arxiv.org/abs/2309.16070
- MathWorld, *Sunlet Graph* (graph-family identification). https://mathworld.wolfram.com/SunletGraph.html

# A moving conductance threshold for sharp cut–cycle projection norms on weighted wheels

## Finding

Let \(n\ge 3\) be an integer and \(t>0\). On the wheel \(W_n=K_1\vee C_n\), give each spoke conductance \(t\) and each rim edge conductance \(1\). Let \(D\) be any oriented vertex–edge incidence matrix, and let \(W\) be the diagonal matrix of these conductances. On the **unweighted coordinate Banach space** \(\ell_1^{2n}(\mathbb R)\), consider the Euclidean-orthogonal conductance-normalized cut projection
\[
Q_{n,t}=(D W^{1/2})^{\mathsf T}(D W D^{\mathsf T})^+(D W^{1/2}),\qquad C_{n,t}=I-Q_{n,t}.
\]
Here \(\cdot^+\) denotes the Moore–Penrose pseudoinverse, and the edge-coordinate \(\ell_1\) norm is **not** weighted by conductance.

Put \(m=\lfloor n/2\rfloor\), \(s=\sqrt{t(t+4)}\), \(\rho=(t+2-s)/2\in(0,1)\), and
\[
g_k=\frac{\rho^k+\rho^{n-k}}{s(1-\rho^n)}\quad(0\le k<n),\qquad
A_{n,t}=1+2\sqrt t\,(g_0-g_m),\qquad
B_{n,t}=2(1-tg_0)+2\sqrt t\,(g_0-g_m).
\]
Then both induced endpoint norms have the **same exact value**:
\[
\boxed{\|Q_{n,t}\|_{1\to1}=\|C_{n,t}\|_{1\to1}
=\|Q_{n,t}\|_{\infty\to\infty}=\|C_{n,t}\|_{\infty\to\infty}
=\max\{A_{n,t},B_{n,t}\}.}
\]
Every spoke column of \(Q_{n,t}\) has \(\ell_1\) norm \(A_{n,t}\), and every rim column has norm \(B_{n,t}\); these two values are exchanged for \(C_{n,t}\).

For each \(n\ge3\) there is a unique sharp threshold \(\tau_n>0\) satisfying \(\tau_n g_0(\tau_n)=1/2\). It obeys
\[
\tau_3=1,\qquad \tau_4=\sqrt5-1,\qquad
1=\tau_3<\tau_4<\tau_5<\cdots<\frac43,\qquad
\lim_{n\to\infty}\tau_n=\frac43.
\]
For \(0<t<\tau_n\), the **rim** columns maximize \(Q_{n,t}\) and the **spoke** columns maximize \(C_{n,t}\); for \(t>\tau_n\), the maximizing classes reverse. Exactly at \(t=\tau_n\), both edge classes tie for both projections.

There is also an exact limiting phase law. For each fixed \(t>0\),
\[
\lim_{n\to\infty}\|Q_{n,t}\|_{1\to1}
=\max\left\{1+\frac{2}{\sqrt{t+4}},\quad 2+\frac{2(1-\sqrt t)}{\sqrt{t+4}}\right\}=:L(t),
\]
whose two branches exchange dominance at \(t=4/3\). More precisely, as \(n\to\infty\),
\[
\|Q_{n,t}\|_{1\to1}
=L(t)-\frac{2}{\sqrt{t+4}}\left(\rho^{\lfloor n/2\rfloor}+\rho^{\lceil n/2\rceil}\right)+O_t(\rho^n),
\]
and the same holds for \(C_{n,t}\). The leading finite-size deficit therefore has a parity-dependent coefficient and decays exponentially.

## Assumptions and scope

All graphs are finite, simple and connected. The wheel consists of one hub, \(n\) cyclically ordered distinct rim vertices, \(n\) spokes and \(n\) rim edges, with \(n\ge3\). Conductance is a positive electrical parameter; no shortest-path metric or metric edge length is asserted. The projection \(Q_{n,t}\) is orthogonal **in standard Euclidean edge coordinates** after the square-root conductance normalization; its kernel complement \(C_{n,t}\) is also orthogonal. Both norms are induced by the **standard**, real \(\ell_1\) and \(\ell_\infty\) norms on these same coordinates. No minimization over other projections is asserted. Changing an edge orientation conjugates the projections by a diagonal sign matrix and leaves these norms unchanged.

## Proof

**Grounded Green kernel.** Ground the hub at potential zero. On the rim, the weighted vertex Laplacian is the circulant positive-definite matrix
\[
T_{n,t}=tI+L(C_n)=(t+2)I-S-S^{-1},
\]
where \(S\) denotes cyclic shift. Let \(g=T_{n,t}^{-1}e_0\), so \(g_k=(T_{n,t}^{-1})_{k0}\). The number \(\rho\) is the smaller root of \(z^2-(t+2)z+1=0\), whence the stated explicit \(g_k\) solves the homogeneous recurrence away from \(k=0\), is periodic, and has unit defect at \(k=0\). Since \(T_{n,t}\) is positive definite, this characterizes its inverse column. Positivity of \(\rho\) implies \(g_k>0\); for \(0\le k<\lfloor(n-1)/2\rfloor\),
\[
g_k-g_{k+1}=\frac{(1-\rho)(\rho^k-\rho^{n-k-1})}{s(1-\rho^n)}>0.
\]
Thus the minimum is \(g_m\), and the cyclic total variation of \(g\) is \(2(g_0-g_m)\). Also \(T_{n,t}\mathbf1=t\mathbf1\) gives \(t\sum_k g_k=1\), which ensures \(0<tg_0<1\).

**Spoke columns.** Orient each spoke hub-to-rim and the rim cyclically. For the edge basis vector of the spoke at rim vertex zero, the grounded potential is \(\sqrt t\,g\). The normalized cut projection has spoke coordinates \(tg_k\) and rim coordinates \(\sqrt t(g_k-g_{k+1})\). Their total absolute sum is
\[
\sum_k tg_k+\sqrt t\sum_k|g_k-g_{k+1}|=1+2\sqrt t(g_0-g_m)=A_{n,t}.
\]
In its complementary cycle column, the spoke coordinates instead contribute \(2(1-tg_0)\); the rim contribution remains \(2\sqrt t(g_0-g_m)\). Hence that cycle column has norm \(B_{n,t}\).

**Rim columns.** For an oriented rim edge from vertex zero to vertex one, the grounded potential is a signed translate difference \(g_k-g_{k-1}\). The spoke coordinates of its cut column are \(\sqrt t(g_k-g_{k-1})\), again with total absolute sum \(2\sqrt t(g_0-g_m)\). The rim coordinates are, up to a common choice of incidence signs,
\[
(2I-S-S^{-1})g=e_0-tg.
\]
Their absolute sum is \((1-tg_0)+t\sum_{k\ne0}g_k=2(1-tg_0)\). Consequently the rim cut-column norm is \(B_{n,t}\). Subtraction from the corresponding basis vector leaves rim magnitudes \(tg_k\) with sum one and the same spoke contribution; its cycle-column norm is \(A_{n,t}\). Rotational symmetry covers all columns. Since the induced \(\ell_1\) norm is the largest absolute column sum, and a symmetric matrix has the same induced \(\ell_\infty\) norm, the displayed norm identities follow.

**Unique moving threshold.** The orbit-column difference is exactly
\[
B_{n,t}-A_{n,t}=1-2tg_0.
\]
By diagonalizing the rim cycle Laplacian, with \(\lambda_j=2-2\cos(2\pi j/n)\),
\[
tg_0=\frac1n\sum_{j=0}^{n-1}\frac{t}{t+\lambda_j}.
\]
Its derivative is strictly positive because \(\lambda_j>0\) for \(1\le j<n\). It ranges from \(1/n<1/2\) as \(t\downarrow0\) to \(1\) as \(t\to\infty\); hence a unique crossing exists. The formula for \(g_0\) above shows that, at fixed \(t\), \(tg_0=(t/s)(1+\rho^n)/(1-\rho^n)\) strictly decreases as \(n\) increases. Therefore the crossings \(\tau_n\) strictly increase. For \(n=3\), direct inversion gives \(tg_0=(t+1)/(t+3)\), so \(\tau_3=1\); for \(n=4\), the threshold polynomial is \(t^2+2t-4\), giving \(\tau_4=\sqrt5-1\). Finally \(tg_0\to t/s=\sqrt{t/(t+4)}\) as \(n\to\infty\), whose unique half-level occurs at \(t=4/3\). Since \((1+\rho^n)/(1-\rho^n)>1\), each finite crossing is strictly below \(4/3\).

**Asymptotic correction.** The exact Green formula gives \(g_0=s^{-1}+O_t(\rho^n)\) and
\[
g_m=\frac{\rho^m+\rho^{n-m}}{s}+O_t(\rho^n),
\]
where the remainder estimate follows by expanding \((1-\rho^n)^{-1}\) (indeed, the omitted product is even smaller). Thus both orbit-column norms have the same leading negative correction \(-2\sqrt t\,g_m\) and differ from their respective limiting constants by \(O_t(\rho^n)\) beyond that correction. If \(t<4/3\), the \(B\)-branch dominates for all sufficiently large \(n\); if \(t\ge4/3\), the \(A\)-branch dominates for all finite \(n\). Taking their maximum proves the asymptotic formula. For even \(n\) the leading deficit coefficient is \(4\rho^{n/2}/\sqrt{t+4}\); for odd \(n\) it is \(2(1+\rho)\rho^{(n-1)/2}/\sqrt{t+4}\).

## Verification

The standalone symbolic implementation in `wheel_verification.py` constructs each grounded incidence matrix, inverts its conductance Laplacian exactly over rational inputs, and reconstructs both orthogonal projections from their definitions. It verifies idempotence, symmetry, **every** edge-column norm and its correct spoke/rim class, and the orbit-difference identity. It also verifies the stated radical Green formula by direct substitution in the grounded Laplacian. The observed output is `PASS: 63 exact-rational parameter instances, 882 edge columns, 18 radical Green checks`. Run with `python wheel_verification.py` in Python with SymPy installed. These finite tests are diagnostics, not an exhaustive proof for arbitrary real \(t\) or arbitrarily large \(n\); the infinite statements are proved algebraically above.

## Relationship to prior work

Dilworth, Kutzarova and Ostrovskii (first public preprint May 21, 2023) study Banach-space cycle/cut projections and invariant/minimal projections, with detailed examples on discrete tori and Hamming graphs. Their construction motivates studying endpoint projection norms, but does not give the conductance-normalized weighted-wheel two-orbit column formulas or moving threshold. In the mathematical literature, weighted graph Laplacians and electrical Green functions are established tools; the kernel recurrence itself is not claimed to be new. Sedlák and Slavík (2025) give effective-resistance formulas for graph joins, including unweighted wheel resistance, which concern pairwise potential differences and Kirchhoff sums, not the absolute column sums and edge-orbit switching quantified here. Earlier exact minimal-projection constants for wheel cycle spaces concern an infimum over other projections in a different Banach normalization; they do not determine the canonical orthogonal norms here. The novelty claim is specifically the **simultaneous exact endpoint norms in the conductance-normalized model**, their **unique finite-size edge-orbit transition** and its **strict monotone drift to \(4/3\)**.

## Limitations

This is a theorem about one specified Euclidean orthogonal pair, not the best possible projection of the weighted edge space onto the same cut or cycle subspace. The weighted cut/cycle spaces depend on the square-root conductance normalization; they are not identified with ordinary graph cycle-flow subspaces under a weighted coordinate \(\ell_1\) metric. Only real endpoint \(\ell_1\) and \(\ell_\infty\) norms are asserted, not intermediate \(\ell_p\) norms. The analytical derivation is self-contained, but equivalently phrased electrical-current norm calculations in less readily indexed sources cannot be fully excluded. Independent mathematical audit has not been performed.

## References

1. S. J. Dilworth, D. Kutzarova, M. I. Ostrovskii, *Cycle Spaces: Invariant Projections and Applications to Transportation Cost*, Proceedings of Symposia in Pure Mathematics 106 (2024), 97–131; first preprint dated 2023-05-21, arXiv:2305.12582, https://arxiv.org/abs/2305.12582 ; open author offprint https://denka.web.illinois.edu/CycleSpaces.pdf . 2020 MSC primary 46B04.
2. J. Sedlák and A. Slavík, *Resistance distances and Kirchhoff indices in graph joins*, Journal of Physics A: Mathematical and Theoretical 58 (2025), 505203, DOI:10.1088/1751-8121/ae2997, https://doi.org/10.1088/1751-8121/ae2997 . Section 3 treats cycle joins and wheel resistance, as a methodological predecessor.
3. R. Balaji, R. B. Bapat and S. Goel, *An inverse formula for the distance matrix of a wheel graph with an even number of vertices*, Linear Algebra and its Applications 610 (2021), 274–292, DOI:10.1016/j.laa.2020.10.003. This concerns the ordinary distance matrix, distinct from the grounded electrical Green kernel here.

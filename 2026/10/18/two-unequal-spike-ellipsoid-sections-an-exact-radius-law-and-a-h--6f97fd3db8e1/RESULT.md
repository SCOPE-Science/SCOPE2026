# Two-unequal-spike ellipsoid sections: an exact radius law and a heavy-tail transition

## Finding

Let \(N\ge3\) and \(a>b>1\). For the centered ellipsoid
\[
E_N(a,b)=\left\{x\in\mathbb R^N:\frac{x_1^2}{a^2}+\frac{x_2^2}{b^2}+\sum_{j=3}^N x_j^2\le1\right\},
\]
let \(U\) be uniform on \(\mathbb S^{N-1}\), put \(H=U^\perp\), and write \(R_N=\max\{\|x\|_2:x\in E_N(a,b)\cap H\}\). The law of \(R_N\) is determined exactly by a two-dimensional random matrix. Put \(d_1=a^{-2}\), \(d_2=b^{-2}\), \(\alpha=1-d_1\), \(\beta=1-d_2\). Then
\[
\boxed{\quad R_N\stackrel{d}{=}\lambda_{\min}\!\left(\begin{bmatrix}d_1&0\\0&d_2\end{bmatrix}+\begin{bmatrix}\sqrt\alpha U_1\\\sqrt\beta U_2\end{bmatrix}\begin{bmatrix}\sqrt\alpha U_1&\sqrt\beta U_2\end{bmatrix}\right)^{-1/2}.\quad}
\]
In fact, this equality holds for each fixed unit normal \(U\), not merely in distribution. For \(b<r<a\), writing \(s=r^{-2}\), the exact cumulative distribution is
\[
\boxed{\quad\Pr(R_N\le r)=\Pr\!\left(\alpha U_1^2\ge(s-d_1)\left(1+\frac{\beta U_2^2}{d_2-s}\right)\right),\quad}
\]
where \((U_1^2,U_2^2,1-U_1^2-U_2^2)\sim\operatorname{Dirichlet}(1/2,1/2,(N-2)/2)\). In particular \(b\le R_N\le a\), and the deterministic best one-hyperplane radius is exactly \(b\).

For a sequence \(a_N\ge b_N>1\) with
\[
\frac{b_N}{\sqrt N}\longrightarrow c_2\in(0,\infty),\qquad\frac{a_N}{\sqrt N}\longrightarrow c_1\in[c_2,\infty],
\]
there is a complete critical/supercritical limit
\[
\boxed{\quad\frac{R_N}{\sqrt N}\ \Longrightarrow\ Z_{c_1,c_2}:=\lambda_{\min}\!\left(\begin{bmatrix}c_1^{-2}&0\\0&c_2^{-2}\end{bmatrix}+GG^{\mathsf T}\right)^{-1/2},\quad}
\]
where \(G=(G_1,G_2)^{\mathsf T}\) has independent standard Gaussian entries and \(\infty^{-2}=0\). If \(c_1=c_2\), the limiting radius equals \(c_2\) deterministically; for \(c_2<c_1<\infty\) its distribution is nondegenerate and supported on \([c_2,c_1]\). For \(c_1=\infty\), it is unbounded and satisfies the sharp tail law
\[
\boxed{\quad\lim_{t\to\infty}t\Pr(Z_{\infty,c_2}>t)=\sqrt{\frac2\pi}\,\mathbb E\sqrt{1+c_2^2G_2^2}.\quad}
\]
Thus \(\mathbb E Z_{\infty,c_2}^p<\infty\) holds exactly for \(0<p<1\); in particular its mean is infinite. Every finite-dimensional radius, by contrast, is bounded. Furthermore, in this supercritical regime, \(\mathbb E[R_N/\sqrt N]\to\infty\), whereas the optimal one-hyperplane radius obeys \(b_N/\sqrt N\to c_2\). This is a distributional, moment, and expected-performance transition for random one-measurement recovery from ellipsoids with two unequal exceptional axes.

## Assumptions and scope

All radii and orthogonality are Euclidean. The hyperplane is **central** and its normal is Haar uniform; this is different from an affine hyperplane chosen using translation-invariant Crofton measure. The exact matrix and CDF assertions assume \(N\ge3\), \(a>b>1\). The asymptotic assertion concerns sequences of two exceptional semiaxes, with the remaining \(N-2\) semiaxes equal to one. The secondary limit \(c_1=\infty\) means \(a_N/\sqrt N\to\infty\), not that a finite-dimensional ellipsoid has an infinite axis. If \(a=b\), every central hyperplane intersects the two-dimensional top eigenspace nontrivially and has radius exactly \(a\).

## Proof

**1. Exact spectral reduction.** For each unit vector \(x\in H\), the squared ellipsoid gauge is
\[
\|x\|_{E_N(a,b)}^2=1-\alpha x_1^2-\beta x_2^2.
\]
Consequently \(R_N^{-2}\) is the minimum gauge squared on the unit sphere in \(H\). Let \(P_H=I-UU^{\mathsf T}\), and define \(B:\mathbb R^2\to H\) by \(Bz=P_H(\sqrt\alpha z_1e_1+\sqrt\beta z_2e_2)\). The largest eigenvalue of \(BB^{\mathsf T}\) is that of
\[
B^{\mathsf T}B=egin{bmatrix}\alpha&0\\0&\beta\end{bmatrix}-ww^{\mathsf T},\qquad w=(\sqrt\alpha U_1,\sqrt\beta U_2)^{\mathsf T}.
\]
Therefore
\[
R_N^{-2}=1-\lambda_{\max}(B^{\mathsf T}B)
=\lambda_{\min}\big(\operatorname{diag}(d_1,d_2)+ww^{\mathsf T}\big).
\]
This works also when \(B\) is rank deficient, because \(\dim H\ge2\) and the missing eigenvalues of \(BB^{\mathsf T}\) are zero. Rayleigh interlacing for a positive rank-one update gives \(d_1\le R_N^{-2}\le d_2\). The lower radius bound \(R_N\ge b\) can also be seen directly from \(H\cap\operatorname{span}(e_1,e_2)\ne\{0\}\); equality is achieved by \(H=e_1^\perp\).

**2. Exact finite-dimensional distribution.** For \(s\in(d_1,d_2)\), the lower-right diagonal entry of \(D-sI\), with \(D=\operatorname{diag}(d_1,d_2)+ww^{\mathsf T}\), is \(d_2-s+\beta U_2^2>0\). Therefore \(\lambda_{\min}(D)\ge s\) is equivalent to \(\det(D-sI)\ge0\). Expanding and canceling the quartic term gives
\[
\det(D-sI)=(d_1-s)(d_2-s)+(d_2-s)\alpha U_1^2+(d_1-s)\beta U_2^2.
\]
Solving this inequality proves the displayed CDF formula. The Dirichlet distribution follows by writing \(U_j=G_j/(\sum_{k=1}^N G_k^2)^{1/2}\) for independent standard Gaussian coordinates. Equivalently, the formula is a one-dimensional beta integral: conditional on \(Y=U_2^2\sim\operatorname{Beta}(1/2,(N-1)/2)\), the variable \(U_1^2/(1-Y)\) is independent of \(Y\) and has law \(\operatorname{Beta}(1/2,(N-2)/2)\). Thus the CDF can be evaluated without sampling spherical directions.

**3. Gaussian critical limit.** Couple all dimensions using an infinite i.i.d. Gaussian sequence \((G_j)_{j\ge1}\). The strong law of large numbers gives \(\sqrt N(U_1,U_2)\to(G_1,G_2)\) almost surely. Entry by entry,
\[
N\big(\operatorname{diag}(a_N^{-2},b_N^{-2})+w_Nw_N^{\mathsf T}\big)
\longrightarrow\operatorname{diag}(c_1^{-2},c_2^{-2})+GG^{\mathsf T}.
\]
Its smallest eigenvalue is strictly positive almost surely: this is immediate for finite \(c_1\), and for \(c_1=\infty\) its determinant equals \(c_2^{-2}G_1^2>0\) almost surely. Continuity of the smallest eigenvalue and reciprocal square root proves the distributional limit, in fact almost sure convergence under this coupling. At equal finite parameters \(c_1=c_2\), a rank-one update of a scalar matrix leaves one eigenvalue equal to \(c_2^{-2}\). For unequal finite parameters, the continuous Gaussian input yields a nondegenerate law with support \([c_2,c_1]\): varying \(G_1\) with \(G_2=0\) approaches both endpoints, and neighborhoods of those inputs have positive Gaussian measure.

**4. Sharp supercritical tail and moments.** Put \(q=c_2^{-2}\). In the case \(c_1=\infty\), for every \(t>c_2\), the same determinant argument, with \(s=t^{-2}<q\), gives the **exact** tail probability
\[
\Pr(Z_{\infty,c_2}>t)=\mathbb E\left[\operatorname{erf}\left(\frac1{\sqrt2t}\sqrt{1+\frac{G_2^2}{q-t^{-2}}}\right)\right].
\]
Since \(\operatorname{erf}(y)\sim2y/\sqrt\pi\) as \(y\downarrow0\), dominated convergence applies after multiplication by \(t\), using \(\operatorname{erf}(y)\le2y/\sqrt\pi\) and the integrability of \(\sqrt{1+c_2^2G_2^2}\). This gives the stated positive finite tail constant. The layer-cake formula \(\mathbb E Z^p=p\int_0^\infty t^{p-1}\Pr(Z>t)\,dt\) then proves the exact moment threshold. To derive divergence of the finite-dimensional normalized expectations, apply convergence in distribution to each bounded continuous truncation \(x\mapsto\min(x,M)\). For every \(M>0\), one obtains \(\liminf_N\mathbb E[R_N/\sqrt N]\ge\mathbb E[\min(Z_{\infty,c_2},M)]\); the right-hand side increases without bound as \(M\to\infty\).

## Verification

The standalone file `check_two_spike.py` uses only Python's standard library. It constructs orthonormal hyperplane bases independently of the two-by-two reduction, computes the smallest eigenvalue of the restricted quadratic form by Jacobi rotations, and compares the resulting radii with the two-by-two formula. Its fixed-seed execution checks 420 independent normal/axis configurations (dimensions three, four, six, and eight), the determinant-event equivalence, exact axial boundary cases, a coupled high-dimensional crossover example, and numerical Gaussian quadrature for the asymptotic tail coefficient. Observed maximal absolute error of the direct eigenvalue comparisons was below \(1.1\times10^{-13}\). Numerical checks are not used as proofs of the all-dimensional statements.

Reproduce by running `python3 check_two_spike.py` in the directory containing this report and the checker. No third-party packages or data files are required.

## Relationship to prior work

Guedon, Litvak, Tatarko, and Vritsiou (2026, arXiv:2609.24131) study random radii of general convex bodies and \(p\)-ellipsoids; their Section 6.3 treats two-valued semiaxis sequences by high-probability bounds. Hinrichs, Krieg, Novak, Prochno, and Ullrich (arXiv:1901.06639) develop general high-probability estimates for random ellipsoid sections, and Hinrichs, Prochno, and Sonnleitner (arXiv:2109.14504) extend upper bounds to \(p\)-ellipsoids. The previously published exact **one-spike** beta law covers an ellipsoid with just one exceptional axis, not two distinct exceptional axes. The claim here is the exact unequal-two-spike finite-dimensional radius law, its critical Gaussian rank-two limit, and the supercritical sharp tail and moment transition, not a general bound from these papers.

## Limitations

The result is restricted to one central hyperplane measurement and exactly two exceptional semiaxes. It does not describe general Grassmannian codimension, noncentral affine sections, or more than two spikes. The infinite-mean assertion applies to the limiting supercritical distribution only; every radius at finite dimension has all moments. The cited general estimates and one-spike law are existing results and are not claimed as new. A generic finite-rank random matrix result may encode an equivalent distribution in another language; no claim of exhaustive historical priority is made.

## References

1. O. Guedon, A. E. Litvak, K. Tatarko, B.-H. Vritsiou, *On random diameters of convex bodies*, arXiv:2609.24131, first submitted September 21, 2026. https://arxiv.org/abs/2609.24131
2. A. Hinrichs, D. Krieg, E. Novak, J. Prochno, M. Ullrich, *Random sections of ellipsoids and the power of random information*, arXiv:1901.06639, first submitted January 20, 2019. https://arxiv.org/abs/1901.06639
3. A. Hinrichs, J. Prochno, M. Sonnleitner, *Random sections of \(\ell_p\)-ellipsoids, optimal recovery and Gelfand numbers of diagonal operators*, arXiv:2109.14504, first submitted September 29, 2021. https://arxiv.org/abs/2109.14504

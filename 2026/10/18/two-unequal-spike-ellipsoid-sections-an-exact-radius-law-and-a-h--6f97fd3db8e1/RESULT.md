# Sharp supercritical radius tail for central hyperplane sections of two-spike ellipsoids

## Finding

Let \(U_N\) be Haar uniform on \(\mathbb S^{N-1}\), and let \(R_N\) be the Euclidean radius of the section by \(U_N^\perp\) of the centered ellipsoid with semiaxes \((a_N,b_N,1,\ldots,1)\), where \(N\ge3\) and \(a_N\ge b_N>1\). Suppose \(b_N/\sqrt N\to c_2\in(0,\infty)\) and \(a_N/\sqrt N\to\infty\). Then \(R_N/\sqrt N\) converges in distribution to
\[
Z=\lambda_{\min}\!\left(\operatorname{diag}(0,c_2^{-2})+GG^{\mathsf T}\right)^{-1/2},
\qquad G=(G_1,G_2)^{\mathsf T},\quad G_1,G_2\stackrel{\rm iid}{\sim}N(0,1).
\]
The sharp upper tail is
\[
\lim_{t\to\infty}t\Pr(Z>t)=\sqrt{2/\pi}\,\mathbb E\sqrt{1+c_2^2G_2^2}.
\]
Among positive orders, \(Z\) has finite moments exactly for \(0<p<1\). Moreover \(\mathbb E[R_N/\sqrt N]\to\infty\), whereas the optimal central hyperplane section has radius \(b_N\), so its normalized radius tends to \(c_2\). The finite-dimensional distribution below is a specialization of the classical real orbital interlacing law, used as an input to these asymptotics.

## Assumptions and scope

The hyperplanes are central and all distances are Euclidean. The remaining \(N-2\) semiaxes are exactly one. The supercritical assumption is on a sequence of finite semiaxes; it does not introduce an infinite axis in finite dimension. The tail formula concerns the limiting random variable and does not assert a uniform joint \((N,t)\) estimate. Each finite-dimensional radius is bounded by \(a_N\).

## Proof

### Finite-dimensional reduction

Suppress the index \(N\). Write \(d_1=a^{-2}, d_2=b^{-2}\), \(\alpha=1-d_1\), \(\beta=1-d_2\), and \(H=U^\perp\). The inverse squared radius equals the minimum of \(1-\alpha x_1^2-\beta x_2^2\) over unit vectors in \(H\). If \(C:\mathbb R^2\to H\) has columns \(\sqrt\alpha P_He_1,\sqrt\beta P_He_2\), then this minimum is \(1-\lambda_{\max}(CC^{\mathsf T})\). The top eigenvalue is also that of \(C^{\mathsf T}C\), including in rank-deficient cases. For \(w=(\sqrt\alpha U_1,\sqrt\beta U_2)^{\mathsf T}\), the latter matrix is \(\operatorname{diag}(\alpha,\beta)-ww^{\mathsf T}\). Thus, for every fixed normal,
\[
R^{-2}=\lambda_{\min}(D),\qquad D=\operatorname{diag}(d_1,d_2)+ww^{\mathsf T}.
\]
Positive rank-one interlacing gives \(d_1\le R^{-2}\le d_2\); the lower radius bound \(R\ge b\) is attained for \(H=e_1^\perp\). If \(a=b\), the radius is \(b\) for every central hyperplane. When \(a>b\) and \(b<r<a\), set \(s=r^{-2}\). The lower-right entry of \(D-sI\) is positive, so \(R\le r\) is equivalent to \(\det(D-sI)\ge0\), or equivalently
\[
\alpha U_1^2\ge (s-d_1)\left(1+\frac{\beta U_2^2}{d_2-s}\right).
\]
The triple \((U_1^2,U_2^2,1-U_1^2-U_2^2)\) is Dirichlet with parameters \((1/2,1/2,(N-2)/2)\), by the normalized Gaussian representation. For another derivation in law, apply Assiotis–Najnudel, Definition 1.1 and Proposition 1.7, with real parameter \(\theta=1/2\) to the spectrum \((d_1,d_2,1,\ldots,1)\). Summing the Dirichlet weights of the repeated eigenvalue 1 and factoring out \((s-1)^{N-3}\) in the secular polynomial leaves exactly \(\det(sI-D)\). The repeated eigenvalue 1 cannot reduce the smallest eigenvalue. The exact finite-dimensional law is therefore already contained in that general result.

### Scaling and tail

Use a common infinite sequence of independent standard normals, writing \(U_N=(G_1,\ldots,G_N)/(\sum_{j=1}^N G_j^2)^{1/2}\). By the strong law, \(\sqrt N(U_1,U_2)\to(G_1,G_2)\) almost surely, and \(\alpha,\beta\to1\). Consequently \(ND\) converges almost surely to \(\operatorname{diag}(0,c_2^{-2})+GG^{\mathsf T}\). The limit is positive definite almost surely since its determinant is \(c_2^{-2}G_1^2\) and its trace is positive. Taking the reciprocal square root of the smallest eigenvalue gives the asserted convergence. The same computation when \(a_N/\sqrt N\to c_1\in[c_2,\infty)\) replaces 0 by \(c_1^{-2}\). That limit is constant \(c_2\) for equal parameters and has support \([c_2,c_1]\) otherwise: for \(G_2=0\), varying \(G_1\) ranges over the full interval, and the Gaussian distribution assigns positive probability to every open neighborhood of these inputs.

Put \(q=c_2^{-2}\). For \(t>c_2\), the lower-right entry of the limiting matrix minus \(t^{-2}I\) is positive. Its determinant is negative precisely when \(G_1^2<t^{-2}(1+G_2^2/(q-t^{-2}))\). Independence therefore gives
\[
\Pr(Z>t)=\mathbb E\,\operatorname{erf}\!\left(\frac{1}{\sqrt2\,t}\sqrt{1+\frac{G_2^2}{q-t^{-2}}}\right).
\]
Since \(\operatorname{erf}(u)/u\to 2/\sqrt\pi\) at zero and \(\operatorname{erf}(u)\le2u/\sqrt\pi\) for \(u\ge0\), the integrand multiplied by \(t\) is dominated for \(t\ge\sqrt2 c_2\) by \(\sqrt{2/\pi}\sqrt{1+2c_2^2G_2^2}\). Dominated convergence gives the tail constant. The positive finite constant and the layer-cake integral \(p\int_0^\infty t^{p-1}\Pr(Z>t)\,dt\) give the moment criterion. Finally \(x\mapsto\min(x,M)\) is bounded and continuous on \([0,\infty)\), so for each \(M\), \(\liminf_N\mathbb E[R_N/\sqrt N]\ge\mathbb E[\min(Z,M)]\). Let \(M\to\infty\) to obtain divergence without exchanging an unbounded moment with the scaling limit.

## Verification and relationship to prior work

The accompanying `check_two_spike.py` in the original source package provides finite numerical comparisons against a direct restriction to hyperplane bases, event and axial checks, and numerical illustrations of scaling and the tail coefficient. It uses Python's standard library; replay with `python3 check_two_spike.py` from its directory. These checks do not prove the limits; the preceding argument does.

The exact finite law is an explicit specialization of Dixon–Anderson interlacing, not claimed as an independent discovery. The work here evaluates the supercritical one-measurement law at its unbounded endpoint, determines its positive sharp tail coefficient, and compares its expected normalized radius with the bounded optimal benchmark. General estimates for ellipsoid sections do not by themselves supply that coefficient. No claim is made for affine sections, other codimensions, or more than two exceptional axes.

1. T. Assiotis and J. Najnudel, *The boundary of the orbital beta process*, arXiv:1905.08684, Definition 1.1 and Proposition 1.7.
2. O. Guedon, A. E. Litvak, K. Tatarko and V.-B. Vritsiou, *On random diameters of convex bodies*, arXiv:2609.24131, §6.3.
3. A. Hinrichs, D. Krieg, E. Novak, J. Prochno and M. Ullrich, *Random sections of ellipsoids and the power of random information*, arXiv:1901.06639, Theorems 3–5.
4. A. Hinrichs, J. Prochno and M. Sonnleitner, *Random sections of ℓₚ-ellipsoids, optimal recovery and Gelfand numbers of diagonal operators*, arXiv:2109.14504, Theorem A.

# Axial displacement of random simplex sections: exact means and a critical fluctuation crossover

## Finding

Fix an integer \(n\ge2\) and let \(\Delta_n=\operatorname{conv}\{e_0,\ldots,e_n\}\) be a regular simplex in the affine hyperplane \(\sum_{i=0}^n x_i=1\). Put \(c=(e_0+\cdots+e_n)/(n+1)\), \(y_t=(1-t)c+t e_0\), \(0\le t\le1\). Choose a hyperplane \(H_t\) through \(y_t\) whose (unoriented) normal is Haar-uniform on the unit sphere in the \(n\)-dimensional direction space of the affine hull. Let \(V_{n,t}\) count vertices of \(\Delta_n\cap H_t\), including a singleton as one vertex.

For \(0\le t<1\), write \(W=n+2t+nt^2\),
\[
A_n(t)=\arccos\!\left(-\frac{1+nt}{\sqrt{nW}}\right),\qquad
B_n(t)=\arccos\!\left(1-\frac{n+1}{W}\right).
\]
Then the **exact mean** is
\[
\boxed{\mathbb E V_{n,t}=F_n(t)=\frac n\pi A_n(t)+\frac{n(n-1)}{2\pi}B_n(t).}\tag{1}
\]
For \(n=2\), the mean is identically \(2\) on \([0,1)\). For every \(n\ge3\), it decreases **strictly** from the centroid to the vertex: \(F_n'(t)<0\) whenever \(0<t<1\). In fact
\[
F_n'(t)=\frac{n\sqrt{n+1}}{\pi W}
\left[\sqrt{n-1}-\frac{(n-1)(1+nt)}{\sqrt{n-1+4t+2nt^2}}\right].\tag{2}
\]
At the centroid, the exact mean is the previously known
\[F_n(0)=\binom{n+1}{2}\frac{\arccos(-1/n)}\pi,\]
and the new local axial response is
\[
\boxed{F_n''(0)=-\frac{n-2}{\pi}(n+1)\sqrt{\frac{n+1}{n-1}}.}\tag{3}
\]
At the vertex \(t=1\), the section degenerates on a positive-probability set, and its vertex-count law changes discontinuously. If \(K\) is uniform on \(\{0,1,\ldots,n\}\), then
\[
\boxed{V_{n,1}\overset{d}=1+K(n-K),\quad\mathbb E V_{n,1}=1+\frac{n(n-1)}6.}\tag{4}
\]
The size of the downward endpoint jump is exactly \(nA_n(1)/\pi-1>0\), with \(A_n(1)=\arccos(-\sqrt{(n+1)/(2n)})\).

There is also a **sharp two-scale probabilistic transition**. Let \(Z\) be standard normal, \(\Phi\) its CDF, and put \(m=n+1\). For each fixed \(t\in(0,1]\),
\[
\boxed{\frac{V_{n,t}}{m^2}\Longrightarrow\Phi(tZ)[1-\Phi(tZ)]\quad(n\to\infty),}\tag{5}
\]
whereas at \(t=0\) the normalized count converges to \(1/4\). All positive integer moments in (5) converge. In the critical window \(t=c_0/\sqrt m\), with any fixed \(c_0\ge0\), and for all sufficiently large \(m\),
\[
\boxed{\frac{m^2/4-V_{n,c_0/\sqrt m}}m
\Longrightarrow\left(\frac14-\frac1{2\pi}+\frac{c_0^2}{2\pi}\right)Z^2.}\tag{6}
\]
The classical central \(\chi_1^2\) law is the \(c_0=0\) endpoint; a displacement of order \(m^{-1/2}\) changes its coefficient. Finally, for every fixed \(t\in[0,1]\), including the endpoint in the sense of (4),
\[
\boxed{\lim_{n\to\infty}\frac{\mathbb E V_{n,t}}{(n+1)^2}
=\frac1{2\pi}\arccos\frac{t^2}{1+t^2}.}\tag{7}
\]

## Assumptions and scope

The hyperplane distribution is **orientation Haar measure conditioned on passing through a prescribed point**, not a translation-invariant measure on all affine hyperplanes. Sections and face counts are taken within the affine hull of the regular simplex; all genericity exceptions have probability zero for \(t<1\). The vertex endpoint \(t=1\) is treated separately, rather than by invalidly substituting into the generic edge-crossing formula. Formulae (1)–(4) hold at the stated finite dimensions; (5)–(7) are asymptotics, with the limit (6) restricted to any fixed critical-window parameter \(c_0\). No claim is made for arbitrarily shaped simplices or for other normal distributions.

## Proof

**1. Section vertices and the two-angle mean.** Put \(u_i=e_i-c\); their Gram matrix satisfies \(\langle u_i,u_i\rangle=n/(n+1)\) and \(\langle u_i,u_j\rangle=-1/(n+1)\) for \(i\ne j\). For \(t<1\), the point \(y_t\) is strictly interior to the simplex. A generic hyperplane through it meets each crossed edge at one section vertex, and every section vertex arises this way: a generic hyperplane section of a simplex has vertices on original edges, and different edges give different points. For a uniformly random (unoriented) Euclidean normal, the signs of its inner products with two nonzero vectors differ with probability equal to their angle divided by \(\pi\), by rotational symmetry in their two-dimensional span.

The rays from \(y_t\) to the vertices are \(r_0=(1-t)u_0\) and \(r_j=u_j-tu_0\), \(j>0\). Direct dot products give
\[
\cos\angle(r_0,r_j)=-\frac{1+nt}{\sqrt{n(n+2t+nt^2)}},\quad
\cos\angle(r_j,r_k)=1-\frac{n+1}{n+2t+nt^2}\quad(0<j\ne k).
\]
There are exactly \(n\) edges of the first type and \(n(n-1)/2\) of the second type. Summing their crossing probabilities proves (1). Substitution at \(t=0\) gives the known central mean.

**2. Strict monotonicity and local curvature.** Elementary differentiation of the two arccosine expressions in (1) simplifies to (2). Its bracket is zero at \(t=0\). For \(t>0\), comparison of the positive bracket terms is equivalent to
\[
(n-1)(1+nt)^2>n-1+4t+2nt^2.
\]
The difference equals \((n-2)(n+1)(2t+nt^2)\), which is positive for \(n>2\) and zero for \(n=2\). This proves all monotonicity assertions, with no numerical approximation. Differentiating (2) once at zero yields (3). The resulting Taylor expansion has an \(O_n(t^3)\) remainder for each fixed \(n\).

**3. Gaussian sign-count representation.** Let \(G_0,\ldots,G_n\) be independent standard normals and \(\bar G=m^{-1}\sum_{i=0}^n G_i\). The vector \((G_i-\bar G)_i\), after normalization, is Haar-uniform in the \(n\)-dimensional zero-sum subspace. Its signed height at vertex \(e_i\) relative to the hyperplane through \(y_t\) equals
\[
G_i-T_m,\qquad T_m=(1-t)\bar G+tG_0.
\]
For every \(t<1\), the weighted mean of those heights at \(y_t\) vanishes with all positive barycentric weights. Hence both signs occur almost surely. Setting \(K_m=\#\{i:G_i>T_m\}\) gives the **exact distributional identity**
\[
V_{n,t}\overset d=K_m(m-K_m),\qquad 0\le t<1.\tag{8}
\]
For \(t=1\), the distinguished vertex lies on the section. Among the remaining \(n\) heights \(G_j-G_0\), let \(K=\#\{j>0:G_j>G_0\}\). In addition to the one vertex \(e_0\), precisely \(K(n-K)\) crossed edges among the other \(n\) vertices contribute vertices. By exchangeability of distinct iid continuous observations, the rank of \(G_0\) is uniform on \(\{0,\ldots,n\}\), establishing (4). The \(t\uparrow1\) limit of (1) has its second term \(n(n-1)/6\), so its difference from (4) is \(nA_n(1)/\pi-1\). This is positive because \(A_n(1)\ge5\pi/6\) for \(n=2\) and is larger than \(\pi/n\) for all \(n\ge2\) (indeed \(A_n(1)>\pi/2\) and \(nA_n(1)>\pi\) for \(n>2\)).

**4. Fixed-displacement asymptotic law.** On one infinite iid Gaussian sequence, \(\bar G\to0\) almost surely. Uniform convergence of the empirical distribution functions gives \(K_m/m\to1-\Phi(tG_0)\) almost surely for each fixed \(0<t<1\). Inserting this into (8) proves (5) for these \(t\). At \(t=1\), the same limit follows by using the rank count \(K/n\to1-\Phi(G_0)\) and (4). At \(t=0\), \(\bar G\to0\) yields \(K_m/m\to1/2\). Every normalized vertex count is bounded by \(1/4+o(1)\), so bounded convergence supplies all moment limits. For the mean limit, if \(X,Y,Z\) are independent standard normals, \(\mathbb E[\Phi(tZ)(1-\Phi(tZ))]=\Pr(X\le tZ<Y)\). The correlated pair \((X-tZ,Y-tZ)\) has correlation \(t^2/(1+t^2)\), and the bivariate Gaussian angular formula evaluates this probability as the right-hand side of (7).

**5. Critical displacement and the changed chi-square coefficient.** Put \(t_m=c_0/\sqrt m\), \(\phi_0=(2\pi)^{-1/2}\). Then \(T_m=O_{\mathbb P}(m^{-1/2})\) and
\[
\sqrt mT_m=\frac1{\sqrt m}\sum_{i=0}^n G_i+c_0G_0+o_{\mathbb P}(1).
\]
At any random threshold of order \(m^{-1/2}\), the empirical Gaussian CDF differs from its value at zero by \(\phi_0 T_m+o_{\mathbb P}(m^{-1/2})\) after subtracting its empirical fluctuation at zero. For clarity, the needed stochastic equicontinuity follows from a deterministic grid on \([-C/\sqrt m,C/\sqrt m]\) of mesh \(m^{-3/4}\), with \(O_C(m^{1/4})\) points: centered binomial counts from zero to any grid point have variance \(O_C(\sqrt m)\), and Chebyshev plus a union bound controls their maxima by \(o_{\mathbb P}(\sqrt m)\); the counts between adjacent grid points also have \(o_{\mathbb P}(\sqrt m)\) fluctuations. Choosing \(C\) large makes the complement probability arbitrarily small. The normal CDF Taylor remainder is uniformly \(O(m^{-3/2})\) on this interval.

Consequently
\[
\frac{K_m-m/2}{\sqrt m}
=\frac1{\sqrt m}\sum_{i=0}^n
\left(\boldsymbol1_{\{G_i>0\}}-\frac12-\phi_0G_i\right)
-c_0\phi_0G_0+o_{\mathbb P}(1).\tag{9}
\]
The summands are centered and have variance \(\sigma^2=1/4-1/(2\pi)\), since \(\mathbb E[G\boldsymbol1_{\{G>0\}}]=\phi_0\). Omitting the single \(i=0\) summand incurs only \(o_{\mathbb P}(1)\), leaving a classical iid CLT limit independent of \(G_0\). Thus (9) converges to a centered normal of variance \(\sigma^2+c_0^2/(2\pi)\). The exact identity \(m^2/4-V=(K_m-m/2)^2\) and the continuous mapping theorem yield (6). This is an infinite-dimensional asymptotic proof, not an inference from simulations.

## Verification

Run the standalone `verify.py` with Python 3 and NumPy. The program constructs the Euclidean ray vectors independently of the closed trigonometric expressions, compares finite differences for the derivative and Hessian identities, enumerates the distinguished rank exactly, and independently simulates signed edge crossings and the critical-window and fixed-displacement probability laws. Its reproducible execution returned `VERIFY_OK: 2183 deterministic assertions, including rank enumeration and numerical samples.` The analytic argument above, not these finite comparisons, establishes the universal equations and weak limits.

## Relationship to prior work

Brazitikos and Pandis (2026, arXiv:2606.07163v1) study restricted hyperplane sections of regular simplices and cross-polytopes, with central and noncentral geometric volume extremal questions. Dirksen (2015, arXiv:1509.06408) and König (2023, arXiv:2312.01325) address deterministic section-volume questions; the latter was available here only in abstract. These sources motivate the axial noncentral regime but do not provide the distribution of random section **vertex counts**.

Two relevant published research results establish, respectively, the exact mean and chi-square vertex-count fluctuations of **central** regular-simplex sections, and their joint central face-vector fluctuations. The central expectation and the coefficient \(\sigma^2\) above are credited to that work. Their results explicitly restrict the hyperplane to the centroid, whereas the present claim concerns an entire axial displacement, a sharp finite-dimensional monotonicity identity, a vertex degeneracy jump, an order-one displacement law, and the displacement boundary-layer crossover. Affentranger and Schneider (1992) study random **projections** of regular simplices, a different model. The available comparisons do not exclude equivalent statements in older or unindexed literature.

## Limitations

The result is restricted to Euclidean Haar orientation, a regular simplex, and a displacement along one vertex-to-centroid axis. For \(t=1\) it uses a singleton-inclusive convention for section vertex counts. The qualitative fluctuation crossover is proved for fixed \(t\) and for \(t=c_0/\sqrt{n+1}\) with fixed \(c_0\); no uniform distributional approximation over every varying \(t\) is asserted. The historical-novelty search is not exhaustive. Independent scientific validation has not been performed.

## References

1. S. Brazitikos and C. Pandis, *Restricted Hyperplane Sections of the Cross-Polytope and the Simplex*, arXiv:2606.07163v1 (first publicly submitted 2026-06-05).
2. H. Dirksen, *Sections of the regular simplex – Volume formulas and estimates*, arXiv:1509.06408.
3. H. König, *Non-central sections of the regular n-simplex*, arXiv:2312.01325.
4. F. Affentranger and R. Schneider, *Random projections of regular simplices*, Discrete & Computational Geometry 7 (1992), 219–226.
5. *Exact mean and chi-square fluctuations of Haar central simplex-section vertex counts*, published mathematical record: https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exact-mean-and-chi-square-fluctuations-of-haar-central-simplex-s--d3f9b0447a8e.
6. *Joint chi-square face-vector fluctuations of random central regular-simplex sections*, published mathematical record: https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-joint-chi-square-face-vector-fluctuations-of-random-central-regu--aa90c887fe90.

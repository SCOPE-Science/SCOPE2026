# A sharp Euclidean spoke threshold and inverse-square scaling for electrical wheel metrics

## Finding
Let \(m\ge3\) be an integer. Equip the wheel with a hub \(h\) and a cyclic rim \(\{0,\ldots,m-1\}\) with unit electrical conductance on each rim edge and a common positive electrical conductance \(r\) on each hub-to-rim spoke. Let \(R\) be its **effective-resistance distance**, not its vertex shortest-path distance or the square root of resistance.

For \(a>0\) define
\[
r=2(\cosh a-1),\qquad
Q_{m,k}(a)=\frac{\cosh((m/2-k)a)}{\cosh(ma/2)},\qquad
H_m(a)=\frac2m\sum_{k=0}^{m-1}(1-Q_{m,k}(a))^2.
\]
There exists a unique \(a_m>0\) such that \(H_m(a_m)=1\). Put \(r_m=2(\cosh a_m-1)\). Then:

1. **Sharp Euclidean phase transition.** The metric \(R\) is isometrically embeddable in Euclidean space if and only if \(0<r\le r_m\). For \(0<r<r_m\), it has strict \(2\)-negative type and minimum Euclidean embedding dimension \(m\). At \(r=r_m\), it has non-strict \(2\)-negative type and minimum Euclidean embedding dimension \(m-1\); its complete zero-sum equality space is spanned by the coefficients \((m,-1,\ldots,-1)\), with the hub listed first. For \(r>r_m\), it fails \(2\)-negative type. In the latter case the centered Gram matrix of squared resistances has exactly one negative eigenvalue and \(m-1\) positive eigenvalues on the \(m\)-dimensional zero-sum space.
2. **Generalized-roundness regimes.** Writing \(\wp(m,r)\) for the supremal exponent of negative type of \(R\), one has \(\wp(m,r)>2\) when \(r<r_m\), \(\wp(m,r)=2\) when \(r=r_m\), and \(1<\wp(m,r)<2\) when \(r>r_m\). The first alternative permits infinite supremum (the equilateral four-vertex wheel at \(m=3,r=1\) is one such case).
3. **Exact small threshold and continuum scaling.** The first threshold is \(r_3=3+2\sqrt3\). As \(m\to\infty\),
\[
\lim_{m\to\infty}m^2r_m=c_*^2=34.84767129506\ldots,
\]
where \(c_*=5.90319161937\ldots\) is the unique positive solution of
\[
\frac6{c_*}\tanh\left(\frac{c_*}2\right)=1+\operatorname{sech}^2\left(\frac{c_*}2\right).
\]
Thus the spoke strength permitted by Euclidean resistance geometry decays at the exact inverse-square scale of rim size.

## Assumptions and scope
All graph vertices are included. There are \(m+1\) vertices, with \(m\ge3\), and all conductances are strictly positive. Rim conductances are normalized to \(1\); only the common spoke conductance \(r\) varies. Distances are electrical effective resistances in this weighted finite network. A metric \(d\) has \(p\)-negative type if, for every real vector \(z\) indexed by its vertices with \(\sum z_i=0\), one has \(\sum_{i,j}z_i z_j d(i,j)^p\le0\). Strict negative type means strict inequality for every nonzero such vector. A Euclidean embedding of \(R\) means that ordinary Euclidean distance between images equals \(R(i,j)\), so its distance-squared matrix is \((R(i,j)^2)\).

The limiting assertion concerns the sequence of all integral rim lengths \(m\to\infty\), with each threshold defined by its own exact scalar equation. No claim is made about unequal spoke conductances, other rim weights, or the exact general exponent \(\wp(m,r)\) away from the critical boundary.

## Proof
**1. Electrical Green kernel.** Ground the hub. The grounded Laplacian on the rim is the positive-definite matrix \(A=rI+\Delta_{C_m}\), where the cycle Laplacian has diagonal \(2\) and entries \(-1\) at the two cyclic neighbors. With
\[
t=e^{-a}\in(0,1),\qquad r=t+t^{-1}-2=\frac{(1-t)^2}{t},\qquad
C=\frac{t}{(1-t^2)(1-t^m)},
\]
its inverse is the circulant Green matrix
\[
(A^{-1})_{ij}=g_k=C(t^k+t^{m-k}),\qquad k\equiv j-i\pmod m,\quad 0\le k<m.
\]
To verify this directly, apply \(r+2\) times the value at \(k\), minus the values at \(k-1\) and \(k+1\). The result is zero for \(1\le k<m\), by \(r+2=t+t^{-1}\); at \(k=0\), the result is \(C(t^{-1}-t)(1-t^m)=1\). This proves the displayed inverse without a spectral assumption.

The effective resistance from hub to any rim vertex is \(\alpha=g_0=C(1+t^m)\), and between rim vertices at separation \(k\) is
\[
\delta_k=2(g_0-g_k)=2C(1-t^k)(1-t^{m-k})
=2\alpha(1-Q_{m,k}(a)).
\]
Both formulas follow from the voltage-drop identity using the grounded inverse. In particular, \(\delta_0=0\), and all distinct vertices have positive distance.

**2. Every nonconstant rim Fourier mode is strictly Euclidean.** Let \(D_{\mathrm{rim}}^{(2)}\) be the circulant matrix with \((i,j)\)-entry \(\delta_{j-i}^2\). For \(1\le j<m\), put \(x_j=\cos(2\pi j/m)\). Expanding the square of \((1-t^k)(1-t^{m-k})\), and summing the two resulting finite geometric series, gives the exact Fourier eigenvalue
\[
\widehat D_j=-\frac{4C^2(1-t^{2m})(1-t^2)(1-t)^2\bigl((1+t)^2+2t x_j\bigr)}{(1-2t x_j+t^2)(1-2t^2x_j+t^4)}.
\]
Every factor in the denominator is strictly positive and \((1+t)^2+2tx_j\ge1+t^2>0\). Hence \(\widehat D_j<0\) for every nonzero frequency. Consequently the centered matrix \(-\tfrac12J_mD_{\mathrm{rim}}^{(2)}J_m\), where \(J_m=I_m-m^{-1}{\bf1}{\bf1}^{\mathsf T}\), is strictly positive on rim zero-sum vectors and has rank \(m-1\). Its diagonal is constant, equal to
\[
\beta^2=\frac{1}{2m}\sum_{k=0}^{m-1}\delta_k^2
=\frac{\alpha^2}{m/2}\sum_{k=0}^{m-1}(1-Q_{m,k}(a))^2
=\alpha^2 H_m(a).
\]
Thus the rim alone is a full \((m-1)\)-dimensional Euclidean simplex, with every vertex at radius \(\beta\) from its centroid.

**3. Precisely one radial obstruction.** The hub must be at the same ordinary Euclidean distance \(\alpha\) from every rim point. As the rim points affinely span their \((m-1)\)-dimensional space, any such hub has orthogonal projection at their centroid. Such a point exists if and only if \(\alpha^2\ge\beta^2\), equivalently \(H_m(a)\le1\). If \(\alpha>\beta\), a nonzero orthogonal coordinate is needed, giving dimension \(m\); if \(\alpha=\beta\), the hub lies at the rim centroid, giving dimension \(m-1\). The equality coefficients then have hub component \(m\) and \(-1\) on each rim vertex.

For a direct negative-type proof valid also in the non-Euclidean region, write any zero-sum coefficient vector as hub coefficient \(s\), rim coefficients \(-s/m+z_i\) with \(\sum z_i=0\). Cyclic symmetry eliminates the cross term, and its squared-resistance quadratic form is
\[
\sum_{u,v}w_u w_v R(u,v)^2
=z^{\mathsf T}D_{\mathrm{rim}}^{(2)}z
+2s^2(\beta^2-\alpha^2).
\]
The first term is strictly negative when \(z\ne0\); the second changes sign exactly at \(H_m(a)=1\). This proves strictness, complete critical equality, and the exactly-one-obstruction inertia assertion, without presupposing a Euclidean embedding.

**4. Existence and uniqueness of the conductance transition.** For \(1\le k<m\), let \(b=|m/2-k|<m/2\). The logarithmic derivative of \(Q_{m,k}(a)\) is
\[
\frac{d}{da}\log Q_{m,k}(a)=b\tanh(ba)-(m/2)\tanh(ma/2)<0,
\]
because \(u\mapsto u\tanh(au)\) is strictly increasing for \(u>0\). Therefore \(H_m(a)\) increases strictly from \(0\), as \(a\downarrow0\), to \(2(m-1)/m>1\), as \(a\to\infty\). A unique \(a_m>0\) satisfies \(H_m(a_m)=1\), with \(H_m(a)\le1\) exactly for \(a\le a_m\). The map \(a\mapsto2(\cosh a-1)\) is strictly increasing, proving the sharp threshold.

For \(m=3\), the rim is an equilateral three-point metric with side \(2/(r+3)\), and every hub-to-rim resistance equals \((r+1)/(r(r+3))\). The Euclidean circumradius condition reads \((r+1)^2/r^2\ge4/3\). Its unique positive equality point is \(r_3=3+2\sqrt3\).

**5. Supremal negative-type exponent.** When \(r<r_m\), strict \(2\)-negative type persists on a nonzero interval above \(2\): the zero-sum unit sphere is compact and its powered-distance quadratic form depends continuously on the exponent. At \(r=r_m\), the coefficients \((1,-1/m,\ldots,-1/m)\) produce the power-\(p\) form
\[
\alpha^p\left[\frac1m\sum_{k=0}^{m-1}(\delta_k/\alpha)^p-2\right].
\]
At \(p=2\), the bracket is zero. For \(p>2\), Jensen's inequality gives its first term at least \(2^{p/2}>2\), hence negative type fails for all such \(p\). Thus the supremum at equality is exactly \(2\). If \(r>r_m\), the same radial vector fails at \(p=2\), while the ordinary resistance matrix has strict \(1\)-negative type: for any nonzero zero-sum \(w\), its quadratic form is \(-2w^{\mathsf T}L^+w<0\), where \(L^+\) is the electrical Laplacian pseudoinverse. Strictness at \(1\), compactness, and the standard interval property of negative type imply a supremum strictly between \(1\) and \(2\).

**6. Scaling limit.** For fixed \(c>0\), the Riemann sum \(H_m(c/m)\) converges to
\[
H_\infty(c)=2\int_0^1\left(1-\frac{\cosh(c(1/2-u))}{\cosh(c/2)}\right)^2du
=2\left(1+\frac1{1+\cosh c}-\frac3c\tanh(c/2)\right).
\]
Each integrand for \(0<u<1\) increases strictly in \(c\), so \(H_\infty\) is strictly increasing from \(0\) to \(2\). Its unique unit crossing \(c_*\) satisfies the scalar equation in the finding. For any \(c_-<c_*<c_+\), convergence and monotonicity imply \(c_-<ma_m<c_+\) for all sufficiently large \(m\). Hence \(ma_m\to c_*\). Finally, \(r_m=2(\cosh a_m-1)=a_m^2(1+o(1))\), proving \(m^2r_m\to c_*^2\).

## Verification
The standalone standard-library checker `verify_wheel_resistance.py` reconstructs exact rational grounded Laplacians and inverses for rim sizes \(3\) through \(11\), at five rational conductances per size (45 independently inverted networks). It tests the Green formula, cyclic distance identities, the exact radial sign and all nonconstant squared-distance Fourier eigenvalues. It additionally checks the algebraic \(m=3\) threshold and the convergence diagnostic through rim size \(200\). It reports `ALL_WHEEL_RESISTANCE_CHECKS_OK exact_cases= 45` when all assertions pass. These finite and floating-point checks are supporting diagnostics; steps 1–6 provide the proof for every admissible parameter.

## Relationship to prior work
Bapat and Gupta, *Resistance distance in wheels and fans* (2010; author manuscript dated February 24, 2009), derive weighted wheel resistance entries using generalized Fibonacci numbers and grounded Laplacian methods. Those pairwise formulas are a direct and especially close antecedent. Their inspected introduction, main weighted-wheel theorem and proof, and following fan section do not state a squared-resistance negative-type criterion, a unique Euclidean spoke threshold, a one-dimensional obstruction, or its inverse-square scaling. The present result uses the known resistance setup but applies a different centered squared-distance Fourier and circumradius analysis.

Zhang and Yang (first publicly published September 5, 2006) study resistance distances and Kirchhoff indices of circulant graphs, giving spectral resistance formulas; the wheel including its hub is not itself a circulant graph. Li and Weston (arXiv:0901.0695, first public version January 6, 2009) give general strict-negative-type principles. Sánchez (arXiv:1108.0451, August 2, 2011) gives a general finite-metric criterion and evaluates **shortest-path** complete bipartite graphs, rather than resistance metrics of weighted wheels. None of these inspected statements implies the present explicit conductance transition without additional analysis.

Closely named work on wheel symmetric-edge polytopes concerns convex bodies built from graph edge vectors, not the electrical resistance metric. Related exact results for weighted resistance cycles concern only the rim without the hub, and heat-Lipschitz wheel results concern semigroup operator norms rather than Hilbert embeddability. These distinctions compare mathematical implications, not merely titles. A previously unindexed equivalent computation remains possible and would affect priority.

## Limitations
The theorem requires one common spoke conductance and one common rim conductance. It gives the phase at exponent \(2\), the complete equality space at the unique conductance threshold, and the qualitative regimes of supremal negative type; it does not give an exact general formula for \(\wp(m,r)\) away from the threshold. The asymptotic constant comes from a limiting scalar equation, not an assertion of independent publication or priority. No independent audit has been performed. Related weighted-wheel resistance formulas were already known, and the distinction between squared-resistance geometry and previously tabulated distances is essential.

## References
- R. B. Bapat and S. Gupta, *Resistance distance in wheels and fans*, Indian Journal of Pure and Applied Mathematics **41** (2010), 1–13, doi:10.1007/s13226-010-0004-2; accessible author manuscript at https://www.researchgate.net/publication/225679174_Resistance_distance_in_wheels_and_fans (dated February 24, 2009).
- H. Zhang and Y. Yang, *Resistance distance and Kirchhoff index in circulant graphs*, International Journal of Quantum Chemistry **107** (2007), 330–339, first online September 5, 2006, doi:10.1002/qua.21068.
- H. Li and A. Weston, *Strict \(p\)-negative type of a metric space*, arXiv:0901.0695 (first public version January 6, 2009), https://arxiv.org/abs/0901.0695.
- S. Sánchez, *On the supremal \(p\)-negative type of a finite metric space*, arXiv:1108.0451 (first public version August 2, 2011), https://arxiv.org/abs/1108.0451.

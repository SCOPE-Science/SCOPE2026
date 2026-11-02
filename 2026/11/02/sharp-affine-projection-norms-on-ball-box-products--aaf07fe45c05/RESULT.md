# Sharp affine-projection norms on ball–box products

## Finding

Fix integers \(d\ge1\) and \(k\ge0\). Let \(K_{d,k}=B_2^d\times[-1,1]^k\), where \(B_2^d=\{x\in\mathbb R^d:\|x\|_2\le1\}\), with normalized uniform volume measure \(\mu_{d,k}\). Let \(P_{d,k}\) be the real \(L^2(\mu_{d,k})\)-orthogonal projection onto all polynomials of total degree at most one. Its norm here is the induced real \(L^\infty(\mu_{d,k})\to L^\infty(\mu_{d,k})\) norm, not the minimum over all projections onto the same subspace.

For \(m\ge1\), set
\[
c_d=\frac{\Gamma(d/2+1)}{\sqrt\pi\,\Gamma((d+1)/2)},\qquad
H_{d,m}(v)=c_d\int_{-1}^{\min\{v,1\}}(v-z)^m(1-z^2)^{(d-1)/2}\,dz,
\]
where \(H_{d,m}(v)=0\) when \(v\le-1\). Then the **exact, attained sharp norm** for every \(d\ge1,k\ge0\) is
\[
\boxed{\displaystyle
\|P_{d,k}\|_{\infty\to\infty}
=1+\frac{12}{(k+1)!}\left(\frac{d+2}{6}\right)^{k+1}
\sum_{j=0}^{k}(-1)^j\binom kj
H_{d,k+1}\!\left(\frac{3k-1-6j}{d+2}\right).}
\]
The expression is a finite incomplete-beta evaluation, not a variational characterization. When \(d\) is odd, its value is **rational** for every nonnegative integer \(k\). In the ordinary solid circular cylinder, \(d=2,k=1\), it specializes to
\[
\boxed{\|P_{2,1}\|_{\infty\to\infty}=\frac{17}{9}+\frac{3\sqrt3}{4\pi}.}
\]

The absolute kernel-row integral reaches its maximum **precisely** at \(\partial B_2^d\times\{-1,1\}^k\); when \(k=0\), interpret the second factor as a singleton. Each maximizing row yields an extremizing input given by the sign of its integral kernel. The largest possible negative value in absolute magnitude of \(P_{d,k}f\), over all measurable \(0\le f\le1\), equals \((\|P_{d,k}\|_{\infty\to\infty}-1)/2\).

Write \(N=d+k\). Along **every** sequence with \(N\to\infty\),
\[
\boxed{\displaystyle
\frac{\|P_{d,k}\|_{\infty\to\infty}}{\sqrt{d+2+3k}}
\longrightarrow\sqrt{\frac2\pi}.}
\]
In particular, whenever \(k/N\to\theta\in[0,1]\),
\[
\boxed{\displaystyle \frac{\|P_{d,k}\|_{\infty\to\infty}}{\sqrt N}
\longrightarrow \sqrt{\frac{2(1+2\theta)}\pi}.}
\]
Thus the limiting stability coefficient interpolates continuously between a Euclidean-ball regime and a cubical regime, with sharp factor \(\sqrt3\) between the two endpoints.

## Assumptions and scope

All bodies are solid, with normalized Lebesgue measure and a real scalar field. The ball factor has dimension at least one; any positive number of independent interval factors is allowed. Affine coordinate rescalings preserve the norm, so axis lengths do not enter. The projection is the canonical ordinary \(L^2\) least-squares projector onto the **total-degree-one** polynomial space, not a tensor-product projection onto all separately degree-one terms. No independent audit or priority certification is implied.

## Proof

**1. Kernel reconstruction.** By symmetry, the mean of every coordinate on \(K_{d,k}\) is zero, the ball-coordinate covariance is \((d+2)^{-1}I_d\), the interval-coordinate covariance is \(3^{-1}I_k\), and cross covariances vanish. Consequently the exact reproducing kernel is
\[
\mathcal K((x,t),(y,s))=1+(d+2)\langle x,y\rangle+3\sum_{i=1}^kt_is_i.
\]
Orthogonality follows directly by integrating this kernel against each basis function \(1,y_j,s_i\). For a bounded input \(f\),
\(P_{d,k}f(x,t)=\int_{K_{d,k}}\mathcal K((x,t),(y,s))f(y,s)\,d\mu_{d,k}\).

**2. Exact location of maximizers.** Let \(Z_d\) be the first coordinate of a uniformly distributed point of \(B_2^d\), and let \(U_1,\ldots,U_k\) be independent uniform variables on \([-1,1]\), independent of \(Z_d\). Rotational invariance and symmetry show that the absolute kernel-row integral for \((x,t)\) is
\[
F(\|x\|_2,|t_1|,\ldots,|t_k|)
=\mathbb E\left|1+(d+2)\|x\|_2Z_d+3\sum_{i=1}^k|t_i|U_i\right|.
\]
For a symmetric variable \(X\) independent of \(V\), \(a\mapsto\mathbb E|V+aX|\) is convex, even, and therefore nondecreasing for \(a\ge0\). Thus all row integrals are at most \(F(1,1,\ldots,1)\). This maximum is strict whenever one amplitude is reduced: to test a reduced ball amplitude, first set all interval amplitudes to one; \(1+3\sum U_i\) has support meeting zero when \(k\ge1\), and for \(k=0\) the remaining value \(1\) lies strictly inside the support of \((d+2)Z_d\). To test any reduced interval amplitude, first maximize the remaining amplitudes; \(1+(d+2)Z_d\) has density positive near zero. In either case, averaging the absolute value over the varied symmetric variable is strictly larger at full amplitude because an open set of the remaining values experiences a sign change. Monotonicity in the other amplitudes completes the strict characterization.

The kernel is continuous on a compact support having positive volume in every interior neighborhood. Hence essential suprema equal the corresponding spatial suprema. At any maximizing row \((x_*,t_*)\), the bounded measurable input \(f(y,s)=\operatorname{sgn}\mathcal K((x_*,t_*),(y,s))\) attains the sharp operator norm. Since every kernel row integrates to one, choosing instead the indicator of its negative region gives sharp negative output magnitude \((\|P_{d,k}\|-1)/2\).

**3. A finite exact formula.** The random variable \(Z_d\) has density
\[
f_d(z)=c_d(1-z^2)^{(d-1)/2}\mathbf1_{[-1,1]}(z).
\]
Write \(U_i=2V_i-1\), with \(V_i\) uniform on \([0,1]\), and put \(S=\sum_{i=1}^kV_i\) (take \(S=0\) when \(k=0\)). Conditional on \(Z_d=z\), the kernel at a maximizing row has the law \(1+(d+2)z+6S-3k\). The elementary positive-part identity \(|a|=a+2(-a)_+\), combined with the Irwin–Hall positive-part formula
\[
\mathbb E(t-S)_+
=\frac1{(k+1)!}\sum_{j=0}^k(-1)^j\binom kj(t-j)_+^{k+1},
\]
which also holds for the degenerate \(k=0\) case, produces precisely the displayed finite sum after averaging over \(Z_d\). The Irwin–Hall identity follows by integrating its standard inclusion–exclusion cumulative distribution once, so the formula makes no unverified continuity or sampling assumption.

For explicit evaluation by incomplete beta functions, expand \((v-z)^m\) in \(H_{d,m}\). On \(-1<v<1\), the moments \(\int_{-1}^v z^j(1-z^2)^{(d-1)/2}\,dz\) are finite combinations of the complete and incomplete beta functions with parameters \(((j+1)/2,(d+1)/2)\), using the substitution \(u=z^2\) separately on the two half-intervals. Outside this interval, use either zero or the full beta moments. For odd \(d\), both \(c_d\) and the weight \((1-z^2)^{(d-1)/2}\) are rational polynomials, while every integration endpoint in the finite sum is rational; rationality follows. For \(d=2,k=1\), integrating the uniform interval variable first reduces the absolute value to \(((1+4z)^2+9)/6\) on \(-1\le z\le1/2\) and to \(1+4z\) on \(1/2\le z\le1\). Integrating against \((2/\pi)\sqrt{1-z^2}\) gives \(17/9+3\sqrt3/(4\pi)\).

**4. Sharp high-dimensional limit.** Independence and the computed covariances give variance \(d+2+3k\) for \((d+2)Z_d+3\sum U_i\). As \(d\to\infty\), \(\sqrt{d+2}Z_d\) converges in distribution to a standard normal, by the Gaussian representation of uniform ball directions and concentration of the radius. As \(k\to\infty\), \(\sqrt{3/k}\sum U_i\) converges to an independent standard normal by the bounded-variable central limit theorem. For every diverging \(d+k\), subsequences of the two variance proportions yield an asymptotically standard normal sum, including the cases where one component remains bounded. Normalized second moments remain exactly one, giving uniform integrability of the absolute value. The additive kernel constant \(1\) vanishes after division by \(\sqrt{d+2+3k}\), and the expectation converges to \(\mathbb E|G|=\sqrt{2/\pi}\). Rewriting the denominator in terms of \(N\) and \(k/N\) gives the second limit.

## Verification

The accompanying standalone `verification.py` compares the exact truncated-positive-part formula against independent nested integration of the raw absolute kernel. It passed 24 such dimension-pair comparisons, 24 exact-rational comparisons for odd ball dimensions, an independent symbolic disk-cylinder benchmark, and four numerical monotonicity sanity checks. Each equality in the proof is analytic for all allowed dimensions; finite checks are not presented as proofs of the infinite or strict statements. Run `python3 verification.py` with Python 3, NumPy, SciPy and SymPy. The source file and its hash are embedded with this result.

## Relationship to prior work

Wade, *A Discretized Fourier Orthogonal Expansion in Orthogonal Polynomials on a Cylinder*, arXiv:0906.2408 (first posted 12 June 2009), studies a disk–interval cylinder using a **Chebyshev weight in the interval direction** and a discretized Radon-data Fourier expansion, with a large-degree Lebesgue-constant order; its displayed operator is not the ordinary uniform-volume degree-one orthoprojector here. Li and Xu, *Spectral Approximation on the Unit Ball*, arXiv:1310.2283 (first posted 8 October 2013), study ball polynomial approximations and Sobolev error bounds, not this mixed product's exact affine \(L^\infty\) constant.

The pure cube case \(d=1\), the pure ball case \(k=0\), and affine least-squares projection on simplices are important benchmarks, not asserted to be independently new. The present mixed-family exact finite formula, strict product-boundary extremizers, and full ball-to-cube asymptotic crossover are not implied by the compared statements. The comparison is evidence of distinction, not a proof that no equivalent older result exists.

## Limitations

This concerns uniform-volume product domains, affine **orthogonal** projection, real bounded inputs, and exact endpoint norms. It does not give sharp constants for projections onto higher polynomial degrees, nonproduct measures, general smooth cylinders, or arbitrary optimal projections. The method is algebraic and analytic; computational comparisons have finite scope. Equivalence with older unlocated product-domain approximation results remains a scientific priority risk. Independent review has not been performed.

## References

1. J. Wade, *A Discretized Fourier Orthogonal Expansion in Orthogonal Polynomials on a Cylinder*, arXiv:0906.2408, originally submitted 12 June 2009. https://arxiv.org/pdf/0906.2408
2. H. Li and Y. Xu, *Spectral Approximation on the Unit Ball*, arXiv:1310.2283, originally submitted 8 October 2013. https://arxiv.org/pdf/1310.2283

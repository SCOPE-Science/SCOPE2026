# Mixed diffuse–Boolean ANOVA projection norms and a sharp square-root crossover

## Finding

There is an exact formula for the endpoint amplification of *cumulative* functional-ANOVA truncation when some independent inputs are nonatomic and the others are fair binary variables. It also has a three-regime asymptotic: the transition between Boolean and diffuse-coordinate domination occurs when the number of diffuse variables is of order the square root of the number of binary variables.

Let \(m,n\geq0\), \(d=m+n\geq1\), and \(0\leq k<d\). For \(Z_1,\ldots,Z_n\) independent fair signs, put \(e_0(Z)=1\) and let \(e_\ell(Z)\) denote the elementary symmetric polynomial of degree \(\ell\) (zero outside \(0\leq\ell\leq n\)). Define
\[
 A_{m,n,k,j}(Z)=\sum_{h=0}^{k-j}(-1)^h\binom{m-j}{h}\sum_{\ell=0}^{k-j-h}e_\ell(Z),\quad 0\leq j\leq\min(m,k),
\]
with out-of-range binomial coefficients interpreted as zero. The exact sharp endpoint norms of the cumulative order-\(k\) ANOVA projector \(Q_{m,n,k}\) are
\[
 \boxed{\|Q_{m,n,k}\|_{L^1\to L^1}=\|Q_{m,n,k}\|_{L^\infty\to L^\infty}=C_{m,n,k}:=\sum_{j=0}^{\min(m,k)}\binom mj\,\mathbb E|A_{m,n,k,j}(Z)|.}
\]

For fixed \(k\geq1\), suppose \(n\to\infty\) and \(m=m_n\) satisfies \(m/\sqrt n\to\lambda\in[0,\infty)\). With \(G\) standard normal and \(\operatorname{He}_r\) the probabilists' Hermite polynomial,
\[
 \boxed{\lim_{n\to\infty}n^{-k/2}C_{m,n,k}=F_k(\lambda):=\sum_{j=0}^{k}\frac{\lambda^j}{j!(k-j)!}\,\mathbb E\big|\operatorname{He}_{k-j}(G-\lambda)\big|.}
\]
The formula includes the Boolean endpoint \(F_k(0)=\mathbb E|\operatorname{He}_k(G)|/k!\). Its high-\(\lambda\) profile satisfies \(F_k(\lambda)\sim 2^k\lambda^k/k!\). In the genuinely diffuse-dominated regime \(m\to\infty\), \(n/m^2\to0\), the corresponding *joint* asymptotic is
\[
 \boxed{\lim C_{m,n,k}/m^k=2^k/k!.}
\]
These three conclusions identify the sharp threshold at \(m\asymp\sqrt n\), not just separate growth estimates.

For the natural first-order truncation, the finite formula simplifies to
\[
 C_{m,n,1}=m+\mathbb E\left|1-m+\sum_{i=1}^n Z_i\right|.
\]
For quadratic truncation, the crossover is explicitly
\[
 F_2(\lambda)=\tfrac12\mathbb E|(G-\lambda)^2-1|+\lambda\mathbb E|G-\lambda|+\tfrac12\lambda^2,
\]
so \(F_2(0)=\sqrt{2/(\pi e)}\) and \(F_2(\lambda)\sim2\lambda^2\).

## Assumptions and scope

The probability space is \(X=[0,1]^m\times\{-1,+1\}^n\), equipped with product Lebesgue measure on its interval coordinates and independent uniform distributions on its sign coordinates. All functions are scalar real or complex functions; the endpoint operator norm has the same value for both fields. For each coordinate, \(E_i\) integrates that coordinate while leaving the others fixed. Define the mutually orthogonal ANOVA components in \(L^2(X)\) by
\[
 P_S=\prod_{i\in S}(I-E_i)\prod_{i\notin S}E_i,
 \qquad Q_{m,n,k}=\sum_{\substack{S\subseteq\{1,\ldots,d\}\\|S|\leq k}}P_S.
\]
All these operators extend boundedly to \(L^1\) and \(L^\infty\). No smoothness assumption is imposed on the input, and no convergence claim is made for growing interaction order \(k\).

## Proof

**1. Kernel generating polynomial.** Since the \(E_i\) commute, introduce the finite polynomial
\[
 \mathcal K(z)=\prod_{i=1}^d\big(E_i+z(I-E_i)\big).
\]
Its coefficient of \(z^r\) is the sum of all ANOVA components of order \(r\); hence \(Q_{m,n,k}\) is the sum of coefficients through degree \(k\).

Fix an evaluation point \(x\). For an interval coordinate, the kernel factor is the signed measure \((1-z)\,du+z\,\delta_{x_i}\). For a fair binary coordinate \(x_i\), relative to uniform measure on the binary state space, the factor is \(1+zZ_i\), where \(Z_i\) equals \(+1\) if the integration variable matches \(x_i\) and \(-1\) otherwise. These signs remain independent under the product reference measure.

**2. Singular-face decomposition and the sharp norm.** Select a subset \(T\) of the interval coordinates to use point masses and use Lebesgue measure on all remaining interval coordinates. Such face measures are mutually singular for distinct \(T\), because the interval coordinates are nonatomic. If \(|T|=j\), its coefficient polynomial is
\[
 z^j(1-z)^{m-j}\prod_{i=1}^n(1+zZ_i).
\]
Summing coefficients through \(k\), the density on that face is exactly \(A_{m,n,k,j}(Z)\). Therefore the total variation of the signed evaluation kernel is
\[
 \sum_{j=0}^{\min(m,k)}\binom mj\mathbb E|A_{m,n,k,j}(Z)|=C_{m,n,k}.
\]
This immediately proves the pointwise uniform upper bound on \(L^\infty\), hence the upper bound for its operator norm.

For the reverse inequality, choose a measurable interval event of Lebesgue probability \(\varepsilon\) independently in each of the \(m\) coordinates and restrict inputs to functions of these event indicators and the binary variables. At evaluation points where all event indicators equal one (a set of measure \(\varepsilon^m>0\)), the resulting row is the full finite Bernoulli product kernel with exceptional-state probability \(\varepsilon\). As \(\varepsilon\downarrow0\), its absolute row sum converges to the sum of the face total variations above. Indeed, a state in which exactly \(j\) of the \(m\) indicators match the exceptional state has probability of order \(\varepsilon^j\), and the corresponding kernel has leading term \(\varepsilon^{-j}A_{m,n,k,j}\) for \(j\leq k\); all \(j>k\) contributions vanish. Since there are finitely many states, the limit passes through the absolute sums. This constructs genuine positive-measure near-extremizers and proves equality without relying on values of \(L^\infty\) functions at singletons. Since every \(P_S\) is self-adjoint on \(L^2\), duality gives the identical sharp \(L^1\) norm.

**3. Square-root window.** Fix \(k\). Let \(S_n=n^{-1/2}\sum_{i=1}^nZ_i\). The central limit theorem gives \(S_n\Rightarrow G\). Newton identities for elementary symmetric polynomials show, jointly for \(0\leq r\leq k\),
\[
 n^{-r/2}e_r(Z)\ \Rightarrow\ \frac{\operatorname{He}_r(G)}{r!}.
\]
One way to check the normalization is to expand \(\prod_i(1+tZ_i/\sqrt n)\) modulo \(t^{k+1}\). Its logarithm has first two coefficients \(S_nt-t^2/2\); every higher coefficient converges to zero in probability, since the signs are bounded. If \(m/\sqrt n\to\lambda\), then for each fixed \(j\leq k\), expansion of \((1-t/\sqrt n)^{m-j}\) gives
\[
 n^{-(k-j)/2}A_{m,n,k,j}\ \Rightarrow\ \frac{\operatorname{He}_{k-j}(G-\lambda)}{(k-j)!}.
\]
The sums of terms of degree below \(k-j\) disappear at this scale. The relevant normalized elementary symmetric polynomials have uniformly bounded second moments, because \(\mathbb E e_r(Z)^2=\binom nr\); also \(\binom{m-j}h n^{-h/2}=O(1)\). Consequently the displayed random variables have uniformly bounded second moments, and their absolute first moments converge. Finally \(n^{-j/2}\binom mj\to\lambda^j/j!\), giving \(F_k(\lambda)\). This argument also includes \(m=0\), \(\lambda=0\), and any nonnegative integer interaction order held fixed.

**4. Diffuse-dominated regime.** If \(m\to\infty\) with \(n/m^2\to0\), the terms containing at least one symmetric polynomial \(e_\ell\) of positive degree are \(o_{L^1}(m^{k-j})\) in \(A_{m,n,k,j}\), since \(\|e_\ell\|_2=\sqrt{\binom n\ell}=O(n^{\ell/2})\). Its deterministic leading term is the alternating sum
\[
 \sum_{h=0}^{k-j}(-1)^h\binom{m-j}h=(-1)^{k-j}\binom{m-j-1}{k-j}
 =\frac{(-1)^{k-j}m^{k-j}}{(k-j)!}+O(m^{k-j-1}).
\]
Thus \(\mathbb E|A_{m,n,k,j}|/m^{k-j}\to1/(k-j)!\), while \(\binom mj/m^j\to1/j!\). Sum over the finitely many \(j\)'s to obtain \(2^k/k!\). Separately, \(\operatorname{He}_r(G-\lambda)/\lambda^r\to(-1)^r\) in \(L^1\), proving \(F_k(\lambda)\sim2^k\lambda^k/k!\) as \(\lambda\to\infty\).

## Verification

The standalone `check.py` computes the asserted endpoint constants from the face formula with exact rational arithmetic and compares them to a second implementation using the full finite biased-product Walsh kernel. Its finite exceptional-atom probabilities tend toward zero, supplying a separate near-extremizer check. It also checks the exact all-interval special case and the first-order closed formula. Run with `python3 check.py` using only Python's standard library. The checked script reports 440 parameter-family assertions. These computations check finite formulas and are not a substitute for the four analytical proof steps above.

## Relationship to prior work

Hegland and Pestov (arXiv:cs/9912020, first public 1999-12-30) formulate the classical orthogonal additive/ANOVA decomposition and bounds on mean-square approximation error for smooth inputs; their Theorem 3.1 gives the expansion but not this sharp endpoint norm. Griebel, Kuo and Sloan (2010) prove smoothing properties of ANOVA components for kinked or discontinuous inputs, particularly their Theorems 7 and 11, rather than the mixed-coordinate sharp norm. Ginsbourger and collaborators (arXiv:1409.6008) treat tensor projections of random-field covariance kernels, not this stability crossover.

The finite Boolean homogeneous-degree projector and general Bernoulli resampling derivative norms have related established formulas. In particular, a published rare-vertex theorem for Bernoulli resampling derivatives provides a useful comparison and can recover part of the finite discrete approximation step. It does **not** include the singular-face norm formula for the stated mixed measure or the joint \(m/\sqrt n\) Hermite-shift law and diffuse-dominated regime. The present contribution is that complete mixed-domain sharp profile, not the classical ANOVA identity nor the basic rare-vertex mechanism.

## Limitations

Only independent uniform interval coordinates and *fair* binary coordinates are treated. The crossover assumes interaction order \(k\) fixed while dimensions grow; it does not cover growing-order chaos or correlated inputs. At finite dimensions the exact operator norm may be approached rather than attained by a single global \(L^\infty\) input. Claims of complete historical priority are not made; related literature under conditional-expectation kernel or generalized ANOVA terminology could overlap. Independent review is outstanding.

## References

1. M. Hegland and V. Pestov, *Additive models in high dimensions*, arXiv:cs/9912020, first version 1999-12-30, especially Section 3.1 and Theorem 3.1. https://arxiv.org/abs/cs/9912020
2. M. Griebel, F. Y. Kuo and I. H. Sloan, *The Smoothing Effect of the ANOVA Decomposition*, 2010 preprint, especially Section 2 and Theorems 7 and 11. https://ins.uni-bonn.de/media/public/publication-media/GKS09-smoothing.pdf
3. D. Ginsbourger, O. Roustant, D. Schuhmacher, N. Durrande and N. Lenz, *On ANOVA decompositions of kernels and Gaussian random field paths*, arXiv:1409.6008, especially Sections 2–3 and the conclusion. https://arxiv.org/abs/1409.6008

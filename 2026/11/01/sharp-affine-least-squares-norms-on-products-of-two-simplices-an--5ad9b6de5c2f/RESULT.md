# Sharp affine least-squares norms on products of two simplices and the balanced-dimension law

## Finding
Let \(\Delta_d\) and \(\Delta_e\) be arbitrary nondegenerate real simplices of positive dimensions \(d,e\), and equip their Cartesian product with normalized Lebesgue measure. Let \(P_{d,e}\) be the real \(L^2\)-orthogonal projector onto all globally affine functions of the \(d+e\) ambient coordinates. The exact attained norm is
\[
\boxed{\|P_{d,e}\|_{L^\infty\to L^\infty}=1+2B_{d,e},\qquad
B_{d,e}=\mathbb E[(C-AU-BV)_+],}
\]
where \(A=(d+1)(d+2)\), \(B=(e+1)(e+2)\), \(C=d+e+3\), \(U\sim\operatorname{Beta}(1,d)\), and \(V\sim\operatorname{Beta}(1,e)\) are independent. Here \(z_+=\max\{z,0\}\). This is a finite, exactly rational invariant, computable without optimization or approximation. The maximum possible magnitude of a negative projector output from \(0\le f\le1\) is exactly \(B_{d,e}\).

For an explicit finite sum, set
\[
H_{ij}(t)=\frac{i!j!}{(i+j+3)!}(t_+)^{i+j+3},
\]
\[
\begin{aligned}
R_{ij}={}&H_{ij}(C)
-\sum_{r=0}^{i}\binom{i}{r}A^{i-r}H_{rj}(C-A)
-\sum_{s=0}^{j}\binom{j}{s}B^{j-s}H_{is}(C-B)\\
&+\sum_{r=0}^{i}\sum_{s=0}^{j}\binom{i}{r}\binom{j}{s}A^{i-r}B^{j-s}H_{rs}(C-A-B).
\end{aligned}
\]
Then
\[
\boxed{B_{d,e}=\frac{de}{AB}\sum_{i=0}^{d-1}\sum_{j=0}^{e-1}
\frac{(-1)^{i+j}\binom{d-1}{i}\binom{e-1}{j}}{A^iB^j}R_{ij}.}
\]
For example, \(\|P_{1,1}\|=233/108\), \(\|P_{1,2}\|=11/4\), and \(\|P_{2,2}\|=1027567/311040\).

If both factor dimensions diverge and \(d/(d+e)\to\theta\in(0,1)\), then
\[
\boxed{\lim\frac{\|P_{d,e}\|}{d+e}=2b(\theta),\quad
b(\theta)=\mathbb E[(1-\theta E_1-(1-\theta)E_2)_+],}
\]
where \(E_1,E_2\) are independent unit-mean exponentials. For \(\theta\ne1/2\), this is the elementary expression
\[
b(\theta)=1-\frac{\theta^2(1-e^{-1/\theta})-(1-\theta)^2(1-e^{-1/(1-\theta)})}{2\theta-1},
\qquad b(1/2)=2e^{-2}.
\]
The function \(b\) is symmetric and strictly convex on \((0,1)\). Its unique minimizer is \(\theta=1/2\), and its limiting endpoint values are \(e^{-1}\). Thus balanced dimension splitting has optimal leading norm coefficient \(4e^{-2}\), versus \(2e^{-1}\) for the unsplit simplex of the same total dimension. The leading coefficient ratio is \(2e^{-1}\).

## Assumptions and scope
Dimensions \(d,e\) are positive integers. The simplices are full-dimensional in their affine hulls; each carries uniform normalized volume. All functions are real-valued. The projector is globally affine, **not** the tensor-product projector onto bilinear or bi-affine functions. Its source and target norm is the essential-supremum norm with respect to the product volume. The exact finite formula also applies when one factor is one-dimensional. The asymptotic minimization applies to sequences with both dimensions diverging and an interior limiting ratio, not to any claim about finite-dimensional minimizing splits.

## Proof
**1. Simplex evaluation kernel.** Let \(\lambda_0,\ldots,\lambda_d\) denote barycentric coordinates on \(\Delta_d\). For uniform volume,
\[
\mathbb E[\lambda_i\lambda_j]=\frac{1+\mathbf 1_{i=j}}{(d+1)(d+2)}.
\]
Inverting the resulting Gram matrix shows that the \(L^2\)-affine projector evaluated at vertex \(i\) has representing kernel
\[
K_d(i,y)=(d+1)(d+2)\lambda_i(y)-(d+1).
\]
Here \(\lambda_i(y)\sim\operatorname{Beta}(1,d)\). The barycentric Gram inverse follows from \((I+\mathbf1\mathbf1^T)^{-1}=I-\mathbf1\mathbf1^T/(d+2)\). In a product, the affine space is the orthogonal sum of constants, centered affine functions on the first factor, and centered affine functions on the second factor. Therefore its projector kernel at a product vertex is
\[
K((i,j),(y,z))=K_d(i,y)+K_e(j,z)-1=AU+BV-C.
\]
This kernel integrates to one. No tensor-product bilinear interactions are included.

**2. Why vertex rows give the operator norm and extremizers.** For every fixed integration point, the affine evaluation kernel depends affinely on the evaluation point. Hence the function of the evaluation point obtained by integrating its absolute value is convex. A convex function on the product polytope attains its maximum at some vertex; affine simplex automorphisms permuting vertices preserve normalized volume, so all vertex rows have the same integral. The projector is represented by a continuous polynomial output, and its essential supremum equals the maximum of its values on the closed product polytope. Taking \(f\) to be the sign of a maximizing vertex kernel attains that maximal output; neighborhoods near the vertex give the same essential-supremum lower bound. Because \(\int K=1\), \(\int|K|=1+2\int(-K)_+\). With \(0\le f\le1\), the minimum value at any chosen point is obtained by \(f=\mathbf1_{\{K<0\}}\); vertex maximization yields the universal sharp negative defect \(B_{d,e}\).

**3. Exact finite sum.** The independent scaled barycentric coordinates \(X=AU\), \(Y=BV\) have densities \(\frac dA(1-x/A)^{d-1}\) on \([0,A]\) and \(\frac eB(1-y/B)^{e-1}\) on \([0,B]\). Expand both density polynomials. For monomials \(x^iy^j\), the untruncated positive-quadrant hinge integral is
\[
\int_{x,y\ge0}x^iy^j(t-x-y)_+\,dx\,dy=H_{ij}(t).
\]
Remove \(x>A\) and \(y>B\) using inclusion-exclusion. After translating \(x\mapsto x+A\) and \(y\mapsto y+B\), the binomial theorem produces exactly the displayed four-term \(R_{ij}\). Summing the density coefficients yields the stated finite rational formula, including cases where \(C\) exceeds either side length.

**4. Asymptotic coefficient.** For \(U\sim\operatorname{Beta}(1,d)\), the tail of \(dU\) is \((1-t/d)^d\) on \([0,d]\), which converges to \(e^{-t}\). Similarly \(eV\) converges to an independent unit exponential. If \(d/(d+e)\to\theta\in(0,1)\), then \((AU+BV)/(d+e)\) converges in distribution to \(\theta E_1+(1-\theta)E_2\). The scaled hinge is bounded between zero and \(C/(d+e)\to1\), so bounded-continuous convergence yields the limit of \(B_{d,e}/(d+e)\). Integration of the two-exponential convolution gives the displayed elementary formula; at \(\theta=1/2\), the sum is gamma with shape two and scale one half, giving \(b(1/2)=2e^{-2}\).

For every fixed \(E_1,E_2\), the hinge \((1-\theta E_1-(1-\theta)E_2)_+\) is convex in \(\theta\). The expectation is symmetric under exchanging the independent exponentials. It is strictly convex because, for any two distinct parameter values, there is a positive-probability open set of pairs \((E_1,E_2)\) for which the affine interpolation crosses the hinge at one of those parameter values; Jensen's convexity is then strict. Symmetry and strict convexity imply the unique minimum at one half. At either endpoint the hinge reduces to \((1-E_1)_+\), with expectation \(e^{-1}\). Finally, for a single \((d+e)\)-simplex the same one-factor kernel shows that the leading projector norm is \(2(d+e)e^{-1}+o(d+e)\), yielding the stated ratio.

## Verification
A standalone exact-arithmetic checker is supplied as `verify.py`. It evaluates the finite inclusion-exclusion sum with rational numbers and compares it with an independently integrated one-dimensional conditional-hinge formula for every pair of dimensions from one through seven. It verifies symmetry, the displayed small-dimensional rational values, projection-kernel identities in the square case, and sampled barycentric kernels. It also checks the balanced asymptotic prediction by independent numerical integration at three larger dimensions. Finite numerical tests are corroboration only; Steps 1–4 provide the proof for all dimensions.

## Relationship to prior work
Hangelbroek, Narcowich, Sun and Ward (arXiv:1005.2424, first posted 2010-05-13) establish stability for certain kernel-based least-squares projectors on manifolds. Their Theorem 5.1 gives a uniform \(L^p\) bound under localization hypotheses, not the exact affine-projector constants on simplex products. A separately recorded exact norm for one simplex yields a natural comparison baseline but does not imply the two-factor convolution or its balanced asymptotic minimizer. Chernov's polynomial \(L^2\)-projection work on one simplex develops Sobolev trace-error estimates; its accessible abstract does not resolve the present sharp \(L^\infty\) product-domain problem. No general assertion of unpublished or complete-literature uniqueness is made.

## Limitations
Only uniform normalized volume and globally affine orthogonal projection on exactly two simplex factors are considered. No finite-dimension optimality among all product decompositions or other convex-body shapes is asserted. The all-dimensional claims are analytical; sampled and finite exact calculations do not establish them independently. An equivalent result in an older or inaccessible product-domain projector treatment remains a possible literature risk. Independent external verification has not been performed.

## References
- T. Hangelbroek, F. J. Narcowich, X. Sun and J. D. Ward, *Kernel Approximation on Manifolds II: The \(L^\infty\)-norm of the \(L^2\)-projector*, arXiv:1005.2424 (first public version 2010-05-13), DOI: 10.1137/100795334. Full-text sections 1, 4–5 and the main norm theorem were consulted.
- A. Chernov, *Optimal convergence estimates for the trace of the polynomial \(L^2\)-projection operator on a simplex*, *Mathematics of Computation* 81 (2012), 765–787, DOI: 10.1090/S0025-5718-2011-02513-5. Only publicly accessible summary and introductory material could be checked.
- *Exact positivity defect and max norm of the affine least-squares projector on a simplex*, public mathematical research result (2026). The accessible statement is for one simplex, rather than a Cartesian product of two simplices.

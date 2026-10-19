# A sharp positivity boundary for three-node Gaussian kernel quadrature and its tensor instability

## Finding
For the exact Gaussian-kernel quadrature rule on the three symmetric nodes \((-a,0,a)\) under \(N(0,1)\), the center weight has one and only one sign transition as the node distance increases. Its exact transition is expressed by the unique positive solution of
\[
\frac{2\log\cosh y}{y}=\frac1{1+\ell^2},\qquad a_*(\ell)=\ell\sqrt y.
\]
The outer weights are always positive. Thus the center weight is negative for \(0<a<a_*\), zero at \(a=a_*\), and positive for \(a>a_*\). The natural scaled three-node Gauss–Hermite grid always lies strictly on the positive side, for *every* kernel length scale. In contrast, tight symmetric three-node grids yield signed rules whose normalized tensor products have exponentially growing worst-case data amplification.

## Assumptions and scope
Let \(\ell>0\), let \(\mu=N(0,1)\), and let
\[
k_\ell(x,y)=\exp\!\left(-\frac{(x-y)^2}{2\ell^2}\right).
\]
For \(a>0\) use nodes \((-a,0,a)\). *Exact kernel quadrature* means the unique weights \((w,v,w)\) solve the Gram-system \(K(w,v,w)^{\mathsf T}=k_\mu\), where \(K_{ij}=k_\ell(x_i,x_j)\) and \((k_\mu)_i=\int k_\ell(x_i,t)\,d\mu(t)\). This is not the truncated-Mercer approximate-weight construction in [1]. Distinct Gaussian translates give strictly positive definite \(K\), so the solution is unique.

Define the elementary quantities
\[
c=\frac{\ell}{\sqrt{1+\ell^2}},\quad t=e^{-a^2/(2\ell^2)},\quad u=e^{-a^2/(2(1+\ell^2))},\quad y=\frac{a^2}{\ell^2}.
\]
Then the weights and their sum are exactly
\[
w=\frac{c(u-t)}{(1-t^2)^2},\qquad
v=\frac{c(1+t^4-2tu)}{(1-t^2)^2},\qquad
S=2w+v=c+2(1-t)w>0.
\]
Define \(h(y)=2\log\cosh(y)/y\) for \(y>0\) and let \(y_\ell\) be its unique solution of \(h(y_\ell)=1/(1+\ell^2)\). Put \(a_*=\ell\sqrt{y_\ell}\). For a fixed standard-Gaussian *target measure*, also consider the auxiliary node-scale family
\[
a(\alpha,\ell)^2=\frac3{2\alpha\sqrt{\alpha^2+2/\ell^2}}\quad(\alpha>0).
\]
Here \(\alpha\) changes **only the nodes**, not the target measure. The natural value \(\alpha=1/\sqrt2\) gives \(a_{GH}^2=3/\sqrt{1+4/\ell^2}\), the three-node prescription from [1]. The following statements concern all \(a,\ell>0\), and tensor powers of the same rule in every integer dimension \(d\ge1\).

## Proof
**1. Kernel weights.** Standard Gaussian convolution yields the kernel-mean vector \((cu,c,cu)\); the Gram matrix is
\[
K=\begin{pmatrix}1&t&t^4\\ t&1&t\\t^4&t&1\end{pmatrix}.
\]
The symmetry-reduced linear system is \((1+t^4)w+tv=cu\), \(2tw+v=c\). Eliminating \(v\) gives \((1-t^2)^2w=c(u-t)\), hence the displayed formulas. Since \(a>0\) and \(1+\ell^2>\ell^2\), one has \(u>t\), so \(w>0\) and \(S>0\).

**2. Complete sign classification.** Because \(u/t=\exp(y/[2(1+\ell^2)])\) and \((1+t^4)/(2t)=t\cosh y\),
\[
\operatorname{sgn}v=\operatorname{sgn}\left(\log\cosh y-\frac{y}{2(1+\ell^2)}\right).
\]
Differentiating \(y\tanh y-\log\cosh y\) gives \(y\operatorname{sech}^2y>0\), and this expression vanishes at zero. Therefore \(h'(y)>0\). Moreover \(h(0+)=0\) and \(h(\infty)=2\). Since \(0<1/(1+\ell^2)<1\), there is exactly one crossing \(y_\ell\); all sign and equality assertions follow.

**3. Location and asymptotic behavior of the frontier.** For every \(y>0\), \(\tanh y>y/(1+y)\): in terms of exponentials it is exactly the true inequality \(e^{2y}>1+2y\). Integration yields \(\log\cosh y>y-\log(1+y)>y^2/[2(1+y)]\), where the second inequality follows by differentiation and equality at zero. Thus \(h(y)>y/(1+y)\). With \(y=\ell^{-2}\) this exceeds \(1/(1+\ell^2)\), proving \(0<a_*<1\). As \(\ell\to\infty\), \(h(y)=y+O(y^3)\) near zero, so \(y_\ell\sim\ell^{-2}\) and \(a_*\to1\). As \(\ell\to0\), the right side tends to 1 and \(y_\ell\to y_0\), uniquely defined by \(\cosh y_0=e^{y_0/2}\). With \(\tau=e^{y_0/2}>1\), the latter is equivalent to \((\tau-1)(\tau^3-\tau^2-\tau-1)=0\), so \(a_*/\ell\to\sqrt{2\log\tau}\).

**4. Positivity at the natural scaled Gauss–Hermite nodes.** Put \(z=\ell^2\). If \(z\ge1/2\), then \(a_{GH}^2=3/\sqrt{1+4/z}\ge1>a_*^2\). If \(0<z\le1/2\), then \(a_{GH}^2=3\sqrt z/\sqrt{z+4}\ge2z\), since \(9\ge4z(z+4)\) on this range. Also \(h(2)=\log\cosh2>1\), whence \(y_\ell<2\) and \(a_*^2=zy_\ell<2z\). Thus \(a_{GH}>a_*\) in every case, and all three exact kernel weights are strictly positive. For general \(\alpha>0\), the function \(a(\alpha,\ell)\) is strictly decreasing from infinity to zero. Solving \(a(\alpha_*,\ell)=a_*\) for \(\alpha_*^2\) gives
\[
\alpha_*^2=-\ell^{-2}+\sqrt{\ell^{-4}+\frac9{4a_*^4}}.
\]
Therefore the exact center weight is positive for \(\alpha<\alpha_*\), zero at equality, and negative for \(\alpha>\alpha_*\), while \(\alpha_*>1/\sqrt2\).

**5. Sharp normalized tensor amplification.** The one-dimensional weight sum is \(S=2w+v>0\) and absolute-weight sum is \(W=2w+|v|\). The \(d\)-dimensional tensor product of the Gaussian kernels and measures has Gram matrix and kernel-mean vector equal to tensor products of the one-dimensional ones, so its *unnormalized* exact kernel-quadrature weight array is the tensor power of \((w,v,w)\). Its sum is \(S^d\), generally not one. Divide all weights by \(S^d\) **only to obtain a constant-reproducing signed rule**; this normalized rule is no longer exact on the original kernel translates. Its operator norm on the space of arbitrary bounded nodal data, with supremum norm, is exactly
\[
\Lambda_d=\frac{W^d}{S^d}=\left(\frac{2w+|v|}{2w+v}\right)^d.
\]
The upper bound follows by the triangle inequality; equality is attained by choosing data values equal to the signs of the tensor weights. If \(a\ge a_*\), all weights are nonnegative and \(\Lambda_d=1\). If \(a<a_*\), then \(v<0\) and \(W>S\), so \(\Lambda_d>1\) and increases exponentially with \(d\).

For the coalescing-node limit at fixed \(\ell\), Taylor expansion of the *explicit exact formulas*, not of an ill-conditioned computed inverse, gives
\[
w=\frac{c^3}{2a^2}+O_\ell(1),\qquad v=-\frac{c^3}{a^2}+O_\ell(1),\qquad S\to c+\frac{c^3}{2\ell^2}>0.
\]
Therefore
\[
\frac{W}{S}\sim\frac{4\ell^2}{(2\ell^2+3)a^2}\qquad (a\downarrow0).
\]
The one-node center rule has a positive weight, and a two-node symmetric rule has both equal positive weights \(cu/(1+t^4)\); thus three nodes are the first symmetric case exhibiting signed weights.

## Verification
The independent-of-third-party-packages script `verify.py` runs 441 deterministic high-precision checks of the closed formulas, equations \(Kw=k_\mu\), sign reversals, natural scaling, the auxiliary \(\alpha\)-threshold, tensor-norm identities, and coalescence. Run `python3 verify.py` in a directory containing this result and the script. Representative illustrative (not proof-level) values: for \(\ell=1\), \(a_*=0.7225858840638799\ldots\); at \(a=0.1\), the normalized one-dimensional data-amplification base is about \(79.44\), so its \(d\)-dimensional counterpart is approximately \((79.44)^d\). Universal conclusions follow from the exact algebra, monotonicity, and inequalities above; no finite computation certifies the all-parameter claims.

## Relationship to prior work
Karvonen and Särkkä [1] introduce the natural scaled Gauss–Hermite nodes, compute approximations from a truncated Mercer expansion, and report *numerical evidence* of positivity for both approximate and exact weights. The present theorem proves **exact-kernel-weight positivity for precisely three natural nodes**, not positivity of their approximate Mercer weights or an all-node theorem. Karvonen, Kanagawa, and Särkkä [2] establish general sufficient positivity conditions for variance-optimal nodes and investigate quadrature-weight magnitudes, but those results do not determine this fixed-grid sharp sign frontier. Karvonen and Särkkä [3] establish convergence to polynomial-based approximation in the flat-kernel limit, which explains a limiting regime but does not directly supply the complete finite-length-scale threshold. Tensor-product factorization and its basic \(\ell^1\)-multiplicativity are established background from [1,2]; the new quantitative component is the identified sharp sign boundary and the corresponding explicit normalized amplification base. No mathematical uniqueness or independent publication-priority certification is inferred from database search alone.

## Limitations
The analysis is for a standard one-dimensional Gaussian integration measure, one Gaussian-kernel length scale, **exactly three symmetric nodes**, and tensor powers of that rule. The auxiliary \(\alpha\) varies only the node locations while keeping the target measure fixed; changing the integration measure with \(\alpha\) is a different problem. The normalized tensor rule is not exact on kernel translates, while the original tensor rule need not reproduce constants. The sharp \(\ell^\infty\) stability factor is for unrestricted bounded nodal data, not an RKHS worst-case integration error. No numerical conditioning guarantee is asserted for solving nearly singular Gram systems. No positivity claim is made for four or more nodes or for the approximate Mercer quadrature weights.

## References
[1] T. Karvonen and S. Särkkä, *Gaussian kernel quadrature at scaled Gauss–Hermite nodes*, arXiv:1803.09532 (first public 2018-03-26), https://arxiv.org/abs/1803.09532.

[2] T. Karvonen, M. Kanagawa, and S. Särkkä, *On the positivity and magnitudes of Bayesian quadrature weights*, arXiv:1812.08509 (first public 2018-12-20), https://arxiv.org/abs/1812.08509.

[3] T. Karvonen and S. Särkkä, *Worst-case optimal approximation with increasingly flat Gaussian kernels*, arXiv:1906.02096 (first public 2019-06-05), https://arxiv.org/abs/1906.02096.

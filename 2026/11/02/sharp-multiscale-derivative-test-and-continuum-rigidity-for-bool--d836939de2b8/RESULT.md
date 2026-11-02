# Sharp multiscale derivative test and continuum rigidity for Boolean-angle quadrature encodings

## Finding
Fix an integer \(d\ge0\), put \(q=d+1\), and let \(g:[0,1]\to[0,1]\) have the continuously \(q\)-times differentiable angle \(\theta(x)=2\arcsin\sqrt{g(x)}\), with values in \([0,\pi]\). For each integer \(n\ge q\), sample the dyadic grid \(\mathcal X_n=\{k2^{-n}:0\le k<2^n\}\). Its angle table is viewed as a function of the \(n\) binary digits of \(k\), and \(\mathcal G_n^{(d)}\) denotes the class of angle tables with Boolean multilinear degree at most \(d\), as in [1].

Set \(L_n=2^{n-q}\) and define the signed low-bit interaction on coarse block \(m\) by
\[
D_{n,m}(\theta)=\sum_{k=0}^{2^q-1}(-1)^{q-\operatorname{popcount}(k)}\theta\!\left(\frac{2^q m+k}{2^n}\right),\qquad 0\le m<L_n.
\]
Let \(R_n(\theta)=\max_{0\le m<L_n}|D_{n,m}(\theta)|\). Then the exact sharp derivative-recovery law is
\[
\boxed{\lim_{n\to\infty}2^{qn-q(q-1)/2}R_n(\theta)=\|\theta^{(q)}\|_{L^\infty([0,1])}.}
\]
More precisely, with \(\omega_{\theta^{(q)}}\) the ordinary modulus of continuity,
\[
\left|2^{qn-q(q-1)/2}R_n(\theta)-\|\theta^{(q)}\|_\infty\right|\le 2\omega_{\theta^{(q)}}(2^{q-n}).
\]
It follows that \(g|_{\mathcal X_n}\in\mathcal G_n^{(d)}\) for every sufficiently large \(n\) **if and only if** \(\theta\) is a real polynomial of degree at most \(d\). Thus the smooth, uniformly low-degree continuum class consists exactly of \(g(x)=\sin^2(P(x)/2)\) with \(P\) a degree-at-most-\(d\) polynomial mapping \([0,1]\) into \([0,\pi]\).

There is a quantitative robustness counterpart. If either \(\theta^{(q)}\ge m_0>0\) everywhere or \(\theta^{(q)}\le-m_0<0\) everywhere, then for every \(n\ge q\), every Boolean multilinear polynomial \(B_n\) of degree at most \(d\) satisfies
\[
\boxed{\max_{b\in\{0,1\}^n}|\theta(i(b)/2^n)-B_n(b)|\ge m_0\,2^{-q(q+1)/2-q},}\quad i(b)=\sum_{j=0}^{n-1}2^jb_j.
\]
This lower bound is uniform in grid refinement. For example, when \(\theta(x)=\theta_0+\alpha e^{cx}\), with \(\alpha,c>0\) and \(0\le\theta_0+\alpha e^{cx}\le\pi\) on \([0,1]\), every nonempty Boolean monomial coefficient is exactly
\[
\alpha\prod_{j\in S}(e^{c2^{j-n}}-1)\ne0.
\]
Hence its angle table has full Boolean degree \(n\) and all \(2^n\) monomial coefficients nonzero for every \(n\ge1\); specifically on the face of the \(q\) most significant bits the optimal \(L^\infty\) degree-\(d\) approximation error equals
\[
\frac{\alpha}{2^q}\prod_{j=1}^q(e^{c2^{-j}}-1)>0.
\]
The last equality concerns that face, and is a lower bound—not necessarily the optimum—on the entire \(n\)-bit table. The \(2^n\) count concerns the explicit monomial-rotation factorization in [1], not a lower bound for every possible quantum circuit representation.

## Assumptions and scope
The integers \(d\) and \(q=d+1\) are fixed as \(n\to\infty\). All sampling is exact on the left-endpoint dyadic grids from [1], with \(g\) fixed across resolutions. The smoothness assumption is on the *angle* \(\theta\), not merely on \(g\). Angles use the principal branch \(2\arcsin\sqrt{g}\in[0,\pi]\); no arbitrary-angle branch changes are permitted. For the approximation lower bound, comparison polynomials \(B_n\) may have arbitrary real coefficients and need not be valid rotation angles; the result is therefore also a lower bound on the smaller class of angle-valid approximants.

## Proof
**1. Coarse-cell mixed differences.** For \(n\ge q\), write \(x_m=m2^{q-n}\) and \(h_j=2^{j-n}\) for \(0\le j<q\). The sampled nodes in \(D_{n,m}\) are \(x_m+\sum_{j\in S}h_j\), as \(S\) ranges over subsets of \(\{0,\ldots,q-1\}\). Therefore repeated application of the fundamental theorem of calculus gives the exact identity
\[
D_{n,m}(\theta)=\int_0^{h_0}\!\cdots\!\int_0^{h_{q-1}}\theta^{(q)}(x_m+t_0+\cdots+t_{q-1})\,dt_{q-1}\cdots dt_0.
\]
The normalization is \(\prod_{j=0}^{q-1}h_j=2^{q(q-1)/2-qn}\). Every integration point is within \(2^{q-n}\) of \(x_m\). Thus the normalized difference is within \(\omega_{\theta^{(q)}}(2^{q-n})\) of \(\theta^{(q)}(x_m)\). The coarse block bases \(x_m\), spaced by \(2^{q-n}\), approach every point of \([0,1]\) within this same distance, including the final endpoint. Maximizing absolute values and applying the modulus bound twice proves both the explicit error estimate and the limit.

**2. Complete smooth all-resolution classification.** If the table is of Boolean degree at most \(d=q-1\), then after fixing its \(n-q\) higher digits the restriction to the \(q\) low digits still has degree at most \(q-1\), so its alternating \(q\)-fold difference \(D_{n,m}\) vanishes. If this holds for every sufficiently large \(n\), the limit from Step 1 forces \(\theta^{(q)}\equiv0\), hence \(\theta\) is a polynomial of degree at most \(d\). Conversely, if \(\theta=P\) is such a polynomial, substitute \(x=2^{-n}\sum_j2^jb_j\) into \(P(x)\): after using \(b_j^k=b_j\) for Boolean digits, every monomial has at most \(d\) distinct bit variables. Thus every sampled table lies in \(\mathcal G_n^{(d)}\). The inverse angle map in [1] gives \(g=\sin^2(P/2)\).

**3. Sharp order-independent approximation obstruction.** Fix the \(n-q\) lower-significance bits to zero and vary only the \(q\) most significant bits. The corresponding spatial increments are \(2^{-1},\ldots,2^{-q}\). The same integral identity shows that the alternating \(q\)-fold difference of \(\theta\) across this face has modulus at least \(m_0\,2^{-q(q+1)/2}\). Every Boolean polynomial of degree at most \(q-1\) has vanishing such difference. If its uniform approximation error is \(\varepsilon\), the triangle inequality over the \(2^q\) vertices bounds the difference of the errors by \(2^q\varepsilon\). This proves the claimed lower bound, independently of \(n\).

**4. Exact analytic witness and face optimum.** The Boolean identity \(e^{c2^{j-n}b_j}=1+(e^{c2^{j-n}}-1)b_j\) factorizes \(e^{cx}\) and yields every stated nonzero coefficient. On the leading \(q\)-bit face, its highest coefficient is \(a=\alpha\prod_{j=1}^{q}(e^{c2^{-j}}-1)\). The preceding difference argument gives the minimax lower bound \(|a|/2^q\). It is attained on that face: subtract the sign pattern \((a/2^q)(-1)^{q-\sum b_j}\) from the tabulated values; the correction has degree \(q\) with highest coefficient \(a\), so the remainder is a Boolean polynomial of degree at most \(q-1\), while the residual has constant modulus \(|a|/2^q\). This establishes the exact face optimum.

## Verification
The self-contained script `verify_angle.py` performs exact rational checks of the normalization and zero-interaction identity for polynomial examples through order six, computes Boolean Möbius coefficients of polynomial tables, and checks the analytic exponential coefficient factorization and leading-bit obstruction. Its current deterministic replay prints `PASS: 2644 total checks after leading-bit and angular-range tests`. The proof above, not finite tests, establishes every quantified theorem. To reproduce, run `python verify_angle.py` using Python 3.9 or newer; no third-party packages are required.

## Relationship to prior work
Chinesta, Falcó and Falcó-Pomares [1] introduce \(\mathcal G_n^{(d)}\), its degree test, and a direct controlled-rotation factorization **at a fixed discrete resolution**, as well as examples whose low-degree angle tables are constructed for a specified grid. Those results provide the definitions and the fixed-grid degree property, but do not state a smooth all-resolution classification, derivative recovery constant, or uniform low-degree approximation obstruction. Classical Boolean expansions [2] and numerical finite differences [3] furnish the underlying separate ingredients. The combination here concerns the compatibility of the same continuous quadrature integrand across arbitrarily fine dyadic grids; this multiscale quantifier is essential.

## Limitations
The classification assumes \(\theta\in C^{d+1}([0,1])\). Without this regularity, continuous nonpolynomial examples can have bounded Boolean degree across grids; e.g. a dyadic hinge is piecewise affine and can have degree two. The numerical limit is for exact arithmetic and fixed \(d\), not for growing degree or floating-point coefficient estimation. The lower approximation barrier requires a uniform one-sign derivative bound. Neither the monomial count nor the angle-degree barrier is a lower bound on all possible quantum oracle circuits, some of which may exploit other algebraic encodings.

## References
[1] F. Chinesta, A. Falcó, D. Falcó-Pomares, *On the complexity of quantum numerical integration: an angle-structure characterization*, arXiv:2604.24289, first publicly submitted 2026-04-27. https://arxiv.org/abs/2604.24289 . Specifically Sections C.1–C.3, D.1–D.4, and F.2.

[2] R. O'Donnell, *Analysis of Boolean Functions*, Cambridge University Press, 2014, Chapter 1. https://doi.org/10.1017/CBO9781139814782 .

[3] B. Fornberg, *Generation of finite difference formulas on arbitrarily spaced grids*, Mathematics of Computation 51 (1988), 699–706. https://doi.org/10.1090/S0025-5718-1988-0935077-0 .

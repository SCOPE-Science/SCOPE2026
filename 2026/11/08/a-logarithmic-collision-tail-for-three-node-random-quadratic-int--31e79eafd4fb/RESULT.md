# A logarithmic collision tail for three-node random quadratic interpolation

## Finding
Let three nodes be sampled independently and uniformly from \([0,1]\). For any fixed evaluation point \(z\in[0,1]\), let \(L_j(z)\) denote the degree-two Lagrange evaluation weights and put \(W(z)=(\sum_{j=1}^3 L_j(z)^2)^{1/2}\). Then
\[
\lim_{T\to\infty}\frac{T}{\log T}\,\Pr\{W(z)>T\}=6\sqrt2\int_0^1(z-u)^2\,du=6\sqrt2\left(z^2-z+\frac13\right)>0.
\]
Consequently \(\mathbb E W(z)^p<\infty\) holds exactly for \(0<p<1\). For independent centered Gaussian errors of variance \(\sigma^2>0\) at the three nodes, the interpolation error for the zero function has a finite absolute \(p\)-moment exactly when \(0<p<1\); in particular, even its mean absolute error diverges. At \(z=1/2\), the exact leading constant is \(1/\sqrt2\).

## Assumptions and scope
The sampling law is exactly three independent \(U[0,1]\) nodes, without spacing constraints, almost surely distinct. The interpolating polynomial has degree at most two, evaluation is at one deterministic \(z\in[0,1]\), and all operations use exact real arithmetic. Lagrange weights are ordinary polynomial interpolation weights, not regularized or barycentrically safeguarded weights. No result is claimed for other node laws or numbers of nodes.

## Proof
Order the nodes as \(a=u<b=u+s<c=u+s+t\). The joint density in \((u,s,t)\) is \(6\) on \(u,s,t>0\) with \(u+s+t<1\). Direct Lagrange evaluation gives
\[
L_a=\frac{(z-u-s)(z-u-s-t)}{s(s+t)},\qquad
L_b=-\frac{(z-u)(z-u-s-t)}{st},\qquad
L_c=\frac{(z-u)(z-u-s)}{t(s+t)}.
\]
Since all numerators are at most one in absolute value, \(W\le\sqrt3/(st)\). Fix a small \(\eta>0\). If either gap is at least \(\eta\), the portion of \(\Pr(W>T)\) is \(O_\eta(T^{-1})\). If both gaps are less than \(\eta\), but \(\eta\le s/t\le\eta^{-1}\), the bound \(st<\sqrt3/T\) confines the two-gap area to \(O_\eta(T^{-1})\). Hence only the two strongly unbalanced collision regions can contribute on the scale \((\log T)/T\).

In the region \(0<s<\eta t\) and \(0<t<\eta\), take \(u\) away from the endpoints and from \(z\) by a fixed distance \(\rho>0\). Uniformly as \(\eta\downarrow0\),
\[
W=\frac{\sqrt2(z-u)^2}{st}(1+o_{\rho}(1)),
\]
where the relative error is bounded by a quantity tending to zero with \(\eta\), uniformly over this region. For a positive constant \(C\), the elementary area identity
\[
\int_0^\eta\min\left\{\eta t,\frac{C}{Tt}\right\}\,dt
=\frac{C}{2T}\log T+O_{\eta,C}(T^{-1})
\]
holds as \(T\to\infty\). It follows by first integrating over \(s\) that the contribution from this one unbalanced region is asymptotic, on the \((\log T)/T\) scale, to \(3\sqrt2\int(z-u)^2du\), with \(u\) in the restricted interior range. The second region \(0<t<\eta s\) contributes the same constant, by exchanging the two gaps.

To remove the restrictions on \(u\), note that the global bound \(W\le\sqrt3/(st)\) and the same product-area integral bound the logarithmically rescaled contribution of any \(u\)-set of Lebesgue measure \(\lambda\) by \(O(\lambda)\). Thus the regions within distance \(\rho\) of \(0,1,z\) contribute at most \(O(\rho)\). The constraint \(u+s+t<1\) changes the one-gap integral only in a boundary interval of length at most \(s+t\), which gives no leading logarithmic contribution. First let \(T\to\infty\), next \(\eta\downarrow0\), then \(\rho\downarrow0\). The two collision contributions add to \(6\sqrt2\int_0^1(z-u)^2du\), proving the displayed limit. Positivity follows from \(\int_0^1(z-u)^2du=z^2-z+1/3\ge1/12\).

The layer-cake identity \(\mathbb E W^p=p\int_0^\infty T^{p-1}\Pr(W>T)dT\) yields the sharp cutoff at \(p=1\), including divergence at equality because the tail is asymptotic to a positive constant times \((\log T)/T\). For independent Gaussian observation noise, conditional on the nodes the interpolation error has law \(\sigma W Z\), where \(Z\) is a standard Gaussian independent of the nodes in a coupling. Therefore all absolute moments factor into \(\sigma^p\mathbb E|Z|^p\mathbb EW^p\), proving the final assertion.

## Verification
The accompanying standalone `checker.py` verifies the polynomial reproduction identities for degrees zero, one and two, both single-gap residue formulas, and the midpoint constant exactly using symbolic rational expressions. An independent event-weighted importance-sampling diagnostic uses a log-uniform proposal for each positive gap and reports finite-threshold ratios for two evaluation points. Those samples are diagnostic only; the infinite-tail theorem follows from the analytic area argument above. Run `python checker.py` with Python, SymPy and NumPy installed.

## Relationship to prior work
Kunis and Nagel (arXiv:1812.08645, public 2018-12-20) analyze deterministic conditioning for Fourier Vandermonde matrices with well-separated pairs of near-colliding nodes, not iid quadratic Lagrange evaluations or a logarithmically amplified tail. Chkifa and Dolbeault (arXiv:2306.07435, public 2023-06-12) study stabilized sampling for approximation and interpolation in general spaces rather than this unsafeguarded iid three-node tail. Standard Lagrange interpolation formulas can be found in NIST DLMF Section 3.3. This calculation isolates the simultaneous near-collision scales that distinguish iid sampling from one-per-stratum node sampling.

## Limitations
The limit is for fixed degree two and a fixed deterministic evaluation point. The result neither treats regularized interpolation nor asserts accuracy of interpolating smooth noiseless data. The convergence of the displayed asymptotic may be slow because of logarithmic corrections. Independent literature precedence review has not been performed; equivalent singular-integral tail calculations may exist under another terminology.

## References
- S. Kunis and D. Nagel, “On the condition number of Vandermonde matrices with pairs of nearly-colliding nodes,” arXiv:1812.08645 (first submitted 2018-12-20), https://arxiv.org/abs/1812.08645.
- M. Dolbeault and M. A. Chkifa, “Randomized least-squares with minimal oversampling and interpolation in general spaces,” arXiv:2306.07435 (first submitted 2023-06-12), https://arxiv.org/abs/2306.07435.
- NIST Digital Library of Mathematical Functions, Section 3.3 “Interpolation,” https://dlmf.nist.gov/3.3.

# Exact first-Walsh-band concentration spectra on Boolean Hamming balls

## Finding
For every integer \(n\ge3\) and radius \(0\le r\le n\), let \(\Omega_n=\{-1,1\}^n\) carry normalized counting measure, let \(K(x)=|\{i:x_i=-1\}|\), and set \(B_r=\{x:K(x)\le r\}\). Let \(H_1\subset L^2(\Omega_n)\) be the \((n+1)\)-dimensional space spanned by \(1,x_1,\ldots,x_n\), with orthogonal projector \(P_1\). Its Hamming-ball concentration operator is
\[
C_{n,r}=P_1M_{\mathbf1_{B_r}}P_1\big|_{H_1}.
\]
Use the convention \(\binom ab=0\) if \(b<0\) or \(b>a\), and define
\[
p=2^{-n}\sum_{j=0}^{r}\binom nj,\qquad
s=2^{-n}\binom{n-1}r,\qquad
t=2^{-n}\left(\binom{n-2}r-\binom{n-2}{r-1}\right).
\]
The entire concentration spectrum consists of
\[
\lambda_- =p+\frac{(n-1)t}{2}-\sqrt{n s^2+\frac{(n-1)^2t^2}{4}},\qquad
\lambda_0=p-t,\qquad
\lambda_+=p+\frac{(n-1)t}{2}+\sqrt{n s^2+\frac{(n-1)^2t^2}{4}},
\]
with multiplicities \(1,n-1,1\), respectively, combining equal eigenvalues. For \(1\le r\le n-2\) they satisfy the strict interlacing \(0<\lambda_-<\lambda_0<\lambda_+\le1\). The restriction map from \(H_1\) to the ball is injective for every \(r\ge1\). At \(r=0\), the spectrum is \(\{(n+1)2^{-n},0^{[n]}\}\); at \(r=n-1\), it is \(\{1^{[n]},1-(n+1)2^{-n}\}\); and at \(r=n\), it is \(\{1^{[n+1]}\}\).

There is a continuum limit with two persistent spectral outliers. If \(n\to\infty\) and integer radii \(r_n\) satisfy \((2r_n-n)/\sqrt n\to z\in\mathbb R\), write \(\phi(z)=(2\pi)^{-1/2}e^{-z^2/2}\) and \(\Phi(z)=\int_{-\infty}^z\phi(u)\,du\). Then
\[
\lambda_0\to\Phi(z),\qquad
\lambda_{\pm}\to \Phi(z)-\frac{z\phi(z)}2\pm\phi(z)\sqrt{1+\frac{z^2}{4}}.
\]
These are exactly the spectral levels of concentration of the first two normalized Gaussian Hermite polynomials on a half-line; the middle level has multiplicity tending to infinity.

For the balanced half-ball in every odd dimension \(n=2m+1\ge3\), with \(r=m\), the spectral levels are \(1/2-c_m,1/2,1/2+c_m\), where
\[
c_m=\sqrt{2m+1}\,\frac{\binom{2m}{m}}{2^{2m+1}}.
\]
The sharp ratio of the largest to the smallest singular value of restriction to the half-ball is
\[
\kappa_m=\sqrt{\frac{1+2c_m}{1-2c_m}}.
\]
It **strictly decreases** with \(m\ge1\) and converges to
\[
\kappa_\infty=\sqrt{\frac{1+\sqrt{2/\pi}}{1-\sqrt{2/\pi}}}=2.9825048367\ldots.
\]

## Assumptions and scope
The integer \(n\ge3\) and all radii \(0\le r\le n\) are permitted. The Hilbert-space norm on \(L^2(\Omega_n)\) is induced by \(2^{-n}\sum_{x\in\Omega_n}\), and the restriction-map range carries the corresponding restricted sum over \(B_r\). Singular-value claims use this normalization. The symbols \(p,s,t\) are scalar binomial-tail moments, not free parameters. The Gaussian statement fixes a real, finite central-limit coordinate \(z\), not a uniform regime in \(z\) or an arbitrary moving frequency bandwidth.

## Proof
**Gram representation.** The characters \(1,x_1,\ldots,x_n\) form an orthonormal basis for \(H_1\). Put \(J=\sum_{i=1}^n\mathbf1_{\{x_i=-1\}}\) on \(\Omega_n\). By permutation symmetry and direct conditioning on one coordinate,
\[
\mathbb E[\mathbf1_{\{J\le r\}}]=p,\qquad
\mathbb E[x_i\mathbf1_{\{J\le r\}}]=\frac12\Pr\{\operatorname{Bin}(n-1,1/2)=r\}=s.
\]
Conditioning on two distinct coordinates likewise gives
\[
\mathbb E[x_ix_j\mathbf1_{\{J\le r\}}]
=\frac14\bigl(\Pr\{Y=r\}-\Pr\{Y=r-1\}\bigr)=t,
\quad Y\sim\operatorname{Bin}(n-2,1/2).
\]
Consequently the matrix of \(C_{n,r}\) is
\[
G=\begin{pmatrix}p&s\mathbf1^{\mathsf T}\\s\mathbf1&(p-t)I_n+t\mathbf1\mathbf1^{\mathsf T}\end{pmatrix}.
\]

**All eigenvalues and ordering.** On the coordinate-sum-zero subspace, \(G\) acts by \(p-t\), with multiplicity \(n-1\). On the span of the constant character and \(n^{-1/2}\sum_i x_i\), it acts by
\[
R=\begin{pmatrix}p&\sqrt n\,s\\\sqrt n\,s&p+(n-1)t\end{pmatrix}.
\]
The quadratic formula for this real symmetric \(2\times2\) matrix gives \(\lambda_-\) and \(\lambda_+\). Pascal's identity gives \(t=s(n-1-2r)/(n-1)\) for every radius. Therefore
\[
\det(R-(p-t)I_2)=n(t^2-s^2)<0\quad(1\le r\le n-2),
\]
so its two eigenvalues strictly bracket \(p-t\). All concentration eigenvalues lie in \([0,1]\), since \(0\le M_{\mathbf1_{B_r}}\le I\). The values at \(r=0,n-1,n\) follow by direct substitution. To prove strict positivity for \(r\ge1\), note that an affine Walsh polynomial vanishing on \(B_1\) vanishes at the all-plus vertex and its \(n\) one-coordinate flips; subtracting those evaluations forces every linear coefficient and then the constant coefficient to vanish. Since \(B_1\subseteq B_r\), restriction is injective for all \(r\ge1\).

**Gaussian spectral limit.** Under \((2r_n-n)/\sqrt n\to z\), the binomial central limit theorem gives \(p\to\Phi(z)\), and the binomial local limit theorem gives \(\sqrt n\,s\to\phi(z)\). The Pascal identity then implies \((n-1)t=(n-1-2r_n)s\to-z\phi(z)\), while \(t\to0\). Thus \(R\) converges entrywise to
\[
R_z=\begin{pmatrix}\Phi(z)&\phi(z)\\\phi(z)&\Phi(z)-z\phi(z)\end{pmatrix},
\]
which is the Gaussian half-line Gram matrix for normalized first-chaos basis \(1,u\) after reflecting the Gaussian coordinate. Continuity of eigenvalues of symmetric matrices proves the three limits, including the two distinct outliers for finite \(z\).

**Odd-dimensional half-ball stability.** At \(n=2m+1\) and \(r=m\), binomial symmetry gives \(p=1/2\) and \(t=0\). Hence \(\lambda_\pm=1/2\pm c_m\) and \(\lambda_0=1/2\). The singular values of restriction are the square roots of the concentration eigenvalues, so the claimed \(\kappa_m\) is exact. Central-binomial ratios give
\[
\frac{c_{m+1}^2}{c_m^2}=\frac{(2m+1)(2m+3)}{(2m+2)^2}=1-\frac1{(2m+2)^2}<1.
\]
Since \(0<c_m<1/2\), \(\kappa_m\) strictly decreases. Stirling's central-binomial asymptotic gives \(c_m\to(2\pi)^{-1/2}\) and the displayed limit.

## Verification
A standalone standard-library checker, `verify.py`, forms each restricted Walsh Gram matrix by direct enumeration by enumerating all cube vertices for \(3\le n\le8\) and every radius. It compares the matrices exactly as rational numbers and reconstructs their characteristic polynomials by Newton identities from matrix-power traces. All 39 finite parameter cases agree with the predicted multiplicities and eigenvalue factors. The checker also verifies 99 exact central-binomial monotonicity steps and three numerical Gaussian-scaling comparisons at a larger dimension. These finite checks support, but do not substitute for, the all-dimension combinatorial proof and central/local limit argument.

## Relationship to prior work
Harrow, Kolla, and Schulman (2014) use Walsh and Krawtchouk spectral decompositions to prove a dimension-free spherical maximal inequality on the same Boolean cube. Tsitsvero, Barbarossa, and Di Lorenzo (2015) introduce general graph spatial/frequency concentration operators and explain why the nonzero spectra control sampling and localization; their abstract graph-projection theory does not specialize to exact Hamming-ball binomial spectra. Hogan and Lakey (2018, 2019) directly investigate Boolean-hypercube Slepian operators; their first article computes invariant-operator commutators, numerically approximates eigenvectors and lists some equal-radius spectra, while already proving the general full-rank criterion for distinct spatial and frequency radii. Their subsequent Corollary 9 is an eigenspace reduction via finite matrices for equal radii. These results supply the setting and encompass the injectivity consequence here, but neither supplies the all-radius first-band closed eigenvalue formula, strict three-sector interlacing and the Gaussian crossover or the balanced condition-number limit. The earlier spherical-mean spectral multipliers and maximal estimates do not themselves determine the concentration operator \(P_1M_{\mathbf1_{B_r}}P_1\) or its sampling condition numbers. Avni and Samorodnitsky (2024) obtain a far-reaching spectrum and eigenfunction description for **induced-ball adjacency operators**, using Krawtchouk zeros; induced adjacency \(M_{\mathbf1_{B_r}}AM_{\mathbf1_{B_r}}\) is distinct from low-Walsh-band spatial concentration. The present result treats the latter complete spectrum, the exact interlacing, and its binomial-to-Gaussian limit.

Halfspace complementation symmetry explains the middle half-energy level in the odd balanced case but does not by itself determine the off-central eigenvalues, their sharp condition number, or the all-radius formulas. Degree-two single-shell concentration and Gaussian Hermite half-line formulas likewise concern different operators or limiting cases.

## Limitations
The claim concerns the first Walsh band only, not arbitrary Fourier degree. The two outlying eigenvalues do not constitute a nontrivial limiting empirical spectral fraction: their combined multiplicity remains two while the middle multiplicity grows. The stated Gaussian limit assumes a fixed finite central-limit coordinate, and no uniform tail-regime rate is asserted. The formula follows from specific exchangeable binomial moments; analogous exact simplifications are not asserted for general spatial sets. An equivalent presentation may exist in older coding-theoretic covariance or Krawtchouk literature; the source search is not proof of worldwide novelty. Scientific checks here do not constitute independent external audit.

## References
1. Aram W. Harrow, Alexandra Kolla, and Leonard J. Schulman, *Dimension-Free \(L_2\) Maximal Inequality for Spherical Means in the Hypercube*, Theory of Computing **10** (2014), 55–75, DOI: 10.4086/toc.2014.v010a003; publicly published 2014-05-23. https://www.theoryofcomputing.org/articles/v010a003/
2. Mikhail Tsitsvero, Sergio Barbarossa, and Paolo Di Lorenzo, *Signals on Graphs: Uncertainty Principle and Sampling*, arXiv:1507.08822v1 (2015-07-31), Theorem 2.3 on bandlimited concentration projectors. https://arxiv.org/abs/1507.08822
3. Jeffrey A. Hogan and Joseph D. Lakey, *Spatio-spectral limiting on hypercubes: eigenspaces*, arXiv:1812.08905v1 (2018-12-21), Corollary 9 and its equal-radius specialization. https://arxiv.org/abs/1812.08905
4. Jeffrey A. Hogan and Joseph D. Lakey, *An Analogue of Slepian Vectors on Boolean Hypercubes*, Journal of Fourier Analysis and Applications **25** (2019), 2004–2020, published online 2018-11-20, DOI: 10.1007/s00041-018-09654-w; numerical spectra and the general band/ball-rank identity in Sections 2–5. https://doi.org/10.1007/s00041-018-09654-w
5. Amit Avni and Alex Samorodnitsky, *Eigenvalues and eigenfunctions of a Hamming ball*, arXiv:2411.14597v1 (2024-11-21). https://arxiv.org/abs/2411.14597

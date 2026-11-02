# An arithmetic flux split in the sharp high-density conditioning of first-Hermite Gabor frames

## Finding

Let \(h_1(t)=2^{5/4}\sqrt{\pi}\,t e^{-\pi t^2}\) be the real first Hermite function, normalized in \(L^2(\mathbb R)\). For \(q>0\), form the square-lattice Gabor system
\[
\mathcal G_q=\{M_{n/\sqrt q}T_{m/\sqrt q}h_1:m,n\in\mathbb Z\},
\qquad T_xf(t)=f(t-x),\quad M_\xi f(t)=e^{2\pi i\xi t}f(t).
\]
Let \(A_q\) and \(B_q\) be its **optimal** lower and upper frame bounds, and set \(\kappa_q=B_q/A_q\) whenever it is a frame.

**Theorem.** For every integer or half-integer \(q\ge3\), this system is a frame. Define
\[
\beta_q=(\pi q-1)e^{-\pi q/2},\qquad
H(q)=\begin{cases}4,&q\in\mathbb Z,\\2\sqrt2,&q\in\mathbb Z+\tfrac12.\end{cases}
\]
Then the following **uniform explicit spectral error** holds:
\[
\boxed{\left|\frac{A_q}{q}-(1-H(q)\beta_q)\right|\le100q e^{-\pi q},\qquad
\left|\frac{B_q}{q}-(1+H(q)\beta_q)\right|\le100q e^{-\pi q}.}
\]
In particular, along either indicated arithmetic sequence,
\[
\boxed{\kappa_q=1+2H(q)(\pi q-1)e^{-\pi q/2}+O(q^2e^{-\pi q}).}
\]
Consequently the two sharp conditioning limits are distinct:
\[
\boxed{
\lim_{\substack{q\to\infty\\q\in\mathbb Z}}
\frac{\kappa_q-1}{q e^{-\pi q/2}}=8\pi,
\qquad
\lim_{\substack{q\to\infty\\q\in\mathbb Z+1/2}}
\frac{\kappa_q-1}{q e^{-\pi q/2}}=4\sqrt2\,\pi.}
\]
Thus the reciprocal-density parity produces a sharp \(\sqrt2\) contrast in the leading conditioning defect, even though both lattice families approach the same continuous tight-frame limit.

## Assumptions and scope

All operators act on complex \(L^2(\mathbb R)\). The operator \(S_q\) of \(\mathcal G_q\) is defined by
\[
\langle S_qf,f\rangle=\sum_{m,n\in\mathbb Z}|\langle f,M_{n/\sqrt q}T_{m/\sqrt q}h_1\rangle|^2.
\]
For a positive invertible frame operator its optimal bounds are the spectral infimum and supremum. Only square lattices, the fixed first Hermite window, and the integer or half-integer reciprocal-density sequences are claimed. All displayed error constants are independent of \(q\ge3\).

## Proof

**1. A four-generator reduction.** Put \(L=\sqrt q\), \(U=T_L\), and \(V=M_L\). The Gaussian integral verifies \(\|h_1\|_2=1\). The short-time Fourier transform of the normalized first Hermite function is
\[
\langle h_1,M_\xi T_xh_1\rangle
=e^{-\pi ix\xi}(1-\pi(x^2+\xi^2))e^{-\pi(x^2+\xi^2)/2}.
\tag{1}
\]
One may also obtain (1) directly by completing the square in the integral for \(t(t-x)e^{-\pi(t^2+(t-x)^2)}\). Since \(h_1\) is Schwartz, Poisson summation in each Gabor lattice index gives the absolutely operator-norm convergent Janssen identity
\[
q^{-1}S_q=\sum_{k,l\in\mathbb Z}
\langle h_1,M_{kL}T_{lL}h_1\rangle M_{kL}T_{lL}.
\tag{2}
\]
For clarity, this follows first by applying Poisson summation to the modulation sum in \(S_qf\), which produces translations \(T_{lL}f\), and then to the translation sum, which produces the coefficients in (2). Schwartz decay permits the exchanges for test functions and the absolutely convergent operator series extends the identity to \(L^2\).

In (2), the term \((k,l)=(0,0)\) is the identity, and the four terms with \(k^2+l^2=1\) all have the same real coefficient
\[
c_q=(1-\pi q)e^{-\pi q/2}=-\beta_q.
\]
Therefore, setting \(\mathcal H_q=U+U^*+V+V^*\), we have
\[
q^{-1}S_q=I-\beta_q\mathcal H_q+R_q.
\tag{3}
\]

**2. A uniform, summable remainder.** Formula (1) and unitarity of each Weyl shift give, for \(q\ge2\),
\[
\|R_q\|\le\sum_{\substack{k,l\in\mathbb Z\\k^2+l^2\ge2}}
(1+\pi q(k^2+l^2))e^{-\pi q(k^2+l^2)/2}.
\]
For each positive integer \(m\), the number of integer pairs with \(k^2+l^2=m\) is at most \(4(m+1)\). Since \(1+\pi qm\le q(1/2+\pi m)\) and \(q\ge2\),
\[
\|R_q\|\le Cq e^{-\pi q},\quad
C=4\sum_{j=0}^{\infty}(j+3)\left(\tfrac12+\pi(j+2)\right)e^{-\pi j}<100.
\tag{4}
\]
The final bound is elementary: \(\pi<22/7\), \(e^{-\pi}<1/20\), and summing the resulting geometric series and its first two derivatives yields
\(C\le617840/6859<100\). This is an infinite-tail estimate, not a finite truncation.

**3. Opposite spectral edges have equal magnitude.** Define the unitary \(W=M_{1/(2L)}T_{1/(2L)}\). The commutation relations imply \(WUW^*=-U\) and \(WVW^*=-V\). Hence
\(W\mathcal H_qW^*=-\mathcal H_q\), so its spectrum is symmetric about zero. Write \(h(q)=\|\mathcal H_q\|\). Both spectral edges are therefore \(h(q)\) and \(-h(q)\).

**4. Integer flux: \(h(q)=4\).** When \(q\in\mathbb Z\), \(UV=VU\). The triangle inequality gives \(h(q)\le4\). To prove equality, choose a smooth unit \(L^2\) bump \(\varphi_\varepsilon\) supported in \((-\varepsilon,\varepsilon)\), with \(\varepsilon<L/4\), and normalize the disjoint finite comb
\[
f_{N,\varepsilon}=(2N+1)^{-1/2}
\sum_{j=-N}^{N}\varphi_\varepsilon(\cdot-jL).
\]
Translation by \(L\) changes only the two end bumps, so \(\|(U-I)f_{N,\varepsilon}\|\to0\) as \(N\to\infty\). At every bump center, \(e^{2\pi iL(jL)}=e^{2\pi iqj}=1\), giving \(\|(V-I)f_{N,\varepsilon}\|\le2\pi L\varepsilon\). Taking \(N\to\infty\) and then \(\varepsilon\to0\) proves \(\|(\mathcal H_q-4I)f_{N,\varepsilon}\|\to0\), whence \(h(q)=4\).

**5. Half-integer flux: \(h(q)=2\sqrt2\).** If \(q\in\mathbb Z+\tfrac12\), then \(UV=-VU\), and the same anticommutation holds with either unitary replaced by its inverse. Consequently
\[
\mathcal H_q^2=4I+U^2+U^{*2}+V^2+V^{*2},
\]
so \(\|\mathcal H_q\|^2\le8\). Repeat the preceding comb construction with centers \(2jL\) instead of \(jL\). Translation by \(2L\) is approximately the identity, while modulation by \(2L\) equals one at every center because
\(e^{2\pi i(2L)(2jL)}=e^{8\pi i qj}=1\).
Thus \(U^2f_{N,\varepsilon}\to f_{N,\varepsilon}\) and \(V^2f_{N,\varepsilon}\to f_{N,\varepsilon}\) in successive limits, and
\(\langle\mathcal H_q^2f_{N,\varepsilon},f_{N,\varepsilon}\rangle\to8\). It follows that \(h(q)^2=8\), giving \(h(q)=2\sqrt2\).

**6. Optimal bounds and conditioning.** By (3), spectral symmetry and the selfadjoint perturbation inequality, the lower and upper spectral edges of \(q^{-1}S_q\) differ from \(1-h(q)\beta_q\) and \(1+h(q)\beta_q\), respectively, by at most \(\|R_q\|\). The exact values of \(h(q)\) and (4) give the two explicit estimates in the theorem. For \(q\ge3\), the monotone decreasing function
\(4(\pi q-1)e^{-\pi q/2}+100qe^{-\pi q}\) is already smaller than one at \(q=3\). Thus \(A_q>0\), proving the frame assertion without relying on a separate frame-set theorem.

Finally, \(\beta_q=O(qe^{-\pi q/2})\), the lower bound tends to one, and expansion of \(B_q/A_q\) gives
\(\kappa_q=1+2h(q)\beta_q+O(q^2e^{-\pi q})\). Inserting the two exact values of \(h(q)\) proves both limits. \(\square\)

## Verification

The included `CHECK.py` runs with Python 3 and the standard library alone (`python3 CHECK.py`). It checks a rigorously conservative tail bound on selected integer and half-integer parameters and samples the explicit one-dimensional and two-dimensional Bloch eigenvalue formulas for commuting and anticommuting unitary generators. On the recorded run it passed **20,430 finite assertions**. The infinite operator-norm assertions, spectral edge attainability, and the limit are proved above; the finite tests are supplementary diagnostics.

## Relationship to prior work

The Janssen representation and the Hermite ambiguity identity are classical and are used explicitly by Faulhuber, Shafkulovska and Zlotnikov, *Asymptotic safety regions for Gabor frames generated by Hermite functions* (arXiv:2609.01296, first posted September 1, 2026). Their principal new bounds control frame-set regions as the Hermite **order grows**; this theorem instead fixes order one and calculates **sharp optimal-bound asymptotics** with reciprocal-density arithmetic dependence.

Faulhuber and Petersen, *The frame set of the first Hermite function* (arXiv:2609.02610, September 2, 2026), classify whether the system is a frame, not its sharp conditioning defect. Faulhuber, Shafkulovska and Zlotnikov, *On the Frame Property of Hermite Functions and Exploration of their Frame Sets* (2025), analyze threshold safety and Janssen estimates rather than the present two arithmetic subsequences. Faulhuber and Shafkulovska, *Gabor frame bound optimizations* (arXiv:2204.02917), optimize several non-Hermite windows; Faulhuber and Steinerberger, *Optimal Gabor frame bounds for separable lattices and estimates for Jacobi theta functions* (2017), concern the Gaussian. These statements do not imply the displayed first-Hermite constants \(8\pi\) and \(4\sqrt2\,\pi\). Classical magnetic Harper spectral algebra explains the two nearest-neighbor operator norms; the conclusion here is their quantitative appearance in the *optimal* frame bounds of a particular Hermite window.

## Limitations

The asymptotic formulas are proved for the fixed first Hermite window, square lattices, and the two specified reciprocal-density subsequences. There is no claim of global lattice-shape optimality, of complete spectral formulas for arbitrary flux, or of a uniform expansion in Hermite order. The leading-order constants and explicit errors are analytical, while the checker is finite. The originality comparison is based on the cited accessible sources and mathematical-record searches; it cannot exclude an implicit equivalent calculation in unindexed older literature. No independent mathematical audit has been performed.

## References

1. M. Faulhuber, I. Shafkulovska and I. Zlotnikov, *Asymptotic safety regions for Gabor frames generated by Hermite functions*, arXiv:2609.01296 (2026), https://arxiv.org/abs/2609.01296.
2. M. Faulhuber and P. Petersen, *The frame set of the first Hermite function*, arXiv:2609.02610 (2026), https://arxiv.org/abs/2609.02610.
3. M. Faulhuber, I. Shafkulovska and I. Zlotnikov, *On the Frame Property of Hermite Functions and Exploration of their Frame Sets*, Journal of Fourier Analysis and Applications 31, 21 (2025), https://doi.org/10.1007/s00041-025-10153-y.
4. M. Faulhuber and I. Shafkulovska, *Gabor frame bound optimizations*, Applied and Computational Harmonic Analysis 67 (2023), arXiv:2204.02917.
5. M. Faulhuber and S. Steinerberger, *Optimal Gabor frame bounds for separable lattices and estimates for Jacobi theta functions*, Journal of Mathematical Analysis and Applications 445 (2017), 407--422, https://doi.org/10.1016/j.jmaa.2016.07.074.
6. A. J. E. M. Janssen, *The Gabor Frame Operator (its Structure and Numerical Consequences)*, in Gabor Analysis and Algorithms (1998).

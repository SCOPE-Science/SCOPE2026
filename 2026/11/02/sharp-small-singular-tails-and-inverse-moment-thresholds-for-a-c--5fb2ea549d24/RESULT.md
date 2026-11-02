# Sharp small-singular tails and inverse-moment thresholds for a circular Fourier sketch

## Finding

Let \(L\ge2\) be an integer, let \(\Theta_1,\ldots,\Theta_L\) be independent uniform angles on \([0,2\pi)\), and let \(\xi_j\in\{-1,1\}\) be arbitrary signs. Form the unnormalized two-frequency sketch
\[
S_L=\begin{pmatrix}
\xi_1&\cdots&\xi_L\\
\xi_1e^{i\Theta_1}&\cdots&\xi_Le^{i\Theta_L}
\end{pmatrix}\in\mathbb C^{2\times L}.
\]
Put \(\lambda_L=\lambda_{\min}(S_LS_L^*)\). Then \(S_L\) has full row rank almost surely, and for every *fixed* \(L\ge2\),
\[
\boxed{\lim_{\varepsilon\downarrow0}
\frac{\Pr\{\lambda_L\le\varepsilon\}}
{\varepsilon^{(L-1)/2}}
=\frac{\sqrt L}{(2\pi)^{(L-1)/2}\Gamma((L+1)/2)}=:C_L.}
\]
For every real \(q>0\), this yields the sharp inverse-Gram moment criterion
\[
\boxed{\mathbb E\,\lambda_L^{-q}<\infty\quad\Longleftrightarrow\quad q<(L-1)/2.}
\]
In particular, \(\mathbb E\|S_L^\dagger\|_2^2=\infty\) for \(L=2,3\), and is finite for all \(L\ge4\). The spectral condition number \(\kappa_L=\|S_L\|_2\|S_L^\dagger\|_2\) has exact power-law tail
\[
\boxed{\Pr\{\kappa_L>t\}\sim C_L(2L)^{(L-1)/2}t^{-(L-1)}\quad(t\to\infty),}
\]
and \(\mathbb E\kappa_L^p<\infty\) exactly when \(0<p<L-1\).

The distinction is present already with three sketch columns: a \(2\times3\) matrix of independent standard *complex Gaussian* entries has finite expected squared pseudoinverse norm, whereas the displayed isotropic circular Fourier sketch does not.

## Assumptions and scope

The columns are independent copies of the circular Fourier functional restricted to Fourier modes \(0\) and \(1\): \(s(x)=\xi\sum_{n\in\mathbb Z}x_ne^{in\Theta}\), when evaluated on the two coordinate vectors. The signs may be independent Rademacher variables as in the motivating construction; because each column sign has squared modulus one, the Gram matrix and all conclusions are sign-independent. The angles are genuinely continuous and independent. The underlying scalar field is complex, and matrix singular values and operator norms are complex Euclidean ones. The sketch is **unnormalized**; dividing its columns by \(\sqrt L\) rescales the Gram eigenvalues by \(1/L\) but leaves the condition number and exponent unchanged. Every small-threshold asymptotic is at fixed \(L\), not uniformly in an increasing sample count.

## Proof

**1. Exact Gram reduction.** Write \(Z_L=\sum_{j=1}^L e^{i\Theta_j}\). Direct multiplication gives
\[
S_LS_L^*=\begin{pmatrix}L&\overline{Z_L}\\ Z_L&L\end{pmatrix},
\qquad \lambda_L=L-|Z_L|,\qquad
\lambda_{\max}=L+|Z_L|.
\]
The triangle inequality implies \(\lambda_L\ge0\). Equality occurs only when all phases agree modulo \(2\pi\). The latter event has probability zero for \(L\ge2\); therefore, \(S_L\) has full row rank almost surely, and \(\|S_L^\dagger\|_2^2=\lambda_L^{-1}\).

**2. Localization of the small-eigenvalue event.** Multiplying \(Z_L\) by the unit scalar \(e^{-i\Theta_1}\) leaves its magnitude unchanged. Conditional on \(\Theta_1\), the relative phases \(\phi_j=\Theta_j-\Theta_1\pmod{2\pi}\), represented in \((-\pi,\pi]\), are independent uniform angles. Set \(m=L-1\) and \(\phi=(\phi_2,\ldots,\phi_L)\). We have the identity
\[
L^2-|Z_L|^2=2\sum_{1\le i<j\le L}
\bigl(1-\cos(\Theta_i-\Theta_j)\bigr).
\]
If \(\lambda_L\to0\), the left side equals \(\lambda_L(2L-\lambda_L)\to0\). Every summand on the right is nonnegative, so every relative angle converges to zero modulo \(2\pi\), including each \(\phi_j\). By compactness of the relative-angle torus, for every sufficiently small fixed neighborhood of the origin, all small-eigenvalue configurations lie inside that neighborhood when \(\varepsilon\) is sufficiently small. No other alignment strata contribute.

**3. Nondegenerate quadratic defect.** Taylor expansion of sine and cosine, or of the preceding identity, gives uniformly near \(\phi=0\)
\[
\lambda_L(\phi)=\frac12\left(\sum_{j=2}^L\phi_j^2
-\frac1L\left(\sum_{j=2}^L\phi_j\right)^2\right)
+O(\|\phi\|_2^4)
=\tfrac12\phi^{\mathsf T}M\phi+O(\|\phi\|_2^4),
\]
where \(M=I_m-L^{-1}\mathbf1\mathbf1^{\mathsf T}\). Its eigenvalues are \(1\) with multiplicity \(m-1\), and \(1/L\) with multiplicity one. Hence \(M\) is positive definite and \(\det M=1/L\). In a sufficiently small neighborhood, \(\lambda_L\) is bounded above and below by positive multiples of \(\|\phi\|_2^2\); consequently, the event \(\lambda_L\le\varepsilon\) lies in a ball of radius \(O(\sqrt\varepsilon)\).

**4. Ellipsoid-volume limit.** Substitute \(\phi=\sqrt\varepsilon\,y\) in the exact relative-angle integral. The uniform density is \((2\pi)^{-m}\). On bounded sets,
\[
\varepsilon^{-1}\lambda_L(\sqrt\varepsilon\,y)
\longrightarrow\tfrac12y^{\mathsf T}My.
\]
The bounds in Step 3 supply a common compact integration region after scaling. The indicator functions converge almost everywhere, since the ellipsoid boundary has Lebesgue measure zero. Dominated convergence therefore yields
\[
\lim_{\varepsilon\downarrow0}\varepsilon^{-m/2}\Pr(\lambda_L\le\varepsilon)
=(2\pi)^{-m}\operatorname{vol}
\{y:y^{\mathsf T}My\le2\}.
\]
An orthogonal change of coordinates gives the volume \(\sqrt L\,(2)^{m/2}\pi^{m/2}/\Gamma(1+m/2)\); the claimed \(C_L\) follows by \(m=L-1\).

**5. Negative moments and condition numbers.** Since the distribution function \(F(x)=\Pr(\lambda_L\le x)\) satisfies \(F(x)\sim C_Lx^{\alpha}\) with \(\alpha=(L-1)/2\) and \(C_L>0\), the layer-cake formula, or integration by parts near the origin, shows that \(\mathbb E\lambda_L^{-q}\) has the same convergence criterion as \(\int_0^1 x^{\alpha-q-1}\,dx\). This integral converges exactly for \(q<\alpha\), and diverges logarithmically at equality. For the condition number, the exact Gram eigenvalues give
\[
\kappa_L^2=\frac{2L-\lambda_L}{\lambda_L},\qquad
\Pr(\kappa_L>t)=\Pr\left(\lambda_L<\frac{2L}{1+t^2}\right).
\]
Substitution into the small-ball limit proves the stated power-law constant and moment threshold.

**6. A Gaussian comparator.** Let \(G\in\mathbb C^{2\times L}\) have independent standard circular complex Gaussian entries and let \(W=GG^*\). Conditional on the second row, the squared Euclidean norm of the first row projected orthogonally to the second is gamma distributed with integer shape \(L-1\) and unit scale. The first diagonal entry of \(W^{-1}\) is the reciprocal of this residual square, by the Schur complement. Therefore for \(L\ge3\), \(\mathbb E(W^{-1})_{11}=1/(L-2)\), and symmetrically \(\mathbb E\operatorname{tr}W^{-1}=2/(L-2)\). Since \(\|G^\dagger\|_2^2=\lambda_{\min}(W)^{-1}\le\operatorname{tr}W^{-1}\), its expected squared pseudoinverse norm is finite at \(L=3\), unlike for \(S_3\).

## Verification

For \(L=2\), letting the phase difference be uniform gives the independent exact check
\[
\Pr(\lambda_2\le\varepsilon)
=\frac2\pi\arccos(1-\varepsilon/2),\qquad0\le\varepsilon\le2.
\]
Its expansion yields \(C_2=2/\pi\). Also \(C_3=\sqrt3/(2\pi)\). The accompanying Python verifier checks the Gram identity, positive-definiteness and quadratic expansion on seeded samples, the condition-number identity, the closed-form two-column CDF, and finite Monte Carlo consistency checks. All infinitely quantified assertions follow from Steps 1–6, **not** finite experiments. Run the standalone standard-library checker by `python verifier.py` from the extracted finding directory.

## Relationship to prior work

Lynch-Davies and Webb introduce the circular Fourier sketch as an isotropic but low-entropy example in Section 4.2 of their 2026 paper. They note possible near-linear dependence and the relevance of a pseudoinverse in the structural error bound, but do not provide this fixed-two-frequency sharp small-ball coefficient or the exact inverse-moment oversampling threshold. The earlier work of Ryan and Debbah studies large-dimensional asymptotic positive Gram moments of random unit-circle Vandermonde matrices under a joint dimension limit; those results do not imply the fixed-two-row near-zero spectral tail. Kunis and Nagel prove deterministic separation bounds for clustered-node Vandermonde systems under the condition that the number of nodes is strictly smaller than the number of polynomial coefficients. The present overcomplete two-frequency sketch has the reverse orientation, with \(L\ge2\) sample columns, and requires a stochastic codimension calculation. Classical circular resultant-length statistics provide the equivalent planar-random-walk language but, among the inspected sources, no exact edge coefficient together with its sketch-conditioning consequence was identified. Lack of an identified result is not an exhaustive proof of novelty.

## Limitations

The result concerns only the two consecutive Fourier coordinates and independent uniformly distributed continuous phases; it does not bound the full numerical randomized-SVD error, a general infinite-dimensional operator, correlated phase sampling, or more than two active modes. The constant is fixed-sample-size, not uniform in \(L\). The Gaussian comparator is complex Gaussian with the same unnormalized covariance, not real Gaussian. The underlying planar-resultant boundary asymptotic could appear elsewhere in directional-statistics literature; historical priority remains subject to independent expert confirmation. No independent mathematical audit has been performed.

## References

1. M. Lynch-Davies and M. Webb, *Sketching Outside the Hilbert Space for the Infinite-Dimensional Randomised SVD*, arXiv:2610.31333v1 (first public October 22, 2026), especially Section 4.2, pp. 29–30. https://arxiv.org/abs/2610.31333
2. Ø. Ryan and M. Debbah, *Asymptotic Behaviour of Random Vandermonde Matrices with Entries on the Unit Circle*, arXiv:0802.3570, especially the introduction and Section III (2008–09). https://arxiv.org/abs/0802.3570
3. S. Kunis and D. Nagel, *On the smallest singular value of multivariate Vandermonde matrices with clustered nodes*, arXiv:1907.07119v1 (2019), especially Definition 2.1 and the main separation-bound setting. https://arxiv.org/abs/1907.07119

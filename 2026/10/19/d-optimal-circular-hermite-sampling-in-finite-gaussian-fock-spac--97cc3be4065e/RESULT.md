# D-optimal circular Hermite sampling in finite Gaussian Fock space and its exponential volume penalty

## Finding

Let \(n\ge2\), let \(\mathcal P_{2n-1}\) be the complex polynomials of degree at most \(2n-1\), with Gaussian Fock norm
\[
\|p\|_{\mathcal F}^2=\int_{\mathbb C}|p(z)|^2 e^{-\pi|z|^2}\,dA(z).
\]
At \(n\) distinct points \(z_j=\rho\zeta_j\) on one circle, take **both** value evaluations and first-derivative evaluations, each divided by its own norm as a linear functional on \(\mathcal P_{2n-1}\). Let \(M_H\) be the resulting square \(2n\)-row measurement matrix in any orthonormal polynomial basis, and let \(D_H=\det(M_H^*M_H)\). Define \(t=\pi\rho^2\),
\[
S_0(t)=\sum_{k=0}^{2n-1}\frac{t^k}{k!},\qquad
S_2(t)=\sum_{k=1}^{2n-1}\frac{k^2t^k}{k!},\qquad
C_n=\prod_{k=0}^{2n-1}k!.
\]
**Exact determinant and angular classification:** for every \(t>0\),
\[
D_H(t;\zeta_1,\ldots,\zeta_n)=
\frac{t^{n(2n-1)}}{C_n[S_0(t)S_2(t)]^n}
\prod_{1\le i<j\le n}|\zeta_j-\zeta_i|^8.
\]
For every fixed radius, this determinant has its unique maximum up to rotation and permutation when the \(\zeta_j\) are a regular \(n\)-gon, giving
\[
\mathcal D_H(n,t)=\frac{n^{4n}t^{n(2n-1)}}{C_n[S_0(t)S_2(t)]^n}.
\]
**Unique optimal radius:** its global maximum occurs at exactly one \(t=t_H(n)>0\), characterized by
\[
\frac{\sum_{k=0}^{2n-1}k t^k/k!}{S_0(t)}
+\frac{\sum_{k=1}^{2n-1}k^3t^k/k!}{S_2(t)}=2n-1.
\]
For regular-polygon nodes the *entire* squared singular-value spectrum is the union, for \(j=0,\ldots,n-1\), of the two eigenvalues of \(B_j^*B_j\), where
\[
B_j=\sqrt n\begin{pmatrix}
a_j/\sqrt{S_0(t)}&a_{j+n}/\sqrt{S_0(t)}\\
j a_j/\sqrt{S_2(t)}&(j+n)a_{j+n}/\sqrt{S_2(t)}
\end{pmatrix},\qquad a_k=\sqrt{t^k/k!}.
\]

**Exponential cost of co-located jets:** let \(\mathcal D_V(n)\) be the global maximum of \(\det(M_V^*M_V)\) for **\(2n\) distinct normalized value evaluations** on a freely chosen common circle in the same polynomial space. Their unique optimal radius \(t_V(n)>0\) satisfies
\[
\frac{\sum_{k=0}^{2n-1}k t^k/k!}{S_0(t)}=\frac{2n-1}{2}.
\]
As \(n\to\infty\),
\[
t_H(n)=n-\frac32+\frac1{2n}+O(n^{-2}),\qquad
 t_V(n)=n-\frac12+O(e^{-cn})
\]
for some absolute \(c>0\). In particular \(t_V(n)-t_H(n)\to1\), and the exact sharp *squared-volume* penalty is
\[
\boxed{\lim_{n\to\infty}4^n\frac{\max_{t>0}\mathcal D_H(n,t)}{\mathcal D_V(n)}=e.}
\]
Thus replacing \(2n\) distinct normalized value samples by values and derivatives co-located at \(n\) nodes has an asymptotically \(e\,4^{-n}\) determinant ratio under the same total number of normalized complex measurements. The comparison concerns determinant volume, not an asserted universal condition-number optimum.

## Assumptions and scope

The radial parameter is strictly positive, the \(n\) Hermite nodes are distinct, and value and ordinary complex derivative are normalized separately **in the finite polynomial Hilbert space**. Precisely, in the orthonormal basis \(e_k(z)=\pi^{k/2}z^k/\sqrt{k!}\), the squared evaluation norm is \(S_0(t)\) and the squared derivative-evaluation norm is \(S_2(t)/\rho^2\). Multiplying each normalized derivative row by \(\zeta_j\) is unitary row scaling and turns it into the normalized Euler derivative \(zp'(z)\); therefore the determinant and singular values are unchanged. The value-only comparator uses the identical Hilbert space and individually normalized evaluation rows, with \(2n\) distinct common-circle sites. No claims are made about sampling points at different radii, arbitrarily placed planar points, or uniform sampling over the entire infinite-dimensional Fock space.

## Proof

**1. Confluent determinant.** Set \(m=2n-1\) and \(\zeta_j=e^{i\theta_j}\). The coefficient of \(e_k\) in the value row is \(t^{k/2}\zeta_j^k/\sqrt{k!S_0(t)}\); after multiplying the derivative row by \(\zeta_j\), its coefficient is \(k t^{k/2}\zeta_j^k/\sqrt{k!S_2(t)}\). For the underlying unscaled Hermite-Vandermonde matrix, replacing ordinary derivatives by Euler derivatives multiplies its confluent Vandermonde determinant by \(\prod_j z_j\). Thus
\[
|\det M_H|^2=\frac{t^{\sum_{k=0}^{m}k}}{C_n[S_0(t)S_2(t)]^n}\prod_{i<j}|\zeta_j-\zeta_i|^8.
\]
Here \(\sum_{k=0}^{m}k=n(2n-1)\). The formula is exact even for nonuniform node angles.

**2. Angular rigidity.** The ordinary \(n\)-by-\(n\) Vandermonde matrix \((\zeta_j^k)_{j,0\le k<n}\) has each column of squared norm \(n\). Hadamard's bound gives \(\prod_{i<j}|\zeta_j-\zeta_i|^2\le n^n\). Equality requires mutually orthogonal columns, so \(\sum_j\zeta_j^k=0\) for \(1\le k\le n-1\). Newton's identities then say the monic node polynomial is \(z^n-c\) with \(|c|=1\): exactly a rotated regular \(n\)-gon. This proves the unique angular optimum and the factor \(n^{4n}\).

**3. Radial uniqueness.** Let \(p_k(t)=(t^k/k!)/S_0(t)\) for \(0\le k\le m\). Write \(\mu_0(t)=\sum k p_k(t)\) and \(\mu_2(t)=\sum k^3p_k(t)/(\sum k^2p_k(t))\). Differentiating \(\log\mathcal D_H(n,t)\) yields
\[
\frac{d}{dt}\log\mathcal D_H(n,t)=\frac n t\,[m-\mu_0(t)-\mu_2(t)].
\]
In the exponential-family parameter \(\log t\), each mean is strictly increasing because its derivative is the variance of \(k\) under its probability weights (ordinary \(p_k\) and weights proportional to \(k^2p_k\), respectively). The sum increases strictly from \(1\) as \(t\downarrow0\) to \(2m\) as \(t\to\infty\). Since \(m\ge3\), there is one critical point, which is the unique global maximum: the determinant tends to zero at both endpoints. The same variance argument with \(\mu_0(t)=m/2\) yields the value-only optimum. The ordinary value Vandermonde gives
\[
\mathcal D_V(n,t)=\frac{(2n)^{2n}t^{nm}}{C_nS_0(t)^{2n}}.
\]

**4. Exact spectrum.** At regular nodes \(\zeta_j=e^{i\theta_0}\omega^j\), apply the unitary \(n\)-point discrete Fourier transform independently to value and (phase-corrected) derivative rows. Reorder polynomial coefficients by residue modulo \(n\). This produces the displayed direct sum of \(2\)-by-\(2\) blocks \(B_j\), up to harmless unitary phases. Each squared singular pair is
\[
\lambda_{j,\pm}=\frac{T_j\pm\sqrt{T_j^2-4E_j}}2,
\]
where
\[
T_j=n\left[\frac{a_j^2+a_{j+n}^2}{S_0(t)}+
\frac{j^2a_j^2+(j+n)^2a_{j+n}^2}{S_2(t)}\right],\quad
E_j=\frac{n^4a_j^2a_{j+n}^2}{S_0(t)S_2(t)}.
\]
All \(E_j>0\), so Hermite interpolation is nonsingular for distinct nonzero nodes.

**5. Sharp asymptotic ratio.** For \(t\) in any fixed-width interval around \(n\), truncated-Poisson tail estimates give, uniformly with the derivatives needed below,
\[
S_0(t)=e^t[1+O(e^{-cn})],\quad
S_2(t)=e^t(t^2+t)[1+O(e^{-cn})]
\]
with some fixed \(c>0\). Polynomial factors absorbed by choosing a smaller \(c\). The two radial stationarity equations consequently become
\[
\mu_0(t)=t+O(e^{-cn}),\qquad
\mu_2(t)=t+2-\frac1{t+1}+O(e^{-cn}).
\]
Monotonicity first locates both maxima in that fixed-width interval, and then yields
\[
t_V=n-\tfrac12+O(e^{-cn}),\quad
2t_H+2-\frac1{t_H+1}=2n-1+O(e^{-cn}).
\]
Expanding the latter equation proves the displayed formula for \(t_H\).

At any common radius, exact cancellation of the factorial and monomial factors gives
\[
\frac{\mathcal D_H(n,t)}{\mathcal D_V(n,t)}
=\left(\frac{n^2S_0(t)}{4S_2(t)}\right)^n.
\]
At \(t=t_V\), its product by \(4^n\) tends to \(1\), because \(S_2(t_V)/S_0(t_V)=t_V^2+t_V+O(e^{-cn}n^2)=n^2-\tfrac14+o(1)\). Finally, for every fixed real \(s\), the log-determinant increment satisfies
\[
\log\mathcal D_H(n,t_V+s)-\log\mathcal D_H(n,t_V)
\longrightarrow -2s-s^2,
\]
uniformly for bounded \(s\). Since \(t_H-t_V\to-1\), this increment at the maximizer tends to \(1\). Multiplying the exact common-radius ratio by this improvement yields \(4^n\mathcal D_H(n,t_H)/\mathcal D_V(n,t_V)\to e\), as claimed.

## Verification

The included `verify.py` independently constructs the finite Fock evaluation and derivative matrices, evaluates their determinant numerically, checks the exact confluent determinant at perturbed nonuniform angles, verifies each regular-polygon two-by-two spectral block, solves both strict radial equations, and tracks the rescaled asymptotic ratio. The verifier reports 45 passing tests, largest direct algebraic discrepancy below \(2.2\times10^{-14}\), and rescaled ratios approaching \(e\) through \(n=160\). These finite experiments corroborate but do not prove the asymptotic statement; the proof above supplies the infinite-order argument.

## Relationship to prior work

Escudero, Haimi, and Romero (first arXiv posting 2020-04-27) characterize multiple sampling and interpolation with derivatives in weighted infinite-dimensional Fock spaces through Beurling densities. Their theorems do not state this finite-degree, common-circle exact D-optimal design, its block spectrum, or the exponential comparison with distinct value-only samples. Gröchenig and Ortega-Cerdà (first arXiv posting 2021-09-24) relate polynomial Fock sampling to Marcinkiewicz–Zygmund families, also without this finite Hermite determinant classification. Classical confluent Vandermonde determinants and roots-of-unity Fekete bounds are essential prior tools, not claimed as discoveries. A previously obtained value-only circular finite Fock design supplies the comparator optimum; the present contribution is the co-located jet classification and the sharp \(e4^{-n}\) volume ratio, neither implied by that value-only case without analysis of normalized derivative rows.

## Limitations

Only the normalized, fixed-total-count, one-common-circle Gaussian-polynomial model is analyzed. The asymptotic factor concerns **determinant of the squared measurement matrix**, not spectral condition number or noisy minimax reconstruction risk. Distinct angular nodes are required; colliding nodes make the Hermite matrix singular. The novelty assessment is best-knowledge and may be affected by an older unindexed exact design formula for confluent Vandermonde matrices. Independent scientific validation is not included.

## References

1. L. A. Escudero, A. Haimi, J. L. Romero, *Multiple sampling and interpolation in weighted Fock spaces of entire functions*, arXiv:2004.12922 (first posted 2020-04-27); doi:10.1007/s11785-020-01065-4.
2. K. Gröchenig, J. Ortega-Cerdà, *Marcinkiewicz–Zygmund inequalities for polynomials in Fock space*, arXiv:2109.11825 (first posted 2021-09-24); doi:10.1007/s00209-022-03087-4.
3. Classical confluent Vandermonde determinant, Hadamard determinant inequality, Newton identities, and Poisson exponential-tail estimates (standard tools; no novelty claimed).

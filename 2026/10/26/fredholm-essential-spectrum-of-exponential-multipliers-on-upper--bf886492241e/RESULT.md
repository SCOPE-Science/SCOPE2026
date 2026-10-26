# Fredholm essential spectrum of exponential multipliers on upper-half-plane Hardy–Sobolev spaces

## Finding

For every real \(a>0\), integer \(n\ge0\), and exponent \(1\le p\le\infty\), define
\[
H_n^p(\mathbb C^+)=\{F\in H(\mathbb C^+):F^{(j)}\in H^p(\mathbb C^+)\text{ for }0\le j\le n\},
\qquad \|F\|_{H_n^p}=\sum_{j=0}^n\|F^{(j)}\|_{H^p}.
\]
The operator \(M_aF(z)=e^{iaz}F(z)\) is bounded on this space, and its Fredholm essential spectrum is
\[
\sigma_{\mathrm{ess}}^{F}(M_a)=\{\lambda\in\mathbb C:M_a-\lambda I\text{ is not Fredholm}\}=\overline{\mathbb D}.
\]
Thus every point of the ordinary spectral disk is non-Fredholm, not only its boundary.

## Assumptions and scope

Here \(\mathbb C^+=\{z\in\mathbb C:\operatorname{Im}z>0\}\), \(H^p(\mathbb C^+)\) is the classical half-plane Hardy space, and Fredholm means bounded with closed range and finite-dimensional kernel and cokernel. The claim uses the derivative-defined Hardy–Sobolev norm above, including the endpoint exponents \(p=1\) and \(p=\infty\). No result is asserted for arbitrary multiplier symbols or for other Hardy–Sobolev norms.

## Proof

Put \(\theta(z)=e^{iaz}\). Since \(|\theta(x+iy)|=e^{-ay}\le1\) and \(\theta^{(r)}=(ia)^r\theta\), Leibniz's rule gives
\[
(\theta F)^{(k)}=\sum_{j=0}^k\binom{k}{j}(ia)^{k-j}\theta F^{(j)}.
\]
Multiplication by \(\theta\) is contractive on each \(H^p(\mathbb C^+)\), so this formula proves boundedness on \(H_n^p(\mathbb C^+)\).

If \(|\lambda|>1\), then \(|\theta(z)-\lambda|\ge |\lambda|-1>0\). The function \((\theta-\lambda)^{-1}\) and all its derivatives are bounded and holomorphic on \(\mathbb C^+\). Applying Leibniz's rule again shows that multiplication by this reciprocal is bounded on \(H_n^p\). Hence \(M_a-\lambda I\) is invertible, and \(\lambda\notin\sigma_{\mathrm{ess}}^{F}(M_a)\).

Now fix \(0<|\lambda|<1\), write \(\lambda=\rho e^{i\phi}\), and choose a fixed argument \(\phi\). The equation \(e^{iaz}=\lambda\) has the infinitely many distinct solutions
\[
z_k=\frac{\phi+2\pi k}{a}+i\frac{-\log\rho}{a},\qquad k\in\mathbb Z,
\]
all in \(\mathbb C^+\). Every function in the range of \(M_a-\lambda I\) vanishes at each \(z_k\).

For any finite selection of \(N\) such zeros, the corresponding evaluation map from \(H_n^p\) onto \(\mathbb C^N\) is surjective: given prescribed values, interpolate them by a polynomial \(P\) of degree at most \(N-1\) and use \(F(z)=P(z)/(z+i)^{N+n+1}\). This rational function is holomorphic on \(\mathbb C^+\), and its derivatives through order \(n\) have boundary decay sufficient to lie in every \(H^p\), including \(H^\infty\). Consequently, the common kernel of those evaluations is a closed subspace of codimension \(N\). The range of \(M_a-\lambda I\) lies in that subspace for every \(N\); it therefore cannot be both closed and finite-codimensional. Thus \(M_a-\lambda I\) is not Fredholm for every \(0<|\lambda|<1\).

Let \(|\lambda|=1\), and choose \(x\in\mathbb R\) with \(e^{iax}=\lambda\). For \(\varepsilon>0\), use the analytic rational test function
\[
F_\varepsilon(z)=\frac{c_\varepsilon}{(z-x+i\varepsilon)^2},
\]
where \(c_\varepsilon\) is chosen so that \(\|F_\varepsilon^{(n)}\|_{H^p}=1\). Scaling of the boundary integrals gives \(|c_\varepsilon|\asymp\varepsilon^{n+2-1/p}\) for finite \(p\), and \(|c_\varepsilon|\asymp\varepsilon^{n+2}\) for \(p=\infty\). Hence \(\|F_\varepsilon^{(j)}\|_{H^p}=O(\varepsilon^{n-j})\) for \(j<n\), and \(\|F_\varepsilon\|_{H_n^p}\) stays bounded away from zero and infinity.

On the boundary, \(|e^{iat}-\lambda|\le\min\{2,a|t-x|\}\). Applying this bound to each derivative of \((\theta-\lambda)F_\varepsilon\), and using the same scaling, shows that \(\|(\theta-\lambda)F_\varepsilon\|_{H_n^p}\to0\). At the endpoint \(p=1\), the zeroth-derivative estimate may include the factor \(\log(1/\varepsilon)\), but it is multiplied by a positive power of \(\varepsilon\), so it still tends to zero. Since multiplication by the nonzero analytic function \(\theta-\lambda\) is injective, a Fredholm operator \(M_a-\lambda I\) would have closed range and be bounded below. These test functions contradict that requirement. Therefore every \(|\lambda|=1\) is also in the Fredholm essential spectrum.

The Fredholm essential spectrum is closed. Since it contains every nonzero point of \(\mathbb D\) and the entire unit circle, it contains \(0\) as well. Together with invertibility for \(|\lambda|>1\), this proves \(\sigma_{\mathrm{ess}}^{F}(M_a)=\overline{\mathbb D}\).

## Verification

The proof has three independent components: boundedness of \(M_a\) from the Leibniz formula; infinite codimension of the range for nonzero interior spectral parameters; and normalized approximate null vectors for boundary parameters. The reciprocal multiplier excludes all parameters outside the closed disk. The proof is uniform in \(n\ge0\) and covers \(1\le p\le\infty\); it uses neither finite numerical experiments nor an unproved infinite enumeration.

## Relationship to prior work

Liang, Li, and Qian establish the derivative-defined spaces \(H_n^p(\mathbb C^+)\), a Paley–Wiener model for \(p=2\), the ordinary spectrum formula for multiplication operators, and the rigidity that a compact multiplication operator must be zero. The inspected paper does not give the Fredholm essential spectrum of the exponential multiplier considered here. Cao, He, and Zhu study essential spectra and Fredholmness for multipliers on Hilbert Hardy–Sobolev spaces over the unit ball. That is a close Hilbert-space analogue, but it does not establish the present all-\(p\) statement on the derivative-defined upper-half-plane scale. The new claim is the explicit Fredholm classification for \(M_a\) across this Banach range, proved by its zero lattice and boundary-localized test functions.

## Limitations

This result concerns only the symbol \(e^{iaz}\) with \(a>0\). It does not characterize Fredholmness for a general \(\psi\in\operatorname{Mult}(H_n^p)\), compute indices for other symbols, or settle whether the full Hilbert-space boundary-cluster formula extends to all Banach exponents. The literature search is bounded; a broader theorem for this exact Banach scale could reduce the originality claim.

## References

1. H. Liang, H. Li, and T. Qian, “Banach Hardy–Sobolev Spaces on the Upper Half-plane and Operator Theory,” arXiv:2603.13983 (first public version, 2026-03-14).
2. G. Cao, L. He, and K. Zhu, “Spectral Theory of Multiplication Operators on Hardy–Sobolev Spaces,” arXiv:1709.02047 (2017).
3. S. Elliott and M. T. Jury, “Composition operators on Hardy spaces of a half-plane,” *Bulletin of the London Mathematical Society* 44 (2012), 489–495, DOI: 10.1112/blms/bdr110.

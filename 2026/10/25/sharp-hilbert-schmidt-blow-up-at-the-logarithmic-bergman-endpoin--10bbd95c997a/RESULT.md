# Sharp Hilbert–Schmidt blow-up at the logarithmic Bergman endpoint

## Finding

Let \(dA=dx\,dy/\pi\) on the unit disk, and let \(A^2_{\log^\alpha}\) be the analytic Hilbert space with norm
\[
\|f\|_\alpha^2=\int_{\mathbb D}|f(z)|^2\left(\log\frac{e}{1-|z|^2}\right)^\alpha dA(z).
\]
For the coefficient Hilbert matrix \(\mathcal H\), defined by \((\mathcal H a)_m=\sum_{k\ge0}a_k/(m+k+1)\), mapping this space to unweighted \(A^2\), set
\[
v_k(\alpha)=\int_0^1t^k\left(\log\frac{e}{1-t}\right)^\alpha dt,
\qquad S_k=\sum_{m\ge0}\frac1{(m+1)(m+k+1)^2}.
\]
Its exact squared Hilbert–Schmidt norm (allowing \(+\infty\)) is
\[
\boxed{\|\mathcal H\|_{\mathcal S_2}^2=\sum_{k=0}^\infty\frac{S_k}{v_k(\alpha)}.}
\]
The summands have the explicit harmonic-number formula
\[
S_0=\zeta(3),\qquad S_k=\frac{H_k}{k^2}-\frac{\zeta(2)-H_k^{(2)}}{k}\quad(k\ge1).
\]
The exact threshold and sharp one-sided growth law are
\[
\boxed{\mathcal H\in\mathcal S_2\iff\alpha>2,\qquad
\|\mathcal H\|_{\mathcal S_2}^2=\frac1{\alpha-2}+O(1)\quad(\alpha\downarrow2).}
\]
The coefficient of the divergence is exactly one for the stated normalization.

## Assumptions and scope

The logarithm is natural; both Bergman spaces use normalized disk area. The domain norm is as displayed for every real \(\alpha\), and the theorem concerns the coefficient Hilbert matrix wherever its Hilbert–Schmidt sum makes sense. All eigenvalue and trace statements refer to the map between these **two distinct** Hilbert spaces. The convergence claim requires \(\alpha>2\), which is precisely the range where the series converges; at \(\alpha=2\) the operator is known to be bounded but is not Hilbert–Schmidt.

## Proof

**Monomial diagonalization.** Angular integration gives \(\|\sum_{k\ge0}a_kz^k\|_\alpha^2=\sum_{k\ge0}|a_k|^2v_k(\alpha)\), and \(\|\sum_{m\ge0}b_mz^m\|_{A^2}^2=\sum_{m\ge0}|b_m|^2/(m+1)\). In their orthonormal monomial bases the matrix of \(\mathcal H\) has entries
\[
B_{m,k}(\alpha)=\frac1{(m+k+1)\sqrt{(m+1)v_k(\alpha)}}.
\]
Summing \(|B_{m,k}|^2\) over all nonnegative \(m,k\) gives the stated exact Hilbert–Schmidt series by Tonelli's theorem, even when it diverges.

**Explicit inner sum.** For \(k\ge1\), writing \(n=m+1\) and using partial fractions,
\[
\frac1{n(n+k)^2}=\frac1{k^2}\left(\frac1n-\frac1{n+k}\right)-\frac1k\frac1{(n+k)^2}.
\]
Summation for \(n\ge1\) yields \(S_k=H_k/k^2-[\zeta(2)-H_k^{(2)}]/k\). At \(k=0\), \(S_0=\sum_{n\ge1}n^{-3}=\zeta(3)\). Since \(H_k=\log k+\gamma+O(k^{-1})\) and \(\zeta(2)-H_k^{(2)}=k^{-1}+O(k^{-2})\),
\[
S_k=\frac{\log k+\gamma-1+O(k^{-1})}{k^2}.
\]

**Uniform moment estimate.** For \(2\le\alpha\le3\) and \(k\to\infty\), set \(s=k(1-t)\) in \(v_k(\alpha)\). Splitting at \(s=k^{1/2}\) and using the exponentially decaying factor \((1-s/k)^k\), dominated comparison with \(e^{-s}\) gives, uniformly in this compact range of \(\alpha\),
\[
v_k(\alpha)=\frac{(\log k)^\alpha}{k}\left(1+O((\log k)^{-1})\right).
\]
Indeed \(\log(e/(1-t))=\log k+1-\log s\); integration against \(e^{-s}\,ds\) has uniformly finite first and second logarithmic moments. The part \(s>k^{1/2}\) is exponentially negligible. The same estimate with \(\alpha\) fixed holds for every real \(\alpha\).

Consequently, uniformly for \(2\le\alpha\le3\),
\[
\frac{S_k}{v_k(\alpha)}=\frac1{k(\log k)^{\alpha-1}}+O\!\left(\frac1{k(\log k)^\alpha}\right).
\]
The error series converges uniformly on the given parameter interval. Integral comparison gives
\[
\sum_{k\ge3}\frac1{k(\log k)^{\alpha-1}}
=\frac1{\alpha-2}+O(1)\qquad(\alpha\downarrow2).
\]
This proves the coefficient-one blow-up, and shows divergence at \(\alpha=2\). For any fixed \(\alpha>2\), the same asymptotic gives convergence. For \(\alpha<2\), the leading term has exponent at most one and diverges. Thus the exact Schatten-two phase diagram follows.

## Verification

The matrix normalization comes directly from orthogonal monomials. The inner series was independently reduced by the displayed partial-fraction identity and can be checked at \(k=1\), where \(S_1=2-\zeta(2)\). The uniform asymptotic proof bounds the sum of errors by a convergent logarithmic series, so the leading constant is not inferred from numerical fitting. This is a fully analytic infinite-dimensional proof; no finite truncation is treated as exhaustive.

## Relationship to prior work

Norrbo (2026) established boundedness of \(\mathcal H:A^2_{\log^2}\to A^2\), together with failure below the threshold. Published subsequent results establish the compactness trichotomy and an exact essential norm of two at the critical exponent. They are credited as prior work. Neither the inspected compactness proof nor the inspected essential-norm proof computes the \(\mathcal S_2\) trace series for \(\alpha>2\) or its sharp divergent coefficient. The present statement refines the supercritical compact regime by a trace-ideal invariant rather than repeating that phase diagram.

## Limitations

The result determines Hilbert–Schmidt membership and the blow-up of its squared norm, not the trace norm, individual singular values, or arbitrary Schatten exponents. The exact coefficient depends on the explicitly fixed norm and area normalization. Earlier literature may contain implicit variants of the summation argument; mathematical priority remains subject to independent review.

## References

1. D. Norrbo, *The Hilbert matrix operator into the Bergman space*, arXiv:2610.00252v1 (first publicly available September 23, 2026).
2. *Compactness phase transition for the logarithmic Hilbert matrix endpoint*, published-finding corpus (2026), record a9d8a0e8b341.
3. *Exact essential norm at the logarithmic Bergman endpoint*, published-finding corpus (2026), record 5c93039df7cd.

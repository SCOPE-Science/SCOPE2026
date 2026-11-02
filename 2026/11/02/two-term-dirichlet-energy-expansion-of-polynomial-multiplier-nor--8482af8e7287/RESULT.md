# Two-term Dirichlet-energy expansion of polynomial multiplier norms at a degenerate kernel

## Finding

For any **fixed, nonconstant** complex polynomial \(p(z)=\sum_{j=0}^d p_jz^j\), put
\[
D(p)=\sum_{j=1}^d j|p_j|^2>0,\qquad H_0=0,\quad H_j=\sum_{r=1}^j\frac1r,
\]
and
\[
C(p)=|p_0|^2-\sum_{j=1}^d jH_{j-1}|p_j|^2
+\frac1{D(p)}\sum_{n=1}^d\frac1n
\left|\sum_{m=n}^d m p_m\overline{p_{m-n}}\right|^2.
\]
The exact two-term singular-limit law is
\[
\boxed{\|M_p\|_{\mathcal H_a\to\mathcal H_a}^2=\frac{D(p)}a+C(p)+O_p(a),\qquad a\downarrow0.}
\]
In particular \(a\|M_p\|^2\to D(p)\), the usual Dirichlet energy of the polynomial (with normalized area). The second term captures interactions between the nonconstant coefficients and the constant coefficient. For example, \(p(z)=z^2\) gives \(\|M_p\|^2=2/a-2+O(a)\), whereas \(p(z)=1+z^2\) gives \(\|M_p\|^2=2/a+O(a)\). The first term alone cannot distinguish them.

## Assumptions and scope

Work over the complex disc \(\mathbb D\). For \(0<a<1\), let \(\mathcal H_a\) be the analytic reproducing-kernel Hilbert space with kernel
\[K_a(z,w)=(1-z\overline w)^{-a}.\]
Its orthonormal basis is \(e_n(z)=\sqrt{c_n(a)}z^n\), with \(c_0(a)=1\) and \(c_n(a)=(a)_n/n!\). The multiplier \(M_p f=pf\) is bounded for every fixed polynomial and every \(a>0\). The parameter \(a\) is real and tends to zero through positive values. Constants implied by \(O_p(a)\) depend on the fixed polynomial, not on \(a\). We make no uniform-in-degree assertion.

## Proof

Identify \(\mathcal H_a\) with \(\ell^2(\mathbb N_0)\) using the orthonormal basis above. Then
\[
M_p e_n=\sum_{j=0}^d p_j\sqrt{\frac{c_n(a)}{c_{n+j}(a)}}\,e_{n+j}.
\]
For \(n\ge1\), and \(0<a\le a_0<1\), every weight ratio in this finite band is uniformly bounded and differs in operator norm by \(O_p(a)\) from its limit \(\sqrt{(n+j)/n}\). Indeed, for each fixed \(j\), this ratio is the square root of \(\prod_{r=0}^{j-1}(n+1+r)/(n+a+r)\), and its derivative is uniformly bounded over all \(n\ge1\).

Split the basis into \(\mathbb Ce_0\oplus\overline{\operatorname{span}}\{e_n:n\ge1}\). Since multiplication never lowers degree,
\[
M_p=\begin{pmatrix}p_0&0\\ a^{-1/2}v(a)&B(a)\end{pmatrix},\qquad
v_j(a)=p_j\sqrt{a/c_j(a)}\ (1\le j\le d),
\]
where \(B(a)\to B_0\) in operator norm at rate \(O_p(a)\); \(B_0\) has entries \((B_0)_{n+j,n}=p_j\sqrt{(n+j)/n}\), for \(n\ge1\). Define \(v_0=(\sqrt j\,p_j)_{j\ge1}\), with zeros beyond \(d\). The expansion
\[
\frac{a}{c_j(a)}=j\prod_{r=1}^{j-1}(1+a/r)^{-1}=j(1-aH_{j-1}+O_p(a^2))
\]
gives
\[
\|v(a)\|^2=D(p)-a\sum_{j=1}^d jH_{j-1}|p_j|^2+O_p(a^2),
\quad v(a)=v_0+O_p(a).
\]
The operator \(B(a)\) stays uniformly bounded, while the upper-left entry of \(M_p^*M_p\) grows like \(D(p)/a\). For sufficiently small \(a\), the largest spectral value \(\lambda(a)=\|M_p\|^2\) lies above \(\|B(a)\|^2\); the Schur-complement eigenvalue equation is
\[
\lambda=\frac{\|v(a)\|^2}a+|p_0|^2+
\frac1a\langle B(a)^*v(a),(\lambda-B(a)^*B(a))^{-1}B(a)^*v(a)\rangle.
\]
Rank-one dominance first yields \(\lambda=D(p)/a+O_p(1)\). Expanding the resolvent uniformly in operator norm, \((\lambda-B^*B)^{-1}=\lambda^{-1}I+O_p(a^2)\), gives
\[
\lambda=\frac{D(p)}a-\sum_{j=1}^d jH_{j-1}|p_j|^2+|p_0|^2+
\frac{\|B_0^*v_0\|^2}{D(p)}+O_p(a).
\]
Finally direct matrix multiplication, without infinite summation, shows
\[
(B_0^*v_0)_n=\frac1{\sqrt n}\sum_{m=n}^d m p_m\overline{p_{m-n}},\quad 1\le n\le d,
\]
and the vector is zero beyond \(d\). Substitution proves the asserted finite formula. This analytic argument applies to the infinite operator, not just a truncation.

## Verification

The standalone script `CHECKER.py` verifies the coefficient formula for multiple complex and real polynomials, constructs finite-section multiplier matrices directly from \(c_n(a)\), and reports errors in \(\|M_p\|^2-D(p)/a-C(p)\) as \(a\downarrow0\). Finite sections are diagnostics, not proof of the infinite-dimensional assertion. The \(O_p(a)\) bound follows instead from the explicit uniform weight-ratio and resolvent estimates in the proof. In the direct numerical checks, all tested discrepancies decreased proportionally to \(a\).

## Relationship to prior work

Fu, Guo and Yan (2024) introduced a coanalytic model for logarithmic Hardy-type operators using weighted Bergman/Dirichlet spaces. Monsalve-López and Seco (2025), Theorem 1.5, determine the full spectral picture for \(M_{c-z}^*M_{c-z}\) (linear symbols) on the corresponding spaces. In particular our degree-one specialization is already implied by that stronger result and **is not claimed as original**. Their section 7(b) specifically names degrees \(d\ge2\) as a prospective extension, rather than supplying general polynomial spectra. The claim here is a two-term, all-degrees, small-kernel-exponent asymptotic with explicit finite correction, not a full spectral classification at fixed exponent.

## Limitations

The polynomial and its degree are fixed as \(a\downarrow0\). No uniform degree estimates, full finite-exponent spectrum, exact fixed-exponent norm for degree at least two, or extensions to arbitrary analytic multipliers are asserted. The verification calculations do not by themselves establish the asymptotic. A general unpublished operator-perturbation formulation might imply the result; no independent mathematical audit has been performed.

## References

1. X. Fu, K. Guo, F. Yan, *Coanalytic models for Hardy-type operators*, Science China Mathematics 67 (2024), 2771–2788; first published online 2024-08-26; DOI 10.1007/s11425-023-2192-2.
2. M. Monsalve-López, D. Seco, *Towards spectral descriptions of cyclic functions*, Annals of Functional Analysis (2025), Theorem 1.5 and Section 7(b); DOI 10.1007/s43034-025-00446-0.

# High-order origin-parity crossover for photon-subtracted squeezed thermal light

## Finding

Fix a squeezing amplitude \(r>0\) and a thermal seed population \(\nu\geq0\). Let \(\rho_{\nu,r}=S(r)\rho_{\mathrm{th}}(\nu)S(r)^\dagger\), with squeezed quadrature variances
\[
 v=(\nu+\tfrac12)e^{-2r},\qquad w=(\nu+\tfrac12)e^{2r}.
\]
For each integer \(m\geq1\), define the normalized ideal \(m\)-photon-subtracted state and its number parity by
\[
 \rho_m=\frac{a^m\rho_{\nu,r}(a^\dagger)^m}{\operatorname{Tr}[(a^\dagger)^m a^m\rho_{\nu,r}]},\qquad
 \Pi_m(\nu,r)=\operatorname{Tr}[(-1)^{a^\dagger a}\rho_m].
\]
We adopt the convention \(W_m(0)=2\Pi_m/\pi\) for the phase-space Wigner value at the origin. Suppose \(v<\tfrac12\); the domain includes the thermal threshold \(\nu_*=\sinh^2r\). Write
\[
 R_-(\nu,r)=\frac{\tfrac12-v}{2v(w-\tfrac12)},\qquad
 R_+(\nu,r)=\frac{1}{2w},\qquad
 R_g=\sqrt{R_-R_+}.
\]
For every fixed \(\nu>0\) in this domain the following **sharp asymptotic laws, including their multiplicative constants**, hold as \(m\to\infty\):
\[
 \Pi_m\sim
 \begin{cases}
 (-1)^mR_-^{m+1/2}, &0<\nu<\nu_*,\\
 R_+^{m+1/2}, &\nu_*<\nu<\tfrac12(e^{2r}-1).
 \end{cases}
\]
At \(\nu=\nu_*\) the odd parities vanish **exactly**; for even \(m\to\infty\),
\[
 \Pi_m\sim 2R_*^{m+1/2},\qquad R_*=\frac{2}{1+e^{4r}}.
\]
Moreover, at any fixed real \(s\), along even or odd integers \(m\to\infty\) with \(\nu_m=\nu_*+s/m\), the **uniform thermal boundary-layer law** is
\[
 \lim_{m\to\infty}\frac{\Pi_m(\nu_m,r)}{R_g(\nu_m,r)^{m+1/2}}
 =\begin{cases}
 2\cosh\!\left(\dfrac{2s}{\sinh(2r)}\right),&m\text{ even},\\
 2\sinh\!\left(\dfrac{2s}{\sinh(2r)}\right),&m\text{ odd}.
 \end{cases}
\]
In particular, the thermal crossover width is of order \(1/m\), while the origin-parity contrast decays exponentially with \(m\) at every fixed strictly positive thermal population in the stated domain. The theorem gives neither an integrated Wigner-negative volume nor a finite-sample discrimination bound.

## Assumptions and scope

The mode satisfies \([a,a^\dagger]=1\), with number basis \(\{|n\rangle:n\geq0\}\). The thermal density operator has diagonal weights \(\nu^n/(1+\nu)^{n+1}\), and \(S(r)\) is a centered single-mode squeezing unitary with vacuum variances \((e^{-2r}/2,e^{2r}/2)\). The subtraction channel is the ideal trace-decreasing filter \(\rho\mapsto a^m\rho(a^\dagger)^m\), conditional on success. The denominator is finite and positive at every finite \(m\), since the squeezed thermal distribution has arbitrarily high occupied number states when \(r>0\). No detector inefficiency or postselection success rate is included.

The displayed asymptotics require \(r>0\), \(0<\nu<(e^{2r}-1)/2\). For the pure squeezed vacuum boundary \(\nu=0\), parity is exactly \(\Pi_m=(-1)^m\), without exponential contrast loss. At the threshold \(\nu_*=\sinh^2r\), the strict inequality \(v<1/2\) holds because \(e^{-2r}\cosh(2r)<1\).

## Proof

**1. Known generating function and normalized parity.** Set
\[
 G(z)=\operatorname{Tr}(\rho_{\nu,r}z^{a^\dagger a})
 =\left[(v+\tfrac12+(\tfrac12-v)z)(w+\tfrac12+(\tfrac12-w)z)\right]^{-1/2}.
\]
For \(0<z<1\), the normalized operator \((1-z)z^{a^\dagger a}\) is a thermal state of covariance \((1+z)/(2(1-z))\) times the identity. The centered Gaussian overlap formula gives the displayed \(G(z)\), initially in that interval and then by analytic continuation in its connected domain. Differentiating the number series, the output parity after subtraction is
\[
 \Pi_m=\frac{G^{(m)}(-1)}{G^{(m)}(1)}.
\]
Indeed, a seed number state \(|n\rangle\) contributes \((n)_m\) to the success probability and \((-1)^{n-m}(n)_m\) to parity; these are precisely the terms of the derivatives at \(1\) and \(-1\).

**2. Exact sign and thermal threshold.** Around \(z=-1\) write \(z=-1+t\). The generating function becomes
\[
 G(-1+t)=\frac{1}{2\sqrt{vw}}\big[(1+\alpha t)(1-\beta t)\big]^{-1/2}
 =\frac{1}{2\sqrt{vw}}(1+ct-dt^2)^{-1/2},
\]
where \(\alpha=(\tfrac12-v)/(2v)>0\), \(\beta=(w-\tfrac12)/(2w)>0\), \(c=\alpha-\beta=(v+w-4vw)/(4vw)\), and \(d=\alpha\beta>0\). Expanding first in \(ct\) and then in \(dt^2\),
\[
 [t^m](1+ct-dt^2)^{-1/2}
 =\sum_{k+2j=m}\frac{(-1)^k(\tfrac12)_k(k+\tfrac12)_j}{k!j!}\,c^k d^j.
\]
The Pochhammer factors are positive. All nonzero summands have sign \((-\operatorname{sgn}c)^m\), and the normalizing derivative \(G^{(m)}(1)\) is strictly positive. Finally,
\[
 \operatorname{sgn}c=\operatorname{sgn}\big(\cosh(2r)-2\nu-1\big)
 =\operatorname{sgn}(\nu_*-\nu).
\]
Thus every even \(\Pi_m\) is positive, every odd \(\Pi_m\) is negative below \(\nu_*\), zero at \(\nu_*\), and positive above \(\nu_*\). This exact sign statement is an intermediate consequence of an already known generating function; the asymptotic boundary layer is the principal result.

**3. Two-singularity transfer.** For a fixed compact neighborhood of \(\nu_*\) contained within \(\nu>0\), \(v<1/2\), the numerator Taylor function has exactly two real algebraic branch points, at \(t=-1/\alpha\) and \(t=1/\beta\). The denominator Taylor function \(G(1+t)=[(1+bt)(1-et)]^{-1/2}\), with \(b=1/2-v\) and \(e=w-1/2\), has a unique nearest branch point \(t=1/e\), since \(e>b>0\). Standard square-root coefficient transfer, by deforming a Cauchy contour into separate keyhole contours about the two numerator branch points, yields uniformly in that compact neighborhood
\[
 \begin{split}
 [t^m]G(-1+t)={1\over2\sqrt{vw}\sqrt{\pi m}}\bigg[&(-1)^m\alpha^m(1+\beta/\alpha)^{-1/2}\\
 &+\beta^m(1+\alpha/\beta)^{-1/2}
 +O\!\left(\frac{\max(\alpha,\beta)^m}{m}\right)\bigg],
 \end{split}
\]
while
\[
 [t^m]G(1+t)=\frac{e^m}{\sqrt{\pi m}}(1+b/e)^{-1/2}\big(1+O(1/m)\big).
\]
For clarity, the error estimate on the numerator uses the local analytic-factor expansion at each distinct nonzero branch point, with the remaining contour exponentially smaller; separation of those branch points is uniform in the chosen neighborhood even where their absolute moduli agree. The two resulting normalized leading prefactors simplify **exactly** to \(\sqrt{\alpha/e}=\sqrt{R_-}\) and \(\sqrt{\beta/e}=\sqrt{R_+}\). Since \(\alpha/e=R_-\) and \(\beta/e=R_+\), division gives
\[
 \boxed{\Pi_m=(-1)^mR_-^{m+1/2}+R_+^{m+1/2}
 +O\!\left(\frac{\max(R_-,R_+)^{m+1/2}}{m}\right)}.
\]
For fixed \(\nu\neq\nu_*\), one of the two bases is strictly larger, producing the sharp asymptotics above. At equality the odd terms cancel exactly by Step 2; even terms add. For fixed \(\nu>0\), both bases are smaller than one: \(R_+<1\) because \(w>1/2\), and \(2v(w-1/2)-(1/2-v)=2\nu(\nu+1)>0\) implies \(R_-<1\). This proves exponential decay.

**4. Uniform critical scaling.** Define
\[
 \delta(\nu)=\frac12\log\frac{R_-(\nu,r)}{R_+(\nu,r)}.
\]
Direct differentiation gives \(\delta(\nu_*)=0\) and
\[
 \delta'(\nu_*)=-\frac{2}{\sinh(2r)}.
\]
Since \(R_-=R_g e^\delta\), \(R_+=R_g e^{-\delta}\), and \((m+1/2)\delta(\nu_*+s/m)\to-2s/\sinh(2r)\), Step 3 divided by \(R_g^{m+1/2}\) converges to \((-1)^m e^{-2s/\sinh(2r)}+e^{2s/\sinh(2r)}\). This equals the displayed hyperbolic profile for even and odd subsequences. Uniformity of the Step 3 error in a compact neighborhood ensures that the scaling limit is not inferred from fixed-parameter asymptotics alone.

## Verification

The accompanying standalone numerical checker first computes \(G^{(m)}(\pm1)\) from a high-precision Taylor recurrence and independently constructs squeezed thermal density matrices in a truncated number basis. It compares 16 full Fock-space parities, tests 120 exact-sign instances, 12 fixed-parameter large-order prefactors, and 12 double-scaled boundary values. The observed maximum discrepancy on the 16 direct Fock comparisons was approximately \(3.21\times10^{-11}\). Run `python verify.py` with the dependencies in `requirements.txt`. Truncation, floating point, and finite values of \(m\) cannot certify an infinite-order limit; the latter follows from the coefficient-transfer proof.

## Relationship to prior work

Hu, Xu, Wang and Xu (2010, arXiv:1008.5256v1) defined the photon-subtracted squeezed thermal family, evaluated Wigner functions for arbitrary fixed subtraction order and identified the single-photon thermal central-negativity threshold \(\nu_*\). Hu and Zhang (2011, arXiv:1112.0854v1) gave the squeezed thermal photon-number generating function and exact finite-order normalization and distributions in Legendre-polynomial form. Those fixed-order formulas and the basic thermal threshold are not claimed as new here. Hertz and De Bièvre (2022, arXiv:2204.06358v1; revised 2023) considered nonclassicality and Wigner negativity for photon addition and subtraction in Gaussian states, particularly the single-photon regime. The contribution assessed here is the explicit sharp two-branch large-order origin-parity asymptotic with a **uniform** near-threshold \(1/m\) crossover, including its alternating hyperbolic profile; it requires simultaneous control of competing branch singularities rather than substitution of an individual fixed \(m\) into a known Wigner function. It does not assert that the exact finite-order generating function or the existence of thermal threshold is new.

## Limitations

Only the origin value of the Wigner function is controlled; the sign at the origin is sufficient for Wigner negativity when negative, but a positive origin value does not establish global Wigner positivity. The result is specific to one centered mode, ideal conditional subtraction, real squeezing amplitude, the stated quadrature-variance regime, and asymptotic subtraction order. Photon-subtraction success probabilities and the cost of performing large \(m\) are not optimized. The large-order asymptotic is not uniform as \(\nu\to0\), where exact parity \((-1)^m\) takes over. The same exponential conclusion may have physical measurement implications, but no experimental error or sample-complexity theorem is asserted. Publication-priority coverage beyond the checked literature remains a residual risk.

## References

- L.-Y. Hu, X.-X. Xu, Z.-S. Wang and X.-F. Xu, *Photon-subtracted squeezed thermal state: nonclassicality and decoherence*, arXiv:1008.5256v1 (public 2010-08-31), https://arxiv.org/abs/1008.5256.
- L.-Y. Hu and Z.-M. Zhang, *New approach for normalization and photon-number distributions of photon-added (-subtracted) squeezed thermal states*, arXiv:1112.0854v1 (public 2011-12-05), https://arxiv.org/abs/1112.0854.
- A. Hertz and S. De Bièvre, *Decoherence and nonclassicality of photon-added/subtracted multi-mode Gaussian states*, arXiv:2204.06358v1 (public 2022-04-13), https://arxiv.org/abs/2204.06358.

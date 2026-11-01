# Balanced signed logarithmic Weyl law for boundary-chirp Bergman Toeplitz operators

## Finding

Consider the bounded, real-valued radial symbol
\[
u_{c,\vartheta}(z)=\cos\!\left(\frac{c}{1-|z|^2}+\vartheta\right),\qquad c>0,\quad \vartheta\in\mathbb R,
\]
and its Toeplitz compression \(T_{c,\vartheta}=P_\alpha M_{u_{c,\vartheta}}\) on the standard weighted analytic Bergman space \(A^2_\alpha(\mathbb D)\), with \(\alpha>-1\). The symbol is smooth in the open disk but has no radial boundary limit; it attains values arbitrarily close to both \(1\) and \(-1\) along radii approaching the boundary.

**Theorem.** For each fixed triple \((\alpha,c,\vartheta)\) with \(\alpha>-1\), \(c>0\), and \(\vartheta\in\mathbb R\), \(T_{c,\vartheta}\) is a compact self-adjoint operator in every Schatten class \(\mathcal S_p\), \(p>0\), with infinitely many strictly positive and strictly negative eigenvalues. If
\[
N_+(t)=\#\{\lambda\in\sigma(T_{c,\vartheta}):\lambda>t\},\qquad
N_-(t)=\#\{\lambda\in\sigma(T_{c,\vartheta}):\lambda<-t\},
\]
where eigenvalues are counted with multiplicity, then
\[
\boxed{\lim_{t\downarrow0}\frac{N_+(t)}{\log^2(1/t)}
=\lim_{t\downarrow0}\frac{N_-(t)}{\log^2(1/t)}=\frac{1}{4c}.}
\]
The coefficient is independent of both the Bergman weight and the chirp's phase. In particular, if \(\lambda_j^+\) and \(\lambda_j^-\) are the decreasing lists of strictly positive eigenvalues of \(T_{c,\vartheta}\) and \(-T_{c,\vartheta}\), respectively, then
\[
\lim_{j\to\infty}\frac{\log\lambda_j^+}{\sqrt j}
=\lim_{j\to\infty}\frac{\log\lambda_j^-}{\sqrt j}=-2\sqrt c.
\]
The singular values \(s_j(T_{c,\vartheta})\), arranged in decreasing order, obey
\[
\lim_{j\to\infty}\frac{\log s_j(T_{c,\vartheta})}{\sqrt j}=-\sqrt{2c}.
\]
The new assertion is the *two-sided signed logarithmic spectral counting law* and its weight/phase universality, not the classical diagonalization of radial Toeplitz operators or the classical large-parameter special-function expansion used below.

## Assumptions and scope

Normalize area measure on \(\mathbb D\) by \(dA=dx\,dy/\pi\), and set \(dA_\alpha=(\alpha+1)(1-|z|^2)^\alpha dA\). Then \(A_\alpha^2(\mathbb D)\) is the analytic subspace of \(L^2(dA_\alpha)\), and \(P_\alpha\) is the orthogonal projection onto it. The rank-one monomial sectors are indexed by \(n\in\mathbb Z_{\ge0}\). The symbols are bounded and real; no positivity, boundary continuity, analytic-symbol assumption, or norm decay of the symbol is imposed.

The special-function asymptotic below is asserted for fixed \(\alpha\), fixed positive \(c\), and \(n\to\infty\). It is **not** a joint uniform limit as \(c\downarrow0\), \(c\to\infty\), or \(\alpha\to-1\). Each eigenvalue has multiplicity one as a monomial-sector entry, but different sectors may accidentally have the same numerical eigenvalue; the counting functions always include their multiplicities.

## Proof

**1. Exact diagonal reduction.** Rotational invariance makes every monomial an eigenvector. After setting \(t=|z|^2\), the complex moment preceding the real part is
\[
L_n(c)=\frac{1}{B(n+1,\alpha+1)}
\int_0^1 t^n(1-t)^\alpha\exp\!\left(\frac{ic}{1-t}\right)dt,
\qquad \tau_n=\operatorname{Re}(e^{i\vartheta}L_n(c)).
\]
The measure normalization cancels in the ratio. Every \(\tau_n\) is real and \(\lvert\tau_n\rvert\le1\).

The substitution \(s=t/(1-t)\) gives
\[
\int_0^1 t^n(1-t)^\alpha e^{ic/(1-t)}dt
=e^{ic}\int_0^\infty s^n(1+s)^{-n-\alpha-2}e^{ics}ds.
\]
The integrand is absolutely integrable since \(\alpha>-1\), even at the purely imaginary Laplace parameter. By the standard integral representation of Tricomi's confluent hypergeometric function, taking its continuous boundary value from positive real part,
\[
\boxed{L_n(c)=e^{ic}\frac{\Gamma(n+\alpha+2)}{\Gamma(\alpha+1)}
U(n+1,-\alpha,-ic).}
\]
This identity fixes all normalizations and branches. The principal branches of the complex powers and square root are used throughout.

**2. The complex saddle asymptotic.** Put \(a=n+1\), \(z=-ic\), and \(\rho=\alpha/2+1/4\). The established large-first-parameter expansion of \(U(a,b,z)\), DLMF 13.8.11 with \(b=-\alpha\) and fixed \(z\ne0\), starts with
\[
U(a,-\alpha,z)=\frac{2e^{z/2}}{\Gamma(a)}
\left(\frac za\right)^{(\alpha+1)/2}
K_{\alpha+1}(2\sqrt{az})\left(1+O(a^{-1/2})\right).
\]
Here the relative remainder follows by comparing the adjacent-order Bessel term with the leading one and using the fixed-order large-argument asymptotic of \(K_\nu\). The point \(z=-ic\) stays off the negative real branch cut, and \(\operatorname{Re}\sqrt z>0\). Applying
\[
K_\nu(w)=\sqrt{\frac\pi{2w}}e^{-w}\bigl(1+O(|w|^{-1})\bigr),
\qquad w=2\sqrt{az},
\]
and \(\Gamma(a+\alpha+1)/\Gamma(a)=a^{\alpha+1}(1+O(a^{-1}))\), yields
\[
\boxed{
L_n(c)=\frac{\sqrt\pi\,c^\rho}{\Gamma(\alpha+1)}
 a^\rho e^{-\sqrt{2ca}}
 e^{i\left(\sqrt{2ca}+c/2-\pi\rho/2\right)}
\left(1+O_{\alpha,c}(a^{-1/2})\right).
}
\]
In particular, defining \(b_c=\sqrt{2c}\), \(C_{\alpha,c}=\sqrt\pi c^\rho/\Gamma(\alpha+1)>0\), and \(\psi=c/2-\pi\rho/2+\vartheta\),
\[
\tau_n=C_{\alpha,c}a^\rho e^{-b_c\sqrt a}
\left(\cos(b_c\sqrt a+\psi)+O_{\alpha,c}(a^{-1/2})\right).
\]
The error is absolute *inside the final parentheses*. No relative estimate is claimed for the **real** eigenvalue at zeros of the leading cosine. By contrast, the preceding complex moment has a relative error estimate.

**3. Equidistributed phase and sign.** For every fixed \(v\in\mathbb R\setminus\{0\}\), comparison of a sum with its integral gives
\[
\sum_{a=1}^N e^{iv\sqrt a}
=\int_1^N e^{iv\sqrt x}dx+O_v(\sqrt N)=O_v(\sqrt N),
\]
because \(\int_1^N e^{iv\sqrt x}dx=2\int_1^{\sqrt N}y e^{ivy}dy=O_v(\sqrt N)\). Weyl's criterion therefore makes \(b_c\sqrt a+\psi\) equidistributed modulo \(2\pi\) for \(b_c>0\), independently of \(\psi\). Consequently, for any \(0<\delta<1\), the numbers of indices \(a\le N\) with cosine greater than \(\delta\), or less than \(-\delta\), each equal \(\frac{\arccos\delta}{\pi}N+o(N)\). After \(\delta\downarrow0\), each sign occupies natural density one half. The \(O(a^{-1/2})\) error does not alter these densities, by sandwiching signs between cosine thresholds.

**4. A two-sided logarithmic cutoff.** Write \(L=\log(1/t)\), and fix \(\varepsilon>0\). The amplitude estimate implies that, for all sufficiently small \(t\), no \(\lvert\tau_n\rvert>t\) occurs beyond
\[
a>\frac{(1+\varepsilon)^2 L^2}{b_c^2},
\]
because the polynomial factor \(a^\rho\) changes the exponent only by \(O(\log a)\). Conversely, for indices within
\[
a\le\frac{(1-\varepsilon)^2 L^2}{b_c^2}
\]
whose cosine is greater than a fixed \(\delta>0\), the asymptotic lower bound gives \(\tau_n>t\) except for finitely many initial indices. The analogous negative-phase indices give \(\tau_n<-t\). Equidistribution therefore yields
\[
\frac{(1-\varepsilon)^2}{b_c^2}\frac{\arccos\delta}{\pi}
\le\liminf_{t\downarrow0}\frac{N_\pm(t)}{L^2}
\le\limsup_{t\downarrow0}\frac{N_\pm(t)}{L^2}
\le\frac{(1+\varepsilon)^2}{2b_c^2}.
\]
Letting \(\delta\downarrow0\) and \(\varepsilon\downarrow0\) proves the common limit \(1/(2b_c^2)=1/(4c)\). This proof only counts the spectrum of this fixed, explicit operator, rather than claiming a Weyl law for arbitrary oscillatory symbols.

**5. Operator ideals and sorted eigenvalues.** The complex expansion bounds \(\lvert\tau_n\rvert\) by \(C a^\rho e^{-b_c\sqrt a}\) for all sufficiently large \(a\), so \(\tau_n\to0\) and \(\sum_n|\tau_n|^p<\infty\) for every \(p>0\). Thus the diagonal self-adjoint operator is compact and lies in every \(\mathcal S_p\). The signed counting limits imply infinitely many eigenvalues of each sign. Inverting the monotone eigenvalue counts gives the claimed logarithmic limits for \(\lambda_j^+\) and \(\lambda_j^-\); adding the two counts gives \(N_{\mathrm{abs}}(t)\sim\log^2(1/t)/(2c)\), which yields the singular-value limit.

## Verification

`CHECK.py` uses fixed high precision through `mpmath` (version pinned in `requirements.txt`). Its finite checks compare the Tricomi representation with a *separately derived exact exponential-integral finite sum* when \(\alpha\) is a nonnegative integer:
\[
L_n(c)=B(n+1,\alpha+1)^{-1}
\sum_{k=0}^n(-1)^k\binom nk E_{\alpha+k+2}(-ic).
\]
This follows by expanding \((1-u)^n\) after replacing \(u=1-t\). The checker also compares complex asymptotic amplitudes and phases for weights both above and below zero, checks signs away from phase zeros, and illustrates the finite-cutoff phase balance. During verification the checker completed **98 finite assertions** without failure. It does not prove the analytic infinite-series expansion, phase equidistribution, or infinite-dimensional spectral counting. Those steps are supplied in the proof above from established special-function asymptotics and elementary harmonic analysis.

Reproduce with `python -m pip install -r requirements.txt` followed by `python CHECK.py` from the extracted research files. No external data files are required.

## Relationship to prior work

Li and Wang (2026) characterize compactness through vanishing Berezin transforms for general bounded Toeplitz symbols on radial weighted Bergman spaces; this is qualitative and does not prescribe signed eigenvalue counting, all-Schatten membership, or the present explicit boundary chirp. Looi (2026) constructs oscillatory radial Bergman and Fock symbols whose eigenvalues retain macroscopic oscillations, disproving a Berezin-liminf essential-positivity criterion. Looi's Bergman construction oscillates on a logarithmic boundary scale, whereas the symbol here oscillates at reciprocal boundary distance, inducing **root-exponential damping** and a logarithmic-square counting law. His frequency-cutoff distributions do not supply this signed small-eigenvalue asymptotic.

Rozenblum (2010/2011) studies sign-changing radial Toeplitz operators and gives cancellation examples; his disk lower bounds assume compact support, while his rapidly oscillating explicit example is in the Bargmann (whole-plane) setting with different symbol and counting scales. Rozenblum and Vasilevski (2019/2020) establish trace-class criteria for distributional Toeplitz symbols, but do not state a signed counting asymptotic for this bounded radial chirp. DLMF 13.8.11 supplies the pre-existing complex moment asymptotic after a Tricomi reduction: neither that classical analytic fact nor standard monomial diagonalization is claimed as new.

## Limitations

The theorem concerns fixed parameters on weighted analytic disk Bergman spaces, not all radial weights or higher-dimensional balls. It does not determine finite-index signs, exact zero eigenvalues, joint uniformity in the parameter \(c\), or stronger-order corrections to the signed counting law. An older theorem on oscillatory Mellin transforms or rapidly oscillating Toeplitz symbols could imply the present specialization; in particular, the full 2016 article by El-Fallah, Mahzouli, Marrhich and Naqos on eigenvalue decay was unavailable beyond its abstract. Originality is assessed on accessible literature rather than certified definitively. The verification is not an independent mathematical audit.

## References

1. Y. Li and Z. Wang, *Compact Toeplitz operators on radial weighted Bergman spaces*, arXiv:2608.23733, first public 2026-08-24, https://arxiv.org/abs/2608.23733.
2. S. Looi, *The Berezin liminf criterion fails for radial Toeplitz operators*, arXiv:2603.10879, first public 2026-03-11, https://arxiv.org/abs/2603.10879.
3. G. Rozenblum, *On lower eigenvalue bounds for Toeplitz operators with radial symbols in Bergman spaces*, arXiv:1012.3528 (2010), *J. Spectr. Theory* 1 (2011), 299–325, https://arxiv.org/abs/1012.3528.
4. G. Rozenblum and N. Vasilevski, *Trace class Toeplitz operators with singular symbols*, arXiv:1912.05855 (2019), https://arxiv.org/abs/1912.05855.
5. NIST Digital Library of Mathematical Functions, §13.8(iii), formula 13.8.11 (large-first-parameter Tricomi asymptotic), https://dlmf.nist.gov/13.8.E11.

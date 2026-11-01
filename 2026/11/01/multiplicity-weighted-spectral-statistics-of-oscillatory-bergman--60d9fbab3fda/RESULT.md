# Multiplicity-weighted spectral statistics of oscillatory Bergman and Fock Toeplitz operators

## Finding

Let \(d\ge1\) be any fixed integer. Consider the radial Fock Toeplitz symbol \(f_F(z)=\frac12+\cos(2|z|)\) on \(F^2(\mathbb C^d)\), and the radial Bergman Toeplitz symbol
\[
f_{B,d}(z)=c_d+\cos\!\left(\log\frac1{1-|z|^2}\right)
\]
on \(A^2(\mathbb B_d)\), where
\[
a=|\Gamma(1-i)|=\sqrt{\frac\pi{\sinh\pi}},\qquad
r_d=\frac{|\Gamma(d+1+i)|}{\Gamma(d+1)},\qquad
c_d=\frac a2(1+r_d).
\]
These are the previously published counterexample symbols. For each operator, truncate its monomial diagonalization to *all* monomials of total degree at most \(M\). Count eigenvalues with multiplicity, normalize by \(K_d(M)=\binom{M+d}{d}\), and denote the resulting empirical spectral probability measures by \(\mu^F_{d,M}\) and \(\mu^B_{d,M}\).

**(Fock universal law).** In every complex dimension, the full sequence \(\mu^F_{d,M}\) converges weakly as \(M\to\infty\) to the same shifted arcsine law:
\[
\mu^F_{d,M}\Longrightarrow (\theta\mapsto \tfrac12+e^{-1/2}\cos\theta)_\#\frac{d\theta}{2\pi}.
\]
In particular, the proportion of negative eigenvalues converges to the dimension-independent value
\[
\lim_{M\to\infty}\mu^F_{d,M}(( -\infty,0))=\frac1\pi\arccos\left(\frac{\sqrt e}{2}\right).
\]

**(Bergman log-periodic limit family).** Let \(\phi=\arg\Gamma(1-i)\). For every phase \(\theta\in\mathbb R/(2\pi\mathbb Z)\), define
\[
\mathcal B_{d,\theta}=(u\mapsto c_d+a\cos(\theta+\log u))_\#(d u^{d-1}\,du),\quad 0<u<1.
\]
The complete set of subsequential weak limits of \(\mu^B_{d,M}\) is exactly \(\{\mathcal B_{d,\theta}:\theta\in\mathbb R/(2\pi\mathbb Z)\}\). More precisely, whenever \((\log M+\phi)\bmod2\pi\to\theta\), the empirical measure converges to \(\mathcal B_{d,\theta}\), and every phase is achieved along some sequence of integer cutoffs.

Put \(\gamma_d=\arccos(c_d/a)\in(0,\pi/2)\). The set of subsequential limits of the **negative-eigenvalue proportions** is exactly the nondegenerate interval
\[
\boxed{\left[L_d,U_d\right],\qquad
L_d=\frac{e^{2d\gamma_d}-1}{e^{2\pi d}-1},\qquad
U_d=\frac{1-e^{-2d\gamma_d}}{1-e^{-2\pi d}}.}
\]
In particular, the Bergman proportions have no limit for any finite \(d\ge1\), and the dimension-dependent extremal limits satisfy the sharp logarithmic asymptotics
\[
\log L_d=-2\pi d+\sqrt{2d}+O(d^{-1/2}),\qquad
\log(1-U_d)=-\sqrt{2d}+O(d^{-1/2})
\]
as \(d\to\infty\). Thus the lower extreme tends to zero and the upper extreme tends to one, although every symbol retains strictly positive Berezin-transform boundary liminf. These empirical statistics are separate from, and do not strengthen, the previously established counterexample to essential positivity.

## Assumptions and scope

The Fock norm uses Gaussian weight \(\pi^{-d}e^{-|z|^2}\,dV(z)\). The Bergman norm uses normalized volume \(d!\pi^{-d}dV(z)\) on the unit ball. The Toeplitz operator is orthogonal compression of multiplication by the displayed bounded real radial symbol. In both spaces the monomials of total degree \(m\) have eigenvalue \(\lambda_m\) with multiplicity \(w_d(m)=\binom{m+d-1}{d-1}\). The dimension \(d\) stays fixed when the cutoff \(M\) tends to infinity; the final asymptotics concern the subsequent limit \(d\to\infty\) of the *already evaluated* extremal density numbers, not an unproved simultaneous \((d,M)\) limit.

The source establishes for each fixed \(d\) the input eigenvalue asymptotics
\[
\lambda_m^F=\tfrac12+e^{-1/2}\cos(2\sqrt{m+d})+o(1),\qquad
\lambda_m^B=c_d+a\cos(\log(m+d)+\phi)+o(1).
\]
No new eigenvalue asymptotic or Berezin counterexample is claimed here. Weak convergence means convergence against every bounded continuous real test function on \(\mathbb R\); the operator eigenvalues are bounded, so equivalently against continuous functions on a fixed compact interval.

## Proof

**1. Monomial weights and inherited diagonal asymptotics.** Rotation invariance diagonalizes both Toeplitz operators, and stars-and-bars gives exactly \(w_d(m)=\binom{m+d-1}{d-1}\) and \(\sum_{m=0}^M w_d(m)=K_d(M)=\binom{M+d}{d}\). The eigenvalue asymptotics are Proposition 3.8 and Proposition 3.9, using the one-dimensional oscillatory calculation from Proposition 2.3 and Proposition 3.3, respectively, of Looi (arXiv:2603.10879). Their error \(o(1)\) does not affect any normalized weighted empirical integral: for fixed \(\varepsilon>0\), discard the finitely many \(m\) below the source's error threshold, which carry proportion tending to zero, and use uniform continuity of a test function on the common bounded eigenvalue range.

**2. Weighted Fock equidistribution.** For any fixed nonzero integer \(k\), set \(h_k(x)=\exp(2ik\sqrt{x+d})\). Integral comparison using \(\int_1^M|h_k'(x)|dx=O_k(\sqrt M)\) and the substitution \(v=\sqrt{x+d}\) shows
\[
\sum_{m=1}^M h_k(m)=O_k(\sqrt M).
\]
Abel summation with the degree-\((d-1)\) polynomial \(w_d(m)\) yields
\[
\sum_{m=0}^M w_d(m)h_k(m)=O_{k,d}(M^{d-1/2}).
\]
Since \(K_d(M)\sim M^d/d!\), all nonconstant Fourier coefficients of the weighted phases \(2\sqrt{m+d}\bmod2\pi\) tend to zero. The Fourier/Weyl criterion and source asymptotics give the shifted arcsine weak law. Because the limiting arcsine measure assigns no mass to \(0\) and \(0<\sqrt e/2<1\), its negative mass is the Haar fraction of phases with \(\cos\theta<-\sqrt e/2\), namely \(\arccos(\sqrt e/2)/\pi\).

**3. Complete Bergman limit family.** The normalized multiplicity weights satisfy the elementary Riemann-sum limit
\[
\frac1{K_d(M)}\sum_{m=0}^M w_d(m)F\!\left(\frac{m+d}{M}\right)
\longrightarrow \int_0^1d u^{d-1}F(u)\,du
\]
for every continuous \(F\) on \([0,1]\), since \(w_d(m)=m^{d-1}/(d-1)!+O_d((m+1)^{d-2})\) when \(d>1\), with the \(d=1\) constant case direct. For a continuous spectral test function \(g\), the corresponding oscillatory function \(F(u)=g(c_d+a\cos(\theta+\log u))\) is bounded on \((0,1]\) but need not have a limit at zero. Cut the sum and integral at \(u=\delta\); the discarded normalized mass is at most \(O_d(\delta^d)+o(1)\). On \([\delta,1]\) ordinary Riemann sums work uniformly for phases approaching \(\theta\). Sending \(\delta\downarrow0\) proves convergence along the specified phase subsequence. Compactness of the circle supplies a convergent phase subsubsequence from any sequence \(M\to\infty\), so these exhaust all possible weak limits. Conversely choose integers \(M_j\) nearest \(\exp(2\pi j+\theta-\phi)\) to realize any phase.

**4. Exact negative-mass extrema.** The ratio \(r_d<1\) for every finite \(d\), since
\[
r_d=|\Gamma(1+i)|\prod_{j=1}^d\sqrt{1+j^{-2}}
=\exp\!\left(-\tfrac12\sum_{j=d+1}^{\infty}\log(1+j^{-2})\right)<1.
\]
Therefore \(0<c_d<a\), \(\gamma_d=\arccos(c_d/a)\in(0,\pi/2)\), and each limit law gives mass zero to the threshold \(0\). Write \(u=e^{-v}\); then the measure \(d u^{d-1}du\) becomes the exponential law \(d e^{-dv}dv\) on \(v>0\). The inequality \(c_d+a\cos(\theta-v)<0\) selects, modulo \(2\pi\), a single moving arc of length \(2\gamma_d\). The wrapped exponential law on one angular period has density
\[
g_d(v)=\frac{d e^{-dv}}{1-e^{-2\pi d}},\quad 0\le v<2\pi.
\]
For an arc of fixed length \(\ell=2\gamma_d\), the largest wrapped mass is attained by the arc starting at \(v=0\), namely \((1-e^{-d\ell})/(1-e^{-2\pi d})\). The smallest is attained by the arc ending at \(v=2\pi\), namely \((e^{d\ell}-1)/(e^{2\pi d}-1)\). To see these are global extremes, shift an arc whose endpoints avoid the seam: its derivative is the right-end density minus the left-end density, which is strictly negative for non-wrapping arcs and strictly positive while crossing the seam. The continuous phase parameter covers every arc placement. Thus the continuous negative-mass function has full range \([L_d,U_d]\), and weak limit convergence transfers this exactly to empirical negative proportions. The extrema differ strictly because the wrapped exponential is not constant.

**5. Large-d sharp rate.** Euler's product for \(\sinh\pi\) (or the gamma recurrence) gives the convergent product in step 4. Expanding its logarithmic tail yields \(\log r_d=-1/(2d)+O(d^{-2})\). Therefore \(c_d/a=1-1/(4d)+O(d^{-2})\), and \(\gamma_d=(2d)^{-1/2}+O(d^{-3/2})\). Since \(2d\gamma_d=\sqrt{2d}+O(d^{-1/2})\), direct logarithms of the exact expressions for \(L_d\) and \(1-U_d\) give the stated expansions, with exponentially small denominator corrections. This closes the proof for all dimensions and identifies the order of limits.

## Verification

The accompanying `verify.py` uses independent finite weighted sums for the Fock model phases, exact gamma-ratio eigenvalues for the Bergman model, and numerical evaluation of the wrapped-exponential phase masses. It checks normalization, low-dimensional first-moment formulas, and the sharp density extremal formulas. All such tests are finite corroboration; the proof above supplies the infinite-dimensional, all-cutoff and large-d statements. Running the verifier requires Python 3 with NumPy and SciPy installed and prints its actual assertions/count.

## Relationship to prior work

Sam Looi, arXiv:2603.10879 (public March 11, 2026), explicitly constructs the symbols, proves positivity of the Berezin-transform liminf, and computes every required degreewise eigenvalue asymptotic (Propositions 2.3, 3.3, 3.8, 3.9). Those constructions and input asymptotics are NOT new results here. Our additional question is the *multiplicity-weighted asymptotic distribution* of all modes up to degree \(M\), and the resulting complete range and dimension dependence of negative-mode **proportions**. The source's existence of a negative spectral cluster does not determine these averages. Earlier studies of eigenvalue sequences for radial Toeplitz algebras, including Suárez (2008) and Maximenko–Pacheco (2025), concern algebraic/regularity structure rather than the present oscillatory cutoff-distribution classification. The phase analysis uses classical equidistribution and wrapped-exponential elementary methods, acknowledged as mathematical tools rather than novel lemmas.

## Limitations

The results use the specific published symbols and the ordering by total monomial degree; they are not claims about every radial Toeplitz symbol or arbitrary spectral enumerations. The \(d\to\infty\) limit follows after the \(M\to\infty\) limit for fixed \(d\), and no uniform joint regime is asserted. Although searched literature did not reveal an equivalent full weighted counting theorem, implicit overlap in older radial Toeplitz spectral sequence literature cannot be excluded. The calculations are self-reviewed only; no independent scientific audit or external certification is asserted.

## References

1. S. Looi, *Positive Berezin liminf does not imply essential positivity for radial Toeplitz operators on Bergman and Fock spaces*, arXiv:2603.10879 (first public version March 11, 2026), particularly Propositions 2.3, 3.3, 3.8 and 3.9, and Remarks 2.5, 3.7. https://arxiv.org/html/2603.10879v2
2. E. A. Maximenko and C. G. Pacheco, *Toeplitz operators in Bergman space induced by radial measures*, arXiv:2503.23649 (2025). https://arxiv.org/abs/2503.23649
3. D. Suárez, *The eigenvalues of limits of radial Toeplitz operators*, Bull. Lond. Math. Soc. 40 (2008), 631–641, DOI 10.1112/blms/bdn042.

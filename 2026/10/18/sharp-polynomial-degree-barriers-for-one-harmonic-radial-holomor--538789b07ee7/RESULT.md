# Sharp polynomial degree barriers for one-harmonic radial holomorphic intensity inversion

## Finding

For real \(\beta>-1\), integers \(k\ge1\) and \(d\ge k\), consider the radial intensity map
\[
\mathcal R_\beta(P)(e^{i\theta})=\int_0^1 t^\beta |P(te^{i\theta})|^2\,dt
\]
on complex polynomials \(P\) of degree at most \(d\). Restrict the output to a *single nonconstant Fourier harmonic*, with normalized mean:
\[
\mathcal R_\beta(P)(e^{i\theta})=1+2\varepsilon\cos(k\theta+\phi),
\qquad \varepsilon>0,\quad \phi\in\mathbb R.
\]
Then the exact maximum possible amplitude is
\[
\boxed{\varepsilon_*(d,k,\beta)=\frac12\sqrt{1-\frac{k^2}{(2d-k+\beta+1)^2}}.}
\]
Every amplitude \(0<\varepsilon\le\varepsilon_*(d,k,\beta)\) is attainable, for every \(\phi\); no larger amplitude is attainable. Equality holds only for the polynomial
\[
\boxed{P(z)=e^{i\gamma}z^{d-k}\left(\sqrt{\frac{2d-2k+\beta+1}{2}}+e^{i\phi}\sqrt{\frac{2d+\beta+1}{2}}\,z^k\right),\quad \gamma\in\mathbb R.}
\]

For any \(0<\varepsilon<1/2\), the **sharp minimal degree** for exact representation is
\[
\boxed{d_{\min}(\varepsilon,k,\beta)=\max\left\{k,\left\lceil\frac{k/\sqrt{1-4\varepsilon^2}+k-\beta-1}{2}\right\rceil\right\}.}
\]
At \(\varepsilon=0\), a constant polynomial suffices; at \(\varepsilon\ge1/2\), no polynomial can satisfy the normalized target. Put \(\delta=\frac12-\varepsilon\). For fixed \(k,\beta\), as \(\delta\downarrow0\),
\[
 d_{\min}(\varepsilon,k,\beta)=\frac{k}{4\sqrt\delta}+O_{k,\beta}(1).
\]
The original unweighted radial operator corresponds to \(\beta=0\). For example, for \(k=1\), the maximum first-harmonic coefficient among degree-at-most-\(d\) inverses is exactly \(\frac12\sqrt{1-(2d)^{-2}}\).

## Assumptions and scope

The boundary variable lies on \(\mathbb T=\{e^{i\theta}:\theta\in\mathbb R\}\). The measure is exactly \(t^\beta\,dt\) on \([0,1]\), not normalized to total mass one; the output is normalized by requiring the zeroth Fourier coefficient to equal one. Polynomial coefficients may be arbitrary complex numbers. The frequency \(k\) is any positive integer. The degree bound \(d\) is an upper bound, and equality in the amplitude theorem is classified even when the polynomial initially has lower degree. Phase \(\phi\) is arbitrary modulo \(2\pi\).

A moment-form companion lemma also holds: for any finite positive radial measure \(\mu\) with strictly positive moments \(M_j=\int t^j\,d\mu(t)\), the largest amplitude at degree at most \(d\), among outputs with only frequencies \(0,\pm k\) and mean one, is
\[
\max_{0\le m\le d-k}\frac{M_{2m+k}}{2\sqrt{M_{2m}M_{2m+2k}}}.
\]
The sharp power-weight formulas above follow from \(M_j=(j+\beta+1)^{-1}\). No monotonicity in \(m\) is asserted for arbitrary radial measures.

## Proof

Write \(P(z)=\sum_{j=0}^d a_jz^j\), and set \(a_j=0\) outside this range. Expanding the square and integrating termwise gives, for every integer \(0\le\ell\le d\),
\[
\widehat{\mathcal R_\beta(P)}(\ell)
=\sum_{j=0}^{d-\ell}\frac{a_{j+\ell}\overline{a_j}}{2j+\ell+\beta+1}.
\tag{1}
\]
In particular the zeroth coefficient is the nonnegative energy
\[
H_0=\sum_{j=0}^d\frac{|a_j|^2}{2j+\beta+1}.
\tag{2}
\]
For a nonzero polynomial, let \(m\) and \(M\) be the least and greatest indices with nonzero coefficients. The top nonzero Fourier harmonic of its radial intensity is **exactly** \(M-m\): the coefficient at this frequency has the unique summand
\[
\widehat{\mathcal R_\beta(P)}(M-m)=\frac{a_M\overline{a_m}}{m+M+\beta+1}\ne0,
\]
while every higher positive-frequency coefficient vanishes. Thus any nonconstant one-harmonic output at frequency \(k\) forces \(M=m+k\), necessarily \(0\le m\le d-k\). This remains true even if lower harmonics cancel.

For this support diameter, put
\[
X=\frac{|a_m|^2}{2m+\beta+1},\qquad Y=\frac{|a_{m+k}|^2}{2m+2k+\beta+1}.
\]
Equation (2) gives \(1=H_0\ge X+Y\). The single surviving positive Fourier coefficient satisfies
\[
\begin{aligned}
\varepsilon&=\frac{|a_{m+k}a_m|}{2m+k+\beta+1}\\
&=\frac{\sqrt{(2m+\beta+1)(2m+2k+\beta+1)}}{2m+k+\beta+1}\sqrt{XY}\\
&\le\frac12\sqrt{1-\frac{k^2}{(2m+k+\beta+1)^2}},
\end{aligned}
\tag{3}
\]
using \(2\sqrt{XY}\le X+Y\le1\). Since \(\beta>-1\) and \(k\ge1\), the right side of (3) is strictly increasing in \(m\). Therefore \(m\le d-k\) gives the stated sharp upper bound.

For equality, strict monotonicity forces \(m=d-k\). Equality in \(1\ge X+Y\) excludes every interior nonzero coefficient, and equality in the arithmetic-geometric mean inequality gives \(X=Y=1/2\). The magnitudes of the two remaining coefficients and their required phase difference \(\phi\) yield the displayed unique equality family up to one unimodular multiplier. Substitution in (1) confirms attainment.

For an arbitrary \(0<\varepsilon\le\varepsilon_*\), fix \(m=d-k\). Choose \(u\in(0,\pi/4]\) so that \(\sin(2u)=\varepsilon/\varepsilon_*\), and take
\[
P(z)=z^m\big(\sqrt{2m+\beta+1}\cos u+e^{i\phi}\sqrt{2m+2k+\beta+1}\sin u\,z^k\big).
\]
Then its zero-frequency coefficient is \(\cos^2u+\sin^2u=1\), its only positive-frequency coefficient equals \(\varepsilon e^{i\phi}\), and its conjugate is the only negative-frequency coefficient. This proves sufficiency.

The degree condition is now equivalent to
\[
2d-k+\beta+1\ge \frac{k}{\sqrt{1-4\varepsilon^2}},\qquad d\ge k,
\]
and taking the least integer gives the formula for \(d_{\min}\). Since the strict upper bound is below \(1/2\) at every finite \(d\), a target with \(\varepsilon\ge1/2\) is impossible; \(\varepsilon=0\) is generated by a constant. Finally, with \(\delta=1/2-\varepsilon\), \(1-4\varepsilon^2=4\delta(1-\delta)\); inserting this into the degree formula proves \(d_{\min}=k/(4\sqrt\delta)+O_{k,\beta}(1)\).

For the moment companion lemma, replace each denominator in (1) by \(M_{2j+\ell}\). The same unique highest-frequency summand forces support diameter \(k\), and arithmetic-geometric mean bounds its normalized amplitude by the displayed moment ratio. Choosing the two endpoints only, with equal normalized energies, achieves each candidate ratio. Taking their finite maximum proves the claim.

## Verification

A standalone Python checker using exact rational arithmetic exhaustively tested 6,558 integer-coefficient polynomials of exact degrees from one through seven; 112 had exactly one nonconstant harmonic, and every one obeyed the predicted support-diameter rigidity and sharp bound. It also checked 110 exact sharp-amplitude algebra instances across frequency and degree pairs, 336 nontrivial one-harmonic instances under four rational power weights, and 42 independently constructed phase-resolved targets. A non-binomial example, \(P(z)=1+z-2z^2\), produces \(\mathcal R_0(P)(e^{i\theta})=32/15-(4/3)\cos(2\theta)\); the bound applies even though an interior coefficient is present. All finite checks passed. The general assertion is proved by the algebra above; finite tests alone do not certify all degrees or weights.

Run `python3 check_radial_inverse.py` with Python 3 and SymPy installed; its recorded stdout is in `check_output.txt`. No external data is needed for this checker.

## Relationship to prior work

Kot and Pierzchała prove that for the unweighted operator and any \(p>0\), every strictly positive continuous function on the unit circle has a holomorphic Radon preimage. Their proof constructs sequences of high-order polynomial pieces and proves existence, not a sharp *single-polynomial* degree threshold for one-harmonic data. The present result addresses that finite-complexity question exactly for \(p=2\), and also handles every power weight \(t^\beta\). Their related work on circular strictly convex domains likewise concerns general holomorphic existence and lacunary polynomial constructions, not the stated one-variable sharp formula.

Classical Fejér–Riesz factorization represents a nonnegative trigonometric polynomial directly as a boundary squared modulus of an analytic polynomial of the same harmonic degree. The radial averaging in this theorem is a different nonlinear transform: when \(\beta>-1\), a fixed-degree radial intensity has a strict amplitude deficit, even for the simplest positive one-harmonic targets. That distinction explains the divergence of the minimal degree near a target with a boundary zero.

## Limitations

The sharp inverse-degree classification concerns one nonconstant Fourier harmonic, not arbitrary positive boundary data. It addresses exact noiseless boundary values and polynomial degrees, not numerical stability or an algorithm for arbitrary targets. For arbitrary radial measures only the moment maximum is asserted; the explicit closed-form degree threshold requires the power weights above. An equivalent older finite-degree formulation has not been ruled out beyond the searched sources, so priority remains provisional.

## References

1. P. Kot and P. Pierzchała, *The Radon Inversion Problem for Holomorphic Functions in the Unit Disc*, Computational Methods and Function Theory 22 (2022), 135–156. First online 8 May 2021. DOI: 10.1007/s40315-021-00379-4.
2. P. Pierzchała and P. Kot, *Radon Inversion Problem for Holomorphic Functions on Circular, Strictly Convex Domains*, Complex Analysis and Operator Theory 15 (2021). DOI: 10.1007/s11785-021-01130-6.
3. T. T. Georgiou and A. Lindquist, *On a Fejér–Riesz factorization of generalized trigonometric polynomials* (2020), arXiv:2005.11920. Cited solely for contrast with ordinary boundary spectral factorization.

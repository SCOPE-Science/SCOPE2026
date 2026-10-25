# A quartic-edge impurity crossover in a zigzag quantum chain

## Finding
For the self-adjoint next-nearest-neighbor hopping operator on the infinite one-dimensional lattice with first-neighbor hopping one, second-neighbor hopping \(a_\varepsilon=1/4+s\varepsilon^{2/3}>0\), and a single repulsive on-site potential \(\varepsilon>0\), let \(E_b(\varepsilon,s)\) denote its unique bound-state energy above the free band. For every **fixed** \(s\in\mathbb R\),
\[
\lim_{\varepsilon\downarrow0}\frac{E_b(\varepsilon,s)-(2-2a_\varepsilon)}{\varepsilon^{4/3}}=t(s)^2,
\qquad t(s)^2\bigl(t(s)-4s\bigr)=\frac14,
\quad t(s)>\max\{0,4s\}.
\]
There is exactly one such positive solution \(t(s)\). Relative to the **actual** upper free-band edge, the bound-state gap obeys
\[
 E_b(\varepsilon,s)-E_{\max}(a_\varepsilon)
 =\varepsilon^{4/3}\left[t(s)^2-16\bigl(\max\{s,0\}\bigr)^2+o(1)\right],
\]
with strictly positive bracket coefficient for every finite \(s\). At the quartic-edge value \(s=0\), the coefficient is exactly \(2^{-4/3}\). Its two tails are \(t(s)^2\sim1/(16|s|)\) as \(s\to-\infty\) and \(t(s)^2-16s^2\sim1/(8s)\) as \(s\to+\infty\). These tail laws are asymptotics **of the crossover function**; they do not assert a uniform two-parameter expansion outside fixed \(s\).

## Assumptions and scope
On \(\ell^2(\mathbb Z)\), define for each \(\varepsilon>0\) and \(s\in\mathbb R\) with \(a_\varepsilon>0\)
\[
 (H_{\varepsilon,s}\psi)_n=-\psi_{n-1}-\psi_{n+1}-a_\varepsilon(\psi_{n-2}+\psi_{n+2})+\varepsilon\mathbf1_{\{n=0\}}\psi_0.
\]
The free operator \(H_{0,a}\) is the same convolution operator without the on-site term; its Bloch dispersion is
\[
 E_a(k)=-2\cos k-2a\cos(2k),\qquad -\pi\le k\le\pi.
\]
For all \(a>0\), the free spectrum is one compact interval with upper edge
\[
 E_{\max}(a)=\begin{cases}2-2a,&0<a\le1/4,\\ 2a+1/(4a),&a\ge1/4.\end{cases}
\]
The result is for an infinite, translation-invariant background with one positive rank-one on-site defect. It does not include finite chains, complex gain/loss, multiple defects, nonlinear excitations, or a nonzero rescaling of the defect-linked hoppings. The hopping ratio approaches \(1/4\) with a fixed scaled detuning \(s\), while the defect strength tends to zero.

## Proof
**1. Edge and discrete eigenvalue.** Put \(u=1+\cos k\in[0,2]\) and \(\eta=a-1/4\). The exact identity
\[
 E_a(k)=E_\pi+8\eta u-(1+4\eta)u^2,\qquad E_\pi=2-2a
\]
shows that the maximum occurs at \(u=0\) for \(\eta\le0\) and at \(u=4\eta/(1+4\eta)\) for \(\eta>0\). In the latter case
\[
 E_{\max}(a)-E_\pi=\frac{16\eta^2}{1+4\eta}.
\]
For every \(\varepsilon>0\), the rank-one resolvent equation for an eigenvalue \(E>E_{\max}(a)\) is
\[
 1=\varepsilon G_a(E),\qquad G_a(E)=\frac{1}{2\pi}\int_{-\pi}^{\pi}\frac{dk}{E-E_a(k)}.
\]
The function \(G_a\) is positive, continuous and strictly decreasing in \(E\); it approaches zero at infinity and diverges as \(E\downarrow E_{\max}(a)\), since each maximum of the real-analytic dispersion has even order and a nonzero local Fourier weight. Hence there is one and only one \(E_b>E_{\max}(a)\), and the rank-one eigenvalue is simple. This uses the full infinite-lattice resolvent, not a finite-size eigenvalue census.

**2. Critical rescaling.** Fix \(s\). Write \(a=1/4+s\varepsilon^{2/3}\) and try \(E=E_\pi+\varepsilon^{4/3}y\), with \(y>\max\{0,16s^2\}\) if \(s>0\), and \(y>0\) otherwise. Around \(k=\pi\), use \(k=\pi-\varepsilon^{1/3}x\). Since \(u=1-\cos(\varepsilon^{1/3}x)=\varepsilon^{2/3}x^2/2+O(\varepsilon^{4/3}x^4)\),
\[
 E-E_a(k)=\varepsilon^{4/3}\left(y-4sx^2+\frac{x^4}{4}+o(1)\right)
\]
for each fixed \(x\ge0\). For a global domination, set \(w=\varepsilon^{1/3}\) and \(z=(1-\cos(wx))/w^2\) on \(0\le x\le\pi/w\). Then \(2x^2/\pi^2\le z\le x^2/2\), and the **exact** scaled denominator is \(y-8sz+(1+4sw^2)z^2\). On every compact set of \(y\) values strictly above the limiting edge, this denominator is uniformly positive for sufficiently small \(w\), and its reciprocal is bounded by \(C/(1+x^4)\) for a constant depending only on that compact set and \(s\). Thus dominated convergence gives, locally uniformly on such compact \(y\)-sets,
\[
 \lim_{\varepsilon\downarrow0}\varepsilon G_{a_\varepsilon}(E_\pi+\varepsilon^{4/3}y)
 =\frac1\pi\int_0^\infty\frac{dx}{y-4sx^2+x^4/4}
 =\frac{1}{2\sqrt y\sqrt{\sqrt y-4s}}.
\]
For completeness, the integral follows by rescaling the standard elementary quartic integral \(\int_{-\infty}^{\infty}(z^4+bz^2+1)^{-1}dz=\pi/\sqrt{2+b}\) for \(b>-2\). Both the finite resolvent and the limiting function are strictly decreasing in \(y\). The limit diverges as \(y\) approaches the limiting upper edge and tends to zero as \(y\to\infty\). Bracketing the root of \(\varepsilon G=1\) between any two fixed points around the unique limiting root proves convergence without interchanging an eigenvalue limit with an uncontrolled singular integral.

**3. Crossover equation and the band-edge subtraction.** Equating the final integral to one, and setting \(t=\sqrt y\), gives
\[
 t^2(t-4s)=\frac14,\qquad t>\max\{0,4s\}.
\]
On the stated interval the left side is strictly increasing from zero to infinity. Since the exact scaled free-edge shift is zero for \(s\le0\), and equals \(16s^2/(1+4s\varepsilon^{2/3})\) for \(s>0\), subtraction yields the second claim. At \(s=0\), \(t=2^{-2/3}\), giving the quartic-edge coefficient \(2^{-4/3}\). Finally, solving the cubic asymptotically gives \(t\sim1/(4\sqrt{|s|})\) as \(s\to-\infty\), and \(t=4s+1/(64s^2)+o(s^{-2})\) as \(s\to+\infty\), proving the two tail statements.

## Verification
The included standalone `CHECK.py` reconstructs the exact infinite-chain bound-state energy by Fourier-resolvent quadrature and a monotone scalar root search, independently evaluates the crossover cubic, and compares four cases against the top eigenvalue of a 1201-site Dirichlet truncation. Its documented run passed 15 singular-resolvent roots (five scaled detunings and three defect strengths), four independent matrix comparisons, and the critical constant. The maximum relative difference from the fixed-\(s\) limit at the smallest strength \(10^{-4}\) in the five cases was below \(0.017\); this convergence evidence is illustrative and not an infinite-limit proof. The analytical proof above supplies the limiting theorem.

## Relationship to prior work
Stockhofe and Schmelcher, arXiv:1506.01937 (first public version 2015-06-05), derive the next-nearest-neighbor zigzag dispersion and analyze defect scattering and bound-state energies, including the hopping transition at \(a=1/4\) and the single on-site defect case. Those underlying dispersion, bound-state existence, and resolvent mechanisms are not new. The present statement isolates the **simultaneous weak-defect / band-edge-merger scaling regime**, identifies the \(\varepsilon^{4/3}\) exponent with its exact coefficient, and obtains one explicit cubic crossover that distinguishes the unsplit and split-band sides. The continuum quartic point-interaction integral is an equivalent limiting description; its generic algebra is not claimed as independent novelty. Koiller and Brandi (1981) treated next-neighbor impurity states through transfer matrices; only the publisher abstract was accessible, so a historically equivalent specialization cannot be excluded.

## Limitations
The theorem is pointwise for each fixed scaled detuning \(s\); no uniform claim is made as \(|s|\to\infty\) simultaneously with \(\varepsilon\to0\). All coefficients assume first-neighbor hopping normalized to one and a positive on-site impurity; negative impurities bind below a different edge and are not included. It does not characterize wave-packet scattering, disorder, finite-size measurements, or boundary robustness. The exact constants are analytic, whereas numerical comparisons only test finite parameter values. Earlier transfer-matrix literature not available in full leaves an explicit priority risk.

## References
1. J. Stockhofe and P. Schmelcher, *Sub- and supercritical defect scattering in Schrödinger chains with higher-order hopping*, arXiv:1506.01937, original submission 2015-06-05, https://arxiv.org/abs/1506.01937. Relevant complete-text sections: II, IV, VII.
2. B. Koiller and H. S. Brandi, *Localized states in polymeric molecules. I. The transfer matrix for long range interactions*, Theoretica Chimica Acta 60 (1981), 11–17, https://doi.org/10.1007/BF00554383. Publisher abstract inspected; complete text inaccessible.
3. M. Saha, B. K. Agarwalla, M. Kulkarni, and A. Purkayastha, *Arbitrary order transfer matrix exceptional points and Van Hove singularities*, Phys. Rev. B 111 (2025), L041405, https://doi.org/10.1103/PhysRevB.111.L041405. Background only on higher-order band singularities; not a bound-state crossover theorem.

# Quadratic-width Lorentzian transmission spikes and an \(L^p\) crossover in a Robin quantum graph

## Finding
For the two-pendant scale-invariant quantum graph specified below, a weak high-energy Robin phase shift produces a unit-height transmission spike of **quadratic**, rather than linear, phase width. Across one Neumann antiresonance cell, the discrepancy between Robin and Neumann transmission has different dominant mechanisms below and above the sharp exponent \(p=2\).

Put \(\kappa_n=(n+\tfrac12)\pi/\ell\), \(\delta_n=\arctan(a/\kappa_n)\), where \(a>0\), \(\ell>0\), and \(n\to\infty\) ranges over positive integers. Define the cell \(I_n=(\kappa_n-\pi/(2\ell),\,\kappa_n+\pi/(2\ell))\). There is a unique near-central exact Robin transmission resonance \(k_n^*\) with
\[
\ell(k_n^*-\kappa_n)=\frac{\delta_n}{3}+O(\delta_n^3).
\]
Writing \(w_n=2\delta_n^2/27\), the transmission probabilities obey
\[
T^{\rm Rob}\left(k_n^*+\frac{w_nu}{\ell}\right)\longrightarrow\frac1{1+u^2},\qquad
T^{\rm Neu}\left(k_n^*+\frac{w_nu}{\ell}\right)\longrightarrow0
\]
locally uniformly for \(u\in\mathbb R\). Consequently, for every fixed \(\varepsilon\in(0,1)\),
\[
\ell\operatorname{meas}\{k\in I_n:|T^{\rm Rob}(k)-T^{\rm Neu}(k)|>\varepsilon\}
=\frac4{27}\delta_n^2\sqrt{\varepsilon^{-1}-1}+o(\delta_n^2).
\]
In particular, the half-maximum discrepancy window has asymptotic full physical width \(4\delta_n^2/(27\ell)\), although the peak is displaced by order \(\delta_n/\ell\). Its maximum discrepancy tends to one.

For every finite real \(p\ge1\), set
\[
E_{p,n}^p=\ell\int_{I_n}|T^{\rm Rob}(k)-T^{\rm Neu}(k)|^p\,dk.
\]
Define \(g\) and \(G_p\) on \([-\pi/2,\pi/2]\) by
\[
g(x)=\frac{8\sin x\cos x\,(3-4\sin^2x)(6\sin^2x-5)}{[\sin^2x+4\cos^2x(3-4\sin^2x)^2]^2},\qquad
G_p=\int_{-\pi/2}^{\pi/2}|g(x)|^p\,dx>0.
\]
Then the following three exact leading regimes hold:
\[
E_{p,n}^p\sim
\begin{cases}
G_p\delta_n^p,&1\le p<2,\\
(G_2+\pi/27)\delta_n^2,&p=2,\\
\displaystyle\frac{2\sqrt\pi}{27}\frac{\Gamma(p-1/2)}{\Gamma(p)}\delta_n^2,&p>2.
\end{cases}
\]
At the endpoint, \(\lim_{n\to\infty}\|T^{\rm Rob}-T^{\rm Neu}\|_{L^\infty(I_n)}=1\). The result distinguishes bulk linear response from the narrowing order-one resonant spike, with both contributing at \(p=2\).

## Assumptions and scope
A metric quantum graph consists of a line with **two** identical pendant edges of length \(\ell>0\), attached at points separated by \(h=2\ell\). The Hamiltonian acts as \(-d^2/dx^2\) on every edge. At each degree-three junction the same scale-invariant type-I coupling has vector \((\theta_1,\theta_2,\theta_3)=(1,1,\sqrt2)\). At the pendant endpoints compare the Robin condition \(\alpha\psi+\beta\psi'=0\) with \(\alpha,\beta>0\) to Neumann conditions; write \(a=\alpha/\beta>0\). The transmission observable is the probability of transmission at wave number \(k>0\), and the fixed parameters do not vary with \(n\). This is the concrete two-resonator configuration considered in Buhrii–Golovaty–Hryniv [1, Section 5.3]; no generality for other vertex weights, more pendants, or different separations is asserted.

## Proof
**1. Exact phase reduction.** The source transfer formula [1, Eq. (5.12)] with two pendants, \(A=B=1\), \(U_1(z)=2z\), and \(h=2\ell\), gives
\[
T^{\rm Rob}(k)=\frac{\cos^4(k\ell-d(k))}{\cos^4(k\ell-d(k))+4\sin^2(k\ell-d(k))\cos^2(3k\ell-d(k))},
\quad d(k)=\arctan(a/k).
\]
The Neumann formula replaces \(d(k)\) by zero. Put \(x=\ell(k-\kappa_n)\); the odd-half-period trigonometric identities reduce both to
\[
F(x,z)=\frac{\sin^4(x-z)}{\sin^4(x-z)+4\cos^2(x-z)\sin^2(3x-z)},\quad
R_n(x)=F\bigl(x,d(\kappa_n+x/\ell)\bigr),\quad N(x)=F(x,0).
\]
Set the continuous physical value \(N(0)=0\). Note \(N(x)=O(x^2)\) at zero. Throughout the cell, \(d(\kappa_n+x/\ell)=\delta_n+O(\delta_n^2)\) uniformly, and the error improves to \(O(\delta_n^3)\) when \(|x|=O(\delta_n)\); these estimates follow by differentiating \(d(k)\) with \(\ell,a\) fixed.

**2. Center and line shape.** For large \(n\), the function \(x\mapsto3x-d(\kappa_n+x/\ell)\) is strictly increasing on \(|x|<3\delta_n\), with derivative \(3-d'(k)/\ell>3\). It has one root \(x_n\) there, and \(x_n=\delta_n/3+O(\delta_n^3)\). At that root the second term in the denominator of \(F\) vanishes and its numerator is nonzero, hence \(R_n(x_n)=1\). For \(x=x_n+w_nu\) with \(w_n=2\delta_n^2/27\) and bounded \(u\),
\[
\sin(x-d(k))=-\tfrac23\delta_n+O(\delta_n^2),\qquad
\sin(3x-d(k))=3w_nu+o(\delta_n^2).
\]
The two denominator terms, divided by \(16\delta_n^4/81\), converge to \(1\) and \(u^2\) respectively. This establishes the locally uniform Lorentzian limit. Since \(x_n=O(\delta_n)\), \(N(x_n+w_nu)=O(\delta_n^2)\) on compact \(u\)-sets.

**3. A uniform envelope and exceptional-window measure.** Fix the shrinking inner strip \(|x|\le3\delta_n\). The phase \(3x-d(k)\) has a single simple zero \(x_n\), and its derivative is bounded below by \(3\). Its sine is therefore bounded below in absolute value by a fixed positive multiple of \(|x-x_n|\) throughout this strip, for all sufficiently large \(n\). Because \(|\sin(x-d(k))|\le C\delta_n\) and \(|\cos(x-d(k))|\ge1/2\), direct inspection of the denominator gives
\[
0\le R_n(x)\le\frac{C\delta_n^4}{\delta_n^4+(x-x_n)^2}
\quad (|x|\le3\delta_n),
\]
with \(C\) independent of \(n\). On the complementary strip \(|x|\ge3\delta_n\), \(R_n(x)-N(x)=O(\delta_n)\) uniformly, by the denominator estimates in step 4. In the inner strip, \(N(x)=O(\delta_n^2)\). Hence for every fixed \(\varepsilon>0\), all exceedances of \(|R_n-N|>\varepsilon\) lie at \(|x-x_n|=O(\delta_n^2)\). Rescale \(x=x_n+w_nu\), apply the locally uniform Lorentzian limit and the envelope to exclude remote \(u\), and use the fact that the limiting level crossings occur at \(u=\pm\sqrt{\varepsilon^{-1}-1}\). The measure statement follows, with the factor \(2w_n=4\delta_n^2/27\); the supremum statement follows from \(R_n(x_n)=1\) and \(N(x_n)\to0\).

**4. Regular part of the norm.** For \(|x|\ge3\delta_n\), \(F(x,z)\) is twice differentiable for \(|z|\le\delta_n+O(\delta_n^2)\), with its second \(z\)-derivative bounded uniformly in \(x,n\). Near \(x=0\), this follows from \(|3x-z|\ge c|x|\): the numerator of \(F\) and its first two \(z\)-derivatives are respectively \(O(x^4)\), \(O(x^3)\), \(O(x^2)\), while the denominator is bounded below by \(cx^2\), and its first two derivatives are \(O(x)\), \(O(1)\). Away from zero, ordinary smoothness suffices. Differentiating the displayed rational-trigonometric formula gives \(\partial_z F(x,0)=g(x)\) for \(x\neq0\), with continuous extension \(g(0)=0\). Taylor's formula and the variation of \(d(k)\) now yield uniformly
\[
R_n(x)-N(x)=\delta_n g(x)+O(\delta_n^2)
\quad (|x|\ge3\delta_n).
\]
For every fixed real \(p\ge1\), integration over this complementary strip gives \(G_p\delta_n^p+o(\delta_n^p)\), since \(g\) is continuous and not identically zero.

**5. Resonant part of the norm.** On the inner strip, \(\|N\|_{L^p}=O(\delta_n^{2+1/p})\), whereas the Lorentzian peak has norm of order \(\delta_n^{2/p}\). The envelope from step 3, rescaled with \(u=(x-x_n)/w_n\), is an integrable majorant of the \(p\)-th power for every \(p\ge1\). Dominated convergence yields
\[
\int_{|x|\le3\delta_n}|R_n(x)-N(x)|^p dx
=w_n\int_{\mathbb R}\frac{du}{(1+u^2)^p}+o(\delta_n^2)
=\frac{2\sqrt\pi}{27}\frac{\Gamma(p-1/2)}{\Gamma(p)}\delta_n^2+o(\delta_n^2).
\]
Combining this with step 4 establishes each of the three stated regimes. At \(p=2\), both terms have equal power, and the integral of the squared Lorentzian is \(\pi/2\), giving the additional coefficient \(\pi/27\). The proof concerns exact transmission probabilities, not only finite simulations.

## Verification
The standalone `verify.py` checks the explicit rational-trigonometric formula, derivative, center, Lorentzian shape, superlevel widths, and independently quadrature-evaluated norm predictions. Run `python verify.py` in an environment with NumPy and SciPy. The script checks several finite indices, orders and thresholds; asymptotic uniformity, the integrated constants, and the exact range of \(p\) are established by the analytic argument above, not by a finite test suite.

## Relationship to prior work
Buhrii–Golovaty–Hryniv [1] establish the transfer formula, reflection zeros, perfect-transmission resonances and Robin–Neumann uniform convergence away from fixed neighborhoods (Property 8). Their explicit commensurate two-pendant construction gives an order-\(\kappa_n^{-1}\) displacement of a unit-height resonance and failure of global uniform convergence (Remark 4). The new conclusion is not that unit-height peaks exist, but that the **width of their order-one discrepancy is instead order \(\kappa_n^{-2}\)**, with an exact Lorentzian shape, exact superlevel measure, and a three-regime \(L^p\) law. The earlier dipole-comb analysis [2] addresses a different point-interaction model. Drinko–Andrade–Bazeia [3] analyze narrow full-transmission peaks in diamond and hexagonal graph compositions, not the Robin–Neumann comparison or its moving high-energy phase window.

## Limitations
The coefficient and exponent \(p=2\) crossover have been proved only for two pendants with \(h=2\ell\), type-I couplings \((1,1,\sqrt2)\), and positive fixed Robin ratio \(a\). This does not determine a universal resonance width for arbitrary graphs. The norm uses one fixed-length cell and the stated normalization; it is not a whole-half-line \(L^p\) norm. The quoted source formulas and earlier literature are credited; no general Fano line-shape novelty is asserted, and uninspected literature may contain a broader theorem implying the special case.

## References
[1] K. Buhrii, Y. Golovaty and R. Hryniv, *Scattering in Quantum Graphs with Scale-Invariant Vertex Couplings: Resonances, Gaps and (Quasi-)Periodic Transmission*, arXiv:2606.14931v1 (public 12 June 2026), especially Eq. (5.12), Section 5.3 and Property 8. https://arxiv.org/html/2606.14931v1

[2] Y. Golovaty, R. Hryniv and S. Lavrynenko, *Transmission resonances in scattering by δ′-like combs*, arXiv:2503.23837v1 (2025); https://arxiv.org/abs/2503.23837

[3] A. Drinko, F. M. Andrade and D. Bazeia, *Narrow peaks of full transmission in simple quantum graphs*, Phys. Rev. A **100**, 062117 (2019), DOI:10.1103/PhysRevA.100.062117; https://arxiv.org/abs/1907.00656

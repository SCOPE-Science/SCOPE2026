# Universal elliptic fidelity law and arithmetic transfer exceptions in a flux-staggered rhombic chain

## Finding

For the static binary-flux rhombic quantum chain described below, the probability of transfer between the two adjacent central sites of a non-\(\pi\) plaquette is
\[
P_\phi(t)=\frac14\bigl[\cos(\omega_-t)-\cos(\omega_+t)\bigr]^2,\qquad
\omega_\pm=J\sqrt{4\pm2\cos(\phi/2)}.
\]
Write \(r(\phi)=\omega_-/\omega_+\). When \(r(\phi)\) is irrational, the long-time empirical distribution of \(P_\phi(t)\) is **independent of both the flux and hopping strength**. It has the probability density
\[
f(z)=\frac{2K(1-z)}{\pi^2\sqrt z},\quad 0<z<1,\qquad
K(m)=\int_0^{\pi/2}\frac{du}{\sqrt{1-m\sin^2u}}.
\]
In particular, for every \(0<\varepsilon<1\), the proportion of observation times with transfer fidelity exceeding \(1-\varepsilon\) converges to
\[
D(\varepsilon)=\frac2{\pi^2}\int_0^\varepsilon
\frac{K(u)}{\sqrt{1-u}}\,du
=\frac\varepsilon\pi+\frac{3\varepsilon^2}{8\pi}+O(\varepsilon^3)
\quad(\varepsilon\downarrow0).
\]
The exact arithmetic alternative is: if \(r(\phi)=p/q\) in lowest positive terms, perfect transfer occurs if and only if \(p,q\) have opposite parity; if both are odd, even arbitrarily good transfer fails. More quantitatively, when both are odd,
\[
\sup_{t\ge0}P_\phi(t)\le
\cos^4\!\left(\frac{\pi}{2(p+q)}\right)<1.
\]
If \(r(\phi)\) is irrational, transfer can approach unit probability arbitrarily closely, but unit probability is not attained at any finite time. Both kinds of rational exception form dense countable sets of fluxes; the universal elliptic law holds for Lebesgue-almost every flux in \([0,\pi]\).

## Assumptions and scope

Use a one-particle Hermitian nearest-neighbor Hamiltonian on the **infinite** rhombic chain. Its vertices are \(A_n\) for every \(n\in\mathbb Z\), together with \(B_n,C_n\) between \(A_n\) and \(A_{n+1}\). All hopping magnitudes equal \(J>0\); all onsite terms are zero. Specify the gauge through matrix elements
\[
H_{A_n,B_n}=H_{A_n,C_n}=H_{A_{n+1},B_n}=J,
\qquad H_{A_{n+1},C_n}=Je^{i\phi_n},
\]
with Hermitian conjugate reverse elements, where \(\phi_n=\phi\) for even \(n\), \(\phi_n=\pi\) for odd \(n\), and \(0\le\phi\le\pi\). The launch vertex is \(A_0\), and the target is \(A_1\). Transfer fidelity means \(P_\phi(t)=|\langle A_1|e^{-itH}|A_0\rangle|^2\). The long-time empirical probability measure is
\[
\mu_T(E)=T^{-1}\int_0^T\mathbf1_{\{P_\phi(t)\in E\}}\,dt
\]
for Borel \(E\subseteq[0,1]\). Statements about \(\mu_T\) mean weak convergence as \(T\to\infty\); the displayed threshold frequency is an ordinary limit of proportions. No decoherence, boundaries, wave-packet averaging, or periodically switched flux is assumed.

## Proof

**Exact local reduction.** The lattice is bipartite between the \(A\)-sites and the \(B,C\)-sites. The \(A\)-to-\(A\) block of \(H^2\) has diagonal \(4J^2\), and the adjacent \(A_n,A_{n+1}\) entry equals \(J^2(1+e^{\pm i\phi_n})\), with the sign depending on matrix orientation. Thus every odd \(n\) bond contributes zero. The restriction of \(H^2\) to the \(A\) sector splits into independent pairs \((A_{2k},A_{2k+1})\), with the pair matrix
\[
S=J^2\begin{pmatrix}4&1+e^{-i\phi}\\1+e^{i\phi}&4\end{pmatrix}.
\]
It has eigenvalues \(\omega_-^2,\omega_+^2\). Since the \(A\)-to-\(A\) block of the odd powers of \(H\) vanishes, its exact propagator equals \(\cos(t\sqrt S)\). Both eigenprojectors have off-diagonal entry of modulus \(1/2\) with opposite sign for \(0\le\phi<\pi\), which gives the asserted \(P_\phi(t)\); the endpoint \(\phi=\pi\) follows by continuity and yields \(P_\pi(t)=0\).

**Irrational frequencies and universal law.** For irrational \(r=\omega_-/\omega_+\), the orbit \((\omega_-t,\omega_+t)\) is uniquely equidistributed modulo \(2\pi\) on the two-torus. The transfer function on that torus satisfies
\[
\frac14(\cos x-\cos y)^2
=\sin^2\!\left(\frac{x+y}{2}\right)
 \sin^2\!\left(\frac{x-y}{2}\right).
\]
The integer linear map \((x,y)\mapsto(x+y,x-y)\pmod{2\pi}\) is a surjective torus homomorphism, so the pushforward of Haar measure is product Haar measure. Consequently the limiting fidelity has the law of \(XY\), where \(X,Y\) are independent arcsine variables on \((0,1)\), each with density \(g(a)=1/[\pi\sqrt{a(1-a)}]\).

For \(0<z<1\), the multiplicative convolution gives
\[
\begin{aligned}
f(z)&=\int_z^1g(a)g(z/a)\,\frac{da}{a}\\
&=\frac1{\pi^2\sqrt z}\int_z^1\frac{da}{\sqrt{a(1-a)(a-z)}}
=\frac{2K(1-z)}{\pi^2\sqrt z}.
\end{aligned}
\]
The last identity uses \(a=1-(1-z)\sin^2u\). Integration over \(z>1-\varepsilon\) gives \(D(\varepsilon)\). The hypergeometric expansions \(K(u)=\tfrac\pi2(1+u/4+O(u^2))\) and \((1-u)^{-1/2}=1+u/2+O(u^2)\) yield \(D(\varepsilon)=\varepsilon/\pi+3\varepsilon^2/(8\pi)+O(\varepsilon^3)\). Since the limiting law is continuous on \((0,1)\), the indicator of any such strict fidelity threshold is a continuity set, so equidistribution proves the asserted time proportion.

**Arithmetic exceptions.** The ratio varies continuously and strictly increasingly from \(1/\sqrt3\) to \(1\) as \(\phi\) traverses \([0,\pi]\), with inverse relation
\[
\cos(\phi/2)=\frac{2(1-r^2)}{1+r^2}.
\]
If \(r=p/q\) is reduced, write \(\omega_-=p\Omega\), \(\omega_+=q\Omega\). Then \(P(t)=\tfrac14(\cos(p\Omega t)-\cos(q\Omega t))^2\). Equality \(P=1\) requires one cosine to equal \(+1\) and the other \(-1\), i.e., \(p\Omega t,q\Omega t\) are integer multiples of \(\pi\) of opposite parity. Coprimality implies \(\Omega t\in\pi\mathbb Z\), so this happens at positive time if and only if \(p,q\) are of opposite parity (and at \(t=\pi/\Omega\) then). If both are odd, define the distances \(\delta_p,\delta_q\in[0,\pi]\) of \(p\Omega t,q\Omega t\) to the nearest phase targets \(0,\pi\), in whichever order makes the cosine difference nonnegative. The identity \(q(p\Omega t)-p(q\Omega t)=0\), and oddness of \(p,q\), imply \(q\delta_p+p\delta_q\ge\pi\), so at least one distance is \(\ge\pi/(p+q)\). The other cosine is at most one. Therefore the amplitude modulus is at most \((1+\cos(\pi/(p+q)))/2\), proving the stated strict probability bound. If \(r\) is irrational, the torus orbit approaches either phase target \((0,\pi)\) or \((\pi,0)\) arbitrarily closely, while exact alignment would force a rational ratio. Finally, rationals with both odd reduced numerator and denominator, and those with opposite parity, are each dense in the nondegenerate ratio interval; the continuous inverse map preserves density. Each exceptional set is countable, hence null.

## Verification

The companion standalone program `verify.py` reconstructs finite segments of the given infinite Hamiltonian and checks the target transition probability against the closed two-frequency formula for seven flux choices and seven time choices; the segment is large enough to contain the invariant cage. It independently integrates the product-arcsine density and its elliptic form, checks the tail formula by a separate phase-area integral, checks three rational perfect-transfer configurations and four odd/odd caps, and compares deterministic long-time samples at two irrational fluxes. It reports 71 passing finite checks and a largest transition-probability discrepancy below \(7\times10^{-15}\) in those tests. None of these finite tests substitutes for the infinite-time equidistribution proof.

## Relationship to prior work

Hang Li et al., *Engineering topological chiral transport in a flat-band lattice of ultracold atoms* (arXiv:2401.03611v1, 7 January 2024), introduce and experimentally implement the binary-flux rhombic chain, establish the relevant flat bands and local two-frequency cosine amplitudes, and specify discrete flux choices for **perfect** transfers used in Floquet routing. The local transition formula itself is prior work and is independently reconstructed above, not claimed new. The present contribution concerns **the complete long-time fidelity distribution at generic static flux** and its exact elliptic high-fidelity observation-time law, together with the arithmetic exceptional set and explicit rational-resonance ceiling.

The general Kronecker approach to arbitrarily good quantum state transfer predates this work: Vinet and Zhedanov (2012), and Banchi, Coutinho, Godsil and Severini (2016/2018), develop it for spin chains. Accordingly, rational/irrational phase alignment in isolation is not claimed as an original mathematical mechanism. No inspected primary result gives this specific rhombic-chain empirical distribution or its flux-independent elliptic density. Related general product-distribution identities could furnish alternative, shorter derivations.

## Limitations

This is an exact ideal one-particle infinite-chain result for the selected \(A_0\)-to-\(A_1\) transfer and alternating fluxes; it makes no statement about noisy finite experiments, multi-particle dynamics, or the switched-flux Floquet circuit. The universal law describes a \(T\to\infty\) limit and supplies **no uniform finite-time convergence rate** near rational resonances. At rational ratios the limiting time distribution is periodic rather than the stated elliptic law. Other equivalent formulations in uninspected specialized transport or time-statistics literature remain possible; independent priority review has not been performed.

## References

1. Hang Li, Qian Liang, Zhaoli Dong, Hongru Wang, Wei Yi, Jian-Song Pan, Bo Yan, *Engineering topological chiral transport in a flat-band lattice of ultracold atoms*, arXiv:2401.03611v1 (7 January 2024), https://arxiv.org/abs/2401.03611 .
2. Luc Vinet and Alexei Zhedanov, *Almost perfect state transfer in quantum spin chains*, arXiv:1205.4680v3 (2012), https://arxiv.org/abs/1205.4680 .
3. Leonardo Banchi, Gabriel Coutinho, Chris Godsil, Simone Severini, *Pretty Good State Transfer in Qubit Chains — The Heisenberg Hamiltonian*, arXiv:1608.04722v3 (2018), https://arxiv.org/abs/1608.04722 .

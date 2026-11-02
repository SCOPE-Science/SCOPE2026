# Critical scaling of the finite-cell covariance lower-bound coefficient

## Finding
Let \(E\in C^4([0,\pi])\) be positive on \([0,\pi)\), with \(E(\pi)=0\). Suppose that for an integer \(z\ge1\) and a constant \(v>0\), as \(s\downarrow0\),
\[
E(\pi-s)=v s^z+O(s^{z+1}),\qquad E'(\pi-s)=-vz s^{z-1}+O(s^z).
\]
For \(\beta>0\) and integer \(M\ge1\) define \(h=\pi/M\), \(I_{j,M}=[(j-1)h,jh]\), \(\bar E_{j,M}=h^{-1}\int_{I_{j,M}}E(k)\,dk\), and the nonnegative interval-covariance functional
\[
S_M(\beta)=\frac{\beta}{\pi}\sum_{j=1}^M\int_{I_{j,M}}(E(k)-\bar E_{j,M})\tanh(\beta E(k))\,dk.
\]
For each **fixed** \(\beta>0\), as \(M\to\infty\),
\[
S_M(\beta)=\frac{C_E(\beta)}{M^2}+O_{E,\beta}(M^{-4}),\qquad
C_E(\beta)=\frac{\pi\beta^2}{12}\int_0^\pi E'(k)^2\operatorname{sech}^2(\beta E(k))\,dk.
\]
The exact limiting coefficient has the distinct subsequent low-temperature asymptotic
\[
C_E(\beta)\sim K_z(\beta v)^{1/z}\quad (\beta\to\infty),\qquad
K_z=\frac{\pi z}{12}\int_0^\infty u^{1-1/z}\operatorname{sech}^2(u)\,du>0.
\]
In particular \(K_1=\pi/12\), and for the critical transverse-field Ising dispersion \(E(k)=2J\cos(k/2)\) with \(J>0\), one has \(z=1\), \(v=J\), hence \(C_E(\beta)\sim \pi J\beta/12\).

**Order-of-limits restriction.** These are iterated limits: \(M\to\infty\) for each fixed \(\beta\), followed by \(\beta\to\infty\) in the coefficient. The leading term \(C_E(\beta)/M^2\) is smaller than a tolerance \(\varepsilon>0\) when \(M\gtrsim\sqrt{C_E(\beta)/\varepsilon}\), suggesting a *formal leading-coefficient* resolution proportional to \((\beta v)^{1/(2z)}\). This is **not** asserted as a necessary or sufficient growth rate of \(M\) for the exact \(S_M(\beta)\) in a joint limit, or as a statement about actual physical preparation error. Without a remainder bound uniform in \(\beta\), no such joint inference follows.

Indeed, the distinction is sharp. With the admissible linear dispersion \(E(k)=\pi-k\) and any fixed integer \(M\),
\[
\lim_{\beta\to\infty}S_M(\beta)=\frac{\log2}{2M},\qquad
C_E(\beta)=\frac{\pi\beta}{12}\tanh(\pi\beta)\sim\frac{\pi\beta}{12}.
\]
Thus for any fixed \(\varepsilon>0\), an \(M>\log2/(2\varepsilon)\) already makes \(S_M(\beta)<\varepsilon\) for all sufficiently large \(\beta\), despite \(M\) not growing with \(\beta\). The preceding formal coefficient scale cannot be promoted to a uniform necessity claim.

## Assumptions and scope
The unique zero is at the right endpoint; the stated positive one-sided power and derivative asymptotics are assumptions, not consequences of \(C^4\) regularity. The coefficient formula is an exact two-stage asymptotic of the explicitly defined mathematical functional. Identifying that functional with a physical entropy lower-bound contribution requires the specific model derivation in the motivating source. The result does not extend the physical bound to arbitrary Hamiltonians or assert finite-\(M\) saturation.

## Proof
**Cellwise limit.** Put \(g(k)=\tanh(\beta E(k))\). On a cell of width \(h\) centered at \(c\), Taylor expansion about \(c\), subtraction of the cell mean, and parity imply
\[
\int_{c-h/2}^{c+h/2}(E-\bar E)g\,dk
=\frac{h^3}{12}E'(c)g'(c)+O_{E,\beta}(h^5)
=\frac{\beta h^3}{12}E'(c)^2\operatorname{sech}^2(\beta E(c))+O_{E,\beta}(h^5).
\]
The remainder is uniform in \(c\) for any fixed \(\beta\) because \(E\in C^4\) on a compact interval. The composite midpoint rule for the \(C^2\) coefficient function has error \(O(h^2)\). Summing \(M=\pi/h\) cells and multiplying by \(\beta/\pi\) gives
\[
S_M(\beta)=\frac{\beta^2h^2}{12\pi}\int_0^\pi E'(k)^2\operatorname{sech}^2(\beta E(k))\,dk+O_{E,\beta}(h^4),
\]
which is the displayed \(M^{-2}\) expansion. Each cell contribution is nonnegative because \(\tanh(\beta x)\) is increasing: writing it as a double integral of \((E(x)-E(y))(g(x)-g(y))\) shows nonnegativity even when \(E\) itself is not monotone.

**Critical endpoint.** Away from any fixed neighborhood of \(k=\pi\), positivity of \(E\) exponentially suppresses the integrand as \(\beta\to\infty\). Set \(s=\pi-k\), then \(t=(\beta v)^{1/z}s\). The one-sided expansions and exponential domination yield
\[
\int_0^\pi E'(k)^2\operatorname{sech}^2(\beta E(k))\,dk
\sim v^2z^2(\beta v)^{-(2z-1)/z}
\int_0^\infty t^{2z-2}\operatorname{sech}^2(t^z)\,dt.
\]
Substituting \(u=t^z\) after multiplication by \(\pi\beta^2/12\) gives the expression for \(K_z\). The defining integral converges at the origin, where \(1-1/z\ge0\), and exponentially at infinity. At \(z=1\) it equals one. The Ising specialization follows from \(2J\cos((\pi-s)/2)=Js+O(s^3)\).

**Why the two limits cannot be merged without further analysis.** For \(E(k)=\pi-k\), use the coordinate \(s=\pi-k\) and observe that each cell integral of \(E-\bar E\) is zero. For fixed \(M\), the integrals weighted by \(1-\tanh(\beta s)\) away from the terminal cell \(s\in[0,h]\) vanish exponentially after multiplication by \(\beta\). On the terminal cell \(\bar E=h/2\), and
\[
\frac{\beta}{\pi}\int_0^h(s-h/2)\tanh(\beta s)\,ds
=\frac1\pi\int_0^{\beta h}(u/\beta-h/2)(\tanh u-1)\,du
\longrightarrow\frac{h\log2}{2\pi}=\frac{\log2}{2M},
\]
using \(\int_0^\infty(1-\tanh u)\,du=\log2\) and \(\int_0^\infty u(1-\tanh u)\,du<\infty\). Direct integration gives \(C_E(\beta)=(\pi\beta/12)\tanh(\pi\beta)\). This proves the stated counterexample to any unconditional joint-limit resolution inference while leaving both iterated asymptotic theorems intact.

## Verification
The analytic Taylor/midpoint and endpoint-domination proofs establish the unrestricted fixed-temperature and subsequent low-temperature claims. Independent numerical quadrature at \(\beta=2\), \(z=1,2\), and \(M=10,20,40\), together with exact symbolic checks of the terminal-cell boundary-layer calculation, corroborates the formulas but is not their proof. The counterexample is an analytic calculation rather than an inferred failure from finite sampling.

## Relationship to prior work
T. Shirai, *Quasi-adiabatic thermal ensemble preparation in the thermodynamic limit*, arXiv:2510.13555v1 (first public 2025-10-15; revised 2026-02-25; *Physical Review E* 113, 054113 (2026)), derives the physical interval-covariance lower bound in Eq. (42), reports the \(M^{-2}\) order, and treats the Ising critical universality class in Appendix C. The source does not state the exact limiting coefficient integral or its arbitrary-endpoint-order \(z\) asymptotic in the inspected full text. Classical midpoint quadrature and endpoint Laplace methods are established prior art, not claimed novel. The contribution is the explicit physically motivated coefficient and its conditional critical-exponent classification, with the nonuniformity of the two limits now stated sharply.

## Limitations
The \(O(M^{-4})\) constant may depend strongly on \(\beta\), and the theorem proves **no uniform joint \((M,\beta)\) error bound**, no necessary cell-count law at fixed tolerance as \(\beta\to\infty\), and no preparation-complexity bound for a new Hamiltonian. Multiple dispersion zeros, vanishing prefactors, nonsmooth dispersions, and gapped spectra require separate analysis. The source's entropy lower bound need not be saturated for finite cells. Historical priority of related endpoint-integral expansions cannot be certified absolutely.

## References
1. T. Shirai, *Quasi-adiabatic thermal ensemble preparation in the thermodynamic limit*, arXiv:2510.13555v1, first submitted 2025-10-15; revised 2026-02-25; *Physical Review E* **113**, 054113 (2026), DOI:10.1103/dcwj-j65m.
2. Classical composite-midpoint quadrature and endpoint Laplace asymptotic estimates (standard techniques, not claimed original).

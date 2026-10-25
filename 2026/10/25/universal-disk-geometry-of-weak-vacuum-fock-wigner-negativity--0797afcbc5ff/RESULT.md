# Universal disk geometry of weak vacuum–Fock Wigner negativity

## Finding
For every fixed integer \(n\ge1\), let \(h_n\) be the normalized physicists' Hermite function and let
\[
\psi_{n,a,\phi}=\frac{h_0+a e^{i\phi}h_n}{\sqrt{1+a^2}},\qquad a>0,\quad\phi\in\mathbb R.
\]
Write \(\Omega_{n,a,\phi}=\{(q,p)\in\mathbb R^2:W_{\psi_{n,a,\phi}}(q,p)<0\}\) using the Wigner convention below. Put \(C_n=\sqrt{2^n/n!}\), and let \(\zeta_1,\ldots,\zeta_n\) be the distinct roots of \(\zeta^n=-e^{i\phi}/C_n\).

**Theorem.** There is an \(a_n>0\), depending only on \(n\), such that for every \(0<a<a_n\) and every \(\phi\), \(\Omega_{n,a,\phi}\) consists of **exactly \(n\) disjoint bounded strictly convex components**, each having a smooth Jordan boundary. With \(\delta=a^{1/n}\), translate the \(j\)-th component by \(-\delta^{-1}\zeta_j\), identifying the \((q,p)\)-plane with \(\mathbb C\). Its boundary converges, in every fixed \(C^k\) radial-graph norm, to the circle \(|w|=1/\sqrt2\). Consequently
\[
\lim_{a\downarrow0}\operatorname{Area}(\Omega_{n,a,\phi})=\frac{n\pi}{2},
\]
uniformly in the relative phase \(\phi\). The component centers escape to radius \(a^{-1/n}(n!/2^n)^{1/(2n)}\), but their limiting diameter stays \(\sqrt2\). Moreover, for the integrated negative Wigner mass \(\mathcal N_n(a)=\iint_{\mathbb R^2}(-W_{\psi_{n,a,\phi}})_+\,dq\,dp\),
\[
\lim_{a\downarrow0}a^{2/n}\log\mathcal N_n(a)=-\left(\frac{n!}{2^n}\right)^{1/n}.
\]
The integrated mass is independent of \(\phi\), as rotation changes only the directions of the islands.

## Assumptions and scope
For \(n\ge0\), use \(h_n(x)=\bigl(2^n n!\sqrt\pi\bigr)^{-1/2}H_n(x)e^{-x^2/2}\), with \(H_n\) the physicists' Hermite polynomial. The phase-space transform is
\[
W_f(q,p)=\frac1{2\pi}\int_{\mathbb R}f(q+y/2)\overline{f(q-y/2)}e^{-ipy}\,dy.
\]
The theorem concerns the coherent **pure-state** superposition, not the incoherent convex mixture. The amplitude \(a\) tends to zero with \(n\) fixed; no assertion is made uniformly in growing \(n\) or at arbitrary positive \(a\). The area is ordinary planar Lebesgue area, not the integrated negative mass.

## Proof
**Exact polynomial.** The Gaussian/Hermite generating function in the Wigner integral gives
\[
W_{h_0}=\pi^{-1}e^{-r^2},\quad W_{h_n}=\pi^{-1}(-1)^n e^{-r^2}L_n(2r^2),\quad W_{h_0,h_n}=\pi^{-1}e^{-r^2}C_n(q+ip)^n,
\]
where \(r^2=q^2+p^2\), and \(L_n(x)=\sum_{j=0}^n(-1)^j\binom nj x^j/j!\). Thus
\[
W_{\psi_{n,a,\phi}}(q,p)=\frac{e^{-r^2}}{\pi(1+a^2)}\left[1+a^2(-1)^nL_n(2r^2)+2aC_n\operatorname{Re}(e^{-i\phi}(q+ip)^n)\right].
\]
In particular the sign equals the sign of the square-bracket polynomial.

**Singular scaling.** Put \(\epsilon=a^{2/n}\) and \(\zeta=\sqrt\epsilon(q+ip)\). The square-bracket polynomial becomes exactly
\[
Q_\epsilon(\zeta)=1+\epsilon^n(-1)^nL_n(2|\zeta|^2/\epsilon)
+2C_n\operatorname{Re}(e^{-i\phi}\zeta^n).
\]
By the finite Laguerre expansion, on every compact set, with convergence of all derivatives,
\[
Q_\epsilon(\zeta)=|1+C_ne^{-i\phi}\zeta^n|^2
-\epsilon\frac{n^2C_n^2}{2}|\zeta|^{2n-2}+O_n(\epsilon^2).
\]
For \(n=1\) the remainder vanishes identically. The leading term has precisely \(n\) isolated, nondegenerate quadratic zeros \(\zeta_j\), each satisfying \(|\zeta_j|^2=R_n^2=(n!/2^n)^{1/n}\).

**Exclusion away from the roots.** The leading \(C_n^2|\zeta|^{2n}\) term dominates all other terms uniformly for \(|\zeta|\) sufficiently large and \(0<\epsilon\le1\). On a compact set separated from all \(\zeta_j\), the leading square has a strictly positive minimum and the polynomial converges uniformly to it. In a small fixed disk around any \(\zeta_j\), the leading square is bounded below by a positive constant times \(|\zeta-\zeta_j|^2\), while the perturbation is bounded by \(O_n(\epsilon)\). Therefore any negative point satisfies \(|\zeta-\zeta_j|\le M_n\sqrt\epsilon\) for some \(j\), with one fixed \(M_n\).

**Universal disks and topology.** In the translated physical coordinate \(w=(q+ip)-\epsilon^{-1/2}\zeta_j\), substitute \(\zeta=\zeta_j+\sqrt\epsilon\,w\). The exact polynomial gives locally uniformly with all derivatives
\[
\epsilon^{-1}Q_\epsilon(\zeta_j+\sqrt\epsilon\,w)
\longrightarrow n^2C_n^2R_n^{2n-2}\left(|w|^2-\tfrac12\right).
\]
The positive Hessian of this limiting quadratic persists uniformly on \(|w|\le M_n\) when \(\epsilon\) is sufficiently small. There is therefore exactly one strictly convex negative component in each of the \(n\) mutually disjoint neighborhoods; its zero boundary is a smooth radial graph approaching \(|w|=1/\sqrt2\) in every fixed \(C^k\). The exclusion argument proves that there are no other negative components. Translation and convergence of the bounded domains give \(\pi/2+o(1)\) area per component, proving the total-area limit. Changing \(\phi\) rotates all components together and leaves the estimates unchanged.

**Negative-mass logarithm.** All negative points lie in these translated bounded neighborhoods. There, uniformly,
\[
r^2=\frac{R_n^2}{\epsilon}+O_n(\epsilon^{-1/2}),\qquad 0<-Q_\epsilon\le O_n(\epsilon).
\]
On the interior subdisk \(|w|\le1/4\) around each root, the limiting quadratic is strictly negative, so \(-Q_\epsilon\ge c_n\epsilon\) for all sufficiently small \(\epsilon\). The Wigner integral is therefore bounded above and below by positive polynomial factors in \(\epsilon\) multiplying \(e^{-R_n^2/\epsilon+O_n(\epsilon^{-1/2})}\). Taking \(\epsilon\log\) and letting \(\epsilon\downarrow0\) gives the asserted limit.

## Verification
The standalone script `verify.py` checks the Wigner/Hermite formula against five direct high-precision Wigner integrals, verifies the leading and first perturbative Laguerre coefficients exactly for degrees 1 through 30, and numerically counts and measures small-amplitude negativity components for degrees 1 through 5. Its recorded output is in `checker_output.txt`. These are finite checks; the arbitrary-degree and small-amplitude quantifiers are established by the proof above.

## Relationship to prior work
Kenfack and Życzkowski (2004) introduce integrated Wigner negativity and give Fock-state Wigner formulas; they do not state the coherent vacuum–\(n\)-Fock weak-amplitude disk limit. Miranowicz et al. (2013) give the general Fock-superposition Wigner cross-term formula and study qudit coherent states; the finite-mode interference formula is credited, not new. Earlier geometric work on the \(n=2\) coherent vacuum–Hermite superposition establishes its exact two-component/annular phase transition and a small-amplitude logarithmic negative-mass limit; it is a covered special case of portions of the present analysis, not claimed here as new. A nearby published mathematical finding on maximal Wigner-positive vacuum–Fock coherence identifies the same escaping radial scale via a different (mixed-state positivity) optimization. Its complete public RESULT.md was inspected: it establishes radial boundary-layer expansions for maximal Wigner-positive **mixed** states, not the present all-order negativity-island geometry or unweighted area law for pure coherent states. Abreu, Chabaud, Dias and Prata (2025) investigate finite-Hermite Wigner nodal geometry and prove structural rigidity theorems; the primary text was not available in full in this comparison, leaving a publication-priority risk.

## Limitations
This is a leading weak-amplitude geometric theorem for each **fixed** \(n\), not a complete all-amplitude topology classification. The area law is unweighted phase-space area; it must not be confused with Wigner-negativity mass, which decays exponentially. The center escape scale is not independently novel in view of prior near-vacuum coherence analysis. The closest published radial-boundary-layer record was inspected in full, but the potentially broader Abreu et al. 2025 nodal-geometry preprint was read only at abstract level, and publication priority is not independently certified.

## References
1. A. Kenfack and K. Życzkowski, *Negativity of the Wigner function as an indicator of nonclassicality*, first arXiv release 2004-06-02, arXiv:quant-ph/0406015, https://arxiv.org/abs/quant-ph/0406015.
2. A. Miranowicz, M. Paprzycka, A. Pathak and F. Nori, *Phase-space interference of states optically truncated by quantum scissors*, first arXiv release 2013-07-26, arXiv:1307.6950, https://arxiv.org/abs/1307.6950.
3. *Sharp near-vacuum boundary layer for maximal Wigner-positive Fock coherence*, publicly indexed mathematical record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-sharp-near-vacuum-boundary-layer-for-maximal-wigner-positive-foc--bd630ca1caac (summary accessible; full file not available in the present comparison).
4. L. D. Abreu, U. Chabaud, N. C. Dias and J. N. Prata, *Inverse problems for the zeros of the Wigner function*, first arXiv release 2025-04-29, arXiv:2504.20324, https://arxiv.org/abs/2504.20324 (abstract inspected, not full text).

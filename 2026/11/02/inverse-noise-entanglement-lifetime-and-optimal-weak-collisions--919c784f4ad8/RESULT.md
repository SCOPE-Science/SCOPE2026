# Inverse-noise entanglement lifetime and optimal weak collisions in a thermal qubit battery

## Finding

For the ideal bit-flipped partial-swap collision model of [1], with fresh cold ancillas and an initially maximally mixed system qubit, the complete transient entanglement history is a single initial block of non-positive-partial-transpose (NPT) contacts. Its length has an exact formula and a sharp optimized low-temperature law.

For ancilla excited-state probability \(0<p<1/2\), collision strength \(0<t<1\), \(r=1-2p\), and \(\varepsilon=1-r^2\), put
\[
 X_*(p,t)=\frac{\varepsilon\bigl(r+\sqrt{1+4t(1-t)}\bigr)}{r\bigl(4t(1-t)+\varepsilon\bigr)}.
\]
The number of consecutive NPT contacts, beginning with the first and counted **before** each ancilla reset, is exactly
\[
 \boxed{N_p(t)=\max\left\{0,\left\lceil\frac{\log X_*(p,t)}{\log(1-t)}\right\rceil\right\}.}
\]
There exists any entangling contact at any strength if and only if
\[
 \boxed{p<\frac12\left(1-\frac1{\sqrt2}\right).}
\]
When \(p\downarrow0\), allowing the collision strength to depend on \(p\) gives the **sharp optimum**
\[
 \boxed{\lim_{p\downarrow0}p\max_{0<t<1}N_p(t)=K_*=\frac1{a_*+1}=0.231960952986\ldots,}
\]
where \(a_*=3.311070407000\ldots\) is the unique solution greater than one of
\[
 \log\frac{a+1}{2}=\frac{a}{a+1}.
\]
For every asymptotically optimizing selection \(t_p\), necessarily \(t_p/p\to a_*\). Equivalently, if the contact rotation is \(\theta_p\in(0,\pi/2)\) with \(t_p=\sin^2\theta_p\), then \(\theta_p/\sqrt p\to\sqrt{a_*}\). At each fixed strength \(0<t<1\), by contrast, \(N_p(t)=O(\log(1/p))\). The reciprocal-noise lifetime requires weak collisions of the same order as the thermal defect.

## Assumptions and scope

The system \(S\) and each fresh ancilla \(A\) are qubits with ground state \(\lvert0\rangle\) and excited state \(\lvert1\rangle\). The system starts in \(\rho_S^{[0]}=I/2\). Each ancilla is independently initialized as \(\tau_p=(1-p)\lvert0\rangle\langle0\rvert+p\lvert1\rangle\langle1\rvert\), with the same \(0<p<1/2\) at every contact. Each contact uses the ideal unitary
\[
 U_\theta=\exp\bigl[-i\theta(\lvert00\rangle\langle11\rvert+\lvert11\rangle\langle00\rvert)\bigr],\quad 0<\theta<\pi/2,
\]
followed by perfect ancilla removal/reset, without any intervening system operation. Thus, writing \(\rho_S^{[k]}\) for the reduced state after \(k\) resets, the pre-reset state at contact \(k+1\) is \(\rho_{SA}^{[k+1]}=U_\theta(\rho_S^{[k]}\otimes\tau_p)U_\theta^\dagger\). The nonnegative integer \(N_p(t)\) counts the contacts \(k+1\) for which \(\rho_{SA}^{[k+1]}\) is entangled, equivalently NPT for two qubits.

The strength \(t=\sin^2\theta\) and bath probability \(p\) are *constant within each trajectory*. Only the cross-trajectory optimum varies \(t\) with \(p\). Endpoint couplings \(t=0,1\) are excluded: neither creates entanglement from diagonal inputs. The statement concerns existence of strictly positive negativity, not a fixed experimental threshold or a minimum entanglement magnitude.

## Proof

**Step 1: exact population trajectory.** Put \(q=1-p\), \(r=q-p=1-2p\), and \(x_k=(1-t)^k\). Every reduced state stays diagonal because the contact couples only \(\lvert00\rangle\) and \(\lvert11\rangle\) and the ancilla enters diagonally. Its excited-state population \(a_k=\langle1\rvert\rho_S^{[k]}\lvert1\rangle\) obeys
\[
 a_{k+1}=(1-t)a_k+tq,\quad a_0=\tfrac12,\quad a_k=q-\frac r2 x_k.
\]
This agrees with the ideal antithermalizing collision update in [1, Eq. (8)] for the prescribed diagonal initial state.

**Step 2: the partial transpose gives an exact one-dimensional threshold.** In basis \(\lvert00\rangle,\lvert01\rangle,\lvert10\rangle,\lvert11\rangle\), the pre-reset joint state is an X-state with off-diagonal magnitude
\[
 \bigl|\rho_{00,11}^{[k+1]}\bigr|=\frac r2\sqrt{t(1-t)}\,x_k.
\]
Its two untouched odd-parity populations are \(A_k=(1-a_k)p\) and \(B_k=a_kq\). Partial transpose moves the coherence to this odd-parity block; the block has a strictly negative eigenvalue precisely when \(\lvert\rho_{00,11}^{[k+1]}\rvert^2>A_kB_k\). With \(\varepsilon=4p(1-p)=1-r^2\), straightforward expansion reduces that inequality to
\[
 4t(1-t)r^2x_k^2>\varepsilon\bigl[1-r^2(1-x_k)^2\bigr]. \tag{1}
\]
The difference is a quadratic in \(x_k\), strictly negative at zero and with exactly one positive root \(X_*(p,t)\) printed in the Finding. Its leading coefficient is positive and its constant term negative, so (1) holds exactly for \(x_k>X_*\). Since \(x_k\) strictly decreases with \(k\), NPT contacts cannot return after the first PPT contact. The unique real crossing index is \(\log X_*/\log(1-t)\), and counting integer indices \(k\ge0\) proves the displayed ceiling formula, including the strict-equality case.

**Step 3: complete thermal cutoff.** The strongest possible contact is the first one, \(x_0=1\). Criterion (1) at \(x_0=1\) is
\[
 t(1-t)(1-2p)^2>p(1-p).
\]
Using \(t(1-t)\le1/4\) and \(p(1-p)=(1-(1-2p)^2)/4\), some contact strength satisfies this exactly when \(2(1-2p)^2>1\), which is equivalent to the claimed sharp probability cutoff. Above and at equality, no contact is NPT.

**Step 4: finite-ratio lower limit.** Fix \(a>0\) and take \(t=ap\), for sufficiently small \(p\). The explicit threshold gives
\[
 \lim_{p\downarrow0}X_*(p,ap)=\frac2{1+a}.
\]
As \(\log(1-ap)\sim-ap\), the exact count implies
\[
 \lim_{p\downarrow0}pN_p(ap)=F(a):=\frac1a\left[\log\frac{1+a}{2}\right]_+.
\]
The threshold at \(a=1\) is continuous and yields zero. For \(a>1\), the derivative of \(\log((1+a)/2)/a\) has the sign of \(f(a)=a/(a+1)-\log((a+1)/2)\). The derivative \(f'(a)=-a/(a+1)^2<0\), with \(f(1)>0\) and \(f(a)\to-\infty\), shows that there is one maximizer \(a_*\), and \(F(a_*)=1/(a_*+1)\).

**Step 5: global upper bound and uniqueness of optimal scale.** From (1) and the elementary inequality
\[
 1-r^2(1-x)^2\ge r^2(2x-x^2)\quad(0<x\le1),
\]
any entangling contact must satisfy
\[
 x>\frac{2p(1-p)}{t(1-t)+p(1-p)}\ge\frac{2p(1-p)}{t+p}.
\]
Let \(a=t/p\). Because \(-\log(1-t)\ge t\) and a ceiling is strictly below its argument plus one, this gives the uniform bound
\[
 pN_p(t)\le p+\frac1a\left[\log\frac{a+1}{2(1-p)}\right]_+.
\]
For an arbitrary sequence \(p\downarrow0\), take a subsequence on which \(a\) converges in the compactification \([0,\infty]\). At \(a\to0\) the positive logarithm vanishes; at \(a\to\infty\) the logarithmic expression divided by \(a\) tends to zero. For finite positive limits, the upper bound tends to \(F(a)\), matching Step 4 and hence never exceeding \(F(a_*)\). Inserting \(t=a_*p\) proves the sharp global limit. If a strength sequence is asymptotically optimal, every convergent subsequence of \(t/p\) must instead approach the unique maximizer \(a_*\); therefore \(t/p\to a_*\). The small-angle relation \(t=\sin^2\theta\) yields the pulse-angle result.

**Step 6: fixed-strength regime and zero-temperature boundary.** For fixed \(0<t<1\), the explicit threshold is \(X_*(p,t)=\Theta(p)\) as \(p\downarrow0\), giving \(N_p(t)=O(\log(1/p))\). At the separate boundary \(p=0\), inequality (1) holds for every finite \(k\) and every \(0<t<1\), so the sequence of NPT contacts is infinite; this boundary is excluded from the finite-temperature count formula because the threshold is zero.

## Verification

The self-contained program `verify.py` (Python 3; NumPy as declared in `requirements.txt`) constructs the exact two-qubit unitary and joint density matrices, diagonalizes the partial transpose independently of the closed-form negativity, and checks the exact threshold and count at multiple probabilities and collision strengths. Crucially it also independently iterates the full trace-and-fresh-ancilla-reset map for 55 steps at each of 20 parameter pairs and compares with the closed-form trajectory.

The program completed **9,301 finite assertions** without failure; four representative optimized counts at excited probabilities \(0.01\), \(0.002\), \(0.0005\), and \(0.0001\) are respectively \(22\), \(114\), \(462\), and \(2318\). These finite checks corroborate but do not prove the universal asymptotic theorem; Steps 1–6 above provide its proof.

## Relationship to prior work

Pal, Hovhannisyan, Porat, Dutta, Anders, and Knowles [1] give the ideal antithermalizing bit-flipped partial-swap model, collision population update, and numerical finite-collision negativity (including Fig. 3(d)). The new contribution is not that model, its state update, or the general phenomenon of entanglement generation. It is the **complete exact strict-NPT lifetime, the sharp no-entanglement thermal cutoff, and especially the globally optimized inverse-noise collision-count law with necessary weak-coupling scale**.

Scarani, Ziman, Stelmachovič, Gisin, and Bužek [2] establish the general repeated-qubit-ancilla collision framework and analyze maximal entangling power of thermalizing machines. Their optimization concerns single-contact entanglement and uses energy-preserving swaps, rather than the present consecutive-contact lifespan for an antithermalizing (bit-flipped) operation at fixed maximally mixed target input. Uppalapati, McClarty, Haque, and Dutta [3] develop antithermalization by engineered coupling to dissipative reservoirs, but not this finite-collision counting optimization. A wider earlier literature may contain a different formulation of the same elementary two-qubit optimization; independent historical priority has not been certified.

## Limitations

The bath reset is ideal and independent; the coupling and bath state are identical at each step. The theorem assumes an initially maximally mixed target and precisely the pair-creation partial-swap unitary, not arbitrary initial coherences, imperfections, finite reuse memory, or simultaneous target dynamics. Maximizing the **number of strictly positive-negativity collisions** is distinct from maximizing the negativity itself, a fixed minimum measurable negativity, charging speed, ergotropy, or resource efficiency. At the optimal scaling, individual contact entanglement can be arbitrarily small as \(p\to0\). Finite numerical tests do not certify the asymptotics, which are proved analytically.

## References

[1] S. Pal, K. Hovhannisyan, O. Porat, S. Dutta, J. Anders, and H. Knowles, *Ancilla mediated steady-state engineering in open quantum systems*, arXiv:2609.04905v1, first public 2026-09-04, https://arxiv.org/html/2609.04905v1. Read Eqs. (1), (3), (6)–(8), Fig. 3(d), conclusions, and Supplement S2.

[2] V. Scarani, M. Ziman, P. Štelmachovič, N. Gisin, and V. Bužek, *Thermalizing Quantum Machines: Dissipation and Entanglement*, arXiv:quant-ph/0110088v2, https://arxiv.org/pdf/quant-ph/0110088. Read the full four-page text, especially the collision recurrence and entangling-power discussion.

[3] J. Uppalapati, P. A. McClarty, M. Haque, and S. Dutta, *Anti-thermalization: Heating by cooling and vice versa*, arXiv:2412.07630v1, first public 2024-12-10, https://arxiv.org/html/2412.07630v1.

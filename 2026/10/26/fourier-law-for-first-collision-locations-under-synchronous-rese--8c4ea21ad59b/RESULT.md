# Fourier law for first-collision locations under synchronous resetting on odd cycles

## Finding

Consider two independent nearest-neighbor simple random walkers on an odd cycle, updated simultaneously and reset **together** to their distinct initial vertices with probability \(r\) at every step. The process stops at its **first collision anywhere on the cycle**, not upon arrival at a prescribed target. Its entire collision-location probability law has an explicit Fourier representation, and its mean first-collision time has a sharp exact finite-cycle weak-reset threshold.

For every odd integer \(N\ge3\), distinct starting vertices \(a,b\in\mathbb Z/N\mathbb Z\), and \(0\le r<1\), define the modular inverse \(c\equiv2^{-1}\pmod N\), the modular midpoint \(u=c(a+b)\pmod N\), and the half-separation \(i=c(a-b)\pmod N\), represented by an integer \(1\le i\le N-1\). Put \(k_\ell=2\pi\ell/N\) and
\[
\alpha_\ell(r)=\operatorname{arcosh}\left(\frac{2}{1-r}-\cos k_\ell\right),\qquad
h_\ell(r)=\frac{\cosh((i-N/2)\alpha_\ell(r))}{\cosh(N\alpha_\ell(r)/2)}.
\]
The quotients are interpreted continuously at \(\alpha_0(0)=0\). If \(J\) is the first-collision vertex, then for every \(\ell\in\{0,\ldots,N-1\}\),
\[
\mathbb E\left[e^{ik_\ell(J-u)}\right]=\frac{h_\ell(r)}{h_0(r)},
\quad
\Pr(J=j)=\frac1N\sum_{\ell=0}^{N-1}e^{-ik_\ell(j-u)}\frac{h_\ell(r)}{h_0(r)}.
\]
The mean number of discrete update steps to this first collision is
\[
\mathbb E[T_r]=\frac{h_0(r)^{-1}-1}{r}\quad(0<r<1),
\qquad \mathbb E[T_0]=2i(N-i).
\]
Writing \(q=i(N-i)\), its right derivative at zero reset is exactly
\[
\left.\frac{d}{dr}\mathbb E[T_r]\right|_{r=0+}
=\frac{2q}{3}\bigl(5q-(N^2-2)\bigr).
\]
Consequently a sufficiently small positive reset probability **strictly lowers** the expected collision time when \(q<(N^2-2)/5\), and **strictly raises** it when \(q>(N^2-2)/5\). There is no equality case for integer \(N\), because it would require \(N^2\equiv2\pmod5\), which is impossible. A strictly negative derivative guarantees some minimizing positive reset probability because the mean diverges as \(r\uparrow1\), but uniqueness of a minimizer is not claimed.

For example, on the five-cycle an adjacent pair \((a,b)=(0,1)\) has \(i=2\), \(q=6\) and derivative \(+28\), whereas the pair \((0,2)\) has \(i=4\), \(q=4\) and derivative \(-8\). Thus simultaneous-motion parity makes geometric closeness an unreliable guide to whether restarting facilitates collision.

## Assumptions and scope

The walkers occupy vertices in \(\mathbb Z/N\mathbb Z\). Until absorption, at each integer update, with probability \(r\) the ordered pair is reset jointly to \((a,b)\); otherwise the two walkers independently choose increments \(+1\) or \(-1\), each with probability \(1/2\). An encounter is detected after every update, and absorption happens immediately at the first time their vertices coincide. A reset to distinct initial sites cannot itself be a collision. This is a collective resetting protocol, not two independently triggered resets.

The oddness of \(N\) ensures that division by two is well defined modulo \(N\) and the unreset pair process can reach a collision from any distinct start. For even \(N\), if the two initial sites have opposite parity, synchronized nearest-neighbor updates and common resets preserve opposite parity, so no collision is possible. The even-cycle sectors with equal parity are not covered by the stated Fourier formula.

## Proof

**1. Independent center and difference moves.** Set \(U_t=c(X_t+Y_t)\) and \(V_t=c(X_t-Y_t)\) modulo \(N\). These coordinates are invertible because \(N\) is odd, with inverse \(X=U+V\), \(Y=U-V\). Conditional on a non-reset step, choosing equal increments makes \(U\mapsto U\pm1\) and leaves \(V\) fixed, each with probability \(1/4\); choosing opposite increments makes \(V\mapsto V\pm1\) and leaves \(U\) fixed, each with probability \(1/4\). First collision is precisely first arrival at \(V=0\), and its position is \(J=U\) there.

**2. A Fourier boundary-value problem.** Temporarily suppress resets and denote the first time \(V=0\) by \(S\). Lift \(V\) to the interval \(\{0,1,\ldots,N\}\), absorbed at either endpoint (both represent zero modulo \(N\)). For \(0<z\le1\) and every Fourier frequency \(k=k_\ell\), define
\[
f_v(k,z)=\mathbb E_{(u,v)}\left[z^S e^{ik(U_S-u)}\right],\qquad f_0=f_N=1.
\]
The increment cases in Step 1 give, for \(1\le v\le N-1\),
\[
f_v=\frac z4\bigl(f_{v-1}+f_{v+1}+2\cos k\,f_v\bigr).
\]
This is the constant-coefficient second-order recurrence
\[
f_{v+1}+f_{v-1}=2\left(\frac2z-\cos k\right)f_v.
\]
Its unique bounded solution with both boundary values one is
\[
f_v(k,z)=\frac{\cosh((v-N/2)\alpha)}{\cosh(N\alpha/2)},\quad
\cosh\alpha=\frac2z-\cos k.
\]
For \(z=1\), \(k=0\), the solution is the constant one, obtained by continuity. Uniqueness follows from the maximum principle when \(z<1\) and the finite absorbing-walk harmonic principle at \(z=1\). Thus \(f_i(k_\ell,1-r)=h_\ell(r)\).

**3. Independent resetting cycles.** An unreset excursion reaches its first collision before any reset with probability \(\phi=h_0(r)=\mathbb E[(1-r)^S]\). Its unnormalized collision-location Fourier transform is \(h_\ell(r)\). Each failed excursion ends at a reset and independently restarts at exactly the same ordered pair, so the total collision-location transform is the convergent geometric sum \(h_\ell\sum_{m\ge0}(1-\phi)^m=h_\ell/\phi\). Fourier inversion gives the stated probability law, and \(h_0/\phi=1\) proves normalization. The mean length of one attempted excursion is \(\mathbb E[\min(S,R)]=(1-\phi)/r\), where \(R\) is the first independent geometric reset time; renewal gives \(\mathbb E[T_r]=(1-\phi)/(r\phi)\). For \(r=0\), the walk is absorbed almost surely and the formulas continue by limits.

**4. The exact reset derivative.** Let \(m_v=\mathbb E_v[S]\), \(g_v=\mathbb E_v[S(S-1)]\). The lazy difference chain has transition probabilities \(1/4,1/2,1/4\) to \(v-1,v,v+1\). Its first-step recurrences and zero endpoint boundary values are
\[
\Delta m_v=-4,\qquad \Delta g_v=-8(m_v-1),\qquad
\Delta f_v=f_{v+1}-2f_v+f_{v-1}.
\]
Writing \(q_v=v(N-v)\), the identities \(\Delta q_v=-2\) and \(\Delta(q_v^2)=2(N^2+1)-12q_v\) produce the unique polynomial solutions
\[
m_v=2q_v,\qquad
g_v=\frac43q_v^2+\left[\frac43(N^2+1)-4\right]q_v.
\]
Since \(h_0(r)=\mathbb E[(1-r)^S]=1-m_i r+g_i r^2/2+O(r^3)\), the mean-renewal formula yields \(\mathbb E[T_r]=m_i+(m_i^2-g_i/2)r+O(r^2)\), which simplifies to the stated derivative. Finite-state absorption supplies all needed moments. For \(r\uparrow1\), \(\mathbb E[(1-r)^S]\to0\) because \(S\ge1\), so \(\mathbb E[T_r]\to\infty\).

## Verification

The bundled `verify_collision.py` solves the **original ordered-pair transient chain**, without the change of coordinates, for odd sizes \(N=3,5,7,9\) and several initial pairs and reset rates. It compares every absorbing-vertex probability and the mean time against the closed Fourier formulas. It also compares the exact derivative formula with finite differences for \(N=5,7,9,11,21,51\). The program reports 242 successful comparisons. This finite diagnostic is supplementary; the proof above covers every odd \(N\ge3\), all distinct starting vertices, and all \(0\le r<1\).

To reproduce in an environment with Python, NumPy, and SciPy, run `python3 verify_collision.py`. The primary finite comparison uses the linear systems \((I-Q)\,t=\mathbf1\) and \((I-Q)\,P=R\), where \(Q\) is the original nonabsorbing ordered-pair transition matrix and \(R\) records one-step absorption at each vertex.

## Relationship to prior work

Suarez-Jimenez, Riascos, and Boyer (first public April 22, 2026) derive general spectral **mean first-encounter times at a prescribed node** for multiple walkers with synchronous resetting, with numerical ring examples. Rubio-Gomez, Riascos, and Mateos (first public August 7, 2025) consider individual walker reset probabilities and likewise analyze mean first encounter **at a specified vertex**. Neither result supplies a first-collision **anywhere** location law, where absorption at one vertex preempts all subsequent target visits. Summing prescribed-target first-passage means does not compute this different observable.

Pal and Prasad (2018) derive renewal and continuous Brownian interval first-passage formulas, including the known continuum weak-reset threshold \(5u^2-5u+1>0\). Those principles underpin the present method and the large-cycle limiting threshold; that continuum condition is **not claimed as new**. Vega Coso (2026) studies absorption-channel splitting probabilities of a single biased interval walker with resetting, a related but different observable. The original aspects advanced here are the exact odd-cycle **first-collision position Fourier law** with jointly resetting two walkers, and the exact finite-lattice reset derivative including its \(-2\) correction and physical cycle-parity consequence. General absorbing-chain and renewal formulas are acknowledged as preexisting tools.

## Limitations

The model is discrete time, two walkers, odd cycles, simple independent nearest-neighbor hops, and shared geometric resets. The weak-reset inequality characterizes the **initial slope** of the mean; it does not classify all possible nonzero reset-rate optima or their uniqueness. The meeting-location distribution is not a meeting-time/location joint distribution. No originality priority beyond inspected sources is certified; a broader general killed-chain Fourier theorem could imply these special formulas. Neither independent validation nor experimental confirmation is claimed.

## References

1. C. D. Suarez-Jimenez, A. P. Riascos and D. Boyer, *Encounter times of random walkers with simultaneous resetting on networks*, arXiv:2604.20770v1 (April 22, 2026); revised v2 October 2, 2026. https://arxiv.org/abs/2604.20770
2. D. Rubio-Gomez, A. P. Riascos and J. L. Mateos, *Mean first-encounter times of simultaneous random walkers with resetting on networks*, arXiv:2508.05313v1 (August 7, 2025); *J. Phys. A* 58, 325003 (2025). https://arxiv.org/abs/2508.05313
3. A. Pal and V. V. Prasad, *First passage under stochastic resetting in an interval*, arXiv:1812.03009 (2018). https://arxiv.org/abs/1812.03009
4. J. A. Vega Coso, *Channel Duality and Midpoint Invariance in Random Walks with Resetting*, arXiv:2603.24803 (2026). https://arxiv.org/abs/2603.24803

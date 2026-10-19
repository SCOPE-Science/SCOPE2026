# Sharp temperature-only limits on entangling collisions in ideal qubit reset channels

## Finding

Consider a target qubit initially in \(\lvert0\rangle\), colliding repeatedly with fresh qubit ancillas in the same diagonal state \(\tau=(1-p)\lvert0\rangle\langle0\rvert+p\lvert1\rangle\langle1\rvert\), where \(0<p<1/2\). Each collision has the same nontrivial angle, \(h=\cos^2\theta\in(0,1)\). After each collision, discard/reset the ancilla, but inspect its joint state with the target *immediately before* this reset. Compare the ordinary exchange gate \(U_-\), which mixes \(\lvert01\rangle\) and \(\lvert10\rangle\), with the counter-rotating gate \(U_+\), which mixes \(\lvert00\rangle\) and \(\lvert11\rangle\). Their explicit matrices are given below.

Define
\[
 z(r,h)=\frac{2r}{\sqrt{1+4h(1-h)}-1+2r},\qquad 0<r<1,\ 0<h<1.
\]
If \(N_\pm(p,h)\) is the number of collisions for which the pre-reset target–ancilla pair is entangled, then the entangled collisions are **exactly** the initial consecutive collisions \(1,\ldots,N_\pm\), with
\[
 N_-(p,h)=\left\lceil\frac{\log z(1-p,h)}{\log h}\right\rceil,\qquad
 N_+(p,h)=\left\lceil\frac{\log z(p,h)}{\log h}\right\rceil.
\]
There are no later entanglement revivals, and both formulas include exact-threshold equality (zero entanglement at equality). More strongly, for every nontrivial angle the temperature-only bounds are
\[
 1\le N_-(p,h)\le2,
 \qquad 1\le N_+(p,h)\le\left\lceil\frac1p\right\rceil.
\]
Both upper bounds are **sharp as bounds over interaction angles**: for each fixed \(p\in(0,1/2)\), every sufficiently weak, but strictly nonzero, collision strength attains its respective bound. Hence the largest possible entangling-collision count for ordinary thermalization is two, while for the counter-rotating anti-thermalizing gate it is \(\lceil1/p\rceil\).

If \(p=(1+e^{\beta\omega})^{-1}\), where \(\omega>0\) is the ancilla gap and \(\beta>0\), the latter sharp maximum is \(\lceil1+e^{\beta\omega}\rceil\). At a *fixed* nontrivial angle it instead grows only as \(\beta\omega/\lvert\log h\rvert+O(1)\) when \(\beta\to\infty\). The nonuniformity between low temperature and weak collision strength is part of the theorem, not a claim about how large the entanglement is near the identity gate.

## Assumptions and scope

Use the computational basis \(\lvert0\rangle,\lvert1\rangle\), with the ancilla excitation probability \(p\). Set \(K_-=\lvert01\rangle\langle10\rvert+\lvert10\rangle\langle01\rvert\) and \(K_+=\lvert00\rangle\langle11\rvert+\lvert11\rangle\langle00\rvert\), and take \(U_\pm=\exp(-i\theta K_\pm)\) with \(0<\theta<\pi/2\). Every cycle acts on \(\rho_{k-1}\otimes\tau\) by \(U_\pm\), yielding the two-qubit pre-reset state \(\Omega_k^\pm\). The reduced state \(\rho_k=\operatorname{Tr}_A\Omega_k^\pm\) proceeds to the next cycle with a fresh uncorrelated ancilla. The target starts at \(\rho_0=\lvert0\rangle\langle0\rvert\). These are ideal gates without free rotations, control errors, or residual inter-ancilla memory.

Here \(N_\pm\) counts \(k\ge1\) such that \(\Omega_k^\pm\) is nonseparable. For two qubits this is equivalent to a negative partial transpose. Concurrence and negativity are *zero simultaneously* for these states; no equivalence of their numerical values is implied. The density matrices themselves are available for all finite \(k\), not just in the stationary limit.

## Proof

**Step 1: Reduced dynamics.** Both gates mix only their stated two-dimensional subspaces; their restricted matrices have diagonal \(\cos\theta\) and off-diagonal \(-i\sin\theta\), and both are the identity on the other two basis states. The reduced target state remains diagonal. Let \(q_k=\langle1\rvert\rho_k\lvert1\rangle\), and write \(x_-=p\), \(x_+=1-p\). Multiplying the two-qubit matrices and tracing the ancilla gives
\[
 q_k=hq_{k-1}+(1-h)x_\pm,
 \qquad q_k=x_\pm(1-h^k).
\]
Thus both protocols approach their known respective thermal and bit-flipped thermal populations, but at the same exponential rate.

**Step 2: Exact entanglement test.** Fix either protocol and abbreviate \(x=x_\pm\), \(r=1-x\), and \(z=h^{k-1}\). The population immediately before collision \(k\) is \(q=x(1-z)\). The two states mixed by the gate have a pre-unitary population difference \(x-q=xz\). Accordingly, the unique nonzero off-diagonal pair of \(\Omega_k\) has magnitude \(xz\sqrt{h(1-h)}\). The two inert diagonal populations have product \(prq(1-q)\) in the minus protocol with \(r=1-p\), or \(p(1-p)q(1-q)\) in the plus protocol with \(r=p\); in either case their product is \(xrq(1-q)\).

Partial transposition moves that off-diagonal pair to the inert two-by-two block. The only potentially negative partial-transpose eigenvalue belongs to this block, and its determinant is negative exactly when
\[
 x^2z^2h(1-h)>xrq(1-q).
\]
Since \(x>0\), substituting \(q=x(1-z)\) reduces this to the explicit scalar condition
\[
 F(z):=h(1-h)z^2-r(1-z)(r+xz)>0. \tag{1}
\]
Indeed the complete concurrence is
\[
 C_k=2\max\!\left\{0,\ xz\sqrt{h(1-h)}-\sqrt{xr\,q(1-q)}\right\}.
\]
The last expression is a consequence of the standard two-qubit X-state formula, and is not needed to infer entanglement from the partial transpose.

**Step 3: Exactly one finite cutoff.** The polynomial \(F\) has positive leading coefficient \(h(1-h)+rx\), negative constant term \(-r^2\), and therefore precisely one positive zero. Moreover \(F(0)=-r^2<0\) and \(F(1)=h(1-h)>0\), so that zero is in \((0,1)\). Solving the quadratic and rationalizing, using \((x-r)^2+4rx=(x+r)^2=1\), gives exactly \(z(r,h)\). Since \(z=h^{k-1}\) strictly decreases from one to zero, (1) is true if and only if \(h^{k-1}>z(r,h)\). Equivalently \(k-1<\log z(r,h)/\log h\). The last eligible integer is precisely \(\lceil\log z(r,h)/\log h\rceil\), including the case when this ratio is an integer. The same sign argument rules out any later revival.

**Step 4: Uniform temperature bound and optimality.** Let \(\delta=1-h\in(0,1)\). The inequality \(\sqrt{1+4h(1-h)}\le1+2\delta\) implies
\[
 z(r,h)\ge\frac r{r+\delta}.
\]
Elementary logarithmic inequalities give
\[
 \log\left(1+\frac\delta r\right)\le\frac\delta r
 \le -\frac{\log(1-\delta)}r.
\]
Consequently \(z(r,h)\ge h^{1/r}\), strictly for \(0<h<1\). Dividing the logarithmic inequality by \(\log h<0\), with its sign reversal, yields
\[
 0<\frac{\log z(r,h)}{\log h}<\frac1r.
\]
Hence \(N\le\lceil1/r\rceil\). For \(U_-\), \(r=1-p>1/2\) so the cap equals two; for \(U_+\), \(r=p\), giving the stated cap. Finally, as \(h\uparrow1\), \(z(r,h)=1-(1-h)/r+O((1-h)^2)\), and therefore \(\log z(r,h)/\log h\to1/r\) from below. This proves sharpness of both ceiling bounds (including integral \(1/r\), for which the approaching ceilings equal that integer).

**Step 5: Low-temperature distinction.** With \(h\in(0,1)\) fixed and \(p\downarrow0\), the plus-protocol threshold satisfies \(z(p,h)\sim2p/[\sqrt{1+4h(1-h)}-1]\). Its count is thus \(\log(1/p)/\lvert\log h\rvert+O(1)\). Meanwhile its angle-optimized upper count is \(\lceil1/p\rceil\). If \(p=0\) exactly, the plus gate remains entangling at every finite collision: \(C_k=2h^{k-1}\sqrt{h(1-h)}>0\). For \(U_-\) at \(p=0\) the target and ancilla never leave \(\lvert00\rangle\), giving zero entanglement. These endpoint statements are distinguished from the strict finite-temperature theorem.

## Verification

The accompanying standalone `CHECK.py` reconstructs both four-by-four gates, both product inputs, their matrix conjugations, the reduced populations and the partial-transpose determinant. It compares these direct calculations to independent exact-rational evaluations of (1) across multiple parameter pairs and collision indices, including the first nonentangling collision. It also tests examples approaching the sharp angle-independent bound and both pure-bath endpoints. Run `python3 CHECK.py` using Python 3 and no external dependencies. This produced 1302 passing assertions in the present package. Numerical tests do not certify the arbitrary-parameter inequalities; Steps 1–5 are their proof.

Illustratively, \(p=1/10\), \(h=1/2\) gives \((N_-,N_+)=(1,2)\), whereas \(p=1/10\), \(h=99/100\) gives \((N_-,N_+)=(2,10)\). The second choice saturates both respective temperature-only caps.

## Relationship to prior work

Pal, Hovhannisyan, Porat, Dutta, Anders and Knowles (2026) introduce and experimentally study the two ideal collision gates, their thermal and anti-thermal stationary states, and the transient negativity and mutual information. In particular, their ideal population recurrence is not asserted as new here. The contribution established above is the **sharp analytic finite-collision entanglement horizon**, its coupling-independent optimal ceiling, and the cold-bath separation between the two gate types. The proof uses standard two-qubit partial-transpose theory rather than claiming a new entanglement criterion.

Lalita and Banerjee (2025) analyze concurrence in a different two-system-qubit model involving ancilla–ancilla memory and two reservoir architectures. Doğan, Ödemiş, Yunt and Müstecaplıoğlu (2026) study entanglement *among network nodes* under coherent ancilla-mediated gates, rather than system–fresh-thermal-ancilla entanglement immediately before each reset. Neither accessible treatment states the above sharp temperature-only count comparison. These are comparisons of observables and implications, not evidence that all possible literature has been exhausted.

## Limitations

The result is for a ground-initialized target, diagonal identical fresh ancillas, two ideal gates with one fixed collision angle, and the entanglement of the *current target–ancilla pair just before resetting*. It is not a claim about persistent entanglement among network qubits, arbitrary initial target coherence, thermal ancilla–ancilla correlations, control imperfections, off-resonant pulse sequences, or a unique universal entanglement lifetime for all collision models. At the weak-gate values attaining the maximum count, each collision can create arbitrarily small entanglement; the count is not an amount-of-entanglement bound. Material from the source's separately displayed supplemental subsections was not independently available for a complete comparison; potential implicit or independently known coverage of the sharp bound remains a literature risk.

## References

1. S. Pal, K. Hovhannisyan, O. Porat, S. Dutta, J. Anders, H. Knowles, *Ancilla mediated steady-state engineering in open quantum systems*, arXiv:2609.04905v1 (first public 2026-09-04). https://arxiv.org/abs/2609.04905
2. J. Lalita and S. Banerjee, *Non-classicality of two-qubit quantum collision model: non-Markovian effects*, arXiv:2506.23818v1 (2025). https://arxiv.org/abs/2506.23818
3. M. Doğan, Ö. F. Ödemiş, E. Yunt, Ö. E. Müstecaplıoğlu, *Distribution of Bell State Entanglement in Qubit Networks via Collision Models*, arXiv:2604.01773v1 (2026). https://arxiv.org/abs/2604.01773
4. A. Peres, *Separability Criterion for Density Matrices*, Physical Review Letters 77, 1413 (1996), DOI:10.1103/PhysRevLett.77.1413.
5. M. Horodecki, P. Horodecki, R. Horodecki, *Separability of mixed states: necessary and sufficient conditions*, Physics Letters A 223, 1–8 (1996), DOI:10.1016/S0375-9601(96)00706-2.

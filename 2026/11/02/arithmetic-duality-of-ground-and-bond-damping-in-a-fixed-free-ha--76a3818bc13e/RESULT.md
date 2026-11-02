# Arithmetic duality of ground and bond damping in a fixed–free harmonic chain

## Finding

For every integer \(n\ge2\), consider \(n\) equal masses in a one-dimensional chain, with one end connected to a fixed wall by a spring and the other end free. All \(n\) springs have stiffness \(k>0\) and all masses have mass \(m>0\). Attach any nonempty finite selection of strictly positive viscous ground dashpots at mass positions \(P\subseteq\{1,\ldots,n\}\) and/or strictly positive bond dashpots across spring positions \(B\subseteq\{1,\ldots,n\}\). The first bond joins the wall and mass one.

Define the odd integer and its arithmetic damping invariant by
\[
N=2n+1,\qquad g=\gcd\bigl(N,\{p:p\in P\},\{2b-1:b\in B\}\bigr).
\]
For an empty collection in a gcd, omit that collection. Since at least one dashpot is present, \(g\) is a proper odd divisor of \(N\).

**Complete surviving-mode and stability law.** Exactly \((g-1)/2\) oscillatory normal modes survive permanently. Their angular frequencies, each occurring once, are
\[
\omega_t=2\sqrt{k/m}\,\sin\!\left(\frac{\pi t}{2g}\right),
\qquad t=1,3,5,\ldots,g-2.
\]
Every other component of every finite-energy trajectory decays exponentially. In particular, every trajectory decays to rest exponentially **if and only if** \(g=1\), independently of the positive dashpot strengths.

**Local-injection energy law.** If the chain starts with zero displacements and the sole initial velocity is \(v\) at mass \(j\), the exact fraction of the initial energy remaining at infinite time is
\[
\frac{E_\infty}{E_0}=
\begin{cases}
0,&g\mid j,\\[2pt]
\dfrac{g}{2n+1},&g\nmid j.
\end{cases}
\]
This includes \(g=1\), when no positive fraction survives. Therefore some initial kicks dissipate completely even in a network that supports undamped modes, whereas all other single-mass kicks retain the *same* nonzero energy fraction.

**Placement consequence.** A single ground dashpot at position \(p\) eliminates all undamped modes exactly when \(\gcd(p,N)=1\). A single bond dashpot at \(b\) does so exactly when \(\gcd(2b-1,N)=1\). Each type has precisely \(\varphi(N)/2\) individually stabilizing positions, with \(\varphi\) Euler's totient. In particular, a bond dashpot on the last bond \(b=n\) always stabilizes the chain, because \(\gcd(N,N-2)=1\). The two damping types can have identical undamped spectra and local retained-energy laws without having the same transient decay rates.

## Assumptions and scope

Index masses from \(1\) at the fixed wall to \(n\) at the free end, set \(u_0(t)=0\), and write \(u(t)\in\mathbb R^n\) for displacement. Let \(e_j\) be the standard Euclidean basis and \(e_0=0\). The stiffness matrix \(T\) has diagonal \((2,2,\ldots,2,1)\) and entries \(-1\) on its immediate off-diagonals. For ground coefficients \(\alpha_p>0\) and bond coefficients \(\beta_b>0\), define
\[
C=\sum_{p\in P}\alpha_p e_pe_p^{\mathsf T}
 +\sum_{b\in B}\beta_b(e_b-e_{b-1})(e_b-e_{b-1})^{\mathsf T}.
\]
The model is the autonomous linear initial-value problem
\[
m\ddot u+C\dot u+kTu=0.
\]
The energy is \(E(t)=(m\|\dot u(t)\|^2+k u(t)^{\mathsf T}Tu(t))/2\). Only viscous, positive local dashpots are allowed; no claim is made about nonlinear loss, active elements, other endpoint conditions, nonuniform masses or springs, infinite chains, or a rate uniform in system size or in vanishing dashpot coefficients.

## Proof

**1. Undamped spectral basis.** Put \(q_s=(2s-1)\pi/N\), \(s=1,\ldots,n\). The fixed condition \(u_0=0\) and free condition \(u_{n+1}=u_n\) give the complete orthonormal eigenbasis
\[
\phi_{s,j}=\frac{2}{\sqrt N}\sin(jq_s),\quad
T\phi_s=(2-2\cos q_s)\phi_s,\quad
\omega_s=2\sqrt{k/m}\sin(q_s/2).
\]
The eigenvalues are positive and pairwise distinct. The normalization follows from \(\sum_{j=1}^n\sin^2(jq_s)=N/4\).

**2. A site dashpot and a bond dashpot obey the same divisibility test.** A mode \(\phi_s\) is killed by the ground-damping vector \(e_p\) precisely when
\[
e_p^{\mathsf T}\phi_s=0\quad\Longleftrightarrow\quad N\mid p(2s-1).
\]
For the bond-damping vector, the sine-difference identity gives
\[
(e_b-e_{b-1})^{\mathsf T}\phi_s
=\frac{4}{\sqrt N}\sin(q_s/2)
\cos\!\left(\frac{(2b-1)q_s}{2}\right).
\]
Since \(0<q_s<\pi\) and all of \(N\), \(2b-1\), and \(2s-1\) are odd, the last expression vanishes **if and only if** \(N\mid(2b-1)(2s-1)\). The apparently different damping mechanisms therefore impose identical integer-divisibility conditions with different position labels.

**3. Simultaneous constraints.** Positivity of every dashpot coefficient implies \(\phi_s^{\mathsf T}C\phi_s=0\) precisely when every active damping vector annihilates \(\phi_s\). Bézout's identity reduces all conditions \(N\mid d(2s-1)\), where \(d\) runs through the active labels, to
\[
\frac{N}{g}\mid(2s-1).
\]
As \(2s-1\) ranges through the odd integers \(1,3,\ldots,N-2\), this is equivalent to \(2s-1=(N/g)t\) for \(t=1,3,\ldots,g-2\). Exactly \((g-1)/2\) modes survive, with \(q_s=t\pi/g\) and the frequencies displayed above.

**4. Exponential attraction to the surviving oscillations.** Direct differentiation gives
\[
\frac{dE}{dt}=-\dot u^{\mathsf T}C\dot u\le0.
\]
Hence the first-order evolution is a contraction in the positive mechanical-energy norm; its eigenvalues have nonpositive real parts. A nonzero purely imaginary eigenvalue necessarily has an undamped stiffness eigenvector \(\phi_s\) in \(\ker C\); zero cannot occur because \(T\) is positive definite. The span of these protected eigenvectors and its orthogonal complement are both invariant under \(T\) and \(C\), since \(T\) and \(C\) are symmetric and \(C\) annihilates the protected span. On the complement there are no imaginary-axis eigenvalues; all eigenvalues consequently have strictly negative real parts. Finite-dimensional linear-system theory gives exponential decay there, even when nonnormal decaying blocks have nontrivial Jordan structure. On the protected span, the motion is exactly harmonic at the displayed frequencies.

**5. Exact asymptotic energy from a local kick.** Let \(\Pi\) project orthogonally onto the protected stiffness modes. For initial conditions \(u(0)=0\), \(\dot u(0)=v e_j\), the protected energy divided by \(E_0=mv^2/2\) is \(\|\Pi e_j\|^2\). Using the basis above gives
\[
\|\Pi e_j\|^2=\frac4N\sum_{\substack{1\le t<g\\t\text{ odd}}}
\sin^2\!\left(\frac{\pi jt}{g}\right).
\]
Because \(g\) is odd, the odd integers \(1\le t<g\) contain exactly one representative from each pair \(\{r,g-r\}\) of nonzero residues modulo \(g\). Thus this sum is one half of \(\sum_{r=1}^{g-1}\sin^2(\pi jr/g)\), which is \(g/2\) for \(g\nmid j\) and zero for \(g\mid j\). This proves the stated energy fraction. The decaying complement contributes zero to the limiting energy.

**6. Number of stabilizing single-dashpot placements.** A lone site dashpot works iff its index is coprime to \(N\). Among the reduced residues \(1,\ldots,N-1\), the involution \(r\mapsto N-r\) pairs exactly one index at most \(n\) with one larger than \(n\), yielding \(\varphi(N)/2\). A lone bond dashpot works iff the odd label \(2b-1\) is coprime to \(N\). Since \(N\) is odd, the same involution pairs one odd and one even reduced residue; exactly \(\varphi(N)/2\) bond labels are suitable.

## Verification

Run `python verify_damping.py` with NumPy and SciPy installed. It checks **6,478 single-dashpot mode-index cases**, **238 single-dashpot state-space spectra**, **390 mixed-dashpot state-space spectra**, **79 totient placement identities**, and **31,950 local-kick projector identities**. Its tolerances and finite ranges are visible in the script. These finite checks are diagnostics only; the proof for every finite chain and all positive loss coefficients is above.

## Relationship to prior work

Giurdanella and Sparavigna (2010) studied self-frequency-locking of a fixed–free uniform oscillator chain with one site damper, reporting selected surviving modes from computations and an interpretation through matched subchain frequencies. Their analysis motivates the present question but does not state the mixed *ground-and-bond* damping invariant, the general joint gcd classification, or the site-resolved retained-energy formula. In particular, the present result is not a claim that the underlying fixed–free eigenfrequencies or single-site synchronization mechanism are new.

Lecomte (2014) developed exact transfer-function pole/zero results for nominal chains and selected low-rank endpoint disturbances, with broad damping applications. His §6 identifies multi-rank and multi-parameter disturbances at other locations as possible extensions. The present result instead classifies the imaginary-axis spectrum and asymptotic retained energy for **arbitrary positive collections of interior site and bond dashpots** under one-fixed, one-free boundary conditions. General energy dissipation and orthogonal mode decomposition are standard tools; the arithmetic equivalence between the two physical damping mechanisms and the uniform local-kick retention law are the specific statements assessed here.

## Limitations

This theorem concerns linear autonomous finite networks with homogeneous masses and springs and passive viscous dashpots. It determines *which* oscillations survive, their exact frequencies, and a class of asymptotic energy fractions, but not the exact negative-real-part eigenvalues or a uniform decay-rate bound. The single-site phenomenon and much underlying modal theory predate this result. Equivalent arithmetic formulations may exist in the broader controllability and vibration literature; historical priority is not independently certified.

## References

1. S. Giurdanella and A. C. Sparavigna, *Self frequency-locking of a chain of oscillators*, arXiv:1006.1722, initial public version 2010-06-09. https://arxiv.org/abs/1006.1722 ; https://arxiv.org/pdf/1006.1722
2. C. Lecomte, *Zero and root loci of disturbed spring–mass systems*, Proceedings of the Royal Society A **470** (2014), 20130751, doi:10.1098/rspa.2013.0751. Lawful full text: https://pmc.ncbi.nlm.nih.gov/articles/PMC3928960/

# An arithmetic-renewal dichotomy for quantum resetting: exact limit cycles and a no-cancellation criterion

## Finding

For every finite-dimensional, discrete-time unitary quantum system fully reset at independent identically distributed positive integer waiting times of finite mean, the lattice span of the waiting-time distribution determines whether the averaged density matrix converges or approaches a periodic orbit. The result includes a necessary-and-sufficient condition for convergence under arithmetic renewal clocks, an exact trace-norm phase limit, and an explicit strict phase-separation certificate.

Let \(L\) denote the integer time between resets, \(m=\mathbb E L<\infty\), and
\[
d=\gcd\{\ell\geq1:\Pr(L=\ell)>0\}.
\]
When \(d=1\), the ensemble density matrix converges in trace norm to
\[
\rho_\infty=\frac1m\sum_{a=0}^\infty \Pr(L>a)\,U^a\rho_*U^{-a}.
\]
When \(d>1\), write \(K=L/d\), \(\nu=\mathbb E K\), and
\[
B=\frac1\nu\sum_{k=0}^\infty\Pr(K>k)\,U^{dk}\rho_*U^{-dk}.
\]
For each integer \(j\in\{0,\ldots,d-1\}\),
\[
\lim_{n\to\infty}\left\|\rho_{dn+j}-U^jBU^{-j}\right\|_1=0.
\]
The phase limits are all equal, and the ordinary limit exists, **if and only if** \([U,\rho_*]=0\). In particular, every noncommuting reset state yields a genuinely nonconstant periodic asymptotic density-matrix orbit despite independent resets with finite positive mean waiting time.

There is no accidental cancellation of an active off-diagonal matrix element. If \(Ue_a=u_ae_a\) is an orthonormal eigenbasis, define
\[
H_K(z)=\frac1\nu\sum_{k\ge0}\Pr(K>k)z^k,
\quad |z|=1.
\]
Then
\[
\langle e_a,Be_b\rangle
=\langle e_a,\rho_*e_b\rangle\,H_K((u_a\overline{u_b})^d),
\qquad H_K(z)\ne0\ \text{for every }|z|=1.
\]
Consequently the difference between the first two limit phases has the exact nonnegative square
\[
\|UBU^{-1}-B\|_2^2
=\sum_{a,b}|u_a\overline{u_b}-1|^2
|\langle e_a,\rho_*e_b\rangle|^2
\left|H_K((u_a\overline{u_b})^d)\right|^2.
\]
It is strictly positive precisely when \([U,\rho_*]\ne0\). The conclusion is independent of the particular eigenbasis, including degenerate eigenspaces.

## Assumptions and scope

Take any finite-dimensional complex Hilbert space \(\mathcal H\), a fixed unitary \(U\), and a positive trace-one density matrix \(\rho_*\). At time zero the quantum system has state \(\rho_*\). Independently draw successive waiting times \(L_1,L_2,\ldots\) with the distribution of \(L\) on the positive integers, independently of the quantum evolution, with \(0<m=\mathbb EL<\infty\). At renewal epochs \(S_n=\sum_{i=1}^n L_i\) the system is instantaneously returned to \(\rho_*\); at all other integer times it evolves by the same conjugation \(\mathcal U(X)=UXU^{-1}\). The epoch itself is observed *after* resetting. Let \(A_t=t-\max\{S_n:S_n\le t\}\) be the age at time \(t\) (including \(S_0=0\)), and define the ensemble state \(\rho_t=\mathbb E[U^{A_t}\rho_*U^{-A_t}]\). No stationarity is assumed at time zero, and the full reset state may be mixed. The positive waiting times may have unbounded support; no second moment is required. Trace norm is \(\|X\|_1=\operatorname{tr}\sqrt{X^\dagger X}\), and Hilbert--Schmidt norm is \(\|X\|_2^2=\operatorname{tr}(X^\dagger X)\).

## Proof

**1. Exact age mixture.** Set \(u(n)=\sum_{r\ge0}\Pr(S_r=n)\), with \(S_0=0\). Because the strictly positive renewal epochs cannot coincide, this is a renewal-epoch probability and obeys \(0\le u(n)\le1\). For integers \(0\le a\le t\), the event that the last renewal was at \(t-a\) and the next interval exceeds \(a\) has probability
\[
\Pr(A_t=a)=u(t-a)\Pr(L>a).
\]
These disjoint events partition the sample space, so the weights sum to one. It follows that
\[
\rho_t=\sum_{a=0}^t u(t-a)\Pr(L>a)\,U^a\rho_*U^{-a}.
\]

**2. Lattice renewal limit.** The integer \(d\) is the maximal lattice span because the resets begin at epoch zero. Since every \(L\) is divisible by \(d\), \(u(n)=0\) off multiples of \(d\). For \(K=L/d\), the support has greatest common divisor one and mean \(\nu=m/d\). The ordinary discrete arithmetic renewal theorem gives
\[
\lim_{n\to\infty}u(dn)=1/\nu=d/m.
\]
Fix a residue \(j\in\{0,\ldots,d-1\}\) and let \(t=dn+j\). Only ages \(a=dk+j\), with \(k=0,\ldots,n\), contribute to the exact age mixture. Because \(L=dK\) and \(0\le j<d\),
\[
\Pr(L>dk+j)=\Pr(K>k).
\]
For each fixed \(k\), the corresponding probability mass tends to \(\nu^{-1}\Pr(K>k)\). Furthermore, the tail is summable by the tail-sum identity \(\sum_{k\ge0}\Pr(K>k)=\nu\). The bound \(u(n)\le1\) and dominated convergence over the countable index \(k\) show that the *entire age probability distribution* converges in total variation to that sequence, not merely pointwise. Each conjugated density matrix has trace norm one. The triangle inequality therefore upgrades the coefficient convergence to the asserted trace-norm convergence of \(\rho_{dn+j}\) to \(U^jBU^{-j}\). At \(d=1\) this gives the displayed ordinary limit with \(K=L\).

**3. Nonvanishing renewal multiplier.** The absolutely convergent power series \(H_K\) satisfies \(H_K(1)=1\). For \(|z|=1\) and \(z\ne1\), the finite geometric-sum identity, followed by expectation, gives
\[
H_K(z)=\frac{1-\mathbb E[z^K]}{\nu(1-z)}.
\]
If it vanished, then \(\mathbb E[z^K]=1\). All values \(z^K\) lie on the unit circle, so equality in the triangle inequality forces \(z^K=1\) almost surely. Bezout's identity applied to the (possibly infinite) support with gcd one gives \(z=1\), contrary to assumption. Thus the multiplier never vanishes on the unit circle. No analytic continuation or second moment is needed.

**4. Exact no-cancellation criterion and phase gap.** Diagonalize \(U\). The previous step gives the spectral-entry formula for \(B\), with a nonzero multiplicative coefficient for every pair of eigenvalues. Hence, for each pair \(a,b\), \((u_a\overline{u_b}-1)\langle e_a,Be_b\rangle=0\) exactly when \((u_a\overline{u_b}-1)\langle e_a,\rho_*e_b\rangle=0\). Consequently \([U,B]=0\) is equivalent to \([U,\rho_*]=0\). Expanding the squared Hilbert--Schmidt norm of \(UBU^{-1}-B\) in the eigenbasis gives the claimed nonnegative sum. It is strictly positive if and only if the commutator is nonzero. If the ordinary sequence \(\rho_t\) converges, its residue-zero and residue-one limits are the same, hence \([U,B]=0\). Conversely if \([U,\rho_*]=0\), then every trajectory state equals \(\rho_*\), so convergence holds even at finite times. This establishes the stated if-and-only-if and the genuinely nonconstant nature of the limiting cycle for \(d>1\).

**5. Cycle-average identity.** As an additional consequence, the average of the \(d\) phases is
\[
\frac1d\sum_{j=0}^{d-1}U^jBU^{-j}
=\frac1m\sum_{a=0}^\infty\Pr(L>a)U^a\rho_*U^{-a}.
\]
Indeed, write \(a=dk+j\) and use \(\Pr(L>dk+j)=\Pr(K>k)\) and \(m=d\nu\). Boundedness and residue-wise convergence imply that the Cesàro mean \(T^{-1}\sum_{t=0}^{T-1}\rho_t\) has the same limit. Thus ordinary convergence and convergence of time averages are different questions for arithmetic clocks.

## Verification

The included standalone Python checker `verify_periodic_reset.py` uses only the standard library and can be executed as `python3 verify_periodic_reset.py`. It verifies exact finite-horizon age convolution identities; probability conservation; exact rational renewal distribution limits for multiple finite-support clocks; finite spectral multiplier calculations; and phase-gap identities. It also tests a nonconstant two-phase example. These **1212 finite diagnostics are not proofs of the infinite-horizon statements**; the proof is the discrete renewal theorem plus steps 1--5 above.

An explicit qubit example has \(U=\operatorname{diag}(1,i)\), reset state \(\rho_*=\tfrac12\begin{psmallmatrix}1&1\\1&1\end{psmallmatrix}\), and \(\Pr(L=2)=\Pr(L=4)=\tfrac12\). Here \(d=2\), \(K\in\{1,2\}\), and the phase limits have off-diagonal elements \(1/6\) and \(-i/6\), respectively. Therefore
\[
\|\rho^{(1)}-\rho^{(0)}\|_1=\frac{\sqrt2}{3}>0.
\]
Every reset waiting time is finite, and the clock is genuinely random; the persisting phase oscillation is not due to an infinite no-reset probability.

## Relationship to prior work

Wald, Yao, Platini, Hooley and Carollo (arXiv:2410.11497v1, Section II and Section IV; later arXiv:2410.11497v3) introduce precisely the discrete-time quantum reset ensemble with general age-dependent hazards, derive an age-probability recursion and discuss deterministic periodic resets and non-Poisson protocols with nonzero probability of never resetting. Those foundational identities and the deterministic special case are prior results. The present claim instead classifies **all proper finite-mean independent integer renewal clocks** by their arithmetic span; it gives the exact residue-phase density matrices and proves the strict absence of spectral cancellation and the full criterion for ordinary convergence. The cited paper's sections and appendices inspected for this comparison did not provide this classification.

Sevilla and Valdés-Hernández (arXiv:2209.05643v1, Sections 2 and 3.1) derive a renewal representation for continuous-time quantum resetting with arbitrary interarrival densities and analyze equilibrated states where a limit exists. Their continuous interarrival model and conditional equilibrium analysis do not imply the arithmetic integer-clock phase classification. The arithmetic renewal theorem itself is standard probability theory and is not claimed as a new theorem. Indexed related findings involving Poisson qubit resetting, infinite escape probabilities, and continuous Erlang clocks concern different hypotheses or observables.

## Limitations

The result requires a complete reset to one fixed density matrix, an identical unitary gate between resets, independent identically distributed strictly positive integer intervals, and finite mean waiting time. It is about ensemble-averaged state matrices; it does not assert pathwise convergence or independently validated experimental realizability. The generalization to partial resets, state-dependent intervals or infinite-mean proper clocks is not established. The theorem does not quantify finite-time convergence rates without additional tail assumptions. Novelty beyond the inspected sources is subject to broader-literature and independent expert review, particularly because parts of the argument are classical renewal theory applied to an operator-valued observable.

## References

- S. Wald, L. H. Yao, T. Platini, C. Hooley, and F. Carollo, *Stochastic resetting in discrete-time quantum dynamics: steady states and correlations in few-qubit systems*, arXiv:2410.11497v1 (first posted 2024-10-15), https://arxiv.org/html/2410.11497v1; updated published version, *Quantum* **9**, 1742 (2025), https://doi.org/10.22331/q-2025-05-13-1742.
- F. J. Sevilla and A. Valdés-Hernández, *Dynamics of closed quantum systems under stochastic resetting*, arXiv:2209.05643v1 (2022), https://arxiv.org/html/2209.05643v1.
- Elementary arithmetic renewal theorem for positive integer-valued interarrival times of span one (classical result; used as a named standard lemma, not claimed as original).

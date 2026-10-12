# Exact phase-ensemble Pauli fourth moments for arbitrary Born distributions

## Finding
Fix any integer \(n\ge1\) and let \(N=2^n\). For an arbitrary Born probability distribution \(p=(p_x)_{x\in\mathbb F_2^n}\), attach independent uniform phases to its square-root amplitudes, obtaining \(|\psi_\theta\rangle\). Write
\[
C(a)=\sum_{x\in\mathbb F_2^n}p_xp_{x\oplus a},\qquad
K(\psi)=\frac1N\sum_{P\in\{I,X,Y,Z\}^{\otimes n}}\langle\psi|P|\psi\rangle^4.
\]
Then the exact phase-ensemble mean is
\[
\boxed{\mathbb E_\theta K(\psi_\theta)=4\sum_{a\ne0}C(a)^2-2C(0)^2+3\sum_xp_x^4.}
\]
Here \(K(\psi)=2^{-M_2(\psi)}\) for the stabilizer Rényi-\(2\) entropy \(M_2\). In particular, if \(p_x=1/N\) for all \(x\),
\[
\mathbb E K=\frac{4N^2-6N+3}{N^3},\qquad
\mathbb E M_2\ge -\log_2\mathbb EK\ge n-2,
\]
and the rigorous left-tail estimate
\[
\Pr\{M_2\le n-2-t\}\le 2^{-t}\qquad(t\ge0)
\]
holds. Thus phase randomization of the flat-Born state, whose zero-phase member is stabilizer and has \(M_2=0\), produces near-extensive nonstabilizerness in expectation and a quantified one-sided high-probability guarantee.

## Assumptions and scope
All sums over \(x\) and \(a\) are over the finite additive group \(\mathbb F_2^n\), with \(\oplus\) denoting bitwise XOR. The distribution has \(p_x\ge0\) and \(\sum_xp_x=1\). Every \(\theta_x\) is independent and uniform on \([0,2\pi)\); the phase at a zero-probability position is irrelevant. The Pauli set consists of the \(4^n\) Hermitian tensor-product strings without additional global signs. Expectations and probabilities refer only to this independent-phase ensemble. No spatial locality, circuit realizability, or Haar-state assumption is imposed.

## Proof
For each \(a,b\in\mathbb F_2^n\), the Hermitian Pauli string \(P_{a,b}=i^{a\cdot b}X^aZ^b\) has an expectation whose absolute fourth power equals that of the Walsh transform of
\[
c_a(x)=\overline{\psi_x}\psi_{x\oplus a}
=\sqrt{p_xp_{x\oplus a}}\,e^{i(\theta_{x\oplus a}-\theta_x)}.
\]
Indeed, the extra Pauli phase has modulus one and the expectation is real. Define the fixed-XOR sector
\[
K_a=\frac1N\sum_b\left|\sum_x(-1)^{b\cdot x}c_a(x)\right|^4,
\qquad K=\sum_aK_a.
\]
The fourth-power Walsh identity follows by expanding two factors and two conjugates and using \(N^{-1}\sum_b(-1)^{b\cdot w}=\mathbf1_{w=0}\). In the \(a=0\) sector, \(c_0=p\) is real and deterministic, so its fourth Walsh moment is its additive energy,
\[
K_0=\sum_{u\in\mathbb F_2^n}\left(\sum_x p_xp_{x\oplus u}\right)^2=\sum_uC(u)^2.
\]
Fix \(a\ne0\). Translation by \(a\) partitions the positions into disjoint two-element orbits \(O=\{x,x\oplus a\}\). Put \(q_O=p_xp_{x\oplus a}\), which is independent of the chosen endpoint. The random phase of \(c_a\) on one endpoint is opposite to that on the other, and phases on distinct orbits are independent and uniform. In the Walsh fourth-power expansion, averaging phases annihilates every term except those with balanced endpoints in each orbit. Precisely two shapes remain: all four endpoints are in one orbit, with two occurrences of each endpoint (six arrangements), or two orbits each contribute one occurrence of both endpoints (twenty-four arrangements). Each surviving endpoint quadruple has XOR zero, so its Walsh factor equals one. Hence
\[
\mathbb E K_a=6\sum_Oq_O^2+24\sum_{O<O'}q_Oq_{O'}.
\]
Because \(C(a)=2\sum_Oq_O\) and \(D(a)=\sum_xp_x^2p_{x\oplus a}^2=2\sum_Oq_O^2\), this simplifies to
\[
\mathbb E K_a=3C(a)^2-3D(a).
\]
Summing the \(a=0\) sector and all \(a\ne0\) sectors, and using
\[
\sum_{a\ne0}D(a)=\left(\sum_xp_x^2\right)^2-\sum_xp_x^4=C(0)^2-\sum_xp_x^4,
\]
yields exactly the asserted formula. These identities are finite sums, so zeros in \(p\) and all boundary cases are included without limiting arguments.

If \(p_x=1/N\), then \(C(a)=1/N\) for every \(a\), giving \(\mathbb EK=(4N^2-6N+3)/N^3\). By convexity of the negative logarithm, \(\mathbb EM_2\ge-\log_2\mathbb EK\). Moreover \(N\mathbb EK/4=1-3/(2N)+3/(4N^2)\le1\), which proves \(\mathbb EM_2\ge n-2\). Finally, Markov's inequality applied to the nonnegative variable \(K=2^{-M_2}\) at threshold \(2^{-(n-2-t)}\) gives \(\Pr\{M_2\le n-2-t\}\le2^{-t}\). No statement about concentration on both sides is needed.

## Verification
The standalone standard-library script `verify_magic_phase.py` independently computes the complete Pauli sum on all fifth-root phase configurations for six two- and four-amplitude probability vectors, including zero entries; fifth-root quadrature is exact for each monomial arising from the fourth-power phase average. It separately checks the two-orbit enumeration formula against the closed form for 450 additional reproducible probability instances in dimensions two, four, and eight, and the flat-law specialization in eight qubit counts. Its successful output is `VERIFY_OK` with 464 test instances. These computations corroborate the finite algebraic proof; they do not replace it.

## Relationship to prior work
Płodzień, arXiv:2609.32025v1 (2026), Appendix A, develops the same Walsh-sector representation and proves that the positive-square-root amplitude state minimizes \(M_2\) within a prescribed Born distribution. Its numerical methods also sample random phases, but the inspected complete article gives neither the all-distribution exact random-phase mean above nor its flat-law left-tail bound. The present theorem concerns a phase-ensemble **mean of \(2^{-M_2}\)** rather than that paper's deterministic **minimum of \(M_2\)**, so neither statement logically determines the other without the new orbit enumeration.

Turkeshi, Dymarsky, and Sierant, arXiv:2312.11631v2, derive exact Pauli spectra for Haar-random unitary and orthogonal states and numerically study sparse sign-phase states. Haar randomness includes random amplitudes; it is not the fixed-probability independent continuous phase ensemble considered here. Leone, Oliviero, and Hamma (2022) introduced the stabilizer Rényi-entropy functional. Related codeword-stabilized-code magic results of Liu and Xu, arXiv:2608.22017v1, concern structured codeword sets rather than this independent phase average. The universal numerical coefficient \(4\) in the flat-law leading mean agrees with the known generic typical-magic scale, while the exact finite-size correction and distribution-dependent identity distinguish the ensembles.

## Limitations
The derived quantity is \(\mathbb E(2^{-M_2})\), not \(2^{-\mathbb EM_2}\); Jensen provides only a one-sided bound on expected entropy. The high-probability statement controls the low-magic tail and does not establish a central limit theorem or high-magic upper-tail concentration. Independent phases on **all computational-basis amplitudes** are required; general local-depth diagonal random circuits need not generate independent phases. Published priority was checked against the cited related work and public discovery resources, but unindexed equivalent calculations remain possible. The supporting Liu–Xu paper was accessible at abstract level only; its relevance is limited by its codeword-structured setting.

## References
1. M. Płodzień, *Nonstabilizerness of the entangling layer in quantum circuit Born machines*, arXiv:2609.32025v1 (first posted 2026-09-25), especially Sec. III, Appendix A and Appendix B. https://arxiv.org/html/2609.32025v1
2. X. Turkeshi, A. Dymarsky and P. Sierant, *Pauli Spectrum and Non-stabilizerness of Typical Quantum Many-Body States*, arXiv:2312.11631v2, Phys. Rev. B 111, 054301 (2025). https://arxiv.org/html/2312.11631v2
3. L. Leone, S. F. E. Oliviero and A. Hamma, *Stabilizer Rényi Entropy*, Phys. Rev. Lett. 128, 050402 (2022), DOI:10.1103/PhysRevLett.128.050402.
4. Y. Liu and K.-M. Xu, *Quantifying Nonstabilizerness of Codeword-Stabilized Codes*, arXiv:2608.22017v1 (2026). https://arxiv.org/abs/2608.22017

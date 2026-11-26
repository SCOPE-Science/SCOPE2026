# Sharp diagonal-purity frontier for depolarization-resistant qudit entanglement

## Finding

For any integer \(d\ge3\), fix the computational-basis collision purity \(s\in[1/d,1]\) of a pure qudit input. After ideal controlled-shift conversion and global depolarization of weight \(q\in[0,1]\), some input at that purity has negative partial transpose (NPT) if and only if \(q<q_*(d,s)\), where
\[
q_*(d,s)=\frac{d^2L_d(s)}{1+d^2L_d(s)},\qquad
L_d(s)=\begin{cases}
\dfrac{1+\sqrt{(d-2)(ds-1)/2}}{d},&1/d\le s\le1/2,\\
\sqrt{(1-s)/2},&1/2\le s\le1.
\end{cases}
\]
Below \(s=1/2\), the maximizing population spectrum has two equal largest entries and a flat tail (the whole spectrum is uniform at \(s=1/d\)). At \(s=1/2\) the two levels are equally occupied and the tail vanishes. For \(1/2<s<1\), precisely two unequal levels are occupied. At \(s=1\) there is one occupied level; no noise weight, including zero, produces NPT, and the frontier value is \(q_*(d,1)=0\). Over all \(s\), the frontier peaks at \(d^2/(d^2+2)\), above the uniform \(d\)-level threshold \(d/(d+1)\).

## Assumptions and scope

Write \(|\psi\rangle=\sum_j c_j|j\rangle\) and \(x_j=|c_j|^2\), where \(x_j\ge0\) and \(\sum_j x_j=1\). The diagonal purity is \(s=\sum_j x_j^2\); the full input state has purity one. The ideal conversion with a basis-state ancilla gives \(|\Psi\rangle=\sum_jc_j|jj\rangle\). The output is \(\rho_q=(1-q)|\Psi\rangle\langle\Psi|+qI_{d^2}/d^2\). The noise is global, not a tensor product of local channels. The frontier is an open upper boundary of the admissible weights, not an admissible maximum. Equivalently it is their supremum in the ordered interval \([0,1]\), including the empty set at \(s=1\).

## Proof

**Fixed-state threshold.** The partial transpose on the second system has eigenvalues \(q/d^2\pm(1-q)\sqrt{x_i x_j}\) on each pair span \(\{|ij\rangle,|ji\rangle\}\), \(i<j\), and nonnegative eigenvalues \(q/d^2+(1-q)x_i\) on \(|ii\rangle\). Thus, with \(m(x)=\max_{i<j}\sqrt{x_i x_j}\), NPT holds exactly when \(q<d^2 m(x)/(1+d^2m(x))\). The fraction increases with \(m(x)\), so it suffices to maximize \(m(x)\) at fixed \(s\).

**Low-purity branch.** Relabel the two largest populations as \(x_1,x_2\), which achieve \(m(x)\), let \(t=x_1+x_2\), and write \(u=(1/d,\ldots,1/d)\), \(h=(1,1,0,\ldots,0)\). Then
\[
2m(x)\le t=\frac2d+\langle h-(2/d)\mathbf 1,x-u\rangle
\le \frac2d+\sqrt{\frac{2(d-2)}d}\sqrt{s-1/d}.
\]
The candidate attaining both inequalities is \((a,a,b,\ldots,b)\), with \(a=[1+\sqrt{(d-2)(ds-1)/2}]/d\) and \(b=(1-2a)/(d-2)\). For \(1/d\le s\le1/2\), \(0\le b\le a\) and this vector has the required sum and purity. At nonuniform purity, equality in Cauchy–Schwarz fixes \(x-u\) to a positive multiple of \(h-(2/d)\mathbf 1\); at \(s=1/d\) the vector must be uniform. Hence these are precisely the maximizing spectra up to permutation.

**High-purity branch.** For the same pair, \(s+2m(x)^2=t^2+\sum_{j\ge3} x_j^2\le t^2+(1-t)^2\le 1\). Since \(t>0\) for the two largest entries, equality forces \(t=1\). For \(1/2\le s\le1\) the pair of populations
\[
\left(\frac{1+\sqrt{2s-1}}2,\frac{1-\sqrt{2s-1}}2\right)
\]
with zero tail attains equality and is unique up to permutation. At \(s=1\) the second displayed population is zero and every feasible input is a basis state up to phase. Input phases do not affect either branch. Both branches give \(m=1/2\) at \(s=1/2\). They are respectively increasing and decreasing, so this is the unique maximizing purity. Uniform populations give \(m=1/d\). For all input purities, the equality boundary \(q=q_*(d,s)\) has no negative partial-transpose eigenvalue.

## Verification

The accompanying standard-library script `verify.py` checks the optimizer construction on 101 grid points for each of \(3\le d\le18\) and tests the bound on 6,400 random population vectors. Its constructed high-purity vector includes the one-level endpoint at \(s=1\). The analytic inequalities and explicit witnesses, rather than sampling, establish the sharp frontier for every allowed parameter.

## Relationship to prior work

The fixed-input threshold is not new. It is equivalent to Vidal and Tarrach's pure-state random robustness: for Schmidt amplitudes \(a_1\ge a_2\ge\cdots\), their noise-to-signal ratio is \(d^2 a_1a_2\); dividing it by one plus itself gives the mixture weight used here. Ali et al. derive the controlled-shift conversion and the same pairwise partial-transpose spectrum under global depolarization. The uniform input threshold and the unrestricted optimum follow directly from the fixed-input formula (in the latter case \(a_1a_2\le1/2\)). The distinct claim is the two-branch optimum and its attaining spectra at **every fixed collision purity**, including the change in support. Related two-qubit conversion and collective spin noise address different restrictions or channels.

## Limitations

The frontier is for strictly NPT states, not an optimization of negativity magnitude. It does not cover mixed inputs, imperfect conversion, or independent local depolarization. A prior fixed-collision-purity envelope under different terminology has not been ruled out exhaustively.

## References

1. G. Vidal and R. Tarrach, *Robustness of entanglement*, arXiv:quant-ph/9806094, Eq. (41) and Appendix B.
2. A. Ali et al., *High-dimensional coherence to entanglement transduction under canonical noise*, arXiv:2606.16695v1, Eqs. (43)–(49).
3. A. Ali et al., *Quantifying Coherence-to-Entanglement Conversion Efficiency under Noisy Operations*, arXiv:2606.16916.
4. J. Denis and J. Martin, *Extreme depolarization for any spin*, Phys. Rev. Research 4, 013178 (2022), DOI: 10.1103/PhysRevResearch.4.013178.

# Sharp diagonal-purity frontier for depolarization-resistant qudit entanglement

## Finding

For any integer \(d\ge3\), the largest global depolarizing-noise parameter compatible with **negative partial transpose** (NPT) after ideal controlled-shift coherence-to-entanglement conversion, at fixed input diagonal purity \(s\), is
\[
q_*(d,s)=\frac{d^2L_d(s)}{1+d^2L_d(s)},\qquad
L_d(s)=\begin{cases}
\frac{1+\sqrt{(d-2)(ds-1)/2}}d,&1/d\le s\le1/2,\\
\sqrt{(1-s)/2},&1/2\le s\le1.
\end{cases}
\]
The optimal population spectrum changes sharply at \(s=1/2\): below this value two equal largest populations coexist with \(d-2\) equal smaller populations; above it only two levels are occupied. The all-input optimum is \(q_*=d^2/(d^2+2)\) and comes from two equal occupied levels, exceeding the equal-population \(d\)-level threshold \(d/(d+1)\) for every \(d\ge3\).

## Assumptions and scope

The input is a pure \(d\)-level state \(|\psi\rangle=\sum_j c_j|j\rangle\) with populations \(x_j=|c_j|^2\). Its **diagonal purity** means \(s=\sum_jx_j^2\), the collision probability of a projective measurement in the computational basis; the purity of the *full input density matrix* is identically one and is not the quantity held fixed. The populations satisfy \(x_j\ge0\) and \(\sum_jx_j=1\). The fixed target is \(|\Psi\rangle=\sum_jc_j|jj\rangle\), obtained by an ideal generalized controlled shift. The output is \(\rho_q=(1-q)|\Psi\rangle\langle\Psi|+qI_{d^2}/d^2\) for global depolarization \(0\le q\le1\). We optimize **NPT survival**, i.e. strict negativity \(\mathcal N(\rho_q)>0\), and the threshold is the supremum of these admissible \(q\).

## Proof

**1. Partial-transpose spectrum.** Taking the second-system transpose, each distinct unordered pair \(\{i,j}\) supports a two-dimensional invariant block on \(|ij\rangle,|ji\rangle\), with eigenvalues \(q/d^2\pm(1-q)\sqrt{x_ix_j}\). All remaining diagonal eigenvalues are nonnegative. Thus
\[
\mathcal N(\rho_q)=\sum_{i<j}\left[(1-q)\sqrt{x_ix_j}-\frac q{d^2}\right]_+.
\]
Writing \(m(x)=\max_{i<j}\sqrt{x_ix_j}\), NPT holds exactly when \(q<d^2m(x)/(1+d^2m(x))\). Maximizing the threshold therefore amounts to maximizing \(m(x)\) subject to fixed \(s\).

**2. Universal high-purity bound.** Relabel so \(x_1,x_2\) realize \(m(x)^2=x_1x_2\), and put \(t=x_1+x_2\). Since \(\sum_{j\ge3}x_j^2\le(1-t)^2\),
\[
s+2m(x)^2=t^2+\sum_{j\ge3}x_j^2
\le t^2+(1-t)^2\le1.
\]
Hence \(m(x)\le\sqrt{(1-s)/2}\). Equality for \(s\ge1/2\) requires \(t=1\), meaning exactly two occupied levels; their populations are the roots of \(z^2-z+(1-s)/2=0\), namely the values stated above. These values are nonnegative precisely in the regime \(s\ge1/2\).

**3. Sharp low-purity bound.** For \(m=m(x)\ge1/d\), by AM–GM \(t\ge2m\) and \(x_1^2+x_2^2=t^2-2m^2\). Cauchy–Schwarz on the remaining \(d-2\) populations gives
\[
s\ge t^2-2m^2+\frac{(1-t)^2}{d-2}.
\]
The right side is nondecreasing as a function of \(t\) for \(t\ge2m\ge2/d\), because its derivative is \(2t-2(1-t)/(d-2)\ge0\). Thus
\[
s\ge2m^2+\frac{(1-2m)^2}{d-2}.
\]
On \(1/d\le m\le1/2\), this last expression is increasing, with equality at \(m=1/d\) for \(s=1/d\) and at \(m=1/2\) for \(s=1/2\). Solving for \(m\) gives \(m\le[1+\sqrt{(d-2)(ds-1)/2}]/d\) for \(s\le1/2\). If \(m<1/d\), the bound is automatic. Equality forces \(x_1=x_2=m\) and all remaining populations equal to \((1-2m)/(d-2)\). Their sum and square sum directly yield the claimed \(s\), establishing attainment and uniqueness up to permutation/phase. The same equality structure at \(s=1/2\) yields the two-level state.

**4. Global optimum and endpoints.** Both branches of \(L_d(s)\) meet at \(s=1/2\), where \(L_d(1/2)=1/2\); the first is strictly increasing over \([1/d,1/2]\), and the second strictly decreasing on \([1/2,1]\). Therefore \(q_*\) is uniquely largest at \(s=1/2\), with value \(d^2/(d^2+2)\). For the equal-population input \(s=1/d\), \(m=1/d\), giving \(q_*=d/(d+1)\). This latter threshold is strictly smaller whenever \(d>2\). The boundary \(q=q_*\) has zero negativity, not NPT.

## Verification

Run `python3 verify.py` with Python 3 standard library only. The script reconstructs all equality witnesses for \(3\le d\le18\) on 101 diagonal-purity grid points, verifies their normalization and collision purity, and tests the universal inequality on 6,400 randomized population vectors (8,016 checks total). These computations corroborate, but are not used as a replacement for, the analytic proof. In particular no finite randomized check establishes a universal theorem by itself.

## Relationship to prior work

Ali, Rostom, Al-Kuwari, Kuniyil, Rahim and Haddadi, High-dimensional coherence to entanglement transduction under canonical noise, arXiv:2606.16695v1 (15 June 2026). establishes the ideal controlled-shift conversion, the exact pairwise partial-transpose spectrum under global depolarization, and the sudden-death condition governed by the largest amplitude pair; these facts are **imported**, not claimed new. That source reports the equal-population \(d\)-level threshold. The result here optimizes the largest pair at *fixed diagonal purity*, classifies all extremizing input spectra, and identifies the two-level versus fully coherent survival reversal. Previous two-qubit coherence-conversion studies constrain different dimensions. Denis and Martin (2022) study collective depolarization of spin states, a different noise model and state family.

## Limitations

The source preprint was available through indexed full-text extracts, not an uninterrupted full-document download during this analysis; an unindexed prior formulation of the fixed-diagonal-purity envelope remains a priority risk. The result covers pure qudit inputs, ideal conversion, **global** white-noise depolarization, and strictly NPT outputs. It does not assert entanglement absence for every positive-partial-transpose output, optimize the magnitude of negativity at fixed noise, address local depolarizing channels, or cover mixed input states. Global versus independent local depolarization produces different partial-transpose blocks and different optimization questions.

## References

1. Ali, Rostom, Al-Kuwari, Kuniyil, Rahim and Haddadi, High-dimensional coherence to entanglement transduction under canonical noise, arXiv:2606.16695v1 (15 June 2026). https://arxiv.org/abs/2606.16695
2. Asad Ali et al., *Quantifying Coherence-to-Entanglement Conversion Efficiency under Noisy Operations*, arXiv:2606.16916 (2026). https://arxiv.org/abs/2606.16916
3. Jérôme Denis and John Martin, *Extreme depolarization for any spin*, Physical Review Research **4**, 013178 (2022). https://doi.org/10.1103/PhysRevResearch.4.013178

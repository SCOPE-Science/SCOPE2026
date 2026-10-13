# Vanishing-resolution regime for ancilla-free dynamical time-reversal certification
## Finding
Let \(d_n=2^n\), fix \(\tau\in\{+1,-1\}\), and let \(\epsilon_n\in(0,1]\) be any sequence satisfying
\[
\frac{\epsilon_n^2 n}{\log n}\longrightarrow\infty.
\]
For the adaptive-interference protocol without an auxiliary quantum system introduced by Liu, Du, Tang, Liu, Eisert, and Roth, the promise problem
\[
f_\tau(\mathcal U)=1
\qquad\text{versus}\qquad
f_\tau(\mathcal U)\le 1-\epsilon_n
\]
has, for every \(0<\delta\le 1/3\) and all sufficiently large \(n\), worst-case error at most \(\delta\) using
\[
O\!\left(
\frac{2^n\log n}{\epsilon_n^2 n}
\log\frac1\delta
\right)
\]
queries. For fixed \(\delta\), this is \(o(2^n)\), even though \(\epsilon_n\) may tend to zero.

The signature gap has the dynamical interpretation
\[
1-f_\tau(\mathcal U)
=
\Delta_\tau(U)^2,
\qquad
\Delta_\tau(U):=
\frac{\|\Xi_\tau U\Xi_\tau^{-1}-U^\dagger\|_{\mathrm F}}{\sqrt{2d_n}}.
\]
Hence every normalized Frobenius-distance threshold
\[
\Delta_n=\omega\!\left(\left(\frac{\log n}n\right)^{1/4}\right)
\]
can be certified by this no-auxiliary protocol with \(o(2^n)\) queries.

## Assumptions and scope
The unknown operation is an \(n\)-qubit unitary channel reused across queries. The physical time-reversal operator is fixed and known, and the sign \(\tau\) selects either canonical dynamical time-reversal class considered in arXiv:2610.01555v1. The protocol is exactly the source's adaptive-interference construction: all preparations, known controls, and measurements act on the query register alone, quantum systems are discarded after every use, and only classical memory is retained.

The statement is asymptotic and applies to sufficiently large \(n\). It assumes \(0<\epsilon_n\le1\) and the displayed growth condition. It is an achievability statement for this protocol, not a lower bound and not an optimality statement for vanishing gaps.

## Proof
Write \(d=2^n\) and use the source parameters
\[
b=\left\lfloor\frac{\log d}{4\log\log d}\right\rfloor,\qquad
m=\left\lceil\frac db\right\rceil,\qquad
r=\left\lceil\frac{2048d}{\epsilon_n^2b}\right\rceil.
\]
All logarithms in these source parameters are natural. Since
\[
b=(1+o(1))\frac{n\log 2}{4\log n},
\]
the hypothesis \(\epsilon_n^2n/\log n\to\infty\) is equivalent to
\[
\epsilon_n^2b\longrightarrow\infty.
\]

The source proves a good-event estimate
\[
\Pr(\mathsf G)\ge1-\zeta_d,\qquad
\zeta_d=
\frac{2(m+2)}{d+1}
+\frac1{Lh_d}
+\frac4{b+1}
=o(1),
\]
uniformly in the unknown unitary and in \(\tau\). This term contains no adverse dependence on \(\epsilon_n\).

Under the exact \(\tau=-1\) null hypothesis, the base test accepts with probability one. Under the exact \(\tau=+1\) null hypothesis, the source's bound gives
\[
\Pr(\mathrm{reject}\mid H_0^{(+1)})
\le
r\left(\frac1{d+1}+\frac1{2(d-1)}\right).
\]
Because \(r=O(d/(\epsilon_n^2b))\), this probability is
\[
O\!\left(\frac1{\epsilon_n^2b}\right)=o(1).
\]

Under either alternative hypothesis, the source proves
\[
\Pr(\mathrm{accept}\mid H_1^{(\tau)})
\le
e^{-4}+\zeta_d
+\frac{32}{(d+1)\epsilon_n^2}
+\frac{128d}{(d-2)\epsilon_n^2b}.
\]
The last term tends to zero because \(\epsilon_n^2b\to\infty\). The third term also tends to zero: indeed
\[
d\epsilon_n^2
=
\frac db\,(\epsilon_n^2b)\longrightarrow\infty,
\]
since \(d/b\to\infty\). Therefore the base false-acceptance probability tends to \(e^{-4}<1/3\), while the only nonzero base false-rejection probability tends to zero. Thus, for all sufficiently large \(n\), the base test has worst-case error at most \(1/3\).

The base query count satisfies
\[
T_0=m+r
=
O\!\left(
\frac{d\log\log d}{\epsilon_n^2\log d}
\right).
\]
Independent repetition followed by majority vote, exactly as in the source, reduces the worst-case error to any \(0<\delta\le1/3\) using \(O(\log(1/\delta))\) repetitions. Hence
\[
T=
O\!\left(
\frac{d\log\log d}{\epsilon_n^2\log d}
\log\frac1\delta
\right)
=
O\!\left(
\frac{2^n\log n}{\epsilon_n^2n}
\log\frac1\delta
\right).
\]
For fixed \(\delta\), the ratio \(T/2^n\) tends to zero by the assumed growth condition.

Finally, the source identity
\[
1-f_\tau(\mathcal U)
=
\frac{\|\Xi_\tau U\Xi_\tau^{-1}-U^\dagger\|_{\mathrm F}^2}{2d}
=
\Delta_\tau(U)^2
\]
shows that setting \(\epsilon_n=\Delta_n^2\) converts the condition to
\[
\frac{\Delta_n^4n}{\log n}\to\infty,
\]
equivalently \(\Delta_n=\omega((\log n/n)^{1/4})\).

## Verification
The proof is analytic and uses the quantitative inequalities in Appendix C.4 of arXiv:2610.01555v1 rather than a finite experiment. The critical uniformity check is that every \(\epsilon\)-dependent error term in the published fixed-\(\epsilon\) proof vanishes under the single condition \(\epsilon_n^2b_n\to\infty\). The source's \(\zeta_d=o(1)\) estimate is already uniform in the unknown unitary and in \(\tau\).

No numerical computation is used as evidence for the asymptotic statement. The only asymptotic conversion is \(b_n\sim n\log 2/(4\log n)\), obtained directly from \(d_n=2^n\).

## Relationship to prior work
Liu et al. state their no-auxiliary theorem for every fixed \(0<\epsilon\le1\), with query complexity \(O(2^n\log n/(\epsilon^2n))\) at fixed confidence. Their proof retains explicit \(\epsilon\)-dependent error terms, which yield the uniform vanishing-gap regime above but the paper does not state this sequence-level consequence.

Earlier work by Chen et al. and by Hayashi et al. studies antiunitary operator invariance rather than the dynamical condition
\[
\Xi U\Xi^{-1}=U^\dagger.
\]
The recent source explicitly distinguishes these notions. Those papers therefore do not imply the present shrinking-gap statement for the adaptive-interference protocol.

Targeted searches for the exact source identifier, vanishing accuracy, shrinking gaps, the scale \(\sqrt{\log n/n}\) in the signature variable, the scale \((\log n/n)^{1/4}\) in normalized Frobenius distance, and adaptive interference found no statement covering this claim.

## Limitations
The scale \((\log n/n)^{1/4}\) is a sufficient protocol-level crossover for sub-\(2^n\) query count; no necessity or optimality is claimed. The statement does not improve the source's entanglement-assisted protocol, does not address open-system dynamics, and does not apply to the distinct operator-invariance notion called time-reversal symmetry in some earlier quantum-information literature. Constants hidden in \(O(\cdot)\) are not optimized.

## References
1. Z. Liu, Z. Du, Y. Tang, Z.-W. Liu, J. Eisert, and I. Roth, "Efficient certification of time-reversal symmetry requires entanglement," arXiv:2610.01555v1, 2026. Appendix C.4 and Eqs. (9), (237)--(276).
2. Y.-A. Chen, C. Zhu, K. He, Y. Liu, and X. Wang, "Hypothesis testing of symmetry in quantum dynamics," arXiv:2411.14292v2; Phys. Rev. A 111, 052406 (2025).
3. M. Hayashi, Y.-A. Chen, C. Zhu, and X. Wang, "Optimal sample complexity for testing unitary properties," Phys. Rev. A 113, L040402 (2026), doi:10.1103/hv11-djmz.

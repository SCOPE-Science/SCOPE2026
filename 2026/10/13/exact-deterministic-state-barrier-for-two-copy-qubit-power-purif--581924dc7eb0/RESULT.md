# Exact deterministic-state barrier for two-copy qubit power purification
## Finding
For the diagonal qubit family
\[
\rho_p=(1-p)|0\rangle\langle0|+p|1\rangle\langle1|,
\qquad 0\le p\le1,
\]
define the normalized square, or one-round power-purification target,
\[
\mathcal P_2(\rho)=\frac{\rho^2}{\operatorname{Tr}(\rho^2)}.
\]
Then the exact deterministic physical approximation problem from two identical copies is
\[
\inf_{\Lambda\;\mathrm{CPTP}}
\sup_{0\le p\le1}
D\!\left(\Lambda(\rho_p^{\otimes2}),\mathcal P_2(\rho_p)\right)
=
\delta_*,
\]
where
\[
\delta_*=
\frac{\sqrt5-1}{4}\sqrt{\sqrt5-2}
=
0.1501415530003888\ldots .
\]
Here \(\Lambda:(\mathbb C^2)^{\otimes2}\to\mathbb C^2\) is any deterministic completely positive trace-preserving map and \(D(\sigma,\tau)=\tfrac12\|\sigma-\tau\|_1\).

The optimum is attained by the elementary channel that discards either copy and returns the other unchanged. Consequently, on this natural commuting one-parameter family, no deterministic two-copy physical state transformation can uniformly reproduce the normalized square target with trace-distance error smaller than about fifteen percent.

## Assumptions and scope
The input to \(\Lambda\) is exactly two identical copies \(\rho_p^{\otimes2}\), matching a single \(N=2\) power-purification round. The channel is fixed independently of \(p\), deterministic, and trace preserving. The output is one qubit. No restriction is imposed on the channel's internal ancillas, measurements, or coherent processing.

The theorem concerns physical output states. It does not obstruct signed estimators of observables of \(\rho^2/\operatorname{Tr}(\rho^2)\), and it does not address postselected or heralded transformations. It also does not claim an optimal bound for higher powers or larger local dimensions.

## Proof
Write
\[
f(p)=\frac{p^2}{p^2+(1-p)^2},
\]
so that
\[
\mathcal P_2(\rho_p)=
(1-f(p))|0\rangle\langle0|+f(p)|1\rangle\langle1|.
\]

For \(0\le x\le1\), set
\[
p_- = \frac{1-x}{2},
\qquad
p_+ = \frac{1+x}{2}.
\]
The two-copy inputs are diagonal in the computational basis. Their four classical probabilities differ only in the \(|00\rangle\) and \(|11\rangle\) entries, by magnitude \(x\) in each entry, while the two mixed entries agree. Hence
\[
D\!\left(\rho_{p_-}^{\otimes2},\rho_{p_+}^{\otimes2}\right)=x.
\]

The normalized-square targets are also diagonal, and direct substitution gives
\[
f(p_+)-f(p_-)=\frac{2x}{1+x^2}.
\]
Therefore
\[
D\!\left(\mathcal P_2(\rho_{p_-}),\mathcal P_2(\rho_{p_+})\right)
=
\frac{2x}{1+x^2}.
\]

Let
\[
\Delta(\Lambda)=
\sup_{0\le p\le1}
D\!\left(\Lambda(\rho_p^{\otimes2}),\mathcal P_2(\rho_p)\right).
\]
The triangle inequality and trace-distance contraction under the same CPTP map give
\[
\frac{2x}{1+x^2}
\le
2\Delta(\Lambda)+x.
\]
Thus every deterministic channel obeys
\[
\Delta(\Lambda)
\ge
\frac{x(1-x^2)}{2(1+x^2)}.
\]
Maximizing the right-hand side on \([0,1]\), its derivative has the sign of
\[
1-4x^2-x^4.
\]
The unique interior maximizer satisfies
\[
x^2=\sqrt5-2,
\]
and substitution yields
\[
\Delta(\Lambda)\ge
\frac{\sqrt5-1}{4}\sqrt{\sqrt5-2}
=\delta_*.
\]

For the reverse inequality, let \(\Lambda_0\) discard the second input and output the first. Then \(\Lambda_0(\rho_p^{\otimes2})=\rho_p\), so
\[
D\!\left(\rho_p,\mathcal P_2(\rho_p)\right)=|f(p)-p|.
\]
With \(x=|2p-1|\),
\[
|f(p)-p|=
\frac{x(1-x^2)}{2(1+x^2)}.
\]
Its maximum is the same \(\delta_*\). Hence the lower bound is attained and the minimax value is exact.

## Verification
The argument is analytic for the full interval \(0\le p\le1\) and for every deterministic CPTP map. No finite sampling is used to prove the universal quantifiers.

The bundled checker verifies the symbolic one-variable identities, the critical equation, and the numerical value of \(\delta_*\). It is a transcription check only; the channel lower bound itself follows from trace-distance contractivity and the two explicitly evaluated input states.

## Relationship to prior work
Raghoonanan and Byrnes define the same normalized square map and derive the physical SWAP branches
\[
\rho_\pm=
\frac{\rho\pm\rho^2}{1\pm\operatorname{Tr}(\rho^2)}.
\]
Their full text also shows that the ordinary branch average returns \(\rho\), whereas the signed branch average isolates \(\rho^2\). They explicitly describe the non-postselected construction as physical branch dynamics together with signed access to expectation values of the normalized power state. The theorem here does not dispute those estimator identities. It instead determines the exact best deterministic physical-state approximation to the normalized square target on a minimal two-copy qubit family.

Huggins et al. introduced virtual distillation precisely as estimation with respect to \(\rho^M/\operatorname{Tr}(\rho^M)\) without explicitly preparing that state. That result explains why the target is naturally virtual, but it does not quantify the optimal deterministic state-conversion error from the available copies.

A public source-specific review of arXiv:2603.11568 has already emphasized the qualitative distinction between the unconditional physical output and the signed power-state estimator. The present result is narrower but quantitative: it proves an exact minimax obstruction, allows an arbitrary deterministic CPTP transformation of both copies, and identifies an optimal channel and a sharp constant.

## Limitations
The theorem is a one-round \(N=2\) result on a diagonal qubit family. It does not give the optimal approximation for \(N>2\), noncommuting input families, or higher-dimensional systems. It does not constrain postselected purification, heralded success branches, or observable-only virtual-distillation estimators. The exact minimax value is for uniform trace distance over the displayed family; other metrics can have different optima.

The literature comparison found no prior statement of this exact two-copy minimax constant, but an equivalent channel-approximation result could exist under different terminology in nonlinear-map simulation or statistical experiment comparison.

## References
1. J. Raghoonanan and T. Byrnes, *Hybrid Quantum Error Correction and Mitigation by Purification*, arXiv:2603.11568v2 (first public 2026-03-12).
2. W. J. Huggins et al., *Virtual Distillation for Quantum Error Mitigation*, Physical Review X 11, 041036 (2021), DOI 10.1103/PhysRevX.11.041036.
3. Pith, public review record for arXiv:2603.11568 (reviewed 2026-08-02), used only for comparison with the already-public qualitative objection.

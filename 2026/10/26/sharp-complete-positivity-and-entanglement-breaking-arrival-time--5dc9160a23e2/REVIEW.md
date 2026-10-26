# Scientific review of sharp CP/EB arrival times in an affine qubit semigroup

## Correctness — PASS

The map is precisely the affine qubit semigroup of Eq. (41) in Diesel–Bäcker–Strunz (arXiv:2610.20258v1). Its independently reconstructed normalized Choi matrix splits into two Hermitian blocks. Comparing the two determinants reduces complete positivity to \(|e^{-\alpha t}-e^{-t}|\le\sqrt{1-\beta^2}(1-e^{-t})\). Partial transpose exchanges the two anti-diagonal entries, reducing separability and entanglement breaking (via the two-qubit PPT theorem) to \(e^{-\alpha t}+e^{-t}\le\sqrt{1-\beta^2}(1-e^{-t})\). Strict monotonicity yields the exact thresholds. The fixed-parameter singular gap follows by the mean-value theorem, and the critical layer from \(\alpha=1+u/\log(1/s)\). The boundaries \(\alpha=0\) and \(|\beta|=1\) are explicitly handled. A standalone, independently built matrix-unit implementation passed 2,230 finite assertions. Computations are corroboration, not proof of the continuous quantifiers.

## Originality — PASS (qualified best-knowledge)

The October 2026 source establishes the generator's GKSL region and restricted-positivity domains, not the finite-time Choi/PPT arrival equations or their singular gap. The closest broad result is Szczygielski–Chruściński (2024, arXiv:2407.16583), which already defines arrival times and analyzes eventual entanglement breaking in positive and non-GKSL evolution: the concept and qualitative existence are not new. Its phase-covariant examples impose equal transverse Bloch decays, whereas the interesting branch here has distinct transverse rates when \(\alpha\ne1\). Hanson–Rouzé–França (2020) treats Markovian CP semigroups, and Rahaman–Jaques–Paulsen (2018) treats powers of CP channels; neither inspected contribution evaluates the exact anisotropic translated semigroup crossover. Other semantic scientific searches and accessible earlier result statements revealed no stronger statement covering this full claim. These are bounded comparisons; an earlier general anisotropic-qubit result remains a priority risk. The phase-covariant 2020 paper was checked at abstract level only.

## Mathematical value — PASS

For an intentionally non-GKSL semigroup, the first time when the entire Bloch ball is mapped by a legitimate quantum channel matters separately from the later time when it cannot preserve system–reference entanglement. The theorem classifies both phases globally across two natural physical parameters and quantifies the loss of their intervening window near a pure stationary state. The parameter-dependent fractional-power gap and critical logarithmic crossover identify a motivated singular boundary not conveyed by generic eventual-EB existence or a routine Choi eigenvalue calculation. It does not claim experimental implementation or universal validity for arbitrary qubit generators.

## Closest literature and limitations

Diesel–Bäcker–Strunz, *Gaussian and Qubit Semigroup Dynamics beyond GKSL*, arXiv:2610.20258v1 (full Section 4); Szczygielski–Chruściński, *Eventually entanglement breaking divisible quantum dynamics*, arXiv:2407.16583 (full text, especially Eq. (6.2), Theorems 12 and 17); Hanson–Rouzé–França, *Eventually Entanglement Breaking Markovian Dynamics*, arXiv:1902.08173; Rahaman–Jaques–Paulsen, *Eventually Entanglement Breaking Maps*, arXiv:1801.05542v2. The physicality of non-CP early-time maps is expressly excluded. The double-scaling statement fixes nonzero \(u\) and does not cover jointly vanishing \(u\). Independent literature-wide priority and proof validation are not established.

Self-review: passed. Independent audit: not yet performed.

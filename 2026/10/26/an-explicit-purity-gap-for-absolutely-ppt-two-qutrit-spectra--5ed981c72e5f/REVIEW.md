# Review

## Correctness — PASS

For ordered probability spectra in \(\mathcal S_9\), the fifteen vertices are enumerated exactly. Their purity values give the unique outer maximum \(25/169\), second value \(11/75\), and the exact constants \(\gamma=16/12675\), \(q_0=16/845\), and \(D^2=58/1183\). The first qutrit Hildebrand matrix at the outer maximizer has least eigenvalue \(-(2\sqrt2-2)/13\). Its Frobenius perturbation bound forces every APPT spectrum to lie at Euclidean distance at least \((\sqrt2-1)/13\), which yields the stated rational gap by the two quadratic bounds in the proof. The standard-library verifier confirms the finite rational calculations; the remaining inequalities are proved analytically.

## Originality — PASS, subject to documented risk

Tran's primary paper proves that the APPT purity is strictly below the outer-polytope maximum for \(3\otimes n\), and explicitly leaves the exact maximum open. Its strictness argument does not state the rational gap \(12544/27568125\). The 2026 two-qutrit classification paper supplies the explicit Hildebrand matrix but does not state this purity-gap bound. The claim is a quantitative corollary from those ingredients, not a solution of the exact optimization problem. The literature comparison is best-knowledge only; absence from search results is not proof of priority.

## Mathematical value — PASS

The result replaces a qualitative strict inequality with an explicit, reproducible rational margin in the smallest qutrit–qutrit case. This gives a rigorous exclusion threshold for interval or numerical investigations of the still-open exact maximum and rules out the outer-polytope extremizer with a stated quantitative separation. The constant is not sharp, and no practical tightness is claimed.

## Closest literature and limitations

- A. T. Tran, *Spectral Optimization for Absolutely PPT States: Purity, Entropy, and Volume Decay*, arXiv:2609.18568, especially the outer-polytope maximizer and the proof of strictness in \(3\otimes n\).
- R. Hildebrand, *PPT from spectra*, arXiv:quant-ph/0502170; the spectral criterion supplies necessary linear matrix inequalities.
- N. Wang, L. Chen, and Z. Song, *Extreme points of absolutely PPT states with exactly three distinct eigenvalues*, arXiv:2603.20717, including the explicit two-qutrit matrices.

The result is only an upper bound for \(3\otimes3\) APPT states. It does not determine the true maximum, characterize maximizers, or establish a bound for all \(3\otimes n\). Independent audit remains unperformed.

Self-review: passed. Independent audit: not yet performed.

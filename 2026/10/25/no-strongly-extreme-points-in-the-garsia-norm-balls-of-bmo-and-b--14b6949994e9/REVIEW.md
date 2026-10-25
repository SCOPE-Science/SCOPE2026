# Scientific review

## Correctness — PASS

For every unit \(f\in\mathrm{BMO}\), the Poisson variance tends to zero nontangentially at any common Lebesgue point of \(f\) and \(|f|^2\). The explicitly normalized Möbius perturbations \(g_a=b_a+a\) are in VMOA, have Garsia norm exactly one, and their variance superlevel sets contract into a fixed Stolz region at that boundary point. Hence \(\Delta_r=\sup\min(V_f,V_{g_a})\to0\); the centered Poisson \(L^2\) triangle inequality gives \(\|f\pm g_a\|_G\le1+\sqrt{\Delta_r}\). These steps prove absence of strongly extreme points in all four stated balls; lower-norm points are excluded separately. No computation or unchecked approximation is used to justify the universal quantifiers.

## Originality — PASS, subject to residual historical-priority risk

The focal paper [1] explicitly proposes describing strongly extreme points of the Garsia-norm BMO/BMOA balls. Its inspected Section 2 and addendum do not supply this answer. The full relevant statements and discussions in [2] establish *ordinary* Garsia-extremity for norm-attaining functions and VMO but not strong extremity; stronger implications do not follow from its claims. Classical strongly extreme theorems in \(H^\infty\) use the supremum norm, while Axler–Shields' BMO/VMO extremity concerns a different, arc-average norm. Targeted searches did not identify a prior theorem with the exact four-space classification, but indexing gaps and earlier literature may contain an equivalent result.

## Value — PASS

This is a full answer to the explicitly proposed strong-extremity variant, simultaneously on BMO, BMOA and their vanishing-oscillation subspaces. The contrast with [2] is structural rather than quantitative: every Garsia-unit VMO point is *ordinary* extreme, yet none is strongly extreme. The construction handles arbitrary unbounded BMO data using only Lebesgue-point localization, and yields perturbations in the disk algebra even in the nonanalytic case.

## Closest literature and limitations

[1] K. M. Dyakonov, *The Strong Reproducing Kernel Thesis for Hankel Operators and the Garsia Norm*, arXiv:2609.33242 (first posted 2026-09-27), Section 2 and Addendum. [2] K. M. Dyakonov, *Extremal Problems in BMO and VMO Involving the Garsia Norm*, arXiv:2404.05565 (first posted 2024-04-08), Theorem 2.7 and Corollary 2.8. Strong extremity is norm dependent, and the ordinary extreme-point problem for general BMO/BMOA is untouched. Independent priority verification remains outstanding.

Self-review: passed. Independent audit: not yet performed.

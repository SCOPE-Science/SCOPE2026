# Scientific review

## Correctness

**PASS.** All quantifiers and boundaries are explicit: fixed \(\beta\ge0\), positive deterministic weights, independent parent choices, and tree order \(n\to\infty\). The insertion-depth generating function, conditional weighted-depth martingale, and exact orthogonal variance identity follow from the parent law. For \(\beta<1\), summable squared hub probabilities times logarithmic depth moments yield almost-sure and \(L^2\) convergence; the centering correction is an absolutely convergent series. For \(\beta\ge1\), two old hubs always retain positive fractions of attachment mass and have distinct expected depths, giving a uniform martingale-innovation variance lower bound at each dyadic time and a logarithmically divergent normalized variance. The exact finite checker tests the core identities but does not replace these infinite proofs.

## Originality

**PASS, with bounded historical risk.** The 2026 motivating work supplies the innovation identities and a sufficient \(O(1/n)\) condition; it explicitly identifies irregular deterministic weight sequences as an open direction. Its sufficient theorem does not imply the dyadic classification when \(\beta>0\). Sénizergues's stronger profile analysis may cover the \(\beta<1\) side, and the positive side alone is not advanced as novel. The joint boundary classification, notably normalized variance divergence at every exponent \(\beta\ge1\), was not located in the accessible literature or mathematical-record comparisons. Kuba–Panholzer (2007) could only be checked from its abstract; broader historical coverage therefore remains possible.

## Value

**PASS.** This resolves a specific, naturally scaled test family for a published open boundary question: geometric sparse arrivals have negligible aggregate weight below a linear exponent but retain macroscopic parent-selection mass at and above it. The theorem proves a strict transition between finite nonzero linear-scale variance and a variance diverging at least logarithmically. This is a structural boundary for tree-depth fluctuations rather than a numerical experiment, an arbitrary finite slice, or a reparametrization of a known result.

## Related sources and limits

The closest primary works are Gałązka–Wdowicka (2026, arXiv:2610.00614) and Sénizergues (2019/2021, arXiv:1904.07115). Additional related context is Mailler–Uribe Bravo (2018/2019, arXiv:1810.02735) and Kuba–Panholzer (2007, DOI:10.1017/S0269964807000058). A stronger historical theorem specialized to sparse irregular attachment weights remains an originality risk. The theorem does not give tightness or a limiting law for exponents at or above the threshold.

Self-review: passed. Independent audit: not yet performed.

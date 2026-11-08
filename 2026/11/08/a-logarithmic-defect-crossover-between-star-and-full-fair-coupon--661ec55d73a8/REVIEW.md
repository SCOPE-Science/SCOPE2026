# Self-review

## Correctness

**PASS.** The missed-set representation gives exact factorial moments for all integers \(N,M,t\), with pairwise negative covariance proving \(\mathrm{Var}(U_t)\le\mathbb EU_t\). Stirling's formula gives the critical mean \(e^x/\sqrt{2\pi}\); for every fixed factorial order, growing-time errors are bounded by \(O_r((c+1)/M+(c+1)/N)\). Factorial moments then imply Poisson convergence, and Chebyshev/Markov locate the cover time in adjacent rounds. The two-sided expectation-tail estimate proves convergence of the mean, while the exact star-stage identity and a duplicate-center union bound finish the comparison. The limits \(x\to\pm\infty\) are interpreted only through sequences satisfying the stated \(o(\log m)\) restriction. The standalone `verify.py` produced 131 finite passes; these do not replace the infinite proof.

## Originality

**PASS (provisional historical assessment).** The closest paper is Barak-Pelleg and Berend, arXiv:2606.28216, whose star analysis treats a fixed center deficit and a proportional regime, not logarithmically growing deficit. Berend and Sher, arXiv:2605.06953, prove a fixed-critical-integer Poisson regime; their assumption does not yield a conclusion with a diverging critical draw count. The candidate's new combined assertion is the centered logarithmic star/full expectation transition and its two-point law. Published mathematical record searches and the accessible local research ledger revealed no equivalent or stronger covering statement. An older general group-drawing Poisson estimate could imply the isolated full-model count under nontrivial uniformity checks, so priority remains subject to independent assessment.

## Mathematical value

**PASS.** The first fair star/full comparison has opposite expectation orderings for fixed deficit and fixed-proportion parameters. The logarithmic intermediate scale explains the onset of a full-round gap and gives the exact crossover profile; it is a natural missing regime of a published comparison, not an arbitrary parameter slice. The proof also shows why full sampling has a rare-event Poisson obstruction while star sampling finishes at the information-theoretic minimum number of rounds.

## Literature and limitations

Closest sources: Barak-Pelleg–Berend (2026), Sections 2.2, 4, 5; Berend–Sher (2026), Theorem 2.3 and Proposition 3.1; Berend–Sher (2025/2026), Sections 1–2. The theorem is only for the specified two mechanisms and logarithmic defect. It neither proves global extremality among fair mechanisms nor determines a convergence rate. The checker is a finite consistency test, and historical priority is not independently certified.

Self-review: passed. Independent audit: not yet performed.

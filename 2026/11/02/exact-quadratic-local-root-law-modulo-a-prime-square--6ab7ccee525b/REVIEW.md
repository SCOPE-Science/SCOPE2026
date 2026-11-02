# Scientific assessment: exact quadratic local root law

## Correctness — PASS

The domain is all nonzero coefficient triples of degree at most two modulo \(p^2\), with no monicity or separability restriction. The proof partitions reductions modulo \(p\) into zero-root, one-simple-root, two-simple-root and one-singular-root classes, with an independent zero-polynomial branch. For every prime, the respective counts are obtained by elementary coefficient classification; characteristic two is checked separately at the singular-root step. The Hensel lifting step yields either \(p\) or zero roots from a singular reduction, with exactly \(p^2\) successful coefficient lifts. Adding the branches and excluding exactly the all-zero coefficient triple gives the five-term law. Exhaustive enumeration for \(p=2,3,5,7\) also checks the first two moments directly. The independent pair-evaluation argument verifies the formula \(\mathbb E R^2=3-2/p\) before exclusion. Finite enumeration is corroboration, not the proof for all primes.

## Originality — PASS, subject to residual priority risk

Simhi's Lemma 3.4 gives only an upper bound on moments for arbitrary degree, and Appendix Lemma A.2 gives a lower probability bound for the singular event; neither specifies this five-term conditional distribution, the exact first two moments, or leading high-moment constant. Sofos's global counting results do not imply the local exact coefficient distribution. Existing studies of random \(p\)-adic field roots distinguish infinite lifts, while the current count includes modular roots that can die at the next lifting step. Literature searches for root-count laws, their probability generating functions, and aliases found no decisive covering result. An unlocated exact polynomial-over-finite-ring law remains a real priority risk, especially given the elementary proof. No novelty guarantee or independent priority certificate is claimed.

## Mathematical value — PASS

The object \(\rho_g(p^2)\) is the exact local factor used in the newly published random-squarefree-polynomial model, and the first nonlinear degree is a natural calibration regime. The full law proves the recent general bound's exponent is sharp in quadratic degree and identifies its leading constant. Its rare singular-lift tail produces an explicit, somewhat counterintuitive separation between weak convergence and second-moment convergence. This is a self-contained structural local result, not an arbitrary numeric cutoff or a claimed extension of the global limit law.

## Limits and closest literature

The result is for coefficient-uniform quadratic local models only. It does not address degree at least three, higher prime powers, monic ensembles, or global squarefree-density distributions. The primary full-text comparisons were Simhi arXiv:2610.29911v1, Sofos arXiv:2601.19319v1, Bhargava–Cremona–Fisher–Gajović DOI:10.1112/plms.12438, Caruso's random p-adic zero study, and Hakami's finite-ring quadratic-form bound. Historical priority remains subject to specialist review.

Self-review: passed. Independent audit: not yet performed.

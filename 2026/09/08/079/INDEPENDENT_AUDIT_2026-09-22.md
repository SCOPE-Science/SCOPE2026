# Independent Audit — 2026-09-22 campaign

**Record:** `2026/09/08/079`  
**Audit performed:** 2026-09-26 UTC  
**Audited source tree:** `722cc250190a4b5901cd8372ad6b70f6051f8db0`

## Claim audited

The record gives exact minimum string-attractor sizes and witnesses for dyadic prefixes through length 64 of the Rudin–Shapiro and regular-paperfolding words, plus certified finite bounds for larger dyadic prefixes.

## Correctness — PASS

I re-derived both binary words directly from the definitions in the record; the length-64 prefixes match the committed strings. I then constructed, independently of the committed solver, the family of occurrence spans for every distinct factor and solved the resulting minimum hitting-set problems for all twelve exact instances (two words at lengths 2,4,8,16,32,64).

The exact optima reproduce the claimed sequences:

- Rudin–Shapiro: (1,2,2,4,5,8).
- Regular paperfolding: (1,2,2,3,4,5).

Every committed witness was independently cover-checked against every distinct factor. The exact distinct-factor totals through length 64 also match the record: RS (2,7,23,101,418,1730), PF (2,8,26,100,407,1631). The larger-prefix claims are correctly presented as bounds rather than exact minima.

## Originality — PASS, finite-scope claim

Schaeffer–Shallit, *String Attractors for Automatic Sequences* (arXiv:2012.06840), develops the automatic-sequence attractor framework and decidability results and treats other canonical sequences, but I found no Rudin–Shapiro or regular-paperfolding table matching these finite exact minima and witnesses. Kempa–Prezza supplies the general string-attractor framework; OEIS factor-complexity entries concern a different invariant and do not imply the attractor hitting sets.

The originality finding is only for this finite exact inventory and its certificates. It does not claim an infinite-family formula or resolve the eventual asymptotic side for either word.

Relevant sources:
- https://arxiv.org/abs/2012.06840
- https://arxiv.org/abs/1710.10964
- https://oeis.org/A020985
- https://oeis.org/A014577
- https://oeis.org/A337120

A later author note records a gap in part of Theorem 18 of the Schaeffer–Shallit paper; this audit does not rely on the affected claims. The finite computations here stand independently.

## Scientific value — PASS

Rudin–Shapiro and paperfolding are canonical automatic words, and minimum attractor size is a standard compression invariant. Exact optimal witnesses through length 64 and reproducible larger-prefix bounds are useful benchmark instances for attractor solvers and experiments on automatic-sequence compression. The contribution is deliberately finite and computational.

## Final disposition

**PASS.** Correctness, narrow finite-scope originality, and benchmark scientific value are supported.

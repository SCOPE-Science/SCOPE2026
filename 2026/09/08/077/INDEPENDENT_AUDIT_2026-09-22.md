# Independent Audit — 2026-09-22 campaign

**Record:** `2026/09/08/077`  
**Audit performed:** 2026-09-26 UTC  
**Audited source tree:** `6a597ecc02b28816663aeea6002850a851242690`

## Claim audited

The record gives exact Ehrhart data, h*-vectors, and explicit non-IDP witnesses for the three reflexive 6-simplices on the precommitted line (a(t)=(1,1,2,2,2,t)), (t\in\{1,3,9\}).

## Correctness — PASS

I independently reconstructed the facet inequalities and counted lattice points by exact integer stars-and-bars slicing. The recount reproduces the committed (L(k)) values through (k=9) for all three members:

- (t=1): 1, 8, 37, 128, 366, 911, 2038, 4187, 8023, 14506.
- (t=3): 1, 8, 37, 130, 380, 967, 2206, 4607, 8947, 16354.
- (t=9): 1, 9, 46, 172, 522, 1360, 3151, 6651, 13015, 23923.

From those counts I independently recovered the stated h*-vectors
((1,1,2,2,2,1,1)), ((1,1,2,4,2,1,1)), and ((1,2,4,4,4,2,1)). They are palindromic, sum to the normalized volumes 10, 12, and 18, and are unimodal. The three stated witnesses lie in (2P), and exhaustive splitting against all lattice points of (P) finds no representation as (p_1+p_2), proving non-IDP in each case.

## Originality — PASS, narrowly scoped

Braun–Davis–Solus, *Detecting the Integer Decomposition Property and Ehrhart Unimodality in Reflexive Simplices* (arXiv:1608.01614), proves the relevant IDP/unimodality result for the two-part family (q=(r^m,s^x)) and explicitly treats broader simplex classes as further/open directions. The (t=1) member is a two-part control and is therefore structurally covered by that theorem. The (t=3,9) weight systems are genuinely three-part and fall outside that theorem.

The originality finding is limited to the exact finite data/certificate layer for this specified line: the three Ehrhart polynomials/h*-vectors together with explicit 2P nondecomposition witnesses. No new general Hibi–Oda theorem is claimed, and the segment-wide implication IDP => unimodal is vacuous because no member is IDP.

Relevant open-access source: https://arxiv.org/abs/1608.01614

## Scientific value — PASS

The record supplies a reproducible small-dimensional benchmark at the first dimension where Gorenstein h*-nonunimodality phenomena arise. Exact Ehrhart polynomials, h*-vectors, and explicit non-IDP witnesses are useful test data for implementations of weighted-projective/reflexive-simplex invariants and for experiments around the IDP/unimodality boundary. Its value is finite and computational rather than a new general theorem.

## Final disposition

**PASS.** Correctness, originality (with the narrow scope above), and scientific value are all supported.

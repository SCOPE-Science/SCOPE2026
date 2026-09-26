# Independent audit — 2026-09-26

Record: `2026/09/09/048`. Verdict: **correctness PASS; originality PASS (explicit specialization); scientific value PASS (correlation only).** Disposition: retain accepted.

## Correctness
For h≠0, the translated sheaf is lisse at 0 while the quadratic Kummer twist of Kl2 is nontrivially tame there. Geometric irreducibility therefore prevents an isomorphism F≈[+h]*F, so the geometrically constant summand of F⊗F_h^∨ is absent and H²_c vanishes. On P¹ minus {0,−h,∞}, rank 4 and χ_c=−1 give dim H¹_c=4+Swan∞. Each factor's infinity slopes are 1/2; tensor slopes are at most 1/2, hence Swan∞≤2, dim H¹_c≤6. The two omitted points contribute zero by K_a(0)=0. Deligne's weight estimate gives |C(h)|≤6√p and thus the announced 12√p, uniformly for odd p, a≠0, h≠0. This checks the actual sheaf argument, conditional on Katz's established local monodromy and Weil II. I independently evaluated the defining exponential sums for all 17 odd primes ≤61 and every nonzero h at a=1: largest ratio 2.63866611076 occurs at p=53, h=18 and equivalently h=35 by C(−h)=conj C(h). The record naming only h=35 omits that symmetric tie, without affecting the bound.

## Prior work and originality
Katz's Kloosterman local data and the general sheaf-correlation/Weil estimates are prior. Fouvry–Kowalski–Michel et al., arXiv:1508.00512, study short trace-function sums; the cited bilinear literature develops much broader machinery. I found no exact quadratic-twisted translated pair and explicit constant 6 in the compared open sources. Originality is confined to this specialization and its conductor arithmetic, not a new method or Burgess-range estimate.

## Scientific value and limits
A uniform empty-exception correlation bound is a usable complete-sum input. The claimed p^0.46 short-sum power saving is expressly absent: correlation alone does not supply amplifier bookkeeping, so no short-sum result is credited. The proof is mathematical given the cited sheaf theorems; small-prime computation is only corroboration.

Sources: RESULT.md and output/artifacts/verify.py; Katz, *Gauss Sums, Kloosterman Sums, and Monodromy Groups*, Theorem 4.1.2; https://arxiv.org/abs/1508.00512; https://arxiv.org/abs/2511.09459.

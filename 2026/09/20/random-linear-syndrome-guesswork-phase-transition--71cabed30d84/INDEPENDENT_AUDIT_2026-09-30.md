# Independent audit — 2026-09-30

**Record:** `2026/09/20/random-linear-syndrome-guesswork-phase-transition--71cabed30d84`  
**Audited source tree:** `2f197e5e946ba7a83f95418eaeaef6ef16682868`  
**Disposition:** passed

## Correctness — PASS

PASS. For fixed x, G_H(x)-1 is the number of earlier likelihood-ranked difference vectors killed by H. Expanding integer moments by the span rank d gives annihilation probability q^{-md} and a valid O_{q,j}(M^d) count of rank-d tuples, yielding the required upper moments. For 0<rho<1, the second-moment bound E Z^2 <= (q-1)mu+mu^2 follows because each nonzero vector has at most q-2 other nonzero scalar multiples in the set; Paley--Zygmund supplies the lower bound for mu>=1 and G>=1 handles mu<1. Jensen/Lyapunov cover rho>=1. The uniform full-row-rank case uses the exact fixed-subspace containment probability; the small-kernel endpoint has bounded proxy and is covered by G>=1. The exact first-moment coefficients are correct. Arikan's one-shot bound plus the finite moment law gives rho[h_alpha-r]_+, while a cellwise Arikan/convexity converse applies to every encoder; deterministic lower bounds plus ensemble Markov control give the typical-matrix exponent. I also exhaustively enumerated a small binary instance and recovered the exact first-moment identity. The full-row-rank variant is, as usual, understood only when m<=n.

## Originality — PASS

PASS, with adjacent-literature risk. Tavakoli's 2026 coset-guesswork theorem gives the affine exponent under explicit subcriticality conditions; it does not state the all-rate positive-part theorem. Arikan and Bunte--Lapidoth already supply the unconstrained guesswork and arbitrary-task-encoder Rényi bounds, and random binning is established prior art. I found no inspected source giving the source-independent finite constant-factor moment law for uniform random linear syndrome maps, its exact one-shot first moment, or the conclusion that this structured linear ensemble is exponent-optimal at all rates. Because universal-hashing/random-binning literature is broad, the originality conclusion is appropriately qualified.

## Scientific value — PASS

PASS. The finite-length collision-moment law is a reusable structural statement stronger than an IID weight-enumerator exponent. It closes the low-rate side of a recent coset formula, applies to arbitrary source sequences with a Rényi entropy rate, and reveals a moment-dependent phase transition while retaining structured linear encoding.

## Independent checks

- Reconstructed the rank-d tuple moment bound and the rho<1 Paley--Zygmund argument.
- Checked the full-row-rank subspace-containment formula and endpoint behavior.
- Exhaustively enumerated a q=2,n=3,m=2 example, obtaining E_H G_H=2.25=1+2^-2(G0-1).
- Compared the theorem assumptions directly with Tavakoli's current preprint and with classical Rényi task-encoding results.

## Literature evidence

- https://arxiv.org/abs/2607.00205 — Tavakoli (2026), closest recent coset-guesswork result; the main exact exponent theorem is stated under subcriticality conditions.
- https://doi.org/10.1109/18.481781 — Arıkan (1996), classical one-shot Rényi guesswork inequality used in the exponent step.
- https://arxiv.org/abs/1401.6338 — Bunte and Lapidoth (2014), arbitrary task-encoder Rényi threshold; this makes the unstructured encoder converse prior art.

## Limitations

- Constants are for fixed q and are not claimed uniform if q grows with n.
- The theorem concerns optimal likelihood-ordered guessing, not an efficient implementation of that order.
- Only the leading exponential rate is claimed; sharp logarithmic second-order terms are outside scope.
- The full-row-rank ensemble exists only for m<=n, which is the implicit domain of that variant.

No GitHub write was performed by the audit chat. This file is staged by the guarded `scope-audit-change-set-v1` plan only.

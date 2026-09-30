# Independent Audit — A 186,821,495-element non-cancelling-intersections counterexample bound

Audit date: 2026-09-29 (UTC)
Record path: `2026/09/17/a-186-821-495-element-non-cancelling-intersections-counterexample-bound--defc451df7ae`
Audited tree: `49ad3c2efb83122eda7d7aebd3669cf54ebe4092`

## Disposition

**PASSED** — All three audit axes pass, subject to the explicit qualifications below.

## Correctness

**PASS**. The refined first-moment certificate checks. For a t-set T in the affine plane, the identities sum j_l=t(p+1) and sum j_l^2=t(t+p) are correct. Bounding the number of nonempty lines by p(p+1) gives sum_{j_l>=2}(j_l-1)>=(p+1)(t-p); Cauchy–Schwarz therefore yields N>=(p+1)^2(t-p)^2/[t(t+p)]. Removing lines with j_l>=20 leaves the stated real lower bound S(t) on traces of size 2,...,19. At p=571,w=35, the exact hit probability is about 0.7053150868<353/500; the derivative lower bound is 389246/14275>27; the successive union-bound terms contract by <0.023623<1/40; S(2p)=328042/15>21869; and the exact integer comparison used with e<11/4 gives the first term <7/20. Thus the total expected number of admissible T in [2p,4p] is <14/39<1. Wilhelm's public abstract states precisely that a marking with no admissible set in this size interval is the ingredient excluding a winning dot-algebra representation. The lattice-size arithmetic p^3+2p^2+2=186,821,495 is exact.

## Originality

**PASS**. Wilhelm's arXiv:2608.27416 gives the same structural marked-plane method only for every prime p>=10^5. Searches for p=571, 186821495, and equivalent smaller-parameter NCI certificates did not locate the audited numerical sharpening. The conceptual mechanism is inherited and is not credited as new; the originality lies in the substantially tighter incidence/trace estimate and concrete parameter certification.

## Scientific value

**PASS**. The contribution is quantitative rather than conceptual, but the compression is scientifically meaningful: it lowers the documented explicit lattice-size upper bound from roughly 10^15 (the p=100003 scale reported in the record) to 186,821,495 while staying inside the published structural framework. This directly addresses the size of a concrete counterexample and is backed by an exact finite certificate, so it clears the threshold for a substantive quantitative lemma/note even though p=571 is not claimed minimal.

## Literature evidence

- https://arxiv.org/abs/2608.27416 — Wilhelm, Refutation of the Non-Cancelling-Intersections Conjecture, posted 2026-08-27; public abstract states that no admissible set of size 2p through 4p suffices and that every prime p>=10^5 works.
- https://arxiv.org/abs/2401.16210 — Amarilli–Monet–Suciu, original NCI conjecture context.

## Independent checks

- Re-derived the affine-plane moment identities and the Cauchy lower bound on lines with trace size at least two.
- Computed q=1-C(552,35)/C(571,35)≈0.7053150868<353/500 and all exact derivative/geometric-tail inequalities.
- Verified p=571 is prime and p^3+2p^2+2=186,821,495.

## Limitations

- The audit independently verifies the new numerical/probabilistic step; it relies on Wilhelm’s published structural implication as stated in the accessible public source rather than re-proving the entire lattice/dot-algebra reduction.
- The construction is existential and p=571 is not claimed minimal.
- No inaccessible paper is represented as read.

GitHub was used only as read-only evidence. The repository tree matched the assigned tree exactly.

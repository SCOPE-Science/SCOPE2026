# Independent Audit — 2026/09/20/prime-degree-hurwitz-maximal-monodromy--8fc9ce1cb33f

- Audit date: 2026-09-30 (UTC) (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Branch: `main`
- Inventory commit: `e9ed144c13b7834896a844cc4f9cac3c25a168a6`
- Source-tree checked commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `c3afe9ff9309ecabc6737eeca5c49e4c2b312a87`
- Disposition: **PASSED**

## Correctness

**PASS** — The local cycle criterion and all group-theoretic consequences are correct. If q occurs exactly once and divides no other part, raising the branch cycle to the lcm of the other parts leaves a single nontrivial q-cycle; conversely, a power that is a single q-cycle forces the supporting original cycle to have length q uniquely and every other cycle length to divide that power, so none can be divisible by q. A connected degree-p realization is transitive and hence primitive because p is prime. Jordan's theorem then forces A_p<=G, while the parity of the prescribed cycle defects selects A_p versus S_p. The point stabilizer in the natural A_p/S_p action is self-normalizing, so the deck group is trivial. The normal-closure genus formula is exactly Riemann-Hurwitz with inertia orders lcm(Lambda_i). The two degree-seven examples and their genera recompute correctly.

## Originality

**PASS** — Song-Wen-Zhang (2026) provide the new universal prime-degree Hurwitz existence theorem but do not, in the located text, state this partition-level Jordan-visibility criterion or the resulting every-realization A_p/S_p rigidity. Jordan's theorem, prime-degree primitivity, normalizer formulas, and use of small cycles in Hurwitz theory are classical and are not claimed new. The contribution is the exact passport-local criterion combined with universal realizability, which upgrades existence to a forced-monodromy theorem. Searches for the same criterion in prime-degree Hurwitz/passport language found only broader classical Jordan applications, not this statement.

## Scientific value

**PASS** — On an explicit and easily checked locus of prime-degree passports, the result determines the geometric monodromy of every connected realization, proves trivial deck groups, and gives the Galois-closure degree and genus directly from the passport. This is a useful structural strengthening of the new existence theorem even though Jordan visibility is only sufficient, not necessary.

## Sources

- **The Hurwitz existence problem in prime degree** — Jijian Song; Hailin Wen; Zebao Zhang. https://arxiv.org/abs/2609.20572 — Primary 2026 existence theorem: every compatible branch datum of prime degree over the sphere is realizable by a connected cover.
- **Primitive Permutation Groups Containing a Cycle of Prime-Power Length** — Peter M. Neumann. https://doi.org/10.1112/blms/7.3.298 — Classical Jordan-type permutation-group background.
- **Harbater-Mumford subvarieties of moduli spaces of covers** — Anna Cadoret. https://doi.org/10.1007/s00208-005-0680-0 — Prior use of prime-degree primitivity and small-cycle/Jordan arguments in Hurwitz-space constructions.

## Limitations

- Jordan visibility is sufficient but not necessary for maximal monodromy.
- Passports outside the criterion can still realize A_p or S_p and are not classified here.
- The existence source is a very recent preprint, so later revisions or concurrent work remain a priority risk.

## Independent checks

```json
{
  "local_cycle_criterion_reconstructed": true,
  "jordan_step_checked": true,
  "parity_dichotomy_checked": true,
  "deck_normalizer_checked": true,
  "riemann_hurwitz_examples_checked": true,
  "open_access_first": true,
  "oxford_used": false
}
```

The assigned record tree was unchanged between the inventory commit and the source-tree-check commit. GitHub was used only as read-only evidence and no repository mutation was performed. Open-access and preprint sources were checked first; no decisive comparison required institutional retrieval in this audit.

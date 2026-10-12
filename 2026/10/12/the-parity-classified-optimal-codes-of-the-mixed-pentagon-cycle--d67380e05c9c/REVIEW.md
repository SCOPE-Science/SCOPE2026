# Scientific review: mixed pentagon–cycle optimal code classification

## Correctness — PASS

The exact claim holds for all integers \(n\ge6\) on the stated labeled alphabet. The pivotal covering lemma is checked explicitly: each independent two-set of \(C_5\) has closed-neighborhood union all of \(\mathbb Z/5\mathbb Z\); consequently neighboring columns are empty. The count of empty and doubly occupied columns gives the universal upper bound \(n\). Equality makes the doubly occupied-column set invariant under a shift of two, forcing either all singleton columns or, on even cycles, alternating empty/double columns. Cyclic closed walks enumerate the singleton family; five pair choices in each occupied column enumerate the other. Construction and spectrum complete the proof, including boundary and parity cases. The exact-integer column transfer checker and a separate exhaustive column enumerator agree through the stated finite ranges; an independent raw-vertex maximal-clique census reproduces the counts through \(n=9\), but no finite check is offered as an infinite proof.

## Originality — PASS with explicit bibliographic uncertainty

The graph-theoretic numerical bound \(\alpha(C_5\boxtimes C_n)=n\) is known in earlier literature and is not the novelty. The reviewed statement classifies *all* equality cases and gives the all-length exact labeled count and parity-sensitive solution-family growth. The Hales 1973, Sonnemann–Krafft 1974, and Vesel 1998 sources concern independence numbers; their complete primary texts could not be inspected, so an unindexed subsidiary equality enumeration remains possible. Full inspection of Badalyan–Markosyan (2009) and Korže–Vesel (2012) did not find this all-optima census. The cycle-power and graph-product results are compared by implication, not merely by title. Known pentagon-square results at \(n=5\) are outside the new claimed range.

## Value — PASS

This is a complete equality classification for a natural heterogeneous zero-error transmission model, not merely an optimized numerical parameter. It establishes two structural mechanisms for optimal codebooks and an unexpected parity-dependent exponential count of possible optimal designs, despite the same linear optimal cardinality. Odd cycles also exhibit the strict mixed-use improvement \(n>2\lfloor n/2\rfloor\). These distinctions inform exact codebook enumeration and construction choices; the result does not claim new homogeneous-channel capacity bounds.

## Primary literature and limitations

Shannon (1956), Hales (1973), Sonnemann–Krafft (1974), Badalyan–Markosyan (2009), and Korže–Vesel (2012) provide the closest foundational and structural context. Full text was obtained and inspected for the latter two works; the two older primary texts remained an access-limited novelty risk. The statement is restricted to the first factor \(C_5\) and the fixed labeled alphabet. Independent external validation has not been carried out.

Self-review: passed. Independent audit: not yet performed.

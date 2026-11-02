# Scientific assessment — run-two binary circular covers

## Correctness — PASS

For each \(k\ge3\), the mandatory restricted de Bruijn edges have vertex imbalance \(b(v)={\bf1}_{v_1=v_2}-{\bf1}_{v_{k-2}=v_{k-1}}\). The explicitly defined set of doubled edges cancels this imbalance, and alternating bridges prove strong connectivity. Hence an Eulerian tour constructs the claimed cover. The potential \(\phi(v)\) based on the first equal adjacent pair satisfies a unit-step upper bound on **every** binary de Bruijn edge, including forbidden edges, so the resulting circulation duality proves a lower bound for unrestricted circular hosts. Tightness of precisely the prescribed extra edges and Fibonacci run compositions establish the full formula. Direct construction and potential checks through \(k=18\) and \(k=14\), respectively, and an independently formulated full-graph min-cost-flow optimization through \(k=13\) agree. Finite tests do not replace the all-\(k\) proof.

## Originality — PASS, with residual literature risk

The closest source is Chee et al., *Maximum Length RLL Sequences in de Bruijn Graph* (arXiv:2403.01454v1), which optimizes a different longest-distinct-window objective under a zero-run restriction. Moreno and Matamala (arXiv:0711.1695) treat exactly-once cycles for periodically admissible forbidden-substring languages and a lexicographic optimization; their target set is smaller in general than all locally admissible finite factors. Chen, Kitaev and Sun (arXiv:1908.01116) study exactly-once universal cycles for a prescribed deletion set. None of these inspected passages implies the stated minimum **covering** length with factor repetitions for avoidance of **both** constant triples. The integers coincide with OEIS A168674, so the bare numerical formula is emphatically not a novelty claim. The substantive claim is the precise extremal language interpretation, lower bound allowing forbidden windows, and constructive repeated-factor characterization. A possibly unindexed covering formulation or general directed-postman treatment of the same forbidden-language graph remains the chief residual risk. See the structured originality comparisons in `AUDIT.json`.

## Value — PASS

A symmetric run-length limit is a natural timing and constrained-sequence model. Not every locally valid factor can be included in a shortest circular enumeration exactly once; the result determines the necessary repetition overhead **exactly at every length**, supplies an efficient Eulerian construction with exact target multiplicities, and rules out any gain from admitting forbidden windows elsewhere in the host. This is a structural coding/reconstruction benchmark rather than a new integer-sequence recurrence.

## Scientific boundaries

The proof is binary, limited to maximum run length two, and does not claim uniqueness of the covering word. No independent mathematical audit has been performed. The linked literature and OEIS provide scientific context, not definitive exhaustive priority certification.

Self-review: passed. Independent audit: not yet performed.

A prior result enumerating four-gram histograms for circular words avoiding both constant triples concerns the same language but a different factor-profile observable; it does not fix the minimal all-factor cover. The 1991 Bryant–Fredricksen paper *Covering the de Bruijn graph* was located bibliographically but not examined in full, so historical priority beyond the inspected sources is not asserted.

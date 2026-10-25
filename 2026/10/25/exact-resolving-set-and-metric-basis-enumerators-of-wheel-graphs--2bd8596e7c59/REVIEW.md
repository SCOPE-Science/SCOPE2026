# Scientific assessment

## Correctness — PASS

The distance-signature reduction is verified directly: a rim landmark has distance one exactly to adjacent unselected rim vertices, while the hub cannot distinguish two rim vertices. Three or more rim landmarks always distinguish the hub. Equal empty signatures correspond exactly to two centers of unselected triples; equal nonempty signatures correspond exactly to cyclic `00100`. These imply the explicit independent long-gap condition, and the root-selection double count \(m/k\) with the cycle independent-set formula yields the coefficient expression. The minimum size and the five metric-basis counting formulas follow by the maximal gap capacity and extracting deficits of at most two. Independent BFS-based exhaustive computations and exact-integer recurrence checks are recorded in the verifier outputs.

## Originality — PASS with residual bibliographic risk

The closest source, Sooryanarayana–Suma–Chandrakala (2021), already provides the metric dimension and a gap-based if-and-only-if feasibility theorem (Theorem 7.11). Neither is new here. The assessed claim is **only** the explicit all-cardinality resolving-set polynomial and the five exact metric-basis multiplicity formulas; these are not stated or counted in the inspected wheel section of that paper. Bergougnoux–Defrain–Mc Inerney (2023) address general algorithmic enumeration, not the wheel coefficient formulas. The 2020 missing-spoke-wheel paper addresses a different graph family. Searches of indexed literature and accessible research records did not uncover the specific complete formula. An unindexed equivalent enumeration or an unstated easy prior specialization remains possible; this is a priority risk rather than proof of uniqueness.

## Value — PASS

The formula determines a natural complete counting invariant, refining the known scalar metric dimension at every cardinality, with an explicit integer sum suitable for exact evaluation. The residue-class result in particular counts every minimum landmark configuration rather than just its size; for instance, consecutive rim sizes have sharply different basis multiplicities. The transfer from local collision constraints to cyclic independent-set enumeration explains that variation and is useful for enumerating landmark designs. This is not merely a restatement of the known minimum or the gap admissibility test.

## Scope and limits

The conclusions require at least seven rim vertices and use ordinary graph-distance resolving sets. Exact calculations for finite instances corroborate, but do not substitute for, proof for arbitrary order. Indexed-source coverage is incomplete and priority remains open to independent scrutiny.

Self-review: passed. Independent audit: not yet performed.

# Independent audit — 2026-10-01

## Final claim

An explicit iterated-log lower bound for the finite Garsia rearrangement constant

## Disposition

**Passed.** Correctness, originality, and value all pass for the final claim as stated in `RESULT.md`; no claim repair is required.

## Correctness

The proof was reconstructed through the finite coloring estimate, the balanced-coloring averaging step, the quantitative progression bound, and the two-copy Fourier transfer. With \(K=m^2\), the bad-coloring exponent is \(2\log(m-1)-\log K=2\log(1-1/m)\), while the chosen progression-free density makes the deletion entropy negligible compared with \(1/m\). Gowers' stated quantitative scale is five exponentials in \(m\); Karagulyan supplies a \(c\log m\) finite trigonometric obstruction; the arithmetic-progression modulation/dilation and the two-copy restriction preserve that obstruction up to an absolute factor. Inverting the five-fold scale yields \(G(N)\gtrsim\log_{(6)}N\). A later, independently packaged 2026-09-20 derivation gives the same rate with more explicit constants and is consistent with these steps.

## Originality

Lewko supplies the qualitative two-copy pattern mechanism, Karagulyan the logarithmic finite Fourier obstruction, Gowers a quantitative Szemeredi bound, and Bourgain the upper bound; none of those inspected statements gives the six-fold iterated-log finite Garsia rate. A published-record search located a later 2026-09-20 SCOPE record with essentially the same six-logarithm theorem, but it postdates this 2026-09-17 record and therefore does not establish prior coverage of the audited claim.

### Equivalent formulations

**Searches**
- Published-record semantic search: explicit quantitative divergence rate finite Garsia rearrangement constant iterated logarithm Lewko Karagulyan Szemeredi
- Web search: Lewko Garsia rearrangement quantitative lower bound iterated logarithm

**Evidence**
- The exact 2026-09-17 record and a later 2026-09-20 six-logarithm SCOPE formulation were found; no earlier equivalent theorem was located.

**Reasoning**

The later formulation changes notation and constants but states the same asymptotic rate; chronology makes it later duplication rather than prior coverage.

### Broader coverage

**Searches**
- Mark Lewko, arXiv:2609.18491
- G. A. Karagulyan, arXiv:2004.01003
- W. T. Gowers, GAFA 11 (2001)
- J. Bourgain, LNM 1376 (1989)

**Evidence**
- Lewko states the qualitative two-copy construction and prescribed-pattern lemma; Karagulyan advertises a sharp logarithmic finite maximal lower bound; Gowers is the quantitative progression input; Bourgain supplies the known upper bound.

**Reasoning**

The audited theorem requires quantitative bookkeeping through Lewko’s counting argument and inversion of the resulting scale; it is not a stated special case of any single broader theorem inspected.

### Exact database or table

**Searches**
- Published-record semantic search for Garsia six-logarithm lower bounds

**Evidence**
- A later 2026-09-20 SCOPE record states the same rate; no pre-2026-09-17 database/table entry with the theorem was found.

**Reasoning**

This is a theorem about an extremal operator constant, not a table lookup; the only exact record match found is later.

### Claim versus prior implication

**Searches**
- Direct implication comparison: Lewko qualitative permutation embedding + Karagulyan logarithmic obstruction + Gowers quantitative Szemeredi

**Evidence**
- The ingredients jointly support a route to the result, but deriving the stated rate requires inserting an explicit density bound into Lewko’s exceptional-coloring estimate and controlling the balanced-coloring entropy before inverting a five-fold exponential scale.

**Reasoning**

The final quantitative theorem is a nontrivial synthesis of prior ingredients rather than a direct corollary already stated with the needed dependence.

### Source inspections

- **On Kolmogorov's rearrangement problem and Garsia's conjecture** — INPUT_NOT_EXACT_RATE. Current arXiv abstract and theorem-level description of the two-copy trigonometric construction and prescribed-pattern lemma; direct PDF access was unavailable. The abstract describes the qualitative construction and its use of Szemeredi plus counting, not a finite six-logarithm rate.

- **On Weyl multipliers of the rearranged trigonometric system** — INPUT_NOT_COMBINED_THEOREM. ArXiv abstract describing the sharp logarithmic L2 lower bound for the rearranged trigonometric majorant operator. It supplies the logarithmic obstruction but not the two-copy Garsia growth theorem.

### Checked sources
- https://arxiv.org/abs/2609.18491
- https://arxiv.org/abs/2004.01003
- https://doi.org/10.1007/s00039-001-0332-9
- https://doi.org/10.1007/BFb0090057
- Published SCOPE record dated 2026-09-20: quantitative-garsia-rearrangement-constant--4185b4e0fd93

### Residual risks
- Lewko and the audited claim are extremely recent; unindexed contemporaneous observations may exist.
- Lewko full PDF was not accessible through the available route, although the critical finite counting was reconstructed from the package and cross-checked against the later explicit derivation.

## Value

Turning a new qualitative divergence theorem into the first explicit universal growth rate for the finite Garsia constant is mathematically substantive: it identifies an arithmetic-combinatorial bottleneck and yields a reusable quantitative benchmark even though the rate is far from sharp.

## Limitations

The lower rate is asymptotic with an enormous threshold and is not claimed sharp. The audit could inspect Lewko's current arXiv abstract but the arXiv PDF route was unavailable; the decisive finite counting argument was therefore reconstructed from the record itself and cross-checked against the later explicit 2026-09-20 derivation. Contemporaneous work on the very recent Lewko preprint remains the main originality risk.

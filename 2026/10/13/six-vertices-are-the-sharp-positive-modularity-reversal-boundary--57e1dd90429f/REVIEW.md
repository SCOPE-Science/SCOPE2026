# Self-review

## Correctness
**PASS.** For a bipartition with side volumes \(a,b\), cut size \(c\), and \(m\) graph edges,
\[
Q=\frac{ab}{2m^2}-\frac{c}{m}
\]
and
\[
\operatorname{Ncut}=\frac{2mc}{ab},
\]
hence
\[
Q=\frac{ab}{2m^2}\left(1-\operatorname{Ncut}\right).
\]
The packaged verifier enumerates every connected labeled graph through six vertices and every admissible bipartition, using exact rational arithmetic. It finds no strict reversal through five vertices, \(420\) labeled reversing partition pairs at six vertices, and exactly two isomorphism classes after exhaustive canonicalization. The verifier returns `VERIFY_OK`.

Risk: the statement intentionally excludes singleton sides and nonpositive-modularity splits.

## Originality
**PASS.** Shi–Malik normalized cut and Newman–Girvan modularity are established graph-partitioning and community-detection objectives. Newman 2013 directly relates their spectral algorithms. That broader relation does not state that the original discrete objectives preserve partition rankings, nor does it imply the sharp positive-modularity finite boundary. Searches by objective names, bipartition formulas, volume balance, reversal, and small-graph language did not locate the six-vertex cutoff or the two complete first-layer classes.

Risk: a specialist note or software test could contain one of the small witnesses without framing the sharp boundary.

## Value
**PASS.** Modularity maximization and normalized-cut minimization are standard but conceptually different ways to choose communities. The exact identity isolates when they are guaranteed to agree—fixed volume product—and shows the smallest positive-modularity network where changing balance is enough to reverse their choices. Requiring both splits to have positive modularity and nontrivial sides makes the witnesses community-like rather than artifacts of plainly poor partitions.

Self-review: passed. Independent audit: not yet performed.

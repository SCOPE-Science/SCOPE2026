# Independent scientific audit — SCOPE-20260914-047

Audited at: 2026-10-01T04:13:22.005211Z

Disposition: **passed**

## Correctness — PASS

The shortest-cycle lifting criterion reduces exactly to an affine system over the two-element field. Independent reconstruction of the first 12-vertex witness gives girth 4, ten 4-cycles, coefficient rank 6 with inconsistent augmented system, and signed spectral radius about 2.561553, safely below the cubic Ramanujan threshold about 2.828427. The three-equation obstruction for complete bipartite graphs with degree at least 3 is an exact parity contradiction. The finite cube census in the inspected verifier is exhaustive over all 4096 signings.

## Originality — PASS

The general 2-lift and graph-lift literature supplies spectral existence and global lift-girth theory, but the searches and primary sources inspected do not state this explicit 12-vertex Ramanujan one-step-frozen witness, its rank-6 inconsistent shortest-cycle system, or the frozen-versus-raisable comparison.

### Equivalent formulations

The explicit finite obstruction is not an alternate wording of the MSS existence theorem.

### Broader coverage

Neither source implies that these particular Ramanujan children are one-step girth-frozen.

### Exact database or table

No independent database or table was located that contains the rank-6 UNSAT certificate.

### Claim versus prior implication

The witness is an additional finite structural fact, not a corollary of the cited general results.

## Value — PASS

The witness isolates a concrete failure mode for greedy simultaneous spectral-and-girth branch selection and pairs it with a raisable cube comparison. The claim is deliberately one-step only, making it a motivated structural counterexample rather than an overclaimed tower impossibility.

## Sources inspected

- Interlacing Families I: Bipartite Ramanujan Graphs of All Degrees — https://doi.org/10.4007/annals.2015.182.1.7. NOT_COVERING: Provides existence of good spectral signings but no simultaneous girth-raising guarantee or this finite frozen witness.
- On the Girth of Graph Lifts — https://arxiv.org/abs/2401.01238. NOT_COVERING: Studies extremal lift sizes and girth rather than branch-specific shortest-cycle parity infeasibility.

## Residual risks

- The literature search is best-of-knowledge rather than a priority proof.
- The spectral check is numerical, but its margin to the Ramanujan threshold is large; the freezing certificate itself is exact.

## Limitations

- One-step frozenness does not prevent a later descendant from becoming girth-raisable.
- The nontrivial explicit frozen witnesses are cubic.
- Spectral certification is numerical with a comfortable margin; the finite-field inconsistency is exact.

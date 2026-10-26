# Review

## Correctness

**PASS.** The lower bound follows from the support of an exact simulator: almost every shared seed must have a decoder-output set intersecting every target support. The exact neighborhood-intersection formula bounds the union of any two output neighborhoods by \(q^2-2\) for \(q\ge3\). The three-word construction covers all inputs; randomized coordinate injections and an unbiased shared tie-breaker make the output law invariant under the stabilizer of each input, hence uniform on its target support. The binary case has four singleton target supports and therefore needs all four outputs.

## Originality

**PASS, with residual risk.** Exact-formulation searches for the q-ary two-use optimum, the associated Hamming-distance covering problem, and zero-error simulation of the off-diagonal channel returned no direct matching claim. The closest primary text explicitly treats the ternary off-diagonal channel but does not state this exact two-use optimum. The recent asymptotic paper excludes zero simulation error and requires positive dispersion. These comparisons do not prove global novelty; an uninspected general support-covering result could subsume the finite case.

## Value

**PASS.** This is an exact operational invariant at a mathematically meaningful boundary excluded by the recent positive-dispersion asymptotic theorem. The alphabet-independent optimum \(3\) for all \(q\ge3\), contrasted with the binary value \(4\), is not a numerical recomputation: it is proved by a symmetry-based exact simulation and a sharp covering obstruction. Its scope is deliberately limited to the first nontrivial two-use case.

## Closest literature and limitations

The recent third-order analysis of symmetric channel simulation treats fixed positive error and positive dispersion. Earlier finite-blocklength work includes the ternary one-use off-diagonal channel as an example, but not the exact two-use optimum. Exact channel synthesis under an i.i.d. source uses average prefix-free length and is a different operational objective.

Self-review: passed. Independent audit: not yet performed.

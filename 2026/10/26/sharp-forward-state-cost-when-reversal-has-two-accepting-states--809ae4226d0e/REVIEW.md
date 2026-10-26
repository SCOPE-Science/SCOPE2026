# Scientific review

## Correctness

PASS. The orbit of the accepting set supplies the reachable, minimal reverse DFA, and transitivity forces exactly two orbit-block memberships per forward state. Minimality injects forward states into unordered pairs of reverse blocks; incidence counting gives the sharp quadratic bound. Equality makes that injection bijective, forcing the complete-graph edge model and 2-homogeneous action. The converse constructs a minimal edge-action DFA with the stipulated forward and reversal accepting-state counts. The standalone verifier independently checks small cases; no infinite conclusion depends on those cases.

## Originality

PASS under the available literature comparison, with residual risk. Rauch–Holzer (2022) considers attainable reversal accepting-state values; German (2026) proves full attainability and supplies the upper-bound witness. The searched text of neither establishes a lower bound on the **number of forward states** among such witnesses, nor a characterization of every state-minimal witness. The new universal lower bound and rigidity implication are mathematically different from the prior existence statement. Unindexed results and conceptual reformulations remain possible risks.

## Value

PASS. The literature's attainable-spectrum question naturally leads to optimizing witness size: the published construction uses quadratically many states for reverse accepting-state count two, but it was not shown necessary. The exact minimum proves that this quadratic cost is intrinsic. The rigidity theorem further identifies all optimal architectures as 2-homogeneous complete-graph edge actions, a meaningful structural restriction rather than a numerical restatement of a construction.

## Verification and limitations

The finite verifier passes for \(m=2,\ldots,12\), with an exhaustive smaller-state check for the first two parameters. The proof handles every integer \(m\ge2\). Larger reversed accepting-state counts and optimal generator-word lengths are outside scope. The novelty assessment is literature-bounded and the work awaits independent scrutiny.

Self-review: passed. Independent audit: not yet performed.

# Scientific review

## Correctness

PASS. The graph-theoretic argument proves that every nonedge of the antihole has full geodesic hull for every \(n\ge7\), while all proper convex sets are cliques. This gives an exact trace characterization, not only a bound. The proof of the online equality reduces the version-space recurrence to two independently proved lemmas: hereditary independent-set dimension and the one-top augmented-path formula. The parity cases and boundary \(m=0\) are explicit. Finite verification tests the definitions independently, but is not substituted for these all-order proofs.

## Originality

PASS under accessible comparisons. The 2022 article by Thiessen and Gärtner provides general graph-convex learning bounds, including a general VC characterization from earlier work; its main text was inspected through Section 6 and does not contain this exact antihole specialization. The graph-convexity survey by Dourado et al. studies structural convexity and does not supply these learning dimensions. The older graph-defined VC set-system literature concerns, among other things, neighborhoods, connected sets and paths; its inspected abstract does not establish this hypothesis family. The cycle independence polynomial is pre-existing and credited. Literature and accessible prior-claim comparisons found no stronger matching antihole claim; incomplete historical coverage, especially alternate terminology for adjoining one universal hypothesis to an independence complex, remains a real novelty risk.

## Value

PASS. Antiholes are canonical complements of induced cycles and, at odd orders, standard obstruction graphs in perfect-graph theory. The result classifies the whole family of geodesic-convex hypotheses and **all** shattered supports, then proves a sharp parity transition in optimal adversarial online mistake complexity across every order \(n\ge7\). The two parity cases have the same static dimension scale but different exact adaptive gaps, providing a natural benchmark for graph-convex online learning rather than an arbitrary finite subcase.

## Scope and remaining risks

The complete classification is claimed only for simple, unweighted antiholes of order at least seven. The conventional independence polynomial is not new. The accessible literature comparison cannot exclude an older equivalent result under another phrase or a proof embedded in a broader theorem. An independent scientific review has not been performed.

Self-review: passed. Independent audit: not yet performed.

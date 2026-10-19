# Scientific review: delayed coalescence on the self-power escort simplex

## Correctness

PASS. The theorem is fully quantified for labelled probability vectors, with separate scopes for dimension three and dimension at least four. The first-step image belongs to a strictly monotone scalar-coordinate slab for every \(n\ge4\), by an explicit rational proof of \(e^{1+1/e}<4\). Equality of normalized weights then forces equality of all coordinates, using the common multiplier and the fixed sum constraint. On the dimension-three invariant line, the derivative changes sign at a unique interior point of the image interval. The sign at the right endpoint has a strict exact arithmetic certificate; intermediate values produce an open continuum of distinct first images with the same second image. The Python diagnostic supports but does not replace these infinite-domain arguments.

## Originality

PASS, with bibliographic risk. The closest primary paper, Lei Zhou (2026), was inspected in accessible full-text HTML in the directly relevant sections, especially the basic log-ratio identity, compact-core Proposition 2, global convergence theorem, and Section 6's complete one-step *uniform-point* fiber classification. The new comparison is about nonuniform *two-step* fibers and eventual injectivity on the full first-step image, which the source does not analyze. Its scalar monotonicity and core estimate help prove the higher-dimensional half; they do not supply the sharp dimension-three internal fold and continuum of late mergers. Targeted research-record searches on the source title, normalized self powers, post-image injectivity, coalescence and equivalents did not identify a covering finding. The possibility of a previously unindexed equivalent or an unstated corollary in adjacent literature remains.

## Mathematical value

PASS. The natural question of whether a contracting regularization map can erase further distinctions *after* its first regularization step has a sharp dimension-dependent answer. The exceptional dimension-three fold is an exact nonuniform finite-time collapse, rather than a renamed equilibrium fact: two distinguishable first images reach exactly the same second iterate throughout an interval of target values. Conversely in four or more coordinates all future information loss occurs in the first step. This distinction complements rather than duplicates global convergence and the one-step uniform equilibrium fiber.

## Scope and limits

No complete dimension-three preimage census, no general escort family, no independent validation, and no exhaustive bibliographic priority claim are made. The numerical witness has separation at first image and machine-precision agreement at the second; the analytical sign and monotonicity proof is decisive.

Self-review: passed. Independent audit: not yet performed.

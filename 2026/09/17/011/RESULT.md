# A 2,080,643-element non-cancelling-intersections counterexample bound

> **Review status: same-model review.** Correctness, originality and value were assessed by the same-model review, not an independent reviewer. The source run states the theorem conditionally on the published structural lemmas of Wilhelm's construction. Originality is claimed only to the best of our knowledge. Publication is not peer review or a guarantee of priority.

## Claim

Using Hermann Wilhelm's marked-affine-plane lattice architecture, the source run proposes the following quantitative refinement.

For `p=127` and marking width

`w = ceil(sqrt(2p)) + 1 = 17`,

there exists a marking for which the lattice `P_{p,m}` has no winning dot-algebra tree. The lattice therefore gives an unrestricted Non-Cancelling Intersections counterexample with exactly

`p^3 + 2p^2 + 2 = 2,080,643`

elements.

The marking is existential, not explicitly exhibited. No claim is made that `p=127` or `2,080,643` is minimal.

## Context

Wilhelm's arXiv:2608.27416v2 proves the unrestricted NCI conjecture false using the same lattice family and gives a theorem for primes `p >= 10^5`; the displayed finite example uses `p=100003` and has `1,000,110,003,900,047` elements. The source run targets the large slack in the paper's first-moment estimate while retaining its lattice architecture and structural reductions.

## Incidence strengthening

Let `T subset F_p^2` have size `t`, with `2p <= t <= 4p`, and for every affine line `ell` put `j_ell = |T intersect ell|`. The standard affine-plane identities used by Wilhelm are

`sum_ell j_ell = t(p+1)`

and

`sum_ell j_ell^2 = t(t+p)`.

Let `N` be the number of lines with `j_ell >= 2`, let `n_1` be the number of singleton lines, and let `L=p(p+1)` be the number of affine lines. The source run strengthens the estimate used in the parent argument from `n_1 <= L` to

`n_1 <= L-N`,

because a nonsingleton line cannot simultaneously be a singleton line.

Writing

`A=(p+1)(t-p)` and `C=t(t+p)`,

the mass on nonsingleton lines satisfies

`S := sum_{j_ell>=2} j_ell >= A+N`.

Cauchy--Schwarz and the second-moment identity then give the realizability constraint

`(A+N)^2 <= C N`.                                      (1)

## Exact first-moment certificate

For `p=127`, the source verifier evaluates for every integer `254 <= t <= 508` the least integer `N` permitted by (1).

Take cutoff `K=6`. Since every line with `j_ell>=7` contributes at least `49` to `sum j_ell^2=C`, at most `floor(C/49)` lines can have trace size at least seven. Hence there are at least

`E(t)=N_min(t)-floor(C/49)`

lines whose trace size lies between two and six. The reported minimum is

`E(254)=2442`,

and all values are positive.

Choose on each affine line an independent uniformly random 17-point marking. A trace of size at most six is hit with probability at most

`q = 1 - C(121,17)/C(127,17)`
`  = 312329993535824646690 / 533290643186622881175`
`  < 293/500`.

Thus, for a fixed `T` of size `t`,

`Pr[T admissible] <= (293/500)^E(t)`.

The source run reports an exact-integer evaluation of

`U = sum_{t=254}^{508} C(127^2,t) (293/500)^E(t)`

showing

`U < 9/100 < 1`.

Consequently some marking has no admissible set throughout the required cardinality range.

The final implication uses Wilhelm's published structural lemmas: a winning dot-algebra tree for `P_{p,m}` would induce a winning plane tree, and such a tree must contain an admissible node state in the relevant size interval. The source run therefore obtains the claimed counterexample within that framework.

## Reproducibility

The source run reports a local exact-arithmetic verifier checking primality of 127, the width requirement `C(17,2)>=126`, inequality (1), the `E(t)` bounds, `q<293/500`, and the full rational first-moment sum. That local verifier is not one of the generated files available in the present conversation, so it is not fabricated in this archive.

## Closest prior work

- Hermann Wilhelm, *Refutation of the Non-Cancelling Intersections Conjecture*, arXiv:2608.27416v2, is the direct parent result.
- Wilhelm's earlier left-linear construction is arXiv:2608.19414.
- The source run identifies an August 2026 private communication from Alexander Walz, described by Wilhelm, as the strongest inaccessible originality threat.

The source run searched for the exact new prime, exact lattice size, and quantitative-improvement formulations and found no public equivalent. This remains a qualified, to-the-best-of-our-knowledge originality assessment.

## Limitations

The marking is nonconstructive. No lower bound on the true smallest counterexample is obtained, and no optimality of `p=127` is claimed. The private Walz argument and any unindexed author-side optimization could reduce originality. No independent proof audit is asserted.

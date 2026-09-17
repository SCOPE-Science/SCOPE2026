# Six-cell orbit-closure periodicity for exact translational tilings of Z^2

> **Review status: same-model review.** Correctness, originality and value were assessed by the same-model review, not an independent reviewer. The source run itself identifies a residual correctness risk in transporting part of Khetan's spectral argument to cardinality six. Originality is claimed only to the best of our knowledge. Publication is not peer review or a guarantee of priority.

## Claim

Let `F subset Z^2` be an exact cluster of full affine span with `|F|=6`, and let `T` be any `F`-tiling. The source run proposes and same-model review the theorem that the orbit closure of `T` contains a 1-periodic `F`-tiling.

Combined with Khetan's eight-cell counterexample and the already settled smaller cardinalities cited in the source run, this would make eight the smallest full-affine-span exact-cluster cardinality at which orbit-closure 1-periodicity can fail.

## Context

The closest source is Abhishek Khetan's July 2026 paper, arXiv:2607.09830v2, which constructs a full-affine-span exact cluster of size eight admitting an orbit closure with no 1-periodic tiling, proves positive results for several smaller cardinalities, and explicitly leaves `|F|=6` unresolved.

## Proof structure reported by the source run

### 1. Unequal-prime product tilings

The run proves the following auxiliary statement. Let `p,q` be primes and let `A,B subset Z` satisfy `|A|=p`, `|B|=q`, `gcd(A-A)=gcd(B-B)=1`. If `T` tiles `Z^2` by `A x B`, then `T` has period `(p,0)` or `(0,q)`.

The argument extends Khetan's prime-cardinality fibre method: one-dimensional rigidity makes row and column unions cosets of `pZ` and `qZ`; formal-series defects give annihilation relations; if one residue function is nonconstant, Khetan's combinatorial lemma forces the other to be constant, yielding an axis period. The source run also reports an exhaustive torus sanity check for `A={0,1}`, `B={0,1,5}` on `Z_6^2`, finding 60 exact tilings and no violation of the predicted `(2,0)` or `(0,3)` period.

### 2. Six-point section profiles from an infinite common-zero direction

Following the spectral setup in Khetan, suppose a rational character-kernel direction contains infinitely many common zeros for all dilations `alpha` coprime to six. Factoring the denominator into its `2`- and `3`-parts and an invertible part, the source run obtains one nontrivial root of unity common to every nonempty section parallel to that direction. A singleton section cannot vanish, so every section has at least two points.

Because `F` has six points and full affine span, the only possible section-size profiles are

`(3,3)`, `(2,4)`, or `(2,2,2)`.

### 3. Multiple infinite-common-zero directions

The source run analyzes transverse profile pairs.

- Two `(3,3)` profiles are impossible because two families of two lines have at most four intersection points.
- A `(3,3)` profile with an even profile forces the even profile to be `(2,2,2)` and yields a full `2 x 3` grid. Full affine span makes the grid unimodular, reducing the cluster to an unequal-prime product and hence to the preceding periodicity lemma.
- A `(2,4)` profile cannot coexist with another even profile for the same intersection-count reason.
- Two `(2,2,2)` profiles give a 2-regular bipartite incidence graph on `3+3` support lines. Its complement is a perfect matching. The three two-point sections then impose root-of-unity equations on three signed line separations; two equations multiply to force `+1` for the third pair while that section requires `-1`, a contradiction.

Thus the only viable multi-direction branch reduces to the periodic product case.

### 4. At most one infinite-common-zero direction

For the remaining branch, the source run imports Khetan's spectral Case (2): dilation identities force nonzero spectral support into the common-zero set, leaving at most one kernel with infinite support plus finitely many exceptional spectral points. Integer-valued exponential rigidity then yields a nonzero period for an origin-anchor cylinder, and Khetan's orbit-closure transfer theorem gives a 1-periodic tiling in the orbit closure.

The source run argues that the cardinality-specific notation in Khetan's paper is not essential here because the underlying dilation theorem and common-zero lemma are stated for every `alpha` with `gcd(alpha,|F|)=1`; for `|F|=6` this becomes `gcd(alpha,6)=1`.

## Prior work and originality scope

The source run checked Khetan's arXiv:2607.09830v2, a current MathDB entry, and Rao--Xue's 2006 prime-cardinality tiling work, and searched for six-cell, cardinality-six, semiprime/`pq`, product-of-two-primes, orbit-closure, and tiling-periodicity formulations. It found no subsequent direct solution.

It explicitly identifies older literature phrased in factorization or vanishing-sum language as a serious originality threat, including Szegedy (1998), Horak--Kim (2016), Kari--Szabados (2020), Khetan's earlier work, Lam--Leung (2000), and semiprime translational-factorization literature.

## Reproducibility and evidence

The archival record now includes the compact supporting files that were generated by the source run and are accessible in this conversation:

- `artifacts/research_note.md`: the source proof note;
- `artifacts/verify.py`: the finite torus sanity-check script.

The finite computation is only a sanity check and is not part of the general proof. Adding these artifacts does not change the record's same-model review status or remove the residual correctness risk described below.

## Limitations

The source run itself states the main residual correctness risk: there may be a subtle hidden dependency in the imported spectral results or in transporting Khetan's “at most one infinite direction” branch from the prime-square setting to cardinality six. It explicitly says this deserves independent proof checking before publication-ready reliance.

The result has not received an independent human or independent-agent audit, and absolute originality cannot be established from search coverage. These qualifications are part of the archival record, not later downgrades or upgrades.

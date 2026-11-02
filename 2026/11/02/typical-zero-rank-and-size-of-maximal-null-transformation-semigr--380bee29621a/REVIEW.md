# Review: typical zero rank and size of maximal null transformation semigroups

## Correctness — PASS

The exact normal form follows by decomposing a null subsemigroup along the kernel classes of its zero idempotent. On a block with root \(a\) and admissible image set \(W\), all maps collapse \(W\) to \(a\) and map the remaining points into \(W\). The count \(k\binom{k-1}{j-1}\) and order \(j^{k-j}\) are independently reconstructed, including the two exceptional small block sizes. Direct labeled-set assembly gives the marked generating function.

For the limits, a unique positive saddle \(t\) satisfies \(n=tB'(t)\). Independent Poisson block variables conditioned on total size \(n\) reproduce uniform maximal null subsemigroups exactly. A characteristic-function expansion proves the needed normal approximation for the total size excluding singleton blocks. This gives a quantitative, non-negligible lower bound for the conditioning event, sufficient for the Poisson Chernoff rank law and the exponentially tilted bad-block bound. Uniformly typical block sizes and root-subset sizes prove the logarithmic semigroup-order law. The coefficient identity and Stirling's formula give total-count growth.

The verifier constructs transformation multiplication independently and exhaustively tests all maximal null families for ground-set sizes one through four. It checks the complete zero-rank spectra and first two order moments against the marked formula. These finite checks are corroboration, not proof of the asymptotic assertions.

## Originality — PASS, with priority limits

Cameron et al., arXiv:2110.09701, Section 4.2, already classified inclusion-maximal null subsemigroups, computed their component weights, and provided an exact total-count recurrence and initial table. Those are **not** presented as new. The exact bivariate and Mellin-marked identities are straightforward explicit transformations of their classification and are not the independent novelty basis. The assessed addition is the quantitative description of a uniformly chosen maximal null subsemigroup: zero rank asymptotic to \(n/\log n\), logarithmic order asymptotic to \(n\log\log n/2\), and total-count logarithmic growth with its linear constant. Cain–Malheiro–Paulista, arXiv:2310.08481, addresses extremal cardinalities of commutative nilpotent transformation semigroups rather than these typical inclusion-maximal statistics. Relevant scientific-index and primary-literature searches did not reveal an equivalent calculation, but absence from searched sources does not certify priority. General asymptotic theorems for decorated set partitions may subsume portions of the result; a broader unlocated analysis remains the main risk.

## Mathematical value — PASS

The space of maximal-by-inclusion null subsemigroups is structurally much larger than the set of maximum-cardinality examples. A typical member has a zero with a logarithmically thinning fraction of kernel classes and has semigroup size on a radically different scale from the largest examples. These intrinsic statistics explain the typical structure of a natural finite-semigroup family, not merely an arbitrary numerical slice. The marked formula also allows exact zero-rank and order-moment extraction at every finite dimension.

## Limitations

The results concern labeled full transformation semigroups and uniform sampling of inclusion-maximal **null** subsemigroups. They do not imply analogous laws for maximal commutative nilpotent semigroups, unlabeled isomorphism classes, or arbitrary nilpotent transformation semigroups. An independent literature and mathematical audit has not been carried out.

Self-review: passed. Independent audit: not yet performed.

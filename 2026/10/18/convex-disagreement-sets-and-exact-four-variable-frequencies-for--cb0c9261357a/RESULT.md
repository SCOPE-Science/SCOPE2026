# Exact ordered-pair distance distribution for four-variable positive Boolean term functions

## Finding

Let \(\mathcal F_4\) consist of the distinct Boolean truth functions obtained from four available variables using only binary conjunction and disjunction, with no constants. The four variables are available to each formula, not necessarily essential. For \(f,g\in\mathcal F_4\), let \(d(f,g)\) be the Hamming distance between their truth tables on the sixteen assignments. There are \(166\) functions. The number of **ordered** pairs at each distance is exactly:

| \(d\) | Ordered pairs |
|---:|---:|
| 0 | 166 |
| 1 | 904 |
| 2 | 2560 |
| 3 | 4616 |
| 4 | 5824 |
| 5 | 5312 |
| 6 | 3736 |
| 7 | 2176 |
| 8 | 1188 |
| 9 | 568 |
| 10 | 296 |
| 11 | 136 |
| 12 | 56 |
| 13 | 16 |
| 14 | 2 |
| **Total** | **27556** |

For two independent uniform draws from \(\mathcal F_4\), these counts divided by \(27556\) are the exact probabilities of the corresponding disagreement distances, or equivalently of agreement fractions \(1-d/16\). This gives a finite benchmark for distance distributions of sampled monotone functions conditioned to be nonconstant. A count of possible disagreement masks alone cannot provide that benchmark: it counts each mask once, rather than once for each ordered pair that realizes it.

## Assumptions and scope

Assignments are classical and ordered coordinatewise. Equality of formulas means equality of truth functions, not equality of symbolic expressions. Self-pairs are included, and pairs at positive distance are counted in both orders. The experiment is uniform on distinct term functions, not on formula syntax, pairs of comparable functions, or distinct disagreement masks.

## Exact enumeration

A term function is isotone and fixes the two extreme assignments. Conversely, each such function is the disjunction, over its minimal true sets, of the corresponding conjunctions of variables. The endpoint conditions ensure a nonempty disjunction of nonempty conjunctions. This is precisely the family of all monotone Boolean functions except the two constants.

Encode a function by the truth-table word with bit \(a\) at assignment \(a\in\{0,\ldots,15\}\) (bit-set encoding of the assignment). Enumerate all \(2^{16}\) words; keep the $166$ for which bit zero is zero, bit fifteen is one, and each covering relation in the four-cube is nondecreasing. Testing covers suffices because every comparable pair is connected by a chain of covers. For each ordered pair of retained words, increment the cell indexed by the population count of their bitwise XOR. The procedure visits each admissible pair exactly once.

A second enumeration starts with the two functions on the zero-variable cube and, one coordinate at a time, pairs two monotone lower and upper slices exactly when the lower slice is pointwise at most the upper slice. The decomposition by this coordinate is unique. Removing the two constants after reaching four coordinates gives the same truth tables and independently reproduces the table. A third way to generate the same family is to choose each nonempty antichain of nonempty assignments as the minimal true sets. For distance fourteen, the two functions must take opposite values throughout the interior of the cube; the orientation cannot change on comparable interior vertices. All such vertices belong to one component of the comparability graph: every interior assignment contains a singleton and every pair of singletons lies beneath a common interior two-element set. Thus only the full conjunction and the full disjunction attain this distance, in either order.

## Order-theoretic background

The characterization of which masks can occur is a consequence of the difference-of-ideals representation for interval-closed subsets of a poset (Elder et al., Proposition 2.5 and its proof, or its order-dual form). In detail, if \(U,V\) are the true upsets of two terms, their symmetric difference is \((U\cup V)\setminus(U\cap V)\), a difference of nested upsets, hence order-convex. It omits both extremes. Conversely a nonempty order-convex set \(D\) omitting both extremes is the difference of the nested upsets \(\uparrow D\) and \((\uparrow D)\setminus D\): convexity guarantees that the second is an upset, and both upsets contain the top and omit the bottom. The empty mask comes from equal functions. In the formal terminology of Canonne et al., interval-closed indicators are 2-monotone (the forbidden chain pattern is \(1,0,1\)); the endpoint constraints select the masks relevant here.

For reference, with \(C_k\) the number of interval-closed subsets and \(M_k\) the number of upsets in the \(k\)-cube, the number of distinct realizable masks is \(C_k-2M_k+3\). The interval-closed sets containing the bottom are the nonempty ideals, and those containing the top are the nonempty filters; only the entire cube belongs to both classes. In four variables the known values \(C_4=3938\) and \(M_4=168\) give \(3605\) distinct masks, not \(3605\) ordered pairs. Up to three variables the interior has no chain of three, so all interior subsets are order-convex; the four-variable interior already has the chain \(\{1\}\subset\{1,2\}\subset\{1,2,3\}\). Every agreement count from \(2\) to \(2^k\) can occur: take the conjunction as one term and, for the other, any upset of size \(m\) from \(1\) to \(2^k-1\) given by the first \(m\) vertices in decreasing Hamming weight. The count is then \(2^k-m+1\). Thus across arities the spectrum consists of positive dyadics at most one; these unweighted existence statements are not claimed as contributions of the census.

## Reproduction

Run `python3 verify_positive_equations.py` with Python 3.10 or later (uses `int.bit_count`). It scans truth tables and independently generates monotone pairs of slices, recomputes the exact distance table, and cross-checks the distinct masks against order-convex subsets through arity four. The expected final line is `POSITIVE_EQUATIONAL_CONVEXITY_VERIFY_OK`. Exhaustiveness applies to the specified finite census, not to distance distributions at higher arities.

## Relationship to prior work and limitations

The term-function count is the fourth Dedekind number minus two, and the mask family is interval-closed, a previously characterized and enumerated object. The exact histogram is instead the distance enumerator of **all** ordered pairs of nonconstant monotone functions, not only nested pairs of ideals or one canonical representative per distinct mask. Equivalently, take the lattice of upsets of the four-cube restricted to those containing the top and omitting the bottom. A path by single-point deletions down to the intersection and additions up to the second upset shows that distance in its cover graph is the symmetric-difference size. The displayed vector therefore gives its distance polynomial in the ordered-pair convention.

Fihman, Van Hirtum and Plessl use Hamming distances between monotone functions as a sampling diagnostic; the inspected section reports sampled distance statistics in much larger arities, not this exact four-variable distribution. Cardó's Example 6.4 discusses density of an equational spectrum, not pair multiplicities. Its statement identifying terms with all functions fixing zero is not the endpoint-and-monotonicity condition of this signature. The inspected sources do not settle absolute priority for the exact ordered-pair table. It is specific to arity four and is not an estimate of a large-arity distribution.

## References

1. J. Elder, N. Lafrenière, E. McNicholas, J. Striker and A. Welch, *Toggling, rowmotion, and homomesy on interval-closed sets*, [arXiv:2307.08520](https://arxiv.org/abs/2307.08520), Definition 2.1 and Proposition 2.5.
2. C. L. Canonne et al., *Testing \(k\)-Monotonicity*, [arXiv:1609.00265](https://arxiv.org/abs/1609.00265), §1 and Definition B.1.
3. OEIS [A369313](https://oeis.org/A369313), interval-closed subsets, and [A000372](https://oeis.org/A000372), Dedekind numbers.
4. A. Fihman, L. Van Hirtum and C. Plessl, *Statistical Estimation of higher Dedekind Numbers*, [arXiv:2607.08446](https://arxiv.org/abs/2607.08446), §3.4.2.1.
5. C. Cardó, *Probabilistic equational spectrum, primality and approximation in finite algebras*, [arXiv:2604.08446](https://arxiv.org/abs/2604.08446), Example 6.4.

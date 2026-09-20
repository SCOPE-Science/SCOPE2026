# Same-model review

**Same-model review: passed. Cross-model review: not yet performed.**

## Correctness

The key collision identity was checked first because overlap is the main possible hidden dependence issue. Two length-\(k\) windows separated by \(r<k\) agree exactly when the \(k+r\) letters form an \(r\)-periodic block; there are \(d^r\) such blocks out of \(d^{k+r}\), so the probability is exactly \(d^{-k}\). This justifies the pair-collision expectation used for every long length.

For \(k>\lfloor\log_d n\rfloor\), the deterministic maximum at that length is the number of window positions. The missing distinct words are bounded by the number of colliding window pairs. Combining the first moment of that pair count with \(G_{n,k}\le n\) gives the stated \(L^q\) bound; the geometric sum and Markov optimization were rederived separately and give the published constants.

For the centered result, the union bound for the longest repeated substring is valid with overlapping windows by the same collision identity. On the event that no repeated substring reaches length \(L_n\), all contributions at lengths at least \(L_n\) are deterministic. Changing one letter affects at most \(k\) windows at length \(k<L_n\), so the total restricted Lipschitz constant is \(c_n=L_n(L_n-1)/2\). McShane extension preserves this constant, and clipping preserves both the range and agreement on the good set. Efron--Stein and McDiarmid then give the displayed variance and tail bounds. The exceptional-set contribution was checked using \(D_n\le n(n+1)/2\).

The finite verification artifact exhaustively checks the deterministic maximum for small binary and ternary words, exact overlapping collision probabilities for several \((d,k,r)\), and the restricted Hamming-Lipschitz inequality on representative good sets. These computations support but do not replace the general proof.

## Originality

The recent Godbole paper explicitly asks whether variance estimates can give deeper concentration information for the total distinct-substring count. The older Janson--Lonardi--Szpankowski paper already provides substantially sharper first-moment information than is needed here, so no first-moment novelty is claimed. The deterministic maximum is also prior work, including Flaxman--Harrow--Sorkin. Ahmadi--Ward obtain second-moment information for the number of distinct words at one prescribed length, and Gaither--Ward study variance of the suffix-tree internal profile at a prescribed level.

The total statistic also has the standard suffix-array representation
\[
D_n=n(n+1)/2-\sum_i\operatorname{LCP}_i.
\]
Searches therefore included equivalent formulations involving the sum of adjacent-suffix longest common prefixes, suffix-tree additive quantities, total factor complexity, total subword complexity, and longest repeated substrings. No prior theorem matching either the all-moment deficit estimate or the stated total variance/concentration bounds was located.

The principal residual originality risk is older analytic suffix-tree literature: an equivalent result could be phrased as a variance bound for a total tree or longest-common-prefix functional rather than as distinct-substring complexity. The available related profile-variance literature does not itself imply the published total-statistic bound without additional covariance control. Originality is therefore assessed only to the best of our knowledge.

## Value

The variance bound directly addresses the concentration question for the all-length statistic and gives an explicit polynomial-logarithmic scale rather than only a first-moment estimate. The independent deficit theorem shows that maximum-complexity loss has all moments linear in \(n\) and an exponential tail. The arguments are short, transparent, and potentially adaptable to other random-word complexity functionals.

## Limitations

The variance scale is probably improvable: the result is an upper bound, not an asymptotic. No lower bound, limit law, or sharp constants are supplied. Uniform independent letters are essential to the exact collision identity in its present form; nonuniform or dependent sources require separate overlap estimates. No claim is made that the displayed concentration window is optimal.

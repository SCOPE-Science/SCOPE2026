# Complete covariance-kernel transition in finite Page–Rényi dimer parking

## Finding

**Theorem (exact covariance rank and kernel at every time).** Fix an integer \(n\ge4\). Give the \(n-1\) edges of a path on sites \(1,\ldots,n\) independent exponential clocks of rate one. When edge \((i,i+1)\) first rings, occupy both endpoints if both are free; otherwise reject it. Let \(X(t)=(X_1(t),\ldots,X_n(t))\in\{0,1\}^n\) denote the occupied-site indicators at time \(t\). Write \(X(\infty)\) for the state after all edges have rung, and \(\Sigma_n(t)=\operatorname{Cov}(X(t))\) for the real covariance matrix. Define
\[
s=(1,-1,1,-1,\ldots,(-1)^{n-1})^\top,
\]
and let \(e_i\) denote the \(i\)-th coordinate vector. Then for every finite \(0<t<\infty\),
\[
\boxed{\ker\Sigma_n(t)=\operatorname{span}\{s\},\qquad \operatorname{rank}\Sigma_n(t)=n-1.}
\]
At complete jamming,
\[
\boxed{\ker\Sigma_n(\infty)=\operatorname{span}\{s,e_2,e_{n-1}\},\qquad\operatorname{rank}\Sigma_n(\infty)=n-3.}
\]
The two additional singular directions appear **only** at complete jamming, not at any positive finite time. At \(t=0\), the covariance is the zero matrix. Thus the two time regimes are sharply distinct even though \(X(t)\to X(\infty)\) almost surely as \(t\to\infty\).

**Principal-minor consequence.** At finite positive time, deleting any one site's row and column yields a positive-definite principal covariance submatrix. At jamming, site coordinates \(2\) and \(n-1\) are deterministic; after deleting both and any one additional coordinate, the remaining \((n-3)\times(n-3)\) covariance principal submatrix is positive definite.

## Assumptions and scope

The path has no periodic boundary and each edge has exactly one effective attempt, since a rejected edge can never become available again. The clocks are independent, identically distributed, and atomless, with exponential law fixing the time parameter. The same conclusions hold for any independent identically distributed atomless first-arrival law at a time \(t\) where the common arrival distribution function lies strictly between zero and one, because the support argument does not depend on clock densities.

The terminal law is supported on the occupied-site vectors of maximal matchings of the path. Here maximal means that no additional edge can be adjoined, not maximum cardinality. The theorem concerns **the complete position-indexed covariance matrix**, not merely variance of the total number of occupied sites.

## Proof

**1. Covariance kernels are the affine-support annihilators.** For every finite random vector \(Y\),
\[
a^\top\operatorname{Cov}(Y)a=\operatorname{Var}(a^\top Y).
\]
Because covariance matrices are positive semidefinite, \(a\) is in the covariance kernel if and only if \(a^\top Y\) is almost surely constant. Accordingly, we classify the linear forms constant on the positive-probability state support.

**2. Finite-time support.** For \(0<t<\infty\), the event that none of the \(n-1\) clocks has rung by time \(t\) has positive probability and yields the zero vector. For each edge \(i\), the event that exactly that clock rings by \(t\) has positive probability and yields \(e_i+e_{i+1}\). Therefore any linear form \(a^\top X(t)\) constant on the support must have value zero on the zero state and must satisfy
\[
a_i+a_{i+1}=0\quad(1\le i<n).
\]
These equations force \(a\) to be proportional to \(s\). Conversely each accepted dimer occupies one site of each parity, so \(s^\top X(t)=0\) in every realization. This proves the finite-time kernel and rank for all \(n\ge2\).

**3. Terminal support and three invariants.** Every terminal accepted edge set is a maximal matching, since there are no adjacent vacant sites left. Conversely, every maximal matching has positive probability: order all its edges before all other edges. Its edges are disjoint and hence all accepted; maximality blocks every remaining attempt. Thus the terminal support consists of **all** maximal-matchings' occupied-site vectors. Every maximal matching necessarily covers site \(2\), since otherwise site \(1\) also is uncovered and edge \((1,2)\) could be added. By reflection it covers site \(n-1\). Moreover, every matching covers equally many odd and even sites. Hence \(s^\top X(\infty)=0\) and \(X_2(\infty)=X_{n-1}(\infty)=1\). These give three independent kernel vectors when \(n\ge4\).

**4. Affine-support rigidity lemma.** We prove by induction that for every integer \(n\ge4\), a linear form \(a^\top x\) constant on occupied-site vectors of **all** maximal matchings of the path must belong to \(\operatorname{span}\{s,e_2,e_{n-1}\}\).

The initial cases \(n=4,5,6,7\) can be checked from the complete sets of attainable site bitstrings (in order):

| \(n\) | Occupied-site words of all maximal matchings |
|---|---|
| 4 | `0110`, `1111` |
| 5 | `01111`, `11011`, `11110` |
| 6 | `011011`, `011110`, `110110`, `111111` |
| 7 | `0110110`, `0111111`, `1101111`, `1111011`, `1111110` |

For each row, subtract its first vector from the others. The resulting differences have rank \(n-3\): using the first \(n-3\) difference rows and columns \((1)\), \((1,3)\), \((1,3,4)\), and \((1,3,4,5)\) respectively, the determinant has absolute value one. Since the three independent invariants already give an upper bound of \(n-3\), this proves the base cases.

For the induction step \(n\ge8\), consider the subfamily of maximal matchings **containing edge \((1,2)\)**. Its restrictions to sites \(3,\ldots,n\) range over *all* maximal matchings of the remaining path of length \(n-2\). The induction hypothesis forces the restriction \((a_3,\ldots,a_n)\) to be alternating away from positions \(4\) and \(n-1\): there is a constant \(c\) such that \(a_i=c(-1)^{i-1}\) for each \(i\in\{3,\ldots,n\}\setminus\{4,n-1\}\). Likewise, matchings containing the last edge \((n-1,n)\) restrict to every maximal matching on sites \(1,\ldots,n-2\). Thus there is a constant \(d\) such that \(a_i=d(-1)^{i-1}\) for every \(i\in\{1,\ldots,n-2\}\setminus\{2,n-3\}\). Index \(i=3\) is nonexceptional in both restrictions for \(n\ge8\), giving \(c=d\). Every index outside \(\{2,n-1\}\) is nonexceptional in at least one restriction: the only other potential clash is \(4=n-3\), which is excluded by \(n\ge8\). Hence \(a_i=c(-1)^{i-1}\) for all \(i\notin\{2,n-1\}\). The remaining two coefficients are free, proving the lemma.

**5. Terminal rank and principal minors.** Steps 1, 3 and 4 give the terminal kernel exactly, hence rank \(n-3\). For a positive-semidefinite matrix, a principal submatrix is positive definite precisely when no nonzero kernel vector is supported entirely on its retained coordinate set. At finite positive time the sole kernel generator \(s\) has no zero coordinates, so any proper principal submatrix is positive definite. At jamming remove sites \(2\) and \(n-1\); any kernel vector supported on the remaining sites must be proportional to the restriction of \(s\), which is nonzero at every remaining coordinate. Deleting any further site therefore makes the principal submatrix positive definite. This completes the proof.

## Verification

The standalone `verify.py` uses exact rational arithmetic and only the Python standard library. Run `python3 verify.py`. It enumerates every maximal matching of paths through twelve sites and computes the affine rank of the distinct terminal occupied-site words. For paths of four through seven sites it independently compares this support against all possible orderings of edge-attempt times. Separately, it enumerates each subset of edge clocks occurring before a finite time at which each clock has arrival probability \(1/2\), averages uniformly over chronological orders, and computes the full **rational covariance matrix** for paths of four through seven sites. The script checks its exact rank and alternating null vector. It passed 294 exact assertions.

The unrestricted statement is proved by Steps 1–5. Exhaustive checks through finite sizes are corroboration, not infinite proofs. No asymptotic spectral decay rate, general-graph extension, or independent external certification is asserted.

## Relationship to prior work

Gerin's *The Page–Rényi parking process* gives the same random sequential adsorption model, continuous-time construction, a local-minimum representation and probability laws for occupation/vacancy, but the inspected full text does not state the **time-indexed covariance-kernel and rank classification** above. Its primary 2015 classification is 60C05; the first public arXiv version dates to 2014-11-28.

The earlier *Discrete Spacings* work of Klaassen and Runnenburg concerns the global distribution of vacancy counts, rather than the affine support of the full position-indexed indicator vector. Tural's *Valid Inequalities for the Maximal Matching Polytope* (2019) studies a general polyhedral formulation and notes prior tree-polytope descriptions. Its broader maximal-matching constraints are highly relevant and could furnish an alternative route to the **terminal affine-rank calculation**, but no explicit covariance-rank jump or complete site-coordinate kernel was located in the inspected text. The distinction between maximum and maximal matchings is essential: maximum-matching results are not substituted for terminal support.

The full text of Page's foundational 1959 treatment of vacancy totals was not available for inspection. It could contain an earlier implicit derivation, particularly of endpoint coverage. Historical priority for an explicit covariance-rank statement remains a residual risk.

## Limitations

The exact classification is for path graphs with two-site dimers; it does not assert a corresponding rank or identifiability structure for cycles, general trees, longer cars, or spatially heterogeneous arrivals. The theorem does not provide entries or eigenvalue magnitudes of the covariance matrices, nor a rate of approach to terminal singularity. Existing matching-polytope theory may implicitly encode the terminal affine dimension, so explicit novelty and priority require independent literature review. The proof and checker are mathematical and computational evidence, not independent external validation.

## References

- L. Gerin, *The Page–Rényi parking process*, Electronic Journal of Combinatorics 22 (2015), #P4.4. First public arXiv version 2014-11-28: https://arxiv.org/abs/1411.8002 . Full text: https://www.combinatorics.org/ojs/index.php/eljc/article/download/v22i4p4/pdf/ .
- C. A. J. Klaassen and J. Th. Runnenburg, *Discrete Spacings*, arXiv:math/0112056 (2001): https://arxiv.org/abs/math/0112056 .
- M. K. Tural, *Valid Inequalities for the Maximal Matching Polytope*, Adıyaman University Journal of Science 9(2) (2019), 374–385: https://open.metu.edu.tr/handle/11511/57995 .
- E. S. Page, *The Distribution of Vacancies on a Line*, Journal of the Royal Statistical Society, Series B 21 (1959). DOI: https://doi.org/10.1111/j.2517-6161.1959.tb00343.x . Full text not inspected.

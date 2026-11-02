# A cubic distance scale for conditional leaf abundance in uniformly labeled trees

## Finding

**Theorem.** Let \(n\ge2\), and choose a tree \(T\) uniformly from the \(n^{n-2}\) labeled trees with vertex set \(\{1,\ldots,n\}\). Fix two distinct vertices \(u,v\). Write \(D=d_T(u,v)\) for their graph distance and \(L\) for the total number of degree-one vertices (leaves).

For each integer \(1\le \ell\le n-2\), set \(r=\ell+1\) and \(m=n-\ell-1\). Define \(X_q^{(k)}\) to be the number of empty boxes among \(q\) fixed distinguished boxes after \(k\) independent uniform draws into \(n\) labeled boxes. Then the complete conditional law is
\[
 \mathcal L(L\mid D=\ell)=\frac{\ell-1}{\ell+1}\mathcal L(X_{m+2}^{(m-1)})+\frac2{\ell+1}\mathcal L(X_{m+1}^{(m-1)}).
\]
For the boundary distance \(\ell=n-1\), the tree is a path and \(L=2\) almost surely under the conditioning. In particular, for all \(1\le\ell\le n-1\), including this boundary,
\[
 h_n(\ell):=\mathbb E[L\mid D=\ell]
 =\left(1-\frac1n\right)^{n-\ell-2}
  \left(n-\ell-1+\frac{2\ell}{\ell+1}\right).
\]
For every \(1\le\ell\le n-2\), consecutive means satisfy the exact identity
\[
 h_n(\ell+1)-h_n(\ell)
 =\frac{(1-1/n)^{n-\ell-2}}{(n-1)(\ell+1)(\ell+2)}
 \left(2(n-1)-\ell(\ell+1)^2\right).
\]
Thus these conditional expected leaf counts are strictly increasing, possibly have a single two-point plateau, and then strictly decreasing. Let \(\rho_n>0\) be the unique positive solution of \(x(x+1)^2=2(n-1)\). When \(\rho_n\) is not an integer, the maximizing integer distance is \(\max\{1,\lceil\rho_n\rceil\}\); when \(\rho_n=k\) is an integer, both \(k\) and \(k+1\) maximize. For \(n=2\) the sole possible distance is one. The maximizing distance is asymptotic to \((2n)^{1/3}\). Exactly two consecutive maximizers occur for each \(n=1+k(k+1)^2/2\), \(k\ge1\).

There is a distributional obstruction to interpreting the rising mean as stochastic growth. For every \(n\ge11\), \(h_n(3)>h_n(2)\), but
\[
 \Pr(L\ge n-1\mid D=2)=\frac1{3n^{n-4}}>0
 \quad\text{and}\quad
 \Pr(L\ge n-1\mid D=3)=0.
\]
Therefore the leaf-count laws at distances two and three are incomparable in first-order stochastic order for every \(n\ge11\).

## Assumptions and scope

All graphs are finite simple unrooted labeled trees, with the uniform measure on the \(n^{n-2}\) trees. Distance counts edges. A leaf has degree exactly one. Each event \(D=\ell\) has positive probability for every \(1\le\ell\le n-1\). The occupancy variables are auxiliary distributional descriptions, not independently defined observables of the original tree. Only the conditional expectation at the maximal path boundary is extended by the displayed formula; the occupancy mixture is stated for \(m\ge1\) only.

## Proof

**1. Conditioning on the marked path.** A prescribed ordered simple path from \(u\) to \(v\) with \(\ell-1\) internal vertices uses \(r=\ell+1\) vertices. Removing its \(\ell\) path edges leaves a forest of \(r\) rooted components whose roots are precisely the path vertices. Conversely, each such rooted forest joined to the prescribed path yields exactly one tree with that path, and the restriction to those trees is uniform. Conditional on the distance, every ordered choice of the internal path vertices has the same count of rooted forests. In particular, the subsequent conditional leaf law depends only on \(n,\ell\), not on the internal labels.

**2. Rooted-forest child-count identity.** For a fixed root set \(R\) of size \(r<n\), with \(m=n-r\), orient forest edges away from the roots and let \(c_i\) count children of vertex \(i\). The weighted directed matrix-tree identity gives
\[
 \sum_{F\,\text{rooted at}\,R}\prod_{i=1}^n x_i^{c_i}
 =\left(\sum_{i\in R}x_i\right)\left(\sum_{i=1}^n x_i\right)^{m-1}.
\]
For completeness, direct a nonroot vertex toward its parent and assign an edge toward \(j\) weight \(x_j\). With \(W=\sum_i x_i\), the root-deleted directed Laplacian is \(W I_m-\mathbf1(x_j)_{j\notin R}^{\mathsf T}\). The matrix determinant lemma evaluates its determinant as \(W^{m-1}\sum_{i\in R}x_i\), proving the identity and the absence of directed cycles. Setting all weights to one gives \(r n^{m-1}\) forests. Normalizing the polynomial proves that the entire child-count vector has the law of one draw \(S\) uniformly from \(R\), together with \(m-1\) independent draws \(U_1,\ldots,U_{m-1}\) uniformly from all \(n\) vertices, where the number of appearances of each label is its child count.

**3. Recovering degree-one leaves.** Every vertex outside the marked path has exactly one parent edge, hence is a leaf if and only if its child count is zero. Each endpoint of the marked path has one path edge, hence is a leaf exactly when its child count is zero. Each of the \(r-2\) internal path vertices has at least two path edges and is never a leaf. If the extra root draw \(S\) is internal (probability \((r-2)/r\)), all \(m+2\) eligible vertices are empty-box candidates. If \(S\) is an endpoint (probability \(2/r\)), that endpoint is excluded and only \(m+1\) eligible vertices remain. The other \(m-1\) draws are uniform over all \(n\) vertices, so the displayed occupancy mixture follows. If \(m=0\), the original tree consists only of the prescribed path; it has two leaves.

The occupancy identity also yields all binomial moments for \(m\ge1\): for \(0\le j\le n\),
\[
 \mathbb E\left[\binom Lj\middle|D=\ell\right]
 =\left[\binom{m+2}{j}-\frac2{\ell+1}\binom{m+1}{j-1}\right]
 \left(1-\frac jn\right)^{m-1},
\]
where binomial coefficients with an invalid lower index are zero. This follows because a specified set of \(j\) designated boxes is simultaneously empty with probability \((1-j/n)^{m-1}\). The case \(j=1\) gives the conditional mean. For \(m=0\), direct substitution into the mean formula gives two, consistent with the path boundary.

**4. Sharp difference and maximizers.** Divide the conditional mean at \(\ell+1\) by the common factor \((1-1/n)^{n-\ell-2}\), subtract the mean at \(\ell\), and put terms over the common denominator \((n-1)(\ell+1)(\ell+2)\). The numerator reduces exactly to \(2(n-1)-\ell(\ell+1)^2\). As \(\ell(\ell+1)^2\) is strictly increasing for positive integers, all increments change sign at most once, with equality exactly when \(2(n-1)=\ell(\ell+1)^2\). Since the unique positive real root satisfies \(\rho_n\sim(2n)^{1/3}\), the maximizer has that asymptotic scale. For integer \(k\ge1\), the equation gives \(n=1+k(k+1)^2/2\), an integer, producing all and only the two-point plateaus.

**5. Stochastic incomparability.** The difference formula at \(\ell=2\) is positive exactly when \(n>10\). For \(D=2\), the internal path vertex is selected by \(S\) with probability \(1/3\); all \(n-4\) remaining draws must select that same internal vertex for every other vertex to be a leaf. Thus the probability of \(n-1\) leaves is exactly \(1/(3n^{n-4})\). For \(D=3\), both internal path vertices have degree at least two, so the tree has at most \(n-2\) leaves. One law has a larger expectation but a smaller upper tail at threshold \(n-1\), excluding either direction of stochastic domination.

## Verification

The accompanying `verify.py` uses exact rational arithmetic and enumerates all labeled trees by all Prüfer words for \(2\le n\le8\), comparing every conditional binomial moment and conditional mean. It also checks the exact consecutive-mean difference for all admissible \(n\le200\), and the positive distance-two-to-three mean difference for \(11\le n\le50\). The script reports 20,000 passed exact assertions. The all-size theorem rests on the proof above; finite enumeration alone would not establish it.

## Relationship to prior work

Jim Pitman, *Abel-Cayley-Hurwitz multinomial expansions associated with random mappings, forests, and subsets* (University of California, Berkeley Technical Report 498, 1998), gives the weighted rooted-forest enumerator in Theorem 1 and describes fixed paths in random trees in Section 5.7. Those are **prior foundations**, not claimed as new here. In particular, the occupancy mixture can be derived by specializing that established enumerator. The claimed additional structural conclusion is the exact, globally unimodal distance profile, its cubic maximizing scale and complete two-point-tie classification, together with a uniform stochastic-order incomparability family. This comparison is made at the level of mathematical implications, not paper titles. Classical marginal results on leaves or marked-vertex distances do not themselves state this conditional optimization.

## Limitations

The result concerns uniformly labeled trees, two fixed marked vertices and the total number of degree-one leaves, not weighted Cayley trees, arbitrary host graphs or a full multivariate law involving several marked distances. The elementary forest-enumerator input is known; historical novelty of the cross-distance optimization remains dependent on whether earlier literature already draws the same comparison. This is a mathematical proof and a reproducible finite check, not an independently certified or independently audited result.

## References

1. Jim Pitman, *Abel-Cayley-Hurwitz multinomial expansions associated with random mappings, forests, and subsets*, Technical Report 498, University of California, Berkeley (1998), Theorem 1 and Section 5.7. https://statistics.berkeley.edu/sites/default/files/tech-reports/498.pdf
2. A. Meir and J. W. Moon, *The distance between points in random trees*, Journal of Combinatorial Theory **8** (1970), 99–103. https://doi.org/10.1016/S0021-9800(70)80012-6
3. D. J. Aldous, *The random walk construction of uniform spanning trees and uniform labelled trees*, SIAM Journal on Discrete Mathematics **3** (1990), 450–465. https://doi.org/10.1137/0403039

# A sharp rank-independent SVD positivity boundary with vanishing nonnegative-approximation cost

## Finding

Let \(n\geq3\), \(\alpha>0\), \(\beta>0\), and \(u=n^{-1/2}(1,\ldots,1)^\top\). Consider the strictly entrywise-positive, positive-definite matrix
\[
A=\alpha I_n+\beta uu^\top.
\]
For every intermediate rank \(2\leq r\leq n-1\), write \(\mathcal B_r(A)\) for the set of all Frobenius-best rank-at-most-\(r\) approximations. The exact *worst-entry envelope* across all optimal truncated singular-value decompositions is
\[
\min_{B\in\mathcal B_r(A)}\ \min_{1\leq i,j\leq n} B_{ij}
=\frac{\alpha+\beta}{n}-\frac{\alpha}{2}.
\tag{1}
\]
Thus **every** optimal rank-\(r\) truncation is entrywise nonnegative if and only if
\[
\beta\geq\frac{n-2}{2}\,\alpha;
\tag{2}
\]
all are strictly positive when the inequality is strict. The sharp threshold does not depend on the intermediate rank. At equality some optimal truncations have a zero entry; below it there are both strictly positive and negative-entry optimal truncations.

Nevertheless, for *every* \(1\leq r\leq n\) there exists a strictly entrywise-positive, nonnegative-factorizable rank-\(r\) matrix attaining the unconstrained optimal Frobenius error
\[
\min_{\operatorname{rank}(X)\leq r}\|A-X\|_F
=\alpha\sqrt{n-r}.
\tag{3}
\]
Hence nonnegativity and even a nonnegative factorization with \(r\) components carry **zero** approximation penalty on this family.

This coexistence is not merely an artifact of an exact eigenvalue tie. If \(0<\beta<\alpha(n-2)/2\), for every intermediate rank \(r\) there is a rank-\((r-1)\) orthogonal projector \(P\) and, for every \(0<\varepsilon\leq\beta/n\), an entrywise-positive positive-definite matrix \(A_\varepsilon=A+\varepsilon P\) with a **unique** unconstrained best rank-\(r\) approximation \(B_\varepsilon\) such that
\[
(B_\varepsilon)_{12}=-\delta-\frac{\varepsilon}{2},\qquad
\delta=\frac{\alpha}{2}-\frac{\alpha+\beta}{n}>0.
\tag{4}
\]
Writing \(E_\varepsilon=\min_{\operatorname{rank}(X)\leq r}\|A_\varepsilon-X\|_F\), and \(E_\varepsilon^{\mathrm{NNF}}\) for the *infimum* over matrices admitting a factorization \(X=UV^\top\) with \(U,V\in\mathbb R_+^{n\times r}\), one has
\[
E_\varepsilon=\alpha\sqrt{n-r},\qquad
0<E_\varepsilon^{\mathrm{NNF}}-E_\varepsilon\leq\varepsilon\sqrt{r-1}.
\tag{5}
\]
The same upper bound and a strictly positive lower gap hold for the larger class of all entrywise-nonnegative matrices of rank at most \(r\). In particular, as \(\varepsilon\downarrow0\), a unique SVD truncation retains a negative entry of magnitude at least \(\delta\), while the actual cost of imposing nonnegativity or nonnegative factors tends to zero.

## Assumptions and scope

All matrices and factorizations are real; \(\|\cdot\|_F\) is the Frobenius norm, rank constraints mean rank *at most* the stated target, and entrywise positivity means each entry is strictly positive. Calculations are in exact arithmetic. For the first assertion \(2\leq r\leq n-1\); at rank one the unique best approximation \((\alpha+\beta)uu^\top\) is strictly positive, and at rank \(n\) the exact matrix \(A\) is strictly positive. The perturbation and positive-gap assertions require \(0<\beta<\alpha(n-2)/2\). No assertion is made for the degenerate leading-eigenvalue case \(\beta=0\).

The nonnegative-factorization error \(E_\varepsilon^{\mathrm{NNF}}\) is an infimum rather than a presumed attained minimum; no global existence theorem for arbitrary nonnegative factorizations is used.

## Proof

**1. Parametrize all SVD truncations.** The eigenvalues of \(A\) are \(\alpha+\beta\) along \(u\) and \(\alpha\) with multiplicity \(n-1\) on \(u^\perp\). By the Eckart--Young--Mirsky characterization and the strict leading gap \(\beta>0\), for \(2\leq r\leq n-1\) its entire set of best rank-\(r\) approximants is
\[
\mathcal B_r(A)=\{(\alpha+\beta)uu^\top+\alpha P:\ P^2=P=P^\top,\ \operatorname{rank}(P)=r-1,\ Pu=0\}.
\tag{6}
\]
Every member has error \(\alpha\sqrt{n-r}\).

**2. Sharp off-diagonal projector bound.** If \(P\) is any real orthogonal projector, \(0\preceq P\preceq I\). For \(i\ne j\), put \(w_\pm=(e_i\pm e_j)/\sqrt2\). Then
\[
P_{ij}=\frac12\left(w_+^\top P w_+-w_-^\top P w_-\right)\geq-\frac12,
\tag{7}
\]
since both Rayleigh quotients belong to \([0,1]\). Also \(P_{ii}\geq0\). Consequently every entry of (6) is at least \((\alpha+\beta)/n-\alpha/2\).

The bound is attained simultaneously at every intermediate rank: set \(k=r-1\) and \(v=(e_1-e_2)/\sqrt2\); take \(S=\{3,4,\ldots,k+2\}\), a set of size \(k\). Let \(R_S\) be the orthogonal projector onto vectors supported on \(S\) whose coordinates sum to zero (it is the zero projector when \(k=1\)). Then
\[
P=vv^\top+R_S
\tag{8}
\]
is an orthogonal projector of rank \(1+(k-1)=k\) in \(u^\perp\), and \(P_{12}=-1/2\). This proves (1) and (2), including sharpness and strictness.

**3. Construct a positive optimal approximation with nonnegative factors.** Partition the indices into any \(r\) nonempty disjoint groups \(G_1,\ldots,G_r\). Let \(Z\in\{0,1\}^{n\times r}\) be their membership matrix, \(D=\operatorname{diag}(|G_1|,\ldots,|G_r|)\), and \(Q=ZD^{-1}Z^\top\), the rank-\(r\) orthogonal projector onto groupwise-constant vectors. As \(Q u=u\),
\[
C=\alpha Q+\beta uu^\top
=Z\left(\alpha D^{-1}+\frac{\beta}{n}\mathbf1_r\mathbf1_r^\top\right)Z^\top.
\tag{9}
\]
All entries of \(C\) are at least \(\beta/n>0\). The displayed product yields nonnegative factors \(U=Z\), \(V^\top=(\alpha D^{-1}+\beta\mathbf1_r\mathbf1_r^\top/n)Z^\top\), and \(\operatorname{rank}(C)=r\) because the middle factor is positive definite. As \(A-C=\alpha(I-Q)\),
\[
\|A-C\|_F^2=\alpha^2(n-r),
\tag{10}
\]
exactly the Eckart--Young--Mirsky optimum. Hence every target rank has zero nonnegative-factorization penalty, even when other optimal truncations have negative entries.

**4. Remove degeneracy without removing sign loss.** Under the strict subthreshold assumption define \(P\) by (8) and \(A_\varepsilon=A+\varepsilon P\). Since every off-diagonal entry of \(P\) is at least \(-1/2\), all off-diagonal entries of \(A_\varepsilon\) are at least \(\beta/n-\varepsilon/2\geq\beta/(2n)>0\); all diagonal entries are positive. Its three ordered eigenvalue levels are \(\alpha+\beta\) along \(u\), \(\alpha+\varepsilon\) on \(\operatorname{ran}P\), and \(\alpha\) on the remaining \(n-r\) dimensions. The restriction \(\varepsilon\leq\beta/n<\beta\) makes the gap at the target rank strictly positive. Hence its best rank-\(r\) approximation is uniquely
\[
B_\varepsilon=(\alpha+\beta)uu^\top+(\alpha+\varepsilon)P,
\tag{11}
\]
with error \(\alpha\sqrt{n-r}\), while its \((1,2)\) entry is exactly (4).

Any entrywise-nonnegative rank-\(r\) matrix cannot equal \(B_\varepsilon\). The closed set of entrywise-nonnegative matrices of rank at most \(r\) has a minimizer for the Frobenius objective (restrict to a bounded sublevel set). If its minimum equaled the unconstrained error, uniqueness in (11) would force that minimizer to be \(B_\varepsilon\), a contradiction. Thus there is a strict positive penalty even in this larger feasible class, hence also for nonnegative factorizations. On the other hand, the fixed nonnegative-factorizable \(C\) from (9) satisfies
\[
\|A_\varepsilon-C\|_F
\leq\|A-C\|_F+\varepsilon\|P\|_F
=\alpha\sqrt{n-r}+\varepsilon\sqrt{r-1}.
\tag{12}
\]
Together these give (5). Finally \(\|A_\varepsilon-A\|_F=\varepsilon\sqrt{r-1}\to0\), while (4) remains bounded above by \(-\delta\). This proves the full claim.

**Exact three-dimensional illustration.** Set \(n=3\), \(r=2\), \(\alpha=1\), \(\beta=1/4\). Then \(\delta=1/12\); choosing \(\varepsilon=1/12\), the perturbed input has every entry strictly positive, but the unique best rank-two approximation has \((B_\varepsilon)_{12}=-1/8\). The unconstrained Frobenius error is \(1\), while a nonnegative-factorizable rank-two competitor has error at most \(13/12\).

## Verification

The standalone \`verify.py\` uses only the Python standard library. It constructs the exact rational projectors (8) and (9), checks idempotence, rank via trace, zero row sums, sharp \((1,2)\) entry, the Frobenius error identity, entrywise positivity and the perturbed error identity for every intermediate rank in dimensions three through ten. It also checks the three-dimensional illustration. Run it with \`python verify.py\`. These finite checks supplement, but do not replace, the dimension-uniform algebraic proof above.

## Relationship to prior work

Matveev and Budzinskiy (first publicly posted 26 January 2022) introduce sketched alternating projections for nonnegative low-rank matrix approximation and document entrywise-negative truncated-SVD outputs, but do not classify all singular-subspace tie choices on the compound-symmetric positive family or establish a rank-independent sign threshold and vanishing-cost perturbation separation. Song, Ng and Jiang analyze tangent-space alternating projections and convergence, not this exact family. Montaño, Salas and Soto provide general nonnegativity-preserving singular-value perturbation conditions; those conditions do not state the sharp simultaneous extrema over intermediate-rank projectors or the perturbation/NMF comparison. The Eckart--Young--Mirsky theorem, the projector bound, and nonnegative block factorizations are standard ingredients; the precise combined threshold and separation are the assessed result, not a claim that these ingredients are new.

## Limitations

The exact rank-independent boundary is proved only for the compound-symmetric family \(\alpha I+\beta uu^\top\) with \(\beta>0\), not for arbitrary positive matrices, arbitrary rectangular data, weighted Frobenius norms or specific floating-point SVD implementations. The perturbation result gives an *upper bound* on the nonnegative-factorization error excess, not its exact value. A negative unconstrained optimum does not imply that a particular numerical SVD routine must produce that choice at an exact tie. No independent scientific validation or general algorithmic convergence guarantee is asserted.

## References

1. S. A. Matveev and S. Budzinskiy, *Sketching for low-rank nonnegative matrix approximation: a numerical study*, arXiv:2201.11154v1, first posted 2022-01-26, https://arxiv.org/abs/2201.11154.
2. G. Song, M. K. Ng and T.-X. Jiang, *Tangent Space Based Alternating Projections for Nonnegative Low Rank Matrix Approximation*, arXiv:2009.03998v1, 2020-09-02, https://arxiv.org/abs/2009.03998.
3. E. Montaño, M. Salas and R. L. Soto, *Nonnegativity Preservation under Singular Values Perturbation*, Mathematical Problems in Engineering (2009), DOI:10.1155/2009/301582, https://doi.org/10.1155/2009/301582.
4. C. Eckart and G. Young, *The Approximation of One Matrix by Another of Lower Rank*, Psychometrika 1 (1936), 211–218, DOI:10.1007/BF02288367.

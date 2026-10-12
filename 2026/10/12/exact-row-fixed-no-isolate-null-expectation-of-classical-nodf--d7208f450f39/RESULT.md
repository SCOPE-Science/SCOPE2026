# Exact row-fixed, no-isolate null expectation of classical NODF

## Finding
Fix positive integers \(m,n\ge2\) and a prescribed row-degree vector \(\mathbf r=(r_1,\ldots,r_m)\) with \(1\le r_i\le n\) and \(\sum_i r_i\ge n\). Choose a binary \(m\times n\) matrix uniformly from those with row sums \(r_i\) and **positive column sums**. Its exact expected classical, degree-sorted NODF, normalized to \([0,1]\), is computable by the closed finite coefficient formula below using \(O(nm^4)\) integer/rational arithmetic operations, rather than enumerating its exponentially many possible matrices. This includes all column-degree ties exactly. For \(m=3\), \(n=4\), and \(\mathbf r=(1,2,3)\), the exact expectation is \(7/15\), across 60 permitted labeled matrices.

## Assumptions and scope
Rows and columns are labeled. Put \(r_i=\sum_{a=1}^n A_{ia}\), \(d_a=\sum_{i=1}^m A_{ia}\), and \(K=\binom m2+\binom n2\). For a row pair \(i<k\), write \(O_{ik}=\sum_a A_{ia}A_{ka}\); for a column pair \(a<b\), write \(O_{ab}=\sum_i A_{ia}A_{ib}\). The classical degree-sorted index is
\[
\mathrm{NODF}(A)=\frac1K\left(\sum_{i<k:\,r_i\ne r_k}\frac{O_{ik}}{\min(r_i,r_k)} + \sum_{a<b:\,d_a\ne d_b}\frac{O_{ab}}{\min(d_a,d_b)}\right).
\]
Pairs with equal degrees contribute zero. The positive-degree assumption makes every denominator nonzero. The null ensemble holds **only** the row degrees fixed and requires every column to have degree at least one; it does not fix the column degrees. The ensemble is nonempty because \(\sum_i r_i\ge n\), as can be seen by assigning each column at least one of the available row incidences and distributing remaining row incidences without repetition within a row.

Define \(B(t,k)=\binom tk\) for integers \(0\le k\le t\) and zero otherwise. Let
\[
Z=\sum_{j=0}^{n}(-1)^j\binom nj\prod_{i=1}^m B(n-j,r_i).
\]
For each \(1\le i<k\le m\), put
\[
H_{ik}=\sum_{j=0}^{n-1}(-1)^j\binom{n-1}j B(n-1-j,r_i-1)B(n-1-j,r_k-1)\prod_{h\notin\{i,k\}}B(n-j,r_h).
\]
For \(0\le j\le n-2\), define a three-variable polynomial
\[
Q_j(u,v,w)=\prod_{i=1}^m\left[B(n-2-j,r_i)+B(n-2-j,r_i-1)(u+v)+B(n-2-j,r_i-2)uvw\right].
\]
Define coefficients for \(0\le a,b,c\le m\) by
\[
T_{a,b,c}=\sum_{j=0}^{n-2}(-1)^j\binom{n-2}j[u^av^bw^c]Q_j(u,v,w).
\]
The expectation is exactly
\[
\boxed{\mathbb E[\mathrm{NODF}]=\frac{n\displaystyle\sum_{i<k:\,r_i\ne r_k}\frac{H_{ik}}{\min(r_i,r_k)}+\binom n2\displaystyle\sum_{\substack{1\le a,b\le m\\a\ne b}}\frac1{\min(a,b)}\sum_{c=1}^{\min(a,b)}cT_{a,b,c}}{KZ}.}
\]
Every term on the right is an integer count or an explicitly stated rational multiple of one.

## Proof
**Ensemble cardinality.** Independently choosing an \(r_i\)-element subset of \(n\) columns for each row produces each row-constrained matrix once. Inclusion–exclusion over the set of empty columns gives \(Z\). The prescribed inequalities imply \(Z>0\): cover the columns with a union of the row-selected sets, possible because the total capacity is at least \(n\), then fill each row to its target cardinality.

**Row contributions.** Fix different rows \(i,k\) and one marked column, and require both marked entries to be 1. To force all remaining columns nonempty, exclude \(j\) of the other \(n-1\) columns. The two selected rows have \(B(n-1-j,r_i-1)\) and \(B(n-1-j,r_k-1)\) choices, while each other row \(h\) has \(B(n-j,r_h)\) choices. Inclusion–exclusion gives \(H_{ik}\) matrices containing the marked overlap. All \(n\) columns are exchangeable, so the total overlap across matrices is \(nH_{ik}\). Divide by \(Z\) and the smaller fixed row degree.

**Column contributions.** Fix two distinct marked columns. In a row of prescribed sum \(r_i\), selecting neither marked column gives \(B(n-2-j,r_i)\) options; exactly one gives the coefficient \(B(n-2-j,r_i-1)\) for each choice; both gives \(B(n-2-j,r_i-2)\). The monomials \(u,v,w\) record the first marked degree, the second marked degree, and their overlap respectively. Multiplying the factors and including the other \(m-1\) rows yields \(Q_j\). Inclusion–exclusion over the remaining \(n-2\) columns gives \(T_{a,b,c}\), the number of matrices for which those remaining columns are all nonempty and the two marked degrees and overlap are \((a,b,c)\). Restricting to \(a,b\ge1\) makes all columns positive; consequently
\[
\sum_{a,b\ge1}\sum_c T_{a,b,c}=Z.
\]
For column degrees \(a\ne b\), each matrix contributes \(c/\min(a,b)\). All \(\binom n2\) unordered column pairs are exchangeable. The row and column numerators combined, divided by \(KZ\), give the displayed formula.

**Complexity.** For each \(j\), form \(Q_j\) by multiplying \(m\) sparse three-term row factors and retaining coefficient states indexed by three counts between zero and \(m\). There are \(O(m^3)\) such states and \(O(m)\) row updates, hence \(O(m^4)\) arithmetic operations for a given \(j\). The \(n-1\) inclusion–exclusion indices cost \(O(nm^4)\); the \(O(m^2)\) row pairs each require \(O(nm)\) straightforward work, which is no larger. Binomial coefficients can be precomputed. The bound counts exact arithmetic operations and does not claim a constant-time bit model.

## Verification
The accompanying standard-library Python file `verify_fixed_row_nodf.py` directly enumerates every labeled matrix for 305 feasible, sorted row-degree profiles in fifteen small dimension pairs (including \(2\le m\le5\), \(2\le n\le6\) as specified in code), totaling 145,503 admissible matrices. For each profile it independently computes NODF from the pairwise definition and compares the rational mean with the coefficient formula. It also verifies nonnegativity and normalization of the permitted two-column coefficient counts. The command `python verify_fixed_row_nodf.py` prints `VERIFY_OK distinct_profiles 305 covered_matrices 145503 sample_profile (1, 2, 3) sample_mean 7/15 sample_count 60`.

A second example: for \(m=3\), \(n=4\), and \(\mathbf r=(2,2,3)\), there are \(108\) permitted matrices and \(\mathbb E[\mathrm{NODF}]=37/81\). Enumeration is a check on the finite cases; the inclusion–exclusion proof establishes all feasible dimensions.

## Relationship to prior work
Almeida-Neto et al. (2008) introduced NODF and evaluated null behavior using randomized matrices, not the exact conditioned row-fixed expectation above. Britton, Almeida Neto and Corso (2016) rigorously formulated NODF and characterized extremal zero/one matrices rather than this mean. Payrató-Borràs, Hernández and Moreno (2019) analytically addressed expected nestedness for a **canonical soft-constraint** random network ensemble with independent edge probabilities (and approximations tied to marginal degrees), whereas this result uses uniformly sampled hard row sums and explicitly conditions on having no isolated columns. Bruno et al. (2020) contrasted soft and hard constraints and used a microcanonical ensemble fixing both row and column degrees; their experiments do not supply the present exact one-sided-conditioned formula. These are genuinely different probability laws; none of the inspected claims implies the displayed formula by direct specialization.

## Limitations
The formula is for binary incidence matrices, normalized degree-sorted classical NODF, hard **row** constraints, and positive column degrees. It is not a formula for a fixed-fixed ensemble, weighted NODF, full NODF distribution, variance, or a sampling p-value. Arithmetic complexity does not quantify numerical conditioning if the alternating sums are evaluated in floating point; use exact integers/rationals. Although relevant full texts were inspected, a broader unindexed exact combinatorial-algorithm treatment of this null ensemble remains a residual originality risk. No independently reviewed mathematical certification is claimed.

## References
1. Almeida-Neto, M., Guimarães, P., Guimarães, P. R. Jr., Loyola, R. D. and Ulrich, W. (2008). A consistent metric for nestedness analysis in ecological systems: reconciling concept and measurement. *Oikos* 117:1227–1239. DOI: 10.1111/j.0030-1299.2008.16644.x. First published 2008-08-07.
2. Britton, N. F., Almeida Neto, M. and Corso, G. (2016). Which matrices show perfect nestedness or the absence of nestedness? *Biomath* 4:1512171. DOI: 10.11145/j.biomath.2015.12.171.
3. Payrató-Borràs, C., Hernández, L. and Moreno, Y. (2019). Breaking the spell of nestedness: the entropic origin of nestedness in mutualistic systems. *Physical Review X* 9:031024. DOI: 10.1103/PhysRevX.9.031024.
4. Bruno, M. et al. (2020). The ambiguity of nestedness under soft and hard constraints. *Scientific Reports*. DOI: 10.1038/s41598-020-76300-1.

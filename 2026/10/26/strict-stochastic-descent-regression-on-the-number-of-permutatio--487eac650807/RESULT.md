# Strict stochastic descent regression on the number of permutation records

## Finding
Let \(\Pi_n\) be uniformly distributed on the \(n!\) one-line permutations of \(\{1,\ldots,n\}\), and define \(D_n=\#\{i<n:\Pi_n(i)>\Pi_n(i+1)\}\) and \(R_n=\#\{i:\Pi_n(i)>\max_{j<i}\Pi_n(j)\}\), counting the first entry as a record.

**Theorem.** For every integer \(n\ge2\) and all \(1\le r<n\), the conditional descent count given \(R_n=r\) **strictly exceeds** the conditional descent count given \(R_n=r+1\) in first-order stochastic order. Explicitly,
\[
\Pr(D_n\ge h\mid R_n=r)\ge\Pr(D_n\ge h\mid R_n=r+1)
\]
for every integer \(h\), with a strict inequality for at least one integer \(h\) for each \((n,r)\). In fact these conditional distributions admit an almost-sure monotone coupling. The exact aggregate covariance is
\[
\boxed{\operatorname{Cov}(D_n,R_n)=-\frac{n-1}{2n}<0.}
\]
The stochastic assertion is stronger than the negative covariance: every nonconstant increasing test function on the realized descent support has a nonincreasing conditional mean as the record count grows (and the mean descent count decreases strictly at each step).

## Assumptions and scope
The probability law is uniform on the ordinary one-line symmetric group. The comparison is between **total** ordinary descents and **total** left-to-right strict upper records. It is not a comparison between the full sets of descent positions or of record positions. There are no asymptotic assumptions; all \(n\ge2\) and all attainable record counts are covered. First-order stochastic order is tested through all upper tails.

## Proof
**1. Inserting the smallest letter.** Generate \(\Pi_n\) recursively by taking \(\Pi_{n-1}\), increasing all its entries by one, and independently inserting the new smallest entry \(1\) into one of the \(n\) gaps, uniformly. Let \(B_n\) indicate the first (beginning) gap. Then the \(B_j\), \(2\le j\le n\), are independent with \(\Pr(B_j=1)=1/j\), and
\[
R_n=1+\sum_{j=2}^n B_j.
\]
If the old permutation has \(d\) descents, insertion at the beginning preserves descents and adds one record. Among the other \(n-1\) insertion gaps, precisely \(d\) are descent gaps (which preserve the descent count); the other \(n-1-d\) add one descent. With independent \(U_j\sim\operatorname{Uniform}(0,1)\), the exact joint transition therefore is
\[
D_1=0,\quad D_j=D_{j-1}+(1-B_j)\mathbf1\{U_j>D_{j-1}/(j-1)\}.
\tag{1}
\]
This supplies a coupling of the exact \((D_n,R_n)\) law from independent innovations.

**2. Monotone Bernoulli conditioning.** We prove the elementary lemma that if \(B_1,\ldots,B_m\) are independent, nondegenerate Bernoulli variables, their vectors conditioned on \(\sum B_i=k\) admit coordinatewise monotone couplings as \(k\) increases through \(0,\ldots,m\). Write \(w_i=p_i/(1-p_i)>0\) and \(e_k=e_k(w_1,\ldots,w_{m-1})\), with \(e_0=1\) and \(e_k=0\) outside \(0\le k\le m-1\). For the final coordinate,
\[
q_k:=\Pr(B_m=1\mid\textstyle\sum_i B_i=k)
=\frac{w_m e_{k-1}}{e_k+w_m e_{k-1}}.
\]
The elementary symmetric coefficients of positive weights are strictly log-concave on their positive support (Newton's inequalities); hence \(q_k\) increases strictly from \(q_0=0\) to \(q_m=1\). Couple the last Bernoulli coordinate for sums \(k\) and \(k+1\) by one common uniform variable so that the first is at most the second. If the two last coordinates agree, the remaining conditional vectors have adjacent prescribed sums; if they differ, their remaining prescribed sums agree. Induction on \(m\) gives the claimed coordinatewise coupling. This argument includes the boundary cases \(k=0\) and \(k=m-1\) with the stated conventions.

**3. Transfer to descents and strictness.** For fixed \(u\in[0,1]\), the update
\[
(d,b)\longmapsto d+(1-b)\mathbf1\{u>d/(j-1)\}
\]
is nondecreasing in integer \(d\in\{0,\ldots,j-2\}\) and nonincreasing in \(b\in\{0,1\}\). Indeed increasing \(d\) by one can remove at most one unit of the indicator, while adding one to \(d\) itself. Apply the lemma to the independent record-increment vector \((B_2,\ldots,B_n)\), conditioned on its sum \(r-1\) or \(r\), and use common \(U_2,\ldots,U_n\) in (1). Coordinatewise larger \(B\) produces no more descents. This proves the all-tail order.

To see it is strict, the monotone Bernoulli coupling has positive probability that \(B_n\) changes from \(0\) to \(1\), because \(q_r>q_{r-1}\) for the nondegenerate odds \(w_n=1/(n-1)\). Before the last insertion the low-record descent count is at least the high-record count. On this event, if it is already larger, the last update preserves a strict difference (both outputs are integers and the high-record update is zero); if equal, the low-record last update increases it with conditional probability \(1-d/(n-1)>0\), since \(d\le n-2\). Consequently \(\Pr(D^{(r)}>D^{(r+1)})>0\). The mean therefore decreases strictly, forcing a strict upper-tail inequality.

**4. Exact covariance.** Denote \(C_j=\operatorname{Cov}(D_j,R_j)\). From (1), \(\mathbb E[D_j-D_{j-1}\mid D_{j-1},B_j]=(1-B_j)(1-D_{j-1}/(j-1))\), and the standard Eulerian mean is \(\mathbb E D_{j-1}=(j-2)/2\). The increment has mean \(1/2\). Independence of \(B_j\) from previous states gives
\[
\operatorname{Cov}(D_j-D_{j-1},R_{j-1})=-\frac{C_{j-1}}{j},\qquad
\operatorname{Cov}(D_j-D_{j-1},B_j)=-\frac{1}{2j}.
\]
Thus \(C_j=(1-1/j)C_{j-1}-1/(2j)\) with \(C_1=0\); induction yields \(C_n=-(n-1)/(2n)\), as claimed.

## Verification
Run the enclosed standalone `verify_records_descents.py` with Python 3. It compares the insertion recurrence against **independent exhaustive one-line permutation enumeration through size eight**, tests **36,848 exact rational conditional upper-tail inequalities** for sizes through 48, verifies each strict adjacent comparison, and checks the covariance formula at all tested sizes. The checker reports PASS. These finite tests check the implementation and boundary cases; the proof for every \(n\) is the analytic coupling and induction above.

The exact joint-count recurrence used by the checker is
\[
A_j(d,r)=A_{j-1}(d,r-1)+d A_{j-1}(d,r)+(j-d)A_{j-1}(d-1,r),
\quad A_1(0,1)=1,
\]
with out-of-range entries zero. Here \(A_j(d,r)\) counts permutations with exactly \(d\) descents and \(r\) upper records. No exhaustive enumeration beyond size eight is claimed.

## Relationship to prior work
The joint distribution of descents and left-to-right maxima is classical: Carlitz and Scoville's \((\alpha,\beta)\)-Eulerian generating function counts both, and the equality with the cycle/excedance \(q\)-Eulerian distribution is documented explicitly by Ji (2023, Section 1, equations (1.6), (1.11), (1.12)). Jin (2022, Theorem 5) presents an enriched generating function for Euler–Stirling statistics including descents and upper records. These full counting formulas are acknowledged and are not claimed to be new.

The contribution asserted here is the **conditional stochastic inequality for all sample sizes and every pair of adjacent record counts**, with a coordinatewise coupling and exact covariance. The inspected main statements of those counting papers do not state that inequality or give the Bernoulli-conditioning argument. Gnedin's 2006 treatment of conditional record laws and initial-rank generation establishes classical marginal/coherent constructions but does not state the conditional descent-order law. The result has also been compared against related permutation-descent local covariance statements in published research records, which concern different conditioning variables or local indicators.

## Limitations
This is a first-order stochastic ordering of the *scalar descent count*, not a likelihood-ratio ordering and not stochastic domination of entire descent sets. No generalization to arbitrary nonuniform permutation laws is asserted. Earlier polynomial and generating-function identities completely specify the joint distribution; it is possible that an unlocated consequence of those formulas, or classical total positivity theory, has already established the stochastic comparison. The priority claim therefore remains provisional pending external mathematical review.

## References
1. A. Gnedin, “Coherent random permutations with record statistics,” arXiv:math/0611538, first posted 2006-11-17. Open proceedings full text: https://dmtcs.episciences.org/en/articles/3551/download.
2. L. Carlitz and R. Scoville, “Generalized Eulerian numbers: combinatorial applications,” 1974, classical \((\alpha,\beta)\)-Eulerian polynomial framework (as quoted and reconstructed in reference 4).
3. E. Y. Jin, “Symmetric generating functions and Euler–Stirling statistics on permutations,” arXiv:2210.08789, first posted 2022-10-17, Theorem 5. https://ar5iv.labs.arxiv.org/html/2210.08789.
4. K. Q. Ji, “The \((\alpha,\beta)\)-Eulerian Polynomials and Descent-Stirling Statistics on Permutations,” arXiv:2310.01053, first posted 2023-10-02, Section 1. https://arxiv.org/pdf/2310.01053.

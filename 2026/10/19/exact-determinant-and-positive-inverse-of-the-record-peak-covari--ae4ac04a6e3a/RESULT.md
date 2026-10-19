# Exact determinant and positive inverse of the record–peak covariance kernel

## Finding

Let \(n\ge3\), and let \(X_1,\ldots,X_n\) be independent observations from any common continuous distribution. Write
\[
R_i=\mathbf1\{X_i>\max(X_1,\ldots,X_{i-1})\},\qquad
P_j=\mathbf1\{X_{j-1}<X_j>X_{j+1}\}.
\]
The first is the upper-record indicator at position \(i\); the second is the strict local-peak indicator at the interior position \(j\). Define the square cross-covariance matrix
\[
M_n=\bigl[\operatorname{Cov}(R_i,P_j)\bigr]_{2\le i,j\le n-1}.
\]
The **entire** matrix is tridiagonal. For all \(2\le i,j\le n-1\),
\[
\boxed{
(M_n)_{ij}=\begin{cases}
-\dfrac{1}{3i},&j=i-1,\\[3pt]
\dfrac{2i-1}{3i(i+1)},&j=i,\\[3pt]
-\dfrac{i-1}{3i(i+2)},&j=i+1,\\[3pt]
0,&|i-j|\ge2.
\end{cases}}
\tag{1}
\]
In the formulas, an out-of-range diagonal or off-diagonal is simply absent. The exact determinant is
\[
\boxed{\det M_n=\frac{1}{3^{n-2}(n-1)!}>0.}
\tag{2}
\]
More strongly, **every entry of the inverse is strictly positive**. If \(2\le i,j\le n-1\), it is given by the finite, explicit formula
\[
\boxed{
(M_n^{-1})_{ij}=3j\sum_{k=\max(i,j)}^{n-1}
\prod_{s=i}^{k-1}\frac{s-1}{s+2}>0,
}
\tag{3}
\]
where an empty product is one. Thus every nonzero linear combination of interior upper-record indicators has nonzero covariance with at least one interior peak indicator, and conversely. This is a statement about linear cross-covariance, not about samplewise recovery or nonlinear independence.

## Assumptions and scope

The samples are independent and identically distributed with a continuous common law, so ties have probability zero. Equivalently, their relative-order permutation is uniform on the symmetric group. No moment assumption on the observation values is needed, since the statistics are bounded indicators. The matrix contains \(n-2\) nonconstant upper-record indicators and \(n-2\) interior peak indicators. Its rank is \(n-2\) for every integer \(n\ge3\), including the one-dimensional boundary case \(n=3\).

The inverse in (3) is the algebraic inverse of a **cross-covariance** matrix between two different indicator vectors; it is not a covariance precision matrix and does not encode conditional independence.

## Proof

By applying the common continuous distribution function, it suffices to work with independent uniform random variables on \((0,1)\). For each eligible \(i,j\), \(\Pr(R_i=1)=1/i\) and \(\Pr(P_j=1)=1/3\). Hence
\[
\operatorname{Cov}(R_i,P_j)=\frac1i\left[\Pr(P_j=1\mid R_i=1)-\frac13\right].
\tag{4}
\]
We now compute the conditioned peak probability in five exhaustive positional cases.

If \(j\le i-2\), the local peak depends only on the relative order of observations strictly preceding \(i\). This relative order is independent of the event that observation \(i\) exceeds all its predecessors; consequently the conditional peak probability remains \(1/3\). If \(j\ge i+2\), the three observations defining the peak are all after \(i\), so independence again gives \(1/3\).

If \(j=i-1\), a peak would require \(X_{i-1}>X_i\), which is impossible under \(R_i=1\). Thus the conditional probability is zero.

If \(j=i\), then \(R_i=1\) already forces \(X_i>X_{i-1}\). The conditioned observation \(X_i\) is distributed as the maximum of \(i\) independent uniforms and therefore has mean \(i/(i+1)\). Since \(X_{i+1}\) is independent and uniform, the remaining inequality \(X_i>X_{i+1}\) has probability \(i/(i+1)\).

If \(j=i+1\), the event is \(X_i<X_{i+1}>X_{i+2}\). Under \(R_i=1\), denote \(X_i\) by \(Z\), with density \(i z^{i-1}\) on \((0,1)\). Conditioning on \(Z=z\) and integrating over the prospective peak value \(y=X_{i+1}\) gives
\[
\Pr(P_{i+1}=1\mid R_i=1)
=\int_0^1 i z^{i-1}\!\left(\int_z^1 y\,dy\right)dz
=\frac{1}{i+2}.
\tag{5}
\]
These five cases establish the exact conditional probability table
\[
\Pr(P_j=1\mid R_i=1)=
\begin{cases}
0,&j=i-1,\\
i/(i+1),&j=i,\\
1/(i+2),&j=i+1,\\
1/3,&|i-j|\ge2.
\end{cases}
\tag{6}
\]
Substitution into (4) proves (1).

We next give a factorization valid for every dimension. Define lower and upper bidiagonal matrices \(L,U\), indexed by \(2,\ldots,n-1\), through
\[
L_{ii}=1,\quad L_{i,i-1}=-\frac{i-1}{i}\quad(i\ge3),
\tag{7}
\]
and
\[
U_{ii}=\frac1{3i},\quad U_{i,i+1}=-\frac{i-1}{3i(i+2)}\quad(i\le n-2).
\tag{8}
\]
All unspecified entries are zero. The lower and upper off-diagonals of \(LU\) agree immediately with (1). Its diagonal at \(i=2\) is \(1/6\), which is \((2i-1)/(3i(i+1))\) there. For \(i\ge3\), the diagonal is
\[
\frac1{3i}+\frac{i-2}{3i(i+1)}
=\frac{2i-1}{3i(i+1)}.
\]
Thus \(M_n=LU\). Both factors have nonzero diagonal, and their diagonal product gives (2).

Finally the triangular inverses can be computed without asymptotics:
\[
(L^{-1})_{ij}=\frac ji\quad(j\le i),
\qquad
(U^{-1})_{ik}=3k\prod_{s=i}^{k-1}\frac{s-1}{s+2}\quad(k\ge i),
\tag{9}
\]
with all opposite-triangular entries zero. These formulas follow by directly multiplying each candidate inverse with the respective bidiagonal factor (or by one-step triangular recurrences). Since \(M_n^{-1}=U^{-1}L^{-1}\), summing over the shared index \(k\) yields (3). Every term is nonnegative, and at least the term \(k=\max(i,j)\) is strictly positive. Therefore all entries of \(M_n^{-1}\) are positive. Invertibility implies both asserted full-rank linear detection properties, completing the proof.

## Verification

The standalone Python 3 script `verify.py` requires only the standard library. It computes each covariance using exact fractions, checks it against exhaustive enumeration of all \(n!\) uniform permutations for \(3\le n\le8\), verifies the bidiagonal factorization and determinant for \(3\le n\le34\), and computes the rational inverse and checks every inverse entry for strict positivity for \(3\le n\le13\). The script reports **1,167 exact-rational assertions passed**. These finite checks independently corroborate the formulas but do not replace the proof for arbitrary \(n\).

## Relationship to prior work

Upper records and permutation peak statistics are classical objects. Gnedin's *Coherent random permutations with record statistics* (first public version 2006) develops coherent permutation laws and record statistics. Diaconis, Fulman and Holmes, *Analysis of casino shelf shuffling machines* (first public version 2011, primary classification in probability), develops peak statistics and peak-algebra methods. Kasraoui's *The most frequent peak set of a random permutation* (first public version 2012) studies peak-set counts and their optimization. Ji's *The \(\alpha,\beta\)-Eulerian Polynomials and Descent-Stirling Statistics on Permutations* (first public version 2023) is a particularly relevant later joint enumerator for **total numbers** of peaks and records, but its theorem weights totals rather than specific positions; differentiating that polynomial yields aggregate correlations, not the present position-indexed matrix or its positive inverse. These sources motivate the two individual indicator families but their inspected results do not give the cross-covariance matrix between **position-labeled records and interior peaks**, its determinant, or an entrywise-positive inverse. Results for inversion-indicator covariance or fixed-point/descent cross-covariance concern different variables and do not imply (1)–(3) by an identified reduction.

The exact conditioning in (6), the all-size factorization, and inverse positivity are the claims made here; no originality is claimed for the separate one-point record and peak probabilities.

## Limitations

The theorem assumes uniform relative order (equivalently iid continuous samples); it makes no assertion for nonidentical observations, ties, other peak definitions, or conditional independence. A zero cross-covariance entry only expresses vanishing linear covariance, not independence. The result is self-reviewed and has not undergone independent audit or comprehensive historical priority certification. An uninspected general joint record–peak enumerator could in principle imply the formulas, so historical implicit coverage remains a residual originality risk.

## References

1. A. Gnedin, *Coherent random permutations with record statistics*, arXiv:math/0611538, first publicly submitted 2006-11-17. https://arxiv.org/abs/math/0611538
2. P. Diaconis, J. Fulman, S. Holmes, *Analysis of casino shelf shuffling machines*, arXiv:1107.2961, first publicly submitted 2011-07-14. https://arxiv.org/abs/1107.2961
3. A. Kasraoui, *The most frequent peak set of a random permutation*, arXiv:1210.5869, first publicly submitted 2012-10-22. https://arxiv.org/abs/1210.5869
4. K. Q. Ji, *The \(\alpha,\beta\)-Eulerian Polynomials and Descent-Stirling Statistics on Permutations*, arXiv:2310.01053, first publicly submitted 2023-10-02. https://arxiv.org/abs/2310.01053

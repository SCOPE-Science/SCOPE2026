# Fixed points and records have a triangular covariance kernel

## Finding

Let \(\Pi\) be uniformly random in \(S_n\), \(n\ge2\). Define
\[
I_i=\mathbf 1\{\Pi(i)=i\},
\qquad
F_n=\sum_{i=1}^n I_i,
\]
and
\[
R_j=\mathbf 1\!\left\{\Pi(j)=\max_{1\le t\le j}\Pi(t)\right\}.
\]
Thus
\[
R_n^\ast=\sum_{j=1}^nR_j
\]
is the number of left-to-right maxima.

For every \(2\le j\le n\),
\[
\boxed{
\operatorname{Cov}(I_i,R_j)=
\begin{cases}
\dfrac{1}{n j(j-1)},&i<j,\\[6pt]
\dfrac1n\left(\binom{n-1}{j-1}^{-1}-\dfrac1j\right),&i=j,\\[8pt]
0,&i>j.
\end{cases}}
\tag{1}
\]

Summing over \(i\) gives
\[
\boxed{
\operatorname{Cov}(F_n,R_j)
=
\frac{1}{n\binom{n-1}{j-1}}>0,
\qquad 2\le j\le n.
}
\tag{2}
\]
Equivalently,
\[
\boxed{
\mathbb E[F_n\mid R_j=1]
=
1+\frac{j}{n\binom{n-1}{j-1}}.
}
\tag{3}
\]

For \(n\ge4\), the diagonal term has the sharp sign pattern
\[
\operatorname{Cov}(I_j,R_j)<0
\quad(2\le j\le n-2),
\tag{4}
\]
\[
\operatorname{Cov}(I_{n-1},R_{n-1})=0,
\tag{5}
\]
and
\[
\operatorname{Cov}(I_n,R_n)>0.
\tag{6}
\]

The total record count satisfies
\[
\boxed{
\operatorname{Cov}(F_n,R_n^\ast)
=
\frac1n\sum_{k=1}^{n-1}\binom{n-1}{k}^{-1}.
}
\tag{7}
\]
Moreover
\[
\operatorname{Var}(F_n)=1,
\qquad
\operatorname{Var}(R_n^\ast)=H_n-H_n^{(2)},
\tag{8}
\]
where
\[
H_n=\sum_{j=1}^n\frac1j,
\qquad
H_n^{(2)}=\sum_{j=1}^n\frac1{j^2}.
\]
Hence
\[
\boxed{
\operatorname{Corr}(F_n,R_n^\ast)
=
\frac{
\displaystyle\sum_{k=1}^{n-1}\binom{n-1}{k}^{-1}
}{
n\sqrt{H_n-H_n^{(2)}}
}.
}
\tag{9}
\]
Since
\[
\sum_{k=1}^{n-1}\binom{n-1}{k}^{-1}=1+O(n^{-1}),
\]
we obtain
\[
\boxed{
\operatorname{Cov}(F_n,R_n^\ast)\sim\frac1n,
\qquad
\operatorname{Corr}(F_n,R_n^\ast)\sim\frac1{n\sqrt{\log n}}.
}
\tag{10}
\]

Thus cycle-local fixed points and order-local records are asymptotically almost orthogonal, but their finite interaction has an exact triangular positional structure.

## Assumptions and scope

The permutation is uniform on the full symmetric group \(S_n\). Records are upper records in one-line notation.

The result is finite and exact. It does not assert independence or extend the formula to arbitrary conjugation-invariant or record-biased permutation measures.

Equation (8) uses the classical independence of the sequential record indicators of a uniform permutation.

## Proof

For each \(i\),
\[
\Pr(I_i=1)=\frac1n,
\]
and for each \(j\),
\[
\Pr(R_j=1)=\frac1j.
\tag{11}
\]

Fix \(2\le j\le n\).

If \(i>j\), conditioning on \(\Pi(i)=i\) removes one position and value outside the first \(j\) positions. Their relative order remains exchangeable, so
\[
\Pr(R_j=1\mid I_i=1)=\frac1j.
\tag{12}
\]
This yields the zero case of (1).

If \(i<j\), condition on \(\Pi(i)=i\). Among the other \(j-1\) prefix positions, position \(j\) is exchangeable and has probability \(1/(j-1)\) to contain their maximum. That maximum must exceed \(i\), because only \(i-1\) values lie below \(i\), whereas the other \(j-1\) positions require at least \(i\) distinct values. Hence
\[
\Pr(R_j=1\mid I_i=1)=\frac1{j-1}.
\tag{13}
\]
Therefore
\[
\operatorname{Cov}(I_i,R_j)
=
\frac1n\left(\frac1{j-1}-\frac1j\right)
=
\frac1{n j(j-1)}.
\tag{14}
\]

If \(i=j\), condition on \(\Pi(j)=j\). Then \(R_j=1\) exactly when the first \(j-1\) positions contain the values
\[
1,2,\ldots,j-1.
\]
Among the \(\binom{n-1}{j-1}\) possible value sets in those positions, exactly one works. Thus
\[
\Pr(R_j=1\mid I_j=1)
=
\binom{n-1}{j-1}^{-1},
\tag{15}
\]
which completes (1).

Summing (1) over \(i\), the \(j-1\) earlier indices contribute
\[
\frac1{nj}.
\]
This cancels the \(-1/(nj)\) part of the diagonal term, leaving (2). Because
\[
\mathbb EF_n=1
\quad\text{and}\quad
\Pr(R_j=1)=\frac1j,
\]
equation (3) follows.

The diagonal term has the sign of
\[
j-\binom{n-1}{j-1}.
\]
For \(n\ge4\), the binomial coefficient is larger than \(j\) for \(2\le j\le n-2\), equals \(j\) at \(j=n-1\), and equals \(1<j\) at \(j=n\). This proves (4)--(6).

Summing (2) from \(j=2\) to \(n\) proves (7), since \(R_1=1\) deterministically.

For \(n\ge2\), the standard fixed-point second-moment calculation gives
\[
\operatorname{Var}(F_n)=1.
\]
The sequential ranks of a uniform permutation are independent and uniform on their possible ranks, so the \(R_j\) are independent Bernoulli variables with means \(1/j\). This gives the second identity in (8), and therefore (9).

Finally, with \(m=n-1\), the reciprocal-binomial sum has endpoint contribution \(1\), two next-largest terms of order \(1/m\), and all remaining terms together of order \(m^{-2}\). Hence it is \(1+O(m^{-1})\). Since
\[
H_n-H_n^{(2)}=\log n+O(1),
\]
equation (10) follows.

## Verification

The accompanying checker exhaustively enumerates every permutation through \(n=9\).

For every admissible \((i,j)\), it reconstructs the fixed-point and record indicators and verifies (1) exactly with rational arithmetic. It also checks (2), (3), (7), and both variances in (8).

The finite replay is supplementary. The all-\(n\) theorem follows from the conditional exchangeability proof above.

## Relationship to prior work

Foata and Han develop multivariate fixed-point permutation statistics such as \((\mathrm{fix},\mathrm{des},\mathrm{maj})\) and \((\mathrm{fix},\mathrm{exc},\mathrm{maj})\). The inspected full article text defines these fixed-point statistics and transformations but does not pair fixed points with left-to-right maxima in the displayed families.

Gnedin and Gorin develop a framework for record-dependent probability measures on symmetric groups. Their accessible abstract and bibliographic record are directly relevant to the record side, but full article text was not available in the inspected source; this remains a residual comparison risk.

Mukherjee's inspected full manuscript develops fixed-point and cycle-structure limit theory for broad random permutation models. Full-text searches found no left-to-right-maxima statistic.

Recent work of Dubach is the strongest contextual comparison: it proves that the asymptotic number of records in conjugation-invariant permutations changes with fixed-point abundance. The present result is complementary and finite: it identifies the exact covariance between individual fixed-point indicators and individual record indicators under the uniform law.

## Limitations

The kernel relies on the full uniform law. A fixed conjugacy class or nonuniform record-biased law need not preserve the same conditional exchangeability.

The small positive total covariance does not imply a stronger positive-dependence property.

Recent conjugation-invariant theory already establishes broad asymptotic interaction between records and fixed-point abundance. The originality claim here is limited to the exact finite uniform positional kernel, its sign pattern, and the aggregate covariance and correlation.

Older multivariate permutation-enumeration or mesh-pattern literature may encode equivalent mixed moments implicitly.

## References

1. D. Foata and G.-N. Han, “Fix-Mahonian Calculus, I: Two Transformations,” arXiv:math/0703099, first posted 2007-03-04; later *European Journal of Combinatorics* 29 (2008), 1721–1732, DOI 10.1016/j.ejc.2007.09.002.
2. A. Gnedin and V. Gorin, “Record-dependent measures on the symmetric groups,” arXiv:1202.3680, first posted 2012-02-16; later *Random Structures & Algorithms* 46 (2015), 688–706, DOI 10.1002/rsa.20526.
3. S. Mukherjee, “Fixed points and cycle structure of random permutations,” arXiv:1509.04552, first posted 2015-09-15; later *Electronic Journal of Probability* 21 (2016), paper 40, DOI 10.1214/16-EJP4622.
4. V. Dubach, “A geometric approach to conjugation-invariant random permutations,” *Probability Theory and Related Fields* 194 (2026), 245–298, DOI 10.1007/s00440-025-01449-7.

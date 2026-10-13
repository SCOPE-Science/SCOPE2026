# Cycles and records have an exact positive local covariance kernel

## Finding

Let
\[
\Pi_n
\]
be uniformly distributed on the symmetric group \(S_n\), and let
\[
C_n
\]
be the number of cycles of \(\Pi_n\). For each position \(j\), define the upper-record indicator
\[
R_{n,j}
=
\mathbf 1\!\left\{
\Pi_n(j)=\max_{1\le i\le j}\Pi_n(i)
\right\}.
\]

Then, for every
\[
2\le j\le n,
\]
\[
\boxed{
\operatorname{Cov}(C_n,R_{n,j})
=
\frac{j-1}
{n j\binom{n-1}{j-1}}
>0.
}
\tag{1}
\]
At \(j=1\), the record indicator is deterministic, so
\[
\operatorname{Cov}(C_n,R_{n,1})=0.
\tag{2}
\]

Writing
\[
R_n=\sum_{j=1}^nR_{n,j}
\]
for the total number of upper records,
\[
\boxed{
\operatorname{Cov}(C_n,R_n)
=
\frac1n
\sum_{j=2}^n
\frac{j-1}{j\binom{n-1}{j-1}}.
}
\tag{3}
\]
In particular,
\[
\boxed{
\operatorname{Cov}(C_n,R_n)
=
\frac1n+O\!\left(\frac1{n^2}\right).
}
\tag{4}
\]

The two classical statistics have the same variance,
\[
\operatorname{Var}(C_n)
=
\operatorname{Var}(R_n)
=
H_n-H_n^{(2)},
\tag{5}
\]
where
\[
H_n=\sum_{k=1}^n\frac1k,
\qquad
H_n^{(2)}=\sum_{k=1}^n\frac1{k^2}.
\]
Therefore
\[
\boxed{
\operatorname{Corr}(C_n,R_n)
=
\frac{
\displaystyle
\sum_{j=2}^n
\frac{j-1}{j\binom{n-1}{j-1}}
}{
n\left(H_n-H_n^{(2)}\right)
}.
}
\tag{6}
\]
Consequently,
\[
\boxed{
\operatorname{Corr}(C_n,R_n)
\sim
\frac1{n\log n}.
}
\tag{7}
\]

Cycles and upper records are classically equidistributed under the uniform law. Equations (1)--(7) show that this equality in distribution is not an independence phenomenon on the same permutation: every nontrivial record coordinate is positively correlated with the cycle count, while the aggregate standardized dependence nevertheless vanishes.

## Assumptions and scope

Permutations are uniform on \(S_n\). Cycles are taken in the usual disjoint-cycle decomposition. Records are upper left-to-right records in one-line notation.

The result concerns the two statistics evaluated on the same permutation. The classical fundamental bijection sends a record statistic of one permutation to a cycle statistic of another permutation; that equidistribution alone does not determine the same-permutation joint law studied here.

The finite formula (1) is exact for every \(n\ge2\). The asymptotics in (4) and (7) let \(n\) tend to infinity.

## Proof

Use the standard cycle-insertion construction. Given
\[
\sigma\in S_{n-1}
\]
and an insertion site
\[
A\in[n],
\]
construct \(\pi\in S_n\) as follows.

If
\[
A=n,
\]
make \(n\) a singleton cycle and leave \(\sigma\) unchanged on \([n-1]\).

If
\[
A=a<n,
\]
insert \(n\) immediately after \(a\) in the cycle containing \(a\). Equivalently,
\[
\pi(a)=n,
\qquad
\pi(n)=\sigma(a),
\]
and all other images agree with \(\sigma\).

This is a bijection between
\[
S_{n-1}\times[n]
\]
and \(S_n\). Hence, for a uniform permutation, \(\sigma\) and \(A\) are independent, with \(\sigma\) uniform on \(S_{n-1}\) and \(A\) uniform on \([n]\).

The cycle count satisfies
\[
C_n=C_{n-1}+\mathbf 1\{A=n\}.
\tag{8}
\]

Fix
\[
j<n.
\]
In one-line notation the value \(n\) appears at position \(A\). Therefore
\[
R_{n,j}=1
\]
exactly in either of two situations:

1. \(A=j\), so the value at position \(j\) is the global maximum \(n\);
2. \(A>j\) and position \(j\) was already a record of \(\sigma\).

Let
\[
M_{n,j}=\mathbb E[C_nR_{n,j}].
\]
Since
\[
\Pr(R_{n-1,j}=1)=\frac1j
\]
and
\[
\mathbb E C_{n-1}=H_{n-1},
\]
conditioning on \(A\) gives
\[
M_{n,j}
=
\frac1n
\left(
H_{n-1}
+
(n-j)M_{n-1,j}
+
\frac1j
\right).
\tag{9}
\]

Put
\[
d_{n,j}
=
M_{n,j}-\frac{H_n}{j}
=
\operatorname{Cov}(C_n,R_{n,j}).
\]
Using
\[
H_n=H_{n-1}+\frac1n,
\]
equation (9) reduces to
\[
d_{n,j}
=
\frac{n-j}{n}d_{n-1,j}.
\tag{10}
\]

The initial value occurs at \(n=j\). In that case the final position is a record exactly when
\[
A=j,
\]
so
\[
M_{j,j}
=
\frac{H_{j-1}+1}{j}.
\]
Hence
\[
d_{j,j}
=
\frac{j-1}{j^2}.
\tag{11}
\]

Iterating (10) from (11),
\[
d_{n,j}
=
\frac{j-1}{j^2}
\prod_{t=j+1}^n\frac{t-j}{t}
=
\frac{j-1}
{n j\binom{n-1}{j-1}},
\]
which proves (1). The same expression at \(j=n\) is already contained in the base case.

Summing (1) over record positions proves (3).

For the asymptotic covariance, the \(j=n\) term equals
\[
\frac{n-1}{n^2}.
\]
For
\[
2\le j\le n-1,
\]
put \(k=j-1\). Then
\[
\sum_{j=2}^{n-1}
\frac{j-1}{j\binom{n-1}{j-1}}
\le
\sum_{k=1}^{n-2}
\binom{n-1}{k}^{-1}.
\]
The two endpoint terms of the last sum equal \(1/(n-1)\), and every interior term is at most
\[
\binom{n-1}{2}^{-1}.
\]
Thus that whole sum is \(O(1/n)\). Multiplication by the outer factor \(1/n\) in (3) proves (4).

Finally, the cycle-insertion construction also gives
\[
C_n
\overset d=
\sum_{k=1}^n B_k,
\qquad
B_k\sim\operatorname{Bernoulli}(1/k)
\]
independently. The initial-rank representation of a uniform permutation gives the analogous independent Bernoulli representation for \(R_n\). Therefore both variances equal (5). Substituting (3) and using
\[
H_n-H_n^{(2)}\sim\log n
\]
proves (6)--(7).

## Verification

The accompanying checker exhaustively enumerates every permutation in
\[
S_n,
\qquad
2\le n\le9.
\]

For each permutation it computes the disjoint-cycle count directly and identifies every upper-record position directly from one-line notation. Using exact rational arithmetic, it verifies the record probabilities, every local covariance in (1), the total covariance in (3), and both variance formulas in (5).

The exhaustive replay covers
\[
409112
\]
permutations.

Finite enumeration is supplementary. The all-\(n\) theorem follows from the insertion recurrence (9)--(11).

## Relationship to prior work

Gnedin and Gorin study probability measures on permutations that depend on upper-record sets. Their full public manuscript uses exactly the upper-record convention in this result, recalls the independent initial-rank representation under the uniform law, and notes that the fundamental bijection maps record-weighted measures to Ewens cycle-weighted measures. This explains the classical equidistribution link between records and cycles, but it compares the two statistics through a bijection rather than giving their joint law on the same permutation.

Bakšajeva and Manstavičius study additive statistics under the Ewens distribution, with particular attention to cycle counts. Their work provides the standard combinatorial-probability setting for cycle statistics but does not introduce upper-record coordinates in the stated results.

Targeted searches for cycle count together with record indicators, left-to-right maxima, or total record count did not locate the finite kernel (1). The strongest residual risk is older enumerative work on joint permutation statistics, where an equivalent bivariate generating function could imply the same covariance after differentiation.

## Limitations

The theorem is for the uniform law. Under a nonuniform permutation measure, neither the simple insertion-site independence nor the independent-record-rank representation need remain valid.

Positive covariance of every record indicator with the cycle count does not imply association between the full cycle structure and the record process.

The result does not claim a new proof of the classical equidistribution of cycle count and record count. Its content is their same-permutation local covariance kernel and the resulting aggregate dependence scale.

Older permutation-enumeration literature is extensive. An equivalent joint generating function may exist in notation not located by the targeted searches; this is the principal originality risk.

## References

1. A. Gnedin and V. Gorin, “Record-dependent measures on the symmetric groups,” arXiv:1202.3680, first submitted 2012-02-16; later *Random Structures & Algorithms* 46 (2015), 688–706, DOI 10.1002/rsa.20526.
2. T. Bakšajeva and E. Manstavičius, “On statistics of permutations chosen from the Ewens distribution,” arXiv:1303.4540, first submitted 2013-03-19; later *Combinatorics, Probability and Computing* 23 (2014), 889–913, DOI 10.1017/S0963548314000376.

# A sharp quotient-floor phase boundary for critical non-autonomous Hénon basins

## Finding

Fix
\[
0<\kappa<1.
\]
For every
\[
\gamma>0
\]
and integer
\[
n\ge1,
\]
set
\[
k(n)=\lfloor\log_2 n\rfloor
\]
and
\[
q_n^{(\gamma)}
=
\frac{2^n}{n}
\left(
\frac{n}{2^{k(n)}}
\right)^\gamma.
\]
Consider the non-autonomous quadratic Hénon sequence
\[
F_n^{(\gamma)}(z,w)
=
\left(
z^2+\kappa^{q_n^{(\gamma)}}w,
\;\kappa^{q_n^{(\gamma)}}z
\right),
\]
and denote its basin by
\[
\Omega_\gamma.
\]

Every member of this family is on the critical root scale:
\[
\left(q_n^{(\gamma)}\right)^{1/n}
\longrightarrow2.
\]
At the same time,
\[
\rho_n
=
\frac{q_n^{(\gamma)}}{2^n}
\longrightarrow0,
\]
and the successive-quotient sequence has exactly two limit points:
\[
\operatorname{LimPts}
\left(
\frac{q_{n+1}^{(\gamma)}}{q_n^{(\gamma)}}
\right)
=
\left\{2^{1-\gamma},2\right\}.
\]
Hence every prescribed lower quotient limit
\[
L\in(0,2)
\]
is realized by the choice
\[
\gamma=1-\log_2L.
\]

The recent paper identifies convergence of the derivative-normalization series as a central division in the critical regime. For this explicit quotient-oscillating family that division has an exact threshold. If
\[
a_n=\kappa^{q_n^{(\gamma)}},
\qquad
\lambda_n
=
\frac{a_1\cdots a_n}{a_{n+1}},
\]
then
\[
\sum_{n=1}^{\infty}\lambda_n<\infty
\quad\Longleftrightarrow\quad
0<\gamma\le1.
\]
Equivalently, summability holds exactly when the lower quotient limit is at least one:
\[
2^{1-\gamma}\ge1.
\]

All of the basins in the family are parabolic, so none is a Short
\[
\mathbb C^2.
\]
On the entire summable side one can say more:
\[
0<\gamma\le1
\quad\Longrightarrow\quad
\Omega_\gamma\simeq\mathbb C^2.
\]

The endpoint
\[
\gamma=1
\]
is especially informative. There the quotient equals two on every ordinary dyadic step and equals one at every dyadic reset. Thus the elementary positive-gap criterion from the source does not apply, because
\[
2q_n-q_{n+1}=0
\]
on infinitely many, indeed almost all, steps. Nevertheless the source's stronger capture theorem applies: the normalization series is summable and its exponent satisfies
\[
\alpha_n\longrightarrow1.
\]

For
\[
\gamma>1,
\]
the normalization series diverges in the strongest possible local sense: along the indices immediately preceding a dyadic reset,
\[
\lambda_n\longrightarrow\infty.
\]
The source does not determine whether those parabolic basins are biholomorphic to
\[
\mathbb C^2.
\]
Thus the family gives an explicit nonsummable critical test bed on the unresolved side of the new theory.

## Assumptions and scope

The Hénon family and the quantities
\[
\rho_n,
\qquad
\lambda_n,
\qquad
\alpha_n
\]
are used with the normalization of the recent primary source.

The coefficient base
\[
\kappa
\]
is fixed in
\[
(0,1).
\]
The parameter
\[
\gamma
\]
is fixed while
\[
n\to\infty.
\]

The conclusion for
\[
\gamma>1
\]
is deliberately limited. The basin is proved parabolic and the derivative-normalization series is proved nonsummable, but biholomorphism with
\[
\mathbb C^2
\]
is not decided.

The result does not answer the source's question asking for a basin that is neither Short
\[
\mathbb C^2
\]
nor biholomorphic to
\[
\mathbb C^2.
\]
Instead it isolates an explicit one-parameter family that crosses the source's summability boundary while remaining on the same critical root scale.

## Proof

Write
\[
k=k(n)=\lfloor\log_2n\rfloor
\]
and
\[
b_n
=
\left(
\frac{n}{2^k}
\right)^\gamma.
\]
Then
\[
1\le b_n<2^\gamma
\]
and
\[
q_n^{(\gamma)}
=
\frac{2^n b_n}{n}.
\]
It follows immediately that
\[
\frac{1}{n}
\log q_n^{(\gamma)}
=
\log2
+
O\!\left(
\frac{\log n}{n}
\right),
\]
so
\[
\left(q_n^{(\gamma)}\right)^{1/n}\to2.
\]
Also
\[
\rho_n
=
\frac{b_n}{n}\to0.
\]

Now examine the quotient. If
\[
2^k\le n\le2^{k+1}-2,
\]
then
\[
k(n+1)=k(n)
\]
and
\[
\frac{q_{n+1}^{(\gamma)}}{q_n^{(\gamma)}}
=
2
\left(
1+\frac1n
\right)^{\gamma-1}
\longrightarrow2.
\]
At a reset index
\[
n=2^{k+1}-1,
\]
one has
\[
\frac{q_{n+1}^{(\gamma)}}{q_n^{(\gamma)}}
=
2
\frac{n}{n+1}
\left(
2-2^{-k}
\right)^{-\gamma}
\longrightarrow
2^{1-\gamma}.
\]
These are the only two kinds of indices, so the quotient limit set is exactly
\[
\left\{2^{1-\gamma},2\right\}.
\]

Next verify the source's product condition. Let
\[
S_{n-1}
=
\sum_{j=1}^{n-1}q_j^{(\gamma)}.
\]
Since
\[
1\le b_j<2^\gamma,
\]
we have
\[
\frac{S_{n-1}}{q_n^{(\gamma)}}
\le
2^\gamma
\sum_{j=1}^{n-1}
2^{j-n}
\frac{n}{j}.
\]
Split the sum at
\[
j=n/2.
\]
For
\[
j\ge n/2,
\]
the factor
\[
n/j
\]
is at most two, while for
\[
j<n/2
\]
the geometric factor contributes only
\[
O(n2^{-n/2}).
\]
Hence
\[
\sup_{n\gg1}
\frac{S_{n-1}}{q_n^{(\gamma)}}
<\infty.
\]
Choose an integer
\[
m
\]
larger than this bound. Because
\[
0<\kappa<1,
\]
we obtain
\[
\prod_{j=1}^{n-1}a_j
=
\kappa^{S_{n-1}}
\ge
\kappa^{mq_n^{(\gamma)}}
=
a_n^m
\]
for all large
\[
n.
\]
Together with
\[
\rho_n\to0,
\]
the source's parabolicity theorem shows that every
\[
\Omega_\gamma
\]
is parabolic and therefore is not a Short
\[
\mathbb C^2.
\]

We now locate the exact normalization threshold. Put
\[
E_n
=
\sum_{j=1}^nq_j^{(\gamma)}
-q_{n+1}^{(\gamma)}.
\]
Then
\[
\lambda_n
=
\kappa^{E_n}
\]
and the elementary identity
\[
E_n-E_{n-1}
=
2q_n^{(\gamma)}-q_{n+1}^{(\gamma)}
\]
will be useful.

Assume first that
\[
0<\gamma<1.
\]
Let
\[
a=1-\gamma>0.
\]
On a non-reset step,
\[
2q_n-q_{n+1}
=
2q_n
\left[
1-
\left(1+\frac1n\right)^{-a}
\right].
\]
The mean-value theorem gives, for all sufficiently large
\[
n,
\]
\[
1-
\left(1+\frac1n\right)^{-a}
\ge
\frac{c_a}{n}
\]
with a constant
\[
c_a>0.
\]
Since
\[
q_n\ge\frac{2^n}{n},
\]
we obtain
\[
2q_n-q_{n+1}
\ge
c'_a\frac{2^n}{n^2}.
\]
At reset indices the quotient tends to
\[
2^{1-\gamma}\in(1,2),
\]
so the same difference is a positive fixed proportion of
\[
q_n
\]
for all large resets. Consequently
\[
2q_n-q_{n+1}\to+\infty.
\]
The source's elementary basin criterion therefore yields
\[
\Omega_\gamma\simeq\mathbb C^2.
\]
The same estimates show directly that
\[
E_n\to+\infty
\]
at least exponentially fast, so
\[
\sum_n\kappa^{E_n}<\infty.
\]

At the endpoint
\[
\gamma=1,
\]
we have the exact formula
\[
q_n=2^{n-k(n)}.
\]
Let
\[
C_k=E_{2^k},
\qquad
k\ge1.
\]
A direct use of
\[
E_n-E_{n-1}=2q_n-q_{n+1}
\]
shows that
\[
E_n=C_k
\]
for exactly the
\[
2^k
\]
indices
\[
2^k-1\le n\le2^{k+1}-2,
\]
and
\[
C_1=0,
\qquad
C_{k+1}
=
C_k
+
2^{2^{k+1}-k-1}.
\]
In particular,
\[
C_k\ge2^{2^k-k}
\]
for
\[
k\ge2.
\]
Therefore
\[
\sum_{n=1}^{\infty}\lambda_n
=
\sum_{k=1}^{\infty}
2^k\kappa^{C_k}
<\infty.
\]

Let
\[
L_n
=
\sum_{j=n}^{\infty}\lambda_j
\]
and let
\[
\alpha_n
=
\frac{\log(1/L_n)}{\log(1/\lambda_n)}
\]
be the source's capture exponent. The block masses
\[
B_k=2^k\kappa^{C_k}
\]
satisfy
\[
\frac{B_{k+1}}{B_k}
=
2\kappa^{C_{k+1}-C_k}
\longrightarrow0.
\]
Hence, uniformly for indices carrying the exponent
\[
C_k,
\]
we have for all large
\[
k
\]
\[
\lambda_n
\le
L_n
\le
2^{k+1}\lambda_n.
\]
It follows that
\[
1-
\frac{(k+1)\log2}
{C_k\log(1/\kappa)}
\le
\alpha_n
\le1.
\]
Since
\[
k/C_k\to0,
\]
we get
\[
\alpha_n\to1.
\]
The source's stronger derivative-normalization theorem now gives
\[
\Omega_1\simeq\mathbb C^2.
\]

Finally assume
\[
\gamma>1
\]
and put
\[
a=\gamma-1>0.
\]
Choose the last non-reset index in the
\[
k
\]
th dyadic block,
\[
N_k=2^{k+1}-2.
\]
Within that block,
\[
\frac{q_j}{q_{N_k+1}}
=
2^{j-(N_k+1)}
\left(
\frac{j}{N_k+1}
\right)^a.
\]
Writing
\[
h=N_k+1-j
\]
and expanding the absolutely summable geometric moment gives
\[
\sum_{j=2^k}^{N_k}
\frac{q_j}{q_{N_k+1}}
=
\sum_{h\ge1}
2^{-h}
\left(
1-\frac{h}{N_k+1}
\right)^a
+
O(2^{-2^k})
\]
and therefore
\[
\sum_{j=2^k}^{N_k}
\frac{q_j}{q_{N_k+1}}
=
1-
\frac{2a}{N_k+1}
+
O\!\left(N_k^{-2}\right).
\]
The contribution of all earlier dyadic blocks is exponentially smaller than
\[
N_k^{-2}.
\]
Thus
\[
\frac{E_{N_k}}{q_{N_k+1}}
=
-\frac{2(\gamma-1)}{N_k+1}
+
O\!\left(N_k^{-2}\right).
\]
Because
\[
q_{N_k+1}/N_k\to\infty,
\]
we have
\[
E_{N_k}\to-\infty.
\]
Consequently
\[
\lambda_{N_k}
=
\kappa^{E_{N_k}}
\to\infty,
\]
so the normalization series diverges.

This proves the sharp summability threshold and all stated basin consequences.

## Verification

The recent primary paper was inspected at the exact Hénon normalization
\[
a_n=\kappa^{q_n},
\]
the definitions of
\[
\rho_n,
\qquad
d_n=2q_n-q_{n+1},
\qquad
\lambda_n,
\qquad
\alpha_n,
\]
its parabolicity theorem, its simple
\[
\mathbb C^2
\]
criterion, and its stronger derivative-normalization capture theorem.

The source explicitly says that critical sequences with
\[
q_n^{1/n}\to2
\]
but without convergence of
\[
q_{n+1}/q_n
\]
remain a further question. It also identifies convergence or divergence of
\[
\sum_n\lambda_n
\]
as the first natural division in the derivative-normalization analysis.

The older Fornæss–Pal theorem was inspected in its primary preprint, including the theorem and its construction of critical-scale Short and Fatou–Bieberbach examples. That theorem is existential in the auxiliary sequence tending to two and does not state a prescribed quotient-limit set or the sharp normalization threshold obtained here.

All phase-boundary calculations above are exact asymptotic estimates. No finite experiment is used as proof.

## Relationship to prior work

The 2026 paper proves broad sufficient criteria for parabolicity and for biholomorphism with
\[
\mathbb C^2,
\]
and gives a detailed theory of derivative normalization. Under the additional assumption
\[
q_{n+1}/q_n\to2,
\]
it obtains a clean Short-versus-parabolic characterization. Its concluding remarks explicitly separate the nonconvergent-quotient critical regime as a further problem.

The present family stays on the same critical root scale while prescribing the quotient oscillation exactly. It shows that the lower quotient limit can be any number in
\[
(0,2)
\]
and that the normalization series changes behavior at the exact lower-limit value
\[
1.
\]
The endpoint lower-limit value
\[
1
\]
is nontrivial: the source's elementary positive-gap criterion fails there, but its stronger capture theorem still proves biholomorphism with
\[
\mathbb C^2.
\]

Fornæss and Pal previously proved existence of both Short and Fatou–Bieberbach basins on the critical root scale. Their result does not give this quotient-floor phase diagram, and the 2026 source still treats nonconvergent quotients as an unresolved direction.

## Limitations

For
\[
\gamma>1,
\]
the result does not decide whether
\[
\Omega_\gamma
\]
is biholomorphic to
\[
\mathbb C^2.
\]
It proves only parabolicity, failure of the Short property, and divergence of the derivative-normalization series.

Thus no example here is proved to be a third biholomorphism type.

The dyadic family is chosen because it isolates quotient oscillation and the normalization threshold transparently. No claim is made that every critical quotient-oscillating sequence is governed only by its lower quotient limit.

## References

1. L. Boc Thaler, *Complex structures of non-autonomous basins*, arXiv:2610.00627v1, 2026.
2. J. E. Fornæss and R. Pal, *Notes on Short \(\mathbb C^k\)'s*, arXiv:2104.12413v1; Journal of Geometric Analysis 32 (2022), Paper 133.
3. J. E. Fornæss, *Short \(\mathbb C^k\)*, Advanced Studies in Pure Mathematics 42 (2004), 95–108.

# Exact finite-length optimality of uniform rank-one masks for maximal-correlation secrecy

## Statement

Let \(q\) be a prime power, let \(n\ge 3\), and let \(A\) be uniform on
\(\mathbb F_q^{n\times n}\). Consider the rank-one masking class
\[
X=L_1(A+K)L_2,
\]
where \((L_1,L_2,K)\) is independent of \(A\), \(L_1,L_2\in GL_n(\mathbb F_q)\),
and \(\operatorname{rank}(K)\le 1\) almost surely. Then
\[
\boxed{
\inf \rho_{\mathrm m}(A;X)
=
\frac{q^{2n-1}-2q^n+1}{(q^n-1)^2}.
}
\]
The infimum is attained by taking \(L_1=L_2=I\) and taking \(K\) uniformly from
the nonzero rank-one matrices.

Consequently, for independent uniform inputs \(A,B\), if independent masks
\(R,S\) are uniform nonzero rank-one matrices and the server observes
\[
T=(X,Y,Z)=(A+R,B+S,(A+R)(B+S)),
\]
then
\[
\boxed{
\rho_{\mathrm m}((A,B);T)
=
\frac{q^{2n-1}-2q^n+1}{(q^n-1)^2},
}
\]
and this is optimal among complete-view schemes in the same input-independent
rank-at-most-one masking class, even when secret invertible left and right
transformations are allowed.

## Context

Cohen, D'Oliveira and Sprintson prove for every input-independent mask of rank at
most \(r\le n-2\), even with secret invertible transformations, the converse
\[
\rho_{\mathrm m}(A;X)
\ge
\frac{q^{2n-r}-2q^n+1}{(q^n-1)^2}.
\]
They also give two efficiently sampled constructions with secrecy at most
\(q^{-r}\), and conclude finite-length optimality only up to a factor of two and
asymptotic optimality for fixed \(q\) and \(r=o(n)\). The result here closes that
gap exactly at the first nontrivial rank budget \(r=1\).

The Fourier spectrum of fixed-rank matrix relations belongs to the classical
bilinear-forms association scheme of Delsarte. The contribution here is not a
new rank-metric spectrum, but the observation that the nonzero rank-one shell
exactly matches the recent universal privacy converse, yielding a finite-length
minimax theorem for the masking problem.

## Proof

Write \(N=q^n\). A uniform nonzero rank-one matrix can be sampled as
\[
K=uv^\top,
\]
where \(u,v\) are independent and uniform on \(\mathbb F_q^n\setminus\{0\}\).
Indeed, every nonzero rank-one matrix has exactly \(q-1\) representations of
this form, obtained by \((u,v)\mapsto(cu,c^{-1}v)\).

For a nontrivial additive character \(\psi\) of \(\mathbb F_q\), define the
matrix character
\[
\chi_H(M)=\psi(\operatorname{Tr}(H^\top M)).
\]
If \(H\) has rank \(s\ge1\), then
\[
\mathbb E\,\chi_H(K)
=
\mathbb E_{u,v\ne0}\psi(u^\top Hv).
\]
There are \(q^{n-s}-1\) nonzero vectors \(v\) in \(\ker H\). For each such
\(v\), the sum over \(u\ne0\) is \(N-1\). For each of the remaining
\(N-q^{n-s}\) nonzero \(v\), character orthogonality gives a sum of \(-1\).
Therefore the Fourier coefficient depends only on \(s\) and equals
\[
\lambda_s
=
\frac{(q^{n-s}-1)(N-1)-(N-q^{n-s})}{(N-1)^2}
=
\frac{q^{2n-s}-2q^n+1}{(q^n-1)^2}.
\]

For a uniform input on the additive matrix group, additive-noise channels are
diagonalized by these characters, so their maximal correlation is the largest
absolute nontrivial Fourier coefficient:
\[
\rho_{\mathrm m}(A;A+K)=\max_{1\le s\le n}|\lambda_s|.
\]
This is the same Fourier characterization used in the achievability proof of
Cohen--D'Oliveira--Sprintson.

The sequence \(\lambda_s\) is strictly decreasing in \(s\), with
\[
\lambda_n=-\frac1{q^n-1}.
\]
Hence the largest absolute value occurs at an endpoint. For \(q\ge2\) and
\(n\ge3\),
\[
\lambda_1\ge |\lambda_n|
\quad\Longleftrightarrow\quad
q^n(q^{n-1}-3)+2\ge0.
\]
Thus
\[
\rho_{\mathrm m}(A;A+K)
=
\lambda_1
=
\frac{q^{2n-1}-2q^n+1}{(q^n-1)^2}.
\]

The universal converse of Cohen--D'Oliveira--Sprintson with \(r=1\) gives the
same quantity as a lower bound for every admissible
\(L_1(A+K)L_2\). Therefore the displayed construction is exactly optimal.

For two independent inputs with independent rank-one-shell masks, the two upload
channels are independent copies. Their joint Fourier singular values are
products, so the largest nonconstant one is again the single-channel value.
Adding \(Z=XY\) does not change the information in \((X,Y)\), since it is a
deterministic function of them. Hence the complete-view equality follows. For
any competing complete-view scheme, the server may ignore all observations
except an upload, and the same universal converse supplies the matching lower
bound.

## Strict comparison with the two existing samplers at rank one

For the independent-factor sampler of Cohen--D'Oliveira--Sprintson,
\(\rho_{\mathrm m}=q^{-1}\). The rank-one shell is strictly better at every
finite \(n\ge3\):
\[
\frac1q-
\frac{q^{2n-1}-2q^n+1}{(q^n-1)^2}
=
\frac{(q-1)(2q^n-1)}{q(q^n-1)^2}>0.
\]

The uniform rank-ball sampler at radius one mixes the zero matrix with the
nonzero rank-one shell. Its rank-one Fourier coefficient is therefore a strict
convex combination of \(1\) and \(\lambda_1\), and is strictly larger than
\(\lambda_1\). Thus the exact-rank-one shell strictly improves both samplers at
finite length, while approaching \(q^{-1}\) as \(n\to\infty\).

Sampling remains simple: choose independent nonzero \(u,v\) and set
\(K=uv^\top\). In the matrix-multiplication protocol this keeps the rank-one
encoding and decoding cost at \(O(n^2)\) field operations.

## Verification

`artifacts/verify_rank_one_masking.py` performs two supporting checks. First, for
prime fields \(q=2,3,5\) at \(n=3\), it explicitly enumerates all nonzero
rank-one matrices, verifies the shell cardinality and rank, and computes the
character averages for every possible character rank. Second, it verifies the
closed formulas, monotonicity, endpoint comparison, converse match, and gap to
\(1/q\) for 72 additional \((q,n)\) parameter pairs, including nonprime prime
powers. The recorded output is in `artifacts/verify_rank_one_masking.txt`.
These checks support, but do not replace, the analytic proof.

## Limitations

The theorem is specific to the rank budget \(r=1\). It does not prove that the
uniform exact-rank-\(r\) shell is exactly optimal for \(r\ge2\). The strict
finite-length improvement over the factor sampler tends to zero exponentially
in \(n\), so the main gain is an exact minimax characterization rather than a
new asymptotic exponent. The assumptions of uniform inputs and input-independent
rank-constrained masks are inherited from the converse being matched.

## References

1. A. Cohen, R. G. L. D'Oliveira, A. Sprintson, “Low-Rank Masking for Single-Server Matrix Multiplication,” arXiv:2609.18876v1, 2026. https://arxiv.org/abs/2609.18876
2. P. Delsarte, “Bilinear forms over a finite field, with applications to coding theory,” Journal of Combinatorial Theory, Series A 25(3), 226–241, 1978. https://doi.org/10.1016/0097-3165(78)90015-8

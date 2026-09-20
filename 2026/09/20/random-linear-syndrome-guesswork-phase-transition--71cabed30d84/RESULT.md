# Random linear syndromes attain the all-rate Rényi guesswork exponent

## Result

Let \(q\) be a fixed prime power, let \(X\) be an arbitrary random variable on
\(\mathbb F_q^n\), and fix a total order \(\prec\) that refines nonincreasing
probability \(P_X\). Write
\[
G_0(x)=1+|\{y:y\prec x\}|
\]
for the unconstrained optimal guessing rank. Let
\(H\in\mathbb F_q^{m\times n}\) have independent uniform entries and define the
optimal rank inside the syndrome class of \(x\) by
\[
G_H(x)=1+|\{y:y\prec x,\ Hy=Hx\}|.
\]
Because conditioning on \(HX\) only renormalizes probabilities inside each
syndrome class, this is the optimal guessing rank given the syndrome.

For every fixed \(q\) and \(\rho>0\), there are constants
\(0<c_{q,\rho}\le C_{q,\rho}<\infty\), independent of \(n,m\), the source law,
and \(x\), such that with
\[
\mu_x=q^{-m}(G_0(x)-1),
\]
we have the pointwise moment comparison
\[
\boxed{
 c_{q,\rho}(1+\mu_x)^\rho
 \le \mathbb E_H[G_H(x)^\rho]
 \le C_{q,\rho}(1+\mu_x)^\rho .
}
\]
Consequently,
\[
\boxed{
\mathbb E_{H,X}G_H(X)^\rho
\asymp_{q,\rho}
\mathbb E_X\!\left(1+q^{-m}(G_0(X)-1)\right)^\rho
}
\]
and equivalently
\[
\boxed{
\mathbb E_{H,X}G_H(X)^\rho
\asymp_{q,\rho}
1+q^{-m\rho}\mathbb E_X[(G_0(X)-1)^\rho].
}
\]
Here \(A\asymp_{q,\rho}B\) means that their ratio is bounded above and below by
positive constants depending only on \(q,\rho\).

The same constant-factor statement holds when \(H\) is instead uniform over
full-row-rank \(m\times n\) matrices.

### Exact first moment

The first moment has an exact one-shot identity. For the independent-entry
ensemble,
\[
\boxed{
\mathbb E_{H,X}G_H(X)
=1+q^{-m}\bigl(\mathbb E_XG_0(X)-1\bigr).
}
\]
For a uniformly random full-row-rank \(H\),
\[
\boxed{
\mathbb E_{H,X}G_H(X)
=1+\frac{q^{n-m}-1}{q^n-1}
\bigl(\mathbb E_XG_0(X)-1\bigr).
}
\]

## All-rate exponent

Let \(X_n\in\mathbb F_q^n\) be any source sequence and put
\[
\alpha=\frac{1}{1+\rho}.
\]
Suppose
\[
\frac1nH_\alpha(X_n)\to h_\alpha,
\qquad
\frac{m_n}{n}\log_2q\to r.
\]
Then for either the independent-entry ensemble or the uniform full-row-rank
ensemble,
\[
\boxed{
\lim_{n\to\infty}\frac1n\log_2
\mathbb E_{H_n,X_n}[G_{H_n}(X_n)^\rho]
=\rho\,[h_\alpha-r]_+.
}
\]
Moreover the same exponent holds for a typical parity-check matrix:
\[
\boxed{
\frac1n\log_2\mathbb E_{X_n}[G_{H_n}(X_n)^\rho]
\xrightarrow{\mathbb P}
\rho\,[h_\alpha-r]_+.
}
\]
Thus random linear syndrome maps attain, in exponent, the optimum available to
arbitrary encoders with the same number of labels. In particular, deterministic
linear maps with the same exponent exist.

For an IID \(q\)-ary source \(P^{\otimes n}\) and a linear code of rate \(R\),
\(m=n(1-R)\), this becomes
\[
\boxed{
\Lambda_{\rm lin}(\rho)
=\rho\left[
H_{1/(1+\rho)}(P)-(1-R)\log_2q
\right]_+.
}
\]
For binary Bernoulli\((p)\),
\[
\boxed{
\Lambda_{\rm lin}(\rho)
=\rho\,[h_{1/(1+\rho)}(p)+R-1]_+.
}
\]

## Proof of the finite moment law

Fix \(x\), let
\[
T_x=\{y-x:y\prec x\}\subset\mathbb F_q^n\setminus\{0\},
\qquad M=|T_x|=G_0(x)-1,
\]
and set
\[
Z_H=\sum_{v\in T_x}\mathbf 1\{Hv=0\}.
\]
Then \(G_H(x)=1+Z_H\) and
\[
\mathbb EZ_H=Mq^{-m}=\mu.
\]

For an integer \(j\ge1\), expand \(Z_H^j\) over ordered \(j\)-tuples from
\(T_x\). A tuple whose span has dimension \(d\) is annihilated by \(H\) with
probability \(q^{-md}\). The number of rank-\(d\) ordered tuples is at most
\[
\binom jd M^d q^{d(j-d)}:
\]
choose positions and values of a basis, then every remaining vector lies in its
\(q^d\)-element span. Hence
\[
\mathbb EZ_H^j
\le C_{q,j}\sum_{d=1}^j\mu^d,
\]
so for every integer \(j\),
\[
\mathbb E(1+Z_H)^j\le C'_{q,j}(1+\mu)^j.
\]
If \(\rho\ge1\), Jensen gives the lower bound
\(\mathbb E(1+Z_H)^\rho\ge(1+\mu)^\rho\), while Lyapunov's inequality with
\(j=\lceil\rho\rceil\) gives the upper bound.

It remains to handle \(0<\rho<1\), where Jensen points in the wrong direction.
For any \(v\ne0\), at most \(q-2\) other nonzero scalar multiples of \(v\) can
occur in \(T_x\). Therefore
\[
\mathbb EZ_H^2\le (q-1)\mu+\mu^2.
\]
If \(\mu\ge1\), Paley--Zygmund yields
\[
\Pr\{Z_H\ge\mu/2\}\ge c_q>0,
\]
and hence
\(\mathbb E(1+Z_H)^\rho\ge c'_{q,\rho}(1+\mu)^\rho\). If \(\mu<1\), the
trivial lower bound \(G_H\ge1\) suffices. The upper bound for
\(0<\rho<1\) is Jensen. This proves the constant-factor identity.

For uniform full-row-rank \(H\), its kernel is a uniform
\((n-m)\)-dimensional subspace. If \(V\) has dimension \(d\), then
\[
\Pr[V\subseteq\ker H]
=
\prod_{i=0}^{d-1}
\frac{q^{n-m}-q^i}{q^n-q^i}
\]
when \(d\le n-m\), and the probability is zero otherwise. For fixed \(d\) this
is within a \(q,d\)-dependent constant factor of \(q^{-md}\); the cases
\(n-m<d\) only decrease higher-rank contributions. The same moment argument
follows, with the bounded-dimension endpoint handled by \(G_H\ge1\). Taking
\(d=1\) gives the exact full-rank first-moment coefficient above.

## Proof of the exponent and optimality

Arıkan's one-shot guessing inequality implies, because
\(|\mathbb F_q^n|=q^n\),
\[
(1+n\ln q)^{-\rho}2^{\rho H_\alpha(X_n)}
\le
\mathbb E G_0(X_n)^\rho
\le
2^{\rho H_\alpha(X_n)}.
\]
Together with
\(G_0^\rho\asymp_\rho 1+(G_0-1)^\rho\), the finite linear-hashing law gives
\[
\frac1n\log_2\mathbb E_{H_n,X_n}G_{H_n}^\rho
\to \rho[h_\alpha-r]_+.
\]

For completeness, the matching converse for an arbitrary encoder can be obtained
by applying Arıkan's bound inside every encoder cell. Let an encoder have at most
\(M\) labels, and let
\(S_b=\sum_{x:f(x)=b}P_X(x)^\alpha\). Then
\[
\mathbb E G_f(X)^\rho
\ge
(1+n\ln q)^{-\rho}
\sum_b S_b^{1/\alpha}.
\]
Since \(1/\alpha=1+\rho>1\), convexity gives
\[
\sum_bS_b^{1/\alpha}
\ge M^{-\rho}
\left(\sum_xP_X(x)^\alpha\right)^{1/\alpha},
\]
and therefore
\[
\boxed{
\mathbb E G_f(X)^\rho
\ge
(1+n\ln q)^{-\rho}
2^{\rho(H_\alpha(X)-\log_2M)}.
}
\]
Together with \(G_f\ge1\), this is the all-encoder lower bound with exponent
\(\rho[H_\alpha/n-(\log_2M)/n]_+\).

For a random linear syndrome map, \(M\le q^{m_n}\). The deterministic converse
therefore gives the lower exponent uniformly in \(H_n\), while the ensemble
upper bound and Markov's inequality imply that exceeding the claimed exponent by
any fixed positive amount has vanishing probability. This proves convergence in
probability over \(H_n\).

## Relation to recent coset-guesswork results

Tavakoli (2026) proved, for random binary linear codes under IID
Bernoulli\((p)\) noise, the exponent
\[
\rho h_{1/(1+\rho)}(p)+\rho(R-1)
\]
under explicit subcriticality assumptions. In particular, the binary theorem
assumes both
\[
h_b(\delta^*)>1-R,
\qquad
h_b(p)>1-R,
\]
and the q-ary theorem has the analogous condition. These assumptions keep the
stated exponent positive. The result here agrees with Tavakoli's formula inside
that regime, but removes the subcriticality and weight-spectrum conditions and
shows that the continuation to all rates is the positive part. It also applies to
arbitrary source sequences with a Rényi entropy rate, not only IID Hamming-weight
models.

The all-rate threshold is moment-dependent. For an IID source it is
\[
R_c(\rho)=1-\frac{H_{1/(1+\rho)}(P)}{\log_2q}.
\]
For binary Bernoulli\((0.1)\), for example,
\[
R_c(1)=1-h_{1/2}(0.1)=0.3219280949\ldots,
\]
while
\[
R_c(2)=1-h_{1/3}(0.1)=0.2265096268\ldots.
\]
At rate \(R=0.25\), the first-moment exponent is therefore zero whereas the
second-moment exponent is
\[
2\bigl(h_{1/3}(0.1)-0.75\bigr)
=0.0469807463\ldots.
\]
Thus the low-rate regime can exhibit a moment cascade: the mean guess count is
subexponential (and, by the exact first-moment identity here, approaches one
exponentially for this example), while higher moments still grow exponentially.

As \(\rho\downarrow0\), \(R_c(\rho)\) tends to
\(1-H(P)/\log_2q\), the usual additive-channel capacity boundary; higher moments
cross at lower code rates because lower-order Rényi entropy is larger.

## Verification

The accompanying finite enumerator checks three small prime-field instances. It
verifies the exact independent-entry first-moment identity, the exact full-rank
first-moment identity, and, in binary, the exact second-moment identity
\[
\mathbb E_HG_H(x)^2
=1+3\lambda M+\lambda^2M(M-1),
\qquad \lambda=2^{-m},\ M=G_0(x)-1.
\]
It also evaluates several noninteger and integer moments against the
\((1+q^{-m}(G_0-1))^\rho\) proxy. The output is `PASS`. These finite checks are
sanity tests only; the theorem is analytic and covers every finite field.

## Limitations

The constant-factor theorem is stated for fixed field size \(q\); its constants
are not claimed uniform when \(q\) grows with \(n\). The typical-matrix statement
is an exponent statement, not a finite-length concentration theorem with optimized
deviation constants. The result concerns optimal likelihood-ordered guessing
inside a syndrome class; it does not supply a computationally efficient procedure
for generating that order. It also does not provide the second-order
\(\Theta(\log n)\) refinement studied in the recent IID coset-guesswork work.

Originality is claimed only to the best of our knowledge. Random binning and
arbitrary-encoder Rényi/task-encoding bounds are established prior art; the new
claim is that uniform random **linear syndrome maps** satisfy the source-independent
finite constant-factor moment law above and hence attain the optimal all-rate
Rényi guesswork exponent, including the low-rate positive-part transition.

## References

1. H. Tavakoli, *Guesswork Under Linear Constraints: Exact Exponent for Coset Decoding*, arXiv:2607.00205 (2026). https://arxiv.org/abs/2607.00205
2. E. Arıkan, *An Inequality on Guessing and Its Application to Sequential Decoding*, IEEE Transactions on Information Theory 42(1), 99--105 (1996). https://doi.org/10.1109/18.481781
3. C. Bunte and A. Lapidoth, *Encoding Tasks and Rényi Entropy*, IEEE Transactions on Information Theory 60(9), 5065--5076 (2014); arXiv:1401.6338. https://arxiv.org/abs/1401.6338
4. A. Bracher, A. Lapidoth and C. Pfister, *Guessing with Distributed Encoders*, Entropy 21(3), 298 (2019). https://doi.org/10.3390/e21030298
5. A. Bracher, E. Hof and A. Lapidoth, *Guessing Attacks on Distributed-Storage Systems*, arXiv:1701.01981 (2017). https://arxiv.org/abs/1701.01981

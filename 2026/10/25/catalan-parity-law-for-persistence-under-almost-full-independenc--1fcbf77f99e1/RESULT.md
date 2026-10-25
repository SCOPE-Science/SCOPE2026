# Catalan parity law for persistence under almost-full independence

## Finding

Let \(\varepsilon_1,\ldots,\varepsilon_n\) be fair signs such that every proper subset is jointly independent, and put \(\theta=\mathbb E[\prod_{i=1}^n\varepsilon_i]\). For \(S_k=\sum_{i=1}^k\varepsilon_i\) and \(C_j=\frac1{j+1}\binom{2j}{j}\),
\[
\mathbb P(S_k>0\text{ for all }1\le k\le n)=
\begin{cases}
2^{-n}\binom{n-1}{(n-1)/2}, & n\ge3\text{ odd},\\[3pt]
2^{-n}\left[\binom{n-1}{n/2-1}+(-1)^{n/2-1}C_{n/2-1}\theta\right], & n\text{ even}.
\end{cases}
\]
The full-order dependence parameter therefore cancels at every odd horizon and enters with a signed Catalan coefficient at every even horizon.

## Assumptions and scope

Here \(n\ge2\), each \(\varepsilon_i\in\{-1,1\}\) has probability \(1/2\) for each sign, and every subset of at most \(n-1\) coordinates has the product law. The only unconstrained Walsh moment is \(\theta=\mathbb E[\prod_i\varepsilon_i]\in[-1,1]\). Persistence is strict: every partial sum \(S_k\) must be positive. The statement is finite-horizon and does not assert an infinite-time limit.

## Proof

Because every nonempty proper subset of coordinates is independent and fair, all its nonempty Walsh moments vanish. The joint probability mass function is therefore
\[
\mathbb P(\varepsilon=e)=2^{-n}\left(1+\theta\prod_{i=1}^n e_i\right),\qquad e\in\{-1,1\}^n.
\]
Let \(E_n\) be the set of sign sequences whose partial sums are all strictly positive. Then
\[
\mathbb P(E_n)=2^{-n}(N_n+\theta A_n),\quad
N_n=\sum_{e\in E_n}1,\quad A_n=\sum_{e\in E_n}\prod_i e_i.
\]

A sequence in \(E_n\) must start with \(+1\); after removing that first step and lowering the remaining heights by one, its remaining \(n-1\) steps form a nonnegative meander. The ballot/reflection count gives
\[
N_n=\binom{n-1}{\lfloor(n-1)/2\rfloor}.
\]
For a nonnegative meander of length \(m=n-1\) with \(d\) down-steps, the number of paths is \(\binom{m}{d}-\binom{m}{d-1}\), with \(\binom{m}{-1}=0\). Its sign-product weight is \((-1)^d\). Hence
\[
A_n=\sum_{d=0}^{\lfloor(n-1)/2\rfloor}(-1)^d\left[\binom{n-1}{d}-\binom{n-1}{d-1}\right].
\]
Using \(\sum_{d=0}^{r}(-1)^d\binom{m}{d}=(-1)^r\binom{m-1}{r}\) for \(r<m\), this evaluates to \(A_n=0\) for odd \(n\ge3\), and \(A_n=(-1)^{n/2-1}C_{n/2-1}\) for even \(n\). Substitution proves the formula.

## Verification

The proof uses the exact Walsh expansion of the joint law and the ballot/reflection count for nonnegative meanders. The signed count is evaluated by an alternating binomial identity; no simulation or finite sample extrapolation is used. For example, at \(n=4\) the formula is \((3-\theta)/16\), and at \(n=6\) it is \((10+2\theta)/64\), consistent with direct enumeration.

## Relationship to prior work

Berger and Béthencourt study persistence for exchangeable and sign-invariant variables and prove Sparre-Andersen-type bounds, with equality in their atomless setting. The present sign vectors are discrete and have positive probability of zero partial sums; for odd \(n\), a nonzero \(\theta\) also breaks global sign-invariance. Their atomless equality theorem therefore does not give this formula. The result identifies the exact effect of the sole unconstrained \(n\)-way Walsh moment for every finite horizon.

## Limitations

The formula assumes fair signs and independence of every proper coordinate subset. It does not cover arbitrary \((n-1)\)-wise independent nonuniform variables or persistence events with a nonzero barrier. The result is exact for strict positivity and does not identify other statistics of the sign vector.

## References

1. Q. Berger and L. Béthencourt, “An application of Sparre Andersen’s fluctuation theorem for exchangeable and sign-invariant random variables,” arXiv:2304.09031, first submitted 18 April 2023.
2. E. Sparre Andersen, classical fluctuation theorem for symmetric random walks; see Berger–Béthencourt, Section 1, for the statement and references.

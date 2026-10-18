# Exact all-lag position correlations for the Pelikan random map

## Finding

The stationary physical-position autocorrelation of the Pelikan random map admits an exact finite binomial expression at *every* nonnegative integer lag, despite the noncommutativity of doubling and halving. For each \(1/2<p<1\), write \(q=1-p\). If the map at every step is independently selected as \(D(x)=2x\bmod1\) with probability \(p\) or \(U(x)=x/2\) with probability \(q\), begin with the absolutely continuous stationary law \(\mu_p\) and put \(R_n(p)=\mathbb E_{\mu_p,\mathrm{maps}}[X_0X_n]\).

For integers \(n\ge0\), define \(h,k\ge0\) with \(h+k\le n\) and \(n-h+k\) even, and \(m=(n+h+k)/2\). Then

\[
\boxed{R_n(p)=\sum_{\substack{h,k\ge0\\h+k\le n\\n-h+k\ \mathrm{even}}}\biggl[\binom nm-\binom n{m+1}\biggr]p^{(n-h+k)/2}q^{(n+h-k)/2}2^{-h}I_k(p).}
\]

Here \(\binom na=0\) for \(a>n\), and \(I_k(p)=\mathbb E_{\mu_p}[X_0\{2^kX_0\}]\) is given by the explicit expression in the next section. In particular, the sum needs only quadratically many indexed terms as a function of lag, rather than all exponentially many map words. The initial zero lag gives \(R_0(p)=\mathbb E[X_0^2]=4(2p-1)/(3(5p-1))\).

## Assumptions and scope

The position state space is \([0,1)\). All random map choices are mutually independent and independent of \(X_0\). The initial law is the unique absolutely continuous invariant probability \(\mu_p\), not a point mass at the origin. Let \(J_j=(2^{-(j+1)},2^{-j})\) for integers \(j\ge0\). The known invariant density is constant on each cell, with its mass

\[
\pi_j(p)=\mu_p(J_j)=\begin{cases}
\displaystyle\frac{2p-1}{3p-2}\left(2^{-(j+1)}-\left(\frac qp\right)^{j+1}\right),&p\ne 2/3,\\[5pt]
\displaystyle(j+1)2^{-(j+2)},&p=2/3.
\end{cases}
\]

These are nonnegative and sum to one for \(1/2<p<1\). Dyadic endpoints are null sets. Define the fractional part \(\{z\}=z-\lfloor z\rfloor\). Then, for all integers \(k\ge0\),

\[
\boxed{I_k(p)=\frac34\sum_{j=0}^{k-1}\frac{\pi_j}{2^{j+1}}+\frac1{12\,2^k}\sum_{j=0}^{k-1}\pi_j+\frac{7\,2^k}{3}\sum_{j=k}^\infty\frac{\pi_j}{4^{j+1}}.}
\]

Empty sums equal zero. To make the final tail explicitly evaluable, set \(r=q/p\), \(B=(2p-1)/(3p-2)\), \(T_k=\sum_{j=k}^\infty\pi_j/4^{j+1}\). For \(p\ne2/3\),

\[
T_k=B\left(\frac{8^{-(k+1)}}{1-1/8}-\frac{(r/4)^{k+1}}{1-r/4}\right).
\]

For \(p=2/3\), with \(t=1/8\),

\[
T_k=\frac{t^k}{16}\left(\frac{k+1}{1-t}+\frac{t}{(1-t)^2}\right).
\]

Thus all quantities require finitely many arithmetic operations and integer binomial coefficients, including the resonant value \(p=2/3\). For rational \(p\), every \(R_n(p)\) is rational.

## Proof

**1. Map-word normal form.** For an arbitrary length-\(n\) word in the maps \(D,U\), define \(S_0=0\) and let \(S_t\) gain \(+1\) whenever the selected map is \(U\) and \(-1\) whenever it is \(D\). Set

\[
K=-\min(0,S_0,S_1,\ldots,S_n),\qquad H=S_n+K.
\]

Both are nonnegative. For every non-dyadic initial position, the full map-word composition obeys the exact identity

\[
X_n=2^{-H}\{2^KX_0\}.
\]

To prove this, express the binary expansion of \(X_0\) as an infinite string of digits. Applying \(D\) deletes its leading binary digit; applying \(U\) prepends a zero. Each down-step that exceeds the current height of prepended zeros deletes an original digit instead. Hence exactly \(K\) original digits are removed, and exactly \(H\) zeros remain, determined respectively by the lowest prefix sum and terminal prefix sum. This induction accounts for noncommutativity exactly; no interchange of \(D\) and \(U\) is assumed.

**2. Count noncommuting words.** For fixed \(K=k\), \(H=h\), the endpoint is \(S_n=h-k\). Therefore the word contains exactly \(d=(n-h+k)/2\) doubling operations and \(u=(n+h-k)/2\) halving operations. The elementary reflection principle, applied to nearest-neighbor walks from zero ending at \(h-k\) whose minimum is *exactly* \(-k\) (including \(k=0\)), shows that their number is

\[
N_n(h,k)=\binom n{u+k}-\binom n{u+k+1}
=\binom n{(n+h+k)/2}-\binom n{(n+h+k)/2+1}.
\]

For completeness, the number with minimum at least \(-k\) is \(\binom n u-\binom n{u+k+1}\); subtract the count with minimum at least \(-k+1\) to obtain the stated difference, taking the \(k=0\) restriction as minimum zero. Consequently \(\Pr(H=h,K=k)=N_n(h,k)p^dq^u\) and is zero outside the displayed parity/range conditions.

**3. Compute the fractional-position moment.** Conditioned on \(J_j\), the normalized variable \(V=2^{j+1}X_0-1\) is uniform on \((0,1)\). If \(j\ge k\), then \(\{2^kX_0\}=2^kX_0\) and

\[
\mathbb E[X_0\{2^kX_0\}\mid J_j]=\frac{7\,2^k}{3\,4^{j+1}}.
\]

If \(j<k\), put \(a=k-j-1\). Now \(\{2^kX_0\}=\{2^aV\}\). The exact digit-cell identities

\[
\int_0^1\{2^a v\}\,dv=\frac12,\qquad
\int_0^1v\{2^a v\}\,dv=\frac14+\frac1{12\,2^a}
\]

hold for all integers \(a\ge0\), directly by integration over the \(2^a\) equal intervals. Thus

\[
\mathbb E[X_0\{2^kX_0\}\mid J_j]=2^{-(j+1)}\left(\frac34+\frac1{12\,2^{k-j-1}}\right).
\]

Weighting these two cases by \(\pi_j\) gives the formula for \(I_k\). The infinite tail is geometric or arithmetico-geometric and evaluates to the expressions above.

**4. Average.** Independence of the map choices and \(X_0\), together with the word-normal form, gives \(\mathbb E[X_0X_n\mid H=h,K=k]=2^{-h}I_k(p)\). Multiplying by the exact word probabilities and summing proves the displayed finite formula for every \(n\ge0\).

## Verification

The included standalone `verify.py` uses Python's standard-library exact rational arithmetic. For \(p\in\{3/5,2/3,3/4,9/10\}\) and all lags \(0\le n\le5\), it compares the binomial formula to an independently constructed exact integral obtained by enumerating every map word, partitioning at dyadic breakpoints, and integrating the piecewise-affine integrand with the exact stationary density. The script also checks the published closed expressions for lags \(1,2,3\). Every comparison passed. The verification is a finite consistency test; the proof of the claim for unbounded \(n\) is the preceding combinatorial and integral argument.

## Relationship to prior work

Yan, Majumdar, Ruffo, Sato, Beck, and Klages derive the stationary density and the exact physical-position correlations at lags \(1,2,3\), then give an approximate all-lag formula obtained by simplifying noncommuting map words. Their Section III.2 and Appendix D provide explicit expressions for the first three lags. The result here agrees exactly with those expressions and retains the noncommuting word order for *all* lags.

Brevitt and Klages subsequently analyze related closed/open Pelikan dyadic-cell Markov chains and obtain return and Green-function generating functions, notably a top-cell return resolvent. Such cell-state results and the elementary reflection principle are important predecessors, but neither alone supplies the within-cell fractional-position moment needed to compute \(\mathbb E[X_0X_n]\). The contribution is the synthesis of the exact reflected-word count with the nontrivial within-cell positional moment, producing a finite expression for the original physical-position statistic.

## Limitations

This is an exact finite-lag identity, not an asymptotic mixing-rate theorem. It excludes the transition parameter \(p=1/2\), where the absolutely continuous invariant probability used here does not exist; in particular it does **not** settle the originating article's all-time correlation problem at that transition. No uniqueness of this formula across all published literature is established. An equivalent general dyadic-transfer-operator identity could have been published elsewhere; the comparison covers the specific original and related research checked here.

## References

1. J. Yan, M. Majumdar, S. Ruffo, Y. Sato, C. Beck, and R. Klages, *Transition to anomalous dynamics in a simple random map*, Chaos **34**, 023128 (2024), arXiv:2308.09269, initially public August 18, 2023. https://arxiv.org/html/2308.09269v2
2. S. Brevitt and R. Klages, *Quasi-stationary and quasi-ergodic distributions in the Pelikan random map*, arXiv:2607.19084 (2026). https://arxiv.org/abs/2607.19084
3. S. Pelikan, original random-interval-map invariant-density analysis, *Transactions of the American Mathematical Society* **281**, 813 (1984), as cited in reference [1].

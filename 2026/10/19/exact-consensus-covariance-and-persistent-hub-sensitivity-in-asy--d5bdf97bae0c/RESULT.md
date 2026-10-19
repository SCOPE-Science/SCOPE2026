# Exact consensus covariance and persistent hub sensitivity in asynchronous star networks

## Finding

In a uniformly asynchronous closed-neighborhood averaging model on a star with one hub and \(m\ge1\) leaves, deterministic initial opinions \(c,\ell_1,\ldots,\ell_m\in\mathbb R^d\) converge almost surely and in mean square to a common random opinion \(Z\). Provided their initial Euclidean diameter does not exceed the confidence radius, the limiting expectation and covariance are exactly

\[
\mathbb E Z=\frac{(m+1)c+2\sum_{i=1}^m\ell_i}{3m+1},
\qquad
\operatorname{Cov}(Z)=
\frac{\sum_{i=1}^m d_i d_i^{\mathsf T}}{(2m+1)(3m+1)}
+\frac{(m-1)\,s s^{\mathsf T}}{(2m+1)(3m+1)^2},
\]
where \(d_i=\ell_i-c\) and \(s=\sum_{i=1}^m d_i\). These are exact identities for every finite \(m\), not asymptotic approximations.

For the natural family with all leaves initially at \(\ell\) and the hub at \(c\),
\[
\operatorname{Cov}(Z)=\frac{m(m+1)^2}{(2m+1)(3m+1)^2}(\ell-c)(\ell-c)^{\mathsf T}
\ \longrightarrow\ \frac1{18}(\ell-c)(\ell-c)^{\mathsf T}.
\]
Thus, despite almost-sure consensus at every finite size, the consensus location remains non-concentrated in the large-star limit whenever \(c\ne\ell\). In contrast, if \(s=0\), the second rank-one term vanishes: only individual squared disagreements contribute.

## Assumptions and scope

Let \(d\ge1\), \(m\ge1\), and \(\varepsilon>0\). Take the simple undirected star \(K_{1,m}\), with center labeled \(0\) and leaves labeled \(1,\ldots,m\). Starting from deterministic vectors \(x_0(0)=c\) and \(x_0(i)=\ell_i\), suppose
\[
\max_{0\le i,j\le m}\|x_0(i)-x_0(j)\|_2\le\varepsilon.
\]
At each integer step select exactly one vertex independently and uniformly from the \(m+1\) vertices. Replace the chosen vertex's opinion by the equally weighted average of its own current opinion and those of its adjacent vertices within confidence radius \(\varepsilon\); leave every other opinion unchanged. Every subsequent opinion lies in the initial convex hull, whose diameter is at most \(\varepsilon\). Consequently every social edge remains active at every time and the update is exactly the closed-neighborhood average. No nonuniform activation, dynamic edge selection, or exogenous noise is assumed.

## Proof

It suffices initially to prove the scalar statement; apply it to the projection along every \(v\in\mathbb R^d\) to obtain the vector mean and covariance by polarization. At a given time write \(c\) for the hub, \(\ell_i\) for each leaf, and \(d_i=\ell_i-c\). Define
\[
E=\sum_i d_i^2,\qquad s=\sum_i d_i,\qquad T=s^2,
\qquad w=3m+1,\quad n=m+1,
\quad M=\frac{(m+1)c+2\sum_i\ell_i}{w}.
\]
Updating the hub gives \(c'=c+s/n\), whence \(d_i'=d_i-s/n\), \(E'=E-(m+2)T/n^2\), \(T'=T/n^2\) and \(M'-M=s/w\). Updating leaf \(i\) gives \(d_i'=d_i/2\), every other \(d_j\) unchanged, \(E'=E-3d_i^2/4\), \(T'=(s-d_i/2)^2\) and \(M'-M=-d_i/w\).

Taking the average over the \(n\) equally likely updates yields the exact conditional identities
\[
\begin{aligned}
\mathbb E[M'-M\mid x]&=0,\\
\mathbb E[(M'-M)^2\mid x]&=\frac{E+T}{nw^2},\\
\mathbb E[E'\mid x]&=E-\frac1n\left(\frac34 E+\frac{m+2}{n^2}T\right),\\
\mathbb E[T'\mid x]&=T+\frac1n\left(\frac14 E-\left(2-\frac1{n^2}\right)T\right).
\end{aligned}
\]
In particular, \(\mathbb E E_t\le(1-3/(4n))^t E_0\), and \(E_t\) is pathwise nonincreasing. Hence \(E_t\to0\) almost surely and in \(L^1\). The scalar process \(M_t\) is a bounded martingale, since every opinion remains in the initial convex hull. It converges almost surely and in \(L^2\) to some \(Z\), while \(E_t\to0\) forces every opinion to converge to the same \(Z\). This also proves \(\mathbb E Z=M_0\).

To compute the variance without interchanging unverified infinite series, put
\[
a=\frac1{(2m+1)w},\qquad b=\frac{m-1}{(2m+1)w^2},\qquad Q=M^2+aE+bT.
\]
The displayed conditional moment identities imply \(\mathbb E[Q'\mid x]=Q\) exactly, because the coefficients of \(E\) and \(T\) in its conditional drift, after multiplication by \(n\), are respectively
\[
\frac1{w^2}-\frac{3a}{4}+\frac b4=0,
\qquad
\frac1{w^2}-\frac{a(m+2)}{n^2}-b\left(2-\frac1{n^2}\right)=0.
\]
The process \(Q_t\) is bounded (by the initial opinion range) and converges almost surely to \(Z^2\). Bounded convergence therefore gives \(\mathbb E Z^2=M_0^2+aE_0+bT_0\), proving the scalar variance formula. Applying the scalar argument to \(v\cdot x\) for every \(v\in\mathbb R^d\) and using the uniqueness of symmetric matrices determined by their quadratic forms gives the stated covariance matrix. All coordinate limits agree as vectors and are bounded, proving \(L^2\) convergence.

For equal leaves \(d_i=d\), so \(E_0=md^2\) and \(T_0=m^2d^2\); substitution simplifies the variance to \(m(m+1)^2d^2/((2m+1)(3m+1)^2)\). Dividing numerator and denominator by \(m^3\) proves the nonzero \(1/18\) limit. For \(m=1\), the variance reduces exactly to \((\ell_1-c)^2/12\).

## Verification

Run the included standard-library Python file `verification.py` using `python verification.py`. It tests rational-arithmetic one-step updates against all four conditional moment identities and against the harmonic polynomial identity, for star sizes \(m=1,\ldots,8\) and fourteen exact initial configurations per size. It also checks the exact equal-leaf finite-size variance for \(m=1,\ldots,199\). All **872 exact assertions** passed. The all-sizes identities and large-size limit follow from the preceding proof, not from these finite tests.

## Relationship to prior work

Berenbrink, Hoefer, Kaaser, Lenzner, Rau and Schmand introduce and analyze this precise uniform asynchronous, self-inclusive social bounded-confidence rule on arbitrary networks, proving convergence-time statements. Their model and Theorem 1 motivate the question but provide no closed-form star consensus covariance. Elboim, Peres and Peretz give a general martingale framework and variance **bounds** for arbitrary transition matrices, including lazy self-weighted networks; their Corollary 2.4 does not specify the sharp exact coefficient of the present star. Berenbrink, Cooper, Gava, Mallmann-Trenn, Radzik, Kohan Marzagão and Rivera study a related unilateral averaging protocol, but its NodeModel has one global self-weight and a fixed number of randomly sampled neighbors, unlike the varying closed-neighborhood self-weights \(1/(m+1)\) and \(1/2\) here. The present exact covariance and non-concentration law require the explicit two-moment closure for the star. General martingale and covariance identities are not themselves claimed as new.

## Limitations

The theorem is for the complete-confidence regime, so it does not characterize opinion splitting or changing confidence neighborhoods. It assumes uniform independent vertex activation, equal self-and-neighbor averaging at a selected vertex, and deterministic initial opinions. It computes only the first two moments of the limiting consensus and not its full distribution, convergence time, or concentration for other graph families. Publication priority against uninspected general random-matrix-product or stochastic-consensus literature remains an uncertainty; an independently conducted novelty audit has not been performed.

## References

1. P. Berenbrink, M. Hoefer, D. Kaaser, P. Lenzner, M. Rau and D. Schmand, *Asynchronous Opinion Dynamics in Social Networks*, first arXiv version 2022-01-30, arXiv:2201.12923. https://arxiv.org/abs/2201.12923 .
2. D. Elboim, Y. Peres and R. Peretz, *The Asynchronous DeGroot Dynamics*, first arXiv version 2022-09-13, arXiv:2209.05764. https://arxiv.org/abs/2209.05764 .
3. P. Berenbrink, C. Cooper, C. Gava, F. Mallmann-Trenn, T. Radzik, D. Kohan Marzagão and N. Rivera, *Distributed Averaging in Opinion Dynamics*, 2023, arXiv:2211.17125 (2022 preprint). https://arxiv.org/abs/2211.17125 .

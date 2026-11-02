# A universal size-dependent cycle covariance switch in Ewens derangements

## Finding
For every \(\theta>0\), weighted random derangements exhibit a single transition in the sign of the covariance between the total number of cycles and the number of cycles of a prescribed length. Short cycles have positive covariance with the total count; sufficiently long cycles have negative covariance. The transition occupies asymptotically the fraction \(1-e^{-1/\theta}\) of the labels. Both an exact finite-size formula and a full macroscopic covariance profile are available.

Precisely, write \(C_r\) for the count of cycles of length \(r\), \(K=\sum_{r\ge2}C_r\), and \(A_m(\theta)\) for the total \(\theta^K\)-weight of derangements of \(m\) labels, with \(A_0=1,A_1=0\). Put \(\mu_0=0\) and \(\mu_m=\theta A_m'(\theta)/A_m(\theta)\) for \(m\ge2\). For \(n\ge4\) and \(r\in\{2,\ldots,n-2,n\}\),
\[
\operatorname{Cov}(C_r,K)=\frac{\theta n!A_{n-r}(\theta)}{r(n-r)!A_n(\theta)}\left(1+\mu_{n-r}-\mu_n\right).
\]
The covariance signs are nonincreasing across admissible lengths, beginning positive at \(r=2\) and ending negative at \(r=n\), with no return to positivity. Equality is not excluded at an intervening length. The impossible length \(n-1\) has \(C_{n-1}\equiv0\).

Let \(r_n(\theta)\) be the first admissible cycle length with covariance at most zero. Then
\[
\lim_{n\to\infty}\frac{r_n(\theta)}n=1-e^{-1/\theta}.
\]
More strongly, for fixed \(0<\alpha<1\) and \(r=\lfloor\alpha n\rfloor\),
\[
\lim_{n\to\infty} n\operatorname{Cov}(C_r,K)
=\frac{\theta}{\alpha}(1-\alpha)^{\theta-1}
\left(1+\theta\log(1-\alpha)\right).
\]
For example, the asymptotic boundary is \(1-e^{-1}\) in uniform derangements, \(1-e^{-2}\) when \(\theta=1/2\), and \(1-e^{-1/2}\) when \(\theta=2\).

## Assumptions and scope
A derangement is a permutation of \(n\) labels with no fixed point. Every derangement \(\pi\) has probability \(\theta^{K(\pi)}/A_n(\theta)\), with fixed \(\theta>0\). The main finite statements require \(n\ge4\). A cycle of length \(n-1\) would leave a forbidden singleton and therefore cannot occur. The empty derangement on zero labels has weight one and cycle count zero; the one-label derangement does not exist. Macroscopic limits hold at fixed \(\theta>0\), for \(\alpha\) strictly between zero and one. They do not assert uniformity when \(\theta\) or \(\alpha\) vary with \(n\).

## Proof
**Cycle marking.** Mark one \(r\)-cycle in a weighted derangement of \(n\) labels. There are \(n!/[r(n-r)!]\) ways to choose its labels and cyclic order; it contributes weight \(\theta\). Deleting the marked cycle leaves an independently weighted derangement of size \(n-r\). Therefore
\[
\mathbb E C_r=\frac{\theta n!A_{n-r}(\theta)}{r(n-r)!A_n(\theta)},\qquad
\mathbb E(C_rK)=\mathbb E C_r\,(1+\mu_{n-r}).
\]
Subtracting \(\mathbb E C_r\,\mathbb EK\) proves the covariance identity. If \(n-r=1\), the factor \(A_1=0\), and this size is excluded from the sign comparison.

**Monotonicity of the residual mean.** Let \(B_m=\theta A_m'(\theta)\). Deleting the largest label from a cycle of length at least three, or deleting its entire two-cycle when necessary, gives the standard weighted derangement recurrence
\[
A_m=(m-1)(A_{m-1}+\theta A_{m-2}),\qquad
B_m=(m-1)(B_{m-1}+\theta B_{m-2}+\theta A_{m-2}),\quad m\ge4.
\]
The initial values are \(A_2=\theta,A_3=2\theta,B_2=\theta,B_3=2\theta\), so \(\mu_2=\mu_3=1\). Defining
\[
p_m=\frac{A_{m-1}}{A_{m-1}+\theta A_{m-2}}\in(0,1),
\]
gives \(\mu_m=p_m\mu_{m-1}+(1-p_m)(1+\mu_{m-2})\). If \(\delta_m=\mu_m-\mu_{m-1}\), then \(\delta_3=0\) and \(\delta_m=(1-p_m)(1-\delta_{m-1})\). Induction proves \(0<\delta_m<1\) for \(m\ge4\), as well as
\[
\delta_m+\delta_{m-1}=1-p_m(1-\delta_{m-1})<1.
\]
Consequently \(\mu_m\) is nondecreasing over admissible \(m\), strictly increasing after \(m=3\), and \(0<\mu_n-\mu_{n-2}<1\) for every \(n\ge4\). Hence \(1+\mu_{n-2}-\mu_n>0\) whereas \(1+\mu_0-\mu_n=1-\mu_n<0\); the second inequality holds since \(\mu_n>1\). Because \(\mu_{n-r}\) decreases as \(r\) increases through admissible sizes, the sign can cross zero only once in the weak sense claimed.

**Asymptotic boundary and covariance profile.** The exponential generating function of \(A_m\) is
\[
F(z,\theta)=\sum_{m\ge0}\frac{A_m(\theta)}{m!}z^m
=\exp\!\left(\theta\sum_{j\ge2}\frac{z^j}{j}\right)
=e^{-\theta z}(1-z)^{-\theta}.
\]
For each fixed \(\theta>0\), standard coefficient asymptotics at \(z=1\), locally uniform in \(\theta\), give
\[
\frac{A_m(\theta)}{m!}=\frac{e^{-\theta}}{\Gamma(\theta)}m^{\theta-1}\bigl(1+O_\theta(m^{-1})\bigr).
\]
Differentiating its logarithm with respect to \(\theta\), justified by locally uniform analytic coefficient asymptotics, yields
\[
\mu_m=\theta\partial_\theta\log A_m(\theta)
=\theta\log m-\theta-\theta\psi(\theta)+O_\theta(m^{-1}),
\]
where \(\psi\) is the logarithmic derivative of the gamma function. If \(r=\lfloor\alpha n\rfloor\), then \(n-r\) is proportional to \(n\) and
\[
1+\mu_{n-r}-\mu_n\longrightarrow1+\theta\log(1-\alpha),\qquad
n\mathbb EC_r\longrightarrow\frac{\theta}{\alpha}(1-\alpha)^{\theta-1}.
\]
Multiplying proves the signed profile. Its sign changes at the unique solution of \(1+\theta\log(1-\alpha)=0\), namely \(\alpha=1-e^{-1/\theta}\). For any fixed \(\varepsilon>0\), the signs at fractions at least \(\varepsilon\) to either side of that solution are eventually opposite, and the established finite monotonicity traps \(r_n(\theta)/n\) between them. This proves convergence of the transition fraction.

## Verification
A standalone exact-arithmetic program, `checks/verify.py`, validates the weighted derangement recurrences for three rational Ewens parameters, independently enumerates all derangements through \(n=8\), compares the exact marked-cycle and mixed-moment identities against direct enumeration, checks covariance signs and monotonicity through \(n=450\), and probes the predicted phase fraction. The program uses only Python's standard library. The delivered check completed 5,658 assertions without a failure, representing 51,024 enumerated weighted derangement cases across parameters. Finite checks illustrate the theorem; the all-size conclusions follow from the proof above.

## Relationship to prior work
Da Silva, Jamshidpey and Tavaré derive weighted derangement cycle-count factorial moments and mean total cycle counts. Their equations already determine all individual finite covariance values in principle; the moment formula is **not** presented as new. The contribution here is the simultaneous sign ordering over cycle length, the proof of an exact one-transition structure for every \(\theta>0\), the parameter-dependent limiting transition fraction, and the full signed macroscopic covariance profile. Their later work develops biased derangement Markov representations but does not present this particular joint cycle-count sign classification. Ford's toolkit treats cycle statistics of unrestricted permutations and supplies related but different bounds. An implicit earlier derivation of the sign classification remains possible.

## Limitations
The finite theorem is stated only for \(n\ge4\), excludes the structurally forbidden length \(n-1\), and allows exact zero covariance at a transition; it does not claim strict signs at every interior frequency. The asymptotic profile concerns fixed \(\theta\) and a macroscopic \(r\), not small cycles with fixed \(r\) or parameters changing with \(n\). Covariance signs do not imply independence, negative association, or a general stochastic ordering. Priority has not been independently certified.

## References
1. P. H. da Silva, A. Jamshidpey, S. Tavaré, *Random derangements and the Ewens Sampling Formula*, arXiv:2006.04840 (first posted 2020-06-08); journal version *The Feller Coupling for random derangements*, Stochastic Processes and their Applications 150 (2022), 1139–1164, DOI:10.1016/j.spa.2021.09.003.
2. P. H. da Silva, A. Jamshidpey, S. Tavaré, *Markov chains arising from biased random derangements*, arXiv:2211.13831 (first posted 2022-11-24).
3. K. Ford, *Cycle type of random permutations: A toolkit*, arXiv:2104.12019 (first posted 2021-04-24), Discrete Analysis 2022:9.

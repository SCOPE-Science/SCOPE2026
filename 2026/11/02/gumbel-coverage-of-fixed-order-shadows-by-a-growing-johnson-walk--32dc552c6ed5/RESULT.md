# Gumbel coverage of fixed-order shadows by a growing Johnson walk

## Finding

**Theorem (growing-block Markovian super-coupons).** Fix an integer \(s\ge2\). Let \(r_n\) be integers satisfying
\[
r_n\longrightarrow\infty,\qquad r_n\log n=o(n),\qquad s\le r_n<n.
\]
Start a Markov chain \(H_0,H_1,\ldots\) uniformly on the \(r_n\)-subsets of \([n]\). Independently at every update, remove a uniformly chosen element of \(H_t\) and replace it by a uniformly chosen element of \([n]\setminus H_t\). An \(s\)-subset is collected as soon as it belongs to any visited state, including \(H_0\). Write \(T_n\) for the first update index by which all \(s\)-subsets are collected, and put
\[
M_n=\binom ns,\qquad \beta_n=\binom{r_n-1}{s-1},\qquad a_n=\frac{M_n}{\beta_n}.
\]
For every fixed real \(x\), the number \(N_n(x)\) of uncollected \(s\)-subsets at update \(\lfloor a_n(\log M_n+x)\rfloor\) satisfies
\[
N_n(x)\ \Longrightarrow\ \operatorname{Poisson}(e^{-x}).
\]
Consequently,
\[
\Pr\!\left\{\frac{T_n}{a_n}-\log M_n\le x\right\}\longrightarrow \exp(-e^{-x}),
\qquad
\mathbb E T_n\sim a_n\log M_n\sim\frac{n^s\log n}{r_n^{s-1}}.
\]
The law holds uniformly for *every* sequence of growing blocks satisfying the displayed sparse-growth assumptions, not only for a chosen polynomial growth rate.

## Assumptions and scope

All graphs and random variables are finite for each \(n\); the statement concerns \(n\to\infty\) with \(s\) fixed. The Markov chain is the discrete-time, nonlazy, single-replacement walk on the Johnson graph and is initialized in its uniform stationary law. The time \(T_n\) counts updates after the initially observed state, not independent drawings of entire blocks. Constants hidden in \(O_{s,d}(\cdot)\) may depend on fixed \(s\) and fixed number \(d\) of target subsets, but not on their overlap pattern or on the allowed sequence \(r_n\).

## Proof

**1. A bounded projection for any finite target family.** Fix any \(d\ge1\) distinct target \(s\)-subsets \(S_1,\ldots,S_d\). Set \(U=\bigcup_i S_i\), \(u=|U|\le ds\), and \(J_t=H_t\cap U\). Let \(B=\{J:\exists i,\ S_i\subseteq J\}\), and restrict the transition matrix of \(J_t\) to subsets avoiding \(B\), obtaining the substochastic matrix \(Q\). If \(J\) contains \(k\) labels of \(U\), put \(h=n-r_n-u+k\). The exact un-killed transition probabilities are the following contributions, summed when two descriptions reach the same state:
\[
\begin{aligned}
J\to J\setminus\{z\}\ (z\in J)&:\quad \frac{h}{r_n(n-r_n)},\\
J\to (J\setminus\{z\})\cup\{y\}\ (z\in J,\ y\in U\setminus J)&:\quad\frac1{r_n(n-r_n)},\\
J\to J\cup\{y\}\ (y\in U\setminus J)&:\quad\frac{r_n-k}{r_n(n-r_n)},\\
J\to J&:\quad\frac{(r_n-k)h}{r_n(n-r_n)}.
\end{aligned}
\]
Transitions reaching \(B\) are killed. The initial probability of a particular admissible \(J\) is exactly
\[
\nu(J)=\frac{\binom{n-u}{r_n-|J|}}{\binom n{r_n}},
\]
using zero for infeasible binomial coefficients. In particular \(\nu(\varnothing)=1+O_{s,d}(r_n/n)\). For sufficiently large \(n\), all \(2^u\) subsets are feasible before killing.

**2. Spectral isolation, uniformly in growing block size.** Let \(Q_0\) be the pure-death transition matrix on the admissible subsets: each currently tracked label is removed with probability \(1/r_n\), and there are no insertions into \(U\). The formula above gives
\[
\|Q-Q_0\|\le\frac{C_{s,d}}{n-r_n}.
\]
The functions \(f_A(J)={\mathbf{1}}\{A\subseteq J\}\), indexed by admissible \(A\), form a basis on the downward-closed admissible state family and obey \(Q_0f_A=(1-|A|/r_n)f_A\). The change-of-basis matrix and its inverse are uniformly bounded because \(u\le ds\) is fixed. Thus the eigenvalue \(1\), associated with \(A=\varnothing\), is simple and separated by \(1/r_n\) from the other eigenvalues. Since \(r_n/n\to0\), elementary finite-matrix resolvent perturbation yields one simple Perron eigenvalue \(\rho\) near \(1\), its rank-one projector \(P\) satisfies \(\|P-P_0\|=O_{s,d}(r_n/n)\), and a circular resolvent contour of radius \(1-1/(2r_n)\) gives, for integer \(t\ge0\),
\[
Q^t=\rho^tP+R_t,\qquad
\|R_t\|\le C_{s,d}r_n\bigl(1-\tfrac1{2r_n}\bigr)^t.
\]
Here \(P_0\) is the projection onto the empty state of the pure-death chain. Since the initial law is concentrated at the empty state up to \(O_{s,d}(r_n/n)\),
\[
\Pr\{S_1,\ldots,S_d\hbox{ all unseen through time }t\}
=(1+O_{s,d}(r_n/n))\rho^t+O_{s,d}\bigl(r_ne^{-t/(2r_n)}\bigr).
\tag{1}
\]

**3. Uniform evaluation of the rare killing eigenvalue.** Write \(r=r_n\) here. In the *un-killed* projected chain, a stationary transition into \(B\) from outside \(B\) has flux \(\vartheta\). For one fixed target \(S\), reversibility gives the exact entrance flux
\[
\Pr_\pi\{S\nsubseteq H_t,\ S\subseteq H_{t+1}\}
=\frac{s}{r}\frac{(r)_s}{(n)_s}
=\frac{\binom{r-1}{s-1}}{\binom ns}=\frac{\beta_n}{M_n}.
\]
For distinct targets, a discrepancy between the sum of individual fluxes and the flux into their union requires two targets to be contained in the arriving state. Two distinct \(s\)-subsets have union size at least \(s+1\). By bounding their joint stationary probability by \(O_{s,d}((r/n)^{s+1})\), and the relevant reverse deletion probability by \(O_{s,d}(1/r)\), inclusion-exclusion gives the *uniform* bound
\[
\vartheta=d\frac{\beta_n}{M_n}\bigl(1+O_{s,d}(r/n)\bigr).
\tag{2}
\]

Regenerate the un-killed chain at \(J=\varnothing\). Let \(\tau\) be its first positive return time and let \(q\) be the probability of entering \(B\) before that return. The empty-state stationary probability is \(1+O_{s,d}(r/n)\), hence Kac's identity yields
\[
\mathbb E_\varnothing\tau=1+O_{s,d}(r/n).
\]
On departure from the empty state the chain has only one tracked element. From *any* nonempty tracked state, the expected time until emptiness is \(O_{s,d}(r)\), and its second moment is \(O_{s,d}(r^2)\): in a fixed multiple of \(r\) steps, all at most \(u\) present labels can be deleted with a probability bounded below, while a new tracked-label insertion has probability at most \(u/(n-r)=o(1/r)\) per step. Repeating this block argument proves a geometric tail on the \(r\)-step scale. An excursion departing from emptiness therefore produces an expected \(O_{s,d}(r/n)\) *new* tracked-label insertions before return. After the first entry to \(B\), any further entrance from outside \(B\) requires such a new insertion. Hence the expected number of entries to \(B\) per return cycle is \(q(1+O_{s,d}(r/n))\). The stationary renewal-reward identity, combined with (2), gives
\[
q=d\frac{\beta_n}{M_n}\bigl(1+O_{s,d}(r/n)\bigr).
\tag{3}
\]
The chance of departing from emptiness in one step is \(u/(n-r)\); the return-time geometric bound then implies \(\mathbb E\tau^2=1+O_{s,d}(r^2/n)\).

Let \(F(z)=\mathbb E_\varnothing[z^\tau;\,B\text{ is avoided before the return}]\). Then \(F(1)=1-q\) and \(F'(1)=1+O_{s,d}(r/n)\): deleting cycles that encounter \(B\) changes the derivative by at most \(\mathbb E[\tau;\tau>1]=O_{s,d}(r/n)\). The first-return renewal equation for survival from emptiness shows that \(F(1/\rho)=1\). Its Taylor expansion is legitimate on a neighborhood of radius \(c_{s,d}/r\), thanks to the geometric return-time tail. Since \(q r=O_{s,d}((r/n)^s)=o(1)\) and \(q\mathbb E\tau^2=O_{s,d}(r/n)\), expansion at \(1\) and (3) give
\[
1-\rho=d\frac{\beta_n}{M_n}\bigl(1+O_{s,d}(r/n)\bigr).
\tag{4}
\]

**4. Poisson and Gumbel limits.** Put \(t=\lfloor a_n(\log M_n+x)\rfloor\). Equations (1) and (4), together with \((r_n/n)\log M_n\to0\), imply uniformly over all distinct target families of any fixed size \(d\),
\[
\Pr\{S_1,\ldots,S_d\hbox{ all unseen through }t\}
=M_n^{-d}e^{-dx}(1+o(1)).
\tag{5}
\]
Indeed \(t/r_n\asymp(n/r_n)^s\log M_n\), making the residual term in (1) negligible even after multiplication by \(M_n^d\). Summing (5) over the \((M_n)_d\) ordered distinct target families gives \(\mathbb E[(N_n(x))_d]\to e^{-dx}\) for every fixed \(d\). These are the factorial moments of \(\operatorname{Poisson}(e^{-x})\), proving the first claim; the event \(T_n\le t\) is exactly \(N_n(x)=0\), proving the Gumbel claim.

**5. Mean cover time.** The Gumbel limit makes \(T_n/(a_n\log M_n)\to1\) in probability, giving the lower expectation bound. For the upper bound, specialize (1) and (4) to \(d=1\) and apply the union bound over the \(M_n\) possible missing targets. For any fixed \(\varepsilon>0\), start summing the resulting geometric tails after \(t_0=\lceil(1+\varepsilon)a_n\log M_n\rceil\); their combined expectation is \(o(a_n\log M_n)\), while the sum of the preceding tail probabilities is at most \(t_0\). Taking \(\varepsilon\downarrow0\) gives \(\mathbb ET_n\sim a_n\log M_n\). The final elementary asymptotic follows from \(s\) fixed and \(r_n\to\infty\). \(\square\)

## Verification

The self-contained `verify.py` script uses exact rational arithmetic and two independently constructed finite-state chains: the full walk on all \(r\)-subsets and its projected, killed chain on the union of marked targets. It verifies their survival probabilities and projected distributions at eight consecutive times, as well as the exact stationary single-target entrance flux. On execution it reports **396 exact-rational comparisons across 22 small-volume target families**. These finite checks validate the formulas used above; they do not replace the uniform spectral, regenerative, or asymptotic arguments. Run with `python3 verify.py` using the standard library.

## Relationship to prior work

Athreya, Mukherjee and Mukherjee introduced the super-coupon problem and proposed the Markovian single-replacement cover-time scale in their 2023 preprint; the open-access journal version retains this as Conjecture 2.4 and proves the special state-cover case in Theorem 2.5. Its independent-draw Gumbel theorem addresses a different, temporally independent process. An earlier mathematical result establishes the Markovian Gumbel law for **fixed** \(r\) and fixed \(s\), but does not assert uniformity for any diverging block size. The present theorem proves a distinct triangular-array regime \(r_n\to\infty\), where one cannot substitute growing parameters into a fixed-parameter limit. In particular, it quantifies the range of block-size growth for which both the precise limiting distribution and first-order mean continue to hold.

## Limitations

This proof requires the stationary start, fixed target order \(s\ge2\), single-element replacement, and \(r_n\log n=o(n)\). It does not address growing target order, nonstationary or adversarial starting states, blocks of positive limiting density, or the sharp boundary of the sufficient sparsity condition. The \(O_{s,d}\) errors are uniform for each *fixed* factorial-moment order \(d\), not for orders diverging with \(n\).

## References

1. S. Athreya, S. Mukherjee and S. S. Mukherjee, *On a generalisation of the coupon collector problem*, arXiv:2304.01145 (first posted 2023-04-03), https://arxiv.org/abs/2304.01145.
2. S. Athreya, S. Mukherjee and S. S. Mukherjee, *On a Generalisation of the Coupon Collector Problem*, Journal of Theoretical Probability 38, Article 54 (2025), https://doi.org/10.1007/s10959-025-01417-w (open-access full text, including Theorems 2.3 and 2.5 and Conjecture 2.4).

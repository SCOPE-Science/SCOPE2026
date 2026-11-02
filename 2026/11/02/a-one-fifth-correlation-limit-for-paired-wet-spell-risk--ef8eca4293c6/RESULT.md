# A one-fifth correlation limit for paired-wet-spell risk

## Finding

A finite daily-rainfall occurrence model can show an interior maximum of the risk of observing two consecutive wet days even if the fraction of wet days is held exactly fixed. Consider a binary, stationary, first-order Markov chain \(X_1,X_2,\ldots\), with \(X_t=1\) meaning a wet day, with \(\Pr(X_t=1)=1/2\) and a common same-state transition probability \(q\in[0,1]\). For each integer \(n\ge2\), define the paired-wet-spell indicator probability
\[
P_n(q)=\Pr\{X_t=X_{t+1}=1\text{ for at least one }1\le t<n\}.
\]
The following hold.

1. For four days, \(P_4(q)=3q/2-q^2\), and its **unique** global maximum on \([0,1]\) is \(9/16\) at \(q=3/4\). At \(q=1/2\) and \(q=1\) it is only \(1/2\); at \(q=0\) it is zero.
2. Every integer horizon \(n\ge4\) has at least one global maximizing persistence \(q_n\) in the open interval \((0,1)\).
3. There is an integer \(N_0\) such that for every \(n\ge N_0\) the maximizing persistence is unique and obeys
\[
q_n=\frac35+\frac{4}{15n}+O(n^{-2}),\qquad n\to\infty.
\]
The optimized probability of **no** paired-wet spell is
\[
1-P_n(q_n)=\frac98\left(\frac45\right)^n\bigl(1+O(n^{-1})\bigr).
\]
4. The exponential avoidance rate is optimized uniquely at \(q=3/5\): writing \(F_n(q)=1-P_n(q)\),
\[
\lim_{n\to\infty}F_n(q)^{1/n}=\lambda(q)
=\frac{q+\sqrt{q^2+4(1-q)^2}}2\ge\frac45,
\]
with equality **only** for \(q=3/5\). Thus the limiting maximizing lag-one correlation, \(2q_n-1\), is \(1/5\). The sequence of finite-horizon maxima need not be claimed unique for all \(n\ge5\); the theorem establishes uniqueness for \(n=4\) and all sufficiently large horizons.

## Assumptions and scope

The transition matrix in dry/wet order is
\[
T(q)=\begin{pmatrix}q&1-q\\1-q&q\end{pmatrix},
\qquad \Pr(X_1=0)=\Pr(X_1=1)=\frac12.
\]
Its stationary marginal is \(1/2\) for every \(q\in[0,1]\), including the alternating and frozen endpoint chains under the specified initial law. The parameter \(q\) is **persistence**, not wet-day probability. The lag-one correlation is \(2q-1\). The event is the occurrence of at least one pair of adjacent wet days within an \(n\)-day observation window, not the frequency of such pairs and not a claim that this event necessarily causes a flood.

All asymptotics concern integers \(n\to\infty\), with this fixed family of stationary binary Markov laws. The asymptotic optimizer refers to global maxima over the complete closed parameter interval \([0,1]\), not a fixed subinterval.

## Proof

**Avoidance matrix and recurrence.** Killing a path on the first wet-to-wet transition leaves the substochastic matrix
\[
M(q)=\begin{pmatrix}q&1-q\\1-q&0\end{pmatrix}.
\]
For \(\pi=(1/2,1/2)\) and \({\bf1}=(1,1)^{\mathsf T}\), the exact probability of avoiding a wet-wet pair is
\[
F_n(q)=\pi M(q)^{n-1}{\bf1}.
\]
This statement includes both endpoints, because the first day has the stipulated marginal law. Cayley--Hamilton gives
\[
M(q)^2=qM(q)+(1-q)^2I,
\quad F_1(q)=1,\quad F_2(q)=1-q/2,
\]
and therefore
\[
F_n(q)=qF_{n-1}(q)+(1-q)^2F_{n-2}(q)\quad(n\ge3).
\]
Direct substitution yields \(F_4(q)=1-3q/2+q^2\), proving the four-day formula and its unique optimizer.

**Interior finite-horizon extrema.** At \(q=0\) the days strictly alternate so \(F_n(0)=1\). At \(q=1\) the chain is frozen and \(F_n(1)=1/2\) for \(n\ge2\). At \(q_0=3/5\), the roots of the avoidance-matrix characteristic equation are \(4/5\) and \(-1/5\); solving from \(F_1=1\) and \(F_2=7/10\) gives
\[
F_n(q_0)=\frac9{10}\left(\frac45\right)^{n-1}
+\frac1{10}\left(-\frac15\right)^{n-1}.
\]
In particular \(F_4(q_0)=23/50<1/2\). Avoidance of a run over \(n\) days implies avoidance over the first four days; hence \(F_n(q_0)\le23/50\) for every \(n\ge4\). Continuity and the strict comparisons to both endpoint values give an interior global minimizer of \(F_n\), equivalently a maximizer of \(P_n\).

**The sharp asymptotic rate.** The eigenvalues of \(M(q)\) are
\[
\lambda_\pm(q)=\frac{q\pm\sqrt{q^2+4(1-q)^2}}2.
\]
For any \(q\in[0,1]\), its positive Perron eigenvalue \(\lambda=\lambda_+\) is the unique positive root of \(f_q(z)=z^2-qz-(1-q)^2\). The exact identity
\[
f_q(4/5)=-\left(q-3/5\right)^2
\]
proves \(\lambda(q)\ge4/5\) with equality only at \(q=3/5\). For fixed interior \(q\), the positive eigenvector gives \(F_n(q)^{1/n}\to\lambda(q)\). The same limit holds at \(q=0,1\), where avoidance is respectively \(1\) and \(1/2\) for all \(n\ge2\), with \(\lambda=1\).

To control *moving* optimizing parameters, choose a nonnegative right Perron eigenvector \(v(q)\) normalized by \(\max_i v_i=1\). Since \({\bf1}\ge v\),
\[
F_n(q)\ge\pi M(q)^{n-1}v(q)
=\lambda(q)^{n-1}\pi v(q)
\ge\tfrac12\lambda(q)^{n-1}.
\]
This remains valid at the endpoints with a nonnegative Perron eigenvector. Conversely \(F_n(q_0)\le(4/5)^{n-1}\). Outside every fixed neighborhood of \(q_0\), continuity and the strict uniqueness of the minimum of \(\lambda\) give \(\lambda\ge4/5+\varepsilon\) for some \(\varepsilon>0\). The displayed exponential bounds force **every** global minimizer of \(F_n\) to converge to \(q_0\).

**Eventual uniqueness and first finite-window correction.** On a sufficiently small closed neighborhood \(U\subset(0,1)\) of \(q_0\), put \(\lambda=\lambda_+\), \(\mu=\lambda_-\), and
\[
A(q)=\frac{1-q/2-\mu(q)}{\lambda(q)-\mu(q)}.
\]
The recurrence yields the exact decomposition
\[
F_n(q)=A(q)\lambda(q)^{n-1}+(1-A(q))\mu(q)^{n-1}.
\]
On \(U\), \(A>0\), \(|\mu/\lambda|<c<1\), and all functions are analytic. Differentiating this expression up to second order gives, uniformly on \(U\),
\[
\log F_n(q)=(n-1)\log\lambda(q)+\log A(q)+O(c^n),
\]
where the error and its first two derivatives are \(O(n^2c^n)\). At \(q_0\), implicit differentiation of \(\lambda^2-q\lambda-(1-q)^2=0\) gives \(\lambda'=0\) and \(\lambda''=2\). Also \(\lambda=4/5\), \(\mu=-1/5\), \(A=9/10\), and direct differentiation gives \(A'=-3/5\). Thus
\[
(\log\lambda)''(q_0)=\frac52,
\qquad (\log A)'(q_0)=-\frac23.
\]
Shrink \(U\) so that \((\log\lambda)''\) remains strictly positive. For all sufficiently large \(n\), \((\log F_n)''>0\) throughout \(U\). As every global minimizer eventually lies in the interior of \(U\), strict convexity makes it unique, and its derivative vanishes. Taylor expansion of the preceding first derivative at \(q_0\) gives first \(q_n-q_0=O(n^{-1})\), then
\[
0=(n-1)\frac52(q_n-q_0)-\frac23+O(n^{-1}),
\]
which gives \(q_n=3/5+4/(15n)+O(n^{-2})\). Substituting this into the eigenvalue decomposition proves
\[
F_n(q_n)=\tfrac9{10}(4/5)^{n-1}(1+O(n^{-1}))
=\tfrac98(4/5)^n(1+O(n^{-1})).
\]
All claims follow.

## Verification

Run `python3 verify.py` using Python 3 and the standard library. The checker constructs the survival polynomials symbolically with exact rational coefficients; compares the recursion and the killed-chain calculation against direct enumeration for up to thirteen days and eight exact persistence values; verifies the four- and five-day polynomials, the explicit \(q=3/5\) eigenvalue formula, and the factorization of the characteristic polynomial. It also numerically checks stationary-point behavior and convergence of the scaled finite-window displacement at longer horizons. Exact enumeration cannot prove any all-horizon statement, and approximate root checks do not establish uniqueness; those statements rely on the analytic proof above.

## Relationship to prior work

Binary daily-rainfall Markov models were used by Weiss (1964) and Chin (1977). General Markov-dependent run probabilities and waiting-time distributions were studied by Schwager (1982/1983), Wang and Ji (1995), and Oh, Park and Kim (2022). In particular, the complete 2022 preprint gives eigenvalue/recurrence formulas for run waiting times with *arbitrary* two-state transition parameters. Those known formulas are acknowledged as containing the same spectral roots after specialization; neither the recurrence nor the \(2\times2\) eigenvalue formula is claimed here as original. The assessed result is the **constrained global extremization** at fixed wet-day marginal, including the sharp \(3/5\) long-window optimizer, the nontrivial positive \(4/(15n)\) finite-window drift, and the finite-horizon interior optimum. The Cornell technical report and historical 1993 Wang--Liang article were not substantively available for comparison; these create a real priority risk, especially if they optimize transition persistence rather than merely give the full run distribution.

## Limitations

The wet-day marginal is fixed at one half, self-transition probabilities are symmetric, and the chain has only one-step memory. Real daily precipitation may have seasonal or higher-order dependence, unequal wet/dry durations, and varying rainfall intensity. A two-day wet run is an occurrence index and is not automatically an extreme-rainfall or flood event. The result makes no empirical hazard prediction and no claim about optimal causal control of weather. The eventual-uniqueness theorem does not assert a numerical value for the smallest admissible \(N_0\), and uniqueness for each intermediate finite horizon is not proved. Earlier equivalent optimized-run results may exist.

## References

- L. L. Weiss, “Sequences of Wet or Dry Days Described by a Markov Chain Probability Model,” *Monthly Weather Review* **92** (1964), 169–176. https://doi.org/10.1175/1520-0493(1964)092%3C0169:SOWODD%3E2.3.CO;2 . Public date: 1964-04-01, as displayed by the journal.
- E. H. Chin, “Modeling Daily Precipitation Occurrence Process with Markov Chain,” *Water Resources Research* **13** (1977), 949–956. https://doi.org/10.1029/WR013i006p00949 .
- S. J. Schwager, “Run Probabilities in Sequences of Markov-Dependent Trials,” Cornell Biometrics Unit Technical Report BU-765-M, revised (1982); *J. Amer. Statist. Assoc.* **78** (1983), 168–175. https://hdl.handle.net/1813/32867 .
- Y. H. Wang and S. Ji, “Limit Theorems for the Number of Occurrences of Consecutive k Successes in n Markovian Trials,” *J. Appl. Probab.* **32** (1995), 727–735. https://doi.org/10.2307/3215125 .
- J. Oh, C. Park and S. Kim, “Recurrence Algorithms of Waiting Time for the Success Run of Length k in Relation to Generalized Fibonacci Sequences,” arXiv:2210.08797 (2022), especially Sections 2.2–2.3 and Theorem 2.14. https://arxiv.org/pdf/2210.08797 .

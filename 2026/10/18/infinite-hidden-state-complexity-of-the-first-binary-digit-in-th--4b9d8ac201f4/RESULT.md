# Infinite hidden-state complexity of the first binary digit in the Pelikan random map

## Finding

For every parameter \(1/2<p<1\), the stationary first-binary-digit process of the Pelikan expanding/contracting random interval map has **full binary symbolic support, but no representation as the output of any time-homogeneous hidden Markov chain with finitely many states**. In particular it is not a Markov process of any finite order, although its dyadic-shell extension is a countable-state Markov chain and the return times of the digit \(1\) are independent and identically distributed.

The obstruction is exact: the positive return-time probability-generating function is algebraic of degree two and is never rational. Its coefficients additionally exhibit a sharp three-regime asymptotic at \(p=4/5\), where the square-root singularity and the reset-depth pole coincide. This last threshold is already visible in the spectral analysis of a different (position-correlation) observable in Monthus's work; the claim of new mathematical information is the **finite-state impossibility for the stationary binary observation** and the explicit first-return coefficient asymptotics, not discovery of the underlying countable-shell transition kernel or its spectral threshold.

## Assumptions and scope

Let \(p\in(1/2,1)\), let \(q=1-p\), and independently at each nonnegative integer time choose the map \(x\mapsto2x\pmod1\) with probability \(p\) or the map \(x\mapsto x/2\) with probability \(q\) on \([0,1)\). Initialize \(X_0\) with the absolutely continuous invariant probability \(\mu_p\), whose existence and piecewise-flat dyadic density are known [1,2]. Probabilities here average over both the stationary initial state and the independent random map choices; no pathwise or quenched assertion is made.

Write \(J_t=j\) if \(2^{-(j+1)}\le X_t<2^{-j}\), for \(j\ge0\), and let the observable \(A_t=\mathbf1_{\{J_t=0\}}\), namely the first binary digit of \(X_t\), equal to \(1\) exactly on \([1/2,1)\). Condition on \(A_0=1\), define \(\tau=\inf\{n\ge1:A_n=1\}\), and set \(f_n=\Pr(\tau=n\mid A_0=1)\).

Define the unique formal power series \(t(z)\) with zero constant term satisfying
\[
 t(z)=z\bigl(p+qt(z)^2\bigr)
 \quad\text{and}\quad
 t(z)=\frac{1-\sqrt{1-4pqz^2}}{2qz}.
\]
Then the exact return generating function is
\[
\boxed{R_p(z)=\sum_{n\ge1}f_nz^n=z\left(qt(z)+\frac{p}{2-t(z)}\right).}
\]
Its analytic germ is **not rational** over \(\mathbb R(z)\) for every \(1/2<p<1\). Therefore the infinite Hankel matrix \((f_{i+j+1})_{i,j\ge0}\) has infinite rank, and the stationary binary process cannot have a finite-state hidden Markov representation. Its stationary one-frequency is \(\Pr(A_t=1)=(2p-1)/(2p)\).

For completeness, the exact renewal-gap asymptotics take three forms. Set \(\ell_p=2\sqrt{pq}\) and, when \(1/2<p<4/5\), put \(r_p=\sqrt{p/q}\) and
\[
 C_\pm(p)=\frac{q+p/(2\mp r_p)^2}{2q\sqrt{2\pi}}.
\]
With \(n\to\infty\) through positive integers:
\[
\boxed{f_n=\ell_p^n n^{-3/2}\bigl(C_+(p)+(-1)^nC_-(p)+o(1)\bigr),\qquad 1/2<p<4/5;}
\]
\[
\boxed{f_n\sim\frac{(4/5)^n}{2\sqrt{2\pi n}},\qquad p=4/5;}
\]
\[
\boxed{f_n\sim\frac{p(5p-4)}{(4-3p)^2}\left(\frac{4-3p}{2}\right)^n,\qquad 4/5<p<1.}
\]
The asymptotics are pointwise in fixed \(p\), not uniform across the transition. The binary support contains every finite word; the associated **measure**, unlike the support, requires infinitely many hidden states.

## Proof

**1. The observed dyadic-shell chain is Markov.** Known invariant densities for this model are constant on each half-open dyadic shell [1,2]. Conditional on a fixed shell, \(X_0\) is therefore uniform on that shell. This uniformity persists conditional on any finite past shell history: the two maps are affine, and each origin-shell/destination-shell transition maps a uniform interval onto either another entire shell or, from shell zero under doubling, onto an entire subinterval of \([0,1)\). Conditioning on the destination shell preserves uniformity. By induction, the shell labels \(J_t\) have the time-homogeneous transition probabilities
\[
 \Pr(J_{t+1}=j-1\mid J_t=j)=p,\quad
 \Pr(J_{t+1}=j+1\mid J_t=j)=q \qquad(j\ge1),
\]
and from \(j=0\), \(\Pr(J_{t+1}=k\mid J_t=0)=q\mathbf1_{\{k=1\}}+p2^{-k-1}\) for every \(k\ge0\). This kernel was already established in [2]; the conditional-uniformity argument identifies it with the actual stationary **joint** shell process, not merely the evolution of one-time densities.

**2. Regeneration and return transform.** At each occurrence of \(J_t=0\), the future shell chain restarts from the same state by the strong Markov property; successive positive return intervals are independent and identically distributed. From shell \(1\), before visiting \(0\) the process follows a nearest-neighbor walk decreasing its index with probability \(p\) and increasing it with probability \(q\). Its first-hit transform is \(t(z)\), because the first step either hits zero or rises one level and then needs two independent downward hitting stages. Equivalently, first-step conditioning gives \(t=z(p+qt^2)\), with the branch having \(t(0)=0\). From zero, a contraction moves to shell one, while a doubling reset lands at shell \(k\) with probability \(2^{-k-1}\). A return from shell \(k\) has transform \(t^k\), including \(k=0\) for an immediate return. Hence
\[
 R_p(z)=z\left(qt(z)+p\sum_{k\ge0}2^{-k-1}t(z)^k\right)=z\left(qt(z)+\frac p{2-t(z)}\right).
\]
At \(z=1\), \(t(1)=1\) since \(p>q\), so \(R_p(1)=1\). Differentiating the two defining identities yields \(t'(1)=1/(2p-1)\) and \(R_p'(1)=2p/(2p-1)\). The regenerative renewal-frequency formula gives \(\Pr(A_t=1)=[R'_p(1)]^{-1}=(2p-1)/(2p)\), consistently with [2]. Moreover \(f_1=p/2>0\); for \(n\ge2\), a reset into shell \(n-1\), followed by \(n-1\) downward steps, has probability \((p/2)^n>0\). Every finite binary word has positive stationary probability by concatenating such excursions and immediate returns, proving full-shift support.

**3. A nonrationality and finite-state obstruction.** From \(t=z(p+qt^2)\), we have \(z=t/(p+qt^2)\), so as a rational function of \(t\),
\[
 R_p=\frac{t\,[qt(2-t)+p]}{(p+qt^2)(2-t)}.
\]
The quadratic equation for \(t\) over \(\mathbb R(z)\) has discriminant \(1-4pqz^2\), which is not a square of a rational function when \(pq>0\). Its other root is \(t^\dagger=p/(qt)\). Were \(R_p\in\mathbb R(z)\), its rational-in-\(t\) expression would be invariant under the conjugation \(t\mapsto p/(qt)\). This is impossible: the displayed expression tends to \(0\) as \(t\to0\), whereas its conjugate tends to \(1\), since the expression tends to \(1\) as \(t\to\infty\). Consequently \(R_p\) is nonrational (indeed quadratic-algebraic).

For any stationary finite-state hidden Markov process with binary emissions, its joint probability of the word \(10^{n-1}1\), for \(n\ge1\), is a fixed row vector times the \((n-1)\)-st power of a finite matrix times a fixed column vector. Dividing by its positive one-frequency, the first-return coefficients \(f_n\) therefore have a **rational** generating function, by the finite-matrix resolvent \((I-zM)^{-1}\). This contradicts the preceding algebraic nonrationality. In particular, every finite-order Markov binary process would have a finite-state presentation by its finite history blocks, so no such order is possible. Finally, finite Hankel rank of \((f_{i+j+1})\) would force a finite linear recurrence, hence a rational generating function; its rank is therefore infinite.

**4. Sharp first-return tails.** Let \(z_\star=(2\sqrt{pq})^{-1}\) and \(r_p=\sqrt{p/q}\). For \(p<4/5\), the principal branch \(t(z)\) reaches the finite values \(r_p<2\) and \(-r_p\) at \(z=z_\star\) and \(z=-z_\star\), respectively; the denominator \(2-t\) does not vanish before or on their singularity circle. At both points the quadratic square root has a square-root singularity. Explicitly,
\[
 t(z)=r_p-r_p\sqrt{2}\sqrt{1-z/z_\star}+O(1-z/z_\star)
\]
near the positive point; near the negative point replace \(z\) by \(-z\) and \(r_p\) by \(-r_p\). The standard coefficient transfer of \((1-w)^{1/2}\), namely \(-w^n/(2\sqrt\pi n^{3/2})\) after rescaling, yields precisely the two parity-dependent constants \(C_+(p)\) and \(C_-(p)\) shown above. The support of the odd and even terms excludes cancellation of their leading coefficients. Analyticity in slit neighborhoods and the positivity of the odd Taylor coefficients of \(t\) exclude additional competing singularities.

When \(p>4/5\), the principal branch instead reaches \(t=2\) first, at the simple pole \(z_0=2/(4-3p)<z_\star\). Implicit differentiation gives \(t'(z_0)=(4-3p)^2/(5p-4)\), so the pole coefficient is \(p(5p-4)/(4-3p)^2\), yielding the stated pure geometric tail. At \(p=4/5\) the pole collides with the positive square-root branch point \(z_\star=5/4\), and \(R_p(z)\sim (2\sqrt2)^{-1}(1-z/z_\star)^{-1/2}\). Its binomial coefficients yield the middle asymptotic. The ordinary negative branch point gives a lower-order correction there. Each argument treats fixed \(p\), and no finite enumeration is used to deduce these asymptotics.

## Verification

Run \(`python verify.py`\) in the package directory. The standalone standard-library checker compares the algebraic generating-function coefficients with an independently implemented absorbing-shell-chain calculation using exact rational arithmetic for six rational values of \(p\), through return time \(25\). It also verifies positivity of those coefficients and performs six **finite numerical diagnostics** of the three asymptotic regimes at lengths \(200\) and \(400\). All \(318\) checks pass. The infinite-state and infinite-time statements are established by the preceding analytic arguments; no finite computation proves an infinite-rank or singularity assertion.

## Relationship to prior work

Pelikan's map and invariant-density mechanism are classical [3]. Yan and collaborators [1] analyze the stationary density and position autocorrelation for this very map. Monthus [2] explicitly gives the countable-shell Markov kernel, its general finite-time resolvent (especially Section IV, equation (52)), first-passage transforms, and a spectral transition at \(p=4/5\) for **position** correlations. Those known results already encompass the basic shell transition probabilities and implicitly encode first-return distributions. The new claim is not that this transition kernel, its resolvent, or the \(4/5\) spectral edge were previously unknown: it is that the **first-digit stationary output cannot be realized by any finite-state hidden Markov model for any \(1/2<p<1\)**, notwithstanding its full binary support, with a transparent algebraic-return obstruction and explicit waiting-time prefactors. The distinction between random-position correlations, dyadic-depth excursion maxima and the stochastic-process representation of an observed single binary digit is essential to this comparison.

## Limitations

The result is annealed and stationary. It assumes a piecewise-uniform dyadic-shell conditional law; it does not assert this representation under arbitrary fixed deterministic seeds, nonstationary initial densities, or finite-precision implementations. No nondegenerate stationary absolutely continuous initial law is asserted at \(p=1/2\), and the endpoint \(p=1\) is excluded: there the pure doubling map yields independent fair binary digits and a finite-state model. The transition-time asymptotics are not uniform when \(p\to4/5\). Existing full propagator formulas in [2] could permit alternative equivalent derivations of the waiting-time results, and independently checking priority for the finite-state representation obstruction remains worthwhile.

## References

[1] J. Yan, M. Majumdar, S. Ruffo, Y. Sato, C. Beck, and R. Klages, *Transition to anomalous dynamics in a simple random map*, arXiv:2308.09269, publicly posted 2023-08-18. https://arxiv.org/abs/2308.09269

[2] C. Monthus, *Explicit dynamical properties of the Pelikan random map in the chaotic region and at the intermittent critical point towards the non-chaotic region*, arXiv:2409.19999, publicly posted 2024-09-30. https://arxiv.org/abs/2409.19999

[3] S. Pelikan, *Invariant densities for random maps of the interval*, Transactions of the American Mathematical Society 281 (1984), 813–825. DOI: 10.1090/S0002-9947-1984-0722776-1.

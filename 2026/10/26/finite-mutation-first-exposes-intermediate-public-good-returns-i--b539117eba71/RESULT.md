# Finite mutation first exposes intermediate public-good returns in a four-person population

## Finding
For four individuals playing a three-person public-goods game with multiplication factors \(u=r(1)\), \(v=r(2)\), and \(w=r(3)\), a positive mutation probability makes the interior returns affect the weak-selection abundance even though the rare-mutation limit depends only on \(w\). Precisely, for every fixed \(0<\mu<1\), contribution cost \(c>0\), and fixed real return values, the stationary cooperator proportion is
\[
 f_C(\delta)=\frac12+\frac{c(1-\mu)\bigl[(w-9)+\mu(2v+2w-u-27)\bigr]}{12(1+3\mu)(1+11\mu)}\,\delta+O(\delta^2),\quad\delta\downarrow0.
\]
This is the smallest admissible interaction size at which intermediate returns can influence the first weak-selection coefficient: with two-person interaction groups, the coefficient is independent of \(r(1)\) for every population size \(N\ge3\) and every fixed \(0<\mu<1\).

A sign reversal occurs **within nondecreasing returns**. At \(c=1\), \(\mu=1/2\), \(u=2\), and \(w=9\), choosing \(v=2\) gives \(f_C'(0)=-7/780\), whereas choosing \(v=8\) gives \(f_C'(0)=5/780\). Both profiles have the same full-cooperation return and the same cost. For every sufficiently small positive selection strength the first favors defection and the second favors cooperation. In both cases the rare-mutation coefficient vanishes.

## Assumptions and scope
A well-mixed population has fixed size \(N\), and each individual is a cooperator \(C\) or defector \(D\). The interacting group size is \(n\), where \(2\le n<N\). In an interaction containing \(j\) cooperators, a cooperator receives \(cj\,r(j)/n-c\) and a defector receives \(cj\,r(j)/n\). Expected payoffs \(P_C(k),P_D(k)\) in a population of \(k\) cooperators are evaluated by sampling the other \(n-1\) participants without replacement.

At every discrete update, a uniformly selected focal individual flips strategy with probability \(\mu\). Otherwise the focal selects a distinct, uniformly random model individual and imitates that model with probability \(F(\delta(P_{\rm model}-P_{\rm focal}))\), where \(F(z)=1/(1+e^{-z})\). The parameter \(\mu\) is fixed and strictly between zero and one when differentiating in selection strength \(\delta\ge0\). This explicit distinct-model convention resolves an implementation choice for finite mutation; no claim is made for different sampling conventions. The resulting finite Markov chain is irreducible, with unique stationary law \(\pi_\delta\), and \(f_C(\delta)=\sum_{k=0}^N k\pi_\delta(k)/N\).

## Proof
Put \(\Delta_k=P_C(k)-P_D(k)\). Conditional on \(k\) cooperators, the exact birth and death probabilities are
\[
 T_k^+=\frac{N-k}{N}\left[\mu+(1-\mu)\frac{k}{N-1}F(\delta\Delta_k)\right],\qquad
 T_k^-=\frac{k}{N}\left[\mu+(1-\mu)\frac{N-k}{N-1}F(-\delta\Delta_k)\right].
\]
The probability of remaining at the same count is the complement. These transition probabilities are positive on the respective adjacent edges. Their difference is
\[
 T_k^+-T_k^-=\frac{\mu(N-2k)}{N}+\frac{(1-\mu)k(N-k)}{N(N-1)}\tanh\left(\frac{\delta\Delta_k}{2}\right).
\]
At neutral selection the chain is invariant under \(k\mapsto N-k\), hence \(f_C(0)=1/2\). Stationarity of the mean and differentiation at zero give the exact first-order drift identity
\[
 f_C'(0)=\frac{1-\mu}{4\mu N(N-1)}\sum_{k=1}^{N-1}\pi_0(k)k(N-k)\Delta_k.
\]
The differentiation is valid because each adjacent transition probability is analytic in \(\delta\) and remains positive at zero, so stationary probabilities are analytic by their detailed-balance products.

For \(N=4\) and \(n=3\), direct sampling without replacement gives
\[
 \Delta_1=\frac{c(u-9)}9,\qquad
 \Delta_2=\frac{c(-u+2v-9)}9,\qquad
 \Delta_3=\frac{c(-2v+3w-9)}9.
\]
At neutrality the birth rates are \(T_k^+=(4-k)[\mu+(1-\mu)k/6]/4\), and similarly \(T_k^-=k[\mu+(1-\mu)(4-k)/6]/4\). Detailed balance yields, writing \(D=(1+3\mu)(1+11\mu)\),
\[
 \pi_0(0)=\pi_0(4)=\frac{(1+\mu)(1+2\mu)}{2D},\qquad
 \pi_0(1)=\pi_0(3)=\frac{4\mu(1+2\mu)}D,\qquad
 \pi_0(2)=\frac{3\mu(1+5\mu)}D.
\]
These five nonnegative values sum to one, and substitution into the drift identity simplifies to the formula in the finding. At \(\mu=1/2\), \(u=2\), and \(w=9\), its coefficient is \((2v-11)/780\), giving the two displayed signs. Analyticity turns these strict derivatives into the claimed inequalities for all sufficiently small positive \(\delta\). Taking \(\mu\downarrow0\) **after** calculating the derivative gives \(c(w-9)/12\), matching the low-mutation result; the big-O remainder is not asserted uniform in \(\mu\).

For the sharp lower boundary, take group size \(n=2\) in any population \(N\ge3\). A direct two-person payoff calculation gives
\[
 \Delta_k=c\left[\frac{(k-1)r(2)+(N-2k)r(1)/2}{N-1}-1\right].
\]
For every \(0<\mu<1\), neutral symmetry implies \(\pi_0(k)=\pi_0(N-k)\); the weights \(\pi_0(k)k(N-k)\) are likewise symmetric, whereas the coefficient \(N-2k\) of \(r(1)\) is antisymmetric. Its total contribution to the drift identity is therefore zero. Because an interacting group must be smaller than the population, the smallest admissible three-person game has \(N=4\), and the coefficient of \(v\) there is \(c\mu(1-\mu)/[6(1+3\mu)(1+11\mu)]>0\). This proves minimality and genuine interior-return sensitivity.

## Verification
The accompanying `check.py` computes hypergeometric payoffs from the definitions, independently differentiates the birth-death detailed-balance products, and compares the resulting stationary derivative with both the closed formula and the stationary-drift identity using exact rational arithmetic. It checks \(302\) parameter instances, including all \(64\) triples of four return values at each of three positive mutation rates and group-size-two invariance over nine population sizes. It also evaluates the original nonlinear Fermi transition probabilities at small nonzero selection and verifies the two opposite signs. Run `python check.py` in the directory containing this file.

## Relationship to prior work
Wang, Liu, Chen and Szolnoki (2026), Section 2.2, Proposition 2.1 and Appendix B, analyze the low-mutation two-state chain and obtain dependence only on \(r(n)\). The present finite-positive-mutation stationary law is not the same limit: its first-order coefficient depends on intermediate return levels as soon as three-person groups are allowed. The \(\mu\to0\) boundary reproduces their formula without claiming the boundary law as new.

Gokhale and Traulsen (2011) establish general abundance conditions for multiplayer games with recurrent mutation by coalescence methods. Their three-player formulas invoke a large-population and weak-selection approximation; they do not themselves provide the finite-four-person distinct-model Fermi-flip formula or the two-person sharpness/reversal. Kroumi and Lessard (2022) study recurrent mutation in a **Moran birth-death** game with random payoffs, rather than this imitation-flip process. Wu, Gokhale, Wang and Traulsen (2012), Section 2 and equations (6)–(9), provide the general exact detailed-balance stationary formula for a two-strategy Fermi birth–death chain and study the accuracy of rare-mutation approximations. Their treatment uses two-person payoffs and a different model-sampling convention, and does not give the stated return-specific first interaction-size boundary or sign reversal. Detailed balance itself is prior mathematical knowledge, not claimed as new. The claimed contribution is the exact finite-process special-case classification and sharp smallest-interaction boundary, not the general observation that positive mutation can affect abundance.

## Limitations
Only a finite, well-mixed, two-strategy, one-shot public-goods process with symmetric **strategy-flipping** mutations and the specified distinct-model Fermi convention is covered. The expansion is at fixed \(\mu>0\) in weak selection and is not uniform near \(\mu=0\). The two sign examples are asymptotic, not a claim for all selection strengths. Classical general coalescent and mutation-selection theory may contain equivalent results after nontrivial specialization; publication priority is not independently certified.

## References
1. Q. Wang, Y. Liu, X. Chen and A. Szolnoki, “Evolutionary dynamics in public goods games with general frequency-dependent returns” (first public 2026-07-18), arXiv:2607.16809, https://arxiv.org/abs/2607.16809.
2. C. S. Gokhale and A. Traulsen, “Strategy abundance in evolutionary many-player games with multiple strategies” (2011), arXiv:1106.4049, https://arxiv.org/pdf/1106.4049.
3. D. Kroumi and S. Lessard, “Average abundancy of cooperation in multi-player games with random payoffs” (2022), arXiv:2202.11930, https://arxiv.org/abs/2202.11930.
4. B. Wu, C. S. Gokhale, L. Wang and A. Traulsen, “How small are small mutation rates?” Journal of Mathematical Biology 64 (2012), 803–827, doi:10.1007/s00285-011-0430-8.
5. C. S. Gokhale and A. Traulsen, “Evolutionary multiplayer games” (2014), arXiv:1404.1421, https://arxiv.org/html/1404.1421v1.

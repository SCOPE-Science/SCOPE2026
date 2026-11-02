# A sharp Cesàro interval for dyadically held tent-map orbits

## Finding

Let \(T:[0,1]\to[0,1]\) be the full tent map \(T(x)=1-|1-2x|\). Given \(x\in[0,1]\), define a proportionally delayed orbit by \(u_0=x\) and
\[
u_{n+1}=T\bigl(u_{\lfloor n/2\rfloor}\bigr),\qquad n\geq0.
\]
Write \(A_N(x)=N^{-1}\sum_{n=0}^{N-1}u_n\) for \(N\geq1\).

**Theorem.** For every \(x\in[0,1]\) and integer \(N\geq1\),
\[
0\leq A_N(x)\leq\frac45+\frac{x}{5N}.
\]
If the ordinary forward tent-map orbit of \(x\) is dense in \([0,1]\), then the set of subsequential limits of the physical-time averages is exactly
\[
\operatorname{Acc}\bigl(A_N(x)\bigr)=[0,4/5].
\]
In particular, the last conclusion holds for Lebesgue-almost every \(x\in[0,1]\). For almost every such \(x\), the undelayed Cesàro averages \(K^{-1}\sum_{j=0}^{K-1}T^j(x)\) converge to \(1/2\), whereas the delayed averages have *every* value between zero and \(4/5\) as a subsequential limit.

## Assumptions and scope

The orbit is scalar, deterministic and initialized by a single state in the invariant unit interval. The delay is exactly \(\lfloor n/2\rfloor\), with no instantaneous term and no noise. The accumulation statement assumes density of the original forward orbit; it is not asserted for all initial conditions. The finite upper estimate is unconditional. All asymptotics refer to integer physical time \(N\to\infty\), not to the number of underlying tent-map compositions.

## Proof

**1. Exact plateau representation.** Put \(v_j=T^j(x)\). Direct induction in the recurrence gives
\[
u_n=v_{\lfloor\log_2(n+1)\rfloor}.
\]
Indeed the index for \(u_{n+1}\) is one more than the index for \(u_{\lfloor n/2\rfloor}\), and \(1+\lfloor\log_2(1+\lfloor n/2\rfloor)\rfloor=\lfloor\log_2(n+2)\rfloor\). Thus \(v_j\) is repeated exactly \(2^j\) times, for \(2^j-1\leq n\leq2^{j+1}-2\).

**2. A sharp affine calibration.** Introduce \(\Phi(y)=4/5-y/5\). For all \(y\in[0,1]\), a direct calculation on the two affine branches shows
\[
2\Phi(Ty)-\Phi(y)-y=
\begin{cases}
\frac45(1-2y),&0\leq y\leq1/2,\\
0,&1/2\leq y\leq1.
\end{cases}
\]
In particular, \(y+\Phi(y)\leq2\Phi(Ty)\). For \(K\geq1\) let
\[
B_K=\sum_{j=1}^{K}2^{-j}v_{K-j}.
\]
Multiply the calibration by \(2^{-j}\), apply it to \(y=v_{K-j}\), and telescope over \(1\leq j\leq K\). This yields the *exact finite bound*
\[
B_K\leq\Phi(v_K)-2^{-K}\Phi(x).
\]
Write any \(N\geq1\) uniquely as \(N=2^K-1+r\) with \(K\geq1\) and \(0\leq r<2^K\). By the plateau representation,
\[
\sum_{n=0}^{N-1}u_n=2^K B_K+r v_K.
\]
Set \(t=r/2^K\in[0,1)\). The elementary inequality
\[
\Phi(y)+ty\leq\frac45(1+t),\qquad 0\leq y,t\leq1,
\]
follows by checking the endpoints \(y=0,1\) (the left side is affine in \(y\)). Therefore
\[
\sum_{n=0}^{N-1}u_n
\leq\frac45(2^K+r)-\Phi(x)
=\frac45N+\frac{x}{5}.
\]
Nonnegativity follows from \(0\leq u_n\leq1\). This proves the universal estimate.

**3. The upper extreme is attained arbitrarily late.** Define the right-branch inverse \(R(y)=1-y/2\). Let \(z_0=0\) and, for \(j\geq1\),
\[
z_{-j}=R^j(0)=\frac23\bigl(1-(-1/2)^j\bigr).
\]
These points form a legal backward tent-map orbit: \(T(z_{-j})=z_{-(j-1)}\). Its discounted mean is exactly
\[
\sum_{j=1}^{\infty}2^{-j}z_{-j}
=\frac23\left(1-\sum_{j=1}^{\infty}(-1/4)^j\right)
=\frac45.
\]
Fix \(m\geq1\). By continuity of the finitely many iterates \(T^0,\ldots,T^{m-1}\), there is a nonempty open neighborhood of \(z_{-m}\) on which the next \(m\) iterates shadow \(z_{-m},\ldots,z_{-1}\) to arbitrary prescribed accuracy. If \(x\) has a dense forward orbit, its orbit visits this neighborhood at arbitrarily late times: deleting finitely many points from a dense orbit in an interval leaves a dense set. Choose an arbitrarily large \(K\) with \(v_{K-m}\) in this neighborhood. The most recent \(m\) terms of \(B_K\) then approximate \(\sum_{j=1}^{m}2^{-j}z_{-j}\), while all earlier terms lie between zero and \(2^{-m}\). Taking successively finer shadowing and \(m\to\infty\) gives \(\limsup_{K\to\infty}B_K\geq4/5\). The universal bound gives the reverse inequality. At the complete-block times \(N_K=2^K-1\),
\[
A_{N_K}(x)=\frac{2^K}{2^K-1}B_K,
\]
so \(\limsup_{N\to\infty}A_N(x)=4/5\).

**4. The lower extreme is attained arbitrarily late.** Since \(T(0)=0\), continuity implies that, for any \(m\) and any \(\eta>0\), all the first \(m\) iterates of points in some relative open neighborhood of zero lie in \([0,\eta)\). A dense orbit visits that neighborhood at arbitrarily late times. Choosing \(K\) after such a visit, the most recent \(m\) terms in \(B_K\) contribute less than \(\eta\), and all remaining terms contribute at most \(2^{-m}\). Thus \(\liminf_{K\to\infty}B_K=0\), and the complete-block times yield \(\liminf_{N\to\infty}A_N(x)=0\).

**5. All intermediate limits and almost-everywhere assertion.** Since \(u_N\in[0,1]\),
\[
|A_{N+1}-A_N|=\frac{|u_N-A_N|}{N+1}\leq\frac1{N+1}.
\]
A bounded real sequence with successive differences tending to zero has a connected set of subsequential limits: between arbitrarily late visits below and above any intermediate level, it must cross that level with an error bounded by the largest late step. Its limit set is therefore the closed interval between its liminf and limsup, here \([0,4/5]\).

Finally, the two inverse branches of \(T\) each contract by \(1/2\). Their symbolic cylinder intervals have Lebesgue measure \(2^{-m}\), and consecutive branch symbols under Lebesgue measure are independent fair bits. In particular, the full tent map is Lebesgue-preserving and ergodic. Almost every orbit visits every interval with positive frequency and is dense; Birkhoff's theorem also gives the ordinary average \(\int_0^1y\,dy=1/2\). This completes the proof.

## Verification

The file `verify.py` uses only Python's standard-library rational arithmetic. It checks the universal finite-time estimate at 71,844 exact rational arithmetic assertions, checks the Bellman inequality at rational test points, and checks exact inverse-orbit relations and discounted partial sums. Run `python verify.py` to reproduce the assertions. These finite checks are corroborative; the two-branch calibration and density argument establish the infinite claims.

## Relationship to prior work

Gade and Bhalekar (2026) study homogeneous pantograph logistic and tent maps, and derive their increasing plateaus and the associated exact composition structure. Their Section 3 explicitly observes that delayed and undelayed time averages need not agree, without identifying their limiting values. The present theorem uses the dyadic member of that same class and determines an exact universal upper bound and the entire almost-sure accumulation interval. Classical symbolic dynamics and the Bernoulli coding of the full tent map are background, not claimed as discoveries. The right-branch inverse orbit and affine Bellman calibration are used here to calculate the new physical-time extremum.

## Limitations

The sharp constant and the full interval concern the exact dyadic delay and full-slope tent map, not arbitrary proportional delays, partial instantaneous coupling, other tent slopes, or higher-dimensional maps. The dense-orbit assumption cannot be omitted: for example \(x=0\) gives the constant zero trajectory. The result does not describe empirical-measure limit sets for arbitrary observables. Literature comparison is based on the identified primary source and accessible related material; absence of a matching search result is not a proof of priority.

## References

1. P. M. Gade and S. Bhalekar, *Pantograph Difference Equations: Stability, Multistability, and Chaos*, arXiv:2610.21635, first submitted 2026-10-15, especially Section 3. https://arxiv.org/abs/2610.21635
2. P. Boyland, A. de Carvalho and T. Hall, *Itineraries for inverse limits of tent maps: A backward view*, Topology and its Applications 232 (2017), 1–12. https://doi.org/10.1016/j.topol.2017.09.012
3. A. Dzhalilov and X. Abdusalomov, *Symbolic Dynamics and Markov Structure for Tent-Type Maps*, Uzbek Mathematical Journal 70(3) (2026), 48–61. https://doi.org/10.29229/uzmj.2026-3-6

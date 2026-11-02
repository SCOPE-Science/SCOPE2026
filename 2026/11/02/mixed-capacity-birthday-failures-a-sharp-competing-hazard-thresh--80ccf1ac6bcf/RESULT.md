# Mixed-capacity birthday failures: a sharp competing-hazard threshold

## Finding

A system has \(N\ge1\) labeled bins. Exactly \(a_N\) bins have capacity one; the other \(b_N=N-a_N\) have capacity two. Balls independently select uniformly among all \(N\) bins, irrespective of whether a bin is full. Let \(T_N\) be the index, including the rejected arrival, of the first ball directed to a full bin; let \(J_N\in\{1,2\}\) be that bin's capacity.

For \(a=a_N\), \(b=b_N\), define \(G_{a,b}(z)=(1+z)^a(1+z+z^2/2)^b\). For every integer \(m\ge0\), with negative-index coefficients interpreted as zero,

\[
\begin{aligned}
\Pr(T_N>m)&=\frac{m!}{N^m}[z^m]G_{a,b}(z),\\
\Pr(T_N=m+1,J_N=1)&=\frac{a\,m!}{N^{m+1}}[z^{m-1}](1+z)^{a-1}(1+z+z^2/2)^b,\\
\Pr(T_N=m+1,J_N=2)&=\frac{b\,m!}{2N^{m+1}}[z^{m-2}](1+z)^a(1+z+z^2/2)^{b-1}.
\end{aligned}
\]

A term with zero multiplicity is defined as zero, so no negative powers are required at \(a=0\) or \(b=0\).

The asymptotic regimes are a complete trichotomy:

1. If \(a_N/N^{2/3}\to0\), then \(T_N/N^{2/3}\) converges to a positive variable with survival \(e^{-x^3/6}\), and \(\Pr(J_N=2)\to1\).
2. If \(a_N/N^{2/3}\to\alpha\in(0,\infty)\), then \((T_N/N^{2/3},J_N)\) converges to a time-and-mark pair with sub-probability densities on \(x>0\):

\[
 f_1(x)=\alpha x\exp(-\alpha x^2/2-x^3/6),\qquad
 f_2(x)=\frac{x^2}{2}\exp(-\alpha x^2/2-x^3/6).
\]

Consequently the time has survival \(\exp(-\alpha x^2/2-x^3/6)\) and, at a positive failure time \(x\), the limiting conditional probability of a capacity-one failure is \(2\alpha/(2\alpha+x)\).
3. If \(a_N/N^{2/3}\to\infty\), then \(T_N/(N/\sqrt{a_N})\) has limiting survival \(e^{-x^2/2}\), and \(\Pr(J_N=1)\to1\).

At criticality the capacity-one first-failure probability

\[
 p_1(\alpha)=\int_0^\infty \alpha x\exp(-\alpha x^2/2-x^3/6)\,dx
\]

is continuous and strictly increasing from zero to one. It equals \(1/2\) at a unique \(\alpha_*\approx0.5522\). Hence a vanishing fraction of single-slot bins, of order \(N^{2/3}\), competes equally with the \(N-O(N^{2/3})\) double-slot bins for the first failure. If \(a_N=\lfloor\alpha N^{2/3}\rfloor\) with fixed \(\alpha\ge0\), then for each fixed \(R<\infty\), the Poissonized log-survival approximation has uniform error \(O_{\alpha,R}(N^{-1/3})\) on \([0,R]\); no finite-size rate for the discrete arrival clock is asserted here.

## Assumptions and scope

The bins' capacities are fixed before sampling. Every ball chooses uniformly and independently from all \(N\) labels; a rejected ball is not redirected. The two capacities are precisely one and two. Limits are taken along arbitrary integer sequences \(N\to\infty\) and \(0\le a_N\le N\) subject only to the displayed scaling assumptions. There is exactly one first failed arrival, so the mark \(J_N\) is unambiguous. Convergence of marked laws means weak convergence on \([0,\infty)\times\{1,2\}\). Zero-capacity classes in the finite formulas contribute zero.

## Proof

**Finite-size identities.** Given an occupancy vector \((k_1,\ldots,k_N)\) with \(\sum_i k_i=m\), its probability after \(m\) independent throws is \(m!/(N^m\prod_i k_i!)\). No failure in the first \(m\) throws means \(k_i\le1\) for each capacity-one bin and \(k_i\le2\) for each capacity-two bin. Multiplying the corresponding exponential-polynomial factors gives \(G_{a,b}\), proving the survival formula. To fail at throw \(m+1\) in class one, choose a class-one bin occupied exactly once after \(m\) safe throws, contributing \(z\), then send the next ball to that bin with probability \(1/N\); sum over the \(a\) choices. For class two, the chosen bin must contain exactly two balls, contributing \(z^2/2\); sum over the \(b\) choices. These arguments prove both marked coefficient formulas, including the endpoints.

**Exact Poisson embedding.** Embed the successive throws at the arrival times \(S_k=E_1+\cdots+E_k\) of a unit-rate Poisson process, with iid unit-exponential waiting times \(E_k\), independent of all chosen bin labels. Each bin then receives an independent rate-\(1/N\) Poisson process. Write \(\tau_N=S_{T_N}\). The time until rejection at a particular capacity-one bin is the second arrival of its own process, distributed as \(\operatorname{Gamma}(2,1/N)\); for a capacity-two bin it is \(\operatorname{Gamma}(3,1/N)\). These clocks are mutually independent. For \(\lambda=t/N\), the exact no-rejection probability is

\[
 \Pr(\tau_N>t)=e^{-t}(1+\lambda)^{a_N}(1+\lambda+\lambda^2/2)^{b_N}.
\]

The minimum rejection times within the two capacity classes are independent. Ties occur with probability zero, so the class of the minimum is well-defined.

**Critical window.** Take \(t=xN^{2/3}\) and \(\lambda=xN^{-1/3}\). Uniformly for \(x\) in a bounded interval,

\[
 \log\bigl(e^{-\lambda}(1+\lambda)\bigr)=-\lambda^2/2+O(\lambda^3),
 \qquad
 \log\bigl(e^{-\lambda}(1+\lambda+\lambda^2/2)\bigr)=-\lambda^3/6+O(\lambda^4).
\]

If \(a_N/N^{2/3}\to\alpha<\infty\), the capacity-one class therefore has limiting minimum survival \(e^{-\alpha x^2/2}\), while \(b_N/N\to1\) makes the capacity-two class minimum survival converge to \(e^{-x^3/6}\). Their independence for every \(N\) yields independent limiting failure clocks, and their minimum has survival \(e^{-\alpha x^2/2-x^3/6}\). Differentiating the classwise limiting survivals gives the two competing-hazard densities \(f_1\) and \(f_2\). For \(\alpha=0\), the first class's clock escapes to infinity. When \(a_N=\lfloor\alpha N^{2/3}\rfloor\), the two Taylor remainders multiplied by their class sizes, together with the rounding and the difference \(b_N-N\), are \(O_{\alpha,R}(N^{-1/3})\) in the displayed log survival, uniformly on \(0\le x\le R\).

**Dominant fragile-bin regime.** When \(a_N/N^{2/3}\to\infty\), put \(t=xN/\sqrt{a_N}\), hence \(\lambda=x/\sqrt{a_N}\). Then

\[
 a_N\log\bigl(e^{-\lambda}(1+\lambda)\bigr)\to-x^2/2,
 \qquad
 b_N\log\bigl(e^{-\lambda}(1+\lambda+\lambda^2/2)\bigr)
 =O\bigl(N/a_N^{3/2}\bigr)\to0.
\]

Thus the first class has a Rayleigh-scale minimum and the other class fails only later with probability tending to one. This proves the third regime and its mark assertion.

**Returning to discrete arrivals.** In all regimes the continuous failure times divided by their stated scaling sequences are tight, and those scaling sequences diverge (they are at least of order \(\sqrt N\) in the third regime). For any fixed \(R>0\) and scale \(c_N\to\infty\), the centered exponential partial sums satisfy

\[
 \Pr\left(\max_{k\le\lceil Rc_N\rceil}|S_k-k|>\varepsilon c_N\right)
 \le \frac{\lceil Rc_N\rceil}{\varepsilon^2c_N^2}\to0
\]

by the square-integrable martingale maximal inequality. Tightness of \(\tau_N/c_N\) and the preceding bound imply \((T_N-\tau_N)/c_N\to0\) in probability. Crucially the bin that causes rejection, and hence \(J_N\), does not change when the same label sequence is run on the embedded clock. This transfers the joint time-and-mark limits to discrete throws.

**Unique class-balance parameter.** For \(\alpha>0\), independently generate \(U,V\sim\operatorname{Exp}(1)\) and set \(X_1(\alpha)=\sqrt{2U/\alpha}\), \(X_2=(6V)^{1/3}\). Their survivals are exactly those of the two limiting classwise failure times. The event \(X_1(\alpha)<X_2\) increases strictly as \(\alpha\) increases. Dominated convergence gives its limits zero and one as \(\alpha\) approaches zero and infinity, respectively, and ensures continuity. This proves existence and uniqueness of \(\alpha_*\). The integral expression follows by multiplying the class-one density by the other class's survival. Numerical quadrature gives the quoted approximate root; the root's uniqueness does not depend on the numerical calculation.

## Verification

The accompanying standalone \(\texttt{check.py}\) performs exact-rational comparisons between the coefficient formulas and a completely separate occupancy-count Markov recursion, for every \(1\le N\le8\), all \(0\le a\le N\), and selected early times. A third check enumerates actual ordered arrival words for \(N\le4\). It also checks probability conservation, numerical convergence of the Poissonized logarithmic survival, and the approximate class-balance root. The checker completed 2,183 deterministic assertions. It tests finite formulas and numerical consistency, not the infinite limiting proof; the latter is the analytic Poisson-embedding argument above. Run it with \(\texttt{python3 check.py}\) using the standard Python library only.

## Relationship to prior work

Gouet, Hitczenko, and Wesołowski (first public version 2019) prove Poisson and Gaussian limits for overflow when **every** bin has a common fixed capacity \(r\), even allowing unequal sampling probabilities. Their common-capacity theorem does not itself give the joint first-failure time and its bin-capacity mark for two different capacities. Henze (1998) establishes Poisson limits for a fixed occupancy threshold in uniformly sized cells. Arratia, Garibaldi, and Kilian (2013) analyze the number of draws to a specified number of ordinary birthday collisions, all defined by the same occupancy threshold. The exact coefficient formulas here and the simultaneous two-power first-failure crossover address a different, heterogeneous capacity question. Standard Poissonization and rare-event limit techniques are explicitly acknowledged as the ingredients; the results should not be interpreted as a new general Poisson-approximation theorem. A broad older mixed-threshold occupancy theorem may subsume part of the limiting statement; historical priority remains subject to independent checking.

## Limitations

Only independent uniform destinations, two fixed capacity classes and the first overflow are treated. Redirected or adaptive allocations, nonuniform selection probabilities, arbitrary capacity profiles and later overflow counts require separate analysis. The numerical balance constant is an approximation, not a certified interval. The Poissonized \(O(N^{-1/3})\) bound is not claimed for the discrete time. Independent historical-priority validation has not been performed.

## References

- R. Gouet, P. Hitczenko, and J. Wesołowski, *Asymptotics of the overflow in urn models*, arXiv:1905.06663, first public May 16, 2019, https://arxiv.org/abs/1905.06663.
- R. Arratia, S. Garibaldi, and J. Kilian, *Asymptotic distribution for the birthday problem with multiple coincidences, via an embedding of the collision process*, arXiv:1310.7055, first public October 26, 2013, https://arxiv.org/abs/1310.7055.
- N. Henze, *A Poisson limit law for a generalized birthday problem*, *Statistics & Probability Letters* 39 (1998), 333–336, https://doi.org/10.1016/S0167-7152(98)00076-5.

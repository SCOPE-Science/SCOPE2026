# Sharp entropy–arrow frontier for locally fair binary memory-three processes

## Finding

Consider a stationary binary process that is a strictly positive Markov chain of order three and whose **eight consecutive three-letter words are equally likely**. Let \(p_4(w)\) be its stationary four-word distribution, and let \(w^{\mathrm R}\) mean the letters of \(w\) in reverse order. Define its four-word time-arrow total variation and reversal divergence by

\[
\tau=\frac12\sum_{w\in\{0,1\}^4}|p_4(w)-p_4(w^{\mathrm R})|,\qquad
D_4=\sum_{w\in\{0,1\}^4}p_4(w)\log\frac{p_4(w)}{p_4(w^{\mathrm R})}.
\]

Using natural logarithms, the **complete set of feasible entropy–arrow pairs** \(\mathcal R\) is

\[
\boxed{\mathcal R=\{(0,0)\}\cup\{(t,d):0<t<1/2,\ d\ge 2t\operatorname{artanh}(2t)\}.}
\]

Every point of this region is attained by such a strictly positive stationary order-three chain. The origin is the only point with zero arrow. For each fixed \(0<\tau<1/2\), the lower bound is attained exactly when the one independent four-word circulation is distributed equally between two alternating channel pairs. At \(\tau=0\) all chains in this family are reversible. The full length-\(n\) block divergence obeys the exact identity

\[
D_n=(n-3)D_4\quad(n\ge3),
\]

so the stationary observed-path entropy-production rate per symbol is \(\sigma=D_4\). Thus the inequality is also a sharp rate bound. All one-, two- and three-consecutive-letter observations are **exactly fair independent bits**, even when \(\tau>0\). These assertions concern statistical irreversibility of the observed symbolic process, not a calibrated physical heat current.

## Assumptions and scope

The alphabet is \(\{0,1\}\), time is integer-valued and indexed by \(\mathbb Z\), and stationarity is strict. Markov order at most three means that the conditional distribution of the next bit given the entire past depends only on the preceding three bits. Each of the eight consecutive three-word probabilities is exactly \(h=1/8\). Each conditional transition probability lies strictly between zero and one. Logs are natural and \(0\log0\) conventions are unnecessary since all relevant word probabilities are positive. Reversal does not complement the symbols.

This is a **local** fairness condition: it does not assert that three bits at arbitrarily separated times are independent. The conclusion holds for all real feasible parameters, not just rational examples. A unique stationary full-support chain is induced by each positive compatible four-word table, since its order-three history chain has the strongly connected binary de Bruijn support and a self-loop.

## Proof

**1. All admissible four-word tables.** Put \(h=1/8\). Stationarity and the uniform three-word marginal require, for every binary triple \(v\),

\[
\sum_{c\in\{0,1\}}p_4(vc)=h,\qquad
\sum_{c\in\{0,1\}}p_4(cv)=h.
\]

Solving these sixteen linear equations gives the following table; each entry is a **four-word probability**, with the row prefix and column suffix concatenated:

| First two bits | \(00\) | \(01\) | \(10\) | \(11\) |
|---|---:|---:|---:|---:|
| \(00\) | \(a\) | \(h-a\) | \(x\) | \(h-x\) |
| \(01\) | \(x-J\) | \(h-x+J\) | \(b\) | \(h-b\) |
| \(10\) | \(h-a\) | \(a\) | \(h-x\) | \(x\) |
| \(11\) | \(h-x+J\) | \(x-J\) | \(h-b\) | \(b\) |

To be explicit, the row \(01\) and column \(00\) denote the word \(0100\), and similarly for every cell. Conversely any table of this form with

\[
0<a,b<h,\qquad |J|<h,\qquad \max(0,J)<x<\min(h,h+J)
\]

is positive, has total mass one, and satisfies both triple-marginal constraints. The conditional transition law is \(K(v,c)=8p_4(vc)\). The vector assigning mass \(h\) to each history triple is stationary; irreducibility and aperiodicity give its uniqueness. The parametrization is therefore necessary and sufficient, and no hidden normalization restrictions remain.

**2. Reversal geometry.** Four reverse-paired channels have nonzero possible differences; choosing the indicated orientations, these are

\[
\begin{aligned}
p_4(0010)-p_4(0100)&=J,\\
p_4(0101)-p_4(1010)&=J,\\
p_4(1011)-p_4(1101)&=J,\\
p_4(1100)-p_4(0011)&=J.
\end{aligned}
\]

Every other reverse-paired difference is zero. It follows that \(\tau=4|J|\). The feasibility condition \(|J|<h\) proves the strict bound \(\tau<1/2\); every allowed value is realized by choosing, for instance, \(J=\tau/4\), \(x=(h+J)/2\), \(a=b=h/2\). When \(J=0\), every four-word probability is equal to its reversed counterpart. The chain's order-three property then makes all longer path laws reversible. When \(J\neq0\), its four-word law witnesses irreversibility.

**3. Exact finite-word and rate identity.** Let \(p_n\) denote the stationary law of a word \(w=w_0\ldots w_{n-1}\). The uniform history distribution and order-three Markov rule imply, for every \(n\ge3\),

\[
p_n(w)=h\prod_{i=0}^{n-4}\bigl(8p_4(w_iw_{i+1}w_{i+2}w_{i+3})\bigr).
\]

The empty product for \(n=3\) is one. In the reversed word the four-word factors appear in opposite order and with each four-word reversed; hence, **pathwise**, 

\[
\log\frac{p_n(w)}{p_n(w^{\mathrm R})}
=\sum_{i=0}^{n-4}\log\frac{p_4(w_iw_{i+1}w_{i+2}w_{i+3})}{p_4((w_iw_{i+1}w_{i+2}w_{i+3})^{\mathrm R})}.
\]

Taking expectations and invoking stationarity yields \(D_n=(n-3)D_4\) exactly, as asserted. It follows that \(\lim_{n\to\infty}D_n/n=D_4\). All shorter word probabilities equal \(2^{-n}\) for \(n\le3\), so \(D_1=D_2=D_3=0\).

**4. Sharp lower envelope.** Write \(y=h-x\). Grouping the four nontrivial reverse pairs gives the exact expression

\[
D_4=2J\log\frac{x}{x-J}+2J\log\frac{h-x+J}{h-x}.
\]

For \(J\neq0\), differentiation within the open feasible interval gives

\[
\frac{dD_4}{dx}=2J^2\left(\frac1{(h-x)(h-x+J)}-\frac1{x(x-J)}\right).
\]

All denominators are positive, and the sign of this derivative is exactly the sign of \(2x-h-J\). Consequently the **unique** minimizer for a given nonzero circulation is \(x=(h+J)/2\). Substitution gives

\[
\begin{aligned}
D_{4,\min}&=4|J|\log\frac{h+|J|}{h-|J|}\\
&=2\tau\operatorname{artanh}(2\tau),\qquad \tau=4|J|.
\end{aligned}
\]

At the minimizing value the two distinct types of reverse-paired channel masses are equal in magnitude, with relative probabilities \((h+|J|)/2\) and \((h-|J|)/2\). The free values of \(a,b\) do not affect \(\tau\) or \(D_4\). Equality at \(\tau>0\) is therefore equivalent to \(x=(h+J)/2\); equality at zero holds for every reversible chain in the family.

**5. Full attainable region and boundary.** For any nonzero fixed \(J\), the feasible interval for \(x\) is connected, the divergence is continuous, it attains the displayed minimum, and it tends to \(+\infty\) as \(x\) approaches the endpoint where either \(x-J\) or \(h-x\) vanishes. Hence its image is exactly the half-line beginning at the minimum, with all points attained while **remaining strictly positive**. For \(J=0\), every value of \(x\) gives \(D_4=0\). Thus every point of the displayed set, and no other, is attainable. At zero arrow only the origin occurs. The upper arrow endpoint \(\tau=1/2\) is excluded by strict positivity, and \(2\tau\operatorname{artanh}(2\tau)\to+\infty\) there.

## Verification

The accompanying standard-library-only program `verify.py` constructs the positive four-word law over 32 seeded exact-rational parameter tuples, verifies all row and column triple constraints and their consequences, compares exact reversal total variation against \(4|J|\), and independently enumerates every binary word through length eight. It checks the forward/reversed block divergence identity numerically against an independent direct sum, plus exact-rational normalization, sharp equality examples and divergence near the feasible boundary. It reports 266 word-normalization and finite-block consistency checks. The infinite family and sharp optimization are proved analytically above, **not inferred** from finite computations.

## Relationship to prior work

Arola-Fernández and Lacasa (2023) prove the general fact that stationary binary symbolic processes have no time-arrow in one-, two-, or three-word statistics and identify four-word reversal pairs. That detection threshold and reversal-pair enumeration are **prior work** here. Roldán and Parrondo (2010) derive the connection between consecutive block relative entropies and the entropy-production rate for finite-order Markov observations; the linear finite-block relationship and KL method are likewise **prior ideas**. Sagawa (2026) develops an overarching stochastic-thermodynamics treatment of autoregressive and non-Markovian observed sequences and is the recent motivation. Berend, Harremoës and Kontorovich (2014) study general constrained-relative-entropy and total-variation optimization, which supplies relevant conceptual context.

The narrower claim assessed here is the exact **stationary uniform-triple binary order-three** four-word probability polytope, its single chiral circulation, the complete **sharp** entropy–variation region including equality and unbounded upper fiber, and constructive attainment by strictly positive memory-three chains. These source comparisons do not imply a proof of worldwide publication priority.

## Limitations

The fairness condition is for contiguous triples, not arbitrary times. Higher alphabets, longer memories, nonstationary processes and nonuniform three-word marginals are outside the stated sharp frontier. Strictly positive transitions exclude the maximal total-variation boundary; limits may be singular. The divergence is an **observational pathwise information statistic**, not necessarily all of a hidden physical system's entropy production or heat. Results are self-reviewed, not independently audited. A more general unlocated sharp divergence theorem may imply part of this result; publication priority requires human literature review.

## References

1. T. Sagawa, *Stochastic Thermodynamics for Autoregressive Generative Models: A Non-Markovian Perspective* (first public 9 April 2026), arXiv:2604.07867, https://arxiv.org/abs/2604.07867 .
2. L. Arola-Fernández and L. Lacasa, *Irreversibility of symbolic time series: a cautionary tale* (2023), arXiv:2303.11868, https://arxiv.org/abs/2303.11868 .
3. É. Roldán and J. M. R. Parrondo, *Estimating dissipation from single stationary trajectories* (2010), arXiv:1004.2831, https://arxiv.org/abs/1004.2831 .
4. D. Berend, P. Harremoës and A. Kontorovich, *Minimum KL-divergence on complements of L1 balls* (2014), arXiv:1206.6544, https://arxiv.org/abs/1206.6544 .

# Exact finite-group crossover ladder in the symmetric volunteer's dilemma

## Finding

For every integer \(n\geq2\), consider the classic simultaneous, identical-agent volunteer's dilemma with benefit \(b>0\), individual volunteering cost \(0<c<b\), and provision of the public good whenever **at least one** individual volunteers. All players benefit upon provision; every volunteer pays the cost even if others volunteer. All players independently use the same mixed action in the symmetric Nash equilibrium. Define
\[
\lambda=\log(b/c)>0,\qquad V_n(\lambda)=n\bigl(1-e^{-\lambda/(n-1)}\bigr).
\]
Here \(V_n\) is the expected total number of volunteering individuals, not the provision probability.

**Exact crossover ladder.** For every \(n\geq2\), the equation
\[
\sum_{j=1}^{n-1}\left(e^{\lambda j/[n(n-1)]}-1\right)=1
\tag{1}
\]
has one root \(\lambda_n>0\). These thresholds obey
\[
\lambda_2=2\log 2<\lambda_3<\lambda_4<\cdots<2,
\qquad\lim_{n\to\infty}\lambda_n=2,
\tag{2}
\]
and the exact neighboring comparison is
\[
V_{n+1}(\lambda)\begin{cases}
<V_n(\lambda),&\lambda<\lambda_n,\\
=V_n(\lambda),&\lambda=\lambda_n,\\
>V_n(\lambda),&\lambda>\lambda_n.
\end{cases}
\tag{3}
\]
Consequently, for fixed \(\lambda\), there is **at most one peak** as group size increases. If \(0<\lambda<2\log2\), the sequence strictly decreases; at \(\lambda=2\log2\), the first two sizes \(2\) and \(3\) tie before strict decrease. For \(\lambda_k<\lambda<\lambda_{k+1}\) the unique global maximum occurs at size \(k+1\); for \(\lambda=\lambda_k\), exactly the two adjacent sizes \(k,k+1\) attain the global maximum. For \(\lambda\geq2\), the sequence strictly increases toward \(\lambda\), with no finite maximizer.

The transition thresholds have the sharp finite-size asymptotic
\[
\lambda_n=2-\frac{4}{3n}+O(n^{-2}).
\tag{4}
\]
As \(\lambda\uparrow2\) from below, each maximizing group size \(N_*(\lambda)\) therefore satisfies
\[
N_*(\lambda)\sim \frac{4}{3(2-\lambda)}.
\tag{5}
\]
The finite-peaked regime is equivalently \(e^{-2}<c/b<1/4\); a discrete tie occurs only at its countably many threshold ratios.

## Assumptions and scope

There are \(n\geq2\) individuals with exactly the same benefit and cost. Actions are simultaneous and chosen independently according to a common probability; costs are nonrefundable, and one contribution suffices. This concerns the symmetric mixed Nash equilibrium, not the game's asymmetric pure Nash equilibria, evolutionary equilibria, sequential volunteering, heterogeneity, or a requirement of two or more contributors.

Under independent volunteering with probability \(q\), a player receives expected utility \(b-c\) from volunteering and \(b[1-(1-q)^{n-1}]\) from not volunteering. Strict inequality \(0<c<b\) gives the unique interior symmetric equilibrium
\[
q_n=1-(c/b)^{1/(n-1)}=1-e^{-\lambda/(n-1)}.
\tag{6}
\]
Thus \(V_n=nq_n\). The symmetric equilibrium probability of successful provision is \(1-e^{-\lambda n/(n-1)}\), which **strictly decreases** with \(n\) for every \(\lambda>0\), even in parameter regimes where the expected number of volunteers initially rises.

## Proof

**Step 1: exact sign decomposition.** Fix \(n\ge2\), \(\lambda>0\), and put \(z=e^{-\lambda/[n(n-1)]}\in(0,1)\). Then \(e^{-\lambda/(n-1)}=z^n\) and \(e^{-\lambda/n}=z^{n-1}\). Therefore
\[
\begin{aligned}
V_{n+1}-V_n
&=1-(n+1)z^{n-1}+nz^n\\
&=(1-z)z^{n-1}\left(\sum_{j=1}^{n-1}(z^{-j}-1)-1\right).
\end{aligned}
\tag{7}
\]
Define \(S_n(\lambda)=\sum_{j=1}^{n-1}(e^{\lambda j/[n(n-1)]}-1)\). The sign of \(V_{n+1}-V_n\) is the sign of \(S_n(\lambda)-1\). Since \(S_n(0)=0\), \(S_n\) is strictly increasing and continuous, and \(S_n(\lambda)\to\infty\) as \(\lambda\to\infty\), a unique positive root \(\lambda_n\) exists. This proves the neighboring comparison (3).

**Step 2: monotonicity of the entire crossover ladder.** Compare the following \(n\)-component vectors, each written in nonincreasing order:
\[
\mathbf a^{(n)}=\operatorname{sort}_{\downarrow}\left(\frac{1}{n(n-1)},\ldots,\frac{n-1}{n(n-1)},0\right),
\quad
\mathbf b^{(n)}=\operatorname{sort}_{\downarrow}\left(\frac{1}{n(n+1)},\ldots,\frac{n}{n(n+1)}\right).
\]
Both have total sum \(1/2\), while the difference between their first \(r\) partial sums is exactly
\[
\sum_{i=1}^r a_i^{(n)}-\sum_{i=1}^r b_i^{(n)}
=\frac{r(n-r)}{n(n^2-1)}>0\quad(1\le r<n).
\tag{8}
\]
Thus \(\mathbf a^{(n)}\) strictly majorizes \(\mathbf b^{(n)}\). Strict convexity of \(u\mapsto e^{\lambda u}-1\) for \(\lambda>0\), together with the finite-dimensional majorization inequality, yields
\[
S_n(\lambda)>S_{n+1}(\lambda)\quad\text{for every }\lambda>0.
\tag{9}
\]
Because each \(S_n\) is strictly increasing in its argument, (9) implies \(\lambda_n<\lambda_{n+1}\).

**Step 3: limit and global classification.** The identity
\[
\sum_{j=1}^{n-1}\frac{j}{n(n-1)}=\frac12
\]
and \(e^t-1>t\) for positive \(t\) show \(S_n(\lambda)>\lambda/2\), so \(\lambda_n<2\). Moreover \(j/[n(n-1)]\le1/n\), hence Taylor's theorem uniformly for bounded \(\lambda\) gives \(S_n(\lambda)\to\lambda/2\). From strict increase and the root condition it follows that \(\lambda_n\uparrow2\). The explicit \(n=2\) equation is \(e^{\lambda/2}-1=1\), yielding \(\lambda_2=2\log2\). Combining the strict ordering of thresholds with (3) proves every case of the claimed global classification, including the two-size ties and the absence of a finite maximizer when \(\lambda\ge2\). The elementary limit \(\lim_{n\to\infty}V_n=\lambda\) follows from \(e^{-t}=1-t+O(t^2)\).

**Step 4: sharp near-critical law.** Uniformly for \(\lambda\) in a fixed bounded interval, sum the exponential series in the definition of \(S_n\):
\[
S_n(\lambda)=\frac{\lambda}{2}
+\frac{\lambda^2(2n-1)}{12n(n-1)}+O(n^{-2})
=\frac{\lambda}{2}+\frac{\lambda^2}{6n}+O(n^{-2}).
\tag{10}
\]
The remainder is uniformly \(O(n^{-2})\) because the sum of the cubes of the summands' exponents is \(O(n^{-2})\). Substitute \(S_n(\lambda_n)=1\) and \(\lambda_n\to2\). First (10) gives \(2-\lambda_n=O(n^{-1})\), and substitution again gives \(2-\lambda_n=4/(3n)+O(n^{-2})\). The two adjacent threshold inequalities bracketing a maximizing size give (5).

**Example.** At \(\lambda=3/2\), one has \(\lambda_2<3/2<\lambda_3\), so size \(3\) is the unique optimal group size for maximizing expected volunteer count. Numerically, \(V_2\approx1.553740\), \(V_3\approx1.582900\), and \(V_4\approx1.573877\).

## Verification

The standalone standard-library script `verify.py` checks \(660\) exact rational identities, comprising the majorization partial sums and the algebraic forward-difference identity, and \(825\) floating-point consistency checks. It numerically evaluates the threshold roots, verifies their ordering and the asymptotic coefficient, checks forward differences over a range of parameters, and independently recomputes the volunteer expectation using binomial probabilities. Its output is reported in `VERIFICATION.md`. These finite checks do not substitute for the all-\(n\) analytical proof.

## Relationship to prior work

The volunteering game, symmetric equilibrium (6), large-group limit, and the fact that public-good provision probability decreases with group size are known. Diekmann (1985) introduced the canonical dilemma. Chen, Gross, and Dieckmann (2013) develop rewarding and evolutionary results for generalized volunteering. Nöldeke and Peña (2020, with an accessible 2018 preprint) analyze group-size comparative statics of participation games mainly under a contributor threshold greater than one; they explicitly record the classical one-volunteer expected-count expression and asymptotic limit, and identify the harder general case's missing all-size monotonicity classification. The **claim here** is only the exact, strictly ordered all-finite-size crossover ladder for the one-volunteer case, the full corresponding maximizer classification, and the \(4/3\) near-critical drift coefficient. This conclusion is not a claim of having solved the threshold-greater-than-one problem.

## Limitations

The game uses identical payoffs, independent simultaneous choices, a single required volunteer, and the particular symmetric equilibrium. It does not compare welfare-optimal collective decisions, symmetric equilibria under stochastic group size, or alternative payoff specifications. The cross-literature originality assessment cannot exclude a prior textbook or network-economics proof of an equivalent exact finite-size ladder under different notation; the formulas are elementary enough that independent rediscovery is plausible. No independent mathematical audit has been performed.

## References

1. Andreas Diekmann, *Volunteer's Dilemma*, Journal of Conflict Resolution **29** (1985), 605–610. DOI: 10.1177/0022002785029004003.
2. Xiaojie Chen, Thilo Gross, Ulf Dieckmann, *Shared rewarding overcomes defection traps in generalized volunteer's dilemmas*, arXiv:1306.4782, first posted 2013-06-20. https://arxiv.org/abs/1306.4782.
3. Georg Nöldeke, Jorge Peña, *Group size and collective action in a binary contribution game*, Journal of Mathematical Economics **88** (2020), 42–51, DOI: 10.1016/j.jmateco.2020.02.003; accessible preprint: https://publications.ut-capitole.fr/id/eprint/26531/1/wp_iast_1886.pdf.
4. Thomas R. Palfrey, Howard Rosenthal, *Participation and the provision of discrete public goods: A strategic analysis*, Journal of Public Economics **24** (1984), 171–193.

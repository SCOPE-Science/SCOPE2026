# Stochastic persistence ordering by the number of domain walls

## Finding
Fix an integer \(n\ge 2\). Start a sign walk \((\sigma_i)_{i=1}^n\) with a fair sign, and for each subsequent step retain the current sign with probability \(p\in[0,1]\), independently of all previous retention decisions. Let \(S_n=\sum_{i=1}^n\sigma_i\), and let \(T_n\) be its number of sign switches.

**Stochastic persistence theorem.** For every \(0\le p_1<p_2\le1\) and every real threshold \(h\),
\[
\Pr_{p_1}(|S_n|\ge h)\le\Pr_{p_2}(|S_n|\ge h).
\]
For \(n\bmod2<h\le n\), the inequality is strict; at all other thresholds the two probabilities are identically zero or one. Thus absolute displacement is first-order stochastically increasing in persistence across the entire parameter interval, including the anti-persistent regime \(p<1/2\).

The mechanism is a stronger **conditional likelihood-ratio ordering**. If \(Q_a\) is the law of \(|S_n|\) given \(T_n=2a-1\), then the conditional laws at \(2a-1\) and \(2a\) switches are exactly identical whenever both counts are admissible. Whenever \(2a+1\le n-1\), \(Q_{a+1}\) is smaller than \(Q_a\) in monotone likelihood-ratio order. These equalities also hold for the *signed* displacement before taking its absolute value.

## Assumptions and scope
All statements concern the stationary symmetric two-state Markov chain on \(\{-1,+1\}\) with free endpoints, at an arbitrary but fixed finite horizon \(n\ge2\). The switch indicators are independent Bernoulli variables of parameter \(1-p\). The conditional laws in the proof are combinatorially defined even at \(p=0,1\), when some switch counts have zero unconditional probability. The ordering is not claimed for biased initial signs, asymmetric transition probabilities, applied magnetic fields, or cyclic boundary conditions.

Set \(B(r,k)=\binom{r}{k}\) for integers \(0\le k\le r\), and \(B(r,k)=0\) otherwise. For a signed displacement \(s\in\{-n,-n+2,\ldots,n\}\), write \(j=(n+s)/2\) and \(\ell=(n-s)/2\). If \(a\ge1\) and \(2a-1\le n-1\), the exact conditional mass is
\[
\Pr(S_n=s\mid T_n=2a-1)
 =\frac{B(j-1,a-1)B(\ell-1,a-1)}{B(n-1,2a-1)}.
\]
For \(2a\le n-1\), the same expression gives \(\Pr(S_n=s\mid T_n=2a)\). Zero binomial factors give zero mass at both fully aligned endpoints. Conditioned on no switches, \(S_n\) is equally likely to be \(-n\) or \(+n\).

## Proof
**1. Uniform switch subsets and exact run counts.** The event \(T_n=m\) selects a uniformly random \(m\)-element subset of the \(n-1\) bonds; the initial sign remains fair. Thus there are \(2B(n-1,m)\) equiprobable sign words for each prescribed switch count. If a word has \(j\) plus signs and \(\ell\) minus signs, exactly \(2a-1\) switches create \(a\) runs of each sign. Compositions of the two run lengths and the two possible initial signs produce \(2B(j-1,a-1)B(\ell-1,a-1)\) words, hence the asserted conditional mass.

For exactly \(2a\) switches, the word begins and ends with the same sign. The two start-sign choices contribute
\[
 B(j-1,a)B(\ell-1,a-1)+B(j-1,a-1)B(\ell-1,a).
\]
When \(j,\ell\ge a\), the last quantity equals
\[
 \frac{n-2a}{a}B(j-1,a-1)B(\ell-1,a-1).
\]
The identity is also valid by zero conventions at the support boundary. Since
\[
 \frac{B(n-1,2a)}{B(n-1,2a-1)}=\frac{n-2a}{2a},
\]
division by the total \(2B(n-1,2a)\) shows that the conditional **signed** mass at \(2a\) switches equals that at \(2a-1\) switches. This establishes the pairwise equality with all normalization factors.

**2. A strict likelihood-ratio cascade.** Compare the common mass formula for \(2a-1\) switches with the formula for \(2a+1\). For every \(s\) in the support of the older law,
\[
 \frac{\Pr(S_n=s\mid T_n=2a+1)}
 {\Pr(S_n=s\mid T_n=2a-1)}
 =\frac{B(n-1,2a-1)}{a^2 B(n-1,2a+1)}
 \frac{(n-2a)^2-s^2}{4}.
\]
Here \(2a+1\le n-1\). The formula includes the extreme points of the older support, where the new mass vanishes, and is nonnegative everywhere. The ratio depends only on \(|s|\) and strictly decreases as \(|s|\) increases on its admissible support. Consequently the same ratio holds for the absolute-value laws \(Q_{a+1}\) and \(Q_a\); cancellation of the doubling at nonzero signed values is exact. Since the ratio is decreasing and integrates to one, the elementary reverse-Chebyshev covariance inequality gives, for every nondecreasing function \(g\),
\[
 \mathbb E_{Q_{a+1}}g\le \mathbb E_{Q_a}g.
\]
This proves monotone likelihood-ratio order, hence first-order stochastic order. When an even switch count lies between two odd counts, its law equals that of the preceding odd count. At zero switches, \(|S_n|=n\) almost surely, which dominates every other conditional law. Hence the conditional tail \(f_m(h)=\Pr(|S_n|\ge h\mid T_n=m)\) is nonincreasing in every integer \(m\in\{0,\ldots,n-1\}\).

**3. Parameter comparison and strictness.** Couple all persistence values using independent uniform variables \(U_1,\ldots,U_{n-1}\) and declare a switch on bond \(i\) precisely when \(U_i>p\). This gives \(T_n(p_2)\le T_n(p_1)\) almost surely for \(p_1<p_2\). Conditioning on the number of switches,
\[
 \Pr_p(|S_n|\ge h)=\mathbb E[f_{T_n(p)}(h)],
\]
and the monotonicity of \(f_m\) proves the theorem. Let \(d=n\bmod2\). If \(d<h\le n\), then \(f_0(h)=1\), while \(f_1(h)<1\): one switch can place the endpoint at absolute displacement \(d\). The coupling event \(T_n(p_2)=0\), \(T_n(p_1)=1\) has positive probability for \(0\le p_1<p_2\le1\), including the boundary cases. Thus the stochastic inequality is strict at exactly these nontrivial thresholds. For \(h\le d\) all possible absolute displacements exceed the threshold, and for \(h>n\) none does. This handles all real thresholds and endpoints.

## Verification
The standalone `verify.py` uses exact integer enumeration of all switch subsets and both first-sign choices for every length \(2\le n\le14\). It separately checks each displayed conditional signed mass, normalization, equality of paired switch laws, the explicit decreasing likelihood ratio, conditional tail ordering, and direct parameter-tail comparisons at eleven rational persistence values including \(0\) and \(1\). Running `python verify.py` reproduces the assertion count recorded in `verification_output.txt`. The proof of the theorem is the all-length argument above, not finite enumeration.

## Relationship to prior work
The main literature source is Pemmasani, *Uniform Bessel bounds for endpoint crossings in the persistent random walk*, arXiv:2610.06935v1 (2026-10-03), especially Theorem 2.1 and Section 4. That paper gives the run-count coefficients, analyzes individual bin heights and central/end crossings, and supplies the exact model; it does not state the unconditional first-order stochastic comparison in the persistence parameter or the conditional odd/even switch-law identity and likelihood-ratio cascade. The binomial counting formula itself is prior work and is not claimed as novel.

Dekking and Kong, *Multimodality of the Markov Binomial Distribution*, arXiv:1102.3613v1, analyze shape, log-concavity and moment formulas of the same occupancy family, not the parameter-dependent absolute-deviation stochastic order. Zheng, Lin and Zhang, *Landau free energy and the absence of spontaneous magnetization of the one-dimensional Ising model*, arXiv:2605.06691v1, derive density-of-states and thermodynamic magnetization comparisons; fixed-energy monotonicity in magnetization does not imply the cross-energy normalized distributional order established here. Renshaw and Henderson's older exact-law study is a substantial historical-priority risk because only its abstract was accessible.

## Limitations
The all-parameter order relies on fair initial sign, symmetric sign-change probability, a finite open chain, and observations of the final total absolute displacement. It does not order entire paths, arbitrary individual bin masses, or models with boundary fields. No independent mathematical audit or definitive historical-priority certification has been performed. The inaccessible 1981 primary article could contain an equivalent observation despite its abstract emphasizing transition probabilities and limiting laws.

## References
1. A. Pemmasani, *Uniform Bessel bounds for endpoint crossings in the persistent random walk*, arXiv:2610.06935v1, 2026-10-03, https://arxiv.org/html/2610.06935v1 .
2. M. Dekking and D. Kong, *Multimodality of the Markov Binomial Distribution*, arXiv:1102.3613v1, 2011, https://arxiv.org/pdf/1102.3613 .
3. Z. F. Zheng, R. K. Lin, and J. M. Zhang, *Landau free energy and the absence of spontaneous magnetization of the one-dimensional Ising model*, arXiv:2605.06691v1, 2026, https://arxiv.org/html/2605.06691v1 .
4. E. Renshaw and R. Henderson, *The correlated random walk*, J. Appl. Probab. 18 (1981), 403–414, https://doi.org/10.2307/3213286 .

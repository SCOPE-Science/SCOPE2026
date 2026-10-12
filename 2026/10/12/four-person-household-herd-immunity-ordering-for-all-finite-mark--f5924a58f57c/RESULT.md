# Four-person household herd-immunity ordering for all finite Markovian local rates

## Finding

In the four-person common-household SEIR epidemic model of Ball, Critcher, Neal and Sirl [1], assume individual infectious periods are independent rate-one exponentials. For every finite local pairwise infectious-contact rate \(\ell>0\) and every first-epidemic global escape probability \(0<\pi<1\), the infection-depleted population has a strictly larger second-epidemic household threshold parameter than independent random vaccination of the same proportion of individuals:

\[
\widehat R_{DI}(z)>\widehat R_U(z).
\]

Consequently, whenever the unmodified household epidemic is supercritical (\(R_*>1\)), the approximate disease-induced herd immunity level defined in [1] satisfies \(\widetilde h_D>h_C\). This settles the first household size beyond the previously proved cases \(n=2,3\) in Conjecture 4.12 of [1], subject to exponential infectious periods.

## Assumptions and scope

Every household has exactly four individuals. Within an infectious period, each infective contacts any particular other household member through an independent Poisson process of rate \(\ell>0\); its infectious period is exponential with mean one. The common global contact rate is positive, and \(\pi\in(0,1)\) denotes an individual's probability of avoiding all global infectious contacts during the first epidemic. The latent-period law does not enter the final-outcome identities. All recovered first-epidemic individuals are perfectly immune at the start of the second epidemic. The first-epidemic immune fraction is \(z=1-s\), with \(s\) the mean susceptible fraction; vaccination immunizes each individual independently with probability \(z\).

The threshold parameters use household branching-process reproduction numbers (not the generation-based reproduction number \(R_0\)). For any global contact rate \(g>0\), both thresholds below carry a common factor \(g\) because the infectious mean equals one. To infer the herd-immunity comparison, \(\widetilde h_D\) and \(h_C\) are precisely the quantities defined in [1, §3]; \(\widetilde h_D\) is an approximation to the full disease-induced level \(h_D\), not its synonym.

## Proof

For integers \(k=1,2,3,4\), put

\[
q_j=(1+j\ell)^{-1}\quad(j\ge1),\qquad \beta_1=1,\qquad
\beta_k=k-\sum_{j=1}^{k-1}\binom{k}{j}\beta_jq_j^{k-j},
\]
\[
\mu_0=0,\qquad
\mu_k=k-\sum_{j=1}^{k-1}\binom{k-1}{j}\beta_jq_j^{k-j}.
\]

These are the source's within-household final-infection expectations [1, (2.2)] specialized to \(\varphi(t)=1/(1+t)\). In particular \(\mu_1=1\), \(\mu_2=(1+2\ell)/(1+\ell)\). For \(v=0,1,2,3\), recursively define

\[
P_v=\left[\binom4v\pi^{4-v}-\sum_{i=0}^{v-1}\binom{4-i}{v-i}P_i q_{4-v}^{-i}\right]q_{4-v}^{v},
\qquad P_4=1-\sum_{v=0}^3P_v.
\]

By [1, (2.5)], \(P_v\) is exactly the probability that a four-person household has \(v\) infected members after the first epidemic. Define

\[
s=\frac14\sum_{v=0}^3(4-v)P_v,\qquad z=1-s.
\]

The corresponding vaccination distribution is \(U_v=\binom4v z^v s^{4-v}\). The formulas in [1, (3.1), §4.4] yield the following normalized exact threshold difference:

\[
D(\ell,\pi):=\frac{\widehat R_{DI}(z)-\widehat R_U(z)}g
=\sum_{v=0}^3\frac{4-v}{4}(P_v-U_v)\mu_{4-v}.
\]

**Exact positivity identity.** The displayed finite recursions are rational in \(\ell,\pi\). Clearing their denominators and extracting boundary factors gives

\[
D(\ell,\pi)=\frac{\ell^2\pi^2(1-\pi)\,H(\ell,\pi)}{(1+\ell)^{15}(1+2\ell)^{10}(1+3\ell)^5}.
\]

Here \(H\) is a polynomial of degree \(28\) in \(\ell\) and degree \(13\) in \(\pi\), specified **exactly** by the accompanying coefficient file `positivity_coefficients.tsv`:

\[
H(\ell,\pi)=\sum_{k=0}^{13}\binom{13}{k}\pi^k(1-\pi)^{13-k}\underbrace{\sum_{j=0}^{28}b_{kj}\ell^j}_{B_k(\ell)}.
\]

The tab-separated file records all \(14\cdot29=406\) rational coefficients \(b_{kj}\), including zeros. Every coefficient is nonnegative and every \(B_k\) is nonzero. The accompanying `verify_household.py` recomputes the source recursions and the rational numerator, checks the denominator and degree, inverts the Bernstein basis *exactly* coefficient by coefficient, matches every coefficient to the supplied table, and checks all 406 signs without floating-point tolerances. Since \(\ell>0\) and \(0<\pi<1\), all Bernstein weights are positive, so \(H(\ell,\pi)>0\) and hence \(D(\ell,\pi)>0\).

Finally, at the contact-rate restriction that defines \(\widetilde h_D\) in [1, §3], the post-infection threshold is one. The strict comparison gives \(\widehat R_U(\widetilde h_D)<1\). Since \(\widehat R_U(c)\) is continuous and strictly decreasing, with its unique unit root at \(c=h_C\) [1, §3.1], it follows that \(h_C<\widetilde h_D\).

## Verification

Run `python verify_household.py` from the extracted directory using Python 3 and SymPy 1.14 (or a compatible version). The program checks a complete coefficient identity and the 406 nonnegative rational signs. An independent rational continuous-time Markov chain recurrence in `independent_dp.py` checks the four-household infection-count distribution and mean local outbreak sizes at \(\ell=1\), \(\pi=1/2\). The independently obtained distribution is

\[
(P_0,P_1,P_2,P_3,P_4)=(1/16,1/16,1/16,7/64,45/64),
\]

with \((\mu_1,\mu_2,\mu_3,\mu_4)=(1,3/2,13/6,143/48)\), giving the exact normalized gap \(D(1,1/2)=10262378043/68719476736>0\). That single test is only a cross-check; global positivity follows from the polynomial certificate, not sampling.

## Relationship to prior work

Theorem 4.11 of [1] proves \(\widetilde h_D>h_C\) for common household sizes two and three, and Conjecture 4.12 proposes the inequality for all sizes. Its Corollary 4.10 treats sufficiently small positive local contact rates, while the infinite-contact limit is covered separately. Neither statement implies the new \(n=4\) assertion for every finite rate. The source's Appendix B.3 explicitly proves only \(n=3\). Earlier work [2] develops household reproduction-number and critical-vaccination comparisons but does not compare these two *post-first-epidemic* four-person immunity distributions. The later multitype household framework [3] concerns branching approximations, final sizes and reproduction numbers, not the strict comparison here. Network-based herd-immunity comparisons [4] use different mixing geometry.

## Limitations

Only exponential infectious periods of mean one are proved, though the time unit can be rescaled. The conclusion applies to four-person households and finite positive local contact rates. It does not prove the general conjecture for non-Markovian infectious periods or other household sizes, nor equality or strictness at degenerate boundaries \(\ell=0\), \(\pi=0\), or \(\pi=1\). The proved herd-immunity ordering concerns \(\widetilde h_D\), not the true unrestricted disease-induced threshold \(h_D\). The novelty comparison relies on discoverable published literature and cannot exclude unpublished or unindexed equivalent statements.

## References

[1] F. Ball, L. Critcher, P. Neal, D. Sirl, “The impact of household structure on disease-induced herd immunity,” *Journal of Mathematical Biology* **87**, 83 (2023), published 2023-11-08, DOI: 10.1007/s00285-023-02010-7, https://link.springer.com/article/10.1007/s00285-023-02010-7.

[2] F. Ball, L. Pellis, P. Trapman, “Reproduction numbers for epidemic models with households and other social structures II: comparisons and implications for vaccination,” *Mathematical Biosciences* **274**, 108–139 (2016), DOI: 10.1016/j.mbs.2016.01.006, preprint https://arxiv.org/abs/1410.4469.

[3] F. Ball and L. Critcher, “Multitype SIR epidemics among a population partitioned into households with proportionate global mixing,” *Journal of Mathematical Biology* **92**, 77 (2026), DOI: 10.1007/s00285-026-02359-5, https://link.springer.com/article/10.1007/s00285-026-02359-5.

[4] T. Hiraoka et al., “Strength and weakness of disease-induced herd immunity in networks,” preprint arXiv:2307.04700 (2023), https://arxiv.org/abs/2307.04700.

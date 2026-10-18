# A unique finite peak in independence optimism for Beta-mixed majority juries

## Finding
For real parameters \(\alpha,\beta>0\), let a common latent per-voter competence \(P\) have the distribution \(\operatorname{Beta}(\alpha,\beta)\). Conditional on \(P\), the correctness indicators of any finite number of jurors are independent Bernoulli variables with success probability \(P\). Let \(C_r\) denote the probability of a correct strict-majority verdict from \(2r+1\) jurors, where \(r\) is any nonnegative integer.

Let \(\mu=\alpha/(\alpha+\beta)\), and let \(I_r\) denote the correct-majority probability for \(2r+1\) **unconditionally independent** Bernoulli voters with the same marginal competence \(\mu\). Set \(G_r=|I_r-C_r|\).

**Theorem.** If \(\alpha\ne\beta\), \(G_r\) has a finite unimodal sequence of values: it strictly increases from \(G_0=0\) to one maximizing index and strictly decreases thereafter, with the sole possible exception of a tie between exactly two consecutive maximizing indices. More precisely, writing \(s=\alpha+\beta\) and the rising factorial \((x)_k=\prod_{j=0}^{k-1}(x+j)\), define
\[
R_r=\frac{s^{2r+3}(\alpha)_{r+1}(\beta)_{r+1}}{(\alpha\beta)^{r+1}(s)_{2r+2}(s+2r+2)},\qquad r=0,1,2,\ldots.
\]
Then \(R_0<1\), the set \(\{r\ge0:R_r\ge1\}\) is a nonempty upper interval of integers, and
\[
r_*=\min\{r\ge0:R_r\ge1\}
\]
is the first maximizing index. It is the unique maximizer if \(R_{r_*}>1\); if \(R_{r_*}=1\), indices \(r_*\) and \(r_*+1\) alone maximize the gap. In either case \(G_r>0\) for all \(r\ge1\). If \(\alpha=\beta\), all \(G_r\) vanish identically.

In particular, the maximum optimism from incorrectly treating correlated voters as independent need **not** occur at the largest jury size. For \((\alpha,\beta)=(10,1)\), the unique maximum is attained by **five jurors**, even though the gap tends to a strictly positive limit as the jury grows.

## Assumptions and scope
The decision has one objectively correct binary outcome, jurors vote simultaneously and sincerely for what they individually judge correct, and the aggregation rule is unweighted strict majority with odd jury size. Dependence arises solely from a shared Beta-distributed latent competence, independently resampled across decision instances, with conditional independence of jury votes. There are no strategic effects, deliberation, or jury-size-dependent changes in \(\alpha\) or \(\beta\). The comparator uses **the same marginal voter correctness probability** but assumes unconditional independence. The result applies to all real positive shape parameters, not only integers.

## Proof
Define the usual binomial-majority polynomial
\[
h_r(p)=\sum_{k=r+1}^{2r+1}\binom{2r+1}{k}p^k(1-p)^{2r+1-k},\quad 0\le p\le1.
\]
Adding two voters changes the majority outcome only in the two borderline old-majority cases. A direct enumeration gives the exact step identity, for every \(r\ge0\):
\[
h_{r+1}(p)-h_r(p)=\binom{2r+1}{r}p^{r+1}(1-p)^{r+1}(2p-1).
\]
Thus \(I_r=h_r(\mu)\) and \(C_r=\mathbb E[h_r(P)]\). Using Beta moments and \(\mathbb E[2P-1]\) under the beta density tilted by \(P^{r+1}(1-P)^{r+1}\), we obtain the successive gains
\[
I_{r+1}-I_r=\binom{2r+1}{r}\frac{(\alpha\beta)^{r+1}(\alpha-\beta)}{s^{2r+3}},
\]
\[
C_{r+1}-C_r=\binom{2r+1}{r}\frac{(\alpha)_{r+1}(\beta)_{r+1}(\alpha-\beta)}{(s)_{2r+2}(s+2r+2)}.
\]
For \(\alpha\ne\beta\), both gains have the same nonzero sign, and their positive ratio is exactly \(R_r\) displayed above. Put \(D_r=I_r-C_r\) and \(\varepsilon=\operatorname{sgn}(\alpha-\beta)\). Since \(D_0=0\),
\[
\varepsilon(D_{r+1}-D_r)=|I_{r+1}-I_r|(1-R_r).
\]
The signs of these increments determine the variation of \(H_r=\varepsilon D_r\). Direct cancellation yields
\[
R_0=\frac{s^2}{(s+1)(s+2)}<1,\qquad
\frac{R_{r+1}}{R_r}=\frac{s^2(\alpha+r+1)(\beta+r+1)}{\alpha\beta(s+2r+3)(s+2r+4)}.
\]
Set \(t=r+1\). The numerator of the last quotient minus its positive denominator is the quadratic
\[
F(t)=(\alpha-\beta)^2t^2+[s^3-\alpha\beta(4s+6)]t-\alpha\beta(3s+2).
\]
Since \(\alpha\ne\beta\), the leading coefficient is positive and the constant is negative. The product of its roots is negative; therefore it has exactly one positive real root, with \(F(t)<0\) below it and \(F(t)>0\) above it for \(t>0\). Consequently the positive sequence \(R_r\) first weakly decreases and then increases; a single equal consecutive pair is possible at its valley. Because \(R_0<1\), it **cannot** meet or cross 1 during the initial nonincreasing portion.

Moreover,
\[
\lim_{r\to\infty}\frac{R_{r+1}}{R_r}=\frac{(\alpha+\beta)^2}{4\alpha\beta}>1,
\]
so \(R_r\) eventually grows geometrically without bound. There is hence exactly one first index \(r_*\) with \(R_{r_*}\ge1\). Before that index the increments of \(H_r\) are strictly positive, and after it strictly negative, apart from an exactly zero increment at \(r_*\) if \(R_{r_*}=1\). This proves the claimed single peak or adjacent tie for \(H_r\).

It remains to identify \(G_r\) with \(H_r\), rather than only with its absolute value. For \(\alpha>\beta\), the strong law conditional on \(P\), then bounded convergence and the continuity of the Beta density, give \(I_r\to1\) and \(C_r\to\Pr(P>1/2)<1\). Thus \(H_r\to1-\Pr(P>1/2)>0\). For \(\alpha<\beta\), \(I_r\to0\), \(C_r\to\Pr(P>1/2)>0\), and again \(H_r\) has a strictly positive limit. The just-proved increase-then-decrease pattern from \(H_0=0\), together with a positive limiting value, ensures \(H_r>0\) for every \(r\ge1\). Hence \(G_r=H_r\) for all \(r\), completing the proof. Finally, if \(\alpha=\beta\), the Beta mixing distribution is symmetric and \(\mu=1/2\); both majority accuracies equal \(1/2\) for all odd sizes.

## Verification
The self-contained standard-library program `verify_jury_beta.py` recomputes the independent binomial and beta-binomial majority sums as exact rational numbers. It checks the closed-form successive-gain ratio and its recurrence over 336 nontrivial combinations of shape parameters and jury increments, as well as symmetry cases. It also checks the explicit \((10,1)\) example. Execute `python verify_jury_beta.py` from the same directory as this document.

For that example the gap is \(G_1=525/34606\) at three jurors, and \(G_2=226461/14655641\) at five jurors, with \(G_0=0<G_1<G_2>G_3>G_4>\cdots\). The proof of the global statement is algebraic; finite computation provides only additional checks.

## Relationship to prior work
Classical Condorcet voting analysis and correlated-vote extensions establish how the correctness probability can depend on panel size and dependence. In particular, Kaniovski's published analysis of alternative correlated binary-vote joint distributions and Kaniovski–Zaigraev's homogeneous-jury voting-quota results concern a **second-order Bahadur joint-law truncation**, with higher-order correlations constrained differently from the Beta-mixture law. Those results do not supply the displayed Beta-mixture sequence ratio, its one-valley property, or the finite worst-size classification. Berend and Sapir study beneficial augmentation of dependent juries rather than the difference between one fixed Beta-mixture majority accuracy and its equal-marginal independent surrogate. Ladha's de Finetti-based jury theorem and Berg's dependent-jury analysis provide closer general context; their complete texts were not available for comparison, so an equivalent specialized statement cannot be categorically ruled out. The established fact that positive dependence may reduce majority accuracy is not claimed as new.

## Limitations
The exact one-peak law is specific to Beta mixing with exchangeable conditional Bernoulli votes, a fixed latent distribution across jury sizes, odd simple-majority aggregation, and an equal-marginal independent comparator. It need not hold for arbitrary exchangeable mixtures, heterogeneous marginals, adaptive voters, or strategic election mechanisms. The result is not an empirical claim about actual jury competence; full comparison to all historical voting-theory papers remains incomplete. Individual shape parameters can make the peak occur at very large jury sizes, so an exact index may be computationally costly to find even though the recurrence terminates in principle.

## References
1. Kaniovski, S., and Zaigraev, A. *Optimal jury design for homogeneous juries with correlated votes*. Theory and Decision 71, 439–459 (2011), first published online 30 July 2009. https://doi.org/10.1007/s11238-009-9170-2
2. Kaniovski, S. *Aggregation of correlated votes and Condorcet's Jury Theorem*. Theory and Decision 69, 453–468 (2010). https://doi.org/10.1007/s11238-008-9120-4 ; openly available author text https://serguei.kaniovski.wifo.ac.at/fileadmin/pdf/condorcet.pdf
3. Berend, D., and Sapir, L. *Monotonicity in Condorcet's Jury Theorem with dependent voters*. Social Choice and Welfare 28, 507–528 (2007). https://doi.org/10.1007/s00355-006-0179-y
4. Ladha, K. K. *Condorcet's jury theorem in light of de Finetti's theorem: Majority-rule voting with correlated votes*. Social Choice and Welfare 10, 69–85 (1993); working paper record https://econpapers.repec.org/paper/fthwaslbp/157.htm
5. Berg, S. *Condorcet's jury theorem, dependency among jurors*. Social Choice and Welfare 10, 87–95 (1993). https://doi.org/10.1007/BF00187435

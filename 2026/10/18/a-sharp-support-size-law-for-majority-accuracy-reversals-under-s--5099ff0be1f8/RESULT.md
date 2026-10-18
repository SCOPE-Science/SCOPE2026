# A sharp support-size law for majority-accuracy reversals under shared information

## Finding

An exchangeable electorate can alternately gain and lose accuracy when two voters are added, even when each voter's unconditional correctness exceeds one half. The number of such changes is controlled exactly by the number of effectively distinct latent variability levels, not by the total number of voters.

Let \(P\) be a random conditional probability of casting a correct binary judgment, taking finitely many values strictly between zero and one. Given \(P\), all individuals vote correctly independently with probability \(P\). With \(2r+1\) voters, let \(J_r\) denote the probability of a correct strict-majority decision. For each latent state \(p_i\) with positive weight \(w_i\), set \(\lambda_i=p_i(1-p_i)\). Combine states having the same \(\lambda_i\) into coefficients \(a_\lambda=\lambda\sum_{i:\lambda_i=\lambda}w_i(2p_i-1)\). Discard coefficients equal to zero and let \(d\) be the number remaining.

**Sharp switching law.** If \(d\ge1\), then, after zeros are omitted, the sequence \(J_{r+1}-J_r\) changes sign at most \(d-1\) times as \(r=0,1,2,\ldots\). If \(d=0\), all these increments vanish. The bound is attainable for every integer \(d\ge2\), with positive dependence among voters, unconditional voter correctness above one half, and latent states favoring correctness carrying more than one-half of all mixing probability.

## Assumptions and scope

There is a single objectively correct alternative in each binary decision. A latent environment \(P\in(0,1)\) is sampled once per decision, shared by all jurors, and its distribution is supported on finitely many points. Given \(P\), all correct-vote indicators are independent Bernoulli variables with parameter \(P\). Sincere choices and strict-majority aggregation are assumed. Jury sizes compared are precisely \(2r+1\) and \(2r+3\), for integers \(r\ge0\). Unconditional independence is not assumed, and latent competence may lie below one half in some environments.

A **sign reversal** is an adjacent reversal in the sign sequence obtained by deleting zero entries from \((J_{r+1}-J_r)_{r\ge0}\). This definition does not count zero-valued plateaus as additional reversals. A tie in the variability parameters \(\lambda_i\) may cancel; hence the effective count \(d\) is at most the number of states.

## Proof

**Step 1: Exact marginal-jury identity.** Condition on \(P=p\), put \(n=2r+1\), and compare an odd jury with two additional independent voters. A formerly incorrect majority can be corrected only when precisely \(r\) of the original \(n\) are correct and both new votes are correct. A formerly correct majority can become incorrect only when precisely \(r+1\) of the old jury are correct and both new votes are incorrect. Subtracting these two disjoint events gives

\[
\Pr(M_{2r+3}\mid P=p)-\Pr(M_{2r+1}\mid P=p)
=\binom{2r+1}{r}(2p-1)[p(1-p)]^{r+1}.
\]

Consequently

\[
J_{r+1}-J_r=\binom{2r+1}{r}\sum_{\lambda}a_\lambda\lambda^r,
\qquad
 a_\lambda=\lambda\sum_{i:\lambda_i=\lambda}w_i(2p_i-1).
\]

The binomial factor is strictly positive. If every coefficient is zero, the sequence is constant, proving the \(d=0\) case.

**Step 2: At most \(d-1\) reversals.** With the effective, distinct positive parameters ordered as \(0<\lambda_1<\cdots<\lambda_d\), consider the real exponential polynomial

\[
f(x)=\sum_{i=1}^{d}a_i e^{x\log\lambda_i}.
\]

It has at most \(d-1\) distinct real zeros. For completeness, divide by the first exponential and differentiate. The derivative is a linear combination of \(d-1\) distinct exponentials with nonzero coefficients; the assertion follows by induction from Rolle's theorem: if \(f\) had \(d\) distinct zeros, the differentiated quotient would have at least \(d-1\) distinct zeros, contradicting the induction hypothesis for \(d-1\) terms. The base case is a nonzero single exponential, which has no zeros. Every strict sign reversal among samples \(f(0),f(1),\ldots\), ignoring samples equal to zero, forces a separate real zero between consecutive nonzero samples of opposite sign. Hence there can be at most \(d-1\) reversals.

**Step 3: Attainment for every \(d\ge2\).** Fix \(0<t<1/2\) and introduce

\[
Q_d(z)=z\prod_{j=0}^{d-2}(z-t^{2j+3})=\sum_{i=1}^{d}c_i z^i.
\]

All \(c_i\) are nonzero and alternate in sign because every elementary symmetric function of the positive root parameters is strictly positive. Set \(\lambda_i=t^{2i}\), \(\delta_i=\sqrt{1-4t^{2i}}>0\), and choose

\[
p_i=\frac{1+\operatorname{sgn}(c_i)\delta_i}{2},\qquad
W=\sum_{i=1}^{d}\frac{|c_i|}{\delta_i},\qquad
w_i=\frac{|c_i|}{W\delta_i}.
\]

These are legitimate pairwise-distinct competence states in \((0,1)\) with positive weights summing to one, and satisfy \(p_i(1-p_i)=\lambda_i\) and \(w_i(2p_i-1)=c_i/W\). Thus the exact increment identity becomes

\[
J_{r+1}-J_r=\frac{\binom{2r+1}{r}}{W}Q_d(t^{2r+2}).
\]

For each \(j=0,\ldots,d-2\), the root \(t^{2j+3}\) lies strictly between consecutive arguments \(t^{2j+2}\) and \(t^{2j+4}\). Hence the first \(d\) increments have strictly alternating signs and give \(d-1\) reversals. Step 2 proves that there can be no others.

**Step 4: Competence and dependence.** With \(d\) fixed and \(t\downarrow0\), the polynomial tends coefficientwise to \(z^d\), so \(c_d=1\), whereas each other coefficient tends to zero. Hence \(w_d\to1\), \(p_d\to1\), and therefore \(\sum_iw_ip_i\to1\) and \(\Pr(P>1/2)\to1\). For sufficiently small positive \(t\), both exceed one half. For distinct latent states, the correct-vote indicators have covariance \(\operatorname{Var}(P)>0\), proving strict positive pairwise correlation despite alternating jury accuracy.

## Verification

The accompanying `verify.py` uses only the Python standard library. It checks exact rational expansions of \(Q_d\), strict alternating signs at the first \(d\) sampled arguments, and the exact \(d-1\) reversal counts for all integers \(2\le d\le15\). It also checks a concrete three-state example through independently computed conditional binomial majority probabilities at 100-digit decimal precision. These finite checks corroborate the algebra but are not used as a proof of the real-zero bound or the unbounded family.

For \(d=3\) and \(t=1/3\),

\[
Q_3(z)=z^3-\frac{10}{243}z^2+\frac{z}{6561}.
\]

The exact first three signs are represented by

\[
Q_3(1/9)=\frac{52}{59049}>0,\quad
Q_3(1/81)=-\frac4{1594323}<0,\quad
Q_3(1/729)=\frac{52}{387420489}>0.
\]

Thus additions of two jurors first help, then hurt, then help again; the general theorem rules out a third reversal for this mixture.

## Relationship to prior work

The classical Condorcet jury theorem treats independent voters with positive competence. Dietrich and Spiekermann (MPRA:40135; publicly deposited 18 July 2012) treat correlated interchangeable votes using de Finetti's representation and formulate conditions for monotonicity in jury size. Kaniovski and Zaigraev analyze homogeneous correlated jury design under a correlation-parametrized family, and Kaniovski studies other correlated-vote distributions and their majority probabilities. None of the examined complete texts establishes this exact finite-support bound or the arbitrary-reversal construction.

Berend and Sapir (2007) treat dependent-voter beneficial subcommittee augmentation, and their abstract describes necessary and sufficient comparisons. Their full article was not accessible during the review; it remains a material possible source of stronger or equivalent coverage. The present theorem is not a claim that the classical mixed-binomial marginal identity or the general exponential-polynomial zero count is new individually. Its claimed contribution is the sharp, attainable and competence-compatible implication for the finite-support correlated-jury model.

## Limitations

Finite support is essential to the stated count. The statement does not bound oscillations under arbitrary continuous mixing distributions, strategic voting, non-exchangeable networks, or unmodeled state-dependent incentives. It concerns the signs of successive odd-jury *incremental* gains, not maximum accuracy or costs of forming a jury. The construction uses finely tuned shared-environment mixture weights and some hostile-competence environments; positive unconditional competence does not imply uniformly competent latent states. A full historical bibliographic check, especially of Berend and Sapir (2007), remains desirable.

## References

- Dietrich, F. and Spiekermann, K. *Epistemic Democracy with Defensible Premises*. MPRA Paper 40135 (public deposit 18 July 2012). https://mpra.ub.uni-muenchen.de/40135/1/MPRA_paper_40135.pdf
- Kaniovski, S. *Aggregation of Correlated Votes and Condorcet's Jury Theorem*. Accessible author manuscript. https://serguei.kaniovski.wifo.ac.at/fileadmin/pdf/condorcet.pdf
- Kaniovski, S. and Zaigraev, A. *Optimal Jury Design for Homogeneous Juries with Correlated Votes*, Theory and Decision **71** (2011), 439–459, DOI:10.1007/s11238-009-9170-2. Accessible workshop version: https://www.lse.ac.uk/cpnss/assets/documents/voting-power-and-procedures/workshops/2011/Kaniovski-Paper.pdf
- Berend, D. and Sapir, L. *Monotonicity in Condorcet's Jury Theorem with Dependent Voters*, Social Choice and Welfare **28** (2007), 507–528, DOI:10.1007/s00355-006-0179-y (full text not inspected).

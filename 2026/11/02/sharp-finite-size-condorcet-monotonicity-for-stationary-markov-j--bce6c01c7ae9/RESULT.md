# Sharp finite-size Condorcet monotonicity for stationary Markov juries

## Finding

Let \((X_i)_{i\in\mathbb Z}\) be a stationary binary first-order Markov chain, with \(X_i=1\) representing a correct vote, and with transition matrix (rows and columns indexed by \(0,1\))
\[
P=\begin{pmatrix}1-s&s\\t&1-t\end{pmatrix},\qquad 0<s,t<1.
\]
For every integer \(m\ge0\), put
\[
J_m=\Pr\!\left\{\sum_{i=1}^{2m+1}X_i\ge m+1\right\},\qquad
G_m=\Pr\!\left\{X_0=X_{2m+2}=1,\ \sum_{i=1}^{2m+1}X_i=m\right\}.
\]
Then the **exact finite-size increment** is
\[
\boxed{J_{m+1}-J_m=\frac{s-t}{s}\,G_m.}
\]
Moreover \(G_m>0\) for every \(m\). Consequently, the majority-correctness probability of consecutive odd-size committees is strictly increasing for every size if \(s>t\), exactly \(1/2\) for every size if \(s=t\), and strictly decreasing for every size if \(s<t\). These conditions are equivalent to stationary individual competence being greater than, equal to, or less than \(1/2\), respectively.

Furthermore, as \(m\to\infty\), \(J_m\to1\) when \(s>t\) and \(J_m\to0\) when \(s<t\). The result holds for both positive and negative serial correlation; no independence or exchangeability of the votes is assumed.

## Assumptions and scope

The correct answer to a fixed binary question is held constant, and each voter votes sincerely according to a joint law modeled by a **stationary**, time-homogeneous, two-state first-order Markov chain. The same law governs all finite contiguous committees of sizes \(1,3,5,\ldots\); odd sizes ensure ties cannot occur. Both transition probabilities \(s\) and \(t\) belong to the open unit interval. No assertion is made for nonstationary initial states, arbitrary higher-order dependence, changing transition laws with committee size, or strategic voting.

The unique stationary distribution is \(\pi_0=t/(s+t)\) and \(\pi_1=s/(s+t)\). In particular, every juror has competence \(p=s/(s+t)\), and the lag-one Pearson correlation of votes is \(\rho=1-s-t\). Either sign of \(\rho\) is admissible, including zero.

## Proof

**1. Compare nested stationary windows.** For fixed \(m\ge0\), let \(Y=(X_1,\ldots,X_{2m+1})\). By stationarity, the middle-window majority event \(\sum Y_i\ge m+1\) has probability \(J_m\), and the enlarged-window majority event \(X_0+\sum Y_i+X_{2m+2}\ge m+2\) has probability \(J_{m+1}\). Subtracting indicators, every sequence cancels except two disjoint configurations:
\[
G_m=\{X_0=X_{2m+2}=1,\ \sum Y_i=m\},\qquad
L_m=\{X_0=X_{2m+2}=0,\ \sum Y_i=m+1\}.
\]
Thus \(J_{m+1}-J_m=\Pr(G_m)-\Pr(L_m)\).

**2. Compare individual finite-path weights.** Each path in \(G_m\) has length \(2m+3\), begins and ends in state \(1\), and contains \(m+2\) ones and \(m+1\) zeros. Write \(N_{ab}\) for its number of successive \(a\)-to-\(b\) transitions. Beginning and ending in state \(1\) implies \(N_{01}=N_{10}\). Counting outgoing transitions from the two states also gives \(N_{11}=N_{00}\): indeed \(N_{11}+N_{10}=m+1\) and \(N_{00}+N_{01}=m+1\).

Bitwise complementation bijects such paths with paths in \(L_m\). It interchanges \(N_{00}\) and \(N_{11}\), and interchanges \(N_{01}\) and \(N_{10}\), so these four equalities make the Markov **transition products identical** for each path and its complement. The path's initial stationary probability, however, changes from \(\pi_1=s/(s+t)\) to \(\pi_0=t/(s+t)\). Therefore, path by path,
\[
\Pr(X_0=x_0,\ldots,X_{2m+2}=x_{2m+2})
=\frac{s}{t}\Pr(X_0=1-x_0,\ldots,X_{2m+2}=1-x_{2m+2})
\]
whenever \(x\in G_m\). Summing the bijection yields \(\Pr(G_m)=(s/t)\Pr(L_m)\), and therefore
\[
J_{m+1}-J_m=\Pr(G_m)-\frac ts\Pr(G_m)
=\frac{s-t}{s}\,G_m.
\]

**3. Strict sign and limiting accuracy.** Every transition and both stationary probabilities are strictly positive, so \(G_m>0\) for each finite \(m\). The sign is hence precisely the sign of \(s-t\). Stationarity gives \(p=s/(s+t)\); thus \(\operatorname{sgn}(p-1/2)=\operatorname{sgn}(s-t)\). In the equality case \(s=t\), bitwise complementation preserves all finite-word weights, so every odd-length majority has probability exactly \(1/2\). Since the positive-transition finite-state chain is irreducible and aperiodic, the Markov-chain ergodic theorem gives \((2m+1)^{-1}\sum_{i=1}^{2m+1}X_i\to p\) almost surely. For \(p>1/2\), eventually a correct majority occurs with probability tending to one; for \(p<1/2\), its probability tends to zero. This completes the proof for every specified committee size and parameter pair.

## Verification

The accompanying standalone Python script `check_markov_jury.py` uses only the standard library, especially exact rational arithmetic. It independently evaluates majority probabilities by full path enumeration and by a count-and-last-state dynamic program. For eight rational parameter pairs, including positive, negative and zero correlation and all three competence signs, it compares each \(1\)-through-\(11\)-voter majority calculation, the exact pivotal-event identity, and each path/complement probability ratio. It additionally checks an explicit anti-correlated example. The script completed with **1043 passed exact assertions**.

For \(s=9/10\) and \(t=3/5\), the stationary competence is \(p=3/5\), but the adjacent-vote correlation is \(\rho=-1/2\). Nevertheless, the successive exact majority accuracies for committee sizes \(1,3,5,7,9\) are
\[
\frac35,\quad\frac{177}{250},\quad\frac{9687}{12500},\quad
\frac{102621}{125000},\quad\frac{5342487}{6250000}.
\]
Finite checks are not presented as a proof for arbitrary size. That proof is the pathwise bijection and ergodic argument above.

Run `python3 check_markov_jury.py` with Python 3.8 or newer. No third-party modules, external data, or network access are necessary.

## Relationship to prior work

Condorcet's classical jury theorem assumes independent equally competent votes. Berend and Sapir's 2005 study proves nonasymptotic monotonicity for randomly chosen subcommittees in an independent-vote model. Their 2007 follow-up considers random subcommittees with dependent heterogeneous experts, and is a particularly plausible historical overlap; the full 2007 article was not accessible for a decisive theorem-by-theorem comparison. It cannot be ruled out that its general criteria can yield this specialization, although the available description does not state the stationary-Markov, all-odd-size strict sign law or the pivotal-probability identity.

Kaniovski's 2007 conference manuscript (subsequently published in 2010) establishes jury-size comparisons for several specially constructed **homogeneous equicorrelated** voting distributions, where all distinct voter pairs have the same correlation. In the present stationary Markov model, the lag-\(k\) correlation is \(\rho^k\), generally depending on separation; moreover both positive and negative serial dependence obey the same sharp competence sign rule. The equicorrelated results therefore cannot be directly substituted for the present chain law.

Xia and Zhang's Markov-binomial distribution study concerns exactly the same count object (the number of ones in a two-state Markov sequence), but derives approximation theorems, not the nonasymptotic strict-majority increment identity. Zaigraev and Kaniovski's correlated-binary-trials formulas use a second-order truncation of the Bahadur expansion and an equicorrelation assumption; that is not the general exact Markov path measure. Peleg and Zamir's dependent-jury work and Pivato's correlated-voter work focus on broad conditions for asymptotic competence and strategic considerations rather than this finite-size Markov classification.

## Limitations

The result is a precise consequence of a stationary two-state first-order Markov model; that model may not capture real-world deliberation, heterogeneity, common evidence or strategic feedback. There is no claim that voter dependence is generally harmless: nonlinear or nonstationary dependence can invalidate finite-size monotonicity. The strict sign law does not quantify rates of approach to accuracy one or zero beyond the exact pivotal-event identity. Historical originality has not received an independent literature audit, and the inaccessible 2007 dependent-subcommittee work remains a concrete priority risk.

## References

- D. Berend and L. Sapir, *Monotonicity in Condorcet Jury Theorem*, Social Choice and Welfare **24** (2005), 83–92, https://doi.org/10.1007/s00355-003-0293-z.
- D. Berend and L. Sapir, *Monotonicity in Condorcet's Jury Theorem with dependent voters*, Social Choice and Welfare **28** (2007), 507–528, https://doi.org/10.1007/s00355-006-0179-y.
- S. Kaniovski, *Aggregation of Correlated Votes and Condorcet's Jury Theorem*, author manuscript dated 2007-11-25, https://www.accessecon.com/pubs/scw2008/generalpdfscw2008/scw2008-08-00027s.pdf; published in Theory and Decision **69** (2010), 453–468.
- A. Xia and M. Zhang, *On approximation of Markov binomial distributions*, Bernoulli **15** (2009), 1335–1350, https://doi.org/10.3150/09-BEJ194, https://arxiv.org/abs/1001.2144.
- A. Zaigraev and S. Kaniovski, *A note on the probability of at least k successes in n correlated binary trials*, manuscript dated 2012-09-05, https://serguei.kaniovski.wifo.ac.at/fileadmin/pdf/corr_binom_01.pdf; Operations Research Letters **41** (2013), 116–120.
- B. Peleg and S. Zamir, *Extending the Condorcet Jury Theorem to a general dependent jury*, Social Choice and Welfare **39** (2012), 91–125, https://doi.org/10.1007/s00355-011-0546-1.
- M. Pivato, *Epistemic democracy with correlated voters*, MPRA Paper 69546 (2016), https://mpra.ub.uni-muenchen.de/69546/.

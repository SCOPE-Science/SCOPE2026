# An exact quartic residual-risk law for first-choice-only instant-runoff polls

## Finding

In a three-candidate instant-runoff election with potentially truncated ballots, a first-choice-only poll can leave a strictly positive, exactly computable uncertainty about the winner even when the poll becomes arbitrarily large. Under an independent flat Dirichlet prior over all fifteen nonempty ordered ballots, fix distinct first-choice population shares \(a>b>c>0\) with \(a+b+c=1\) and define \(\delta=(a-b)/c\). The conditional probability that the plurality runner-up \(B\) defeats the plurality leader \(A\) is exactly

\[
Q(a,b,c)=\begin{cases}
\tfrac12(1-\delta)^3(1+\delta),&0<\delta<1,\\
0,&\delta\ge1.
\end{cases}
\]

The plurality leader is therefore the unique Bayes-optimal winner prediction under zero-one loss (away from first-choice ties), and its exact conditional classification error is \(Q\). If the first-choice proportions satisfy \(a<1/2\), then \(0<\delta<1\) and \(Q>0\), so learning first choices perfectly does not identify the eventual winner. At the majority frontier, \(Q\sim(1-\delta)^3\) as \(\delta\uparrow1\).

The same expression is the limiting posterior probability of a victory by \(B\) for a sequence of first-choice-only polls with count proportions converging to \((a,b,c)\), when the Dirichlet model and its fixed prior are retained.

For comparison, if only the six complete rankings are permitted and the flat Dirichlet prior is instead imposed on those six types, the corresponding runner-up winning probability is \(\tfrac12(1-\delta)\) for \(0<\delta<1\). The comparison concerns two different ballot spaces and hence different priors; it is not a causal or prior-free assertion about ballot truncation.

## Assumptions and scope

There are exactly three candidates \(A,B,C\). Voters may submit any nonempty strict ordering of one, two, or all three candidates; there are exactly fifteen admissible ballot types. Their population fractions have the prior \(\operatorname{Dirichlet}(1,\ldots,1)\), with one unit parameter for each ballot type. First-choice-only observations record the top-ranked candidate but not other ranks or ballot length. The eventual instant-runoff winner is computed from the population ballot-type proportions with exhausted ballots removed after the associated choices are eliminated. Exact population-level ties have prior probability zero. The conditional formulas use the continuous regular conditional kernel for shares strictly ordered as \(a>b>c>0\).

No assertion about real-world voter preferences is made absent the specified prior, independence model, or permitted ballot space. The posterior limit assumes the number of polled voters tends to infinity and the first-choice frequencies have the indicated limit.

## Proof

**1. Conditioning and transfer law.** For each ballot type \(s\), let \(G_s\) be independent unit-rate exponential random variables and set \(\pi_s=G_s/\sum_t G_t\). This is the fifteen-dimensional flat Dirichlet distribution. There are five admissible types beginning with each first-choice candidate. Consequently their totals \((P_A,P_B,P_C)\) have the distribution \(\operatorname{Dirichlet}(5,5,5)\). The normalized component vector inside each first-choice group is independent of the group totals, by the independent-gamma representation.

The five types beginning with \(C\) are \(C\), \(CA\), \(CB\), \(CAB\), and \(CBA\). If \(C\) is eliminated, \(CA\) and \(CAB\) transfer to \(A\); \(CB\) and \(CBA\) transfer to \(B\); and \(C\) exhausts. Denote their fractions *within the first-choice-\(C\) group* by \(U_A,U_B,U_E\). Independent gamma additivity gives

\[
(U_A,U_B,U_E)\sim\operatorname{Dirichlet}(2,2,1),
\]

independent of \((P_A,P_B,P_C)\). Hence this transfer law remains valid after conditioning on any interior first-choice share vector \((a,b,c)\).

**2. Exact difference density.** The joint density of \((U_A,U_B)\) on the triangle \(u,v\ge0\), \(u+v\le1\), is \(24uv\). Set \(D=U_B-U_A\) and \(T=U_A+U_B\). The absolute Jacobian is \(1/2\), so for \(-1<d<1\),

\[
f_D(d)=3\int_{|d|}^1(t^2-d^2)\,dt
=1-3d^2+2|d|^3.
\]

This nonnegative symmetric density integrates to one. When \(a>b>c\), candidate \(C\) is eliminated first. The final difference \(B-A\) equals \(b-a+cD\), and \(B\) wins precisely when \(D>\delta=(a-b)/c\). For \(0<\delta<1\),

\[
\Pr(D>\delta)=\int_{\delta}^1(1-3d^2+2d^3)\,dd
=\tfrac12-\delta+\delta^3-\tfrac12\delta^4
=\tfrac12(1-\delta)^3(1+\delta).
\]

For \(\delta\ge1\), the event is impossible. Since \(a+b+c=1\), \(\delta<1\) is equivalent to \(a<1/2\). If \(a\ge1/2\), the majority candidate \(A\) is the instant-runoff winner immediately, also yielding probability zero for \(B\). For \(0<\delta<1\), the displayed expression lies strictly between zero and one half. Thus \(A\) is the Bayes-optimal zero-one classifier and its error probability is \(Q\). The cubic asymptotic follows directly from the factorization.

**3. First-choice-only posterior and irreducible uncertainty.** Suppose a poll records first-choice counts \(n_A,n_B,n_C\), with total \(N\). As its likelihood is proportional to \(P_A^{n_A}P_B^{n_B}P_C^{n_C}\), the posterior group totals are

\[
(P_A,P_B,P_C)\mid(n_A,n_B,n_C)
\sim\operatorname{Dirichlet}(n_A+5,n_B+5,n_C+5).
\]

The within-group Dirichlet vectors, in particular \((U_A,U_B,U_E)\), retain their prior laws and their independence from the group totals. If \(n_i/N\to(a,b,c)\) with \(a>b>c>0\), the posterior group totals converge in probability to \((a,b,c)\) by the Dirichlet moment formulas. The posterior probability of any first-round elimination other than \(C\) tends to zero, and conditional runoff tie events have probability zero. Taking expectations of the bounded winner indicator gives the asserted limit by dominated convergence (or the continuous mapping theorem away from the null tie surface). It equals \(Q\) and is positive whenever \(a<1/2\).

**4. Complete-ranking comparator.** If the ballot universe consists only of the six full rankings and the prior is flat on those six types, the two types beginning with \(C\) transfer to \(A\) or \(B\) with proportions \((1-U,U)\sim\operatorname{Dirichlet}(1,1)\). Hence \(B\) wins iff \(U>(1+\delta)/2\), an event of probability \((1-\delta)/2\) for \(0<\delta<1\). The distinction is driven by the explicitly different ballot-type model.

## Verification

The accompanying standalone `check.py` verifies the exact polynomial identity and relevant bounds over hundreds of rational \(\delta\) values, checks normalization of the derived density exactly, and independently samples five unit-exponential weights to reproduce the predicted posterior tail at three benchmark gaps. Run it using `python check.py`. These computational checks are diagnostics only; the proof for all admissible shares is the integration and Dirichlet aggregation above.

For example, with \((a,b,c)=(0.42,0.33,0.25)\), \(\delta=0.36\) and the conditional probability of a runner-up victory is \(0.17825792\). It does not shrink as the number of first-choice-only responses grows if their limiting shares remain those values.

## Relationship to prior work

Rosenman and Liang (2026, arXiv:2606.31022) formulate the full ballot-type Dirichlet model for ranked-choice polling, expressly enumerate the fifteen possible three-candidate truncated ballots, advocate a flat prior, and compute winner probabilities by posterior simulation. Their Sections 2.1, 4.2, 4.5, and 4.6 were inspected. The present result conditions on *first-choice-only* information, deriving a closed exact conditional risk and an infinite-poll nonidentification limit rather than reproducing their simulation method or its full-ranking poll conclusions.

Classical analyses of plurality/instant-runoff winner disagreement under random ranking models, including the three-candidate probability catalog at RangeVoting.org, address unconditional frequencies under different ballot universes. They do not specify this fifteen-category, first-choice-conditional posterior quartic. Dirichlet aggregation and finite-dimensional polynomial integration are standard techniques and are not themselves claimed as new.

## Limitations

The uniform fifteen-type prior is a modeling choice and is not invariant to merging or splitting ballot categories. The computed probability is conditional Bayesian risk, not a distribution-free statement about the chance of an electoral upset. The result concerns exactly three candidates, first-choice-only data, independent sampling under the stated model, and strict first-choice ordering. It does not supply a finite-poll closed form after integrating uncertainty in the three first-choice totals; the general finite-poll posterior can still be evaluated by numerical integration. Equivalence to unindexed published formulas cannot be ruled out by the searches conducted.

## References

1. Evan T. R. Rosenman and Jason Liang, *Bayesian Uncertainty Quantification for Ranked Choice Voting Polls*, arXiv:2606.31022, first posted 2026-06-30. https://arxiv.org/abs/2606.31022.
2. Warren D. Smith, *IRV Paradox Probabilities in 3-candidate elections — Master List*, RangeVoting.org, https://www.rangevoting.org/IrvParadoxProbabilities.html (accessed 2026-10-24). This is comparison literature about unconditional random-election frequencies, not a source for the new formula.

# Three patches sharply identify the severity and rate of synchronized partial habitat catastrophes

## Finding

Consider a finite collection of at least three exchangeable habitat patches, observed at stationarity with perfect occupancy detection. Empty patches colonize independently at rate \(a>0\), occupied patches go locally extinct at rate \(b>0\), and a common Poisson catastrophe process of rate \(c>0\) independently clears each occupied patch with probability \(q\in(0,1]\) at each event. Let \(p_j\) be the stationary probability that \(j\) *specified distinct* patches are all occupied (not the probability that exactly \(j\) patches are occupied), for \(j=1,2,3\).

**Exact inverse and sharp sample-size theorem.** Three simultaneous patch occupancy indicators identify the ratios \(a/(a+b)\) and \(c/(a+b)\), and the severity \(q\), uniquely. Write

\[
 m=p_1,\qquad A=1-\frac{p_1^2}{p_2},\qquad B=1-\frac{p_1p_2}{p_3}.
\]

Then the unique reconstruction is

\[
 q=3-\frac{3B}{2A},\qquad
 s=\frac{2A}{q},\qquad
 \frac{a}{a+b}=\frac{m}{1-s},\qquad
 \frac{c}{a+b}=\frac{s}{q(1-s)}.
\]

A positive triple \((p_1,p_2,p_3)\) is realizable by this model for any prescribed number of patches at least three **if and only if**

\[
 0<m<1,\quad A>0,\quad \frac43\le\frac BA<2,\quad
 0<\frac{2A}{q}<1-m,
 \qquad q=3-\frac{3B}{2A}.
\]

The inequalities characterize the complete feasible three-patch observation domain, not merely a necessary moment restriction. With one or two patches, the same static experiment does *not* identify severity and event rate separately: every admissible two-patch law belongs to a nontrivial continuum of parameter ratios. Three is the sharp minimum. Absolute rates remain unidentifiable under a common rescaling of time.

In the physically meaningful coordinates \(x=a/(a+b)\), \(s=cq/(a+b+cq)\), and \(q\), the Jacobian of the forward map to \((p_1,p_2,p_3)\) is

\[
 \det\frac{\partial(p_1,p_2,p_3)}{\partial(x,s,q)}
 =-\frac{x^5s(1-s)^6q^2}
 {6(1-sq/2)^3[1-s(q-q^2/3)]^2}<0.
\]

Thus the inverse is regular throughout the interior, but its local sensitivity necessarily degenerates quadratically as \(q\downarrow0\) with \(s\) held fixed.

## Assumptions and scope

For every integer \(N\ge3\), the state is \(X(t)\in\{0,1\}^N\), where one means occupied. All patches have identical rates, there are no dispersal interactions, colonization and local extinction clocks are independent across patches, and catastrophes occur on an independent Poisson clock. At each catastrophe, different currently occupied patches are cleared with independent Bernoulli probability \(q\); vacant patches remain vacant. The parameters satisfy \(a,b,c>0\), \(0<q\le1\). The finite chain is irreducible (local colonization and local extinction suffice), has a unique exchangeable stationary law, and observations refer exactly to that law. These are structural, population-level identifiability statements, not claims about a finite noisy dataset or unknown detection probability.

## Proof

**1. Stationary joint-occupancy recursion.** For any fixed set \(S\) of \(j\) distinct patches, let \(Y_S=\prod_{i\in S}X_i\), and set \(p_0=1\). Local colonization contributes \(ja(p_{j-1}-p_j)\) to its mean drift; local extinction contributes \(-jb p_j\). Given a catastrophe, \(Y_S\) survives precisely when each of its \(j\) occupants survives, an event of probability \((1-q)^j\); catastrophe drift is \(-c[1-(1-q)^j]p_j\). Hence stationarity gives, for \(1\le j\le N\),

\[
 [j(a+b)+c\{1-(1-q)^j\}]p_j=ja p_{j-1},
 \qquad
 \frac{p_j}{p_{j-1}}=\frac{ja}{j(a+b)+c[1-(1-q)^j]}.
\]

The recursion follows directly from the finite-state generator and does not rely on an infinite-population limit.

**2. Exact inverse.** Put \(L=a+b\), \(x=a/L\), \(t=cq/L\), and \(s=t/(1+t)\). The first three recursion equations yield

\[
 p_1=x(1-s)=m,\quad
 \frac{p_1^2}{p_2}=1-\frac{sq}{2},\quad
 \frac{p_1p_2}{p_3}=1-s\left(q-\frac{q^2}{3}\right).
\]

Thus \(A=sq/2\), \(B=s(q-q^2/3)\), and \(B/A=2-2q/3\). These identities force the displayed unique inverse. All divisions are legal because every stationary joint occupancy probability is positive and \(s,q>0\).

**3. Exact feasible domain.** Necessity follows from \(0<x<1\), \(0<s<1\), \(0<q\le1\): the ratio \(B/A\) is in \([4/3,2)\), while \(m=x(1-s)\) implies \(s<1-m\). Conversely assume the displayed inequalities. The formulas give \(q\in(0,1]\), \(s\in(0,1-m)\), and \(x=m/(1-s)\in(0,1)\). Choose an arbitrary \(L>0\), define \(a=Lx\), \(b=L(1-x)\), and \(c=Ls/[q(1-s)]\). These are strictly positive. Substitution in the recursion recovers each supplied \(p_j\) for \(j=1,2,3\), proving sufficiency and uniqueness modulo multiplication of all three rates by one positive constant.

**4. Sharpness at two patches.** An exchangeable stationary distribution on two binary patches is determined by \(p_1\) and \(p_2\). These determine \(m\) and \(A=sq/2\), but not \(q\) and \(s\) separately. Choose any \(q'\in(0,1]\) sufficiently close, but unequal, to a given admissible \(q\), and put \(s'=2A/q'\), \(x'=m/(1-s')\), \(c'/L'=s'/[q'(1-s')]\). Strict positivity of \(a,b,c\) ensures \(0<s'<1-m\) for all such nearby choices. The resulting distinct normalized parameters give exactly the same two-patch distribution. One-patch observations carry still less information. Therefore three is necessary.

**5. Exact conditioning boundary.** Factor the forward map as \((x,s,q)\mapsto(m,A,B)\mapsto(m,p_2,p_3)\). The first Jacobian equals \(-(1-s)sq^2/6\); the second equals \(m^5/[(1-A)^3(1-B)^2]\). Multiplying them gives the displayed strictly negative determinant, with the exact quadratic vanishing at fixed \(x,s\) as \(q\downarrow0\).

## Verification

The standalone `CHECKER.py` independently constructs the finite \(2^N\)-state generator and solves the stationary linear equations using only exact rational arithmetic. It verifies the recursion, reconstruction, positivity, all represented joint marginals, the Jacobian factorization and the two-patch ambiguity across \(N=3,4\) and 216 full parameter combinations. Running `python3 CHECKER.py` produces `PASS 10975 exact checks`.

For \((a,b,c,q)=(2,1,3,1/2)\), the three joint probabilities are

\[
 (p_1,p_2,p_3)=\left(\frac49,\frac{64}{297},\frac{1024}{9207}\right).
\]

The alternative \((a,b,c,q)=(32,22,27,2/3)\) has exactly the same first two joint probabilities but \(p_3=512/4653\); thus a third patch resolves the distinction. This is an illustration, not a substitute for the general proof.

The feasibility test is substantive: \((p_1,p_2,p_3)=(1/2,3/10,9/50)\) is a valid exchangeable three-Bernoulli law (the probabilities of exactly zero, one, two and three occupied patches are \(11/50,6/25,9/25,9/50\)), yet \(B/A=1\), which violates the model's necessary lower bound \(4/3\).

## Relationship to prior work

Poisson-triggered binomial catastrophes and stationary factorial-moment recursions are established. Kapodistria, Phung-Duc and Resing's 2015 preprint proves a forward factorial-moment product for linear birth/immigration-death populations with binomial catastrophes; formally allowing a negative per-capita birth coefficient recovers the present *forward* finite-capacity recursion. Section 5.3 and Lemma 5.2 of that preprint further establish stochastic/factorial-moment ordering when the effective catastrophe rate is fixed but severity varies. These forward order comparisons, and the methodological ancestor in Economou (2004), are acknowledged rather than claimed as new. The claim here is the **global inverse of the static spatial moment map**, its complete attainable data domain, the sharp impossibility with fewer than three simultaneously observed patches, and the exact singularity order. Dorazio and colleagues' metacommunity inference work supplies ecological motivation but uses a different observation/model framework. No general assertion of priority over inaccessible papers is made.

## Limitations

The theorem assumes stationary, exchangeable, perfectly observed and locally independent patches with a single common catastrophe mechanism and conditional independent patch clearing. If patch rates vary, catastrophic severity is random, detection is imperfect, or local recolonization depends on other patches, the formulas need not hold. Stationary marginal information cannot recover absolute physical clock speed, and a nonzero Jacobian provides no finite-sample efficiency or robustness guarantee. The 2015 forward formula is closely related, and older inaccessible methodological literature creates residual historical-priority uncertainty.

## References

1. S. Kapodistria, T. Phung-Duc and J. Resing, *Linear birth/immigration-death process with binomial catastrophes*, EURANDOM Preprint Series 2015-006, dated 2015-03-16, https://www.eurandom.tue.nl/reports/2015/006-report.pdf . In particular the model definition and equation (3.5), plus Section 7.
2. A. Economou, *The compound Poisson immigration process subject to binomial catastrophes*, Journal of Applied Probability **41** (2004), 508–523, https://doi.org/10.1239/jap/1082999082 .
3. J. R. Artalejo, A. Economou and M. J. López-Herrero, *Evaluating growth measures in an immigration process subject to binomial and geometric catastrophes*, Mathematical Biosciences and Engineering **4** (2007), 573–594, https://doi.org/10.3934/mbe.2007.4.573 .
4. R. M. Dorazio, M. Kéry, J. A. Royle and M. Plattner, *Models for inference in dynamic metacommunity systems*, Ecology **91** (2010), 2466–2475, https://doi.org/10.1890/09-1033.1 .

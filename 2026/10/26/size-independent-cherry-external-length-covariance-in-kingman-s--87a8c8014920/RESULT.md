# Size-independent cherry–external-length covariance in Kingman's coalescent

## Finding

Let a standard Kingman coalescent with \(n\) labeled leaves have every unordered pair of extant ancestral lineages merge at rate one. Denote by \(C_n\) the number of *cherries* (internal vertices with two leaf children) and by \(E_n\) the sum of the lengths of all external, or pendant, branches, in coalescent time units. Then

\[
\operatorname{Cov}(C_n,E_n)=\begin{cases}
0,&n=2,3,\\
-2/9,&n\ge4.
\end{cases}
\]

The constant covariance is an exact finite-size phenomenon: the number of leaves does not appear once \(n\ge4\).

A stronger intermediate result describes every partially resolved coalescent with \(k\ge4\) extant lineages, of which \(b\in\{0,\ldots,k\}\) are still singleton original leaves and the other \(k-b\) have already been formed by mergers. Write \(C_{b,k}\) for the number of *future* mergers of two singleton lineages and \(E_{b,k}\) for the *future* cumulative external-branch length, measured from that state. With the same pairwise rate-one dynamics,

\[
\boxed{\operatorname{Cov}(C_{b,k},E_{b,k})=
-\frac{2b(b-1)(3k-2b-2)}{9k(k-1)(k-2)}.}
\]

This covariance is strictly negative for all \(2\le b\le k\) and vanishes for \(b\le1\). For \(k=3\), the formula also holds for \(b\le2\), but the all-singleton state \((b,k)=(3,3)\) instead has covariance zero. These exceptions are essential boundary cases, not limiting approximations.

Combining the displayed covariance with published marginal variance identities yields the associated asymptotic correlation

\[
\operatorname{Corr}(C_n,E_n)\sim-\frac{\sqrt5}{6\sqrt{\log n}}\qquad(n\to\infty).
\]

This last relation is a consequence of the principal covariance identity, not a separate claim of novelty.

## Assumptions and scope

The coalescent starts from \(n\ge2\) singleton lineages at time zero. At a state with \(k\ge2\) lineages, the next waiting time is exponentially distributed with rate \(\binom{k}{2}\), independently of the uniformly chosen pair that merges, and independently of future merger choices. A cherry remains a cherry after subsequent mergers above its parent. Consequently, every merger of two still-singleton lineages creates exactly one cherry, whereas the other types of mergers create none. A lineage is counted toward external length precisely while it remains a singleton descendant of an original leaf. No mutations, recombination, multiple mergers, or population-size changes are included.

States \((b,k)\) in the intermediate formula may be initialized with any abstract arrangement of \(b\) original singletons and \(k-b\) internally merged lineages: the future distribution depends only on these two counts. The historical composition of an internally merged lineage does not affect either future statistic. The full \(n\)-coalescent corresponds to \((b,k)=(n,n)\).

## Proof

**1. Transition probabilities.** In state \((b,k)\), write \(r=k-b\). The next merge is of two singletons, one singleton with one internal lineage, or two internal lineages, with respective probabilities

\[
p_2=\frac{b(b-1)}{k(k-1)},\quad
p_1=\frac{2b(k-b)}{k(k-1)},\quad
p_0=\frac{(k-b)(k-b-1)}{k(k-1)}.
\]

A zero-numerator transition is omitted. Under these three transitions, respectively, the new singleton count is \(b_2=b-2\), \(b_1=b-1\), or \(b_0=b\); the lineage count becomes \(k-1\). The new cherry indicator is \(I_2=1\), \(I_1=I_0=0\). If \(T_k\) is the waiting time to the next merger, then

\[
C_{b,k}=I_i+C_{b_i,k-1}',\qquad
E_{b,k}=bT_k+E_{b_i,k-1}',
\]

conditional on transition \(i\). The prime denotes an independent copy of the future process from the indicated new state, conditional on that state. The waiting time satisfies \(\mathbb E T_k=2/[k(k-1)]\) and is independent of the transition type and subsequent genealogy.

**2. First moments.** Denote future means by \(f(b,k)=\mathbb E C_{b,k}\) and \(g(b,k)=\mathbb E E_{b,k}\). Applying the transition probabilities and induction gives, for \(k\ge3\),

\[
f(b,k)=\frac{b(b-1)}{3(k-1)},\qquad
g(b,k)=\frac{2b}{k}.
\]

Indeed, \(f(b,k)=p_2+\sum_{i=0}^{2}p_i f(b_i,k-1)\), while \(g(b,k)=2b/[k(k-1)]+\sum_{i=0}^{2}p_i g(b_i,k-1)\). Substitution of the displayed rational expressions verifies both recurrences exactly. The reachable \(k=2\) terminal states have at most one singleton, so \(f=0\) there, and \(g(b,2)=b\); the exceptional initial two-leaf state has \(f(2,2)=1\) and \(g(2,2)=2\). At \((3,3)\), \(f=1\) since exactly one initial pair merges and no more singleton pairs can merge. Thus all recurrences used for \(k\ge3\) have the stated boundary values.

**3. Covariance recursion and induction.** Write \(K(b,k)=\operatorname{Cov}(C_{b,k},E_{b,k})\). Since \(T_k\) is independent of the entire merger tree, \(\operatorname{Cov}(C_{b,k},bT_k)=0\). The law of total covariance over the three transition types therefore gives

\[
K(b,k)=\sum_{i=0}^2p_i K(b_i,k-1)
+\operatorname{Cov}_i\!\left(I_i+f(b_i,k-1),g(b_i,k-1)\right),
\]

where \(\operatorname{Cov}_i\) means covariance under the discrete distribution of transition type \(i\) with weights \(p_i\), not over any future randomness.

For \(k=3\), the possible states with at most two singletons have

\[
K(0,3)=K(1,3)=0,\qquad K(2,3)=-2/9.
\]

The last identity can be seen directly: with two singletons and one internal lineage, the singleton–singleton merger occurs with probability \(1/3\), yields one cherry and no remaining external length; the other merger types yield no cherry and a single remaining singleton until the final merger. Its remaining branch has mean length one, so the covariance is \(-\frac13\cdot\frac23=-2/9\). In the separate all-singleton state \((3,3)\), the total cherry count is the constant one, so \(K(3,3)=0\). For all \(k\ge4\), successor states at level three, when that level is reached, have at most two singletons; hence the exceptional \((3,3)\) state never enters the induction.

For \(k\ge4\), substituting the first-moment formulas and carrying out the finite three-term expansion gives

\[
\operatorname{Cov}_i\!\left(I_i+f(b_i,k-1),g(b_i,k-1)\right)
=\frac{4b(b-1)(b-k)}{3k(k-2)(k-1)^2}.
\]

Set

\[
H(b,k):=-\frac{2b(b-1)(3k-2b-2)}{9k(k-1)(k-2)}.
\]

Direct expansion of the three transition terms also gives the rational identity

\[
\sum_{i=0}^2p_iH(b_i,k-1)
=H(b,k)-\frac{4b(b-1)(b-k)}{3k(k-2)(k-1)^2}.
\]

Both displayed algebraic identities are obtained by bringing the three terms to their common denominator \(9k(k-1)^2(k-2)(k-3)\) before cancellation; at \(k=4\) one uses the valid \(k=3\) successor values. Therefore \(K(b,k)=H(b,k)\) by induction for every \(k\ge4\) and \(0\le b\le k\). The sign follows because \(3k-2b-2\ge k-2>0\), and the factor \(b(b-1)\) vanishes exactly for \(b=0,1\).

**4. The complete tree and small cases.** Taking \(b=k=n\ge4\) gives

\[
K(n,n)=-\frac{2n(n-1)(n-2)}{9n(n-1)(n-2)}=-\frac29.
\]

For \(n=2\) and \(n=3\) every resolved tree has exactly one cherry, so the covariance is zero. This proves the stated all-size classification.

**5. Correlation consequence.** The known Yule–Harding–Kingman cherry variance is \(\operatorname{Var}(C_n)=2n/45\) for \(n\ge5\) (Wu and Choi, Corollary 2; attributed there to Heard and McKenzie–Steel). The coalescent external-length variance is

\[
\operatorname{Var}(E_n)=\frac{8}{(n-1)(n-2)}\bigl(n H_{n-1}-2(n-1)\bigr),
\quad H_j=\sum_{a=1}^j\frac1a.
\]

It follows that \(\operatorname{Var}(E_n)\sim8\log n/n\), and substituting the proven covariance into the correlation definition gives the asymptotic expression in the Finding section.

## Verification

The included `verify.py` implements the state recursion using exact rational arithmetic. It confirms the means and covariance polynomial for each \(4\le k\le65\) and \(0\le b\le k\), comprising 2,201 state comparisons, including 62 all-singleton sizes. A completely different check enumerates *all labeled pair-merger histories* for \(2\le n\le7\), without using the two-count dynamic program, and averages the conditional external length over the independent exponential holding times. The history counts are \(1,3,18,180,2700,56700\) for \(n=2,\ldots,7\); their exact covariances are zero for \(n=2,3\) and \(-2/9\) for \(n=4,5,6,7\). This verifies the normalization and the exceptional boundary. The all-size statement is proved analytically above; finite checks are not asserted to certify it.

Run `python verify.py` with a standard Python installation. No input datasets or third-party packages are required.

## Relationship to prior work

Janson and Kersting (arXiv:1004.5011, first public 2010-04-28) analyze the external lengths in Kingman's coalescent and the reversible black/red urn coding of its lineage process; their Section 2 gives the relevant singleton/internal-lineage representation. Wu and Choi (arXiv:1508.03139, first public 2015-08-13) study joint cherry/pitchfork counts under the Yule–Harding–Kingman model, and recover the cherry mean and variance. Steel and Mooers (arXiv:0910.5240, first public 2009-10-27) study pendant/interior edge lengths for a *pure-birth Yule process*, whose holding-time rates differ from the Kingman coalescent rates used here.

The present claim is not the known cherry marginal law, the known external-length variance, the pure-birth Yule mean-length result, or the general black/red transition rule. It is the evaluated **mixed** covariance of cherry count and metric external length, with a uniform negative kernel for partially resolved states and an \(n\)-independent complete-tree value. General transition rules make such a moment computable in principle, but the inspected primary statements do not give this evaluated result.

## Limitations

The conclusion depends on unit rate for each unordered merging pair. Changing the overall coalescent clock scale multiplies external length and the covariance by the inverse scale; the literal numerical constant \(-2/9\) is not invariant under clock renormalization. For variable population size or time-dependent pair rates, waiting times need no longer have the assumed homogeneous exponential law. The theorem concerns ordinary Kingman pair mergers, not simultaneous multiple mergers. Its covariance does not establish negative association or conditional stochastic ordering for the full joint distribution. The sources inspected do not conclusively rule out an unlocated equivalent earlier formula; bibliographic priority therefore remains uncertain. No independent audit has been performed.

## References

1. S. Janson and G. Kersting, *The external lengths in Kingman's coalescent* (2010 preprint; 2011 journal version), arXiv:1004.5011, https://arxiv.org/abs/1004.5011.
2. T. Wu and K. P. Choi, *On joint subtree distributions under two evolutionary models* (2015 preprint; 2016 journal version), arXiv:1508.03139, https://arxiv.org/html/1508.03139v1.
3. M. Steel and A. Mooers, *Expected length of pendant and interior edges of a Yule tree* (2009), arXiv:0910.5240, https://arxiv.org/html/0910.5240v1.
4. E. Alimpiev and N. A. Rosenberg, *A compendium of covariances and correlation coefficients of coalescent tree properties* (2021), arXiv:2103.13467, https://arxiv.org/abs/2103.13467; cited only for contextual marginal-length calculations, not claimed to have been fully examined.

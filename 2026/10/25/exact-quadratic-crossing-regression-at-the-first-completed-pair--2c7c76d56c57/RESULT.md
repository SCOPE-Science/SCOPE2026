# Exact quadratic crossing regression at the first completed pair

## Finding

A uniform random perfect matching on \(2n\) linearly ordered vertices has a precise relation between its **first completion time** and its global number of crossings. Write \(T_n\) for the least right endpoint of a matched pair, and \(X_n\) for the number of unordered chord pairs with alternating endpoints. For all integers \(n\ge2\) and \(2\le t\le n+1\),

\[\boxed{\mathbb E[X_n\mid T_n=t]=\frac{n(n-3)}6+\frac{(t-1)(t+2)}{12}.}\]

This regression strictly increases with the first-completion time. Consequently \(\operatorname{Cov}(T_n,X_n)>0\) for all \(n\ge2\), and

\[\boxed{\frac{\operatorname{Cov}(T_n,X_n)}{n^{3/2}}\longrightarrow\frac{\sqrt\pi}{6},\qquad \sqrt n\operatorname{Corr}(T_n,X_n)\longrightarrow\frac{\sqrt{5\pi}}{2\sqrt{4-\pi}}.}\]

Thus the covariance grows, although the correlation decreases to zero.

## Assumptions and scope

The probability space is the finite set of all \((2n-1)!!\) perfect matchings of \(\{1,\ldots,2n\}\), each equally likely. Represent each matched pair as \((a,b)\), where \(a<b\). Define \(T_n=\min b\) over all matched pairs and \(X_n\) as the number of unordered distinct pairs \((a,b),(c,d)\) for which \(a<c<b<d\) or \(c<a<d<b\). Then \(T_n\in\{2,\ldots,n+1\}\) and all conditioning events in the displayed formula have positive probability. Chords are considered with respect to this fixed linear endpoint order; the crossing definition is the standard alternating-endpoint rule.

## Proof

**Step 1: first-completion survival.** Let \(p_{n,t}=\Pr(T_n>t)\), with \(p_{n,0}=p_{n,1}=1\). Given \(T_n>s-1\), all first \(s-1\) endpoints have partners among later endpoints. The partner of vertex \(s\) is uniformly distributed among the other \(2n-s+1\) available vertices, of which \(s-1\) are earlier exposed vertices. Thus, for \(2\le s\le n+1\),

\[\frac{p_{n,s}}{p_{n,s-1}}=\frac{2(n-s+1)}{2n-s+1},\qquad p_{n,t}=\prod_{s=2}^{t}\frac{2(n-s+1)}{2n-s+1}.\]

The last factor vanishes at \(t=n+1\), and all earlier factors are positive.

**Step 2: crossing count given survival.** On \(T_n>t\), the first \(t\) vertices are distinct opening endpoints, each matched to a distinct point in the remaining \(2n-t\) positions. Conditional symmetry makes their partners a uniformly injected assignment, and the other \(n-t\) pairs form a uniformly random matching of the remaining points. Partition the crossing pairs into three categories:

* Two opening chords cross exactly when the two randomly assigned tail partners occur in the same order as their openers, with probability \(1/2\), giving \(\binom t2/2\).
* One opening chord and one wholly tail chord cross exactly when the opening chord's tail partner lies between the two tail-chord endpoints. All three orders are symmetric, so the probability is \(1/3\), giving \(t(n-t)/3\).
* Two wholly tail chords cross with probability \(1/3\), giving \(\binom{n-t}{2}/3\).

Adding these expectations and simplifying, for \(0\le t\le n\), yields

\[e_{n,t}:=\mathbb E[X_n\mid T_n>t]=\frac{n(n-1)}6+\frac{t(t-1)}{12}.\]

**Step 3: exact conditional regression.** For \(2\le t\le n+1\), subtract the weighted crossing contributions from the nested survival events:

\[\mathbb E[X_n\mid T_n=t]=\frac{p_{n,t-1}e_{n,t-1}-p_{n,t}e_{n,t}}{p_{n,t-1}-p_{n,t}}.\]

Use \(p_{n,t}/p_{n,t-1}=2(n-t+1)/(2n-t+1)\) and \(e_{n,t}-e_{n,t-1}=(t-1)/6\). Direct simplification gives

\[\mathbb E[X_n\mid T_n=t]=\frac{n(n-3)}6+\frac{(t-1)(t+2)}{12}.\]

The endpoint \(t=n+1\) is included because the ratio of survival probabilities is zero. Define \(g_n(t)\) as this quadratic. Then \(g_n(t+1)-g_n(t)=(t+1)/6>0\) and \(\operatorname{Cov}(T_n,X_n)=\operatorname{Cov}(T_n,g_n(T_n))\). Applying the independent-copy identity \(2\operatorname{Cov}(T_n,g_n(T_n))=\mathbb E[(T_n-T_n')(g_n(T_n)-g_n(T_n'))]\) proves strict positivity, because \(T_n\) has at least two possible values.

**Step 4: covariance and its asymptotic.** Expand the regression:

\[\operatorname{Cov}(T_n,X_n)=\frac{\mathbb E[T_n^3]+\mathbb E[T_n^2]-\mathbb E[T_n](\mathbb E[T_n^2]+\mathbb E[T_n])}{12}.\]

This is an exact finite formula using the first three moments obtained from

\[\mathbb E[T_n^j]=\sum_{t=0}^{n}\big((t+1)^j-t^j\big)p_{n,t},\quad j=1,2,3.\]

Taking logarithms of the product in Step 1 gives, for every fixed \(x\ge0\), \(p_{n,\lfloor x\sqrt n\rfloor}\to e^{-x^2/4}\). Moreover, \(p_{n,t}\le \exp(-t(t-1)/(4n))\); hence the scaled moments through order three are uniformly integrable and converge by domination. With \(R\) having survival function \(\Pr(R>x)=e^{-x^2/4}\), we obtain \(\mathbb ER=\sqrt\pi\), \(\mathbb ER^2=4\), and \(\mathbb ER^3=6\sqrt\pi\). Therefore

\[n^{-3/2}\operatorname{Cov}(T_n,X_n)\to\frac{\mathbb ER^3-(\mathbb ER)(\mathbb ER^2)}{12}=\frac{\sqrt\pi}{6}.\]

Also \(\operatorname{Var}(T_n)/n\to4-\pi\). The classical exact crossing variance is \(\operatorname{Var}(X_n)=n(n-1)(n+3)/45\); combining these three relations gives the stated scaled-correlation limit.

## Verification

The standalone standard-library Python program `verify_first_close.py` enumerates all perfect matchings for each \(n=2,3,4,5,6,7\), computing crossing counts and first-completion times directly. It compares every attainable conditional regression value, each survival probability, each conditional survival-crossing mean, and the unconditional crossing mean with exact-rational expressions. This tests a total of \(146{,}598\) matchings, including \(135{,}135\) at \(n=7\). All assertions pass. The checks are finite and are not substitutes for the preceding all-size proof.

## Relationship to prior work

Velleman and Warrington (2012) studied the *first match* in the card-memory model and derived its expectation of order \(\sqrt{\pi n}\), matching the statistic \(T_n\) under the natural pairing representation. Flajolet and Noy (2000) studied chord-diagram crossings and derived their classical moments and Gaussian asymptotics. Acan and Hitczenko (2014) studied right endpoints, chord-diagram growth, and random graph quantities. Paguyo's later paper presents modern crossing-statistic limit theory. These precedents establish the marginal questions and model, but the conditional crossing regression and its mixed covariance asymptotic were not identified in the material inspected. This is a historical-coverage assessment, not a claim of exhaustive bibliographic uniqueness.

## Limitations

The result is an exact first conditional **moment** of crossings, not a conditional distribution, not a stochastic-order theorem, and not a joint central limit theorem. The asymptotic is specific to uniformly random pairings and the first completion time. Earlier work on more general weighted chord-diagram growth could contain an equivalent mixed-moment formula; historical priority remains subject to independent inspection.

## References

1. D. J. Velleman and G. S. Warrington, *Matching Expectations*, first publicly posted 2012-08-23, arXiv:1208.4854v1, https://arxiv.org/abs/1208.4854 .
2. P. Flajolet and M. Noy, *Analytic Combinatorics of Chord Diagrams*, INRIA Research Report 3914, March 2000, https://algo.inria.fr/flajolet/Publications/FlNo00.pdf .
3. H. Acan and P. Hitczenko, *On a memory game and preferential attachment graphs*, first publicly posted 2014-11-21, arXiv:1411.5751v1, https://arxiv.org/abs/1411.5751 .
4. A. Paguyo, *Convergence rates of limit theorems in random chord diagrams*, arXiv:2104.01134, https://arxiv.org/abs/2104.01134 .

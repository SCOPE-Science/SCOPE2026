# An exact edge-conditioned degree-covariance sign reversal in random circle graphs

## Finding

Choose a uniform perfect matching of \(2n\) points on a circle, where \(n\ge2\). Its circle graph has one vertex for each chord and an edge precisely when two chords cross. Independently mark two distinct chords \(A,B\) uniformly; let \(D_A,D_B\) be their graph degrees, and let \(E=\mathbf1\{A\text{ crosses }B\}\). Then

\[
\operatorname{Cov}(D_A,D_B\mid E=0)=\frac{(n-2)(16-3n)}{700},\qquad
\operatorname{Cov}(D_A,D_B\mid E=1)=\frac{(n-2)(n+18)}{525}.
\]

Thus the degree covariance of *nonadjacent* graph vertices is positive for \(3\le n\le5\), negative for every \(n\ge6\), and zero for \(n=2\). For *adjacent* vertices it is positive for \(n\ge3\) and zero for \(n=2\). The nonedge sign switch is sharp between five and six chords. For context, the corresponding unconditioned covariance is always positive:
\[
\operatorname{Cov}(D_A,D_B)=\frac{3n+4}{45}.
\]
This last aggregate identity is a consistency consequence of previously studied marginal degree and total crossing statistics; the edge/nonedge split is the finding.

## Assumptions and scope

All \((2n-1)!!\) matchings of the specified, distinct, cyclically ordered endpoints have equal probability. The two marked chords are sampled uniformly in ordered succession, after sampling the matching. Equivalently, label all chords independently of the matching and designate labels \(0\) and \(1\); the degrees then count distinct *other* chords that cross the designated chord. Conditional covariance is defined with respect to \(E\in\{0,1\}\); both conditioning events have positive probability for every \(n\ge2\).

## Proof

Uniformly label the chords \(0,1,\ldots,n-1\), representing their cyclic endpoint order by a **double-occurrence word** in which each label occurs exactly twice. The induced subword on any fixed \(m\) chord labels is uniform over the \((2m)!/2^m\) distinct words. Indeed a uniform random labeled matching is equivalent to uniformly permuting the multiset containing two occurrences of every label; erasing other labels preserves uniform order by symmetry.

For labels \(a,b\), put \(X_{ab}=1\) when the two label occurrences alternate, and \(0\) otherwise. Write \(E=X_{01}\). A reproducible finite, exhaustive count of the induced words on three or four chord labels gives the following complete local event table. The numbers are conditional probabilities:

| \(e\) | \(\Pr(E=e)\) | \(q_e=\Pr(X_{02}=1\mid E=e)\) | \(r_e=\Pr(X_{02}=X_{12}=1\mid E=e)\) | \(s_e=\Pr(X_{02}=X_{13}=1\mid E=e)\) |
|---:|---:|---:|---:|---:|
| \(0\) | \(2/3\) | \(3/10\) | \(1/10\) | \(3/35\) |
| \(1\) | \(1/3\) | \(2/5\) | \(1/5\) | \(17/105\) |

For explicit exact counts, there are \(90\) three-label words: \(60\) with \(E=0\) and \(30\) with \(E=1\). Respectively, the events \(X_{02}=1\) occur \(18\) and \(12\) times, and \(X_{02}=X_{12}=1\) occur \(6\) and \(6\) times. There are \(2520\) four-label words: \(1680\) with \(E=0\) and \(840\) with \(E=1\); the events \(X_{02}=X_{13}=1\) occur \(144\) and \(136\) times, respectively. The included verifier generates every word exactly once by inserting two occurrences of each new label at every pair of positions; hence these small counts are exhaustive combinatorial identities, not sampled data or finite-size extrapolations.

Given \(E=e\), the constant contribution of the marked chord to each degree is \(e\), and
\[
D_0=e+\sum_{c=2}^{n-1}X_{0c},\qquad
D_1=e+\sum_{c=2}^{n-1}X_{1c}.
\]
Every same-third-chord term in the cross-covariance equals \(r_e-q_e^2\). Every different-third-chord term equals \(s_e-q_e^2\). The exact number of ordered terms in these two classes is, respectively, \(n-2\) and \((n-2)(n-3)\). Therefore
\[
\operatorname{Cov}(D_0,D_1\mid E=e)
=(n-2)(r_e-q_e^2)+(n-2)(n-3)(s_e-q_e^2).
\]
The local counts give
\[
r_0-q_0^2=\frac1{100},\quad s_0-q_0^2=-\frac3{700};\qquad
r_1-q_1^2=\frac1{25},\quad s_1-q_1^2=\frac1{525}.
\]
Substitution and simplification yield the two asserted closed forms, for every integer \(n\ge2\), without approximation. Their signs follow immediately, because \(16-3n\) is positive for integers \(n\le5\) and negative for integers \(n\ge6\), while \(n+18\) is always positive. Finally \(\mathbb E[D_0\mid E=0]=3(n-2)/10\), \(\mathbb E[D_0\mid E=1]=1+2(n-2)/5\); conditioning on the Bernoulli event with probability \(1/3\) gives the stated positive unconditional covariance via total covariance. \(\square\)

## Verification

Run `python3 verify.py` with Python 3's standard library. It independently enumerates the \(90\) and \(2520\) induced words, checks each displayed conditional probability as an exact rational number, and confirms that the covariance-sum expression agrees algebraically with both closed forms for \(2\le n\le300\). The proof's infinite-\(n\) conclusion instead rests on the exact four-label table and exchangeability, so no bound on \(n\) is inferred from testing. The local word generator itself is transparent and exhaustive.

## Relationship to prior work

H. Acan (2015 preprint) studied the marginal degree of a random vertex in the uniform chord-diagram intersection graph, not the conditional joint degrees of two randomly marked distinct vertices. J. E. Paguyo (first public preprint April 2, 2021) developed limit theorems and exact aggregate crossing moments. Arenas-Velilla and Arizmendi (2022) studied crossings in randomly embedded graphs. Their aggregate crossing calculations do not themselves identify the separate positive edge-conditioned and sign-changing nonedge-conditioned degree covariances, even where marginal information determines the positive *unconditional* covariance. The finding refines the familiar aggregate statistic by describing an edge/nonedge dependence dichotomy.

## Limitations

This theorem concerns the unconditional uniform-matching model, not fixed-crossing-count chord diagrams, other circle-graph distributions, or conditional correlations (which have different normalization). The exhaustive table is a finite proof of the required local probabilities; it does not assert classification of all global circle graphs. Published-priority coverage is best-knowledge rather than independently certified: an implicit derivation or earlier graph-assortativity formula could give equivalent results. No independent scientific audit has been performed.

## References

1. Hüseyin Acan, “On a uniformly random chord diagram and its intersection graph,” arXiv:1501.01489, 2015, https://arxiv.org/abs/1501.01489.
2. J. E. Paguyo, “Convergence rates of limit theorems in random chord diagrams,” arXiv:2104.01134, initial posting 2021-04-02, https://arxiv.org/abs/2104.01134.
3. Santiago Arenas-Velilla and Octavio Arizmendi, “Crossings in Randomly Embedded Graphs,” arXiv:2205.03995, 2022, https://arxiv.org/abs/2205.03995.

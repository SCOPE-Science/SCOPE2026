# A rare-chord covariance correction for crossings in uniform circular matchings

## Finding

In a uniform chord diagram, chords with no crossings create a measurable negative dependence with the total crossing count. The rare chords that are *not* incident to consecutive cyclic endpoints disappear in probability, yet their covariance contribution tends to a nonzero constant.

For an integer \(n\ge2\), let \(X_n\) be the number of unordered pairs of intersecting chords, let \(I_n\) be the number of chords intersecting none, and let \(S_n\) be the number of chords joining cyclically consecutive endpoints. Every such simple chord is isolated. Put \(J_n=I_n-S_n\). With \((-1)!!=1\), set

\[
p_{n,r}=\frac{(2r-1)!!(2n-2r-3)!!}{(2n-1)!!},\qquad 0\le r\le n-1.
\]

The exact finite covariance and expectation are

\[
\boxed{\operatorname{Cov}(I_n,X_n)=-\frac n3\sum_{r=0}^{n-1}p_{n,r}\bigl[n-1+r(n-1-r)\bigr]<0,}\qquad
\mathbb E I_n=n\sum_{r=0}^{n-1}p_{n,r}.
\]

The simple-chord contribution is

\[
\operatorname{Cov}(S_n,X_n)=-\frac{2n(n-1)}{3(2n-1)}.
\]

As \(n\to\infty\),

\[
\boxed{\operatorname{Cov}(I_n,X_n)=-\frac n3-\frac16+O(n^{-1}),}
\qquad
\boxed{\operatorname{Cov}(J_n,X_n)=-\frac13+O(n^{-1}),}
\]

and \(\mathbb E J_n=(2n)^{-1}+O(n^{-2})\). In particular, \(J_n\to0\) in probability while its covariance with \(X_n\) tends to \(-1/3\).

## Assumptions and scope

Place \(2n\) distinct labeled endpoints in a fixed cyclic order and choose each of the \((2n-1)!!\) perfect matchings with equal probability. Chords are straight segments; two chords cross if their endpoints alternate in cyclic order. Crossing pairs and isolated chords are counted without multiplicity. A chord is *simple* if its endpoints are consecutive in the cyclic order, including the wrap-around pair. All assertions are for integer \(n\ge2\), unless an asymptotic limit is stated. Landau constants are absolute. All factorials have their ordinary integer meanings.

## Proof

**1. Condition on an isolated prescribed chord.** Fix any candidate chord \(e\). Its two arcs leave \(2r\) endpoints on one side and \(2(n-1-r)\) on the other. To make \(e\) a chord with no crossings, all other endpoints must match entirely within their own side. The probability of this event \(A_e\) is exactly \(p_{n,r}\). Conditioned on \(A_e\), the two side matchings are independent uniform chord diagrams with \(r\) and \(n-1-r\) chords. Every crossing is wholly inside one side.

For a uniform diagram with \(k\) chords, each pair crosses with probability \(1/3\), because among the three pairings of four chosen endpoints exactly one crosses. Therefore

\[
\mathbb E[X_n]=\frac13\binom n2,\qquad
\mathbb E[X_n\mid A_e]=\frac13\left[\binom r2+\binom{n-1-r}2\right].
\]

Subtracting yields

\[
\mathbb E[X_n\mid A_e]-\mathbb E[X_n]=-rac{n-1+r(n-1-r)}3.
\]

Thus the covariance between \(\mathbf1_{A_e}\) and \(X_n\) is \(-p_{n,r}[n-1+r(n-1-r)]/3\). The desired statistic \(I_n\) is the sum of \(\mathbf1_{A_e}\) over all \(\binom{2n}{2}\) candidate chords.

**2. Count the candidates without double counting.** For each \(r\in\{0,\ldots,n-1\}\) and each starting endpoint there is an *oriented* chord leaving \(2r\) endpoints on its forward arc. Hence there are \(2n\) oriented choices for each \(r\). Every unoriented chord appears exactly twice in the union over all \(r\), under \(r\leftrightarrow n-1-r\), also when these two indices agree. The factor is therefore \(2n/2=n\). Summing the covariance and indicator expectations proves both exact formulas. Each summand of the covariance is strictly negative for \(n\ge2\).

**3. Split simple and non-simple chords.** The indices \(r=0\) and \(r=n-1\) correspond exactly to simple chords; they satisfy \(p_{n,0}=p_{n,n-1}=1/(2n-1)\). Their contribution gives the stated exact \(\operatorname{Cov}(S_n,X_n)\) and \(\mathbb ES_n=2n/(2n-1)\). The remaining indices are precisely the non-simple isolated chords \(J_n\).

For \(n\ge4\), the two outermost remaining terms \(r=1,n-2\) contribute exactly

\[
\mathbb E[J_n;\,r\in\{1,n-2\}]=\frac{2n}{(2n-1)(2n-3)},
\qquad
\operatorname{Cov}_{\{1,n-2\}}(J_n,X_n)=-\frac{2n}{3(2n-1)}.
\]

The notation in these two expressions means the partial sums of the exact expectation and covariance formulas, not a conditional expectation. Both are interpreted only when the two indices are distinct.

**4. Bound all longer isolated chords.** For \(0\le r<n-1\),

\[
\frac{p_{n,r+1}}{p_{n,r}}=\frac{2r+1}{2n-2r-3},\qquad p_{n,r}=p_{n,n-1-r}.
\]

The weights decrease through the first half of the range. For sufficiently large \(n\) and \(2\le r\le\lfloor n/4\rfloor\), the successive ratios are at most \(1/2\). Moreover,

\[
p_{n,2}=\frac3{(2n-1)(2n-3)(2n-5)}=O(n^{-3}).
\]

Consequently the one-sided sum \(\sum_{r\ge2}^{\lfloor n/4\rfloor}(r+1)p_{n,r}\) is \(O(n^{-3})\). The remaining weights through the midpoint are bounded by a geometric factor \(O(2^{-n/4}n^{-3})\) using monotonicity, and symmetry handles the other half. The expectation contribution of \(r\in\{2,\ldots,n-3\}\) is therefore \(O(n^{-2})\). Because \(n-1+r(n-1-r)\le n(r+1)\), its covariance contribution is \(O(n^{-1})\).

Combining these bounds with step 3 gives \(\mathbb E J_n=(2n)^{-1}+O(n^{-2})\) and \(\operatorname{Cov}(J_n,X_n)=-1/3+O(n^{-1})\). Finally

\[
-\frac{2n(n-1)}{3(2n-1)}=-\frac n3+\frac16+O(n^{-1}),
\]

so addition gives \(\operatorname{Cov}(I_n,X_n)=-n/3-1/6+O(n^{-1})\). Since \(J_n\ge0\), Markov's inequality proves \(J_n\to0\) in probability. This finishes the proof.

## Verification

The accompanying standalone `verify_chord_isolation.py` uses exact rational arithmetic and exhaustively enumerates all \((2n-1)!!\) matchings for each \(1\le n\le7\), a total of 146,599 matchings. It independently calculates crossings, zero-crossing chords, cyclic simple chords, their expectations and both mixed covariances. Each exact quantity agrees with the theorem, including all small-size boundary cases. Run `python3 verify_chord_isolation.py` from a directory containing the extracted file. Exhaustive checks at bounded \(n\) support, but do not replace, the proof for all sizes.

## Relationship to prior work

Flajolet and Noy (2000) treat connected components of chord diagrams, monolithicity, and marginal crossing moments, including the asymptotic prevalence of simple isolated chords. Acan (2015) studies the intersection graph, local degrees, simple chords, and monolithic structure. Paguyo (2021) gives marginal convergence rates for crossings and simple chords. Their relevant full texts were checked for stronger mixed coverage. None of those inspected results states the finite covariance between *all* isolated chords and crossings or determines the nonzero \(-1/3\) contribution of non-simple isolated chords.

An earlier calculation for adjacent **linear** endpoints gives a covariance with crossings but excludes the cyclic wrap-around chord and, more importantly, does not count non-simple isolated chords. A direct extension to cyclic simple chords supplies only the \(S_n\) term above, not the \(J_n\) correction. This comparison is about implications of mathematical statements, not bibliographic priority certification.

## Limitations

Historical completeness and independent validation are not claimed. The result concerns uniform perfect matchings of labeled cyclic endpoints, not general circle graphs sampled uniformly over graph isomorphism classes. The limit \(\operatorname{Cov}(J_n,X_n)\to-1/3\) does not imply that \(J_n\) has a nonzero limiting distribution or that products involving the unnormalized crossing count are uniformly integrable. No claim is made about higher mixed moments or joint large deviations.

## References

- P. Flajolet and M. Noy, *Analytic Combinatorics of Chord Diagrams*, INRIA Research Report 3914, manuscript dated 2000-03-04. https://algo.inria.fr/flajolet/Publications/FlNo00.pdf
- H. Acan, *On a uniformly random chord diagram and its intersection graph*, arXiv:1501.01489v1, 2015-01-07. https://arxiv.org/html/1501.01489v1
- A. Paguyo, *Convergence rates of limit theorems in random chord diagrams*, arXiv:2104.01134v2, 2021. https://arxiv.org/html/2104.01134v2

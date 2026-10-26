# Sharp finite-agenda displacement of the median outcome under Borda voting

## Finding

Let \(m\ge2\) alternatives be arranged in fixed order \(0,1,\ldots,m-1\), and let \(2r+1\) voters, with \(r\ge1\), have strict rankings single-peaked on this common axis. Define the median peak \(h\) as the \((r+1)\)-st smallest top-ranked alternative. It is the unique Condorcet winner. Let \(w\) be the **unique** Borda winner, if one exists, with scores \(m-1,m-2,\ldots,0\) for the successive ranks.

The **maximum possible** candidate-axis displacement, over all such profiles with a unique Borda winner, is exactly

\[
D(m,r)=\max |w-h|=\left\lfloor\frac{r(m-1)-1}{r+1}\right\rfloor
=m-2-\left\lfloor\frac{m-1}{r+1}\right\rfloor.
\]

Both the upper bound and its attainment hold for every integer \(m\ge2\) and \(r\ge1\), without assuming equal spacing of cardinal utilities or Euclidean voter preferences. As a corollary, for every \(m\ge3\) the largest theoretically possible displacement \(m-2\) first becomes attainable with exactly \(2m-1\) voters (and remains attainable for every larger odd electorate). The first three-voter disagreement occurs at four alternatives; with three alternatives disagreement first occurs at five voters.

## Assumptions and scope

There are finitely many, linearly ordered alternatives identified by consecutive integer *indices*, not necessarily equally separated policies in a metric. Each voter's strict complete ranking has a unique peak \(p\); within the two sides of that peak, alternatives nearer to \(p\) in axis order are always preferred to those farther on the same side. No restriction is imposed on interleaving the two sides. The electorate has odd size \(2r+1\) with \(r\ge1\). All ballots are sincere. Borda scores are the integers \(m-1\) down to zero. The claim concerns profiles with **unique** Borda winners; it does not claim the same formula for arbitrary tied winner sets. Displacement is measured in *axis index steps*, not physical policy distance, majority margin, or Kemeny distance between rankings.

## Proof

**Median.** For any alternative \(x<h\), at least \(r+1\) voters have peaks at or to the right of \(h\). All these voters strictly prefer \(h\) to \(x\) by single-peakedness; the symmetric argument applies to \(x>h\). Hence \(h\) defeats every other alternative in pairwise majority comparisons.

**Uniform upper bound.** By symmetry reflect the axis to assume \(w<h\), and write \(d=h-w\). For each of at least \(r+1\) voters with peak at or to the right of \(h\), the relative Borda score of \(h\) over \(w\) is at least \(d\): the \(d-1\) intervening alternatives also lie ahead of \(w\) but behind \(h\). For each other voter, the score difference in favor of \(w\) is at most \(m-1\). Thus

\[
S(h)-S(w)\ge(r+1)d-r(m-1).
\]

Since \(w\) is a **unique** Borda winner, \(S(w)>S(h)\), forcing \((r+1)d<r(m-1)\), equivalently

\[
d\le\left\lfloor\frac{r(m-1)-1}{r+1}\right\rfloor.
\]

(The strict inequality is essential when the ratio happens to be an integer.) If \(w>h\), apply the reflection \(x\mapsto m-1-x\).

**Matching construction.** Put

\[
a=1+\left\lfloor\frac{m-1}{r+1}\right\rfloor.
\]

Take \(r+1\) voters with the ranking

\[
m-1\succ m-2\succ\cdots\succ0
\]

and \(r\) voters with the ranking

\[
a\succ a-1\succ\cdots\succ0\succ a+1\succ a+2\succ\cdots\succ m-1.
\]

Both rankings are strict and single-peaked. The median peak is \(h=m-1\). Every voter prefers \(a\) to each \(y<a\), so \(S(a)>S(y)\). For each \(y>a\), the right-peaked voters give \(y\) an advantage of \(y-a\) points per vote over \(a\); the other voters give \(a\) an advantage of \(y\) points per vote over \(y\). Consequently the exact score gap is

\[
S(a)-S(y)=r y-(r+1)(y-a)=(r+1)a-y.
\]

Because \((r+1)a>m-1\), this difference is strictly positive for every \(a<y\le m-1\). Hence \(a\) is the unique Borda winner. Its distance from \(h\) is

\[
(m-1)-a=m-2-\left\lfloor\frac{m-1}{r+1}\right\rfloor,
\]

exactly the upper bound. This also proves the sharp electorate threshold: equality with \(m-2\) holds exactly when \(\lfloor(m-1)/(r+1)\rfloor=0\), or \(r+1>m-1\), equivalently \(2r+1\ge2m-1\) for integer \(r\).

## Verification

A dependency-free exact-integer verifier (`verify.py`) generates all single-peaked ballots by endpoint deletion, independently validates their single-peakedness directly, and checks every anonymous profile for \(2\)–\(5\) alternatives and \(3\), \(5\), or \(7\) voters, together with \(6\) alternatives and \(3\) voters. It confirms the predicted maximum displacement in all \(13\) exhaustive instances and verifies the sharp construction for \(1960\) further parameter pairs covering \(2\le m\le50\) and \(1\le r\le40\). Exact results are preserved in `certificate.json`. Finite tests corroborate but are **not** the proof for unrestricted \(m,r\); that proof is the preceding counting argument and construction. Reproduce using `python3 verify.py`; Python 3 standard library suffices.

For example, with four alternatives and three voters, two submit \(3\succ2\succ1\succ0\) and one submits \(2\succ1\succ0\succ3\). Alternative \(3\) is the Condorcet winner, but \(2\) is the unique Borda winner, at distance one. With five alternatives and five voters, the construction has median peak \(4\) and Borda winner \(2\), at distance two.

## Relationship to prior work

Black (1948) establishes the median-voter connection for single-peaked majority preferences. Feld and Grofman (1988), especially pp. 169–170 and 174, explicitly note that discrete, finite-alternative Borda and Condorcet winners may disagree, and prove coincidence for a *continuous feasible* one-dimensional spatial domain; these are different quantifiers and neither determines the sharp bound for a finite ordered agenda. Klamler (2003/2005) measures distance to Condorcet consistency using **profile modification / Kemeny-style ranking distances**, not candidate-axis displacement on the single-peaked domain. Mousseau, Surugue, and Wilczynski (2025) derive expected-winner and asymptotic agreement results under probabilistic single-peaked cultures, rather than a worst-case bound across all realized odd-electorate profiles. The stated theorem is a sharp finite-agenda quantity in that gap, not a rediscovery of the already-known existence of Borda–Condorcet disagreement.

## Limitations

The exact maximum is only for **strict single-peaked rankings and a unique Borda winner**, odd voter totals, equal voter weights, and consecutive **index** positions along a common axis. Tied Borda correspondences, even voter totals, other positional scores, multidimensional issue spaces, non-axis-aligned rankings, strategic ballots, and metric policy distances are not classified. The verified novelty assessment is bibliographic rather than an independent priority determination: older extreme-deviation results under alternate terminology may exist, and some historically relevant source texts are not freely accessible.

## References

1. D. Black, *On the Rationale of Group Decision-making*, Journal of Political Economy **56** (1948), 23–34. DOI: 10.1086/256633 (publisher records publication date 1948-02-01).
2. S. L. Feld and B. Grofman, *The Borda count in n-dimensional issue space*, Public Choice **59** (1988), 167–176. DOI: 10.1007/BF00054452. Author-hosted full text: https://sites.socsci.uci.edu/~bgrofman/R32-Feld-Grofman-Borda%20count%20in%20n-dimensional%20issue%20space.pdf
3. C. Klamler, *Borda and Condorcet: Some distance results*, working paper (September 2003), subsequently Theory and Decision **59** (2005), 97–109. DOI: 10.1007/s11238-005-5459-y.
4. V. Mousseau, H. Surugue, and A. Wilczynski, *Agreement Among Voting Rules Under Single-Peaked Preference Distributions*, ECAI (2025), DOI: 10.3233/FAIA251226. Open full text: https://www.ac.tuwien.ac.at/comsoc2025/comsoc2025-papers/107.pdf

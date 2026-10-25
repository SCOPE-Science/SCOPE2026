# Exact geometric domination numbers for the prime tori of orders five and seven

## Finding

Let \(T_p=\mathbb{F}_p^2\) for a prime \(p\), with its lines the affine lines over \(\mathbb{F}_p\). Define \(D_p\) to be the minimum cardinality of a set \(S\subseteq T_p\) such that every point of \(T_p\) lies on a line determined by two points of \(S\). Then
\[
D_5=5,\qquad D_7=6.
\]

## Assumptions and scope

For prime \(p\), the discrete torus \(\mathbb{Z}_p\times\mathbb{Z}_p\) is the affine plane \(\mathbb{F}_p^2\). A line through distinct \(a,b\in\mathbb{F}_p^2\) is \(\{a+t(b-a):t\in\mathbb{F}_p\}\), equivalently the image of an integer line under reduction modulo \(p\). A set \(S\) dominates \(T_p\) when every torus point is in \(S\) or belongs to at least one line through a pair of distinct points of \(S\). Only the two orders \(p=5,7\) are classified here.

## Proof

**A counting lower bound.** If \(|S|=s\), each pair of selected points determines a line containing at most \(p-2\) points outside \(S\). Thus the number of points covered is at most
\[
s+\binom{s}{2}(p-2).
\]
For \(s\leq4\), this is at most \(4+6(5-2)=22<25\) when \(p=5\), and at most \(4+6(7-2)=34<49\) when \(p=7\). Therefore \(D_5\geq5\) and \(D_7\geq5\).

**A five-point dominator for \(T_5\).** Take
\[
S_5=\{(0,0),(0,1),(1,0),(1,2),(3,2)\}\subseteq\mathbb{F}_5^2.
\]
The pair-lines include the vertical lines \(x=0,1\) and the eight lines
\[
y=0,\ 2,\ x+1,\ x+4,\ 2x,\ 2x+1,\ 4x,\ 4x+1
\pmod 5.
\]
The two vertical lines cover their columns. For each \(x\in\{2,3,4\}\), the eight displayed lines attain every residue \(y\in\mathbb{F}_5\). Hence \(S_5\) dominates all \(25\) points, so \(D_5=5\).

**No five-point dominator for \(T_7\).** Suppose \(|S|=5\). If three selected points are collinear, the line containing that triple contributes at most \(7-3=4\) points outside \(S\); there are at most seven other distinct pair-lines, each contributing at most \(7-2=5\) outside points. The union therefore covers at most \(4+7\cdot5=39<44\) points outside \(S\), so it cannot dominate.

It remains to consider a five-point set with no three collinear. Its ten pair-lines are distinct, each containing exactly five points outside \(S\), for \(50\) external incidences in total. There are
\[
\binom{5}{2}\binom{3}{2}/2=15
\]
unordered pairs of disjoint pair-lines: each of the ten lines is disjoint in endpoints from three others, and each pair is counted twice. There are eight affine directions in \(\mathbb{F}_7^2\). In any one direction, at most two pair-lines can occur, since each such line contains at most two selected points and there are only five selected points. Thus at most eight of the fifteen disjoint-line pairs are parallel. At least seven such pairs are nonparallel and meet at finite points outside \(S\).

At any point outside \(S\), at most two of these ten pair-lines can meet: distinct lines through that point use disjoint pairs of selected endpoints, so three such lines would require six selected points. Consequently the at least seven nonparallel intersections are seven distinct points, each counted twice in the \(50\) external incidences. At most \(50-7=43\) distinct external points are covered, fewer than the \(49-5=44\) external points. No five-point set dominates \(T_7\), so \(D_7\geq6\).

**A six-point dominator for \(T_7\).** Take
\[
S_7=\{(0,0),(0,1),(0,2),(1,0),(1,1),(5,2)\}\subseteq\mathbb{F}_7^2.
\]
Its pair-lines include the vertical lines \(x=0,1\) and the eleven lines
\[
y=0,\ 1,\ 2,\ x,\ 2x+6,\ 3x+1,\ 4x+3,\ 5x+2,\ 6x,\ 6x+1,\ 6x+2
\pmod 7.
\]
The vertical lines cover the columns \(x=0,1\). Substitution of each \(x\in\{2,3,4,5,6\}\) into the eleven displayed equations gives all seven residues for \(y\). Hence every point is covered and \(D_7\leq6\). Together with the lower bound, \(D_7=6\).

## Verification

The proof gives analytic lower bounds for sets of size at most four, a secant-intersection obstruction for five points in \(T_7\), and explicit witnesses for both upper bounds. The accompanying standard-library program `verify.py` checks both witness coverages by exact modular arithmetic and independently exhausts all \(\binom{49}{5}=1{,}906{,}884\) five-point subsets of \(T_7\); it finds no five-point dominator. Running `python3 verify.py` prints `CHECKS_PASSED`. The enumeration is finite corroboration, not an infinite theorem; the stated classification is only for \(p=5,7\).

## Relationship to prior work

Aichholzer, Eppstein, and Hainzl define the same minimum geometric domination invariant on the discrete torus. Their 2022 preprint gives a square-root lower bound and an \(O(\sqrt{p\log p})\) upper bound for prime orders, proves a four-point upper bound for even orders or orders divisible by three, and explicitly asks for which torus orders the exact domination number is known. Those statements do not imply the exact values \(D_5=5\) or \(D_7=6\).

Fowler, Groot, Pandya, and Snapp study the same torus line model but the different maximum problem of selecting as many points as possible with no three collinear. That maximum-general-position invariant does not determine the minimum size of a set whose pair-lines cover the entire torus.

## Limitations

The result gives two finite exact values, not a formula or asymptotic improvement for general prime orders. The exhaustive check is reproducible, but the proof of nonexistence is also supplied analytically. Literature and database searches cannot establish global novelty; unindexed or differently named work remains a residual risk. Independent audit has not been performed.

## References

1. O. Aichholzer, D. Eppstein, and E.-M. Hainzl, “Geometric Dominating Sets,” arXiv:2203.13170 (first public posting 2022-03-24); *Computational Geometry* 108 (2023), article 101913, DOI: 10.1016/j.comgeo.2022.101913.
2. J. Fowler, A. Groot, D. Pandya, and B. Snapp, “The no-three-in-line problem on a torus,” arXiv:1203.6604 (2012).

# Exact four-stake phase diagram for the Bernoulli averaging problem
## Finding
For \(0<p\le t\le1\), let \(B_1,\ldots,B_4\) be independent Bernoulli variables with common success probability \(p\). For a stake vector \(w=(w_1,\ldots,w_4)\) with \(w_i\ge0\) and \(\sum_iw_i=1\), put
\[
S_w=\sum_{i=1}^4w_iB_i,
\quad
M_4(p,t)=\max_w\Pr(S_w\ge t),
\quad q=1-p.
\]
Then
\[
\boxed{M_4(p,t)=
\begin{cases}
1-q^4,&0<t\le1/4,\\
1-q^3,&1/4<t\le1/3,\\
1-q^2,&1/3<t\le1/2,\\
\max\{p,3p^2-2p^3\},&1/2<t\le2/3,\\
p,&2/3<t\le1.
\end{cases}}
\tag{1}
\]
Every maximum in (1) is attained by an equal-stake strategy with at most four positive stakes. Explicit choices, including zeros, are
\[
(1/4,1/4,1/4,1/4),\quad
(1/3,1/3,1/3,0),\quad
(1/2,1/2,0,0),\quad
(1,0,0,0)
\]
in the respective initial three and final threshold ranges. For \(1/2<t\le2/3\), the one-stake strategy is optimal for \(p\le1/2\), while the three-equal-stake strategy is optimal for \(p\ge1/2\); both are optimal when \(p=1/2\). No uniqueness of optimizers is asserted.

## Assumptions and scope
The coin tosses are independent and identically distributed, their success probability satisfies \(0<p\le t\le1\), and four nonnegative stake positions (possibly zero) sum to exactly one. The event uses a non-strict threshold \(\ge\), so equality at \(t=1/4,1/3,1/2,2/3\) matters.

This is the full four-stake finite-dimensional problem, not the unrestricted problem over an arbitrary number of positive stakes. No asymptotic limit or numerical discretization is part of the theorem.

## Proof
Call a subset \(J\subseteq\{1,2,3,4\}\) *winning* if \(\sum_{j\in J}w_j\ge t\). The winning subsets form an upward-closed family. A *winning singleton* is an index \(i\) for which \(w_i\ge t\). Let \(s\) be the number of winning singletons.

**Case \(0<t\le1/4\).** Since \(t>0\), the empty successful set is impossible. Therefore \(\Pr(S_w\ge t)\le1-q^4\). Four equal stakes attain this bound.

**Case \(1/4<t\le1/3\).** Four winning singletons would give \(\sum_iw_i\ge4t>1\), so \(0\le s\le3\). On the event that at least one winning singleton succeeds, the threshold is already reached; conditional on all of them failing, success requires at least two successes among the other \(4-s\) tosses. Consequently,
\[
\Pr(S_w\ge t)
\le1-q^s+q^s\Pr\{\operatorname{Bin}(4-s,p)\ge2\}.
\tag{2}
\]
For each integer \(s\in\{0,1,2,3\}\), a direct expansion gives
\[
(1-q^3)-\left(1-q^s+q^s\Pr\{\operatorname{Bin}(4-s,p)\ge2\}\right)
=(3-s)pq^3\ge0.
\]
The vector with three stakes equal to \(1/3\) attains \(1-q^3\).

**Case \(1/3<t\le1/2\).** Now \(s\le2\). If \(s=2\), the other stakes sum to at most \(1-2t<t\), so success is equivalent to success of at least one of the two winning singletons. Its probability equals \(1-q^2\). If \(s=1\), the same conditioning gives
\[
\Pr(S_w\ge t)\le p+q\Pr\{\operatorname{Bin}(3,p)\ge2\}
=p+q(3p^2-2p^3).
\]
The gap to \(1-q^2\) is exactly
\[
pq^2(1-2p)\ge0
\]
because \(p\le t\le1/2\). If \(s=0\), success needs at least two of all four tosses, so
\[
\Pr(S_w\ge t)\le6p^2-8p^3+3p^4.
\]
The gap to \(1-q^2\) is
\[
pq^2(2-3p)\ge0.
\]
Two stakes of size \(1/2\) attain \(1-q^2\).

**Case \(1/2<t\le2/3\).** A winning singleton, if present, is unique and all remaining stakes sum to at most \(1-t<t\); thus the winning event is exactly the success of that singleton and has probability \(p\). Suppose no singleton wins. Form the graph \(G\) on the four indices whose edges are winning pairs. Two disjoint edges cannot both win, since their total weight would exceed \(2t>1\). Every pairwise-intersecting edge family on four vertices is either contained in a star or in a triangle, or is empty.

If the winning edges form a triangle on three vertices, every winning subset has at least two of those three vertices: a winning singleton is excluded; every winning pair is in the triangle, and every subset of size three or four meets the triangle in at least two vertices. Therefore
\[
\Pr(S_w\ge t)\le\Pr\{\operatorname{Bin}(3,p)\ge2\}=3p^2-2p^3.
\]
If all winning edges lie in a star centered at index \(i\), a winning set with \(B_i=1\) needs at least one other success, and a winning set with \(B_i=0\) needs all three other successes. Thus
\[
\Pr(S_w\ge t)
\le p(1-q^3)+qp^3
=3p^2-2p^3.
\]
If there is no winning pair, a winning set must have at least three successes, and
\[
\Pr(S_w\ge t)\le4p^3-3p^4
\le3p^2-2p^3,
\]
where the difference in the final inequality equals \(3p^2q^2\). Thus the maximum is \(\max\{p,3p^2-2p^3\}\), achieved by either one stake or three equal stakes. Their difference is
\[
(3p^2-2p^3)-p=pq(2p-1).
\]

**Case \(2/3<t\le1\).** A winning singleton forces the winning event to be the success of that singleton, giving \(p\). Suppose no singleton wins. As above, winning pairs form an intersecting edge family. A winning triangle of pairs is now impossible: summing its three pair weights gives at most \(2\), but winning each would require at least \(3t>2\).

If two winning edges share a vertex \(i\), say \(\{i,j\}\) and \(\{i,k\}\), then the triple consisting of the other three vertices cannot win: adding its weight to those two winning pair weights gives at most \(2\), whereas three winning conditions would require more than \(2\). Thus every winning subset contains \(i\), so its probability is at most \(p\).

If exactly one pair \(\{i,j\}\) wins, the two triples \(\{i,k,l\}\) and \(\{j,k,l\}\) cannot both win, since together with the winning pair their weights sum to exactly \(2<3t\). Therefore either every winning subset contains \(i\) or every winning subset contains \(j\); again the probability is at most \(p\).

Finally suppose no pairs win. Winning subsets must have three or four elements. If at most three triples win, then
\[
\Pr(S_w\ge t)\le3p^3q+p^4\le p,
\]
as
\[
p-(3p^3q+p^4)=pq^2(1+2p)\ge0.
\]
If all four triples win, summing their weights gives \(3\ge4t\), so \(t\le3/4\) and hence \(p\le3/4\). The probability is then at most
\[
4p^3q+p^4=4p^3-3p^4\le p,
\]
because
\[
p-(4p^3-3p^4)=pq(1+p-3p^2)\ge0
\]
for \(0\le p\le3/4\). The one-stake strategy always attains \(p\). This completes all cases and establishes (1).

## Verification
The accompanying standalone Python script `verify.py` performs exact rational checks. It enumerates weight vectors on several finite simplex grids and all sixteen Bernoulli outcomes. For each tested pair satisfying \(0<p\le t\le1\), it compares the exact event probability against (1). It separately verifies that all displayed equal-stake strategies attain their predicted pieces, including threshold endpoints and the \(p=1/2\) switch. The script uses `fractions.Fraction` throughout and requires only the Python standard library.

Finite sampling is not an exhaustive proof over real weights, probabilities, or thresholds. The case analysis above is the proof.

## Relationship to prior work
Fokkink, Meester, and Pelekis formulate Csóka's conjecture that an optimal convex combination of identically distributed Bernoulli variables is an equal-stake average when the threshold is at least the success probability. They prove the conjecture in several regions of the parameter triangle, leaving gaps. Their Theorem 4.4, Corollaries 5.2–5.4, and Theorem 6.1 establish stronger *unrestricted-number-of-stakes* results in subregions; these portions of (1) are therefore already implied by published work.

The new assertion is a complete two-parameter formula with arbitrary nonnegative weights in **all four positions**, including within the published gap. For example \(p=3/10\) and \(t=31/100\) are not in the stated low-probability sufficient regime of Theorem 6.1, nor in the high-threshold or exactly-one-third special cases, while (1) proves the four-stake optimum \(1-(7/10)^3\). It does not establish this optimum when five or more stakes are allowed.

The paper credits Fishburn, Frankl, Freed, Lagarias, and Odlyzko for the optimal \(p\)-weight of intersecting families; that earlier theorem implies several high-threshold comparisons here, but an intersecting-family bound alone does not yield the low-threshold four-stake classification. The proof uses elementary winning-set graphs and the explicit four-coordinate weight constraint.

## Limitations
The result concerns **at most four** positive stake positions. It neither settles Csóka's general conjecture nor proves a dimension-free bound. No uniqueness classification of all optimizing stake vectors is claimed.

Some parameter subregions of (1) are already covered by published stronger theorems; the genuinely new part is the *complete finite-dimensional classification* across their gaps. An equivalent small-dimension weighted-threshold-family result under older combinatorial/game-theoretic terminology remains a bibliographic risk.

## References
1. R. Fokkink, L. Meester, and C. Pelekis, “Optimizing stakes in simultaneous bets,” arXiv:2002.06804v1, publicly posted 17 February 2020; *ALEA, Latin American Journal of Probability and Mathematical Statistics* 20 (2023), 153–165. DOI: 10.30757/ALEA.v20-07.
2. P. C. Fishburn, P. Frankl, D. Freed, J. C. Lagarias, and A. M. Odlyzko, “Probabilities for Intersecting Systems and Random Subsets of Finite Sets,” *SIAM Journal on Algebraic and Discrete Methods* 7 (1986), 73–79. DOI: 10.1137/0607009.

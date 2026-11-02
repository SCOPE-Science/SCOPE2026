# Popular roomings and maximum mixing under unanimous heterophily

## Finding

**Theorem.** Let \(s\ge2\) and \(m\ge1\) be integers. Partition \(sm\) individually labeled agents into \(m\) *unlabeled* rooms, each holding exactly \(s\) agents. There are \(r\ge0\) red agents and \(b\ge0\) blue agents, with \(r+b=sm\). Every agent strictly prefers more roommates of the opposite type and is indifferent between arrangements producing the same number. An outcome \(\pi\) is **popular** if for every competing outcome \(\sigma\), at least as many agents strictly prefer \(\pi\) to \(\sigma\) as strictly prefer \(\sigma\) to \(\pi\).

Let \(h(\pi)\) be the number of rooms containing both types, and let \(H=\min\{m,r,b\}\). Whenever either \(s=3\) **or** \(\min\{r,b\}\le m\),

\[
\boxed{\pi\text{ is popular}\quad\Longleftrightarrow\quad h(\pi)=H.}
\]

This is stronger than mere existence: every outcome with \(H\) mixed rooms *strictly wins its pairwise popularity comparison* against every outcome with fewer mixed rooms, independently of which labeled agents occupy those rooms. Two outcomes each having \(H\) mixed rooms tie their popularity comparison. Consequently the popular set is exactly the set of maximum-cross-type-room allocations, and it can be recognized and constructed in linear time in the number of agents.

**Exact count.** Let \(P_{s,m}(r,b)\) denote the number of popular partitions of these labeled agents into unlabeled rooms. If \(c=\min\{r,b\}\le m\) and \(d=sm-c\),

\[
\boxed{P_{s,m}(r,b)=\frac{d!}{((s-1)!)^c(s!)^{m-c}(m-c)!}.}
\]

In the remaining three-person regime \(s=3\), \(m<r<2m\) (so that also \(m<b<2m\)),

\[
\boxed{P_{3,m}(r,3m-r)=\frac{r!(3m-r)!}{2^m(2m-r)!(r-m)!}.}
\]

The second formula also agrees with the first at the two boundary splits \(r=m\) and \(r=2m\). For example, the popular-partition counts at \((s,m,r,b)=(3,2,3,3),(3,3,3,6),(3,3,4,5),(3,4,6,6)\) are respectively \(9,90,180,8100\).

## Assumptions and scope

Agents are distinct, rooms are not labeled, room sizes are fixed and identical, and transfers or partial assignments are not permitted. There are exactly two fixed types. Preferences are **strictly heterophilic**: for a red agent in a room with \(j\) red agents (including themself), the utility representative is \(s-j\); for a blue agent in that room it is \(j\). These integer utilities encode the relevant ordinal ranking, not interpersonal welfare weights. Popularity is the head-to-head agent-vote criterion, not core stability, Pareto efficiency or the existence of a popular lottery. Equality of two room-level utilities is agent indifference and contributes no vote.

The theorem covers all color splits when \(s=3\), as well as any larger room size for which the less numerous type has at most \(m\) members. It does not assert any classification for \(s\ge4\) when \(\min(r,b)>m\). The degenerate one-color cases are included.

## Proof

**1. Attainable maximum and its structure.** Each mixed room contains at least one agent of each color, hence \(h(\pi)\le H\). If \(c=\min(r,b)\le m\), place one minority agent in each of \(c\) separate rooms, give each such agent \(s-1\) majority roommates, and fill the other \(m-c\) rooms entirely with majority agents. This realizes \(H=c\). Conversely, achieving \(c\) mixed rooms requires exactly one minority agent in each and none elsewhere, so this describes *every* maximum-mixing composition in the sparse-minority regime. If \(s=3\) and \(m\le r\le2m\), both colors have at least \(m\) agents; all \(m\) rooms can be made mixed. Every such room has exactly one or two red agents. Writing \(a\) for the number with one red and \(d\) for the number with two reds, the equations \(a+d=m\), \(a+2d=r\) force \(a=2m-r\) and \(d=r-m\). Thus these maximum-mixing compositions are also completely determined.

**2. Sparse-minority comparisons in every room size.** By exchanging the two colors, assume red is the minority, with \(r=c\le m\). Fix a maximum-mixing outcome \(\pi\). All red agents then have utility \(s-1\); exactly \((s-1)c\) blue agents have utility \(1\), and the remaining blue agents have utility \(0\). No red agent can improve over \(\pi\).

For an arbitrary competing outcome \(\sigma\), write \(y_j\) for its number of rooms with exactly \(j\) red agents, where \(0\le j\le s\). Then \(c=\sum_{j=0}^s j y_j\). The number of blue agents having positive utility in \(\sigma\) is

\[
T=\sum_{j=1}^{s-1}(s-j)y_j
  =(s-1)c-s\sum_{j=2}^{s}(j-1)y_j.
\]

Let \(A\) be the number of blue agents with utility \(0\) in \(\pi\) but positive utility in \(\sigma\), and \(B\) the number moving from utility \(1\) in \(\pi\) to zero in \(\sigma\). Counting positive blue utilities in both allocations gives

\[
A-B=-s\sum_{j=2}^{s}(j-1)y_j.
\]

Every blue improvement is either a move from zero to positive utility (at most \(A\) agents), or from utility \(1\) to more than \(1\), which requires occupying one of the at most \(\sum_{j=2}^{s}(s-j)y_j\) blue places in rooms with at least two reds. Every blue loss is exactly one of the \(B\) moves from one to zero. In addition, exactly \(\sum_{j=2}^{s}j y_j\) red agents lose utility, since they had the maximal \(s-1\) before and now share with another red.

Therefore the *challenger's net vote margin* satisfies

\[
\begin{aligned}
\#(\sigma\succ\pi)-\#(\pi\succ\sigma)
&\le A+\sum_{j=2}^{s}(s-j)y_j-B-\sum_{j=2}^{s}j y_j\\
&=-\sum_{j=2}^{s}\bigl(j(s+2)-2s\bigr)y_j.
\end{aligned}
\]

For every \(j\ge2\), \(j(s+2)-2s\ge4\). Thus \(\pi\) strictly defeats any \(\sigma\) with some \(y_j>0\) for \(j\ge2\); such a challenger has fewer than \(c\) mixed rooms. If all \(y_j=0\) for \(j\ge2\), then \(\sigma\) also has exactly \(c\) one-minority rooms. In that case all red utilities are equal and both allocations give exactly \((s-1)c\) blue agents utility \(1\), so each blue gain balances a blue loss. Their vote margin is precisely zero. The symmetric majority/minority orientation follows by exchanging colors.

**3. The remaining three-person regime.** Let \(s=3\) and \(m<r<2m\), and choose an all-mixed \(\pi\). Each mixed triple has exactly one minority-color occupant with utility \(2\) and two occupants with utility \(1\). Accordingly \(\pi\) has exactly \(m\) utility-two agents, all others having utility one. A competing outcome \(\sigma\) with \(h\) mixed rooms has exactly \(h\) utility-two agents; agents in pure rooms have utility zero.

Write \(U\) for the number of agents improving from utility \(1\) in \(\pi\) to utility \(2\) in \(\sigma\), and \(L\) for the number of agents losing utility \(2\) from \(\pi\). No other improvement is possible. The number of utility-two agents in \(\sigma\) is \(m+U-L=h\), so \(L-U=m-h\). The challenger has only \(U\) improvement votes and at least \(L\) worsening votes. Hence the original outcome's majority margin is at least \(m-h\), strictly positive whenever \(h<m\). If \(h=m\), no agent can receive zero utility, and the margin is exactly zero. This proves the classification and the strong comparison statements in all cases.

**4. Enumeration.** In the sparse-minority regime every minority label uniquely identifies a mixed room. Allocate \(s-1\) majority agents to each of the \(c\) individually distinguished minority agents, then partition the remaining \(s(m-c)\) majority agents into \(m-c\) unlabeled pure rooms. This gives

\[
\frac{d!}{((s-1)!)^c(s!)^{m-c}(m-c)!}.
\]

For all-mixed triples the numbers of rooms of the two compositions are \(a=2m-r\) and \(d=r-m\). The number of labeled-agent partitions into these unlabeled rooms is

\[
\frac{r!b!}{(1!\,2!)^a(2!\,1!)^d a!d!}
=\frac{r!b!}{2^m(2m-r)!(r-m)!}.
\]

**5. Complexity.** Counting mixed rooms examines each agent once. A maximizing partition can be constructed by the explicit arrangement in Step 1; hence a popular outcome can be built and checked in \(O(sm)\) time, assuming the agents' type labels are given.

## Verification

Run `python3 verify_popularity.py` in the directory containing this document and the standalone verifier. The verifier uses only the Python standard library. A direct enumeration of all labeled three-person room partitions for \(m=1,2,3\) checks \(21\) population splits. An independent exact-integer assignment optimization compares all composition profiles for \(m=1,\ldots,7\) in the triple case (\(329\) composition profiles and \(1843\) composition-pair checks) and for sparse minorities with \(s=2,\ldots,7\), \(m=1,\ldots,6\) (\(403\) profile checks). These are finite corroborations; the proof above establishes the all-size result.

## Relationship to prior work

Boehmer and Elkind (2020) develop the roommate diversity model and analyze core, exchange, Pareto and envy-free properties; their results are not pairwise majority-popularity classifications. Ge and Itoh (2022) establish polynomial-time popular outcomes for arbitrary preferences when room size is two and give hardness results at variable room sizes. The sparse-minority statement above extends beyond room size two, while the all-split three-person statement supplies a full Condorcet-style popularity characterization for a uniform strictly diversity-seeking preference family. Ge and Itoh (2023) study popularity under Euclidean-distance preferences in three-dimensional space, a different preference domain. Related literature may contain equivalent specializations not identified in this comparison.

## Limitations

The result requires every agent to strictly prefer more opposite-type roommates. It does not cover a mixture of homophilic and heterophilic agents, type-specific ideal diversity ratios, nonuniform room sizes, or color splits with \(s\ge4\) and \(\min(r,b)>m\). A popular outcome is not necessarily strictly popular in the uniqueness sense: different maximizing partitions are pairwise tied. The analytic proof does not rely on finite enumeration. Independent external validation and an exhaustive specialist-literature priority determination have not been performed.

## References

- S. Ge and T. Itoh, *Popularity on the Roommate Diversity Problem*, arXiv:2210.07911 (first public arXiv posting October 14, 2022), https://arxiv.org/abs/2210.07911.
- N. Boehmer and E. Elkind, *Stable Roommate Problem with Diversity Preferences*, arXiv:2004.14640 (first public posting April 30, 2020), https://arxiv.org/abs/2004.14640; IJCAI 2020.
- S. Ge and T. Itoh, *Popularity on the 3D-Euclidean Stable Roommates*, arXiv:2311.10585 (first public posting November 17, 2023), https://arxiv.org/abs/2311.10585.

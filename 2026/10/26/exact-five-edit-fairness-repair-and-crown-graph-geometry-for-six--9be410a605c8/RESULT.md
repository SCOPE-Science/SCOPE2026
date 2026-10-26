# Exact five-edit fairness repair and crown-graph geometry for six-voter majority extensions

## Finding

Consider every resolute, monotone, candidate-neutral, two-alternative voting rule on **six labeled voters** that agrees with simple majority whenever the sides differ in size. Among the \(2^{10}=1024\) such rules, exactly \(12\) give equal Banzhaf influence to all voters. These are exactly the \(12\) rules giving equal Shapley–Shubik influence, and each is a balanced choice of one triple from every complementary pair of triples.

A *tie-pair edit* reverses the outcomes on both opposite profiles associated with one complementary pair of three-voter coalitions; this preserves monotonicity, neutrality, and majority agreement. Let \(d(f)\) be the minimum number of these edits needed to reach a rule fair under both indices. The complete number of rules at each repair distance is

\[
\begin{array}{c|rrrrrr}
 d(f)&0&1&2&3&4&5\\\hline
 \#\{f\}&12&120&360&380&140&12.
\end{array}
\]

Consequently **every rule can be made power-fair with at most five tie-pair edits**, and the bound is sharp. The twelve hardest rules are precisely the six rules that give all tied outcomes to a particular voter's chosen side, and their six opposites that give all tied outcomes against a particular voter.

The fair rules themselves form a binary length-ten set of minimum Hamming distance \(4\). Their unordered pair-distance distribution is \(30\) pairs at distance \(4\), \(30\) at distance \(6\), and \(6\) at distance \(10\). Connecting two fair rules when four tie-pair edits separate them gives the crown graph \(K_{6,6}\) with one perfect matching deleted. There is one voter-relabeling orbit, with automorphism group of size \(60\).

## Assumptions and scope

Let \(N=\{0,1,2,3,4,5\}\). A coalition \(S\subseteq N\) consists of those voting for the first of two alternatives, and \(f(S)\in\{0,1\}\) denotes whether it wins. A rule is **monotone** if \(S\subseteq T\) entails \(f(S)\le f(T)\), **neutral** if \(f(N\setminus S)=1-f(S)\), and **majority-preserving** if \(f(S)=0\) for \(|S|\le2\) and \(f(S)=1\) for \(|S|\ge4\).

Thus only the twenty tied coalitions \(|S|=3\) remain variable. Their ten unordered complementary pairs \(\{S,N\setminus S\}\) are independent: one member must win, and either orientation respects all three axioms. Label these pairs in increasing numerical order of the six-bit mask of the member not containing voter \(5\); their representatives are

`012, 013, 023, 123, 014, 024, 124, 034, 134, 234`.

The ten binary decisions form a word \(z\in\{0,1\}^{10}\), whose bit is one when the displayed representative wins. Hamming distance between words is exactly the number of tie-pair edits, *not* the number of individual tied profiles changed (each edit changes two such profiles). No statements are made here about rules that fail majority preservation, elections with a different voter count, voter weights, or preference intensity.

For voter \(i\), its Banzhaf influence is the fraction of all \(2^5\) coalitions of the other voters on which adding \(i\) changes defeat to victory; its Shapley–Shubik influence is the probability that \(i\) is pivotal in a uniformly random order of all six voters. Fairness means equality of the six corresponding indices, with no requirement of anonymity.

## Proof

**1. A linear fairness criterion.** Every orientation has ten winning triples. Write \(t_i\) for the number of those containing voter \(i\). There are exactly \(t_i\) pivotal coalitions of size two (their union with \(i\) is a winning triple). Among coalitions of size three avoiding \(i\), exactly \(t_i\) are losing: there are ten such triples, while the number winning and avoiding \(i\) is \(10-t_i\). All other coalition sizes cannot be pivotal. Therefore voter \(i\) has exactly \(2t_i\) Banzhaf swings and

\[
\beta_i=\frac{2t_i}{32}=\frac{t_i}{16},\qquad
\phi_i=\frac{2t_i\,(2!3!)}{6!}=\frac{t_i}{30}.
\]

The sum \(\sum_i t_i=30\), since there are ten winning triples of size three. Hence either index is equal for every voter if and only if

\[
(t_0,t_1,t_2,t_3,t_4,t_5)=(5,5,5,5,5,5).
\]

In fact, such a balanced family contains every pair of voters in exactly two winning triples: for distinct \(i,j\), let \(a_{ij}\) be the number of winning triples containing both. Exactly four triples avoid both, and by complementation their number of winners is \(4-a_{ij}\); by inclusion–exclusion it is \(10-5-5+a_{ij}=a_{ij}\). Thus \(a_{ij}=2\). This identifies the familiar \(2\)-\((6,3,2)\) biplane but does not presume its uniqueness or the full repair distances.

**2. Exact finite classification certificate.** For a subset \(S\), encode it by \(b(S)=\sum_{i\in S}2^i\), a six-bit integer. Form

\[
P=\operatorname{sort}\bigl\{\min\{b(S),63-b(S)\}:|S|=3\bigr\},
\]

which has ten entries. For each integer \(0\le z<1024\), choose \(P_j\) as a winning triple if bit \(j\) of \(z\) is one, and otherwise choose its complementary triple \(63-P_j\). Direct integer sums compute \(t_i(z)\), and retain precisely those \(z\) for which all six sums equal five. Exhausting the explicitly bounded set of \(1024\) integers gives the *complete* list

`220, 234, 316, 358, 425, 453, 570, 598, 665, 707, 789, 803`.

No search limit, probabilistic extrapolation, or floating-point comparison is involved. For each of the \(1024\) words, evaluate \(d(z)=\min_{u\in F}\operatorname{popcount}(z\mathbin{\mathrm{xor}}u)\), where \(F\) is the displayed twelve-element set. Counting all entries gives exactly \(12,120,360,380,140,12\) at distances zero through five; these counts sum to \(1024\). In particular, no word lies farther than five from \(F\).

The twelve distance-five words are

`0, 15, 113, 183, 347, 402, 621, 676, 840, 910, 1008, 1023`.

For every specified voter \(i\), the rule that chooses a winning tied coalition precisely when it contains \(i\) and its opposite rule both occur in that list. These produce twelve different orientation words, so the list characterizes all extremal rules, proving sharpness and extremal rigidity.

**3. Geometry among fair rules.** Exact comparison of all \(\binom{12}{2}=66\) pairs of members of \(F\) gives Hamming distances \(4,6,10\) with respective multiplicities \(30,30,6\). The twelve words split into

`A = {220, 358, 425, 570, 707, 789}`

and

`B = {234, 316, 453, 598, 665, 803}`.

For every \(u\in A\), its five distance-four neighbors are exactly the members of \(B\) other than \(1023-u\); the same holds with the classes exchanged. Hence this graph is \(K_{6,6}\) minus the six antipodal edges. Permuting all six voter labels and applying them to the winning triples of word \(220\) produces every member of \(F\). As there are \(6!=720\) permutations and twelve distinct images, the stabilizer has \(720/12=60\) members.

Each integer assertion in steps 2 and 3 is independently replayable by the included `verify.py`. Its loops cover the full finite domains and check neutrality, monotonicity, exact swing counts, the biplane incidence, the repair histogram, antipodes, adjacency, and the voter-relabeling orbit. These finite computations are proofs of the stated **finite** classification, not claims about an infinite family.

## Verification

Run `python3 verify.py` using Python 3 and its standard library. The script uses exact integers only, enumerates all \(1024\) neutral majority extensions and all \(66\) pairs of fair choices, and checks Banzhaf and Shapley–Shubik indices from their original pivotal-coalition definitions. It also checks the twelve farthest rules against the twelve explicit tie-dictator and anti-dictator choices. An execution of this bundled program completed successfully with all assertions satisfied. See `VERIFICATION.md` for check details and limitations.

## Relationship to prior work

Dhar, Mittal, and Thomas (2026, arXiv:2602.13894v1), especially Proposition 2.2, Lemma 4.3, and Figure 2, give the power-index formulas and the link between unbiasedness and complementary balanced families, and explicitly identify the classical six-player `Icos` example. Its **existence** and the general biplane connection are not asserted to be new here. Loeb and Conway (2000) study transitive maximal intersecting families, including `Icos`; general classification of the unique \(2\)-\((6,3,2)\) design was already known. Khosrovshahi, Maimani, and Torabi (1999) classify six-point triple trades of volumes \(4,6,10\), consistent with the fair-to-fair Hamming distances, so those **possible distances alone** are not independently new.

The contribution isolated here is the **exact covering-radius and repair-distance profile of all 1024 majority-preserving neutral orientations relative to the fair families**, the characterization of the twelve worst repairs, and the explicit adjacency graph of the fair subset. The trade classification applies to differences between designs, whereas most input orientations in this theorem are not designs; it does not directly supply their full nearest-fair repair histogram.

## Limitations

This is a small, fully labeled, finite classification. Its accuracy is contingent on the explicit definitions and exact program, with no extrapolation to larger even electorates. The result is not an independent scholarly audit. Earlier descriptions of the icosahedral game, biplane labelings, trades, or covering codes might encode equivalent metric statements; those historical-priority risks deserve further external review. A precise match for the full repair distribution was not found in the inspected material, but absence from searches does not establish global priority.

## References

1. M. Dhar, K. Mittal, C. Thomas, *Existence of Fair Resolute Voting Rules*, arXiv:2602.13894v1 (first posted February 14, 2026), https://arxiv.org/pdf/2602.13894.
2. D. E. Loeb and A. R. Conway, *Voting Fairly: Transitive Maximal Intersecting Families of Sets*, Journal of Combinatorial Theory, Series A **91** (2000), 386–410, https://doi.org/10.1006/jcta.2000.3103.
3. G. B. Khosrovshahi, H. R. Maimani, R. Torabi, *Classification of simple 2-(6,3) and 2-(7,3) trades*, Australasian Journal of Combinatorics **19** (1999), 55–72, https://www.academia.edu/110519045/Classification_of_simple_2_6_3_and_2_7_3_trades.
4. *Modelling biplanes on surfaces*, European Journal of Combinatorics **25** (2004), 899–909, https://doi.org/10.1016/j.ejc.2003.05.004 (background on known small-biplane classification).

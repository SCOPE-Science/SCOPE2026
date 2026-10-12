# Sharp five-player dominance boundary for the Public Good index
## Finding
Let \(v\) be a proper simple voting game on a finite player set \(N\), with minimal winning coalitions \(\mathcal M(v)\).

The normalized **Public Good index** is
\[
PG_i(v)=
\frac{|\{S\in\mathcal M(v):i\in S\}|}
{\sum_{j\in N}|\{S\in\mathcal M(v):j\in S\}|}.
\]

For distinct players \(i,j\), write \(i\succeq j\) for **Isbell dominance** when
\[
v(S\cup\{j\})=1\Longrightarrow v(S\cup\{i\})=1
\]
for every coalition \(S\subseteq N\setminus\{i,j\}\).

Every proper simple game with at most \(4\) players satisfies
\[
i\succeq j\Longrightarrow PG_i(v)\ge PG_j(v).
\]

For \(5\) players there are exactly
\[
2645
\]
labeled proper simple games. Exactly
\[
460
\]
violate the displayed dominance implication. Thus the exact labeled incidence is
\[
\frac{460}{2645}=\frac{92}{529}.
\]

The \(460\) games form exactly
\[
9
\]
isomorphism classes under player relabeling. All nine classes are weighted voting games.

The numbers of labeled violating games with exactly one, two, or three violating directed dominance comparisons are respectively
\[
300,\qquad 120,\qquad 40.
\]

Using players \(A,B,C,D,E\), canonical representatives of the nine classes are shown below. Each listed weighted representation realizes every displayed dominance violation as a local-monotonicity violation because the dominating player has strictly larger voting weight but strictly smaller Public Good power.

| Minimal winning coalitions | Orbit | Weighted representation | Normalized \(PG\) | Violating comparisons |
| --- | ---: | --- | --- | --- |
| \(\{AB,ACD,ACE\}\) | \(60\) | \([8;5,3,2,1,1]\) | \((3/8,1/8,1/4,1/8,1/8)\) | \(B\succeq C\), \(PG_B<PG_C\) |
| \(\{AB,ACD,ACE,ADE\}\) | \(20\) | \([6;4,2,1,1,1]\) | \((4/11,1/11,2/11,2/11,2/11)\) | \(B\succeq C,D,E\), \(PG_B<PG_C=PG_D=PG_E\) |
| \(\{AB,ACD,ACE,BCDE\}\) | \(60\) | \([7;4,3,2,1,1]\) | \((1/4,1/6,1/4,1/6,1/6)\) | \(B\succeq C\), \(PG_B<PG_C\) |
| \(\{AB,ACD,ACE,ADE,BCDE\}\) | \(20\) | \([5;3,2,1,1,1]\) | \((4/15,2/15,1/5,1/5,1/5)\) | \(B\succeq C,D,E\), \(PG_B<PG_C=PG_D=PG_E\) |
| \(\{AB,ACD,BCD,ACE\}\) | \(120\) | \([9;5,4,3,2,1]\) | \((3/11,2/11,3/11,2/11,1/11)\) | \(B\succeq C\), \(PG_B<PG_C\) |
| \(\{AB,ACD,BCD,ACE,ADE\}\) | \(60\) | \([7;4,3,2,2,1]\) | \((2/7,1/7,3/14,3/14,1/7)\) | \(B\succeq C,D\), \(PG_B<PG_C=PG_D\) |
| \(\{AB,ACD,BCD,ACE,BCE\}\) | \(30\) | \([6;3,3,2,1,1]\) | \((3/14,3/14,2/7,1/7,1/7)\) | \(A\succeq C\), \(B\succeq C\), \(PG_A=PG_B<PG_C\) |
| \(\{AB,AC,BCD,BCE\}\) | \(30\) | \([7;4,3,3,1,1]\) | \((1/5,3/10,3/10,1/10,1/10)\) | \(A\succeq B,C\), \(PG_A<PG_B=PG_C\) |
| \(\{AB,ACD,BCD,ACE,BCE,ADE\}\) | \(60\) | \([9;5,4,3,2,2]\) | \((4/17,3/17,4/17,3/17,3/17)\) | \(B\succeq C\), \(PG_B<PG_C\) |

The orbit sizes sum to
\[
60+20+60+20+120+60+30+30+60=460.
\]

A particularly compact witness is
\[
\mathcal M(v)=\{AB,ACD,ACE\},
\]
with weighted representation
\[
[8;5,3,2,1,1].
\]
Here \(B\succeq C\), and the displayed representation has
\[
w_B=3>2=w_C,
\]
but
\[
PG_B=\frac18<\frac14=PG_C.
\]

Thus \(5\) players are the sharp first size for failure of Public-Good dominance within proper simple games, and also the sharp first size for a Public-Good local-monotonicity failure within proper weighted games.

## Assumptions and scope
A simple game is a monotone \(0\)-\(1\) cooperative game with the grand coalition winning. It is **proper** when no coalition and its complement are both winning.

Every simple game is represented uniquely by the antichain of its minimal winning coalitions.

The dominance relation used here is the usual desirability comparison restricted to single-player substitutions. It need not be total.

For a weighted representation
\[
[q;w_1,\ldots,w_n],
\]
local monotonicity requires
\[
w_i\ge w_j\Longrightarrow PG_i\ge PG_j.
\]
The theorem does not claim that the displayed integer representations are uniquely minimal; they are explicit certificates.

The exhaustive classification covers all proper simple games on one through five labeled players. No count for six or more players is asserted.

## Proof
The verifier enumerates every nonempty antichain of nonempty subsets of \(N\), interprets that antichain as the family of minimal winning coalitions, and filters exactly for properness.

The resulting numbers of labeled proper simple games for one through five players are
\[
1,\ 3,\ 11,\ 80,\ 2645.
\]
Their corresponding numbers of isomorphism classes are
\[
1,\ 2,\ 5,\ 14,\ 86.
\]

For every game the Public Good index is computed independently in two exact rational ways:
1. count the minimal winning coalitions containing each player and normalize the counts;
2. form the explicit player-minimal-coalition incidence multiset and normalize its player frequencies.

The two computations agree for every game.

Dominance is also tested independently in two equivalent ways.

First, for each ordered pair \(i,j\), every coalition
\[
S\subseteq N\setminus\{i,j\}
\]
is checked for the implication
\[
v(S\cup\{j\})=1\Longrightarrow v(S\cup\{i\})=1.
\]

Second, every winning coalition containing \(j\) but not \(i\) is checked after replacing \(j\) by \(i\). The two implementations agree for every ordered pair in every enumerated game.

No proper game on one through four players has a pair \(i\succeq j\) with \(PG_i<PG_j\).

At five players exactly \(460\) labeled games do. Canonicalization under all
\[
5!=120
\]
player permutations gives exactly nine canonical antichains, listed in the table above.

For each canonical class, an exact brute-force integer search finds the displayed weighted representation and verifies its truth table against the simple game. For every violating pair in every displayed representation, the dominating player has strictly greater weight and strictly smaller Public Good power. Therefore every one of the nine classes supplies a genuine local-monotonicity failure.

Counting the violating ordered dominance comparisons in all \(460\) labeled games gives
\[
300
\]
games with one,
\[
120
\]
with two, and
\[
40
\]
with three.

## Verification
The embedded `verify_public_good_dominance_first_layer.py` uses only the Python standard library and exact rational arithmetic.

It verifies:
- every proper simple game on one through five players;
- exact labeled counts \(1,3,11,80,2645\);
- exact isomorphism-class counts \(1,2,5,14,86\);
- two independent exact computations of the normalized Public Good index;
- two independent tests of the dominance relation;
- no Public-Good dominance violation through four players;
- exactly \(460\) labeled five-player violations;
- exact incidence \(92/529\);
- exactly nine violating isomorphism classes;
- orbit sizes summing to \(460\);
- the distribution \(300,120,40\) by one, two, or three violating comparisons;
- all nine displayed weighted representations;
- strict weight reversal for every displayed Public-Good dominance violation;
- the compact witness \(\{AB,ACD,ACE\}\) with representation \([8;5,3,2,1,1]\).

Run:

`python3 verify_public_good_dominance_first_layer.py`

The first output line must be `VERIFY_OK`.

## Relationship to prior work
Failure of local monotonicity for the Public Good index is already known and is not claimed here.

Holler and Napel discuss local monotonicity as a substantive property of voting power and give weighted examples where the Public Good index can assign less power to a voter with greater weight.

Freixas and Kurz explicitly state that the Public Good index violates local monotonicity and therefore can violate the dominance postulate. They prove dominance for uniform complete games and local monotonicity for uniformly weighted games. They also exhibit the four-player weighted game
\[
[3;2,1,1,1]
\]
with minimal winning coalitions
\[
\{AB,AC,AD,BCD\},
\]
noting that it is nonuniform yet still satisfies Public-Good dominance.

Those prior results establish both the pathology and substantial positive subclasses. They do not, in the inspected material, give the exhaustive smallest-size boundary proved here.

The contribution here is therefore restricted to the sharp finite classification: no proper simple-game violation through four players; exactly \(460\) labeled violations at five players; exactly nine isomorphism classes; and explicit weighted realizations of the complete first layer.

Targeted searches using Public Good and Holler terminology, dominance and local-monotonicity aliases, five-player and proper-simple-game restrictions, the exact counts, and representative weighted games did not locate an equivalent census.

## Limitations
The result concerns the normalized Public Good index, but normalization does not affect the dominance inequalities because it multiplies all raw Public Good scores in one game by the same positive constant.

The theorem is restricted to proper simple games through five players.

The displayed weighted representations certify local-monotonicity failures but are not claimed to be unique or representation-minimal.

The result does not classify the frequency or isomorphism types of violations for six or more players.

A historical table, software corpus, thesis appendix, or source not indexed by the searches could contain some or all of the same five-player census.

## References
1. M. J. Holler and S. Napel, “Local monotonicity of power: Axiom or just a property?”, *Quality & Quantity* 38 (2005), 637–647. DOI: 10.1007/s11135-005-4755-5.
2. J. Freixas and S. Kurz, “The cost of getting local monotonicity,” arXiv:1411.0944, first submitted 4 November 2014.

# Five alternatives are the sharp decisiveness boundary between Copeland and the uncovered set
## Finding
Let \(T=(A,\succ)\) be a finite tournament. The **Copeland set** is
\[
CO(T)=\{a\in A:\deg^+(a)=\max_{b\in A}\deg^+(b)\},
\]
and the **uncovered set** is the set of alternatives not covered by another alternative. Equivalently, \(a\in UC(T)\) exactly when \(a\) reaches every alternative by a directed path of length at most two.

The separation between these two tournament solutions has two distinct small-order thresholds.

First, they agree for every tournament on at most \(3\) alternatives. At order \(4\), disagreement first appears, but it is necessarily tie-based. Exactly
\[
24
\]
of the
\[
2^{\binom42}=64
\]
labeled four-alternative tournaments satisfy
\[
CO(T)\subsetneq UC(T).
\]
Every such tournament has
\[
(|CO(T)|,|UC(T)|)=(2,3),
\]
and all \(24\) are relabelings of one tournament.

Second, a **unique** Copeland winner can first coexist with a strictly larger uncovered set at order \(5\). Exactly
\[
280
\]
of the
\[
2^{\binom52}=1024
\]
labeled five-alternative tournaments have
\[
|CO(T)|=1,
\qquad
CO(T)\subsetneq UC(T).
\]
Thus the unconditional incidence is
\[
\frac{280}{1024}=\frac{35}{128}.
\]
There are exactly \(600\) labeled five-alternative tournaments with a unique Copeland winner, so the conditional incidence is
\[
\frac{280}{600}=\frac7{15}.
\]

The \(280\) decisive disagreements form exactly three isomorphism classes. Their orbit sizes and uncovered-set sizes are
\[
(120,3),\qquad (120,4),\qquad (40,5).
\]
Hence the labeled counts by uncovered-set size are exactly
\[
120,
\qquad
120,
\qquad
40.
\]
Every tournament in this first decisive layer has outdegree multiset
\[
\{3,2,2,2,1\}
\]
and top cycle equal to all five alternatives.

Using labels \(A,B,C,D,E\), representatives of the three five-alternative classes can be given by their directed edges:

1. \(A\succ D,A\succ E,B\succ A,C\succ A,C\succ B,D\succ B,D\succ C,E\succ B,E\succ C,E\succ D\). Here \(CO=\{E\}\) and \(UC=\{A,C,E\}\).
2. \(A\succ E,B\succ A,B\succ D,C\succ A,C\succ B,D\succ A,D\succ C,E\succ B,E\succ C,E\succ D\). Here \(CO=\{E\}\) and \(UC=\{A,B,C,D,E\}\).
3. \(A\succ B,A\succ E,B\succ D,C\succ A,C\succ B,D\succ A,D\succ C,E\succ B,E\succ C,E\succ D\). Here \(CO=\{E\}\) and \(UC=\{A,C,D,E\}\).

Thus the first set-level difference occurs at four alternatives only through a Copeland tie, while five alternatives are necessary and sufficient for the stronger phenomenon in which Copeland makes an unambiguous choice that the uncovered set still refuses to isolate.

## Assumptions and scope
A tournament is a finite complete asymmetric directed graph. Outdegree is the number of alternatives an alternative defeats.

An alternative \(x\) covers \(y\) when \(x\succ y\) and every alternative defeated by \(y\) is also defeated by \(x\). The uncovered set consists of the alternatives covered by nobody.

The **top cycle** is the set of alternatives that can reach every other alternative along a directed path of arbitrary finite length.

All counts are for labeled tournaments. Isomorphism means equality after relabeling alternatives.

The exhaustive classification covers every tournament through order \(5\). No frequency statement is made for orders \(6\) or larger.

## Proof
A tournament on \(n\) labeled alternatives is encoded by one orientation choice for each of the \(\binom n2\) unordered pairs. The verifier therefore exhausts exactly
\[
2^{\binom n2}
\]
tournaments for every \(1\le n\le5\).

For each tournament, the Copeland set is computed independently in two forms: directly from out-neighborhood cardinalities, and from an independently accumulated pairwise-win score vector. The two implementations agree on every tournament.

The uncovered set is also computed independently in two forms. The first constructs the covering relation directly. The second uses the classical two-step characterization: an alternative is uncovered exactly when it reaches every alternative in at most two directed steps. The two implementations agree on every tournament.

The exhaustive tuple
\[
(\text{total tournaments},\ \#\{CO\ne UC\},\ \#\{|CO|=1\},\ \#\{|CO|=1,CO\ne UC\})
\]
for orders \(1\) through \(5\) is
\[
\begin{array}{c|c}
 n & \text{tuple}\\ \hline
1&(1,0,1,0)\\
2&(2,0,2,0)\\
3&(8,0,6,0)\\
4&(64,24,32,0)\\
5&(1024,640,600,280).
\end{array}
\]
The containment
\[
CO(T)\subseteq UC(T)
\]
is checked in every case.

At order \(4\), all \(24\) strict cases have size pair \((2,3)\). Canonicalization under all \(4!\) relabelings yields a single class whose orbit has size \(24\).

At order \(5\), restricting to the \(280\) strict cases with a unique Copeland winner yields uncovered-set-size counts
\[
|UC|=3:120,
\qquad
|UC|=4:120,
\qquad
|UC|=5:40.
\]
Canonicalization under all \(5!\) relabelings yields exactly three classes, with orbit sizes \(120,120,40\). Their orbits are disjoint and their union has size \(280\).

Finally, direct inspection of every tournament in this decisive layer verifies that its sorted outdegree sequence is
\[
(3,2,2,2,1)
\]
and that every vertex belongs to the top cycle.

## Verification
The embedded `verify_copeland_uncovered_decisiveness.py` uses only the Python standard library.

It verifies:
- every labeled tournament through five alternatives;
- two independent Copeland-set implementations;
- two independent uncovered-set implementations;
- \(CO(T)\subseteq UC(T)\) throughout the tested domain;
- equality through three alternatives;
- exactly \(24\) four-alternative disagreements, all with size pair \((2,3)\), in one isomorphism class;
- exactly \(600\) five-alternative tournaments with a unique Copeland winner;
- exactly \(280\) decisive five-alternative disagreements;
- exact incidences \(35/128\) and \(7/15\);
- uncovered-set-size counts \(120,120,40\);
- exactly three decisive isomorphism classes with orbit sizes \(120,120,40\);
- outdegree multiset \(\{3,2,2,2,1\}\) throughout the decisive layer;
- full five-alternative top cycle throughout that layer.

Run:

`python3 verify_copeland_uncovered_decisiveness.py`

The first output line must be `VERIFY_OK`.

## Relationship to prior work
The Copeland and uncovered sets are classical tournament solutions. Brandt's tournament-solutions treatment defines the Copeland set as the alternatives of maximal outdegree and the uncovered set as the maximal elements of the covering relation. It also records the classical two-step, or tournament-king, characterization of uncovered alternatives and the known containment
\[
CO(T)\subseteq UC(T).
\]

That literature establishes the concepts, their inclusion relation, and their computational structure. It does not, in the inspected material, state the two-stage small-order boundary classified here: first set disagreement at order four but only through ties, followed at order five by the first unique-Copeland-versus-nonsingleton-uncovered disagreement, with exact labeled counts and three isomorphism classes.

Targeted searches using the solution names, the phrases “unique Copeland winner,” “five alternatives,” “uncovered set,” the exact count \(280\), the exact fractions \(35/128\) and \(7/15\), and isomorphism-class language did not locate an equivalent census.

## Limitations
This is a finite exact classification through five alternatives, not a general formula for larger tournaments.

The stronger order-five threshold concerns a unique Copeland winner together with a strictly larger uncovered set. Ordinary set disagreement already occurs at order four.

The three five-alternative classes are obtained by exhaustive canonicalization under all relabelings rather than by a separate symbolic classification theorem.

A historical data table, thesis appendix, software corpus, or unindexed enumeration could contain the same small-order counts.

## References
1. F. Brandt, “Minimal Stable Sets in Tournaments,” arXiv:0803.2138, first submitted 14 March 2008; later *Journal of Economic Theory* 146(4), 2011.
2. F. Brandt, *Tournament Solutions: Extensions of Maximality and their Applications to Decision-Making*, habilitation thesis, sections 7.1–7.2.
3. K. A. Shepsle and B. R. Weingast, “Uncovered Sets and Sophisticated Voting Outcomes with Implications for Agenda Institutions,” *American Journal of Political Science* 28(1), 1984.

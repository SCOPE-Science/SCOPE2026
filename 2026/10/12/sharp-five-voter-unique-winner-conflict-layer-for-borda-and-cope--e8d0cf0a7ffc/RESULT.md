# Sharp five-voter unique-winner conflict layer for Borda and Copeland
## Finding
Consider elections with exactly three candidates and complete strict ballots. Let \(B(P)\) be the Borda winner correspondence with scores \(2,1,0\), and let \(C(P)\) be the Copeland correspondence with pairwise contest scores \(1,1/2,0\).

No profile with at most \(4\) voters has different unique Borda and Copeland winners. With \(5\) voters, among all
\[
6^5=7776
\]
labeled profiles, exactly
\[
60
\]
have
\[
|B(P)|=|C(P)|=1,\qquad B(P)\ne C(P).
\]
Thus the exact impartial-culture incidence is
\[
\frac{60}{7776}=\frac5{648}.
\]

At the anonymous level there are
\[
\binom{10}{5}=252
\]
five-voter ballot-multiplicity profiles, and exactly \(6\) have different unique winners. Hence the impartial-anonymous-culture incidence is
\[
\frac6{252}=\frac1{42}.
\]

All \(60\) labeled conflicts are relabelings of candidates and voters of one profile:
\[
3(B\succ C\succ A)+2(C\succ A\succ B).
\]
Its Borda scores are
\[
(A,B,C)=(2,6,7),
\]
so \(C\) is the unique Borda winner. Its pairwise majority margins are
\[
(A-B,A-C,B-C)=(-1,-5,1),
\]
so \(B\) beats both opponents by majority and is the unique Condorcet and Copeland winner.

The boundary concerns **different unique winners**. Set-valued disagreements occur earlier only through ties: with \(3\) voters, \(18\) profiles have a unique Copeland winner inside a two-way Borda tie; with \(4\) voters, \(72\) profiles have a unique Borda winner inside a two-way Copeland tie.

## Assumptions and scope
There are exactly three candidates and every ballot is a complete strict ranking. No external tie-breaking rule is imposed.

Borda uses \(2,1,0\) positional scores. Copeland awards \(1\) for a pairwise win, \(1/2\) for a tie, and \(0\) for a loss.

The theorem exhausts electorates of sizes \(1\) through \(5\). The labeled incidence uses impartial culture; the anonymous incidence weights ballot-multiplicity vectors equally.

## Proof
There are \(6\) strict rankings of three candidates. For each
\[
n\in\{1,2,3,4,5\},
\]
all
\[
6^n
\]
labeled profiles are enumerated.

Borda is computed in two exact ways. The first uses positional scores \(2,1,0\). The second uses the identity that, with three candidates, a candidate's Borda score equals its total pairwise-support count against the other two candidates.

Copeland is also computed in two exact ways. The first awards \(1,1/2,0\) contest by contest. The second uses
\[
1+\frac12\sum_{y\ne x}\operatorname{sgn}\!\bigl(n_P(x,y)-n_P(y,x)\bigr).
\]
Both pairs of implementations agree on every profile.

The complete relation histogram is:
\[
\begin{array}{c|r}
\text{case} & \text{profiles}\\ \hline
n=1,\ B=C\text{ singleton} & 6\\
n=2,\ B=C\text{ singleton/two-way/three-way} & 24,\ 6,\ 6\\
n=3,\ B=C\text{ singleton} & 186\\
n=3,\ C\subsetneq B,\ (|B|,|C|)=(2,1) & 18\\
n=3,\ B=C\text{ three-way} & 12\\
n=4,\ B=C\text{ singleton/two-way/three-way} & 972,\ 162,\ 90\\
n=4,\ B\subsetneq C,\ (|B|,|C|)=(1,2) & 72\\
n=5,\ B=C\text{ singleton/three-way} & 6396,\ 360\\
n=5,\ C\subsetneq B,\ (|B|,|C|)=(2,1) & 780\\
n=5,\ B\subsetneq C,\ (|B|,|C|)=(1,3) & 180\\
n=5,\ B\cap C=\varnothing,\ (|B|,|C|)=(1,1) & 60.
\end{array}
\]

A second enumeration covers all \(252\) anonymous five-voter multiplicity vectors. It finds \(6\) unique conflicts; exact multinomial weighting gives \(60\) labeled profiles again.

Canonicalization under all candidate permutations gives one anonymous class. In ballot order `ABC, ACB, BAC, BCA, CAB, CBA`, its canonical multiplicity vector is `0,0,0,3,2,0`. Each such anonymous profile has
\[
\frac{5!}{3!\,2!}=10
\]
voter orderings. Candidate and voter relabeling generates exactly the complete \(60\)-profile conflict set.

## Verification
The embedded `verify_borda_copeland_unique_conflict.py` uses only the Python standard library and exact rational arithmetic.

It verifies every labeled profile through \(5\) voters; two independent Borda computations; two independent Copeland computations; the complete relation histograms; the \(60\)-profile unique-conflict count; exact incidences \(5/648\) and \(1/42\); the independent anonymous census; one anonymous candidate-relabeling class; one combined candidate/voter orbit; and the displayed representative's exact scores and margins.

Run:

`python3 verify_borda_copeland_unique_conflict.py`

The first output line must be `VERIFY_OK`.

## Relationship to prior work
Favardin, Lepelley, and Serais study Borda and Copeland side by side for three-candidate elections, give the standard definitions, parameterize anonymous profiles by the six ballot types, and derive exact manipulation conditions and vulnerability measures. Their analysis imposes a fixed alphabetical tie-breaker because its subject is manipulation.

Diss also studies Borda and Copeland together for three alternatives and derives exact relations for manipulation probabilities under self-selectivity.

The present event is different: direct disagreement of truthful winner correspondences with no imposed tie-breaker. Requiring both outcomes to be unique removes tie-breaking conventions from the main boundary.

For an odd three-candidate electorate, a unique Copeland winner is the Condorcet winner. Classical Condorcet-efficiency work, including Van Newenhizen's probabilistic comparison of weighted voting systems, is therefore a directly relevant broader formulation. The inspected material does not give the exact five-voter \(60\)-profile census or the one-orbit classification.

The existence of a five-voter Borda/Condorcet counterexample is not claimed as new. The contribution is the sharp lower bound through four voters, the complete first-layer count, the exact two culture incidences, and the proof that every first unique conflict has one symmetry type.

## Limitations
The theorem is finite: it concerns exactly three candidates and electorates through five voters.

Borda and Copeland can have different winner sets at smaller electorate sizes because of ties. Only the different-unique-winner boundary is claimed sharp.

The Condorcet-efficiency literature is extensive. An older finite-electorate table, formula, software test set, or teaching computation not surfaced in the searches could contain the same count.

The 2002 Borda–Copeland article is older than the exact-day repository anchor used in the metadata; no exact public day was invented for that older publication.

## References
1. P. Favardin, D. Lepelley, and J. Serais, “Borda rule, Copeland method and strategic manipulation,” *Review of Economic Design* 7(2) (2002), 213–228. DOI: 10.1007/s100580200073.
2. M. Diss, “Strategic manipulability of self-selective social choice rules,” GATE Working Paper 1302 / HAL halshs-00785366v1, public repository version dated 6 February 2013.
3. J. Van Newenhizen, “The Borda Method Is Most Likely to Respect the Condorcet Principle,” *Economic Theory* 2(1) (1992), 69–83.

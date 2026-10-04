# Sharp five-voter divergence boundary for Kemeny and Slater with three candidates
## Finding
Consider elections with exactly three candidates, complete strict ballots, and an odd number of voters.

For a profile \(P\), let \(K(P)\) be the set of candidates that top at least one Kemeny-optimal linear ranking, and let \(S(P)\) be the set of candidates that top at least one Slater-optimal linear ranking.

Five voters are the smallest odd electorate for which
\[
K(P)\ne S(P).
\]

For one voter and for three voters,
\[
K(P)=S(P)
\]
for every profile.

For five voters there are
\[
6^5=7776
\]
labeled profiles. Exactly
\[
180
\]
of them have different Kemeny and Slater winner sets, so under independent uniform strict ballots the exact divergence probability is
\[
\frac{180}{7776}=\frac{5}{216}.
\]

Every divergent profile has a cyclic majority tournament with positive majority-margin multiset
\[
(1,1,3).
\]
Moreover, all divergent profiles form one anonymous class up to relabeling the candidates. A canonical representative has
\[
2(A\succ B\succ C),\qquad
2(B\succ C\succ A),\qquad
1(C\succ A\succ B).
\]

Its pairwise majority margins are
\[
A\succ B:\ 1,\qquad
B\succ C:\ 3,\qquad
C\succ A:\ 1.
\]
The Slater-optimal rankings are exactly
\[
A\succ B\succ C,\qquad
B\succ C\succ A,\qquad
C\succ A\succ B,
\]
so
\[
S(P)=\{A,B,C\}.
\]
The Kemeny-optimal rankings reverse one of the two weakest majority edges:
\[
A\succ B\succ C
\quad\text{and}\quad
B\succ C\succ A.
\]
Thus
\[
K(P)=\{A,B\}\subsetneq S(P).
\]

The six anonymous labeled-candidate profiles in this single relabeling orbit each have multinomial multiplicity
\[
\frac{5!}{2!\,2!\,1!}=30,
\]
giving the total
\[
6\cdot30=180.
\]

## Assumptions and scope
The candidate set has cardinality exactly \(3\). Every voter submits a complete strict linear order, and the electorate size is odd so every pairwise comparison has a strict majority winner.

A Kemeny ranking minimizes total Kendall disagreement with the ballots, equivalently maximizes total pairwise support consistent with the ranking.

A Slater ranking minimizes the number of majority-tournament edges that must be reversed to obtain the ranking.

The finding concerns the sets of top candidates of all optimal linear rankings; no tie-breaking is imposed.

The universal lower-bound statement covers odd electorate sizes \(1\) and \(3\), and the exact census covers size \(5\). No frequency formula for larger electorates is claimed.

## Proof
For three candidates, the relationship between the rules is elementary once the majority tournament is fixed.

If the majority tournament is transitive, its unique topological order is both the unique Slater ranking and the unique Kemeny ranking.

If the majority tournament is the cycle
\[
A\succ B,\qquad B\succ C,\qquad C\succ A
\]
with positive margins \(m_{AB},m_{BC},m_{CA}\), then every linear order must reverse at least one majority edge. The three Slater-optimal rankings are exactly the three cyclic orders that reverse one edge:
\[
A\succ B\succ C,\quad
B\succ C\succ A,\quad
C\succ A\succ B.
\]
Hence the Slater winner set is all three candidates.

For Kemeny, reversing an edge incurs its majority-margin cost. Therefore the Kemeny-optimal rankings are exactly those cyclic orders that reverse an edge of minimum margin. Consequently,
\[
K(P)=S(P)
\]
for a cyclic profile if and only if
\[
m_{AB}=m_{BC}=m_{CA}.
\]

With one voter, a majority cycle is impossible. With three voters, every majority cycle necessarily has margins
\[
(1,1,1),
\]
so Kemeny and Slater again have the same winner set on every profile.

For five voters, the verifier exhausts all \(6^5=7776\) labeled profiles. It computes Kemeny rankings in two independent ways: directly from total pairwise support and by minimizing reversed majority-margin weight. It computes Slater rankings both by direct feedback-edge count and by the three-candidate cycle formula. The implementations agree on every profile.

The complete five-voter histogram is:
\[
\begin{array}{c|r}
\text{winner-set relation} & \text{profiles}\\ \hline
K(P)=S(P),\ |K(P)|=|S(P)|=1 & 7236\\
K(P)=S(P),\ |K(P)|=|S(P)|=3 & 360\\
K(P)\subsetneq S(P),\ |K(P)|=2,\ |S(P)|=3 & 180
\end{array}
\]

All \(180\) divergent profiles have cyclic margin multiset \((1,1,3)\).

As an independent count, the verifier enumerates all
\[
\binom{10}{5}=252
\]
anonymous five-voter profiles, weighting each by its multinomial number of labeled voter sequences. Exactly six anonymous labeled-candidate profiles diverge, all in one orbit under candidate relabeling. Each has multiplicity \(30\), yielding
\[
6\cdot30=180.
\]

## Verification
The embedded `verify_kemeny_slater_five_voters.py` uses only the Python standard library and exact integer arithmetic.

It checks:
- all \(6\) one-voter profiles;
- all \(6^3=216\) three-voter profiles;
- all \(6^5=7776\) five-voter profiles;
- Kemeny rankings by two independent objective implementations;
- Slater rankings by direct majority-edge reversal count and an independent three-candidate structural implementation;
- the exact five-voter histogram \(7236,360,180\);
- the exact divergence probability \(5/216\);
- the unique candidate-relabeling orbit of divergent anonymous profiles;
- the canonical \(2,2,1\) cyclic witness and its Kemeny and Slater ranking sets.

Run:

`python3 verify_kemeny_slater_five_voters.py`

The first output line must be `VERIFY_OK`.

## Relationship to prior work
Kemeny and Slater are classical distance-based aggregation rules. Klamler gives a direct comparison of them, emphasizes that Kemeny uses majority-margin magnitudes while Slater minimizes disagreement with the unweighted majority relation, and constructs stronger antagonistic examples with at least four alternatives.

Lamboray treats the three-alternative case explicitly. For a cyclic majority relation, his analysis gives the three Slater orders and states that the Kemeny order is obtained by reversing a smallest-margin edge, with all possibilities retained when the minimum is tied. Thus the structural three-candidate rule comparison used in the proof is prior work.

The contribution here is the electorate-size boundary and exact first nontrivial census: three voters are still too few for unequal positive margins around a majority cycle, while five voters are sufficient; exactly \(180\) labeled five-voter profiles diverge, all from one anonymous candidate-relabeling class.

Targeted searches for a five-voter Kemeny–Slater boundary, the exact count \(180\), the probability \(5/216\), and the \(2,2,1\) anonymous classification did not locate an equivalent published statement.

## Limitations
The result is restricted to exactly three candidates and odd electorates with strict ballots.

The structural characterization of Kemeny and Slater on a three-candidate cycle is not new; the new claim is the sharp voter threshold and complete five-voter census.

The exact count is a finite first-boundary invariant. It does not provide a closed formula for larger odd electorates.

An unindexed exercise, thesis table, software enumeration, or supplementary computation could contain the same five-voter census.

## References
1. C. Klamler, “Kemeny’s rule and Slater’s rule: A binary comparison,” *Economics Bulletin* 4(35) (2003), 1–7. RePEc:ebl:ecbull:eb-03d70009.
2. C. Lamboray, *Prudent ranking rules: theoretical contributions and applications*, doctoral thesis, University of Luxembourg / Université Libre de Bruxelles, 2007. Public repository record: ORBilu 10993/15582.
3. D. Bachmeier, F. Brandt, C. Geist, P. Harrenstein, K. Kardel, D. Peters, and H. G. Seedig, “\(k\)-Majority Digraphs and the Hardness of Voting with a Constant Number of Voters,” *Journal of Computer and System Sciences* 105 (2019), 130–157. DOI: 10.1016/j.jcss.2019.04.005.

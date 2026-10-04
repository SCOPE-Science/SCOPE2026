# Complete minimal homogeneous monotonicity classification for three-candidate instant runoff
## Finding
Consider three-candidate instant-runoff voting (IRV) with complete strict ballots. A **homogeneous support change** means that a nonempty group of voters who all cast the same ballot change identically by moving the current IRV winner upward while preserving the relative order of the other two candidates.

Require the IRV winner to be uniquely determined both before and after the change, with no first-elimination tie. Then no harmful homogeneous support change exists with fewer than
\[
17
\]
voters.

At \(17\) voters, every harmful change necessarily involves exactly two voters. There are exactly
\[
252
\]
anonymous profiles with labeled candidates that admit such a change. Since the number of anonymous three-candidate profiles is
\[
\binom{22}{5}=26{,}334,
\]
the exact incidence is
\[
\frac{252}{26{,}334}=\frac{2}{209}.
\]

Modulo simultaneous relabeling of the three candidates, the \(252\) profiles form exactly \(42\) classes, all with orbit size \(6\).

The classification has a two-family normal form. Normalize the old winner to \(A\), the new winner to \(B\), and the remaining candidate to \(C\). Order ballot types as
\[
ABC,\ ACB,\ BAC,\ BCA,\ CAB,\ CBA.
\]
Every minimal profile is exactly one of
\[
(x,6-x,y,5-y,2,4),
\]
where the two \(CAB\) voters change to \(ACB\), or
\[
(x,6-x,y,5-y,0,6),
\]
where two \(CBA\) voters change to \(ACB\), with
\[
0\le x\le6,\qquad 3\le y\le5.
\]
Each family therefore contains \(7\cdot3=21\) candidate-normalized classes.

Every one of the \(252\) bad profiles has exactly one harmful homogeneous support change in this anonymous sense. Half of the profiles raise the winner by one position and half raise the winner by two positions.

## Assumptions and scope
A profile is anonymous: only the number of voters of each strict ranking type matters. Candidates remain labeled for the count \(252\); the \(42\)-class count then quotients by all six candidate permutations.

With three candidates, IRV first elects a strict majority winner if one exists. Otherwise the unique candidate with the fewest first-place votes is eliminated, and those ballots transfer to their preferred remaining candidate. Profiles with a tie for fewest first-place votes are outside the theorem.

A support change may involve any positive number of voters, but all changed voters must start with the same ranking and must make the same ranking change. The current winner moves strictly upward, and the order of the other two candidates is unchanged.

## Proof
Let \(A\) be the original IRV winner. If a changed ballot raises \(A\) without putting \(A\) first, then first-choice totals do not change. With three candidates the eliminated candidate is therefore unchanged, and any altered transfer can only move toward \(A\). Such a change cannot make \(A\) lose. Hence every harmful change promotes \(A\) to first place.

Let \(C\) be the candidate from whose first-place ballots the changed voters come. For the eliminated candidate to change, the original plurality loser must be the third candidate \(B\), and after the change \(C\) must become the plurality loser. The new winner is therefore \(B\).

Write the original first-choice totals as
\[
a,\ b,\ c
\]
for \(A,B,C\), respectively. Since \(B\) is the unique original loser,
\[
a\ge b+1.
\]
Write
\[
c=b+\delta,\qquad \delta\ge1.
\]
If \(k\) voters move from a \(C\)-first ballot to an \(A\)-first ballot, then \(C\) can become the unique new loser only if
\[
c-k<b,
\]
so
\[
k\ge\delta+1.
\]

After \(C\) is eliminated, even in the most favorable possible transfer pattern for \(B\), candidate \(B\) has at most
\[
b+c-k
\]
votes, while \(A\) has at least
\[
a+k.
\]
For \(B\) to defeat \(A\), it is therefore necessary that
\[
b+c-k>a+k.
\]
Substituting \(c=b+\delta\) gives
\[
2b+\delta-a>2k\ge2\delta+2.
\]
Since \(a\ge b+1\), the left-hand side is at most \(b+\delta-1\). Thus
\[
b+\delta-1>2\delta+2,
\]
which forces
\[
b\ge\delta+4.
\]
Consequently the total electorate satisfies
\[
n=a+b+c\ge(b+1)+b+(b+\delta)\ge4\delta+13\ge17.
\]

If \(n=17\), every inequality above is forced to its minimal integer value:
\[
\delta=1,\qquad (a,b,c)=(6,5,6).
\]
Moreover,
\[
11-k>6+k
\]
is necessary for the post-change runoff, while \(k\ge2\); hence
\[
k=2.
\]

It remains to resolve the six ballot types. Let \(x\) be the number of \(ABC\) ballots, so there are \(6-x\) \(ACB\) ballots. Let \(y\) be the number of \(BAC\) ballots, so there are \(5-y\) \(BCA\) ballots. Since \(B\) is eliminated in the original election, \(A\) wins precisely when
\[
6+y>6+(5-y),
\]
which is equivalent to
\[
y\ge3.
\]
Thus
\[
0\le x\le6,\qquad 3\le y\le5.
\]

Finally let \(u\) be the number of \(CAB\) ballots, so there are \(6-u\) \(CBA\) ballots.

If the changed voters are two \(CAB\) voters, they become \(ACB\). After the change \(C\) is eliminated, and the final totals are
\[
A:6+u,\qquad B:11-u.
\]
For \(B\) to win, \(11-u>6+u\), while the move requires \(u\ge2\). Hence \(u=2\), giving
\[
(x,6-x,y,5-y,2,4).
\]

If the changed voters are two \(CBA\) voters, they again become \(ACB\). The final totals are
\[
A:8+u,\qquad B:9-u.
\]
For \(B\) to win, \(9-u>8+u\), so \(u=0\), giving
\[
(x,6-x,y,5-y,0,6).
\]

There are \(7\cdot3=21\) profiles in each normalized family. The old winner and new winner are distinct, so six ordered candidate relabelings are possible, and the unique winner plus unique eliminated candidate rule out any nontrivial stabilizer. Thus the total is
\[
(21+21)\cdot6=252.
\]

## Verification
The embedded `verify_irv17_homogeneous_monotonicity.py` performs an exhaustive exact replay.

Its first route enumerates every anonymous three-candidate profile for electorate sizes \(1\) through \(17\). For every uniquely resolved profile it tests every nonempty homogeneous group and every ranking change that raises the current winner while preserving the order of the other candidates. It finds no harmful event below \(17\) and exactly \(252\) at \(17\).

Its second route generates the two symbolic normal-form families directly and requires exact equality with the normalized exhaustive event set. It also checks the \(42\) candidate-relabeling classes, full orbit size \(6\), uniqueness of the harmful move at each bad profile, the split \(126+126\) by one-position versus two-position raises, and the incidence \(2/209\).

Replay with:

`python3 verify_irv17_homogeneous_monotonicity.py`

The first output line must be `VERIFY_OK`.

## Relationship to prior work
Ornstein and Norman study upward monotonicity failure for three-candidate IRV and give necessary and sufficient conditions for whether some upward support shift can make the current winner lose. Their paper was published online on 17 October 2013. Their analysis is aimed at frequency under a spatial model and does not give the finite minimal homogeneous-support census proved here.

Miller gives a transparent three-candidate characterization of upward monotonicity failure and relates it to competitiveness and pairwise majority comparisons. This is broader in electorate size and in the number of changed voters, but it does not state the \(17\)-voter two-family classification.

Brandt, Matthäus, and Saile give a tie-independent minimal Additional Support example for three-candidate instant runoff with \(17\) voters and explain why at least two voters must change in their convention. Thus the sharp number \(17\) and existence of a two-voter witness are prior work. The contribution here is the complete boundary classification: every homogeneous harmful change at that size has the same first-choice totals \(6,5,6\), necessarily changes exactly two voters, and belongs to one of the two normal-form families above, yielding \(252\) labeled-candidate profiles and \(42\) candidate-relabeling classes.

## Limitations
The theorem concerns exactly three candidates, complete strict ballots, homogeneous groups, and tie-independent unique IRV outcomes. It does not classify heterogeneous coalitions whose members begin with different ballots or make different support changes.

The count is for anonymous ballot profiles. It does not count assignments of individually labeled voters to ranking types.

Targeted searches and inspection of the closest primary literature did not reveal the \(252\)-profile, \(42\)-class, or two-family boundary census. An unindexed thesis, teaching note, software table, or supplementary computation could nevertheless contain the same classification.

## References
1. J. T. Ornstein and R. Z. Norman, “Frequency of monotonicity failure under Instant Runoff Voting: estimates based on a spatial model of elections,” *Public Choice* 161 (2014), 1–9. DOI: 10.1007/s11127-013-0118-2. Published online 17 October 2013.
2. N. R. Miller, “Closeness matters: monotonicity failure in IRV elections with three candidates,” *Public Choice* 173 (2017), 91–108. DOI: 10.1007/s11127-017-0465-5.
3. F. Brandt, M. Matthäus, and C. Saile, “Minimal voting paradoxes,” *Journal of Theoretical Politics* 34 (2022), 527–551. DOI: 10.1177/09516298221122104.

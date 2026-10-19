# Twelve voters are the sharp tie-free boundary for global versus sequential PAV

## Finding

For **exactly three candidates** and **two committee seats**, suppose all approval ballots are nonempty. Global proportional approval voting (PAV) chooses a committee maximizing total harmonic satisfaction, while sequential PAV (also called greedy PAV) adds the largest marginal-score candidate in each of two rounds. Call an election a *strict separation* if global PAV has exactly one winning committee, sequential PAV has exactly one choice at each round, and their final committees differ.

**Theorem.** A strict separation is possible with \(n\) voters if and only if \(n\geq12\). With \(n=12\), precisely **six anonymous profiles with fixed candidate labels** strictly separate the two rules. They form one orbit under candidate relabeling, represented by
\[
4\cdot\{A,B\},\qquad3\cdot\{A,C\},\qquad2\cdot\{B\},\qquad3\cdot\{C\}.
\]
Every strict separation at the threshold has this form up to relabeling.

In this profile the approval counts of \(A,B,C\) are \(7,6,6\), respectively. The global committee scores are \(P(AB)=11\), \(P(AC)=23/2\), and \(P(BC)=12\), so the unique global winner is \(\{B,C\}\). Sequential PAV selects \(A\) uniquely in round one; its remaining marginal scores are \(4\) for \(B\) and \(9/2\) for \(C\), giving the unique greedy committee \(\{A,C\}\). Neither outcome depends on tie-breaking.

## Assumptions and scope

All voters have one of seven nonempty approval sets over \(\{A,B,C\}\); there are no voter weights or extra candidates. For an approval ballot \(S\) and a committee \(W\) with two winners, the harmonic satisfaction is \(H(|W\cap S|)\), where \(H(0)=0\), \(H(1)=1\), and \(H(2)=3/2\). The PAV score is the sum of satisfaction over voters. Sequential PAV first maximizes ordinary approval count; subsequently it chooses the remaining candidate with largest marginal increase of PAV score. Strictness means **both sequential comparisons are unique**, and **the global maximum is unique**. If the greedy method has a tie at either stage, that election is outside the theorem's accepted class. Profiles are anonymous (voter order ignored), but candidate labels distinguish profiles for counting.

## Proof

**Step 1: normalize and parameterize every potential separation.** Suppose a strict separation exists. Relabel candidates so that sequential PAV's first winner is \(A\); it is uniquely most approved. The second greedy round maximizes the *same complete PAV score* among the two committees containing \(A\), because the score of \(\{A\}\) is a common constant. If the unique global optimum contained \(A\), the second greedy round would therefore choose it. Thus a distinct unique global optimum must be \(\{B,C\}\). Let the nonnegative numbers of ballots \(\{A\},\{B\},\{C\},\{A,B\},\{A,C\},\{B,C\},\{A,B,C\}\) be, respectively, \(a,b,c,x,y,z,w\). Let \(v_A,v_B,v_C\) be their total single-candidate approvals, and write the positive integer approval gaps as \(d_B=v_A-v_B\geq1\) and \(d_C=v_A-v_C\geq1\).

For any two candidates \(i,j\), the pair score is their separate approval counts minus half the number of ballots approving both. Thus
\[
P(BC)-P(AB)=-d_C+\frac{x-z}{2},\qquad
P(BC)-P(AC)=-d_B+\frac{y-z}{2}.
\]
Because \(BC\) is the **unique** global optimum, both expressions are strictly positive. All quantities are integers except halves, so there exist integers \(u,v\geq0\) for which
\[
x=z+2d_C+1+u,\qquad y=z+2d_B+1+v.
\]
The definitions of the approval gaps then give
\[
b=a+d_B+1+v,\qquad c=a+d_C+1+u.
\]
Adding the seven ballot multiplicities yields the **exact identity**
\[
\boxed{n=3a+3d_B+3d_C+4+2u+2v+3z+w.}
\]
It follows in particular that \(n\geq10\).

**Step 2: the second greedy round supplies the extra two voters.** After \(A\) is selected, the marginal score of \(B\) is \(G_B=v_B-(x+w)/2\), and that of \(C\) is \(G_C=v_C-(y+w)/2\). Consequently,
\[
2(G_B-G_C)=2(v_B-v_C)-(x-y)=v-u.
\]
The second selection is **strict** precisely when \(u\ne v\). For nonnegative integers, that implies \(u+v\geq1\). Substitution into the exact voter identity proves \(n\geq12\) for every strict separation. This is an all-profiles proof, not a truncated search.

**Step 3: attain and classify the boundary.** For \(n=12\), equality in every nonnegative term requires
\[
a=z=w=0,\quad d_B=d_C=1,\quad u+v=1.
\]
Thus \((u,v)=(1,0)\) or \((0,1)\), and the preceding equations force the two normalized profiles
\[
(\{A\},\{B\},\{C\},\{AB\},\{AC\},\{BC\},\{ABC\})
=(0,2,3,4,3,0,0)
\]
or the version with \(B\) and \(C\) exchanged. These constitute the single displayed symmetry class. The explicit scores in the Finding section prove strict separation. There are three possible choices for the uniquely first-elected candidate and two choices for the second-round winner, hence exactly \(3\cdot2=6\) fixed-label anonymous profiles.

**Step 4: every larger electorate.** To obtain a strict separation with any \(n>12\), add \(n-12\) voters who approve all three candidates to the displayed twelve-voter profile. This increases every first-round approval count equally by \(n-12\), every two-seat global score equally by \(3(n-12)/2\), and each remaining greedy marginal score equally by \((n-12)/2\). Every strict inequality is preserved. This proves existence for all \(n\geq12\) and completes the iff statement. \(\square\)

## Verification

The companion standalone Python program `verify_pav.py` computes both rule scores **directly from all seven ballot types** using doubled integer arithmetic. It checks every anonymous three-candidate nonempty approval profile with \(1\leq n\leq12\), a total of 50,387 profiles. The counts of globally unique winning committees that omit the uniquely most-approved candidate are zero for \(n\leq9\), three at \(n=10\), three at \(n=11\), and nine at \(n=12\); **exactly six** of the twelve-voter profiles have a strict second greedy round. The numerical enumeration independently corroborates the fully general algebraic proof; it is not offered as proof of the all-electorate statement.

Run `python3 verify_pav.py`. No third-party packages, datasets, or external services are needed.

## Relationship to prior work

The rules and their differing behavior are well known. In particular, Lackner and Skowron, *Multi-Winner Voting with Approval Preferences* (2023), Appendix A, Proposition A.2, **already give the ten-voter profile** \(2\cdot\{a\},3\cdot\{a,c\},3\cdot\{b,c\},2\cdot\{b\}\) showing that global PAV fails committee monotonicity. It is a candidate-relabeling of the ten-voter normalized profile implicit in Step 1, and it has a **second-round greedy tie**, so it is not a strict separation in the present sense. Their Example 2.5 also gives a larger explicit PAV/seq-PAV divergence. Neither is claimed as a new disagreement. Dong and Lederer characterize sequential valuation rules, and Janeczko and Faliszewski study ties for global and greedy committee rules. The present result specifically supplies the sharp **tie-free** electorate threshold and complete twelve-voter classification for the smallest candidate/seat setting; these do not follow as stated from the cited results.

## Limitations

Only three candidates, two seats, nonempty unweighted approval ballots, global harmonic PAV and its forward sequential version are addressed. The theorem does not describe minima for more candidates/seats, reverse greedy elimination, general Thiele weights, or rule behavior under ties. Its publication priority beyond the explicitly examined sources has not been independently established; a broader enumerative theorem might imply the boundary. The six-profile conclusion counts labeled-candidate *anonymous* profiles, not individually ordered voter lists.

## References

1. C. Dong and P. Lederer, *Characterizations of Sequential Valuation Rules*, arXiv:2302.11890v1, first public 2023-02-23, https://arxiv.org/abs/2302.11890.
2. Ł. Janeczko and P. Faliszewski, *Ties in Multiwinner Approval Voting*, arXiv:2305.01769v1, first public 2023-05-02, https://arxiv.org/abs/2305.01769.
3. M. Lackner and P. Skowron, *Multi-Winner Voting with Approval Preferences*, Springer, 2023, Appendix A, Proposition A.2 and Chapter 2, Example 2.5, https://doi.org/10.1007/978-3-031-09016-5.

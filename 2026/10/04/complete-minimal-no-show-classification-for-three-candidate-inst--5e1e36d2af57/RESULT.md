# Complete minimal no-show classification for three-candidate instant runoff
## Finding
Consider three-candidate instant-runoff voting (IRV) with complete strict ballots and no tie-breaking: only elections with a unique first-round elimination and a unique final winner are admitted. A homogeneous no-show move removes a nonempty group of voters who all submit the same ranking and who strictly prefer the winner after their abstention to the winner when they participate.

No such paradox occurs with fewer than \(11\) voters. At the sharp size \(11\), exactly
\[
60
\]
of the
\[
\binom{11+6-1}{6-1}=\binom{16}{5}=4{,}368
\]
anonymous labeled-candidate profiles admit a homogeneous no-show move. Thus the incidence on the full anonymous \(11\)-voter domain is
\[
\frac{60}{4{,}368}=\frac{5}{364}.
\]
Exactly \(4{,}080\) anonymous profiles have a unique full-election IRV winner, so conditional on that tie-independent full-election domain the incidence is
\[
\frac{60}{4{,}080}=\frac1{68}.
\]

Every one of the \(60\) bad profiles has exactly one harmful anonymous abstention move, and that move removes exactly two voters. Up to simultaneous relabeling of the three candidates, the bad profiles form exactly \(10\) classes, all with orbit size \(6\).

Normalize the two abstainers' ranking to \(A\succ B\succ C\), and list ballot counts in the order
\[
ABC,\ ACB,\ BAC,\ BCA,\ CAB,\ CBA.
\]
The complete list of normalized classes is the union of the two families
\[
(4,0,0,3,t,4-t),\qquad
(4,0,1,2,t,4-t),
\]
for
\[
t\in\{0,1,2,3,4\}.
\]
In every class the full-election winner is \(C\), the abstainers rank \(C\) last, and after exactly two \(ABC\) voters abstain the winner becomes \(B\), their second choice.

## Assumptions and scope
There are exactly three candidates and every voter submits one of the six strict rankings. An anonymous profile records the six nonnegative ballot-type counts. IRV elects an absolute first-choice majority immediately; otherwise it eliminates the unique candidate with the fewest first choices and transfers that candidate's ballots to the next remaining choice. Profiles with a first-round elimination tie or a tied final contest are outside the asserted tie-independent domain.

The abstaining group must be nonempty and homogeneous: all abstainers share one ranking. Their welfare comparison uses that common strict ranking. Voters are anonymous, while candidate labels are retained until the symmetry quotient is taken.

## Proof
First, removing voters who rank \(A\) first cannot make \(A\) change from loser to winner in three-candidate IRV. If \(A\) already has a majority after removal, adding back \(A\)-first ballots preserves it. Otherwise the unique smallest first-choice count among the other two candidates is unchanged, so the same opponent is eliminated, and adding \(A\)-first ballots only improves \(A\)'s final pairwise tally. Consequently, after relabeling candidates, any beneficial homogeneous abstention may be normalized so that the abstainers rank
\[
A\succ B\succ C,
\]
the full-election winner is \(C\), and the post-abstention winner is \(B\).

Write the six ballot counts as
\[
(x,y,z,u,v,w)
\]
for \(ABC,ACB,BAC,BCA,CAB,CBA\), respectively, and let
\[
a=x+y,\qquad b=z+u,\qquad c=v+w
\]
be the first-choice totals. Suppose \(k\) voters of type \(ABC\) abstain.

Because the full winner is \(C\) but the post-abstention winner is \(B\), the unique eliminated candidate must switch from \(B\) in the full election to \(A\) after abstention. Hence
\[
b<a,\qquad b<c,\qquad a-k<b,\qquad a-k<c.
\]
In particular,
\[
a\ge b+1,\qquad a\le b+k-1,\qquad c\ge b+1,
\]
so \(k\ge2\).

When \(B\) is eliminated in the full election, the \(BAC\) ballots transfer to \(A\) and the \(BCA\) ballots transfer to \(C\). Since \(C\) wins,
\[
c+u>a+z.
\]
Using \(u=b-z\), this becomes
\[
c+b-a>2z\ge0.
\]
After abstention, \(A\) is eliminated. The remaining \(ABC\) ballots transfer to \(B\), while the \(ACB\) ballots transfer to \(C\). Since \(B\) wins,
\[
b+x-k>c+y.
\]
Using \(x=a-y\), this becomes
\[
a+b-c-k>2y\ge0.
\]
Combining the latter strict inequality with \(a\le b+k-1\) yields
\[
c<2b-1.
\]
Together with \(c\ge b+1\), this forces \(b\ge3\). Therefore
\[
a\ge4,\qquad b\ge3,\qquad c\ge4,
\]
and every paradox requires at least
\[
a+b+c\ge11
\]
voters.

At equality \(n=11\), all three lower bounds are tight, so
\[
(a,b,c)=(4,3,4).
\]
The post-abstention final inequality reduces to
\[
3-k>2y.
\]
Since \(k\ge2\), necessarily \(k=2\) and \(y=0\), hence \(x=4\). The full-election final inequality becomes
\[
3>2z,
\]
so \(z\in\{0,1\}\) and \(u=3-z\). Finally \(v+w=4\), giving exactly
\[
(4,0,0,3,t,4-t)
\]
or
\[
(4,0,1,2,t,4-t)
\]
with \(0\le t\le4\).

Direct substitution verifies that in each of these ten profiles \(C\) wins the full election and \(B\) wins after two \(ABC\) voters abstain. Exhaustive checking of the ten normal forms shows there is no second harmful homogeneous move. Therefore a bad profile has a unique such move. Any candidate automorphism of a bad profile must preserve that unique abstainer ranking and hence fixes all three candidates, so every orbit has size \(6\). Thus the ten normalized classes give exactly \(10\cdot6=60\) labeled-candidate anonymous profiles.

## Verification
The embedded `verify_irv11_noshow.py` is a standard-library-only exact verifier.

Its first route enumerates every weak composition of each electorate size through \(11\) into the six ballot types, evaluates tie-independent IRV exactly, and tests every nonempty homogeneous abstention group. It returns no paradox through size \(10\), then exactly \(60\) profiles and \(60\) harmful moves at size \(11\).

A separately organized event-first route enumerates every possible post-abstention profile, ballot type, and abstention-group size whose reconstructed full electorate has size \(11\). It reproduces exactly the same set of \(60\) events. The verifier also checks the two-voter group size, the last-to-second winner improvement, the \(10\) candidate-relabeling classes, orbit size \(6\), the exact two-family normal form, and the two incidence fractions.

Replay with:

`python3 verify_irv11_noshow.py`

The first output line must be `VERIFY_OK`.

## Relationship to prior work
Fishburn and Brams introduced the no-show terminology in their 1983 study of preferential-voting paradoxes and supplied early examples for preferential elimination rules. Existence of the phenomenon is therefore not new.

Lepelley and Merlin give necessary and sufficient inequalities for abstention and participation paradoxes in three-candidate scoring run-off rules and tabulate their frequencies under Impartial Culture and Impartial Anonymous Culture. For three-candidate plurality run-off, which is the relevant IRV specialization, their small-electorate calculation deliberately resolves ties in whichever way produces the paradox. They explicitly warn that this convention overestimates small-electorate probabilities. Their table reports an IAC no-show probability of \(0.07005\) at \(11\) voters under that convention, so it is not the present tie-independent count.

Brandt, Matthäus, and Saile later impose a tie-independent convention and show that the minimal three-candidate IRV no-show example has \(11\) voters; they also observe that at least two identical voters must abstain. Thus the sharp size \(11\) and existence of a two-voter witness are prior work. Their minimality compilation does not enumerate every minimal profile.

The contribution here is the complete tie-independent boundary classification: the exact \(60\)-profile count, both incidence fractions, uniqueness and size of the harmful abstention group, the \(10\) candidate-relabeling classes, and the explicit two-family normal form.

## Limitations
The theorem concerns exactly three candidates, anonymous electorates, complete strict rankings, homogeneous abstaining groups, and uniquely determined IRV outcomes. It does not classify larger electorates, heterogeneous abstaining coalitions, incomplete ballots, or any fixed tie-breaking rule.

The originality search cannot exclude an unindexed thesis, teaching note, software table, or unpublished enumeration that contains the same ten-class boundary census. The 1983 Fishburn--Brams primary article was verified bibliographically and through later scholarly descriptions, while the directly comparative 2001 and 2022 sources were inspected in detail.

## References
1. P. C. Fishburn and S. J. Brams, “Paradoxes of Preferential Voting,” *Mathematics Magazine* 56(4) (1983), 207–214. DOI: 10.1080/0025570X.1983.11977044.
2. D. Lepelley and V. Merlin, “Scoring run-off paradoxes for variable electorates,” *Economic Theory* 17 (2001), 53–80. DOI: 10.1007/PL00004103.
3. F. Brandt, M. Matthäus, and C. Saile, “Minimal voting paradoxes,” *Journal of Theoretical Politics* 34 (2022), 527–551. DOI: 10.1177/09516298221122104.

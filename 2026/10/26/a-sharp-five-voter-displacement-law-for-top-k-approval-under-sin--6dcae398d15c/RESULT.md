# A sharp five-voter displacement law for top-\(k\) approval under single-peaked preferences

## Finding

Let the alternatives be \(0,1,\ldots,m-1\). Each of five voters has a strict single-peaked ranking on this axis and approves exactly the \(k\) highest-ranked alternatives. If \(w\) is the unique top-\(k\)-approval winner and \(h\) is the median peak, then a unique winner is possible for some profile exactly when \(m\ge 2k-1\). Over all such profiles,

\[
D_5(m,k):=\max |w-h|=\begin{cases}
k-1,&2k-1\le m<5k-1,\
m-3k,&m\ge 5k-1.
\end{cases}
\]

## Assumptions and scope

Here \(m,k\) are integers with \(1\le k<m\). A top-\(k\) ballot under a strict single-peaked ranking is a contiguous interval of exactly \(k\) alternatives containing the voter's peak. Conversely, every such interval can be realized as the top \(k\) alternatives of a strict single-peaked ranking by choosing an appropriate interleaving of the left and right sides. The median peak is the Condorcet winner for five strict single-peaked voters. The maximum is taken only over profiles with a unique approval winner; ties are excluded.

If \(m<2k-1\), every length-\(k\) interval on the axis has a common intersection of at least \(2k-m\ge2\) alternatives. Hence at least two candidates receive all five approvals, so a unique winner is impossible.

## Proof

Write \(A(x)\) for the number of approvals received by candidate \(x\). Reversing the axis if necessary, assume \(w<h\), and put \(d=h-w\).

First, if \(d<k\), then \(d\le k-1\). Suppose instead that \(d\ge k\). No voter whose peak is at or to the right of \(h\) can approve \(w\): an interval containing both that voter's peak and \(w\) would have to contain \(h\) and \(w\), whose index distance is at least \(k\), impossible for a length-\(k\) interval. At most two voters have peaks strictly left of the median peak. Thus \(A(w)\le2\). Since the median voter approves \(h\), uniqueness of \(w\) forces \(A(w)=2\), \(A(h)=1\), and both voters with peaks left of \(h\) to approve \(w\).

Their two approval intervals must intersect only at \(w\), or another candidate would also receive two approvals. For \(k>1\), the intervals therefore have the forms \([w-k+1,w]\) and \([w,w+k-1]\); for \(k=1\), both are the singleton \(\{w\}\). In either case, their union contains every candidate in \([w-k+1,w+k-1]\). Each of the other three ballots must avoid that union, since any overlap at a candidate other than \(w\) would give that candidate at least two approvals.

Write the median voter's interval as \([h-\ell,h+k-1-\ell]\), where \(0\le\ell\le k-1\). To avoid the union, its left endpoint must be at least \(w+k\), so \(d\ge k+\ell\). The two voters whose peaks lie right of \(h\) must have intervals disjoint from the median voter's interval and from each other; otherwise a candidate would receive two approvals and tie \(w\). These two length-\(k\) intervals must lie after the median interval, leaving at least \(2k\) alternatives after its right endpoint. Therefore

\[
m-1-(h+k-1-\ell)\ge2k,
\]

so \(h\le m-3k+\ell\). Since \(w\ge k-1\),

\[
d=h-w\le m-4k+1+\ell\le m-3k.
\]

Combining this with \(d\ge k+\ell\) gives \(m\ge5k-1\). Thus no displacement at least \(k\) is possible below that threshold, and above it every such displacement is at most \(m-3k\). The same argument applies when \(w>h\) by reversing the axis.

It remains to attain both bounds. For every \(m\ge2k-1\), let three voters have peak \(0\) and approve \([0,k-1]\), and let two voters have peak \(k-1\) and approve \([k-1,2k-2]\). Candidate \(k-1\) receives all five approvals, every other candidate receives at most three, and the median peak is \(0\). This gives displacement \(k-1\).

When \(m\ge5k-1\), set \(w=k-1\) and \(h=m-2k-1\). Use the following five peak/interval pairs:

- peak \(0\), interval \([0,k-1]\);
- peak \(k-1\), interval \([k-1,2k-2]\);
- peak \(h\), interval \([h-k+1,h]\);
- peak \(h+1\), interval \([h+1,h+k]\);
- peak \(h+k+1\), interval \([h+k+1,h+2k]\).

All intervals have length \(k\) and lie in the candidate set. The first two intersect only at \(w\); the other three intervals are pairwise disjoint and disjoint from their union because \(m\ge5k-1\). Thus \(w\) receives two approvals and every other candidate at most one. The sorted peaks have median \(h\), and \(|w-h|=m-3k\). Since \(m-3k\ge k-1\) in this regime, the two constructions attain the claimed piecewise maximum. This completes the proof.

## Verification

The proof is exact and does not use finite enumeration as a substitute for the general argument. The feasibility boundary \(m=2k-1\) is attained by the first construction. At the transition \(m=5k-1\), the second construction has displacement \(2k-1\), matching \(m-3k\). For \(k=1\), the formula reduces to displacement \(0\) for \(m=2,3\) and \(m-3\) for \(m\ge4\).

## Relationship to prior work

Black's median-voter framework identifies the median peak as the Condorcet winner under single-peaked preferences. Weber surveys approval voting and discusses median-voter results in positioning models. Brandt, Brill, and Hemaspaandra examine approval ballots in single-peaked electorates for computational-complexity questions. Those sources motivate the model, but the exact five-voter, fixed-\(k\) displacement law and its threshold \(m=5k-1\) are not stated in the material inspected. The result concerns a different invariant from winner-computation or manipulation complexity.

## Limitations

The theorem is specific to five voters, strict single-peaked rankings, exactly \(k\) approved top-ranked alternatives, and a unique winner. It does not cover arbitrary approval thresholds, tied rankings, even electorates, or the displacement of a tied winner set. The cited approval-voting survey's full text was inaccessible during this check, so an unindexed related bound remains a residual literature risk.

## References

1. Duncan Black, “On the Rationale of Group Decision-making,” *Journal of Political Economy* 56(1), 23–34 (1948), DOI: 10.1086/256633.
2. Robert J. Weber, “Approval Voting,” *Journal of Economic Perspectives* 9(1), 39–49 (1995), DOI: 10.1257/jep.9.1.39.
3. Felix Brandt, Markus Brill, Edith Hemaspaandra, and Lane A. Hemaspaandra, “Bypassing Combinatorial Protections: Polynomial-Time Algorithms for Single-Peaked Electorates,” *Proceedings of AAAI* 24(1), 715–722 (2010), DOI: 10.1609/aaai.v24i1.7637.

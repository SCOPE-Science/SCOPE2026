# Exact five-candidate majority-tournament fibers for three voters
## Finding
Consider three ordered voters and five alternatives. Each voter submits one of the \(5!=120\) strict rankings, and every pairwise contest is decided by simple majority. Thus every ordered profile induces a tournament on the five alternatives.

Up to relabeling the alternatives there are exactly 12 tournament classes, and every one is induced by some three-voter profile. Their exact fibers under the majority map are:

| Sorted outdegrees | Cyclic triangles | Sorted \((d_v,t_v)\) signature | Aut. order | Ordered profiles | Probability |
|---|---:|---|---:|---:|---:|
| \((2,2,2,2,2)\) | 5 | \(((2,3)^5)\) | 5 | 720 | \(1/2400\) |
| \((3,2,2,2,1)\) | 4 | \(((3,2),(2,3),(2,3),(2,2),(1,2))\) | 1 | 8,640 | \(1/200\) |
| \((3,2,2,2,1)\) | 4 | \(((3,2),(2,4),(2,2),(2,2),(1,2))\) | 1 | 17,280 | \(1/100\) |
| \((3,2,2,2,1)\) | 4 | \(((3,3),(2,2),(2,2),(2,2),(1,3))\) | 3 | 2,160 | \(1/800\) |
| \((3,3,2,1,1)\) | 3 | \(((3,2),(3,1),(2,3),(1,2),(1,1))\) | 1 | 28,080 | \(13/800\) |
| \((3,3,2,1,1)\) | 3 | \(((3,3),(3,1),(2,1),(1,3),(1,1))\) | 1 | 32,400 | \(3/160\) |
| \((3,3,2,2,0)\) | 2 | \(((3,2),(3,1),(2,2),(2,1),(0,0))\) | 1 | 95,760 | \(133/2400\) |
| \((3,3,3,1,0)\) | 1 | \(((3,1),(3,1),(3,1),(1,0),(0,0))\) | 3 | 91,440 | \(127/2400\) |
| \((4,2,2,1,1)\) | 2 | \(((4,0),(2,2),(2,1),(1,2),(1,1))\) | 1 | 95,760 | \(133/2400\) |
| \((4,2,2,2,0)\) | 1 | \(((4,0),(2,1),(2,1),(2,1),(0,0))\) | 3 | 96,720 | \(403/7200\) |
| \((4,3,1,1,1)\) | 1 | \(((4,0),(3,0),(1,1),(1,1),(1,1))\) | 3 | 91,440 | \(127/2400\) |
| \((4,3,2,1,0)\) | 0 | \(((4,0),(3,0),(2,0),(1,0),(0,0))\) | 1 | 1,167,600 | \(973/1440\) |

Here \(d_v\) is the outdegree of vertex \(v\), and \(t_v\) is the number of directed 3-cycles containing \(v\). For five vertices the displayed multiset of pairs \((d_v,t_v)\), together with the sorted outdegrees and total number of cyclic triangles, distinguishes all 12 classes. The profile counts sum to \(120^3=1{,}728{,}000\).

Two boundary classes are especially simple. The unique regular five-vertex tournament, whose every vertex has outdegree \(2\), has only \(720\) ordered three-voter realizations, so its impartial-culture probability is
\[
rac{720}{120^3}=rac1{2400}.
\]
The transitive tournament class has \(1{,}167{,}600\) realizations, hence probability
\[
rac{1{,}167{,}600}{120^3}=rac{973}{1440}.
\]

## Assumptions and scope
The electorate has exactly three ordered voters. Every voter has a strict complete ranking of five alternatives. Profiles are counted under impartial culture: all \(120^3\) ordered triples of rankings are equally likely. The output is only the unweighted pairwise-majority tournament; pairwise margins beyond their signs are discarded.

The table quotients the output tournaments by relabeling of alternatives, but it does not quotient the input by voter permutations. The verifier separately enumerates anonymous three-ranking multisets and restores their multinomial weights, providing an independent check of the ordered-profile totals.

## Proof
Encode a strict ranking by the ten orientation bits on the unordered pairs of five alternatives. For three rankings with bit vectors \(a,b,c\), a pair is oriented forward by majority exactly when at least two of the three bits are \(1\), which is computed bitwise by
\[
(a\mathbin{\&}b)\;\mathbin{|}\;igl(c\mathbin{\&}(a\mathbin{|}b)igr).
\]
There are only \(120^3\) ordered triples, so exhaustive evaluation is finite and complete.

Independently, every one of the \(2^{10}=1024\) labeled five-vertex tournaments is canonically reduced under all \(5!=120\) relabelings. This produces exactly 12 orbits. For each orbit representative, its automorphism order is counted directly, and its invariant signature is computed from outdegrees and directed-triangle incidences. The 12 signatures in the table are pairwise distinct.

The first enumeration loops over all ordered triples of rankings and increments the canonical tournament class. A second enumeration loops only over the \(inom{122}{3}=295{,}240\) multisets of three rankings, weighting a multiset by \(1\), \(3\), or \(6\) according to whether all three rankings coincide, exactly two coincide, or all are distinct. These two exhaustive calculations agree entry by entry, proving the table.

## Verification
The embedded `verify_five_candidate_three_voter_tournaments.py` reconstructs all 1024 labeled tournaments, all 12 relabeling classes, and all \(120^3\) ordered preference profiles from scratch using only the Python standard library. It then performs the independent anonymous-profile enumeration and checks exact equality of the 12 class counts. It also verifies orbit-stabilizer divisibility and the uniqueness of the human-readable signatures.

Replay command:

`python3 verify_five_candidate_three_voter_tournaments.py`

The leading output must be `VERIFY_OK`.

## Relationship to prior work
Shepardson and Tovey study which tournaments can arise at a specified supermajority threshold and prove that every tournament on at most seven vertices is \(2/3\)-realizable. Eggermont, Hurkens, and Woeginger specialize to realizations by a fixed finite family of permutations and prove that every tournament on at most seven vertices is realizable by three permutations. Their 2013 paper performs isomorphism-level feasibility tests for seven through nine vertices and cites McKay's tournament catalogues.

Those results imply the surjectivity part of the present five-vertex statement: every five-vertex tournament class has at least one three-ranking realization. The inspected papers do not tabulate how many three-voter profiles map to each of the 12 five-vertex tournament classes. The present result refines realizability to the complete exact fiber distribution under impartial culture.

## Limitations
This is an exact finite census at five alternatives and three voters. It does not provide a closed formula for arbitrary numbers of alternatives or voters. It also does not retain pairwise majority margins, so profiles yielding the same unweighted tournament are intentionally identified at the output. A targeted literature and database search found no equivalent 12-class fiber table, but unindexed course notes, software output, or supplementary data could still contain one.

## References
1. D. Shepardson and C. A. Tovey, “Smallest Tournaments Not Realizable by \(2/3\)-Majority Voting,” prepublication version dated May 2008; *Social Choice and Welfare* 33 (2009), 495–503. DOI: 10.1007/s00355-009-0375-7.
2. C. Eggermont, C. Hurkens, and G. J. Woeginger, “Realizing Small Tournaments Through Few Permutations,” *Acta Cybernetica* 21 (2013), 267–271. DOI: 10.14232/actacyb.21.2.2013.4.
3. B. McKay, “Combinatorial Data — Catalogue of non-isomorphic tournaments up to 10 vertices,” cited as 2008 in Eggermont–Hurkens–Woeginger.

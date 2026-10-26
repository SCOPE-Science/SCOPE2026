# Ten voters are necessary and sufficient for tie-independent PAV house nonmonotonicity with three candidates

## Finding
Consider ordinary unweighted Proportional Approval Voting (PAV) on precisely three candidates. Call a profile *strongly nonnested* if no PAV-optimal one-member committee is contained in any PAV-optimal two-member committee. Such a profile has at least **ten voters**, even allowing empty ballots. At ten voters, exactly **three labeled anonymous approval profiles** are strongly nonnested, constituting one orbit under renaming the candidates. Up to renaming, the unique pattern comprises two ballots approving only \(B\), three approving \(A,B\), three approving \(A,C\), and two approving only \(C\). Its unique one-member winner is \(\{A\}\), while its unique two-member winner is \(\{B,C\}\).

The ten-voter witness additionally has voter-interval approval structure: arranging voters as two \(B\)-only, three \(AB\), three \(AC\), and two \(C\)-only makes each candidate's approving voters a contiguous interval. Thus even this structured domain need not admit a nested chain of *PAV-optimal* committees.

## Assumptions and scope
There are exactly three labeled candidates \(A,B,C\), and any finite number \(n\) of unweighted voters, each reporting any subset (possibly empty) of those candidates. For a committee \(W\) of cardinality \(k\), its PAV score is \(\operatorname{PAV}(W)=\sum_i H_{|W\cap S_i|}\), where \(H_0=0\), \(H_1=1\), and \(H_2=3/2\). Winners maximize this score separately for \(k=1\) and \(k=2\); ties are treated set-valuedly. Strong nonnesting demands \(W_1\not\subseteq W_2\) for every optimal singleton \(W_1\) and optimal pair \(W_2\). The conclusion is independent of tie-breaking; it does not claim that every ordinary tie-breaking failure requires ten voters.

## Proof
Let \(\mathcal W_1\) and \(\mathcal W_2\) denote the nonempty families of maximizers of sizes one and two. Every singleton is contained in two of the three candidate pairs. If \(\mathcal W_1\) contained at least two different singletons, then each possible pair would contain one of them. If \(\mathcal W_2\) contained at least two pairs, every possible singleton would lie in one. Therefore strong nonnesting forces \(\mathcal W_1\) and \(\mathcal W_2\) to be singletons as *families*, and their members must be complementary. Rename so \(\mathcal W_1=\{\{A\}\}\) and \(\mathcal W_2=\{\{B,C\}\}\).

Write \(p,q,r,u,v,w,t,e\) for the counts of ballots \(A,B,C,AB,AC,BC,ABC,\varnothing\), respectively. Unique singleton optimality gives
\[
 p+v>q+w,\qquad p+u>r+w.
\]
For the two-member comparison, a ballot approving only the newly added candidate contributes one point, whereas a ballot approving that candidate and the retained member contributes one half point. Consequently
\[
 \operatorname{PAV}(BC)-\operatorname{PAV}(AC)
 =q-p+\tfrac12(w-v)>0,\qquad
 \operatorname{PAV}(BC)-\operatorname{PAV}(AB)
 =r-p+\tfrac12(w-u)>0.
\]
The two pairs of strict inequalities equivalently imply
\[
 q\le p+v-w-1,\qquad 2q+w\ge2p+v+1,
\]
and the analogous pair with \(q,v\) replaced by \(r,u\). Doubling the first bound and combining with the second proves \(v-w\ge3\); similarly \(u-w\ge3\). Then the strict pair comparisons imply \(q\ge p+2\) and \(r\ge p+2\). All ballot counts are nonnegative integers, so
\[
\begin{aligned}
 n&=e+p+q+r+u+v+w+t\\
  &\ge e+3p+3w+t+10\ge10.
\end{aligned}
\]
For \(n=10\), equality forces \(e=p=w=t=0\) and the four other counts to attain their individual lower bounds: \(q=r=2\) and \(u=v=3\). This completely classifies minimal witnesses after candidate relabeling.

Conversely, for these ten ballots the singleton scores of \(A,B,C\) are respectively \(6,5,5\); the two-member PAV scores of \(AB,AC,BC\) are respectively \(19/2,19/2,10\). Hence the unique singleton and pair are \(A\) and \(BC\), proving both existence and the claimed uniqueness up to renaming. Choosing the distinguished singleton among the three labeled candidates yields exactly three anonymous profiles. The indicated voter order proves the voter-interval assertion.

## Verification
The self-contained \(\texttt{verify.py}\) program uses exact integers equal to six times the PAV scores, and enumerates every anonymous profile over the seven nonempty approval types for electorate sizes zero through ten. There are \(\binom{17}{7}=19{,}448\) such profiles in total. It finds no strongly nonnested profiles below ten voters and precisely three at ten voters. Run with Python 3.10 or later: `python verify.py`. This finite check is independent corroboration; the argument above proves the unbounded lower bound and full ten-voter classification. Adding empty ballots cannot create a smaller witness because they do not affect scores.

## Relationship to prior work
PAV is the harmonic Thiele optimization rule. Janson's *Phragmén's and Thiele's Election Methods* [2] explains the lack of house monotonicity in the general Thiele optimization method, including a four-voter example dependent on ties (Section 5) and a substantially larger three-candidate nonnested instance with twelve \(AB\), twelve \(AC\), ten \(B\), and ten \(C\) ballots (Section 13.4). Thus **nonmonotonicity and its existence are prior results**, not claimed here. The contribution is the exact minimum electorate size for *tie-independent* nonnesting with exactly three candidates, together with complete rigidity at that minimum. Manurangsi and Sornat [1] study efficient Thiele optimization and concavity of optimal objective values on voter-interval profiles; concavity of optimal *values* does not ensure nested *argmax committees*. The ten-voter witness makes that distinction explicit. Schünke [3] studies Pareto optimality in approval multiwinner elections, a weaker criterion than PAV-score maximality.

## Limitations
The minimum is proved only for exactly three candidates and unweighted ballots; no analogous minimum is claimed for larger candidate sets or weighted votes. The property is strong, tie-independent nonnesting rather than tie-dependent committee changes. Mathematical novelty is evaluated against cited, materially inspected primary sources and relevant literature searches, not certified as absolute historical priority. No external independent audit has been performed.

## References
[1] P. Manurangsi and A. Sornat, *Polynomial-Time Algorithm for Thiele Voting Rules with Voter Interval Preferences*, arXiv:2604.05953v1 (first posted April 7, 2026), especially Theorem 5.

[2] S. Janson, *Phragmén's and Thiele's Election Methods*, arXiv:1611.08826 (first posted November 2016), especially Sections 5 and 13.4.

[3] J. Schünke, *Pareto Optimality in Approval-Based Multiwinner Voting*, arXiv:2605.30490v1 (first posted May 2026).

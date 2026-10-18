# Sharp nine-voter separation between sequential PAV and sequential Phragmén

## Finding

For exactly three candidates, two committee seats, and nonempty approval ballots, consider elections in which each of the two sequential rules has a unique choice in both rounds. **Their committees can differ if and only if the electorate has at least nine voters.** At nine voters, precisely **six anonymous profiles with fixed candidate labels** yield such strict disagreement; they form **one** orbit under candidate relabeling. A representative is
\[
4\times\{C\},\qquad3\times\{A,C\},\qquad2\times\{B\}.
\]
Sequential PAV elects \(\{B,C\}\), whereas sequential Phragmén elects \(\{A,C\}\). The sharp nine-voter witness extends to every larger electorate by adding voters who approve only \(C\).

## Assumptions and scope

Let \(N\) be a finite nonempty electorate, \(C_0=\{A,B,C\}\) the candidate set, and \(k=2\) the number of seats. A ballot is any nonempty subset of \(C_0\). Voters are interchangeable but candidate labels distinguish profiles. Sequential PAV greedily adds the candidate maximizing the increase in the harmonic approval score \(\sum_v H_{|W\cap B_v|}\), where \(H_0=0\), \(H_1=1\), and \(H_2=3/2\). Sequential Phragmén uses the standard load-sharing rule: initially all loads vanish; a selected candidate costs one unit, divided among its supporters so their final loads are equal, and the candidate minimizing that common new load is selected.

A **strict separation** means that approval support has a unique largest candidate in round one and that each rule's second-round candidate is uniquely selected, with the two second-round candidates different. Cases in which either algorithm needs tie-breaking are explicitly outside this theorem. The result does not concern globally optimizing PAV, reverse sequential PAV, other committee sizes, or more than three candidates.

## Proof

**Two-round comparison.** Let \(C\) denote the uniquely chosen first candidate, with \(d\) approvals. Rename the other two candidates so that sequential Phragmén selects \(A\) in round two, while sequential PAV selects \(B\). Let their total approvals be \(a\) and \(b\), and let \(p\) and \(q\) count their respective approving voters who do **not** approve \(C\). Then \(a,b>0\), \(0\le p\le a\), \(0\le q\le b\), \(d>\max(a,b)\), and the electorate size \(n\) satisfies \(n\ge d+\max(p,q)\).

After \(C\) is selected, the sequential-PAV marginal of a remaining candidate with \(s\) supporters, \(u\) of whom did not approve \(C\), equals \((s+u)/2\). Sequential Phragmén's common new load for the same candidate equals
\[
L(s,u)=\frac{1+(s-u)/d}{s}=\frac1d+\frac{d-u}{ds}.
\]
In particular, strict disagreement in the indicated direction is equivalent to the **two strict inequalities**
\[
 b+q>a+p,\qquad a(d-q)>b(d-p). \tag{1}
\]
Every statement below follows from these two inequalities, positivity, and the support bounds. This reduction is exact: it is not a heuristic comparison of score proxies.

**Sharp lower bound.** Write \(t=a-b\).

If \(t=0\), the first inequality in (1) gives \(q>p\), while the second gives \(p>q\), impossible.

Suppose \(t>0\). The first inequality implies \(q-p\ge t+1\), so \(b\ge q\ge p+t+1\) and \(a=b+t\ge p+2t+1\). The second inequality rearranges to
\[
 dt>a(q-p)+tp\ge a(t+1)+tp.
\]
For \(t=1\), this gives \(d>2a+p\ge6+3p\), hence \(d\ge7+3p\). Therefore \(n\ge d+q\ge9+4p\). At \(n=9\), necessarily \(p=0\), \(q=2\), \(d=7\), \(a=3\), \(b=2\). For \(t\ge2\), the bound \(a\ge2t+1\) gives \(d>(2t+1)(t+1)/t=2t+3+1/t\), so the integer \(d\ge2t+4\). Hence \(n\ge d+q\ge3t+5\ge11\).

Suppose instead \(t<0\), and put \(h=b-a\ge1\). Inequality (1) becomes
\[
q-p>-h,\qquad bp-aq>hd.
\]
If \(p\le q\), then \(bp-aq\le hp\le ha<hd\), a contradiction. Thus \(r=p-q\ge1\); the first strict inequality forces \(r\le h-1\), so \(h\ge2\). Since \(d\ge b+1\), the second inequality forces
\[
 b(h-r)<h(p-r-1).
\]
The positive left side implies \(p\ge r+2\ge3\). Consequently \(n\ge d+p\ge b+p+1\ge2p+h+1\ge9\). If equality \(n=9\) were possible, every inequality used here would force \(p=3\), \(r=1\), \(h=2\), \(a=3\), \(b=5\), and \(d=6\). But then the required inequality \(bp-aq>hd\) would read \(9>12\), false. Thus this case requires more than nine voters.

It follows that no strict disagreement can occur with fewer than nine voters. At nine, the \(t>0\) case uniquely yields \((d,a,b,p,q)=(7,3,2,0,2)\). As \(a=3\) and \(p=0\), all three \(A\)-supporters approve \(C\); as \(b=q=2\), both \(B\)-supporters are outside the \(C\)-support group; as \(d+q=9\), there are no other voters. Thus the only possible approval profile is exactly \(3\) ballots \(\{A,C\}\), \(4\) ballots \(\{C\}\), and \(2\) ballots \(\{B\}\). All six candidate permutations have distinct labeled profiles, establishing the complete single-orbit classification.

**Existence and all larger sizes.** For the displayed witness the first-round support counts are \((a,b,d)=(3,2,7)\). The second-round sequential-PAV scores are \(3/2\) for \(A\) and \(2\) for \(B\), so it strictly elects \(B\). Sequential Phragmén's loads are \(L(3,0)=10/21\) for \(A\) and \(L(2,2)=1/2\) for \(B\), so it strictly elects \(A\). If \(j\ge0\) further ballots \(\{C\}\) are added, \(d=7+j\), while \(a=3\), \(b=2\), \(p=0\), \(q=2\) remain fixed. The PAV inequality remains strict, while Phragmén's criterion is \(3(d-2)>2d\), equivalently \(d>6\). Therefore a strict disagreement exists for every \(n=9+j\).

**Minimal structural domain.** With just one committee seat, both rules reduce to approval voting. With exactly two candidates and two committee seats, both necessarily elect the same committee. Three candidates and two seats therefore form the smallest candidate/seat domain where disagreement of the two rules is possible.

## Verification

Run `python3 verify.py` using Python's standard library. It independently implements exact rational sequential-PAV marginal scores and the two-round voter-load recurrence for sequential Phragmén, then exhausts all nonempty anonymous three-candidate approval profiles with \(1\le n\le9\). Every profile corresponds bijectively to a weak composition of \(n\) into the seven nonempty ballot types. Exactly \(11,439\) profiles are examined; all rules are scored exactly with rational arithmetic. The checker finds no strict separation for \(n\le8\), exactly six at \(n=9\), and verifies their relabeling orbit. It additionally checks \(100\) members of the unbounded extension family. The preceding case analysis, not the finite check, proves the assertions for arbitrary electorate size.

## Relationship to prior work

The sequential Thiele/PAV harmonic rule and the standard sequential Phragmén load rule are classical. Janson's survey, especially Sections 3, 4.2, and Examples 13.5–13.8, gives their definitions and explicit separating examples; Example 13.6 already exhibits a two-seat divergence for a much larger profile. Lackner and Skowron present both algorithms side by side in their approval-based committee voting monograph, Chapter 2. Brill and coauthors establish structural representation properties of Phragmén's methods. None of those statements is presented here as new.

The result proved above isolates a different finite boundary: the smallest strict separation with precisely three candidates and two seats, a complete labeled-profile classification at that boundary, and a witness for every larger electorate. No claim is made that arbitrary rule disagreements, ties, or larger candidate sets were previously unknown.

## Limitations

The lower bound and six-profile count require exactly three candidate labels, two seats, nonempty ballots, and unique selections in both rounds. They cannot be transferred to elections with a different number of candidates or to unresolved ties without further proof. Anonymous counting does not count separately all permutations of voter identities. The mathematical argument establishes the claim; independent publication-priority verification remains necessary.

## References

1. S. Janson, *Phragmén's and Thiele's election methods*, arXiv:1611.08826, first public version 27 November 2016; particularly Sections 3, 4.2, and 13. https://arxiv.org/abs/1611.08826
2. M. Lackner and P. Skowron, *Multi-Winner Voting with Approval Preferences*, Chapter 2, *Dramatis Personae: ABC Rules*, Springer, DOI:10.1007/978-3-031-09016-5_2. https://link.springer.com/chapter/10.1007/978-3-031-09016-5_2
3. M. Brill, R. Freeman, S. Janson, and M. Lackner, *Phragmén's Voting Methods and Justified Representation*, AAAI, DOI:10.1609/aaai.v31i1.10598. https://ojs.aaai.org/index.php/AAAI/article/view/10598

# The sharp four-voter manipulability frontier for three-project Nash budget division

## Finding

Consider approval-based division of one divisible budget among **three labeled projects**, with a nonempty truthful approval ballot from each voter. The Nash product rule maximizes the product of voters' approval utilities. A unilateral manipulation replaces one voter's ballot by any other nonempty approval ballot, and profitability is evaluated using that voter's **true** approvals.

1. For every electorate with one, two, or three voters, and every profile with three projects, **no voter has a profitable unilateral manipulation**, regardless of how the Nash rule resolves a nonunique maximizing budget allocation. Two-project Nash division is strategyproof for **any** finite electorate.
2. Four voters and three projects are the sharp first simultaneous sizes at which Nash division can be manipulated. Of the \(\binom{10}{6}=210\) anonymous four-voter approval profiles on the three labeled projects, exactly **six** permit manipulation. They form **two** project-relabeling orbits, each of size three. Each has exactly two profitable (truthful-ballot type, reported-ballot type) changes; hence there are **12** such changes across the 210 anonymous profiles. All are profitable under **every** maximizing-allocation tie resolution.
3. The largest true-utility multiplicative gain over these four-voter, three-project profiles is exactly \(5/4\). The complete set of strict-gain ratios is
   \[
   \left\{\frac54,\ \frac{9-\sqrt{17}}4\right\}.
   \]
   The first ratio occurs in one project-relabeling orbit and the second in the other.

A pair of representative four-ballot multisets, with projects \(A,B,C\), is \(\{\{B\},\{A,B\},\{C\},\{A,C\}\}\) and \(\{\{A,B\},\{C\},\{A,C\},\{B,C\}\}\). No claim is made about the first manipulation threshold when *more than three* projects are available, nor about manipulation by coalitions.

## Assumptions and scope

Let \(C=\{A,B,C\}\), \(N=\{1,\ldots,n\}\), and each truthful ballot \(S_i\subseteq C\) be nonempty. For a budget vector \(p\in\Delta(C)=\{p_j\geq0:\sum_jp_j=1\}\), voter \(i\)'s true approval utility is \(u_i(p)=\sum_{j\in S_i}p_j\). At the reported profile \(T\), any Nash allocation maximizes \(\prod_{i=1}^n\sum_{j\in T_i}p_j\). Uniform allocation makes all reported utilities positive, so maximizing their summed logarithms is equivalent. The induced vector of reported utilities is unique, although the allocation itself need not be. We use **ordinary** strategyproofness, allowing a manipulator to benefit from allocations to candidates they have falsely reported disliking; this is distinct from excludable strategyproofness.

An anonymous profile is the seven-vector \(c=(c_1,\ldots,c_7)\) of multiplicities of the nonempty approval masks \(001,010,011,100,101,110,111\), where the bit positions denote \(A,B,C\). The count of anonymous profiles for \(n\) voters is \(\binom{n+6}{6}\). Project relabeling permutes mask positions.

## Proof

**Concave optimality certificate.** Put \(v_{s,j}=1\) when mask \(s\) contains project \(j\) and zero otherwise, and let \(U_s(p)=\sum_jv_{s,j}p_j\). For every mask with \(c_s>0\), require \(U_s(p)>0\). The concave logarithmic objective is \(L_c(p)=\sum_sc_s\log U_s(p)\). Define the marginal scores
\[
G_j(p)=\sum_{s:c_s>0}\frac{c_sv_{s,j}}{U_s(p)}.
\]
Since \(\sum_jp_jG_j(p)=n\), the Karush–Kuhn–Tucker conditions \(G_j(p)\le n\), with equality whenever \(p_j>0\), are necessary and sufficient for a **global** optimum: the first-order concavity inequality gives \(L_c(q)-L_c(p)\le\sum_jG_j(p)(q_j-p_j)\le0\). Strict concavity in the positive utility vector implies that all Nash-optimal allocations have the same reported utility vector.

**Exact finite certificate for up to four voters.** The standalone \(\texttt{verify.py}\) enumerates all \(\binom{n+6}{6}\) count vectors for \(n=1,2,3,4\). For each vector it searches the simplex lattice with coordinates in \(\{0,1/24,\ldots,1\}\) and **accepts a candidate only after directly verifying the global KKT conditions using exact rational arithmetic**. The lattice alone does not constitute a proof of completeness: the executable assertion that every profile has an accepted certificate does. Three four-voter profiles have nonrational optima; for them it additionally checks the exact algebraic candidates consisting, up to permutation, of
\[
(t,t,1-2t),\qquad t=\frac{7-\sqrt{17}}{16}.
\]
For example, the three nonrational profiles are relabelings of the multiset \(\{\{A,B\},\{A,C\},\{B,C\},\{C\}\}\). The invariant \(t\) is the positive maximizing root of \(8t^2-7t+1=0\) in \((0,1/2)\), obtained by maximizing \((1-2t)(2t)(1-t)^2\); its exact KKT inequalities are independently checked by the program.

**Tie-independent manipulation test.** For a reported count vector, the program intersects the probability simplex with the equations fixing every reported voter's uniquely optimal utility. This intersection is *exactly* the Nash-optimal allocation face. Every vertex of that face is the intersection of three independent constraints drawn from its utility equations, the normalization equation and the three possible zero-coordinate equations. The program enumerates every such vertex by exact symbolic linear algebra, discards infeasible intersections, and evaluates the manipulator's true utility at **all** vertices. A linear true-utility function is maximized and minimized on this face at its vertices. Thus the test covers all possible Nash-optimal tie resolutions, not just the particular allocation used for the KKT certificate.

For \(n=1,2,3\), this complete test finds no strict gain. For \(n=4\), it finds six anonymous profiles, two profitable report types per profile, and the two gains in the Finding. The program checks that each profitable report is strictly beneficial at *every* vertex of the new optimal face. The six profiles are precisely all project permutations of the two displayed representatives; each orbit has three elements.

For clarity, in the first representative, the voter truly approving \(\{A,B\}\) can report \(\{A\}\). The truthful Nash allocation can be represented as \(p=(0,1/2,1/2)\), and the deviating allocation is \(q=(3/8,1/4,3/8)\); their true utilities are \(1/2\) and \(5/8\). In the second representative, a voter truly approving \(\{A,C\}\) can report \(\{A\}\). Their truthful utility equals \((9+\sqrt{17})/16\), and their new true utility is \(1\), giving ratio \((9-\sqrt{17})/4\).

**Two projects, arbitrary electorate.** If there are only two projects, let \(a\) and \(b\) count the singleton ballots approving just the first and just the second project. Voters approving both always have utility one, so for \(a+b>0\) Nash divides the budget \((a/(a+b),b/(a+b))\); when \(a+b=0\), all voters approve both and obtain utility one. A voter who truly approves both can never improve. A voter approving just one project cannot increase its funded share by replacing their singleton ballot with either of the other nonempty reports. Hence two-project Nash division is strategyproof for all finite electorates.

## Verification

Run \(\texttt{python verify.py}\) with Python 3.11+ and SymPy 1.14 (specified in \(\texttt{requirements.txt}\)). The checker performs 329 exact global-KKT certificates, examines all one-voter ballot changes across the \(7,28,84,210\) anonymous profiles, and uses exact rational and quadratic-field signs rather than numerical optimization. Expected per-electorate numbers of manipulable profiles are \(0,0,0,6\), with 12 profitable report pairs at four voters. Expected possible strict-gain ratios are \(5/4\) and \((9-\sqrt{17})/4\). This exhaustive finite proof covers only \(n\le4\) and three projects; the unrestricted two-project statement is proved analytically above.

## Relationship to prior work

Aziz, Lederer and Vollen (2026) establish the unrestricted Nash incentive ratio of two and bounds for other budget-division rules; their global asymptotic extremal bound does not specify the smallest market where Nash manipulation first occurs, the complete four-voter three-project orbit classification, or the sharp finite-market ratio \(5/4\). Aziz, Bogomolnaia and Moulin (2017) prove that Nash max product violates even *excludable* strategyproofness using a four-outcome construction with many more voters; this is a distinct incentive notion, and the present ordinary manipulation examples do not imply an excludable violation. Brandl et al. (2020/2022) study a related public-project Nash funding mechanism and its participation incentives, not this exact finite-profile classification. The concave-optimality criterion and the Nash rule themselves are established tools and are not claimed as contributions.

## Limitations

These are exact results for unweighted binary approvals and at most three projects, including all nonempty approval reports and all Nash tie resolutions. The sharp size, six-profile census and gain ratio apply to the four-voter, three-project cell, **not** to larger markets. The maximal gain approaches the known global upper bound only in other, larger instances; the present result does not sharpen that global bound. Independent verification and an exhaustive historical-priority search have not been performed; alternative earlier formulations cannot be ruled out. The computational certificate is a finite exhaustive proof because every finite case receives a checked exact optimality certificate and every deviation is examined, not because a numerical search was truncated.

## References

1. H. Aziz, P. Lederer and J. Vollen, *Approximate Strategyproofness in Approval-based Budget Division*, arXiv:2605.11736, first posted 2026-05-12. https://arxiv.org/abs/2605.11736
2. H. Aziz, A. Bogomolnaia and H. Moulin, *Fair Mixing: The Case of Dichotomous Preferences*, arXiv:1712.02542, first posted 2017-12-07. https://arxiv.org/abs/1712.02542
3. F. Brandl, F. Brandt, M. Greger, D. Peters, C. Stricker and W. Suksompong, *Funding Public Projects: A Case for the Nash Product Rule*, arXiv:2005.07997, first posted 2020-05-16. https://arxiv.org/abs/2005.07997

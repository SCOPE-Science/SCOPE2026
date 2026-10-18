# Sharp twelve-voter boundary for two-person group abstention under sequential PAV

## Finding

In sequential proportional approval voting (seqPAV) with exactly three candidates and a committee of size two, suppose every voter submits a nonempty approval ballot, all ties at both greedy stages are retained, and exactly two voters may abstain together. Under the Kelly extension of approval-count preferences, a beneficial two-voter abstention exists **if and only if the participating electorate has at least twelve voters**. The assertion for larger electorates follows by adjoining voters who approve all three candidates to a twelve-voter witness, which changes each first-round approval score equally and every second-round marginal by the same amount; hence it preserves both choice sets and the coalitional comparison.

Among twelve-voter elections, there are exactly **six** offending anonymous labeled instances, counted as pairs consisting of an unordered ten-voter profile and an unordered two-voter abstaining coalition. All six are images of one instance under permutations of the three candidate names. In particular, twelve is the sharp threshold within the specified two-abstainer, three-candidate domain. This does not assert a threshold for larger coalitions or for more candidates.

## Assumptions and scope

Let \(C=\{A,B,C\}\), \(k=2\), and let \(P\) be a finite multiset of nonempty ballots \(B_i\subseteq C\). For a committee \(W\), the proportional approval score is \(S_P(W)=\sum_i H_{|W\cap B_i|}\), where \(H_0=0\), \(H_1=1\), and \(H_2=3/2\). SeqPAV begins with the empty committee, adds an alternative of largest score increment in each of two rounds, and retains **every** committee arising from any possible tied greedy choice. Denote its nonempty set of winning committees by \(G(P)\).

For an unordered pair of voters \(I=\{i,j\}\), write \(P\setminus I\) for their joint abstention. Following the Kelly extension, the two voters benefit as a coalition exactly when, for each \(r\in I\),

\[
\min_{W\in G(P\setminus I)}|W\cap B_r|\ \ge\ \max_{V\in G(P)}|V\cap B_r|,
\]

and for at least one \(r\in I\),

\[
\max_{W\in G(P\setminus I)}|W\cap B_r|\ >\ \min_{V\in G(P)}|V\cap B_r|.
\]

The existential strict comparison is **not** a claim that every possible tie resolution strictly improves some voter's outcome. At least one voter must strictly prefer some abstention outcome to some participation outcome, while no coalition member may prefer any participation outcome to any abstention outcome.

## Proof

**Step 1: an integer characterization of seqPAV.** Write \(v_P(c)\) for the number of ballots containing candidate \(c\), and \(v_P(a,b)\) for the number containing both candidates. The first greedy stage chooses every \(a\) maximizing \(v_P(a)\). Given a first-stage choice \(a\), twice the marginal PAV score of a second candidate \(b\ne a\) equals

\[
M_P(a,b)=2v_P(b)-v_P(a,b).
\]

Indeed a voter who approves \(b\) contributes \(2\) to the doubled marginal when not already represented by \(a\), and \(1\) when also approving \(a\). Maximizing this integer expression yields exactly the second-stage greedy choices. Taking the union over all ties gives \(G(P)\) with no approximation or numerical tie tolerance.

**Step 2: complete finite boundary certificate.** Encode the seven nonempty ballot types by the bitmasks \(1,\ldots,7\). An anonymous multiset of \(n-2\) ballots is uniquely represented by a weakly increasing sequence of these seven masks; its number of possibilities is \(\binom{n+4}{6}\). The unordered two-person coalition is independently represented by one of \(\binom{8}{2}=28\) weakly increasing pairs of masks. Consequently every relevant election-and-coalition instance with \(n\) total voters appears exactly once in a search of

\[
28\binom{n+4}{6}
\]

cases. For each case, evaluate the integer two-round rule in Step 1 for the participating and abstaining profiles, and apply the two explicit Kelly inequalities above. The accompanying standalone `verify.py` enumerates precisely these complete finite sets; it has no randomization, external dependencies, floating-point comparisons, or early termination. Its exact counts are:

| Total voters | Anonymous profile/coalition cases | Beneficial pairs |
| ---: | ---: | ---: |
| 3 | 196 | 0 |
| 4 | 784 | 0 |
| 5 | 2,352 | 0 |
| 6 | 5,880 | 0 |
| 7 | 12,936 | 0 |
| 8 | 25,872 | 0 |
| 9 | 48,048 | 0 |
| 10 | 84,084 | 0 |
| 11 | 140,140 | 0 |
| 12 | 224,224 | 6 |

No valid two-voter abstaining coalition exists with fewer than three total voters while leaving a nonempty electorate. This exhaustive, arithmetically exact certificate proves the lower bound and the count at the first feasible size. Candidate permutations generate six distinct instances from the representative in Step 3; the script independently checks that this orbit is exactly the six enumerated instances, proving the uniqueness up to candidate relabeling.

**Step 3: the twelve-voter witness.** The ten voters remaining after abstention have approval profile

\[
3\times\{A\},\quad 2\times\{B\},\quad 2\times\{A,C\},\quad 3\times\{B,C\}.
\]

The two abstainers approve \(\{A\}\) and \(\{A,C\}\), respectively. Without them, all three first-round support totals equal \(5\). Starting with \(A\) or \(B\), the best continuation produces \(\{A,B\}\); starting with \(C\), the best continuation produces \(\{A,C\}\). Thus

\[
G(P\setminus I)=\bigl\{\{A,B\},\{A,C\}\bigr\}.
\]

With both abstainers participating, first-round support is \(7,5,6\) for \(A,B,C\), respectively, so \(A\) is the unique first choice. The doubled second-stage marginal scores are \(10\) for \(B\) and \(9\) for \(C\), hence

\[
G(P)=\bigl\{\{A,B\}\bigr\}.
\]

The voter approving only \(A\) obtains one approved committee member in all outcomes. The voter approving \(\{A,C\}\) obtains one when participating and either one or two when abstaining. Consequently both satisfy every required weak comparison and the latter supplies a strict comparison, establishing the claimed Kelly group-participation failure.

**Step 4: persistence at larger electorate sizes.** From this twelve-voter example, append any number of voters approving all three candidates. Adding one such voter contributes \(1\) to every first-round candidate's score and \(1\) to each doubled second-round marginal, regardless of the previously selected candidate. It therefore leaves both output sets and the two original abstainers' preference comparisons unchanged, establishing existence at each larger size.

## Verification

Running `python verify.py` recomputes every profile/coalition case in the table, the exact six-instance candidate orbit, and the representative outcomes. It also checks those outcomes by a separate routine that evaluates PAV marginal scores directly with rational arithmetic, independently of the support-count identity. The finite certificate is exhaustive for the **specified** domain because every nonempty ballot is one of seven masks and all anonymous multisets and unordered two-ballot coalitions are enumerated. It is not a claim about arbitrary numbers of candidates or abstainers.

## Relationship to prior work

Bullinger, Dong, Lederer and Mehler introduced the Kelly group-participation criterion for approval-based committee elections and proved group participation for **globally optimizing** ABC scoring rules, including optimizing PAV. Their Theorem 2 gives individual-participation failures for broad sequential rules for committee sizes at least three, whereas their Remark 1 explicitly states that sequential Thiele rules satisfy **individual** participation for committee size at most two. Neither fact implies group participation of the *greedy*, two-seat rule. The present result isolates exactly that distinction and gives a finite sharp bound and a complete minimal symmetry classification. The established global-PAV and individual-participation statements are not claimed as novel.

Lackner and Skowron describe the sequential PAV greedy selection rule and its difference from optimizing PAV. Dong and Lederer provide general axiomatic characterizations of sequential valuation rules; these do not state the specific two-person no-show census. The searched literature did not disclose the same sharp twelve-voter theorem, but this does not establish absolute publication priority.

## Limitations

The benefit is defined using Kelly's set-valued extension and involves an abstention-induced tie. Some **fixed deterministic tie-breaking orders** can select the participation committee after abstention as well, so the witness does not establish benefit under every deterministic tie-breaking rule. The sharp bound uses exactly three candidates, exactly two seats, exactly two abstainers, nonempty approval ballots, and anonymous counting of labeled-candidate profiles. It does not assert a minimum over unrestricted coalition sizes or candidate counts. The computer-assisted finite classification is conditional on the transparent exhaustive search code and has not received independent scientific audit.

## References

1. M. Bullinger, C. Dong, P. Lederer, C. Mehler, *Participation Incentives in Approval-Based Committee Elections*, arXiv:2312.08798v1 (publicly posted 14 December 2023), Sections 2.2 and 3.1, Theorems 1–2, Remark 1, and supplementary proofs. https://arxiv.org/pdf/2312.08798v1
2. M. Lackner and P. Skowron, *Multi-Winner Voting with Approval Preferences*, arXiv:2007.01795, Chapter 2.3, sequential Thiele methods. https://arxiv.org/abs/2007.01795
3. C. Dong and P. Lederer, *Characterizations of Sequential Valuation Rules*, arXiv:2302.11890 (2023), definitions and characterizations of greedy approval rules. https://arxiv.org/abs/2302.11890

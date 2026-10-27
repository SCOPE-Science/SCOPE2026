# Rigidity and minimum electorate size at the worst local-PAV score ratio

## Finding

For every integer \(k\ge 2\), consider an unweighted approval election with finite labeled voters, candidate set of size at least \(k\), and committees of \(k\) candidates. Let \(W\) be an exactly single-swap-local maximizer of the proportional approval voting (PAV) harmonic score, and let \(O\) be a globally optimal committee with positive score. The sharp ratio \(\operatorname{PAV}(W)/\operatorname{PAV}(O)=2k/(3k-1)\) was attained by a construction of Peters, Vaish, and Yadav (2026), whose Lemma 3.2 supplies the matching universal inequality. This result classifies **every equality profile**, up to approvals outside \(W\cup O\), and determines the **minimum number of voters** in any election realizing that equality:

\[
 n_{\min}(k)=\begin{cases}
 \dfrac{(3k-1)(k+1)}4,&k\text{ odd},\\[4pt]
 \dfrac{(3k-1)(k+2)}2,&k\text{ even}.
 \end{cases}
\]

In particular, \(n_{\min}(2)=10\), \(n_{\min}(3)=8\), \(n_{\min}(4)=33\), and \(n_{\min}(5)=21\). The source's uniform construction uses \(3k^2-k\) voters, generally more than necessary.

**Rigidity.** Necessarily \(W\cap O=\varnothing\), and every voter whose ballot meets \(W\cup O\) approves either exactly one candidate of \(O\) and none of \(W\), or exactly one candidate from each of \(W\) and \(O\). Index \(W=\{w_1,\ldots,w_k\}\) and \(O=\{a_1,\ldots,a_k\}\). There are nonnegative integers \(d_1,\ldots,d_k\), not all zero, such that the number of pair voters approving \(\{w_j,a_t\}\) is \(d_t\) independently of \(j\), and the number approving \(\{a_t\}\) alone, after projection onto \(W\cup O\), equals

\[
 b_t=S-\frac{k+1}{2}d_t\ \in\mathbb Z_{\ge0},\qquad S=\sum_{t=1}^{k}d_t>0.
\]

Voters approving none of \(W\cup O\) may be present; approvals outside \(W\cup O\) do not affect the displayed projection. Conversely, whenever the candidate set consists **exactly** of these \(2k\) candidates and the displayed nonnegative integer conditions hold, the resulting election has \(W\) exactly swap-local and \(O\) globally PAV-optimal, with equality at the sharp ratio. This is an exact characterization of the projected structure of all equality instances and of all equality instances with precisely \(2k\) candidates.

## Assumptions and scope

Each voter carries unit weight and an approval subset of candidates; repeated ballots represent distinct voters. Let \(H_0=0\) and \(H_s=\sum_{j=1}^{s}1/j\) for \(s\ge1\). Define \(\operatorname{PAV}(T)=\sum_i H_{|A_i\cap T|}\) for any committee \(|T|=k\). Exact swap locality means \(\operatorname{PAV}((W\setminus\{w\})\cup\{a\})\le\operatorname{PAV}(W)\) for each \(w\in W\) and \(a\notin W\). Exclude the zero-score case so that the ratio is meaningful. In the rigidity statement, voters may approve other candidates outside \(W\cup O\); their intersections with the two specified committees are the classified data.

## Proof

**1. Known harmonic bound with equality conditions reconstructed.** Fix a competitor \(O\ne W\), let \(r=|O\setminus W|=|W\setminus O|\), and for voter \(i\) set \(u=|A_i\cap W|\), \(x=|A_i\cap(O\setminus W)|\), \(y=|A_i\cap(W\setminus O)|\). The exact total contribution from all \(r^2\) directed swaps equals

\[
 \Gamma=\frac{x(r-y)}{u+1}-\frac{y(r-x)}u \quad(u>0),\qquad \Gamma=rx\quad(u=0).
\]

Lemma 3.2 of Peters, Vaish, and Yadav proves

\[
 (3r-1)H_u+2\Gamma\ge2rH_{u+x-y}.
\]

Summing and using the nonpositive swap gains gives \(\operatorname{PAV}(W)\ge 2r\operatorname{PAV}(O)/(3r-1)\). Since \(2r/(3r-1)\) decreases strictly in \(r\), equality at \(2k/(3k-1)\) with positive optimum implies \(r=k\), so the committees are disjoint. Equality also forces every swap from \(W\) to \(O\) to have exactly zero gain and every voter to attain equality in the displayed harmonic inequality.

We now independently determine *all* equality cases of that cited pointwise lemma for \(r\ge2\). When \(u=0\) we have \(y=0\) and the inequality reduces to \(x\ge H_x\), with equality exactly for \(x\in\{0,1\}\). For \(u>0\) and \(x\ge y\), the harmonic increment is at most \((x-y)/(u+1)\), whence

\[
 \frac{3r-1}{2}H_u+\Gamma-rH_{u+x-y}
 \ge\frac{r-1}{2}H_u-\frac{y(r-x)}{u(u+1)}\ge0.
\]

If \(x=0\) then \(y=0\) and this inequality is strict. If \(x\ge1\), using \(y\le u\) and \(r-x\le r-1\), the subtracted term is at most \((r-1)/(u+1)\). Thus equality requires \(u=1\), \(y=1\), \(x=1\); these values indeed give equality. If \(x<y\), the negative harmonic increment is at most \((x-y)/u\), giving instead the lower bound

\[
 \frac{r-1}{2}H_u-\frac{x(r-y)}{u(u+1)}>0,
\]

because \(x<y\le u\), \(r-y\le r-1\), and \(r\ge2\). Consequently the *only* equality voter types are \((u,x,y)=(0,0,0),(0,1,0),(1,1,1)\). This proves the claimed projected ballot patterns.

**2. Solve the entire equality system.** Let \(e_{jt}\) count voters whose projection is the pair \(\{w_j,a_t\}\), and \(b_t\) count voters projected to the singleton \(\{a_t\}\). Write \(R_j=\sum_t e_{jt}\) and \(C_t=\sum_j e_{jt}\). Directly evaluating the swap \(w_j\to a_t\), using the harmonic gain \(1/2\) for adding a second approved candidate, gives

\[
 \Delta_{jt}=-R_j+\tfrac12(e_{jt}+C_t)+b_t.
\]

All \(\Delta_{jt}\) vanish. Summing the identities \(2R_j-e_{jt}-C_t=2b_t\) over \(t\) shows \((2k-1)R_j=\sum_t C_t+2\sum_t b_t\), independent of \(j\). Hence every row total is the same. Comparing different rows in each remaining identity forces \(e_{jt}=d_t\) independent of \(j\). Defining \(S=\sum_td_t\), the identities reduce precisely to \(b_t=S-(k+1)d_t/2\). Conversely, these identities make all swaps between the \(2k\) displayed candidates neutral. The PAV scores then are

\[
 \operatorname{PAV}(W)=kS,\qquad
 \operatorname{PAV}(O)=kS+\sum_t b_t=\tfrac{3k-1}{2}S.
\]

The known universal harmonic inequality makes \(O\) globally optimal. Outside candidates can create additional swaps, so the converse is explicitly confined to a candidate set \(W\cup O\).

**3. Exact minimum.** Each nonzero \(d_t\) must satisfy \(S\ge(k+1)d_t/2\). For odd \(k\), choosing \(d_t=1\) for exactly \((k+1)/2\) columns and zero elsewhere attains the smallest possible \(S=(k+1)/2\), with integral nonnegative \(b_t\). For even \(k\), integrality of \(b_t\) forces every \(d_t\) to be even. A positive one is at least \(2\), giving \(S\ge k+1\); as \(S\) is even, \(S\ge k+2\). Equality is attained by setting \(d_t=2\) on \((k+2)/2\) columns and zero on the others. Each positive-score equality election has at least \(kS+\sum_t b_t=(3k-1)S/2\) voters; the constructions have no irrelevant voters and attain this bound. This proves the formula and its parity distinction.

## Verification

The standalone `verify.py` uses exact rational arithmetic to check the pointwise harmonic inequality and its equality cases for \(2\le r\le20\), \(0\le u\le24\), and all admissible \(x,y\) (57,627 tuples). It builds the predicted smallest elections for \(2\le k\le14\), checks all single swaps and exact score ratios, and enumerates all committees for \(2\le k\le6\). All checks passed. These finite tests corroborate the separately given argument and are not relied upon for its all-\(k\) quantifier.

## Relationship to prior work

Peters, Vaish, and Yadav (2026), Theorem 3.1, Lemma 3.2 and Appendix B, **already supply** the sharp harmonic inequality and an equality witness using \(3k^2-k\) voters. Neither the inequality nor the source's witness is claimed as new. The contribution here is the full equality-profile rigidity, parity-sensitive integer feasibility, and exact minimum electorate size, yielding substantially sparser extremizers. Kraiczy and Elkind (2024) study convergence lower bounds for PAV local search, a different invariant.

## Limitations

The theorem concerns exact one-swap local maxima and unweighted elections; it does not establish analogous rigidity for positive swap tolerances, approximate worst-case ratios, other Thiele scoring sequences, or extra-candidate converse instances. Equality profiles can contain voters irrelevant to both committees; these only increase electorate size. Historical priority beyond the specifically inspected literature is not independently certified.

## References

1. D. Peters, R. Vaish, J. Yadav, *Finding Representative and Approximately Efficient Committees*, arXiv:2609.07554v1, initially public 2026-09-07; Theorem 3.1, Lemma 3.2, Appendix B. https://arxiv.org/abs/2609.07554
2. S. Kraiczy, E. Elkind, *A Lower Bound for Local Search Proportional Approval Voting*, ESA 2024, DOI:10.4230/LIPIcs.ESA.2024.82. https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESA.2024.82

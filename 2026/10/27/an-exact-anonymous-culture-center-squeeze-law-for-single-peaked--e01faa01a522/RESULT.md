# An exact anonymous-culture center-squeeze law for single-peaked instant runoff

## Finding

Fix the ordered alternatives \(L<C<R\), an odd electorate \(n=2r+1\geq1\), and the four strict preferences compatible with this axis:
\(LCR\), \(CLR\), \(CRL\), and \(RCL\). Under *restricted impartial anonymous culture* (IAC), each nonnegative four-component frequency vector with total \(n\) is equally probable. Let \(E_n\) be the event that instant-runoff voting (IRV, or the Hare rule) fails to elect the Condorcet winner **for every admissible first-round tie break**. There is always a unique Condorcet winner in this single-peaked, odd-electorate setting.

Define
\[
q=\lfloor r/2\rfloor,\qquad h=\lfloor(2r-1)/3\rfloor,\qquad
B_n=\binom{n+3}{3},
\]
with empty sums interpreted as zero. Then the **exact finite probability** is
\[
\boxed{\Pr_{\mathrm{IAC}}(E_n)=\frac{1}{B_n}\left[
\sum_{m=1}^{q}m(m+1)+
\sum_{m=q+1}^{h}(m+1)(2r-3m)
\right].}
\]
It has the positive, exact large-electorate limit
\[
\boxed{\lim_{r\to\infty}\Pr_{\mathrm{IAC}}(E_{2r+1})=\frac7{144}.}
\]
The finite formula and its limiting constant concern uniformly sampled **anonymous histograms restricted to a fixed single-peaked axis**, not uniformly sampled independent ballots, not a randomly drawn axis, and not uniform anonymous histograms over all six unrestricted orders.

## Assumptions and scope

An election has three named, linearly ordered candidates and \(n\) odd voters, each submitting a complete strict ranking compatible with the known axis. Denote the histogram for the four displayed rankings by \((a,b,c,d)\), so \(a+b+c+d=n\). The first preferences for the left, center, and right candidates are \(a\), \(m=b+c\), and \(d\), respectively. IAC means that each of the \(\binom{n+3}{3}\) such integer histograms receives exactly the same probability; labels of voters carry no weight. Every admissible resolution of ties at IRV elimination stages is considered. All strict majority comparisons are tie-free because \(n\) is odd.

## Proof

**Step 1 (complete characterization of failure).** The center \(C\) defeats \(L\) exactly when \(a\le r\), and defeats \(R\) exactly when \(d\le r\). If \(a\ge r+1\) or \(d\ge r+1\), that extreme candidate has a strict first-preference majority and is simultaneously the Condorcet and IRV winner. Therefore, a Condorcet failure is possible only when \(C\) is the Condorcet winner, which requires \(a,d\le r\). On that region, IRV eliminates \(C\) under every permissible tie break if and only if \(m<\min(a,d)\). Indeed, the strict inequality makes \(C\) the unique smallest first-preference tally; otherwise there is either a first-round elimination of an extreme or a tie resolution eliminating an extreme, after which \(C\) beats the surviving extreme head-to-head. Consequently
\[
E_n\ \Longleftrightarrow\ a,d\le r\ \text{and}\ m<\min(a,d).
\]
In particular, the possible tie between \(L\) and \(R\) in first preferences when they both exceed \(m\) does not affect this characterization.

**Step 2 (finite enumeration).** For a fixed integer \(m\ge1\), there are \(m+1\) ways to choose \((b,c)\) with sum \(m\). With \(d=n-m-a\), the two inequalities from Step 1 give
\[
\max\{m+1,r+1-m\}\ \le a\ \le\ \min\{r,2r-2m\}.
\]
For \(1\le m\le\lfloor r/2\rfloor\), the interval contains exactly \(m\) integers; for \(\lfloor r/2\rfloor<m\le\lfloor(2r-1)/3\rfloor\), it contains exactly \(2r-3m\) integers; for larger \(m\) it is empty. Multiplying by \(m+1\) and summing proves the claimed numerator. Stars and bars gives the stated denominator.

**Step 3 (limiting probability).** Set \(t=m/n\) and \(x=a/n\), and scale the counting measure by \(n^{-3}\). The grid of feasible integer triples \((m,a,b)\), where \(c=m-b\), converges by elementary Riemann sums to the volume
\[
V=\int_0^{1/4}t^2\,dt+\int_{1/4}^{1/3}t(1-3t)\,dt=\frac7{864}.
\]
The first integrand uses the feasible \(a/n\)-interval of length \(t\), while the second uses length \(1-3t\). The remaining factor \(t\) is the continuum length of the possible \(b/n\)-interval. Integer floor boundaries contribute only a lower-order \(O(n^2)\) number of histograms: each boundary is linear and the feasible region is a fixed rational polytope. Thus the numerator equals \(Vn^3+O(n^2)\). Because \(\binom{n+3}{3}=n^3/6+O(n^2)\), division yields \(6V=7/144\), with an \(O(n^{-1})\) convergence error along odd \(n\). This proof covers all odd \(n\), including the small empty-sum cases.

## Verification

The accompanying standard-library program `verify.py` independently enumerates all anonymous preference histograms through odd electorate size \(17\), evaluates pairwise majority comparisons from the four full rankings, runs all legal IRV tie-breaking branches, and checks agreement with both the closed formula and the simple integer-inequality event. It also tests the algebraic count and the approach to \(7/144\) for larger electorates. Exact rational arithmetic is used for all finite probabilities. The finite code checks do not substitute for Step 3's proof of the infinite limit.

## Relationship to prior work

The single-peaked preference restriction, IRV's failure to always select a Condorcet winner, and the deterministic center-elimination mechanism are established prior facts; see Walsh (2015) for the four-order axis and Miller (2012) for center-elimination analysis. The distinction between impartial culture (independently sampled labeled ballots) and impartial anonymous culture (uniform frequency vectors) is standard and emphasized in the voting-probability literature, including Lackner and Lackner (2017). Existing analyses of scoring-runoff paradoxes on single-peaked domains, including Kamwa, Merlin, and Top (2023), examine different events such as participation and abstention. The claim here is restricted to the **exact** Condorcet-failure probability under uniform *four-type anonymous histograms* and its positive rational asymptotic limit; an exact probability or large-deviation result under an independent-ballot culture does not imply the unweighted count of anonymous histograms.

## Limitations

The probability is descriptive of a specified synthetic election culture, not an empirical frequency of IRV failures. It is sensitive to choosing uniform anonymous histograms *after* restricting to a common fixed single-peaked axis. With independent uniformly sampled ballots, the asymptotic behavior is different. The result establishes neither a voting-rule comparison across more than three candidates nor priority over inaccessible earlier literature. In particular, publications on Condorcet efficiency under spatial preferences and restricted domains may contain an equivalent count; historical novelty still requires independent validation.

## References

1. Toby Walsh (2015), *Generating Single Peaked Votes*, arXiv:1503.02766v1 (public 2015-03-10). https://arxiv.org/abs/1503.02766
2. Nicholas R. Miller (2012), *Monotonicity Failure in IRV Elections with Three Candidates*, conference manuscript dated 2012-02-28. https://userpages.umbc.edu/~nmiller/MONFAIL.CONF.FIN.REV.pdf
3. Marie-Louise Lackner and Martin Lackner (2017), *On the likelihood of single-peaked preferences*, Social Choice and Welfare.
4. Eric Kamwa, Vincent Merlin and Faty Mbaye Top (2023), *Scoring Run-off Rules, Single-peaked Preferences and Paradoxes of Variable Electorate*, working paper hal-03143741. https://ideas.repec.org/p/hal/wpaper/hal-03143741.html

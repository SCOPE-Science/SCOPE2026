# The first divergence of difference and ratio fairness in Borda-scored stable marriage

## Finding

In a complete strict one-to-one stable-marriage market with \(n\) agents on each side, assign each agent the positive rank utility \(u_a(M)=n+1-r_a(M)\), where \(r_a(M)\in\{1,\ldots,n\}\) is the rank of their partner in matching \(M\). Let
\[
 D(M)=\max_a u_a(M)-\min_a u_a(M),\qquad
 R(M)=\frac{\max_a u_a(M)}{\min_a u_a(M)}.
\]
Then:

1. For every \(n\leq3\) and every strict complete preference profile, \(D\) and \(R\) induce **exactly the same weak ordering** on all stable matchings, including ties. Thus their sets of minimizers coincide.
2. For \(n=4\), the two objectives never strictly reverse the order of two matchings: \(D(M)<D(M')\) implies \(R(M)\leq R(M')\) (indeed this holds for arbitrary complete matchings). Consequently, the two objectives always possess at least one common optimum.
3. Nevertheless at \(n=4\) their full optimum sets can differ. The explicit profile below has precisely two stable matchings, both of difference gap \(2\), with ratios \(2\) and \(3\). Thus the difference objective selects both while the ratio objective selects only one. Hence four pairs are the smallest market size permitting different minimizer sets under these canonical utilities.

## Assumptions and scope

There are \(n\) men and \(n\) women, every individual strictly ranks all \(n\) members of the other side, and all pairs are acceptable. A matching is a bijection. Stability means no unmatched man-woman pair strictly prefers each other to their assigned partners. All \(2n\) individual utilities contribute to each objective; every utility is in \(\{1,\ldots,n\}\), so the ratio is well defined. Claims concern only the positive Borda (rank-reversal) coding, not arbitrary cardinal utilities, incomplete lists, or capacities.

## Proof

**Small-market structural lemma.** When \(n=3\), any stable matching either assigns at least one agent their first choice or assigns **every** agent their second choice.

Suppose to the contrary that no agent receives a first-choice partner but some agent receives a third-choice partner. Relabeling the sides if necessary, take a man \(a\) who receives woman \(z\) as his third choice, and let \(x,y\) be his two preferred women. Let \(b\) and \(c\) be the partners of \(x\) and \(y\), respectively. To prevent \((a,x)\) and \((a,y)\) from blocking, both women must prefer their current partners to \(a\). With no first-choice assignment anywhere, each of \(x,y\) ranks her current partner second and \(a\) third. Therefore \(x\) ranks \(c\) first, and \(y\) ranks \(b\) first. Since \(b\) receives \(x\), he cannot rank \(x\) first (by assumption), and cannot rank \(y\) first (as \(y\) ranks him first, they would block). Thus \(b\) ranks \(z\) first. Symmetrically \(c\) ranks \(z\) first. For neither \((b,z)\) nor \((c,z)\) to block, \(z\) must prefer her assigned man \(a\) to both \(b,c\), giving \(z\) her first choice, a contradiction. The lemma follows.

For \(n=2\), a matching with no first-choice assignments would assign everyone their second choice. Either unmatched pair then consists of mutual first choices and blocks, so every stable matching has at least one first-choice agent. The case \(n=1\) is immediate.

Now for \(n=3\), if a stable matching has no first-choice recipient, the lemma forces all six rank values to equal \(2\), hence \(D=0\) and \(R=1\). Otherwise its minimum attained rank is \(1\). Writing \(h\) for its largest attained rank gives
\[
 D=h-1,\qquad R=\frac{3}{4-h},\qquad h\in\{1,2,3\}.
\]
Both expressions are strictly increasing functions of \(h\), and the all-second case (if present) is uniquely best in both scores. Thus \(D\) and \(R\) yield the same strict comparisons and ties on the entire stable set. For \(n=2\), the same argument with first-choice rank \(1\) applies. This proves assertion 1 analytically.

For \(n=4\), list every possible ratio at a given difference gap. Since utilities lie in \(\{1,2,3,4\}\), the possibilities are

| \(D\) | possible \(R\) |
|---|---|
| \(0\) | \(1\) |
| \(1\) | \(4/3,\ 3/2,\ 2\) |
| \(2\) | \(2,\ 3\) |
| \(3\) | \(4\) |

Every ratio in a smaller-gap row is less than or equal to every ratio in a larger-gap row. Therefore strict improvements in \(D\) cannot worsen \(R\), and a minimizer of \(R\) can be chosen among the minimum-\(D\) matchings. This does not require stability. This proves assertion 2.

**Exact four-pair witness.** Each row lists the strict preference order from best to worst, with people indexed \(1,2,3,4\) on each side. Men's rows are
\[
 (3,1,4,2),\ (3,1,2,4),\ (4,3,2,1),\ (4,2,1,3),
\]
and women's rows are
\[
 (4,3,1,2),\ (1,4,3,2),\ (4,3,2,1),\ (1,2,3,4).
\]
Encode a matching by the women assigned to men \(1,2,3,4\). Directly testing every possible man-woman pair for a blocking pair in each of the \(4!=24\) bijections leaves **exactly**
\[
 M=(1,3,4,2),\qquad N=(1,4,3,2).
\]
For \(M\), the sorted eight partner ranks are \((1,1,2,2,2,3,3,3)\); therefore \((D(M),R(M))=(2,2)\). For \(N\), they are \((2,2,2,2,2,2,3,4)\); therefore \((D(N),R(N))=(2,3)\). Hence both matchings minimize difference, but only \(M\) minimizes ratio. Assertion 3 and sharpness follow.

## Verification

The self-contained Python program `verify.py` checks every strict complete profile at \(n=1,2,3\), enumerates all bijections and all possible blocking pairs, compares every ordered pair of stable matchings under both objectives using exact rational arithmetic, and evaluates all \(24\) bijections of the four-pair witness. It checks \(1\), \(16\), and \(46{,}656\) profiles respectively, involving \(1\), \(18\), and \(60{,}324\) stable-matching occurrences, and confirms the precise two-element stable set at the witness. Run `python3 verify.py` without third-party dependencies. The universal small-market conclusions are proved above independently of this finite verification; the witness's exhaustive \(24\)-matching check is a complete finite certificate.

## Relationship to prior work

Sheng and Yokoi introduced difference- and ratio-based minimum-utility-gap objectives and polynomial-time algorithms for both, including far more general many-to-many settings and utility functions. The present finding is a specialized structural relationship between their two objectives under the natural fixed Borda rank coding: complete weak-order equivalence through three pairs, guaranteed common optima through four pairs, and the first exact separation of their optimum sets at four pairs. Their published algorithms solve each objective but do not imply equality of argmin sets, and their non-submodularity examples use different utility specifications. Classical stability and deferred acceptance are due to Gale and Shapley. Other comparisons with optimal stable-marriage welfare and minimum-regret criteria use different objective functions and are not substitutes for the present difference-versus-ratio analysis.

## Limitations

This is not an impossibility statement for all utility codings or all larger markets. No claim is made about strict reversals, common optimum existence, or optimal-set containment for \(n\geq5\). The four-pair example distinguishes minimizer **sets**, not their optimal difference values (both are \(2\)). Prior-publication priority beyond the inspected indexed records remains a residual risk; no independent scientific audit has been performed.

## References

1. Y. Sheng and Y. Yokoi, *Stable Matchings with Minimum Utility Gap*, arXiv:2607.07160, first public July 8, 2026, https://arxiv.org/abs/2607.07160 .
2. D. Gale and L. S. Shapley, *College Admissions and the Stability of Marriage*, American Mathematical Monthly 69 (1962), 9–15.
3. D. Gusfield and R. W. Irving, *The Stable Marriage Problem: Structure and Algorithms*, MIT Press, 1989.

# Exact finite-electorate quality price for two-seat reciprocal justified representation

## Finding
Fix an integer \(n\ge 2\). Consider every approval-based election with exactly \(n\) voters, at least two candidates, committee size two, positive candidate qualities at most one, and at least one approving voter for every candidate. Let \(Q^{\star}\) be the maximum sum of two candidate qualities, and let \(Q_{\mathrm{rJR}}\) be the maximum sum over size-two committees satisfying reciprocal justified representation (rJR). Then
\[
\sup_{\mathcal I:\,|V|=n,\ k=2}\frac{Q^{\star}(\mathcal I)}{Q_{\mathrm{rJR}}(\mathcal I)}
=\frac{4(n-1)}{3n-2}.
\]
The supremum is attained by a three-candidate election for every \(n\ge 2\). In particular, the exact maximum quality loss for a finite electorate is strictly smaller than the unrestricted asymptotic price \(4/3\), except in the limit as \(n\) tends to infinity. More precisely, the difference between these prices is \(4/[3(3n-2)]\).

There is also an extremal necessary condition when \(n\ge3\): if equality holds and \(\{a,b\}\) is any maximum-quality committee, then \(h_a=h_b=1\), and some unselected candidate \(c\) has quality \(h_c=n/[2(n-1)]\), approved by all but one voter who approve neither \(a\) nor \(b\). Thus the worst loss requires a maximally large unrepresented bloc and a candidate exactly at its reciprocal affordability boundary. This condition is necessary, not claimed sufficient in elections with additional candidates.

## Assumptions and scope
A profile consists of a finite voter set \(V\) of size \(n\), a candidate set \(C\) with \(|C|\ge 2\), approval sets \(A_i\subseteq C\) for every voter \(i\), and qualities \(h_c\in(0,1]\). Every candidate has at least one supporter. A committee \(W\subseteq C\) contains exactly two candidates; its quality is \(h(W)=\sum_{c\in W}h_c\). Let \(N(c)=\{i:c\in A_i\}\) and \(U(W)=\{i:A_i\cap W=\varnothing\}\).

Reciprocal JR is as in Boehmer, Dong, Kreisel, and Utke (2026): a group \(S\) that commonly approves candidate \(c\) can demand some representation when \(|S|\ge n/(2h_c)\); the requirement is met when at least one voter in the group approves an elected candidate. Equivalently, for a particular committee,
\[
W\text{ satisfies rJR}\quad\Longleftrightarrow\quad
2h_c\,|N(c)\cap U(W)|<n\quad\text{for every }c\in C.
\tag{1}
\]
Equality in the inequality on the right means **failure** of rJR. This exact integer/support formulation avoids rounding or tie ambiguities.

## Proof
**Reduction (1).** If a committee violates rJR, there is an unrepresented voter group \(S\subseteq U(W)\) and a commonly approved candidate \(c\), with \(|S|\ge n/(2h_c)\). Consequently, \(|N(c)\cap U(W)|\ge n/(2h_c)\). Conversely, if this latter inequality holds, choosing \(S=N(c)\cap U(W)\) gives a group entitled to representation but receiving none. This proves (1).

**Universal upper bound.** Choose the two top-quality candidates \(a,b\), and write \(\alpha=h_a\ge\beta=h_b\); their sum is \(Q^{\star}=\alpha+\beta\). If \(W_0=\{a,b\}\) satisfies rJR then the ratio is one. Otherwise (1) supplies a candidate \(c\notin W_0\) and a set of \(s=|N(c)\cap U(W_0)|\) unrepresented supporters with \(2h_cs\ge n\). Because \(a\) has at least one supporter, and nobody in \(U(W_0)\) approves \(a\), we have \(s\le n-1\). Thus
\[
h_c\ge r_n:=\frac{n}{2(n-1)}.
\tag{2}
\]
If \(h_c<1\), then \(s\ge n/(2h_c)>n/2\), so \(c\) alone represents a strict majority. In particular \(|U(\{a,c\})|<n/2\). Every quality is at most one, whence every candidate \(d\) satisfies \(2h_d|N(d)\cap U(\{a,c\})|<n\). By (1), \(\{a,c\}\) satisfies rJR, and \(Q_{\mathrm{rJR}}\ge\alpha+h_c\). Since \(\beta\le\alpha\le1\),
\[
\frac{Q^{\star}}{Q_{\mathrm{rJR}}}
\le\frac{\alpha+\beta}{\alpha+h_c}
\le\frac{2\alpha}{\alpha+r_n}
\le\frac{2}{1+r_n}
=\frac{4(n-1)}{3n-2}.
\tag{3}
\]
For completeness, if \(h_c=1\), maximality of \(a,b\) implies \(\alpha=\beta=1\). We show that there exists an rJR committee of quality two. If \(|N(c)|>n/2\), then \(\{a,c\}\) satisfies rJR by the same majority argument. Otherwise \(|N(c)|=n/2\), so \(n\) is even; put \(R=V\setminus N(c)\). If some candidate \(d\) of quality one is approved by every voter in \(R\), then \(\{c,d\}\) covers all voters and satisfies rJR. If no such \(d\) exists, consider \(\{c,a\}\). All of its unrepresented voters lie in \(R\). A violating candidate would need at least \(n/2\) of them and quality one; it would therefore be approved by all of \(R\), contrary to the assumption. Hence \(\{c,a\}\) is rJR. In either case the ratio is one, proving the upper bound also in this case.

**Attainment.** Take three candidates \(a,b,c\) with qualities \(h_a=h_b=1\) and \(h_c=r_n\). One voter approves exactly \(a,b\), and all other \(n-1\) voters approve exactly \(c\). The unrestricted optimal committee is \(\{a,b\}\) of quality two. It fails rJR because \(2h_c(n-1)=n\). Both \(\{a,c\}\) and \(\{b,c\}\) cover all voters and therefore satisfy rJR, each of quality \(1+r_n\). There are no other size-two committees. Thus \(Q_{\mathrm{rJR}}=1+r_n\), and the ratio is exactly the right-hand side of (3). This also handles \(n=2\), when the price equals one.

**Necessary extremal geometry.** For \(n\ge3\), the claimed optimal ratio exceeds one. Therefore in an instance attaining it, \(W_0\) violates rJR and the witness candidate cannot have quality one (that case gives ratio one). Equality throughout (3) forces \(\alpha=\beta=1\) and \(h_c=r_n\): the first equality requires \(\beta=\alpha\), the next requires \(h_c=r_n\), and the final requires \(\alpha=1\). Then \(s\ge n/(2r_n)=n-1\) and \(s\le n-1\), so \(s=n-1\). The lone remaining voter must approve both \(a\) and \(b\) because each is supported, and all other voters approve \(c\) but neither \(a\) nor \(b\), as claimed.

## Verification
The proof above applies to all finite candidate counts and all real qualities in \((0,1]\); it does not depend on numerical enumeration. `checker.cpp` independently implements the exact support criterion (1) using bit masks and checks the ratio by cross-multiplying integers. It exhausts supported approval configurations for \(n=2,3,4,5\) and three candidates, and for \(n=2,3\) and four candidates, with qualities in the exact grid \(\{1/2,2/3,3/4,1\}\). It also checks the explicit rational sharpness construction separately for every \(2\le n\le15\). Compile with `g++ -std=c++17 -O2 checker.cpp -o checker` and execute `./checker`. The observed output concludes `ALL EXACT CHECKS PASS`. These finite checks corroborate but do not substitute for the universal proof.

## Relationship to prior work
Boehmer, Dong, Kreisel, and Utke (arXiv:2609.08830v1, 8 September 2026) introduced reciprocal representation and proved the unrestricted quality price \(4/3\), including a three-candidate, two-seat family approaching this price (Proposition 5.6 and Example G.1). Their example gives the lower-bound extremal profile above on choosing the smallest quality satisfying a finite bloc's entitlement. What is proved here beyond that construction is a matching finite-\(n\) upper bound **uniform over arbitrary numbers of supported candidates** and a necessary geometry for equality. Their general approximation guarantee \(3/4\) alone does not imply this strict finite-\(n\) improvement. Related quality-floor bounds fix a lower bound on candidate qualities and optimize over electorate sizes; they do not state the fixed-electorate identity here.

## Limitations
The conclusion is for reciprocal **JR only**, committee size two, and candidates approved by at least one voter. It does not assert the same finite-\(n\) price for reciprocal EJR, threshold-PJR+, value-EJR, larger committees, or unsupported candidates. The equality geometry is only a necessary condition in elections with more than three candidates. The construction in the source paper already contains the lower-bound mechanism, so the novelty claim rests on the universal finite-electorate upper bound and equality structure. Unidentified independently discovered equivalent finite-parameter bounds remain a publication-priority risk. The result has undergone only the accompanying self-review; independent audit has not been performed.

## References
Boehmer, N., Dong, C., Kreisel, L., and Utke, M. (2026). *Approval-Based Multiwinner Voting with Candidate Qualities.* arXiv:2609.08830v1, first posted 8 September 2026. In particular, Definitions 5.1–5.3, Proposition 5.6, Theorem 5.5, and Appendix G. https://arxiv.org/abs/2609.08830

Brill, M. and Peters, J. (2023). *Robust and Verifiable Proportionality Axioms for Multiwinner Voting.* Context for proportional representation, as cited in the preceding paper.

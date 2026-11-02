# Exact minimum-support quality frontier for two-seat reciprocal representation

## Finding
Fix integers \(n\ge4\) and \(2\le d\le n\). In an approval election with \(n\) voters, at least two candidates, positive candidate qualities at most one, every candidate approved by at least \(d\) voters, and a two-seat committee, let \(Q^*\) denote the maximum sum of two candidate qualities. Let \(Q_{\mathrm{rJR}}\) be the maximum sum among size-two committees satisfying reciprocal justified representation (rJR). Then the *sharp* worst-case retained quality is
\[
\inf_{\mathcal I}\frac{Q_{\mathrm{rJR}}(\mathcal I)}{Q^*(\mathcal I)}=
\begin{cases}
\dfrac{3n-2d}{4(n-d)},&2d<n,\\[4pt]
1,&2d\ge n.
\end{cases}
\]
The infimum is attained for every parameter pair. A quality-maximizing two-seat committee needs at most one candidate substitution to meet rJR while attaining the guarantee. If \(2d>n\), each quality-maximizing committee is rJR; at equality a quality-maximizing rJR committee exists, but not necessarily every quality-maximizing committee qualifies. Thus strict majority support removes the quality/representation tradeoff altogether.

## Assumptions and scope
Let \(V\) be a labeled voter set with \(|V|=n\), and \(C\) any finite set with \(|C|\ge2\). Each voter \(i\in V\) approves a set \(A_i\subseteq C\), and each \(c\in C\) has exogenous quality \(0<h_c\le1\) and support \(N(c)=\{i:c\in A_i\}\) with \(|N(c)|\ge d\). A committee \(W\subseteq C\) has \(|W|=2\), value \(Q(W)=\sum_{c\in W}h_c\), and uncovered voters \(U(W)=\{i:A_i\cap W=\varnothing\}\). A group \(S\subseteq V\) blocks rJR if some \(c\in C\) satisfies \(S\subseteq N(c)\cap U(W)\) and \(|S|\ge n/(2h_c)\). Consequently, \(W\) satisfies rJR precisely when
\[
2h_c\,|N(c)\cap U(W)|<n\quad\text{for every }c\in C.
\]
The inequality is strict: equality constitutes a violation. No disjointness among candidate supports or assumption that every voter approves a candidate is needed.

## Proof
Choose a maximum-quality pair \(W=\{a,b\}\), labeling its members so that \(h_a\ge h_b\). If \(W\) is rJR, then \(Q_{\mathrm{rJR}}=Q^*\), as required. Suppose \(W\) fails. By the displayed criterion there is a candidate \(c\notin W\) with \(s=|N(c)\cap U(W)|\) and \(2h_c s\ge n\). Since \(N(a)\cap U(W)=\varnothing\) and \(|N(a)|\ge d\), we have \(s\le n-d\). Therefore
\[
h_c\ge \frac{n}{2s}\ge\frac{n}{2(n-d)}=:\alpha_{n,d},\qquad s\ge\frac{n}{2h_c}\ge\frac n2.
\]
The support union \(N(a)\cup N(c)\) contains the \(s\) uncovered supporters of \(c\) and at least \(d\ge2\) distinct supporters of \(a\), hence has cardinality at least \(s+d>n/2\). Set \(W'=\{a,c\}\). Every group capable of violating rJR has size at least \(n/2\), because all qualities are at most one; but only \(<n/2\) voters lie outside the union \(N(a)\cup N(c)\). Therefore no blocking group is disjoint from \(W'\), and \(W'\) satisfies rJR.

If \(2d<n\), the repaired pair has \(Q(W')\ge h_a+\alpha_{n,d}\). Since \(Q^*=h_a+h_b\le2h_a\) and \(0<h_a\le1\),
\[
\frac{Q(W')}{Q^*}\ge\frac{h_a+\alpha_{n,d}}{2h_a}
\ge\frac{1+\alpha_{n,d}}2
=\frac{3n-2d}{4(n-d)}.
\]
If \(2d>n\), then the same violation would force \(h_c\ge\alpha_{n,d}>1\), impossible; hence every maximum-quality pair satisfies rJR. If \(2d=n\), a violation forces \(h_c=1\); since \(c\notin W\) and \(W\) maximizes total quality, \(h_a=h_b=1\) as well. The rJR repair \(W'\) also has maximum quality two. For \(d=n\), no committee can have uncovered voters, and the same conclusion holds directly.

To attain the lower-branch bound when \(2d<n\), divide \(V=T\sqcup S\) with \(|T|=d\) and \(|S|=n-d\). Introduce exactly three candidates \(a,b,c\), with \(h_a=h_b=1\), \(h_c=n/[2(n-d)]\), \(N(a)=N(b)=T\), and \(N(c)=S\). All support constraints hold. The top-quality pair \(\{a,b\}\) leaves all \(n-d\) supporters of \(c\) uncovered and violates rJR at equality \(2h_c(n-d)=n\). Every pair containing \(c\) covers all voters and is rJR. Its maximum attainable value is \(1+h_c\), whereas \(Q^*=2\), proving sharpness. For \(2d\ge n\), the upper bound one is attained by every admissible instance (for example, universal approvals). This completes the proof.

## Verification
The analytical proof covers every allowed integer \(n,d\), every finite candidate set, and every real quality vector in the stated interval. The independent standalone finite-arithmetic checker `verify.py` enumerates \(434161\) approval/quality profiles using integer-scaled qualities, checks the exact lower bound and one-substitution repair, and verifies explicit sharp three-candidate examples for \(870\) parameter pairs (including boundary consistency checks with \(d=1\), which is not a novel case). Run `python verify.py`. The expected completed output begins `VERIFY_OK`. Finite enumeration is not substituted for the proof.

## Relationship to prior work
Boehmer, Dong, Kreisel, and Utke (2026), *Approval-Based Multiwinner Voting with Candidate Qualities*, introduce reciprocal representation and show a general \(3/4\) lower bound on retained committee quality, asymptotically tight. An earlier finite-electorate analysis determined the precise two-seat price when each candidate merely has at least one supporter, \(4(n-1)/(3n-2)\). The case \(d=1\) is therefore **previously covered**. The present theorem establishes the different, sharp \(d\)-dependent frontier for \(d\ge2\), including the majority-support phase transition and a constructive single-replacement certificate; neither cited baseline alone implies the improved \(d\)-specific bound. Classical JR counts shared approvals without using quality-dependent reciprocal affordability, and thus does not itself imply this frontier.

## Limitations
The result is confined to size-two committees, positive qualities bounded above by one, and a uniform **minimum** number of approving voters per candidate. It does not assert the same frontier for larger committees, weighted voters, or alternative proportionality axioms. The proof does not classify all equality cases. Closely related unpublished analyses or stronger general statements may exist, so independent priority verification remains appropriate. The finite checker covers selected small profiles and exact extremizers, not all real-quality profiles; the proof supplies the infinite guarantee.

## References
1. N. Boehmer, C. Dong, L. Kreisel, and M. Utke, *Approval-Based Multiwinner Voting with Candidate Qualities*, arXiv:2609.08830v1, publicly available 2026-09-08. In particular quality cost of reciprocal representation and its appendix.
2. H. Aziz et al., classical justified representation and approval-based committee voting; see the related literature and references in arXiv:2609.08830v1.
3. *Exact finite-electorate quality price for two-seat reciprocal justified representation*, earlier related finite-electorate finding, 2026, stable internal identifier `aaaa6781-69eb-4ef4-8cc4-991f32faff24` (used only to distinguish covered special case).

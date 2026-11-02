# Exact two-voter quality price of reciprocal justified representation

## Finding
For every integer \(k\ge2\), among all finite elections with precisely two voters, at least \(k\) candidates of quality in \((0,1]\), each approved by at least one voter, and size-\(k\) committees, the exact supremum of the unrestricted maximum total candidate quality divided by the maximum total quality obtainable subject to reciprocal justified representation (rJR) is
\[
\boxed{R_k=\frac{k^2}{k^2-k+2}.}
\]
Every instance admits an rJR committee attaining the corresponding quality approximation \((k^2-k+2)/k^2\). Over all committee sizes, the largest possible quality price is \(8/7\), attained among sizes \(k\ge2\) exactly at \(k=4\). These are exact maxima, not merely limiting suprema.

## Assumptions and scope
Let \(V=\{1,2\}\), \(C\) be a finite candidate set of cardinality \(m\ge k\ge2\), and each candidate \(c\) have quality \(0<h_c\le1\). Approval sets \(A_i\subseteq C\) satisfy \(A_1\cup A_2=C\). For a size-\(k\) committee \(W\), define \(Q(W)=\sum_{c\in W}h_c\). A coalition \(S\subseteq V\) can reciprocally demand one representative when it commonly approves some candidate \(c\) with \(|S|\ge 2/(k h_c)\). The rJR condition demands \(W\cap(\bigcup_{i\in S}A_i)\ne\varnothing\) for every such \(S\). This is precisely the JR-level reciprocal affordability notion of Boehmer et al. (Definition 5.2), specialized to two voters; no requirements of stronger rEJR/rPJR notions are claimed.

## Proof
**Two-voter reduction.** Every selected candidate has a voter who approves it, so any nonempty size-\(k\) committee represents the whole electorate \(\{1,2\}\); the coalition containing both voters cannot violate rJR. A singleton coalition \(\{i\}\) can reciprocally afford one candidate exactly when \(\max_{c\in A_i}h_c\ge2/k\), and then rJR requires \(W\cap A_i\ne\varnothing\). Consequently rJR is equivalent to representing each individually eligible voter.

**Upper bound and construction.** Let \(W^*\) select the \(k\) candidates of highest quality (break ties arbitrarily), of total quality \(Q^*\). If \(W^*\) is rJR, the price is one. Otherwise, exactly one voter \(i\) is eligible but unrepresented: at least one voter approves every selected candidate, and all selected candidates therefore have an approver different from \(i\). Choose an approved candidate \(c\in A_i\) with \(h_c\ge2/k\). It is outside \(W^*\). Let \(t\) be the smallest selected quality, so \(2/k\le h_c\le t\le1\), and select a quality-\(t\) candidate \(d\in W^*\). The committee \(W=(W^*\setminus\{d\})\cup\{c\}\) represents \(i\). Since \(k\ge2\), it still contains another selected candidate approved by the other voter, so it represents both voters and is rJR. All original \(k\) qualities are at least \(t\), giving \(Q^*\ge kt\) and, equivalently, \(Q^*-t\ge(k-1)t\). Therefore
\[
\frac{Q^*}{Q(W)}
=1+\frac{t-h_c}{Q^*-t+h_c}
\le 1+\frac{t-h_c}{(k-1)t+h_c}
=\frac{kt}{(k-1)t+h_c}
\le\frac{k}{k-1+2/k}
=R_k.
\]
This also yields a constructive procedure: sort candidates by quality and, if needed, perform one replacement. Its running time is \(O(m\log m)\), or linear with selection, for fixed-length explicit voter approvals.

**Sharpness.** Take \(k\) candidates approved only by voter 1, each with quality \(1\), and one candidate approved only by voter 2, with quality \(2/k\). The unconstrained optimum consists of the first \(k\), of quality \(k\). Both voters are individually eligible and no candidate has both supporters. Hence any rJR committee must select the lone voter-2 candidate, forcing its maximum quality to be \(k-1+2/k\); the resulting price is exactly \(k/(k-1+2/k)=R_k\).

**Peak.** The identity
\[
\frac87-\frac{k^2}{k^2-k+2}
=\frac{(k-4)^2}{7(k^2-k+2)}\ge0
\]
shows that \(R_k\le8/7\) with equality if and only if \(k=4\).

## Verification
The analytical inequalities prove the statement for every finite candidate set and every real quality vector satisfying the hypotheses. The standalone standard-library `verify.py` independently checks rJR directly against every nonempty coalition for 73,710 exhaustive profiles with \(k\in\{2,3,4\}\), candidate counts \(k\) or \(k+1\), three exact rational quality levels, and every nonempty approval mask. It additionally checks 3,150 seeded random rational instances for \(2\le k\le10\), and the rational sharpness witnesses for \(2\le k\le50\). The verification program is supplementary; finite checks are not used to infer the universal theorem.

## Relationship to prior work
Boehmer, Dong, Kreisel and Utke (2026) introduce reciprocal JR (Definition 5.2) and obtain a global quality-price upper bound \(4/3\), tight over unrestricted electorates and committee sizes (Appendix G). Their lower-bound construction uses two seats and a growing electorate; their published unrestricted theorem does not yield the exact two-voter sequence \(R_k\) or its four-seat peak. The present theorem addresses only rJR, and exploits the precise two-voter collapse of coalitional demands to eligible singletons. Prior two-seat fixed-electorate results cover the overlap \(k=2\) but do not imply the entire variable-seat classification. Existing classical JR price-of-representation literature studies different objectives or axioms.

## Limitations
The exact expression is specific to two voters, all candidates being approved by at least one voter, positive qualities no greater than one, and reciprocal JR rather than stronger proportionality axioms. It neither asserts the same bound for three voters nor studies welfare-weighted voter satisfaction. A literature search and comparisons do not prove publication priority; inaccessible or unindexed equivalent results remain possible. No independent scientific audit has been conducted.

## References
1. N. Boehmer, C. Dong, L. Kreisel, M. Utke, *Approval-Based Multiwinner Voting with Candidate Qualities*, arXiv:2609.08830v1, first submitted 2026-09-08. Definition 5.2, Section 5.2, Appendix G. https://arxiv.org/abs/2609.08830
2. *The Price of Justified Representation*, arXiv:2112.05994v2, 2021 preprint with subsequent revision; related but distinct quality objective. https://arxiv.org/abs/2112.05994

# Sharp quality-retention frontier for three-seat, four-candidate reciprocal representation

## Finding

Consider an approval election with exactly four candidates and three committee seats, a finite electorate of \(n\ge 2\) voters, and positive qualities \(h_c\in(0,1]\). Every candidate is approved by at least \(r\) voters, where \(1\le r\le n\). Let \(Q^*\) be the maximum sum of the qualities of any three candidates and \(Q_{\mathrm{rJR}}\) the maximum sum among three-candidate committees satisfying reciprocal justified representation (rJR).

The **exact worst-case retained fraction**, over all such elections and qualities, is

\[
\inf\frac{Q_{\mathrm{rJR}}}{Q^*}=
\begin{cases}
\displaystyle \frac{2}{3}+\frac{n}{9(n-r)},&3r<2n,\\
1,&3r\ge 2n.
\end{cases}
\]

The infimum is attained for every pair of integers \((n,r)\) in the first regime. An rJR committee exists in every instance. The result covers overlapping approvals and nonintegral qualities, and distinguishes the majority-support regime where the quality constraint is free.

## Assumptions and scope

Let \(V\) be an electorate of \(n\ge2\) voters, \(C=\{a,b,c,d\}\) four candidates, and \(A_i\subseteq C\) the approval ballot of voter \(i\). No particular ballot pattern is imposed. Each candidate \(x\) has \(h_x\in(0,1]\), and \(\lvert\{i:x\in A_i\}\rvert\ge r\). A committee is any subset \(W\subset C\) with \(\lvert W\rvert=3\); its quality is \(Q(W)=\sum_{x\in W}h_x\). We use the reciprocal JR definition of Boehmer, Dong, Kreisel and Utke: for each voter group \(S\) that jointly approves a candidate \(x\) and satisfies \(\lvert S\rvert\ge n/(3h_x)\), some voter in \(S\) must approve a member of \(W\).

For a candidate \(x\), put \(e_x=\lvert\{i:A_i=\{x\}\}\rvert\), the count of singleton ballots for \(x\). In the four-candidate, three-seat setting, \(C\setminus\{x\}\) satisfies rJR **if and only if**
\[
3h_x e_x<n.
\]
Indeed, a violating group must be unrepresented, jointly approve an unelected candidate, and therefore consist entirely of singleton-\(x\) voters; conversely, that group witnesses a violation whenever the displayed strict inequality fails. Equality counts as a violation.

## Proof

Relabel candidates so that \(h_a\ge h_b\ge h_c\ge h_d\), and let \(Q^*=h_a+h_b+h_c\). The unrestricted optimum \(W_0=C\setminus\{d\}\) is rJR exactly when \(3h_d e_d<n\). If it is rJR, the desired bound is immediate.

Assume it violates rJR, so \(e_d\ge n/(3h_d)\). Since the at least \(r\) supporters of \(a\) cannot have singleton ballot \(\{d\}\), we have \(e_d\le n-r\). If \(3r<2n\), write
\[
q=\frac{n}{3(n-r)},\qquad \frac13<q<1.
\]
It follows that \(h_d\ge q\). We show that some rJR committee loses at most \((1-q)/3\) of optimum quality.

**Case 1: omitting \(c\) is rJR.** Then \(W_c=C\setminus\{c\}\) has quality \(Q^*-h_c+h_d\). Since \(Q^*\ge3h_c\), \(h_d\ge q\), and \(h_c\le1\),
\[
\frac{Q^*-Q(W_c)}{Q^*}
=\frac{h_c-h_d}{Q^*}
\le\frac{h_c-q}{3h_c}
\le\frac{1-q}{3}.
\]

**Case 2: omitting \(c\) violates rJR.** Then \(e_c\ge n/(3h_c)\) and \(e_c+e_d\le n-r\), because every supporter of \(a\) lies outside those disjoint singleton-ballot groups. Hence
\[
\frac{1}{h_c}+\frac{1}{h_d}\le\frac{1}{q}.
\]
Since qualities are at most one, this case is impossible when \(q>1/2\). Otherwise \(q\in(1/3,1/2]\), and the last inequality with \(h_d\le h_c\le1\) yields
\[
h_c\ge2q,\qquad h_d\ge\frac{q}{1-q}.
\]
Omitting \(b\) must satisfy rJR: otherwise all of \(e_b,e_c,e_d\) are at least \(n/3\), while the \(r\ge1\) supporters of \(a\) are outside those groups, forcing the contradiction \(n\le e_b+e_c+e_d\le n-r\).

Thus \(W_b=C\setminus\{b\}\) is rJR. Using \(h_a\ge h_b\ge h_c\), \(h_b\le1\), and monotonicity of \((z-h_d)/(2z+h_c)\) for \(z\ge h_d\),
\[
\frac{Q^*-Q(W_b)}{Q^*}
=\frac{h_b-h_d}{h_a+h_b+h_c}
\le\frac{1-h_d}{2+h_c}
\le\frac{1-2q}{2(1-q)(1+q)}
\le\frac{1-q}{3}.
\]
For the final inequality, clearing positive denominators gives
\[
2q^3-2q^2+4q-1\ge0.
\]
This polynomial equals \(5/27\) at \(q=1/3\) and has derivative \(6q^2-4q+4>0\) throughout the indicated interval. Cases 1 and 2 yield the claimed retention \(1-(1-q)/3=2/3+n/[9(n-r)]\).

If \(3r>2n\), the original top-quality committee cannot violate rJR: \(e_d\le n-r<n/3\le n/(3h_d)\). If \(3r=2n\), any violation requires \(e_d=n/3\) and \(h_d=1\), so all four qualities equal one. At least one of the four singleton counts is strictly below \(n/3\) (since their sum is at most \(n\)), and omitting that candidate gives a full-quality rJR committee. Thus retention one is guaranteed whenever \(3r\ge2n\).

**Sharpness.** Fix \(3r<2n\), let \(q=n/[3(n-r)]<1\), and give \(a,b,c\) quality one and \(d\) quality \(q\). Choose a set of \(r\) voters who approve all three of \(a,b,c\), and let all remaining \(n-r\) voters approve only \(d\). If \(n-r<r\), also let any \(2r-n\) of the first \(r\) voters approve \(d\). Thus all candidates have at least \(r\) supporters and \(e_d=n-r=n/(3q)\). The unique quality-optimal committee \(\{a,b,c\}\) violates rJR at equality. Every committee containing \(d\) and two of \(a,b,c\) represents all voters, hence satisfies rJR, and has quality \(2+q\), whereas \(Q^*=3\). This realizes \((2+q)/3\) exactly. ∎

## Verification

Run `python verify.py` in the same directory as this file. The script uses only the Python standard library and exact rational arithmetic. It checks every nonempty approval profile on \(n=2,3\) voters with four candidates and qualities from \(\{1/2,3/4,1\}\), supplementing these with deterministic tests for \(n=4,5\) and exact sharpness witnesses for all admissible \((n,r)\) with \(2\le n\le40\). The actual execution reported `VERIFY_OK exact_profile_checks=206077 sharp_witnesses=520`. Exhaustive finite cases do not constitute an infinite proof; the proof above establishes the stated universal quantifiers.

## Relationship to prior work

Boehmer, Dong, Kreisel and Utke introduced reciprocal JR and proved a uniform \(3/4\) quality-retention bound, with a tight asymptotic example for two-seat elections (Theorem 5.5, Proposition 5.6 and Appendix G of [1]). Their results do not give this fixed-four-candidate, three-seat, support-dependent optimal fraction. Elkind and coauthors [2] study standard JR's price in terms of approval welfare and coverage, rather than reciprocal JR's exogenous quality objective. The general-quality theorem and the earlier two-seat support-density results do not imply the exact three-seat statement: the proof must handle a second unsafe omission, yielding the reciprocal-sum inequality above.

## Limitations

This theorem concerns exactly four candidates, three seats, reciprocal **JR** (not reciprocal EJR or PJR), and positive qualities at most one. It does not assert the same ratio for more candidates or other representation notions. Quality is treated as exogenous and approval ballots are unrestricted. The novelty assessment is based on the identified primary literature and accessible research records; equivalent unindexed work remains a possibility. No independent audit is claimed.

## References

[1] N. Boehmer, C. Dong, L. Kreisel and M. Utke, *Approval-Based Multiwinner Voting with Candidate Qualities*, arXiv:2609.08830, first submitted September 8, 2026. https://arxiv.org/abs/2609.08830

[2] E. Elkind, P. Faliszewski, A. Igarashi, P. Manurangsi, U. Schmidt-Kraepelin and W. Suksompong, *The Price of Justified Representation*, arXiv:2112.05994, first submitted December 11, 2021. https://arxiv.org/abs/2112.05994

# Quota-bounded approval support collapses core, core+, and justified representation, with a sharp one-voter breach

## Finding

**Theorem (collapse and sharp breach).** In an unweighted approval-based committee election with \(n\ge 1\) voters, \(m\ge k\ge1\) candidates, and Hare quota \(q=n/k\), suppose every candidate is approved by at most \(q\) voters. For **every** committee \(W\) of exactly \(k\) candidates, the following are equivalent:

1. \(W\) satisfies justified representation (JR).
2. \(W\) lies in the ordinary, integral Hare core.
3. \(W\) satisfies the **core+** fractional-blocking criterion of Becker, Greger, and Peters (Definition 3.1).

For nonintegral \(q\), all three properties hold for every size-\(k\) committee. For integral \(q\), they are equivalent to the explicit condition: each unelected candidate approved by exactly \(q\) voters has **at least one supporter represented** by \(W\). Therefore, a greedy maximal family of pairwise disjoint quota-size supporter sets, extended arbitrarily to \(k\) candidates, constructs a core+ committee. The structural condition can be checked in \(O(nm)\) elementary approval incidences.

The supporter cap is **sharp**: for every integer \(q\ge1\), an election with \(n=2q\), \(k=2\), and only three candidates has a committee in JR and in the integral core but **not** core+; exactly one candidate has supporter count \(q+1\), and the other two have counts \(q\) and \(1\). Thus relaxing the cap by a single supporter can break the equivalence for every integral quota.

## Assumptions and scope

Each voter \(i\in N\) submits an arbitrary approval set \(A_i\subseteq C\). Put \(S_c=\{i:c\in A_i\}\), and for any candidate set \(T\), define additive approval utility \(u_i(T)=|A_i\cap T|\). Define \(q=n/k\), without rounding. Voters with empty ballots and candidates without supporters are permitted. JR means: there is no unelected candidate \(c\) with at least \(q\) supporters all satisfying \(u_i(W)=0\). This is equivalent to the standard cohesive-group formulation of JR.

An integral core block is a nonempty voter coalition \(V\subseteq N\) and a candidate set \(T\subseteq C\) satisfying \(|V|\ge q|T|\) and \(u_i(T)>u_i(W)\) for every \(i\in V\). Define core+ by **infeasibility** of the following fractional system, with variables \(x_{ic}\) for \(i\in S_c\), \(y_i\) for voters, and \(z_c\) for candidates, all in \([0,1]\):

\[
 \sum_{c\in A_i}x_{ic}=(u_i(W)+1)y_i\quad(i\in N),\qquad
 x_{ic}\le z_c\quad(i\in S_c),
\]
\[
 x_{iw}\le y_i\quad(w\in W\cap A_i),\qquad
 \sum_i y_i\ge q\sum_cz_c,\qquad \sum_i y_i>0.
\]

These are the original paper's assignment constraints and fractional relaxation, not the stronger and distinct ordinary Lindahl-priceability property. Core+ entails the integral core since integral blocks give feasible integral variables.

## Proof

**1. Counting integral blocks.** Suppose all \(|S_c|\le q\). If \((V,T)\) blocks \(W\), every \(i\in V\) approves at least \(u_i(W)+1\) candidates from \(T\). Double counting incidences gives

\[
 q|T|\le |V|+\sum_{i\in V}u_i(W)
 \le\sum_{i\in V}|A_i\cap T|
 \le\sum_{c\in T}|S_c|\le q|T|.
\]

Thus equality holds throughout: \(V\) contains at least one voter, all its voters have \(u_i(W)=0\), and every \(c\in T\) has exactly \(q\) supporters, all in \(V\). Any \(c\in T\) therefore witnesses a JR violation. Conversely, a losing candidate with at least \(q\) entirely unrepresented supporters gives a singleton integral core block. This proves JR \(\Longleftrightarrow\) integral core under the cap.

**2. Fractional-block exclusion by explicit payment certificate.** Let \(W\) satisfy JR. Pick \(\varepsilon=1/(k+1)\). For every voter \(i\) and approved selected candidate \(w\in W\cap A_i\), set \(p_{iw}=\varepsilon\), with reserve

\[
 r_i=1-\varepsilon u_i(W).
\]

These are valid nonnegative payments and reserves: \(r_i\ge\varepsilon\), so \(p_{iw}\le r_i\), and the total paid to any selected candidate is at most \(\varepsilon|S_w|\le\varepsilon q<q\). For every losing candidate \(c\), if \(|S_c|<q\) then \(\sum_{i\in S_c}r_i\le |S_c|<q\). Otherwise \(|S_c|=q\), and JR ensures at least one supporter \(i\in S_c\) has \(u_i(W)>0\), so \(r_i<1\) and again \(\sum_{i\in S_c}r_i<q\). By the payment characterization of core+ (Becker–Greger–Peters, Theorem 3.3), \(W\) is core+.

Alternatively, the certificate can be checked directly against the displayed fractional system. If it had a solution, multiplying the voter row equalities by reserves and using \(p_{iw}\le r_i\) and the candidate quota constraints would yield a strict contradiction to \(\sum_i y_i\ge q\sum_cz_c\) for \(\sum_i y_i>0\). The cited theorem supplies the full dual equivalence, including this strictness.

Since core+ implies integral core, equivalence follows. If \(q\notin\mathbb Z\), every candidate count \(|S_c|\), being an integer at most \(q\), is strictly smaller than \(q\); the payment argument works for any \(W\) without invoking JR.

**3. Greedy construction.** If \(q\) is integral, repeatedly add an as-yet-unselected candidate with \(|S_c|=q\) whose supporter set is disjoint from those of all previously added candidates, until none remains. The selected quota-size sets are pairwise disjoint, so their number cannot exceed \(n/q=k\). Extend the candidate collection arbitrarily to size \(k\). Every unselected quota-size supporter set meets one already selected and therefore has a represented supporter. The explicit characterization gives JR, core, and core+. If \(q\) is nonintegral choose any \(k\) candidates. The algorithm is polynomial time and can be implemented by scanning approval incidence data.

**4. Universal one-voter sharpness witness.** For any integer \(q\ge1\), take \(2q\) voters and candidates \(a,b,c\). The first \(q\) voters approve \(a\); among them, one also approves \(c\). One additional voter approves \(\{b,c\}\); the remaining \(q-1\) voters approve only \(c\). Set \(W=\{a,b\}\). Supporter counts are \((q,1,q+1)\). Exactly \(q-1\) voters are unrepresented, while \(c\) is the only losing candidate, so \(W\) satisfies JR. No singleton candidate strictly benefits \(q\) voters: for \(a,b\) nobody strictly improves, and for \(c\) only the \(q-1\) previously unrepresented voters improve. Any two-candidate alternative would require strictly benefiting all \(2q\) voters; no alternative does, since both \(a\) and \(b\) supporters already obtain utility one and at least one has the same utility under every distinct two-candidate alternative. Hence \(W\) is in the integral core.

Nevertheless, core+ fails. In the displayed fractional system, take \(z_c=1\), \(z_a=z_b=0\); set \(x_{ic}=1\) for all \(q+1\) supporters of \(c\), all other \(x\)'s zero; set \(y_i=1\) for the \(q-1\) voters approving only \(c\), \(y_i=1/2\) for each of the two voters approving \(\{a,c\}\) and \(\{b,c\}\), and zero for the \(q-1\) voters approving only \(a\). The voter equalities hold (the two represented \(c\)-supporters each have existing utility one), winning-candidate constraints hold trivially, and

\[
 \sum_i y_i=(q-1)+\tfrac12+\tfrac12=q=q\sum_cz_c>0.
\]

All variables lie in \([0,1]\). This is a feasible fractional blocker, proving the sharp breach for every \(q\).

## Verification

The standalone Python 3 program `verify.py`, relying only on the standard library, exhaustively enumerates the quota-capped profiles in its documented finite test ranges; it checks JR and ordinary core independently for every committee and verifies the greedy construction. It additionally constructs the exceptional example for every integer \(q\) from 1 through 50 and checks all fractional-blocking equalities and inequalities using exact rational arithmetic. Expected output:

```text
PASS capped-profile complete regression: 10893 profiles; 37417 committees
PASS exact fractional obstruction and core stability: quotas 1..50
```

This is a finite regression check; the proof above, not enumeration, establishes the universally quantified result.

## Relationship to prior work

Becker, Greger, and Peters introduced the fractional core+ criterion, proved its payment-system characterization (Definition 3.1 and Theorem 3.3), and proved that general approval elections admit core committees. Those general theorems neither assert equivalence of JR, core, and core+ for **every** quota-capped committee nor identify the exact one-supporter escape from that equivalence. The present result uses their characterization, not a new characterization of arbitrary core+ instances.

Berker and collaborators analyze nonemptiness of stronger core concepts and priceability; ordinary Lindahl priceability is **not** identified with core+ here. Fang gives an existence result under a bound on voter *disapprovals*, orthogonal to this bound on candidate *support*. Casey and Elkind study Hare/Droop representation thresholds rather than this sharp collapse. Existing broad structural theorems might imply the specialized collapse without explicitly recording it; no claim of proven universal historical priority is made.

## Limitations

The collapse requires **every** candidate to have support at most the unrounded Hare quota and applies to unweighted additive approval utilities. It does not claim the condition is necessary for individual elections: above-cap profiles may still admit or force core+ committees. The sharp witness shows failure of universal equivalence, not core+ nonexistence. The payment characterization is imported from the motivating paper; no independent proof of its full duality theorem is claimed. The computer tests cover only the finite displayed ranges and cannot certify arbitrary numbers of voters or candidates. Historical priority requires independent expert review.

## References

1. P. Becker, M. Greger, and D. Peters, *Existence of the Core in Approval-Based Committee Elections*, arXiv:2609.11912, first posted 2026-09-10, especially Definition 3.1 and Theorem 3.3, https://arxiv.org/abs/2609.11912.
2. *On the Edge of Core (Non-)Emptiness*, arXiv:2512.16895, https://arxiv.org/abs/2512.16895.
3. *Sparse Disapproval Guarantees a Nonempty Hare Core*, arXiv:2609.04537, https://arxiv.org/abs/2609.04537.
4. *Justified Representation: From Hare to Droop*, arXiv:2508.00811, https://arxiv.org/abs/2508.00811.

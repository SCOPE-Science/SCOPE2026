# Exact parity-residue law for unavoidable Alabama losses in paired populations

## Finding

Let four constituencies have fixed positive integer populations \((a,a,b,b)\), where \(a<b\) and \(\gcd(a,b)=1\). At each house size \(h\geq1\), apply Hamilton's largest-remainder apportionment, permitting every legitimate tie resolution independently at different house sizes. Call a loss **unavoidable** at the transition \(h\to h+1\) when **every** choice of Hamilton allocations at the two sizes makes at least one constituency lose a seat.

Set \(P=2(a+b)\) and let \(r_h\) be the unique integer in \([0,P)\) congruent to \(ah\pmod P\). An unavoidable loss occurs exactly under the following parity-residue alternatives:

\[
\begin{array}{ll}
 h\text{ even}: & 2(a+b)<2r_h<a+3b,\\
 h\text{ odd}: & a+b<2r_h<2b.
\end{array}
\]

In every such event, one of the two smaller constituencies loses. Equality at a boundary never forces a loss independently of ties.

There is also a closed formula for the number \(N(a,b)\) of unavoidable transitions in one complete house-size period \(P\). For integers \(l\leq u\), define
\[
 E(l,u)=\max\{0,\lfloor u/2\rfloor-\lfloor(l-1)/2\rfloor\},\qquad
 O(l,u)=\max\{0,\lfloor(u+1)/2\rfloor-\lfloor l/2\rfloor\}.
\]
Put
\[
 l_e=a+b+1,\quad u_e=\lfloor(a+3b-1)/2\rfloor,\quad
 l_o=\lfloor(a+b)/2\rfloor+1,\quad u_o=b-1.
\]
Then
\[
 N(a,b)=E(l_e,u_e)+
 \begin{cases}
  O(l_o,u_o),&a\text{ odd},\\
  E(l_o,u_o),&a\text{ even}.
 \end{cases}
\]

The smallest positive-integer paired-population profile admitting any unavoidable loss has total population \(10\), uniquely \((1,1,4,4)\) up to swapping the two pairs. The first possible house-size transition, over all such profiles, is \(3\to4\); this profile attains it. For each fixed positive \(a\), along integers \(b\to\infty\) coprime to \(a\), the proportion of house-size transitions in a period that have an unavoidable loss tends to \(1/4\).

## Assumptions and scope

Hamilton apportionment gives each constituency the integer part of its exact quota \(hp_i/P\) and awards the remaining seats to the largest fractional remainders, with arbitrary tie resolution. House sizes are positive integers, the population vector remains unchanged, and no legal constraint mandates one seat per constituency. The word unavoidable quantifies over both independent tie resolutions. Scaling both population parameters by the same positive integer does not change allocations, hence the primitive assumption only fixes the population scale. The result concerns four constituencies in two equal-sized pairs, not arbitrary four-state apportionment rules or changing populations.

## Proof

Write \(\alpha=a/P\), \(\beta=b/P=1/2-\alpha\); therefore \(0<\alpha<1/4\). Write \(x=\{h\alpha\}=r_h/P\), with braces denoting fractional part. The two small quotas have fractional part \(x\) and the two large quotas have fractional part \(y=\{h\beta\}=\{h/2-h\alpha\}\). Consequently \(y=1-x\) when \(h\) is even and \(0<x<1\). When \(h\) is odd, \(y=1/2-x\) for \(0\leq x<1/2\), while \(y=3/2-x\) for \(1/2<x<1\).

For even \(h\) away from cross-pair ties, the residual-seat count is two: both small constituencies are rounded up if \(x>1/2\), and both large ones if \(x<1/2\). For odd \(h\), the residual-seat count is one when \(0<x<1/2\), awarded to the small pair when \(x>1/4\), otherwise to the large pair. When \(1/2<x<1\), three residual seats remain: the small pair gets one and the large pair two if \(x<3/4\), and the small pair gets two and the large pair one if \(x>3/4\). The boundary cases have the corresponding alternative tied assignments.

Compare an even \(h\) with the following odd size. The only possible fall in a pair total occurs when the small pair had both residual seats, its integer quota part does not increase, and its new residual-seat count drops to one. This requires \(1/2<x<3/4-\alpha\). In all other open regions, either the large pair retains or increases its combined allocation, or an increment in the integer quota parts offsets any lost residual seat. Similarly, for odd \(h\) followed by even \(h+1\), the only possible decrease in a pair total is the small pair losing its sole residual seat without an increase in its integer quota part, which requires \(1/4<x<1/2-\alpha\). The cases \(x>1/2\) at odd sizes cannot decrease either pair total: any fall in rounded-up seats is offset by increasing integer quota parts. Directly at the interval endpoints, Hamilton ties can be resolved so neither pair total falls.

Because the members of each pair have identical quotas, there are legal allocations at both house sizes that nest each member's seat count whenever neither pair total decreases. To see this, within each pair select recipients of residual seats at the second size to retain all previously selected recipients whenever the integer part has not grown; if it has grown, each member gains a base seat and no previous member need lose. Conversely, if a pair total falls, some member loses under every tie resolution. This establishes the equivalence between pair-total loss and the stated unavoidable loss, including boundaries. Multiplying the two strict fractional-part intervals by \(P\) gives the parity-residue inequalities in the finding.

For the count, the residue sequence \(r_h=ah\bmod P\) is periodic in \(h\) with full joint parity-and-residue period \(P\). If \(a\) is odd, coprimality implies \(\gcd(a,P)=1\); hence multiplication by \(a\) permutes the residues modulo even \(P\), preserving parity. Exactly the even residues in \([l_e,u_e]\) and the odd residues in \([l_o,u_o]\) contribute. If \(a\) is even, coprimality forces \(b\) odd; \(\gcd(a,P)=2\), and each even residue appears twice in a full \(P\)-period, once at an even house size and once at an odd house size (the two occurrences differ by the odd integer \(a+b\)). Counting the even residues in both intervals yields the second formula. The functions \(E\) and \(O\) are precisely the counts of even and odd integers in a closed integer interval.

For the minimality statement, no loss can occur at \(h=1\) or \(h=2\): then \(x=\alpha<1/4\) or \(x=2\alpha<1/2\), respectively. For primitive positive \(a<b\) with \(a+b<5\), the only possibilities are \((1,2)\) and \((1,3)\), and the exact count formula yields zero. At \(a+b=5\), the two possibilities are \((1,4)\) and \((2,3)\); only \((1,4)\) has positive count (namely two). At \(h=3\) for \((1,1,4,4)\), the allocations are \((1,0,1,1)\) or \((0,1,1,1)\), whereas at \(h=4\) the only allocation is \((0,0,2,2)\); the loss is unavoidable. Finally each interval in the count formula has length \((b-a)/2+O(1)\), and the parity counts give \(N(a,b)=(b-a)/2+O(1)\), with an absolute error constant. Dividing by \(P=2(a+b)\) proves the asserted limit as \(b\to\infty\) for fixed \(a\).

## Verification

A standalone Python 3 script, `verify.py`, computes all legal Hamilton allocations by exact integer quotients and remainders. It checks the equivalence of the residue condition and the all-tie-resolutions definition for every coprime pair with \(1\leq a<b\leq40\) and every house size in one full period; it independently verifies the closed count formula for every coprime pair with \(1\leq a<b\leq79\), and checks the sharp population and house thresholds. No floating-point comparisons are needed. The proof above establishes the infinite theorem; these finite tests are independent checks, not its logical basis.

## Relationship to prior work

Hamilton's largest-remainder rule and its Alabama paradox are classical. Varshney (2026) proves a global impossibility between quota and population monotonicity for four states when different house sizes may be compared; that statement concerns arbitrary deterministic apportionment rules, not a complete list of forced consecutive-size losses for Hamilton on fixed paired populations. Saari (2026) gives a general geometric explanation of the Alabama paradox and recurrence, but not the paired-population parity-residue criterion or exact period count in the inspected apportionment sections. A publicly accessible related result for three populations of the form \((a,a,c)\) gives a single residue interval and count; the four-population two-pair case has a distinct parity split and is not an instance of its three-population statement. These are claim-level distinctions, not proof of exclusive priority.

## Limitations

The theorem studies simultaneous loss avoidance under every permissible tie resolution, not a particular fixed deterministic tie-breaking convention. It does not classify tie-dependent losses, arbitrary four-state profiles, or changes in the population vector. Prior work may contain equivalent specializations not found through indexed searches; independent scientific validation remains outstanding.

## References

- Lav R. Varshney, *Quota and population monotonicity across house sizes are incompatible for apportionment to four states*, arXiv:2608.02759, first submitted 2026-08-03, https://arxiv.org/abs/2608.02759 .
- Donald G. Saari, *Picture book of apportionment and voting difficulties*, *Public Choice*, published 2026-10-25, https://doi.org/10.1007/s11127-026-01480-9 .
- M. L. Balinski and H. P. Young, *The quota method of apportionment*, *American Mathematical Monthly* 82 (1975), 701–730 (classical background on apportionment and house-size anomalies).

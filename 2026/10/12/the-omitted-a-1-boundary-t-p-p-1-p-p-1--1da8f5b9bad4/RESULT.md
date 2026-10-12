# The omitted \(a=1\) boundary: \(T_p(p+1)=p(p+1)\)
## Finding
For every odd prime \(p\), put \(m=p+1\). With
\[
G(N;m)=\gcd\left\{\binom{N}{k}:0<k<N,\ m\mid k\right\},
\]
let \(r_p(m)\) be the least positive integer \(r\) such that \(m<p^r\), and let \(T_p(m)\) be the least admissible row \(N>m\), \(m\mid N\), for which \(v_p(G(N;m))=r_p(m)\). Then
\[
T_p(p+1)=p(p+1).
\]
At \(p=2\), the same formula gives the previously known identity \(T_2(3)=6\). Thus the new statement is the uniform odd-prime boundary case omitted from the recent \(a\ge2\) formula for \(T_p(p^a+1)\).

## Assumptions and scope
The result concerns primes \(p\) and the restricted multiple-index GCD above. For \(m=p+1\), one has \(p<m<p^2\), hence \(r_p(m)=2\). The recent sharp-maximum theorem therefore says that an extremal row is exactly a row whose restricted GCD has \(p\)-adic valuation \(2\). The proof below independently determines the first such row by examining all smaller admissible multipliers.

## Proof
Write an admissible row as \(N=(p+1)q\) with integer \(q\ge2\). Kummer's theorem identifies \(v_p\binom{N}{k}\) with the number of carries in the base-\(p\) addition \(k+(N-k)\).

First suppose \(2\le q<p\). The selected lower index \(k=p+1\) has base-\(p\) digits \((1,1)\), while
\[
N-k=(p+1)(q-1)=p(q-1)+(q-1)
\]
has digits \((q-1,q-1)\). In each of the two occupied columns the sum is \(q<p\), so no carry occurs. Thus
\[
v_p\binom{(p+1)q}{p+1}=0,
\]
and therefore \(v_p(G((p+1)q;p+1))=0\). No multiplier \(q<p\) is extremal.

Now take \(q=p\), so \(N=p(p+1)\). Every selected lower index is uniquely \(k=(p+1)d\) with \(1\le d\le p-1\). Its base-\(p\) digits are \((d,d)\), and the complementary summand
\[
N-k=(p+1)(p-d)
\]
has digits \((p-d,p-d)\). Their units digits sum to \(p\), producing one carry. In the next column the incoming carry gives
\[
d+(p-d)+1=p+1,
\]
producing a second carry, and no further carry follows. Hence every selected coefficient has valuation exactly \(2\):
\[
v_p\binom{p(p+1)}{(p+1)d}=2\qquad(1\le d\le p-1).
\]
Therefore \(v_p(G(p(p+1);p+1))=2=r_p(p+1)\). Since all admissible multipliers \(2\le q<p\) were excluded, \(p(p+1)\) is the least extremal row.

The same carry argument also works for \(p=2\); in that case there is no smaller admissible multiplier, recovering the already known \(T_2(3)=6\).

## Verification
The standalone script `verify.py` checks the carry counts and Legendre-formula binomial valuations for every prime \(p\le101\), checks every smaller multiplier \(2\le q<p\), checks every selected coefficient in the target row, and additionally computes the actual integer restricted GCD for primes \(p\le31\). Its replay output is:

`VERIFY_OK primes=26 pretarget_rows=1109 target_coefficients=1135 direct_gcd_rows=11`

These finite checks corroborate the formulas; the infinite theorem rests on the carry proof above, not on enumeration.

## Relationship to prior work
Fairfax-Ball's September 2026 theorem for primes congruent to \(-1\) modulo the restriction already implies the target-row valuation \(v_p(G(p(p+1);p+1))=2\): here \(m=p+1\), so \(p=m-1\), and the row has one nonzero digit in each parity class. That result does not define or determine a least extremal row.

The October 2026 follow-up defines \(T_p(m)\), proves the sharp maximum \(r_p(m)\), and determines \(T_p(p^a+1)=p^{3a}+1\) only for \(a\ge2\). Its boundary discussion explicitly states that \(a=1\) is not included and records only the prior instance \(T_2(3)=6\). The theorem here supplies the omitted odd-prime boundary and shows that it obeys the different law \(p(p+1)\), rather than an extrapolation of the \(a\ge2\) formula.

## Limitations
This result determines only the boundary family \(m=p+1\); it does not classify \(T_p(m)\) for general moduli with \(r_p(m)=2\). The originality search compared exact least-row wording, Kummer/carry aliases, the predecessor valuation theorem, the follow-up extremal theorem, the prior restricted-GCD finding, and semantic database hits. No equivalent odd-prime least-row statement was found, but unindexed or differently phrased prior work remains a bibliographic risk.

## References
1. John Fairfax-Ball, *Restricted Binomial GCDs at Primes Congruent to -1*, arXiv:2609.37754v1, 2026.
2. John Fairfax-Ball, *Sharp \(p\)-adic Extrema and Least Extremal Rows for Restricted Binomial GCDs*, arXiv:2610.01328v1, 2026.
3. E. E. Kummer, *Über die Ergänzungssätze zu den allgemeinen Reciprocitätsgesetzen*, J. Reine Angew. Math. 44 (1852), 93--146.

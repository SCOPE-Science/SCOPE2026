# Uniqueness of the four-prime port filling with least prime 157

## Finding

Let
\[
H=(R,c)=(113322,797)
\]
be the key port in Wang's construction. A squarefree product \(B\) fills \(H\) when
\[
cB-R\,\partial(B)=1,
\]
where for squarefree \(B\),
\[
\partial(B)=\sum_{\ell\mid B}\frac{B}{\ell}.
\]

Among four-prime fillings with least prime factor \(157\), there is exactly one:
\[
B=157\cdot1979\cdot10093\cdot16879.
\]
Thus, if \(157<q<r<s\) are primes and
\[
797(157qrs)-113322\!\left(qrs+157rs+157qs+157qr\right)=1,
\]
then necessarily
\[
(q,r,s)=(1979,10093,16879).
\]

## Assumptions and scope

The theorem concerns only squarefree four-prime fillings of the fixed port \(H=(113322,797)\) whose least prime is exactly \(157\). It does not assert that the displayed filling is the only four-prime filling of \(H\) with a different least prime, and it does not classify six-prime fillings.

The source paper proves that the displayed product is a port-primitive filling and explicitly cautions that its displayed smaller fillings are not known to exhaust all smaller \(H\)-fillings. The present theorem closes one natural least-prime branch of that unresolved smaller-filling classification.

## Proof

Assume
\[
B=157qrs
\]
with primes \(157<q<r<s\) and \(B\) filling \(H\). Put
\[
R_1=113322\cdot157=17791554,
\qquad
c_1=797\cdot157-113322=11807.
\]
After fixing the first prime, the remaining three primes satisfy the inherited port equation
\[
c_1qrs-R_1(qr+qs+rs)=1.
\]

Fix \(q\), and set
\[
R_2=R_1q,
\qquad
c_2=c_1q-R_1.
\]
Then the last two primes satisfy
\[
c_2rs-R_2(r+s)=1.
\]
Because the right side is positive, \(c_2>0\), so
\[
q>\frac{R_1}{c_1}.
\]
Hence \(q\ge1507\), and because \(q\) is prime the first possible value is \(1511\).

Dividing the last equation by \(rs\) gives
\[
c_2=R_2\left(\frac1r+\frac1s\right)+\frac1{rs}.
\]
Since \(s>r>q\),
\[
c_2q<2R_2+1.
\]
The left and the first term on the right are integers, so
\[
c_2q\le2R_2.
\]
Using \(R_2=R_1q\) and \(c_2=c_1q-R_1\) yields
\[
q\le\left\lfloor\frac{3R_1}{c_1}\right\rfloor=4520.
\]
Therefore only the \(375\) primes
\[
1507<q\le4520
\]
need be considered.

For each such \(q\), rearranging the last-two-prime equation gives
\[
s(c_2r-R_2)=R_2r+1.
\]
Thus \(c_2r-R_2>0\), so
\[
r>\frac{R_2}{c_2}.
\]
Also, since \(s>r\),
\[
c_2r<2R_2+1,
\]
and integrality again gives
\[
r\le\left\lfloor\frac{2R_2}{c_2}\right\rfloor.
\]
Consequently every possible \(r\) lies in the finite interval
\[
\max\!\left(q+1,\left\lfloor\frac{R_2}{c_2}\right\rfloor+1\right)
\le r\le
\left\lfloor\frac{2R_2}{c_2}\right\rfloor.
\]

The standalone verifier sieves these intervals exactly. Across all \(375\) admissible primes \(q\), there are \(242779\) prime values of \(r\) in the required intervals. For each one it evaluates the uniquely forced rational value
\[
s=\frac{R_2r+1}{c_2r-R_2}.
\]
Exactly one pair \((q,r)\) makes this value integral:
\[
(q,r,s)=(1979,10093,16879).
\]
The verifier then checks primality by its sieve and directly verifies
\[
797B-113322\,\partial(B)=1.
\]
This proves both existence and uniqueness in the least-prime-\(157\) branch.

## Verification

`artifacts/verify.py` is a standard-library-only exact verifier. It constructs a sieve, derives the rigorous \(q\)- and \(r\)-ranges from the inequalities above, enumerates all admissible prime pairs, checks exact divisibility for the forced final prime, and verifies the defining filling identity.

Its packaged replay is:

`VERIFY_OK q_primes=375 r_primes=242779 integral_candidates=1 solution=157*1979*10093*16879 filling_identity=yes`

No floating-point arithmetic, heuristic primality test, factorization oracle, timeout inference, or unproved search cutoff is used.

## Relationship to prior work

Wang proves that
\[
157\cdot1979\cdot10093\cdot16879
\]
fills \(H\) and is port-primitive. The same paper later emphasizes that the displayed smaller \(H\)-fillings are not known to exhaust all smaller fillings; this incompleteness matters because additional smaller fillings could create extra inherited channels in the six-prime problem.

The present result is not another verification that the known product fills \(H\). It classifies the entire four-prime branch with least prime \(157\), showing that no second four-prime filling can begin with that prime. Searches by the exact four primes, the port parameters, least-prime language, and equivalent inherited-port equations found no prior statement of this branch uniqueness.

## Limitations

This theorem leaves open four-prime fillings whose least prime is not \(157\). It therefore does not establish a complete classification of four-prime \(H\)-fillings and does not remove all unknown inherited channels from the source paper's six-prime problem.

## References

1. Han Wang, *Port Fillings for Primary Pseudoperfect Numbers*, arXiv:2605.21518v1, submitted 2026-05-18.
2. Han Wang, public Erdős Problems forum post on Problem 313, 2026-05-16, announcing the write-up and its new primary pseudoperfect construction.

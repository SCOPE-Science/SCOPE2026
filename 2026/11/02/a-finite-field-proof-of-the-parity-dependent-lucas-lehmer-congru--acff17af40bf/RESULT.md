# A finite-field proof of the parity-dependent Lucas–Lehmer congruence for primes \(2^{n-1}+3\)

## Finding
Let \(s_0=4\) and \(s_{j+1}=s_j^2-2\). For every integer \(n\ge3\) such that \(P=2^{n-1}+3\) is prime,
\[
\frac{s_{n-2}}2\equiv\begin{cases}7\pmod P,&n\text{ odd},\\-2\pmod P,&n\text{ even}.\end{cases}
\]
Equivalently, \(s_{n-2}/2+2^n-1\) is congruent to \(0\) for odd \(n\) and \(-9\) for even \(n\), modulo \(P\). This proves the necessary prime-case congruences posed in the July 2026 conjecture. It does **not** assert a converse or that this is a primality test.

## Assumptions and scope
All congruences involve ordinary integers; \(s_j\) is even for all \(j\), so the indicated halves are integers. The premise is that \(n\ge3\) is an integer and \(P=2^{n-1}+3\) is prime. No assertion is made for composite \(P\).

## Proof
Put \(\alpha=2+\sqrt3\) and \(\beta=2-\sqrt3=\alpha^{-1}\). Since \(\alpha+\beta=4\) and \(\alpha\beta=1\), induction from \((\alpha^m+\beta^m)^2-2=\alpha^{2m}+\beta^{2m}\) gives
\[s_j=\alpha^{2^j}+\beta^{2^j}.\]
Let \(E=2^{n-2}=(P-3)/2\). Work in the finite field \(\mathbb F_{P^2}\), choose \(u^2=3\), \(v^2=2\), and set \(y=(1+u)/v\). Then \(y^2=2+u=\alpha\), \(y^{-1}=(u-1)/v\), and \(\beta=\alpha^{-1}\). The two elements \(\alpha,\beta\) are interchangeable under the choice of \(u\), so the trace is well defined modulo \(P\).

For odd \(n\ge5\), \(P\equiv3\pmod8\) and \(P\equiv7\pmod{12}\). Quadratic reciprocity yields \((2/P)=-1\) and \((3/P)=-1\), so \(v^P=-v\) and \(u^P=-u\). Hence
\[y^P=\frac{1-u}{-v}=y^{-1},\qquad \alpha^{(P+1)/2}=y^{P+1}=1.\]
Because \(E=(P+1)/2-2\), we obtain \(\alpha^E=\alpha^{-2}\) and \(\beta^E=\beta^{-2}\). Thus
\[s_{n-2}=\alpha^2+\beta^2=(\alpha+\beta)^2-2=14\pmod P.\]
For even \(n\ge4\), \(P\equiv3\pmod8\) and \(P\equiv11\pmod{12}\). Therefore \((2/P)=-1\) but \((3/P)=1\), so \(v^P=-v\), \(u^P=u\), and
\[y^P=-y,\qquad \alpha^{(P-1)/2}=y^{P-1}=-1.\]
Now \(E=(P-1)/2-1\) implies \(\alpha^E=-\alpha^{-1}=-\beta\) and \(\beta^E=-\alpha\). Therefore \(s_{n-2}\equiv-4\pmod P\). The remaining case \(n=3\) has \(P=7\) and \(s_1=14\), so \(s_1/2=7\), as required.

Finally \(2^n=2(P-3)\), hence \(s_{n-2}/2+2^n-1\equiv s_{n-2}/2-7\pmod P\). The two cases give the stated residues \(0\) and \(-9\). \(\square\)

## Verification
Run `python3 verify.py` with Python 3 and SymPy installed. The program checks the prime-case statement for every \(3\le n\le400\) producing a prime \(P\), checks a separate general trace identity for primes below 20,000, and reports `VERIFY_OK`. Computational checks supplement, rather than replace, the proof.

## Relationship to prior work
The public July 23, 2026 Conjecture 112 attributed to Davide Rotondo proposes precisely the odd/even congruences as experimental implications of primality for \(P=2^{n-1}+3\). Classical Lucas sequences give the trace representation; the Lucas–Lehmer–Riesel test uses a related trace method but tests a different family of numbers, \(k2^m-1\). The present observation is the explicit reduction of the conjecture's unusual index to \((P-3)/2\), followed by the two quadratic-character cases. No claim of novelty is made for the elementary finite-field technique itself.

## Limitations
Only a necessary congruence for prime \(P\) is proved. The converse, pseudoprime existence or nonexistence, effectiveness as a primality test, and behavior for composites are not established. Priority remains subject to the possibility of an earlier implicit formulation among classical Lucas-sequence congruences.

## References
1. Davide Rotondo, “Conjecture 112. A possible Lucas-Lehmer type test for primes of the form 2^k+3”, Prime Puzzles, dated July 23, 2026, https://www.primepuzzles.net/conjectures/conj_112.htm .
2. “Lucas–Lehmer–Riesel test”, overview of the classical trace-sequence construction and different modulus family, https://en.wikipedia.org/wiki/Lucas%E2%80%93Lehmer%E2%80%93Riesel_test .
3. “Lucas sequence”, definitions of the companion trace \(V_m(P,Q)\), https://en.wikipedia.org/wiki/Lucas_sequence .

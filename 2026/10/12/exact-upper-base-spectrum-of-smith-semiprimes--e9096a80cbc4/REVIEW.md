# Review

## Correctness
PASS. In the stated domain \(q<B\le pq\), both prime factors are one-digit. For odd \(p,q\), writing \(pq=(a,c)_B\) makes the Smith equation exactly
\[
a+c=p+q.
\]
With \(m=B-1\), this is equivalent to
\[
pq-p-q=am.
\]
The remaining digit condition \(c\le m\) is exactly
\[
m^2-(p+q)m+(pq-p-q)\ge0.
\]
Because \(q\) lies strictly between the two positive roots, divisor complementation converts this to the claimed cutoff \(a\le\rho_-\). All boundary cases, including \(p=2\), \(pq=9\), \(p=3\), and \(p=5\), are handled explicitly. Exhaustive direct digit-sum replay agrees with the theorem.

## Originality
PASS, with a material historical-access risk. The named all-base invariant is the Dunckley set, so the 2001 Vella--Vella article is the most relevant comparison. Its full text could not be obtained through the inspected accessible routes, and no noncoverage conclusion is drawn from that absence. The associated A060209 record gives the all-base counting invariant and initial values but no semiprime upper-spectrum formula.

The complete accessible 2013 and 2014 Witno papers were inspected. They concern decimal Smith constructions from repunits and do not vary the base. A098837 tabulates decimal Smith semiprimes only. Statement-level searches for a fixed semiprime's Smith bases, the formula \(B=(p-1)(q-1)\), the divisor \(pq-p-q\), and one-digit-factor/two-digit-product formulations did not locate an equivalent theorem.

A previously known fixed-base residue condition supplies only the necessity
\[
B-1\mid pq-p-q.
\]
It does not by itself imply the exact varying-base spectrum: the digit-bound inequality is essential, and the theorem derives its sharp divisor cutoff and the universal canonical base.

## Value
PASS. The number of bases in which a fixed composite is Smith is an established named invariant rather than an arbitrary parameter slice. The theorem resolves a natural semiprime layer of that invariant exactly on the maximal range where both factors remain one-digit. It gives a finite symbolic spectrum, proves a universal existence law for every odd semiprime except \(9\), explains the even-base rigidity, and yields complete \(p=3\) and \(p=5\) layers.

Self-review: passed. Independent audit: not yet performed.

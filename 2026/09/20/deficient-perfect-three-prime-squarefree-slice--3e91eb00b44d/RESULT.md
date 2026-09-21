# Exact parametrization of deficient-perfect numbers with squarefree odd part and three prime factors

## Statement

Let \(a\ge 1\), and let \(p<q\) be odd primes. Put
\[
n=2^a p q,\qquad M=2^{a+1}-1.
\]
Recall that \(n\) is **deficient-perfect** if
\[
\sigma(n)=2n-d
\]
for some proper divisor \(d\mid n\); equivalently, its deficiency
\[
D(n):=2n-\sigma(n)
\]
is a positive divisor of \(n\).

Then \(n=2^a p q\) is deficient-perfect if and only if one of the following two mutually exclusive constructions holds for some integer \(e\) with \(0\le e\le a\).

### Family I: power-of-two deficiency

Let
\[
A_e=M(M+1)+2^e.
\]
There is a positive divisor \(s\mid A_e\) with \(s^2<A_e\) such that
\[
p=M+s,\qquad q=M+\frac{A_e}{s}
\]
are prime. In this case
\[
D(n)=2^e.
\]

### Family II: deficiency containing the smaller odd prime

Let
\[
B_e=2^{a+1}+2^e.
\]
There is a positive divisor \(s\mid B_e\) such that
\[
k:=\frac{B_e}{s}\ge2,
\qquad p=M+s,
\qquad q=kp-1
\]
are prime. In this case
\[
D(n)=2^e p.
\]

In particular, for every deficient-perfect number of the form \(2^a p q\), the deficient divisor is never divisible by the larger odd prime \(q\). The theorem gives a finite exact enumeration for each fixed \(a\), reducing the problem to divisors of the explicit integers \(A_e\) and \(B_e\), \(0\le e\le a\).

## Proof

Because \(p\) and \(q\) occur to the first power,
\[
\sigma(n)=(2^{a+1}-1)(p+1)(q+1)=M(p+1)(q+1).
\]
Hence
\[
\begin{aligned}
D(n)
&=2^{a+1}pq-M(p+1)(q+1)\\
&=pq-M(p+q+1)\\
&=(p-M)q-M(p+1). \tag{1}
\end{aligned}
\]
If \(D(n)>0\), equation (1) immediately forces \(p>M\).

Now suppose that \(n\) is deficient-perfect, so \(D(n)\) is a positive divisor of \(2^a p q\). Reducing (1) modulo \(q\) gives
\[
D(n)\equiv -M(p+1)\pmod q.
\]
But \(M<p<q\) and \(p+1<q\), so the prime \(q\) divides neither \(M\) nor \(p+1\). Therefore \(q\nmid D(n)\). Since \(p\) occurs only to the first power in \(n\), there are only two possibilities:
\[
D(n)=2^e\quad\text{or}\quad D(n)=2^e p,
\qquad 0\le e\le a. \tag{2}
\]

### Case I: \(D(n)=2^e\)

Set \(s=p-M>0\). From (1),
\[
sq=M(p+1)+2^e.
\]
Using \(p=M+s\), this becomes
\[
sq=M(M+s+1)+2^e
=Ms+M(M+1)+2^e.
\]
Thus
\[
s(q-M)=A_e:=M(M+1)+2^e.
\]
Consequently \(s\mid A_e\) and
\[
p=M+s,\qquad q=M+\frac{A_e}{s}.
\]
The ordering \(p<q\) is exactly \(s^2<A_e\).

Conversely, if these formulas hold with prime \(p<q\), then substituting them into (1) gives
\[
D(n)=A_e-M(M+1)=2^e.
\]
Since \(e\le a\), this is a divisor of \(n\), so \(n\) is deficient-perfect.

### Case II: \(D(n)=2^e p\)

Reducing (1) modulo \(p\) gives
\[
0\equiv D(n)\equiv -M(q+1)\pmod p.
\]
Since \(p>M\), we have \(p\nmid M\), and therefore \(p\mid q+1\). Write
\[
q+1=kp,
\]
where \(k\ge2\) because \(q>p\). With \(s=p-M\), substituting \(q=kp-1\) into (1) and dividing by \(p\) yields
\[
2^e=k(p-M)-(M+1)=ks-2^{a+1}.
\]
Hence
\[
ks=B_e:=2^{a+1}+2^e.
\]
Thus \(s\mid B_e\), \(k=B_e/s\), and
\[
p=M+s,\qquad q=kp-1.
\]

Conversely, suppose these formulas produce primes \(p<q\). Since \(ks=2^{a+1}+2^e=M+1+2^e\), equation (1) gives
\[
\begin{aligned}
D(n)
&=s(kp-1)-M(p+1)\\
&=p(ks-M)-(s+M)\\
&=p(2^e+1)-p\\
&=2^e p.
\end{aligned}
\]
Again \(e\le a\), so \(D(n)\mid n\). This proves the converse and completes the classification. \(\square\)

## Effective bounds

The parametrization immediately gives explicit finite bounds. In Family I,
\[
p<M+\sqrt{M(M+1)+2^a}
\]
and
\[
q\le M+M(M+1)+2^a.
\]
In Family II,
\[
s\le \frac{B_e}{2}\le 3\cdot2^{a-1},
\]
while \(B_e\le3\cdot2^a\). Hence
\[
p\le M+3\cdot2^{a-1},
\qquad
q<15\cdot4^a.
\]
Thus a fixed exponent \(a\) admits a finite, explicitly bounded search with no search over arbitrary odd primes.

## Initial exact cases

Applying the theorem gives:

- \(a=1\): no solutions.
- \(a=2\): \(884=2^2\cdot13\cdot17\), with deficiency \(4\).
- \(a=3\):
  \[
  17176=2^3\cdot19\cdot113,\quad
  18632=2^3\cdot17\cdot137,\quad
  18904=2^3\cdot17\cdot139,
  \]
  with deficiencies \(152,4,8\), respectively.
- \(a=4\): exactly five solutions:
  \[
  63248,\ 85936,\ 106928,\ 116624,\ 117808.
  \]

These values agree with the existing deficient-perfect sequence data.

## Verification

The accompanying `artifacts/verify.py` uses exact integer arithmetic. It independently checks the parametrization against a direct definition-based search for every \(1\le a\le7\), using the proved finite bounds, and reports zero mismatches. It also enumerates the parametrized solutions through \(a=12\); the counts are
\[
0,1,3,5,9,8,24,9,11,23,36,21.
\]
The computation is supporting evidence only; the theorem is proved above without a finite cutoff.

## Context and prior literature

Tang, Ren and Li introduced the deficient-perfect terminology in this form and classified deficient-perfect numbers having at most two distinct prime factors. Tang and Feng subsequently proved that no **odd** deficient-perfect number has exactly three distinct prime divisors. The present theorem addresses the first even three-prime slice in which both odd prime factors are squarefree, namely \(2^a p q\), and gives an exact parametrization rather than a bounded table.

Current OEIS entry A271816 records deficient-perfect numbers and the known two-prime classification. It lists \(884=2^2\cdot13\cdot17\) as the smallest term with three distinct prime factors, but does not state the parametrization above.

To the best of our knowledge, searches of the deficient-perfect literature, current sequence records, and exact/synonymous formulations did not locate a prior theorem giving this two-family classification for \(2^a p q\), the exclusion \(q\nmid D(n)\), or the resulting fixed-\(a\) finite divisor search.

## Limitations

The odd part is assumed squarefree: this theorem does not classify \(2^a p^b q^c\) when \(b>1\) or \(c>1\), nor does it classify deficient-perfect numbers with four or more distinct prime factors. The originality statement is literature-bounded rather than exhaustive. The 2013 paper's relevant scope was confirmed from its abstract and from the 2014 paper's literature summary, but its full article text was not directly inspected here. No formal proof-assistant verification is claimed.

## References

1. M. Tang, X.-Z. Ren, M. Li, *On near-perfect and deficient-perfect numbers*, Colloquium Mathematicum **133** (2013), 221–226. https://doi.org/10.4064/cm133-2-8
2. M. Tang, M. Feng, *On deficient-perfect numbers*, Bulletin of the Australian Mathematical Society **90** (2014), 186–194. https://doi.org/10.1017/S0004972714000082
3. OEIS A271816, *Deficient-perfect numbers*. https://oeis.org/A271816

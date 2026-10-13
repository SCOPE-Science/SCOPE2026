# Sharp fixed-\(\Omega\) envelope for the divisor/unitary-divisor ratio
## Finding
Let \(d(n)\) denote the number of positive divisors, let \(d^*(n)\) denote the number of unitary divisors, and write
\[
D(n)=\frac{d(n)}{d^*(n)}=\frac{d(n)}{2^{\omega(n)}}.
\]
For every integer \(m\ge1\), define
\[
M_m=\max_{\Omega(n)=m}D(n).
\]
Then the maximum is exact and has the following complete form:
\[
M_1=1,\qquad M_2=\frac32,\qquad M_5=3,
\]
while
\[
M_{3q}=2^q\quad(q\ge1),
\]
\[
M_{3q+1}=\frac52\,2^{q-1}\quad(q\ge1),
\]
and
\[
M_{3q+2}=\frac{25}4\,2^{q-2}\quad(q\ge2).
\]
The equality cases are also exact. If \(n=\prod_i p_i^{a_i}\), then the multiset of exponents \(\{a_i\}\) is:

- \(\{1\}\) for \(m=1\);
- \(\{2\}\) for \(m=2\);
- \(\{5\}\) or \(\{3,2\}\) for \(m=5\);
- \(q\) copies of \(3\) when \(m=3q\);
- one \(4\) and \(q-1\) copies of \(3\) when \(m=3q+1\);
- two \(4\)'s and \(q-2\) copies of \(3\) when \(m=3q+2\) with \(q\ge2\).

Hence the sharp fixed-\(\Omega\) envelope has an exact period-three shape and satisfies \(M_m\asymp2^{m/3}\).

## Assumptions and scope
The statement ranges over all positive integers \(n\) with prescribed total prime-factor multiplicity \(\Omega(n)=m\). Prime values themselves are irrelevant: only the positive exponent multiset matters. The result concerns \(D(n)=d(n)/d^*(n)\), equivalently the \(k=2\) specialization of Karras's \(D_{k,\omega}(n)=d(n)/k^{\omega(n)}\). It does not assert the analogous exact envelope for arbitrary \(k\ge3\).

## Proof
Write
\[
n=\prod_{i=1}^r p_i^{a_i},\qquad a_i\ge1,\qquad \sum_{i=1}^r a_i=m.
\]
Since \(d(n)=\prod_i(a_i+1)\) and \(d^*(n)=2^r\),
\[
D(n)=\prod_{i=1}^r F(a_i),\qquad F(a)=\frac{a+1}2.
\]
Thus the problem is a finite optimization over partitions of \(m\).

First reduce the possible parts. If a maximizing partition with \(m\ge2\) contains a part \(1\) and another part \(b\), replacing \((1,b)\) by \((b+1)\) preserves the sum and strictly increases the product because
\[
F(b+1)=\frac{b+2}2>\frac{b+1}2=F(1)F(b).
\]
So no maximizing partition for \(m\ge2\) contains \(1\). If a part \(a\ge6\) occurs, replace it by \((3,a-3)\). Then
\[
F(3)F(a-3)=a-2>\frac{a+1}2=F(a),
\]
so no maximizing partition contains a part at least \(6\). Finally,
\[
F(5)=3=F(3)F(2),
\]
so every occurrence of \(5\) may be replaced, without changing the product, by \((3,2)\). Except for the isolated equality possibility at total sum \(5\), it therefore suffices to optimize with parts \(2,3,4\).

For parts \(2,3,4\), three local improvements are decisive:
\[
F(2)^2=\frac94<\frac52=F(4),
\]
\[
F(2)F(4)=\frac{15}4<4=F(3)^2,
\]
and
\[
F(4)^3=\frac{125}8<16=F(3)^4.
\]
Therefore a maximizing canonical partition has at most one \(2\); if it has a \(2\), it has no \(4\); and it has at most two \(4\)'s.

Now reduce the sum modulo \(3\). For \(m\equiv0\pmod3\), the only canonical possibility is all \(3\)'s. For \(m\equiv1\pmod3\), it is exactly one \(4\) with the rest \(3\)'s. For \(m\equiv2\pmod3\), the two canonical possibilities are one \(2\) with the rest \(3\)'s, or two \(4\)'s with the rest \(3\)'s. When \(m=3q+2\) and \(q\ge2\), their product ratio is
\[
\frac{(25/4)2^{q-2}}{(3/2)2^q}=\frac{25}{24}>1,
\]
so the two-\(4\) pattern is uniquely maximal. At \(m=2\) only the single \(2\) is available; at \(m=5\), the canonical pattern \((3,2)\) ties the unreduced part \((5)\). This gives both the displayed maxima and every equality case.

## Verification
The accompanying `verify.py` exhausts every integer partition of every \(m\) from \(1\) through \(40\), evaluates the exact rational product \(\prod(a_i+1)/2\), and compares both the maximum and the complete equality-pattern set with the theorem. The stored output is `VERIFY_OUTPUT.txt`. This finite computation is regression evidence only; the proof above is symbolic and has no cutoff.

## Relationship to prior work
Karras defines \(D_{k,\omega}(n)=d(n)/k^{\omega(n)}\), records the prime-power local factor \((a+1)/k\), and studies mean values. The same paper notes that \(k=2\) is exactly \(D(n)=d(n)/d^*(n)\). Its main results are asymptotic mean-value formulas, not extrema at fixed \(\Omega(n)\).

Derbal's 2012 paper studies the maximum order of \(D(n)\) as \(n\) grows; Bouakkaz and Derbal explicitly restate that size-based maximum-order theorem before studying mean values in arithmetic progressions. A fixed-\(\Omega\) extremum is different: the size of \(n\) is unconstrained, and the theorem above determines the exact exponent partition and equality cases in every multiplicity layer. Targeted searches for the fixed-\(\Omega\) formulation, the equivalent \(d(n)/2^{\omega(n)}\) formulation, and equality-pattern variants found no checked source that implies this classification.

## Limitations
The result treats only the ratio \(d(n)/d^*(n)\), or \(k=2\) in the broader family \(D_{k,\omega}\). The analogous fixed-\(\Omega\) optimization for general \(k\) has a different part-size tradeoff and is not claimed here. The literature comparison cannot exclude an independently published equivalent theorem under notation not recovered by the searches. The 2012 Derbal paper was available through an indexed abstract and is quoted explicitly in the inspected 2023 full text; direct retrieval of its full PDF was unavailable during this review.

## References
1. Meselem Karras, *Asymptotic formula for the multiplicative function \(d(n)/k^{\omega(n)}\)*, arXiv:2209.14573v1 (2022); DOI 10.46298/cm.10104.
2. Abdallah Derbal, *Ordre Maximum d'une Fonction Liée aux Diviseurs d'un Nombre Entier*, INTEGERS 12 (2012), A44.
3. Ouarda Bouakkaz and Abdallah Derbal, *The mean value of the function \(d(n)/d^*(n)\) in arithmetic progressions*, Notes on Number Theory and Discrete Mathematics 29 (2023), 445–453; DOI 10.7546/nntdm.2023.29.3.445-453.
4. Abdallah Derbal and Meselem Karras, *Valeurs moyennes d'une fonction liée aux diviseurs d'un nombre entier*, Comptes Rendus Mathématique 354 (2016), 555–558; DOI 10.1016/j.crma.2016.03.007.

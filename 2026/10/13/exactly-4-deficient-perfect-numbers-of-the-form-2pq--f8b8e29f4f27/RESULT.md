# Exactly \(4\)-deficient-perfect numbers of the form \(2pq\)
## Finding
Let \(p<q\) be odd primes and let \(n=2pq\). Then \(n\) is exactly \(4\)-deficient-perfect if and only if
\[
n\in\{238,310,322\}.
\]
Within the stated support, the complete exactly \(4\)-deficient-perfect list is
\[
2\cdot7\cdot17,\qquad 2\cdot5\cdot31,\qquad 2\cdot7\cdot23.
\]
The corresponding four deficient divisors may be chosen as \(\{1,2,7,34\}\), \(\{1,2,10,31\}\), and \(\{1,7,14,46\}\), respectively.

## Assumptions and scope
An integer \(m\) is exactly \(k\)-deficient-perfect when there are \(k\) distinct proper divisors \(d_1,\ldots,d_k\) such that
\[
\sigma(m)=2m-(d_1+\cdots+d_k).
\]
The theorem concerns the squarefree three-prime support \(m=2pq\) with odd primes \(p<q\). It does not classify nonsquarefree integers or squarefree integers with four or more prime factors.

## Proof
For \(n=2pq\), multiplicativity gives
\[
\sigma(n)=3(p+1)(q+1),
\]
so the deficiency is
\[
\Delta=2n-\sigma(n)=pq-3p-3q-3.
\]
If \(n\) is exactly \(4\)-deficient-perfect, then \(\Delta>0\). Hence \(p>3\), so \(p\ge5\), and since \(p<q\), also \(q\ge7\). Because \(\Delta<pq\), the proper divisor \(pq\) cannot occur among the four deficient divisors. Thus the four divisors must form a four-subset \(E\) of
\[
\{1,2,p,q,2p,2q\}.
\]
Write
\[
\sum_{{d\in E}}d=Ap+Bq+c,
\]
where \(A\) is the total coefficient of \(p\), \(B\) the total coefficient of \(q\), and \(c\in\{0,1,2,3\}\) is the contribution of \(1\) and \(2\). The equality \(\Delta=\sum_{{d\in E}}d\) becomes
\[
pq-(3+A)p-(3+B)q=c+3,
\]
and hence
\[
\bigl(p-(3+B)\bigr)\bigl(q-(3+A)\bigr)=(3+A)(3+B)+c+3=:K_E.
\]
Now \(q-(3+A)>0\), since \(q\ge7\) and \(A\le3\). Since \(K_E>0\), also \(p-(3+B)>0\). Therefore every solution arises from a positive divisor \(d\mid K_E\) through
\[
p=3+B+d,\qquad q=3+A+K_E/d.
\]
There are exactly \(\binom64=15\) choices of \(E\). Their constants \(K_E\) are, in lexicographic subset order,
\[
22,24,26,26,24,31,28,28,34,34,29,29,35,35,39.
\]
Factoring these constants and retaining only odd primes \(p<q\) leaves exactly three admissible cases:
\[
E=\{1,2,p,2q\},\quad (p,q)=(7,17),
\]
\[
E=\{1,2,q,2p\},\quad (p,q)=(5,31),
\]
and
\[
E=\{1,p,2p,2q\},\quad (p,q)=(7,23).
\]
These give \(n=238,310,322\). Direct substitution verifies each witness set, completing both necessity and sufficiency.

## Verification
The accompanying `classification_certificate.json` records all fifteen four-subsets, their coefficients \(A,B,c\), the corresponding constant \(K_E\), and every admissible prime pair produced by a divisor of \(K_E\). The accompanying `verify.py` regenerates the certificate from first principles, checks all divisors of every \(K_E\), and then directly recomputes \(\sigma(n)\) and four-divisor witnesses for the three survivors. Its replay output is recorded in `VERIFICATION.md`.

## Relationship to prior work
Chen introduced the exactly \(k\)-deficient-perfect framework and classified the odd exactly \(2\)-deficient-perfect integers having two distinct prime factors. Aursukaree and Pongsriiam later classified the odd exactly \(3\)-deficient-perfect integers with at most two distinct prime factors. Those results do not treat exactly \(4\)-deficient-perfect numbers on squarefree three-prime support. A published-result search also located a squarefree exactly \(3\)-deficient-perfect classification on \(2pq\), but its equation has three deficient divisors and does not imply the four-divisor classification proved here. OEIS A331627 lists \(238,310,322\) among integers that are exactly \(k\)-deficient-perfect for some \(k\), but that table does not supply the theorem that these are precisely the cases of the form \(2pq\) for \(k=4\).

## Limitations
The argument relies crucially on squarefreeness and on the support \(2pq\), which leaves only six possible deficient divisors below \(pq\). It does not determine exactly \(4\)-deficient-perfect integers of shapes such as \(2^a p^b\), \(2^a p^b q^c\), or odd integers. The originality check is literature-based rather than a formal proof that no uncatalogued publication contains an equivalent statement.

## References
1. FengJuan Chen, *On Exactly k-Deficient-Perfect Numbers*, Integers 19 (2019), Article A37, published 2019-07-31. Open-access PDF: https://math.colgate.edu/~integers/t37/t37.pdf.
2. Saralee Aursukaree and Prapanpong Pongsriiam, *On Exactly 3-Deficient-Perfect Numbers*, arXiv:2001.06953, submitted 2020-01-20; The Fibonacci Quarterly 59 (2021), 33--46.
3. OEIS A331627, *Integers that are (exactly) k-deficient-perfect numbers*.

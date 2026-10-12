# Merca's Conjecture 3: exact prime-square divisor congruences modulo \(4\)
## Finding
For an odd prime \(p\) and \(r\in\{3,5,7\}\), define
\[
\mathcal B_{r,p}=\left\{\beta:0\le\beta<p^2,\quad \tau\!\left(8(p^2n+\beta)+r\right)\equiv0\pmod4\text{ for every }n\ge0\right\},
\]
where \(\tau\) is the positive-divisor counting function. Put \(c_\beta=8\beta+r\). Then
\[
\beta\in\mathcal B_{r,p}
\]
if and only if all three conditions below hold:
\[
p\mid c_\beta,\qquad p^2\nmid c_\beta,
\]
and, writing \(t=c_\beta/p\),
\[
t\not\equiv1\pmod8\quad\text{or}\quad \left(\frac{t}{p}\right)=-1.
\]
Here \(\left(\frac{t}{p}\right)\) is the Legendre symbol. In particular,
\[
\left|\mathcal B_{r,p}\right|=
\begin{cases}
(p-1)/2,&p\equiv r\pmod8,\\
p-1,&p\not\equiv r\pmod8.
\end{cases}
\]
This proves Conjecture 3 in Merca's 2022 paper and strengthens its requested cardinality statement by giving an exact membership criterion.

## Assumptions and scope
The variables satisfy: \(p\) is any odd prime, \(r\in\{3,5,7\}\), \(0\le\beta<p^2\), and \(n\) ranges over all nonnegative integers. The only external theorems used are Dirichlet's theorem on primes in reduced arithmetic progressions, the Chinese remainder theorem, and the classical parity criterion that \(\tau(m)\) is odd exactly when \(m\) is a perfect square.

The result concerns the divisor-counting function \(\tau=\sigma_0\) and the prime-square progressions singled out in the source. It does not claim Conjectures 1, 2, or 4 of that paper.

## Proof
Fix \(p,r,\beta\), and write \(c=8\beta+r\).

First suppose \(p\nmid c\). Since \(c\) is odd, \(\gcd(c,8p^2)=1\). Dirichlet's theorem therefore gives a prime \(q>c\) with
\[
q\equiv c\pmod{8p^2}.
\]
For \(n=(q-c)/(8p^2)\ge0\), one has
\[
8(p^2n+\beta)+r=q,
\]
so \(\tau(q)=2\not\equiv0\pmod4\). Hence every member of \(\mathcal B_{r,p}\) must satisfy \(p\mid c\).

Next suppose \(p^2\mid c\). Because \(0\le\beta<p^2\),
\[
r\le c\le 8p^2-8+r.
\]
Also \(p^2\equiv1\pmod8\), so the only positive multiple of \(p^2\) in this interval that is congruent to \(r\pmod8\) is
\[
c=rp^2.
\]
If \(p\ne r\), then at \(n=0\),
\[
\tau(c)=\tau(rp^2)=2\cdot3=6,
\]
which is not divisible by \(4\). If \(p=r\), choose by Dirichlet a prime \(q>p\) with \(q\equiv p\pmod8\), write \(q=8n+p\), and obtain
\[
8(p^2n+\beta)+p=p^2q,
\]
whose divisor count is again \(3\cdot2=6\). Thus \(p^2\mid c\) is impossible for a member of \(\mathcal B_{r,p}\).

It remains to consider
\[
p\mid c,\qquad p^2\nmid c.
\]
Set \(t=c/p\). Then \(p\nmid t\) and
\[
8(p^2n+\beta)+r=p(8pn+t).
\]
Because \(\gcd(p,8pn+t)=1\), multiplicativity gives
\[
\tau\!\left(8(p^2n+\beta)+r\right)=2\tau(8pn+t).
\]
The right side is divisible by \(4\) exactly when \(\tau(8pn+t)\) is even, and \(\tau(m)\) is even exactly when \(m\) is not a square. Therefore
\[
\beta\in\mathcal B_{r,p}
\]
exactly when the progression \(8pn+t\) contains no square.

That progression contains a square if and only if
\[
x^2\equiv t\pmod{8p}
\]
is soluble. The forward implication is immediate. Conversely, if \(x_0\) solves the congruence, replace it by \(x=x_0+8pk\) with \(k\) large enough that \(x^2\ge t\); then
\[
n=\frac{x^2-t}{8p}\ge0
\]
is an integer and \(8pn+t=x^2\). Since \(t\) is odd and \(p\nmid t\), the Chinese remainder theorem shows that the congruence is soluble exactly when
\[
t\equiv1\pmod8
\]
and \(t\) is a quadratic residue modulo \(p\). This proves the stated membership criterion.

For the count, the congruence
\[
8\beta+r\equiv0\pmod p
\]
has exactly \(p\) solutions in \(0\le\beta<p^2\). Exactly one of these also satisfies \(p^2\mid8\beta+r\), so \(p-1\) candidates remain. As \(\beta\) runs through the \(p\) solutions modulo \(p^2\), increasing \(\beta\) by \(p\) increases \(t=(8\beta+r)/p\) by \(8\); hence the corresponding \(t\)-values run through every residue class modulo \(p\), and after removing the unique zero residue, through every nonzero residue exactly once.

Moreover
\[
pt=8\beta+r\equiv r\pmod8,
\]
so, because every odd residue is its own inverse modulo \(8\),
\[
t\equiv rp\pmod8.
\]
Thus \(t\equiv1\pmod8\) exactly when \(p\equiv r\pmod8\). If \(p\not\equiv r\pmod8\), every one of the \(p-1\) candidates has \(t\not\equiv1\pmod8\), so all are admitted. If \(p\equiv r\pmod8\), membership is equivalent to \(t\) being a quadratic nonresidue modulo \(p\); exactly half of the \(p-1\) nonzero residues have this property. The cardinality formula follows.

## Verification
The symbolic proof establishes the universal result. The accompanying `verify.py` independently checks the membership criterion and count for every odd prime \(p\le199\) and each \(r\in\{3,5,7\}\). It exhausts every \(0\le\beta<p^2\), verifies the square-congruence criterion modulo \(8p\), constructs an exact square witness whenever the criterion predicts failure in the \(p\parallel(8\beta+r)\) branch, and directly evaluates divisor counts on a finite sample of progression terms for every predicted member. The computation is a regression check, not a substitute for Dirichlet's theorem or the universal proof.

## Relationship to prior work
Merca introduced \(\mathcal B_{r,p}\), stated exactly the cardinality formula above as Conjecture 3, proved only the small cases \(p=3,5\), and explicitly identified the absence of a general criterion for the square-obstruction step as the obstacle to automating the argument. The present proof supplies that criterion: square occurrence in \(8pn+t\) is exactly solvability of \(x^2\equiv t\pmod{8p}\), which reduces by the Chinese remainder theorem to one modulo-\(8\) condition and one Legendre-symbol condition.

Craig and Merca's earlier general framework for Ramanujan-type congruences of multiplicative functions gives broad valuation bounds and necessary conditions for \(\sigma_0\), but it does not state this exact \(\mathcal B_{r,p}\) classification or the cardinality formula. The later focal paper still states the formula as a conjecture after citing that framework.

Targeted searches for the notation \(\mathcal B_{r,p}\), the exact cardinality formula, its quadratic-nonresidue reformulation, and the title of the focal paper did not locate a later source proving Conjecture 3. This is evidence of noncoverage, not an absolute guarantee that no uncatalogued proof exists.

## Limitations
The originality assessment is literature-based and therefore retains the ordinary risk of an unindexed or differently phrased prior proof. The theorem does not settle the source paper's other conjectures, including the \(r=1\) cardinality problem or the proposed union characterization. The finite verification only tests bounded primes and bounded progression samples; correctness for all primes and all \(n\) rests on the symbolic proof.

## References
1. M. Merca, “Families of Ramanujan-Type Congruences Modulo 4 for the Number of Divisors,” *Axioms* 11 (2022), 342. DOI: 10.3390/axioms11070342.
2. W. Craig and M. Merca, “On Ramanujan-type Congruences for Multiplicative Functions,” *Revista de la Real Academia de Ciencias Exactas, Físicas y Naturales. Serie A. Matemáticas* 116 (2022), 128. arXiv:2112.05649; DOI: 10.1007/s13398-022-01272-y.

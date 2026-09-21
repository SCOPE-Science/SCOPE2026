# Two-prime-support admirable numbers: a complete converse classification

An integer \(n\) is **admirable** if there is a proper divisor \(d<n\), \(d\mid n\), such that
\[
\sigma(n)-2d=2n.
\]
Equivalently, the sum of the proper divisors of \(n\), with one divisor assigned a minus sign, equals \(n\).

## Theorem

Let
\[
n=2^a p^b,\qquad a,b\ge 1,
\]
where \(p\) is an odd prime. Then \(n\) is admirable if and only if exactly one of the following four possibilities holds.

1. **Binary-deviation family.** \(b=1\), and for some \(0\le s\le a-1\),
   \[
   p=2^{a+1}-1-2^{s+1}
   \]
   is prime. The subtracted divisor is \(d=2^s\).

2. **Isolated odd-divisor case.**
   \[
   (a,b,p)=(3,1,5),
   \]
   so \(n=40\), with subtracted divisor \(d=5\).

3. **Even-perfect-divisor family.** \(b=1\), and for some \(h\ge2\),
   \[
   a=2h-1,\qquad p=2^h-1
   \]
   with \(p\) prime. The subtracted divisor is
   \[
   d=2^{h-1}p,
   \]
   the associated even perfect number.

4. **Mersenne-cube family.** \(b=3\) and
   \[
   p=2^{a+1}-1
   \]
   is prime. The subtracted divisor is
   \[
   d=2^a p,
   \]
   again the associated even perfect number.

In particular, an admirable integer with prime support exactly \(\{2,p\}\) can have odd-prime exponent only
\[
\boxed{b=1\ \text{or}\ b=3,}
\]
and the exponent \(b=3\) occurs precisely in the Mersenne-prime family above.

The first terms represented by the four mechanisms include
\[
12,20,56,88,104,\ldots;\qquad
40;\qquad
24,224,15872,\ldots;\qquad
54,1372,476656,\ldots.
\]

## Proof

Put
\[
A=a+1,\qquad M=2^A-1,\qquad
G_b=1+p+\cdots+p^{b-1}.
\]
Since
\[
\sigma(2^a p^b)=M(G_b+p^b)
\]
and \(2^{a+1}=M+1\), the excess over perfection is
\[
E:=\sigma(n)-2n=M G_b-p^b. \tag{1}
\]
Admirability is exactly the assertion that
\[
E=2d
\]
for a proper divisor \(d=2^s p^t\) of \(n\).

### 1. Parity

Both \(M\) and \(p\) are odd, while \(G_b\equiv b\pmod2\). Hence
\[
E\equiv b-1\pmod2.
\]
Therefore \(E=2d\) is possible only when \(b\) is odd.

### 2. Complete analysis when \(b=1\)

Now \(G_1=1\), so
\[
E=M-p=2d.
\]
Moreover \(0<d<2^a\). A divisor of \(2^a p\) below \(2^a\) is either \(2^s\) or \(2^s p\).

If \(d=2^s\), then
\[
p=M-2^{s+1}=2^{a+1}-1-2^{s+1}.
\]
Positivity forces \(0\le s\le a-1\), and this is exactly family 1. Direct substitution proves the converse.

Suppose instead that \(d=2^s p\). Write \(h=s+1\). Then
\[
M=(2^h+1)p, \tag{2}
\]
so \(2^h+1\mid 2^A-1\).

The multiplicative order of \(2\) modulo \(2^h+1\) is exactly \(2h\): it divides \(2h\), and if it were a proper divisor of \(2h\) it would be at most \(h\), impossible because then the positive integer \(2^h+1\) would divide the smaller positive integer \(2^r-1\). Consequently
\[
2h\mid A.
\]
Write \(A=2hj\).

If \(h\ge2\) and \(j\ge2\), then the quotient
\[
p=\frac{2^{2hj}-1}{2^h+1}
\]
is divisible by \(2^h-1>1\) and is strictly larger than that divisor, contradicting primality. Thus \(j=1\), and
\[
A=2h,\qquad p=2^h-1,
\]
which is family 3.

It remains to take \(h=1\). Then \(A=2j\) and
\[
p=\frac{2^{2j}-1}{3}
=\frac{(2^j-1)(2^j+1)}{3}.
\]
For \(j=1\) the quotient is \(1\); for every \(j\ge3\) the displayed factorization is nontrivial after division by \(3\). The only prime case is \(j=2\), giving \(p=5\), \(a=3\), and \(n=40\). This is family 2.

Thus families 1--3 are the complete \(b=1\) classification.

### 3. The case \(b\ge3\)

We already know \(b\) is odd. Since \(E>0\), (1) gives
\[
M G_b>p^b.
\]
As
\[
G_b=\frac{p^b-1}{p-1}<\frac{p^b}{p-1},
\]
we obtain \(M>p-1\), hence \(M\ge p\).

Let
\[
u=v_p(M).
\]

#### Case 3a: \(u=0\)

Equation (1) is nonzero modulo \(p\), so \(t=0\) and
\[
E=2^{s+1}\le 2^{a+1}=M+1. \tag{3}
\]
Here \(M\ne p\), hence \(M-p\ge2\).

For \(j\ge1\), define
\[
E_j=M(1+p+\cdots+p^{j-1})-p^j.
\]
Then
\[
E_{j+1}-E_j=p^j(M-p+1)>0.
\]
Also
\[
E_2-(M+1)=p(M-p)-1>0.
\]
Thus \(E=E_b>E_2>M+1\), contradicting (3).

#### Case 3b: \(1\le u<b\)

Write \(M=p^u c\) with \(p\nmid c\). From (1),
\[
E=p^u\bigl(cG_b-p^{b-u}\bigr),
\]
and the parenthetical factor is nonzero modulo \(p\). Therefore \(t=u\) and
\[
cG_b-p^{b-u}=2^{s+1}\le M+1=p^u c+1. \tag{4}
\]
Subtracting the right endpoint gives
\[
\begin{aligned}
&cG_b-p^{b-u}-(p^u c+1)\\
&\qquad=c(G_b-p^u)-p^{b-u}-1\\
&\qquad\ge G_b-p^u-p^{b-u}-1.
\end{aligned}
\]
Because \(b\) is odd, \(u\) and \(b-u\) are distinct members of
\(\{1,\ldots,b-1\}\). Hence the final expression is the sum of all terms \(p^j\),
\(0\le j\le b-1\), except the three terms with indices \(0,u,b-u\). It is
nonnegative, and it vanishes only when \(b=3\).

Thus (4) forces \(b=3\) and also \(c=1\). Hence \(u=1\) or \(u=2\).

If \(u=1\), then \(M=p\), and (1) gives
\[
E=p(p+1)=2^{a+1}p,
\]
so \(d=2^a p\). This is family 4.

If \(u=2\), then \(M=p^2\), so
\[
2^{a+1}=p^2+1.
\]
For odd \(p\), the right side is \(2\pmod8\) and is greater than \(2\), so it cannot be a power of \(2\). This case is impossible.

#### Case 3c: \(u\ge b\)

Assume for contradiction that \(n\) is admirable and write
\[
M=Cp^b,\qquad C\ge1.
\]
Since \(E\) is divisible by \(p^b\) while a divisor of \(n\) contains at most
\(p^b\), admirability forces
\[
E=2^{h}p^b
\]
for some \(1\le h\le A-1\). Thus
\[
C G_b=2^h+1. \tag{5}
\]
Using also \(Cp^b=2^A-1\), eliminate \(C\) from (5):
\[
2^h\bigl(2^{A-h}G_b-p^b\bigr)
=G_b+p^b
=1+p+\cdots+p^b. \tag{6}
\]
The factor in parentheses is odd, because \(A-h\ge1\). Therefore
\[
h=v_2(1+p+\cdots+p^b).
\]
Since \(b+1\) is even, the \(2\)-adic lifting-the-exponent formula gives
\[
h=v_2(p+1)+v_2(b+1)-1. \tag{7}
\]
Consequently
\[
2^h+1
\le \frac{(p+1)(b+1)}2+1. \tag{8}
\]
But \(C\ge1\) and (5) give \(G_b\le2^h+1\), whereas
\[
G_b\ge 1+p+(b-2)p^2
>1+\frac{(p+1)(b+1)}2
\]
for every \(p\ge3\), \(b\ge3\). For \(b=3\) the strict inequality reduces to
\((p-2)(p+1)>0\), and its left-minus-right difference increases with \(b\).
This contradicts (8).

All cases have now been exhausted, proving the theorem.

## Relation to prior work

Firoozbakht and Hasler (2010) study equations of the form
\[
\sigma(x)=2(x+m).
\]
Their Theorem 1.1 gives the construction
\[
x=2^{k-1}p,\qquad p=2^k-1-2m,
\]
when \(p\) is an odd prime. Their Remark 1.4 identifies the case where \(m\) is a proper divisor of \(x\) as the admirable-number condition. Their Proposition 1.6 gives
\[
x=2^{k-1}(2^k-1)^3
\]
when \(2^k-1\) is prime, and their Theorem 1.14 contains the even-perfect-divisor construction underlying family 3.

Thus the individual sufficient mechanisms appearing in the theorem are closely related to known constructions. The contribution here is the converse: on prime support exactly \(\{2,p\}\), these mechanisms are exhaustive, all even \(b\) are impossible, every odd \(b\ge5\) is impossible, and \(b=3\) is forced to be precisely the Mersenne-cube family.

The current OEIS entry A111592 records the definition, data, and the Firoozbakht construction, but no equivalent two-prime-support converse was located in the searches performed.

## Reproducible check

The accompanying standalone script `artifacts/verify.py` performs exact integer arithmetic.

It checks all
\[
1\le a\le18,\qquad p<20000\text{ odd prime},\qquad 1\le b\le9,
\]
a total of 366,282 parameter triples. The direct definition and the theorem agree with zero mismatches; 45 tuples are admirable in this box. The only hits with \(b\ge3\) are the five Mersenne-cube cases
\[
(1,3,3),\ (2,7,3),\ (4,31,3),\ (6,127,3),\ (12,8191,3).
\]

The script also separately targets the proof's high-\(p\)-adic-valuation branch for
\(a\le300\), \(p<20000\), and \(b\in\{3,5,7,9\}\). It finds 22 tuples with
\(p^b\mid 2^{a+1}-1\) and no admirable examples. These finite computations are
supporting checks only; the theorem is proved without cutoffs.

## Limitations and originality boundary

The classification concerns integers with exactly two distinct prime factors, one of them \(2\). It does not classify admirable integers with two odd prime factors or with larger prime support.

Originality is claimed only to the best of our knowledge. The full Firoozbakht--Hasler paper, current OEIS A111592, exact formula searches, synonymous searches around admirable numbers and one-odd-prime support, and the current SCOPE archive were checked. No equivalent converse theorem was located.

The original paper of J. M. Sachs, *Admirable Numbers and Compatible Pairs*, The Arithmetic Teacher 7 (1960), 293--295, JSTOR 41184328, is the most relevant source whose article text was not directly inspected here. Its bibliographic record and later expository summaries were inspected. Because it is the original pedagogical source for the notion, an unnoticed equivalent observation there remains a residual originality risk, although the later 2010 paper is much closer to the structural formulas used in this theorem.

## References

1. F. Firoozbakht and M. F. Hasler, "Variations on Euclid's Formula for Perfect Numbers", *Journal of Integer Sequences* 13 (2010), Article 10.3.1.  
   https://cs.uwaterloo.ca/journals/JIS/VOL13/Hasler/hasler2.pdf
2. OEIS A111592, "Admirable numbers".  
   https://oeis.org/A111592
3. J. M. Sachs, "Admirable Numbers and Compatible Pairs", *The Arithmetic Teacher* 7 (1960), 293--295, JSTOR 41184328.  
   https://www.jstor.org/stable/41184328

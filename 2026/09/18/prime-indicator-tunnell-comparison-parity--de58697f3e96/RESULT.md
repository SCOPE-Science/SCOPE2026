# Prime-indicator parity in Tunnell-type comparison progressions

## Statement

Im and Shin construct weight-\(3/2\) forms
\[
G_r(q)=\sum_{n\ge 1}a_r(n)q^n
\]
and, for each row \(r\) of their Tables 8 and 9, a residue set \(C_r\pmod {M_r}\), a ternary comparison form \(Q_r\), and integers \(e_r,d_r\) such that for every positive integer \(n\equiv C_r\pmod {M_r}\),
\[
\frac{a_r(n)}{2^{e_r}}\equiv
\frac{r_{Q_r}(n)}{2^{d_r}}\pmod{\lambda},
\qquad \lambda=1+i.
\]
Here \(r_Q(n)\) is the number of integral representations of \(n\) by \(Q\).

The comparison rows use only
\[
Q_3=x^2+y^2+z^2,\qquad Q_{135}=x^2+3y^2+5z^2,
\]
with \(d_r=3\) for \(Q_3\) and \(d_r=2\) for \(Q_{135}\).

**Theorem.** For every row \(r\) of Im--Shin Tables 8 and 9 and every odd square-free integer \(n>1\) satisfying
\[
n\bmod M_r\in C_r,
\]
one has
\[
\boxed{\frac{r_{Q_r}(n)}{2^{d_r}}\equiv \mathbf 1_{\mathbb P}(n)\pmod 2.}
\]
Consequently,
\[
\boxed{\frac{a_r(n)}{2^{e_r}}\equiv \mathbf 1_{\mathbb P}(n)\pmod{1+i}.}
\]
In particular,
\[
v_{1+i}(a_r(n))=
\begin{cases}
2e_r,& n\text{ prime},\\
\ge 2e_r+1,& n\text{ square-free composite},
\end{cases}
\]
where a zero coefficient is assigned infinite valuation.

Thus the mod-\((1+i)\) comparison used by Im and Shin to prove their prime non-\(\theta\)-congruence theorem is intrinsically prime-selective on every one of its comparison progressions: for every square-free composite index in those same progressions, the normalized comparison coefficient vanishes modulo \(1+i\). Any extension to composites using the same rows must therefore use higher \((1+i)\)-adic information, a different comparison form, or direct information about \(a_r(n)\).

The theorem concerns the following row data from the source paper:

| \(M_r\) | \(C_r\) | \(Q_r\) | \(e_r\) | \(d_r\) |
|---:|---|---|---:|---:|
| 40 | \(\{11,19\}\) | \(Q_3\) | 4 | 3 |
| 40 | \(\{21,29\}\) | \(Q_3\) | 3 | 3 |
| 40 | \(\{3,27\}\) | \(Q_3\) | 3 | 3 |
| 40 | \(\{7,23\}\) | \(Q_{135}\) | 2 | 2 |
| 120 | \(\{53,77\}\) | \(Q_3\) | 4 | 3 |
| 120 | \(\{43,67\}\) | \(Q_3\) | 5 | 3 |
| 120 | \(\{11,59\}\) | \(Q_3\) | 5 | 3 |
| 120 | \(\{31,79\}\) | \(Q_{135}\) | 4 | 2 |
| 120 | \(\{23,47\}\) | \(Q_{135}\) | 5 | 2 |
| 120 | \(\{19,91\}\) | \(Q_3\) | 5 | 3 |
| 120 | \(\{83,107\}\) | \(Q_3\) | 4 | 3 |
| 120 | \(\{7,103\}\) | \(Q_{135}\) | 5 | 2 |

## Three-square rows

Let \(n\) be odd and square-free and put \(k=\omega(n)\).

If \(n\equiv3\pmod 8\), Gauss's three-square formula gives
\[
r_3(n)=24h(-n).
\]
The discriminant \(-n\) has \(k\) prime-discriminant factors, so genus theory gives
\[
2^{k-1}\mid h(-n).
\]
Hence
\[
2^{k-1}\mid \frac{r_3(n)}8.
\]

If \(n\equiv5\pmod8\), then
\[
r_3(n)=12h(-4n).
\]
Now \(-4n\) has \(k+1\) prime-discriminant factors, so
\[
2^k\mid h(-4n),
\]
and again
\[
\boxed{2^{k-1}\mid \frac{r_3(n)}8.}
\]
Therefore \(r_3(n)/8\) is even whenever \(n\) is square-free composite in these residue classes. For prime \(n\equiv3,5\pmod8\), Im--Shin Lemma 7.2 proves that \(r_3(n)/8\) is odd. Every \(Q_3\) row in Tables 8 and 9 lies in one of these two classes modulo \(8\), proving the theorem for all three-square rows.

## The \(x^2+3y^2+5z^2\) rows

For every odd \(n\equiv7\pmod8\), reduction modulo \(8\) in
\[
x^2+3y^2+5z^2=n
\]
forces \(y\) odd and \(x,z\) even. Let
\[
A(n)=\#\{(x,y)\in\mathbb Z_{>0}^2:x^2+3y^2=n\},
\]
\[
B(n)=\#\{(y,z)\in\mathbb Z_{>0}^2:3y^2+5z^2=n\}.
\]
Solutions with both \(x\) and \(z\) nonzero occur in sign orbits of size \(8\), while the two boundary types occur in sign orbits of size \(4\). Thus
\[
\boxed{\frac{r_{135}(n)}4\equiv A(n)+B(n)\pmod2.}
\]
This argument does not require \(n\) to be prime.

We use the following elementary representation-count lemma.

**Lemma.** Let \(m>1\) be square-free and \((m,30)=1\), with \(k=\omega(m)\). For each of the three primitive forms
\[
x^2+3y^2,\qquad x^2+15y^2,\qquad 3x^2+5y^2,
\]
the number of positive representations of \(m\) is either \(0\) or \(2^{k-1}\).

**Proof.** The first form has discriminant \(-12\), whose proper class group is trivial. The latter two are the two proper classes of discriminant \(-60\), whose class group has exponent \(2\). If one of these forms represents \(m\), then every prime dividing \(m\) splits in the corresponding quadratic order. For each of the \(k\) primes there are two conjugate invertible prime ideals. Since inversion is trivial on a class group of exponent \(2\), replacing any chosen prime ideal by its conjugate does not change the proper ideal class. Hence all \(2^k\) ideals of norm \(m\) lie in the same relevant class. The only units are \(\pm1\), giving \(2^{k+1}\) proper integral representations. Because \((m,30)=1\), neither coordinate can vanish, so the four sign choices reduce this to \(2^{k-1}\) positive representations. \(\square\)

For each of the three \(Q_{135}\) rows modulo \(120\), every admissible \(n\) is coprime to \(30\). If \(n\) is composite, then \(k\ge2\), so the lemma makes both \(A(n)\) and \(B(n)\) even. Hence \(r_{135}(n)/4\) is even.

It remains to treat the \(Q_{135}\) row
\[
n\equiv7,23\pmod{40}.
\]
Here \(5\nmid n\). If \(3\nmid n\), the same lemma applies directly. If \(3\mid n\), write \(n=3m\). Square-freeness gives \((m,30)=1\), and reduction modulo \(3\) yields exact bijections of positive representations
\[
A(3m)=A(m),
\]
\[
B(3m)=C(m),\qquad
C(m)=\#\{(u,v)\in\mathbb Z_{>0}^2:u^2+15v^2=m\}.
\]
If \(\omega(m)\ge2\), both terms are even by the lemma. If \(m\) is prime, the residue condition on \(3m\) gives
\[
m\equiv1\text{ or }4\pmod5,
\]
so \((m/5)=1\). The discriminants \(-12\) and \(-60\), each with singleton genera in the relevant classes, then give
\[
A(m)=1\iff (m/3)=1,
\]
while under \((m/5)=1\),
\[
C(m)=1\iff (m/3)=1.
\]
Thus \(A(m)+C(m)\) is even. This proves evenness for every square-free composite in the remaining row.

For prime indices in the \(Q_{135}\) rows, Im--Shin Lemma 7.3 gives oddness in the relevant residue classes. In the modulus-\(40\) row, the prime lifts to modulus \(120\) are \(7,47,23,103\), all among their odd classes. The prime-indicator identity follows.

Finally, Im--Shin Proposition 7.1 transfers the comparator parity to \(a_r(n)/2^{e_r}\). Since \(2=-i(1+i)^2\), the stated \((1+i)\)-adic valuations follow.

## Scope and boundary

The residue-set hypothesis is essential for the \(Q_{135}\) statement. For example,
\[
\frac{r_{135}(39)}4=3,
\qquad
\frac{r_{135}(111)}4=7,
\]
although \(39\) and \(111\) are square-free composite and congruent to \(7\pmod8\). Both lie outside the \(Q_{135}\) comparison sets used in Tables 8 and 9. Thus the theorem is a structural statement about the published Tunnell-comparison progressions, not a global parity theorem for \(r_{135}\).

The result does **not** assert that the relevant Fourier coefficients vanish at composite indices, nor does it produce a new family of composite non-\(\theta\)-congruent numbers. It proves that the first mod-\((1+i)\) layer of the published comparison cannot establish their nonvanishing at any square-free composite index in those progressions.

## Reproducibility

`artifacts/verify.py` uses exact integer arithmetic to enumerate \(r_3(n)\) and \(r_{135}(n)\) through \(100000\), tests square-freeness, and checks the prime-indicator parity identity in every row of Tables 8 and 9. It also verifies the two outside-row counterexamples above. The recorded output reports 29,548 row-membership checks with no failure.

## References

1. B.-H. Im and M. Shin, *Tunnell-type criteria for variants of the congruent number problem*, arXiv:2609.19085v1 (2026). https://arxiv.org/abs/2609.19085
2. D. A. Cox, *Primes of the Form \(x^2+ny^2\): Fermat, Class Field Theory, and Complex Multiplication*, 2nd ed., Wiley, 2013. https://doi.org/10.1002/9781118400722

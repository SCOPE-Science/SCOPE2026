# Prime plus two positive cubes below \(333334^3\)

## Result

Let
\[
B=333334^3=37037259259703704.
\]
Every integer
\[
308<n<B
\]
can be written in the form
\[
n=p+x^3+y^3,
\]
where \(p\) is an odd prime and \(x,y\) are positive integers.

This extends the verified range \(308<n<10^{16}\) in Applegate--Pratt, *Computational Results on Sums of a Prime with Squares or Cubes* (arXiv:2609.20505v1).

The new finite input is the following exact computation, tailored to their Conjecture 5.1.

### Triple-cube exclusion through \(t=333333\)

For every integer \(1\le t\le333333\), there are no nonnegative integers \(a,b,c\) satisfying
\[
t^3+a^3=(t-1)^3+b^3=(t-2)^3+c^3=n
\]
together with
\[
t^3\le n<(t+1)^3.
\]
Equivalently, Applegate--Pratt Conjecture 5.1 has no counterexample with \(\lfloor n^{1/3}\rfloor\le333333\).

## Exhaustive reduction

If the first two equalities hold, then
\[
b^3-a^3=3t^2-3t+1,
\]
so
\[
12(b^3-a^3)-3=(6t-3)^2.
\]
For \(t\le T=333333\), the floor condition gives
\[
a^3<3t^2+3t+1,
\]
hence
\[
a^3\le 3T^2+3T,
\qquad a\le6933.
\]
Also
\[
b^3=a^3+3t^2-3t+1\le6T^2+1,
\qquad b\le8735.
\]
Thus every possible first pair is found by enumerating the finite set
\[
0\le a\le6933,\qquad a<b\le8735,
\]
and retaining exactly those pairs for which \(12(b^3-a^3)-3\) is a square \(s^2\) with \(s\equiv3\pmod6\), so that \(t=(s+3)/6\), followed by the floor condition. The final equality is then checked by testing whether
\[
c^3=a^3+6t^2-12t+8
\]
is a cube.

Exact integer arithmetic checks 36,531,779 pairs. There are 7,683 pairs producing an integral \(t\) in the required range before the floor condition, 579 floor-admissible first-pair solutions, and zero triple-cube solutions. A direct \((t,a)\) search through \(t=10000\) independently gives 110 first-pair solutions, exactly matching the pair-enumeration method on that range.

## Deduction of the improved prime-plus-two-cubes range

We use three results from Applegate--Pratt v1.

1. Their Theorem 3.1 proves that every positive integer \(m<10^{12}\) which is neither a cube nor a member of their finite exceptional set \(\mathcal E_3\) is \(p+x^3\) with \(p\) an odd prime and \(x>0\).
2. Their Theorem 3.2, specialized to \(N_3=10^{12}\), shows that in its range every admissible \(n\) is already \(p+x^3+y^3\), unless both
   \[
   n-t^3\quad\text{and}\quad n-(t-1)^3
   \]
   are cubes, where \(t=\lfloor n^{1/3}\rfloor\).
3. Their Corollary 3.5 proves the desired representation for every \(308<n<10^{16}\). Their exceptional set \(\mathcal E_3\) has maximum element \(78526384\).

Now assume
\[
10^{16}\le n<B,
\qquad t=\lfloor n^{1/3}\rfloor.
\]
Then \(t\le333333\). Moreover
\[
6(333334)^2=666669333336<10^{12}-2,
\]
so \(n<B\) lies inside the range required by Applegate--Pratt Theorem 3.2. If that theorem already gives the desired representation, there is nothing to prove. Otherwise write
\[
n-t^3=a^3,
\qquad n-(t-1)^3=b^3.
\]

Consider
\[
\alpha_2=n-(t-2)^3.
\]
Since \(n<(t+1)^3\),
\[
\alpha_2<9t^2-9t+9\le999995000013<10^{12}.
\]
Since \(n\ge10^{16}\), one has \(t\ge215443\), hence
\[
\alpha_2\ge t^3-(t-2)^3
=6t^2-12t+8
\ge278491532186>78526384.
\]
Thus \(\alpha_2\notin\mathcal E_3\). The exhaustive triple-cube computation above shows that \(\alpha_2\) is not a cube. Applegate--Pratt Theorem 3.1 therefore yields
\[
\alpha_2=p+x^3
\]
with \(p\) an odd prime and \(x>0\). Consequently
\[
n=p+x^3+(t-2)^3,
\]
and \(t-2>0\). Together with their Corollary 3.5, this proves the stated range.

## A local byproduct

Any integer having three representations
\[
n=t^3+a^3=(t-1)^3+b^3=(t-2)^3+c^3
\]
with integer \(a,b,c,t\) satisfies
\[
27\mid n.
\]
Indeed, cubes modulo \(9\) are \(0,\pm1\). Among three consecutive integers, their cubes modulo \(9\) are \(0,1,-1\), so the three requirements that the complementary summands also be cubes force \(n\equiv0\pmod9\). For the unique one of \(t,t-1,t-2\) divisible by \(3\), the complementary cube is then divisible by \(9\), hence its cube root is divisible by \(3\); both cubes in that representation are divisible by \(27\).

## Reproducibility

`artifacts/verify.cpp` is a standalone C++17 verifier using exact integer arithmetic for the exhaustive reduction. Its recorded output is in `artifacts/verification.txt`.

## Limitations

The prime-plus-two-cubes conclusion uses Applegate--Pratt Theorems 3.1 and 3.2 and Corollary 3.5 as published inputs; their underlying large computations were not independently re-executed here. The new computation proves only a finite range of Conjecture 5.1 and does not prove the conjecture in general or Conjecture 5.2.

## References

- Kenny Applegate and Kyle Pratt, *Computational Results on Sums of a Prime with Squares or Cubes*, arXiv:2609.20505v1, submitted 17 September 2026. https://arxiv.org/abs/2609.20505
- Accompanying code repository for the cited paper: https://github.com/kapplegate2020/Sums-of-a-Prime-with-Squares-or-Cubes

# Exact upper-base spectrum of Smith semiprimes
## Finding
Let \(p\le q\) be primes. Consider integer bases \(B\) satisfying
\[
q<B\le pq.
\]
Thus both prime factors are represented by one digit, while their product \(pq\) has exactly two base-\(B\) digits.

If \(p=2\), there is no such base in which \(pq\) is a Smith number.

If \(p\) and \(q\) are odd, put
\[
K=pq-p-q
\]
and
\[
\rho_-=
\frac{p+q-\sqrt{(p+q)^2-4K}}{2}.
\]
Then the complete set of bases in this upper-base stratum for which \(pq\) is Smith is
\[
\left\{
1+\frac{K}{a}:
a\mid K,\ 1\le a\le\rho_-
\right\}.
\tag{1}
\]

In particular, every base in (1) is even. The set is empty exactly for
\[
pq=9.
\]
Every other odd semiprime has the canonical base
\[
B=(p-1)(q-1).
\tag{2}
\]

Two small-prime layers simplify further. If \(p=3\) and \(q\ge5\), the base in (2) is the unique admissible base. If \(p=5\), there are exactly two admissible bases precisely when
\[
q\ge11
\quad\text{and}\quad
q\equiv2\pmod3;
\]
in that case they are
\[
B=4q-4
\quad\text{and}\quad
B=\frac{4q-2}{3}.
\]
Otherwise there is exactly one admissible base.

## Assumptions and scope
For an integer base \(B\ge2\), let \(s_B(n)\) be the sum of the base-\(B\) digits of \(n\). A composite integer \(n\), with prime factorization
\[
n=\prod_i r_i^{e_i},
\]
is a base-\(B\) Smith number when
\[
s_B(n)=\sum_i e_i s_B(r_i).
\]

The theorem fixes a semiprime \(pq\), permits \(p=q\), and varies the base only in the natural range
\[
q<B\le pq.
\]
The lower inequality makes both prime factors one-digit; the upper inequality makes the product two-digit. Bases at most \(q\), where one or both prime factors themselves have multiple digits, are not classified here.

## Proof
First suppose
\[
p=2.
\]
Since \(q<B\le2q\), the two-digit expansion of \(2q\) has leading digit \(1\):
\[
2q=B+c
\]
with
\[
0\le c<B.
\]
Thus
\[
s_B(2q)=1+c=1+2q-B.
\]
Both prime factors are one-digit, so their Smith-side digit sum is
\[
2+q.
\]
Equality would force
\[
1+2q-B=2+q,
\]
hence
\[
B=q-1,
\]
contrary to \(B>q\). Therefore no even semiprime occurs in the stated stratum.

Now let \(p,q\) be odd. Write
\[
pq=aB+c,
\qquad
1\le a<B,\quad 0\le c<B.
\]
Because \(B>q\), both \(p\) and \(q\) are one-digit. The Smith condition is therefore exactly
\[
a+c=p+q.
\tag{3}
\]

Set
\[
m=B-1.
\]
Using (3),
\[
pq=a(m+1)+c
=am+(a+c)
=am+p+q.
\]
Hence
\[
K=pq-p-q=am.
\tag{4}
\]
Thus
\[
m\mid K,
\qquad
a=\frac{K}{m}.
\tag{5}
\]

Conversely, suppose \(m\mid K\), put
\[
a=\frac{K}{m},
\qquad
c=p+q-a,
\qquad
B=m+1.
\]
Then (4) gives
\[
pq=aB+c,
\]
and (3) holds automatically. It remains only to impose the base-\(B\) digit bounds.

Because \(B>q\), one has
\[
m\ge q.
\]
Then
\[
a=\frac{K}{m}
\le\frac{K}{q}
=p-1-\frac{p}{q}
<p-1,
\]
so
\[
1\le a\le p-2.
\]
In particular \(c=p+q-a>0\). The only remaining digit restriction is
\[
c\le m.
\]
By the definition of \(c\), this is equivalent to
\[
m+\frac{K}{m}\ge p+q,
\]
or
\[
f(m):=m^2-(p+q)m+K\ge0.
\tag{6}
\]

The quadratic \(f\) has two positive roots because \(K>0\), and
\[
f(q)
=q^2-(p+q)q+K
=-p-q<0.
\]
Therefore \(q\) lies strictly between the two roots. Let the smaller root be \(\rho_-\) and the larger root be \(\rho_+\). Their product is
\[
\rho_-\rho_+=K.
\]
Since admissible \(m\) satisfy \(m\ge q\), condition (6) is equivalent to
\[
m\ge\rho_+.
\]
Writing
\[
a=\frac{K}{m},
\]
this is equivalent to
\[
a\le\rho_-.
\]
Together with \(a\mid K\), this proves the spectrum formula (1), because
\[
B=m+1=1+\frac{K}{a}.
\]

Since \(p\) and \(q\) are odd,
\[
K=pq-p-q
\]
is odd. Every divisor \(m\) of \(K\) is therefore odd, so every admissible base
\[
B=m+1
\]
is even.

It remains to identify the guaranteed canonical base. The divisor
\[
a=1
\]
is admissible exactly when
\[
1\le\rho_-.
\]
Because \(1<q<\rho_+\), this is equivalent to
\[
f(1)\ge0.
\]
A direct calculation gives
\[
f(1)
=pq-2p-2q+1
=(p-2)(q-2)-3.
\]
For odd primes \(p\le q\), this is nonnegative except at
\[
p=q=3.
\]
Thus \(9\) has no admissible base in the stratum, while every other odd semiprime has \(a=1\), giving
\[
B=K+1=(p-1)(q-1).
\]

For \(p=3\), one has
\[
f(3)=-p-q<0,
\]
so
\[
\rho_-<3.
\]
Since \(K\) is odd, the only positive divisor of \(K\) below \(3\) is \(1\). Hence the canonical base is unique for every \(q\ge5\).

For \(p=5\), similarly
\[
\rho_-<5.
\]
Again \(K\) is odd, so the only possible divisors \(a<5\) are \(1\) and \(3\). Here
\[
K=4q-5,
\]
so
\[
3\mid K
\quad\Longleftrightarrow\quad
q\equiv2\pmod3.
\]
Moreover
\[
f(3)=q-11.
\]
Thus \(a=3\) supplies a second base exactly when
\[
q\ge11
\quad\text{and}\quad
q\equiv2\pmod3,
\]
and that base is
\[
1+\frac{4q-5}{3}
=\frac{4q-2}{3}.
\]
This completes the classification.

## Verification
The accompanying checker directly evaluates base-\(B\) digit sums and exhausts every pair of primes
\[
p\le q<200
\]
and every base
\[
q<B\le pq.
\]
For odd \(p,q\), it compares the directly observed Smith bases with formula (1). For \(p=2\), it confirms that the set is empty.

The checker separately tests the \(p=3\) uniqueness statement and the \(p=5\) two-base criterion for every prime
\[
q<5000.
\]
It also verifies the canonical construction
\[
B=(p-1)(q-1)
\]
for all odd-prime pairs in the exhaustive window except \(p=q=3\).

These finite calculations corroborate the symbolic proof and are not used to infer the unrestricted theorem.

## Relationship to prior work
The natural invariant being studied here is classical: the Dunckley set of a composite integer is the set of bases in which it is a Smith number, and the Dunckley number is the size of that set. OEIS A060209 tabulates exactly this base-count invariant and cites Alfred and Dominic Vella's 2001 article *On Smith and Dunckley Numbers*.

The 2001 article is therefore the closest historical source. Its complete text was not available through the accessible web or repository routes inspected here. The exact database entry supplies the definition, values, bibliographic citation, and the example that \(10\) is Smith in base \(4\), but it does not state the upper-base semiprime spectrum (1). A 2010 thesis explicitly described as an exposition of the Vella article was also identified, but its repository record states that the document itself is unavailable. These access limitations are retained as an originality risk rather than treated as evidence of noncoverage.

Witno's 2013 paper gives a complete accessible primary-text comparison for the Smith predicate. It works in decimal, reviews classical Smith-number constructions, and develops repunit-based infinite families. Its full seven-page text was inspected; it does not vary the number base or classify semiprime base spectra. The paper lists primary MSC \(11A63\).

Witno's 2014 paper likewise concerns decimal Smith constructions from repunits. Its four-page text, including the main theorems and references, was inspected. It also lists MSC \(11A63\).

A separate exact database, A098837, tabulates decimal Smith semiprimes. It concerns one fixed base rather than the set of bases attached to a fixed semiprime.

The closest previously established fixed-base semiprime restriction is the congruence
\[
(p-1)(q-1)\equiv1\pmod{B-1}.
\]
In the present one-digit-factor/two-digit-product stratum, formula (4) shows why that necessary congruence becomes only the first step: the exact converse additionally requires the digit-bound threshold encoded by
\[
a\le\rho_-.
\]
The theorem therefore gives an exact varying-base spectrum rather than only a residue obstruction.

## Limitations
Only the upper-base stratum
\[
q<B\le pq
\]
is classified. A fixed semiprime can have additional Smith bases at or below \(q\), because then a prime factor has more than one digit. For example, the Dunckley invariant counts all bases, not just the upper stratum studied here.

The principal originality risk is the inaccessible 2001 Vella article, whose subject is exactly Smith numbers across varying bases. No full-text noncoverage claim is made for that article. The accessible A060209 record and the unavailable-thesis abstract were inspected specifically to make this risk explicit.

The proof is elementary, but the object is not an arbitrary slice: the number of bases in which a fixed composite is Smith is an established named invariant, and the theorem supplies a complete symbolic spectrum on the natural range where both prime factors remain one-digit.

## References
1. A. Vella and D. Vella, “On Smith and Dunckley Numbers,” *Mathematics Today* 37(2) (2001), 54–56.
2. OEIS Foundation, A060209, “Dunckley sequence: number of bases in which the n-th composite number is a Smith number.”
3. A. Witno, “A Family of Sequences Generating Smith Numbers,” *Journal of Integer Sequences* 16 (2013), Article 13.4.6.
4. A. Witno, “Multiples of repunits as sum of powers of ten,” *Arab Journal of Mathematical Sciences* 20(2) (2014), 246–249, DOI 10.1016/j.ajmsc.2013.09.001.
5. OEIS Foundation, A098837, “Smith semiprimes.”

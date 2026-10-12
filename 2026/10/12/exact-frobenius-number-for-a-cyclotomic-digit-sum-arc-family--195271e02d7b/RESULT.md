# Exact Frobenius number for a cyclotomic digit-sum arc family
## Finding
For every integer base \(b\ge2\) with \(b\not\equiv1\pmod 3\), put
\[
n=b^2+b+1=\Phi_3(b).
\]
Let \(s_b(N)\) denote the sum of the base-\(b\) digits of \(N\), and define
\[
\operatorname{Out}(s_b,n)=\{s_b(N):N\in\mathbb N,\ n\mid N\}.
\]
Then
\[
\max\bigl(\mathbb N\setminus\operatorname{Out}(s_b,n)\bigr)=2b-2.
\]
Equivalently, \(2b-2\notin\operatorname{Out}(s_b,n)\), while every integer \(t\ge2b-1\) belongs to \(\operatorname{Out}(s_b,n)\).

## Assumptions and scope
The base \(b\) is any integer at least \(2\) with \(b\not\equiv1\pmod3\). For \(n=b^2+b+1\),
\[
\gcd(b-1,n)=\gcd(b-1,3)=1,
\qquad
\gcd(b,n)=1.
\]
Thus the source paper's coprime case applies, and its Question 3.4 asks for the Frobenius number in this setting. The statement is an infinite-family theorem; the finite computation described below is only a regression check.

A theorem of Clokie et al. gives the following criterion: a positive integer \(t\) occurs as a base-\(b\) digit sum of a multiple of \(n\) if and only if there are \(t\) distinct powers of \(b\) whose sum is divisible by \(n\). Since
\[
b^3\equiv1\pmod n,
\]
this is equivalent to the existence of nonnegative integers \(x,y,z\) such that
\[
x+y+z=t,
\qquad
x+by+b^2z\equiv0\pmod n.
\]
There is no restriction on how large \(x,y,z\) are, because distinct exponents can be chosen independently in each of the three residue classes modulo \(3\).

## Proof
First, three digit sums occur uniformly. The identity
\[
1+b+b^2=n
\]
gives the value \(3\). For the value \(b+2\), use one power in the exponent class \(0\pmod3\) and \(b+1\) powers in the class \(1\pmod3\). Their residue sum is
\[
1+(b+1)b=n.
\]
For the value \(2b+1\), use \(b+1\) powers in the class \(0\pmod3\) and \(b\) powers in the class \(1\pmod3\). Their residue sum is
\[
(b+1)+b^2=n.
\]
Hence
\[
3,\ b+2,\ 2b+1\in\operatorname{Out}(s_b,n),
\]
and disjoint unions of the corresponding distinct-power witnesses show that every element of the numerical semigroup
\[
\langle3,b+2,2b+1\rangle
\]
belongs to \(\operatorname{Out}(s_b,n)\).

These three generators already cover every integer at least \(2b-1\). If \(b\equiv0\pmod3\), then their residues modulo \(3\) are \(0,2,1\). A target congruent to \(0\) is a multiple of \(3\); a target congruent to \(1\) and at least \(2b-1\) is at least \(2b+1\) and is \(2b+1\) plus a nonnegative multiple of \(3\); and a target congruent to \(2\) is \(b+2\) plus a nonnegative multiple of \(3\), because \((2b-1)-(b+2)=b-3\). If \(b\equiv2\pmod3\), the generator residues are \(0,1,2\). The same argument uses \((2b)-(b+2)=b-2\) for residue \(1\), and \(2b+1\) for residue \(2\). Thus every \(t\ge2b-1\) occurs.

It remains to exclude \(t_0=2b-2\). Suppose, to the contrary, that nonnegative \(x,y,z\) satisfy
\[
x+y+z=t_0,
\qquad
x+by+b^2z\equiv0\pmod n.
\]
Let \(m=\min(x,y,z)\), subtract \(m\) from all three coordinates, and write the resulting total as
\[
t'=t_0-3m.
\]
Because \(1+b+b^2\equiv0\pmod n\), the congruence is preserved. At least one new coordinate is zero. Multiplication by \(b\) cyclically permutes the three residue classes modulo \(n\), so after a cyclic relabeling we may assume the third coordinate is zero. We then have nonnegative \(x',y'\) with
\[
x'+y'=t',
\qquad
n\mid x'+by'.
\]
The quantity \(x'+by'\) is positive and satisfies
\[
x'+by'\le bt'\le b(2b-2)<2n.
\]
Therefore
\[
x'+by'=n.
\]
Since \(x'=t'-y'\), this becomes
\[
t'+(b-1)y'=n.
\]
As \(n-3=(b-1)(b+2)\), there is an integer \(k\) such that
\[
t'=3+k(b-1),
\qquad
y'=b+2-k.
\]
The inequality \(y'\le t'\) forces \(k\ge1\), while \(t'\le2b-2\) forces \(k\le1\). Thus \(k=1\) and
\[
t'=b+2.
\]
But \(t'=t_0-3m\), so \(t'\equiv t_0\pmod3\). Hence
\[
b+2\equiv2b-2\pmod3,
\]
which implies \(b\equiv1\pmod3\), contrary to the hypothesis. Therefore \(2b-2\) is absent. Combined with the preceding coverage, the Frobenius number is exactly \(2b-2\).

## Verification
The bundled script `verify.py` independently enumerates the three residue-class count triples supplied by the distinct-power criterion for every admissible base \(2\le b\le100\). It checks that \(2b-2\) is absent, that every tested value from \(2b-1\) through \(2b+12\) is present, and that explicit integer witnesses for the three generator digit sums are divisible by \(b^2+b+1\) and have the asserted digit sums. Its recorded output is:

`VERIFY_OK bases=66 post_frobenius_checks=924 generator_witnesses=198`

This finite replay is not used to infer the universal theorem; the proof above supplies the infinite argument.

## Relationship to prior work
Phunphayap, Pongsriiam, and Noppakaew prove general structural results for \(\operatorname{Out}(s_b,n)\) and explicitly ask in Question 3.4 for Frobenius numbers in the coprime case. Their paper does not give the cyclotomic family above or the value \(2b-2\).

Clokie et al. prove the distinct-powers characterization used here and a general propagation theorem for attainable digit sums. Those results reduce the present problem to a finite-residue zero-sum question but do not determine this exact Frobenius boundary. A previously checked general numerical-semigroup result for digit sums of multiples supplies a conductor bound, but likewise does not imply the exact value for \(n=\Phi_3(b)\).

## Limitations
The theorem covers the natural order-three cyclotomic family \(n=\Phi_3(b)\) only when \(b\not\equiv1\pmod3\), which is exactly the subfamily with \(\gcd(b-1,n)=1\). It does not determine Frobenius numbers for arbitrary \(n\), for higher cyclotomic values, or for the excluded congruence class \(b\equiv1\pmod3\), where the gcd obstruction changes the target set.

The literature comparison cannot rule out an unindexed or inaccessible source, but exact searches for the formula, the cyclotomic modulus, the digit-sum arc set, and the source question found no statement implying this theorem.

## References
1. P. N. Phunphayap, P. Pongsriiam, and P. Noppakaew, *Directed graphs of integers with arcs determined by an arithmetic function*, arXiv:2303.13017; final version DOI:10.61091/um124-06.
2. T. Clokie et al., *Computational Aspects of Sturdy and Flimsy Numbers*, arXiv:2002.02731; DOI:10.1016/j.tcs.2022.05.029.

# A positive-density squarefree collision family for digit-sum products

## Finding
For an integer base \(b\ge8\), let \(S_b(n)\) be the sum of the digits of \(n\) in base \(b\), and define
\[
H_b(n)=nS_b(n).
\]

Assume
\[
3\nmid b
\]
and each of
\[
b,\qquad b-2,\qquad 2b-3
\]
is squarefree. Then \(H_b\) is not injective on the squarefree positive integers.

Indeed, set
\[
x=b(2b-3),\qquad y=(b-2)(2b-3).
\]
Then \(x\ne y\), both \(x\) and \(y\) are squarefree, and
\[
H_b(x)=H_b(y)=b(b-2)(2b-3).
\]

Moreover, the set of bases satisfying these hypotheses has lower natural density at least
\[
\frac7{900}.
\]
In particular, Question 30 of Noppakaew and Pongsriiam has an affirmative answer for a positive-density set of bases \(b\ge11\).

## Assumptions and scope
The digit sum \(S_b(n)\) uses the ordinary radix-\(b\) expansion with digits in
\[
\{0,1,\ldots,b-1\}.
\]
Squarefree means that no square of a prime divides the integer.

The theorem does not prove noninjectivity on squarefree integers for every base \(b\ge11\). It proves an explicit collision for every base in a positive-density arithmetic family satisfying three simultaneous squarefreeness conditions.

## Proof
For \(b\ge8\),
\[
x=b(2b-3)=2b^2-3b
\]
has base-\(b\) digit expansion
\[
x=(1,\ b-3,\ 0)_b,
\]
because
\[
b^2+(b-3)b=2b^2-3b.
\]
Therefore
\[
S_b(x)=1+(b-3)=b-2.
\]

Similarly,
\[
y=(b-2)(2b-3)=2b^2-7b+6
\]
has base-\(b\) expansion
\[
y=(1,\ b-7,\ 6)_b.
\]
The hypothesis \(b\ge8\) ensures that \(b-7\) and \(6\) are valid base-\(b\) digits. Hence
\[
S_b(y)=1+(b-7)+6=b.
\]

Thus
\[
H_b(x)
=
b(2b-3)(b-2)
=
(b-2)(2b-3)b
=
H_b(y).
\]
Also,
\[
x-y=2(2b-3)>0,
\]
so the two arguments are distinct.

It remains to check squarefreeness. We have
\[
\gcd(b,2b-3)=\gcd(b,3),
\]
which equals \(1\) because \(3\nmid b\). Also
\[
\gcd(b-2,2b-3)=1.
\]
Therefore, if \(b\), \(b-2\), and \(2b-3\) are each squarefree, then both products \(x\) and \(y\) are squarefree.

To prove that such bases have positive density, restrict to
\[
b\equiv5\pmod{36}.
\]
On this progression,
\[
3\nmid b,
\]
and none of the three integers
\[
b,\qquad b-2,\qquad 2b-3
\]
is divisible by \(4\) or by \(9\). Hence only prime squares \(p^2\) with \(p\ge5\) can obstruct squarefreeness.

Fix a prime \(p\ge5\). Because \(p\) is coprime to \(36\), each of
\[
p^2\mid b,\qquad p^2\mid b-2,\qquad p^2\mid 2b-3
\]
cuts out exactly one residue class modulo \(p^2\) inside the progression \(b\equiv5\pmod{36}\). Thus, among integers \(b\le X\) in that progression, the number excluded by this prime is at most
\[
3\left(\frac{X}{36p^2}+1\right).
\]

Only primes with
\[
p^2\le2X
\]
can divide one of the three positive linear forms for \(b\le X\). By the union bound, the number of excluded \(b\le X\) is at most
\[
\frac{X}{12}\sum_{p\ge5}\frac1{p^2}+o(X).
\]
The elementary estimate
\[
\sum_{p\ge5}\frac1{p^2}
\le
\sum_{n=5}^{\infty}\frac1{n^2}
<
\frac1{25}+\int_5^\infty\frac{dt}{t^2}
=
\frac6{25}
\]
therefore gives
\[
\underline d
\ge
\frac1{36}-\frac1{12}\cdot\frac6{25}
=
\frac7{900},
\]
where \(\underline d\) denotes lower natural density.

Every surviving \(b\equiv5\pmod{36}\) is at least \(41\), so the digit expansions above are valid. This proves both the collision family and the density claim.

## Verification
The accompanying `verify.py` checks every base
\[
8\le b\le200000.
\]
Whenever the theorem's squarefreeness hypotheses hold, it independently constructs the two integers
\[
x=b(2b-3),\qquad y=(b-2)(2b-3),
\]
computes their base-\(b\) digit sums by repeated division, verifies that both arguments are squarefree, and confirms
\[
H_b(x)=H_b(y).
\]

It separately counts qualifying bases in the progression
\[
b\equiv5\pmod{36}
\]
as a finite regression check on the positive-density construction. The density theorem itself is proved by the union bound above, not by finite enumeration.

## Relationship to prior work
Noppakaew and Pongsriiam define
\[
H_b(n)=nS_b(n)
\]
and prove that \(H_b\) is noninjective on all positive integers for every base \(b\ge2\). They also exhibit squarefree collisions for each base
\[
2\le b\le10
\]
and explicitly ask in Question 30 whether \(H_b\) is noninjective on squarefree integers for every \(b\ge11\).

The present theorem gives one uniform algebraic collision template valid for every base satisfying three simple squarefreeness conditions and proves that those bases have positive lower density. It therefore supplies an infinite and positive-density partial resolution of the open squarefree problem, rather than a list of isolated computational examples.

Targeted searches for the exact function \(nS_b(n)\), the squarefree restriction, the polynomial pair
\[
b(2b-3),\qquad (b-2)(2b-3),
\]
and later work citing the focal paper did not locate this collision family or its density consequence.

## Limitations
The construction does not cover bases for which one of
\[
b,\qquad b-2,\qquad 2b-3
\]
has a repeated prime factor, and it does not settle all \(b\ge11\).

The density estimate
\[
\frac7{900}
\]
is deliberately elementary and not optimized. A sharper squarefree-sieve calculation would give a larger constant, but no sharper density is claimed here.

The principal residual originality risk is an unindexed observation deriving the same digit identity from Question 30 or a later note not surfaced by the targeted searches.

## References
1. Passawan Noppakaew and Prapanpong Pongsriiam, “Product of Some Polynomials and Arithmetic Functions,” Journal of Integer Sequences 26 (2023), Article 23.9.1.
2. P. Erdős, “Remarks on number theory II: some problems on the \(\sigma\) function,” Acta Arithmetica 5 (1959), 171–177.

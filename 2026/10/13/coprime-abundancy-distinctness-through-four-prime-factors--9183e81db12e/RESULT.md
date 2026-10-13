# Coprime abundancy distinctness through four prime factors

## Finding
Let \\(\\sigma(n)\\) be the sum of the positive divisors of \\(n\\), let
\\[
I(n)=\\frac{\\sigma(n)}{n},
\\]
and let \\(\\Omega(n)\\) count prime factors with multiplicity.

If \\(x\\) and \\(y\\) are distinct coprime positive integers satisfying
\\[
\\Omega(x)\\le4,\\qquad \\Omega(y)\\le4,
\\]
then
\\[
I(x)\\ne I(y).
\\]
Thus the coprime divisor-sum-ratio distinctness conjecture holds throughout the complete total-prime-factor layer \\(\\Omega\\le4\\).

## Assumptions and scope
All integers are positive. For
\\[
n=\\prod_p p^{e_p},
\\]
we use
\\[
\\Omega(n)=\\sum_p e_p
\\]
and
\\[
I(n)=\\prod_{p^{e_p}\\parallel n}\\left(1+\\frac1p+\\cdots+\\frac1{p^{e_p}}\\right).
\\]
The theorem concerns pairs for which both entries have total prime-factor multiplicity at most four. It does not claim distinctness when only one entry has that bound.

## Proof
Assume for contradiction that \\(x\\ne y\\), \\(\\gcd(x,y)=1\\), \\(\\Omega(x),\\Omega(y)\\le4\\), and
\\[
I(x)=I(y)=\\frac ab
\\]
with \\(\\gcd(a,b)=1\\).

Because \\(I(x)=\\sigma(x)/x\\), its reduced denominator \\(b\\) divides \\(x\\). The same argument gives \\(b\\mid y\\). Hence
\\[
b\\mid\\gcd(x,y)=1,
\\]
so \\(b=1\\): the common abundancy is an integer.

We next prove two exact bounds. If \\(\\Omega(n)<4\\), multiplying \\(n\\) by a new prime increases \\(I(n)\\) and raises \\(\\Omega\\) by one. Repeating this shows that it is enough to bound the five exponent partitions of total multiplicity four.

For arbitrary \\(n\\), the largest abundancy for each partition is obtained on the smallest available primes, with the finitely many assignments of exponents compared directly. The maxima are
\\[
\\begin{array}{c|ccccc}
\\text{partition}&(4)&(3,1)&(2,2)&(2,1,1)&(1,1,1,1)\\\\
\\hline
\\max I&\\frac{31}{16}&\\frac52&\\frac{91}{36}&\\frac{14}{5}&\\frac{96}{35}.
\\end{array}
\\]
Every entry is strictly below \\(3\\). Therefore
\\[
\\Omega(n)\\le4\\quad\\Longrightarrow\\quad I(n)<3.
\\]

For odd \\(n\\), the same calculation starts with the primes \\(3,5,7,11\\). The corresponding maxima are
\\[
\\begin{array}{c|ccccc}
\\text{partition}&(4)&(3,1)&(2,2)&(2,1,1)&(1,1,1,1)\\\\
\\hline
\\max I&\\frac{121}{81}&\\frac{16}{9}&\\frac{403}{225}&\\frac{208}{105}&\\frac{768}{385}.
\\end{array}
\\]
Every entry is strictly below \\(2\\). Hence
\\[
n\\text{ odd},\\ \\Omega(n)\\le4\\quad\\Longrightarrow\\quad I(n)<2.
\\]

If one of \\(x,y\\) were \\(1\\), then the common integer abundancy would be \\(1\\), forcing the other integer also to be \\(1\\), contrary to distinctness. Thus the common integer abundancy is at least \\(2\\). The first bound forces it to equal \\(2\\). The odd bound then forces both \\(x\\) and \\(y\\) to be even. This contradicts \\(\\gcd(x,y)=1\\).

Therefore \\(I(x)\\ne I(y)\\).

## Verification
The exponent-partition comparison uses exact rational arithmetic. For fixed exponent \\(e\\), the factor
\\[
1+\\frac1p+\\cdots+\\frac1{p^e}
\\]
is strictly decreasing with \\(p\\). Thus, for a fixed exponent assignment, replacing the ordered support by the first available primes can only increase abundancy; only the finite permutations of the exponent partition remain to compare.

The bundled checker recomputes all ten displayed rational maxima and, as a regression test only, searches all distinct coprime pairs up to \\(100000\\) whose two entries satisfy \\(\\Omega\\le4\\). It finds no equal-abundancy pair. The finite search is not used as the proof of the universal statement.

## Relationship to prior work
Becker studies the abundancy index and friends of integers of the form \\(2p\\), proving necessary support conditions for such friends. That paper gives the standard product and monotonicity properties used in abundancy arguments and classifies the topic under MSC \\(11A25\\), but it does not state a coprime-pair theorem or a total-multiplicity cutoff.

Ziller's work motivates the broader distinctness problem for values of multiplicative arithmetic functions. The current MathDB record for the associated divisor-sum-ratio problem states the conjecture for arbitrary distinct coprime inputs and reports the squarefree case as known, while leaving the general case open. The present theorem is a different slice: it allows repeated prime factors but closes every exponent pattern through total multiplicity four.

Targeted searches were made for the coprime formulation, friendly-number terminology, equal abundancy, and \\(\\Omega\\)-bounded variants. The closest exact low-multiplicity results found concern multiply-perfect and strongly pseudoperfect numbers; they do not imply the coprime equal-ratio statement here.

## Limitations
The theorem does not settle the conjecture for \\(\\Omega\\ge5\\). The proof method genuinely reaches a boundary: odd integers with five prime factors counted with multiplicity can already be abundant, so the simple deficiency argument used for the odd branch no longer extends automatically. No claim is made that \\(4\\) is the largest multiplicity for which the conjecture is true.

A residual originality risk remains that an equivalent low-multiplicity corollary may occur in older friendly-number literature under different terminology. Searches of the focal recent literature, current problem database, and targeted semantic records found no such coverage.

## References
1. Audrey Becker, *Friends of Two Times a Prime Number*, International Journal of Mathematics and Computer Science 18 (2023), 335–341; published 23 January 2023; AMS classification 11A25.
2. Mario Ziller, *Orders and partitions of integers induced by arithmetic functions*, arXiv:2310.15628v1, first submitted 24 October 2023.
3. MathDB problem 360472, *Distinctness conjecture for coprime values of the divisor-sum ratio*, current record consulted for the conjecture statement and status.

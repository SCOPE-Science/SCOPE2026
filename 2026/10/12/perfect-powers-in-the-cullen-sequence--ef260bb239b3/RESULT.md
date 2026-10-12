# Perfect powers in the Cullen sequence
## Finding
For integers \(n\ge1\), \(y\ge2\), and \(k\ge2\),
\[
n2^n+1=y^k
\]
holds if and only if
\[
(n,y,k)=(2,3,2)\quad\text{or}\quad(n,y,k)=(3,5,2).
\]
Thus the only perfect powers among the positive-index Cullen numbers are
\[
C_2=9\qquad\text{and}\qquad C_3=25.
\]

## Assumptions and scope
A positive-index Cullen number is
\[
C_n=n2^n+1\qquad(n\ge1).
\]
A perfect power means an integer \(y^k\) with integers \(y\ge2\) and
\(k\ge2\). The theorem classifies all such powers in the ordinary base-two
Cullen sequence. It does not address generalized Cullen numbers
\(ns^n+1\) with \(s>2\).

## Proof
Assume
\[
n2^n+1=y^k
\]
with \(n\ge1\), \(y\ge2\), and \(k\ge2\).

First suppose that \(k\) is odd. Then \(k\ge3\), and \(y\) is odd because
\(n2^n+1\) is odd. Factor
\[
y^k-1=(y-1)(1+y+\cdots+y^{k-1}).
\]
The second factor is a sum of an odd number of odd terms, hence is odd.
Writing
\[
n=2^t m,
\]
where \(m\) is odd, comparison of \(2\)-adic valuations gives
\[
2^{n+t}\mid y-1.
\]
Therefore
\[
y\ge2^{n+t}+1>2^{n+t}.
\]
Consequently
\[
y^k>2^{k(n+t)}\ge2^{3n}.
\]
But
\[
2^{3n}>n2^n+1
\]
for every \(n\ge1\): after division by \(2^n\), it is enough to note that
\(4^n>n+2^{-n}\). This contradicts \(y^k=n2^n+1\). Hence \(k\) cannot be
odd.

Now suppose that \(k\) is even. Then \(n2^n+1\) is a square. Write
\[
z^2=n2^n+1,
\]
where \(z=y^{k/2}\). The case \(n=1\) gives \(3\), not a square, so assume
\(n\ge2\). The integer \(z\) is odd. Put
\[
A=\frac{z-1}{2},\qquad B=\frac{z+1}{2}.
\]
Then \(A\) and \(B\) are consecutive and coprime, and if
\(n=2^t m\) with \(m\) odd, then
\[
AB=m2^{n+t-2}.
\]
Exactly one of \(A,B\) is even. Since they are coprime, the entire factor
\(2^{n+t-2}\) divides the even member, while the odd member divides \(m\).
The two members differ by \(1\), so necessarily
\[
2^{n+t-2}\le m+1\le n+1. \tag{1}
\]
For \(n=4\), the left side of the first inequality in (1) is \(16\), while
\(m+1=2\), impossible. For every \(n\ge5\),
\[
2^{n+t-2}\ge2^{n-2}>n+1,
\]
again contradicting (1). Thus \(n\le3\). Direct evaluation gives
\[
C_1=3,\qquad C_2=9,
\qquad C_3=25.
\]
Hence the only square Cullen numbers of positive index are \(9\) and \(25\).
Finally, neither \(9=3^2\) nor \(25=5^2\) is a higher perfect power, so in
the original equation \(k=2\). This proves the classification.

## Verification
The proof is unrestricted and uses only exact factorization and elementary
inequalities. The accompanying checker independently verifies the square
classification through \(n=5000\), checks odd exponents through a finite
corroborative range, and rechecks the exact inequalities used in the proof.
No finite search is used to infer the infinite statement.

## Relationship to prior work
Grau and Luca study the ordinary Cullen numbers \(C_n=n2^n+1\) in their work
on the Lehmer property. Their full text defines the same sequence and proves
that no composite Cullen number has the Lehmer property; it does not state a
square or perfect-power classification.

Marques surveys special Diophantine properties of Cullen numbers and notes
that locating Cullen numbers inside other familiar sequences has attracted
substantial attention. His paper treats Cullen and generalized Cullen numbers
that are Fibonacci numbers. The full text contains no square classification;
its occurrences of perfect powers concern auxiliary Fibonacci equations, not
perfect powers inside the Cullen sequence.

The square subcase is already public: Problem 4 of the British Mathematical
Olympiad Round 1 for 2023 asks for all positive integers \(n\) such that
\(n2^n+1\) is a square, and its official solution gives \(n=2,3\). The result
here does not claim novelty for that subcase. Its added content is the
elimination of every odd exponent \(k\ge3\), which together with the known
square boundary yields the complete perfect-power classification.

OEIS A002064 is the exact database for Cullen numbers. It begins
\[
1,3,9,25,65,161,\ldots
\]
and contains extensive Cullen-number references, but its inspected entry has
no square or perfect-power comment.

## Limitations
The theorem is specific to the ordinary base-two Cullen sequence. The argument
for odd exponents uses the concentration of the full \(2\)-adic valuation in
\(y-1\), while the square argument uses the exact power of \(2\) in
\((z-1)(z+1)\); neither is asserted here for arbitrary generalized Cullen
bases.

The square half of the theorem is previously known from the 2023 olympiad
problem. The originality claim is therefore only for the completion from
squares to all perfect powers. Because that completion is short, an equivalent
observation could exist in informal or unindexed problem literature; this is
the principal residual risk.

## References
1. J. M. Grau and F. Luca, "Cullen Numbers with the Lehmer Property",
   arXiv:1103.3578v1, 18 March 2011; later published in *Proceedings of the
   American Mathematical Society* 140 (2012), 129--134.
2. D. Marques, "On Generalized Cullen and Woodall Numbers That are Also
   Fibonacci Numbers", *Journal of Integer Sequences* 17 (2014), Article
   14.9.4, published 3 September 2014. Primary MSC 11B39.
3. UK Mathematics Trust, British Mathematical Olympiad Round 1 2023,
   Problem 4 and official markers' report.
4. OEIS Foundation, A002064, "Cullen numbers: \(a(n)=n2^n+1\)".

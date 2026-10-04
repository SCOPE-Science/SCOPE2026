# Even-base repdigit near-perfect numbers with two distinct prime factors

## Finding
For an integer base \(g\ge2\), put
\[
U_n=\frac{g^n-1}{g-1}=1+g+\cdots+g^{n-1}.
\]
A positive integer with \(n\) identical nonzero base-\(g\) digits equal to \(a\) is \(N=aU_n\), where \(1\le a<g\).

Assume that \(g\) is even, \(n\ge2\), and \(N=aU_n\) is near-perfect with exactly two distinct prime factors. Then necessarily \(n=2\), and exactly one of the following two families occurs.

**Family A.** There is a prime \(p\) for which \(M=2^p-1\) is prime and
\[
g=M^2-1,\qquad a=2^{p-1},\qquad N=2^{p-1}M^2.
\]
The redundant divisor is \(M\).

**Family C.** There are integers \(t\ge k+1\) for which
\[
q=2^t-2^k-1
\]
is an odd prime and
\[
g=q-1,\qquad a=2^{t-1},\qquad 2^{t-1}>2^k+2.
\]
Then
\[
N=2^{t-1}q
\]
and the redundant divisor is \(2^k\).

Conversely every parameter choice in either displayed family gives a two-digit repdigit in the indicated even base and is near-perfect with exactly two distinct prime factors.

For example,
\[
18=(22)_8
\]
is Family A, while
\[
88=(88)_{10},\qquad 104=(88)_{12},\qquad 368=(GG)_{22},\qquad 464=(GG)_{28}
\]
are Family C when the digit value \(G\) is interpreted as \(16\) in the last two bases.

## Assumptions and scope
A positive integer \(N\) is near-perfect if there is a proper divisor \(d\mid N\) such that
\[
\sigma(N)=2N+d.
\]
The symbol \(\omega(N)\) denotes the number of distinct prime factors of \(N\).

The theorem concerns repdigits with at least two digits in even bases and assumes \(\omega(N)=2\). It does not classify repdigit near-perfect numbers with three or more distinct prime factors, nor does it cover arbitrary odd bases.

The proof uses the published classification of near-perfect numbers with exactly two distinct prime factors: they are the three standard types A, B, C together with the isolated number \(40\). That classification is restated explicitly in Hasanalizade's paper and originates with Ren and Chen.

## Proof
Because \(g\) is even,
\[
U_n=1+g+\cdots+g^{n-1}
\]
is odd.

The published two-prime classification says that every near-perfect \(N\) with \(\omega(N)=2\) is one of
\[
2^{p-1}(2^p-1)^2,
\]
\[
2^{2p-1}(2^p-1),
\]
\[
2^{t-1}(2^t-2^k-1),
\]
or \(40\), with the indicated odd factors prime in the standard constructions.

Consider Type A and write \(M=2^p-1\). Since \(U_n\) is odd and \(N=aU_n=2^{p-1}M^2\), the full power \(2^{p-1}\) divides the digit \(a\). Also \(U_n>g>a\).

If \(U_n\) contained only one factor \(M\), then \(a\) would be divisible by \(2^{p-1}M>M=U_n\), contradicting \(a<U_n\). Therefore
\[
U_n=M^2,
\qquad
 a=2^{p-1}.
\]
For \(n\ge3\), the Ljunggren classification of repunit squares says that the only solutions of
\[
\frac{x^n-1}{x-1}=y^2,
\qquad x>1,
\qquad n>2,
\]
are
\[
(x,n,y)=(3,5,11)
\]
and
\[
(x,n,y)=(7,4,20).
\]
Neither \(11\) nor \(20\) is a Mersenne prime. Hence \(n=2\), so
\[
g+1=M^2,
\]
which gives Family A. The converse follows from the standard Type-A construction and \(a<g\).

For Type B, again put \(M=2^p-1\). Since \(M\) occurs only to the first power, oddness of \(U_n\) forces
\[
U_n=M
\]
and
\[
a=2^{2p-1}.
\]
But \(a<g<U_n=M<2^p\), whereas \(2^{2p-1}>2^p\) for \(p\ge2\), a contradiction. Thus Type B never occurs.

For Type C, put
\[
q=2^t-2^k-1.
\]
The odd prime \(q\) occurs once. If it divided the digit rather than \(U_n\), then the odd number \(U_n>1\) would have to divide the pure power of two \(2^{t-1}\), impossible. Therefore
\[
U_n=q,
\qquad
 a=2^{t-1}.
\]
If \(n\ge3\), then
\[
U_n\ge1+g+g^2>g^2>a^2=2^{2t-2}.
\]
For the two-prime Type-C case one has \(t\ge3\), and hence
\[
2^{2t-2}\ge2^t>q=U_n,
\]
a contradiction. Thus \(n=2\). Therefore
\[
g+1=q,
\]
so
\[
g=q-1=2^t-2^k-2.
\]
The digit condition \(a<g\) becomes
\[
2^{t-1}<2^t-2^k-2,
\]
which is equivalent to
\[
2^{t-1}>2^k+2.
\]
This is exactly Family C. Its converse follows from the standard Type-C near-perfect construction.

Finally consider \(N=40\). Since \(U_n\) is an odd divisor of \(40\) larger than \(1\), one must have \(U_n=5\). If \(n=2\), this forces \(g=4\) and \(a=8\), violating \(a<g\); for \(n\ge3\), one has \(U_n\ge7\). Hence \(40\) contributes no even-base repdigit with at least two digits.

The classification is complete.

## Verification
The accompanying `verify.py` checks both parametric families directly from the definition of near-perfectness and then performs an exhaustive regression over all even bases
\[
2\le g\le30,
\]
all digit lengths
\[
2\le n\le5,
\]
and all nonzero digits \(1\le a<g\). It factors each resulting repdigit exactly, tests \(\omega(N)=2\), and tests whether \(\sigma(N)-2N\) is a proper divisor of \(N\).

The exhaustive regression finds exactly five examples in this box:
\[
(22)_8=18,
\]
\[
(88)_{10}=88,
\]
\[
(88)_{12}=104,
\]
\[
(GG)_{22}=368,
\]
and
\[
(GG)_{28}=464,
\]
with \(G=16\). Every one belongs to Family A or Family C, and no example has three or more digits.

The computation is only a regression check. The proof for all even bases is the symbolic argument above.

## Relationship to prior work
Hasanalizade studies repdigit near-perfect numbers and proves that, for every base
\[
2\le g\le10,
\]
a near-perfect repdigit with exactly two distinct prime factors has at most two digits. The paper explicitly invokes the Ren--Chen classification into Types A, B, C and the isolated number \(40\).

The present result removes the upper bound \(g\le10\) for every even base and strengthens the conclusion from a length bound to a complete parametric classification. The even-base parity is decisive because \(U_n\) is odd, so all powers of two in the classified near-perfect forms are forced into the repeated digit.

The Type-A branch uses the same classical Ljunggren theorem on repunit squares that appears in Hasanalizade's proof. The Type-C branch needs only a size argument once parity has isolated the odd prime.

Targeted semantic searches for “near-perfect repdigit arbitrary base”, “repdigit near-perfect even base”, and equivalent phrases found no published theorem covering all even bases or giving these two exact parameter families.

## Limitations
The theorem depends on the published classification of near-perfect numbers with exactly two distinct prime factors. It says nothing about near-perfect repdigits with more prime factors.

Odd bases behave differently because \(U_n\) may carry powers of two, so the forcing argument used here does not transfer directly.

The theorem does not assert infinitude of either family: Family A depends on Mersenne primes, and Family C depends on primality of \(2^t-2^k-1\) together with the digit inequality.

As with any literature search, an equivalent result could exist under different terminology in an unindexed source.

## References
1. Elchin Hasanalizade, “On near-perfect numbers of special forms,” arXiv:2206.10353v1, first public 14 June 2022; Bulletin of the Australian Mathematical Society 108 (2023), 366–372; primary MSC \(11A25\).
2. Xiao-Zhi Ren and Yong-Gao Chen, “On near-perfect numbers with two distinct prime factors,” Bulletin of the Australian Mathematical Society 88 (2013), 520–524.
3. Wilhelm Ljunggren, “Some theorems on indeterminate equations of the form \((x^n-1)/(x-1)=y^q\),” Norsk Mat. Tidsskr. 25 (1943), 17–20.

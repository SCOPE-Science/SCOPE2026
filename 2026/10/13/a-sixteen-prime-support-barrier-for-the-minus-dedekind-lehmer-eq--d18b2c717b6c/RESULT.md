# A sixteen-prime support barrier for the minus Dedekind–Lehmer equation

## Finding
Let \(\psi\) be Dedekind's psi function,
\[
\psi(N)=N\prod_{p\mid N}\left(1+\frac1p\right),
\]
and let \(\omega(N)\) denote the number of distinct prime divisors of \(N\). If integers \(N>1\) and \(M\ge1\) satisfy
\[
\psi(N)=MN-1,
\]
then exactly one of the following holds:

1. \((N,M)=(2,2)\); or
2. \(N\) is odd and squarefree, \(M\) is odd with \(M\ge3\), and
\[
\omega(N)\ge16.
\]

Consequently \((2,2)\) is the unique solution with \(\omega(N)\le15\).

## Assumptions and scope
The equation is the minus-sign companion of the Dedekind-function Lehmer-type equations studied in the cited literature. No existence is asserted for the second branch. The result is a necessary support bound and a complete classification through fifteen distinct prime factors.

The proof uses only the defining Euler product for \(\psi\), parity, and an exact extremal product over the first fifteen odd primes.

## Proof
First, any solution is squarefree. Indeed, if \(p^2\mid N\), then the local factor in \(\psi(N)\) contributed by \(p^a\parallel N\), with \(a\ge2\), is \(p^{a-1}(p+1)\). Hence
\[
p\mid\psi(N).
\]
But \(p\mid N\) gives
\[
MN-1\equiv-1\pmod p,
\]
a contradiction.

Now suppose \(N\) is even. Since it is squarefree, either \(N=2\) or \(N\) has an odd prime divisor. In the latter case \(\psi(N)\) is even, because the factor \(q+1\) attached to an odd prime \(q\mid N\) is even, whereas \(MN-1\) is odd because \(N\) is even. Thus the latter case is impossible. For \(N=2\),
\[
\psi(2)=3=2\cdot2-1,
\]
so \((N,M)=(2,2)\).

It remains to consider odd \(N\). Since \(N\) is squarefree, every local factor \(p+1\) in \(\psi(N)\) is even. Therefore \(\psi(N)\) is even, and from
\[
MN-1=\psi(N)
\]
we infer that \(MN\) is odd. Hence \(M\) is odd. Also \(\psi(N)>N\), so \(M>1\), and therefore
\[
M\ge3.
\]

Assume for contradiction that \(r=\omega(N)\le15\). Write the distinct odd prime divisors as \(p_1<\cdots<p_r\), and let \(q_1=3,q_2=5,\ldots,q_{15}=53\) be the first fifteen odd primes. Since
\[
M=\frac{\psi(N)+1}N
=\prod_{i=1}^r\left(1+\frac1{p_i}\right)+\frac1N,
\]
and this expression decreases when any one of the primes \(p_i\) is increased while the others are held fixed, its maximum for fixed \(r\) occurs at \(p_i=q_i\). Exact evaluation for \(1\le r\le15\) shows that these maxima are nondecreasing, with the largest at \(r=15\):
\[
M\le
\frac{\prod_{i=1}^{15}(q_i+1)+1}{\prod_{i=1}^{15}q_i}
=
\frac{3746042448844705477}{1253429172199617105}
<3.
\]
This contradicts the odd-integer constraint \(M\ge3\). Hence every nontrivial solution has \(\omega(N)\ge16\), as claimed.

## Verification
The accompanying `verify.py` performs all finite arithmetic used above with exact integers and rational numbers. It verifies the first fifteen odd primes, the coordinatewise monotonicity formula, every fixed-support extremal value through \(r=15\), and the displayed terminal fraction. It also independently evaluates \(\psi(N)\) for every \(2\le N\le10^6\) and confirms that the only equation instance in that range with \(\omega(N)\le15\) is \((N,M)=(2,2)\).

The bounded scan is regression evidence only. The theorem is proved by the unrestricted argument above.

## Relationship to prior work
Subbarao's 1998 companion problem treats the plus-sign equation \(\psi(N)=MN+1\). For \(M>1\), the paper proves that \(M\) is odd and \(\omega(N)\ge16\); its displayed extremal-product argument is explicitly for the plus sign.

Yamada's 2023 paper treats both signs in analytic upper bounds. Its Theorem 3 gives an upper bound for \(M\) when \(\psi(N)=MN\pm1\), while Theorem 4 gives a bound in terms of \(\omega(N)\) under the hypothesis \(\omega(N)\ge4\). The paper separately cites Subbarao's \(16\)-prime lower bound only for the plus-sign equation. The minus-sign support barrier above is not implied by those upper bounds.

OEIS A001615 records the Dedekind psi function itself, and A203444 records its range and notes that \(\psi(N)\) is even for \(N>2\). Neither entry states the equation-level support classification.

Targeted searches for the minus equation, congruence \(\psi(N)\equiv-1\pmod N\), and a low-support or sixteen-prime bound found no implication-equivalent result.

## Limitations
The theorem does not prove that any solution with \(\omega(N)\ge16\) exists. The extremal product over the first sixteen odd primes exceeds \(3\), so the present elementary product argument cannot by itself raise the support threshold beyond \(15\).

The strongest residual originality risk is an unindexed observation extending Subbarao's plus-sign product estimate to the minus sign. The full Subbarao paper, Yamada's full paper, the natural OEIS entries, and targeted semantic and web searches were checked without locating that statement.

## References
1. Tomohiro Yamada, “On Lehmer's problem and related problems,” arXiv:2303.16853v1, submitted 29 March 2023. Primary MSC 11A25.
2. M. V. Subbarao, “A companion to a Lehmer problem,” *Publicationes Mathematicae Debrecen* 52 (1998), 683–698.
3. OEIS Foundation, A001615, “Dedekind psi function.”
4. OEIS Foundation, A203444, “Numbers in range of Dedekind Psi function.”

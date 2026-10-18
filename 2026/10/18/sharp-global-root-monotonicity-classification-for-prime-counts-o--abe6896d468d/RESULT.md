# Sharp global root-monotonicity classification for prime counts on integer rays

## Finding

Write \(\pi(x)\) for the number of primes not exceeding \(x\). For **every pair of integers** \(n\ge 2\) and \(k\ge 1\),
\[
\pi(nk)^{1/k}>\pi(n(k+1))^{1/(k+1)}
\]
except exactly at the following three pairs:
\[
(n,k)=(2,1),(2,2)\quad\text{(reverse inequality)},\qquad
(n,k)=(4,1)\quad\text{(equality)}.
\]
In particular, for each fixed integer \(n=3\) or \(n\ge5\), the entire infinite sequence \(\bigl(\pi(nk)^{1/k}\bigr)_{k\ge1}\) is strictly decreasing. For \(n=4\) it is nonincreasing with just one tie; for \(n=2\) it increases in its first two transitions and subsequently decreases.

Equivalently, for positive \(\pi(nk)\), the theorem classifies the sign of the integer expression \(\pi(nk)^{k+1}-\pi(n(k+1))^k\). This exact two-parameter result extends the original bounded-index range \(1\le k\le n\) and includes the sharp low-\(n\) boundary.

## Assumptions and scope

All logarithms are natural. The prime-counting function counts primes \(\le x\). The only analytic input is the unconditional lower bound \(\pi(x)>x/\log x\) for \(x\ge17\), due to Rosser and Schoenfeld (1962). No assumption on prime gaps or the Riemann hypothesis is made. The result treats all integers \(n\ge2\) and all integers \(k\ge1\) without an upper bound on either.

## Proof

Put \(x=nk\), \(A=\pi(x)\), \(B=\pi(x+n)\), \(\Delta=B-A\), and \(c=\lceil n/2\rceil\). When \(x\ge17\), the interval \((x,x+n]\) contains only odd prime candidates, so \(0\le\Delta\le c\). Since \(\log(1+t)\le t\) for \(t\ge0\),
\[
(k+1)\log A-k\log B
=\log A-k\log(1+\Delta/A)
\ge\log A-\frac{kc}{A}.
\]
Thus it suffices to show \(A\log A>kc=(c/n)x\).

For \(x\ge17\), the Rosser--Schoenfeld bound and monotonicity of \(y\log y\) for \(y\ge1\) yield
\[
A\log A>
\frac{x}{\log x}\log\!\left(\frac{x}{\log x}\right)
=x\left(1-\frac{\log\log x}{\log x}\right).
\tag{1}
\]
We need two elementary logarithmic estimates, with their boundary constants explicit.

First, \((\log x)^5<x^2\) for every \(x\ge17\). At \(x=17\), \(\log17<3\) and \(3^5<17^2\). The function \(x^2/(\log x)^5\) is strictly increasing whenever \(\log x>5/2\), which holds for \(x\ge17\). Consequently
\[
\frac{\log\log x}{\log x}<\frac25\qquad(x\ge17).
\tag{2}
\]
Second, \((\log x)^3<x\) for every \(x\ge128\). At \(x=128\), \(\log128<5\) and \(5^3<128\). The function \(x/(\log x)^3\) increases whenever \(\log x>3\), hence
\[
\frac{\log\log x}{\log x}<\frac13\qquad(x\ge128).
\tag{3}
\]
Both starting estimates are elementary, e.g. by positive partial sums of the exponential series verifying \(e^{5/2}<17<e^3\) and \(e^3<128<e^5\).

If \(n=2\), \(n=4\), or \(n\ge5\), then \(c/n\le3/5\). Combining (1) and (2) gives \(A\log A>3x/5\ge cx/n=kc\) whenever \(x\ge17\), proving the strict inequality there. If \(n=3\), then \(c/n=2/3\); (1) and (3) give \(A\log A>2x/3=kc\) for \(x\ge128\).

Only finite cases remain: \(n\ne3\) with \(n\ge2\), \(nk<17\), and \(n=3\), \(3k<128\). There are precisely \(71\) distinct pairs. The accompanying independently executable exact-integer checker constructs the prime-count array by a sieve and compares \(A^{k+1}\) and \(B^k\), never using floating-point powers. Its exhaustive output is strictly positive for every one of these pairs except
\[
(2,1):\ 1^2<2^1,\qquad
(2,2):\ 2^3<3^2,\qquad
(4,1):\ 2^2=4^1.
\]
These are therefore all exceptions. This completes the proof.

## Verification

Run `python3 CHECKER.py` with Python 3.8 or later; expected output begins `BOUNDARY_CHECK_OK 71` and reports exactly the three exceptional transitions. The checker enumerates the full finite boundary region, not an arbitrary sample. The infinite region is proved analytically using (1)--(3) and requires no computation.

## Relationship to prior work

Zhi-Wei Sun's *Problems on combinatorial properties of primes* (arXiv:1402.6641; first version February 25, 2014), Conjecture 2.7(i), proposes the strict inequality only for \(n>4\) and \(1\le k\le n\). A previously established bounded-index proof covers that asserted domain. The present theorem supplies **every unbounded index** \(k>n\), includes the new full ray \(n=3\), and gives the exact three exceptional low-parameter pairs. The bounded statement alone does not imply the unbounded extension.

Sun and Zhao's *On the set \(\{\pi(nk):k=1,2,3,\ldots\}\)* (arXiv:2004.01080) concerns representation of primes or almost primes among values \(\pi(nk)\), not monotonicity of their variable roots. The Rosser--Schoenfeld lower bound is an explicit input rather than a novelty claim.

## Limitations

The theorem concerns integer multipliers \(n\ge2\); it does not assert analogous inequalities for arbitrary real step sizes or generalized prime-counting functions. The finite checker independently corroborates only the finite boundary, not the infinite argument. Earlier unindexed, differently formulated, or stronger published results may exist. No independent scientific audit has been performed.

## References

1. Zhi-Wei Sun, *Problems on combinatorial properties of primes*, arXiv:1402.6641, Conjecture 2.7(i). https://arxiv.org/pdf/1402.6641 (first public version February 25, 2014).
2. Zhi-Wei Sun and Lilu Zhao, *On the set \(\{\pi(nk):k=1,2,3,\ldots\}\)*, arXiv:2004.01080, Sections 1--3. https://arxiv.org/pdf/2004.01080.
3. J. Barkley Rosser and Lowell Schoenfeld, *Approximate formulas for some functions of prime numbers*, Illinois J. Math. 6 (1962), 64--94. Explicit estimate \(\pi(x)>x/\log x\) for \(x\ge17\). See also Olivier Ramaré, *Explicit bounds on primes*, Section 1.2: https://ramare-olivier.github.io/TME-EMT/Latex/booklet.pdf.

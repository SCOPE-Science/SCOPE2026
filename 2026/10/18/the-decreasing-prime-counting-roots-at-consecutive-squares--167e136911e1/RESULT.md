# The decreasing prime-counting roots at consecutive squares

## Finding

Let \(\pi(x)\) be the number of rational primes not exceeding the real number \(x\). For every integer \(n\ge 3\),
\[
\pi(n^2)^{1/n}>\pi((n+1)^2)^{1/(n+1)}.
\]
Equivalently, putting \(A_n=\pi(n^2)\), one has the strict integer inequality
\[
A_n^{n+1}>A_{n+1}^{n}\qquad(n\ge 3).
\]
The lower endpoint is sharp: \(A_2=2\), \(A_3=4\), and \(2^3<4^2\). This proves Conjecture 2.14(ii) of Zhi-Wei Sun, *Problems on combinatorial properties of primes* (2014; arXiv:1402.6641), also recorded as a conjecture in OEIS A038107.

## Assumptions and scope

The integer variable satisfies \(n\ge3\). The prime-counting function counts primes \(p\le x\), including the endpoint if prime; no endpoint \(n^2\) with \(n\ge2\) is prime, so this convention agrees with the strict-inequality convention in OEIS A038107. Only classical unconditional estimates are used. The result does not assert that every interval between consecutive squares contains a prime, and it does not prove Legendre's conjecture.

## Proof

Write \(A=\pi(n^2)\), \(B=\pi((n+1)^2)\), and \(h=B-A\). Since \(B\ge A>1\), the desired inequality is equivalent to
\[
n\log(B/A)<\log A.
\]
We first prove this for every \(n\ge100\). The interval of integers \((n^2,(n+1)^2]\) contains \(2n+1\) integers. All its primes exceed three. In any six consecutive integers exactly two are coprime to six, and in any remaining block of at most five consecutive integers at most two are coprime to six. Consequently,
\[
0\le h\le 2\left\lfloor\frac{2n+1}{6}\right\rfloor+2
\le \frac{2n+7}{3}.
\]
The classical unconditional Rosser--Schoenfeld lower bound \(\pi(x)>x/\log x\) for \(x\ge17\) gives, for these indices,
\[
A>\frac{n^2}{2\log n}.
\]
Using \(\log(1+t)\le t\) for \(t\ge0\), we therefore obtain
\[
 n\log(B/A)
 =n\log(1+h/A)
 \le\frac{nh}{A}
 <\left(\frac43+\frac{14}{3n}\right)\log n
 \le\frac{69}{50}\log n
 <\frac32\log n.
\]
For every real \(t\ge100\), one has \(2\log t<\sqrt t\): the function \(\sqrt t-2\log t\) is positive at \(t=100\) and increasing for \(t>16\). Hence, for \(n\ge100\),
\[
\log A>2\log n-\log(2\log n)
>2\log n-\tfrac12\log n
=\tfrac32\log n.
\]
Combining the inequalities proves \(n\log(B/A)<\log A\), and thus the finding, for all \(n\ge100\).

For \(3\le n\le99\), the attached exact-integer verification enumerates all primes at most \(10000\), constructs \(A_n\) at each square, and tests the strict inequality \(A_n^{n+1}>A_{n+1}^{n}\) for every one of the 97 indices. The complete \((n,A_n,A_{n+1})\) table is included as `FINITE_CASES.csv` and is regenerated and checked by `VERIFY.py`. The finite part is exhaustive because the remaining bound is \(n\le99\), not a sample from the infinite range. This completes the proof.

## Verification

Run `python VERIFY.py` in the directory containing `VERIFY.py` and `FINITE_CASES.csv`. The checker independently identifies primality by a sieve and by trial division for each integer through \(10000\), asserts agreement, reproduces all 97 exact prime-count pairs from the CSV, checks each inequality by arbitrary-precision integer exponentiation, and verifies that the inequality reverses at \(n=2\). The analytical part needs no computational assumptions beyond the cited Rosser--Schoenfeld lower bound. No use of floating-point roots is made for the finite checks.

## Relationship to prior work

The exact strict-decrease assertion is stated without proof as Conjecture 2.14(ii) of Sun's 2014 paper and as the February 2014 conjecture comment in OEIS A038107. Sun's separate Conjecture 2.7(i) concerns the roots \(\pi(kn)^{1/k}\) when \(n\) is fixed and \(k\) varies, so it does not directly compare \(\pi(n^2)^{1/n}\) with \(\pi((n+1)^2)^{1/(n+1)}\). Hassani (2006) discusses the number \(\pi((n+1)^2)-\pi(n^2)\) of primes between consecutive squares, giving an infinitely-often lower estimate; this is not the global normalized-root inequality. OEIS A014085 tabulates those interval counts but does not prove the root inequality. The standard Rosser--Schoenfeld bound is a premise of the proof, not claimed to be new.

## Limitations

This establishes only the stated square-argument root monotonicity, not a prime in every consecutive-square interval or any claim about prime gaps of size \(2n+1\). The algebraic tail holds for \(n\ge100\); the first 97 indices depend on the supplied exhaustive exact-integer certificate. A literature search cannot exclude an earlier equivalent proof that was not indexed or accessed. The result has received no independent audit.

## References

1. Zhi-Wei Sun, *Problems on combinatorial properties of primes*, arXiv:1402.6641 (first submitted 25 February 2014), Conjecture 2.14(ii), https://arxiv.org/html/1402.6641v12.
2. OEIS Foundation, A038107, *Number of primes less than the square of the index*, comment dated 17 February 2014, https://oeis.org/A038107.
3. J. Barkley Rosser and Lowell Schoenfeld, *Approximate formulas for some functions of prime numbers*, Illinois J. Math. 6 (1962), 64--94, https://doi.org/10.1215/ijm/1255631807.
4. Mehdi Hassani, *Counting primes in the interval between consecutive squares*, arXiv:math/0607096 (2006), https://arxiv.org/html/math/0607096v1.
5. OEIS Foundation, A014085, *Number of primes between consecutive squares*, https://oeis.org/A014085.

# Connected Closure of Gaussian Reciprocal-Cube Divisor Sums

## Finding
For every nonzero Gaussian integer \(z\in\mathbb Z[i]\), let
\[
 F(z)=\sum_{[d]:\ d\mid z}|d|^{-3},
\]
where \([d]\) runs over divisors modulo multiplication by a Gaussian unit, and \(|d|\) is the ordinary complex modulus. Then the closure of its range is **one interval**, exactly
\[
 \boxed{\overline{\{F(z):0\ne z\in\mathbb Z[i]\}}
       =[1,\zeta(3/2)L(3/2,\chi_{-4})]}. 
\]
Here \(\chi_{-4}\) is the primitive real character modulo four. This is the smallest positive **integer** reciprocal exponent for which the Gaussian-divisor Euler product is bounded: at exponent three it already fills the entire allowable interval.

## Assumptions and scope
Divisibility, irreducibles and associates are in the Euclidean ring \(\mathbb Z[i]\); every divisor is counted once modulo its four units. For a Gaussian irreducible \(\pi\), let \(N(\pi)=|\pi|^2\). Set \(x_\pi=N(\pi)^{-3/2}\) and \(S_a(x)=1+x+\cdots+x^a\). Unique factorization gives
\[
 F(z)=\prod_{\pi^a\parallel z}S_a(x_\pi).
\]
The multiset of irreducible norms, in increasing order with repetitions, consists of one \(2\), two copies of each rational prime \(q\equiv1\pmod4\), and one \(q^2\) for every rational prime \(q\equiv3\pmod4\). The first thirteen norms are \(2,5,5,9,13,13,17,17,29,29,37,37,41\). Absolute convergence holds because the relevant Dirichlet-series parameter is \(3/2>1\). At reciprocal exponent two, the analogous Euler product is unbounded because the sum of reciprocals of rational primes congruent to \(1\pmod4\) diverges (the prime number theorem in arithmetic progressions), so exponent three is indeed the first bounded positive integer case.

## Proof
**1. An interval-filling lemma.** Let \(0<x_j<1\) be a sequence such that \(\sum_j x_j<\infty\), indexed with repetitions. Put \(T_j=\prod_{k>j}(1-x_k)^{-1}\). If
\[
 T_j\ge1+x_j\qquad\text{for every }j,
\]
then the closure of products \(\prod_j S_{a_j}(x_j)\) having only finitely many nonzero finite exponents \(a_j\) is
\[
 \left[1,\prod_j(1-x_j)^{-1}\right].
\]
Indeed, \(S_{a+1}(x)/S_a(x)\le1+x\), so the intervals \([S_a(x_j),S_a(x_j)T_j]\), over all \(a\ge0\) and the limiting exponent \(a=\infty\), cover \([1,(1-x_j)^{-1}T_j]\) without gaps. Repeatedly select such an exponent for a target \(y\) and divide by its local factor. The remaining target stays between \(1\) and the unused tail maximum. As \(j\to\infty\) the tail maximum tends to \(1\). Truncations (and finite approximations to any selected infinite exponent) converge to \(y\). Conversely every finite product lies in the stated interval.

**2. A short split-prime witness at every sufficiently large norm.** For every **integer** \(N\ge29\), there is a rational prime \(q\equiv1\pmod4\) satisfying
\[
 N<q\le\tfrac32N.
\]
For \(29\le N<8\cdot10^9\), this follows from the explicit list of seventy-three split-prime witnesses embedded in `verify.py`: it starts at \(37\), ends at \(8\,856\,541\,433\), and every successive quotient is less than \(3/2\). The script deterministically checks primality by trial division and all interval inequalities. If \(N\) lies between consecutive witnesses, choose the next witness; for \(N<37\), choose \(37\).

For \(N\ge8\cdot10^9\), Bennett--Martin--O'Bryant--Rechnitzer's Theorem 1.2 (2018), with \((q,a)=(4,1)\), gives for every real \(x\ge8\cdot10^9\)
\[
 |\theta(x;4,1)-x/2|<\frac{x}{160\log x},
\]
where \(\theta(x;4,1)=\sum_{p\le x,\ p\equiv1\ (4)}\log p\). Since \(\log x>20\), the difference \(\theta(3x/2;4,1)-\theta(x;4,1)\) exceeds
\[
 \frac{x}{4}-\frac{(5/2)x}{3200}>0.
\]
Thus the claimed split prime exists throughout the remaining range.

**3. Every norm at least \(29\) passes the overlap test.** Consider any irreducible with norm \(N\ge29\). Let \(q\) be the prime from step 2. Because \(q\equiv1\pmod4\), there are **two nonassociate** Gaussian primes of norm \(q\), both strictly later in the ordered norm multiset. Therefore
\[
 T_j\ge(1+q^{-3/2})^2
 >1+2q^{-3/2}>1+N^{-3/2},
\]
since \(q\le3N/2\) and \(2(3/2)^{-3/2}>1\) (equivalently \(32>27\)). This is precisely the interval-lemma hypothesis.

**4. The five genuinely small tests.** For the first, second and other exceptional norms below \(29\), it is enough to examine the positions \(0,2,3,5,7\) (zero-based) of the thirteen-entry initial norm array given above. A first copy of norm \(5\), \(13\), or \(17\) is immediately followed by an identical norm and automatically passes with equality. For the five remaining positions, the finite later product
\[
 \prod_{k=j+1}^{12}(1+N_k^{-3/2})>1+N_j^{-3/2}
\]
is strictly positive by exact rational enclosure. In `verify.py`, for each positive integer \(n\), the two rational bounds \(u_n^-\le n^{-3/2}\le u_n^+\) are computed with the integer square root of \(10^{16}n\); the script verifies \(\prod(1+u_{N_k}^-)>1+u_{N_j}^+\). These strict finite comparisons suffice because the actual infinite tail is at least the product used in the comparisons.

**5. Endpoint and conclusion.** The interval lemma applies to every norm. Its upper endpoint is the full Gaussian Euler product
\[
 \prod_{[\pi]}(1-N(\pi)^{-3/2})^{-1}
 =\zeta_{\mathbb Q(i)}(3/2)
 =\zeta(3/2)L(3/2,\chi_{-4}).
\]
The lower endpoint is \(F(1)=1\). This proves the claimed closure.

## Verification
Run `python3 verify.py` with a standard Python interpreter; it uses only `math.isqrt` and `fractions.Fraction`. It checks primality of all seventy-three split-prime witnesses by exact trial division, their interval chain and terminal bound, and all five small-norm inequalities using exact rational square-root enclosures. The observed output is:

`EXACT_CERTIFICATE_OK witnesses=73 start=37 last=8856541433 small_cases=5 initial_norms=13`

The cited published prime-distribution bound supplies the infinite-range step; the finite computation alone does not.

## Relationship to prior work
De Sanctis--Reid (2013, arXiv:1305.5502v1) establishes the Gaussian-prime norm decomposition and Gaussian Dedekind-zeta Euler product in a coprimality setting; it does not examine closures of reciprocal divisor sums. Defant (2015, arXiv:1507.02663v1) treats the ranges of reciprocal divisor sums on subsets of the **ordinary positive integers**; its conclusions do not determine the present Gaussian-integer closure, where split primes contribute twice and inert primes contribute squared norms. OEIS A103230 treats the **norm of the complex Gaussian divisor sum**, which is a different function from the **sum of reciprocal norms** defined here. The prime-in-progression bound used for the tail is from Bennett--Martin--O'Bryant--Rechnitzer (2018); that theorem does not discuss divisor-sum topology.

## Limitations
The conclusion is about the **topological closure**, not pointwise realization of every real value, not a measure-theoretic distribution of values, and not divisor sums of arbitrary real exponents or arbitrary quadratic fields. The novelty assessment is based on the identified published sources and searches; unindexed prior computations or papers are a residual risk. The interval's exact upper endpoint is defined by convergent special-function values and need not be attained by a finite Gaussian integer.

## References
- B. De Sanctis and S. Reid, *On the Probability of Relative Primality in the Gaussian Integers*, arXiv:1305.5502v1, first posted 23 May 2013, https://arxiv.org/abs/1305.5502.
- C. Defant, *On the Density of Ranges of Generalized Divisor Functions with Restricted Domains*, arXiv:1507.02663v1, first posted 9 July 2015, https://arxiv.org/abs/1507.02663.
- M. A. Bennett, G. Martin, K. O'Bryant and A. Rechnitzer, *Explicit bounds for primes in arithmetic progressions*, Theorem 1.2, arXiv:1802.00085, first posted 31 January 2018, https://arxiv.org/abs/1802.00085.
- OEIS A103230, *Norm of the sum of divisors function generalized for Gaussian integers*, https://oeis.org/A103230 (related, mathematically distinct divisor function).

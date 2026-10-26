# Exact quasipolynomial growth for fixed rows of the natural-seed Z-game

## Finding
For integers \(m\ge0\), \(n\ge1\), start with \(a_{0,n}=n\) and set
\[
 a_{m+1,n}=Z(a_{m,n},a_{m,n+1}),\qquad Z(u,v)=\frac{uv}{\gcd(u,v)^2}.
\]
Define the odd-binomial support and its polynomial by
\[
 J_m=\left\{j:0\le j\le m,\ \binom{m}{j}\equiv1\pmod2\right\},\qquad P_m(X)=\prod_{j\in J_m}(X+j).
\]
**Theorem.** Every fixed generation satisfies, identically for all \(n\ge1\),
\[
 a_{m,n}=c_m(n)P_m(n),
\]
where \(c_m(n)\) is a positive rational number, periodic as a function of \(n\). An explicit (not necessarily least) period is \(Q_0=Q_1=1\) and, for \(m\ge2\),
\[
 Q_m=\prod_{p\le m\ \mathrm{prime}}p^{H_{m,p}},\qquad
 H_{m,p}=2^{m+1}\bigl(1+\lfloor\log_p m\rfloor\bigr)+1.
\]
The row is therefore an exact integer-valued quasipolynomial in \(n\) whose degree on *every* residue class is
\[
 d_m=|J_m|=2^{s_2(m)},
\]
where \(s_2(m)\) counts the ones in the base-two expansion of \(m\). For \(n\) uniformly distributed on the positive integers at most \(N\), the normalized variable \(a_{m,n}/n^{d_m}\) converges in distribution as \(N\to\infty\) to the finite atomic law
\[
 \frac1{Q_m}\sum_{r=0}^{Q_m-1}\delta_{c_m(r)},
\]
where \(c_m(r)\) means its periodically extended residue-class value.

For instance, \(a_{2,n}=n(n+2)\) when \(n\) is odd, and \(a_{2,n}=n(n+2)/4\) when \(n\) is even; \(a_{3,n}=n(n+1)(n+2)(n+3)/4\) unless \(3\mid n\), in which case the denominator is \(36\).

## Assumptions and scope
All variables \(m\) and \(n\) are integers with \(m\ge0\) and \(n\ge1\). Products are finite, \(\gcd\) is positive, and valuations \(\nu_p(k)\) apply to positive integers \(k\). The logarithm \(\lfloor\log_p m\rfloor\) is the largest integer \(b\) such that \(p^b\le m\); it occurs only for \(p\le m\) when \(m\ge2\). The term quasipolynomial means a polynomial, here with rational coefficients, separately on each residue class of a fixed positive integer period. The theorem does not assert that the displayed period is least.

## Proof
**1. Valuation dynamics.** For any prime \(p\), the defining rule has the exact property
\[
 \nu_p(Z(u,v))=|\nu_p(u)-\nu_p(v)|.
\]
For a vector \((x_0,\ldots,x_m)\) of nonnegative integers, let \(F_m(x_0,\ldots,x_m)\) denote the single number produced by \(m\) iterations of the adjacent absolute-difference operation (with \(F_0(x_0)=x_0\)). Then
\[
 \nu_p(a_{m,n})=F_m\bigl(\nu_p(n),\ldots,\nu_p(n+m)\bigr).
\]

**2. All primes larger than the row index.** If \(p>m\), among the \(m+1\) integers \(n,n+1,\ldots,n+m\) at most one is divisible by \(p\). Its initial valuation, if nonzero, is a single spike of some height \(e\). Absolute differences of values in \(\{0,e}\) are exactly exclusive-or on the indicators, so at step \(m\) the spike survives precisely at the indices with odd binomial coefficient \(\binom mj\). Thus, for every \(p>m\),
\[
 \nu_p(a_{m,n})=\sum_{j\in J_m}\nu_p(n+j)=\nu_p(P_m(n)).
\]
This includes the case with no initial spike.

**3. A uniform one-spike stability lemma.** Let \(B\) be any nonnegative integer, and suppose a vector of length \(m+1\) has one entry \(e\) at index \(j\), the remaining entries between \(0\) and \(B\). If \(e>2^{m+1}B\), the result of \(m\) absolute-difference iterations is
\[
 F_m=\varepsilon_{m,j}e+b,
\]
where \(\varepsilon_{m,j}=\binom mj\bmod2\) is either \(0\) or \(1\), and the integer \(b\), possibly negative, depends on all the other entries and \(j\) but **not on** \(e\). To prove this, write every entry at intermediate depth \(r\) as \(\varepsilon e+b\) with \(\varepsilon\in\{0,1}\) and \(|b|\le2^rB\). The initial statement is evident. If two neighboring coefficients \(\varepsilon\) agree, their difference has no \(e\) term, and its absolute value is an \(e\)-independent integer of absolute value at most \(2^{r+1}B\). If the coefficients differ, their difference is \(\pm e+b'\) with \(|b'|\le2^{r+1}B<e\), so its absolute value is \(e\) plus a fixed integer, again bounded in size by \(2^{r+1}B\). The new coefficient is the exclusive-or of the previous coefficients. Induction through depth \(m\) proves the lemma and the Pascal parity assertion.

**4. All small primes leave only a periodic correction.** Fix \(p\le m\) and put \(B=\lfloor\log_p m\rfloor\), so \(p^{B+1}>m\). Among \(n,n+1,\ldots,n+m\), at most one has \(p\)-valuation exceeding \(B\); otherwise two of these integers would differ by a nonzero multiple of \(p^{B+1}\), impossible for a difference at most \(m\). Put \(H=2^{m+1}(B+1)+1\), and let \(x_j=\nu_p(n+j)\) and \(y_j=\min(x_j,H)\). If all \(x_j\le H\), there is nothing to prove. Otherwise exactly one \(x_j\) exceeds \(H\) and all the others are at most \(B\). Apply the stability lemma twice, to the one-spike vectors of heights \(x_j\) and \(H\):
\[
 F_m(x_0,\ldots,x_m)-F_m(y_0,\ldots,y_m)
 =\varepsilon_{m,j}(x_j-H).
\]
As \(\varepsilon_{m,j}=1\) precisely when \(j\in J_m\), the same difference appears in \(\sum_{i\in J_m}x_i-\sum_{i\in J_m}y_i\). Therefore the exponent
\[
 E_{m,p}(n)=F_m(x_0,\ldots,x_m)-\sum_{j\in J_m}x_j
\]
is determined solely by the truncated valuation vector \((y_0,\ldots,y_m)\). Every \(\min(\nu_p(n+j),H)\) depends only on \(n+j\pmod{p^H}\), including the zero residue (assigned truncated valuation \(H\)). Consequently \(E_{m,p}(n)\) is periodic in \(n\) modulo \(p^H\).

**5. Assemble the exact row formula.** The large-prime result in step 2 gives
\[
 \frac{a_{m,n}}{P_m(n)}=\prod_{p\le m}p^{E_{m,p}(n)}=:c_m(n),
\]
with an empty product interpreted as \(1\) for \(m=0,1\). The exponent in each factor is an integer, and finitely many factors give a positive rational number. Step 4 and the Chinese remainder theorem show that \(c_m\) has period dividing \(Q_m\). On each residue class modulo \(Q_m\), the displayed exact formula is a constant positive rational multiple of the monic polynomial \(P_m(n)\). Thus it has degree \(|J_m|\) on every residue class. Lucas's theorem modulo two (or the binary factorization of \((1+X)^m\) over the two-element field) gives \(|J_m|=2^{s_2(m)}\). Finally \(P_m(n)/n^{d_m}\to1\) as \(n\to\infty\), uniformly over the finitely many residue classes. Each class has natural density \(1/Q_m\), proving the limiting atomic law.

For the examples, \(m=2\) follows from \(Z(n,n+1)=n(n+1)\) and \(\gcd(n(n+1),(n+1)(n+2))=(n+1)\gcd(n,n+2)\), hence \(a_{2,n}=n(n+2)/\gcd(n,2)^2\). For \(m=3\), all primes \(p\ge5\) have zero correction by step 2. For \(p=2\), exactly two of the four consecutive integers are even, at positions separated by two, and their valuations are \(1\) and \(e\ge2\). Three adjacent absolute-difference operations on either initial vector \((e,0,1,0)\) or \((0,e,0,1)\), allowing the positions of \(e\) and \(1\) to interchange, give \(F_3=e-1\), whereas the sum of initial valuations is \(e+1\). The \(2\)-adic correction is therefore always \(-2\). For \(p=3\), if \(3\nmid n\) only one of the four integers is a multiple of three and there is no correction. If \(3\mid n\), both endpoints are divisible by three with valuations \(e\ge1\) and \(1\) (in either order), so \(F_3=|e-1|=e-1\) whereas their sum is \(e+1\); the correction is \(-2\). Thus \(c_3(n)=1/4\) when \(3\nmid n\) and \(c_3(n)=1/36\) otherwise, for all \(n\ge1\).

## Verification
The included standalone `verify.py` checks 1,980 directly computed cells for \(0\le m\le10\) and \(1\le n\le180\), including their local prime valuations and the displayed formulas for \(m=2,3\). It also tests the high-spike stability principle in 337 synthetic configurations at far-separated spike heights. All tests pass. These finite experiments corroborate, but do not replace, the universal induction and prime-local argument.

## Relationship to prior work
Cobeli and Zaharescu (2014) introduce this divisor-and-absolute-difference game, prove prime-initial-sequence statements through Pascal parity, and raise the natural-integer-initial-sequence case. Cobeli, Prunescu and Zaharescu (2015) analyze prime-power tomographies, including a complete \(2\)-adic slice of the natural-seed triangle, and show periodic behavior for a **different, squarefree-kernel initial sequence**. Those results do not, as stated, give a fixed-generation global quasipolynomial, its degree \(2^{s_2(m)}\), a small-prime periodic rational multiplier, or the corresponding normalized limiting distribution. The present argument isolates the contribution of every sufficiently large prime uniformly at any fixed depth and absorbs all small primes into an effective periodic correction.

## Limitations
The period \(Q_m\) is an effective, generally enormous upper bound and is not claimed minimal. The proof describes a fixed generation as the starting position \(n\) varies; it does not establish any polynomial growth statement uniform in the generation index \(m\). The finite atomic law depends on \(m\); no joint limit with \(m\to\infty\) is asserted. A detailed independent literature audit has not been performed and unindexed equivalent formulations remain an originality risk.

## References
1. C. Cobeli and A. Zaharescu, *A game with divisors and absolute differences of exponents*, arXiv:1411.1334v1 (first publicly posted 2014-11-05), https://arxiv.org/abs/1411.1334.
2. C. Cobeli, M. Prunescu and A. Zaharescu, *A growth model based on the arithmetic Z-game*, arXiv:1511.04315v1 (2015-11-13), https://arxiv.org/abs/1511.04315.
3. C. Cobeli and A. Zaharescu, *A promenade around Pascal triangle – number motives*, Bulletin of the Romanian Mathematical Society 56 (2013), Section 9, https://rms.unibuc.ro/bulletin/pdf/56-1/PromenadePascalPart1.pdf.

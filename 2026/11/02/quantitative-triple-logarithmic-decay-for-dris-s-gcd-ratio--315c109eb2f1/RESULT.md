# Quantitative triple-logarithmic decay for Dris's GCD ratio

## Finding
Let \(\sigma(n)\) denote the sum of positive divisors of \(n\), and put
\[
R(n)=\frac{\gcd(n^2,\sigma(n^2))}{\gcd(n,\sigma(n^2))}\in\mathbb Z_{\ge1}.
\]
For **every fixed real number** \(T\ge1\), there exists a constant \(C_T>0\) such that, for all sufficiently large \(X\),
\[
\boxed{\#\{1\le n\le X:R(n)\le T\}
\le C_T\frac{X}{\sqrt{\log\log\log X}}.}
\tag{1}
\]
In particular, Dris's divisor-sum GCD-equality set
\[
\mathcal A=\{n\ge1:\gcd(n,\sigma(n^2))=\gcd(n^2,\sigma(n^2))\}
\]
has the quantitative upper bound \(\#(\mathcal A\cap[1,X])=O(X/\sqrt{\log\log\log X})\). The result strengthens previously established *qualitative* zero-density and ratio-divergence-in-density theorems by supplying a uniform-in-\(X\) asymptotic rate for each fixed threshold.

## Assumptions and scope
All logarithms are natural, the limit is \(X\to\infty\), and the implied constant may depend on fixed \(T\) but not on \(X\). The ratio is an integer because \(\gcd(n,\sigma(n^2))\mid\gcd(n^2,\sigma(n^2))\). No parity, squarefreeness or restricted-prime-support assumption on \(n\) is made. We use the classical Turán–Kubilius mean-square inequality for general additive arithmetic functions, the Siegel–Walfisz theorem in the small-modulus range, and Mertens' theorem for primes in the progression \(1\pmod3\). These are explicitly identified analytic inputs; the finite arithmetic deductions below are unconditional.

## Proof
**1. Local obstruction.** For every prime \(p\equiv1\pmod3\), choose a residue \(r_p\pmod p\) of multiplicative order three. Then \(r_p^2+r_p+1\equiv0\pmod p\). If \(p\parallel n\) and there are at least two distinct primes \(q\equiv r_p\pmod p\) with \(q\parallel n\), the factors \(\sigma(q^2)=1+q+q^2\) of \(\sigma(n^2)\) give \(p^2\mid\sigma(n^2)\). Consequently
\[
\nu_p\bigl(\gcd(n^2,\sigma(n^2))\bigr)=2,
\qquad
\nu_p\bigl(\gcd(n,\sigma(n^2))\bigr)=1,
\]
so \(p\mid R(n)\). In particular \(R(n)>T\) if \(p>T\).

**2. Uniform witness count.** Write \(L=\log\log X\) and \(Y=L^{1/3}\); all subsequent assertions concern sufficiently large \(X\). For each prime \(p\le Y\), \(p\equiv1\pmod3\), define the additive function
\[
f_p(n)=\#\{q\text{ prime}:q\parallel n,\ q\equiv r_p\pmod p\}.
\]
Its prime-power values are \(f_p(q^a)=1\) when \(a=1\) and \(q\equiv r_p\pmod p\), and zero otherwise. The Turán–Kubilius normalizing quantities are therefore exactly
\[
A_p(X)=\sum_{\substack{q\le X\\q\equiv r_p\ (p)}}\left(\frac1q-\frac1{q^2}\right),
\qquad
B_p(X)^2=\sum_{\substack{q\le X\\q\equiv r_p\ (p)}}\frac1q.
\tag{2}
\]
They satisfy, **uniformly in** \(p\le Y\),
\[
A_p(X)=\frac{L}{p-1}+O(\log L),
\qquad B_p(X)^2=\frac{L}{p-1}+O(\log L).
\tag{3}
\]
For completeness, set \(z=\exp(L^2)\). The contribution from primes \(q\le z\) to either sum in (2) is at most \(O(\log\log z)=O(\log L)\), by the ordinary Mertens bound. For \(z<q\le X\), Siegel–Walfisz applies uniformly because \(p\le L^{1/3}\le(\log z)^{1/6}\) and \(z\le X\) for large \(X\). Partial summation gives \((\log\log X-\log\log z)/(p-1)+O(1)\); the convergent \(q^{-2}\) sum alters this by \(O(1)\). This proves (3) with absolute constants (possibly ineffective in the Siegel–Walfisz term).

Since \(L/p\ge L^{2/3}\gg\log L\) for these primes, (3) implies \(A_p(X)\asymp L/p\) and \(B_p(X)^2\ll L/p\), with absolute constants. Turán–Kubilius, in its general additive-function form, states uniformly for these functions that
\[
\sum_{n\le X}|f_p(n)-A_p(X)|^2\ll X B_p(X)^2.
\]
When \(f_p(n)<2\), the difference has size at least \(A_p(X)-2\gg L/p\). Therefore
\[
\#\{n\le X:f_p(n)<2\}\ll X\frac{B_p(X)^2}{A_p(X)^2}\ll X\frac pL.
\tag{4}
\]

**3. Sieve by the outer primes.** Fix \(T\), and let
\[
P_X=\{p\le Y:p\equiv1\pmod3,\ p>T\}.
\]
The union of the exceptional sets in (4) has size
\[
\ll\frac XL\sum_{p\in P_X}p\ll X\frac{Y^2}{L}=X L^{-1/3}.
\tag{5}
\]
If \(R(n)\le T\) and \(n\) lies outside this union, Step 1 forces \(p\not\parallel n\) for every \(p\in P_X\). This latter condition is periodic modulo \(M_X=\prod_{p\in P_X}p^2\), so CRT gives its exact asymptotic density, with a finite-counting error:
\[
\#\{n\le X:p\not\parallel n\ \forall p\in P_X\}
=X\prod_{p\in P_X}\left(1-\frac{p-1}{p^2}\right)+O(M_X).
\tag{6}
\]
The crude bound \(M_X\le\exp(2Y\log Y)=X^{o(1)}\) makes \(M_X=o(X L^{-1/3})\). Mertens' theorem for primes \(p\equiv1\pmod3\) gives
\[
\sum_{\substack{p\le Y\\p\equiv1\ (3)}}\frac1p
=\frac12\log\log Y+O(1).
\]
As \((p-1)/p^2=1/p+O(p^{-2})\), omission of the finitely many \(p\le T\) changes only the constant, and
\[
\prod_{p\in P_X}\left(1-\frac{p-1}{p^2}\right)
\ll_T\frac1{\sqrt{\log Y}}
\asymp\frac1{\sqrt{\log L}}.
\tag{7}
\]
Combining (5)–(7), and observing that \(L^{-1/3}=o((\log L)^{-1/2})\), proves (1), since \(\log L=\log\log\log X\). \(\square\)

## Verification
The accompanying `verify.py` independently reconstructs \(\sigma(n^2)\) from prime-power factors and checks the GCD equality for \(100000\) consecutive integers, matching the five earlier published counts \(10,99,974,9561,93845\) at cutoffs \(10,100,1000,10000,100000\). It constructs the order-three local witnesses for \(p=7,13,19,31,37\) and exactly enumerates a local CRT condition. It returned:

```
VERIFY_OK gcdn_counts=100000 source_cutoffs=5 witness_primes=5 crt_residues=196
```

These tests only verify finite identities and examples. The triple-logarithmic *rate* depends on the analytic inequalities and the uniform estimates (2)–(7), not on numerical extrapolation. The big-O constant is not determined numerically.

## Relationship to prior work
Dris's GCD set and its density question were posed in April–August 2020 and studied in a 2022 paper. Aaron Meyerowitz identified the order-three local obstruction and proposed a product argument in August 2020. That obstruction is credited here, not claimed as new. A later proved qualitative theorem establishes that, for each fixed \(T\), the ratio \(R(n)\) exceeds \(T\) outside a zero-density set; a separate theorem establishes that the equality set has density zero. Neither statement specifies a convergence rate.

The new quantitative implication (1) requires **simultaneously uniform** control of witness counts for a growing collection of primes \(p\le(\log\log X)^{1/3}\). Turán–Kubilius and Siegel–Walfisz provide that control; CRT and progression-Mertens then yield the stated triple-logarithmic bound. The result is not implied quantitatively by either qualitative theorem, nor by the complementary published lower bound of order \(X/\sqrt{\log X}\) for a restricted subfamily of the equality set.

## Limitations
The bound is slow and not claimed optimal. Its constant depends on fixed \(T\) and may be ineffective because of the Siegel–Walfisz input; the statement is asymptotic and does **not** supply a usable numerical threshold for given \(X\). Nothing is asserted when \(T\) grows with \(X\), nor is an exact order of magnitude for the equality set established. The local obstruction and qualitative density-zero results predate this calculation. A complete bibliographic priority guarantee and independent scientific audit are not available.

## References
1. Jose Arnaldo Bebita Dris, “What is the asymptotic density of positive integers \(n\) satisfying \(\gcd(n,\sigma(n^2))=\gcd(n^2,\sigma(n^2))\)?”, *Mathematics Stack Exchange*, question 3629818, first posted 17 April 2020. https://math.stackexchange.com/q/3629818
2. Jose Arnaldo Bebita Dris, question, and Aaron Meyerowitz, answer, “Is the asymptotic density ... equal to zero?”, *MathOverflow*, question 369441, 18–19 August 2020. https://mathoverflow.net/q/369441
3. Jose Arnaldo Bebita Dris, “A new approach to odd perfect numbers via GCDs,” arXiv:2202.08116v1, posted 10 February 2022, Section 5, Conjecture 5.1 and Remark 5.1. https://arxiv.org/abs/2202.08116
4. Published mathematical notes, “A squarefree \(2\bmod3\) subfamily in Dris's GCD set,” and “A density-one divergence theorem for the GCD ratio,” whose conclusions are respectively a lower bound on the equality set and qualitative divergence of \(R(n)\).
5. G. Tenenbaum, *Introduction to Analytic and Probabilistic Number Theory*, statement of the Turán–Kubilius inequality for additive functions; classical Siegel–Walfisz theorem and Mertens theorem for primes in arithmetic progressions.

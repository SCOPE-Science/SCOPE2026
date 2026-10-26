# A negative zero disproves the unitary-Euler reciprocal-coefficient conjecture

## Finding

Let
\[
S(z)=1+\sum_{n=1}^{\infty}\frac{z^n}{2^n-1},\qquad
\frac{1}{S(z)}=\sum_{n=0}^{\infty}b_n z^n
\]
where the latter series is the Taylor expansion at \(z=0\). The function \(S\) has exactly one **negative real zero** in its disk of convergence \(|z|<2\). This zero is simple and equals \(-\alpha\), where
\[
1<\alpha<\frac32.
\]
Consequently, the reciprocal Taylor series has radius of convergence \(R\) satisfying \(0<R\le\alpha<3/2\), and
\[
\limsup_{n\to\infty}|b_n|^{1/n}=\frac1R>\frac23.
\]
In particular, the proposed bound \(b_n=O(2^{-n})\) is false. This resolves the **coefficient conjecture negatively** in Tóth's original preprint, Open Problem 41, and the published article, Open Problem 44.

## Assumptions and scope

The sums and the reciprocal use ordinary complex Taylor series; no restriction on the index \(n\) is imposed except \(n\ge1\) in the definition of \(S\). The radius of the defining series for \(S\) is \(2\), because \((2^n-1)^{-1/n}\to1/2\). The reciprocal has a well-defined analytic germ at zero since \(S(0)=1\). "Unique" refers only to **negative real zeros**; no assertion is made that \(-\alpha\) is the unique complex zero or the nearest complex zero to the origin.

The motivating arithmetic function is the unitary Euler totient \(\varphi^*\), with \(\varphi^*(p^n)=p^n-1\) at prime powers; thus \(S\) is the reciprocal unitary-Euler Bell series at the prime \(2\), exactly as defined by Tóth.

## Proof

**1. Lambert-series identity.** For every \(|z|<2\), absolute convergence of the double series and the geometric-series identity yield
\[
\begin{aligned}
S(z)&=1+\sum_{n\ge1}z^n\sum_{j\ge1}2^{-jn}\\
&=1+\sum_{j\ge1}\frac{z}{2^j-z}.
\end{aligned}
\]
The interchange is valid since
\(\sum_{j\ge1}\sum_{n\ge1}(|z|/2^j)^n<\infty\) for \(|z|<2\).

**2. A unique simple negative zero.** For real \(x\in(0,2)\), write
\[
S(-x)=1-F(x),\qquad F(x)=\sum_{j\ge1}\frac{x}{2^j+x}.
\]
Each summand is strictly increasing in \(x\), and the series converges locally uniformly. Thus \(F\) is continuous and strictly increasing. Moreover
\[
F(1)=\sum_{j\ge1}\frac1{2^j+1}<\sum_{j\ge1}2^{-j}=1.
\]
On the other hand, using only six exact terms,
\[
F\!\left(\frac32\right)
>\sum_{j=1}^{6}\frac{3}{2^{j+1}+3}
=\frac{65011734}{64203755}>1.
\]
The intermediate-value theorem and strict monotonicity give exactly one \(\alpha\in(1,3/2)\) with \(S(-\alpha)=0\). Termwise differentiation is valid on compact subsets of \(|z|<2\); at that zero,
\[
S'(-\alpha)=\sum_{j\ge1}\frac{2^j}{(2^j+\alpha)^2}>0,
\]
so the zero is simple.

**3. The reciprocal coefficient obstruction.** Since \(S\) has a simple zero at \(-\alpha\), its reciprocal has a genuine simple pole there. Hence the radius \(R\) of the Taylor expansion of \(1/S\) at zero is at most \(\alpha\), strictly less than \(3/2\). Cauchy–Hadamard gives \(\limsup_{n\to\infty}|b_n|^{1/n}=1/R>2/3\). If instead \(b_n=O(2^{-n})\), the root test would force \(R\ge2\), a contradiction. This proves the claim.

## Verification

The standalone `verify.py` reproduces the six-term rational identity using `fractions.Fraction`, verifies the independent alternating Taylor partial sum at \(z=-3/2\), and reconstructs the first four published reciprocal coefficients by exact formal-series inversion. Run:

```text
python3 verify.py
```

The finite exact sums are certificates for strict inequalities; the unrestricted zero and coefficient assertions follow from the analytic steps proved above, not from a numerical root search. The decisive certificate is
\[
\sum_{j=1}^{6}\frac{3}{2^{j+1}+3}-1
=\frac{807979}{64203755}>0.
\]

## Relationship to prior work

László Tóth's preprint (first public version dated 2016-08-02), Section 4.10, poses \(b_n\ll2^{-n}\) as Open Problem 41. The 2017 *Journal of Integer Sequences* article repeats the conjecture as Open Problem 44 and lists \(b_0=1\), \(b_1=-1\), \(b_2=2/3\), \(b_3=-10/21\), and \(b_4=104/315\), but does not establish the decay claim or a negative zero. The result here shows the proposed coefficient bound is impossible.

Zurita's 2020 study of generalized alternating sums obtains results for the unitary Euler function, including its direct Bell series and the separate reciprocal-sum problem, but the inspected Section 4.5 does not determine the zeros of the \(1/\varphi^*\) Bell series \(S\) or its reciprocal coefficient radius. Zurita's statement about solving a problem numbered 41 concerns a different sum-of-unitary-divisors result in the later numbering of Tóth's article. The Erdős–Borwein constant (OEIS A065442) describes \(S(1)-1\) and does not imply the location of a negative zero.

## Limitations

The exact value of \(\alpha\), its dominance among all **complex** zeros, and a full asymptotic formula for \(b_n\) are not established. The proof refutes the specific coefficient estimate; it **does not** refute any improved error term for the underlying arithmetic alternating sum, since a different method might yield such an error bound. Priority relative to uncatalogued previous treatments of this Lambert-series zero remains a literature risk. Independent mathematical audit has not been performed.

## References

1. L. Tóth, *Alternating sums concerning multiplicative arithmetic functions*, arXiv:1608.00795v1, 2016-08-02, Section 4.10, Open Problem 41. https://arxiv.org/pdf/1608.00795v1
2. L. Tóth, *Alternating Sums Concerning Multiplicative Arithmetic Functions*, *Journal of Integer Sequences* **20** (2017), Article 17.2.1, Section 4.10, Open Problem 44. https://cs.uwaterloo.ca/journals/JIS/VOL20/Toth/toth25.pdf
3. R. Zurita, *Generalized Alternating Sums of Multiplicative Arithmetic Functions*, *Journal of Integer Sequences* **23** (2020), Article 20.10.4, Section 4.5. https://cs.uwaterloo.ca/journals/JIS/VOL23/Zurita/zur3.pdf
4. OEIS A065442, *Decimal expansion of Erdős–Borwein constant*. https://oeis.org/A065442

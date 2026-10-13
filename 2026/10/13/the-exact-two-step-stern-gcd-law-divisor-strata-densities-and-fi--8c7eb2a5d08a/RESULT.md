# The exact two-step Stern gcd law: divisor strata, densities, and first occurrences

## Finding
Let \(s\) be Stern's diatomic sequence and put \(g(n)=\gcd(s(n),s(n+2))\). The next-nearest-neighbor gcd has an exact arithmetic classification by \(v_2(n+1)\), a sharp first-occurrence function, and an explicit discrete limiting distribution.

For odd \(n\ge1\), uniquely write \(n+1=2^r(2j+1)\) with \(r\ge1\) and \(j\ge0\). Then
\[
g(n)=\gcd\bigl(2r+1,\,s(j)-s(j+1)\bigr).
\]
For even \(n\), one has \(g(n)=1\). Consequently, at every fixed \(r\ge1\), the exact set of values on the stratum \(v_2(n+1)=r\) comprises **all and only the positive divisors of \(2r+1\)**.

For every odd integer \(d\ge3\), the first occurrence is precisely
\[
\min\{n\ge1:g(n)=d\}=3\cdot2^{(d-1)/2}-1.
\]
In particular, for every integer \(X\ge5\),
\[
\max_{1\le n\le X}g(n)
 =2\left\lfloor\log_2\frac{X+1}{3}\right\rfloor+1,
\]
while the maximum equals \(1\) for \(1\le X\le4\).

There is also an exact limiting law. For \(m=2r+1\), a divisor \(d\mid m\), and a prime power \(p^e\parallel m\), define
\[
\lambda_{p,e}(t)=
\begin{cases}
\dfrac{p}{p+1},&t=0,\\[3pt]
\dfrac{p-1}{(p+1)p^t},&1\le t<e,\\[3pt]
\dfrac{1}{(p+1)p^{e-1}},&t=e.
\end{cases}
\]
Put \(P_m(d)=\prod_{p^e\parallel m}\lambda_{p,e}(v_p(d))\), and \(P_m(d)=0\) if \(d\nmid m\). For fixed \(r\) and \(d\mid 2r+1\),
\[
\lim_{X\to\infty}
\frac{\#\{1\le n\le X:v_2(n+1)=r,\ g(n)=d\}}
 {\#\{1\le n\le X:v_2(n+1)=r\}}
=P_{2r+1}(d)>0.
\]
For each positive odd integer \(d\), the natural density among all positive \(n\) exists and equals
\[
\rho(d)=\frac12\mathbf 1_{d=1}+
\sum_{\substack{r\ge1\\d\mid2r+1}}
 2^{-r-1}P_{2r+1}(d)>0.
\]
Every even gcd value is impossible. The series converges absolutely and determines a probability distribution on the positive odd integers.

## Assumptions and scope
The sequence is indexed from zero and defined for all nonnegative integers by
\[
s(0)=0,\quad s(1)=1,\quad s(2n)=s(n),\quad
s(2n+1)=s(n)+s(n+1).
\]
All gcds are nonnegative, so \(\gcd(a,0)=|a|\). The variable \(X\) in limiting density statements is real and tends to positive infinity, with positive integer indices counted. \(v_p\) is the usual prime-adic valuation, and \(p^e\parallel m\) means exactly \(v_p(m)=e\). For density, \(r\) and \(d\) are fixed before \(X\to\infty\); no error bound uniform in unbounded \(r\) or \(d\) is asserted.

## Proof
**Adjacent coprimality.** The recurrence implies \(\gcd(s(j),s(j+1))=1\) for all \(j\ge0\): the two successive pairs at even and odd indices are \((s(j),s(j)+s(j+1))\) and \((s(j)+s(j+1),s(j+1))\), respectively. Each preserves the parent gcd, and the initial pair is \((0,1)\). If \(n\) is even, \(g(n)=\gcd(s(n/2),s(n/2+1))=1\).

**Exact two-step reduction.** Let \(n+1=2^r M\), \(M=2j+1\), and set \(a=s(j)\), \(b=s(j+1)\). Then \(s(M-1)=a\), \(s(M)=a+b\), \(s(M+1)=b\). Since \(s(2^rM)=a+b\) and repeatedly applying the odd recurrence increments each flanking term by \(a+b\), induction on \(r\) gives
\[
s(2^rM-1)=(r+1)a+rb,\qquad
s(2^rM+1)=ra+(r+1)b.
\]
Subtracting these two expressions gives \(a-b\). As \(\gcd(a,b)=1\), one obtains
\[
\begin{aligned}
g(n)&=\gcd(a-b,(r+1)a+rb)\\
&=\gcd(a-b,(2r+1)b)\\
&=\gcd(a-b,2r+1).
\end{aligned}
\]
This also proves that the gcd is odd and divides \(2r+1\).

**Complete strata and first occurrences.** Given any divisor \(d\mid2r+1\), choose \(j=2^{d+1}-1\). Direct induction on the defining recurrence gives \(s(2^k-1)=k\) and \(s(2^k)=1\) for \(k\ge1\). Thus \((a,b)=(d+1,1)\), and the preceding formula gives \(g(n)=\gcd(d,2r+1)=d\), proving the complete stratum spectrum. To attain \(d\ge3\), one must have \(r\ge(d-1)/2\). The choice \(j=0\) yields \((a,b)=(0,1)\) and \(g(n)=1\), so \(j\ge1\) and \(n\ge3\cdot2^r-1\). Equality is realized at \(r=(d-1)/2\), \(j=1\), for which \(a=b=1\), giving \(g(n)=2r+1=d\). This proves the exact first occurrence and, by maximizing permissible \(r\), the stated record formula.

**Conditional density.** Bruce Reznick's theorem on Stern pairs modulo a fixed integer (Theorem 4.7 of arXiv:math/0610601v1) says that \((s(j),s(j+1))\) is asymptotically equidistributed on the residue pairs \((a,b)\pmod m\) with \(\gcd(a,b,m)=1\). For a prime power \(p^e\parallel m\), the proportion of such primitive pairs with \(a-b\equiv0\pmod{p^t}\), \(1\le t\le e\), equals
\[
\frac{p^{2e-t}(1-1/p)}{p^{2e}(1-1/p^2)}
=\frac{p^{1-t}}{p+1}.
\]
Subtract successive tail probabilities to get \(\lambda_{p,e}(t)\) for \(0\le t\le e\). The Chinese remainder theorem makes the local conditions independent across the prime powers dividing \(m\), giving \(P_m(d)\). Replacing \(j\) by \(n=2^r(2j+1)-1\) gives the claimed conditional limit and shows each divisor has positive frequency.

**Global density.** For each fixed \(r\ge1\), its index stratum has natural density \(2^{-r-1}\); even \(n\) have density \(1/2\) and gcd \(1\). For any fixed cutoff \(R\), summing the finitely many stratum limits gives the corresponding truncated expression for \(\rho(d)\). The omitted strata have upper density at most \(2^{-R-1}\), independently of \(d\); letting \(R\to\infty\) proves existence and the absolutely convergent formula. Positivity follows by taking \(r=(d-1)/2\) for odd \(d\ge3\) and from even indices for \(d=1\). Summing probabilities over \(d\) gives total mass one by the same tail bound.

## Verification
The included `verify.py` uses only exact Python integer arithmetic and rational fractions. Running `python verify.py` checks the two-step identity independently for the first 249,999 positive indices; the complete divisor spectrum for 15 valuation strata; the first occurrences of every odd gcd up to 31; and the local probability formulas by exhaustive enumeration of primitive residue pairs for nine moduli (through 45). The observed output is:

`EXACT_CERTIFICATE_OK pointwise_n=249999 valuation_strata=15 first_occurrences_through=31 finite_residue_moduli=9`

These finite computations are consistency checks. The infinite statements rely on the preceding symbolic arguments and the published equidistribution theorem, not numerical extrapolation.

## Relationship to prior work
Stern's classical result establishes neighboring coprimality, but does not classify gcds at separation two. Reznick (2006), Section 2, gives the dyadic interpolation identity, and Section 4, Theorem 4.7, proves equidistribution for consecutive pairs modulo fixed integers. Those are the necessary pre-existing ingredients. The two-step valuation reduction, complete divisor-stratum spectrum, sharp first-occurrence/record envelope, and resulting explicit gcd distribution are not statements found in those inspected results. Allouche (2012) recalls Reznick's identity and derives Coons's additive correlation formula; the latter concerns a sum of Stern values rather than the gcd statistic. OEIS A002487 contains the base sequence and many identities, not an identified record of this complete two-step gcd theorem.

## Limitations
The distribution result depends on Reznick's published equidistribution theorem; this is not independently reproved here. The claim does not give a uniform convergence rate across all gcd values. Prior formulations of the theorem may be unindexed, and the full original Coons correlation paper was not available for complete page-by-page comparison; its stated theorem is additive and does not directly imply the stated gcd classification.

## References
1. B. Reznick, *Regularity properties of the Stern enumeration of the rationals*, first arXiv version dated 2006-10-19, arXiv:math/0610601v1, especially Sections 2 and 4; https://arxiv.org/pdf/math/0610601.
2. J.-P. Allouche, *On the Stern sequence and its twisted version*, arXiv:1202.4171, 2012; https://arxiv.org/pdf/1202.4171.
3. M. Coons, *A correlation identity for Stern's sequence*, Integers **12** (2012), A3; https://www.kurims.kyoto-u.ac.jp/EMIS/journals/INTEGERS/papers/m3/m3.pdf.
4. OEIS Foundation, sequence A002487, *Stern's diatomic series*; https://oeis.org/A002487.

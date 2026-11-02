# The exact first nondivisibility index for the triple-binomial family

## Finding

For positive integers \(b,n\) consider the divisibility
\[
 bn+1\mid \binom{(b+3)n}{3n}.
\]
Following the first-nondivisibility-index convention, let \(f(3,b)=0\) if the relation holds for all positive \(n\), and otherwise let \(f(3,b)\) be the smallest positive \(n\) at which it fails. Then, for every positive integer \(b\),
\[
\boxed{f(3,b)=\begin{cases}
0,&b\equiv0\pmod3,\\
1,&b\equiv2\pmod3,\\
\dfrac{3^{\nu_3(b+2)}+1}{2},&b\equiv1\pmod3.
\end{cases}}
\]
In particular, \(f(3,3^s-2)=(3^s+1)/2\) for every integer \(s\ge1\). The first-failure threshold is consequently unbounded as \(b\) varies, even though the first parameter is fixed at three.

## Assumptions and scope

Here \(b\ge1\) and \(n\ge1\) are integers; \(\nu_3(m)\) is the exponent of three dividing a nonzero integer \(m\). Divisibility always refers to ordinary integers. The result is an exact classification of the earliest failure; it does not classify every subsequent index at which failure occurs. The case \(3\mid b\) means absence of failures, not a failure at zero.

## Proof

**1. A cyclic divisibility lemma.** Put \(N=(b+3)n\), \(K=3n-1\), \(m=bn+1\), and \(B=\binom{N}{K}\). Regard the \(N\) positions as \(n\) consecutive blocks of \(b+3\) positions. Cyclic rotation through whole blocks is an action of the group \(C_n\) on the \(K\)-subsets of these positions. If a subset were fixed by a nonidentity rotation, its stabilizer would have some order \(d>1\) dividing \(n\). The stabilizer acts freely on individual positions (each stabilizer orbit has size \(d\)), so \(d\) would divide \(K=3n-1\). But \(\gcd(3n-1,n)=1\). Thus the action on the \(K\)-subsets is free, and therefore
\[
 n\mid B. \tag{1}
\]
The standard adjacent-binomial identity gives the exact rational equality
\[
 \frac{1}{bn+1}\binom{(b+3)n}{3n}
 =\frac{1}{3n}\binom{(b+3)n}{3n-1}=\frac{B}{3n}.\tag{2}
\]
Hence the original divisibility holds precisely when \(3n\mid B\).

**2. All indices with \(3\nmid bn+1\) succeed.** Put \(t=\nu_3(n)\). The base-three expansion of \(K=3n-1\) has digit two at positions \(0,1,\ldots,t\), since \(3^{t+1}\mid3n\). The lowest \(t\) digits of \(m=bn+1\) are a units digit one followed by zeros; when \(t=0\), the units digit of \(m\) is one or two because \(3\nmid m\). Adding \(K+m=N\) in base three therefore creates a carry at position zero and propagates a carry through each position up to \(t\), regardless of the higher digits of \(m\). (If \(t=0\), the units-digit sum is at least three.) Kummer's carry theorem yields
\[
 \nu_3(B)\ge t+1=\nu_3(n)+1.
\]
Together with (1), this implies \(3n\mid B\), so no failures occur when \(3\nmid bn+1\).

**3. Failure reduces to a Lucas digit test.** If \(3\mid bn+1\), then \(3\nmid n\). By (1), \(n\mid B\), and consequently \(3n\mid B\) if and only if \(3\mid B\). By Lucas's theorem,
\[
 3\nmid B \quad\Longleftrightarrow\quad
 \text{every base-three digit of }3n-1\text{ is at most the corresponding digit of }(b+3)n.
 \tag{3}
\]
If \(3\mid b\), then \(bn+1\equiv1\pmod3\) for all \(n\), giving \(f(3,b)=0\). If \(b\equiv2\pmod3\), choose \(n=1\). Now \(N=b+3\equiv2\pmod3\) and \(K=2\), hence \(B=\binom{b+3}{2}\equiv1\pmod3\) by Lucas's theorem; by (2) the first index fails, giving \(f(3,b)=1\).

**4. The exact threshold when \(b\equiv1\pmod3\).** Write
\[
 b+2=3^s h,\qquad s=\nu_3(b+2)\ge1,\qquad3\nmid h.
\]
An index can fail only if \(bn+1\equiv0\pmod3\), equivalently \(n\equiv2\pmod3\). For such an index let \(n=\sum_{j\ge0}d_j3^j\), with \(d_0=2\) and all \(d_j\in\{0,1,2\}\). Because
\[
 N=(b+3)n=n+3^s hn,
\]
its digits at positions \(0,\dots,s-1\) coincide with those of \(n\). The digits of \(K=3n-1\) are
\[
 k_0=2,\qquad k_1=d_0-1=1,\qquad k_j=d_{j-1}\quad(j\ge2).
\]
If (3) holds, comparison at positions \(1,\ldots,s-1\) forces \(d_1\ge1\) and \(d_j\ge d_{j-1}\ge1\) for every \(2\le j<s\). Thus every failing \(n\) satisfies
\[
 n\ge 2+\sum_{j=1}^{s-1}3^j=\frac{3^s+1}{2}=:n_*.\tag{4}
\]
At this bound, the base-three digits of \(n_*\) are two in the units place and one at each of the positions \(1,\ldots,s-1\), with all higher digits zero. Therefore \(K_*=3n_*-1\) has digit two at position zero and digit one at each position \(1,\ldots,s\), with all higher digits zero. In \(N_*=n_*+3^shn_*\), the lowest \(s\) digits coincide with those of \(n_*\), while the digit at position \(s\) is \(hn_*\bmod3\), which is either one or two because \(3\nmid hn_*\). Thus every digit of \(K_*\) is at most the corresponding digit of \(N_*\). Equation (3) shows \(3\nmid B_*\), hence by (2) this index fails. The lower bound (4) and this witness prove \(f(3,b)=n_*\). This proves every case.

## Verification

The accompanying standalone Python script `verify_f3.py` performs exact-integer binomial divisibility checks without using the proof's Lucas digit criterion. It checked 4,276 relevant \((b,n)\) configurations for \(1\le b\le150\), including the stated first failure and every preceding index within the tested range. Additional exact tests verify the first failure for \(b=3^s-2\), for \(1\le s\le6\). Output: `VERIFY_OK b_range=1..150 exact_divisibility_tests=4276 higher_depth_witnesses=6`. These finite checks are corroboration, not a proof of the universally quantified result.

## Relationship to prior work

Zhi-Wei Sun [1] introduced the least nondivisibility index \(f(a,b)\), proved that \((bn+1)/\gcd(a,bn+1)\) always divides the relevant binomial coefficient, and tabulated examples for other parameter pairs. Guo and Krattenthaler [2, Theorem 2.1] proved the conjectured infinite occurrence of failed divisibilities when a prime dividing \(a\) does not divide \(b\), and supplied a general, much larger upper bound for the least failure. Their stated results neither provide nor imply the exact threshold as a function of \(\nu_3(b+2)\) with \(a=3\). The present result uses familiar Kummer/Lucas tools to determine the sharp first failure, including its unbounded growth, in this complete natural parameter family.

## Limitations

The theorem addresses only the first-parameter value three and determines the smallest failing index, not the full set of failures or any parameter \(a\ne3\). Mathematical originality is qualified by the possibility of an unlocated equivalent classical identity or more general published formula; searching cannot establish uniqueness. Independent validation has not been performed.

## References

[1] Zhi-Wei Sun, *On divisibility of binomial coefficients*, Journal of the Australian Mathematical Society 93 (2012), 189–201, DOI: 10.1017/S1446788712000171 (first public online 2012-09-19), especially Theorem 1.1 and the definition of \(f\) on p. 190.

[2] Victor J. W. Guo and C. Krattenthaler, *Some divisibility properties of binomial and q-binomial coefficients*, arXiv:1301.7651 (first submitted 2013-01-31), especially Theorem 2.1 and the Lucas-theorem argument of Section 4.

# Strict likelihood-ratio ordering with paired plateaus for Pólya-urn total runs

## Finding

For every \(n\ge2\) and every pair \(0<\alpha_1<\alpha_2\), let \(f_\alpha(r)=\Pr_\alpha(R_n=r)\) be the distribution of the total number of runs in a symmetric two-color Pólya urn with unit reinforcement. Then every \(f_\alpha(r)\) is positive, and

\[
\frac{f_{\alpha_2}(r+1)}{f_{\alpha_1}(r+1)}\ge
\frac{f_{\alpha_2}(r)}{f_{\alpha_1}(r)},\qquad 1\le r<n.
\]

Equality holds **if and only if** \(r=2s\) is even; in particular the likelihood ratios have the exact pattern

\[
\frac{f_{\alpha_2}(1)}{f_{\alpha_1}(1)}
<\frac{f_{\alpha_2}(2)}{f_{\alpha_1}(2)}
=\frac{f_{\alpha_2}(3)}{f_{\alpha_1}(3)}
<\frac{f_{\alpha_2}(4)}{f_{\alpha_1}(4)}
=\frac{f_{\alpha_2}(5)}{f_{\alpha_1}(5)}<\cdots,
\]

truncated to the available values \(1,\ldots,n\). Therefore increasing the initial concentration makes the entire run-count distribution strictly larger in stochastic order; more strongly, it increases in likelihood-ratio order with completely classified equality steps.

The plateau identity is universal: **for any exchangeable law on binary words** of length \(n\),

\[
\Pr(R_n=2s+1)=\frac{n-2s}{2s}\Pr(R_n=2s),
\qquad 1\le s,\ 2s+1\le n.
\]

## Assumptions and scope

Fix an integer \(n\ge2\) and a real concentration \(\alpha>0\). Start with masses \(\alpha\) of each of two colors. At each step choose a color proportionally to its current mass and add one mass unit of that color; write its color as \(X_i\in\{0,1\}\). This is also the de Finetti mixture obtained by first drawing \(P\sim\mathrm{Beta}(\alpha,\alpha)\) and then sampling \(X_1,\ldots,X_n\) independently conditional on \(P\), each with success probability \(P\). Let \(K=\sum_i X_i\), \(B=\min(K,n-K)\), \(h=\lfloor n/2\rfloor\), and \(R_n=1+\sum_{i=1}^{n-1}\mathbf1_{\{X_i\ne X_{i+1}\}}\). A run is a maximal constant-color block; runs of **both** colors are counted. For nonnegative integers \(a,k\), define \(\binom ak=0\) if \(k>a\), and \((z)_{\overline k}=\prod_{j=0}^{k-1}(z+j)\), with empty product one.

The strict claims assume \(\alpha_1<\alpha_2\) and \(n\ge2\). No integer restriction is imposed on \(\alpha\). In the additional exchangeability identity, no Pólya or beta-mixture assumption is made. The boundary \(n=1\) is excluded from strict ordering because there is only one possible run count.

## Proof

**Step 1: conditional run counts.** Conditional on \(K=k\), all \(\binom nk\) words are equiprobable. For \(1\le k\le n-1\) and \(s\ge1\), the counts \(N_{n,k}(r)\) of words with precisely \(k\) ones and \(r\) total runs are

\[
N_{n,k}(2s)=2\binom{k-1}{s-1}\binom{n-k-1}{s-1},
\]

\[
N_{n,k}(2s+1)=\frac{n-2s}{s}\binom{k-1}{s-1}\binom{n-k-1}{s-1}.
\]

For the first equation, each color occupies \(s\) positive-length blocks, and there are two choices of first color. For the second, one color occupies \(s+1\) blocks and the other occupies \(s\); the sum of the two compositions is

\[
\binom{k-1}{s}\binom{n-k-1}{s-1}
+\binom{k-1}{s-1}\binom{n-k-1}{s}
=\frac{n-2s}{s}\binom{k-1}{s-1}\binom{n-k-1}{s-1}.
\]

When \(k=0\) or \(k=n\), only \(R_n=1\) occurs. In every exchangeable binary law, words with the same \(k\) have equal probability; the displayed counts consequently prove the universal paired-runs identity after mixing over \(k\).

**Step 2: a totally positive conditional kernel.** Since exchanging colors leaves \(R_n\) unchanged, write \(g_b(r)=\Pr(R_n=r\mid B=b)=N_{n,b}(r)/\binom nb\). For \(b=0\), this is point mass at \(r=1\). For \(1\le b<h\), on positive common support the ratio between successive rows at even and following odd indices has the same value,

\[
\frac{g_{b+1}(2s)}{g_b(2s)}=
\frac{g_{b+1}(2s+1)}{g_b(2s+1)}
=\frac{b+1}{n-b}\frac{b}{b-s+1}\frac{n-b-s}{n-b-1}.
\]

The only \(s\)-dependent factor is \((n-b-s)/(b-s+1)\). It increases strictly with \(s\) wherever both numerator and denominator are positive, since \(n-2b-1>0\). Moreover, the row with index \(b+1\) has all the run counts of row \(b\) in its support, and possibly additional larger counts. Consequently the kernel \((g_b(r))_{0\le b\le h,\,1\le r\le n}\) is **TP2**: for \(b<c\) and \(r<t\),

\[
g_b(r)g_c(t)-g_b(t)g_c(r)\ge0.
\]

To see the boundary cases, \(g_0\) is concentrated at the smallest run count, and the maximal run count in row \(b\) is \(\min(2b+1,n)\). Chaining adjacent-row likelihood-ratio comparisons proves the displayed determinant inequality for every \(b<c\).

**Step 3: a strictly TP2 concentration family.** The folded composition law is

\[
w_\alpha(b)=\Pr_\alpha(B=b)
=m_b\binom nb\frac{(\alpha)_{\overline b}(\alpha)_{\overline{n-b}}}{(2\alpha)_{\overline n}},
\]

where \(m_b=2\) for \(b<n/2\) and \(m_b=1\) otherwise. Thus for \(0\le b<h\),

\[
\frac{w_\alpha(b+1)}{w_\alpha(b)}
=\frac{m_{b+1}}{m_b}\frac{n-b}{b+1}\frac{\alpha+b}{\alpha+n-b-1}.
\]

The right-hand side increases **strictly** with \(\alpha\), because \(n-b-1>b\) when \(b<h\). Hence for \(\alpha_1<\alpha_2\) and \(b<c\),

\[
w_{\alpha_1}(b)w_{\alpha_2}(c)>
 w_{\alpha_1}(c)w_{\alpha_2}(b).
\]

**Step 4: mixture and the sharp equality classification.** We have \(f_\alpha(r)=\sum_{b=0}^h w_\alpha(b)g_b(r)\). For \(r<t\), expand the two-by-two determinant:

\[
\begin{aligned}
&f_{\alpha_1}(r)f_{\alpha_2}(t)
-f_{\alpha_1}(t)f_{\alpha_2}(r)\\
&=\sum_{0\le b<c\le h}
\bigl[w_{\alpha_1}(b)w_{\alpha_2}(c)
-w_{\alpha_1}(c)w_{\alpha_2}(b)\bigr]
\bigl[g_b(r)g_c(t)-g_b(t)g_c(r)\bigr]\ge0.
\end{aligned}
\]

Every term is nonnegative, proving likelihood-ratio order. For \(r=2s\), the paired-runs identity implies \(g_b(2s+1)=\frac{n-2s}{2s}g_b(2s)\) for every \(b\); hence the whole determinant is exactly zero. For \(r=1\) choose \(b=0,c=1\); for \(r=2s+1<n\) choose \(b=s,c=s+1\). The lower row supports \(r\) but not \(r+1\), while the upper row supports \(r+1\); thus at least one summand is strictly positive. This proves **strictness at precisely the other adjacent steps**. Positivity of all \(f_\alpha(r)\) follows because every binary word has positive Pólya probability.

Stochastic monotonicity is a standard consequence of likelihood-ratio order. Directly, the adjacent transitions satisfy

\[
\Pr_\alpha(X_i\ne X_{i+1})=\frac{\alpha}{2\alpha+1},\qquad
\mathbb E_\alpha R_n=1+\frac{(n-1)\alpha}{2\alpha+1}.
\]

The mean increases strictly with \(\alpha\), consistent with the stronger distributional theorem.

## Verification

The accompanying standalone `verify_polya_runs.py` uses only the Python standard library and exact rational arithmetic. It independently enumerates every binary word through length 11 and compares the folded run-count multiplicities, checks 2-by-2 minors of the conditional kernel through length 35, and compares six concentration parameters across lengths 2 through 28, including strict/equal adjacent likelihood-ratio steps and exact means. Running `python3 verify_polya_runs.py` yields `Exact checks passed: 11202`. This is finite corroboration; the all-size proof is in Steps 1–4.

## Relationship to prior work

The Wald–Wolfowitz and Mood run-count laws condition on the observed two-color composition. Makri, Philippou and Psillakis analyze run statistics for the Pólya–Eggenberger scheme, including the number of success runs of fixed or minimum length; their distributional formulas are a source of motivation, not claimed as new here. Eryilmaz develops joint success/failure run-statistic distributions for multicolor Pólya urns; the inspected definitions and exact distribution results do not directly state the **likelihood-ratio comparison over every concentration parameter** nor its exact adjacent equality pattern. Classical total-positivity composition is a tool in this proof; no novelty is claimed for that general principle. The result identifies a specific ordered family with a nontrivial alternating pattern of strict and equal likelihood-ratio steps, rather than merely a moment inequality.

## Limitations

The strict likelihood-ratio theorem concerns the **symmetric two-color** Pólya law with positive real concentration and fixed \(n\), not asymmetric initial masses, more than two colors, or arbitrary reinforcement. The universal paired-runs identity extends to every exchangeable binary law, but likelihood-ratio ordering does not follow for arbitrary families of such laws. Exact finite run distributions and broader total-positivity theorems in classical literature might contain implicit equivalent formulations; independent priority verification has not been performed. No claims about joint dependence of run lengths, waiting times, or conditional run tests are made.

## References

1. A. M. Mood, *The distribution theory of runs*, Ann. Math. Statist. 11 (1940), 367–392.
2. E. F. Schuster, *Distribution theory of runs via exchangeable random variables*, Statistics & Probability Letters 11 (1991), 379–386. DOI: `10.1016/0167-7152(91)90185-T`.
3. F. S. Makri, A. N. Philippou and Z. M. Psillakis, *Pólya, inverse Pólya, and circular Pólya distributions of order k for l-overlapping success runs*, Communications in Statistics—Theory and Methods 36 (2007), 657–668. DOI: `10.1080/03610920601033942`. First published online 2007-03-22.
4. F. S. Makri, A. N. Philippou and Z. M. Psillakis, *Success run statistics defined on an urn model*, Advances in Applied Probability 39 (2007), 991–1019. DOI: `10.1239/aap/1198177236`. Primary MSC 60C05.
5. S. Eryilmaz, *Run statistics defined on the multicolor urn model*, Journal of Applied Probability 45 (2008), 1007–1023. DOI: `10.1239/jap/1231340230`.

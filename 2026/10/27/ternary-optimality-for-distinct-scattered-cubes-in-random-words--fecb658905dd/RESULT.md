# Ternary optimality for distinct scattered cubes in random words

## Finding

Let \(\Sigma\) be a finite alphabet with \(q\ge 2\) symbols. Let \(W_n\) be an independent and identically distributed random word of length \(n\), with \(\Pr(W_n[i]=a)=p_a>0\) and \(\sum_{a\in\Sigma}p_a=1\). A word \(v\) is a *scattered subsequence* of \(w\) when it occurs at strictly increasing positions; repeated positional occurrences of the same \(v\) count only once. Define

\[
C_n(W_n)=\#\{u\in\Sigma^+:u^3=uuu\text{ occurs as a scattered subsequence of }W_n\}.
\]

Write

\[
g_a(z)=\frac{p_az}{1-(1-p_a)z},\qquad T(z)=\sum_{a\in\Sigma}g_a(z)^3.
\]

Then, for every such probability vector, the ordinary generating function is exactly

\[
\boxed{\sum_{n\ge0}\mathbb E[C_n(W_n)]z^n=\frac{T(z)}{(1-z)(1-T(z))}.}
\]

There is a unique \(r\in(0,1)\) satisfying \(T(r)=1\). For the fixed alphabet and fixed positive probability vector,

\[
\boxed{\mathbb E[C_n(W_n)]\sim\frac{r^{-n}}{(1-r)rT'(r)}.}
\]

Across **all** finite alphabet sizes and **all** positive source distributions, the exponential growth rate \(\lambda=1/r\) satisfies the sharp universal inequality

\[
\boxed{\lambda\le\lambda_*=\frac{2+\sqrt[3]{3}}3.}
\]

Equality holds **if and only if** the alphabet has exactly three symbols, each of probability \(1/3\). In the equality case,

\[
\boxed{\mathbb E[C_n(W_n)]\sim\frac{\sqrt[3]{3}}{3(\sqrt[3]{3}-1)}\left(\frac{2+\sqrt[3]{3}}3\right)^n.}
\]

Thus the optimal mean growth of distinct scattered cubes is supported on **three** equally probable symbols, even when larger source alphabets are allowed.

## Assumptions and scope

A cube means precisely the nonempty string \(u^3\) with the same nonempty root \(u\) repeated three times. It is not required to occur contiguously, and it need not be a cube with primitive root. The count is by **distinct resultant strings**, equivalently by distinct roots, rather than by position triples or embeddings. The ambient alphabet is fixed while \(n\to\infty\); \(q\ge2\) and all \(p_a\) are strictly positive. Exponential-rate equality is asserted across all finite alphabets, not merely for a fixed \(q\). For \(q>3\), distributions concentrating on three letters can approach but do not attain the universal bound when all \(q\) masses must remain positive.

## Proof

**1. Greedy waiting-time identity.** Fix a word \(v=v_1\cdots v_m\). Scan an infinite i.i.d. source greedily to match its letters in order. The waiting time for letter \(v_i\) after the preceding match is geometric on \(\{1,2,\dots\}\) with success probability \(p_{v_i}\). By independence of fresh source letters, the waits are independent. If \(\tau_v\) is their sum, then \(v\) occurs as a scattered subsequence of \(W_n\) exactly when \(\tau_v\le n\). For \(|z|<1\),

\[
\sum_{n\ge0}\Pr(\tau_v\le n)z^n
=\frac{\mathbb E[z^{\tau_v}]}{1-z}
=\frac1{1-z}\prod_{i=1}^m\frac{p_{v_i}z}{1-(1-p_{v_i})z}.
\]

Different nonempty roots produce different cube strings: if \(u^3=v^3\), equality of lengths and then of the first thirds implies \(u=v\). For \(u=u_1\cdots u_\ell\), the waiting-time weight of \(u^3\) is \(\prod_{i=1}^\ell g_{u_i}(z)^3\). Summation over all \(\ell\ge1\) and all roots gives

\[
\sum_{\ell\ge1}\sum_{u\in\Sigma^\ell}\prod_{i=1}^\ell g_{u_i}(z)^3
=\sum_{\ell\ge1}T(z)^\ell=\frac{T(z)}{1-T(z)}.
\]

The claimed expectation generating function follows by linearity of expectation, first as a formal identity in \(z\) and then analytically near the origin.

**2. Exact exponential asymptotics.** Each \(g_a(z)\) has strictly positive Taylor coefficients at every positive degree because \(0<p_a<1\). Hence \(T(z)\) has strictly positive coefficients at every degree \(\ge3\). It is increasing on \([0,1]\), with \(T(0)=0\), \(T(1)=q>1\), so there is exactly one \(r\in(0,1)\) with \(T(r)=1\), and \(T'(r)>0\). For any complex \(z\) with \(|z|=r\) and \(z\ne r\), strict triangle inequality applied to the positive coefficients implies \(|T(z)|<T(r)=1\). Since the displayed generating function is rational, its only singularity on its convergence circle is the simple pole at \(r\). Its leading principal part is

\[
\frac{1}{(1-r)rT'(r)}\frac1{1-z/r}.
\]

All remaining poles have strictly greater modulus, giving the stated asymptotic formula (indeed with an exponentially smaller absolute error).

**3. A three-power equal-support maximization lemma.** For each \(s>0\) and each finite probability vector \(p=(p_1,\dots,p_q)\) with nonnegative coordinates summing to one, put

\[
\Phi_s(p)=\sum_{i=1}^q f_s(p_i),\qquad f_s(x)=\left(\frac{x}{x+s}\right)^3.
\]

**Lemma.** Every global maximizer of \(\Phi_s\) on this simplex has equal positive coordinates. Consequently

\[
\max_p\Phi_s(p)=\max_{1\le m\le q}\frac{m}{(1+ms)^3}.
\]

*Proof of lemma.* Choose a maximizing point and restrict to its positive support. For any two positive coordinates \(x,y\), stationarity under transferring an infinitesimal amount between them requires \(f_s'(x)=f_s'(y)\). Direct differentiation gives

\[
f_s'(x)=\frac{3sx^2}{(x+s)^4},\qquad
f_s''(x)=\frac{6sx(s-x)}{(x+s)^5}.
\]

If \(x\ne y\), the stationarity equation implies \(xy=s^2\): taking positive square roots and cross-multiplying yields \((y-x)(xy-s^2)=0\). Suppose \(x<y\). Thus \(x<s<y\), and substitution of \(xy=s^2\) gives

\[
\frac{f_s''(x)}{-f_s''(y)}=\frac yx>1.
\]

The second derivative of \(f_s(x+t)+f_s(y-t)\) at \(t=0\) is therefore strictly positive. This contradicts local maximality. Hence all positive coordinates at a global maximum are equal, so their common value is \(1/m\) for some integer \(m\), proving the lemma. This also covers maxima on faces, because the argument is made in the relative interior of the positive support. \(\square\)

**4. Sharp universal extremum and equality.** Put \(c=\sqrt[3]{3}\) and \(s_*=(c-1)/3\), so \(1+3s_*=c\). It follows that

\[
\frac3{(1+3s_*)^3}=1.
\]

For real \(t>0\), define \(h(t)=t/(1+s_*t)^3\). Then

\[
h'(t)=\frac{1-2s_*t}{(1+s_*t)^4}.
\]

The elementary inequalities \(1/8<s_*<1/6\) show that the unique continuous maximum of \(h\) occurs strictly between \(3\) and \(4\). Thus its maximum over positive integers occurs at either \(m=3\) or \(m=4\). In fact \(h(4)<1=h(3)\): writing \(d=\sqrt[3]{4}\), the rigorously verified rational bounds

\[
(1442/1000)^3<3,\qquad (1588/1000)^3>4
\]

imply \(c>1442/1000\) and \(d<1588/1000\), whence

\[
s_*=\frac{c-1}{3}>\frac{442}{3000}>\frac{588}{4000}>\frac{d-1}{4}.
\]

Therefore \(1+4s_*>d\) and \(4/(1+4s_*)^3<1\). By the lemma,

\[
\sum_a\left(\frac{p_a}{p_a+s_*}\right)^3\le1,
\]

with equality if and only if the positive support consists of exactly three equally weighted symbols.

For a given source set \(r_*=(1+s_*)^{-1}\). Direct substitution gives \(g_a(r_*)=p_a/(s_*+p_a)\), so \(T(r_*)\le1\). Since \(T\) is strictly increasing and \(T(r)=1\), one has \(r\ge r_*\), hence \(\lambda=r^{-1}\le1+s_*=(2+c)/3\). The equal-support characterization gives equality precisely for the uniform three-symbol source. Finally, for this source \(g_a(z)=z/(3-2z)\), \(T(z)=3z^3/(3-2z)^3\), \(r=3/(2+c)\), and \(rT'(r)=9/(3-2r)\). Substitution into Step 2 simplifies the prefactor to \(c/[3(c-1)]\). \(\square\)

## Verification

The standalone file `verify_cube_expectation.py` contains **independent finite checks**, not a replacement for the proof. It enumerates every input word for six rational source distributions with alphabet sizes two through four, through lengths 7–12 depending on the alphabet, and computes distinct scattered cubes directly by checking every possible nonempty root. Its exact rational expectations agree coefficient-by-coefficient with a separate truncated-power-series implementation of the derived generating function. In total, 115,024 input words were checked. The same code checks the rational bounds used in the discrete optimizer comparison and stationary-pair second-derivative signs. Run with `python verify_cube_expectation.py`; no third-party libraries are needed.

## Relationship to prior work

Biers-Ariel, Godbole and Kelley (first publicly available April 27, 2017, arXiv:1704.08661) study expectations of **all** distinct scattered subsequences, including arbitrary-alphabet recurrences and exponential rates. Their Section 3.1 and Section 3.3 address the unrestricted count, not its cube-language restriction or optimization across both alphabet size and bias. The present waiting-time method uses elementary known machinery; that machinery, and unrestricted expectation results, are not claimed as new.

Rubinchik and Shur (arXiv:1505.08043) analyze random **contiguous** palindromic factors and squares, with square counts of order \(\sqrt n\); the notion of a contiguous factor differs sharply from the scattered cube language here, whose expectation is exponential. The source is contextual rather than the date-defining guide.

The substantive claim is the exact weighted scattered-cube mean combined with the global, all-source **three-symbol rigidity theorem**. The constrained cube language is neither the unrestricted subsequence language nor the palindrome, Lyndon or Abelian-square language. An equivalent specialization of more general weighted-language enumerations may exist outside the inspected literature; the full novelty assessment is therefore bounded by the sources actually checked.

## Limitations

The theorem concerns **expectations**, not concentration or almost-sure growth. The asymptotics fix the finite alphabet and its positive probability vector before taking \(n\to\infty\); there is no uniform error bound as probabilities approach zero or alphabet size grows. Nonprimitive roots are included. The optimality concerns the **exponential base** only; it does not assert finite-\(n\) optimality for the expected cube count. The methods do not automatically prove an identical alphabet optimizer for higher powers, and no such extension is claimed. Independent validation is not part of this result.

## References

1. Y. Biers-Ariel, A. Godbole and E. Kelley, *Expected Number of Distinct Subsequences in Randomly Generated Binary Strings*, arXiv:1704.08661, first version April 27, 2017; Discrete Mathematics & Theoretical Computer Science 19(2), 2018. https://arxiv.org/abs/1704.08661
2. M. Rubinchik and A. M. Shur, *The Number of Distinct Subpalindromes in Random Words*, arXiv:1505.08043, first version May 29, 2015; Fundamenta Informaticae, 2018. https://arxiv.org/abs/1505.08043

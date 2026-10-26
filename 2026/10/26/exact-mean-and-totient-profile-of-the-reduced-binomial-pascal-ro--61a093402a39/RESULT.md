# Exact mean and totient profile of the reduced-binomial Pascal-row deficit

## Finding
For every integer \(n\ge1\), put \(g_{n,k}=\gcd(n,k)\) for \(0\le k\le n\), and let
\[
R(n)=1-\frac{1}{2^n}\sum_{k=0}^{n}\binom{n/g_{n,k}}{k/g_{n,k}}.
\]
Writing \(\varphi\) for Euler's totient and \(\tau\) for the number-of-divisors function, set \(M_n=2^{-n}\binom n{\lfloor n/2\rfloor}\). Then, for all \(n\ge1\),
\[
\left|R(n)-\left(1-\frac{\varphi(n)}n\right)\right|
\le 2\tau(n)M_n+(n+1)2^{-n/2}.
\]
In particular, the error tends to zero as \(n\to\infty\), uniformly over integers of that size. For every integer \(N\ge2\),
\[
\frac1N\sum_{n=1}^N R(n)
=1-\frac6{\pi^2}+O\!\left(\frac{1+\log N}{\sqrt N}\right).
\]
The implied constant is absolute. The exact limiting mean is therefore \(1-6/\pi^2=0.392072898145973\ldots\). This identifies the value sought in the numerical mean-ratio conjecture for OEIS A271834. Further, \(R(p)=0\) for every prime \(p\), whereas \(R(\prod_{p\le y}p)\to1\) as \(y\to\infty\); hence the mean exists despite maximal liminf/limsup oscillation.

## Assumptions and scope
The binomial coefficients are ordinary integer binomial coefficients, and \(n\) ranges over all positive integers; in particular \(\gcd(n,0)=\gcd(n,n)=n\), so both endpoint terms in the reduced row are \(1\). The summation is over all \(k=0,1,\ldots,n\), not just primitive indices. The constant \(6/\pi^2\) comes from the classical mean of \(\varphi(n)/n\). No primality or parity restriction is imposed on \(n\).

## Proof
**1. Separate the primitive columns.** Let \(X_n\) have distribution \(\Pr(X_n=k)=w_{n,k}=2^{-n}\binom nk\) for \(0\le k\le n\). At every \(k\) for which \(g_{n,k}=1\), the reduced and original binomial coefficients agree. Therefore, defining
\[
E_n=2^{-n}\sum_{\substack{0\le k\le n\\g_{n,k}>1}}\binom{n/g_{n,k}}{k/g_{n,k}},
\]
we obtain the exact identity
\[
R(n)=\Pr\bigl(\gcd(n,X_n)>1\bigr)-E_n.
\]
If \(g_{n,k}>1\), then \(n/g_{n,k}\le n/2\) and \(\binom{n/g_{n,k}}{k/g_{n,k}}\le2^{n/g_{n,k}}\). Hence
\[
0\le E_n\le(n+1)2^{-n/2}.
\]
Moreover \(0\le R(n)<1\): replacing a subset of \(n/g\) blocks (each of size \(g\)) by its union gives an injection into the size-\(k\) subsets of \(n\) labelled elements, so \(\binom{n/g}{k/g}\le\binom nk\), and both endpoints of the reduced sum equal \(1\).

**2. Uniform residue-class discrepancy.** Fix a positive integer \(d\), and put \(z_k=\mathbf 1_{d\mid k}-1/d\). For every nonnegative integer \(j\),
\[
S_j=\sum_{k=0}^j z_k=\left\lfloor\frac jd\right\rfloor+1-\frac{j+1}{d},
\qquad 0\le S_j\le1.
\]
Extend \(w_{n,n+1}=0\). Summation by parts and the unimodality of the binomial row yield
\[
\begin{aligned}
\left|\Pr(d\mid X_n)-\frac1d\right|
&=\left|\sum_{j=0}^n S_j(w_{n,j}-w_{n,j+1})\right|\\
&\le\sum_{j=0}^n|w_{n,j}-w_{n,j+1}|\le2M_n.
\end{aligned}
\]
This bound holds **for every divisor size**, including \(d>\sqrt n\); no unproved equidistribution assumption for large moduli is involved.

**3. Recover the totient.** Möbius inversion gives the exact indicator identity
\[
\mathbf 1_{\gcd(n,k)=1}=\sum_{d\mid n,\ d\mid k}\mu(d),
\qquad \frac{\varphi(n)}n=\sum_{d\mid n}\frac{\mu(d)}d.
\]
Taking the binomial-weighted expectation and using the preceding discrepancy bound over all divisors of \(n\),
\[
\left|\Pr(\gcd(n,X_n)=1)-\frac{\varphi(n)}n\right|
\le\sum_{d\mid n} |\mu(d)|\,2M_n\le2\tau(n)M_n.
\]
Combining with step 1 proves the displayed pointwise estimate. The standard central-binomial estimate \(M_n=O(n^{-1/2})\) and the elementary divisor bound \(\tau(n)=O_\varepsilon(n^\varepsilon)\) for every \(\varepsilon>0\) show that its right-hand side tends to zero.

**4. Average the bound.** By the divisor-sum identity \(\tau(n)=\sum_{ab=n}1\),
\[
\sum_{n\le N}\frac{\tau(n)}{\sqrt n}
=\sum_{ab\le N}\frac1{\sqrt{ab}}
\le2\sqrt N\sum_{a\le N}\frac1a
=O(\sqrt N(1+\log N)).
\]
The exponential errors have a bounded sum. Also
\[
\begin{aligned}
\sum_{n\le N}\frac{\varphi(n)}n
&=\sum_{d\le N}\frac{\mu(d)}d\left\lfloor\frac Nd\right\rfloor\\
&=N\sum_{d=1}^{\infty}\frac{\mu(d)}{d^2}+O(1+\log N)
=\frac{6N}{\pi^2}+O(1+\log N).
\end{aligned}
\]
Dividing by \(N\) proves the asserted mean with its error term.

**5. Opposite extremal subsequences.** For a prime \(p\), every interior \(k\) has \(\gcd(p,k)=1\), so the reduced row is the ordinary row and \(R(p)=0\). If \(n_y=\prod_{p\le y}p\) is the primorial, Euler's divergence of the reciprocal-prime series implies \(\varphi(n_y)/n_y=\prod_{p\le y}(1-1/p)\to0\). The pointwise approximation gives \(R(n_y)\to1\). Together with \(0\le R(n)<1\), this proves \(\liminf R(n)=0\) and \(\limsup R(n)=1\).

## Verification
Run the standalone standard-library program `verify.py` with `python3 verify.py`. It independently constructs 320 modified rows using exact integer binomial coefficients, checks the fifteen initial values of A271834, verifies the exact decomposition and the rational pointwise bounds, and tests 1,901 residue-class inequalities at every divisor of the tested moduli. Its successful output is recorded in `VERIFICATION.md`. These checks are finite and do not substitute for the proof above.

## Relationship to prior work
OEIS A082905 introduced the gcd-reduced Pascal triangle (April 23, 2003), and A082906 tabulates its row sums. The OEIS A271834 entry (April 19, 2016) records the normalized deficit and explicitly proposes existence of an average near \(0.3915\), based on a numerical table through \(5{,}000\). The present theorem provides its exact value, a uniform pointwise totient approximation, a quantitative Cesàro error and the full liminf/limsup behavior. The argument uses standard binomial unimodality, Möbius inversion and the classical mean of the totient ratio, but no such answer appears in the inspected entries. This is a literature-bounded priority assessment, not a claim of comprehensive uniqueness.

## Limitations
The error term is a universal sufficient bound, not claimed optimal. The pointwise approximation does not assert convergence of \(R(n)\) itself; indeed its liminf and limsup differ. Other published weighted-coprimality theorems could yield the intermediate discrepancy estimate, and undetected earlier treatments of the precise A271834 limit remain a priority risk. No independent mathematical audit has been performed.

## References
- Labos Elemer, *Modified Pascal-triangle* (OEIS A082905, entered April 23, 2003), https://oeis.org/A082905 .
- Labos Elemer, *Modified Pascal-row sums* (OEIS A082906, entered April 23, 2003), https://oeis.org/A082906 .
- S. Sykora, *Reduced-binomial row deficit* (OEIS A271834, entered April 19, 2016), https://oeis.org/A271834 .
- S. Sykora, *Ratio table for OEIS A271834, indices 1 through 5000*, https://oeis.org/A271834/a271834.txt .

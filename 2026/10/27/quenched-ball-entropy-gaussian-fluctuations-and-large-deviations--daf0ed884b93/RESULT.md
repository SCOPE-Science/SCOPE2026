# Quenched ball entropy, Gaussian fluctuations, and large deviations for the limited-permutation channel

## Finding

For any fixed alphabet size \(q\geq2\), choose a word \(X_n\) uniformly from \(\Sigma_q^n\). Let \(V_n=|B_1(X_n)|\) be the number of **distinct** outputs after a single layer of any number of pairwise disjoint adjacent transpositions; doing nothing is permitted. Set \(p=(q-1)/q\), \(h=1/q\), \(m=n-1\), and use Fibonacci numbers \(F_0=0,F_1=1\). For every real \(t\), there is a unique real number \(P_q(t)\) satisfying

\[
 h\sum_{\ell=0}^{\infty}p^\ell F_{\ell+2}^{\,t}\exp\!\left(-(\ell+1)P_q(t)\right)=1,
 \qquad P_q(t)>\log(p\varphi^t),\quad \varphi=\frac{1+\sqrt5}{2}.
\]

The entire logarithmic moment generating function has the asymptotic form

\[
 \log\mathbb E[V_n^t]=mP_q(t)+O_{q,t}(1),
 \qquad\lim_{n\to\infty}m^{-1}\log\mathbb E[V_n^t]=P_q(t).
\]

The error can be chosen locally analytic in \(t\), with exponentially convergent corrections. The function \(P_q\) is real analytic and strictly convex on \(\mathbb R\). Define

\[
 \mu_q=h^2\sum_{\ell\geq0}p^\ell\log F_{\ell+2},\qquad
 \sigma_q^2=h^2\sum_{\ell\geq0}p^\ell\left(\log F_{\ell+2}-(\ell+1)\mu_q\right)^2.
\]

Both series converge absolutely, and \(\sigma_q^2>0\). One has

\[
 \frac{\log V_n}{m}\longrightarrow\mu_q\quad\text{almost surely},\qquad
 \frac{\log V_n-m\mu_q}{\sqrt{m\sigma_q^2}}\Longrightarrow N(0,1),
\]

\[
 \mathbb E[\log V_n]=m\mu_q+O_q(1),\quad
 \operatorname{Var}(\log V_n)=m\sigma_q^2+O_q(1).
\]

Moreover, \(\log V_n/m\) satisfies a full large-deviation principle with speed \(m\) and good rate function

\[
 I_q(u)=\sup_{t\in\mathbb R}\{tu-P_q(t)\}.
\]

The **annealed** exponent, already implicit in the published mean-ball recurrence, is \(P_q(1)=\log\lambda_q\), with \(\lambda_q=(1+\sqrt{1+4p})/2\). The new typical exponent obeys the **strict** inequality

\[
 0<\mu_q<\log\lambda_q<\log\varphi.
\]

Writing \(d=\log(\sqrt5/\varphi)\), as \(q\to\infty\),

\[
 \mu_q=\log\varphi-\frac d q+O(q^{-2}),\quad
 \sigma_q^2=\frac{d^2}{q}+o(q^{-1}),
\]

\[
 \log\lambda_q-\mu_q=
 \frac{d-1/(\varphi\sqrt5)}{q}+O(q^{-2}),\qquad
 d-\frac1{\varphi\sqrt5}>0.
\]

Thus expected and typical radius-one output balls have distinct exponential growth rates at every fixed finite alphabet; their gap has an explicit positive large-alphabet coefficient.

## Assumptions and scope

The displacement radius is exactly one and the channel applies **one simultaneous set** of disjoint neighboring swaps, not an arbitrary sequential series of swaps. Input letters are independent and uniform on a fixed \(q\)-symbol alphabet; the limits in \(n\) are taken with \(q\) fixed. The statements concern output-ball **volume**, not error-correcting code capacity or the probability distribution of a selected channel output. Natural logarithms are used. The large-alphabet limits concern the previously defined fixed-\(q\) constants.

## Proof

**1. Exact reduction to Bernoulli runs.** Let \(E_i={\bf1}\{X_i\ne X_{i+1}\}\), for \(1\leq i\leq m\). The vector \((E_1,\ldots,E_m)\) is independent Bernoulli with success probability \(p\): each prescribed equality/inequality pattern has exactly \(q\,(q-1)^k\) preimages when it has \(k\) inequalities, giving probability \(p^kh^{m-k}\). Each effective swap set is a matching in the path of edges with \(E_i=1\), and distinct effective matchings produce different words. For the latter assertion, take the first edge \(i\) on which two different matchings disagree; neither matching uses edge \(i-1\), and their output symbols at position \(i\) are respectively \(X_i\) and \(X_{i+1}\), which differ. A run of \(\ell\) consecutive ones contributes \(F_{\ell+2}\) matchings. Hence

\[
 V_n=\prod_{\text{maximal one-runs }J}F_{|J|+2}.
\]

An empty product is one. This product representation is compatible with the antirun ball formula of Langberg, Schwartz and Yaakobi; it is used as the starting point, not claimed as a new theorem.

**2. All real moments and pressure.** Set \(M_m(t)=\mathbb E[V_{m+1}^t]\), with \(M_0(t)=1\). Inspect the initial run: either it contains \(\ell<m\) ones followed by a zero (probability \(hp^\ell\)), or consists of \(m\) ones (probability \(p^m\)). Therefore

\[
 M_m(t)=p^mF_{m+2}^{\,t}
 +h\sum_{\ell=0}^{m-1}p^\ell F_{\ell+2}^{\,t}M_{m-\ell-1}(t).
\]

Define \(A_t(z)=\sum_{\ell\geq0}p^\ell F_{\ell+2}^{\,t}z^\ell\). The exact generating function is

\[
 \sum_{m\geq0}M_m(t)z^m=\frac{A_t(z)}{1-hzA_t(z)}.
\]

By Binet's formula, \(A_t(z)\) has radius \((p\varphi^t)^{-1}\), and diverges to positive infinity approaching that radius along the positive real axis. The strictly increasing function \(hzA_t(z)\) consequently takes value one at exactly one \(z_t\) inside its disc of convergence. Its derivative there is positive, so the generating function has a simple pole. The coefficient of every positive power in \(hzA_t(z)\) is strictly positive, including that of \(z\). The strict triangle inequality excludes any other pole on \(|z|=z_t\); analyticity then gives a strictly larger annulus with no competing singularity. By residue extraction,

\[
 M_m(t)=c_q(t)z_t^{-m}\bigl(1+O_{q,t}(\eta_{q,t}^{m})\bigr),
\]

with \(c_q(t)>0\) and \(0<\eta_{q,t}<1\). Near any fixed real \(t\), the pole and residue continue analytically and the estimate is locally uniform for complex perturbations. Put \(P_q(t)=-\log z_t\). This proves the pressure equation, all-real moment growth and analyticity.

**3. Derivatives, strict convexity, fluctuations.** Let \(L\) be geometric on \(\{0,1,\ldots\}\) with \(\Pr(L=\ell)=hp^\ell\), and put \(T=L+1\), \(R=\log F_{L+2}\). The pressure equation reads \(\mathbb E\exp(tR-P_q(t)T)=1\). Tilt the law of \(L\) by the strictly positive weights inside this expectation, which sum to one. Implicit differentiation gives

\[
 P_q'(t)=\frac{\mathbb E_t[R]}{\mathbb E_t[T]},\qquad
 P_q''(t)=\frac{\mathbb E_t[(R-P_q'(t)T)^2]}{\mathbb E_t[T]}>0.
\]

Strictness holds because the cases \(L=0\) and \(L=1\) cannot simultaneously satisfy \(R=aT\) for any \(a\): they give respectively \((T,R)=(1,0)\) and \((2,\log2)\). At \(t=0\), the tilted law is the original geometric law and \(\mathbb E T=1/h\). Thus \(P_q'(0)=\mu_q\) and \(P_q''(0)=\sigma_q^2\), as displayed. Local analytic pole asymptotics imply uniform convergence of cumulant generating functions on a complex neighborhood of zero. Taylor expansion at arguments of order \(m^{-1/2}\) proves the Gaussian limit; the first two derivatives give the asserted mean and variance errors. Chernoff bounds at small positive and negative \(t\) imply exponentially summable deviations of \(\log V_n/m\) from \(\mu_q\), proving the almost-sure law. Since \(P_q\) is differentiable on all of \(\mathbb R\) and \(0\leq\log V_n/m\leq\log F_{m+2}/m\), exponential tightness and the Gärtner–Ellis theorem give the full large-deviation principle with the stated Legendre-transform rate.

**4. Comparison with the annealed growth rate.** At \(t=1\), the exact recurrence for expected ball sizes simplifies to the published recursion \(\mathbb E V_n=\mathbb E V_{n-1}+p\mathbb E V_{n-2}\), with initial values one. Its exponential growth rate is \(\lambda_q\), so \(P_q(1)=\log\lambda_q\). Strict convexity yields \(P_q(1)>P_q(0)+P_q'(0)=\mu_q\), since \(P_q(0)=0\). The inequalities \(\mu_q>0\) and \(\log\lambda_q<\log\varphi\) follow from positive probability of an effective swap and \(p<1\).

**5. Large-alphabet coefficients.** Binet's formula gives, with \(c=2\log\varphi-\tfrac12\log5\),

\[
 \log F_{\ell+2}=\ell\log\varphi+c+
 \log\bigl(1-(-\varphi^{-2})^{\ell+2}\bigr).
\]

The last term decays geometrically. Substitution into the convergent geometric series for \(\mu_q\) gives \(\mu_q=\log\varphi-h(\log\varphi-c)+O(h^2)\), and \(\log\varphi-c=d\). Furthermore, as \(h\downarrow0\), the variable \(h(L+1)\) converges to a mean-one exponential distribution, with convergence of second moments. The centered cycle reward satisfies \(R-\mu_qT=d(hT-1)+o_{L^2}(1)\); the geometrically decaying Binet remainder vanishes in \(L^2\). Since \(\sigma_q^2=h\mathbb E[(R-\mu_qT)^2]\), this proves \(\sigma_q^2=d^2h+o(h)\). Expanding the explicit \(\lambda_q\) at \(p=1-h\) yields \(\log\lambda_q=\log\varphi-h/(\varphi\sqrt5)+O(h^2)\). Finally, the elementary strict inequality \(\log u>1-1/u\) for \(u>1\), applied to \(u=\sqrt5/\varphi\), proves \(d>1/(\varphi\sqrt5)\).

## Verification

The standalone Python script `verify.py` enumerates every word for \((q,n)=(2,1\ldots10),(3,1\ldots8),(4,1\ldots7),(5,1\ldots6)\). It constructs all disjoint-swap outputs directly, checks injection and the Fibonacci run formula, and compares exact rational first and second ball-size moments with the displayed all-real-moment recurrence at \(t=1,2\). This totals 53,260 words. The script evaluates \(\mu_q\), \(\sigma_q^2\) and \(\log\lambda_q\) numerically at six alphabets and checks the large-alphabet coefficients. Executing `python verify.py` prints `VERIFY_OK`; `verify_output.txt` contains the recorded output. The infinite results above are proved analytically, not inferred from enumeration or finite numerical values.

## Relationship to prior work

Langberg, Schwartz and Yaakobi, *Coding for the \(\ell_\infty\)-Limited Permutation Channel* (2017), Theorems 16 and 18, establish the center-dependent Fibonacci-product formula and the **arithmetic** mean-ball recurrence. These ingredients are explicitly reused. The present result adds the **geometric/quenched** entropy rate, Gaussian variance with strict positivity, a full pressure and large-deviation law, a strict gap from arithmetic mean growth, and the quantitative large-alphabet gap. These are not stated by the cited theorems, and the published mean recurrence by itself does not determine their values. Ben Shimon and Zabokritskiy (first public July 21, 2026) investigate code constructions, extinction, covering and detection for the same channel, including the all-distinct Fibonacci ball; their capacity bounds neither assert nor imply the random-center fluctuation law. The distinct objects are code capacity versus center-ball statistics; no capacity improvement is claimed.

## Limitations

The result treats uniform independent input and simultaneous displacement-one swaps. It does not resolve zero-error capacity, optimal covering sizes, nonuniform or dependent input laws, or higher displacement radii. The pressure uses a uniquely defined convergent implicit series rather than elementary closed formulas at arbitrary real moments. General renewal, analytic-combinatorial, central-limit and large-deviation principles are standard mathematical tools; novelty is claimed only for the explicit limited-permutation-channel application and quantitative relations, subject to independent literature verification. No independent audit has been performed.

## References

1. M. Langberg, M. Schwartz, Y. Yaakobi, *Coding for the \(\ell_\infty\)-Limited Permutation Channel*, IEEE Transactions on Information Theory **63** (2017), 7676–7686, doi:10.1109/TIT.2017.2762676. Full text: https://www.ece.mcmaster.ca/~schwam10/publications/MSjrnl35.pdf . Theorems 16 and 18.
2. N. Ben Shimon and A. L. Zabokritskiy, *Extinction Depth and \(q\)-ary Error-Correcting Codes for the Limited Permutation Channel*, arXiv:2607.19566 (first public July 21, 2026). https://arxiv.org/abs/2607.19566 . In particular Sections 1, 2 and 5.
3. Standard analytic tools used: simple-pole coefficient extraction, analytic implicit-function theorem, and the Gärtner–Ellis large-deviation theorem. These are cited as established background, not as new results.

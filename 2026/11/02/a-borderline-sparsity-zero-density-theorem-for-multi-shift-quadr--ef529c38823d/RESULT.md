# A borderline-sparsity zero-density theorem for multi-shift quadratic Romanoff sets

## Finding

Fix an integer \(r\ge 2\). Let \(F(U,V)=AU^2+BUV+CV^2\) be an integral homogeneous binary quadratic form with nonzero discriminant \(\Delta=B^2-4AC\). Assume the **positive-quadrant coercivity** condition: some \(c>0\) satisfies \(F(u,v)\ge c(u^2+v^2)\) for all real \(u,v\ge0\). Let \((a_k)_{k\ge1}\) be a strictly increasing sequence of positive integers with \(a_k\mid a_{k+1}\) and write \(N_a(X)=|\{k:a_k\le X\}|\). Suppose
\[
\sup_{k\ge1}\sum_{d\mid a_k}\frac1d=+\infty,
\qquad N_a(X)^r=O((\log X)^2)\quad (X\to\infty).
\]
Then the subset of the positive integers
\[
\mathcal S_{F,r}(a)=\{F(p,q)+a_{k_1}+\cdots+a_{k_r}:p,q\text{ prime},\ k_i\ge1\}
\]
has natural density zero:
\[
\lim_{X\to\infty}\frac{|\mathcal S_{F,r}(a)\cap[1,X]|}{X}=0.
\]
For \(r=2\), the growth hypothesis is automatic from the strict divisibility chain. For every fixed \(r\ge3\), the hypotheses are simultaneously realizable on the borderline logarithmic scale by
\[
a_k=k!\,2^{\lceil k^{r/2}\rceil}.
\]
The form class includes both positive-definite forms such as \(U^2+UV+V^2\) and positive-quadrant-coercive reducible forms such as \((U+V)(U+2V)\). No assertion is made for singular discriminant \(\Delta=0\), or if the counting hypothesis is violated.

## Assumptions and scope

All primes are positive rational primes, all indices \(k_i\) are positive integers, the integer \(r\) and the coefficients of \(F\) are fixed as \(X\to\infty\), and \(O\)-constants may depend on these fixed quantities and the sequence. The hypothesis \(c>0\) forces \(A,C>0\). Write \(\sigma_{-1}(n)=\sum_{d\mid n}d^{-1}\), \(\pi(Y)\) for the number of primes not exceeding \(Y\), and \(N_a(X)\) as above.

For an odd prime \(\ell\nmid 2AC\Delta\), set \(\chi_\ell=(\Delta/\ell)\in\{-1,1\}\). The discriminant may be a positive square; the argument uses only \(\Delta\neq0\), and in the square case \(\chi_\ell=1\) outside finitely many primes.

## Proof

**1. Divergent usable prime mass.** Let \(\mathcal P\) be the set of primes dividing at least one \(a_k\). For every positive integer \(n\),
\[
\log\sigma_{-1}(n)\le\sum_{\ell\mid n}\log(1-1/\ell)^{-1}\le 2\sum_{\ell\mid n}\frac1\ell.
\]
Thus \(\sup_k\sigma_{-1}(a_k)=\infty\) forces \(\sum_{\ell\in\mathcal P}1/\ell=\infty\). Removing primes dividing the fixed nonzero integer \(2AC\Delta\) does not affect divergence. Choose any finite nonempty set \(\mathcal L\) of the remaining odd primes. Set
\[
P=\prod_{\ell\in\mathcal L}\ell,\quad H=\sum_{\ell\in\mathcal L}\frac1\ell,\quad
T(n)=\sum_{\ell\in\mathcal L}\chi_\ell\bigl({\bf1}_{\ell\mid n}-1/\ell\bigr).
\]
Since \(a_k\mid a_{k+1}\), there is a fixed \(K\) such that \(P\mid a_k\) for all \(k\ge K\); hence \(T(F(p,q)+\sum_i a_{k_i})=T(F(p,q))\) whenever all \(k_i\ge K\).

**2. Exact local quadratic root count.** For each \(\ell\in\mathcal L\), the congruence \(F(u,v)\equiv0\pmod\ell\), with \(u,v\) nonzero modulo \(\ell\), is equivalent to \(At^2+Bt+C\equiv0\pmod\ell\) for \(t=uv^{-1}\). Its discriminant is \(\Delta\). As \(\ell\nmid2AC\Delta\), it has exactly \(1+\chi_\ell\) distinct roots, all nonzero, and each root admits \(\ell-1\) choices of \(v\). Consequently, under the uniform measure on \(((\mathbb Z/P\mathbb Z)^\times)^2\), the indicators \(I_\ell={\bf1}_{\ell\mid F(u,v)}\) are independent with probabilities
\[
\rho_\ell=\frac{1+\chi_\ell}{\ell-1}.
\]
The Chinese remainder theorem supplies independence, including when \(\Delta\) is a square. Thus the mean \(\mu\) and variance of \(T(F(u,v))\) are
\[
\mu=\sum_{\ell\in\mathcal L}\chi_\ell(\rho_\ell-1/\ell)
=H+\sum_{\ell\in\mathcal L}\frac{1+\chi_\ell}{\ell(\ell-1)}\ge H,
\]
\[
\operatorname{Var}(T(F(u,v)))=\sum_{\ell\in\mathcal L}\rho_\ell(1-\rho_\ell)
\le\sum_{\ell\in\mathcal L}\frac2{\ell-1}\le3H.
\]
(The last inequality holds for all odd primes.) Chebyshev's inequality therefore gives
\[
\mathbb P_{(u,v)\in((\mathbb Z/P\mathbb Z)^\times)^2}\{T(F(u,v))<H/2\}\le\frac{12}{H}.
\]
Under the uniform measure on \(n\pmod P\), the variables \({\bf1}_{\ell\mid n}\) are independent Bernoulli variables of means \(1/\ell\). Hence \(T(n)\) has mean zero and variance at most \(H\). Another Chebyshev bound gives
\[
\#\{1\le n\le X:T(n)\ge H/2\}\le\frac{4X}{H}+O_{\mathcal L}(1).
\]

**3. Prime pairs and shifts.** By quadrant coercivity, each representation \(n=F(p,q)+\sum_i a_{k_i}\le X\) has \(p,q\le Y=\sqrt{X/c}\). For fixed \(P\), the prime number theorem in arithmetic progressions says the unit-residue classes of primes up to \(Y\) become uniformly distributed modulo \(P\). The finitely many prime divisors of \(P\) contribute only \(O_{\mathcal L}(\pi(Y))\) exceptional ordered pairs. Therefore
\[
\#\{p,q\le Y:T(F(p,q))<H/2\}
\le (12/H+o_{\mathcal L,F}(1))\pi(Y)^2.
\]
A representation with at least one index \(k_i<K\) can occur for at most
\[
r(K-1)N_a(X)^{r-1}\pi(Y)^2
=O_{F,\mathcal L,r}(X(\log X)^{-2/r})=o(X)
\]
choices of the ordered parameters. Here we used \(N_a(X)^r=O((\log X)^2)\) and \(\pi(Y)=O(\sqrt X/\log X)\). In all remaining representations, \(T(n)=T(F(p,q))\). Split represented \(n\le X\) into \(T(n)\ge H/2\) and \(T(n)<H/2\). For the first class the count is at most \(4X/H+O_{\mathcal L}(1)\). For the second it is at most
\[
N_a(X)^r(12/H+o_{\mathcal L,F}(1))\pi(Y)^2
\le (C_{F,r,a}/H+o_{\mathcal L,F,r,a}(1))X
\]
for a constant \(C_{F,r,a}\) independent of the finite choice \(\mathcal L\). Therefore
\[
\limsup_{X\to\infty}\frac{|\mathcal S_{F,r}(a)\cap[1,X]|}{X}
\le\frac{4+C_{F,r,a}}{H}.
\]
The finite set \(\mathcal L\) may be chosen with arbitrarily large \(H\), proving zero density.

**4. Genuine higher-shift borderline examples.** Fix \(r\ge3\) and \(a_k=k!\,2^{\lceil k^{r/2}\rceil}\). It is a strictly increasing divisibility chain. Since \(a_k\ge 2^{k^{r/2}}\), we have \(N_a(X)=O((\log X)^{2/r})\). Since \(k!\mid a_k\),
\[
\sigma_{-1}(a_k)\ge\prod_{\ell\le k,\ \ell\text{ prime}}(1+1/\ell)\longrightarrow\infty
\]
by Euler's divergence of the prime reciprocal series. Also \(\log a_k=(\log2)k^{r/2}+o(k^{r/2})\), because \(\log(k!)=O(k\log k)=o(k^{r/2})\) for \(r>2\). Thus the growth condition is met at the \(N_a(X)\asymp(\log X)^{2/r}\) scale; it does not imply zero density by a trivial representation-count bound.

## Verification

A dependency-free `verify.py` independently checks the exact finite-field root-count lemma for six forms and every admissible odd prime below \(150\). It also verifies the exact first-moment expression against finite residue arithmetic for several small primes. It cannot certify an asymptotic prime number theorem, Chebyshev's inequality, or an infinite-density statement: those steps are explicitly proved above from standard theorems. Execute `python3 verify.py` with Python 3. The calculations verify the local nonstandard step but do not replace the infinite proof.

## Relationship to prior work

Yan and Xu, arXiv:2610.28237v1 (October 20, 2026), Theorem 1.2, prove the \(r=2\), \(F(U,V)=U^2+V^2\) instance. Their full proof contains the second-moment obstruction, but does not state the multi-shift critical-growth theorem or extend its local counting lemma to a general nondegenerate cone-coercive quadratic form. Dai and Pan (DOI 10.1016/j.jnt.2026.04.003), as quoted by Yan and Xu and in the publisher abstract, prove positive lower density for the canonical two-square, two-shift setting under complementary bounded-divisor-sum hypotheses; this does not imply our zero-density conclusion. Lam, Schindler and Xiao (arXiv:1809.10755) study primes represented by binary quadratic forms with thin variables, not values at two independent primes plus shifts. The proof strategy here adapts Yan–Xu rather than claiming a new general-purpose second-moment method.

## Limitations

The growth hypothesis \(N_a(X)^r=O((\log X)^2)\) is a sufficient critical-scale assumption, not a claimed necessary or optimal threshold. At \(r>2\), infinitely many chains satisfy both it and the divergent reciprocal-divisor hypothesis, as explicitly shown. The proof excludes \(\Delta=0\) because its root count and mean-separation mechanism need not hold; it excludes quadratic forms not coercive on the positive quadrant because prime variables may then have unbalanced sizes. No positive-density theorem is asserted under bounded \(\sigma_{-1}\). Literature searches cannot prove global uniqueness; an unindexed earlier generalization remains possible. Independent validation has not been performed.

## References

1. X.-H. Yan and Y.-T. Xu, *A necessary condition for a Romanoff type theorem*, arXiv:2610.28237v1, first posted October 20, 2026. https://arxiv.org/html/2610.28237v1
2. L.-X. Dai and H. Pan, *On Erdős' generalization of the Romanoff theorem*, Journal of Number Theory 291 (2027), 65–73, DOI:10.1016/j.jnt.2026.04.003. (Journal date is not used as the source's first-public date.)
3. P. C.-H. Lam, D. Schindler and S. Y. Xiao, *On prime values of binary quadratic forms with a thin variable*, arXiv:1809.10755, 2018. https://arxiv.org/abs/1809.10755
4. H. Davenport, *Multiplicative Number Theory*, 3rd edition, Springer, 2000 (prime number theorem in arithmetic progressions).

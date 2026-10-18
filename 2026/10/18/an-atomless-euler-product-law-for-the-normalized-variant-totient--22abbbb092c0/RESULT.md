# An atomless Euler-product law for the normalized variant totient

## Finding

For each integer \(n\ge2\), define \(T(n)\) to be the number of odd integers \(1\le m\le n\) such that both \(m\) and \((m-1)/2\) are coprime to \(n\); set \(T(1)=0\). Let \(N_x\) be uniformly distributed among the integers \(1,\ldots,\lfloor x\rfloor\), for real \(x\ge1\).

For each prime \(p\), take independent Bernoulli variables \(I_p\) with \(\Pr(I_p=1)=1/p\), and set
\[
B=\frac12\prod_{p\ge3}\left(1-\frac2p\right)^{I_p}\quad\text{if }I_2=1,\qquad
B=\prod_{p\ge3}\left(1-\frac2p\right)^{I_p}\quad\text{if }I_2=0,
\qquad X=\frac B2.
\]
Equivalently, \(B=\prod_p b_p^{I_p}\), with \(b_2=1/2\) and \(b_p=1-2/p\) for odd primes.

**Theorem.** The random variables \(T(N_x)/N_x\) converge in distribution to \(X\) as \(x\to\infty\). The infinite product defining \(X\) converges to a strictly positive number almost surely. **Its distribution has no atoms** (in particular, neither zero nor any positive value has positive mass). For each integer \(r\ge1\),
\[
\lim_{x\to\infty}\frac1{\lfloor x\rfloor}\sum_{n\le x}\left(\frac{T(n)}n\right)^r
=\mathbb E[X^r]
=\frac{1+2^{-r}}{2^{r+1}}
\prod_{p\ge3}\left(1-\frac1p+\frac1p\left(1-\frac2p\right)^r\right).
\]
Moreover, as real \(x\to\infty\),
\[
\sum_{n\le x}T(n)=C x^2+O\!\left(x(\log(2x))^2\right),\qquad
C=\frac3{16}\prod_{p\ge3}\left(1-\frac2{p^2}\right)=0.120987879\ldots.
\]
The \(O\)-constant is absolute. These statements concern the arithmetic function just defined; they make no security guarantees for cryptographic constructions.

## Assumptions and scope

All variables \(n\) are positive integers, \(p\) ranges over rational primes, \(\omega(n)\) counts distinct prime factors, and the empty product equals one. The two independent-product constructions of \(B\) are the same. Convergence in distribution means convergence against each bounded continuous test function on \([0,1/2]\). The displayed moment identity covers every fixed positive integer \(r\); it is not a claim about moment-uniformity as \(r\) grows.

Define the multiplicative function \(b\) by \(b(1)=1\), \(b(2^a)=1/2\) for \(a\ge1\), and \(b(p^a)=1-2/p\) for each odd prime \(p\) and \(a\ge1\). Thus \(0<b(n)\le1\).

## Proof

**1. Uniform arithmetic approximation.** Let \(S(m)=m\prod_{p\mid m}(1-2/p)\) for odd \(m\); this counts residue classes modulo \(m\) avoiding \(0\) and \(1\) at every prime divisor. For odd \(n>1\), the two coprimality conditions on odd \(m\) mean \(m\not\equiv0,1\pmod p\) at every \(p\mid n\). By inclusion-exclusion, each divisor \(d\mid\operatorname{rad}(n)\) contributes \(2^{\omega(d)}\) residue classes modulo \(d\). Since \(n/d\) is odd, each of these classes has an odd-member count among \(1\le m\le n\) differing from \(n/(2d)\) by at most \(1/2\). Summing the absolute discrepancies gives
\[
\left|T(n)-\frac{S(n)}2\right|\le\frac{3^{\omega(n)}}2.
\]

For \(n=2m\) with \(m\) odd, set the candidate odd integer equal to \(2k+1\), with \(0\le k<m\). The conditions are that \(k\) be odd and avoid the two distinct classes \(k\equiv0,-2^{-1}\pmod p\) for every \(p\mid m\). The same inclusion-exclusion argument on the interval \(0\le k<m\), whose relevant residue progressions have odd length, gives \(\left|T(2m)-S(m)/2\right|\le3^{\omega(m)}/2\). When \(n=2^a m\), with \(m\) odd and \(a\ge2\), the admissible \(k\)'s have period \(2m\); each complete period contains exactly \(S(m)\) values, and the full interval consists of \(2^{a-2}\) periods. Hence \(T(2^a m)=2^{a-2}S(m)\) exactly. The convention \(T(1)=0\) and the case \(n=2\) satisfy the same bound directly. In all cases,
\[
\boxed{\left|2T(n)-n b(n)\right|\le3^{\omega(n)}.}\tag{1}
\]

**2. Random Euler product.** For a fixed finite set of primes, the divisibility events \(p\mid N_x\) converge jointly to independent Bernoulli events of probabilities \(1/p\), by counting the residue patterns using the Chinese remainder theorem. The product tail is uniformly small in mean: for \(y\ge3\),
\[
\left|\frac{b(n)}2-\frac12\prod_{p\le y}b_p^{\mathbf 1_{p\mid n}}\right|
\le\sum_{\substack{p>y\\p\mid n}}\frac1p.
\]
Indeed, each missing factor lies in \([0,1]\), and \(1-\prod(1-u_p)\le\sum u_p\); the factor of \(1/2\) cancels the \(2/p\). Averaging over \(n\le x\) gives a bound \(\sum_{p>y}p^{-2}\), uniform in \(x\). For the approximation (1), use \(3^{\omega(n)}\le d_3(n)\), where \(d_3\) is the ternary divisor function, to obtain
\[
\frac1{\lfloor x\rfloor}\sum_{n\le x}\left|\frac{T(n)}n-\frac{b(n)}2\right|
\ll\frac{(\log(2x))^3}{x}.
\]
These estimates and finite-prime convergence establish the stated limiting distribution and, by boundedness, the moment convergence.

**3. Positivity, absence of atoms, and moments.** For odd primes, \(-\log(1-2/p)\ll1/p\) outside finitely many small primes, so \(\sum_p\mathbb E[-I_p\log b_p]<\infty\); the infinite product is therefore positive almost surely. The finite products \(\prod_{p\le y}b_p^{i_p}\) for binary assignments \(i_p\) are all distinct. To see this, take the largest prime \(q\) at which two assignments differ: the ratio of the two products has \(q\)-adic valuation \(1\) or \(-1\), because every factor attached to a smaller prime has numerator and denominator strictly below \(q\); for \(q=2\), the distinct factor \(1/2\) gives the same conclusion. Conditional on the independent tail past \(y\), the probability of any prescribed positive value of \(B\) is therefore at most
\[
\prod_{p\le y}\max\left(\frac1p,1-\frac1p\right)
=\prod_{p\le y}\left(1-\frac1p\right)\longrightarrow0.
\]
Euler's divergence of \(\sum_p1/p\) proves that there are no atoms. Independence gives \(\mathbb E[X^r]=2^{-r}\prod_p(1-1/p+b_p^r/p)\), which is the displayed formula after separating \(p=2\). Each Euler product converges absolutely, because its odd-prime factors equal \(1+O_r(p^{-2})\).

**4. Summatory asymptotic.** Let \(h=b*\mu\), so that \(b=1*h\) in Dirichlet convolution. The function \(h\) is supported on squarefree integers with \(h(2)=-1/2\) and \(h(p)=-2/p\) for odd primes. In particular, \(|h(d)|\le2^{\omega(d)}/d\). Elementary divisor bounds yield
\[
\sum_{d\le x}|h(d)|\ll(\log(2x))^2,
\qquad \sum_{d>x}\frac{|h(d)|}{d}\ll\frac{\log(2x)}x.
\]
Consequently, using \(\sum_{m\le z}m=z^2/2+O(z)\),
\[
\sum_{n\le x}n b(n)
=\sum_{d\le x}d h(d)\sum_{m\le x/d}m
=\frac{x^2}{2}\sum_{d\ge1}\frac{h(d)}d
+O\!\left(x(\log(2x))^2\right).
\]
The constant is \(\sum h(d)/d=(1-1/4)\prod_{p\ge3}(1-2/p^2)\). Finally \(\sum_{n\le x}3^{\omega(n)}\ll x(\log(2x))^2\) by \(3^{\omega(n)}\le d_3(n)\). Summing (1) gives the formula with \(C=\frac14\sum h(d)/d\).

## Verification

Run `python3 verify.py` using Python's standard library. The program independently counts the defining coprime pairs for each \(1\le n\le1200\), checks the sharp type-by-type arithmetic comparison (1) exactly using rational arithmetic, verifies the exact \(4\)-divisible case, and approximates the convergent leading constant from primes through \(200000\). Its recorded output appears in `verification_output.txt`. These finite checks validate implementations and boundary conventions; neither infinitely many moments nor atomlessness is inferred from them.

## Relationship to prior work

Renshaw introduced \(T(n)\), its relation to Schemmel's totient, the exact \(4\)-divisible formula, and pointwise error bounds. The present distributional theorem is a new global question for that nonmultiplicative function; the approximation in Step 1 can also be verified directly as shown. Steuding and Suriajaya determined mean values of generalized multiplicative Schemmel functions \(\varphi_m(n)=n\prod_{p\mid n}(1-m/p)\). Their \(m=2\) function vanishes at even integers and is not \(T(n)\), nor the multiplicative surrogate \(b(n)\), whose local value at the prime \(2\) is \(1/2\). Their mean theorem is related background, not an atomless limiting law for the present statistic. Standard independence of finitely many prime-divisibility events supplies a method but does not by itself identify the explicit infinite law or establish its lack of atoms.

## Limitations

The theorem does not claim a density function, an optimal remainder exponent, an effective Kolmogorov distance, or any security property. The published analogues for generalized Schemmel functions make an implicit equivalent derivation conceivable. The numerical decimal for \(C\) is illustrative, not an exact certified error interval; the Euler product is its exact definition. No independent validation has been performed.

## References

1. J. Renshaw, *A Totient Function Associated with Variants of Groups*, arXiv:2603.13939, first posted 2026-03-14, https://arxiv.org/abs/2603.13939 .
2. J. Steuding and A. I. Suriajaya, *Mean-values associated with a generalized Schemmel function*, Ann. Univ. Sci. Budapest., Sect. Comput. 54 (2023), https://doi.org/10.71352/ac.54.307 .
3. C. Defant, *On Arithmetic Functions Related to Iterates of the Schemmel Totient Functions*, J. Integer Seq. 18 (2015), arXiv:1506.05426, https://arxiv.org/abs/1506.05426 .

# A sharp real-rootedness boundary for maxima of binomial counts

## Finding

Let \(n,m\) be positive integers, let \(0<p<1\), and let \(X_1,\ldots,X_m\) be independent \(\operatorname{Bin}(n,p)\) variables. Put \(M=\max_iX_i\), and write \(G_{n,m,p}(z)=\mathbb E[z^M]\). Call a nonnegative integer-valued distribution *Poisson-binomial* if it is the distribution of a sum of finitely many independent Bernoulli variables, including degenerate ones.

**Theorem.** For every fixed integer \(m\ge2\), the polynomial \(G_{n,m,p}\) is real-rooted for **every** \(0<p<1\) if and only if \(n\le2\). More precisely:

1. If \(n=1\) or \(n=2\), \(M\) is Poisson-binomial for every \(m\ge2\) and every \(0<p<1\). For \(n=2\) all the roots are distinct and strictly negative.
2. If \(n\ge3\), for every fixed \(m\ge2\) there exists \(\varepsilon_{n,m}>0\) such that \(M\) is **not** Poisson-binomial whenever \(0<p<\varepsilon_{n,m}\).
3. For the first non-universal case \(n=3,m=2\), the **full** parameter classification is exact: \(M\) is Poisson-binomial if and only if \(p\ge p_*\), where \(p_*\in(0,1)\) is the unique root of

\[
Q(p)=4p^6+8p^3+3p^2+6p-1=0.
\]

Numerically \(p_*\approx0.150732465335916\). At equality the generating polynomial has a repeated negative real root; below it, it has one negative real root and one nonreal conjugate pair.

This is one integrated boundary/classification result. The statement concerns real-rootedness (equivalently, independent-Bernoulli representability), **not** ordinary or ultra log-concavity.

## Assumptions and scope

All trials are independent, have the same success probability \(p\in(0,1)\), and use the same positive integer binomial trial count \(n\). The sample size \(m\ge2\) is an integer. The assertion in part 2 is an existence statement for a small-\(p\) interval for each specified \((n,m)\); it does not classify every \(p\) when \(n\ge3\). Part 3 provides the complete \(p\)-classification only when \((n,m)=(3,2)\).

A normalized polynomial with nonnegative coefficients is the probability-generating polynomial of a sum of independent Bernoulli variables exactly when all its zeros are real: if the zeros are real, coefficient positivity makes them strictly negative whenever the constant and leading coefficients are positive, after which factorization and evaluation at \(z=1\) give the Bernoulli factors. See Tang and Tang, Theorem 4.1, which states the classical Aissen--Schoenberg--Whitney characterization.

## Proof

Define \(F_{-1}(p)=0\) and, for \(0\le k\le n\),

\[
F_k(p)=\sum_{j=0}^k{n\choose j}p^j(1-p)^{n-j}.
\]

Independence of the \(m\) copies gives \(\Pr(M\le k)=F_k(p)^m\), so

\[
G_{n,m,p}(z)=\sum_{k=0}^n\left(F_k(p)^m-F_{k-1}(p)^m\right)z^k.\tag{1}
\]

**Case \(n\le2\).** For \(n=1\), \(M\) is Bernoulli with success probability \(1-(1-p)^m\). For \(n=2\), put \(q=1-p\), \(A=q^{2m}\), and \(B=(1-p^2)^m=q^m(1+p)^m\). Formula (1) reduces to

\[
G_{2,m,p}(z)=A+(B-A)z+(1-B)z^2.
\]

Its discriminant is

\[
(B-A)^2-4A(1-B)=(A+B)^2-4A
=q^{2m}\left(\left[(1-p)^m+(1+p)^m\right]^2-4\right).
\]

The function \(x\mapsto x^m\) is strictly convex on positive numbers when \(m\ge2\), hence \((1-p)^m+(1+p)^m>2\). Therefore the discriminant is strictly positive. All three coefficients are positive, so both roots are distinct and negative, proving part 1.

**Failure of universal preservation when \(n\ge3\).** For fixed positive integers \(n,m\), the small-\(p\) expansions from (1) are

\[
\Pr(M=0)=1+O(p),\qquad
\Pr(M=k)=m{n\choose k}p^k+O(p^{k+1}),\quad1\le k\le n.
\]

Indeed, \(1-F_{k-1}(p)={n\choose k}p^k+O(p^{k+1})\), and \(1-F_k(p)=O(p^{k+1})\). Consequently the degree-\(n\) polynomials satisfy coefficientwise, and uniformly on compact complex sets,

\[
G_{n,m,p}(t/p)\ \longrightarrow\ 1+m\sum_{k=1}^n{n\choose k}t^k
=m(1+t)^n-(m-1).\tag{2}
\]

The limiting polynomial has the simple roots

\[
t_j=-1+\left(\frac{m-1}{m}\right)^{1/n}\exp\!\left(\frac{2\pi i j}{n}\right),\quad j=0,\ldots,n-1.
\]

At least one root is nonreal when \(n\ge3\). By continuity of roots of fixed-degree polynomials, the degree-\(n\) approximants in (2) also have a nonreal root for all sufficiently small positive \(p\). Rescaling the indeterminate does not change whether a root is real. Thus \(G_{n,m,p}\) is not real-rooted on some interval \((0,\varepsilon_{n,m})\), proving part 2 and the universal sharpness of \(n=2\).

**Exact first phase transition.** When \(n=3,m=2\), direct expansion of (1) gives \(G_{3,2,p}(z)=a+bz+cz^2+dz^3\), with \(q=1-p\) and

\[
\begin{aligned}
a&=q^6,\\
b&=3pq^4(2+p),\\
c&=3p^2q^2(2+2p-p^2),\\
d&=p^3(2-p^3).
\end{aligned}
\]

All four coefficients are strictly positive for \(0<p<1\). The discriminant \(b^2c^2-4ac^3-4b^3d-27a^2d^2+18abcd\) factors exactly as

\[
\operatorname{Disc}_zG_{3,2,p}=108p^6(1-p)^{12}\bigl(4p^6+8p^3+3p^2+6p-1\bigr).\tag{3}
\]

Here \(Q(0)=-1\), \(Q(1)=20\), and

\[
Q'(p)=24p^5+24p^2+6p+6>0\quad(0\le p\le1).
\]

There is exactly one interior threshold \(p_*\). A real cubic with positive leading coefficient has three real roots, counted with multiplicities, exactly when its discriminant is nonnegative; otherwise it has one real root and a nonreal conjugate pair. Positivity of \(a,b,c,d\) rules out nonnegative real roots. Combining this fact with (3) yields the exact classification in part 3. The simple zero of \(Q\) implies the discriminant vanishes simply at \(p_*\), so the repeated root there is double, not triple. This completes the proof.

## Verification

The standalone `checker.py` uses only Python 3's standard library. Run `python checker.py` from the directory containing this document. It recomputes the exact mass polynomials for the first phase transition, reconstructs their cubic discriminant and verifies identity (3) as an integer-polynomial identity. It also checks exact coefficient expansions for \(1\le n\le8\), \(1\le m\le6\), and checks the \(n=2\) discriminant on an exact rational grid for \(1\le m\le35\). The run passed 2,615 exact algebraic and finite checks.

The universal claims depend on the complete symbolic arguments above, not on the finite grid. The floating-point decimal for \(p_*\) is informative only; the exact threshold is defined by \(Q(p_*)=0\).

## Relationship to prior work

Badiella, del Castillo and Puig (2023), Theorem 2, show that discrete order statistics preserve ultra log-concavity. This theorem applies to binomial maxima but does not imply the stronger real-rooted or Poisson-binomial property; its accessible full article develops synchronized log-concave sequences, not a sharp root classification. Kim, Kim and Lee (2018) establish preservation of strong unimodality (ordinary log-concavity), likewise a weaker property. Tang and Tang (2019), Theorem 4.1, review the general equivalence of Poisson-binomial laws, real-rooted probability-generating polynomials, and Pólya-frequency sequences; this criterion supplies the interpretation of the present polynomial classification but does not itself determine the binomial-maximum parameter boundary.

Unlike generic assertions that strong real-rootedness need not survive an operation, the theorem determines the **largest binomial trial size at which preservation holds for every sample size and parameter**, plus the **exact probability boundary in the first failing size**. No identical statement was identified in the searched mathematical records or accessible prior claims; this limited search does not certify absolute novelty.

## Limitations

There is no assertion that all cases with \(n\ge3\) fail: the \((3,2)\) phase diagram proves that some larger success probabilities do give Poisson-binomial maxima. No all-\(p\) classification is proved for general \(n\ge3,m\ge2\). The proof of existence of \(\varepsilon_{n,m}\) does not give an optimized numerical cutoff. Earlier unindexed results, including terminology in reliability theory and Pólya-frequency sequences, could contain equivalent statements. Independent external verification has not been performed.

## References

1. L. Badiella, J. del Castillo, P. Puig, *Ultra log-concavity of discrete order statistics*, Statistics & Probability Letters **201** (2023), 109900. First publicly available online 2023-06-26. DOI: https://doi.org/10.1016/j.spl.2023.109900.
2. B. Kim, J. Kim, S. Lee, *Strong unimodality of discrete order statistics*, Statistics & Probability Letters **140** (2018). DOI: https://doi.org/10.1016/j.spl.2018.04.018.
3. W. Tang, F. Tang, *The Poisson binomial distribution -- Old & New*, arXiv:1908.10024, first posted 2019-08-27; Theorem 4.1. https://arxiv.org/abs/1908.10024.
4. M. Aissen, I. J. Schoenberg, A. Whitney, *On the generating functions of totally positive sequences. I*, Journal d'Analyse Mathématique **2** (1952), 93--103.

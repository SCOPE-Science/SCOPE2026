# Logarithmic runner-up gap and two-adic concentration for the arithmetic derivative

## Finding

For the arithmetic derivative \(D\) and each integer \(k\ge2\), let
\[
M_k=\max_{1\le n<2^k}D(n),\qquad G_k=k2^{k-1}-M_k.
\]
The familiar dyadic value \(D(2^k)=k2^{k-1}\) is strictly greater than \(M_k\). The exact **order** of the first drop below the dyadic endpoint is logarithmic after normalization by \(2^k\).

Define
\[
b=\frac{\log 2}{3\log 3},\qquad c=\frac12-b,\qquad
\gamma=\frac{c}{\log2}+c\log_2\!\left(\frac{b\log2}{c}\right).
\]
Here logarithms without subscripts are natural. Numerically \(b\approx0.210309918\), \(c\approx0.289690082\), and \(\gamma\approx0.130921163\). For every \(k\ge2\),
\[
\boxed{\quad 2^k(c\log_2 k+\gamma)\le G_k
\le 2^{k-1}(\log_2 k+2).\quad}
\]
Hence \(G_k=\Theta(2^k\log k)\) as \(k\to\infty\), or equivalently
\[
\frac{M_k}{k2^{k-1}}=1-\Theta\!\left(\frac{\log k}{k}\right).
\]
If \(n_k\) is *any* maximizer in \(M_k\) and \(t_k=k-\nu_2(n_k)\), then
\[
\boxed{\quad
\log_2\!\left(\frac{2bk}{\log_2k+2}\right)\le t_k\le
\frac{\log_2k+2}{2c},\qquad
0<1-\frac{n_k}{2^k}\le\frac{\log_2k+2}{k}.
\quad}
\]
Thus every runner-up has \(\nu_2(n_k)=k-O(\log k)\), and its distance below \(2^k\) is at most \(O(2^k\log k/k)\).

## Assumptions and scope

The arithmetic derivative on positive integers is the unique function satisfying \(D(p)=1\) for every prime and the Leibniz rule \(D(ab)=aD(b)+bD(a)\). Its explicit factorization formula is
\[
D(n)=n\sum_{p\mid n}\frac{\nu_p(n)}p,\qquad D(1)=0.
\]
The theorem concerns all integers \(k\ge2\), the entire interval of positive integers \(1\le n<2^k\), and *every* maximizing integer, without assuming uniqueness of the runner-up. The logarithmic-order constants need not be optimal.

## Proof

**1. A uniform odd-factor estimate.** For any odd positive integer \(m\), write
\[
S(m)=\sum_{p\mid m}\frac{\nu_p(m)}p.
\]
Since the real function \(u\mapsto u\log u\) is increasing for \(u\ge3\), every odd prime \(p\) satisfies
\[
\frac1p\le\frac{\log p}{3\log3}.
\]
Multiplying by the prime exponents and adding gives
\[
0\le S(m)\le\frac{\log m}{3\log3}
=b\log_2m.
\]
The same inequality holds for \(m=1\), with empty sum.

**2. The exact deficit identity and its lower bound.** Take any \(1\le n<2^k\), write uniquely \(n=2^a m\), where \(a=\nu_2(n)\ge0\) and \(m\) is odd, and put \(t=k-a\). Thus \(1\le t\le k\) and \(1\le m\le2^t-1\). Set \(x=m/2^t\), so \(0<x\le1-2^{-t}\). The factorization formula yields
\[
\frac{D(2^k)-D(n)}{2^k}
=\frac{k}{2}(1-x)+x\left(\frac t2-S(m)\right).
\]
The odd-factor estimate gives \(S(m)\le bt\), whence the right-hand side is at least
\[
\frac{k}{2}(1-x)+ctx.
\]
Because \(t\le k\) and \(c<1/2\), this last affine function decreases in \(x\). Substituting its maximum feasible argument \(x=1-2^{-t}\) gives
\[
\frac{D(2^k)-D(n)}{2^k}
\ge ct+\left(\frac k2-ct\right)2^{-t}
\ge ct+bk2^{-t}.
\tag{1}
\]
The last inequality uses \(k/2-ct\ge(1/2-c)k=bk\). In particular the deficit is positive.

**3. Continuous minimization.** The function \(f_k(u)=cu+bk2^{-u}\) is strictly convex on the real line. Its unique minimum occurs at
\[
u_0=\log_2\!\left(\frac{bk\log2}{c}\right),
\]
and its minimum equals
\[
f_k(u_0)=c\log_2k+\gamma.
\]
Applying this to (1) and then taking the maximum of \(D(n)\) over \(n<2^k\) proves
\[
G_k\ge2^k(c\log_2k+\gamma).
\]

**4. A near-endpoint competitor.** Choose \(t=\lceil\log_2k\rceil\le k\) and
\[
n=2^{k-t}(2^t-1)<2^k.
\]
The arithmetic derivative is nonnegative, so \(D(n)\ge n(k-t)/2\). Hence
\[
\frac{G_k}{2^k}\le\frac{k2^{-t}}2+
\frac{(1-2^{-t})t}{2}
\le\frac{1+t}{2}\le\frac{\log_2k+2}{2}.
\]
Together with the lower bound, this gives the two-sided inequality and the \(\Theta\)-law.

**5. Localization of every runner-up.** If \(n_k\) maximizes \(D(n)\) below \(2^k\), apply (1) with \(t=t_k\). The established upper bound for \(G_k/2^k\) implies separately
\[
ct_k\le\frac{\log_2k+2}{2},\qquad
bk2^{-t_k}\le\frac{\log_2k+2}{2}.
\]
These rearrange to the two bounds on \(t_k\). Finally the exact deficit identity and \(t/2-S(m)\ge ct>0\) show
\[
\frac{k}{2}\left(1-\frac{n_k}{2^k}\right)
\le\frac{G_k}{2^k}
\le\frac{\log_2k+2}{2},
\]
which establishes the relative-distance bound. Since \(t_k=O(\log k)\), also \(\nu_2(n_k)=k-O(\log k)\). This finishes the proof.

## Verification

A self-contained exact-integer verifier, `verify_gap.py`, computes \(D(n)\) by the recurrence \(D(pq)=q+pD(q)\) with \(p\) the least prime divisor of \(n\), independently determines \(M_k\), and checks the displayed bounds at high-precision numerical tolerance for every \(2\le k\le20\). Those finite checks test implementation and small boundary cases, not the universal theorem. The proof above is self-contained and requires no numerical assumptions.

## Relationship to prior work

Barbeau (1961) developed classical bounds for the arithmetic derivative. Ufnarovski and Åhlander (2003) give its factorization rule and related arithmetic differential equations. Dahl, Olsson and Loiko (2011, §3.2, Theorem 3.2.1) establish that powers of two set derivative records. OEIS A131116 and A131117 tabulate record values and arguments. The present statement quantifies the **second-best dyadic gap** for an unbounded sequence of intervals and forces **two-adic concentration of all maximizers**. A maximal-value statement or a finite table alone does not yield the proved logarithmic gap or the uniform location bounds. Related published arithmetic-derivative investigations concern multiplier equations and small-support inequalities, not this dyadic runner-up invariant.

## Limitations

The constants are explicit but are not claimed to be asymptotically optimal; the result does not identify the exact maximizing integer for arbitrary \(k\), does not establish its uniqueness, and does not yield an asymptotic leading constant for \(G_k/(2^k\log k)\). Literature priority is assessed from the inspected sources and searches, not mathematically guaranteed. Independent external validation has not been performed.

## References

- E. J. Barbeau, *Remarks on an Arithmetic Derivative*, Canadian Mathematical Bulletin **4** (1961), 117–122, DOI 10.4153/CMB-1961-013-0.
- V. Ufnarovski and B. Åhlander, *How to Differentiate a Number*, Journal of Integer Sequences **6** (2003), Article 03.3.4, https://cs.uwaterloo.ca/journals/JIS/VOL6/Ufnarovski/ufnarovski.pdf.
- N. Dahl, J. Olsson and A. Loiko, *Investigations on the Properties of the Arithmetic Derivative*, arXiv:1108.4762v1, first posted 2011-08-24, https://arxiv.org/abs/1108.4762.
- OEIS, A003415 (arithmetic derivative), A131116 (record values), A131117 (record locations), https://oeis.org/A003415, https://oeis.org/A131116, https://oeis.org/A131117.

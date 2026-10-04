# Parity-resolved divisor-power sums for \(q=2\)

## Finding
For real \(s\), let
\[
E_s(n)=\sigma_s(n,2,0)-\sigma_s(n,2,1),
\]
where
\[
\sigma_s(n,2,a)=\sum_{\substack{d\mid n\\ d\equiv a\pmod2}}d^s.
\]
Thus \(E_s(n)\) is the sum of \(s\)-th powers of the even divisors minus the corresponding sum over odd divisors.

Write
\[
n=2^a m,\qquad a=v_2(n),\qquad m\ \text{odd}.
\]
Then the exact identity
\[
E_s(n)=\sigma_s(m)\left(\sum_{j=1}^{a}2^{js}-1\right)
\]
holds for every real \(s\), with the empty sum interpreted as \(0\).

This gives a complete pointwise sign classification. If \(s\le-1\), then \(E_s(n)<0\) for every positive integer \(n\). If \(s>0\), then \(E_s(n)<0\) exactly for odd \(n\) and \(E_s(n)>0\) exactly for even \(n\). If \(s=0\), then the sign is negative, zero, or positive according as \(v_2(n)=0\), \(v_2(n)=1\), or \(v_2(n)\ge2\).

For \(-1<s<0\), define
\[
G_a(s)=\sum_{j=1}^{a}2^{js},\qquad
A(s)=\min\{a\ge1:G_a(s)\ge1\}.
\]
Then \(A(s)\) exists and \(E_s(n)<0\) exactly when \(v_2(n)<A(s)\). If \(G_{A(s)}(s)>1\), then \(E_s(n)>0\) exactly when \(v_2(n)\ge A(s)\). If \(G_{A(s)}(s)=1\), then \(E_s(n)=0\) exactly when \(v_2(n)=A(s)\), and \(E_s(n)>0\) exactly when \(v_2(n)>A(s)\).

Hence the natural density of negative values for \(-1<s<0\) is
\[
1-2^{-A(s)}.
\]
If \(G_{A(s)}(s)>1\), the positive density is \(2^{-A(s)}\). If \(G_{A(s)}(s)=1\), the zero and positive densities are both \(2^{-A(s)-1}\).

In particular, the pointwise sequence \(E_s(n)\) has infinitely many adjacent nonzero sign changes for every \(s>-1\), while for \(s\le-1\) it is strictly negative everywhere.

There is also a summatory bias on the entire negative-\(s\) half-line. For every fixed \(s<0\),
\[
\sum_{n\le x}E_s(n)=(2^s-1)\zeta(1-s)x+o(x).
\]
Since \((2^s-1)\zeta(1-s)<0\), the summatory difference is eventually negative for every \(s<0\). Thus for \(-1<s<0\), the pointwise sequence changes sign infinitely often even though its cumulative sum eventually has one fixed negative sign.

## Assumptions and scope
The parameter \(s\) is any fixed real number and \(n\) ranges over positive integers. The notation \(\sigma_s(n,2,a)\) is exactly the residue-class divisor sum proposed in Problem 15 of Pongsriiam's paper.

The pointwise theorem is complete for the modulus \(q=2\). The summatory theorem proved here covers every \(s<0\). No claim is made for the eventual sign of the summatory difference when \(s\ge0\).

“Adjacent nonzero sign changes” means that there are infinitely many integers \(N\) for which \(E_s(N-1)\) and \(E_s(N)\) are both nonzero and have opposite signs.

## Proof
Let \(n=2^a m\) with \(m\) odd. Every divisor of \(n\) has the unique form \(2^j d\) with \(0\le j\le a\) and \(d\mid m\). The odd divisors are exactly the terms with \(j=0\), so
\[
\sigma_s(n,2,1)=\sigma_s(m).
\]
The even divisors are exactly the terms with \(1\le j\le a\), hence
\[
\sigma_s(n,2,0)=\sigma_s(m)\sum_{j=1}^{a}2^{js}.
\]
Subtracting gives the stated factorization. Because \(\sigma_s(m)>0\), the sign is exactly the sign of \(G_a(s)-1\).

For \(s>0\), one has \(G_a(s)>1\) whenever \(a\ge1\), while \(G_0(s)=0\). For \(s=0\), \(G_a(0)=a\). For \(s=-1\),
\[
G_a(-1)=1-2^{-a}<1.
\]
If \(s<-1\), then
\[
G_a(s)<\sum_{j=1}^{\infty}2^{js}=\frac{2^s}{1-2^s}<1.
\]
Thus every value is negative when \(s\le-1\).

Now suppose \(-1<s<0\). Then \(1/2<2^s<1\), and
\[
\lim_{a\to\infty}G_a(s)=\frac{2^s}{1-2^s}>1.
\]
Since \(G_a(s)\) is strictly increasing in \(a\), \(A(s)\) exists and the threshold classification follows immediately.

For densities, the valuation classes satisfy
\[
d\{n:v_2(n)=a\}=2^{-a-1},\qquad d\{n:v_2(n)\ge a\}=2^{-a}.
\]
Summing the relevant valuation classes gives the formulas above.

For adjacent sign changes, if \(s>0\), every odd integer is negative and every even integer is positive. If \(s=0\), each multiple of \(4\) is positive and its predecessor is odd and negative. If \(-1<s<0\) and the threshold is strict, each suitable multiple of \(2^{A(s)}\) is positive and its predecessor is odd and negative; if equality occurs at the threshold, use multiples of \(2^{A(s)+1}\). Hence infinitely many adjacent nonzero sign changes occur for every \(s>-1\).

For the summatory assertion, define
\[
\varepsilon(d)=\begin{cases}1,&2\mid d,\\-1,&2\nmid d.\end{cases}
\]
Then
\[
E_s(n)=\sum_{d\mid n}\varepsilon(d)d^s,
\]
so
\[
\sum_{n\le x}E_s(n)=\sum_{d\le x}\varepsilon(d)d^s\left\lfloor\frac{x}{d}\right\rfloor.
\]
For fixed \(s<0\),
\[
\sum_{d=1}^{\infty}\varepsilon(d)d^{s-1}=(2^s-1)\zeta(1-s),
\]
because the even and odd parts of the absolutely convergent series are \(2^{s-1}\zeta(1-s)\) and \((1-2^{s-1})\zeta(1-s)\), respectively.

Using \(\lfloor x/d\rfloor=x/d+O(1)\) and the tail of the convergent main series gives
\[
\sum_{n\le x}E_s(n)=(2^s-1)\zeta(1-s)x+R_s(x),
\]
where
\[
R_s(x)=\begin{cases}
O_s(x^{s+1}),&-1<s<0,\\
O(\log x),&s=-1,\\
O_s(1),&s<-1.
\end{cases}
\]
In every case \(R_s(x)=o(x)\), proving the summatory asymptotic.

## Verification
The accompanying `verify.py` checks the exact factorization formula against direct divisor enumeration for representative parameters \(s\in\{-2,-1,-1/2,0,1/2,1,2\}\) and all \(1\le n\le5000\). It also checks the predicted sign classes and the threshold rule for \(s=-1/2\).

As a separate summatory regression, it evaluates the divisor-swapped cumulative formula through \(x=200000\) for several negative values of \(s\) and compares the normalized value with \((2^s-1)\zeta(1-s)\).

The finite checks are regression tests only. The theorem itself is proved symbolically above.

## Relationship to prior work
Pongsriiam defines \(\sigma_s(n,q,a)\) in Problem 15 and asks, specifically for \(q=2\), about sign changes between the even-divisor and odd-divisor power sums and about the corresponding cumulative sums.

The later paper of Ding, Pan, and Sun solves several other sign-change problems from Pongsriiam. Its inspected full text does not discuss Problem 15, odd-versus-even divisor sums, or the \(q=2\) residue-class divisor-power comparison treated here.

For \(s=1\), the classical sequence measuring the excess of odd-divisor sum over even-divisor sum is OEIS A002129. That database entry records formulas and generating functions for this single parameter value, but not the real-parameter threshold classification above and not the negative-\(s\) summatory asymptotic.

Targeted literature and database searches for the exact \(q=2\) formulation, the threshold \(A(s)\), and the constant \((2^s-1)\zeta(1-s)\) did not locate a prior statement of this combined result.

## Limitations
The summatory result is restricted to \(s<0\). The behavior for \(s\ge0\) is not asserted. The modulus \(q=2\) is special because parity reduces the divisor comparison to a single \(2\)-adic valuation. No general modulus-\(q\) classification follows automatically.

Literature non-detection cannot exclude an equivalent statement in an unindexed source.

## References
1. Prapanpong Pongsriiam, “Sums of divisors on arithmetic progressions,” arXiv:2110.00237v1, first posted 1 October 2021; primary MSC \(11A25\). Problem 15 asks about \(\sigma_s(n,q,a)\), including the \(q=2\) odd/even divisor comparison.
2. Yuchen Ding, Hao Pan, and Yu-Chen Sun, “Solutions to some sign change problems on functions involving sums of divisors,” arXiv:2401.09842v1.
3. OEIS A002129, the classical odd-versus-even divisor-sum excess for the single case \(s=1\).

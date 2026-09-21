# Exact two-prime-support criterion for Carmichael subset-sum practical numbers

Let \(\lambda\) be the Carmichael function, with \(\lambda(1)=1\). Following Schwab and Thompson, call \(n\) **\(\lambda^\star\)-practical** when every integer in
\[
[1,S_\lambda(n)],\qquad S_\lambda(n)=\sum_{d\mid n}\lambda(d),
\]
is a subset sum of the multiset \(\{\lambda(d):d\mid n\}\), with each divisor used at most once.

The criterion below completely decides \(\lambda^\star\)-practicality on the family \(2^a p^b\) with \(a\ge 3\) and \(p\) odd prime. As a consequence, it gives an explicit infinite family large enough to yield a polynomial lower bound for the counting function \(F_{\lambda^\star}(X)\).

## Theorem

Let \(a\ge 3\), \(b\ge 1\), and let \(p\) be an odd prime. Write
\[
q=p-1,\qquad t=v_2(q),\qquad S_0=2^{a-1}+2,
\]
and define
\[
C=C(a,p):=\sum_{i=0}^{a}\frac{\operatorname{lcm}(q,\lambda(2^i))}{q}.
\]
Then
\[
C=
\begin{cases}
a+1,& a\le t+2,\\[2mm]
t+1+2^{a-t-1},& a>t+2.
\end{cases}
\]

The integer \(2^a p^b\) is \(\lambda^\star\)-practical if and only if
\[
p^{j-1}q\le S_0+C\bigl(p^{j-1}-1\bigr)+1
\tag{1}
\]
for every \(1\le j\le b\).

Equivalently:

- if \(C\ge q\), then \(2^a p^b\) is \(\lambda^\star\)-practical for every \(b\ge1\) exactly when \(q\le S_0+1\);
- if \(C<q\), then \(2^a p^b\) is \(\lambda^\star\)-practical exactly when
\[
p^{b-1}(q-C)\le S_0+1-C.
\tag{2}
\]

### Corollary 1: the squarefree odd part

For \(a\ge3\) and odd prime \(p\),
\[
2^a p\text{ is }\lambda^\star\text{-practical}
\quad\Longleftrightarrow\quad
p\le 2^{a-1}+3.
\tag{3}
\]

### Corollary 2: a lower bound for the counting function

Let
\[
F_{\lambda^\star}(X)=\#\{n\le X:n\text{ is }\lambda^\star\text{-practical}\}.
\]
Then
\[
F_{\lambda^\star}(X)\ge (1-o(1))\frac{\sqrt X}{\log X},
\qquad X\to\infty.
\tag{4}
\]
In particular,
\[
F_{\lambda^\star}(X)\gg \frac{\sqrt X}{\log X}.
\]

Schwab and Thompson proved the upper bound \(F_{\lambda^\star}(X)\ll X/\log X\) and stated that they had been unable to prove a reasonable lower bound. Equation (4) supplies a polynomial-order lower bound, although it remains far below the empirically suggested \(X/\log X\) scale.

## Proof

We use the standard complete-sequence criterion: positive integers \(w_1\le\cdots\le w_r\) have every subset sum from \(0\) to \(\sum_iw_i\) if and only if \(w_1=1\) and
\[
w_{k+1}\le 1+\sum_{i\le k}w_i
\]
for every \(k\).

### 1. The \(2\)-power block

For \(i\ge0\),
\[
\lambda(2^i)=1,1,2,2,4,8,\ldots
\]
(the values at \(i=0,1,2,3,\ldots\)). For \(a\ge3\), these weights form a complete sequence, and their total is
\[
\sum_{i=0}^a\lambda(2^i)
=1+1+2+\sum_{i=3}^a2^{i-2}
=2^{a-1}+2=S_0.
\tag{5}
\]

### 2. The blocks with positive \(p\)-adic exponent

For \(j\ge1\),
\[
\lambda(p^j)=p^{j-1}q.
\]
Since every \(\lambda(2^i)\) is a power of \(2\) and \(p\nmid q\),
\[
\lambda(2^ip^j)
=\operatorname{lcm}(\lambda(2^i),p^{j-1}q)
=p^{j-1}\operatorname{lcm}(\lambda(2^i),q).
\tag{6}
\]

Thus the block of weights belonging to divisors \(2^ip^j\), \(0\le i\le a\), is \(p^{j-1}q\) times the integer multiset
\[
\left\{\frac{\operatorname{lcm}(q,\lambda(2^i))}{q}:0\le i\le a\right\}.
\tag{7}
\]
Its smallest weight is \(p^{j-1}q\), and its total weight is
\[
p^{j-1}qC.
\tag{8}
\]

Because \(t=v_2(q)\ge1\), the normalized multiset in (7) consists of \(1\)'s followed, when \(a>t+2\), by
\[
2,4,\ldots,2^{a-t-2}.
\]
More precisely, if \(a\le t+2\) all \(a+1\) entries are \(1\); otherwise there are \(t+3\) initial \(1\)'s and the displayed powers of \(2\). Therefore its sum is
\[
C=
\begin{cases}
a+1,&a\le t+2,\\
(t+3)+\sum_{r=1}^{a-t-2}2^r
=t+1+2^{a-t-1},&a>t+2,
\end{cases}
\]
as claimed.

Once the smallest weight of one such block can be appended to an already complete interval, the rest of that block can also be appended: equal initial weights cause no gap, and every later doubled weight is at most the accumulated weight of the earlier entries of the same block.

### 3. The exact gap condition

Before the \(j\)-th positive-\(p\) block is added, the total weight already available is
\[
\begin{aligned}
P_{j-1}
&=S_0+qC(1+p+\cdots+p^{j-2})\\
&=S_0+C(p^{j-1}-1),
\end{aligned}
\tag{9}
\]
because \(q=p-1\).

Hence the \(j\)-th block can be appended without a gap exactly when its least weight satisfies
\[
p^{j-1}q\le P_{j-1}+1
=S_0+C(p^{j-1}-1)+1,
\]
which is (1).

This condition is also necessary. If it fails for some \(j\), then every weight in the \(j\)-th and all later blocks exceeds \(P_{j-1}+1\), while the sum of all preceding weights is exactly \(P_{j-1}\). Thus \(P_{j-1}+1\) is not representable.

Rearranging (1) gives
\[
(q-C)p^{j-1}\le S_0+1-C.
\tag{10}
\]
If \(C\ge q\), the left side is nonincreasing as a constraint in \(j\), so the first case \(j=1\), namely \(q\le S_0+1\), is sufficient for all \(j\). If \(C<q\), the left side increases with \(j\), so the endpoint \(j=b\) is the strongest condition, giving (2).

For \(b=1\), (1) reduces to
\[
p-1\le 2^{a-1}+3.
\]
Since \(p\) is odd and \(2^{a-1}+4\) is even, this is equivalent to (3).

### 4. Counting consequence

For sufficiently large \(X\), let \(z=2^a\) be the least power of \(2\) with \(z\ge\sqrt X\). Then
\[
\sqrt X\le z<2\sqrt X.
\]
Put
\[
Y=\min\!\left(\frac z2,\frac Xz\right).
\]
Both terms are at least \(\sqrt X/2\), so
\[
Y\ge\frac{\sqrt X}{2}.
\tag{11}
\]

For every odd prime \(p\le Y\), we have \(zp\le X\) and
\[
p\le \frac z2=2^{a-1}\le2^{a-1}+3.
\]
By Corollary 1, \(zp\) is \(\lambda^\star\)-practical. These integers are distinct as \(p\) varies. Hence
\[
F_{\lambda^\star}(X)\ge \pi(Y)-1.
\]
Since \(Y\in[\sqrt X/2,\sqrt X]\), the prime number theorem gives
\[
\pi(Y)=(1+o(1))\frac{Y}{\log Y}
\ge(1-o(1))\frac{\sqrt X}{\log X},
\]
proving (4).

## Computational verification

A standalone verifier checks the theorem directly from the divisor weights, without using the theorem to compute \(\lambda^\star\)-practicality. It compares the direct complete-sequence test with (1) for

\[
3\le a\le12,\qquad 3\le p<300\text{ prime},\qquad 1\le b\le5.
\]

It checks 3050 triples and finds zero mismatches. It separately checks the threshold (3) on 610 \((a,p)\) pairs and again finds zero mismatches. See `artifacts/verify.py` and `artifacts/verification.txt`.

## Relation to prior literature and limitations

Schwab and Thompson introduced \(f\)-practical numbers and treated the Carmichael function separately because \(\lambda\) is only nearly multiplicative. Their Proposition 1.1 is the complete-sequence criterion used above. In Section 5.2 they defined \(\lambda^\star\)-practical numbers, proved
\[
F_{\lambda^\star}(X)\ll \frac{X}{\log X},
\]
and explicitly reported that they did not have a reasonable lower bound. Their general prime-adjunction theorem is stated for multiplicative \(f\), so it does not directly apply to the Carmichael function.

The current OEIS entry A336508 records the same \(\lambda^\star\)-practical sequence and cites Schwab--Thompson. Searches for the exact terminology, the family \(2^a p^b\), the threshold (3), equivalent Carmichael subset-sum language, and lower bounds for \(F_{\lambda^\star}\) did not locate a prior classification or the lower bound (4). Originality is therefore asserted only **to the best of our knowledge**.

The result is restricted to integers supported on \(\{2,p\}\), with \(a\ge3\). The lower bound (4) does not settle whether the true order of \(F_{\lambda^\star}(X)\) is \(X/\log X\). No formal proof-assistant verification or independent audit is asserted.

## References

1. Nicholas Schwab and Lola Thompson, *A generalization of the practical numbers*, International Journal of Number Theory 14 (2018), 1487--1503. arXiv:1701.08504.  
   https://arxiv.org/abs/1701.08504  
   https://doi.org/10.1142/S1793042118500902
2. OEIS A336508, “lambda*-practical” numbers.  
   https://oeis.org/A336508

# Exponentially sharp logarithmic asymptotics for totative dominance thresholds

## Statement

For \(n\ge 2\), write
\[
A(n)=\pi(n)-\omega(n),\qquad B(n)=\varphi(n)-\pi(n)+\omega(n).
\]
Following Fatehizadeh, let \(N_k\) be the least integer such that
\[
\varphi(n)>k\pi(n)\qquad(n\ge N_k),
\]
and let \(M_k\) be the least integer such that
\[
B(n)>kA(n)\qquad(n\ge M_k).
\]
Fatehizadeh proved \(M_k\le N_{k+1}\) for every \(k\ge1\), determined \(N_1,\ldots,N_6\) and \(M_1,\ldots,M_5\) exactly, and conjectured \(M_k=N_{k+1}\) for all \(k\ge1\).

Let \(\gamma\) be Euler's constant and, for sufficiently large real \(h\), let \(Y(h)>e\) be the large solution of
\[
e^{-\gamma}\frac{Y(h)}{\log Y(h)}=h.
\]
Equivalently,
\[
Y(h)=-e^\gamma h\,W_{-1}\!\left(-\frac{e^{-\gamma}}h\right),
\]
where \(W_{-1}\) is the lower real branch of the Lambert \(W\)-function.

**Theorem.** There is an absolute constant \(c>0\) such that, as \(k\to\infty\),
\[
\boxed{\log N_k=Y(k)\left(1+O\!\left(e^{-c\sqrt{\log k}}\right)\right)}
\]
and
\[
\boxed{\log M_k=Y(k+1)\left(1+O\!\left(e^{-c\sqrt{\log k}}\right)\right)}.
\]
Consequently,
\[
\boxed{0\le \log\frac{N_{k+1}}{M_k}
\ll k\log k\,e^{-c\sqrt{\log k}}.}
\]
Thus the conjectured equality \(M_k=N_{k+1}\), while not proved here, holds to exponentially small relative error on the logarithmic scale.

Expanding the Lambert inverse gives the explicit form
\[
\boxed{
\log N_k=e^\gamma k\left(
\log k+\log\log k+\gamma
+\frac{\log\log k+\gamma}{\log k}
+O\!\left(\frac{(\log\log k)^2}{(\log k)^2}\right)
\right).
}
\]
The identical expansion with \(k\) replaced by \(k+1\) holds for \(\log M_k\). In particular,
\[
\log N_k\sim e^\gamma k\log k,
\qquad
\log M_k\sim e^\gamma (k+1)\log(k+1).
\]

## Proof

Put
\[
F(y)=e^{-\gamma}\frac{y}{\log y}\qquad(y>e).
\]
The proof has two parts: a uniform lower envelope for the ratios and matching primorial witnesses.

### 1. Uniform lower envelope

Let \(p_j\#=\prod_{i\le j}p_i\), and for a given large \(n\) choose \(j\) so that
\[
p_j\#\le n<p_{j+1}\#.
\]
Fatehizadeh's primorial-extremality lemma gives
\[
\frac{n}{\varphi(n)}\le \prod_{p\le p_j}\frac{p}{p-1}.
\]
Write \(x=p_j\) and \(y=\log n\). The classical zero-free-region form of the prime number theorem and the corresponding Mertens product estimate give, for some \(c_0>0\),
\[
\vartheta(x)=x\left(1+O(E(x))\right),
\qquad
\prod_{p\le x}\frac{p}{p-1}
=e^\gamma\log x\left(1+O(E(x))\right),
\]
where
\[
E(x)=e^{-c_0\sqrt{\log x}}.
\]
Since
\[
\vartheta(p_j)\le y<\vartheta(p_{j+1})
=\vartheta(p_j)+\log p_{j+1}
\]
and Bertrand's postulate gives \(p_{j+1}<2p_j\), one has
\[
y=x\left(1+O(E(x))\right).
\]
Hence, after decreasing the positive constant in the exponential error if necessary,
\[
\frac{n}{\varphi(n)}
\le e^\gamma\log y\left(1+O(e^{-c_1\sqrt{\log y}})\right).
\]
The prime number theorem in the form
\[
\frac{n}{\pi(n)}=y-1+O(y^{-1})
\]
therefore yields
\[
\frac{\varphi(n)}{\pi(n)}
\ge F(y)\left(1-O(e^{-c_2\sqrt{\log y}})\right).
\tag{1}
\]
Because \(A(n)=\pi(n)-\omega(n)\le\pi(n)\), one also has
\[
\frac{\varphi(n)}{A(n)}\ge \frac{\varphi(n)}{\pi(n)},
\tag{2}
\]
so the same lower envelope applies to the second threshold problem after the shift \(k\mapsto k+1\), since
\[
B(n)>kA(n)\quad\Longleftrightarrow\quad \varphi(n)>(k+1)A(n).
\]

### 2. Matching primorial witnesses

For real \(x\ge2\), put
\[
P(x)=\prod_{p\le x}p.
\]
Then \(\log P(x)=\vartheta(x)\), and the same prime-number and Mertens estimates give
\[
\frac{\varphi(P(x))}{\pi(P(x))}
=F(x)\left(1+O(e^{-c_3\sqrt{\log x}})\right).
\tag{3}
\]
Indeed, \(\varphi(P(x))/P(x)\) is the Mertens product, while
\[
\frac{P(x)}{\pi(P(x))}
=\log P(x)-1+O\!\left(\frac1{\log P(x)}\right)
=\vartheta(x)\left(1+o(e^{-c_3\sqrt{\log x}})\right).
\]
Moreover \(\omega(P(x))=\pi(x)\), whereas \(\pi(P(x))\) is of exponential size in \(x\). Thus
\[
\frac{\varphi(P(x))}{A(P(x))}
=F(x)\left(1+O(e^{-c_4\sqrt{\log x}})\right).
\tag{4}
\]

Now let \(h\to\infty\) and put \(Y=Y(h)\). Since \(F(Y)=h\),
\[
\frac{F'(Y)}{F(Y)}
=\frac{\log Y-1}{Y\log Y}
=\frac{1+o(1)}Y.
\]
Also \(Y(h)\asymp h\log h\) and \(\log Y(h)\sim\log h\). Choose a sufficiently small positive \(c\) and set
\[
\eta_h=e^{-c\sqrt{\log h}}.
\]
Equations (1)--(4), with \(c\) chosen smaller than the constants in their error terms, imply the following for a sufficiently large fixed \(C\):

- if \(\log n\ge Y(1+C\eta_h)\), then \(\varphi(n)/\pi(n)>h\) and \(\varphi(n)/A(n)>h\);
- at \(x=Y(1-C\eta_h)\), the primorial \(P(x)\) satisfies both \(\varphi(P(x))/\pi(P(x))<h\) and \(\varphi(P(x))/A(P(x))<h\).

Finally,
\[
\log P(x)=\vartheta(x)=x\left(1+o(\eta_h)\right).
\]
Thus the last failure of either inequality with level \(h\) has logarithm
\[
Y(h)\left(1+O(\eta_h)\right).
\]
Taking \(h=k\) gives the formula for \(N_k\); taking \(h=k+1\) gives the formula for \(M_k\). Passing from the last failure to the least eventual threshold by adding \(1\) changes its logarithm by a negligible amount. Fatehizadeh's inequality \(M_k\le N_{k+1}\) then gives the displayed one-sided comparison.

### 3. Lambert-W expansion

Let \(a=e^\gamma h\) and write \(Y(h)=at\). The defining equation becomes
\[
\frac{e^t}{t}=a,
\]
so \(t=-W_{-1}(-1/a)\). With \(L_1=\log a\) and \(L_2=\log L_1\), the standard large-\(a\) expansion is
\[
t=L_1+L_2+\frac{L_2}{L_1}
+O\!\left(\frac{L_2^2}{L_1^2}\right).
\]
Since \(L_1=\log h+\gamma\), substitution gives
\[
Y(h)=e^\gamma h\left(
\log h+\log\log h+\gamma
+\frac{\log\log h+\gamma}{\log h}
+O\!\left(\frac{(\log\log h)^2}{(\log h)^2}\right)
\right).
\]
The threshold-localization error is smaller than every fixed negative power of \(\log h\), so it does not alter any displayed term.

## Relation to the recent threshold problem

Fatehizadeh's current preprint proves exact values only for \(N_1,\ldots,N_6\) and \(M_1,\ldots,M_5\), together with \(M_k\le N_{k+1}\) and the conjecture \(M_k=N_{k+1}\) for all \(k\). The theorem above addresses a different axis: it determines the growth of both threshold sequences as the dominance parameter \(k\) tends to infinity. The final comparison shows that the two conjecturally identical thresholds have logarithms differing by at most
\[
O\!\left(k\log k\,e^{-c\sqrt{\log k}}\right),
\]
which is smaller than \(k/(\log k)^A\) for every fixed \(A>0\).

OEIS A080289 records finite data for integers at which \(\varphi(n)/\pi(n)\) is smaller than at every subsequent integer; it provides historical computational context for the first threshold sequence but does not state an asymptotic formula for \(N_k\).

## Limitations

The result is asymptotic in \(k\) and is not intended to predict the small exact thresholds efficiently. It does not prove the exact conjecture \(M_k=N_{k+1}\), does not assert that the last failures are always primorials, and does not optimize the constant \(c\) in the exponential error. The proof uses classical zero-free-region estimates for the prime number theorem and Mertens' prime product; stronger known zero-free regions could sharpen the displayed error without changing the main mechanism.

Originality is asserted only to the best of our knowledge. The motivating preprint is very recent, so unindexed contemporaneous work remains a residual risk.

## References

1. A. Fatehizadeh, *Prime and Nonprime Totatives: A Sharp Construction and Exact Thresholds*, arXiv:2609.13852v1 (2026).
2. J. B. Rosser and L. Schoenfeld, *Approximate formulas for some functions of prime numbers*, Illinois J. Math. 6 (1962), 64--94.
3. M. Just, *Numbers which are only orders of abelian or nilpotent groups*, J. Théorie des Nombres de Bordeaux 35 (2023), 453--466. Lemma 8 records the de la Vallée Poussin-strength Mertens product estimate used above.
4. C. Sanna, *A new elementary proof of the inequality \(\varphi(n)>\pi(n)\)*, Notes on Number Theory and Discrete Mathematics 18 (2012), 35--37.
5. OEIS A080289, integers at which \(\varphi(n)/\pi(n)\) is smaller than at every subsequent integer.

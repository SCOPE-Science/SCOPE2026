# Second-order digital oscillation for distinct substrings of a uniform random word

## Result

Let \(X_1,\dots,X_n\) be i.i.d. uniform on an alphabet of fixed size \(d\ge2\). For each \(k\), let \(D_{n,k}\) be the number of distinct consecutive substrings of length \(k\), and let
\[
D_n=\sum_{k=1}^n D_{n,k},\qquad
T_n=\frac{n(n+1)}2,\qquad
R_{n,d}=T_n-\mathbb E D_n.
\]

Set
\[
a_n=\log_d n,\qquad \theta_n=\{a_n\},
\]
and define
\[
f(x)=1-x(1-e^{-1/x}),\qquad x>0.
\]
For \(0\le\theta<1\), define
\[
\mathcal P_d(\theta)
=
-\theta
+\sum_{j\le0}\bigl(f(d^{j-\theta})-1\bigr)
+\sum_{j\ge1}f(d^{j-\theta}).
\]
Both series converge absolutely. The endpoint values match, so this defines a continuous one-periodic function.

Then, for every fixed \(d\ge2\),
\[
\boxed{
R_{n,d}
=
n\log_d n
+
n\,\mathcal P_d(\{\log_d n\})
+
O_d((\log n)^2).
}
\]
Equivalently,
\[
\boxed{
\mathbb E D_n
=
\frac{n(n+1)}2
-
n\log_d n
-
n\,\mathcal P_d(\{\log_d n\})
+
O_d((\log n)^2).
}
\]

Thus the first logarithmic deficit has coefficient one, and the entire linear-order correction is an explicit digital oscillation in the fractional part of \(\log_d n\).

The periodic function has the absolutely convergent Fourier series
\[
\boxed{
\mathcal P_d(\theta)
=
-\frac12+\frac{\gamma-1}{\log d}
+
\sum_{\ell\ne0}
\frac{\Gamma(1-\chi_\ell)}
{\log d\,\chi_\ell(1+\chi_\ell)}
e^{2\pi i\ell\theta},
\qquad
\chi_\ell=\frac{2\pi i\ell}{\log d},
}
\]
where \(\gamma\) is Euler's constant. In particular its phase average is
\[
\boxed{
\int_0^1\mathcal P_d(\theta)\,d\theta
=
-\frac12+\frac{\gamma-1}{\log d}.
}
\]

For \(d=2\), the mean is
\[
-1.109948863612096\ldots,
\]
and the peak-to-peak digital oscillation is only about
\[
3.45\times10^{-7}.
\]
For comparison, the peak-to-peak amplitudes are about \(8.25\times10^{-5}\) for \(d=3\), \(5.92\times10^{-4}\) for \(d=4\), and \(1.25\times10^{-2}\) for \(d=10\).

A finite elementary sandwich, independent of the analytic input below, is also useful. If
\[
m=\lfloor\log_d n\rfloor,\qquad N_k=n-k+1,
\]
then
\[
\boxed{
\sum_{k=1}^m(N_k-d^k)
\le
R_{n,d}
\le
\sum_{k=1}^mN_k
+
\sum_{k=m+1}^n {N_k\choose2}d^{-k}.
}
\]
This already gives
\[
R_{n,d}=n\log_d n+O_d(n).
\]

Finally, if
\[
M_{n,d}=\max_{w\in[d]^n}D_n(w),
\]
then
\[
0\le M_{n,d}-\mathbb E D_n=O_d(n),
\]
and the elementary sandwich gives the explicit bound
\[
0\le M_{n,d}-\mathbb E D_n
\le\frac{3dn}{2(d-1)}.
\]

## Proof

### 1. Reduction to an independent-occupancy profile

Gheorghiciuc and Ward (2007), Corollary 2.2, prove a uniform approximation for the expected \(k\)-th subword complexity. Their parameter \(N\) is the number of length-\(k\) windows, so a word of total length \(n\) corresponds to
\[
N=N_k=n-k+1.
\]
For the uniform \(d\)-ary source, their result gives constants \(\varepsilon>0\) and \(0<\mu<1\), depending only on \(d\), such that
\[
\mathbb E D_{n,k}
=
d^k-d^k(1-d^{-k})^{N_k}
+
O_d(N_k^{-\varepsilon}\mu^k).
\]
Their theorem explicitly allows \(N\) and \(k\) to vary together. Since \(N_k\ge1\),
\[
\sum_{k=1}^n N_k^{-\varepsilon}\mu^k=O_d(1).
\]
Therefore
\[
R_{n,d}
=
\sum_{k=1}^n H(N_k,d^k)+O_d(1),
\]
where
\[
H(N,Q)=N-Q+Q(1-Q^{-1})^N.
\]

This identifies the all-length expectation, up to bounded total error, with the deficit in an independent occupancy model having \(N_k\) draws from \(d^k\) boxes at level \(k\).

### 2. Replacing the varying number of windows

For integer \(N\ge0\),
\[
H(N+1,Q)-H(N,Q)
=
1-(1-Q^{-1})^N
\le \min\{1,N/Q\}.
\]
Hence
\[
|H(N_k,d^k)-H(n,d^k)|
\le
(k-1)\min\{1,n/d^k\}.
\]
Summing over \(k\) and splitting at \(\lfloor\log_d n\rfloor\) gives
\[
\sum_{k=1}^n
|H(N_k,d^k)-H(n,d^k)|
=
O_d((\log n)^2).
\]

Next,
\[
H(n,Q)=n-Q+Q(1-Q^{-1})^n,
\]
whereas
\[
n f(Q/n)=n-Q+Qe^{-n/Q}.
\]
For \(Q\ge2\),
\[
0\le e^{-n/Q}-(1-Q^{-1})^n
\le
e^{-n/Q}\frac{n/Q^2}{1-1/Q},
\]
so
\[
|H(n,Q)-nf(Q/n)|
\le
2(n/Q)e^{-n/Q}.
\]
Along the geometric grid \(Q=d^k\), the sum of the right-hand side is \(O_d(1)\). Therefore
\[
R_{n,d}
=
n\sum_{k\ge1}f(d^k/n)
+
O_d((\log n)^2),
\]
where extending the sum past \(k=n\) changes it by an exponentially small amount.

### 3. Extracting the digital phase

Write
\[
\log_d n=m+\theta,\qquad m\in\mathbb Z_{\ge0},\quad 0\le\theta<1.
\]
Changing variables \(k=m+j\),
\[
\sum_{k\ge1}f(d^k/n)
=
\sum_{j=1-m}^{\infty}f(d^{j-\theta}).
\]
Since
\[
f(x)=1-x+O(xe^{-1/x})\quad(x\downarrow0),
\qquad
f(x)=\frac1{2x}+O(x^{-2})\quad(x\to\infty),
\]
the defining series for \(\mathcal P_d\) converges absolutely, and
\[
\sum_{k\ge1}f(d^k/n)
=
m+\theta+\mathcal P_d(\theta)+O_d(d^{-m}).
\]
Because \(d^{-m}=O_d(n^{-1})\), multiplying by \(n\) gives the stated second-order expansion.

### 4. Fourier representation

The Mellin transform of \(f\), initially for \(0<\Re s<1\), is
\[
\mathcal M f(s)
=
\int_0^\infty f(x)x^{s-1}\,dx
=
\frac{\Gamma(1-s)}{s(1+s)}.
\]
One convenient derivation uses
\[
f(1/y)
=
1-\frac{1-e^{-y}}y
=
\int_0^1(1-e^{-ty})\,dt.
\]

Mellin inversion for the geometric sum yields
\[
\sum_{k\ge1}f(d^k/n)
=
\frac1{2\pi i}
\int
\frac{\Gamma(1-s)}
{s(1+s)(d^s-1)}
n^s\,ds.
\]
The poles of \((d^s-1)^{-1}\) are
\[
\chi_\ell=\frac{2\pi i\ell}{\log d},\qquad \ell\in\mathbb Z.
\]
The double pole at \(s=0\) contributes
\[
\log_d n-\frac12+\frac{\gamma-1}{\log d},
\]
and each nonzero \(\chi_\ell\) contributes
\[
\frac{\Gamma(1-\chi_\ell)}
{\log d\,\chi_\ell(1+\chi_\ell)}
e^{2\pi i\ell\log_d n}.
\]
The exponential decay of \(\Gamma(1-it)\) gives absolute convergence of the Fourier series and the displayed formula for \(\mathcal P_d\).

### 5. Elementary finite sandwich

For completeness, a proof not using the 2007 approximation gives the leading coefficient directly. Since at most \(d^k\) different length-\(k\) words exist,
\[
N_k-D_{n,k}\ge N_k-d^k.
\]
For the reverse direction, if \(M_w\) is the number of occurrences of a given length-\(k\) word,
\[
N_k-D_{n,k}
=
\sum_w(M_w-1)_+
\le
\sum_w{M_w\choose2}.
\]
Two distinct length-\(k\) windows match with probability exactly \(d^{-k}\), even when they overlap. If their shift is \(s<k\), equality imposes period \(s\) on the block of \(k+s\) letters, leaving \(s\) free letters, hence probability \(d^s/d^{k+s}=d^{-k}\). Thus
\[
\mathbb E(N_k-D_{n,k})
\le {N_k\choose2}d^{-k}.
\]
Using the deterministic bound for \(k\le m\) and the collision bound for \(k>m\) proves the finite sandwich and the \(n\log_d n+O_d(n)\) corollary.

The same sandwich also yields the additive comparison with the maximum. Every word has deficit at least the lower side \(L\), while the random expectation has deficit at most the upper side \(U\). Therefore
\[
M_{n,d}-\mathbb E D_n\le U-L.
\]
Using \(d^m\le n\) and \(d^{-m}\le d/n\) gives
\[
U-L\le\frac{3dn}{2(d-1)}.
\]

## Relation to prior literature

Gheorghiciuc and Ward (2007) are the essential prior input for the second-order theorem: they give a uniform fixed-length approximation to the expected subword complexity, valid even when the window count and substring length vary together. A uniform-source special case had already been obtained by Jacquet, Lučić and Szpankowski (2001), as noted in their paper. The contribution here is the all-length summation, its explicit linear-order digital phase, and the finite collision sandwich.

Flaxman, Harrow and Sorkin (2004) exactly determine the maximum number of distinct substrings using modified de Bruijn words. They also state that a random word is asymptotically optimal, with the only potentially nonoptimal length range lying between about \(\log_d n\) and \(2\log_d n\). Their comparison is on the leading \(n^2\) scale.

A 2016 MathOverflow comment by Anthony Quas already gives the correct heuristic
\[
\binom n2-\frac{n\log n}{\log d}
\]
for the random all-length count. Thus the coefficient-one logarithmic correction should not be regarded as a previously unsuspected phenomenon. The theorem above supplies a rigorous \(O_d(n)\) bound by an elementary argument and, using the 2007 profile theorem, resolves the full linear correction into an explicit periodic function with an \(O_d((\log n)^2)\) remainder.

Ahmadi and Ward (2020) give refined asymptotics for the \(k\)-th subword complexity when \(k=\Theta(\log n)\), especially for binary memoryless sources. Godbole (2026) recently returned explicitly to the all-length expectation; the bounds proved there start the binary summation at \(3\log_2n\) and the uniform \(d\ge3\) summation at \(2\log_dn\), and do not identify the linear digital correction above.

## Reproducibility

`artifacts/verify_bounds.py` exhaustively checks the elementary finite sandwich for all binary words through length 16 and all ternary words through length 10.

`artifacts/verify_second_order.py` evaluates the defining series and the Fourier series independently, compares them at multiple phases, reports the mean and peak-to-peak oscillations, and checks the occupancy proxy against the asymptotic formula over increasing \(n\). Its output is recorded in `artifacts/second_order_values.txt`.

## Limitations

The theorem assumes a fixed finite alphabet and uniform independent letters. The uniform fixed-level approximation of Gheorghiciuc and Ward is used as an input to obtain the \(O((\log n)^2)\) second-order remainder; the elementary collision proof alone gives only \(O(n)\). The result does not identify the next logarithmic-order phase term, does not cover general nonuniform memoryless sources, and does not address variance or concentration.

Originality is claimed only to the best of our knowledge. The explicit all-length periodic correction was not located in the inspected sources, but it is a natural Mellin summation of a 2007 profile theorem. Older trie/suffix-tree profile analyses, especially Jacquet–Lučić–Szpankowski and later trie-profile work, are therefore a material residual risk of equivalent implicit or explicit coverage.

## References

1. I. Gheorghiciuc and M. D. Ward, *On Correlation Polynomials and Subword Complexity*, DMTCS Proceedings AH (2007), 1–18. https://doi.org/10.46298/dmtcs.3553
2. A. Flaxman, A. W. Harrow, G. B. Sorkin, *Strings with Maximally Many Distinct Subsequences and Substrings*, Electronic Journal of Combinatorics 11 (2004), R8. https://doi.org/10.37236/1761
3. L. Ahmadi and M. D. Ward, *Asymptotic Analysis of the kth Subword Complexity*, Entropy 22(2):207 (2020). https://doi.org/10.3390/e22020207
4. A. Godbole, *The Expected Number of Distinct Substrings in an Alphabet String*, arXiv:2609.19409 (2026). https://arxiv.org/abs/2609.19409
5. MathOverflow question 253576, *Expected number of substring in random string* (2016), including the Anthony Quas heuristic. https://mathoverflow.net/questions/253576/expected-number-of-substring-in-random-string

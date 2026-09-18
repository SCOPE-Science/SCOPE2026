# A reciprocal-weight criterion for periodic Paley–Wiener uniqueness

## Statement

Let \(A\subset[0,1]\) be measurable with \(0<|A|<1\), and put
\[
S=A+\mathbb Z.
\]
Let \(L:[1,\infty)\to(0,\infty)\) be measurable and dyadically comparable: there is \(D\ge1\) such that
\[
D^{-1}L(r)\le L(s)\le D L(r)
\qquad(r\ge1,\ r\le s\le 2r).
\]
Define
\[
W_L(t)=1+|t|L(1+|t|)
\]
and the weighted periodic-spectrum space
\[
PW_{S,L}
=
\left\{
f=\mathcal F^{-1}F:
\operatorname{supp}F\subset S,\ 
\|f\|_{S,L}^2:=\int_S W_L(t)|F(t)|^2\,dt<\infty
\right\}.
\]
For \(j\ge1\), set
\[
a_j=2^{-j}+L(2^j).
\]

Then there is an exact dichotomy.

1. If
\[
\sum_{j=1}^\infty \frac1{a_j}<\infty,
\]
then \(PW_{S,L}\subset C(\mathbb R)\), and \(PW_{S,L}\) has a uniformly discrete uniqueness set.

2. If
\[
\sum_{j=1}^\infty \frac1{a_j}=\infty,
\]
then no uniformly discrete set is a uniqueness set for
\[
PW_{S,L}\cap C(\mathbb R).
\]
More precisely, for every uniformly discrete \(\Lambda\subset\mathbb R\) and every \(x_0\notin\Lambda\), there exists
\[
f\in PW_{S,L}\cap C(\mathbb R)
\]
such that
\[
f(x_0)=1,\qquad f|_\Lambda=0.
\]

Consequently, for the logarithmic critical weights
\[
W_\beta(t)
=
1+|t|[\log(e+|t|)]^\beta,
\]
a uniformly discrete uniqueness set exists if and only if
\[
\boxed{\beta>1}.
\]
Thus the Sobolev threshold \(\alpha=\tfrac12\) for periodic weak gaps has a sharp logarithmic refinement: at the critical power \(|t|\), the extra factor \(\log^\beta(e+|t|)\) restores discrete uniqueness exactly when \(\beta>1\).

## Context

Olevskii and Ulanovskii proved that spectra with periodic weak gaps admit uniformly discrete uniqueness sets in Sobolev regularity \(\alpha>1/2\). Bertolini, Florit-Simon, Liehr and Taylor recently proved that for the full periodic spectrum \(S=A+\mathbb Z\), this power threshold is sharp: when \(\alpha\le1/2\), no uniformly discrete set is a uniqueness set for \(PW_S^{(\alpha)}\cap C\).

The result above resolves the boundary between those two regimes for a dyadically regular family of weights. It also identifies the mechanism governing the transition: summability of the reciprocal frequency weight after periodization. The logarithmic corollary is strictly finer than the power statement. In particular, \(|t|\log^\beta(e+|t|)\) with \(\beta>1\) is smaller than \(|t|^{1+\varepsilon}\) for every fixed \(\varepsilon>0\), yet already suffices for uniqueness.

## Proof

### 1. The reciprocal-weight series

For \(t\in[0,1]\), group \(k\in\mathbb Z\) by dyadic size \(2^j\le |k|<2^{j+1}\). Dyadic comparability gives, uniformly in \(t\),
\[
W_L(t+k)\asymp_D 1+2^jL(2^j).
\]
There are \(\asymp2^j\) integers in the \(j\)-th group, hence
\[
\sum_{k\in\mathbb Z}\frac1{W_L(t+k)}
\asymp_D
1+\sum_{j\ge1}
\frac{2^j}{1+2^jL(2^j)}
=
1+\sum_{j\ge1}\frac1{a_j}.
\tag{1}
\]
The comparison is uniform for \(t\in[0,1]\).

### 2. The summable case

Assume \(\sum_j a_j^{-1}<\infty\). By (1),
\[
\sup_{t\in[0,1]}
\sum_{k\in\mathbb Z}W_L(t+k)^{-1}<\infty.
\tag{2}
\]
For \(F\) supported in \(S=A+\mathbb Z\), weighted Cauchy–Schwarz therefore gives
\[
\int_S|F(t)|\,dt
\le
\left(\int_S W_L|F|^2\right)^{1/2}
\left(\int_S W_L^{-1}\right)^{1/2}<\infty.
\]
Thus every \(f\in PW_{S,L}\) has a continuous representative.

For \(v\in\mathbb R\), define on \([0,1]\)
\[
H_v(t)=
\sum_{k\in\mathbb Z}
e^{2\pi i v(t+k)}F(t+k).
\]
Again by (2),
\[
\|H_v\|_{L^2(0,1)}^2
\lesssim_D
\|f\|_{S,L}^2,
\tag{3}
\]
uniformly in \(v\). This is exactly the periodization estimate used in the Olevskii–Ulanovskii proof; their Sobolev hypothesis enters there through convergence of the reciprocal series.

Take their dense family of shifts \(v_m\) and integer sets \(Z_m\) such that
\[
\Lambda=\bigcup_m(Z_m+v_m)
\]
is uniformly discrete and each exponential system indexed by \(Z_m\) is complete in \(L^2(A)\). If \(f|_\Lambda=0\), then the Fourier coefficients of \(H_{v_m}\) indexed by \(Z_m\) vanish, so completeness gives
\[
H_{v_m}=0\quad\text{in }L^2(A)
\]
for every \(m\).

For almost every \(t\in A\), weighted Cauchy–Schwarz and (2) imply
\[
\sum_k|F(t+k)|<\infty.
\]
Hence \(v\mapsto H_v(t)\) is continuous. Since the \(v_m\) are dense, it vanishes for all \(v\). Uniqueness of Fourier series in the \(v\)-variable yields
\[
F(t+k)=0
\]
for every \(k\), for almost every \(t\in A\). Thus \(F=0\) and \(f=0\). This proves existence of a uniformly discrete uniqueness set.

### 3. A weighted finite-interpolation lemma in the divergent case

Assume now
\[
\sum_j a_j^{-1}=\infty.
\tag{4}
\]
The finite interpolation device in Bertolini–Florit-Simon–Liehr–Taylor can be reused with a different block averaging.

After a physical translation, take the interpolation point to be \(0\). For a compact \(K\) and a finite prescribed zero set, their bandlimited interpolation lemma supplies \(p\in PW_A\) with
\[
p(0)=1
\]
and with the required finite zeros, including the finitely many integers meeting \(K\).

For \(j\ge1\), let
\[
R_j(x)
=
2^{-j}\sum_{k=2^j}^{2^{j+1}-1}e^{2\pi i kx},
\qquad
f_j=pR_j.
\]
Then
\[
R_j(0)=1,
\]
the Fourier support of \(f_j\) lies in \(A+\mathbb Z\), and the Fourier supports of different \(f_j\) are disjoint. The standard geometric-sum estimate, together with the chosen zeros of \(p\) at the relevant integers, gives
\[
\sup_{x\in K}|f_j(x)|\longrightarrow0.
\tag{5}
\]

On the Fourier block \(A+k\) with \(2^j\le k<2^{j+1}\),
\[
W_L\asymp_D1+2^jL(2^j).
\]
Since \(R_j\) has \(2^j\) coefficients, all of size \(2^{-j}\),
\[
\|f_j\|_{S,L}^2
\lesssim_D
 a_j\|p\|_2^2.
\tag{6}
\]

Fix a large \(J\). For \(N\ge J\), define
\[
A_{J,N}=\sum_{j=J}^N a_j^{-1},
\qquad
c_j=\frac{a_j^{-1}}{A_{J,N}},
\qquad
g_{J,N}=\sum_{j=J}^N c_jf_j.
\]
Then \(\sum c_j=1\), so \(g_{J,N}(0)=1\), and all prescribed finite zeros are retained. By (5), choosing \(J\) large makes \(g_{J,N}\) uniformly small on \(K\), independently of \(N\). By disjoint Fourier supports and (6),
\[
\|g_{J,N}\|_{S,L}^2
\lesssim_D
\sum_{j=J}^N c_j^2a_j
=
\frac{C_D}{A_{J,N}}.
\tag{7}
\]
By (4), \(A_{J,N}\to\infty\), so the weighted norm can be made arbitrarily small.

Thus the finite interpolation proposition used in the recent endpoint nonuniqueness proof remains valid precisely under divergence of \(\sum a_j^{-1}\).

### 4. Passing from finite interpolation to an arbitrary uniformly discrete set

Enumerate a uniformly discrete \(\Lambda\) and apply the same successive-correction construction as in the proof of the recent periodic-gap endpoint theorem. At each stage, use the weighted finite-interpolation lemma above to correct the next sample while preserving the preceding zeros, making the correction arbitrarily small both in \(\|\cdot\|_{S,L}\) and uniformly on a prescribed compact set.

The corrections can be chosen summable in the weighted Hilbert norm and locally uniformly. Their sum therefore has Fourier transform supported in \(S\), belongs to \(PW_{S,L}\), and has a continuous representative. The interpolation conditions survive the limit, giving
\[
f(x_0)=1,\qquad f|_\Lambda=0.
\]
Hence no uniformly discrete \(\Lambda\) is a uniqueness set.

### 5. The logarithmic threshold

Take
\[
L(r)=[\log(e+r)]^\beta.
\]
This is dyadically comparable, and
\[
a_j
=
2^{-j}+[\log(e+2^j)]^\beta
\asymp_\beta j^\beta.
\]
Therefore
\[
\sum_j a_j^{-1}<\infty
\iff
\sum_j j^{-\beta}<\infty
\iff
\beta>1.
\]
This proves the stated sharp logarithmic transition.

## Limitations

The theorem is stated for the full one-dimensional periodic spectrum \(S=A+\mathbb Z\) and for weights with uniform dyadic comparability. The positive direction extends immediately to subsets of such periodic spectra, but the negative direction uses the availability of the full translated blocks \(A+k\). No claim is made here for arbitrary irregular weights, higher-dimensional periodic spectra, nonperiodic weak gaps, or quantitative sampling stability. The theorem concerns uniqueness, not stable sampling.

## References

1. S. Bertolini, E. Florit-Simon, L. Liehr, M. A. Taylor, *Universal completeness of exponentials*, arXiv:2609.20805 (2026). https://arxiv.org/abs/2609.20805
2. A. Olevskii, A. Ulanovskii, *Discrete uniqueness sets for functions with spectral gaps*, Sbornik: Mathematics 208 (2017), 864–877; arXiv:1609.04571. https://arxiv.org/abs/1609.04571

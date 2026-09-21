# Sharpness of all fractional trace-defect regimes for discrete Fourier concentration

## Main result

Let
\[
T_{\Omega,S}=P_\Omega B_S P_\Omega,\qquad
D(\Omega,S)=\operatorname{tr}(T_{\Omega,S}-T_{\Omega,S}^2),
\]
be the discrete Fourier concentration operator and its trace defect for finite
\(\Omega\subset\mathbb Z^d\) and measurable \(S\subset\mathbb T^d\).

Mayeli, arXiv:2609.12226, proves that if
\(\Omega_R=(RF)\cap\mathbb Z^d\), the boundary of \(F\) has an upper
Minkowski-neighborhood exponent \(\gamma\in(0,1]\), and \(S\) has spectral
translation exponent \(\eta\in(0,1]\), then
\[
D(\Omega_R,S)\lesssim
\begin{cases}
R^{d-\gamma}\log R,&\gamma=\eta,\\
R^{d-\eta},&\gamma>\eta,\\
R^{d-\gamma},&\gamma<\eta.
\end{cases}
\]
The source proves logarithmic sharpness for the classical endpoint
\(\gamma=\eta=1\), and its Remark 9.4 leaves sharpness for the fractional
critical line and both off-critical powers open.

Here all three regimes are shown to be sharp for every pair
\[
0<\gamma,\eta\le 1
\]
and every dimension \(d\ge1\).

More precisely, for every \(\theta\in(0,1]\) there is an explicit measurable
set \(E_\theta\subset(0,1)\) such that, for all sufficiently small \(h>0\),
\[
c_\theta h^\theta
\le
|E_\theta\triangle(E_\theta-h)|
\le
C_\theta h^\theta,
\tag{1}
\]
and
\[
|(\partial E_\theta)_h|\le C_\theta h^\theta.
\tag{2}
\]
For
\[
F_{\gamma,d}=E_\gamma\times(0,1)^{d-1},
\qquad
S_{\eta,d}=E_\eta\times\mathbb T^{d-1},
\]
and integers \(N\to\infty\),
\[
\Omega_N=(NF_{\gamma,d})\cap\mathbb Z^d
\]
satisfies
\[
\boxed{
D(\Omega_N,S_{\eta,d})\asymp
\begin{cases}
N^{d-\gamma}\log N,&\gamma=\eta,\\
N^{d-\eta},&\gamma>\eta,\\
N^{d-\gamma},&\gamma<\eta.
\end{cases}}
\tag{3}
\]
The implicit constants may depend on \(d,\gamma,\eta\), but not on \(N\).

Thus the logarithm on the whole critical line, including every
\(0<\gamma=\eta<1\), and both off-critical powers in Mayeli's theorem are
unimprovable at the level of the stated geometric/translation hypotheses.

## 1. An alternating-gap Cantor coloring with exact translation modulus

For \(\theta=1\), take any nontrivial interval \(E_1\subset(0,1)\). Then
\[
|E_1\triangle(E_1-h)|=2h
\]
for all sufficiently small \(h>0\), and (2) is immediate.

Now fix \(0<\theta<1\), and put
\[
\alpha=1-\theta.
\]
Choose an integer \(b\ge2\) sufficiently large that, with
\[
r=b^{-1/\alpha},
\]
one has
\[
(2b-1)r\le1.
\]
Set
\[
g=\frac{1-br}{b-1}.
\]
Then \(g\ge r\). Inside \([0,1]\), keep \(b\) intervals of length \(r\),
equally separated by gaps of length \(g\), and iterate the same construction
inside every retained interval. Let \(C_\theta\) be the resulting self-similar
Cantor set. At construction level \(n\), there are
\[
(b-1)b^{n-1}
\]
new gaps, each of length \(g r^{n-1}\).

Define \(E_\theta\) to be the union of the gaps born at odd levels. Gaps born
at even levels belong to the complement. The boundary of \(E_\theta\) is
exactly \(C_\theta\).

Since
\[
b r^\alpha=1,
\]
the Cantor set has similarity dimension \(\alpha=1-\theta\). If
\(r^m\le t<r^{m-1}\), covering \(C_\theta\) by its \(b^m\) level-\(m\)
cylinders gives
\[
|(C_\theta)_t|
\le 3b^m t
\lesssim t^{1-\alpha}
=t^\theta.
\tag{4}
\]
This proves (2).

A small endpoint-density observation gives the matching lower translation
bound. There is \(c_0>0\), depending only on the construction, such that for
every basic cylinder \(I\), every endpoint of \(I\), and every
\(0<t\le |I|\), the length-\(t\) subinterval at that endpoint contains at
least \(c_0t\) of each color, \(E_\theta\) and \(E_\theta^c\).

It is enough to check the left endpoint of the root interval. If
\(r^m\le t<r^{m-1}\), the first gaps born at levels \(m+1\) and \(m+2\)
are both contained in \([0,t]\), have opposite colors, and the smaller has
length
\[
g r^{m+1}\ge g r^2 t.
\]
Self-similarity gives the same assertion in every cylinder; replacing the
color by its complement does not affect the estimate.

Now fix small \(h>0\), and choose an odd integer \(n\) such that
\[
r^n\ge h>r^{n+2}.
\]
Every level-\(n\) gap lies in \(E_\theta\), has length at least \(h\), and
has immediately to its right a level-\(n\) basic interval of length
\(r^n\ge h\). Translate the last length-\(h\) piece of each such gap by
\(h\). By the endpoint-density observation, at least \(c_0h\) of its image
lies in \(E_\theta^c\). Distinct level-\(n\) gaps give disjoint source
pieces. Therefore
\[
|E_\theta\triangle(E_\theta-h)|
\ge c_0(b-1)b^{n-1}h
\gtrsim b^n h.
\]
Because \(h>r^{n+2}\) and \(b=r^{-\alpha}\),
\[
b^n h\gtrsim h^{1-\alpha}=h^\theta.
\tag{5}
\]
The reverse inequality follows from
\[
E_\theta\triangle(E_\theta-h)
\subseteq (\partial E_\theta)_h
\]
together with (4). This proves (1).

The same argument applies after identifying \([0,1)\) with \(\mathbb T\).
In particular \(E_\theta\) has exact small-translation exponent \(\theta\).

## 2. Fourier energy on every macroscopic annulus

Write
\[
\widehat{\mathbf 1_E}(k)
=
\int_{\mathbb T}\mathbf 1_E(x)e^{-2\pi ikx}\,dx.
\]
For an indicator,
\[
|E\triangle(E-h)|
=
\sum_{k\in\mathbb Z}
|e^{2\pi ikh}-1|^2
|\widehat{\mathbf 1_E}(k)|^2.
\tag{6}
\]

Suppose \(E=E_\theta\). From the upper half of (1), taking
\(h=(4L)^{-1}\), one gets for dyadic shells
\[
\sum_{L\le |k|<2L}
|\widehat{\mathbf 1_E}(k)|^2
\lesssim L^{-\theta}.
\tag{7}
\]
Consequently
\[
\sum_{|k|>BL}
|\widehat{\mathbf 1_E}(k)|^2
\lesssim B^{-\theta}L^{-\theta},
\tag{8}
\]
and
\[
L^{-2}\sum_{|k|<aL}
k^2|\widehat{\mathbf 1_E}(k)|^2
\lesssim
a^{2-\theta}L^{-\theta}+O(L^{-2}).
\tag{9}
\]

Apply (6) with \(h=L^{-1}\). The lower half of (1) gives
\[
|E\triangle(E-L^{-1})|\gtrsim L^{-\theta}.
\]
Choose \(a>0\) sufficiently small and \(B>1\) sufficiently large. Equations
(8)--(9) show that the frequencies \(|k|<aL\) and \(|k|>BL\) account for
less than half of this quantity for all large \(L\). Since the multiplier
in (6) is at most \(4\),
\[
\boxed{
\sum_{aL\le |k|\le BL}
|\widehat{\mathbf 1_{E_\theta}}(k)|^2
\gtrsim L^{-\theta}.
}
\tag{10}
\]
Thus the Fourier \(L^2\) mass predicted by the translation exponent occurs
on every sufficiently large multiplicative frequency annulus, not merely
along a sparse subsequence.

## 3. Discretization preserves the lower translation law

Let
\[
\Omega_{\theta,N}^{(1)}
=
(NE_\theta)\cap\mathbb Z
\]
and let \(U_{\theta,N}\) be the union of the grid cells
\([j/N,(j+1)/N)\) with \(j\in\Omega_{\theta,N}^{(1)}\). Every cell on
which \(U_{\theta,N}\) and \(E_\theta\) differ meets the boundary, hence
\[
|U_{\theta,N}\triangle E_\theta|
\lesssim N^{-\theta}.
\tag{11}
\]

For an integer \(k\),
\[
\frac1N
\#\bigl(
\Omega_{\theta,N}^{(1)}
\triangle
(\Omega_{\theta,N}^{(1)}-k)
\bigr)
=
|U_{\theta,N}\triangle(U_{\theta,N}-k/N)|.
\]
The symmetric-difference metric and (11) therefore imply
\[
\left|
\frac1N
\#\bigl(
\Omega_{\theta,N}^{(1)}
\triangle
(\Omega_{\theta,N}^{(1)}-k)
\bigr)
-
|E_\theta\triangle(E_\theta-k/N)|
\right|
\lesssim N^{-\theta}.
\tag{12}
\]
Combining (12) with the lower half of (1), there are constants
\(K_0\) and \(h_0>0\) such that
\[
\boxed{
\#\bigl(
\Omega_{\theta,N}^{(1)}
\triangle
(\Omega_{\theta,N}^{(1)}-k)
\bigr)
\gtrsim
N^{1-\theta}|k|^\theta
}
\tag{13}
\]
whenever
\[
K_0\le |k|\le h_0N
\]
and \(N\) is sufficiently large.

## 4. Trace-defect lower bounds

Mayeli's exact trace identity is
\[
D(\Omega,S)
=
\frac12
\sum_{k\in\mathbb Z^d}
|\widehat{\mathbf 1_S}(k)|^2
\#(\Omega\triangle(\Omega-k)).
\tag{14}
\]

For
\[
S_{\eta,d}=E_\eta\times\mathbb T^{d-1},
\]
the only nonzero Fourier coefficients occur at
\[
k=(m,0,\ldots,0),
\]
and they are \(\widehat{\mathbf 1_{E_\eta}}(m)\).

Likewise,
\[
\Omega_N
=
\Omega_{\gamma,N}^{(1)}
\times J_N^{d-1},
\qquad
J_N=(0,N)\cap\mathbb Z,
\]
so for such \(k\),
\[
\#(\Omega_N\triangle(\Omega_N-k))
=
|J_N|^{d-1}
\#
\bigl(
\Omega_{\gamma,N}^{(1)}
\triangle
(\Omega_{\gamma,N}^{(1)}-m)
\bigr).
\tag{15}
\]

### Critical case: \(\gamma=\eta=\theta\)

Choose a geometric sequence \(L_j\) whose annuli
\([aL_j,BL_j]\) from (10) are disjoint and lie inside
\([K_0,h_0N]\). There are \(\asymp\log N\) such annuli. On each one,
(10), (13), (14), and (15) give
\[
D_j
\gtrsim
N^{d-1}
N^{1-\theta}
L_j^\theta
L_j^{-\theta}
=
N^{d-\theta}.
\]
Summing the disjoint contributions,
\[
D(\Omega_N,S_{\theta,d})
\gtrsim
N^{d-\theta}\log N.
\tag{16}
\]
Mayeli's upper bound supplies the reverse inequality.

### Off-critical case: \(\gamma>\eta\)

Take one annulus in (10) at scale
\[
L=\delta N,
\]
where \(\delta>0\) is fixed small enough that \(BL<h_0N\). Then
(10), (13), (14), and (15) give
\[
D(\Omega_N,S_{\eta,d})
\gtrsim
N^{d-1}
N^{1-\gamma}
L^\gamma
L^{-\eta}
\asymp
N^{d-\eta}.
\tag{17}
\]
Again the source upper bound matches this power.

### Off-critical case: \(\gamma<\eta\)

Because \(E_\eta\) is nontrivial, its indicator has infinitely many nonzero
Fourier coefficients. Indeed, otherwise it would agree almost everywhere
with a trigonometric polynomial; a continuous trigonometric polynomial
taking only the values \(0\) and \(1\) almost everywhere must be constant.
Choose a fixed
\[
|m_*|\ge K_0
\]
with
\[
\widehat{\mathbf 1_{E_\eta}}(m_*)\ne0.
\]
The single term \(k=(m_*,0,\ldots,0)\) in (14), together with (13) and
(15), yields
\[
D(\Omega_N,S_{\eta,d})
\gtrsim
N^{d-\gamma}.
\tag{18}
\]
This matches the source upper bound.

Equations (16)--(18) prove (3).

## 5. Verification of the hypotheses

For
\[
F_{\gamma,d}=E_\gamma\times(0,1)^{d-1},
\]
the boundary consists of the fractal face
\(\partial E_\gamma\times[0,1]^{d-1}\) together with ordinary side faces.
Using (2),
\[
|(\partial F_{\gamma,d})_t|
\lesssim t^\gamma+t
\lesssim t^\gamma,
\qquad 0<t\le1.
\]
Hence \(F_{\gamma,d}\) satisfies the required upper Minkowski-neighborhood
estimate with exponent \(\gamma\).

For
\[
S_{\eta,d}=E_\eta\times\mathbb T^{d-1},
\]
translation in the last \(d-1\) coordinates does nothing, and (1) gives
\[
|S_{\eta,d}\triangle(S_{\eta,d}-h)|
\lesssim \rho(h,0)^\eta.
\]
Thus the required spectral translation seminorm of order \(\eta\) is finite.

Moreover, the lower half of (1) shows that the one-dimensional building
blocks really have the prescribed translation exponents; the construction
is not obtaining the lower bounds by assigning artificially weaker exponents
to smoother sets.

## Consequences

The examples settle the scaling-sharpness questions stated in Remark 9.4 of
arXiv:2609.12226:

1. the logarithmic factor is sharp for every critical exponent
   \(0<\gamma=\eta\le1\), not only at \(\gamma=\eta=1\);
2. when \(\gamma>\eta\), the power \(d-\eta\) is sharp;
3. when \(\gamma<\eta\), the power \(d-\gamma\) is sharp.

The proof also isolates a reusable mechanism: a two-sided translation law
for an indicator forces Fourier energy on every multiplicative annulus, while
a boundary-neighborhood estimate transfers the same scale law to lattice
symmetric differences after discretization.

## Limitations

The result concerns sharpness of the trace-defect growth rates under the
translation/Minkowski hypotheses. It does not optimize the multiplicative
constants, give second-order asymptotics, or determine the exact eigenvalue
profile inside the plunge region. The constructed sets are deliberately
self-similar and disconnected; no claim is made that the same fractional
rates are attained by connected domains or by boundaries with stronger
geometric regularity. The threshold dependence in eigenvalue-counting
estimates is not addressed.

## Literature context and originality

To the best of our knowledge, the result is new. The direct source,
arXiv:2609.12226, proves the three upper regimes, proves critical sharpness
only for the classical box endpoint, presents numerical experiments for
special fractal examples, and explicitly leaves the fractional critical and
off-critical sharpness questions open. Searches for the source identifier and
for combinations of discrete Fourier concentration, trace defect, fractal or
Cantor boundaries, translation seminorms, and plunge-region sharpness did not
locate a theorem implying (3).

Marceca--Romero--Speckbacher (2024) develops non-asymptotic eigenvalue
estimates for Fourier concentration operators on geometric domains, but its
regular-boundary framework does not provide the fractional self-similar
sharpness statement above.

Because the direct source is very recent, unindexed concurrent work remains
a residual originality risk. No inaccessible paper was identified whose
known statement gives substantial evidence of prior coverage of the
all-exponent construction or the three matching lower regimes.

## References

1. A. Mayeli, *Trace-defect bounds for discrete Fourier concentration
   operators*, arXiv:2609.12226 (2026).
   https://arxiv.org/abs/2609.12226

2. F. Marceca, J. L. Romero, M. Speckbacher, *Eigenvalue estimates for
   Fourier concentration operators on two domains*, Archive for Rational
   Mechanics and Analysis **248** (2024), Article 35.
   https://doi.org/10.1007/s00205-024-01979-9

# Sharp curvature-range envelopes and a minimax weight for symmetric three-point rules

## Statement

Let \(f\in C^2([a,b])\), \(h=b-a>0\), and
\[
m=\min_{[a,b]}f'',\qquad M=\max_{[a,b]}f''.
\]
For \(p\in\mathbb R\), define the symmetric endpoint-midpoint error
\[
T_p[f]
=p\frac{f(a)+f(b)}2+(1-p)f\!\left(\frac{a+b}{2}\right)
-\frac1h\int_a^b f(x)\,dx.
\]
Then the following sharp statement holds.

### Theorem

For a fixed \(p\), there is a finite constant \(C\) such that
\[
\left|T_p[f]-\lambda(m+M)h^2\right|
\le C(M-m)h^2                                                \tag{1}
\]
for every \(f\in C^2([a,b])\) only if
\[
\boxed{\lambda=\lambda_p:=\frac{3p-1}{48}}.                 \tag{2}
\]
For this unique centering, the least possible constant is
\[
\boxed{
C(p)=
\begin{cases}
\dfrac{1-3p}{48},&p\le0,\\[1.2ex]
\dfrac{1-3p+8p^3}{48},&0\le p\le\dfrac12,\\[1.2ex]
\dfrac{3p-1}{48},&p\ge\dfrac12.
\end{cases}}                                                 \tag{3}
\]
Thus
\[
\boxed{
\left|T_p[f]-\frac{3p-1}{48}(m+M)h^2\right|
\le C(p)(M-m)h^2}                                            \tag{4}
\]
is sharp for every real \(p\).

Moreover, \(C(p)\) has the unique global minimizer
\[
\boxed{p_*=\frac{1}{2\sqrt2}},\qquad
\boxed{C(p_*)=\frac{1-1/\sqrt2}{48}}.                       \tag{5}
\]
Numerically,
\[
p_*=0.353553390593\ldots,\qquad
C(p_*)=0.00610194205861\ldots .
\]

Finally, a finite *uncentered* oscillation estimate
\[
|T_p[f]|\le C(M-m)h^2\quad\text{for all }f\in C^2([a,b])     \tag{6}
\]
is possible if and only if \(p=1/3\). In that case the optimal constant is
\[
\boxed{C=\frac1{162}},                                       \tag{7}
\]
which is the Simpson weight.

The Simpson-specific sharp constant in (7) is not claimed here as new: it already follows from the sharp \(W^{2,\infty}\) Simpson estimate of Cruz-Uribe and Neugebauer (2002). The new claim is the all-\(p\) sharp curvature-range envelope (2)--(4), its unique centering property, and the minimax parameter (5), to the best of our knowledge.

## Proof

Simić and Bin-Mohsin (2021, Lemma 2.7) give the identity
\[
T_p[f]
=\frac{h^2}{16}\int_0^1 t(2p-t)
\bigl(f''(x_t)+f''(y_t)\bigr)\,dt,                           \tag{8}
\]
where
\[
x_t=a\frac t2+b\left(1-\frac t2\right),\qquad
y_t=b\frac t2+a\left(1-\frac t2\right).
\]
Put
\[
w_p(t)=t(2p-t),\qquad
g(t)=\frac{f''(x_t)+f''(y_t)}2.
\]
Then \(m\le g(t)\le M\) and
\[
T_p[f]=\frac{h^2}{8}\int_0^1 w_p(t)g(t)\,dt.                \tag{9}
\]
Also
\[
\int_0^1 w_p(t)\,dt=p-\frac13.                              \tag{10}
\]

### 1. The centering coefficient is forced

Add \(q x^2/2\) to \(f\). This translates both curvature extrema by \(q\), so \(M-m\) is unchanged and \(m+M\) increases by \(2q\). From (9)--(10), \(T_p\) increases by
\[
q h^2\frac{p-1/3}{8}
=q h^2\frac{3p-1}{24}.
\]
If (1) is to hold uniformly for arbitrary \(q\), the quadratic translation must cancel, forcing
\[
2\lambda=\frac{3p-1}{24},
\]
which is exactly (2).

### 2. Sharp centered envelope

Let
\[
c=\frac{m+M}{2},\qquad d=\frac{M-m}{2}.
\]
Using (9)--(10),
\[
T_p[f]-\lambda_p(m+M)h^2
=\frac{h^2}{8}\int_0^1w_p(t)(g(t)-c)\,dt.
\]
Since \(|g-c|\le d\),
\[
\left|T_p[f]-\lambda_p(m+M)h^2\right|
\le \frac{h^2(M-m)}{16}\int_0^1|w_p(t)|\,dt.                \tag{11}
\]
A direct integration gives
\[
\int_0^1|w_p(t)|\,dt=
\begin{cases}
\dfrac{1-3p}{3},&p\le0,\\[1ex]
\dfrac{1-3p+8p^3}{3},&0\le p\le\dfrac12,\\[1ex]
\dfrac{3p-1}{3},&p\ge\dfrac12,
\end{cases}                                                  \tag{12}
\]
which yields (3)--(4).

The constant is sharp even within \(C^2\). Indeed, any continuous \(G:[0,1]\to[m,M]\) can be realized as the symmetric second-derivative average in (9): on the normalized interval \([0,1]\), prescribe
\[
f''(s)=G\bigl(2\min\{s,1-s\}\bigr)
\]
and integrate twice. Continuous functions \(G_k\) can be chosen with exact range \([m,M]\) and
\[
\frac{G_k-c}{d}\longrightarrow \operatorname{sgn}(w_p)
\]
in \(L^1(|w_p(t)|dt)\). When \(0<p<1/2\), smooth the single jump at \(t=2p\); when \(w_p\) has one sign, place the required opposite extremum inside a shrinking neighborhood of the zero \(t=0\). Hence the right side of (11) is approached arbitrarily closely. For \(m<M\), equality is generally not attained in \(C^2\), because exact saturation would force an incompatible bang-bang profile across sets where \(w_p\ne0\).

This also proves that the three ranges in Simić--Bin-Mohsin Theorem 2.8 are exact infimum/supremum envelopes, not merely valid bounds.

### 3. Minimax choice of the endpoint weight

Outside \([0,1/2]\), (3) is linear and increases away from that interval. Inside it,
\[
C(p)=\frac{1-3p+8p^3}{48},\qquad
C'(p)=\frac{24p^2-3}{48}.
\]
The unique critical point in \((0,1/2)\) is \(p=1/(2\sqrt2)\), where \(C''(p)>0\). Comparison with the endpoints gives the unique global minimum (5).

Thus, after the curvature midpoint \((m+M)/2\) is used for the forced quadratic centering, the best member of this symmetric endpoint-midpoint family is *not* exactly Simpson's \(p=1/3\), but \(p=1/(2\sqrt2)\).

### 4. Why Simpson is uniquely correction-free

An uncentered estimate (6) is a special case of (1) with \(\lambda=0\). By the forced-centering calculation, this can hold with a finite constant only when
\[
3p-1=0,
\]
that is, \(p=1/3\). Substituting \(p=1/3\) into (3) gives
\[
C(1/3)=\frac1{162}.
\]
Hence Simpson's weights are uniquely characterized within this family by the fact that the quadrature error descends to the curvature-oscillation seminorm without any quadratic correction.

## Relation to prior literature and originality boundary

Simić and Bin-Mohsin (2021) prove the three piecewise bounds that correspond to the uncentered lower and upper envelopes of \(T_p\), and in Corollary 2.10 obtain the Simpson estimate \(1/162\), which they conjecture to be best possible. Their paper does not state the all-\(p\) sharpness, the forced centering (2), the centered exact constant (3), or the minimax weight (5).

The Simpson-only sharpness has older coverage. Cruz-Uribe and Neugebauer (2002, Theorem 1.19) prove a sharp Simpson bound in \(W^{2,p}\). At \(p=\infty\), their formula gives the one-panel estimate with distance to affine second derivatives; choosing the constant midpoint of the curvature range yields the \((M-m)/162\) bound. Accordingly, the present record does not claim that resolving the 2021 Simpson constant conjecture is itself original.

Simić and Bin-Mohsin (2020) study the same endpoint-midpoint family under additional convexity/concavity hypotheses on the second derivative and establish different best-possible parameter statements. That setting is distinct from the arbitrary \(C^2\) fixed-curvature-range optimization here.

Searches for the exact cubic \(1-3p+8p^3\), the parameter \(1/(2\sqrt2)\), centered curvature-oscillation formulations, and equivalent three-point quadrature language did not locate the all-\(p\) theorem above. Originality is therefore asserted only to the best of our knowledge. Older general three-point-rule literature, especially Cerone (2001), and two sharp Simpson papers of Ujević (2004), could not be checked theorem-by-theorem from accessible full text and remain the principal literature risk. The Ujević papers are Simpson-specific by title and abstract; Cerone's abstract describes broad three-point Ostrowski-type bounds, so an equivalent parameterized result in different notation cannot be excluded.

## Limitations

- The theorem concerns this one-parameter symmetric endpoint-midpoint rule and the information pair \((m,M)\); it does not optimize over arbitrary node locations or additional derivative information.
- Sharpness for \(m<M\) is generally in the supremum/infimum sense; the extremal bang-bang curvature profile is not continuous, but continuous profiles approach it arbitrarily closely.
- The minimax statement uses the necessary curvature-centering correction \(\lambda_p(m+M)h^2\). Without that correction, Simpson \(p=1/3\) is the unique admissible parameter.
- The Simpson-specific constant \(1/162\) is prior-covered and is not part of the originality claim.
- Equivalent coverage in older general quadrature literature under different notation remains possible; originality is to the best of our knowledge.


## Reproducibility

`artifacts/verify_three_point_envelope.py` checks the polynomial integrations, the equivalence with the Simić--Bin-Mohsin coefficients on representative rational parameters, the Simpson value \(1/162\), and the minimax parameter and constant. The proof itself is analytic and does not depend on numerical computation.

## References

1. S. Simić and B. Bin-Mohsin, *Some generalizations of the Hermite--Hadamard integral inequality*, Journal of Inequalities and Applications **2021**, 72 (2021). https://doi.org/10.1186/s13660-021-02605-y
2. D. Cruz-Uribe and C. J. Neugebauer, *Sharp error bounds for the trapezoidal rule and Simpson's rule*, JIPAM **3**(4), Article 49 (2002). https://eudml.org/doc/123201
3. S. Simić and B. Bin-Mohsin, *Some Improvements of the Hermite--Hadamard Integral Inequality*, Symmetry **12**(1), 117 (2020). https://doi.org/10.3390/sym12010117
4. P. Cerone, *Three point rules in numerical integration*, Nonlinear Analysis **47**(4), 2341--2352 (2001). https://doi.org/10.1016/S0362-546X(01)00358-3
5. N. Ujević, *Sharp inequalities of Simpson type and Ostrowski type*, Computers & Mathematics with Applications **48**(1--2), 145--151 (2004). https://doi.org/10.1016/j.camwa.2003.09.026
6. N. Ujević, *Two Sharp Inequalities of Simpson Type and Applications*, Georgian Mathematical Journal **11**(1) (2004). https://doi.org/10.1515/GMJ.2004.187

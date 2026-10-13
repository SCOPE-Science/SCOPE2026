# A sharp Aitken error bound for positive exponential mixtures

## Finding
Let
\[
x_n=\ell+\sum_{j=1}^m c_j\lambda_j^n,
\qquad
c_j>0,
\qquad
0\le\lambda_-\le\lambda_j\le\lambda_+<1.
\]
For every index \(n\) at which the Aitken denominator is nonzero, define
\[
\widehat x_n
=
x_n-\frac{(x_{n+1}-x_n)^2}{x_{n+2}-2x_{n+1}+x_n}.
\]
Then
\[
0\le
\frac{\widehat x_n-\ell}{x_n-\ell}
\le
\left(
\frac{\lambda_+-\lambda_-}{2-\lambda_+-\lambda_-}
\right)^2.
\]
The upper constant is sharp. For \(0<\lambda_-<\lambda_+<1\), equality is attained by a two-mode endpoint mixture with suitable positive coefficients.

Therefore Aitken extrapolation cannot overshoot the limit on this positive-mixture class. In the one-sided spectral case \(0\le\lambda_j\le q<1\),
\[
\frac{\widehat x_n-\ell}{x_n-\ell}
\le
\left(\frac{q}{2-q}\right)^2
<
q^2.
\]
The right-hand side \(q^2\) is the natural worst-case error factor obtained by simply advancing the raw sequence from \(x_n\) to \(x_{n+2}\). Thus, with the same three scalar inputs, Aitken has a strictly better sharp worst-case factor on positive spectral mixtures.

## Assumptions and scope
The coefficients \(c_j\) are strictly positive and all modes satisfy \(0\le\lambda_j<1\). Zero coefficients can be omitted. If the active modes all have the same \(\lambda\), Aitken is exact and the bound has zero right-hand side.

The result is finite-dimensional as stated, but the proof uses only first and second moments of \(1-\lambda\). Hence it extends verbatim to
\[
x_n=\ell+\int_{[\lambda_-,\lambda_+]}\lambda^n\,d\mu(\lambda)
\]
for any finite positive measure for which \(x_n>\ell\). In particular, if \(T\) is a self-adjoint positive contraction with spectrum contained in \([\lambda_-,\lambda_+]\), then
\[
x_n=\ell+\langle v,T^n v\rangle
\]
has this form by the spectral theorem.

## Proof
Put
\[
e_n=x_n-\ell>0.
\]
For a fixed \(n\), normalize the modal contributions by
\[
w_j=\frac{c_j\lambda_j^n}{e_n},
\qquad
\sum_j w_j=1.
\]
Set
\[
a_j=1-\lambda_j.
\]
Then
\[
m:=1-\lambda_+\le a_j\le M:=1-\lambda_-.
\]
With expectation taken using the weights \(w_j\),
\[
x_{n+1}-x_n=-e_n\,\mathbb E[a],
\]
and
\[
x_{n+2}-2x_{n+1}+x_n=e_n\,\mathbb E[a^2].
\]
Therefore
\[
\frac{\widehat x_n-\ell}{e_n}
=
1-\frac{\mathbb E[a]^2}{\mathbb E[a^2]}
=
\frac{\operatorname{Var}(a)}{\mathbb E[a^2]}.
\]
This proves nonnegativity and the no-overshoot statement.

The pointwise inequality
\[
(a-m)(M-a)\ge0
\]
gives
\[
\mathbb E[a^2]\le(m+M)\mathbb E[a]-mM.
\]
Writing \(y=\mathbb E[a]\in[m,M]\),
\[
1-\frac{\mathbb E[a]^2}{\mathbb E[a^2]}
\le
1-\frac{y^2}{(m+M)y-mM}.
\]
The right-hand side is maximized at
\[
y_\star=\frac{2mM}{m+M},
\]
where its value is
\[
\left(\frac{M-m}{M+m}\right)^2.
\]
Substituting \(m=1-\lambda_+\) and \(M=1-\lambda_-\) yields the claimed constant.

Equality requires support only at \(m\) and \(M\), together with \(y=y_\star\). This forces the normalized endpoint weights
\[
w(\lambda_+)=\frac{1-\lambda_-}{2-\lambda_+-\lambda_-},
\qquad
w(\lambda_-)=\frac{1-\lambda_+}{2-\lambda_+-\lambda_-}.
\]
For positive endpoints these weights can be realized at any fixed \(n\) by choosing positive coefficients proportional to \(w_j\lambda_j^{-n}\).

For \(\lambda_-=0\), the factor becomes
\[
\left(\frac{q}{2-q}\right)^2.
\]
Since \(0<q<1\), one has \(q/(2-q)<q\), proving the comparison with two unaccelerated steps.

## Verification
The embedded `verify.py` uses exact rational arithmetic. It checks the moment identity on several rational mixtures and verifies a sharp endpoint witness.

For
\[
\lambda_-=\frac14,\qquad
\lambda_+=\frac34,\qquad
x_n=3\left(\frac34\right)^n+\left(\frac14\right)^n,
\]
at \(n=0\),
\[
x_0=4,\qquad x_1=\frac52,\qquad x_2=\frac74.
\]
Aitken gives
\[
\widehat x_0=1,
\]
hence
\[
\frac{\widehat x_0}{x_0}=\frac14,
\]
which equals the sharp constant.

The finite computations replay the displayed witnesses only. The universal theorem follows from the moment proof.

## Relationship to prior work
Aitken's \(\Delta^2\) process is classical. Weniger's comprehensive treatment derives it from the one-geometric-mode model
\[
s_n=s+c\lambda^n
\]
and states exactness for that model. The same source explicitly studies the two-geometric-mode model
\[
s_n=s+ax^n+by^n
\]
and gives a transformed formula showing asymptotic removal of the dominant term. Those results establish the transformation and its acceleration mechanism but do not give the endpoint-only sharp finite-index ratio bound for arbitrary positive mixtures proved here.

Pereyra studies acceleration of interval sequences and explicitly includes Aitken-\(\Delta^2\) acceleration under MSC 65B05. He, Hu, Sun, and Weniger likewise classify a convergence-acceleration algorithm under primary MSC 65B05.

The closest semantic-database comparison found was a sharp black-box Aitken--Steffensen robustness result for scalar contractions. That work permits general nonlinear contractions and possible error amplification. It does not imply this theorem, because positive spectral mixtures impose a stronger moment structure that forces a nonnegative Aitken residual and the sharper endpoint bound.

## Limitations
Positive coefficients and nonnegative spectral modes are essential. Signed mixtures or negative modes can destroy the variance representation and can permit overshoot or instability.

The theorem concerns one three-point Aitken transformation at a fixed index. It does not classify repeated Aitken iteration, higher-order epsilon algorithms, or floating-point cancellation when the second difference is very small.

Sharpness is exact for two positive spectral endpoints. When \(\lambda_-=0\) and \(n>0\), mass exactly at zero has vanished from the current error, so the endpoint constant is a uniform sharp envelope approached by a small positive lower endpoint if necessary.

Residual originality risk remains that older convergence-acceleration literature may encode the same moment inequality under Hausdorff-moment or totally monotone sequence terminology. The highly relevant full-text source inspected here gives one- and two-mode Aitken formulas but not this sharp endpoint-only positive-mixture bound.

## References
1. V. Pereyra, “Acceleration of convergence of interval sequences,” Journal of Computational and Applied Mathematics, DOI 10.1016/0377-0427(92)00120-X; publication date 1995-10-08; MSC includes 65B05.
2. E. J. Weniger, “Nonlinear sequence transformations for the acceleration of convergence and the summation of divergent series,” arXiv:math/0306302, public arXiv version 2003-06-19; originally Computer Physics Reports 10 (1989), 189–371.
3. Y. He, X.-B. Hu, J.-Q. Sun, and E. J. Weniger, “Convergence Acceleration Algorithm via an Equation Related to the Lattice Boussinesq Equation,” SIAM Journal on Scientific Computing, DOI 10.1137/100808757; primary MSC 65B05.

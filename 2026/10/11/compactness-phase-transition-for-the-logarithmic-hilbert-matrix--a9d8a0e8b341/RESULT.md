# Compactness phase transition for the logarithmic Hilbert matrix endpoint

## Finding

For
\[
A_{\log^\alpha}^2
=
\left\{
f\in\mathcal H(\mathbb D):
\int_{\mathbb D}
|f(z)|^2
\log^\alpha\!\left(
\frac{e}{1-|z|^2}
\right)dA(z)
<
\infty
\right\},
\]
consider the Hilbert matrix operator
\[
Hf(z)
=
\sum_{m=0}^{\infty}
\left(
\sum_{n=0}^{\infty}
\frac{a_n}{m+n+1}
\right)z^m,
\qquad
f(z)=\sum_{n=0}^{\infty}a_nz^n.
\]

Its behavior from the logarithmically weighted Hilbert scale into the ordinary Bergman space has the exact phase diagram
\[
\alpha>2:
\qquad
H:A_{\log^\alpha}^2\to A^2
\text{ is compact},
\]
\[
\alpha=2:
\qquad
H:A_{\log^2}^2\to A^2
\text{ is bounded but not compact},
\]
and
\[
\alpha<2:
\qquad
H(A_{\log^\alpha}^2)
\not\subset
A^2.
\]

Hence, among all parameters for which \(H\) is bounded as an operator into \(A^2\), compactness occurs exactly when
\[
\alpha>2.
\]

## Assumptions and scope

The normalized area measure is
\[
dA(re^{i\theta})
=
\frac{r\,dr\,d\theta}{\pi}.
\]

The source theorem proves the missing endpoint boundedness
\[
H:A_{\log^2}^2\to A^2.
\]
The same source gives one explicit Taylor-coefficient sequence showing failure of the mapping property for every
\[
\alpha<2.
\]

The new assertion is the compactness classification. No claim is made about exact operator norm or exact essential norm.

## Proof

For
\[
\beta\in\mathbb R
\]
define the monomial weight
\[
\omega_{n,\beta}
=
\int_0^1
t^n
\log^\beta\!\left(
\frac{e}{1-t}
\right)dt.
\]
Radial orthogonality gives
\[
\left\|
\sum_{n\ge0}a_nz^n
\right\|_{A_{\log^\beta}^2}^2
=
\sum_{n\ge0}|a_n|^2\omega_{n,\beta}.
\]

The moment asymptotic proved in the source is
\[
\omega_{n,\beta}
\sim
\frac{\log^\beta(n+3)}{n+3}.
\]

First suppose
\[
\alpha>2.
\]
The inclusion
\[
J_\alpha:
A_{\log^\alpha}^2
\longrightarrow
A_{\log^2}^2
\]
is diagonal in the monomial bases. Its singular values are
\[
s_n(J_\alpha)
=
\left(
\frac{\omega_{n,2}}{\omega_{n,\alpha}}
\right)^{1/2}.
\]
Therefore
\[
s_n(J_\alpha)
\sim
\log^{1-\alpha/2}(n+3)
\longrightarrow0.
\]
Thus \(J_\alpha\) is compact.

The source endpoint theorem gives a bounded operator
\[
H_2:
A_{\log^2}^2
\longrightarrow
A^2.
\]
On \(A_{\log^\alpha}^2\), the Hilbert matrix operator factors as
\[
H
=
H_2J_\alpha.
\]
A bounded operator composed after a compact operator is compact, so
\[
H:
A_{\log^\alpha}^2
\to
A^2
\]
is compact whenever
\[
\alpha>2.
\]

It remains to rule out compactness at the endpoint.

For an integer
\[
N\ge3
\]
write
\[
L_N=\log N
\]
and define the polynomial
\[
f_N(z)
=
L_N^{-3/2}
\sum_{n=N}^{\lfloor N^2\rfloor}z^n.
\]
Using the moment asymptotic uniformly for all sufficiently large indices,
\[
\|f_N\|_{A_{\log^2}^2}^2
\asymp
L_N^{-3}
\sum_{n=N}^{N^2}
\frac{\log^2 n}{n}.
\]
Integral comparison gives
\[
\sum_{n=N}^{N^2}
\frac{\log^2 n}{n}
\asymp
L_N^3.
\]
Hence
\[
0<c_1
\le
\|f_N\|_{A_{\log^2}^2}
\le
c_2
<\infty.
\]

The coefficient supports escape to infinity, so \(f_N\) is weakly null. Indeed, for any fixed
\[
g(z)=\sum_{n\ge0}b_nz^n
\in
A_{\log^2}^2,
\]
Cauchy--Schwarz gives
\[
|\langle f_N,g\rangle|
\le
\|f_N\|_{A_{\log^2}^2}
\left(
\sum_{n\ge N}
|b_n|^2\omega_{n,2}
\right)^{1/2}
\longrightarrow0.
\]

Now let
\[
N\le m\le N^{3/2}.
\]
All coefficients of \(f_N\) are nonnegative, so
\[
\widehat{Hf_N}(m)
=
L_N^{-3/2}
\sum_{n=N}^{N^2}
\frac1{m+n+1}.
\]
Restrict the sum to
\[
N^{3/2}\le n\le N^2.
\]
In this range
\[
m\le n,
\]
hence
\[
m+n+1\le3n
\]
for large \(N\). Therefore
\[
\widehat{Hf_N}(m)
\ge
\frac{L_N^{-3/2}}{3}
\sum_{N^{3/2}\le n\le N^2}
\frac1n.
\]
The harmonic sum is bounded below by a positive constant times
\[
\log\!\left(
\frac{N^2}{N^{3/2}}
\right)
=
\frac12L_N.
\]
Thus, for all large \(N\),
\[
\widehat{Hf_N}(m)
\ge
cL_N^{-1/2}
\]
with an absolute
\[
c>0.
\]

Since
\[
\|h\|_{A^2}^2
=
\sum_{m\ge0}
\frac{|\widehat h(m)|^2}{m+1},
\]
we obtain
\[
\|Hf_N\|_{A^2}^2
\ge
\frac{c^2}{L_N}
\sum_{m=N}^{\lfloor N^{3/2}\rfloor}
\frac1{m+1}.
\]
A second harmonic-sum estimate gives
\[
\sum_{m=N}^{N^{3/2}}
\frac1{m+1}
\asymp
\frac12L_N.
\]
Consequently
\[
\liminf_{N\to\infty}
\|Hf_N\|_{A^2}
>
0.
\]

A compact operator between Hilbert spaces sends bounded weakly null sequences to norm-null sequences. Therefore
\[
H:
A_{\log^2}^2
\to
A^2
\]
is not compact.

Finally, the source constructs
\[
a_n
=
\log^{-3/2}(n+3)
\]
and proves that the corresponding function belongs to
\[
A_{\log^\alpha}^2
\]
for every
\[
\alpha<2,
\]
while its Hilbert image does not belong to \(A^2\). Hence the subcritical mapping property fails.

Combining the three regimes proves the trichotomy.

## Verification

The fresh primary source was inspected through its definition of \(A_{\log^\alpha}^2\), the monomial moment asymptotic, the sequence-space reduction, the endpoint boundedness theorem, and the explicit subcritical counterexample.

The compact inclusion is exact at the Hilbert-space level: radial orthogonality diagonalizes the embedding, and the source moment asymptotic makes its singular values tend to zero exactly when
\[
\alpha>2.
\]

The endpoint obstruction uses explicit polynomials, not a numerical experiment. Their norms stay uniformly bounded, they converge weakly to zero because their coefficient supports escape, and a two-scale positive block of Hilbert-matrix coefficients gives a uniform positive lower bound for the \(A^2\)-norm of their images.

The older logarithmically weighted Bergman paper was inspected at its full theorem level. It proves bounded mapping results only for
\[
\alpha>2
\]
and records the then-open endpoint question; no compactness classification is stated.

## Relationship to prior work

Karapetrović proved in 2018 that for
\[
\alpha>2
\]
the Hilbert matrix maps
\[
A_{\log^\alpha}^2
\]
into logarithmically weighted Bergman targets, including \(A^2\), and explicitly left the range up to the endpoint open.

Norrbo's 2026 paper closes the boundedness problem by proving
\[
H:A_{\log^2}^2\to A^2
\]
and by showing failure below the exponent \(2\). That source contains no compactness or essential-norm statement.

Generalized Hilbert-operator literature contains boundedness and compactness characterizations between standard power-weighted Bergman spaces and related spaces. Those results use different domain weights and do not state the logarithmic-domain endpoint trichotomy above.

Targeted searches for compactness, noncompactness at
\[
\alpha=2,
\]
and an exact logarithmic phase transition did not locate a published statement equivalent to this classification.

## Limitations

No exact value of the essential norm at
\[
\alpha=2
\]
is claimed.

The proof is specific to the Hilbert-space scale
\[
A_{\log^\alpha}^2.
\]
It does not classify compactness for logarithmically weighted \(A^p\) spaces with
\[
p\ne2.
\]

Generalized Hilbert operators associated with arbitrary measures are not treated.

## References

1. D. Norrbo, *The Hilbert matrix operator into the Bergman space*, arXiv:2610.00252v1, 2026.
2. B. Karapetrović, *Libera and Hilbert matrix operator on logarithmically weighted Bergman, Bloch and Hardy-Bloch spaces*, Czechoslovak Mathematical Journal 68 (2018), 559--576. DOI: 10.21136/CMJ.2018.0555-16.
3. S. Ye and G. Feng, *Generalized Hilbert Operator Acting on Weighted Bergman Spaces and on Dirichlet Spaces*, Banach Journal of Mathematical Analysis 17 (2023). DOI: 10.1007/s43037-023-00268-z.
4. P. Tang and X. Zhang, *Generalized Hilbert operator acting on Bergman spaces*, Proceedings of the American Mathematical Society 153 (2025), 3439--3449. DOI: 10.1090/proc/17266.

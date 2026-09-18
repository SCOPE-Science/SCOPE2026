# Exact Rényi-2 total correlation of Gaussian magnitudes

## Statement

Let \(R\) be a positive-definite \(n\times n\) correlation matrix and let
\[
X\sim N(0,R).
\]
Write \(P_R\) for the law of the magnitude vector
\[
|X|=(|X_1|,\ldots,|X_n|)\in(0,\infty)^n
\]
and \(Q\) for the product of its marginals. Since the marginals are standard
half-normal laws, \(Q\) is the law of \(|Z|\) for \(Z\sim N(0,I_n)\).

For a sign vector \(s\in\{-1,1\}^n\), let
\[
D_s=\operatorname{diag}(s_1,\ldots,s_n)
\]
and define
\[
B_s:=R^{-1}+D_sR^{-1}D_s-I_n.
\]

### Theorem 1 (exact order-2 Rényi total correlation)

The order-2 Rényi total correlation satisfies
\[
\boxed{\quad
D_2(P_R\|Q)<\infty
\iff
\lambda_{\max}(R)<2.
\quad}
\tag{1}
\]

When \(\lambda_{\max}(R)<2\),
\[
\boxed{\quad
e^{D_2(P_R\|Q)}
=
\frac{1}{2^n\det R}
\sum_{s\in\{-1,1\}^n}
\det(B_s)^{-1/2}.
\quad}
\tag{2}
\]
When \(\lambda_{\max}(R)\ge2\), the divergence is \(+\infty\).

The sum in (2) may be reduced to \(2^{n-1}\) terms because \(D_s\) and
\(-D_s\) produce the same matrix \(B_s\).

### Corollary 2 (bivariate closed form)

For a standard bivariate Gaussian pair with correlation \(\rho\in(-1,1)\),
\[
R_\rho=
\begin{pmatrix}
1&\rho\\
\rho&1
\end{pmatrix},
\]
the magnitude Rényi total correlation is
\[
\boxed{\quad
D_2\!\left(\mathcal L(|X_1|,|X_2|)
\,\middle\|\,
\mathcal L(|X_1|)\otimes\mathcal L(|X_2|)
\right)
=
-\log(1-\rho^4).
\quad}
\tag{3}
\]

Thus magnitude dependence is quartic, rather than quadratic, at weak
correlation:
\[
D_2=\rho^4+O(\rho^8).
\]

### Corollary 3 (equicorrelation threshold)

For the equicorrelation matrix
\[
R_\rho=(1-\rho)I_n+\rho {\bf1}{\bf1}^{\mathsf T},
\qquad
-\frac1{n-1}<\rho<1,
\]
one has, for \(\rho\ge0\),
\[
\boxed{\quad
D_2(P_{R_\rho}\|Q)<\infty
\iff
\rho<\frac1{n-1}.
\quad}
\tag{4}
\]
For negative \(\rho\) in the positive-definite range, \(D_2\) is finite.
Hence, when \(n\ge3\), a nonsingular positively equicorrelated Gaussian can
already have infinite order-2 total correlation after taking coordinatewise
absolute values.

### Theorem 4 (weak-correlation cycle expansion)

Let \(A\) be a fixed real symmetric matrix with zero diagonal and set
\[
R_\varepsilon=I_n+\varepsilon A.
\]
For sufficiently small \(|\varepsilon|\), \(R_\varepsilon\) is a correlation
matrix and
\[
\boxed{\quad
D_2(P_{R_\varepsilon}\|Q)
=
\varepsilon^4\sum_{i<j}A_{ij}^4
+
8\varepsilon^6
\sum_{i<j<k}
A_{ij}^2A_{ik}^2A_{jk}^2
+
O(\varepsilon^8).
\quad}
\tag{5}
\]
The first nontrivial term is therefore a sum of pairwise fourth powers.
The first genuinely three-way contribution occurs two orders later and is
supported exactly on triangles.

## Proof of Theorem 1

Let \(\varphi_R\) and \(\varphi_I\) denote the densities of \(N(0,R)\) and
\(N(0,I_n)\). The known folded-normal density formula gives, for \(y>0\)
coordinatewise,
\[
p_R(y)=\sum_s\varphi_R(D_sy),
\qquad
q(y)=2^n\varphi_I(y).
\]
Consequently,
\[
\frac{dP_R}{dQ}(y)
=
2^{-n}\sum_s
\frac{\varphi_R(D_sy)}{\varphi_I(y)}.
\tag{6}
\]

Let \(Z\sim N(0,I_n)\). Because the independent standard Gaussian law is
invariant under coordinatewise sign changes, expanding the square in
\[
e^{D_2(P_R\|Q)}
=
\mathbb E\!\left[
\left\{\frac{dP_R}{dQ}(|Z|)\right\}^2
\right]
\]
and reducing pairs of signs to their relative sign matrix gives
\[
e^{D_2(P_R\|Q)}
=
2^{-n}\sum_s
\int_{\mathbb R^n}
\frac{\varphi_R(x)\varphi_R(D_sx)}
{\varphi_I(x)}\,dx.
\tag{7}
\]

The integrand in the \(s\)-term is
\[
(2\pi)^{-n/2}(\det R)^{-1}
\exp\!\left\{
-\frac12x^{\mathsf T}
\bigl(R^{-1}+D_sR^{-1}D_s-I_n\bigr)x
\right\}.
\]
Hence this integral is finite exactly when \(B_s\) is positive definite,
and then it equals
\[
(\det R)^{-1}\det(B_s)^{-1/2}.
\]
This proves (2) provided every \(B_s\) is positive definite.

It remains to identify the finiteness condition. The term \(s=(1,\ldots,1)\)
has
\[
B_s=2R^{-1}-I_n,
\]
which is positive definite exactly when \(\lambda_{\max}(R)<2\). Thus
finiteness implies \(\lambda_{\max}(R)<2\).

Conversely, if \(\lambda_{\max}(R)<2\), then
\[
R^{-1}\succ\frac12I_n.
\]
Conjugating by any sign matrix preserves this strict inequality, so
\[
R^{-1}+D_sR^{-1}D_s-I_n\succ0
\]
for every \(s\). This proves (1) and completes the theorem.

## Proof of the bivariate formula

For
\[
R_\rho^{-1}
=
\frac1{1-\rho^2}
\begin{pmatrix}
1&-\rho\\
-\rho&1
\end{pmatrix},
\]
there are two sign classes. For \(D=I\),
\[
\det(2R_\rho^{-1}-I)=1.
\]
For \(D=\operatorname{diag}(1,-1)\),
\[
R_\rho^{-1}+DR_\rho^{-1}D-I
=
\frac{1+\rho^2}{1-\rho^2}I,
\]
so its inverse square-root determinant is
\[
\frac{1-\rho^2}{1+\rho^2}.
\]
Substitution into (2) yields
\[
e^{D_2}
=
\frac{1}{1-\rho^4},
\]
which is (3).

## Hermite representation and proof of Theorem 4

Let \(H_k\) be the probabilists' Hermite polynomials, normalized by
\[
\mathbb E[H_k(Z)H_\ell(Z)]=k!\,\mathbf 1_{\{k=\ell\}},
\qquad Z\sim N(0,1).
\]
When \(\lambda_{\max}(R)<2\), the Gaussian likelihood ratio
\(\varphi_R/\varphi_I\) is square-integrable. Its product-Hermite expansion has
coefficients determined by
\[
\mathbb E_R\!\left[
\exp\!\left(\sum_i t_iX_i-\frac12\sum_i t_i^2\right)
\right]
=
\exp\!\left(\sum_{i<j}R_{ij}t_it_j\right).
\tag{8}
\]
For a multi-index \(d=(d_1,\ldots,d_n)\), define
\[
c_d(R)
=
[t_1^{d_1}\cdots t_n^{d_n}]
\exp\!\left(\sum_{i<j}R_{ij}t_it_j\right).
\tag{9}
\]

Equation (6) is the coordinatewise sign average of the Gaussian likelihood
ratio. Since \(H_k(-x)=(-1)^kH_k(x)\), sign averaging removes exactly those
Hermite components for which at least one \(d_i\) is odd. Orthogonality
therefore gives the exact series
\[
\boxed{\quad
e^{D_2(P_R\|Q)}
=
\sum_{d\in(2\mathbb N_0)^n}
\left(\prod_i d_i!\right)c_d(R)^2.
\quad}
\tag{10}
\]

Now take \(R=I+\varepsilon A\). The coefficient \(c_d\) can be viewed as a
sum over loopless multigraphs with edge multiplicities \(k_{ij}\), vertex
degrees \(d_i=\sum_{j\ne i}k_{ij}\), and weight
\[
\prod_{i<j}\frac{(\varepsilon A_{ij})^{k_{ij}}}{k_{ij}!}.
\]
Only even vertex degrees survive in (10).

The smallest nonempty even-degree multigraph is a doubled edge. For the pair
\(\{i,j\}\), it gives
\[
c_d=\frac{\varepsilon^2A_{ij}^2}{2}
\]
with \(d_i=d_j=2\), whose contribution to (10) is
\[
(2!)(2!)
\left(\frac{\varepsilon^2A_{ij}^2}{2}\right)^2
=
\varepsilon^4A_{ij}^4.
\]
The only even-degree multigraph with three edges is a triangle. For
\(\{i,j,k\}\) it gives
\[
c_d=\varepsilon^3A_{ij}A_{ik}A_{jk},
\qquad d_i=d_j=d_k=2,
\]
and contributes
\[
(2!)^3\varepsilon^6
A_{ij}^2A_{ik}^2A_{jk}^2
=
8\varepsilon^6
A_{ij}^2A_{ik}^2A_{jk}^2.
\]
All remaining nonconstant terms in (10) have at least four edges and hence
contribute \(O(\varepsilon^8)\). Thus
\[
e^{D_2}=1+\varepsilon^4S_4+\varepsilon^6S_6+O(\varepsilon^8),
\]
with \(S_4,S_6\) as in (5). Taking the logarithm does not alter the
coefficients through order six, proving (5).

## Relation to prior work

Ouimet and Greaves (2026) prove the strong Gaussian product inequality for
all positive exponents. Their Corollary 4.11 introduces exactly the
order-2 Rényi total correlation of the Gaussian magnitude vector considered
here and obtains an explicit lower bound from normalized product moments.
That argument deliberately avoids evaluating the joint density ratio.

The multivariate folded-normal density itself is classical. Benko,
Hübnerová and Witkovský (2025) give the general \(2^n\)-term sign-reflected
Gaussian density formula and derive the moment generating and characteristic
functions. Those ingredients make a direct evaluation of the order-2
divergence possible.

The contribution here is the exact determinant formula (2), the sharp
finiteness threshold (1), the bivariate identity (3), and the weak-correlation
cycle expansion (5). Generic Gaussian and Gaussian-mixture overlap formulas
are standard tools; no novelty is claimed for Gaussian integration itself.

## Verification

The accompanying script `artifacts/verify.py` evaluates (2), checks (3) at
several correlations, checks the coefficients in (5) numerically on a fixed
three-dimensional perturbation, and illustrates the equicorrelation
finiteness threshold.

## Limitations

The result is for positive-definite correlation matrices. Singular Gaussian
laws require a separate formulation because the folded law need not have a
Lebesgue density on the full positive orthant.

The determinant formula has exponentially many sign terms in general; it is
an exact expression, not a polynomial-time algorithm in the dimension.

Order \(2\) is special because the divergence reduces to a quadratic density
overlap. No analogous finite determinant sum is claimed here for arbitrary
Rényi order.

The originality assessment is to the best of our knowledge. A residual risk
comes from older Gaussian-mixture \(L^2\)/chi-square-divergence literature:
generic overlap identities could contain an equivalent specialization
without using the language of Gaussian magnitudes or Rényi total correlation.

## References

1. F. Ouimet and D. Greaves, *A proof of the strong Gaussian product
   inequality conjecture*, arXiv:2609.20234 (2026).
   https://arxiv.org/abs/2609.20234
2. M. Benko, Z. Hübnerová and V. Witkovský, *Characteristic function and
   moment generating function of multivariate folded normal distribution*,
   Statistical Papers (2025), DOI: 10.1007/s00362-025-01711-z.
   https://doi.org/10.1007/s00362-025-01711-z
3. T. van Erven and P. Harremoës, *Rényi Divergence and Kullback-Leibler
   Divergence*, IEEE Transactions on Information Theory 60 (2014), 3797--3820.
   https://doi.org/10.1109/TIT.2014.2320500

# Exact parity-split center correlations for a neutral heterochaos baker map

## Finding

For the volume-preserving three-dimensional heterochaos baker map specified below, let \(m\) be normalized Lebesgue measure, let \(c\) be the central coordinate, and define the stationary lag-\(n\) covariance
\[
 C_n=\int_{[0,1]^3}(c-\tfrac12)\bigl(c\circ F^n-\tfrac12\bigr)\,dm,\qquad n\ge0.
\]
The entire covariance sequence has the following **exact algebraic generating function**:
\[
 \boxed{\sum_{n\ge0}C_nz^n=\frac{1}{4-5z}\left(\frac13-\frac{\eta(z)}{2-\eta(z)}\right),\quad
 \eta(z)=\frac{1-\sqrt{1-z^2}}{z},\quad\eta(0)=0.}
\]
The apparent pole at \(z=4/5\) cancels. The sharp asymptotic distinguishes even and odd lags:
\[
 \boxed{C_n=\sqrt{\frac2\pi}\left(1+\frac{(-1)^n}{81}\right)n^{-3/2}+O(n^{-5/2}),\qquad n\longrightarrow\infty.}
\]
In particular, the leading coefficient for even lags is \(\frac{82}{81}\sqrt{2/\pi}\), whereas that for odd lags is \(\frac{80}{81}\sqrt{2/\pi}\). The first values are \(C_0=1/12\), \(C_1=1/24\), \(C_2=7/192\), \(C_3=5/192\).

## Assumptions and scope

Let \(F:[0,1]^3\to[0,1]^3\) have coordinates \((u,c,s)\) and branches
\[
 F(u,c,s)=\begin{cases}
 (4u,c/2,s/2),&0\le u<1/4,\\
 (4u-1,(c+1)/2,s/2),&1/4\le u<1/2,\\
 (2u-1,2c,s/4+1/2),&1/2\le u\le1,\ 0\le c<1/2,\\
 (2u-1,2c-1,s/4+3/4),&1/2\le u\le1,\ 1/2\le c\le1.
 \end{cases}
\]
On boundaries, arbitrary consistent definitions have no effect on the Lebesgue-integral statements. This is the \(M=2\), \(a=b=1/4\) instance of the generalized heterochaos baker map in Takahasi--Tsujii. Each branch has Jacobian determinant one and the four branch images partition the cube up to null boundaries; hence normalized Lebesgue measure is stationary. The central direction is neutral on average: it contracts by \(1/2\) on the first two branches and expands by \(2\) on the last two, each with total Lebesgue probability \(1/2\).

The theorem concerns exactly the smooth observable \(c-1/2\), all nonnegative integer lags, and stationary Lebesgue initial data. It is not a statement about arbitrary observables or general parameters.

## Proof

**1. Exact one-coordinate transfer.** The full-branch base map on \(u\) has successive branches selected with probabilities \(1/4,1/4,1/2\) under Lebesgue measure, independently of the past base branches and of the initial central coordinate. Integrating the stable coordinate, the central-coordinate transfer operator acts on \(v:[0,1]\to\mathbb R\) by
\[
 (Pv)(c)=\frac12v(2c\bmod1)+\frac14v(c/2)+\frac14v((c+1)/2).
\]
The conventional choice of endpoint for \(2c\bmod1\) is immaterial. Equivalently, \(P\) is the reduced Perron--Frobenius operator in equations (2.6)--(2.8) of Takahasi--Tsujii; their proof of the lower correlation bound explicitly identifies correlations of central-only observables with its iterates. Thus, with \(\phi(c)=c-1/2\),
\[
 C_n=\langle P^n\phi,\phi\rangle_{L^2([0,1])}.
\]

**2. An exact half-line walk.** For Lebesgue-a.e. \(c\in[0,1]\), write its binary expansion \(c=\sum_{j\ge1}b_j(c)2^{-j}\) and define \(r_j(c)=1-2b_j(c)\). The \(r_j\) are an orthonormal family in \(L^2([0,1])\), and
\[
 \phi=-\sum_{j\ge1}2^{-j-1}r_j\quad\text{in }L^2.
\]
The operator is exactly
\[
 Pr_1=\tfrac12r_2,\qquad Pr_j=\tfrac12(r_{j-1}+r_{j+1})\quad(j\ge2).
\]
Consequently its restriction to the closed span of the \(r_j\) is the symmetric nearest-neighbor transition on the positive integers, killed on reaching zero. The boundary condition is \(w_0=0\); no reflecting mass is allowed. The geometric coefficients of \(\phi\) are absolutely summable.

**3. Green-function calculation.** For \(|z|\) sufficiently small, let \(w=(I-zP)^{-1}\phi\) and let \(w_j\) be its coefficient of \(r_j\). Put \(r=1/2\), and define the solution of the characteristic equation that vanishes at the origin,
\[
 \eta(z)+\eta(z)^{-1}=2/z,\qquad \eta(z)=(1-\sqrt{1-z^2})/z.
\]
The inhomogeneous recurrence is
\[
 w_j-\tfrac z2(w_{j-1}+w_{j+1})=-\tfrac12r^j\quad(j\ge1),\qquad w_0=0.
\]
Its summable solution is
\[
 w_j=-\frac{r^j-\eta(z)^j}{2(1-5z/4)}.
\]
The coefficientwise resolvent and absolute convergence for small \(|z|\) justify taking its inner product with \(\phi\). Since
\[
 \sum_{j\ge1}r^{2j}=\frac13,\qquad
 \sum_{j\ge1}(r\eta)^j=\frac{\eta}{2-\eta},
\]
we obtain the boxed generating function. At \(z=4/5\), \(\eta(z)=1/2\), so the numerator and denominator vanish and the singularity is removable. The equation \(|\eta(z)|<1\) for \(|z|<1\) excludes any other pole there.

**4. Sharp two-edge singularity law.** The only remaining singularities on the unit circle occur at \(z=1\) and \(z=-1\). Setting \(z=1-h\) with \(h\downarrow0\) gives
\[
 \sum C_nz^n=\frac23-2\sqrt2\,h^{1/2}+\frac{28}3h+O(h^{3/2}).
\]
Setting \(z=-1+h\) gives
\[
 \sum C_nz^n=\frac2{27}-\frac{2\sqrt2}{81}h^{1/2}+\frac4{81}h+O(h^{3/2}).
\]
These are square-root singular expansions in complex slit neighborhoods. The coefficient transfer formula
\[
 [z^n](1-z)^{1/2}=-\frac{1}{2\sqrt\pi}\,n^{-3/2}+O(n^{-5/2})
\]
and the corresponding \((-1)^n\) factor for the singularity at \(-1\) yield the claimed asymptotic with \(O(n^{-5/2})\) error. The branch points' interference, rather than a single mixing pole, produces the parity-sensitive leading constant.

## Verification

The standalone standard-library script `verify_correlation.py` constructs, independently, coefficients of the algebraic Green function and finite reflected-walk binomial sums. It checks the first \(25\) coefficients as exact rational identities. For the latter calculation, the infinite contribution from starting levels \(j>n\) is evaluated exactly as \(5^n/(12\cdot16^n)\); it is not truncated. The script also performs finite-depth numerical checks at four large lags against the proved two-parity asymptotic. The script is evidence for algebra and normalization, **not** a substitute for the infinite singularity argument. Reproduce with `python3 verify_correlation.py` in a directory containing this file.

## Relationship to prior work

Takahasi and Tsujii (2024, arXiv:2408.16618v1) construct the neutral-center heterochaos baker map, give the exact reduced transfer operator, identify its absorbing random-walk structure, and prove the optimal upper and lower \(n^{-3/2}\) correlation rate for Hölder observables. Their bounds and kernel do not state the all-lag algebraic generating function or the exact **two distinct parity-dependent coefficients** for the natural central-coordinate observable. Those coefficients require evaluating the full geometric-weight Green function and resolving both spectral endpoints. The underlying random-walk reflection formula and square-root coefficient transfer are established methods, not claimed as new. Takahasi (2023, arXiv:2307.08119v1) studies exponential mixing away from the neutral-center regime, hence does not imply this neutral asymptotic. Related periodic-point results concern different invariants.

## Limitations

The theorem is restricted to the specified \(M=2\) volume-preserving neutral parameter and one affine central observable. It does not determine leading constants for arbitrary Hölder observables, rates of nonstationary systems, the two-dimensional non-volume-preserving map, or other center parameters. The exact summation uses techniques implicit in the existing transfer-kernel literature, so an equivalent earlier spectral calculation not indexed by the searches remains a priority risk.

## References

1. H. Takahasi and M. Tsujii, *Polynomial rate of mixing for the heterochaos baker maps with mostly neutral center*, arXiv:2408.16618v1, first submitted 2024-08-29, especially Sections 1.1, 2.3--2.6, and 3.5. https://arxiv.org/html/2408.16618v1
2. H. Takahasi, *Exponential mixing for heterochaos baker maps and the Dyck system*, arXiv:2307.08119v1, first submitted 2023-07-16. https://arxiv.org/html/2307.08119v1
3. H. Takahasi, *Distributions of periodic points for the Dyck shift and the heterochaos baker maps*, arXiv:2409.01261v1, first submitted 2024-09-02. https://arxiv.org/html/2409.01261v1

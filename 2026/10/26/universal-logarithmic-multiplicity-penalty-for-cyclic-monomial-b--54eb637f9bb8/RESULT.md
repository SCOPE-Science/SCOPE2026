# Universal logarithmic multiplicity penalty for cyclic monomial boundary zeros

## Finding
Fix integers \(n\ge m\ge1\), positive integers \(a_1,\ldots,a_m\), and put \(d=a_1+\cdots+a_m\). Normalize the monomial on the complex unit ball by
\[
u(z)=c\prod_{j=1}^m z_j^{a_j},\qquad
c=\left(\frac{d^d}{\prod_{j=1}^m a_j^{a_j}}\right)^{1/2}.
\]
Set \(\alpha_*=n-(m-1)/2\) and give polynomials on \(\mathbb B_n\) the coefficient Hilbert norm
\[
\left\|\sum_{\nu\in\mathbb N^n}b_\nu z^\nu\right\|_{\alpha_*}^2
=\sum_{\nu\in\mathbb N^n}(n+|\nu|)^{\alpha_*}
\frac{(n-1)!\prod_j\nu_j!}{(n-1+|\nu|)!}|b_\nu|^2.
\]
For each fixed positive integer \(r\), the *squared* unrestricted total-degree optimal approximation error is
\[
E_{K,r}:=\min_{\deg q\le dK}\big\|1-(1-u)^r q\big\|_{\alpha_*}^2,
\qquad K=0,1,2,\ldots.
\]
Define the explicit strictly positive normalization
\[
C=(n-1)!(2\pi)^{(m-1)/2}
\left(\prod_{j=1}^m a_j\right)^{1/2}d^{1-m/2}
\]
and the convergent scalar
\[
\Lambda=\gamma+\frac{C}{n^{\alpha_*}}+
\sum_{k=1}^\infty\left(\frac{C}{w_k}-\frac1k\right),
\quad
w_k=(n+dk)^{\alpha_*}(n-1)!c^{2k}
\frac{\prod_{j=1}^m(a_j k)!}{(n-1+dk)!},
\]
where \(\gamma\) is Euler's constant. **The sharp renormalized error law is**
\[
\boxed{\frac{C}{E_{K,r}}=\log K+\Lambda-2H_{r-1}+o(1),\qquad K\to\infty,}
\]
with \(H_0=0\) and \(H_j=\sum_{\ell=1}^j1/\ell\). In particular, the new parameter-free multiplicity invariant is
\[
\boxed{\lim_{K\to\infty}C\left(\frac1{E_{K,r}}-\frac1{E_{K,1}}\right)=-2H_{r-1}.}
\]
For each fixed \(r\ge2\), equivalently,
\[
\boxed{\lim_{K\to\infty}(\log K)^2(E_{K,r}-E_{K,1})
=2C H_{r-1}.}
\]
The leading squared-error law \(E_{K,r}\sim C/\log K\) is independent of multiplicity and was already accessible through earlier cyclic-approximation techniques. The nonzero *second-order multiplicity penalty*, including its exact universal harmonic-number coefficient, is the assertion emphasized here.

## Assumptions and scope
The domain is the **Euclidean complex unit ball**, not the polydisk or a non-Euclidean ellipsoid. Its complex dimension \(n\), support size \(m\), exponent vector \((a_1,\ldots,a_m)\), and boundary multiplicity \(r\) are fixed as \(K\to\infty\). The factors \(a_j\) need not be coprime. All polynomial multipliers of total degree at most \(dK\) are allowed; no one-generator restriction is imposed on the optimization. The exponent \(\alpha_*\) and monomial normalization are essential. All errors are **squared** Hilbert norms, and the displayed \(o(1)\) is not asserted uniformly as parameters vary.

The arithmetic-geometric mean inequality gives \(|u(z)|\le1\) for \(z\in\overline{\mathbb B}_n\). The boundary zero set of \(1-u\) has real dimension \(m-1\) (possibly several connected components). There are no zeros of \(1-u\) in \(\mathbb B_n\). Thus its critical Dirichlet index is the familiar \(\alpha_*\), while the new question resolves the loss due to powers \((1-u)^r\) at the **second** logarithmic order.

## Proof
**1. Invariance reduces the unrestricted multiplier problem exactly.** Let \(T\) be the compact subgroup of coordinatewise unitary rotations satisfying \(\prod_{j=1}^m t_j^{a_j}=1\), with all remaining coordinates freely rotated. Then \(u\), \((1-u)^r\), and \(1\) are invariant under \(T\). Monomials are orthogonal and the norm is invariant under \(T\). Haar averaging is therefore an orthogonal contraction, so replacing an arbitrary multiplier \(q\) by its \(T\)-average does not increase its error. Character duality (including the finite components when \(\gcd(a_1,\ldots,a_m)>1\)) shows that a monomial invariant under all of \(T\) must have exponent vector \(k(a_1,\ldots,a_m,0,\ldots,0)\) for an integer \(k\ge0\). Thus the optimum over degree \(\le dK\) multipliers equals the optimum over \(q=P(u)\) with \(\deg P\le K\). This is an exact unrestricted reduction, not an assumption about a restricted family of multipliers.

**2. Exact finite moment reduction.** The monomial \(u^k\) has squared norm \(w_k\) as defined in the finding, so distinct powers are orthogonal. For a multiplier \(P\) of degree \(\le K\), write \(R(u)=1-(1-u)^rP(u)\), with \(\deg R\le L:=K+r\). Conversely, every such polynomial \(R\) with \(R(1)=1\) and \(R^{(j)}(1)=0\) for \(1\le j<r\) gives a permissible polynomial \(P=(1-R)/(1-u)^r\). In terms of its coefficients \(R(u)=\sum_{k=0}^L\rho_k u^k\), the equivalent moment constraints are \(\sum_{k=0}^L k^j\rho_k=\mathbf1_{\{j=0\}}\) for \(0\le j<r\). Weighted least squares hence gives
\[
E_{K,r}=(G_L^{-1})_{00},\qquad
(G_L)_{ij}=\sum_{k=0}^L\frac{k^{i+j}}{w_k},
\qquad0\le i,j<r.
\]
The Gram matrix is positive definite because \(L+1\ge r+1\) distinct integer sample points occur with positive weights. This exact Gram formula is consistent with the known one-variable higher-multiplicity projection theorem [2]; its use is a proof step, not the claimed new result.

**3. The critical monomial weights have a universal linear tail.** Stirling's formula applied to the factorial ratio yields, for fixed parameters,
\[
w_k=Ck\big(1+O(k^{-1})\big),\qquad
\frac1{w_k}=\frac1{Ck}+O(k^{-2}),\quad k\to\infty.
\]
The displayed constant \(C\) follows because the exponential factor \(c^{2k}\) cancels the factorial large-deviation factor, and the critical exponent gives precisely the power \(k^1\). In particular the series defining \(\Lambda\) converges absolutely, and
\[
C(G_L)_{00}=\log L+\Lambda+o(1).
\]

**4. The finite-rank Schur complement identifies the entire second term.** If \(r=1\), the Gram matrix is scalar and the result follows immediately. Otherwise write the block Gram matrix as \(G_L=\bigl(\begin{smallmatrix}A&v^\mathsf T\\v&B\end{smallmatrix}\bigr)\), indexed by \(0\) versus \(1,\ldots,r-1\). The Schur complement gives
\[
E_{K,r}^{-1}=A-v^\mathsf TB^{-1}v.
\]
For fixed \(i,j\ge1\), the linear weight asymptotic and Riemann sums show
\[
CL^{-i}v_i\longrightarrow\frac1i,
\qquad
CL^{-(i+j)}B_{ij}\longrightarrow\frac1{i+j}.
\]
Put \(b_i=1/i\) and \(H_{ij}=1/(i+j)\), for \(1\le i,j<r\). The matrix \(H\) is positive definite (it is the Gram matrix of \(x^{i-1/2}\) in \(L^2(0,1)\)). Consequently,
\[
C\,v^\mathsf TB^{-1}v\longrightarrow b^\mathsf TH^{-1}b.
\]
To evaluate the scalar exactly, introduce the \(r\)-by-\(r\) Cauchy matrix \(J_{ij}(\varepsilon)=1/(i+j+\varepsilon)\) with indices \(0\le i,j<r\), and its \((r-1)\)-by-\((r-1)\) lower-right principal block \(J_+(\varepsilon)\). The Cauchy determinant identity gives its exact Schur complement:
\[
\frac{\det J(\varepsilon)}{\det J_+(\varepsilon)}
=\frac1\varepsilon\prod_{j=1}^{r-1}
\left(\frac{j}{j+\varepsilon}\right)^2
=\frac1\varepsilon-2H_{r-1}+O(\varepsilon).
\]
On the other hand, directly taking the Schur complement of \(J(\varepsilon)\) gives \(\varepsilon^{-1}-b(\varepsilon)^\mathsf T J_+(\varepsilon)^{-1}b(\varepsilon)\), with \(b_i(\varepsilon)=1/(i+\varepsilon)\). Letting \(\varepsilon\downarrow0\) proves the **exact identity**
\[
b^\mathsf TH^{-1}b=2H_{r-1}.
\]
Thus \(C/E_{K,r}=\log L+\Lambda-2H_{r-1}+o(1)\). Since \(L=K+r\), \(\log L-\log K\to0\), proving the first boxed formula. Subtracting the \(r=1\) expansion yields the second. Taking the difference of reciprocal expansions, using \(E_{K,r}\sim C/\log K\), yields the squared-error difference and its sharp constant. Every limit is for a fixed \(n,m,(a_j),r\).

## Verification
The standalone `verify_critical_multiplicity.py` executes exact rational checks of the Cauchy/Hilbert Schur identity for \(2\le r\le9\), and independent floating-point moment sums at degree \(20{,}000\) for the exponent patterns \((n;a_j)=(2;1,1),(3;1,2),(4;2,3,1)\) and \(r=2,3,4\). All tests completed successfully with `CHECK_OK`. These finite checks test normalization, weight recurrence, and the limiting harmonic coefficient; Steps 1–4 supply the proof for all admissible parameters. Reproduce by running `python3 verify_critical_multiplicity.py` with standard Python only, in the directory containing the embedded file.

## Relationship to prior work
Vavitsas [1, §2] records the sharp qualitative cyclicity threshold for the symmetric squarefree model \(1-m^{m/2}z_1\cdots z_m\), and explicitly poses broader problems about boundary zero geometry in ball Dirichlet spaces. The present theorem studies the **sharp second-order approximation cost of arbitrary fixed powers** of normalized monomial models at that same critical index; it makes no claim to resolve general cyclicity classification.

Bénéteau, Manolaki, and Seco [2, Theorem 7.1] give the exact generic one-variable finite Gram-matrix formula for optimal approximation to \((1-z)^r\), and [2, Theorem 7.3 and subsequent critical case] determine the leading degree-asymptotic norm in Dirichlet weights. Our Step 2 is an instance of their earlier formula after the explicitly proved symmetry reduction. Neither their stated critical asymptotic nor their higher-multiplicity theorem evaluates the **renormalized finite difference** \(C(E_{K,r}^{-1}-E_{K,1}^{-1})\) or the universal value \(-2H_{r-1}\). Their exact finite formula is sufficiently general to provide a starting point for deriving this constant; the new contribution is its proved, geometry-independent second-order extraction. That relation is a genuine historical priority caveat, not a claim that their finite formulas are inapplicable.

Sargent and Sola [3, §§4 and 6] establish general multivariable optimal-approximant methods and discuss polynomial factors in a coordinate product in the bidisk. Their examined statements do not contain a critical logarithmic multiplicity invariant for normalized ball monomials. A separately indexed previous analysis may have already extracted the same Cauchy-matrix constant, which remains the principal residual originality risk.

## Limitations
The asymptotics are fixed-parameter, critical-weight and polynomial-degree results only. There is no uniformity for growing multiplicity or degenerating monomial exponent distributions, and no conclusion about arbitrary stable polynomials or non-polynomial multipliers. The first-order law and exact finite Gram apparatus are known background; only the explicit universal second-order multiplicity penalty is submitted as the finding. A full independent priority check and independent proof audit have not been performed.

## References
[1] D. Vavitsas, *An overview of cyclicity in Dirichlet-type spaces in the unit ball*, arXiv:2607.05997v1, first public 2026-07-07; especially §1.1 and §2.

[2] C. Bénéteau, M. Manolaki, and D. Seco, *Boundary behavior of optimal polynomial approximants*, arXiv:1901.00694v2 (2019), especially §7, Theorems 7.1 and 7.3 and critical-case equation (50).

[3] M. Sargent and A. A. Sola, *Optimal approximants and orthogonal polynomials in several variables*, arXiv:2002.08790v2 (2020), especially §§4 and 6.

# Exact nullspace inflation for Gaussian reduced least-squares pseudoinverses

## Finding

Let integers \(d,r,\ell\) satisfy \(1\le r<d\) and \(r\le\ell\le d\), and let \(J\in\mathbb R^{r\times d}\) have orthonormal rows. Fix any nonzero \(c\in\mathbb R^r\). Draw \(S\in\mathbb R^{d\times\ell}\) with independent standard Gaussian entries and put \(L=\operatorname{col}(S)\). Consider two exact reduced least-squares solutions to \(Jx=c\):

\[
 x_{\mathrm{coeff}}=S(JS)^\dagger c,\qquad
 x_{\mathrm{geom}}=\underset{x\in L,\,Jx=c}{\operatorname{argmin}}\,\|x\|_2,
 \qquad x_*=J^{\mathsf T}c.
\]

The coefficient-pseudoinverse solution minimizes the **sketch coefficient norm**, whereas the geometric solution minimizes the **physical Euclidean norm** among feasible vectors in the same random subspace. Both are almost surely well-defined. Put \(\nu=\ell-r+1\). If \(U_k\) and \(V_\nu\) denote independent chi-squared variables with indicated degrees of freedom (within each displayed marginal distribution), then

\[
 \frac{\|x_{\mathrm{coeff}}-x_*\|_2^2}{\|c\|_2^2}
 \ \overset{\mathrm d}=\ \frac{U_{d-r}}{V_\nu},
 \qquad
 \frac{\|x_{\mathrm{geom}}-x_*\|_2^2}{\|c\|_2^2}
 \ \overset{\mathrm d}=\ \frac{U_{d-\ell}}{V_\nu}\quad(\ell<d).
\]

When \(\ell=d\), the geometric error is identically zero; the coefficient-pseudoinverse law remains valid. The two ratio formulas state **marginal**, not joint, distributions. For either nonzero-error law with numerator degree \(p>0\) and denominator degree \(\nu\), every \(q>0\) satisfies

\[
 \mathbb E\|x-x_*\|_2^q =
 \|c\|_2^q\,
 \frac{\Gamma((p+q)/2)\,\Gamma((\nu-q)/2)}
 {\Gamma(p/2)\,\Gamma(\nu/2)}
 \quad\text{if }q<\nu,
\]

and the expectation is infinite if \(q\ge\nu\). In particular, finite mean-square error for the nonzero-error cases occurs **if and only if** \(\ell\ge r+2\), with the sharp expectations

\[
 \mathbb E\|x_{\mathrm{coeff}}-x_*\|_2^2
 =\frac{d-r}{\ell-r-1}\|c\|_2^2,\qquad
 \mathbb E\|x_{\mathrm{geom}}-x_*\|_2^2
 =\frac{d-\ell}{\ell-r-1}\|c\|_2^2.
\]

The second identity also holds at \(\ell=d\) whenever \(\ell\ge r+2\), with both sides zero. For \(p>0\), the exact positive tail constant is

\[
 \lim_{t\to\infty}t^\nu\,\mathbb P(\|x-x_*\|_2>t)
 =\|c\|_2^\nu\,
 \frac{\Gamma((p+\nu)/2)}{\Gamma(p/2)\,\Gamma(\nu/2+1)}.
\]

As a sharp full-span instance, \(d=2,r=1,\ell=2\) makes \(x_{\mathrm{geom}}=x_*\) exactly, but \(\mathbb E\|x_{\mathrm{coeff}}-x_*\|_2^2=\infty\), despite \(L=\mathbb R^2\) almost surely.

## Assumptions and scope

Everything is in real Euclidean arithmetic. The matrix \(J\) has full row rank and unit orthogonal rows; \(c\) is deterministic and nonzero. The sketch has independent \(N(0,1)\) entries and \(r\le\ell\le d\). The same conclusions hold under a common positive rescaling of the sketch because both computed vectors are scale invariant. The reduced constraint is solved **exactly**, with minimum Euclidean norm in coefficient space for the first rule and in physical space for the second. Neither rule includes regularization, a trust region, noisy residuals, or finite-precision rank decisions.

## Proof

**1. Canonical coordinates and feasibility.** Orthogonal invariance of Gaussian matrices permits taking \(J=(I_r\ 0)\). Then \(x_*=(c,0)\). Write \(S=(G^{\mathsf T},B^{\mathsf T})^{\mathsf T}\) where \(G\in\mathbb R^{r\times\ell}\) and \(B\in\mathbb R^{(d-r)\times\ell}\) are independent standard Gaussian matrices. Almost surely \(G\) has row rank \(r\), and \(S\) has column rank \(\ell\), proving feasible reduced constraints. Every solution has the form \((c,y)\), so its squared excess over the global minimum-norm solution is \(\|y\|_2^2\).

**2. Coefficient-minimum law.** The coefficient-minimal reduced solution is \(S G^\dagger c\); its null component is \(y=B G^\dagger c\). Conditional on \(G\), this is centered Gaussian with covariance \(\|G^\dagger c\|_2^2 I_{d-r}\), and \(\|G^\dagger c\|_2^2=c^{\mathsf T}(GG^{\mathsf T})^{-1}c\). For a standard Gaussian \(p\times n\) matrix \(Z\), with \(n\ge p\), and deterministic unit \(u\in\mathbb R^p\), a Schur-complement argument gives

\[
 \left(u^{\mathsf T}(ZZ^{\mathsf T})^{-1}u\right)^{-1}
 \overset{\mathrm d}=\chi^2_{n-p+1}.
\]

Indeed rotate \(u\) to the first basis vector and project the first Gaussian row onto the orthogonal complement of the other \(p-1\) rows in \(\mathbb R^n\), which has dimension \(n-p+1\). The projected squared norm is the required Schur complement. Using \(p=r,n=\ell\), the conditional Gaussian null component supplies an independent \(\chi^2_{d-r}\) numerator, establishing the first ratio.

**3. Physical-minimum law.** When \(\ell=d\), the subspace is all of \(\mathbb R^d\) and the physical minimum is \(x_*\). Otherwise put \(k=d-\ell\), draw an independent standard Gaussian \(H\in\mathbb R^{k\times d}\), and use \(\ker H\) as an equivalent Haar-distributed random \(\ell\)-plane. Partition \(H=(H_1\ H_2)\), with \(H_1\in\mathbb R^{k\times r}\) and \(H_2\in\mathbb R^{k\times(d-r)}\). The condition \((c,y)\in\ker H\) is \(H_2y=-H_1c\). As \(d-r\ge k\), the unique minimum-norm null component is \(y=-H_2^\dagger H_1c\). The Gaussian vector \(H_1c/\|c\|_2\) is standard normal in \(\mathbb R^k\), independent of \(H_2\). Consequently, its quadratic form with \((H_2H_2^{\mathsf T})^{-1}\) is a ratio of independent \(\chi^2_k\) and \(\chi^2_{d-r-k+1}=\chi^2_{\ell-r+1}\) variables, by rotational invariance and the same Schur-complement identity. This proves the second ratio law.

**4. Moments and tails.** For independent \(U\sim\chi^2_p\), \(V\sim\chi^2_\nu\), direct integration of Gamma densities gives \(\mathbb E(U/V)^{q/2}=\Gamma((p+q)/2)\Gamma((\nu-q)/2)/[\Gamma(p/2)\Gamma(\nu/2)]\) exactly when \(0<q<\nu\); the integral at zero for \(V\) diverges for \(q\ge\nu\). At \(q=2\), this reduces to \(p/(\nu-2)\) if \(\nu>2\). As \(v\downarrow0\), the chi-squared cdf obeys \(\mathbb P(V\le v)\sim v^{\nu/2}/(2^{\nu/2}\Gamma(\nu/2+1))\). Conditioning on \(U\), dominated convergence (the cdf is globally bounded above by a constant times \(v^{\nu/2}\), and \(U\) has all positive moments) yields the stated sharp power-law tail constant. All cases, including moment divergence and the full-span contrast, follow.

## Verification

Run \(\texttt{python verify.py}\) with NumPy installed. The script independently computes each reduced solution by pseudoinverse or QR on eight dimension triples, checks exact feasibility, checks the physical minimum-norm inequality and the full-span special case, and tests the Gamma moment expression against its elementary second-moment specialization. The finite computations serve as independent consistency checks; the proof above, not simulation, establishes the distributional and infinite-moment assertions.

A deterministic full-span witness is \(J=(1\ 0)\), \(S=\begin{psmallmatrix}1&1\\0&1\end{psmallmatrix}\), \(c=1\): here \(S(JS)^\dagger c=(1,1/2)\), whereas the physical minimum is \((1,0)\).

## Relationship to prior work

Cartis, Fowkes and Shao (2022) motivate solving reduced Jacobian least-squares models in random variable subspaces, and supply globalized trust-region/regularized algorithms. This theorem instead concerns **unsafeguarded exact Moore–Penrose completions** of a rank-deficient linear model, not the convergence claims of that safeguarded algorithm. Pes and Rodriguez (2021) motivate selecting minimum physical norm for underdetermined Gauss–Newton steps. LeJeune and coauthors investigate broad asymptotic sketched pseudoinverse behavior and orthogonal-sketch comparisons, rather than the present two exact finite-dimensional marginal laws and threshold under coefficient versus physical tie-breaking. Standard Gaussian inverse-Wishart and chi-squared identities are explicitly used, not asserted to be new.

The claimed contribution is the combined sharp comparison and full-span pathology for two precisely defined reduced-solver tie-breaking rules; independent historical priority checking remains necessary.

## Limitations

The result treats a single rank-deficient, exactly consistent linear least-squares step. It does not address nonlinear iteration convergence, acceptance safeguards, variable-accuracy methods, sketch distributions other than Gaussian/Haar-equivalent, or stable numerical implementations. The marginal ratio formulas do not specify a joint distribution of the two errors. The exact formulas rely on orthonormal measurement rows; arbitrary row conditioning changes the scale and structure. No independent scientific validation is claimed.

## References

1. F. Pes and G. Rodriguez, *A doubly relaxed minimal-norm Gauss–Newton method for underdetermined nonlinear least-squares problems*, arXiv:2101.07560, first public 2021-01-19. https://arxiv.org/abs/2101.07560
2. C. Cartis, J. Fowkes and Z. Shao, *A Randomised Subspace Gauss-Newton Method for Nonlinear Least-Squares*, arXiv:2211.05727, first public 2022-11-10. https://arxiv.org/abs/2211.05727
3. D. LeJeune, P. Patil, H. Javadi, R. G. Baraniuk and R. J. Tibshirani, *Asymptotics of the Sketched Pseudoinverse*, SIAM J. Math. Data Sci., DOI:10.1137/22M1530264, https://doi.org/10.1137/22M1530264

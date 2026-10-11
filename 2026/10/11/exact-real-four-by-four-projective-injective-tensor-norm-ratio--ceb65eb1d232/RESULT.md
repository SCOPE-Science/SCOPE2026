# Exact real four-by-four projective–injective tensor norm ratio

## Finding
For every real \(4\times4\) matrix \(A=(a_{ij})\), with indices \(0\le i,j\le3\), put
\[
P(A)=\sum_{i,j=0}^{3}|a_{ij}|,\qquad
C(A)=\max_{\varepsilon,\delta\in\{-1,1\}^{4}}
\left|\sum_{i,j=0}^{3}a_{ij}\varepsilon_i\delta_j\right|.
\]
Then the optimal constant in the inequality \(P(A)\le K C(A)\) is exactly
\[
\boxed{K=\frac{12}{5}}.
\]
Equivalently, for real finite-dimensional \(\ell_1\) spaces, the projective-to-injective tensor norm ratio is
\[
\boxed{\rho(\ell_1^{4}(\mathbb R),\ell_1^{4}(\mathbb R))=\frac{12}{5}}.
\]
Thus the normalized square endpoint of Santos–Serrano-Rodríguez is \(B_4^{\mathbb R}=6/5\). Their established endpoint-compression identity also gives \(\Gamma_\infty^{\mathbb R}(r;4,4)=12/5\) for every integer \(r\ge4\). These are equivalent descriptions of this single sharp real tensor-norm constant, not separate novel theorems.

## Assumptions and scope
All scalar entries are real; the dimension is exactly \(4\times4\), with no positivity, symmetry, or rank restriction. The standard projective tensor norm on \(\ell_1^4\otimes\ell_1^4\) equals \(P(A)\), while the injective tensor norm equals \(C(A)\). The real field matters: independent complex phases are not covered. The ratio is defined for nonzero matrices; at zero the inequality is trivially true.

## Proof
**1. Exact lower witness.** Take
\[
H=\begin{pmatrix}
2&2&1&1\\
2&-1&-1&-2\\
1&-1&-2&2\\
1&-2&2&1
\end{pmatrix}.
\]
Direct integer summation gives \(P(H)=24\). Among all \(2^8\) signed bilinear evaluations (equivalently, among the \(128\) distinct sign vertices after fixing the first left sign), the largest absolute value is \(10\). Hence \(P(H)/C(H)=24/10=12/5\). The verifier independently enumerates these finitely many evaluations.

**2. Reduction to a finite universal sign inequality.** Given \(A\), let \(S=(s_{ij})\in\{\pm1\}^{4\times4}\) choose an arbitrary sign at every zero entry and the sign of \(a_{ij}\) otherwise. Then \(P(A)=\sum s_{ij}a_{ij}\). Multiplying rows and columns of both \(S\) and \(A\) by independent signs does not change \(P(A)\) or \(C(A)\), and it can transform \(S\) to a *normal form* with first row and first column all \(+1\). Exactly \(2^9=512\) normal-form sign patterns remain, indexed lexicographically by the nine bottom-right signs.

**3. Rational sign-vertex decomposition.** Let \(V\) comprise the \(128\) rank-one sign matrices \(v_{\varepsilon,\delta}=(\varepsilon_i\delta_j)_{ij}\), with \(\varepsilon_0=1\) and arbitrary remaining \(\varepsilon_i,\delta_j\in\{\pm1\}\). For each one of the \(512\) normal-form sign patterns \(S\), the accompanying file `endpoint_certificates.json` supplies a finite family of *strictly positive rational* coefficients \(\lambda_{S,v}\) satisfying the **exact** identities
\[
S=\sum_{v\in V}\lambda_{S,v}v,
\qquad
\sum_{v\in V}\lambda_{S,v}\le\frac{12}{5}.
\]
These are not approximate numerical optimizations: the standalone standard-library verifier `verify_exact.py` reconstructs every \(S\) and every rank-one sign vertex from their definitions, parses every coefficient as an exact rational, and checks all \(512\cdot16\) coordinate equalities and all \(512\) coefficient-mass inequalities. It also independently verifies the witness.

**4. Global upper bound.** If \(A\) is paired with a normal-form sign pattern \(S\), the decomposition yields
\[
P(A)=\sum_{ij}s_{ij}a_{ij}
=\sum_{v\in V}\lambda_{S,v}\sum_{ij}v_{ij}a_{ij}
\le C(A)\sum_{v\in V}\lambda_{S,v}
\le\frac{12}{5}C(A).
\]
The gauge transformation in step 2 extends this inequality to every real \(A\), including those with zero entries. Combined with step 1, sharpness follows. Finally, identification of the two tensor norms is elementary from their definitions on the canonical \(\ell_1\) bases. The endpoint \(\Gamma_\infty\) statement then follows from the previously established endpoint-compression identity, rather than from an additional unproved assertion.

## Verification
The self-contained evidence comprises `endpoint_certificates.json` (all \(512\) explicit rational coefficient sets) and `verify_exact.py` (a standard-library exact checker using `fractions.Fraction`, no network, and no optimization packages). From the directory containing both files run `python3 verify_exact.py`. The expected success marker is `REAL_4x4_PROJECTIVE_INJECTIVE_EXACT_CERTIFICATE_OK`. All scientific checks are equality/integer/rational comparisons; floating-point linear programming used to *discover* the certificates is not needed for their validity.

## Relationship to prior work
Santos and Serrano-Rodríguez, arXiv:2610.04398v1 (public 2026-10-03), define the square tensor-norm endpoint \(B_d^{\mathbb K}\), prove the exact endpoint compression \(\Gamma_\infty^{\mathbb K}(r;m,n)=\rho(\ell_1^m,\ell_1^{\min\{r,n\}})\), and establish general dimension-dependent bounds. Their Section 4 evaluates the complex two-row endpoints, while Section 8 leaves finer square-endpoint behavior open. Neither the sharp real \(4\times4\) ratio nor the above rational certificate appears in the inspected sections. Aubrun–Lami–Palazuelos–Szarek–Winter (arXiv:1809.10616, Proposition 13) establish the equivalent restricted \(1\)-summing formulation, while their Proposition 14 gives the unrestricted bound \(\pi_1(\mathrm{Id}_{\ell_1^4})=8/3\); that upper bound is strictly larger than the present exact restricted value \(12/5\). Earlier work on positive-semidefinite tensor norm ratios by Gupta–Mal–Misra–Ray (arXiv:2607.08441v1) studies a different restricted cone. Ambrus–Grundbacher (arXiv:2502.13752v2) study general signed-sum and summing constants, without the exact four-vector real \(\ell_1^4\) endpoint in the inspected material. The unconditioned real \(4\times4\) problem is not covered by conclusions about positive-semidefinite matrices, generic dimension bounds, or saturation only at larger row counts.

## Limitations
The theorem is restricted to real \(4\times4\) matrices and gives no exact constants for complex entries, higher dimensions, or other exponent pairs. Rational finite certificates prove this *finite* universal matrix inequality; they do not imply new asymptotics for \(B_d^{\mathbb R}\). Source comparison is based on the accessible primary literature and records listed in the accompanying review; an unindexed equivalent older result remains an originality risk. Independent auditing has not been performed.

## References
1. J. Santos and D. Serrano-Rodríguez, *Effective Dimensions in Grothendieck–Hölder Inequalities*, arXiv:2610.04398v1, 2026-10-03, especially Section 4 and Section 8, https://arxiv.org/html/2610.04398v1.
2. R. Gupta, A. Mal, G. Misra and S. K. Ray, *Extreme points, positive Grothendieck constants and tensor product norms*, arXiv:2607.08441v1, 2026-07-09, especially Sections 2 and 3, https://arxiv.org/abs/2607.08441.
3. G. Aubrun, L. Lami, C. Palazuelos, S. J. Szarek and A. Winter, *Universal Gaps for XOR Games from Estimates on Tensor Norm Ratios*, Communications in Mathematical Physics 375 (2020), 679–724, arXiv:1809.10616, especially Propositions 13–14, https://link.springer.com/article/10.1007/s00220-020-03688-2.
4. G. Ambrus and F. Grundbacher, *Large Signed Sums and the Polarization Constant of Convex Bodies*, arXiv:2502.13752v2, Section 4, https://arxiv.org/abs/2502.13752.

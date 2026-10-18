# Sharp discrete second-difference \(\ell^2\to\ell^\infty\) constants and central splines

## Finding

Let \(n\ge1\) be an integer, let \(a=(a_1,\ldots,a_n)\in\mathbb C^n\), and extend \(a_k=0\) outside \(1\le k\le n\). For \(1\le k\le n+2\) put \(b_k=a_k-2a_{k-1}+a_{k-2}\) and \(\mathcal E(a)=\sum_{k=1}^{n+2}|b_k|^2\). For every \(1\le j\le n\), the sharp point-evaluation inequality is

\[
|a_j|^2\le G_{n,j}\mathcal E(a),\qquad
G_{n,j}=\frac{j(j+1)(n+2-j)(n+1-j)\big(2j(n+1-j)+n+3\big)}{6(n+1)(n+2)(n+3)}.
\]

Consequently the optimal global embedding norm \(C_n=\sup_{a\ne0}\|a\|_{\ell^\infty}/\sqrt{\mathcal E(a)}\) is given by \(C_n^2=\max_{1\le j\le n}G_{n,j}\). With \(r\) a nonnegative integer in the odd case and a positive integer in the even case, its closed form is

\[
C_{2r+1}^2=\frac{(r+1)(r+2)(r^2+3r+3)}{12(2r+3)},\qquad
C_{2r}^2=\frac{r(r+1)(r+2)(2r^2+4r+3)}{12(2r+1)(2r+3)}.
\]

For odd \(n\), the sole norming coordinate is \(j=(n+1)/2\); for even \(n\), the two are \(j=n/2\) and \(j=n/2+1\). For each norming coordinate, exactly one complex ray of nonzero sequences attains the global inequality. Explicitly let \(m=n+2\) and

\[
\begin{aligned}
A_j&=\frac{j(j+1)(2m-1-j)}{m(m-1)},\\
B_j&=\frac{j(j+1)(2j-3m+1)}{m(m-1)(m+1)},\\
\rho_{j,k}&=(j+1-k)_+-A_j-B_j k\quad(1\le k\le m),\\
a_i^{(j)}&=\sum_{k=1}^i(i+1-k)\rho_{j,k}\quad(1\le i\le n),
\end{aligned}
\]

where \((x)_+=\max\{x,0\}\). All nonzero global extremizers are precisely the nonzero complex scalar multiples of \(a^{(j)}\) for norming \(j\). The sharp large-length asymptotic is

\[
\lim_{n\to\infty}\frac{C_n}{n^{3/2}}=\frac1{8\sqrt3}.
\]

## Assumptions and scope

The domain consists of every finite complex or real sequence of length \(n\ge1\), with **zero extension on both sides** and the backward second difference on all \(n+2\) potentially nonzero sites. This is the homogeneous discrete clamped second-difference energy, not the first-difference energy, a periodic energy, or an interior-only second-difference sum. No regularity, sign, or symmetry is required. Sharpness and equality are asserted for each finite length, not merely asymptotically.

## Proof

**1. Range and moments.** The linear map \(D:\mathbb C^n\to\mathbb C^{m}\) taking \(a\) to \(b\) is injective: its first \(n\) rows form a triangular matrix with diagonal \(1\). Telescoping the zero-extended second differences gives

\[
\sum_{k=1}^m b_k=0,\qquad \sum_{k=1}^m k b_k=0.
\]

The moment-zero subspace \(H=\{b\in\mathbb C^m:\sum b_k=\sum k b_k=0\}\) has dimension \(m-2=n\). Therefore \(\operatorname{ran}D=H\). Double summation shows that the value at any site can be recovered as

\[
a_j=\sum_{k=1}^j(j+1-k)b_k=\langle b,v_j\rangle,\qquad
(v_j)_k=(j+1-k)_+,\quad 1\le k\le m,
\]

using the standard Hermitian scalar product (\(v_j\) is real). The evaluation functional on \(H\) is represented by \(\rho_j=P_Hv_j\), with \(P_H\) the orthogonal projection. Cauchy–Schwarz yields \(|a_j|^2\le\|\rho_j\|_2^2\|b\|_2^2\), with equality exactly if \(b\) is a complex scalar multiple of \(\rho_j\).

**2. Orthogonal projection and its exact norm.** The orthogonal complement \(H^\perp\) is spanned by \(\mathbf1=(1,\ldots,1)\) and \((1,2,\ldots,m)\). The Gram matrix of this spanning pair and the moments of \(v_j\) are

\[
Q=\begin{pmatrix}m&m(m+1)/2\\m(m+1)/2&m(m+1)(2m+1)/6\end{pmatrix},\qquad
u_j=\begin{pmatrix}j(j+1)/2\\j(j+1)(j+2)/6\end{pmatrix}.
\]

Since \(\det Q=m^2(m^2-1)/12>0\), the least-squares affine polynomial \(A_j+B_j k\) has coefficients \((A_j,B_j)^\top=Q^{-1}\nu_j\), equal to those in the finding. As \(\|v_j\|_2^2=j(j+1)(2j+1)/6\), direct rational simplification gives

\[
\|P_Hv_j\|_2^2=\|v_j\|_2^2-\nu_j^\top Q^{-1}\nu_j=G_{n,j}.
\]

The vector \(\rho_j=v_j-(A_j+B_j k)_{k=1}^m\) belongs to \(H\). Since \(\operatorname{ran}D=H\), it has a unique preimage under \(D\). Repeated summation identifies that preimage with the explicit \(a^{(j)}\); thus the bounds are attained and the pointwise equality cases are exact.

**3. Central maximizers and uniqueness.** Subtracting consecutive rational expressions and factoring yields the exact identity

\[
G_{n,j+1}-G_{n,j}=
\frac{(j+1)^2(n+1-j)^2(n-2j)}{(n+1)(n+2)(n+3)}
\quad(1\le j<n).
\]

Every factor except \(n-2j\) is strictly positive. Hence \(G_{n,j}\) strictly rises toward the center, has a single central tie if \(n\) is even, and strictly declines afterward. Substitution of the central sites gives the claimed odd- and even-length formulas. If a nonzero \(a\) attains the global norm, at least one of its norming sites satisfies equality in the pointwise Cauchy–Schwarz step. Therefore its difference vector lies on the corresponding one-dimensional ray \(\mathbb C\rho_j\), and the injectivity of \(D\) gives the complete list of extremizers.

**4. Asymptotic.** The two closed forms yield \(C_n^2/n^3\to 1/192\), from which \(C_n/n^{3/2}\to1/(8\sqrt3)\).

## Verification

Run `python verify.py` in the directory containing this result. The standalone script uses only exact rational arithmetic for the finite checks. It independently inverts \(D^*D\) on lengths \(1\le n\le17\) and compares every Green diagonal against \(G_{n,j}\). It also reconstructs every proposed spline from its second differences, verifies the moment constraints, every adjacent-site difference identity, the center and parity cases, and three numerical asymptotic diagnostics. In the recorded execution it passed 938 checks. These finite checks corroborate the algebra but are not a proof for unbounded \(n\); the argument above supplies that proof.

## Relationship to prior work

Hindov, Nitzan, Olsen, and Rydhe's *A sharp higher order Sobolev embedding* (first posted 15 November 2024) treats **continuous** \(W_0^{k,2}(-1,1)\to L^1(-1,1)\) sharp inequalities and Landau-kernel extremizers. It motivates exact endpoint constants for second-order derivatives but does not imply the finite-lattice \(\ell^\infty\) norm or its parity-specific splines. Their later *A sharp discrete Sobolev inequality and left inverses of higher order differences* (posted 13 October 2026) gives sharp \(\ell^1\)-from-\(\ell^2\) bounds for all integer difference orders, not the exact \(\ell^\infty\)-from-\(\ell^2\) constant. Its description of the moment-kernel and row-polynomial freedom is consistent with the independent projection argument here; those general facts are not claimed as new. Yamagishi and Nagai (2022) find sharp maximum-norm constants for discrete **first**-difference Dirichlet energies, equivalent to inverses of second-order difference matrices; the present energy is the square norm of a **second** difference and leads to a fourth-order matrix with different boundary corrections.

## Limitations

This statement is restricted to integer difference order two, the zero-extended finite interval, and the Hilbert energy exponent two with supremum target. It does not determine the analogous constants for other exponents, weights, boundary conditions, or higher orders. The originality comparison is based on accessible full texts and record searches, not an exhaustive proof of publication priority. A general earlier formula for the same fourth-order Green diagonal could subsume the calculation despite different terminology; independent literature verification remains worthwhile.

## References

1. R. Hindov, S. Nitzan, J.-F. Olsen, E. Rydhe, *A sharp higher order Sobolev embedding*, arXiv:2411.10201v1 (15 November 2024), https://arxiv.org/abs/2411.10201 .
2. R. Hindov, S. Nitzan, J.-F. Olsen, E. Rydhe, *A sharp discrete Sobolev inequality and left inverses of higher order differences*, arXiv:2610.19010v1 (13 October 2026), https://arxiv.org/abs/2610.19010 .
3. H. Yamagishi, A. Nagai, *The best constant of discrete Sobolev inequality corresponding to a discrete bending problem of a string*, Saitama Mathematical Journal 34 (2022), 19–46, https://www.rimath.saitama-u.ac.jp/research/pdf/smj34-2.pdf .

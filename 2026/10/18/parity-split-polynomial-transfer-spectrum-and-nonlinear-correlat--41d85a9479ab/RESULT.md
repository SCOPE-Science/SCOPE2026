# The finite polynomial spectrum of an even-symmetric four-branch map

## Finding

Let \(0<d<1/2\) and \(a=1/2-d\). Consider the map \(T_d\) with branches
\[
 T_d(x)=\begin{cases}
 x/d,&0\le x<d,\\
 (x-d)/a,&d\le x<1/2,\\
 (1-d-x)/a,&1/2\le x<1-d,\\
 (1-x)/d,&1-d\le x\le1.
 \end{cases}
\]
Its Lebesgue transfer operator \(P_d\) preserves \(\mathcal V_m=\mathbb R[x]_{\le m}\) for every integer \(m\ge0\). On this space it is diagonalizable with multiset
\[
\{1\}\cup\{0\}^{\lceil m/2\rceil}\cup
\{2(d^{2j+1}+a^{2j+1}):1\le j\le\lfloor m/2\rfloor\}.
\]
The kernel consists exactly of polynomials odd about \(1/2\). In particular there are no generalized eigenvectors at zero outside the kernel, and every nonzero polynomial eigenvalue occurs in its least possible degree (zero for the constant mode and \(2j\) for the \(j\)-th nonconstant mode). This determines which polynomial transfer modes vanish after one step and all surviving polynomial decay rates; coordinate or quadratic autocorrelation alone does not determine this spectrum.

## Proof

Changing variables on each affine branch gives, up to null sets,
\[
 (P_df)(y)=d[f(dy)+f(1-dy)]+a[f(d+ay)+f(1-d-ay)].
\]
The weights sum to one, so Lebesgue measure is invariant. In increasing-degree powers of \(u(x)=x-1/2\), the operator is triangular. Reflected arguments cancel identically on all odd powers. On \(u^{2j}\), the highest-degree coefficient is \(2(d^{2j+1}+a^{2j+1})\), also valid for the constant mode at \(j=0\). These coefficients are positive and strictly decrease with \(j\) since \(d,a\in(0,1/2)\). Thus the top nonzero term of any even polynomial survives, proving the kernel assertion. Its dimension equals the number of odd powers in the basis, which is the algebraic multiplicity of zero. The other eigenvalues are each simple, proving diagonalizability. The triangular diagonal and the invariance of lower-degree spaces show the stated first occurrence of each nonzero mode. On mean-zero polynomial densities the constant mode is absent, because \(P_d\) preserves integrals and any eigenvector with eigenvalue other than one has integral zero.

## Context and verification

The map is the four-branch even-symmetric map in El-den, Raslan and Abdullah, *Even symmetric chaotic and skewed maps as a technique in video encryption*, §3.1, doi:10.1186/s13634-023-01003-4. The construction of the map and its cubic conjugate are not contributions here. The exact coordinate and quadratic pair-correlation laws are specializations of the full-branch formulas in *Exact third-order correlations distinguish full-branch interval maps* (Resultary 2158555bdbfa, Proof, pair-correlation identities). The conjugate-map pair laws follow by changing variables, and are not separate findings. The spectrum above concerns all finite polynomial degrees, including the multiplicity and semisimplicity of the zero eigenvalue. It does not assert the whole function-space spectrum, any bitstream property, or any cryptographic security statement. Earlier covariance literature including Sang–Wang–Yan (doi:10.1109/78.863058) was not fully accessible, so equivalent antecedents are not excluded.

The supplied `verify.py` checks the transfer identities and leading terms through degree fourteen, among other low-degree checks. The triangular argument proves the statement for every \(m\) without requiring that script.

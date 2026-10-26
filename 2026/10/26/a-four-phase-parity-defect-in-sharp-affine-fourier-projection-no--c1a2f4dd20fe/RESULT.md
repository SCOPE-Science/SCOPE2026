# A four-phase parity defect in sharp affine Fourier projection norms

## Finding

For each integer \(n\ge3\), let
\[
H_n=\{x\in\{-1,1\}^n:\prod_{i=1}^n x_i=1\}
\]
carry normalized counting measure. Let \(P_n\) be the \(L^2(H_n)\)-orthogonal projection onto the \((n+1)\)-dimensional space of affine coordinate functions \(\operatorname{span}\{1,x_1,\ldots,x_n\}\). Write \(\Lambda_n^+\) for either its \(\ell^1\)- or \(\ell^\infty\)-operator norm, and \(\Lambda_n^{\mathrm{cube}}\) for the norm of the analogous affine projector on the unrestricted uniform sign cube. Define \(b_m=4^{-m}\binom{2m}{m}\). Then the two endpoint norms coincide, and
\[
\boxed{\Lambda_{2m}^+=b_m\left(2m+1+\frac{(-1)^{m+1}}{2m-1}\right)\quad(m\ge2),}
\]
\[
\boxed{\Lambda_{2m+1}^+=b_m\big(2m+1+(-1)^m\big)\quad(m\ge1).}
\]
In particular, the **exact relative effect of imposing one global parity check** is
\[
\boxed{\frac{\Lambda_n^+}{\Lambda_n^{\mathrm{cube}}}=\begin{cases}
1+\dfrac{(-1)^{(n-1)/2}}n,&n\ge3\ \mathrm{odd},\\[2mm]
1+\dfrac{(-1)^{n/2+1}}{n^2-1},&n\ge4\ \mathrm{even}.
\end{cases}}
\]
This alternating correction is of relative order \(1/n\) for odd dimension and \(1/n^2\) for even dimension. It changes the dimension-dependence qualitatively: whenever \(n\equiv2\pmod4\) and \(n\ge6\), one has \(\Lambda_{n+1}^+<\Lambda_n^+\); whenever \(n\equiv1\pmod4\) and \(n\ge5\), one has \(\Lambda_{n+1}^+=\Lambda_n^+\). All other adjacent steps from dimension three onward are strictly increasing. Moreover,
\[
\lim_{n\to\infty}\frac{\Lambda_n^+}{\sqrt n}=\sqrt{\frac2\pi}.
\]
For every dimension and every output vertex, a sign-valued input attains the stated sharp \(\ell^\infty\) norm.

## Assumptions and scope

The code \(H_n\) is the even-parity, single-check binary linear code represented as sign vectors; its size is \(2^{n-1}\). Its natural metric is irrelevant to the operator norm. The measure is normalized counting measure, and \(P_n\) is the uniquely specified orthogonal projection on \(L^2(H_n)\), not an arbitrary projection. All statements apply to real-valued or complex-valued data with the ordinary absolute-value endpoint norms. The exceptional boundary dimension \(n=3\) gives \(\Lambda_3^+=1\), because the affine coordinate space then equals all functions on \(H_3\). The unrestricted reference \(\Lambda_n^{\mathrm{cube}}\) is defined separately on the full cube with \(2^n\) vertices.

## Proof

**1. Kernel and sharpness.** For \(n\ge3\), every proper subset of coordinate signs under the uniform measure on \(H_n\) is a family of independent fair signs. Hence \(1,x_1,\ldots,x_n\) are orthonormal in \(L^2(H_n)\). The integral kernel of the orthogonal projection is exactly
\[
K_n(x,y)=1+\sum_{i=1}^n x_i y_i=n+1-2d_H(x,y),
\]
where \(d_H\) denotes Hamming distance. For fixed \(x\in H_n\), the product \(xy\) ranges over \(H_n\); consequently \(d_H(x,y)\) takes only even values, with multiplicity \(\binom nj\) at even distance \(j\). The matrix entries of \(P_n\) are \(2^{1-n}K_n(x,y)\). Every row and every column has the same absolute sum, which proves
\[
\Lambda_n^+=2^{1-n}\sum_{\substack{0\le j\le n\\j\ \mathrm{even}}}\binom nj|n+1-2j|.
\tag{1}
\]
Choosing \(f(y)=\operatorname{sgn}K_n(x,y)\), with arbitrary signs at zeros, attains the \(\ell^\infty\) norm at the prescribed \(x\); symmetry gives the same \(\ell^1\) norm.

**2. Full-cube baseline.** For the unrestricted cube,
\[
\Lambda_n^{\mathrm{cube}}=2^{-n}\sum_{j=0}^n\binom nj|n+1-2j|.
\tag{2}
\]
If \(S_n\) is a sum of \(n\) independent fair signs, this equals \(\mathbb E|1+S_n|\). The standard simple-walk count gives \(\mathbb E|S_{2m}|=2m b_m\) and \(\Pr(S_{2m}=0)=b_m\); symmetry therefore yields \(\mathbb E|1+S_{2m}|=(2m+1)b_m\). For odd \(n=2m+1\), \(\mathbb E|1+S_n|=\mathbb E|S_{n+1}|=(2m+1)b_m\), using \(b_{m+1}/b_m=(2m+1)/(2m+2)\). Thus
\[
\Lambda_{2m}^{\mathrm{cube}}=\Lambda_{2m+1}^{\mathrm{cube}}=(2m+1)b_m.
\tag{3}
\]

**3. Exact alternating correction.** Splitting even and odd distances in (1) and (2) shows
\[
\Lambda_n^+-\Lambda_n^{\mathrm{cube}}=2^{-n}\sum_{j=0}^n(-1)^j\binom nj|n+1-2j|=:D_n.
\]
Put \(h=\lfloor(n+1)/2\rfloor\). Because the complete alternating sums of both \(\binom nj\) and \(j\binom nj\) vanish for \(n\ge3\), removing the absolute value by reflecting the terms above the sign change yields
\[
2^nD_n=2\sum_{j=0}^{h}(-1)^j\binom nj(n+1-2j).
\]
Use the exact truncated alternating identities
\[
\sum_{j=0}^h(-1)^j\binom nj=(-1)^h\binom{n-1}{h},\qquad
\sum_{j=0}^h(-1)^j j\binom nj=n(-1)^h\binom{n-2}{h-1}.
\]
It follows that
\[
2^nD_n=2(-1)^h\left[(n+1)\binom{n-1}{h}-2n\binom{n-2}{h-1}\right].
\tag{4}
\]
Substitution of \(n=2m\) and \(n=2m+1\) gives, respectively,
\[
D_{2m}=\frac{(-1)^{m+1}}{2m-1}b_m,\qquad D_{2m+1}=(-1)^m b_m.
\tag{5}
\]
Equations (3) and (5) prove both sharp formulas and the relative parity factors.

**4. Dimension pattern and asymptotics.** Direct subtraction of the two formulas, and the central-binomial recurrence, give the exact adjacent differences
\[
\Lambda_{2m+1}^+-\Lambda_{2m}^+=(-1)^m\frac{2m}{2m-1}b_m\qquad(m\ge2),
\]
\[
\Lambda_{2m+2}^+-\Lambda_{2m+1}^+=\frac{2m+1}{2m+2}b_m\big(1-(-1)^m\big)\qquad(m\ge1).
\]
Their signs give precisely the claimed alternating decreases, plateaux, and increases. Stirling's formula gives \(b_m\sim(\pi m)^{-1/2}\), and the corrections in (5) are of smaller order than the baseline \((2m+1)b_m\). This proves the limit.

## Verification

The standalone `verify.py` performs exact-rational binomial calculations in dimensions \(3\) through \(200\), comparing both closed forms, unrestricted baselines, relative ratios and adjacent-difference formulas. For dimensions \(3\) through \(10\), it independently enumerates all parity-code vertices, verifies all Gram entries of the stated orthonormal family, constructs every projection-kernel row, and exhibits sign-valued maximizers. Its successful replay reports `VERIFY_OK finite_n=3..200 exact_binomial_checks=791 direct_dimensions=3..10 direct_rows=1020 Gram_entries=492`. The all-dimensional conclusions follow from the proof, not numerical extrapolation.

## Relationship to prior work

Walsh characters, Fourier orthogonality and projection kernels on Boolean cubes are classical; Tan's 2012 exposition of the O'Donnell lectures supplies an accessible early reference. Defant, Galicer, Mansilla, Mastyło and Muro give a general compact-abelian-group Fourier projection norm formula and study Boolean cube projection constants. Their Theorem 3.1 and its underlying group-theoretic theorem already imply that the norm of a specified Fourier projection is the absolute kernel average; this general principle is explicitly credited. They do not evaluate the **single-parity-check subgroup** in the formulas above or establish the four-phase relative correction and dimension reversals. The known unrestricted-cube affine norm (3) is the comparison baseline, not a new contribution.

Results on first-band Fourier concentration on Hamming balls concern a spatially truncated full cube, not the orthogonal projector on an even-parity subgroup. Results on first absolute moments under arbitrary pairwise independent signs consider an extremal family of distributions; the fixed parity-conditioned distribution, the shift by a constant, and the operator-norm comparison here are different. Signed-permutation reflection-group isotypic projectors exhibit other parity defects but have different characters and averaging groups. In particular, none of the inspected comparison statements implies the explicit corrections (5) or the adjacent-dimension sign pattern.

## Limitations

The theorem only concerns the single even-parity check and affine coordinate functions; it does not classify projections on arbitrary binary linear codes, higher Walsh degrees, intermediate \(\ell^p\) norms, or nonuniform measures. The general row-sum identity is established theory and is not claimed as original. The claimed contribution is the exact finite central-binomial parity defect and its nonmonotone dimension consequence. An equivalent elementary alternating-binomial formula may exist in older coding or probability literature under different terminology; searches cannot exclude that possibility. No independent validation is claimed.

## References

1. L.-Y. Tan, *Analysis of Boolean Functions*, notes from lectures by R. O'Donnell, arXiv:1205.0314v1, first posted 2 May 2012; https://arxiv.org/abs/1205.0314.
2. A. Defant, D. Galicer, M. Mansilla, M. Mastyło and S. Muro, *Asymptotic insights for Projection, Gordon–Lewis and Sidon Constants in Boolean Cube Function Spaces*, arXiv:2302.00233, first posted 1 February 2023, especially Section 3 and its general compact-abelian-group norm formula; https://arxiv.org/html/2302.00233v2.
3. A. Defant, D. Galicer, M. Mansilla, M. Mastyło and S. Muro, *Projection constants for spaces of multivariate polynomials*, arXiv:2208.06467, first posted 12 August 2022; https://arxiv.org/abs/2208.06467.

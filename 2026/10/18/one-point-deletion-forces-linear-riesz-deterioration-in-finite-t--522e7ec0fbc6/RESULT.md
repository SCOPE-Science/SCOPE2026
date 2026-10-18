# One-point deletion forces linear Riesz deterioration in finite two-layer Fourier strips

## Finding
Let \(H\) be any finite abelian group of order \(n\ge2\), let \(m\ge2\), let \(h_0\in H\), and let
\[
G=H\times\mathbb Z_m,\qquad
E=(H\times\{0,1\})\setminus\{(h_0,1)\}.
\]
For \(\xi\in\widehat H\) and \(j\in\mathbb Z_m\), write \(\chi_{\xi,j}(h,y)=\xi(h)\exp(2\pi i jy/m)\). For any **set** \(B\subset\widehat H\times\mathbb Z_m\) of \(2n-1\) distinct characters, let \(T_B\) be the unnormalized square evaluation matrix \((\chi_{\xi,j}(h,y))_{(h,y)\in E,(\xi,j)\in B}\) and \(Q_B=T_B^*T_B\). Write \(B_\xi=\{j:(\xi,j)\in B\}\).

**Complete basis and determinant classification.** The matrix \(T_B\) is invertible if and only if every \(B_\xi\) contains one or two elements. Necessarily there is exactly one singleton fiber \(B_{\xi_0}\), while all other \(n-1\) fibers are doubletons. For such a basis partner,
\[
\boxed{\det Q_B=\prod_{\xi\ne\xi_0}n^2\left|e^{2\pi i j_\xi/m}-e^{2\pi i k_\xi/m}\right|^2},
\]
where \(B_\xi=\{j_\xi,k_\xi\}\). In particular the determinant does not depend on the deleted location \(h_0\), the singleton phase, or the structure of \(H\) beyond its order.

Set \(c_m=1\) when \(m\) is even, and \(c_m=\cos(\pi/(2m))\) when \(m\) is odd. Then
\[
\boxed{\max_{|B|=2n-1}|\det T_B|=(2n c_m)^{n-1}}.
\]
Every maximizing basis has exactly the above fiber occupancy, and every doubleton consists of a maximally separated pair on the regular \(m\)-gon: an antipodal pair for even \(m\), or a pair with difference congruent to \((m\pm1)/2\) for odd \(m\). Conversely every such basis maximizes the determinant. The exact number of unlabelled maximizing frequency sets is
\[
\boxed{n m K_m^{n-1}},\qquad
K_m=\begin{cases}m/2,&m\text{ even},\\m,&m\text{ odd}.\end{cases}
\]

**Sharp Riesz condition number when \(m\) is even.** Let \(L_B=\lambda_{\min}(Q_B)\), \(U_B=\lambda_{\max}(Q_B)\), and \(\rho_B=U_B/L_B\). For every invertible \(T_B\), regardless of parity,
\[
\boxed{L_B\le1,\quad U_B\ge2n,\quad\rho_B\ge2n}.
\]
When \(m\) is even, these three bounds are simultaneously sharp; equality in any of them occurs **exactly** for the same antipodal-doubleton frequency sets that maximize the determinant. For each such basis,
\[
\boxed{\operatorname{spec}(Q_B)=\{1\ (1\text{ time}),\;2n\ (2n-2\text{ times})\}}.
\]
In the terminology of optimal exponential Riesz bases, the four sharp quantities are \(\max_B L_B=1\), \(\min_B U_B=2n\), \(\min_B\rho_B=2n\), and \(\max_B|\det T_B|=(2n)^{n-1}\), with the same full optimizer classification. When \(m\) is odd, the inequality \(\rho_B>2n\) is strict for every basis.

**Complete determinant-optimal spectrum in odd order.** Suppose \(m\ge3\) is odd, and put \(s=\sin(\pi/(2m))\). For every determinant-optimal \(B\), the spectrum of \(Q_B\) consists of \(2n(1-s)\) with multiplicity \(n-2\), \(2n(1+s)\) with multiplicity \(n-2\), and the three values \(2n(1-y)\), where \(y\) runs through the three distinct real roots of
\[
\boxed{2n y^3-(2n-1)y^2-2s^2y+s^2=0}.
\]
All three values are positive. In particular, for fixed odd \(m\) and \(n\to\infty\), every such basis satisfies
\[
\lambda_{\min}(Q_B)\longrightarrow1-s^2,\qquad
\frac{\rho_B}{2n}\longrightarrow\frac1{1-s}.
\]
The odd-order statement optimizes the determinant and evaluates the condition number of the determinant-optimal configurations; it does **not** claim that these configurations minimize \(\rho_B\) among all odd-order partners.

**Deletion-instability contrast.** The unpunctured strip \(H\times\{0,1\}\) has an exponential Riesz basis with squared condition number at most \((1+s)/(1-s)\le3\) for odd \(m\ge3\), and an orthogonal character basis for even \(m\). Removing a **single** sample changes this bounded behavior to the universal lower bound \(2n\). Thus the one-point deletion enforces arbitrarily large relative conditioning as \(|H|\to\infty\).

## Assumptions and scope
All characters are complex-valued homomorphisms of modulus one, and the matrix entries are not normalized by the square root of the sample count. The set \(B\) is unweighted, consists of distinct ambient characters, and has exactly \(|E|=2n-1\) elements. The horizontal factor \(H\) can be cyclic or noncyclic. The two vertical coordinates are distinct because \(m\ge2\). The deleted point may be any \((h_0,1)\). The Riesz ratio \(\rho_B\) is the *squared* singular-value condition number.

All basis, determinant, parity, and spectral statements concern these objects only; there is no assertion about arbitrary near-rectangular subsets or non-character sampling functions.

## Proof
**1. Fiber occupancy and invertibility.** If three or more columns of \(T_B\) share the same horizontal character \(\xi\), their restrictions to \(H\times\{0,1\}\) lie in the two-dimensional space spanned by \(\xi(h)\mathbf1_{\{y=0\}}\) and \(\xi(h)\mathbf1_{\{y=1\}}\); they are dependent even before deleting a row. Every basis therefore has \(|B_\xi|\le2\). With \(n\) horizontal characters and \(2n-1\) columns, every fiber is nonempty, exactly one has size one, and the rest have size two.

Conversely, suppose these counts hold and \(\sum_{(\xi,j)\in B}c_{\xi,j}\chi_{\xi,j}\) vanishes on \(E\). Vanishing at every \((h,0)\) and horizontal Fourier orthogonality give \(\sum_{j\in B_\xi}c_{\xi,j}=0\) for every \(\xi\). The values at \((h,1)\) vanish for all \(h\ne h_0\); hence their horizontal Fourier coefficients have the form \(t\overline{\xi(h_0)}\) for one scalar \(t\) (up to the common Fourier normalization). In the singleton fiber \(\xi_0\), the preceding zero-sum relation forces its unique coefficient to vanish, so its first-layer coefficient also vanishes; therefore \(t=0\). Each doubleton now obeys a homogeneous two-by-two linear system with determinant \(e^{2\pi i k/m}-e^{2\pi i j/m}\ne0\), and all coefficients vanish. Hence \(T_B\) is invertible.

**2. Determinant identity.** Restore the deleted row and write the resulting \(2n\)-by-\((2n-1)\) matrix as \(T_0\), with \(D=T_0^*T_0\). Horizontal character orthogonality makes \(D\) block diagonal. A doubleton contributes the block \(nC^*C\), where \(C=\left(\begin{smallmatrix}1&1\\z_j&z_k\end{smallmatrix}\right)\) and \(z_j=e^{2\pi i j/m}\), of determinant \(n^2|z_k-z_j|^2\); the singleton contributes \(2n\). Consequently
\[
\det D=(2n)\prod_{\xi\ne\xi_0}n^2|z_{k_\xi}-z_{j_\xi}|^2.
\]
Let \(r\) denote the missing evaluation row and \(v=r^*\), so \(Q_B=D-vv^*\). The column space of \(T_0\) has codimension one in the full-strip space. Its orthogonal complement lies in the singleton horizontal Fourier mode and is vertically perpendicular to \((1,z_{j_{\xi_0}})\). The missing standard basis vector has squared projection \(1/(2n)\) onto this complement. Therefore \(1-v^*D^{-1}v=1/(2n)\). The matrix determinant lemma proves the stated determinant.

**3. Determinant optimum and count.** Each \(|z_j-z_k|\) is a chord of a regular \(m\)-gon. Its maximum is \(2\) for even \(m\) and \(2\cos(\pi/(2m))\) for odd \(m\). The factors in the determinant are independent, so all of them must separately attain their maximum. Choose the singleton horizontal character in \(n\) ways, its vertical frequency in \(m\) ways, and each of the remaining \(n-1\) unordered maximally spaced pairs in \(K_m\) ways. This yields the full classification and exact count.

**4. Universal conditioning obstruction and even-order equality.** Since \(v^*D^{-1}v=1-1/(2n)\), the Sherman--Morrison identity yields
\[
 v^*Q_B^{-1}v=\frac{v^*D^{-1}v}{1-v^*D^{-1}v}=2n-1.
\]
Every entry of \(v\) has modulus one and \(\|v\|^2=2n-1\). Its Rayleigh quotient for \(Q_B^{-1}\) is therefore one, so \(L_B\le1\). Because \(Q_B\) has dimension \(2n-1\) and diagonal entries \(2n-1\), its trace is \((2n-1)^2\). Averaging the remaining \(2n-2\) eigenvalues implies
\[
U_B\ge\frac{(2n-1)^2-L_B}{2n-2}\ge2n,
\]
and hence \(\rho_B\ge2n\).

If \(L_B=1\), then the already established Rayleigh quotient of \(v\) for \(Q_B^{-1}\) attains the largest eigenvalue, so \(Q_Bv=v\). Since \(Q_B=D-vv^*\) and \(\|v\|^2=2n-1\), this forces \(Dv=2nv\). Each doubleton block of \(D\) has eigenvalues \(2n(1\pm t)\), where \(t=|\cos(\pi(k-j)/m)|\). The corresponding component of \(v\) is nonzero, so \(Dv=2nv\) is possible only when \(t=0\), meaning opposite vertical phases. Conversely, if every doubleton is antipodal, \(D=2nI\) and \(Q_B=2nI-vv^*\), with eigenvalues \(1\) and \(2n\) in the asserted multiplicities. Therefore \(L_B=1\) holds exactly for antipodal doubletons. Equality \(U_B=2n\) forces \(L_B=1\) by the displayed trace inequality, while equality \(\rho_B=2n\) forces both \(L_B=1\) and \(U_B=2n\) by their universal one-sided bounds. Hence all three equality classifications coincide, and no odd-order basis attains them.

**5. Odd-order determinant-optimal eigenvalues.** In a maximally spaced odd-order doubleton, the two eigenvalues of its full-strip block \(nC^*C\) are \(2n(1\pm s)\). The deleted-row vector has squared projections \(1\pm s\) onto their corresponding eigenlines; this follows by diagonalizing the vertical two-by-two matrix \(CC^*\), whose diagonal entries both equal two. The singleton mode has eigenvalue \(2n\) and deleted-row projection weight one.

Over all \(n-1\) doubletons the eigenspaces at \(2n(1\pm s)\) have dimension \(n-1\), but the rank-one deletion acts nontrivially in only one direction in each. Hence each leaves \(n-2\) unchanged eigenvalues. On the remaining three-dimensional subspace the Gram matrix is unitarily equivalent to
\[
\operatorname{diag}(2n(1-s),2n,2n(1+s))-uu^*,
\]
where \(u=(\sqrt{(n-1)(1-s)},1,\sqrt{(n-1)(1+s)})\). Its secular determinant, with \(y=1-\lambda/(2n)\), is zero exactly when
\[
2ny^3-(2n-1)y^2-2s^2y+s^2=0.
\]
Each of the three positive projection weights is nonzero, so rank-one eigenvalue interlacing is strict at the three distinct diagonal levels. The three new eigenvalues are strictly between \(0\) and \(2n(1-s)\), between \(2n(1-s)\) and \(2n\), and between \(2n\) and \(2n(1+s)\), respectively.

For fixed odd \(m\), \(\|D^{-1}\|=O_m(n^{-1})\) and Sherman--Morrison gives
\[
\|Q_B^{-1}\|=\frac{n-1}{n(1-s^2)}+\frac1{2n}+O_m(n^{-1})
\longrightarrow\frac1{1-s^2}.
\]
For \(n\ge3\), the largest eigenvalue equals the unchanged level \(2n(1+s)\); the asserted asymptotics follow.

**6. The deletion contrast.** On the complete strip, take all \(n\) horizontal characters and an antipodal vertical pair (even \(m\)) or a maximally spaced vertical pair (odd \(m\)). Horizontal orthogonality gives a tensor-product Riesz basis with squared condition number one in the even case and \((1+s)/(1-s)\) in the odd case. Since \(0<s\le1/2\) for odd \(m\ge3\), this latter ratio is at most three. Step 4 proves the claimed deterioration after one deletion.

## Verification
The standalone `verify.py` reconstructs Fourier evaluation matrices directly for cyclic horizontal groups of orders two through five and for the noncyclic Klein four group, for both even and odd vertical moduli. It compares all predicted determinant values, cubic-root spectra, and even-order spectra with numerical eigendecompositions. It additionally exhausts all basis candidates in seven small parameter configurations, checking the fiber criterion, optimal determinant counts, and even/odd Riesz bounds. The exact finite case counts and observed residuals are recorded in `verification_output.txt`. All checks completed successfully; none is used as a substitute for the above all-parameter proof.

## Relationship to prior work
Ferguson, Mayeli, and Sothanaphan (2019) introduce finite-group exponential Riesz tightness quantities and analyze a complete two-layer product in their Examples 6.6 and 6.14. Their Example 4.19 concerns a **full subgroup plus one additional point**, of size \(n+1\), rather than the present full two-layer strip **minus one point**, of size \(2n-1\). Their product theorem does not apply to the punctured set. A subsequent full result on the subgroup-plus-one-point family identifies a cubic and an even-order optimal ratio of \(2n\), but has different row geometry, fiber occupancy, and matrix dimensions. Another full result on two intersecting lines plus an extra point uses an incidence-graph criterion; it does not imply this parallel-fiber classification. For \(m=2\), the ambient group itself is the full strip and the co-singleton Fourier-minor calculation is classical; with \(n=2\), the set is also a subgroup-plus-one-point three-site configuration. These familiar boundary cases are not claimed as new.

The distinct contribution is the complete basis-partner criterion, determinant and optimizer count for **arbitrary finite abelian horizontal groups and any vertical order**, plus the sharp all-basis deletion-instability bound, equality classification, and determinant-optimal odd-order spectrum. No inspected primary full text or closest mathematical record contains this combination or gives a stronger statement implying it. Differently phrased results on punctured product Fourier matrices remain possible.

## Limitations
The least Riesz ratio for odd \(m\) is only bounded strictly below by \(2n\); the determinant-optimal odd-order frequency sets are not proved condition-number optimal. The \(n\to\infty\) asymptotics concern **those determinant-optimal sets**, with \(m\) fixed. For \(m=2\), the result overlaps the elementary one-row/one-column deletion identity for a square Fourier transform. At \(n=2\) the small three-site support also admits a subgroup-plus-point interpretation. No claim is made about noisy reconstruction guarantees beyond the stated finite-dimensional singular values, non-character weights, or more general deletion patterns. Historical priority under alternative formulations remains an originality risk.

## References
1. S. Ferguson, A. Mayeli, and N. Sothanaphan, *Riesz bases of exponentials and multi-tiling in finite abelian groups*, arXiv:1904.04487, first public version 2019-04-09 (especially Sections 3.2, 4.19, 6.6, 6.14, and 6.17); primary MSC 43A70 and 43A40.
2. *Exact Riesz ratio of the subgroup-plus-one-point family*, publicly available mathematical record (2026), `2026/10/4/SCOPE-exact-riesz-ratio-of-the-subgroup-plus-one-point-family--1aeaccf87af3/RESULT.md`.
3. *A unicyclic graph criterion for basis partners of the two-line Riesz family*, publicly available mathematical record (2026), `2026/10/4/SCOPE-a-unicyclic-graph-criterion-for-basis-partners-of-the-two-line-r--6ede33f195c7/RESULT.md`.

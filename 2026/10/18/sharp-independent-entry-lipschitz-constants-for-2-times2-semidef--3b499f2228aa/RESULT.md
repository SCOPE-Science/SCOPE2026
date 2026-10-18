# Sharp independent-entry Lipschitz constants for \(2\times2\) semidefinite projection

## Finding
Let \(\mathcal S_2\) be the real symmetric matrices \(A=\begin{psmallmatrix}a&b\\b&c\end{psmallmatrix}\). On the three independent coordinates define
\[
 \|A\|_{p,\mathrm{ind}}=\|(a,c,b)\|_{\ell_p^3},\qquad p\in\{1,2,\infty\}.
\]
Let \(\Pi(A)\) be the *Frobenius*-nearest positive-semidefinite matrix, equivalently \(\Pi(A)=(A+|A|)/2\) with spectral absolute value. Then the three optimal global same-norm constants are
\[
 \boxed{L_1=L_\infty=\frac32,\qquad L_2=\frac3{2\sqrt2}.}
\]
For \(p=1\), the equality pair \(A=\begin{psmallmatrix}0&1\\1&0\end{psmallmatrix}\), \(B=2A\) attains the bound. The other two sharp constants are approached by derivatives at indefinite matrices tending to a rank-one positive-semidefinite matrix.

## Assumptions and scope
The scalar field is \(\mathbb R\), matrices are symmetric and \(2\times2\), all three coordinate norms count the off-diagonal independent entry exactly **once**, and the *projection itself* minimizes **Frobenius** distance. In particular
\[
\|A\|_{2,\mathrm{ind}}^2=a^2+c^2+b^2,\qquad \|A\|_F^2=a^2+c^2+2b^2,
\]
so the middle formula is not in conflict with Hilbert-space nonexpansivity. The Lipschitz constant is the supremum over every distinct pair of inputs in \(\mathcal S_2\), not merely positive inputs.

## Proof
**1. Orthogonal cone coordinates.** Set \(T=(a+c)/\sqrt2\), \(Z=(a-c)/\sqrt2\), and \(W=\sqrt2 b\). This is a Frobenius isometry, and \(A\succeq0\) exactly when \(T\ge\sqrt{Z^2+W^2}\). For \(r=\sqrt{Z^2+W^2}>0\) and \(-r<T<r\), direct Euclidean projection onto the Lorentz cone gives
\[
 (T,(Z,W))\longmapsto\left(\frac{T+r}2,\frac{T+r}{2r}(Z,W)\right).
\]
In the two other open regions the projection is respectively identity and zero. With \(u=(Z,W)/r\) and \(s=T/r\), the Jacobian in Lorentz coordinates is
\[
 J_s=\frac12\begin{pmatrix}1&u^\mathsf T\\u&(1+s)I_2-suu^\mathsf T\end{pmatrix},\qquad -1<s<1.
\]
In independent-entry coordinates, conjugate \(J_s\) by \(M=2^{-1/2}\begin{psmallmatrix}1&1&0\\1&-1&0\\0&0&2\end{psmallmatrix}\). For a fixed direction \(u\), the resulting Jacobian is affine in \(s\). Consequently every induced operator norm on the mixed region is bounded by the larger of its endpoint limits as \(s\to-1\) and \(s\to1\). These endpoint limits are themselves approached by smooth indefinite matrices.

**2. Rank-one endpoint operators.** For a unit vector \((\alpha,\beta)\in\mathbb R^2\), set
\[
 v=(\alpha^2,\beta^2,\alpha\beta)^\mathsf T,\qquad f=(\alpha^2,\beta^2,2\alpha\beta)^\mathsf T.
\]
Then \(f^\mathsf Tv=1\). The rank-one map \(H\mapsto (\alpha,\beta)^\mathsf TH(\alpha,\beta)\,(\alpha,\beta)(\alpha,\beta)^\mathsf T\) is represented by \(vf^\mathsf T\). As \(s\to-1\), the derivative tends to this rank-one map for the positive eigenvector. As \(s\to1\), it tends to \(I-vf^\mathsf T\) for the *negative* eigenvector. The endpoint eigenvectors differ for a fixed direction \(u\), but both endpoints sweep the entire same unit-vector family as \(u\) varies. It therefore suffices to optimize the norms of \(vf^\mathsf T\) and \(I-vf^\mathsf T\).

Put \(t=\alpha^2\in[0,1]\) and \(q=|\alpha\beta|=\sqrt{t(1-t)}\in[0,1/2]\). The induced \(\ell_1\) and \(\ell_\infty\) norms of the rank-one map are
\[
 \|vf^\mathsf T\|_1=(1+q)\max\{t,1-t,2q\}\le\frac32,
\]
\[
 \|vf^\mathsf T\|_\infty=\max\{t,1-t\}(1+2q)\le\frac{3+2\sqrt2}4<\frac32.
\]
For the latter inequality take \(x=|2t-1|\), \(y=2q\): then \(x^2+y^2=1\), \(x+y\le\sqrt2\), \(xy\le1/2\), and the expression equals \((1+x)(1+y)/2\).

**3. Complementary endpoint operators.** For \(I-vf^\mathsf T\), absolute row sums at diagonal coordinates are \(R(t)=1+t-2t^2+2tq\) and \(R(1-t)\); the off-diagonal row sum is \(1+q-2q^2\le9/8\). Write \(u=2t-1\), \(v_0=2q=\sqrt{1-u^2}\). Since
\[
 (1+u+u^2)^2-(1+u)^2(1-u^2)=u^2(2u^2+4u+3)\ge0,
\]
we have \((1+u)v_0\le1+u+u^2\), and hence \(R(t)=1+(1+u)(v_0-u)/2\le3/2\), with equality when \(t=1/2\). The same holds for \(R(1-t)\). Thus \(\|I-vf^\mathsf T\|_\infty\le3/2\), sharply.

The corresponding absolute column sums at the diagonal coordinates are \(1+t-2t^2+tq\le R(t)\) and its reflection. The off-diagonal column sum is \(1+2q-2q^2\le3/2\), with equality when \(q=1/2\). Therefore \(\|I-vf^\mathsf T\|_1\le3/2\), sharply.

**4. Independent-entry Euclidean norm.** The rank-one operator has Euclidean norm \(\|v\|_2\|f\|_2\). Since \(f^\mathsf Tv=1\), it is a nontrivial oblique projection, whose complementary projection has the **same** Euclidean operator norm. Direct computation yields
\[
 \|vf^\mathsf T\|_2^2=\|I-vf^\mathsf T\|_2^2=(1-q^2)(1+2q^2)=1+q^2-2q^4\le\frac98.
\]
The last polynomial is increasing for \(0\le q^2\le1/4\); equality holds at \(q=1/2\). Thus the sharp endpoint Euclidean operator norm is \(3/(2\sqrt2)\).

**5. Global bounds and sharpness.** The projection is globally Frobenius-nonexpansive and hence locally Lipschitz in every equivalent coordinate norm. For generic line segments, intersections with the switching surfaces of the Lorentz cone are finite: each switching surface lies in the quadratic cone equation, and a noncontained line meets such a quadric at at most two parameters. On every intervening open segment the derivative is respectively zero, identity, or a Jacobian bounded in Steps 2–4. Integrating across these segments proves all three inequalities for generic endpoint pairs. Approximate arbitrary endpoint pairs by generic ones and use the continuity of the projection to extend the same inequalities globally. This avoids assuming differentiability across a segment lying entirely in a switching surface. The \(\ell_1\) equality pair displayed in the finding works because \(\Pi(A)=\frac12\begin{psmallmatrix}1&1\\1&1\end{psmallmatrix}\). For the other norms, let
\[
 (a,c,b)=\left(\frac{1-\varepsilon}{\sqrt2},\frac{1-\varepsilon}{\sqrt2},\frac1{\sqrt2}\right),\quad\varepsilon\downarrow0.
\]
These inputs are indefinite, and their derivatives have \(u=(0,1)\) and \(s=1-\varepsilon\); their \(\ell_\infty\) and \(\ell_2\) induced norms tend to \(3/2\) and \(3/(2\sqrt2)\), respectively. Differentiability gives distinct nearby input pairs with corresponding ratios arbitrarily close to the stated bounds. This proves sharpness without assuming a maximizer for either two-point quotient.

## Verification
Run `python3 verify.py` beside this document. It uses only the Python standard library and checks exact rational identities for oblique projections, compares two independent formulas for the semidefinite projection, finite-differences the interior Jacobian, tests endpoint interpolation, checks sampled induced operator norms and random input pairs, verifies the exact \(\ell_1\) equality pair, and checks approach to both limiting sharp constants. The printed count records executed assertions. Random and finite-grid checks are **not** a proof of the uniform continuum inequalities, which are proved in Steps 2–5.

## Relationship to prior work
Sun and Sun (2002) established Frobenius nonexpansivity, a spectral formula, and strong semismoothness of the positive-semidefinite projection. Shapiro (2002) treated differentiability of symmetric matrix functions, including the spectral positive-part map. The classical equality of the Hilbert-space norms of complementary nontrivial oblique projections is documented by Andreev (2014) and used here only in Step 4. None of those statements gives the present three independent-entry sharp constants without a further norm-specific optimization. The orthogonal identification with a Lorentz cone does **not** preserve the independent-entry norms, so sharp constants stated for standard Lorentz coordinates do not imply the numbers here by a change of notation.

## Limitations
These exact constants concern real symmetric \(2\times2\) matrices and the three specified independent-entry norms. They do not assert sharp constants for larger semidefinite matrices, complex Hermitian inputs, weighted coordinates, arbitrary \(\ell_p\) exponents, or projection *minimizing* independent-entry distance. The elementary differential reduction uses known spectral-projection facts; independent historical novelty beyond the inspected literature is not certified. The off-diagonal entry is intentionally counted once; replacing the norm by full matrix-entry sums changes the question.

## References
1. D. Sun and J. Sun, *Semismooth Matrix-Valued Functions*, Mathematics of Operations Research **27** (2002), 150–169, doi:10.1287/moor.27.1.150.342; author's lawful full-text version: https://www.researchgate.net/publication/220442718_Semismooth_Matrix-Valued_Functions .
2. A. Shapiro, *On Differentiability of Symmetric Matrix Valued Functions*, Optimization Online (2002), https://optimization-online.org/2002/07/499/ .
3. R. Andreev, *A Note on the Norm of Oblique Projections*, Applied Mathematics E-Notes **14** (2014), 43–44, https://www.math.nthu.edu.tw/~amen/2014/131012(final).pdf .

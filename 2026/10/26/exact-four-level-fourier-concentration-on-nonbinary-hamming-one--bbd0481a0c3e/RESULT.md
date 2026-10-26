# Exact four-level Fourier concentration on nonbinary Hamming one-balls

## Finding
Let \(A\) be any finite abelian group of order \(q\ge3\), let \(d\ge3\), and let \(G=A^d\). Write \(B\subset G\) for the radius-one Hamming ball about the identity: the identity together with the elements having exactly one nonidentity coordinate. Let \(\widehat G\) be the character group, and let \(F\subset\widehat G\) be its corresponding radius-one ball. For a function \(f:G\to\mathbb C\) supported on \(B\), use the unitary Fourier transform
\[
\widehat f(\chi)=q^{-d/2}\sum_{x\in G}f(x)\overline{\chi(x)}.
\]
Put
\[
N=1+d(q-1),\qquad T=q^2+1+d(d-2)(q-1)^2,
\qquad \lambda_{\pm}=\frac{T\pm\sqrt{T^2-4q^2}}{2q^d}.
\]
Then the positive concentration operator on \(\mathbb C^B\), with quadratic form \(\sum_{\chi\in F}|\widehat f(\chi)|^2\), has **exactly four distinct eigenvalues**, in strictly increasing order:
\[
\begin{array}{c|c}
\text{eigenvalue}&\text{multiplicity}\\\hline
\lambda_-&1\\
q^{1-d}&d(q-2)\\
q^{2-d}&d-1\\
\lambda_+&1.
\end{array}
\]
All are strictly between zero and one. In particular, the spatially restricted Fourier samples on \(F\) determine every \(f\) supported on \(B\), without a nontrivial kernel; the sharp lower squared singular value is \(\lambda_-\) and the sharp upper value is \(\lambda_+\).

The top eigenspace is one-dimensional and consists of functions whose value is \(\alpha\) at the identity and \(\beta\) at **every** nonidentity element of \(B\), with \(\beta\ne0\) and
\[
\frac\alpha\beta=\frac{d(q-1)(N-q)}{q^d\lambda_+-N}.
\]
The second-largest eigenspace consists of functions vanishing at the identity, constant with value \(c_i\) on each coordinate-axis block of \(q-1\) points, and satisfying \(\sum_{i=1}^d c_i=0\). Hence, if \(\Pi_+\) is the orthogonal projection onto the top eigendirection, then the **sharp stability inequality** is
\[
\sum_{\chi\in F}|\widehat f(\chi)|^2\le
\lambda_+\sum_{x\in B}|f(x)|^2
-\bigl(\lambda_+-q^{2-d}\bigr)\sum_{x\in B}|f(x)-(\Pi_+f)(x)|^2.
\]
The optimal (largest-to-smallest) singular-value condition number equals \(q^d\lambda_+/q\). For fixed \(d\ge3\), \(\lambda_+\sim(d-1)^2q^{2-d}\) as \(q\to\infty\); for fixed \(q\), \(\lambda_+\sim d^2(q-1)^2q^{-d}\) as \(d\to\infty\).

## Assumptions and scope
The Hamming weight counts nonidentity coordinates of an element of \(A^d\) (or nontrivial coordinate characters in its dual). No cyclic or prime-power hypothesis is imposed on \(A\). The ambient Fourier transform is unitary for the **counting** norms \(\|f\|_2^2=\sum_{x\in G}|f(x)|^2\) and \(\|\widehat f\|_2^2=\sum_{\chi\in\widehat G}|\widehat f(\chi)|^2\); all concentration fractions and singular values use this convention. Dimension \(d\ge3\) and group order \(q\ge3\) are essential to the strict four-level statement. The sphere \(\{0\}\cup\{\text{weight one}\}\) is one Hamming **ball**, not a single Hamming shell.

## Proof
**Fourier Gram kernel.** Let \(\chi\) range over the character set \(F\), and let \(x,y\in B\). The compression matrix is
\[
C_{x,y}=q^{-d}\sum_{\chi\in F}\chi(y)\overline{\chi(x)}.
\]
For a coordinate \(i\), character orthogonality in \(A\) gives
\[
\sum_{\gamma\in\widehat A\setminus\{1\}}\gamma(y_i x_i^{-1})=
\begin{cases}q-1,&x_i=y_i,\\-1,&x_i\ne y_i.\end{cases}
\]
Summing over all coordinate blocks therefore yields the **exact universal kernel**
\[
q^d C_{x,y}=N-q\operatorname{dist}_{H}(x,y).
\]
It depends on \(q,d\) but not on the abelian group structure. Put \(L=d(q-1)\), and enumerate \(B\) as the identity followed by the \(d\) axis blocks of \(q-1\) nonidentity points each.

**Complete invariant decomposition.** Work first with the integer matrix \(M=q^dC\). On each axis block, every vector whose coordinates sum to zero is an eigenvector with eigenvalue \(q\); the resulting mutually orthogonal subspaces have dimension \(d(q-2)\). The space of functions vanishing at the identity and constant on each block, with the \(d\) block constants summing to zero, has dimension \(d-1\) and eigenvalue \(q^2\): the diagonal block sum is \(N+(q-2)(N-q)\), while each off-diagonal block sum is \((q-1)(N-2q)\), and their difference is exactly \(q^2\).

The orthogonal complement of these spaces is spanned by the identity basis vector \(e_0\) and the normalized all-ones vector \(L^{-1/2}e_*\) on the nonidentity points. Here \(e_*\) is the \(0/1\) vector that equals one on every nonidentity point. In this orthonormal basis, the remaining matrix is
\[
R=\begin{pmatrix}
N & \sqrt L(N-q)\\
\sqrt L(N-q)& T-N
\end{pmatrix}.
\]
Indeed \(\langle e_*,Me_*\rangle/L=N+(q-2)(N-q)+(d-1)(q-1)(N-2q)=T-N\). The identities
\[
\operatorname{tr}R=T,\qquad
\det R=N(T-N)-L(N-q)^2=q^2
\]
give the roots \(\mu_{\pm}=\tfrac12(T\pm\sqrt{T^2-4q^2})\), whence \(\lambda_{\pm}=q^{-d}\mu_{\pm}\). The eigenspace dimensions add to \(1+d(q-1)=N\), proving completeness. Since \(d\ge3\), one has \(T>q^2+1\). The map \(s\mapsto s+q^2/s\) is strictly increasing for \(s>q\), so the larger root satisfies \(\mu_+>q^2\) and the smaller \(\mu_-=q^2/\mu_+<1<q\). Thus the strict order of all four levels, the simple top, and strict positivity follow.

**No perfect concentration.** Since the Fourier transform is unitary, \(0\le C\le I\). If its largest eigenvalue were one, a nonzero function supported in \(B\) would have Fourier support contained in \(F\). Write its Fourier transform as
\[
q^{d/2}\widehat f(\chi_1,\ldots,\chi_d)=f(0)+\sum_{i=1}^d\phi_i(\chi_i),\qquad
\phi_i(\gamma)=\sum_{a\in A\setminus\{0\}}f(ae_i)\overline{\gamma(a)},
\]
where \(0\) denotes the group identity. For any coordinate \(i\), choose two different other coordinates \(j,k\), fix their characters to be nontrivial, and vary \(\chi_i\). Every such character tuple lies outside \(F\); hence \(\phi_i\) is constant on \(\widehat A\). Its average over \(\widehat A\) is zero by character orthogonality, so the constant vanishes and Fourier inversion gives \(f(ae_i)=0\) for all nonidentity \(a\). This holds for every \(i\), and the remaining Fourier transform of \(f(0)\delta_0\) cannot vanish outside \(F\) unless \(f(0)=0\). Contradiction. Thus \(\lambda_+<1\).

**Extremizers, sharp stability, and asymptotics.** The larger root is simple. Writing its eigenvector as \(\alpha e_0+\beta e_*\), the equation at coordinate zero is \((\mu_+-N)\alpha=L(N-q)\beta\); \(N-q=(d-1)(q-1)>0\) gives the displayed unique ratio. Its next eigenvalue is \(q^{2-d}\), with the explicitly described block-constant contrast eigenspace. Decompose any \(f\) orthogonally into top, second, and remaining eigenspaces and apply the spectral theorem to obtain the sharp stability inequality. The bottom eigenvalue is simple, and \(\mu_+\mu_-=q^2\), so the singular-value condition number is \(\sqrt{\mu_+/\mu_-}=\mu_+/q\), proving the claimed formula. Finally \(T=(d-1)^2q^2+O_d(q)\) when \(q\to\infty\) at fixed \(d\), and \(T=(q-1)^2d^2+O_q(d)\) when \(d\to\infty\) at fixed \(q\). Since \(\mu_+=T+O(q^2/T)\), both asymptotic formulas follow.

## Verification
The accompanying standard scientific-Python checker `verify.py` constructs exact integer Gram matrices and verifies the invariant contrasts, trace, determinant, and second trace-moment identity on all \(49\) pairs \(3\le q,d\le9\). It independently reconstructs the Fourier Gram matrix numerically on six cyclic-group cases, including \(q=6\), and a seventh test on the noncyclic alphabet \(A=(\mathbb Z/2\mathbb Z)^2\). All \(1{,}875\) counted test units passed. The reported finite tests are independent consistency checks, **not** proofs for infinitely many \(q,d\); the orthogonality and decomposition arguments above establish the theorem for all finite abelian alphabets.

## Relationship to prior work
Hogan and Lakey (2018, arXiv:1812.08905v1) analyze spatio-spectral limiting for **Boolean** hypercubes and supply the principal Hamming-ball operator motivation. In particular, the published exact first-Walsh-band Hamming-ball spectral result concerns \(q=2\), where the within-axis contrast eigenvalue \(q^{1-d}\) in this theorem has zero multiplicity. It therefore does not give the four-sector spectrum for nonbinary alphabets. A published first-band \(q\)-ary Hamming-**shell** spectrum concerns restriction to vectors of weight exactly \(k\); at \(k=1\) it has a forced kernel. Adding the center to make a radius-one **ball** changes the radial block, removes that kernel, and gives the present strictly positive new smallest eigenvalue and sharp stability. The split-quadric concentration result contains the special two-coordinate cross \(d=2\), where perfect localization occurs and the present strict four-level classification is inapplicable. Feng, Hollmann, and Xiang (2018) establish general Fourier uncertainty/abelian-code support bounds rather than the present exact two-sided singular spectrum. Standard character orthogonality and block diagonalization are used as tools and are not asserted to be new; the claimed result is their full all-parameter concentration classification and exact optimizer/gap.

## Limitations
The statement is restricted to radius-one Hamming balls and the matching first character band, not larger radii, arbitrary spatial subsets, nonlinear reconstruction, phase retrieval, or higher-frequency bands. The optimal singular values depend on the ambient unitary Fourier normalization. These exact formulas may be implicitly obtainable by older association-scheme eigenmatrices; originality is best knowledge rather than an independently certified priority assertion. Independent scientific validation has not been performed.

## References
1. Jeffrey A. Hogan and Joseph D. Lakey, *Spatio-spectral limiting on hypercubes: eigenspaces*, arXiv:1812.08905v1, first publicly posted 2018-12-21. https://arxiv.org/html/1812.08905v1
2. Tao Feng, H. D. L. Hollmann, and Qing Xiang, *The shift bound for abelian codes and generalizations of the Donoho-Stark uncertainty principle*, arXiv:1804.00367v1, first publicly posted 2018-04-02. https://arxiv.org/abs/1804.00367
3. Mikhail Tsitsvero, Sergio Barbarossa, and Paolo Di Lorenzo, *Signals on Graphs: Uncertainty Principle and Sampling*, arXiv:1507.08822v1, first publicly posted 2015-07-31. https://arxiv.org/abs/1507.08822
4. *Exact first-Walsh-band concentration spectra on Boolean Hamming balls*, full result record, 2026. https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exact-first-walsh-band-concentration-spectra-on-boolean-hamming--a2f5ddac5a0f
5. *Exact q-ary Hamming-shell Fourier concentration and the arithmetic tightness criterion*, full result record, 2026. https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exact-q-ary-hamming-shell-fourier-concentration-and-the-arithmet--89a15e26e594
6. *Exact first-band Fourier concentration on split quadratic cones over odd finite fields*, full result record, 2026. https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exact-first-band-fourier-concentration-on-split-quadratic-cones--dbf8fa8aec40

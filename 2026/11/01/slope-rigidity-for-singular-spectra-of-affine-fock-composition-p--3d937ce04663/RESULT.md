# Slope rigidity for singular spectra of affine Fock composition products

## Finding

Let \(\mathcal F^2\) be the complex one-variable Gaussian Fock Hilbert space with normalized measure \(e^{-|z|^2}\,dA(z)/\pi\). For \(a,b,c,d\in\mathbb C\) with \(|a|<1\) and \(|c|<1\), let \(\varphi(z)=az+b\), \(\psi(z)=cz+d\), and \(C_\varphi f=f\circ\varphi\), \(C_\psi f=f\circ\psi\). Both composition operators are bounded. Consider the two cross-adjoint orientations
\[
P=C_\varphi C_\psi^*,\qquad Q=C_\psi^*C_\varphi.
\]
Put \(\rho=|ac|\), \(D=1-\rho^2>0\), and
\[
A=|a|^2|d|^2+|c|^2|b|^2+2\operatorname{Re}(b\overline d),
\qquad
B=|b|^2+|d|^2+2\operatorname{Re}(c\overline a b\overline d).
\]
Then their full decreasing singular-value sequences, indexed from \(n=0\), are
\[
\boxed{s_n(P)=\exp\!\left(\frac{A}{2D}\right)\rho^n,\qquad
s_n(Q)=\exp\!\left(\frac{B}{2D}\right)\rho^n\quad(n\ge0).}
\]
When \(\rho=0\), the convention is \(\rho^0=1\) and \(\rho^n=0\) for \(n\ge1\): each product then has rank one. Consequently both products belong to every Schatten class \(\mathcal S_p\), \(0<p<\infty\), and
\[
\|P\|_{\mathcal S_p}=\frac{\exp(A/(2D))}{(1-\rho^p)^{1/p}},\qquad
\|Q\|_{\mathcal S_p}=\frac{\exp(B/(2D))}{(1-\rho^p)^{1/p}}.
\]
At \(p=\infty\) these become the respective operator norms \(\exp(A/(2D))\) and \(\exp(B/(2D))\). In particular, the ratio of the singular values, of any positive Schatten quasi-norms, and of operator norms is the same scalar:
\[
\boxed{\frac{s_n(Q)}{s_n(P)}=\frac{\|Q\|_{\mathcal S_p}}{\|P\|_{\mathcal S_p}}=
\exp\!\left(\frac{\Delta}{2D}\right),\qquad \Delta=B-A,}
\]
where the singular-value ratio is understood for nonzero entries if \(\rho=0\).

There is a sharp rigidity dichotomy when the slopes \(a,c\) are fixed and translations \(b,d\) vary over \(\mathbb C\):

1. The inequality \(s_n(Q)\ge s_n(P)\) for every \(b,d\) and every \(n\ge0\) holds **if and only if \(a=c\)**. If \(a=c\), then \(\Delta=(1-|a|^2)|b-d|^2\), and equality throughout holds exactly when \(b=d\).
2. If \(a\ne c\), each orientation dominates the other for suitable translations; indeed the scale ratio \(\|Q\|_{\mathcal S_p}/\|P\|_{\mathcal S_p}\) ranges over every positive real number as \(b,d\) vary. Thus neither orientation has a translation-uniform norm bound by a fixed constant times the other. This statement holds simultaneously for every \(0<p\le\infty\).

## Assumptions and scope

The Fock inner product is linear in the first argument and the standard orthonormal basis is \(e_n(z)=z^n/\sqrt{n!}\), \(n\ge0\). The reproducing kernel is \(K_w(z)=e^{z\overline w}\). The two strict slope bounds ensure the affine composition operators are bounded for every translation. All operator products are bounded everywhere-defined Hilbert-space operators. The result concerns **singular values**, not eigenvalues of the generally nonnormal products, and complex Hilbert-space Schatten quasi-norms, not the Schatten class of a nonlinear map.

## Proof

**Step 1 (kernels identify both products).** Since \(C_\eta^*K_w=K_{\eta(w)}\) for a bounded composition operator \(C_\eta\), direct substitution into the reproducing kernels gives
\[
(PK_w)(z)=e^{(az+b)(\overline c\,\overline w+\overline d)},
\qquad
(QK_w)(z)=e^{\overline d z+(a\overline c\,z+b)\overline w}.
\]
The kernel spans are dense, hence the exact weighted-composition identities are
\[
(Pf)(z)=e^{b\overline d+a\overline d z}\,f(a\overline c\,z+b\overline c),
\qquad
(Qf)(z)=e^{\overline d z}\,f(a\overline c\,z+b).
\]
The identities may also be checked directly on monomials.

**Step 2 (an explicit unitary normal form).** Let \(v,w,\beta,\delta\in\mathbb C\) satisfy \(|v|<1\), and define
\[
(Tf)(z)=e^{\delta+\beta z}f(vz+w).
\]
Define Weyl displacement operators and diagonal dilations by
\[
(U_t f)(z)=e^{\overline t z-|t|^2/2}f(z-t),\qquad
(D_vf)(z)=f(vz).
\]
Each \(U_t\) is unitary, as follows by translation in the Gaussian integral, while \(D_ve_n=v^ne_n\). Set
\[
p=\frac{\overline\beta+\overline v w}{1-|v|^2},
\qquad
q=-\frac{w+v\overline\beta}{1-|v|^2}.
\]
Then \(\overline p+v\overline q=\beta\) and \(-vp-q=w\). Substituting into the definitions gives
\[
U_pD_vU_q=e^E e^{\beta z}C_{vz+w},
\qquad
E=-\frac{|p|^2+|q|^2}{2}-v\overline q p.
\]
Therefore \(T=e^{\delta-E}U_pD_vU_q\). Since multiplication by unitaries does not change singular values, the full sequence is \(s_n(T)=\kappa|v|^n\), with
\[
\begin{aligned}
\log\kappa&=\operatorname{Re}(\delta-E)\\
&=\operatorname{Re}\delta+\frac{|p|^2+|q|^2+2\operatorname{Re}(v\overline q p)}2\\
&=\operatorname{Re}\delta+\frac{1}{2}\left(|\beta|^2+(1-|v|^2)|q|^2\right)\\
&=\operatorname{Re}\delta+\frac{|\beta|^2+|w|^2+2\operatorname{Re}(w\overline v\beta)}{2(1-|v|^2)}.
\end{aligned}
\]
Here the penultimate equality uses \(p+\overline vq=\overline\beta\). This also proves boundedness and compactness of \(T\), including the rank-one case \(v=0\), without relying on an unproved normal-form lemma.

**Step 3 (substitution and simplification).** For \(P\), use \(v=a\overline c\), \(w=b\overline c\), \(\beta=a\overline d\), \(\delta=b\overline d\) in Step 2. Its logarithmic scale is initially
\[
\operatorname{Re}(b\overline d)+\frac{|a|^2|d|^2+|c|^2|b|^2+2|ac|^2\operatorname{Re}(b\overline d)}{2D},
\]
which equals \(A/(2D)\). For \(Q\), use \(v=a\overline c\), \(w=b\), \(\beta=\overline d\), \(\delta=0\) to obtain \(B/(2D)\). Geometric summation yields the displayed \(\mathcal S_p\) formulas for every finite positive \(p\); the largest singular value gives \(p=\infty\).

**Step 4 (rigid orientation comparison).** Direct subtraction yields the real Hermitian quadratic form
\[
\Delta=(1-|c|^2)|b|^2+(1-|a|^2)|d|^2
+2\operatorname{Re}((c\overline a-1)b\overline d).
\]
Its Hermitian \(2\times2\) matrix has strictly positive diagonal entries and determinant
\[
(1-|c|^2)(1-|a|^2)-|1-c\overline a|^2=-|a-c|^2.
\]
If \(a=c\), the form equals \((1-|a|^2)|b-d|^2\) and vanishes exactly at \(b=d\). If \(a\ne c\), the determinant is negative, so the form is indefinite. Along a positive or negative eigenvector, real scaling of the translation pair produces respectively \(\Delta\to+\infty\) or \(\Delta\to-\infty\). Continuity and homogeneity imply that \(\exp(\Delta/(2D))\) takes every value in \((0,\infty)\), proving the second statement. This concludes the proof.

## Verification

The standalone file `check_singular_orientation.py` implements the exact coefficient matrix of each affine composition operator on monomial truncations and numerically compares both cross-adjoint orientations with the first three terms of the claimed singular sequences. It also checks the two algebraic expressions for \(\Delta\), including randomly selected complex coefficients and the exact same-slope identity. Executed with Python 3 and NumPy, it reported 143 passed finite checks. This is supplementary evidence; the proof above, not the truncation, supplies the infinite-dimensional statements.

Concrete sign-reversal witnesses are available already at slopes \(a=1/2\), \(c=-1/2\): with \(b=d=t\in\mathbb R\) the difference \(\Delta=-t^2\), whereas with \(b=-d=t\) it is \(\Delta=4t^2\). Since \(D=15/16\), the relative scale tends respectively to zero and to infinity as \(|t|\to\infty\).

## Relationship to prior work

Tian (2026, arXiv:2610.29786v1) studies compactness, invertibility, and isometric properties of weighted-composition/adjoint products on Gaussian Fock space, and explicitly states equivalent compactness criteria for both orientations of bounded unweighted affine compositions. Its stated theorems do not provide the paired exact singular-value sequences or the slope-rigidity comparison. Barik, Sen, and Paul (2026, arXiv:2607.17170v1) characterize boundedness, compactness, and Hilbert–Schmidt membership of weighted composition operators on power-weighted Fock spaces; the specialization to the Gaussian space motivates testing a stronger, quantitative invariant, but their principal claims do not give this orientation order. Leng and Zhao (2026, arXiv:2610.15472v1) study Schatten membership of products on Hardy and Bergman spaces, not this Gaussian Fock singular-value comparison. The Weyl displacement formula and the monomial diagonalization of a centered Fock dilation are elementary known tools, used here with an explicit composition-product calculation. The claimed addition is the **paired orientation spectrum and if-and-only-if universal slope-rigidity law**, not the definition of the Fock space, Weyl unitary, or known compactness criterion.

## Limitations

No claim is made for nonlinear composition symbols, arbitrary exponential quadratic weights, higher-dimensional Fock spaces, boundary slopes with unconstrained translations, or the spectral eigenvalues of nonnormal products. There is no claim that the geometric single-operator normal form is independently new. The novelty assessment is limited by the possibility of a previously published operator-product or Weyl-calculus identity which implies the paired comparison. The accompanying finite-dimensional tests are not an independent infinite-dimensional validation. No independent scientific audit has been performed.

## References

1. Xianchi Tian, *Weighted composition operators on the Fock space*, arXiv:2610.29786v1, first submitted 2026-10-21. https://arxiv.org/abs/2610.29786
2. Somdatta Barik, Anirban Sen, and Kallol Paul, *Weighted composition operators on weighted Fock spaces*, arXiv:2607.17170v1, 2026-07-19. https://arxiv.org/abs/2607.17170
3. Qianrui Leng and Xianfeng Zhao, *Schatten class membership of products of composition operators and their adjoints*, arXiv:2610.15472v1, 2026-10-11. https://arxiv.org/abs/2610.15472
4. Trieu Le, *Normal and isometric weighted composition operators on the Fock space*, Bulletin of the London Mathematical Society 46 (2014), 847–856, DOI 10.1112/blms/bdu046.

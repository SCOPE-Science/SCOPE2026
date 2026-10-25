# Sharp finite-direction tomography of centered ellipsoids even with known volume

## Finding
For every integer \(n\ge2\), put \(m=n(n+1)/2\). The sharp universal angular sampling threshold for uniquely reconstructing a **centered ellipsoid** from parallel-hyperplane section-volume profiles is \(m\), even when the total ellipsoid volume is supplied and every offset in each sampled direction can be measured. An explicit set of \(m\) normal directions attains it; remarkably, central sections alone suffice without a separate volume measurement.

More precisely, for unit vectors \(u_1,\ldots,u_N\), let \(\mathcal A_Q(u,s)\) be the \((n-1)\)-volume of the section of \(E_Q\) by \(\{x:\langle u,x\rangle=s\}\). Then:

1. The \(m\) normals \(e_i\) and \((e_i+e_j)/\sqrt2\), with \(1\le i<j\le n\), make the map \(Q\mapsto(\mathcal A_Q(u,0))_u\) injective on the positive definite symmetric matrices, and there is an explicit inversion formula not using the ambient volume.
2. For every prescribed collection of \(N<m\) normal directions, there exist distinct positive definite matrices \(Q_+\ne Q_-\) having \(\det Q_+=\det Q_-\) and satisfying \(\mathcal A_{Q_+}(u_i,s)=\mathcal A_{Q_-}(u_i,s)\) for every \(s\in\mathbb R\) and all sampled \(i\).
3. If a height \(t>0\) and the total volume are known, the same \(m\) directions and their *single-height* sections at \(s=t\) suffice within the class \(Q\succ nt^2 I\). The ambiguity in part 2 persists for every smaller number of normal directions even inside this class.

## Assumptions and scope
Work in Euclidean \(\mathbb R^n\), with \(n\ge2\). Write \(Q\in\operatorname{Sym}_n^{++}\) for a real symmetric positive definite matrix and define the centered ellipsoid
\[
E_Q=\{x\in\mathbb R^n:x^{\mathsf T}Q^{-1}x\le1\}.
\]
The orientation of all sampled unit normals is known and fixed. Each line \(\mathbb Ru\) is an unoriented direction; the offset \(s\) is signed relative to a selected orientation, but the centered profiles are even. Let \(\kappa_j\) denote the volume of the unit ball in dimension \(j\). Data are exact real values, not noisy estimates. There is no claim about reconstruction among arbitrary nonellipsoidal convex bodies, or about noncentered ellipsoids.

The section identity valid for every unit \(u\) and real \(s\) is
\[
\mathcal A_Q(u,s)=\kappa_{n-1}
\frac{\sqrt{\det Q}}{\sqrt{u^{\mathsf T}Qu}}
\left(1-\frac{s^2}{u^{\mathsf T}Qu}\right)_+^{(n-1)/2}.
\]
The positive-part convention gives zero beyond the supporting planes.

## Proof
**Section identity.** Express \(E_Q=Q^{1/2}B_2^n\). Under this map, the Euclidean normal \(u\) is transformed to \(Q^{1/2}u\). Applying the coarea transformation on its level sets multiplies their \((n-1)\)-volumes by \(\sqrt{\det Q}/\|Q^{1/2}u\|\). A unit-ball section at normalized distance \(s/\|Q^{1/2}u\|\) has volume \(\kappa_{n-1}(1-s^2/(u^{\mathsf T}Qu))_+^{(n-1)/2}\), giving the identity.

**Sufficiency without volume.** Put \(D=\det Q>0\) and \(H=Q/D\). At height zero, the identity yields
\[
u^{\mathsf T}Hu=\frac{\kappa_{n-1}^2}{\mathcal A_Q(u,0)^2}.
\]
For each coordinate normal \(e_i\), this gives \(H_{ii}\). For each \(u_{ij}=(e_i+e_j)/\sqrt2\), polarization gives
\[
H_{ij}=u_{ij}^{\mathsf T}Hu_{ij}-\frac{H_{ii}+H_{jj}}2.
\]
These exactly \(m\) observations reconstruct \(H\). Since \(\det H=D^{1-n}\), we obtain the unique scaling
\[
D=(\det H)^{-1/(n-1)},\qquad Q=(\det H)^{-1/(n-1)}H.
\]
Thus \(m\) central section volumes alone determine the ellipsoid.

**Sharp lower bound even with complete profiles and volume.** Fix arbitrary \(N<m\) sampled normals. The linear map \(\operatorname{Sym}_n\to\mathbb R^N\) sending \(T\) to \((u_i^{\mathsf T}Tu_i)_i\) has a nonzero kernel. It contains an *indefinite* matrix \(T\): if the normals span \(\mathbb R^n\), a nonzero positive or negative semidefinite kernel element would vanish on a spanning set and hence be zero, so any nonzero kernel element is indefinite. If the normals fail to span, choose \(v\ne0\) perpendicular to all of them and \(w\) linearly independent of \(v\), and take \(T=vw^{\mathsf T}+wv^{\mathsf T}\). It lies in the kernel and has one positive and one negative eigenvalue.

Because \(T\) is indefinite, the positive definiteness interval of \(Q(z)=I+zT\) is a bounded open interval \((\alpha,\beta)\) with \(\alpha<0<\beta\). Its determinant is continuous, equals \(1\) at \(z=0\), and tends to zero at both ends. By the intermediate value theorem, there exist \(z_-\in(\alpha,0)\) and \(z_+\in(0,\beta)\) satisfying \(\det Q(z_-)=\det Q(z_+)=1/2\). The matrices are distinct, are positive definite, and obey \(u_i^{\mathsf T}Q(z_-)u_i=u_i^{\mathsf T}Q(z_+)u_i=1\). By the section identity, their full signed-offset profiles agree for all sampled normals, and equal determinants give them exactly equal \(n\)-volumes \(\kappa_n/\sqrt2\). This proves the sharp lower bound. Scaling both matrices by the same sufficiently large positive scalar preserves equal-volume/equal-section-profile comparisons at all sampled directions and gives arbitrarily large minimum eigenvalue.

**One noncentral offset on a thick class.** Let \(t>0\), and suppose \(Q\succ nt^2I\), with known \(D=\det Q\) from its volume \(\kappa_n\sqrt D\). For \(q=u^{\mathsf T}Qu>nt^2\),
\[
\mathcal A_Q(u,t)=\kappa_{n-1}\sqrt D\,F_t(q),\quad
F_t(q)=(q-t^2)^{(n-1)/2}q^{-n/2}.
\]
Direct differentiation gives
\[
\frac{F_t'(q)}{F_t(q)}=\frac{nt^2-q}{2q(q-t^2)}<0.
\]
Thus each single-height measurement in the chosen \(m\) directions determines its \(q\) uniquely. Polarization reconstructs \(Q\) as above. Scaling the ambiguity pair from the previous paragraph sufficiently far ensures it lies in this same thick class, showing that the count remains necessary.

## Verification
A standalone exact-arithmetic script `verify.py` checks the entire displayed central inversion in a rational three-dimensional test case and constructs two explicit distinct planar matrices with the same determinant and the same full profiles in two normal directions. The script also confirms the strict derivative sign algebraically. The unrestricted-dimensional theorem follows from the arguments above; these finite tests are consistency checks only.

## Relationship to prior work
Fish, Ryabogin, Sun and Yaskin (2026) investigate determination by parallel section functions, including the classical all-direction Minkowski–Funk uniqueness theorem for central sections and the Barker–Larman noncentral section problem. Their treatment varies the offsets and/or uses the continuum of normal directions; it does not state the exact finite-angle cutoff in the restricted ellipsoid class given here. Published global Barker–Larman rigidity for ellipsoids considers every tangent normal direction, so its injectivity statement alone does not give an optimal finite-direction design or the volume-preserving ambiguity construction. The present proof uses the elementary quadratic-form structure of ellipsoids but makes a sharp angular-versus-offset distinction.

## Limitations
The result is an exact, noiseless geometric design theorem for centered ellipsoids only. It does not supply numerical condition-number guarantees, an optimal design for noisy data, or uniqueness for arbitrary convex bodies. The lower bound asserts a pair of equal-volume nonidentifiable ellipsoids for *each* choice of fewer than \(m\) normals; it does not assert nonuniqueness at every fixed prescribed volume and thickness simultaneously. The result is not an independent literature certification; similar finite-dimensional observations may exist under inverse-matrix or quadratic-measurement terminology.

## References
1. A. Fish, D. Ryabogin, W. R. Sun, V. Yaskin, *On determination of convex bodies by their section functions*, arXiv:2610.10229v1, first posted 2026-10-07, https://arxiv.org/html/2610.10229v1.
2. R. J. Gardner, *Geometric Tomography*, 2nd ed., Cambridge University Press, 2006, Chapter 7 (sections and section functions), https://doi.org/10.1017/CBO9781107341029.010.
3. *Global Barker–Larman rigidity for ellipsoids*, published mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-global-barker-larman-rigidity-for-ellipsoids--75abc96cf1f6 (comparison limited to the indexed claim summary).

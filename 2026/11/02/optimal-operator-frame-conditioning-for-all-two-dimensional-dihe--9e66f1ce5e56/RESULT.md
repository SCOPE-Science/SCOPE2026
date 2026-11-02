# Optimal operator-frame conditioning for all two-dimensional dihedral irreducibles

## Finding
Fix an integer \(n\geq3\) and \(1\leq k<n/2\). Put \(\zeta=e^{2\pi i/n}\), and let the standard two-dimensional irreducible representation of the dihedral group of order \(2n\) be
\[
\pi(r)=\operatorname{diag}(\zeta^k,\zeta^{-k}),\qquad
\pi(s)=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]
For a unit vector \(v=(a,b)^T\in\mathbb C^2\), measure a Hermitian matrix \(X\) by the full, group-element-labelled family of scalar products \(\mathcal A_v(X)=(\operatorname{tr}(XP_g))_{g\in D_{2n}}\), where \(P_g=\pi(g)vv^*\pi(g)^*\). Equip Hermitian matrices with the real Hilbert–Schmidt inner product and the data with ordinary Euclidean norm; set \(\mathcal S_v=\mathcal A_v^*\mathcal A_v\).

Write \(d=|a|^2-|b|^2\), \(c=a\overline b\), and \(\ell=\operatorname{ord}(\zeta^{2k})=n/\gcd(n,2k)\). Then the **complete spectrum**, including multiplicities, is
\[
\operatorname{spec}(\mathcal S_v)=
\begin{cases}
\{n,\ nd^2,\ 2n|c|^2,\ 2n|c|^2\},&\ell>2,\\
\{n,\ nd^2,\ 4n(\operatorname{Re}c)^2,\ 4n(\operatorname{Im}c)^2\},&\ell=2.
\end{cases}
\]
In particular, the exact optimal lower squared singular value over **all unit orbit generators** is
\[
\boxed{\max_{\|v\|=1}\lambda_{\min}(\mathcal S_v)=\frac n3.}
\]
The complete equality locus is:

* if \(\ell>2\), precisely \(d^2=1/3\), with no restriction on the relative phase of nonzero \(a,b\);
* if \(\ell=2\), precisely \(d^2=1/3\) and \((\operatorname{Re}c)^2=(\operatorname{Im}c)^2\), equivalently \(\arg c\equiv\pi/4\pmod{\pi/2}\).

The second case arises exactly when \(4\mid n\) and \(k=n/4\). Every optimal orbit has spectrum \(\{n,n/3,n/3,n/3\}\) and constitutes an equally weighted complex projective \(2\)-design, allowing repeated projectors in the group-element-labelled family. The sharp minimum condition number of the linear measurement operator is \(\sqrt3\). A real-valued generator can attain the optimum when \(\ell>2\), whereas no real-valued generator gives matrix recovery in the exceptional \(\ell=2\) representation.

## Assumptions and scope
The representation is the displayed ordinary unitary representation, not a projective representation with an additional multiplier. The domain of \(\mathcal A_v\) is the **four-real-dimensional space** of all \(2\)-by-\(2\) Hermitian matrices, not only rank-one signal matrices; the rank-one measurements include all \(2n\) group elements with repetitions retained, and \(\|v\|=1\) is essential for the numerical normalization. The operator-frame spectrum is for the unweighted measurement map, without division by the number of orbit elements. Equality of measurements for two unknown vectors follows from matrix recovery whenever the smallest eigenvalue is positive, but quantitative phase-retrieval stability in the original signal metric is not asserted.

## Proof
Let \(\sigma_x,\sigma_y,\sigma_z\) be the Pauli matrices, with \(\sigma_y=\begin{psmallmatrix}0&-i\\i&0\end{psmallmatrix}\), and choose the real orthonormal basis \(I/\sqrt2,\sigma_x/\sqrt2,\sigma_y/\sqrt2,\sigma_z/\sqrt2\) of Hermitian matrices. Every rank-one projector in the orbit has coordinates \((1,u_x,u_y,u_z)/\sqrt2\), where \(u\in\mathbb R^3\) is a Bloch unit vector. With \(q=\zeta^{2k}\) and \(0\le j<n\), the projectors of \(r^jv\) have
\[
u_j=(2\operatorname{Re}(cq^j),-2\operatorname{Im}(cq^j),d),
\]
whereas the projectors of \(sr^jv\) have \((u_{j,x},-u_{j,y},-d)\). Because \(\ell\ge2\), the geometric sum \(\sum_{j=0}^{n-1}q^j=0\). It follows that the Bloch-vector mean vanishes, and every off-diagonal entry of the \(3\)-by-\(3\) Bloch second-moment matrix vanishes (the potentially noncancelling \(y,z\) term vanishes upon summation over \(j\)). Hence the Hilbert–Schmidt frame operator is diagonal in the displayed Pauli basis, with its identity eigenvalue \(n\).

If \(\ell>2\), the further geometric sum \(\sum_jq^{2j}=0\) gives equal \(x\)- and \(y\)-direction variances, and direct summation gives respectively \(2n|c|^2\), \(2n|c|^2\) and \(nd^2\) as the other three eigenvalues. If \(\ell=2\), then \(q=-1\), so the Bloch vectors have \(x\)- and \(y\)-coordinates alternating between two opposite values; their variances become \(4n(\operatorname{Re}c)^2\) and \(4n(\operatorname{Im}c)^2\). This proves both exact spectral formulas for every parameter, including degenerate generators.

Since \(\|v\|=1\), \(4|c|^2=1-d^2\), and in either branch the three traceless eigenvalues sum to \(n\). They are nonnegative. Their minimum is therefore at most \(n/3\), while the identity eigenvalue is \(n\). Equality requires all three traceless eigenvalues to equal \(n/3\). In the first branch this is equivalent to \(d^2=1/3\); in the second it is equivalent to \(d^2=1/3\) and \((\operatorname{Re}c)^2=(\operatorname{Im}c)^2\). These conditions are attainable by \(|a|^2=(1+1/\sqrt3)/2\) and \(|b|^2=(1-1/\sqrt3)/2\), with \(a,b\) real in the first branch, and relative argument \(\pi/4\) in the second. The order-two condition \(\zeta^{2k}=-1\), combined with \(0<2k<n\), is equivalent to \(4\mid n\) and \(k=n/4\).

Finally, at equality the operator-frame action is \(\mathcal S_v(X)=\tfrac n3(X+\operatorname{tr}(X)I)\), on all Hermitian \(X\) and hence by complex linearity on all matrices. Equivalently,
\[
\frac1{2n}\sum_{g\in D_{2n}}P_g\otimes P_g
=\frac{I\otimes I+\operatorname{SWAP}}6,
\]
which is exactly the complex projective \(2\)-design moment identity in dimension two. The identity eigenvalue \(n\) forces the optimal analysis-operator condition number to be \(\sqrt{n/(n/3)}=\sqrt3\). For the exceptional branch a real generator has \(\operatorname{Im}c=0\), so one eigenvalue vanishes.

## Verification
The standalone pure-Python program `verify.py` forms every group-element-labelled rank-one projector directly, constructs the real \(4\)-by-\(4\) Hilbert–Schmidt measurement matrix, and computes its eigenvalues by symmetric Jacobi rotations. It compares these independent constructions with the closed forms for every irreducible pair \((n,k)\) with \(3\le n\le29\), at three distinct generators, and verifies the optimal spectrum for each such pair. The replay reports `VERIFY_OK spectra=588 optimal_orbits=196 n_range=3..29`. Its floating-point tolerance is \(2\times10^{-8}\); the unlimited-\(n\) conclusion is proved by the exact geometric-sum argument above, not by extrapolating the finite replay.

## Relationship to prior work
Oussa and Sheehan (2017) study the Haar/full-spark property for a different, generally higher-dimensional induced dihedral representation. Führ and Oussa (2022) give group-orbit phase-retrieval theorems for nilpotent representations, mainly finite \(p\)-groups in the finite setting. A published result entitled *Exact maximal-spanning vectors for two-dimensional dihedral irreducibles* gives the **qualitative** maximal-operator-span criteria for precisely this representation, including the exceptional order-two branch. Those criteria are prior work, not claimed anew here. They do **not** state the quantitative spectrum, the sharp \(n/3\) conditioning law, or the explicit full locus of dihedral projective \(2\)-design generators.

Scott (2006) proves the **general** equivalence between tight rank-one informationally complete measurements and weighted complex projective \(2\)-designs, including their general optimality for linear tomography. That universal principle is also prior work. The specific contribution here is an exact spectral resolution of every unit dihedral fiducial, including the exceptional representation's relative-phase restriction, and thereby the complete realization of the optimum within this entire representation family. A later paper by Cheng (2025) on the phase retrievability of finite-group irreducibles is a relevant possible antecedent; its complete text was not verifiably inspected. Its bibliographic metadata alone cannot exclude implicit coverage, although the present claim is about quantitative conditioning rather than qualitative existence.

## Limitations
This is not a classification of optimal orbits in arbitrary unitary representations, or of global optimum designs beyond the dihedral family. It does not provide a nonlinear noisy-signal stability theorem. Group elements are counted with multiplicity even if their projectors coincide; deleting repetitions changes the normalization. The exact formulas follow without computation, but the numerical checker is finite and uses floating-point arithmetic. Literature priority remains subject to full comparison with inaccessible specialized sources, especially the Cheng article,.

## References
1. V. Oussa and B. Sheehan, *Dihedral Group Frames with the Haar Property*, arXiv:1705.00085v1, first public 2017-04-28, https://arxiv.org/abs/1705.00085.
2. H. Führ and V. Oussa, *Phase Retrieval for Nilpotent Groups*, arXiv:2201.08654v1, first public 2022-01-21, https://arxiv.org/abs/2201.08654.
3. A. J. Scott, *Tight informationally complete quantum measurements*, arXiv:quant-ph/0604049, first public 2006-04-07, https://arxiv.org/abs/quant-ph/0604049.
4. *Exact maximal-spanning vectors for two-dimensional dihedral irreducibles*, public mathematical research record, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-exact-maximal-spanning-vectors-for-two-dimensional-dihedral-irre--254536e7d971.
5. C. Cheng, *On the phase retrievability of irreducible representations of finite groups*, Linear Algebra and its Applications 714 (2025), 64–95, DOI 10.1016/j.laa.2025.03.011.

# Exact quantumness–negativity identity for zero-dipole spin-one states

## Finding

For any spin-one density operator \(\rho\) with \(\operatorname{Tr}(\rho J_a)=0\) for all \(a\in\{x,y,z\}\), put
\[
T_{ab}=\operatorname{Tr}\bigl(\rho(J_aJ_b+J_bJ_a-\delta_{ab}I_3)\bigr),\qquad
\lambda=\lambda_{\min}(T).
\]
The exact Hilbert–Schmidt quantumness relative to all spin-one coherent states is
\[
\boxed{Q(\rho)=\sqrt{\frac38}\max(0,-\lambda)
=\sqrt{\frac32}\,\mathcal N(\rho).}
\]
Here \(\mathcal N(\rho)\) is negativity after identifying spin one with the symmetric subspace of two qubits. For \(\lambda<0\), a unique closest classical state exists, has zero mean spin, and admits a spin-coherent decomposition into exactly three projectors; no decomposition with fewer than three is possible.

## Assumptions and scope

The Hilbert space is \(\mathbb C^3\), with the standard spin-one representation \(J_x,J_y,J_z\) normalized by \(J_x^2+J_y^2+J_z^2=2I_3\). The density operator \(\rho\) is positive semidefinite of trace one. Its first moments vanish in every Cartesian direction. The classical set \(\mathcal C\) is the convex hull of projectors \(|\mathbf n\rangle_{\mathrm{coh}}\langle\mathbf n|\), where \(\mathbf n\in S^2\) labels a normalized SU(2) coherent spin-one state. Define \(Q(\rho)=\min_{\sigma\in\mathcal C}\sqrt{\operatorname{Tr}(\rho-\sigma)^2}\). The negativity convention is \(\mathcal N(\rho)=(\|\rho^{T_2}\|_1-1)/2\) for the symmetric two-qubit embedding. Thus the ordinary Hilbert–Schmidt norm (not its square, and not trace distance) is used throughout.

The real symmetric \(T\) has \(\operatorname{tr}T=1\), and every eigenvalue \(t_i\) obeys \(t_i\le1\). Indeed \(\mathbf n^{\mathsf T}T\mathbf n=2\operatorname{Tr}(\rho J_{\mathbf n}^2)-1\le1\) for every unit \(\mathbf n\), because the spectrum of \(J_{\mathbf n}^2\) is \(\{0,1,1\}\). In particular, at most one eigenvalue of \(T\) can be negative. The zero-dipole condition defines the full five-real-dimensional zero-first-moment sector, not merely states diagonal in a chosen spin-projection basis.

## Proof

**1. Exact classical moment reduction.** The spin-one Bloch-matrix coordinates of a state are \(X_{00}=1\), \(X_{0a}=\operatorname{Tr}(\rho J_a)\), and \(X_{ab}=T_{ab}\). On the specified sector \(X=\operatorname{diag}(1,T)\). Every classical state has Bloch matrix
\[
W=\sum_j w_j\begin{pmatrix}1\\\mathbf n_j\end{pmatrix}
\begin{pmatrix}1&\mathbf n_j^{\mathsf T}\end{pmatrix}
=\begin{pmatrix}1&\mathbf u^{\mathsf T}\\\mathbf u&S\end{pmatrix},
\quad\mathbf u=\sum_jw_j\mathbf n_j,
\quad S=\sum_jw_j\mathbf n_j\mathbf n_j^{\mathsf T}.
\]
Here \(S\succeq0\) and \(\operatorname{tr}S=1\). Replacing each coherent direction by the equally weighted antipodal pair \(\mathbf n_j,-\mathbf n_j\) is an allowed classical operation preserving \(S\) and making \(\mathbf u=0\); it strictly improves the distance whenever \(\mathbf u\ne0\). Conversely any real positive semidefinite \(S\) of trace one is realized by the equal-antipodal pairs along its orthonormal eigenvectors, with total pair weights given by the eigenvalues. Since \(\|\rho-\sigma\|_2=\frac12\|X-W\|_F\), the full original optimization therefore reduces exactly to
\[
Q(\rho)=\frac12\min_{S\succeq0,\ \operatorname{tr}S=1}\|T-S\|_F.
\]
There is no restriction to classical states with a prescribed axis; the reduction is valid against every coherent mixture.

**2. Sharp matrix projection.** If \(\lambda\ge0\), \(S=T\) is feasible and the distance is zero. If \(\lambda<0\), let \(v\) be a unit eigenvector and choose orthonormal eigenvectors \(e_1,e_2\) in its orthogonal plane, with \(t_1\ge t_2>0\). From \(t_1+t_2+\lambda=1\) and \(t_1,t_2\le1\), both \(t_1,t_2\ge-\lambda\). Consequently
\[
T_*=T+\frac\lambda2 I_3-\frac{3\lambda}{2}vv^{\mathsf T}
=\left(t_1+\frac\lambda2\right)e_1e_1^{\mathsf T}
+\left(t_2+\frac\lambda2\right)e_2e_2^{\mathsf T}
\]
is positive semidefinite with trace one and rank two. For every feasible \(S\),
\[
\langle T-T_*, S-T_*\rangle_F
=\frac{3\lambda}{2}\langle v,Sv\rangle\le0.
\]
Expanding \(\|T-S\|_F^2\) around \(T_*\) gives
\[
\|T-S\|_F^2
=\|T-T_*\|_F^2+\|S-T_*\|_F^2
-2\langle T-T_*,S-T_*\rangle_F
\ge\|T-T_*\|_F^2.
\]
Equality holds only for \(S=T_*\), proving global optimality and uniqueness. Its squared distance is
\[
\|T-T_*\|_F^2=\frac32\lambda^2,
\qquad Q(\rho)^2=\frac38\lambda^2.
\]
For \(\lambda=0\) the zero distance likewise fixes the closest classical state uniquely as \(\rho\).

**3. Explicit three-coherent-state minimizer.** For \(\lambda<0\), write \(c=t_1+\lambda/2\), so \(0<c<1\) and \(T_*=c e_1e_1^{\mathsf T}+(1-c)e_2e_2^{\mathsf T}\). The unit directions
\[
\mathbf n_1=e_1,\qquad
\mathbf n_{\pm}=-c e_1\pm\sqrt{1-c^2}\,e_2
\]
with respective weights
\[
w_1=\frac{c}{1+c},\qquad w_+=w_-=\frac{1}{2(1+c)}
\]
have first moment zero, second moment exactly \(T_*\), and weights summing to one. Their spin-coherent projectors therefore give the unique nearest classical density operator. Each coherent projector contributes a rank-one Bloch matrix \((1,\mathbf n)(1,\mathbf n)^{\mathsf T}\), whereas the nearest classical Bloch matrix \(\operatorname{diag}(1,T_*)\) has rank three. Thus at least three coherent projectors are necessary, and the displayed construction is minimal. A preferred \(e_1\) need not be unique in the degenerate positive-eigenvalue case, but the nearest density operator remains unique.

**4. Exact relation to negativity.** In the symmetric two-qubit embedding, the spin-one Bloch matrix is unitarily similar to twice the qubit partial transpose (the explicit transformation is given in the first reference, Eq. (60)). Therefore its partial-transpose eigenvalues are \(\frac12,\frac{t_1}{2},\frac{t_2}{2},\frac\lambda2\). At most one is negative, and \(\mathcal N(\rho)=\max(0,-\lambda)/2\). Combining this with step 2 yields \(Q=\sqrt{3/2}\,\mathcal N\) for every state in the stated sector, with the classical boundary included.

## Verification

An independent exact-rational example, not diagonal in any spin-projection basis, is
\[
\rho=\begin{pmatrix}1/8&0&3/40\\0&3/4&0\\3/40&0&1/8\end{pmatrix}.
\]
Its eigenvalues are \(1/20,1/5,3/4\), its dipole vanishes, and \(T=\operatorname{diag}(9/10,3/5,-1/2)\). The nearest classical state has \(T_*=\operatorname{diag}(13/20,7/20,0)\) and
\[
\sigma_*=\begin{pmatrix}1/4&0&3/40\\0&1/2&0\\3/40&0&1/4\end{pmatrix}.
\]
Direct matrix subtraction yields \(\operatorname{Tr}(\rho-\sigma_*)^2=3/32\). The four eigenvalues of the embedded two-qubit partial transpose are \(-1/4,3/10,9/20,1/2\), so \(\mathcal N=1/4\), verifying \(Q^2=\frac32\mathcal N^2\). The standard-library script `verify.py` checks this with exact rational arithmetic, the three-coherent-moment formula, and 342 rational spectral examples. Its finite checks corroborate the preceding all-state analytic proof; they are not an exhaustive classification by computation. Run `python3 verify.py`.

## Relationship to prior work

Bohnet-Waldraff, Braun and Giraud [1] give the spin-one Bloch representation, the exact Bloch/Hilbert–Schmidt normalization and the unitary partial-transpose correspondence, solve the quantumness optimization for every **pure** spin-one state, and investigate general mixed states numerically, suggesting a pure-state upper envelope. Their mixed-state section does not optimize exactly over the complete zero-dipole sector, provide the formula here, or construct its minimal three-coherent closest state. In particular, their pure-state function equals \(\sqrt{3/8}(-\lambda)\) for \(\lambda\le-1/2\), while the present mixed-state formula holds over the entire zero-dipole sector including \(-1/2<\lambda<0\). The matrix-classicality criterion from Giraud, Braun and Braun [2] supplies membership but not this exact distance and optimizer. Bohnet-Waldraff's later thesis [3], inspected in its substantive quantum-quantumness sections, gives mixed-state bounds and numerical methods, not this zero-dipole identity. The separate full-spin-projection-diagonal optimization does not cover these generic nonaxial zero-dipole states (whose three quadrupole eigenvalues may be distinct). The unrestricted two-qubit nearest-separable-state optimization is a different feasible set and does not imply the symmetric-constrained optimizer in general.

## Limitations

The formula requires vanishing all three first spin moments; neither its exact proportionality to negativity nor the three-coherent optimizer is asserted for general spin-one mixed states with nonzero dipole. The minimizing classical state is unique, but its coherent-state decomposition need not be unique when the quadrupole has degeneracies. The distance is to the **symmetric** separable (spin-coherent) hull, not the unrestricted two-qubit separable hull. Originality comparison leaves a residual possibility of an equivalent result phrased as a Bell-triplet probability-simplex projection or a specialized convex-moment calculation.

## References

[1] F. Bohnet-Waldraff, D. Braun and O. Giraud, *Quantumness of spin-1 states*, arXiv:1510.07848v1 (first public 2015-10-27), https://arxiv.org/html/1510.07848v1 ; Eqs. (2), (6)–(8), (37)–(41), and (60)–(64).

[2] O. Giraud, P. Braun and D. Braun, *Classicality of spin states*, arXiv:0805.2592v1 (first public 2008-05-16), https://arxiv.org/html/0805.2592v1 ; spin-one classicality and correlation criterion.

[3] F. Bohnet-Waldraff, *Entanglement and Quantumness — New Numerical Approaches*, dissertation (2017), https://publikationen.uni-tuebingen.de/xmlui/bitstream/10900/78034/2/PHD_Bohnet_print_final.pdf ; Chapter 4.1.4, pp. 37–38, and reprinted original paper.

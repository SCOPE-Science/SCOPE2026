# Courant-locked Simpson mass and compensating quadratic semi-Lagrangian steps

## Finding

For the periodic piecewise-quadratic nodal semi-Lagrangian advection update described below, the *unique normalized linear invariant* at every nonintegral Courant displacement \(0<f<2\) is
\[
C_f(u)=\frac{dE(u)+(2-d)O(u)}{2N},\qquad d=\min\{f,2-f\},
\]
where \(E(u)=\sum_{i=0}^{N-1}u_{2i}\) and \(O(u)=\sum_{i=0}^{N-1}u_{2i+1}\). At \(f=1\) the same formula gives the unique invariant, although the update is a permutation. The *integral of the piecewise-quadratic interpolant*, normalized by domain length, is composite Simpson mass
\[
Q(u)=\frac{E(u)+2O(u)}{3N}.
\]
For every \(N\ge2\), exact conservation \(Q(T_fu)=Q(u)\) for all nodal data holds **if and only if** \(f\in\{2/3,4/3\}\). For every nonintegral \(f\in(0,2)\), iterates converge to the constant state \(C_f(u)\mathbf1\) and the sharp worst-data asymptotic mass bias is
\[
\sup_{0\le u_j\le1}|C_f(u)-Q(u)|=\left|\frac d2-\frac13\right|.
\]
In particular the sharp bias tends to \(1/3\) as \(f\downarrow0\) or \(f\uparrow2\), despite the displacement tending to an even integer in grid units.

There is also an exact *two-step compensation law*. If \(0<f_1,f_2<2\), let \(d_i=\min\{f_i,2-f_i\}\). The composite \(T_{f_2}T_{f_1}\) preserves \(Q\) for every nodal vector if and only if
\[
3d_1^2+3(1-2d_1)d_2^2+(1-2d_1)(1-2d_2)-1=0.
\]
Thus two steps can together conserve Simpson mass when neither step does; an exact example is \(f_1=1/4\) and \(f_2=(4+\sqrt{46})/12\). The order of the two steps is part of this statement.

## Assumptions and scope

Fix any integer \(N\ge2\), periodic nodes \(x_j=jh\) with \(j\) modulo \(2N\), \(h>0\), and piecewise quadratic interpolation \(I[u]\) on the even-endpoint elements \([x_{2i},x_{2i+2}]\). Each local quadratic interpolates the three values at \(x_{2i},x_{2i+1},x_{2i+2}\). Define \((T_fu)_j=I[u](x_j+fh)\), using periodic extension; \(0<f<2\). These statements concern exact nodal arithmetic, constant displacement, and, for the two-step statement, two prescribed consecutive displacements. They do not assume positivity of every interpolation coefficient.

## Proof

Write the local Lagrange shape functions at scaled position \(t\in[0,2]\) as
\[
L_0(t)=\frac{(t-1)(t-2)}2,\quad L_1(t)=t(2-t),\quad L_2(t)=\frac{t(t-1)}2.
\]
For \(0<f\le1\), the outputs on each pair of nodes are
\[
(T_fu)_{2i}=L_0(f)u_{2i}+L_1(f)u_{2i+1}+L_2(f)u_{2i+2},
\]
\[
(T_fu)_{2i+1}=L_0(1+f)u_{2i}+L_1(1+f)u_{2i+1}+L_2(1+f)u_{2i+2}.
\]
The pair sums obey the exact closed system
\[
\begin{pmatrix}E(T_fu)\\ O(T_fu)\end{pmatrix}
=M_f\begin{pmatrix}E(u)\\O(u)\end{pmatrix},\qquad
M_f=\begin{pmatrix}1-f(2-f)&f(2-f)\\ f^2&1-f^2\end{pmatrix}.
\]
For \(1<f<2\), the even output uses local position \(f\) and the odd output uses local position \(f-1\) on the next element, yielding precisely \(M_{2-f}\) in the pair-sum relation. Hence the unified system is \(M_d\) with \(d=\min\{f,2-f\}\). Its eigenvalues are \(1\) and \(1-2d\); the normalized left eigenvector at eigenvalue \(1\) is \((d/2,1-d/2)\). For \(0<d<1\), this is the unique stationary left vector of the pair-sum system, and its nodal lift is \(C_f\). Directly, \(C_f(T_fu)=C_f(u)\). At \(f=1\), the update is a one-node cyclic permutation, so the unique invariant is the uniform average, which is also the stated formula.

For completeness, uniqueness among *all nodal* linear invariants and convergence of the full update can be proved without assuming positivity of the nodal interpolation matrix. For \(0<f<1\), the block Fourier symbol of \(T_f\) for \(t=e^{i\theta}\) is
\[
A_f(t)=\begin{pmatrix}L_0(f)+tL_2(f)&L_1(f)\\L_0(1+f)+tL_2(1+f)&L_1(1+f)\end{pmatrix}.
\]
Its trace \(\tau\) and determinant \(\Delta\) are
\[
\tau=\frac{(f-1)(f(t-1)-4)}2,\qquad
\Delta=\frac{(1-f)(2-f)-f(f+1)t}2.
\]
For \(|t|=1\), \(|\Delta|\le1-f+f^2<1\). A direct exact expansion, with \(t=e^{i\theta}\), yields
\[
(1-|\Delta|^2)^2-|\tau-\overline\tau\Delta|^2
=4f^4(2-f)(1-f)^2\sin^4(\theta/2).
\]
The quadratic Schur--Cohn criterion therefore puts both eigenvalues strictly in the open unit disk for \(t\ne1\). When \(t=1\), the two eigenvalues are \(1\) and \(1-2f\). Thus the eigenvalue \(1\) is globally simple and all remaining eigenvalues have modulus strictly below \(1\). Finite-dimensional spectral decomposition gives \(T_f^mu\to C_f(u)\mathbf1\) as integer \(m\to\infty\). The map \(T_{-f}\) is conjugate to \(T_f\) by periodic reflection; \(T_{2-f}\) is a one-element cyclic shift composed with \(T_{-f}\). The element shift commutes with \(T_{-f}\) and acts on every block Fourier fiber by a unimodular scalar, proving the same simplicity and convergence for \(1<f<2\).

Integrating the local quadratic on an element gives Simpson weights \((1,4,1)h/3\); summing all elements and dividing by the domain length \(2Nh\) gives \(Q\). Because the left eigenspace of \(T_f\) for eigenvalue \(1\) is one-dimensional (also at \(f=1\)), Simpson conservation is equivalent to \(d/2=1/3\), which is precisely \(f\in\{2/3,4/3\}\). The bias identity follows by subtraction:
\[
C_f(u)-Q(u)=\left(\frac d2-\frac13\right)
\left(\frac{E(u)}N-\frac{O(u)}N\right).
\]
For bounded nodal data \(0\le u_j\le1\), both parity-class averages lie in \([0,1]\), and the two checkerboard configurations \(u_{2i}=1,u_{2i+1}=0\) and its reflection attain the bound. This proves sharpness and both endpoint limits.

Finally, left multiplication of a normalized parity weight \((p,1-p)\) by \(M_d\) replaces \(p\) by \(\phi_d(p)=d^2+(1-2d)p\). Therefore \(Q(T_{f_2}T_{f_1}u)=Q(u)\) for every \(u\) holds exactly when \(\phi_{d_1}(\phi_{d_2}(1/3))=1/3\), giving the displayed polynomial criterion. For \(d_1=1/4\) the criterion reduces to \((24d_2^2-16d_2-5)/16=0\), and its unique root in \((0,1)\) is \((4+\sqrt{46})/12\). Neither parameter equals \(2/3\).

## Verification

The accompanying `verify.py` reconstructs the complete periodic interpolation matrices with exact rational arithmetic for several mesh sizes and shifts, checks all left invariance and Simpson-resonance identities, tests the two-step polynomial identity, and compares finite Fourier symbols against the analytic Schur factorization. These computations supplement, rather than substitute for, the all-mesh and all-shift algebraic proof above.

## Relationship to prior work

Ferretti and Mehrenberger, *Stability of the \(\mathbb P_2\) Semi-Lagrangian scheme* (arXiv:2610.19806v1, first posted 2026-10-14), establish block-Fourier stability of the quadratic scheme for uniform periodic advection. Their spectral analysis supplies the methodological starting point; the present result concerns a different invariant: the exact left stationary mass, its coincidence with Simpson quadrature at only two Courant values, its sharp long-time mass bias, and exact compensation by two nonconservative consecutive steps. Ferretti and Perrone (2007), cited by that paper, treat partial spectral stability; the complete 2007 chapter was not obtained for comparison. Prior work of Hamiaz et al. (2016) discusses nonconservation of classical semi-Lagrangian schemes on curvilinear grids, but not this parity-resolved quadratic mass classification. Simpson quadrature itself is classical and is not claimed as new.

## Limitations

The limit is for a *fixed finite spatial grid* and indefinitely many steps, not for a simultaneous grid-refinement limit. Worst-case data are parity checkerboards; no size-independent bias is asserted for samples of a fixed smooth periodic function under mesh refinement. An integer one-grid-point shift conserves its uniform nodal mean but does not generally converge to a constant. The two-step compensation criterion guarantees Simpson mass preservation only; it does not alone imply positivity, error estimates, or stability for arbitrary variable-step sequences. Older inaccessible specialized interpolation literature may contain an equivalent invariant calculation; independent audit has not been carried out.

## References

1. R. Ferretti and M. Mehrenberger, *Stability of the \(\mathbb P_2\) Semi-Lagrangian scheme*, arXiv:2610.19806v1 (2026-10-14), https://arxiv.org/abs/2610.19806.
2. R. Ferretti and G. Perrone, *On the stability of semi-Lagrangian advection schemes under finite element interpolations*, in *Applied and Industrial Mathematics in Italy II*, 339--350, World Scientific (2007).
3. A. Hamiaz, M. Mehrenberger, H. Sellama and E. Sonnendrücker, *The semi-Lagrangian method on curvilinear grids*, Communications in Applied and Industrial Mathematics 7 (2016), 96--134, https://doi.org/10.1515/caim-2016-0024.
4. R. Ferretti, *On the relationship between semi-Lagrangian and Lagrange--Galerkin schemes*, Numerische Mathematik 124 (2013), 31--56, https://doi.org/10.1007/s00211-012-0505-5.

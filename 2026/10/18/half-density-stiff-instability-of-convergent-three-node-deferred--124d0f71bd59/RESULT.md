# Half-density stiff instability of convergent three-node deferred-correction sweeps

## Finding

For the canonical implicit-Euler-preconditioned spectral deferred correction (SDC) iteration on the three Gauss–Lobatto nodes \(0,\frac12,1\), the scalar decay equation \(y'=\lambda y\), \(\lambda<0\), exhibits an exact distinction between convergence of the *correction iteration* and stability of the *finite-sweep time-step map*.

Write \(z=h\lambda<0\). Starting with constant stages and taking exactly \(K\ge1\) correction sweeps gives a one-step multiplier \(R_K(z)\). Its stiff limit is
\[
R_K^{\mathrm{stiff}}:=\lim_{r\to\infty}R_K(-r)
=1-\frac{2^{1-K}\sin(K\theta)}{\sin\theta},
\qquad \theta=\arccos\!\left(\frac{11}{12}\right).
\]
The angle \(\theta/\pi\) is irrational. Consequently the set of positive sweep counts \(K\) for which \(R_K^{\mathrm{stiff}}>1\) has **natural density exactly \(1/2\)**. For each such count there is a finite negative real \(z\) with \(R_K(z)>1\): the corresponding finite-sweep integrator amplifies an exponentially decaying scalar mode. The **first stiff-limit overshoot occurs at \(K=8\)**, with
\[
R_8^{\mathrm{stiff}}=\frac{35934757}{35831808}
=1+\frac{102949}{35831808}>1.
\]
An explicit finite negative-axis witness is \(R_8(-5000)>1\) in exact rational arithmetic. Yet for every *fixed* \(z<0\), the SDC sweeps converge geometrically to the stable Simpson-collocation update, with correction-iteration spectral radius \(\lvert z\rvert/[2(2+\lvert z\rvert)]<1/2\).

## Assumptions and scope

Let \(h>0\), \(\lambda<0\), and normalize the initial scalar value to \(1\). Use the nodes \(\tau=(0,1/2,1)\), whose Lagrange integration matrix and standard backward-Euler subinterval preconditioner are
\[
Q=\begin{pmatrix}0&0&0\\5/24&1/3&-1/24\\1/6&2/3&1/6\end{pmatrix},
\qquad
D=\begin{pmatrix}0&0&0\\0&1/2&0\\0&1/2&1/2\end{pmatrix}.
\]
Set \(U^{(0)}=(1,1,1)^{\mathsf T}\). For every integer \(K\ge1\), perform exactly \(K\) iterations of
\[
(I-zD)U^{(k+1)}=\mathbf1+z(Q-D)U^{(k)},
\quad k=0,\ldots,K-1,
\]
and define \(R_K(z)\) as the third component of \(U^{(K)}\). At the initial node, every iterate is fixed at \(1\). The final result applies only to this exact-arithmetic, fixed-sweep, three-node iteration, not to alternative preconditioners or adaptive error controllers.

## Proof

**1. The exact collocation map is negative-axis contractive.** Integrating the three Lagrange cardinal polynomials over \([0,\tau_i]\) gives \(Q\), while two backward-Euler subintervals of length \(h/2\) give \(D\). The collocation fixed point solves \((I-zQ)U=\mathbf1\). Its last component is the Simpson/Lobatto stability function
\[
R_{\mathrm{coll}}(z)=\frac{z^2+6z+12}{z^2-6z+12}.
\]
For every \(r>0\), \(0<R_{\mathrm{coll}}(-r)=(r^2-6r+12)/(r^2+6r+12)<1\); numerator positivity follows from \(r^2-6r+12=(r-3)^2+3\).

**2. Every fixed negative-axis correction iteration converges.** Subtracting the collocation fixed point from the sweep equation gives the linear error matrix \(G(z)=z(I-zD)^{-1}(Q-D)\). Its nontrivial two-by-two block \(B(z)\), acting on the two noninitial stages, satisfies
\[
\operatorname{tr}B(z)=\frac{z(11z-24)}{12(z-2)^2},\qquad
\det B(z)=\frac{z^2}{4(z-2)^2},
\]
with discriminant
\[
(\operatorname{tr}B(z))^2-4\det B(z)
=\frac{z^3(48-23z)}{144(z-2)^4}<0
\quad(z<0).
\]
The conjugate eigenvalues therefore have modulus \(\sqrt{\det B(z)}=\lvert z\rvert/[2(2+\lvert z\rvert)]<1/2\). The first-stage error is always zero. Hence \(U^{(K)}\) converges for every fixed \(z<0\) to the stable collocation fixed point.

**3. The stiff-limit endpoint has an oscillating exact recurrence.** Taking \(z\to-\infty\) in the one-sweep rational matrix is legitimate for each fixed sweep count. The initial stage remains \(1\); the remaining two stages obey an affine iteration with linear part
\[
B_{\infty}=\begin{pmatrix}1/3&1/12\\-2/3&7/12\end{pmatrix}
\]
and forcing \((-5/12,1/12)^{\mathsf T}\). The fixed point of this affine map is \((-1/2,1)^{\mathsf T}\), and its eigenvalues are \(\frac12e^{\pm i\theta}\) with \(\cos\theta=11/12\). If \(e_K:=R_K^{\mathrm{stiff}}-1\), then the Cayley–Hamilton identity and the constant-stage initialization give
\[
e_0=0,\quad e_1=-1,\qquad
e_{K+2}=\frac{11}{12}e_{K+1}-\frac14 e_K.
\]
Solving this recurrence yields \(e_K=-2^{1-K}\sin(K\theta)/\sin\theta\), the claimed formula. Exact recurrence evaluation gives \(R_1^{\mathrm{stiff}}=0\), \(R_2^{\mathrm{stiff}}=1/12\), \(R_3^{\mathrm{stiff}}=59/144\), \(R_4^{\mathrm{stiff}}=1189/1728\), \(R_5^{\mathrm{stiff}}=17867/20736\), \(R_6^{\mathrm{stiff}}=236677/248832\), \(R_7^{\mathrm{stiff}}=2955563/2985984\), and the displayed \(R_8^{\mathrm{stiff}}>1\).

**4. The overshoot sweep counts have natural density one half.** If \(\theta/\pi\) were rational, \(\exp(i\theta)\) would be a root of unity and \(2\cos\theta=11/6\) would be a rational algebraic integer, hence an integer. It is not, so \(\theta/\pi\) is irrational. Irrational circle rotations imply that \(K\theta\) is equidistributed modulo \(2\pi\) among positive integers. Exactly half the circle has negative sine. Thus \(\sin(K\theta)<0\), equivalently \(R_K^{\mathrm{stiff}}>1\), for a set of sweep counts of natural density \(1/2\). By continuity of the rational multiplier near \(z=-\infty\), every such count admits a *finite* negative \(z\) with \(R_K(z)>1\). In particular an exact eight-sweep evaluation at \(z=-5000\) is strictly greater than \(1\). Repeating that fixed time step yields geometric amplitude growth although the exact solution decays.

## Verification

The standalone `verify.py` reconstructs the quadrature matrix by exact integration, checks the rational correction-iteration trace, determinant, discriminant, and collocation multiplier symbolically, confirms the stiff-limit affine matrix and recurrence for sixty sweep counts, and independently compares direct triangular sweeps with the full matrix formula. It verifies \(R_8^{\mathrm{stiff}}=35934757/35831808\) and \(R_8(-5000)>1\) using exact rationals. Invoke `python verify.py` with Python 3 and SymPy. The infinite density statement is justified by the irrational-rotation argument in the proof, not by a finite numerical run.

## Relationship to prior work

Saupe and coauthors give the general preconditioned SDC fixed-point equation, implicit-Euler sweepers, and adaptive timestep mechanisms [1]. Their analysis does **not**, in the inspected sections, state the above three-node exact sweep-count recurrence or its natural-density implication. Later work on parallel SDC derives generic stiff-limit iteration matrices and examines stability domains for different preconditioners [2]; this is foundational rather than a proof of the present scalar Lobatto/implicit-Euler half-density classification. Classical semi-implicit SDC literature analyzes stability and accuracy more broadly [3], and work on second-order SDC exhibits sweep-count-dependent stability diagrams [4]. The present statement is specifically the exact first-order three-node linear-decay recurrence, the first stiff-limit overshoot, and the density-half phenomenon, not the invention of SDC, its iteration matrix, or Simpson collocation.

## Limitations

Only the negative real axis is analyzed, and only with the specific matrices, fixed-stage initialization, and exact solves stated above. The theorem does not classify the entire complex absolute-stability region or the behavior of adaptive or nonlinear SDC implementations. The density-half result concerns **sweep counts at their separate infinite-stiffness limits**; for each *fixed finite* stiffness, enough sweeps recover the stable collocation result. Prior stability-region literature could contain a mathematically equivalent special-case calculation not found in the inspected material; independent bibliographic verification remains appropriate.

## References

[1] T. Saupe (formerly T. Baumann), S. Götschel, T. Lunet, D. Ruprecht and R. Speck, *Adaptive time step selection for Spectral Deferred Correction*, arXiv:2403.13454 (first submitted 2024-03-20; revision 2024-09-04), DOI:10.1007/s11075-024-01964-z.

[2] *Improving Efficiency of Parallel Across the Method Spectral Deferred Corrections*, SIAM Journal on Scientific Computing, DOI:10.1137/24M1649800.

[3] M. L. Minion, *Semi-Implicit Spectral Deferred Correction Methods for Ordinary Differential Equations*, Communications in Mathematical Sciences 1 (2003), 471–500, DOI:10.4310/CMS.2003.v1.n3.a6.

[4] I. Akramov, S. Götschel, M. Minion, D. Ruprecht and R. Speck, *Spectral Deferred Correction Methods for Second-Order Problems*, arXiv:2310.08352, DOI:10.1137/23M1592596.

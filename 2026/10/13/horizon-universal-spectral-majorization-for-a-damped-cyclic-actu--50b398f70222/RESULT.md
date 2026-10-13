# Horizon-universal spectral majorization for a damped cyclic actuator

## Finding

Consider a discrete-time system with one scalar control input,
\[
 x_{k+1}=rSx_k+bu_k,
\]
where \(n\ge2\), \(0<r<1\), \(S\) cyclically shifts the coordinates of \(\mathbb R^n\) by one place, and the freely selected actuator vector \(b\in\mathbb R^n\) satisfies \(\|b\|_2=1\). For every horizon \(H\in\{n,n+1,\ldots\}\cup\{\infty\}\), set
\[
 W_H(b)=\sum_{k=0}^{H-1}r^{2k}S^kbb^{\mathsf T}(S^k)^{\mathsf T},
 \qquad
 d_j(H)=\sum_{\substack{\ell\ge0\\j+\ell n<H}}r^{2(j+\ell n)},\quad 0\le j<n,
\]
with an infinite sum when \(H=\infty\). These phase weights satisfy \(d_0(H)>d_1(H)>\cdots>d_{n-1}(H)>0\). Let the eigenvalues of \(W_H(b)\) be in decreasing order \(\lambda_1\ge\cdots\ge\lambda_n\).

**Universal spectral statement.** For every admissible \(b\) and each \(1\le k\le n\),
\[
 \sum_{i=1}^k\lambda_i\ \ge\ \sum_{j=0}^{k-1}d_j(H),
 \qquad \sum_{i=1}^n\lambda_i=\sum_{j=0}^{n-1}d_j(H).
\]
In other words, the controllability-Gramian spectrum **majorizes** the fixed phase-weight vector. The spectra are identical (with multiplicity) if and only if
\[
 \langle b,S^j b\rangle=0\qquad (1\le j<n).
\]
This optimizer condition does **not** depend on the horizon or damping parameter.

The same and only actuator vectors attain all four exact optimal energy/conditioning criteria:
\[
 \boxed{\ \max_b\lambda_{\min}(W_H(b))=d_{n-1}(H)\ },
 \qquad
 \boxed{\ \max_b\det W_H(b)=\prod_{j=0}^{n-1}d_j(H)\ },
\]
\[
 \boxed{\ \min_b\operatorname{tr}(W_H(b)^{-1})=\sum_{j=0}^{n-1}d_j(H)^{-1}\ },
 \qquad
 \boxed{\ \min_b\kappa_2(W_H(b))=d_0(H)/d_{n-1}(H)\ }.
\]
Here the inverse trace and condition number are \(+\infty\) for singular Gramians. All four optimizer sets are exactly the real unit vectors whose \(n\) cyclic shifts are mutually orthogonal. The same vectors also minimize every strictly convex separable spectral cost \(\sum_{i=1}^n\phi(\lambda_i)\) for which \(\phi\) is finite and strictly convex on the relevant spectral interval.

These vectors have an equivalent Fourier characterization: for \(\zeta=e^{-2\pi i/n}\), every discrete Fourier coefficient \(\widehat b_k=\sum_{j=0}^{n-1}b_j\zeta^{jk}\) must have modulus one. Among **nonnegative** unit vectors, the only optimizers are the \(n\) single-coordinate actuators. Without the sign constraint there are also nonlocal optima, for example \(b=(2/3,2/3,-1/3)\) for \(n=3\).

By contrast, \(\operatorname{tr}W_H(b)=\sum_j d_j(H)\) for *every* unit \(b\), including the entirely uncontrollable uniform actuator \(b=n^{-1/2}(1,\ldots,1)\). Thus the Gramian trace cannot rank actuator directions on this directed-cycle family, while the three energy/volume objectives sharply distinguish them.

## Assumptions and scope

The state dimension is any integer \(n\ge2\); the real damping satisfies \(0<r<1\), and the system matrix is exactly the scalar multiple \(rS\) of a single cyclic coordinate permutation. The scalar input is applied at every step through a fixed, real, unit-norm vector, potentially with negative components. The horizon is an integer \(H\ge n\) or infinite. All optimization ranges include singular Gramians, with the stated extended-real conventions. The system has no process or observation noise and no actuator-placement combinatorial restriction.

For finite \(H\), the phase weights can be computed as a finite sum. For infinite \(H\), they simplify to
\[
 d_j(\infty)=\frac{r^{2j}}{1-r^{2n}}.
\]
The optimal worst-case unit-target control energy is therefore
\[
 \frac1{d_{n-1}(H)},
 \qquad
 \frac{1-r^{2n}}{r^{2(n-1)}}\quad\text{for }H=\infty.
\]
This quantity follows from the minimum-energy reachability formula \(\max_{\|v\|_2=1}v^{\mathsf T}W_H^{-1}v=1/\lambda_{\min}(W_H)\) for a nonsingular Gramian.

## Proof

**1. Exact cyclic factorization.** Since \(S^n=I\), write
\[
 C(b)=[\,b\ \ Sb\ \ \cdots\ \ S^{n-1}b\,],\qquad
 D_H=\operatorname{diag}(d_0(H),\ldots,d_{n-1}(H)).
\]
Grouping the powers \(k\) by their residues modulo \(n\) gives the exact identity
\[
 W_H(b)=C(b)D_HC(b)^{\mathsf T}.
\]
Each column of \(C(b)\) has norm one because \(S\) is orthogonal. The terms of \(d_j(H)\) are powers of \(r^2\), starting at \(j\), with no more terms at phase \(j+1\) than at phase \(j\). Hence \(d_j(H)>d_{j+1}(H)>0\) for \(j<n-1\) and all stated horizons.

**2. Majorization and equality.** Set \(B_H=D_H^{1/2}C(b)^{\mathsf T}C(b)D_H^{1/2}\). It is positive semidefinite, has diagonal entries \((d_0(H),\ldots,d_{n-1}(H))\), and has precisely the same eigenvalues as \(W_H(b)\). By the variational characterization of the sum of the \(k\) largest eigenvalues, the trace on the first \(k\) coordinate axes is no greater than their sum; that coordinate trace equals \(\sum_{j<k}d_j(H)\). The total traces coincide. This proves every majorization inequality without a genericity assumption.

If the eigenvalue multiset equals the \(d_j(H)\) multiset, then
\[
 \operatorname{tr}(B_H^2)=\sum_jd_j(H)^2.
\]
But direct expansion gives
\[
 \operatorname{tr}(B_H^2)
 =\sum_jd_j(H)^2
   +2\sum_{0\le i<j<n}d_i(H)d_j(H)\langle S^ib,S^jb\rangle^2.
\]
Every phase weight is positive, so all the cross-inner-products vanish. Conversely, if they vanish then \(C(b)\) is orthogonal and \(W_H(b)\) is orthogonally similar to \(D_H\). Thus spectral equality holds precisely for orthogonal cyclic orbits. Standard convexity of majorization additionally gives the strictly convex spectral-cost claim; equality in any strictly convex spectral sum forces the spectra to coincide and hence orthogonality.

**3. Exact and exclusive energy optima.** By the Hadamard determinant bound for the unit columns of \(C(b)\),
\[
 \det W_H(b)=\det(D_H)\det(C(b))^2\le\prod_jd_j(H),
\]
with equality precisely when the columns are orthonormal.

For the smallest eigenvalue, select a unit vector \(v\) orthogonal to the first \(n-1\) cyclic columns. Then
\[
 \lambda_{\min}(W_H(b))
 \le v^{\mathsf T}W_H(b)v
 =d_{n-1}(H)|\langle v,S^{n-1}b\rangle|^2
 \le d_{n-1}(H).
\]
If equality holds, the last scalar product has modulus one, so \(S^{n-1}b\) is orthogonal to all earlier cyclic columns. Applying cyclic shifts to these relations shows \(\langle b,S^j b\rangle=0\) for every \(1\le j<n\), establishing uniqueness of the optimizer set; orthogonal cyclic columns attain equality.

If \(C(b)\) is nonsingular, let \(w_j^{\mathsf T}\) denote row \(j\) of \(C(b)^{-1}\), using indices \(0\le j<n\). Since \(\langle w_j,S^jb\rangle=1\) and \(\|S^jb\|_2=1\), Cauchy–Schwarz gives \(\|w_j\|_2^2\ge1\). The inverse factorization yields
\[
 \operatorname{tr}(W_H(b)^{-1})
 =\sum_{j=0}^{n-1}d_j(H)^{-1}\|w_j\|_2^2
 \ge\sum_{j=0}^{n-1}d_j(H)^{-1}.
\]
Equality forces every \(w_j=S^jb\), equivalently \(C(b)^{-1}=C(b)^{\mathsf T}\). A singular Gramian has infinite inverse-trace objective and cannot be optimal.

Finally \(\lambda_{\max}(W_H(b))\ge d_0(H)\) by the Rayleigh quotient at \(b\), and the preceding estimate gives \(\lambda_{\min}(W_H(b))\le d_{n-1}(H)\). Consequently \(\kappa_2(W_H(b))\ge d_0(H)/d_{n-1}(H)\), with equality only at the already characterized minimum-eigenvalue optimizers.

**4. Fourier and sign conditions.** Orthogonality of the cyclic columns is equivalent to the periodic autocorrelation equations \(\sum_{m=0}^{n-1}b_mb_{m+j\bmod n}=0\) for each \(1\le j<n\). Because \(C(b)\) is a real circulant matrix, its complex eigenvalues are exactly the unnormalized discrete Fourier coefficients \(\widehat b_k\). Therefore \(C(b)\) is orthogonal if and only if all \(|\widehat b_k|=1\). These equivalences include all real signed optimal vectors, not only standard basis vectors. If \(b\ge0\), any two positive coordinates create a strictly positive summand in one nonzero-lag autocorrelation, so the support has at most one element; unit norm then yields \(b=e_j\). The converse is immediate.

**5. Failure of the trace criterion.** The factorization gives \(\operatorname{tr}W_H(b)=\sum_jd_j(H)\), independent of \(b\), because all orbit columns have unit norm. When \(b=n^{-1/2}(1,\ldots,1)\), it is fixed by \(S\), so the Gramian is a positive multiple of \(bb^{\mathsf T}\) and has rank one. For \(n\ge2\) it is uncontrollable despite attaining exactly the same trace as an optimal coordinate actuator.

## Verification

The standalone file `cyclic_gramian_checker.py` requires Python 3 and its standard library only. Run `python cyclic_gramian_checker.py`. It checks rational Gramian factorization, strict ordering of phase weights, determinant identities and Hadamard bounds, inverse-trace lower bounds, cyclic autocorrelations, and the exact three-state signed example at both finite and infinite horizons. It reports `VERIFY_OK 108 exact-rational Gramian, determinant, and inverse-trace cases`. These examples do not replace the all-dimension, all-horizon algebraic proof.

For \(n=3\), \(r=1/2\), \(H=\infty\), and \(b=(2/3,2/3,-1/3)\), the exact phase weights are \((64/63,16/63,4/63)\). Thus the Gramian is orthogonally similar to the diagonal matrix with these entries, giving \(\det W=4096/63^3\) and \(\operatorname{tr}(W^{-1})=1323/64\), both verified exactly.

## Relationship to prior work

The controllability Gramian and its energy, minimum-eigenvalue, determinant and trace metrics are classical. Summers and Lygeros (arXiv:1306.2491) analyze finite **sets** of possible actuator locations and establish modularity of linear Gramian metrics; they do not characterize freely oriented scalar actuators for a damped directed-cycle permutation over every horizon. Pasqualetti, Zampieri and Bullo (2014, full open manuscript) analyze discrete-time network Gramian energies, including circulant graphs and a trace-based control-node selection problem. Their input matrices select canonical coordinate actuators; the present claim allows every unit signed vector, yields the full spectral majorization, and classifies simultaneous extrema of nonlinear energy criteria.

Tzoumas and collaborators (arXiv:1503.04693) study minimum actuator-**set** selection with energy constraints, rather than the continuous vector and cyclic orthogonality problem. The circulant-network work of Nabi-Abdolyousefi and Mesbahi examines weighted consensus protocols and controllability of node-controlled Laplacian networks. Its available descriptions do not settle whether the full specialized Gramian chapter includes an equivalent statement; the complete thesis/chapter could not be inspected, so this comparison remains a concrete originality risk. The broad 2016 actuator-design work of Chen and Belabbas uses a symmetric continuous-time matrix, in contrast to the present discrete directed permutation. None of these classical approaches or problem definitions is claimed as new.

## Limitations

The theorem is exact only for a uniformly damped one-way cyclic permutation and a *fixed* scalar input direction, without actuator cost heterogeneity, spatially varying damping, or external noise. The four optimality objectives share minimizers **on this family**; no general equivalence is claimed for arbitrary circulant, symmetric, or nonnormal dynamics. Horizons shorter than the state dimension are excluded because a scalar input then yields a singular Gramian. For finite horizons, the stated bounds require \(H\ge n\); for an infinite horizon \(0<r<1\) is essential. The Fourier classification includes potentially signed distributed inputs, which may be physically inadmissible in some applications. The majorization variational principle, Hadamard inequality, and Fourier orthogonality are established mathematical tools, not new lemmas. A historically equivalent specialized treatment in uninspected circulant-control literature remains possible.

## References

1. T. H. Summers and J. Lygeros, *Optimal Sensor and Actuator Placement in Complex Dynamical Networks*, arXiv:1306.2491v1, publicly posted June 11, 2013. https://arxiv.org/abs/1306.2491
2. F. Pasqualetti, S. Zampieri and F. Bullo, *Controllability Metrics, Limitations and Algorithms for Complex Networks*, 2014. Full manuscript: https://motion.me.ucsb.edu/pdf/2013q-pzb.pdf
3. V. Tzoumas, M. A. Rahimian, G. J. Pappas and A. Jadbabaie, *Minimal Actuator Placement with Optimal Control Constraints*, arXiv:1503.04693v1 (2015). https://arxiv.org/abs/1503.04693
4. M. Nabi-Abdolyousefi, *Controllability Gramian, Symmetry Structures, and Application of Circulant Networks*, in *Controllability, Identification, and Randomness in Distributed Systems*, Springer (2014), DOI:10.1007/978-3-319-02429-5_6. Full chapter not inspected. https://doi.org/10.1007/978-3-319-02429-5_6
5. M. Nabi-Abdolyousefi and M. Mesbahi, *On the Controllability Properties of Circulant Networks*, IEEE Transactions on Automatic Control 58 (2013), 3179–3184, DOI:10.1109/TAC.2013.2259992. Full article not inspected. https://doi.org/10.1109/TAC.2013.2259992
6. X. Chen and M.-A. Belabbas, *Optimal Actuator Design for Minimizing the Worst-Case Control Energy*, arXiv:1610.08885v1 (2016), publicly posted after October 4, 2016, cited for comparison only. https://arxiv.org/abs/1610.08885

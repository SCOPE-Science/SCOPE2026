# Sharp error-budget duality for two-observable numerical information

## Finding
Let \(H\) be a finite-dimensional complex Hilbert space, let \(A_1,A_2,B\) be self-adjoint operators on \(H\), and let \(\varepsilon_1,\varepsilon_2\ge0\). Define the worst indistinguishability of the \(B\)-expectation when the first two expectations are recorded only to specified absolute tolerances by
\[
\Delta_{\boldsymbol\varepsilon}(B\mid A_1,A_2)=
\max_{\substack{\|x\|=\|y\|=1\\
|\langle A_jx,x\rangle-\langle A_jy,y\rangle|\le\varepsilon_j\ (j=1,2)}}
|\langle Bx,x\rangle-\langle By,y\rangle|.
\]
Then, with \(\operatorname{spr}(X)=\lambda_{\max}(X)-\lambda_{\min}(X)\) for self-adjoint \(X\),
\[
\boxed{\displaystyle
\Delta_{\boldsymbol\varepsilon}(B\mid A_1,A_2)=
\min_{(t_1,t_2)\in\mathbb R^2}
\left\{\operatorname{spr}(B-t_1A_1-t_2A_2)
+\varepsilon_1|t_1|+\varepsilon_2|t_2|\right\}.}
\]
Equivalently, this is the minimum of
\[
2\|B-cI-t_1A_1-t_2A_2\|+\varepsilon_1|t_1|+\varepsilon_2|t_2|
\]
over real \(c,t_1,t_2\). Both the worst-case pair of *pure states* and the dual minimum are attained. The exact formula applies to any nonnegative error budget, including at least one strictly positive tolerance; the zero-budget case is an established precursor, not an original part of the claim.

The error dependence need not be affine. For \(H=\mathbb C^2\), \(A_1=\sigma_x\), \(A_2=\sigma_z\), \(B=\sigma_x+\sigma_y\), and \((\varepsilon_1,\varepsilon_2)=(e,0)\), the exact profile is
\[
\boxed{\displaystyle
\Delta_{(e,0)}=
\begin{cases}
e+\sqrt{4-e^2},&0\le e\le\sqrt2,\\
2\sqrt2,&e\ge\sqrt2.
\end{cases}}
\]
Thus an active-error regime gives way to a saturated-information regime at the sharp threshold \(e=\sqrt2\).

## Assumptions and scope
The dimension of \(H\) is any positive finite integer; no commutativity, independence, positivity, or spectral gap is assumed for the self-adjoint matrices \(A_1,A_2,B\). Each tolerance is an absolute difference of expectation values, rather than an error in the outcome distribution of a measurement. The extremization is over pairs of unit vectors, not initially over mixed density matrices. The spectral spread and matrix norm use the standard Hilbert-space operator norm. All coefficients in the dual formula are real.

## Proof
**1. Mixed-state dual identity.** Let \(\mathcal D(H)\) be the compact convex set of density matrices. For \(\rho,\sigma\in\mathcal D(H)\), put \(b(\rho,\sigma)=\operatorname{tr}(B(\rho-\sigma))\) and \(a_j(\rho,\sigma)=\operatorname{tr}(A_j(\rho-\sigma))\). By interchanging \(\rho\) and \(\sigma\), maximization of \(b\) is equivalent to maximization of \(|b|\). Define
\[
L((\rho,\sigma),t)=b(\rho,\sigma)-\sum_{j=1}^2 t_ja_j(\rho,\sigma)+\sum_{j=1}^2\varepsilon_j|t_j|.
\]
For any fixed pair \((\rho,\sigma)\), \(\inf_{t\in\mathbb R^2}L=b\) if \(|a_j|\le\varepsilon_j\) for both \(j\), and \(-\infty\) otherwise. Sion's minimax theorem applies because \(\mathcal D(H)^2\) is compact convex, \(L\) is continuous affine in the pair and continuous convex in \(t\). Therefore
\[
\max_{\substack{\rho,\sigma\in\mathcal D(H)\\|a_j|\le\varepsilon_j}}b
=\inf_{t\in\mathbb R^2}\max_{\rho,\sigma\in\mathcal D(H)}L((\rho,\sigma),t).
\]
For a self-adjoint matrix \(X\), \(\max_{\rho,\sigma\in\mathcal D(H)}\operatorname{tr}(X(\rho-\sigma))=\lambda_{\max}(X)-\lambda_{\min}(X)\). This proves the displayed dual formula for *mixed* states.

**2. A rank-rigidity lemma for two error constraints.** Let \(K\) be the compact convex set of mixed-state pairs satisfying \(|a_j|\le\varepsilon_j\). We show that every extreme point \((\rho,\sigma)\) of \(K\) consists of two rank-one densities. Write their ranks as \(r,s\ge1\). Hermitian perturbations supported in the ranges of \(\rho\) and \(\sigma\) form a real vector space of dimension \(r^2+s^2\). To preserve both trace-one constraints imposes two real homogeneous linear equations. For each error constraint, there is at most one *independent* active boundary equation: when \(\varepsilon_j>0\) at most one side of the two-sided bound is active, and when \(\varepsilon_j=0\) the two sides coincide as one equality. Hence there are at most four independent equations in total. If \(r^2+s^2>4\), a nonzero supported Hermitian perturbation solves all active equations. Both signs of a sufficiently small multiple preserve positivity, the trace constraints, and every inactive strict inequality. This expresses the pair as the midpoint of two distinct points of \(K\), contradicting extremality. It follows that \(r^2+s^2\le4\). Since each rank is at least one, necessarily \(r=s=1\).

A continuous linear functional on nonempty compact convex \(K\) attains its maximum at an extreme point. Therefore the mixed-state optimum from step 1 is attained at rank-one projections \(\rho=xx^*\) and \(\sigma=yy^*\), exactly the original pure-state feasible set. This proves the claimed identity and attainment of the primal maximum.

**3. Attainment of the dual minimum.** On the real vector space of self-adjoint matrices modulo scalar multiples of \(I\), spectral spread is a norm. After quotienting \(\mathbb R^2\) by directions \(t\) for which both \(t_1A_1+t_2A_2\) are scalar and \(\varepsilon_1|t_1|+\varepsilon_2|t_2|=0\), the dual objective has bounded sublevel sets: it is the distance, in the finite-dimensional product norm \(\operatorname{spr}(X)+\sum_j|u_j|\), from \(([B],0,0)\) to the finite-dimensional linear image \(t\mapsto([t_1A_1+t_2A_2],-\varepsilon_1t_1,-\varepsilon_2t_2)\). A nearest point to the closed linear image exists. Consequently the infimum is a minimum. The equivalence with the shifted operator norm follows from \(\operatorname{spr}(X)=2\min_{c\in\mathbb R}\|X-cI\|\).

**4. Explicit sharp phase transition.** In dimension two, write pure-state density matrices as \((I+r\cdot\sigma)/2\), with Bloch vectors \(r\in S^2\). Every displacement \(d=r-s\) with \(\|d\|_2\le2\) occurs: choose a midpoint perpendicular to \(d\) of length \(\sqrt{1-\|d\|_2^2/4}\). The displayed Pauli instance therefore maximizes \(d_x+d_y\) subject to \(d_x^2+d_y^2+d_z^2\le4\), \(|d_x|\le e\), and \(d_z=0\). The optimum is \(e+\sqrt{4-e^2}\) for \(e\le\sqrt2\), and \(2\sqrt2\) afterward. This verifies the sharp threshold and both expressions.

## Verification
The theorem is proved for every finite dimension and all nonnegative budgets by the minimax, rank-rigidity and distance-attainment steps above. The standalone computer-reproducible script `CHECK.py` performs 2,540 finite diagnostic assertions for the Pauli profile and checks its primal and dual formulas at ten budgets. These finite computations are supplementary and not a proof of the general theorem.

## Relationship to prior work
Dylan Johnson, *Numerical Information of Hilbert Space Operators* (arXiv:2610.29826v1, October 21, 2026), proves qualitative inclusion of numerical-information sigma algebras and an affine characterization of exact dependence; it does not give the positive-tolerance error budget and the sharp penalized spectral-spread formula. Chen, Dawkins, Ji, Johnston, Kribs, Shultz and Zeng, *Uniqueness of Quantum States Compatible with Given Measurement Results* (arXiv:1212.3503, December 14, 2012), prove a qualitative pure-versus-mixed uniqueness implication for two exact observables, not this worst-case error envelope. A previous exact-budget-zero result establishes the identity when both tolerances vanish; the new result concerns arbitrarily positive tolerances, uses an inequality-constrained rank argument, and yields a sharp nonlinear noise profile. The zero-budget formula is not claimed as novel.

## Limitations
Only two recorded self-adjoint observables are treated, and the argument depends crucially on having at most four active affine constraints on pairs of density matrices. With more recorded observables, extremal feasible pairs may have higher rank, so the pure-state equality is not asserted. The theorem is stated for finite-dimensional complex Hilbert spaces; no unbounded operators, experimental statistical estimators, or outcome-distribution error models are included. The literature comparison is a best-knowledge assessment rather than a definitive publication-priority determination; independent verification is not yet available.

## References
1. D. M. Johnson, *Numerical Information of Hilbert Space Operators*, arXiv:2610.29826v1 (2026), Sections 2, 4 and 5.
2. J. Chen, H. Dawkins, Z. Ji, N. Johnston, D. Kribs, F. Shultz and B. Zeng, *Uniqueness of Quantum States Compatible with Given Measurement Results*, arXiv:1212.3503 (2012), Section IV and Appendix C.
3. M. Sion, *On general minimax theorems*, Pacific Journal of Mathematics **8** (1958), 171–176.

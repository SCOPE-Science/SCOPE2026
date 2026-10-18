# Sharp Lipschitz defect and optimizer rigidity for torus-rotation torsions

## Finding
Let \(d\ge1\), \(\mathbb T^d=\mathbb R^d/(2\pi\mathbb Z)^d\), and \(E=C(\mathbb T^d;\mathbb C)\) with its supremum norm and pointwise complex Banach-lattice modulus. For \(\beta\in\mathbb R^d\), let \(T_\beta f(x)=f(x+\beta)\). A torsion is a complex-linear operator \(U:E\to E\) such that \(|Uf|=|f|\) for all \(f\in E\). Equip the torus with its flat geodesic distance, the unit circle with chordal distance, and denote the resulting Lipschitz seminorm by \(\operatorname{Lip}\).

For every \(\lambda\in\mathbb C\) with \(|\lambda|=1\), and every real \(L\ge0\), the following infimum is attained, with the **exact value**
\[
\Delta_L(\beta,\lambda):=
\inf_{\substack{U\text{ torsion}\\\operatorname{Lip}(U\mathbf1)\le L}}
\|T_\beta U-\lambda UT_\beta\|
=
\min_{\substack{k\in\mathbb Z^d\\\|k\|_2\le L}}
\big|e^{i\langle k,\beta\rangle}-\lambda\big|.
\]
Every minimizing lattice vector \(k\) yields a minimizer \(U=M_{\chi_k}\), where \(\chi_k(x)=e^{i\langle k,x\rangle}\) and \(M_{\chi_k}f=\chi_k f\). Moreover, if the translation by \(\beta\) has a dense orbit and \(\Delta_L(\beta,\lambda)<2\), **these and their unimodular scalar multiples are all the minimizers**.

For a one-dimensional irrational rotation and \(\lambda=-1\), the sharp defect is strictly positive for every finite \(L\), but tends to zero as \(L\to\infty\); no continuous torsion exactly anticommutes with that rotation. Thus the cost of approximating a forbidden exact torsion symmetry is an explicit finite Diophantine minimum, rather than an unspecified approximation constant.

## Assumptions and scope
Here \(\operatorname{Lip}(u)=\sup_{x\ne y}|u(x)-u(y)|/d_{\mathbb T^d}(x,y)\). The infimum includes all bounded complex-linear torsions, not just multipliers stipulated in advance. No ergodicity is required for the exact formula. The dense-orbit assumption is used only to classify *all* optimizers. The unrestricted fixed-winding version of the bound also applies to continuous, not necessarily Lipschitz, circle-valued multipliers. The lattice minimum is nonempty because \(k=0\) is always feasible; \(L\) need not be integral.

## Proof
**1. Torsions are multipliers.** Let \(U\) be a torsion and put \(u=U\mathbf1\). Then \(|u(x)|=1\). If \(f(x)=0\), the torsion identity gives \((Uf)(x)=0\). Apply this to \(f-f(x)\mathbf1\): one gets \((Uf)(x)=u(x)f(x)\) for every \(x\). Hence \(U=M_u\), with \(u\) continuous and circle-valued. Conversely every such multiplier is a torsion. Since translation is an invertible isometry,
\[
\|T_\beta M_u-\lambda M_uT_\beta\|
=\max_{x\in\mathbb T^d}|u(x+\beta)-\lambda u(x)|.
\]

**2. Winding class and Lipschitz budget.** Each continuous \(u:\mathbb T^d\to\mathbb T\) has a unique integer winding vector \(k\in\mathbb Z^d\) and a real-valued continuous periodic \(h\) such that
\[
u(x)=\exp\!\big(i(\langle k,x\rangle+h(x))\big).
\]
Indeed, lift the circle map along \(\mathbb R^d\to\mathbb T^d\); the lift changes by \(2\pi k_j\) under translation by \(2\pi e_j\), and subtracting \(\langle k,x\rangle\) leaves a periodic real function. If \(u\) is Lipschitz, local real phase lifts are Lipschitz, hence the a.e. phase gradient \(k+\nabla h\) has Euclidean norm at most \(\operatorname{Lip}(u)\). Periodicity gives \(\int\nabla h\,dm=0\) for normalized Haar measure \(m\). Therefore
\[
\|k\|_2=\Big\|\int_{\mathbb T^d}(k+\nabla h)\,dm\Big\|_2
\le\int_{\mathbb T^d}\|k+\nabla h\|_2\,dm
\le\operatorname{Lip}(u).
\]
The character \(\chi_k(x)=e^{i\langle k,x\rangle}\) has Lipschitz seminorm exactly \(\|k\|_2\), by the elementary chordal upper bound and its directional derivative. Thus precisely the lattice vectors of Euclidean norm at most \(L\) can occur under the budget, and every one of them is realized by a character.

**3. Optimal defect within a winding class.** Write \(\lambda=e^{it}\), and for the winding decomposition above put
\[
F(x)=\langle k,\beta\rangle-t+h(x+\beta)-h(x),
\qquad D=\max_x|e^{iF(x)}-1|.
\]
By translation invariance of Haar measure, \(\int F\,dm=\langle k,\beta\rangle-t\). If \(D=2\), the desired lower bound is immediate. Otherwise choose \(0\le\vartheta<\pi\) so that \(D=2\sin(\vartheta/2)\). Every \(F(x)\) belongs to one of the disjoint closed intervals \([2\pi j-\vartheta,2\pi j+\vartheta]\), for \(j\in\mathbb Z\). Since the torus is connected and \(F\) is continuous, its entire image belongs to **one** such interval. Its Haar average belongs to that interval too. Consequently
\[
\big|e^{i\langle k,\beta\rangle}-\lambda\big|
=\big|e^{i\int F\,dm}-1\big|
\le D.
\]
The character \(\chi_k\) realizes equality because its phase lift has \(h=0\). Combining this sharp fixed-class inequality with step 2 proves the asserted finite minimum and attainment.

**4. Equality and rigidity.** Suppose the translation has a dense orbit, and an admissible multiplier of winding \(k\) attains \(\Delta_L<2\). Step 3 implies that \(k\) is a minimizing lattice vector and equality holds in its fixed-class bound. With \(\vartheta=2\arcsin(\Delta_L/2)<\pi\), the mean of \(F\) lies at an endpoint of the common interval \([2\pi j-\vartheta,2\pi j+\vartheta]\) (or the interval is a singleton when \(\vartheta=0\)). A continuous real function bounded in that interval and having its mean at an endpoint is constant. Hence \(h(x+\beta)-h(x)=0\) for all \(x\). A continuous function invariant under a dense translation orbit is constant. Thus \(u\) is a unimodular scalar multiple of \(\chi_k\), as claimed.

**5. Forbidden exact anticommutation and approximation.** In dimension one, let \(\beta/(2\pi)\) be irrational. For each integer \(k\), the value \(e^{ik\beta}\) differs from \(-1\), so the finite lattice minimum for \(\lambda=-1\) is positive. A continuous torsion with zero defect would also have a winding vector \(k\) and violate the fixed-class lower bound of step 3. On the other hand, the powers \(\{e^{ik\beta}:k\in\mathbb Z\}\) are dense in the unit circle, so their distance to \(-1\) has infimum zero. Characters with increasing winding and finite Lipschitz seminorm witness convergence of \(\Delta_L\) to zero as \(L\to\infty\). This proves the final assertion.

## Verification
The argument uses exact identities and does not infer infinite statements from finite experiments. The included self-contained `CHECK.py` enumerates feasible character frequencies at several Lipschitz budgets and tests the fixed-class lower bound against explicit nonconstant periodic phase perturbations on dense finite grids in dimensions one and two. Its purpose is to detect sign, normalization, and indexing errors; it is **not** a replacement for the integral and connectedness arguments in steps 2–4. The metric normalization is fixed by the \(2\pi\)-periodic torus and Euclidean geodesic distance, so character Lipschitz seminorms are exactly \(\|k\|_2\), without a hidden \(2\pi\) factor.

## Relationship to prior work
Dobrick's *On the Cyclicity Conjecture* (arXiv:2610.10093v1, first posted October 7, 2026), Example 3.2, treats the irrational circle rotation on \(C(\mathbb T)\) and proves that no torsion exactly anticommutes with it. Sections 3 and Appendix A introduce the relevant torsions and approximate intertwining mechanism. Unlike the paper's asymptotically self-similar minorants, whose torsion is held fixed while the positive minorant varies, the approximations here keep the translation fixed and allow the torsion multiplier to vary with its complexity budget. The present statement does **not** reprove the cyclicity conjecture; it determines a different sharp optimization: the operator-norm defect under a natural Lipschitz budget, in every torus dimension, including a classification of all optimizers below the trivial diameter bound. The use of winding classes, Haar averaging, and characters is classical, and the unrestricted density of rotation eigenvalues is not asserted as new. Exel’s 1992 study of soft-torus commutator norms addresses general unitary-pair perturbations and finite-dimensional local minima, rather than a **fixed torus Koopman translation** with a Lipschitz-constrained multiplication torsion. Hua–Lin’s 2014 preprint proves the Exel trace formula and rotation-relation stability for unitaries in \(C^*\)-algebras; its Bott/trace obstruction can motivate the phase-average lower bound, but does not specify the metric regularity budget, characterize the exact best error over all winding sectors, or classify the constrained optimizers. These prior structural obstructions are acknowledged, not claimed as new.

## Limitations
The result concerns translations on \(C(\mathbb T^d)\), not arbitrary positive operators or arbitrary Banach lattices. It does not provide uniform rates of approximation as \(L\to\infty\): those depend on the arithmetic of the translation. Optimizer rigidity assumes dense translation orbit and defect strictly less than \(2\), and is not claimed at the degenerate boundary \(2\). The originality comparison can miss unindexed classical cocycle or topological-eigenfunction literature; no independent validation is claimed.

## References
1. Alexander Dobrick, *On the Cyclicity Conjecture*, arXiv:2610.10093v1, publicly submitted 2026-10-07. Relevant parts: Example 3.2, Remark 3.3, Proposition 3.4, Appendix A. https://arxiv.org/html/2610.10093v1
2. Ruy Exel, *The Soft Torus II: A Variational Analysis of Commutator Norms*, arXiv:funct-an/9212004v1, 1992, especially §§4–5 on dilated perturbations and finite-dimensional local minima. https://arxiv.org/pdf/funct-an/9212004
3. Jiajie Hua and Huaxin Lin, *Rotation algebras and Exel trace formula*, arXiv:1308.4775v3, 2014, especially Theorem 3.7 and §§4–5. https://arxiv.org/pdf/1308.4775
4. Classical facts used with explanations in the proof: circle-valued maps on a torus are classified by their integral winding vectors; Haar measure is translation invariant; powers of an irrational circle rotation are dense.

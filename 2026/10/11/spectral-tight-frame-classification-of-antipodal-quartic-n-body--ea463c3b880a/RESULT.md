# Spectral tight-frame classification of antipodal quartic N-body oscillations

## Finding
Fix integers \(d\ge2\) and \(m\ge d\). Consider \(2m\) labeled particles in \(\mathbb R^d\), with a positive mass \(\mu_j\) at each of the two initially antipodal positions \(\pm v_j\) for \(1\le j\le m\). Assume that the vectors \(v_j\ne0\) span \(\mathbb R^d\), and that all \(2m\) initial positions are distinct. Their accelerations are given by the attractive quartic force law
\[
\ddot q_\ell=\sum_{k\ne\ell}m_k(q_k-q_\ell)\lVert q_k-q_\ell\rVert^2.
\]
There is a common scalar function \(a(t)\) for which the zero-initial-velocity solution is \(q_{j,\pm}(t)=\pm a(t)v_j\) **if and only if** the following weighted tight-frame structure holds.

There is an orthogonal decomposition \(\mathbb R^d=E_1\oplus\cdots\oplus E_h\), \(1\le h\le d\), together with a partition of the pair indices into nonempty sets \(J_a\), such that \(v_j=r_au_j\in E_a\) for each \(j\in J_a\). Write \(d_a=\dim E_a\), \(W_a=\sum_{j\in J_a}\mu_j\), and \(M=2\sum_{j=1}^{m}\mu_j\). The unit vectors \(u_j\) satisfy the weighted tight-frame identities
\[
\sum_{j\in J_a}\mu_j u_ju_j^{\mathsf T}=\frac{W_a}{d_a}\operatorname{Id}_{E_a},
\qquad\lVert u_j\rVert=1,
\]
and, for a **single** constant \(C>0\) independent of \(a\), the radii obey
\[
\boxed{\quad r_a^2=\frac{C}{M+4W_a/d_a}.\quad}
\]
Conversely, every such weighted orthogonal tight-frame assembly with distinct antipodal positions yields a common scalar trajectory. The canonical decomposition is obtained by grouping vectors in the distinct eigenspaces of the second-moment operator; any decomposition with repeated values of \(W_a/d_a\) may be coarsened accordingly.

Define
\[
S=2\sum_{j=1}^m\mu_jv_jv_j^{\mathsf T},\qquad I=\operatorname{tr}S,\qquad\Lambda=I+C>0.
\]
For these and only these configurations, the common scale satisfies \(a''=-\Lambda a^3\), \(a(0)=1\), \(a'(0)=0\). It is a nonconstant **globally smooth periodic** solution, with least **labeled** period
\[
\boxed{\quad T=\sqrt{\frac{2}{\Lambda}}\,B\!\left(\frac14,\frac12\right),\quad}
\]
where \(B\) is Euler's beta function. All particles pass simultaneously through the origin at \(T/4\) and again at \(3T/4\); the force is polynomial, so these collision instants do not prevent the smooth continuation of the stated model.

In particular, there are at most \(d\) distinct initial pair radii, and this bound is sharp. In the minimal spanning case \(m=d\), the directions must be mutually orthogonal, and for **every** prescribed vector of positive pair masses the sole antipodal shape up to rotation and common scaling is
\[
\boxed{\quad v_j=\sqrt{\frac{C}{M+4\mu_j}}\,e_j\quad(1\le j\le d),\quad}
\]
for an orthonormal basis \((e_j)\). Distinct pair masses give distinct radii.

## Assumptions and scope
The interaction is exactly the positive-quartic polynomial potential, with attraction as in the acceleration formula; it is **not** Newtonian inverse-square gravitation. Every pair has equal masses at its two antipodes, but masses may differ from pair to pair. The initial configuration is collision-free, spans the ambient space, and has no central particle. The resulting trajectory is labeled and passes through total collisions, which are nonsingular for this polynomial force. We classify homothetic trajectories beginning at rest, not every motion or every central configuration of the model without antipodal symmetry. The statement includes arbitrary finite \(d\ge2\) and \(m\ge d\), not only planar rhombi.

## Proof
**1. Exact quartic moment identity.** Denote all \(2m\) labeled positions by \(x_k\) and their masses by \(m_k\). Antipodality makes both odd moments zero:
\[
\sum_km_kx_k=0,\qquad \sum_km_k\lVert x_k\rVert^2x_k=0.
\]
Set \(S=\sum_km_kx_kx_k^{\mathsf T}\), \(I=\sum_km_k\lVert x_k\rVert^2=\operatorname{tr}S\), \(M=\sum_km_k\). Expanding the cubic vector kernel \((y-x)\lVert y-x\rVert^2\) and using the two vanishing moments gives, for every \(x\in\mathbb R^d\),
\[
\sum_km_k(x_k-x)\lVert x_k-x\rVert^2
=-\bigl(I+M\lVert x\rVert^2\bigr)x-2Sx.
\]
Including \(k\) with \(x_k=x\) is harmless because its summand vanishes. This identity is exact, with no limiting or averaging assumptions.

**2. Necessity and the spectral partition.** The trajectory can remain a common scalar multiple of the configuration only if its acceleration at \(t=0\) is a common scalar multiple, say \(-\Lambda v_j\), at every \(v_j\). By the identity,
\[
\bigl(2S+M\lVert v_j\rVert^2\operatorname{Id}\bigr)v_j=Cv_j,
\qquad C=\Lambda-I.
\]
Since each \(v_j\ne0\), every \(v_j\) is an eigenvector of the real symmetric positive-definite operator \(S\). Group the indices by distinct eigenvalues \(s_a\), with eigenspace \(E_a\). The vectors span \(\mathbb R^d\), so these groups span their respective eigenspaces and exhaust the orthogonal spectral decomposition. For each group the displayed equation forces the same radius \(r_a\), satisfying \(Mr_a^2+2s_a=C\). Writing \(v_j=r_au_j\) and restricting \(S\) to \(E_a\) yields
\[
2r_a^2\sum_{j\in J_a}\mu_ju_ju_j^{\mathsf T}
=s_a\operatorname{Id}_{E_a}.
\]
Taking traces gives \(s_a d_a=2r_a^2W_a\). Hence the tight-frame identity and \(C=(M+4W_a/d_a)r_a^2>0\), proving the stated radius law and at most \(d\) different radii. This also shows that the distinct spectral classes have distinct \(W_a/d_a\), as \(s_a=2CW_a/(d_aM+4W_a)\) is strictly increasing in that ratio.

**3. Sufficiency.** Conversely choose the stated orthogonal blocks, unit-norm weighted tight frames, and radii. Direct substitution yields
\[
S\big|_{E_a}=\frac{2W_ar_a^2}{d_a}\operatorname{Id}_{E_a},
\qquad M r_a^2+\frac{4W_ar_a^2}{d_a}=C.
\]
Thus every initial force is \(-(I+C)v_j\) or its negative at the opposite particle, for the same \(\Lambda=I+C\). Homogeneity of degree three in the positions implies that the ansatz \(q_{j,\pm}(t)=\pm a(t)v_j\) solves the full finite system whenever \(a''=-\Lambda a^3\). Uniqueness of solutions of the globally smooth polynomial vector field shows that this is precisely the zero-initial-velocity motion.

**4. Oscillation and least period.** The scalar energy identity is
\[
\frac12(a')^2+\frac{\Lambda}{4}a^4=\frac{\Lambda}{4},
\qquad (a')^2=\frac\Lambda2(1-a^4).
\]
The solution decreases from \(1\) to \(0\) in
\[
Q=\sqrt{\frac2\Lambda}\int_0^1\frac{du}{\sqrt{1-u^4}}
=\frac14\sqrt{\frac2\Lambda}\,B\!\left(\frac14,\frac12\right).
\]
It reaches \(-1\) after \(2Q\) and \(1\) with zero velocity again after \(4Q\). Uniqueness and monotonicity between successive turning points give least scalar period \(4Q\); because all initial \(v_j\ne0\), the labeled particle trajectory has the same least period. In contrast with singular Newtonian forces, collisions at odd multiples of \(Q\) are regular points of this polynomial vector field.

**5. Minimal antipodal spanning systems.** If \(m=d\), the \(d\) vectors \(v_j\) form a basis. For the spectral partition found in Step 2, each block has exactly \(d_a\) unit directions. The corresponding square matrix with columns \(\sqrt{d_a\mu_j/W_a}\,u_j\) has product with its transpose equal to identity, so is orthogonal. Hence the \(u_j\) are mutually orthogonal and all weights are equal within any repeated-eigenvalue block. Combining the blocks, all \(v_j\) are orthogonal; setting \(E_j=\mathbb Re_j\) in the converse construction gives \(r_j^2=C/(M+4\mu_j)\). It is the only such shape modulo orthogonal transformations and a common positive scale. Choosing distinct \(\mu_j\) exhibits \(d\) distinct radii, attaining the upper bound.

## Verification
A standalone symbolic checker, `checker.py`, evaluates the full \(2m\)-particle force sum and independently checks the spectral identity and common multiplier. It exercises 201 exact symbolic cross-polytope mass examples in dimensions two through five, one non-cospherical three-dimensional example with a planar weighted trine and a normal pair, and a high-accuracy numerical integration of the smooth scalar oscillator against the beta-function formula. Execute `python checker.py` with `sympy`, `numpy`, `scipy`, and `mpmath` installed. These finite diagnostics do not prove the arbitrary-dimensional equivalence; Steps 1–5 do.

For example, in \(\mathbb R^2\) with pair masses \(\mu_1=1\), \(\mu_2=2\), and \(C=1\), the two squared radii are \(1/10\) and \(1/14\), and \(\Lambda=52/35\). They are unequal, so this central configuration cannot follow from a theorem requiring all particles on one sphere.

## Relationship to prior work
Nurowski, arXiv:2610.04136v1 (October 2, 2026), proves that a positive weighted spherical design on **one common sphere** gives a central configuration for positive even-power potentials (Theorem 1.3) and develops the general homothetic scalar reduction (Section 2). These establish important prior mechanisms, but do not themselves supply the necessary-and-sufficient spectral block classification with **unequal radii** given here; the oscillator reduction is not claimed to be new. Nurowski also analyzes cross-polytope designs (Section 5).

Santos and da Silva, arXiv:2508.02918v1, classify several **nested regular polyhedral** central configurations using symmetry-adapted representations under the **Newtonian** interaction. Leandro, DOI:10.1007/s10884-018-9687-6, treats the four-body **rhombus** under general homogeneous forces; planar four-body specialization of the minimal-block construction is therefore not claimed as a new stand-alone fact. The present statement concerns arbitrary dimensions and arbitrary antipodal spanning systems, whose complete spectral tight-frame characterization is not implied by a four-body rhombus classification.

## Limitations
The proof does not classify general nonsymmetric quartic configurations, collisions under a singular force law, or stability of the periodic orbits. Tight-frame existence for a proposed mass partition remains an explicit geometric condition, rather than an asserted classification of all realizable frames by weights alone. The historical rhombus literature is particularly close at four bodies; its complete publisher text was not available for review. An equivalent high-dimensional block-frame formulation in older literature remains possible, so mathematical priority is not independently certified. All assertions here concern the stated polynomial force law and exact antipodal symmetry.

## References
1. P. Nurowski, *Continuous Families of Central Configurations for Even-Power Homogeneous Potentials*, arXiv:2610.04136v1, first submitted 2026-10-02, https://arxiv.org/abs/2610.04136.
2. M. P. Santos and L. D. da Silva, *Decomposition of Symmetrical Classes of Central Configurations*, arXiv:2508.02918v1, https://arxiv.org/abs/2508.02918.
3. E. S. G. Leandro, *Structure and Stability of the Rhombus Family of Relative Equilibria under General Homogeneous Forces*, Journal of Dynamics and Differential Equations 31 (2019), 933–958, DOI:10.1007/s10884-018-9687-6.
4. R. Moeckel, *Central Configurations*, Scholarpedia 9(4):10667 (2014), DOI:10.4249/scholarpedia.10667.

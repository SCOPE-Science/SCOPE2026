# Prescribed countable Fréchet-smoothness defects with hereditary Mazur intersection property

## Finding

Let \(H\) be a real separable infinite-dimensional Hilbert space, with reference norm \(\|\cdot\|_2\). Let \(E\) be any nonempty finite or countably infinite set of distinct unoriented unit directions \([u]=\{u,-u\}\), where \(\|u\|_2=1\). There exists an equivalent norm \(P\) on \(H\) such that:

1. \(P\) is Gâteaux differentiable on \(H\setminus\{0\}\);
2. every closed linear subspace of \((H,P)\) has the Mazur intersection property; and
3. for each nonzero \(x\in H\), \(P\) fails to be Fréchet differentiable at \(x\) if and only if \(x\) lies on one of the lines \(\mathbb Ru\) represented by \(E\).

Consequently its exceptional unit-sphere set is exactly
\[
N_P(H)=\{\,\pm u/P(u):[u]\in E\,\}.
\]
Two distinct directions give exactly four exceptional sphere points, and arbitrarily large finite even exceptional sets are obtained similarly. Choosing \(E\) countably dense in the unoriented direction space gives an equivalent smooth norm with hereditary Mazur intersection property whose non-Fréchet-smooth unit-sphere points form a **countably dense** subset of the whole unit sphere. This answers Questions 1 and 2 of Bandyopadhyay–Gothwal (2026) affirmatively, within the Hilbert renorming class.

## Assumptions and scope

All spaces and norms are real. A Banach space has the Mazur intersection property (MIP) when every closed bounded convex set equals the intersection of all closed balls containing it. Hereditary MIP means the induced norm on every closed linear subspace has MIP. Gâteaux and Fréchet differentiability of a norm are considered at nonzero vectors. The set \(E\) contains distinct lines rather than oriented points, as symmetry of a norm always forces antipodal exceptional points.

We use two established inputs: Borwein–Fabian's 1993 Theorem 4 provides on \(H\) an equivalent Gâteaux-smooth norm \(q\) with precisely one exceptional nonzero line; Bandyopadhyay–Gothwal's 2026 Theorems 2 and 6 give, respectively, a sufficient norming-functional density criterion for MIP and hereditary MIP for smooth norms with finite Fréchet-exception sets. The proof below records the transfer argument needed for an infinite countable set; it is not inferred from Theorem 6 alone.

## Proof

**1. Rotated one-line norms.** Fix the Borwein–Fabian norm \(q\) and a reference Hilbert-unit vector \(e\) spanning its unique exceptional line. Choose constants \(0<m\le M<\infty\) so that
\[
m\|x\|_2\le q(x)\le M\|x\|_2\qquad (x\in H).
\]
Enumerate \(E\) as \(\{[u_j]\}_{j\in I}\), with \(I=\{1,\ldots,k\}\) or \(I=\mathbb N\). For each \(j\), choose a surjective Hilbert isometry \(U_j:H\to H\) satisfying \(U_ju_j=e\), and put \(q_j(x)=q(U_jx)\). Then \(q_j\) is Gâteaux smooth at every nonzero vector, its precise set of non-Fréchet-smooth nonzero vectors is \(\mathbb Ru_j\setminus\{0\}\), and the same constants \(m,M\) bound every \(q_j\).

Choose positive weights \(w_j\) adding to one: take \(w_j=1/k\) in the finite case and \(w_j=2^{-j}\) for \(I=\mathbb N\). Define
\[
P(x)=\sum_{j\in I}w_jq_j(x).
\]
This is an equivalent norm with \(m\|x\|_2\le P(x)\le M\|x\|_2\). On each nonzero \(x\), the directional derivative series converges uniformly on the Hilbert unit ball because \(\|Dq_j(x)\|_{2,*}\le M\). Passing the directional derivative through the summable series shows that \(P\) is Gâteaux differentiable with \(DP(x)=\sum_jw_jDq_j(x)\).

**2. Exact non-Fréchet locus.** For a Gâteaux-differentiable norm \(s\), define its nonnegative convexity remainder
\[
R_s(x,h)=s(x+h)-s(x)-Ds(x)h\ge0.
\]
For \(s=q_j\), its Lipschitz bound gives \(0\le R_{q_j}(x,h)\le2M\|h\|_2\). The identity
\[
R_P(x,h)=\sum_jw_jR_{q_j}(x,h)
\]
holds at every nonzero \(x\). If all \(q_j\) are Fréchet differentiable at \(x\), each remainder is \(o(\|h\|_2)\); split the sum into finitely many terms and a uniformly bounded tail to conclude \(R_P(x,h)=o(\|h\|_2)\). Conversely, if some \(q_j\) is not Fréchet differentiable at \(x\), nonnegativity and \(R_P(x,h)\ge w_jR_{q_j}(x,h)\) rule out Fréchet differentiability of \(P\). Thus the exceptional nonzero locus of \(P\) is exactly \(\bigcup_j(\mathbb Ru_j\setminus\{0\})\). This proves the finite and countable classification of the defect set, not merely one inclusion.

**3. Finite case.** If \(I\) is finite, the exceptional unit-sphere set is finite and \(P\) is Gâteaux smooth. Theorem 6 of Bandyopadhyay–Gothwal therefore gives hereditary MIP. The remaining steps establish hereditary MIP when \(I=\mathbb N\); finiteness alone cannot justify that conclusion.

**4. Finite-head norms and uniform derivative control.** For \(N\ge1\), set \(t_N=\sum_{j>N}w_j=2^{-N}\) and define
\[
Q_N(x)=\sum_{j=1}^Nw_jq_j(x)+t_N\|x\|_2.
\]
As above, \(Q_N\) is Gâteaux smooth and its Fréchet-nonsmooth nonzero locus consists exactly of the first \(N\) exceptional lines. Every \(Q_N\) therefore has hereditary MIP by the cited Theorem 6. Its proof, through the Bishop–Phelps theorem, gives the stronger assertion that for every closed subspace \(Y\subset H\) of dimension at least two, the normalized support functionals at Fréchet-smooth points of the restricted norm \(Q_N|_Y\) are norm dense in the dual unit sphere of \((Y,Q_N|_Y)^*\). Equivalently, this follows by removing the finite set of support functionals at bad points from the dual sphere before applying Bishop–Phelps; all the restrictions \(Q_N|_Y\) remain Gâteaux smooth.

Uniformly for \(x\in H\),
\[
|P(x)-Q_N(x)|\le (M+1)t_N\|x\|_2,
\]
and, uniformly for nonzero \(x\in H\),
\[
\|DP(x)-DQ_N(x)\|_{2,*}\le (M+1)t_N.
\]
The derivative bound follows by comparing the tail sum \(\sum_{j>N}w_jDq_j(x)\) with \(t_ND\|\cdot\|_2(x)\). All \(P,Q_N\) are uniformly equivalent to \(\|\cdot\|_2\), with positive lower bound \(\min\{m,1\}\) and upper bound \(\max\{M,1\}\).

**5. Passing dense Fréchet-smooth support functionals to the limit.** Fix a closed subspace \(Y\subset H\) of dimension at least two and a functional \(f\) of dual \(P|_Y\)-norm one. Given \(\varepsilon>0\), take \(N\) sufficiently large that \(t_N\) is small compared with \(\varepsilon\). Uniform equivalence and the displayed primal bound imply \(\|f\|_{(Q_N|_Y)^*}\to1\); after rescaling, \(f_N=f/\|f\|_{(Q_N|_Y)^*}\) lies in the \(Q_N\)-dual unit sphere and \(\|f_N-f\|_{2,*}\to0\).

By the finite-head density assertion, choose a nonzero \(y\in Y\) at which \(Q_N|_Y\) is Fréchet differentiable and whose normalized derivative \(DQ_N(y)|_Y\) is within \(\varepsilon/4\), in the reference dual Hilbert norm, of \(f_N\). Because Fréchet differentiability of a convex norm at \(y\) is equivalent to norm-to-norm continuity of its unique supporting derivative there, \(DQ_N(\cdot)|_Y\) is continuous at \(y\). The countable union \(\bigcup_{j\ge1}\mathbb Ru_j\cap Y\) has dense complement in \(Y\): each included line is a closed nowhere-dense subset of \(Y\), and \(Y\) is complete with dimension at least two. Consequently choose \(z\in Y\setminus\bigcup_j\mathbb Ru_j\) arbitrarily near \(y\) with
\[
\|DQ_N(z)|_Y-DQ_N(y)|_Y\|_{2,*}<\varepsilon/4.
\]
The exact defect-locus calculation shows that \(P\) is Fréchet differentiable at \(z\); hence \(P|_Y\) is Fréchet differentiable there. The uniform derivative estimate now yields
\[
\|DP(z)|_Y-f\|_{2,*}\le (M+1)t_N+\varepsilon/2+\|f_N-f\|_{2,*}<\varepsilon
\]
for sufficiently large \(N\). Here \(DP(z)|_Y\) is automatically a norm-one functional for the dual of \(P|_Y\). Thus the Fréchet-smooth-point support functionals of \(P|_Y\) are dense in its dual unit sphere. Theorem 2(a) of Bandyopadhyay–Gothwal implies \((Y,P|_Y)\) has MIP. One-dimensional subspaces are automatically MIP. Since \(Y\) was arbitrary, \((H,P)\) has hereditary MIP.

**6. Density example.** Let \(\{[u_j]\}\) be a countable dense subset of the unoriented Hilbert-unit-direction space. Radial normalization \(v\mapsto v/P(v)\) is a homeomorphism from the Hilbert unit sphere onto the \(P\)-unit sphere, so the exceptional points \(\{\pm u_j/P(u_j)\}\) are countably dense there. They are all and only the Fréchet-nonsmooth unit vectors.

## Verification

This is an analytic proof. The crucial independent checks are: positivity of each convexity remainder; a common dimension-free Lipschitz majorant that justifies summation and exactness of the defect union; the finite-head norm \(Q_N\) having only finitely many bad lines; uniform \(O(2^{-N})\) control of both norms and derivatives; the Bishop–Phelps density argument for finite bad sets; and the Baire-category perturbation avoiding every exceptional line. The proof works for any countable family, even one dense in the projective unit sphere. No numerical experiment or finite truncation is used as a substitute for the countably infinite conclusion.

## Relationship to prior work

Borwein and Fabian (1993, Theorem 4) construct an equivalent smooth norm with just one exceptional antipodal pair on WCG Asplund spaces. Bandyopadhyay and Gothwal (2026, Theorem 6) prove hereditary MIP when the smooth norm has a *finite* exceptional set and explicitly ask whether this set can have more than two points and whether hereditary MIP permits an *infinite* exceptional set (Questions 1 and 2). The present countable-superposition and approximation argument produces prescribed exceptional sets of either cardinality, including countably dense examples. Neither cited theorem by itself implies the infinite case: it requires the uniform derivative approximation and perturbation step above. The earlier one-line construction and the finite-exception MIP criterion are used as credited inputs, not claimed as new results.

## Limitations

The construction is proved for real separable infinite-dimensional Hilbert spaces and countable collections of unoriented directions. It does not establish a universal preservation theorem for arbitrary sums of MIP norms, prescribe uncountably many singular directions, or give quantitative MIP moduli. The choice of the Borwein–Fabian base norm is noncanonical; the theorem is an existence statement with a defined norm series. Its novelty comparison is limited by the availability of some older broad renorming literature and an inaccessible full 2025 doctoral thesis, which could contain an implicit special case.

## References

1. P. Bandyopadhyay and D. Gothwal, *A short note on hereditary Mazur intersection property*, arXiv:2602.17153v1, first public 19 February 2026; especially Theorems 2 and 6, Questions 1 and 2. https://arxiv.org/html/2602.17153
2. J. M. Borwein and M. Fabian, *On convex functions having points of Gateaux differentiability which are not points of Fréchet differentiability*, Canadian Journal of Mathematics 45 (1993), 1121–1134, Theorem 4, DOI:10.4153/CJM-1993-062-8.
3. D. Gothwal, *Mazur’s Intersection Property and its Variants*, doctoral thesis, Indian Statistical Institute (2025), abstract and public bibliographic record, https://digitalcommons.isical.ac.in/doctoral-theses/628/.

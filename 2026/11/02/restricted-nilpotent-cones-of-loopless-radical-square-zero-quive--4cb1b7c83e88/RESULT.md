# Restricted nilpotent cones of loopless radical-square-zero quiver algebras

## Finding

Let \(Q\) be any finite loopless directed multiquiver (oriented cycles, isolated vertices, and parallel arrows are allowed), let \(k=\mathbb F_q\) have characteristic \(p\), and let \(A=kQ/J^2\), where \(J\) is the arrow ideal. For each class \(\alpha\) of arrows sharing ordered endpoints, write \(m_\alpha\) for its size. Fix \(e\ge1\) and put \(h=p^e\). The first Hochschild cohomology \(\mathfrak g=HH^1(A)\) has its natural restricted power, and the height-\(e\) nilpotent locus is

\[\mathcal N_e(\mathfrak g)=\{\xi\in\mathfrak g:\xi^{[p^e]}=0\}.\]

**Restricted nilcone decomposition.** Each element of \(\mathcal N_e(\mathfrak g)(k)\) has exactly one representative consisting of a tuple \((N_\alpha)_\alpha\) of matrices satisfying \(N_\alpha^h=0\). In particular, there is a bijection

\[\mathcal N_e(\mathfrak g)(k)\longleftrightarrow\prod_\alpha\{N\in M_{m_\alpha}(k):N^h=0\}.\]

It holds over every perfect field \(k\) of characteristic \(p\), not only finite fields. Consequently the complete finite-field count is

\[\boxed{\#\mathcal N_e(\mathfrak g)(\mathbb F_q)=\prod_\alpha\mathcal J_{m_\alpha,h}(q),}\]

where \(\mathcal J_{0,h}(q)=1\), and for \(m\ge1\),

\[\mathcal J_{m,h}(q)=\sum_{\substack{\lambda\vdash m\\\lambda_1\le h}}\frac{|\mathrm{GL}_m(\mathbb F_q)|}{q^{\sum_j(\lambda'_j)^2}\displaystyle\prod_{d\ge1}\prod_{i=1}^{m_d(\lambda)}(1-q^{-i})}.\]

Here \(\lambda'\) is the conjugate partition and \(m_d(\lambda)\) is the multiplicity of a part \(d\). The summands are integers (cardinalities of nilpotent conjugacy classes). The formula counts **outer derivation classes**, not all derivations. Its value depends only on the multiset of parallel-arrow multiplicities, and not on incidence, orientations, cycles, or the number of isolated vertices, so long as there are no loops.

**Geometry.** Over an algebraic closure, the *reduced* algebraic set \(\mathcal N_e(\mathfrak g)_{\mathrm{red}}\) is geometrically irreducible. Write \(m_\alpha=a_\alpha h+r_\alpha\), with \(0\le r_\alpha<h\). Then

\[\boxed{\dim\mathcal N_e(\mathfrak g)_{\mathrm{red}}=\sum_\alpha\left[m_\alpha^2-r_\alpha(a_\alpha+1)^2-(h-r_\alpha)a_\alpha^2\right].}\]

If no parallel-arrow class has size at least two, the restricted nilcone consists of the zero class. Otherwise it contains nonzero classes. The exact number of classes having *minimal* nilpotence height \(e\ge1\) is \(\prod_\alpha\mathcal J_{m_\alpha,p^e}(q)-\prod_\alpha\mathcal J_{m_\alpha,p^{e-1}}(q)\), with \(\mathcal J_{m,1}(q)=1\); the zero class is counted separately. All classes have height at most \(\lceil\log_p(\max_\alpha m_\alpha)\rceil\) when an arrow exists.

**Graph-topology contrast.** A three-edge-class tree with multiplicities \((2,1,1)\) and a directed triangle with the same multiplicities have first Hochschild cohomology dimensions \(3\) and \(4\), respectively, yet both have exactly \(q^2\) restricted-height-one nilpotent classes, in every positive characteristic. The cycle contributes a toral direction but no extra restricted-nilpotent class.

## Assumptions and scope

The quiver is finite and has no loops, but need not be acyclic or connected. All assertions about rational point counts use a finite field \(\mathbb F_q\), with characteristic \(p\); the uniqueness statement extends to perfect fields. The irreducibility and dimension statements are for reduced varieties after extension to an algebraic closure. An empty product is \(1\), yielding the correct zero-dimensional statement for an arrowless quiver. No identification of the potentially nonreduced equation scheme or isomorphism of reduced varieties with the matrix product is asserted.

## Proof

**1. Derivation classes as a central quotient.** Let \(e_v\) denote the primitive vertex idempotents and \(E=\bigoplus_v ke_v\). Given a derivation \(D:A\to A\), set \(w=\sum_vD(e_v)e_v\). The idempotent Leibniz relations show \([w,e_v]=D(e_v)\), so replacing \(D\) by \(D-\operatorname{ad}_w\) gives \(D(e_v)=0\) for every vertex. Such a derivation must map each arrow to a linear combination of parallel arrows, because it preserves the endpoint corners and all paths of length two vanish. Conversely every tuple of arbitrary endomorphisms on the parallel-arrow spaces defines a derivation. An inner derivation that fixes all vertices comes from an element commuting with \(E\); as \(Q\) has no loops, this element is a linear combination of the \(e_v\). Consequently,

\[HH^1(A)\cong\left(\bigoplus_\alpha M_{m_\alpha}(k)\right)\Big/\left\{\big((t_{t(\alpha)}-t_{s(\alpha)})I_{m_\alpha}\big)_\alpha:t_v\in k\right\}.\]

The denominator \(U\) is a linear subspace of the scalar matrices in the respective blocks. Its dimension is the number of vertices minus the number of connected components of the underlying undirected graph.

**2. The restricted power.** In characteristic \(p\), the \(p\)-fold composition of a derivation is again a derivation. On a vertex-fixing representative whose block matrices are \((M_\alpha)\), the restricted \(p^e\)-power is represented by \((M_\alpha^{p^e})\). This is well-defined modulo inner derivations: in general the \(p\)-power of a derivation class is induced from composition, and here the scalar gauge matrices commute blockwise with everything, so the formula also follows directly from the freshman's-dream identity.

Thus the class is killed by \(p^e\) if and only if there is a vertex potential \((t_v)\) with

\[M_\alpha^h=(t_{t(\alpha)}-t_{s(\alpha)})I_{m_\alpha}\quad\text{for all }\alpha.\]

**3. Unique nilpotent normalization.** Since \(k\) is perfect, choose the unique \(h\)-th roots \(s_v\) of the \(t_v\). Setting \(N_\alpha=M_\alpha-(s_{t(\alpha)}-s_{s(\alpha)})I\) gives \(N_\alpha^h=0\). If two such tuples represent the same class, their difference is a vertex-potential scalar tuple; raising the corresponding block equation to the \(h\)-th power forces every scalar difference to be zero. Hence the tuples coincide. This proves the bijection and the independence of graph incidence.

**4. Finite-field and geometric consequences.** Every matrix with \(N^h=0\) has a nilpotent Jordan partition \(\lambda\vdash m\) with largest part at most \(h\). The orbit of type \(\lambda\) has size \(|\mathrm{GL}_m(\mathbb F_q)|/|C_{\mathrm{GL}_m}(J_\lambda)|\), where the centralizer order is

\[|C_{\mathrm{GL}_m}(J_\lambda)|=q^{\sum_j(\lambda'_j)^2}\prod_{d\ge1}\prod_{i=1}^{m_d(\lambda)}(1-q^{-i}).\]

Summing disjoint Jordan orbits gives \(\mathcal J_{m,h}(q)\), and multiplying over arrow classes proves the count. The nilpotent partitions with largest part at most \(h\) have a unique dominance-maximal partition \((h^a,r)\), omitting the zero remainder. The classical dominance criterion for closures of nilpotent general-linear orbits shows that its closure is exactly \(\{N:N^h=0\}_{\mathrm{red}}\). This cone is irreducible, and its dense orbit has dimension \(m^2-\sum_j(\lambda'_j)^2\), yielding the displayed expression. Finally, the projection from the product of these matrix cones to \(HH^1(A)\) is a morphism that is bijective on algebraically closed points onto the restricted nilcone (Step 3), so its fibers are zero-dimensional and it has irreducible image of the same dimension. The image equals the restricted nilcone on geometric points; taking reduced structures proves the geometric assertion. Subtraction of cumulative counts gives exact height statistics.

## Verification

The accompanying `verify.py` tests nine complete scalar-gauge quotients against separately enumerated nilpotent matrix tuples. The cases include prime fields of characteristics two and three, \(\mathbb F_4\), a cycle/tree pair with identical arrow multiplicities, and nilpotence heights \(2\), \(3\), and \(4\). A separate direct Leibniz enumeration for the two-arrow Kronecker algebra over \(\mathbb F_2\) checks all \(4\times4\) linear maps, yielding \(64\) derivations, \(8\) inner derivations, \(8\) outer classes and \(4\) restricted-square-zero classes. Seven additional enumerations compare the Jordan centralizer sum with literal matrix powers. Expected sample height-one counts are \(22\) for a three-arrow Kronecker quiver over \(\mathbb F_2\), \(4\) for the two-arrow case over \(\mathbb F_2\), and \(16\) for that case over \(\mathbb F_4\). These are finite checks, not a substitute for the proof for all quivers and fields.

## Relationship to prior work

Strametz's work on the first Hochschild cohomology of monomial algebras (first public version November 6, 2001) gives the combinatorial Lie bracket and the parallel-arrow presentation over arbitrary characteristic. Sánchez-Flores's 2010 study develops related Lie structure for radical-square-zero monomial algebras, with its reductivity results formulated in characteristic zero. Briggs and Rubio y Degrassi (2020) study the restricted Lie structure of Hochschild cohomology under stable equivalences. The present assertion concerns neither Lie reductivity nor general invariance: it computes each restricted-nilpotence-height locus and its exact finite-field cardinality, showing graph-topology independence despite topology-dependent ambient Lie dimensions. The matrix Jordan orbit formula and dominance order are classical ingredients, not claimed as new. No exhaustive publication-priority determination is asserted.

## Limitations

Loops are excluded: in small characteristic, derivations of loop algebras can contain components that do not preserve the arrow space, so the stated quotient need not apply. The exact formula is for outer derivation **classes**, not for raw derivations or conjugacy orbits. The perfect-field assumption is essential for the displayed rational-point bijection; over an imperfect field the required scalar \(h\)-th roots need not exist. The geometry concerns reduced loci, not scheme-theoretic multiplicities or tangent spaces. The uniqueness of nilpotent representatives does not by itself assert that the parameterization is an isomorphism of varieties. Mathematical correctness is supported by the proof and the stated checks; publication priority and independent audit remain open.

## References

1. C. Strametz, *The Lie algebra structure on the first Hochschild cohomology group of a monomial algebra*, arXiv:math/0111060 (first version November 6, 2001), https://arxiv.org/abs/math/0111060.
2. S. Sánchez-Flores, *On the semisimplicity of the outer derivations of monomial algebras*, arXiv:1004.2820 (first version April 16, 2010), https://arxiv.org/abs/1004.2820.
3. B. Briggs and L. Rubio y Degrassi, *Stable invariance of the restricted Lie algebra structure of Hochschild cohomology*, arXiv:2006.13871 (June 24, 2020), https://arxiv.org/abs/2006.13871.
4. M. Gerstenhaber, *On dominance and varieties of commuting matrices*, Annals of Mathematics 73 (1961), 324–348 (classical nilpotent-orbit closure theory).

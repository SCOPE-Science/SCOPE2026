# Full affine symmetry decomposition of Clebsch-neighborhood second homology

## Finding
Let \(T=\mathbb F_2^5/\langle(1,1,1,1,1)\rangle\), and let \(C\) be the five-regular folded five-cube graph with vertex set \(T\) and edges \([x]\sim[x+e_i]\) for \(0\le i<5\). Denote its ordinary Lovász **open-neighborhood** simplicial complex by \(K=\mathcal N(C)\). The full graph automorphism group is \(G=T\rtimes S_5\), of order \(1920\). The only nonzero reduced rational homology of \(K\) is \(\widetilde H_2(K;\mathbb Q)\), of dimension \(31\).

For a binary vector \(y\) of even weight, let \(\chi_y([x])=(-1)^{\langle x,y\rangle}\). Let \(V_5=S^{(3,1,1)}=\bigwedge^2\mathrm{Std}_5\), the six-dimensional irreducible rational representation of \(S_5\). Let \(J_2=T\rtimes(S_2\times S_3)\) be the stabilizer of \(\chi_{e_0+e_1}\), and \(J_4=T\rtimes S_4\) the stabilizer of \(\chi_{e_0+e_1+e_2+e_3}\), where \(S_4\) fixes the fifth coordinate. Write \(\varepsilon_j\) for the sign representation of \(S_j\), and \(\mathrm{Std}_4\) for the standard three-dimensional representation of \(S_4\). Then the **full rational group representation** is

\[
\boxed{\begin{aligned}
\widetilde H_2(K;\mathbb Q)\cong_{\mathbb Q[G]}
&\operatorname{Inf}_{S_5}^{G} V_5\\
&\oplus \operatorname{Ind}_{J_2}^{G}\bigl(\chi_{e_0+e_1}\otimes(\mathbf1_{S_2}\boxtimes\varepsilon_3)\bigr)\\
&\oplus \operatorname{Ind}_{J_4}^{G}\bigl(\chi_{e_0+e_1+e_2+e_3}\otimes(\varepsilon_4\otimes\mathrm{Std}_4)\bigr).
\end{aligned}}
\]

The three summands are pairwise nonisomorphic, **irreducible over \(\mathbb Q\)**, and have dimensions \(6,10,15\). In particular, \(\widetilde H_2(K;\mathbb Q)^G=0\), even though the subgroup of translations fixes a six-dimensional homology subspace.

## Assumptions and scope
All vector arithmetic is over \(\mathbb F_2\). The graph is the \(5\)-regular Clebsch or Greenwood–Gleason graph with strongly regular parameters \((16,5,0,2)\), **not** the complementary \(10\)-regular graph sometimes also called the Clebsch graph. The group \(S_5\) permutes the five coordinate directions; translations act by addition on quotient classes. The open-neighborhood complex has a simplex on every nonempty vertex set with a **common graph neighbor**, and does not refer to a closed-neighborhood or independence complex. The displayed decomposition is an abstract rational representation isomorphism, not an integral lattice splitting, an equivariant homotopy equivalence, or a canonical geometric splitting.

## Proof
**1. Graph and full symmetry group.** The five images of the unit vectors are distinct and sum to zero in \(T\). They generate \(T\), and the Cayley graph \(C\) has degree five. Affine maps \((t,\pi):[x]\mapsto[t+\pi x]\) preserve these generators. This embeds \(T\rtimes S_5\) as \(1920\) distinct graph automorphisms. Conversely, any automorphism fixing the zero vertex permutes its five neighbors. Every other vertex lies at distance two and is the unique common neighbor *other than zero* of a unique unordered pair of the five neighbors (the strongly regular parameter \(\mu=2\)). Hence a vertex-stabilizing automorphism is determined by the permutation of those neighbors and there are at most \(5!\) choices. Vertex transitivity then shows that the displayed affine group is the entire automorphism group.

**2. Exact chain ranks.** Choose in each antipodal class the unique five-bit representative with final bit zero, interpreted as a number in \(\{0,\ldots,15\}\). For every vertex, form its five open neighbors, and take the union of all nonempty subsets of those sixteen sets. This constructs every face of \(K\), yielding the exact face vector
\[
(f_0,f_1,f_2,f_3,f_4)=(16,80,160,80,16).
\]
Orient simplices by increasing representative number. Form integral matrices \(\partial_k\) with signed entries \((-1)^j\) for deletion of the \(j\)-th vertex. Exact rational Gaussian elimination gives
\[
\bigl(\operatorname{rank}\partial_1,\ldots,\operatorname{rank}\partial_4\bigr)
=(15,65,64,16),
\qquad \partial_{k-1}\partial_k=0.
\]
Thus the rational Betti numbers are \((1,0,31,0,0)\), and only reduced rational degree-two homology remains. The calculation uses exact rational matrix ranks, not a finite-field extrapolation. The existing stronger integral wedge-of-spheres description is credited below and not presented as a new result.

**3. Exact affine character.** For \(g=(t,\pi)\in G\), send each vertex representative \(x\) to the representative of \(t+\pi x\). The trace on the oriented \(k\)-chain group is the sum over invariant \(k\)-simplices of the sign of the permutation induced on their \(k+1\) vertices. Since reduced rational homology is concentrated in degree two, Hopf's trace formula gives
\[
\operatorname{tr}\bigl(g\mid\widetilde H_2(K;\mathbb Q)\bigr)
=\sum_{k=0}^{4}(-1)^k\operatorname{tr}(g\mid C_k(K;\mathbb Q))-1.
\]
Every term is a finite, signed integer. The accompanying independent-replay script enumerates all \(120\) coordinate permutations and all \(16\) translations (all \(1920\) elements), recomputing the signed trace directly from the \(352\) faces. The character takes value \(31\) once; values \(7,3,-5,-1,1\) respectively \(10,60,80,825,944\) times.

**4. Translation Fourier projection and inertia-group characters.** Every irreducible rational character of the elementary abelian group \(T\) is \(\chi_y\) for a unique even-weight five-bit vector \(y\). For \(\pi y=y\), the trace on the corresponding weight space is the integral Fourier average
\[
\operatorname{tr}\bigl(\pi\mid\widetilde H_2[\chi_y]\bigr)
=\frac1{16}\sum_{t\in T}\chi_y(t)\,
\operatorname{tr}\bigl((t,\pi)\mid\widetilde H_2\bigr).
\]
At identity \(\pi\), the weight multiplicities are exactly \(6\) for \(y=0\), \(1\) for each of the ten weight-two vectors, and \(3\) for each of the five weight-four vectors. These are the three \(S_5\)-orbits in the dual of \(T\), with aggregate dimensions \(6+10+15=31\).

For \(y=0\), exhaustive Fourier traces for the seven conjugacy classes of \(S_5\) agree with the character of \(\bigwedge^2\mathrm{Std}_5\): writing \(f(\pi)\) for the number of fixed coordinate positions, the common value is
\[
\frac{(f(\pi)-1)^2-(f(\pi^2)-1)}{2}.
\]
For \(y=e_0+e_1\), its stabilizer in \(S_5\) is \(S_2\times S_3\). The full Fourier table on its twelve elements is \(\mathbf1_{S_2}\boxtimes\varepsilon_3\). For \(y=e_0+e_1+e_2+e_3\), its stabilizer is \(S_4\), and all twenty-four Fourier traces equal
\[
\operatorname{sgn}(\pi)\bigl(f_4(\pi)-1\bigr),
\]
where \(f_4(\pi)\) counts fixed points in the four coordinates; this is the character of \(\varepsilon_4\otimes\mathrm{Std}_4\). An explicit conjugation check transports these stabilizer characters to every other nonzero weight.

**5. Representation reconstruction.** Over \(\mathbb Q\), the three stabilizer modules in Step 4 are irreducible: the trivial-twist sign module is one-dimensional, the sign-twist of the standard \(S_4\)-module is irreducible of dimension three, and \(\bigwedge^2\mathrm{Std}_5\cong S^{(3,1,1)}\) is irreducible of dimension six. For an abelian normal subgroup with rational linear characters, the little-group/Clifford argument identifies a \(G\)-submodule generated by one weight space with the induced representation from its character stabilizer. An invariant subspace must respect the \(T\)-weight-space decomposition; transitivity of the coordinate-permutation orbit and irreducibility on one stabilizer weight space force irreducibility of the induced summand. Distinct weight orbits ensure these three summands are pairwise nonisomorphic. Finally the trivial \(G\)-representation occurs in none of them, giving the fixed-subspace assertion.

## Verification
Run `python3 verify.py` with Python 3.10+ and `sympy` installed. The standalone script reconstructs all vertices, neighborhoods, faces and oriented rational boundary matrices, proves the chain compositions vanish, and computes exact rational ranks. It evaluates signed fixed-simplex traces for all \(1920\) affine group elements, checks the complete translation Fourier multiplicities, checks the seven-type \(S_5\) character, verifies all elements of the two inertia groups, and tests transporter conjugacy for all sixteen weight labels. Expected final output:

`VERIFY_OK 16_VERTICES 352_FACES BOUNDARY_RANKS_15_65_64_16`

`AFFINE_AUTOMORPHISMS_1920 HOMOLOGY_31 IRREDUCIBLES_6_10_15`

The representation-theoretic implications in Step 5 are mathematical deductions from the exact tables and standard Clifford/character arguments. No external homology certification or integral equivariant splitting is claimed.

## Relationship to prior work
Matsushita [1] studies fundamental groups of neighborhood complexes and supplies a general topological framework, not the affine action on Clebsch homology. The published exact calculation [2] establishes \(\mathcal N(C)\simeq\bigvee^{31}S^2\); the family classification [3] establishes the corresponding homotopy type for every odd folded cube. Those nonequivariant theorems do not determine a homology representation. More closely, [4] already identifies every \(T\)-character multiplicity for odd folded cubes, including the Clebsch multiplicities \(6,1,3\) by weight. Its scope expressly leaves the **larger coordinate-permutation action** uncomputed. Weight-space dimensions alone do not determine the stabilizer representations or the full semidirect-product decomposition. This work determines those missing inertia-group characters and therefore the full \(1920\)-element action. The graph identity and automorphism-group order are independently documented in the distance-regular graph catalogue [5].

An overlapping full symmetry calculation could still exist under the aliases *Greenwood–Gleason graph*, *folded five-cube*, or *projective hypercube* or in unindexed literature. Targeted mathematical and indexed-result searches located no statement determining these three full affine constituents. Absence from searches does not establish unconditional novelty or publication priority.

## Limitations
The theorem applies only to the ordinary open-neighborhood complex of the five-regular Clebsch graph and only to **rational representations**. It does not provide an integral \(\mathbb Z[G]\)-lattice decomposition, an equivariant geometric collapse, or a full family formula for all folded cubes under their larger automorphism groups. The finite calculation exhausts this sixteen-vertex complex; no extrapolation to infinitely many graphs is asserted. Bibliographic coverage is incomplete, and some sources were available only as abstracts or indexed results.

## References
[1] T. Matsushita, *Fundamental groups of neighborhood complexes*, arXiv:1210.2803v1, first public 2012-10-10, https://arxiv.org/abs/1210.2803; journal full article, https://www.ms.u-tokyo.ac.jp/journal/jms240302.pdf.

[2] *The five-regular Clebsch neighborhood complex is a wedge of thirty-one two-spheres*, public full result, https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-the-5-regular-clebsch-neighborhood-complex-is-a-wedge-of-31-2-sp--1dc11cc6574a/RESULT.md.

[3] *The neighborhood complexes of odd folded hypercubes are wedges of two-spheres*, public full result, https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-the-neighborhood-complexes-of-odd-folded-hypercubes-are-wedges-o--438357602cff/RESULT.md.

[4] *Translation-character decomposition for odd folded-cube neighborhood complexes*, public full result, https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-translation-character-decomposition-for-odd-folded-cube-neighbor--4651ea532edd/RESULT.md.

[5] *Clebsch graph / folded five-cube*, distance-regular graph catalogue, https://www.math.mun.ca/distanceregular/graphs/clebsch.html.

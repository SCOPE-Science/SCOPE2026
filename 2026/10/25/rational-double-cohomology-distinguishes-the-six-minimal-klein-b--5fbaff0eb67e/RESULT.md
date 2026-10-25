# Rational double cohomology distinguishes the six minimal Klein-bottle triangulations

## Finding
For the **six** combinatorial isomorphism classes of eight-vertex triangulations of the Klein bottle, the rational double cohomology \(HH^{*,*}(\mathcal Z_K;\mathbb Q)\) falls into three types. Every class has \(HH^{0,0}\cong\mathbb Q\). Beyond this unit, the complete list of potentially nonzero groups is
\[
\begin{array}{c|cc|c}
\text{number of types} & \dim_\mathbb Q HH^{-1,4} & \dim_\mathbb Q HH^{-2,8} & \dim_\mathbb Q HH^{*,*}\\\hline
4&1&0&2\\
1&2&1&4\\
1&3&2&6
\end{array}.
\]
All other rational double-cohomology groups are zero. Thus, despite identical homeomorphism type and face vector \((8,24,16)\), these triangulations have different rational double-cohomology invariants. No corresponding integral classification is asserted.

## Assumptions and scope
Let \(V=\{a,b,c,d,e,f,g,h\}\). A word such as `abd` denotes the facet \(\{a,b,d\}\). Each complex below consists of every subset of one of the 16 displayed triangular facets. The six rows specify pairwise nonisomorphic triangulations; they arise in the complete orbit of bistellar \(2\)-\(2\) edge flips from the first row. Published eight-vertex Klein-bottle enumeration establishes that exactly six types exist, and the accompanying program independently enumerates the complete connected flip orbit and tests pairwise isomorphism of their vertex–facet incidence graphs.

| Type | Sixteen maximal faces | \(\dim HH^{-2,8}\) | \(\dim HH^{-1,4}\) |
|---|---|---:|---:|
| 0 | `abd abe acd ace bcf bch bdg bef bgh cdf ceh deg deh dfh efg fgh` | 0 | 1 |
| 1 | `abe abg acd ace adg bcf bch bef bgh cdf ceh deg deh dfh efg fgh` | 2 | 3 |
| 2 | `abd abf acd ace aef bcf bch bdg bgh cdf ceh deg deh dfh efg fgh` | 1 | 2 |
| 3 | `abd abe ace acf adf bcf bch bdg bef bgh ceh deg deh dfh efg fgh` | 0 | 1 |
| 4 | `abd abe acd ach aeh bcf bch bdg bef bgh cdf deg deh dfh efg fgh` | 0 | 1 |
| 5 | `abd abf acd ace aef bce bcf bdg beh bgh cdf deg deh dfh efg fgh` | 0 | 1 |

All coefficients in the theorem are rational. The grading convention, including negative first coordinate, is that of Limonchenko–Panov–Song–Stanley, arXiv:2112.07004.

## Proof
For every subset \(I\subseteq V\), let \(K_I\) be the induced subcomplex and set \(C_{p,l}=\bigoplus_{|I|=l}\widetilde H^p(K_I;\mathbb Q)\). The Hochster double-cohomology differential is the alternating sum of restrictions induced by deleting one vertex. Explicitly, on the summand labeled by \(I=\{i_1<\dots<i_l\}\), the differential from \(C_{p,l}\) to \(C_{p,l-1}\) has the block \((-1)^{p+1+j-1}\rho_{I\setminus\{i_j\},I}\) for deletion of \(i_j\), with cohomological restriction \(\rho\). The uniform \((-1)^{p+1}\) for each \(p\) does not change the resulting cohomology; the executable matrix construction uses \((-1)^{j-1}\). The bidegree corresponding to \(C_{p,l}\) is \((-k,2l)\) with \(-k=p-l+1\).

Compute all \(256\) induced subcomplexes for each type, including the empty subset. For each nonempty \(I\), form oriented simplicial boundary matrices \(B_1(I)\) and \(B_2(I)\), using the sorted vertices as orientations. Compute \(\ker B_1(I)/\operatorname{im}B_2(I)\) by exact rational basis extension, and \(\widetilde H^0(K_I;\mathbb Q)\) from connected components. For \(J\subset I\), compute the inclusion-induced map on first homology by embedding selected oriented cycles and projecting into the quotient basis; transpose to obtain the cohomological restriction. In degree zero use component-incidence differences. The code verifies all products of consecutive differential matrices vanish.

The full nonempty-subset analysis shows that \(\widetilde H^p(K_I;\mathbb Q)=0\) unless \(p=0,1\); in particular all rational second homology groups of induced subcomplexes vanish. The empty set contributes only \(HH^{0,0}=\mathbb Q\). The following rank data suffice to reconstruct every other claimed group, since in a finite cochain complex \(\dim HH=\dim C-\operatorname{rank}d_{\mathrm{out}}-\operatorname{rank}d_{\mathrm{in}}\):

For \(p=0\), every type has \(\dim C_{0,2}=4\). The type-indexed pairs of dimensions \((\dim C_{0,3},\dim C_{0,4})\) are \((4,1),(1,0),(2,0),(3,0),(3,0),(4,1)\), respectively. Ranks of \(C_{0,3}\to C_{0,2}\) are \(3,1,2,3,3,3\), and ranks of \(C_{0,4}\to C_{0,3}\) are \(1,0,0,0,0,1\). All the remaining degree-zero cohomology is zero.

For \(p=1\), the source dimensions at \(l=3,4,5,6,7,8\) are \((20,71,96,60,16,1)\) for types 0 and 5, \((17,70,96,60,16,1)\) for type 1, \((18,70,96,60,16,1)\) for type 2, and \((19,70,96,60,16,1)\) for types 3 and 4. The successive ranks for deletions \(l=4,5,6,7,8\) are \((d,51,45,15,1)\), where \(d\) is the dimension in layer three. Hence at layer four, the resulting cohomology dimensions are \(0,2,1,0,0,0\), respectively, and all other first-cohomology blocks are acyclic. The bidegree formula now proves the theorem.

Finally, each of the six facet systems has 24 edges each contained in exactly two triangles, 16 triangles, and connected vertex links. The starting triangulation is the classical eight-vertex Klein bottle; bistellar flips preserve its PL homeomorphism type. The six isomorphism classes and their closure under all possible flips provide the complete classification under the established six-type enumeration.

## Verification
Run `python verify_klein.py` with Python 3, SymPy, and NetworkX. The self-contained source verifies six nonisomorphic flip classes, 36 directed inter-class-or-self flip incidences, edge pseudomanifold conditions, all induced second-homology vanishings, exact rational differential ranks, composition identities \(d^2=0\), and the claimed bigraded dimensions. The displayed face lists are printed for direct reproduction. In particular, every nonzero rank is over \(\mathbb Q\), not a modular estimate.

## Relationship to prior work
Limonchenko–Panov–Song–Stanley define double cohomology and compute many standard examples, including a minimal projective-plane complex; their construction supplies the differential used here, but does not tabulate this six-type Klein-bottle classification. Valenzuela Ruiz–Stanley investigate possible ranks and supply other non-wedge-decomposable examples, so rank two alone is not claimed as novel. Zhang studies how the invariant changes under facet operations; those general inequalities do not imply the six explicit rational computations. Published studies of eight-vertex Klein-bottle flips determine the list of combinatorial types but do not provide the rational double-cohomology table.

## Limitations
The calculation is rational; integral groups may have torsion (the Klein bottle itself has integral orientation-related torsion). This is an exact finite classification and does not claim a formula for larger nonorientable triangulations. Novelty was assessed against the accessible primary works and indexed related findings; equivalent unindexed calculations remain possible. No independent external mathematical audit has been performed.

## References
1. I. Limonchenko, T. Panov, J. Song, R. Stanley, *Double cohomology of moment-angle complexes*, arXiv:2112.07004, first submitted 2021-12-13, https://arxiv.org/abs/2112.07004 .
2. L. Valenzuela Ruiz and R. Stanley, work on double cohomology and rank restrictions, arXiv:2308.15702, https://arxiv.org/abs/2308.15702 .
3. H. Zhang, work on double cohomology under facet operations, arXiv:2404.06763, https://arxiv.org/abs/2404.06763 .
4. J. Eagon, *Minimal resolutions of ideals associated to triangulated homology manifolds*, source of an explicit eight-vertex Klein-bottle facet system, https://people.math.sc.edu/eagon/Papers/triangulatedhomologymanifolds.pdf .
5. Classification and bistellar-flip enumeration of the six eight-vertex Klein-bottle triangulations (see also public research finding *Exact 2–2 flip graph of the six eight-vertex Klein-bottle triangulations*, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-2-2-flip-graph-of-the-six-eight-vertex-klein-bottle-triang--3078dc303ec9 ).

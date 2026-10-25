# Complement-refined symmetric-group homology of the six-coordinate two-rank Rips space

## Finding

Let \(V=\binom{[6]}{2}\sqcup\binom{[6]}{4}\) with metric \(d(A,B)=|A\mathbin\triangle B|\), and write \(K_r=\operatorname{VR}_{\le r}(V)\), where \(r\ge0\). Coordinate permutations and taking complements commute and act on every \(K_r\) through \(G=S_6\times C_2\). Let \(\varepsilon\) be the nontrivial rational character of the complement factor, and let \(S^{\lambda}\) denote the rational Specht module of partition \(\lambda\vdash6\).

**The new representation assertion** is the complete rational module decomposition

\[
\widetilde H_3(K_2;\mathbb Q)\cong
\big(S^{(3,1,1,1)}\oplus S^{(2,1,1,1,1)}\big)\boxtimes\mathbf1
\;\oplus\;
\big(S^{(2,2,1,1)}\oplus S^{(2,1,1,1,1)}\big)\boxtimes\varepsilon.
\]

It follows that the complement involution has \(15\) invariant and \(14\) anti-invariant third-homology dimensions. At the later scale \(4\),

\[
\widetilde H_{14}(K_4;\mathbb Q)\cong\mathbf1_{S_6}\boxtimes\varepsilon.
\]

For context, the entire nonequivariant homotopy filtration is

\[
K_r\simeq\begin{cases}
\bigsqcup^{30}\{\mathrm{pt}\},&0\le r<2,\\
\bigvee^{29}S^3,&2\le r<4,\\
S^{14},&4\le r<6,\\
\mathrm{pt},&r\ge6.
\end{cases}
\]

In particular, its reduced ordinary barcode consists of \(29\) degree-zero intervals \([0,2)\), \(29\) degree-three intervals \([2,4)\), and one degree-fourteen interval \([4,6)\). **The nonequivariant scale-two homotopy type is an instance of the previously proved theorem of Feng and Nukala and is not asserted to be new.**

## Assumptions and scope

A Rips simplex at inclusive scale \(r\) is a nonempty set of vertices with *every* pairwise symmetric-difference distance at most \(r\). The coordinate ground set has exactly six elements, and the vertex set comprises *only* subsets of cardinality two or four. All group actions are simplicial and the stated decompositions are over \(\mathbb Q\). No integral equivariant splitting or extension to an arbitrary number of coordinates is claimed. Permutations act by \(\sigma\cdot A=\{\sigma(a):a\in A\}\), while \(\iota(A)=[6]\setminus A\). These actions commute.

## Proof

**1. Homotopy and degree concentration.** Every nonzero distance between members of \(V\) is in \(\{2,4,6\}\), so the indicated integer stages exhaust the filtration. At scale two, Theorem 18 of Feng–Nukala [1], applied with \(m=6,n=2\), proves that \(K_2\) is a wedge of three-spheres, possibly with zero summands. The direct face enumeration in `verify.py` yields

\[
(f_0,f_1,f_2,f_3,f_4,f_5)=(30,210,520,480,132,20).
\]

Its Euler characteristic is \(-28\); consequently the wedge contains exactly \(29\) three-spheres. A separate exhaustive rank calculation over \(\mathbb F_2\) returns boundary ranks \((29,181,339,112,20)\), yielding Betti dimensions \((1,0,0,29,0,0)\). The rank computation corroborates, but does not replace, the published homotopy concentration theorem. At scale four, the *only* vertex pairs of distance six are the \(15\) complement pairs \(\{A,[6]\setminus A\}\). Therefore the complex is the join of fifteen copies of \(S^0\), namely the boundary of a fifteen-dimensional cross-polytope \(S^{14}\). At scale six it is the full simplex on thirty vertices.

**2. Reconstructing the entire group character.** Enumerate the \(30\) vertices in the order of all two-subsets followed by all four-subsets, lexicographically within each rank. Enumerate all simplices \(\tau=(v_0<\dots<v_d)\) of the scale-two flag complex, with the ordering induced by that vertex order. Given \(g=(\sigma,\iota^e)\in S_6\times C_2\), let \(g(v_i)\) be the corresponding image vertex. Only simplices satisfying \(g\tau=\tau\) as unordered sets contribute to the cellular trace. If a fixed simplex induces the permutation \(\pi_{g,\tau}\) of its ordered vertices, its contribution to the ordinary Lefschetz number is \((-1)^d\operatorname{sgn}(\pi_{g,\tau})\). Therefore, because the only nonzero rational homology is \(H_0\cong\mathbb Q\) and \(H_3\cong\mathbb Q^{29}\),

\[
\chi_3(g)=1-\sum_{d=0}^{5}(-1)^d
\sum_{\substack{\tau\in(K_2)_d\\g\tau=\tau}}
\operatorname{sgn}(\pi_{g,\tau}).
\]

This is an exact finite integer formula for **every** group element, not a numerical approximation. The standalone verifier reconstructs the vertex lists and faces from the metric, evaluates this formula on all \(720\times2=1440\) group elements, and proves that it is constant on the eleven cycle types of the \(S_6\) factor. Listed by partition \(\mu\vdash6\), the character pairs \((\chi_3(\sigma,1),\chi_3(\sigma,\iota))\) are:

| Cycle type \(\mu\) | Without complement | With complement |
|:--|--:|--:|
| \((1^6)\) | 29 | 1 |
| \((2,1^4)\) | -11 | 1 |
| \((2^2,1^2)\) | 1 | -3 |
| \((2^3)\) | 1 | 5 |
| \((3,1^3)\) | 5 | 1 |
| \((3,2,1)\) | 1 | 1 |
| \((3^2)\) | -1 | 1 |
| \((4,1^2)\) | -1 | -1 |
| \((4,2)\) | -1 | -1 |
| \((5,1)\) | -1 | 1 |
| \((6)\) | 1 | -1 |

**3. Irreducible multiplicities.** The complement-even and complement-odd characters of \(S_6\) are, respectively,

\[
\chi^{\pm}(\sigma)=\tfrac12\big(\chi_3(\sigma,1)\pm\chi_3(\sigma,\iota)\big).
\]

For each partition \(\lambda\vdash6\), calculate \(m_\lambda^{\pm}=\frac1{720}\sum_{\mu\vdash6}(720/z_\mu)\chi^{\pm}(\mu)\chi^{\lambda}(\mu)\), where \(z_\mu=\prod_j j^{a_j}a_j!\) when \(\mu\) has \(a_j\) parts of size \(j\). The irreducible characters \(\chi^\lambda\) are obtained by Murnaghan–Nakayama rim-strip recursion, which is implemented in the accompanying checker using no external packages. Exactly four multiplicities are nonzero: \(m^+_{(3,1,1,1)}=m^+_{(2,1,1,1,1)}=m^-_{(2,2,1,1)}=m^-_{(2,1,1,1,1)}=1\). All others vanish. Rational semisimplicity identifies the stated modules. The dimensions are \(10+5=15\) and \(9+5=14\), agreeing with the identity and complement character values \(29\) and \(1\).

**4. The sphere at scale four.** Its fifteen antipodal vertex pairs are indexed by two-subsets of \([6]\). The top homology line is the orientation line of the associated cross-polytope. Coordinate permutations permute these axes without exchanging positive and negative choices. A coordinate transposition exchanges exactly four pairs of axes (among the fifteen), hence acts on the orientation line by \(+1\). Since transpositions generate \(S_6\), this factor acts trivially. Complementation interchanges the two members of *each* of the fifteen antipodal pairs, and therefore acts on orientation by \((-1)^{15}=-1\). This proves the last module identity. At scale two, quotienting by \(S_6\) removes all positive-degree rational homology, but at scale four the quotient by \(S_6\) retains the one-dimensional degree-fourteen class because its action is trivial. By contrast, quotienting by the complement involution retains a fifteen-dimensional third-homology group at scale two but removes the degree-fourteen class at scale four.

## Verification

The included `verify.py` is a self-contained Python 3 standard-library checker. From the package directory run `python3 verify.py`. It independently regenerates all vertices and cliques, checks the six-entry face vector and exact \(\mathbb F_2\)-boundary ranks, computes the signed Lefschetz character on all \(1440\) automorphisms, reconstructs all eleven character-class values, evaluates all irreducible multiplicities via explicit rim-strip recursion, and verifies the scale-four antipodal-pair description. The final marker is `REPRODUCIBLE_RIPS_S6_C2_CHARACTER_PASS`. This is exhaustive for the specified thirty-vertex complex; the nonstandard degree-concentration input is the cited published topology theorem.

## Relationship to prior work

Feng and Nukala [1, §6, Theorem 18] establish the *nonequivariant* sphere-wedge result for precisely the family of two-separated Boolean weight layers considered here; this covers the scale-two rank \(29\) but does not specify the joint \(S_6\times C_2\) action on homology. Briggs, Feng and Wells [2, §§1,4.2] investigate facets and homology of full cubes and *single* Hamming-weight levels; those statements do not determine the representation of the union of the two complementary levels. Galetto, Montaño and Wellner [3] study the symmetry representation of the *whole* hypercube Rips complex; homology of an induced two-rank subcomplex does not in general follow by restriction of that homology module. Nearby indexed results on a single weight-three layer and a cumulative weight-at-most-three sublevel concern different vertex sets and cannot imply this complete joint character without additional relative or equivariant information. The new assertion is exactly the representation decomposition, not the previously known nonequivariant wedge or barcode multiplicity.

## Limitations

The theorem is a finite, exact rational representation calculation for the 30-vertex six-coordinate two-rank subspace. It does not provide a universal formula for arbitrary Boolean-layer pairs, integral representation lattices, or an equivariant stable splitting of spaces. The scale-two homotopy concentration relies on a published theorem, while the character is established by the accompanying exhaustive exact certificate. A possibility of unindexed equivalent calculations and potentially relevant full-cube equivariant methods remains; no independent mathematical audit has been performed.

## References

1. Z. Feng and N. C. P. Nukala, *On Vietoris–Rips complexes of finite metric spaces with scale 2*, arXiv:2302.14664, first public 2023-02-28; §6, Theorem 18. https://arxiv.org/html/2302.14664v3.
2. J. Briggs, Z. Feng and C. Wells, *Facets in the Vietoris–Rips complexes of hypercubes*, arXiv:2408.01288, first public 2024-08-02; §§1,4.2. https://arxiv.org/html/2408.01288v2.
3. F. Galetto, J. Montaño and Z. Wellner, *Homology of Vietoris–Rips complexes of hypercube graphs via group actions*, arXiv:2606.20784, first public 2026-06-18; verified abstract/scope, full text not relied upon. https://arxiv.org/abs/2606.20784.

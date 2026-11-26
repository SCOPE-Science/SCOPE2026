# Nonisomorphic triangle quiver unit groups with identical conjugacy-class-size multisets

## Finding

Let \(p\ge 5\) be a prime. Let \(Q_{\mathrm{cyc}}\) be the directed triangle \(1\to2\to3\to1\), and let \(Q_{\mathrm{tr}}\) have arrows \(1\to2\), \(2\to3\), \(1\to3\). If \(J\) denotes the arrow ideal in each path algebra, the finite groups
\[
U_{\mathrm{cyc}}=(\mathbb F_pQ_{\mathrm{cyc}}/J^2)^\times,
\qquad
U_{\mathrm{tr}}=(\mathbb F_pQ_{\mathrm{tr}}/J^2)^\times
\]
are **not isomorphic**. Yet their entire multisets of conjugacy-class sizes, with multiplicities, agree. Thus even the full class-size data cannot distinguish the abstract unit groups of two orientations of the same simple triangle.

The class-size equality is an instance of the known orientation-independence theorem for radical-square-zero quiver unit groups [1, 2]. The claim here is the separation of the two *abstract unit groups*, not a new class-count formula or a distinction between the two underlying algebras.

## Proof

Write \(N=1+J\) for the radical subgroup in either group, with \(J\) now denoting its image in the quotient. Since \(J^2=0\), multiplication in \(N\) is addition of radical coordinates. Thus \(N\cong (C_p)^3\) is the normal Sylow \(p\)-subgroup and is characteristic. The quotient is \(T\cong(\mathbb F_p^\times)^3\), represented by diagonal units. The conjugation action of this quotient on \(N\) is well defined because \(N\) is abelian. On the line of the arrow \(i\to j\) the character is
\[
\chi_{ij}(d_1,d_2,d_3)=d_i d_j^{-1}.
\]

An abstract group isomorphism would restrict to an \(\mathbb F_p\)-linear map on the elementary abelian Sylow subgroup and would intertwine the two quotient actions after an isomorphism of their diagonal quotients. The three characters in each representation are distinct, so this would identify the character triples up to a permutation and an isomorphism of \(T\). As a result it would identify, up to permutation of coordinates, the subgroups
\[
\{(x,y,z)\in(\mathbb Z/(p-1))^3:\chi_1^x\chi_2^y\chi_3^z=1\}.
\]
Indeed precomposing a character by an isomorphism preserves whether it is trivial. For the cycle, order the characters as \((\chi_{12},\chi_{23},\chi_{31})\). The powers of \(d_1,d_2,d_3\) in the product are \((x-z,y-x,z-y)\), so the subgroup is \(\{(t,t,t)\}\). For the transitive triangle, order them as \((\chi_{12},\chi_{23},\chi_{13})\). The powers are \((x+z,y-x,-y-z)\), giving \(\{(t,t,-t)\}\). A permutation preserves the all-equal subgroup, whereas \((1,1,-1)\) is not all-equal modulo \(p-1\ge4\). This proves nonisomorphism.

For completeness, the known class-size equality can be seen in the following specialization of [1]. Fix a diagonal \(d\) and let \(B(d)\) be the undirected edges whose endpoint labels in \(d\) coincide. Radical conjugation freely translates the arrow coordinates outside \(B(d)\) and leaves those on \(B(d)\) unchanged. The remaining torus action scales according to the arrow characters. For a support \(F\subseteq B(d)\), its stabilizer consists of diagonal labels constant on every component of the spanning subgraph \((\{1,2,3\},F)\). With \(k(F)\) the number of those components, there are \((p-1)^{|F|-3+k(F)}\) classes of size \(p^{3-|B(d)|}(p-1)^{3-k(F)}\) at this \((d,F)\): divide the \((p-1)^{|F|}\) choices of nonzero supported coordinates by the torus orbit size, and multiply the latter by the radical orbit size to obtain each full class size. Neither expression uses the directions of the edges. Summing over \((d,F)\) gives identical multisets. For example, at \(p=5\) the group order is \(8000\), the number of classes is \(140\), and consequently the commuting probability is \(7/400\) for both groups.

## Scope and prior work

The nonisomorphism is asserted over prime fields with \(p\ge5\); no claim over arbitrary prime powers or for general pairs of orientations is needed. Reference [1] gives both the orientation-independent conjugacy spectra and the consistently directed versus acyclic cycle comparison at the level of spectra and algebra global dimensions. Neither that equality nor a distinction between algebras gives the abstract-group nonisomorphism; the distinguishing invariant above is the character-relation subgroup of the quotient action on the characteristic Sylow subgroup. Reference [2] gives the more general class-size formula, including loops. There is no claim of historical priority or formal verification.

## References

1. *Tutte evaluations and full inner-conjugacy spectra of radical-square-zero quiver algebras*, Resultary, 2026-10-12, [published record](https://github.com/Resultary/2026/blob/main/2026/10/12/SCOPE-tutte-evaluations-and-full-inner-conjugacy-spectra-of-radical-sq--f79766dd4bb5/RESULT.md).
2. *Conjugacy-class size spectrum of radical-square-zero quiver unit groups*, Resultary, 2026-10-18, [published record](https://github.com/Resultary/2026/blob/main/2026/10/18/SCOPE-conjugacy-class-size-spectrum-of-radical-square-zero-quiver-unit--17f3f95e6cb8/RESULT.md).

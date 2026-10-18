# Dihedral homology characters and a twelve-class quotient criterion for cycle independence complexes

## Finding
For each integer \(n\ge3\), the independence complex of the cycle \(C_n\) has a canonical action by the dihedral group \(D_n\). We determine the complete character of that action on reduced rational homology. In particular, **the rational homology of the orbit space is nonzero precisely in two residue classes modulo twelve**, despite the original independence complex having nonzero reduced homology for every \(n\ge3\).

Write \(d_n=\lfloor(n-2)/3\rfloor\) and \(\epsilon_n=(-1)^{d_n+1}\). Let \(p_0=1\), \(p_1=0\), and \(p_k=p_{k-1}-p_{k-2}\) for \(k\ge2\). Let \(c_k=2\cos(\pi k/3)\) for \(k\ge2\); its six-periodic values at residues \(0,1,2,3,4,5\) are \((2,1,-1,-2,-1,1)\).

If \(r\) rotates by one vertex and \(s\) reflects vertex \(i\) to \(-i\), the complete character \(\chi_n\) of the nonzero reduced rational homology is

\[\chi_n(r^j)=\epsilon_n\begin{cases}1,&\gcd(n,j)=1,\\c_{\gcd(n,j)},&\gcd(n,j)\ge2,\end{cases}\]

\[\chi_n(r^js)=\epsilon_n\begin{cases}p_{(n-1)/2},&n\text{ odd},\\p_{n/2+1},&n\text{ even and }j\text{ even},\\p_{n/2-2},&n\text{ even and }j\text{ odd}.\end{cases}\]

When \(3\mid n\), top homology is the irreducible two-dimensional rational representation with rotation eigenvalues primitive third roots of unity for \(n\equiv3\pmod6\), and primitive sixth roots for \(n\equiv0\pmod6\); all reflections have trace zero. Otherwise top homology is one-dimensional. Its generator characters \((\chi_n(r),\chi_n(s))\) are \((1,1)\) when \(n\equiv1,11\pmod{12}\), \((1,-1)\) when \(n\equiv5,7\pmod{12}\), \((-1,1)\) when \(n\equiv2,4\pmod{12}\), and \((-1,-1)\) when \(n\equiv8,10\pmod{12}\).

Consequently,

\[\widetilde H_k(|\operatorname{Ind}(C_n)|/D_n;\mathbb Q)\cong\begin{cases}\mathbb Q,& k=d_n\text{ and }n\equiv1,11\pmod{12},\\0,&\text{otherwise}.\end{cases}\]

## Assumptions and scope
The graph \(C_n\) is the simple cycle on vertex set \(\mathbb Z/n\mathbb Z\), with adjacent residues differing by \(\pm1\). Its simplicial independence complex \(K_n\) consists of vertex subsets containing no neighboring pair. The full dihedral group \(D_n\) acts simplicially, with generators \(r(i)=i+1\) and \(s(i)=-i\). Homology is reduced and has coefficients in \(\mathbb Q\), except where the integral nonequivariant homotopy type is explicitly recalled. For a permutation of a finite set, its sign is defined in the usual way, with the empty permutation having sign \(1\).

The known nonequivariant cycle classification states \(K_{3m}\simeq S^{m-1}\vee S^{m-1}\), \(K_{3m+1}\simeq S^{m-1}\), and \(K_{3m+2}\simeq S^m\) (with the obvious range restrictions). Thus \(\widetilde H_k(K_n;\mathbb Q)\) vanishes unless \(k=d_n\); its dimension is \(2\) for \(3\mid n\), and \(1\) otherwise. This classification is prior work, not a contribution of the present result.

## Proof
**Signed equivariant Euler trace.** Orient each face in increasing vertex order. If \(g\in D_n\) preserves a face \(F\), its trace on that oriented simplex is \(\operatorname{sgn}(g|_F)\). The augmented simplicial Hopf trace theorem and the known concentration of reduced homology therefore yield

\[\chi_n(g)=(-1)^{d_n+1}\sum_{\substack{F\in K_n\\gF=F}}(-1)^{|F|}\operatorname{sgn}(g|_F).\tag{1}\]

The empty face contributes \(1\). In particular, a face formed from complete permutation orbits of \(g\) receives weight \((-1)^{|F|}\operatorname{sgn}(g|_F)=(-1)^{\text{number of selected orbits}}\), since an orbit of length \(\ell\) contributes \((-1)^\ell(-1)^{\ell-1}=-1\).

**Rotations.** Set \(a=\gcd(n,j)\). The rotation \(r^j\) has exactly \(a\) vertex orbits. If \(a=1\), its single nonempty orbit is not an independent set; only the empty face contributes to (1), giving the first rotation case. If \(a\ge2\), every individual orbit is independent, and distinct orbits are adjacent exactly when their labels are neighboring residues modulo \(a\). For \(a=2\) the resulting simple quotient graph is one edge; for \(a\ge3\) it is \(C_a\). Consequently the weighted fixed-face sum is the independence polynomial of this quotient graph evaluated at \(-1\).

For an edge, this polynomial has value \(-1=c_2\). For cycles of length \(a\ge3\), the standard deletion-and-contraction recurrence gives values \(c_a\), characterized by \(c_2=-1\), \(c_3=-2\), \(c_{a+2}=c_{a+1}-c_a\); equivalently \(c_a=2\cos(\pi a/3)\). Substitution in (1) proves the rotation formula, including the identity rotation \(j=0\).

**Reflections.** Each vertex orbit under \(r^js\) is either a singleton or a pair. An orbit containing two adjacent vertices cannot occur in any invariant independent face; discard such orbits. The adjacency graph of the remaining permissible orbits is always a path. For odd \(n\) there is one fixed vertex and one discarded orbit opposite it, leaving exactly \((n-1)/2\) path vertices. For even \(n\) and even \(j\), the axis passes through two opposite vertices, leaving a path with \(n/2+1\) vertices. For even \(n\) and odd \(j\), the axis passes through two opposite edges, so two adjacent-pair orbits must be discarded and \(n/2-2\) path vertices remain. A path of zero vertices is permitted.

The signed independence polynomial at \(-1\) of the path on \(k\) vertices is \(p_k\): if its last vertex is omitted one gets the preceding path, and if selected its neighbor is forbidden. Therefore \(p_0=1\), \(p_1=0\), \(p_k=p_{k-1}-p_{k-2}\). Equation (1) gives the three reflection formulas.

**Representations.** Character evaluation gives \(\chi_n(r)=(-1)^{d_n+1}\) and the stated complete reflection traces. If \(3\nmid n\), homology is one-dimensional, and direct substitution into the recurrences yields the four character pairs recorded above, by \(n\bmod12\). If \(3\mid n\), its dimension is two, every reflection has trace zero, and the rotation character has trace \(-1\) for \(n\equiv3\pmod6\), or \(1\) for \(n\equiv0\pmod6\). The rotation acts with finite order on a two-dimensional rational vector space, so its determinant is either \(1\) or \(-1\). If the determinant were \(-1\), its eigenvalues would be \(1\) and \(-1\), forcing trace zero. Its computed trace is \(\pm1\), hence its determinant is \(1\) and its characteristic polynomial is respectively \(t^2+t+1\) or \(t^2-t+1\). Each is irreducible over \(\mathbb Q\), giving the claimed rational irreducibility and eigenvalues. Equivalently, these identifications are forced directly by the character formulas at all rotations and reflections.

**Quotient.** A finite group acting simplicially on a finite complex admits an equivariant barycentric subdivision without inversions. Over \(\mathbb Q\), the cellular chains of the quotient identify with invariant cellular chains under averaging, so \(\widetilde H_*(|K_n|/D_n;\mathbb Q)\cong\widetilde H_*(K_n;\mathbb Q)^{D_n}\). For the two-dimensional irreducible case the invariant part is zero. For the one-dimensional case it has rank one exactly when both generators act trivially, namely \(n\equiv1,11\pmod{12}\). This proves the quotient criterion.

## Verification
The standalone script `verify_fixed_faces.py` exhaustively enumerates independent sets, signed stabilizer traces and all dihedral elements for every \(3\le n\le20\), checking 414 cases against the closed formulas and checking the quotient invariants. It completed with `FIXED_FACES_OK 414 dihedral elements tested n=3..20`.

The separately implemented script `verify_chain.py` builds the augmented simplicial boundary complex over a prime field and computes boundary-space and induced homology traces directly for every dihedral element and every \(3\le n\le12\). It completed with `CHAIN_REPRESENTATIONS_OK`. This check also verifies the one-degree homology concentration and dimensions throughout its finite range. Execute both with `python verify_fixed_faces.py` and `python verify_chain.py`; no extra packages are required. The infinite-parameter statement follows from the proof above, not from finite enumeration or modular agreement.

## Relationship to prior work
Babson and Kozlov, *Proof of the Lovász Conjecture* (arXiv:math/0402395v1, 2004), Proposition 4.1, record Kozlov's nonequivariant cycle homotopy types; Proposition 4.4 obtains \(\mathbb Z_2\)-equivariant information and reflection-orbit spaces for odd cycles. Živaljević, *WI-posets, graph complexes and \(\mathbb Z_2\)-equivalences* (arXiv:math/0405419v1, 2004), Section 8 and Proposition 43, determine a reflection-equivariant sphere type in the family \(\operatorname{Ind}(C_{6p-1})\). Thus **the sphere-wedge ranks and those reflection-restricted statements are prior work**, and are not newly claimed. Adamaszek's *Splittings of independence complexes and the powers of cycles* (arXiv:1106.6250v1, 2011) studies nonequivariant recursive homotopy types for cycle powers.

The present result instead computes all rotations, both conjugacy classes of reflections when \(n\) is even, the complete dihedral rational representation for every cycle length, and the precise full-dihedral quotient homology criterion. The inspected primary statements do not imply this combined result: reflection-restricted \(\mathbb Z_2\) data cannot determine rotations or the entire \(D_n\)-invariant summand.

## Limitations
Only the rational homology representation and rational homology of the full dihedral orbit space are classified. No integral module-lattice classification, torsion claim for the quotient, or full equivariant homotopy classification is made. Existing \(\mathbb Z_2\)-equivariant results cover substantial restrictions of the character. An equivalent result in unindexed or unpublished literature cannot be ruled out solely by searches. No independent scientific audit has been performed.

## References
1. E. Babson and D. N. Kozlov, *Proof of the Lovász Conjecture*, arXiv:math/0402395v1 (first publicly submitted 2004-02-24), Proposition 4.1 and Proposition 4.4. https://arxiv.org/abs/math/0402395v1
2. R. T. Živaljević, *WI-posets, graph complexes and \(\mathbb Z_2\)-equivalences*, arXiv:math/0405419v1 (2004-05-21), Section 8, Proposition 43. https://arxiv.org/abs/math/0405419
3. M. Adamaszek, *Splittings of independence complexes and the powers of cycles*, arXiv:1106.6250v1 (2011-06-30), introduction and cycle recurrence. https://arxiv.org/abs/1106.6250v1
4. A. Engström, *Complexes of directed trees and independence complexes*, arXiv:math/0508148v1 (2005-08-08), cycle-independence discussion. https://arxiv.org/abs/math/0508148v1

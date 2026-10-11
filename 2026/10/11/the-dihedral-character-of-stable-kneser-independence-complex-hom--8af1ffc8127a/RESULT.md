# The dihedral character of stable Kneser independence-complex homology

## Finding

Let \(m\geq 8\) be an integer, put \(k=m-4\), and let \(K_m=\operatorname{Ind}(\operatorname{SG}_{2,k})\). The vertices of the stable Kneser graph \(\operatorname{SG}_{2,k}\) are the two-element subsets of \(\mathbb Z/m\mathbb Z\) that are not edges of the cyclic polygon; two such vertices are adjacent precisely when they are disjoint. The group \(D_{2m}=\langle r,s\mid r^m=s^2=1,\ srs=r^{-1}\rangle\) acts by \(r(t)=t+1\) and \(s(t)=-t\) on the polygon and hence on \(K_m\).

The only nonzero reduced rational homology group of \(K_m\) is in dimension two. The character \(\chi_m(g)=\operatorname{tr}(g\mid\widetilde H_2(K_m;\mathbb Q))\), which uniquely specifies the rational representation of \(D_{2m}\), is the following. Write
\[
 b_m=\frac{m^3-12m^2+35m-6}{6}.
\]
For \(0\leq j<m\),
\[
\chi_m(r^j)=
\begin{cases}
 b_m,&j=0,\\
 \frac m2-1,&2\mid m\text{ and }j=m/2,\\
 \frac m3-1,&3\mid m\text{ and }j\in\{m/3,2m/3\},\\
 -1,&\text{otherwise},
\end{cases}
\]
and
\[
\chi_m(r^js)=
\begin{cases}
1,&m\text{ odd},\\
3-\frac m2,&m\text{ even and }j\text{ even},\\
\frac m2-3,&m\text{ even and }j\text{ odd}.
\end{cases}
\]
In particular, the character distinguishes the two reflection classes when \(m\) is even. The degree \(b_m\) agrees with the nonequivariant homology rank previously determined by Braun; the remaining character values are the assertion here.

## Assumptions and scope

All graphs are finite and simple. An independence complex contains the empty face and all independent vertex subsets. For a cyclic \(m\)-gon, a *chord* means a two-element vertex set that is not a polygon edge; a triple is *admissible* when its vertices are pairwise nonconsecutive modulo \(m\). All homology is reduced simplicial homology with coefficients \(\mathbb Q\), and all group actions are simplicial. The theorem assumes \(m\ge8\), equivalently \(k\ge4\). Smaller parameters are excluded.

## Proof

**1. A polygonal relative-chain model.** Let \(H_m\) be the complement of the cycle graph on \(\mathbb Z/m\mathbb Z\). Let \(U_m\subseteq K_m\) be the union of the full simplices \(W_v\) consisting of all chords incident to each polygon vertex \(v\). Every pairwise-intersecting family of distinct two-element sets is either contained in a star \(W_v\) or consists of the three sides of a triangle on three polygon vertices. Indeed, given intersecting distinct pairs \(\{a,b\}\) and \(\{a,c\}\), any pair meeting both either contains \(a\) or equals \(\{b,c\}\); if the latter occurs, no fourth distinct pair meets all three. Consequently, the simplices outside \(U_m\) are exactly the two-simplices indexed by admissible triples \(\{a,b,c\}\). Their boundaries belong to \(U_m\). There are no other relative cells.

**2. Equivariant reduction of the star union.** For every nonempty face \(\sigma\) of \(U_m\), define a map into the nonempty-face poset of \(H_m\): a singleton face consisting of chord \(\{v,w\}\) goes to the edge \(\{v,w\}\), while a face containing at least two distinct chords goes to their unique common polygon vertex. This is an order-reversing, \(D_{2m}\)-equivariant face-poset map \(p\). Conversely, an edge \(\{v,w\}\) of \(H_m\) goes to the singleton face containing that chord, and a vertex \(v\) goes to \(W_v\), giving an order-reversing equivariant map \(q\). One checks \(pq=\mathrm{id}\); also \(qp(\sigma)\supseteq\sigma\) for each face \(\sigma\) of \(U_m\). Thus \(qp\) is an extensive equivariant closure operator. The order-homotopy lemma on face posets proves a \(D_{2m}\)-equivariant homotopy equivalence \(U_m\simeq H_m\). The reduction is explicit and avoids a nonequivariant identification of representations.

**3. The rational character formula before counting.** Orient the edges of \(H_m\) by ordered polygon vertices, and orient each additional two-cell of \(K_m/U_m\) using its three chord vertices. The three chord vertices are naturally in bijection with the three omitted vertices of the corresponding polygon triple, so the permutation signs coincide. Let \(V_m\), \(E_m\), and \(T_m\) denote the signed permutation chain representations on polygon vertices, chords, and admissible triples. The preceding steps give, in the rational representation Grothendieck group,
\[
[\widetilde H_2(K_m;\mathbb Q)]=[T_m]-[E_m]+[V_m]-[\mathbb Q].
\]
For this equality, we use Braun's theorem that for \(k\ge4\) the complex \(K_m\) is a wedge of two-spheres, so its reduced homology is concentrated in degree two. The identity follows from additivity of equivariant alternating cellular chain traces applied to \((K_m,U_m)\). Therefore, for each symmetry \(g\), its character is the signed count of setwise fixed admissible triples minus the signed count of setwise fixed chords plus the number of fixed polygon vertices minus one. The sign on a fixed edge or triangle is the orientation sign of the induced permutation.

**4. Rotations.** The identity fixes \(m\) vertices, \(m(m-3)/2\) chords and \(m(m-4)(m-5)/6\) admissible triples. This gives \(b_m\). For a nonidentity rotation, no polygon vertex is fixed. A chord can be setwise fixed only by the half-turn when \(m\) is even; then precisely \(m/2\) opposite-vertex chords are fixed, each with sign \(-1\). An admissible triple can be setwise fixed only by a rotation of order three; when \(3\mid m\), each of the two order-three rotations fixes \(m/3\) orbit triples, each with orientation sign \(+1\). All remaining signed counts vanish. Subtracting the trivial degree-zero trace proves the rotation formula.

**5. Reflections.** For odd \(m\), every reflection fixes one vertex. It reverses \((m-3)/2\) chord pairs and \((m-5)/2\) admissible triples; the corresponding signed traces are their negatives, yielding \(\chi_m=1\). For even \(m\), a reflection \(r^js\) with even \(j\) fixes two opposite vertices, reverses \(m/2-1\) chords, fixes one more chord pointwise, and reverses \(m-4\) admissible triples. Its signed chain traces are therefore \(2\), \(2-m/2\), and \(-(m-4)\), giving \(3-m/2\). If \(j\) is odd, the reflection fixes no polygon vertices and no admissible triples; it reverses \(m/2-2\) chords. The character is consequently \(m/2-3\). These cases exhaust the dihedral group, completing the proof.

## Verification

The standalone standard-library scripts `verify_direct.py` and `verify_cellular.py` supply two independent finite cross-checks. Run each with a Python 3 interpreter from the directory containing the scripts. The first directly enumerates all simplices of \(K_m\) for \(8\le m\le12\), computes signed fixed-simplex Lefschetz traces for every rotation and reflection, and compares them with the formula. The second constructs only the polygonal chord graph and admissible triples, independently computes signed cellular traces for every group element for \(8\le m\le20\), and checks surjectivity of the triangle-boundary map over three prime fields for \(8\le m\le13\). Both scripts terminate with an explicit PASS message when all assertions hold. The direct enumeration confirms \(244,570,1285,2838,6190\) nonempty simplices for \(m=8,9,10,11,12\), respectively. These finite checks are not a substitute for the all-\(m\) proof above.

## Relationship to prior work

Braun, *Independence Complexes of Stable Kneser Graphs*, arXiv:0912.0720v1, Theorem 1.4 and Section 3, proves the nonequivariant wedge-of-two-spheres result and identifies wheel and triangle facets. It determines the character degree but does not supply rotation or reflection traces. Schultz, *The equivariant topology of stable Kneser graphs*, arXiv:1003.5688v1, Sections 4–5, studies the dihedral action on the **graph Hom/box complex** \(\operatorname{Hom}(K_2,\operatorname{SG}_{n,k})\), which is a different complex from \(\operatorname{Ind}(\operatorname{SG}_{2,k})\). The present character is not obtained by substituting the box-complex action. A complete published-literature priority claim is not made.

## Limitations

The conclusion is a rational homology representation and its character, not an equivariant homotopy decomposition or an integral \(\mathbb Z[D_{2m}]\)-module classification. The argument uses a previously established nonequivariant concentration theorem; it does not repropose that theorem as new. Values with \(m<8\) lie outside scope. Unindexed equivalent calculations remain a bibliographic risk.

## References

1. Benjamin Braun, *Independence Complexes of Stable Kneser Graphs*, arXiv:0912.0720v1 (first public version 2009-12-03), Theorem 1.4 and Section 3, https://arxiv.org/pdf/0912.0720.
2. Carsten Schultz, *The equivariant topology of stable Kneser graphs*, arXiv:1003.5688v1 (first public version 2010-03-29), Sections 4 and 5, https://arxiv.org/pdf/1003.5688.

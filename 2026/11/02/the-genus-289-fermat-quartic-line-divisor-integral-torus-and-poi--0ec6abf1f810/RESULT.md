# The genus-289 Fermat quartic line divisor: integral torus and point-free arithmetic

## Finding

Let \(k=\mathbb F_q\) be a finite field of characteristic \(p\ge5\), and let
\(X\subset\mathbb P^3_k\) be the smooth Fermat quartic
\[
X_0^4+X_1^4+X_2^4+X_3^4=0.
\]
Let \(D\subset X\) be the reduced union of **all** its \(48\) geometric lines, regarded as a reduced projective curve over \(k\), and let \(J=\operatorname{Pic}^0_{D/k}\). Write \(C_n\) for a cyclic group of order \(n\). Then:

1. The curve \(D\) has exactly \(192\) ordinary double points and \(24\) ordinary quadruple points, with no other geometric singularities. Its arithmetic genus is \(289\).
2. The connected algebraic group \(J\) has a \(72\)-dimensional unipotent radical \(U\), a \(217\)-dimensional torus quotient \(T=J/U\), and no abelian-variety quotient. The torus has the following **integral isomorphism types over \(k\)**:
\[
T\cong
\begin{cases}
\mathbb G_m^{217},&q\equiv1\pmod8,\\
\mathbb G_m\times(\operatorname{Res}_{\mathbb F_{q^2}/\mathbb F_q}\mathbb G_m)^{108},&q\not\equiv1\pmod8.
\end{cases}
\]
3. For each such \(k\), there are **finite-abelian-group isomorphisms**
\[
J(\mathbb F_q)\cong
\begin{cases}
(\mathbb F_q,+)^{72}\times C_{q-1}^{217},&q\equiv1\pmod8,\\
(\mathbb F_q,+)^{72}\times C_{q-1}\times C_{q^2-1}^{108},&q\not\equiv1\pmod8.
\end{cases}
\]
4. The rational-point counts and Hasse–Weil zeta function of the *singular curve* itself are exactly
\[
\#D(\mathbb F_{q^n})=
\begin{cases}
48q^n-216,&q^n\equiv1\pmod8,\\
0,&q^n\not\equiv1\pmod8,
\end{cases}
\]
\[
Z(D/\mathbb F_q,t)=
\begin{cases}
\dfrac{(1-t)^{216}}{(1-qt)^{48}},&q\equiv1\pmod8,\\
\dfrac{(1-t^2)^{108}}{(1-q^2t^2)^{24}},&q\not\equiv1\pmod8.
\end{cases}
\]
In particular, the union of all geometric lines has **no base-field rational point** exactly when \(q\not\equiv1\pmod8\). The assertion is about the line divisor \(D\), not about the existence of rational points on \(X\).

## Assumptions and scope

Throughout, \(p\ge5\); the restriction avoids the inseparable characteristic-two quartic and the additional line configuration in characteristic three. For each of the three pair partitions \((ab\mid cd)\) of \(\{0,1,2,3\}\) and every \(\alpha,\beta\in\overline{k}\) satisfying \(\alpha^4=\beta^4=-1\), define
\[
L_{ab\mid cd}(\alpha,\beta):\qquad X_b=\alpha X_a,\quad X_d=\beta X_c.
\]
There are exactly \(3\cdot4^2=48\) such distinct lines. Singularities, dimensions and torus isomorphisms are geometric/scheme-theoretic assertions; rational-point groups and zeta functions are over the indicated finite field. Every count refers to the **reduced union**, not a nonreduced product or the ambient surface.

## Proof

**Completeness of the line list.** A line on \(X\) is given by four homogeneous binary linear forms \(l_i(s,t)\) satisfying \(\sum_i l_i^4=0\). In characteristic \(p>3\), the fourth powers of any \(r\le4\) pairwise nonproportional nonzero binary linear forms are linearly independent: after choosing affine slopes, the first \(r\) coefficients give a Vandermonde determinant multiplied by nonzero binomial coefficients \(\binom4j\). Consequently every nonzero direction occurs at least twice in a vanishing sum of at most four fourth powers. A parametrization of a line has at least two distinct directions, so the four forms split into two proportional pairs. The proportionality ratios have fourth powers \(-1\). This proves that the displayed \(48\) are all the geometric lines and that no additional ones occur for \(p\ge5\).

**Geometric incidences.** Fix a pairing. Two different lines of its \(16\)-line family meet precisely when they share the first or the second root parameter. In each of the two cases, four lines concur at a point supported on one coordinate pair. This gives eight ordinary fourfold points per family, hence \(24\) in total. For distinct pairings, a representative pair is given by
\[
X_1=\alpha X_0,\quad X_3=\beta X_2,\qquad
X_2=\gamma X_0,\quad X_3=\delta X_1.
\]
It meets if and only if \(\delta=\beta\gamma/\alpha\). Every ratio on the right again has fourth power \(-1\), so there are \(16\cdot4=64\) intersections for each unordered pair of line families. Such intersections have four nonzero coordinates and are distinct: all root ratios are uniquely determined by the point. The fourth-power coordinate pattern \((a,-a,-a,a)\) rules out a line of the third family unless \(2a=0\), impossible in odd characteristic. The points supported on only one coordinate pair cannot belong to another family. Thus there are \(3\cdot64=192\) ordinary nodes, \(24\) ordinary fourfold points and no other collisions. Because the quartic surface is smooth and all tangent directions of the distinct lines are distinct, the multiple points are ordinary as stated.

For an ordinary \(m\)-fold point, \(\delta=m(m-1)/2\). Normalizing all \(48\) projective lines therefore gives
\[
p_a(D)=192+24\binom42-48+1=289.
\]
This also agrees with adjunction on the K3 surface: the divisor has \(336\) pairwise line intersections counted with multiplicity, so \(D^2=2\cdot336-48\cdot2=576\) and \(p_a=1+D^2/2=289\).

**Normalization graph and local Picard groups.** Form the bipartite incidence graph \(\Gamma\) with one vertex for each of the \(48\) components, one for each of the \(216\) singular geometric points, and one edge for each branch of the normalization above a singularity. It is connected, has \(264\) vertices and \(192\cdot2+24\cdot4=480\) edges. Therefore \(\operatorname{rank} H_1(\Gamma,\mathbb Z)=480-264+1=217\). The normalization exact sequence for unit sheaves identifies the character lattice of the torus quotient of \(\operatorname{Pic}^0_D\) with \(H_1(\Gamma,\mathbb Z)\), up to the harmless integral dual convention (both modules used below are self-dual). Since every normalized component is \(\mathbb P^1\), there is no abelian quotient.

At a node, the local normalization-unit quotient is a one-dimensional torus. At an ordinary quadruple point it has torus rank \(4-1=3\) and a unipotent quotient of dimension \(\binom42-3=3\). Thus the connected unipotent radical has dimension \(24\cdot3=72\). The normalization conductor along each branch of an ordinary quadruple point is the cube of the branch parameter; therefore the local unipotent group is a quotient of principal units modulo those of degree at least three. Since \(p\ge5\), the truncated logarithm identifies its principal-unit group with an additive vector group. The resulting local unipotent group has exponent \(p\), and so does \(U(\mathbb F_q)\). As \(U\) is smooth, connected and unipotent over the finite field, it has exactly \(q^{72}\) rational points. Hence \(U(\mathbb F_q)\cong(\mathbb F_q,+)^{72}\) as abstract abelian groups.

**Integral Frobenius module.** Let \(R=\{\alpha:\alpha^4=-1\}\). The cyclic group \(\mathbb F_q^\times\) contains \(R\) exactly when \(q\equiv1\pmod8\). In that case Frobenius fixes every component, singular point and branch, so \(H_1(\Gamma,\mathbb Z)\cong\mathbb Z^{217}\) with trivial action, proving the split-torus case.

If \(q\not\equiv1\pmod8\), all \(48\) lines are defined over \(\mathbb F_{q^2}\), and Frobenius exchanges their parameters in two-cycles; no root of \(-1\) is individually fixed. Each ordinary fourfold point is labeled by one root in \(R\), so none is fixed. Each node is incident to exactly one line in each of two distinct pairing families, and Frobenius preserves these families: if a node were fixed, both lines would be fixed, a contradiction. Thus Frobenius acts **freely** as an involution on all vertices and edges of \(\Gamma\). The quotient graph is connected with \(132\) vertices and \(240\) edges, hence first Betti number \(109\).

Here is the needed **integral**, not merely rational, graph lemma. If \(\Gamma\to H\) is a connected regular double cover of a connected finite graph, let \(r=b_1(H)\). Contract a spanning tree in \(H\) and its two disjoint lifts. The cover then comes from \(r\) loop generators and a nonzero homomorphism from the free group on those loops to \(\mathbb Z/2\). Nielsen changes of free generators reduce that homomorphism to a single generator with odd voltage and the other \(r-1\) generators with even voltage. The lifted first generator is one two-edge cycle invariant under the deck involution; each remaining generator contributes a swapped pair of loops. Thus, **as integral involution modules**,
\[
H_1(\Gamma,\mathbb Z)\cong\mathbb Z_{+}\oplus\mathbb Z[\mathbb Z/2]^{r-1}.
\]
Substituting \(r=109\) gives \(\mathbb Z_+\oplus\mathbb Z[\mathbb Z/2]^{108}\). The corresponding torus is \(\mathbb G_m\times(\operatorname{Res}_{\mathbb F_{q^2}/\mathbb F_q}\mathbb G_m)^{108}\), establishing the non-split torus claim over the base field.

The rational-point exact sequence \(1\to U(k)\to J(k)\to T(k)\to1\) is surjective on the right by Lang's theorem for \(U\). The order of \(T(k)\) is prime to \(p\), and \(J(k)\) is abelian, so its \(p\)-primary Sylow subgroup is exactly \(U(k)\) and splits off from its prime-to-\(p\) counterpart as an abstract finite group. Finally \(\operatorname{Res}_{\mathbb F_{q^2}/\mathbb F_q}\mathbb G_m(k)=\mathbb F_{q^2}^\times\), a cyclic group of order \(q^2-1\). This proves the two displayed group structures without asserting a nontrivial algebraic-group extension splits canonically.

**Zeta function.** Every line and every singular point is defined over \(\mathbb F_q\) when \(q\equiv1\pmod8\), and otherwise all have degree two. The normalization zeta function is the product of the \(48\) line zeta functions, grouped into Frobenius orbits. At a singular point with \(m\) rational branches, the normalization-to-curve correction contributes \((1-t)^{m-1}\), with \(t\) replaced by \(t^2\) for an orbit of length two. The \(192\) nodes contribute exponent \(192\) in the split case and \(96\) in the quadratic case; the \(24\) fourfold points contribute exponents \(72\) and \(36\), respectively. Combining these corrections with the \(48\) split or \(24\) quadratic-orbit projective lines proves both rational zeta functions.

Independently, a \(k\)-rational point of \(D\) lies in the union of the three complete intersections given by
\[
X_a^4+X_b^4=X_c^4+X_d^4=0.
\]
For \(q\not\equiv1\pmod8\), no nonzero pair of \(k\)-coordinates can satisfy \(u^4+v^4=0\), so the curve has no rational point. In the split case, inclusion-exclusion over the \(48\) rational lines, subtracting \(1\) per node and \(3\) per quadruple point, gives \(48(q+1)-192-72=48q-216\). The same argument over every extension proves the displayed point-count formula.

## Verification

The standalone file `verify.py` constructs all \(48\) lines over \(\mathbb F_{17}\) using a primitive eighth root of unity, computes all \(1128\) unordered line pairs by exact modular row reduction, and reconstructs the \(216\) singular supports, their multiplicities, the connected incidence graph, the \(480\) branches and its Betti number. It computes Frobenius permutations for all \(q\bmod8\in\{1,3,5,7\}\), checks free involution actions in the nonsplit cases, and independently enumerates rational points over the prime fields of orders \(5,7,11,13,17,19,23,41\) using the complete-intersection description. A second standalone verifier `verify_characteristic_five.py` constructs all lines over \(\mathbb F_{25}\) and independently checks their \(192\) nodes and \(24\) ordinary quadruple points in the smallest allowed characteristic.

Running `python verify.py` completes with `VERIFY_OK` and agrees with `verification_output.txt`. The geometric all-characteristics statement rests on the symbolic parametrization and incidence proof, not on one finite-field sample. The torus classification rests on the integral graph-cover lemma; enumerated orbit counts alone do not prove an integral lattice decomposition.

## Relationship to prior work

Segre's classical work on the Fermat quartic concerns its geometric lines and configurations. Shimada and Shioda, *On a smooth quartic surface containing 56 lines which is isomorphic as a K3 surface to the Fermat quartic* (arXiv:1604.06265, first posted 2016-04-21), Section 3, explicitly give the \(48\) line labels, the \(24\) common four-line tangent-plane points, and the cyclotomic Galois action. They do **not**, in the inspected section or the document's statement of results, evaluate the connected generalized Jacobian of the entire line divisor over finite fields, its integral rank-\(217\) Frobenius torus, or the finite abelian group isomorphism classes above. Veniani, *Lines on K3 quartic surfaces in characteristic 3* (arXiv:1608.04209, first posted 2016-08-15), describes the characteristic-three exceptional \(112\)-line situation, which this theorem expressly excludes. Classical normalization and generalized-Jacobian theory supplies the abstract Picard description; the explicit arithmetic evaluation of the canonical \(48\)-line divisor is the contribution assessed here.

## Limitations

This result is confined to \(p\ge5\). It does not classify the additional lines in characteristic three, give the zeta function of the ambient K3 surface, or determine the Picard component group. The finite-abelian-group splittings are abstract; no canonical splitting of the algebraic-group extension is claimed. Literature overlap searches cannot establish universal historical priority, and a specialized earlier account of these arithmetic Picard groups remains a residual risk. Independent external mathematical validation has not been performed.

## References

- I. Shimada and T. Shioda, *On a smooth quartic surface containing 56 lines which is isomorphic as a K3 surface to the Fermat quartic*, arXiv:1604.06265 (initial public version 2016-04-21), Section 3.
- D. C. Veniani, *Lines on K3 quartic surfaces in characteristic 3*, arXiv:1608.04209 (initial public version 2016-08-15), Introduction.
- B. Segre, *On the quartic surface* \(x_1^4+x_2^4+x_3^4+x_4^4=0\), 1944, cited and reviewed in Shimada–Shioda.
- M. Rosenlicht, *Generalized Jacobian varieties*, Ann. of Math. 59 (1954), 505–530 (general background on singular-curve Jacobians).

# Finite-field twists and integral Picard tori of the fifteen-line Igusa boundary

## Finding
Let \(k=\mathbb F_q\) have characteristic \(p>3\). On the Igusa quartic
\[
I:\quad \sum_{i=1}^6 X_i=0,\qquad
\left(\sum_{i=1}^6 X_i^2\right)^2-4\sum_{i=1}^6 X_i^4=0,
\]
let \(D\) be the **reduced** union of its fifteen classical syntheme lines. For every permutation \(\sigma\in S_6\), let \(D_\sigma\) denote the finite-field form obtained by the corresponding coordinate-permutation Frobenius descent. This is a geometrically connected, seminormal curve of arithmetic genus \(16\); its connected Picard scheme is a \(16\)-dimensional algebraic torus.

Let \(s_d\), \(u_d\), and \(f_d\) count the length-\(d\) Frobenius orbits, respectively, on the fifteen syntheme lines, the fifteen triple points indexed by duads, and the forty-five line–point branches (flags). Then the **complete zeta function**, valid for every integer extension degree, is
\[
Z(D_\sigma,T)=\prod_{d\ge1}\frac{(1-T^d)^{f_d-s_d-u_d}}{(1-q^dT^d)^{s_d}},
\qquad \#D_\sigma(k)=(q+1)s_1+u_1-f_1.
\]
The eleven conjugacy classes of \(S_6\) yield exactly **nine distinct zeta functions**. Precisely the five-cycle class (cycle type \((5,1)\), consisting of \(144\) group elements) gives a curve without \(k\)-points. For this class,
\[
Z(D_\sigma,T)=\frac{(1-T^5)^3}{(1-q^5T^5)^3},\qquad
\operatorname{Pic}^0(D_\sigma)\simeq
\mathbb G_m\times\bigl(\operatorname{Res}_{\mathbb F_{q^5}/k}\mathbb G_m\bigr)^3,
\]
and, as finite abelian groups,
\[
\operatorname{Pic}^0(D_\sigma)(k)\simeq C_{q-1}\times C_{q^5-1}^{\,3}.
\]
The torus statement is an **isomorphism over \(k\)**, not only an isogeny or group-order formula. Some distinct classes have identical zeta functions but different Frobenius orbit distributions on the singular locus: types \((2,2,1,1)\) and \((2,1,1,1,1)\) provide an example. The complete eleven-type table is in `s6_orbit_table.csv`.

## Assumptions and scope
A *duad* is a two-element subset of \(\{1,\ldots,6\}\). A *syntheme* is a partition of this six-element set into three duads. For each syntheme \(s=\{\{a,b\},\{c,d\},\{e,f\}\}\), the corresponding projective line \(L_s\) has coordinates \(X_a=X_b=A\), \(X_c=X_d=B\), \(X_e=X_f=C\), subject to \(A+B+C=0\). A flag is \((s,d)\) with duad \(d\in s\).

All claims concern this reduced curve and its forms under the **specified coordinate \(S_6\)-action**; they do not purport to classify every form under possibly larger automorphism groups. The characteristic restriction \(p>3\) ensures the stated incidence and tangent configuration. The torus statement concerns the connected Picard scheme, not its disconnected multidegree components. A type \((5,1)\) form exists over every finite field by descent from the indicated Galois cocycle.

## Proof
**Geometric configuration.** A syntheme line lies on \(I\) because \(A+B+C=0\) implies \((A^2+B^2+C^2)^2=2(A^4+B^4+C^4)\), and the quartic equation restricts to twice the left expression minus four times the second sum. Its six partial derivatives agree along that line, showing the line belongs to the singular locus on the invariant hyperplane. Distinct syntheme lines meet if and only if their synthemes share a duad. For each duad, the three containing synthemes meet at the point with coordinates \(-2,-2,1,1,1,1\), placed in the matching slots. There are exactly fifteen such points and forty-five branches; every other pair of lines is disjoint.

The exhaustive integral calculation in `verify_igusa.py` constructs two spanning vectors for each of the fifteen lines and examines all \(105\) pairs. For the sixty disjoint pairs, the greatest common divisor of all nonzero \(4\)-row maximal minors is \(3\), so they stay disjoint whenever \(p>3\); the other forty-five pairs are exactly the shared-duad pairs. At each triple point, three local tangent directions are linearly independent modulo its radial vector: the relevant integer maximal minors have greatest common divisor a power of \(2\). Thus these three branches have independent tangents for \(p>3\). After formal coordinate change, the reduced completed local curve is the union of three coordinate axes. Its normalization quotient has length \(2\) and its units-gluing quotient is a two-dimensional torus (without a unipotent part). Consequently \(p_a(D)=15(2)-15+1=16\), and the connected Picard torus has dimension \(16\).

**Normalization and zeta.** The normalization is the disjoint union of the fifteen geometric \(\mathbb P^1\)'s. Its preimages of the fifteen triple points are the forty-five flags. On every finite extension, normalization identifies the counted points by subtracting flags and adding triple points:
\[
\#D_\sigma(\mathbb F_{q^n})=\sum_{s\text{ fixed by }\sigma^n}(q^n+1)
+\#\operatorname{Fix}(\sigma^n|\text{duads})-\#\operatorname{Fix}(\sigma^n|\text{flags}).
\]
Taking exponential generating series for these counts gives the displayed zeta product. Its first coefficient gives the displayed formula for rational points.

**Exhaustive conjugacy-class calculation.** For every one of the eleven partitions of six, choose a permutation representative. Enumerate its orbits on the fifteen synthemes, fifteen duads and forty-five flags, and form the rational function above. The standalone script checks all eleven cases and all \(720\) individual permutations, verifies exactly \(144\) five-cycles have no fixed component or triple point, and finds nine distinct complete zeta signatures. Every non-five-cycle permutation has a fixed syntheme or a fixed duad (and hence a rational point; a fixed line is \(\mathbb P^1_k\)), whereas a five-cycle fixes neither. For the five-cycle, all syntheme/duad orbits have length five and the flag orbits have length five, with multiplicities \(3,3,9\), respectively.

**Integral character lattice.** Let \(\Gamma\) be the bipartite incidence graph with syntheme/duad vertices and flags as edges. It is connected, and its integral cycle lattice is free of rank \(45-30+1=16\). The normalization exact sequence identifies the torus character lattice with \(H_1(\Gamma,\mathbb Z)\). For a five-cycle, the group \(C_5\) acts freely on the vertices and edges, and the quotient graph has six vertices, nine edges, and first Betti number four. Contract the lifts of a spanning tree of the quotient; this reduces the graph equivariantly to a single \(C_5\)-orbit of vertices with four edge orbits. Its integral boundary homomorphism is a row \((h_1-1,h_2-1,h_3-1,h_4-1)\) over \(\mathbb Z[C_5]\), with at least one \(h_i\) generating \(C_5\) because the covering graph is connected. Rechoose the quotient free loops and use integral elementary changes of edge-orbit generators so that the boundary becomes \((h-1,0,0,0)\). The kernel is therefore
\[
H_1(\Gamma,\mathbb Z)\simeq
\mathbb Z\oplus \mathbb Z[C_5]^3
\]
**integrally**, with the first summand fixed by Frobenius. The multiplicative-type classification and Weil restriction identify the asserted \(k\)-torus. Taking rational points gives its cyclic decomposition.

## Verification
Running `python3 verify_igusa.py` from the directory containing the CSV recreates `s6_orbit_table.csv` and prints `VERIFY_OK`. The exact integer determinant computations check all line pairs and tangent triples. The script also independently enumerates all \(720\) permutations and their orbits, verifies the eleven-case/nine-zeta enumeration, explicitly constructs the five-cycle graph quotient, and directly enumerates rational points on the untwisted union over \(\mathbb F_5\) and \(\mathbb F_7\). The recorded output is supplied in `verify_igusa_output.txt`. These finite checks do not substitute for the infinite-field normalization and covering-graph arguments above.

## Relationship to prior work
The symmetric fifteen-line geometry of the Igusa quartic is classical. Prokhorov, *Fields of invariants of finite linear groups*, Lemma 3.16 and Lemma 3.17 (arXiv:0707.1738), identifies the \(S_6\)-equivariant fifteen-line configuration and its equations. Rito, arXiv:1310.4071, describes the singular lines and related geometry. Bruin–Kulkarni, arXiv:2309.01959, treat Igusa-quartic twists and the line configuration in genus-four Jacobian geometry. These geometric inputs are **not** claimed as new. The assessed arithmetic contribution is the evaluated eleven-class zeta spectrum, the point-free criterion, and the explicit **integral** five-cycle Picard torus. Searches of these sources did not reveal these exact evaluated statements. Classical graph normalization makes them derivable in principle; historical priority is not asserted as definitive.

## Limitations
Only \(p>3\) and forms under the specified \(S_6\) coordinate action are covered. The computations establish the actual fifteen chosen lines and their incidences; the claim does not require that the entire singular scheme of the quartic have no additional characteristic-dependent components. The group isomorphism is supplied for the five-cycle class, not for all eleven torus isomorphism classes. The eleven-case table classifies **formal arithmetic forms** under the indicated descent, not geometric moduli equivalence beyond that action. All mathematical evaluation has been internal; no independent audit has been performed. Priority could be affected by older literature on the Cremona–Richmond configuration or integral graph tori.

## References
1. Yu. G. Prokhorov, *Fields of invariants of finite linear groups*, arXiv:0707.1738 (first public version 2007-07-12), Lemmas 3.16–3.17.
2. C. Rito, *Cuspidal quintics and surfaces with \(p_g=0\), \(K^2=3\) and 5-torsion*, arXiv:1310.4071 (2013), the Igusa-quartic configuration discussion.
3. N. Bruin and A. Kulkarni, *On (2,2)-decomposable genus 4 Jacobians*, arXiv:2309.01959 (2023), section on twisted Igusa quartics.

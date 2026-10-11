# Dihedral homology characters and quotient congruences for cycle matching complexes

## Finding

For every integer \(n\geq3\), let \(X_n=\mathcal M(C_n)\), the simplicial complex of matchings in the ordinary, simple \(n\)-cycle. Label the cycle edges \(e_j\) by \(j\in\mathbb Z/n\mathbb Z\) in cyclic order. The dihedral group \(D_n=\langle r,s\mid r^n=s^2=1,\ srs=r^{-1}\rangle\) acts through \(r(e_j)=e_{j+1}\) and \(s(e_j)=e_{-j}\). Write \(q_n=\lfloor(n-2)/3\rfloor\) if \(n\equiv2\pmod3\), and \(q_n=\lfloor(n-3)/3\rfloor\) otherwise. Equivalently, \(q_{3k}=q_{3k+1}=k-1\) and \(q_{3k+2}=k\). Define the integer-valued period-six sequences

\[
P_m=(1,0,-1,-1,0,1)_{m\bmod6},\qquad
Q_d=(2,1,-1,-2,-1,1)_{d\bmod6}.
\]

The only nonzero reduced rational homology of \(X_n\) occurs in degree \(q_n\), with rank \(2\) when \(3\mid n\) and rank \(1\) otherwise. Its **entire rational dihedral character** \(\chi_n(g)=\operatorname{tr}(g\mid\widetilde H_{q_n}(X_n;\mathbb Q))\) is specified, with \(\gcd(n,0)=n\), by

\[
(-1)^{q_n}\chi_n(r^a)=-Q_{\gcd(n,a)}\quad(0\leq a<n),
\]
\[
(-1)^{q_n}\chi_n(sr^a)=
\begin{cases}
-P_{(n-1)/2},&n\text{ odd},\\
-P_{n/2+1},&n\text{ even and }a\text{ even},\\
-P_{n/2-2},&n\text{ even and }a\text{ odd}.
\end{cases}
\]

Here \(sr^a\) acts on edge labels as \(j\mapsto-j-a\); parity alone determines its even-length reflection conjugacy class, so the formula is unaffected by the sign of the exponent. The cyclic and full dihedral quotients consequently satisfy, for every \(i\geq0\),

\[
\dim_{\mathbb Q}\widetilde H_i(|X_n|/\langle r\rangle;\mathbb Q)=
\begin{cases}1,&i=q_n,\ \gcd(n,6)=1,\\0,&\text{otherwise},\end{cases}
\]
\[
\dim_{\mathbb Q}\widetilde H_i(|X_n|/D_n;\mathbb Q)=
\begin{cases}1,&i=q_n,\ n\equiv1\text{ or }11\pmod{12},\\0,&\text{otherwise}.\end{cases}
\]

These are rational-homology classifications; zero reduced rational homology is not asserted to imply contractibility or integral acyclicity.

## Assumptions and scope

An \(n\)-cycle is the simple graph with edges \(e_j=\{j,j+1\}\) modulo \(n\), including the ordinary triangle at \(n=3\). A matching is an edge set with no shared endpoints, equivalent to an independent set in the line graph \(L(C_n)\cong C_n\). Thus \(X_n=\operatorname{Ind}(C_n)\), where the vertices of this last cycle are the labels \(j\) of original graph edges. The axis descriptions in the proof refer to these **edge labels**, not to the original polygon's vertex labels. Homology coefficients in the character and quotient statements are \(\mathbb Q\); the homotopy concentration input is integral. The modulus cases include \(n=3,4,5\) and all larger \(n\).

## Proof

**1. Homology concentration.** The three initial complexes are \(X_3\), three isolated vertices and hence \(\bigvee^2 S^0\); \(X_4\), two disjoint edges and hence \(S^0\); and \(X_5\), a pentagon and hence \(S^1\). A known cycle-independence recurrence (Adamaszek, *Clique complexes and graph powers*, Example 6.3; also the four-edge path contraction in Bayer–Jelić Milutinović–Vega, Proposition 7) gives \(X_n\simeq\Sigma X_{n-3}\) for \(n\geq6\). Its hypotheses hold because the selected four-edge path in the simple cycle has internal graph vertices of degree two and distinct endpoints. Consequently \(\widetilde H_i(X_n;\mathbb Z)\) is free and concentrated at \(i=q_n\), with the stated rank. This nonequivariant fact is a literature input, not claimed new.

**2. Signed simplicial Lefschetz sum.** For a vertex permutation \(g\) preserving the complex, the reduced chain Lefschetz number is
\[
\mathcal L_n(g)=\sum_{i\geq0}(-1)^i\operatorname{tr}(g\mid\widetilde H_i(X_n;\mathbb Q))
=-\sum_{I\subseteq\{0,\dots,n-1\}\atop I\text{ independent},\ gI=I}(-1)^{o_g(I)},
\]
where \(o_g(I)\) counts the \(g\)-orbits contained in \(I\), including \(I=\varnothing\) with \(o_g(\varnothing)=0\). Indeed, if \(I\) has \(t\) elements and \(u\) such orbits, the orientation of the induced permutation on its ordered simplex has sign \((-1)^{t-u}\), while its reduced chain degree is \(t-1\); the signed contribution is \((-1)^{u-1}\). The empty face supplies the same value \(-1\). A union of vertex orbits is independent precisely when none contains an adjacency internally and no two selected orbits are adjacent. Let \(B_g\) be the graph of individually admissible vertex orbits, with an edge joining two orbits whenever the cycle has an edge between them. The preceding sum equals \(-I(B_g,-1)\), where \(I(B,z)\) is the independent-set polynomial (including the empty independent set).

**3. Orbit graphs and their exact evaluations.** For a rotation \(r^a\), put \(d=\gcd(n,a)\). The vertex orbits are congruence classes modulo \(d\). When \(d\geq3\), no orbit contains adjacent vertices and \(B_{r^a}=C_d\). When \(d=2\), it is a single edge (the two orbit classes), and when \(d=1\), the sole orbit is inadmissible, leaving an empty graph. Write \(P_m=I(P_m,-1)\) for a path on \(m\) vertices, with the empty path assigned \(P_0=1\). Deletion of an endpoint yields \(P_m=P_{m-1}-P_{m-2}\), with \(P_0=1,P_1=0\), giving the displayed period-six sequence. For \(d\geq3\), conditioning on one cycle vertex gives \(I(C_d,-1)=P_{d-1}-P_{d-3}=Q_d\); direct inspection of \(d=1,2\) gives the same \(Q_d\). Hence \(\mathcal L_n(r^a)=-Q_d\).

For a reflection, relabeling by a rotation reduces the orbit geometry to one of three types. When \(n\) is odd, there is one fixed edge-label vertex; at the opposite axis, precisely one transposition pair contains two adjacent labels and must be discarded. The remaining admissible orbit graph is the path on \((n-1)/2\) vertices. When \(n=2m\) and the reflection fixes two opposite edge-label vertices, all \(m+1\) orbits are admissible and form \(P_{m+1}\). When \(n=2m\) and it fixes no edge-label vertex, precisely the two terminal transposition pairs are internally adjacent and inadmissible, leaving \(P_{m-2}\). These statements include the empty graph \(P_0\) at \(n=4\). Every incidence follows from the cycle adjacencies between successive orbit classes, with no extra incidences. The reflection character formulas follow from \(\mathcal L=-I(B_g,-1)\). Since all reduced homology lies in degree \(q_n\), \(\mathcal L_n(g)=(-1)^{q_n}\chi_n(g)\), which proves the complete character.

**4. Rational orbit-space homology.** For a finite simplicial \(G\)-complex, barycentric subdivision removes simplex inversions: stabilizers fix a chain of faces pointwise. The rational cellular chains of the quotient identify with coinvariants of the subdivided chain complex, hence with invariants by averaging. Exactness of rational invariants yields
\[
\widetilde H_i(|X_n|/G;\mathbb Q)\cong\widetilde H_i(X_n;\mathbb Q)^G
\]
for \(G=\langle r\rangle\) and \(G=D_n\). In both cases the reduced invariant rank is the character average. The period-six values satisfy
\[
Q_d=1-2\mathbf 1_{2\mid d}-3\mathbf 1_{3\mid d}+6\mathbf 1_{6\mid d}.
\]
As \(a\) runs modulo \(n\), exactly \(n/k\) exponents have \(k\mid\gcd(n,a)\) if \(k\mid n\), and none otherwise. Therefore
\[
\sum_{a=0}^{n-1}Q_{\gcd(n,a)}=n(1-\mathbf1_{2\mid n})(1-\mathbf1_{3\mid n}).
\]
When \(\gcd(n,6)=1\), the homology degree \(q_n\) is odd, so the average of \(-Q_{\gcd(n,a)}\) multiplied by \((-1)^{q_n}\) is exactly \(1\). Otherwise the cyclic average is zero. For even \(n=2m\), half the reflections have signed Lefschetz number \(-P_{m+1}\) and half \(-P_{m-2}\), which cancel by \(P_{j+3}=-P_j\). For odd \(n\), every reflection contributes \(-P_{(n-1)/2}\); among odd lengths coprime to six, its resulting homology character is \(+1\) when \(n\equiv1,11\pmod{12}\), and \(-1\) when \(n\equiv5,7\pmod{12}\). This gives the two quotient formulas.

## Verification

The included standalone `verify.py` enumerates independent subsets, tests their invariance under all \(2n\) dihedral permutations, computes the exact simplicial orientation sign, and compares the resulting signed chain Lefschetz number with the displayed formulas for \(3\leq n\leq16\). It makes 266 exact character comparisons and accounts for 8,742 fixed oriented faces; it separately averages the predicted characters to check both quotient congruences. For \(3\leq n\leq12\), it also constructs all independent-set boundary operators and computes their ranks over \(\mathbb F_2\), checking the predicted reduced Betti vector in 10 complete finite instances. Running `python3 verify.py` prints `VERIFY_OK` followed by counts. The finite computations are consistency checks; the recurrence, orbit-graph classification, and averaging argument prove the unbounded statements.

## Relationship to prior work

Bayer, Jelić Milutinović and Vega's *Matching Complexes of Outerplanar Graphs* (first made public 2024-11-07), Theorem 2 and Proposition 7, supplies recent motivation and a broad nonequivariant homotopy/edge-contraction framework. It does not determine symmetry representations or orbit-space homology. The exact cyclic homology ranks and suspension are also already in Adamaszek's *Clique complexes and graph powers* (2011 preprint, Section 6, Example 6.3). Neither ranks nor the cycle homotopy type are claimed new.

An especially close comparison is Adamaszek, Adams, Frick, Peterson and Previte-Johnson, *Nerve complexes of circular arcs* (2014), Section 7: it explicitly determines dihedral homology representations, **but for the different nerve complexes** \(\mathcal N(n,k)\). Its Section 8 determines nonequivariant homotopy types of cycle-power clique complexes and gives a homotopy equivalence to nerves on a different number of vertices, without furnishing a dihedral-equivariant equivalence. For odd \(n\), multiplication by two modulo \(n\) even identifies the abstract complexes \(\operatorname{Ind}(C_n)\cong\operatorname{Cl}(C_n^{(n-3)/2})\), after reparametrizing the dihedral action. This is a genuine overlap with the cycle-power family, not an identification with the nerves whose dihedral characters were computed. The present calculation independently treats the actual natural dihedral action on \(\operatorname{Ind}(C_n)\), including even \(n\), and yields explicit quotient congruences. An equivalent result might exist outside the examined literature.

## Limitations

The action and quotient calculations are over \(\mathbb Q\) and make no claim about integral group representations, homotopy type of the quotients, higher operations, or contractibility of rationally acyclic quotients. The argument does not establish a dihedral-equivariant homotopy wedge decomposition. The fixed finite computations do not certify infinitely many instances on their own. No claim of exhaustive coverage of inaccessible or unpublished literature is made.

## References

1. M. Bayer, M. Jelić Milutinović and J. Vega, *Matching Complexes of Outerplanar Graphs*, arXiv:2411.04601 (v1 dated 2024-11-07; v2 2026-09-23), especially Theorem 2 and Proposition 7. https://arxiv.org/abs/2411.04601
2. M. Adamaszek, *Clique complexes and graph powers*, arXiv:1104.0433 (first publicly posted 2011-04-03), Section 6, Example 6.3, and Appendix. https://arxiv.org/abs/1104.0433
3. M. Adamaszek, H. Adams, F. Frick, C. Peterson and C. Previte-Johnson, *Nerve complexes of circular arcs*, arXiv:1410.4336 (first publicly posted 2014-10-16), Sections 7–8. https://arxiv.org/abs/1410.4336

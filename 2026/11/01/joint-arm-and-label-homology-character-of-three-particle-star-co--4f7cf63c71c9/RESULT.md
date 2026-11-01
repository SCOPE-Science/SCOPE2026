# Joint arm-and-label homology character of three-particle star configurations

## Finding

Let \(S_m\) be the metric star with \(m\geq3\) unit-length arms, one common central endpoint, and distinct outer endpoints. Its ordered collision-free three-point configuration space is
\[
F_3(S_m)=\{(x_1,x_2,x_3)\in S_m^3:x_i\ne x_j\text{ whenever }i\ne j\}.
\]
The arm-permutation group \(\mathfrak S_m\) commutes with the label-permutation group \(\mathfrak S_3\). Put \(c_j(\sigma)\) for the number of cycles of length \(j\) of \(\sigma\in\mathfrak S_m\), and write \(f=c_1(\sigma)\). The complete rational character of their joint action on first homology is
\[
\boxed{\operatorname{tr}\!\left((\sigma,\tau)\mid H_1(F_3(S_m);\mathbb Q)\right)=
\begin{cases}
1+f(f+1)(2f-5),&\tau=\mathrm{id},\\
1-2c_2(\sigma),&\tau\text{ is a transposition},\\
1-3c_3(\sigma),&\tau\text{ is a three-cycle}.
\end{cases}}
\]
In particular, the character distinguishes the label-sign and label-standard sectors in addition to the already accessible unordered sector. For \(m\geq3\), all reduced rational homology of the arm-symmetry quotient vanishes:
\[
\widetilde H_*(F_3(S_m)/\mathfrak S_m;\mathbb Q)=0.
\]
The alternating-arm quotient instead has first rational Betti number \(5\) for \(m=3\), \(2\) for \(m=4\), and \(0\) for every \(m\geq5\). All these quotients have no higher rational homology.

## Assumptions and scope

The three particles are labeled and cannot coincide, including at the central vertex. Every arm is an ordinary closed interval of the same positive length. An arm permutation sends each interval linearly to the corresponding interval, preserving its radial coordinate. A label permutation rearranges the three coordinates. The result holds for every integer \(m\ge3\), every \(\sigma\in\mathfrak S_m\), and every \(\tau\in\mathfrak S_3\). Homology characters and quotient homology use rational coefficients; the underlying first integral homology is free abelian. The phrase 'arm quotient' denotes the ordinary geometric orbit space, not a Borel construction.

The previously known homotopy type \(F_3(S_m)\simeq\bigvee^{1+m(m+1)(2m-5)}S^1\), its Euler characteristic, and the all-particle-number homology representation of *unlabeled* star configurations are not asserted as new. The present claim is the complete *joint* character, in particular its nontrivial particle-label sectors, and the alternating-arm exception.

## Proof

**1. Homological reduction.** Ghrist's radial-tree theorem (1999, Section 4, Proposition 4.1) gives a connected graph as a deformation retract of \(F_3(S_m)\); hence \(H_i=0\) for \(i\ge2\), \(H_0\cong\mathbb Q\) with trivial group action, and
\[
\dim H_1=1+m(m+1)(2m-5).
\]
The action of the finite group \(\mathfrak S_m\times\mathfrak S_3\) on this configuration space has a finite equivariant CW homotopy model: the graph is semialgebraic, its ordered configuration space is semialgebraic, and the action is semialgebraic. For finite-order maps, the equivariant Euler/Lefschetz identity therefore gives
\[
1-\operatorname{tr}((\sigma,\tau)\mid H_1)=\chi\bigl(F_3(S_m)^{(\sigma,\tau)}\bigr).
\]
Here \(\chi\) is ordinary homotopy Euler characteristic, rather than compact-support Euler characteristic.

**2. Nonidentity label permutations.** If \(\tau\) transposes two labels and fixes the third, a fixed configuration forces the exchanged points to form a two-element orbit of the arm permutation at a common positive radial coordinate. The remaining particle lies in the fixed-point subtree \(S_m^\sigma\), which is a contractible star on the \(f\) fixed arms (a single central point if \(f=0\)). Thus the fixed set is a disjoint union of \(2c_2(\sigma)\) copies of \((0,1]\times S_m^\sigma\), each of Euler characteristic one. If \(\tau\) is a three-cycle, all three points form a length-three arm orbit and have a common positive radial coordinate. The fixed set is \(3c_3(\sigma)\) disjoint copies of \((0,1]\). Substitution into the Lefschetz identity proves the second and third character lines. No cycle longer than the corresponding label cycle contributes: a noncentral point must be fixed by the appropriate power of \(\sigma\).

**3. Identity label permutation.** When \(\tau=\mathrm{id}\), every particle is individually fixed by \(\sigma\). Therefore the fixed configuration space is \(F_3(S_f)\), interpreting \(S_0\) as the single central point. To calculate its Euler characteristic directly, subdivide each arm into three edges and use the standard Abrams cubical model: its cells are ordered triples of open vertices or edges with pairwise disjoint *closed* supports. This subdivision is sufficient for three particles on a radial tree.

Let \(z\) mark the number of occupied graph cells and give each chosen edge-cell weight \(-z\), each vertex-cell weight \(+z\). For one arm with its edge adjacent to the center excluded, the weighted independence polynomial of its three noncentral vertices and two remaining edges is
\[
A(z)=1+z+z^2+z^3=(1+z)(1+z^2).
\]
If the center-adjacent edge is selected, its contribution together with all allowed remaining cells on that arm is
\[
B(z)=-z(1+z+z^2).
\]
At most one center-adjacent edge can be selected; if no such edge is selected, the central vertex can independently be selected or omitted. Consequently the weighted generating polynomial for *unlabeled* selections of pairwise disjoint cell supports is
\[
P_f(z)=(1+z)A(z)^f+fB(z)A(z)^{f-1}.
\]
For \(f=0\), the second summand is interpreted as zero. Labeling the three selected cells has \(3!\) choices, so the alternating sum of the actual cubical-cell counts is
\[
\chi(F_3(S_f))=6[z^3]P_f(z)=-f(f+1)(2f-5).
\]
The coefficient identity follows by expanding \(A(z)^f\) to third degree; it is valid also for \(f=0,1,2\), including the disconnected configuration spaces of intervals. The Lefschetz identity now gives the first character line.

**4. Quotients and the label-isotypic refinement.** Finite-group rational transfer identifies rational homology of a geometric quotient with invariants in the original rational homology. Write \(g(f)=f(f+1)(2f-5)\). For uniformly random \(\sigma\in\mathfrak S_m\), the falling-factorial moments satisfy \(\mathbb E (f)_j=1\) for \(j\le m\). Since
\[
g(f)=2(f)_3+3(f)_2-6(f)_1,
\]
we have \(\mathbb E g(f)=-1\) for every \(m\ge3\). Therefore the \(\mathfrak S_m\)-invariant part of first homology has dimension \(\mathbb E(1+g(f))=0\). No positive-degree homology exists otherwise, proving rational acyclicity of the full arm quotient.

The \(\mathfrak A_m\)-invariant multiplicity is the sum of the trivial and sign multiplicities for \(\mathfrak S_m\). The trivial multiplicity vanishes as just proved. The sign-weighted expectation of \(g(f)\) is \(5\) when \(m=3\), \(2\) when \(m=4\), and \(0\) when \(m\ge5\): for each \(j\), the signed average of \((f)_j\) is one if \(m-j\in\{0,1\}\) and zero if \(m-j\ge2\). This proves the alternating-arm assertion.

For completeness, the multiplicity characters for the sign and standard irreducible representations of the *label* group \(\mathfrak S_3\), viewed as characters of \(\mathfrak S_m\), are respectively
\[
\chi_{\mathrm{label\ sign}}(\sigma)=\frac{g(f)+6c_2(\sigma)-6c_3(\sigma)}6,
\qquad
\chi_{\mathrm{label\ std}}(\sigma)=\frac{g(f)}3+c_3(\sigma).
\]
The trivial-label sector is \(1+(g(f)-6c_2(\sigma)-6c_3(\sigma))/6\) and agrees with the unordered three-particle calculation. These three formulas follow by the ordinary \(\mathfrak S_3\) character inner product and determine the entire representation over \(\mathbb Q\).

## Verification

The standalone standard-library program `verify.py` constructs the three-fold cubical discretization with three edges per arm, enumerates **all** ordered triples of cells with disjoint closed supports, checks connectivity of its one-skeleton, and computes signed cellular Lefschetz traces under joint arm and label permutations. It checks one representative of every conjugacy class of \(\mathfrak S_m\) and every conjugacy class of \(\mathfrak S_3\) for \(m=3,4,5\), totaling \(45\) comparisons, against the formulas proved above. The resulting integral Euler characteristics are \(-12,-60,-150\), yielding previously known first Betti ranks \(13,61,151\). The recorded run ends with `STAR_TRIPLE_JOINT_CHARACTER_OK cases=45`. These are finite checks of the proof and orientation conventions; the all-parameter result follows from the preceding symbolic argument and the cited radial-tree theorem, not from finite extrapolation.

## Relationship to prior work

Ghrist's 1999 public preprint, notably Proposition 4.1, establishes the radial-tree deformation and the exact first Betti rank for any particle count. Farley–Sabalka's 2004 preprint supplies the relevant discrete-Morse foundation. Wawrykow's 2024 preprint studies generators, relations, and particle-label representation stability for ordered star configurations, and describes a one-dimensional cubical model (Section 3); its stated theorems do not give the joint \(\mathfrak S_m\times\mathfrak S_3\) character. Known homology-character calculations for *unlabeled* star configurations yield the trivial \(\mathfrak S_3\)-isotypic projection but not the label-sign and label-standard projections. The claim here excludes all those known projections and nonequivariant facts. Presentation-level results in the literature can encode related representations indirectly; direct priority for the explicit closed character is not conclusively established.

## Limitations

Only three *labeled*, collision-free particles and ordinary radial stars are covered. The character is over \(\mathbb Q\); integral \(\mathbb Z[\mathfrak S_m\times\mathfrak S_3]\)-lattices, equivariant homotopy types, and the fundamental groups of the symmetry quotients are not classified. No assertion is made for stars with fewer than three arms. Publication-priority risk remains for unindexed character calculations or implicit extraction from published presentations. No independent mathematical audit has been carried out.

## References

1. Robert Ghrist, *Configuration spaces and braid groups on graphs in robotics*, arXiv:math/9905023, first publicly posted 1999-05-05, particularly Section 4, Proposition 4.1. https://arxiv.org/abs/math/9905023
2. Daniel Farley and Lucas Sabalka, *Discrete Morse theory and graph braid groups*, arXiv:math/0410539, first publicly posted 2004-10-25, Section 4. https://arxiv.org/abs/math/0410539
3. Nicholas Wawrykow, *Homology generators and relations for the ordered configuration space of a star graph*, arXiv:2401.13821, first publicly posted 2024-01-24, Sections 1 and 3. https://arxiv.org/abs/2401.13821

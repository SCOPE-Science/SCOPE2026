# The six-nodal rational elliptic discriminant is the Hermite bielliptic divisor

## Finding

Let \(k=\mathbb C\), and let \(\mathcal U\subset\mathbb P(\operatorname{Sym}^6 k^2)\cong\mathbb P^6\) be the open set of binary sextics with six distinct projective roots. Let \(\mathcal D\subset\mathcal U\) consist of reduced unordered sextuples occurring as the six singular-fiber parameters of a relatively minimal rational elliptic surface with a section and exactly six fibers of Kodaira type \(I_2\).

For a sextic \(f=\prod_{i=1}^6\ell_i\), write \(q_{ij}=\ell_i\ell_j\in\operatorname{Sym}^2 k^2\). For each of the fifteen perfect matchings \(M=\{\{i,j\},\{k,l\},\{m,n\}\}\) of \(\{1,\ldots,6\}\), let

\[
\delta_M=\det\begin{pmatrix}
[q_{ij}]_{s^2}&[q_{ij}]_{st}&[q_{ij}]_{t^2}\\
[q_{kl}]_{s^2}&[q_{kl}]_{st}&[q_{kl}]_{t^2}\\
[q_{mn}]_{s^2}&[q_{mn}]_{st}&[q_{mn}]_{t^2}
\end{pmatrix},\qquad
\mathscr H(f)=\prod_{M}\delta_M.
\]

Use a fixed lexicographic order of the three pairs in each determinant. The product is symmetric in the six roots, so it is a homogeneous polynomial of degree \(15\) in the seven coefficients of \(f\), unique here up to a nonzero scalar. It is nonzero and defines an irreducible, generically reduced degree-\(15\) hypersurface in \(\mathbb P^6\). The **exact characterization** on the simple-root locus is

\[
\boxed{\mathcal D=\mathcal U\cap V(\mathscr H).}
\]

For \(f\in\mathcal U\), this is also equivalent to the smooth genus-two curve \(C_f:\ w^2=f(s,t)\) admitting an involution other than the hyperelliptic one, or equivalently a degree-two elliptic quotient. Hence the image of \(\mathcal D\) in genus-two moduli is precisely the classical bielliptic divisor, the Humbert locus \(H_4\) of \((2,2)\)-split Jacobians. Moreover, the map from isomorphism classes of the indicated rational elliptic surfaces (with their fibrations and sections) to this genus-two divisor is **generically one-to-one**, and consequently gives a birational correspondence of coarse moduli surfaces.

The Hermite invariant and the bielliptic Humbert divisor are classical; what is asserted here is their identification, with a direct fifteen-determinant equation and a generic inverse, **for the specific six-\(I_2\) elliptic-surface discriminant problem posed in Question 25 of the 2026 source**.

## Assumptions and scope

Everything is over \(\mathbb C\), with the base \(\mathbb P^1\). A sextuple always means six distinct geometric points unless its degeneration is explicitly discussed. The Weierstrass surface has a section and a degree-one fundamental line bundle; its relatively minimal desingularization is understood. The product formula may be evaluated with any choice and scaling of linear factors. Under \(\ell_i\mapsto c_i\ell_i\), its value scales by \(\prod_i c_i^{15}\), as appropriate for a degree-fifteen equation in the binary sextic. The scheme-level statement concerns the reduced closure of the locus, not a claim about every boundary singularity of that closure. The birational statement is about coarse isomorphism classes, not stack equivalence or a globally regular inverse at curves with extra automorphisms.

## Proof

**1. The source discriminant and pair-quadratic dependence.** Section 2.4 of Ciliberto--Grassi--Miranda--Verra--Zanardini gives the Weierstrass presentation of every six-\(I_2\) rational elliptic surface as

\[
y^2=(x-Q_1(s,t))(x-Q_2(s,t))(x-Q_3(s,t)),
\qquad Q_1+Q_2+Q_3=0,
\]

where each \(Q_i\) is a binary quadratic, and the three pairwise differences split into six distinct linear factors. The six discriminant points are exactly the zero set of

\[
(Q_1-Q_2)(Q_2-Q_3)(Q_3-Q_1).
\]

The three quadratics \(A=Q_1-Q_2\), \(B=Q_2-Q_3\), \(C=Q_3-Q_1\) obey \(A+B+C=0\). They therefore define a matching \(M\) of the six roots for which \(\delta_M=0\). Conversely, suppose \(\delta_M=0\) for six distinct roots. The three quadratics corresponding to the three pairs are pairwise linearly independent, since they have disjoint unordered root sets. Consequently their unique (up to scalar) linear relation has three nonzero coefficients: \(A+B+C=0\), after rescaling the respective pair quadratics. Set

\[
Q_1=\frac{2A+B}{3},\quad Q_2=\frac{B-A}{3},\quad Q_3=\frac{-A-2B}{3}.
\]

Then \(Q_1+Q_2+Q_3=0\) and their successive pairwise differences are \(A,B,C\). The corresponding Weierstrass equation has exactly six singular parameters, each a simple zero of one difference and not of the other two. At every such point the cubic has one ordinary double root, its discriminant has order two, and its Weierstrass coefficients remain minimal. Therefore each resolved fiber is \(I_2\). The degree-two \(Q_i\) give fundamental line bundle \(\mathcal O_{\mathbb P^1}(1)\); the relatively minimal smooth elliptic surface with section is rational. This proves the zero-set equivalence without relying on parameter counting.

**2. The involution equivalence.** Let three unordered pairs \(\{a_i,b_i\}\) of distinct points of \(\mathbb P^1\) be specified. In an affine chart where all six points are finite, the corresponding quadratic coefficient row is \((1,-a_i-b_i,a_i b_i)\). A projective trace-zero matrix

\[
T=\begin{pmatrix}u&v\\w&-u\end{pmatrix}
\]

interchanges \(a_i\) and \(b_i\) precisely when

\[
 w a_i b_i-u(a_i+b_i)-v=0.
\]

These three homogeneous linear conditions on \((u,v,w)\) have a nonzero solution exactly when \(\delta_M=0\). Its matrix is invertible: a rank-one matrix would define a constant projective map and could not interchange three disjoint pairs. Therefore \(T^2\) is a nonzero scalar matrix and \(T\) is a genuine order-two Möbius transformation. The argument homogenizes and works with roots at infinity. Thus \(\delta_M=0\) if and only if the six points admit an involution permuting them by those three transpositions.

In suitable coordinates the base involution is \(s\mapsto-s\), and the branch sextic becomes proportional to \(\prod_{j=1}^3(s^2-a_j^2t^2)\). On the smooth double cover, the lifted map \((s,w)\mapsto(-s,w)\) is an order-two automorphism with elliptic quotient \(z^2=\prod_{j=1}^3(U-a_j^2)\), using \(U=s^2\). Conversely, a nonhyperelliptic involution of a genus-two curve descends to an involution of its unique hyperelliptic base. It cannot fix a branch point: locally at such a fixed point, the base involution acts on a parameter \(v\) by \(v\mapsto-v\), whereas the branched double cover has \(v=z^2\), forcing any lift to act on \(z\) by a fourth root \(\pm i\) and have order four. Hence all six branch points occur in three two-cycles. This proves the bielliptic characterization. The Humbert-\(H_4\) designation is classical for the degree-two elliptic-subcover locus.

**3. Equation, degree, and irreducibility.** The action of any permutation of root labels maps \(\mathscr H\) to \(\pm\mathscr H\), because it permutes the fifteen determinants, changing column order only by a sign. The sign is a character of the symmetric group. It cannot be the sign character: the specialized roots \((0,0,1,2,4,7)\) have \(\mathscr H\neq0\), whereas a sign-alternating polynomial would vanish whenever two roots coincide. Consequently the product is symmetric. It has degree fifteen in the coefficients of each \(\ell_i\); the standard quotient \(\operatorname{Sym}^6\mathbb P^1\simeq\mathbb P^6\), with pullback of \(\mathcal O(1)\) equal to the multidegree-\((1,\ldots,1)\) bundle, shows that it descends to a degree-fifteen homogeneous polynomial in the sextic coefficients. Its value at roots \((0,1,2,4,7,13)\) is nonzero.

For a fixed matching, the divisor \(\delta_M=0\) on the ordered six-point space is irreducible: on the pairwise-distinct open set it is parametrized by one involution (dimension two) and a choice of three representatives of its pair orbits (dimension three). There is no additional divisor contained in the diagonals, since \(\delta_M\) does not vanish generically on any diagonal. It is reduced because it is a multihomogeneous polynomial of degree one in each root factor, and it has a nonzero first-order derivative at a smooth configuration. The fifteen divisors for the different matchings are distinct; the configuration \((1,-1,2,-2,3,-3)\) lies on precisely one. The symmetric group permutes these fifteen irreducible components transitively, so their reduced union descends to a single irreducible, generically reduced divisor. Its degree is fifteen as asserted.

**4. Generic inverse and coarse moduli.** Because distinct matching divisors intersect in codimension at least two, a general point of \(V(\mathscr H)\cap\mathcal U\) has exactly one matching \(M\). Its three pair quadratics have a unique relation up to scalar, and the formula in Step 1 reconstructs the unordered triple \(Q_1,Q_2,Q_3\) up to a common scalar. Relabeling the three \(Q_i\) does not change the cubic, and common scalar multiplication is absorbed over \(\mathbb C\) by a Weierstrass change \(x\mapsto c x\), \(y\mapsto c^{3/2}y\). Thus the fibration with its zero section is uniquely reconstructed over the base. Its inverse is rational on the open subset where the matching is unique. Taking the quotient by changes of coordinate of \(\mathbb P^1\) yields the stated birational map from the elliptic-surface coarse moduli to the degree-two elliptic-subcover locus in \(\mathcal M_2\).

## Verification

The accompanying standalone `verify.py` uses integer arithmetic only. It enumerates all fifteen matchings, checks \(\mathscr H\neq0\) at \((0,1,2,4,7,13)\), checks all \(720\) label permutations on that sample, verifies nonvanishing at \((0,0,1,2,4,7)\), and confirms that \((1,-1,2,-2,3,-3)\) vanishes for exactly one matching. It also checks the explicit independent Weierstrass example

\[
Q_1=2s^2+22t^2,\quad Q_2=-13s^2+37t^2,\quad Q_3=11s^2-59t^2,
\]

whose differences vanish at the six points \(\pm1,\pm2,\pm3\). Expected output: `VERIFY_OK matchings=15 symmetric_permutations=720 special_zeros=1`. These finite checks corroborate but do not replace Steps 1--4 of the proof; no coefficient-expanded 1716-term (or larger) sextic invariant and no exhaustive classification of boundary singularities is claimed.

## Relationship to prior work

Ciliberto, Grassi, Miranda, Verra, and Zanardini (arXiv:2602.11725v1, \S2.4 and Question 25 in \S2.7) supply the three-quadratic Weierstrass representation and explicitly ask for the discriminant hypersurface equation and the genus-two condition. Those inputs are assumed, not claimed here. Abdesselam and Chipalkatti (arXiv:1008.3117v3, \S1 and \S4) already study the classical locus of binary sextics invariant under a projective involution, and Hermite's degree-fifteen invariant is historically known. Shaska (arXiv:2608.16426v1, introduction and \S2) identifies the degree-two elliptic subcover locus with Humbert \(H_4\) and treats its invariant-theoretic equation. None of those inspected statements identifies this classical locus with the specific six-\(I_2\) rational elliptic discriminant or supplies its explicit matching-based reconstruction of the elliptic fibration. The asserted extension is this compatibility and birational identification, not a new degree-fifteen invariant or a new description of Humbert surfaces in isolation.

## Limitations

The irreducibility/degree statement concerns the closure of the simple-root discriminant locus, not a classification of its boundary points or singularities. The birational inverse is only generic; extra automorphisms or more than one matching cause special fibers with additional presentations. The uniqueness is over \(\mathbb C\) with a chosen elliptic fibration and section, and does not assert uniqueness of unrelated elliptic fibrations on the underlying surface. The equation is given in root-determinantal form and not expanded in seven sextic coefficients. Earlier classical results imply many of the ingredients, so the essential originality claim is only their explicit application to the question posed in the recent elliptic-surface paper. Independent priority review has not been performed.

## References

- C. Ciliberto, A. Grassi, R. Miranda, A. Verra, A. Zanardini, *Rational elliptic surfaces with six singular double fibres*, arXiv:2602.11725v1, posted 2026-02-12, especially \S2.4 and Question 25 in \S2.7. https://arxiv.org/abs/2602.11725
- A. Abdesselam and J. Chipalkatti, *Quadratic involutions on binary forms*, arXiv:1008.3117v3 (2019 version of 2010 preprint), especially \S1.3--1.5 and \S4. https://arxiv.org/abs/1008.3117
- T. Shaska, *Degrees of Genus-Two Split-Jacobian Loci and Humbert-Form Reconstruction*, arXiv:2608.16426v1 (2026), especially the introduction and Section 2. https://arxiv.org/abs/2608.16426
- Classical background: the Hermite invariant of a binary sextic and the Humbert surface of discriminant four; their prior existence and degree are not claimed as new.

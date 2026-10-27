# The characteristic-three Wiman sextic is the complete rational tangent arrangement of a conic

## Finding
Let \(W_3\subset\mathbf P^2_{\mathbf F_3}\) be the scheme-theoretic characteristic-three reduction of the integral Wiman equation
\[
F=X^6+Y^6+Z^6+(X^2+Y^2+Z^2)(X^4+Y^4+Z^4)-12X^2Y^2Z^2=0.
\]
Then \(W_3\) is reduced and has five geometrically irreducible components defined over \(\mathbf F_3\): the smooth conic \(C:X^2+Y^2+Z^2=0\) and its four distinct \(\mathbf F_3\)-rational tangent lines. Its geometric singularities are precisely four ordinary tacnodes (type \(A_3\)) at the conic-line contacts and six ordinary nodes (type \(A_1\)) at the pairwise line intersections. All ten are \(\mathbf F_3\)-rational. The singularity invariants are \(\sum_P\delta_P=14\) and \(\sum_P\tau_P=18\); its arithmetic genus is \(10\), and its normalization is the disjoint union of five copies of \(\mathbf P^1_{\mathbf F_3}\).

The full geometric **projective** stabilizer of this embedded reduced curve is \(\operatorname{PGL}_2(\mathbf F_3)\cong S_4\) (order \(24\)). For every \(m\ge1\), putting \(q=3^m\),
\[
\#W_3(\mathbf F_q)=5q-5,\qquad
Z(W_3/\mathbf F_3,T)=\frac{(1-T)^5}{(1-3T)^5}.
\]
These are counts on the singular plane curve, not a smooth genus-six normalization.

## Assumptions and scope
All geometric statements are made after base extension of the **literal** polynomial model to an algebraic closure of \(\mathbf F_3\), and all arithmetic statements use the displayed model over \(\mathbf F_3\) and its finite extensions. The projective stabilizer consists of linear projective transformations of the plane preserving the reduced subscheme; no assertion is made about the abstract automorphism functor of the reducible curve. These statements do not assert the stable reduction of the complex Wiman curve over a mixed-characteristic discrete valuation ring.

## Proof
**1. Exact factorization.** Put \(C=X^2+Y^2+Z^2\) and define
\[
L_1=X+Y+Z,\quad L_2=X+Y-Z,\quad
L_3=X-Y+Z,\quad L_4=-X+Y+Z.
\]
In characteristic three, the cube identity gives \(X^6+Y^6+Z^6=C^3\) and \(12=0\). Hence
\[
F=C\bigl(C^2+X^4+Y^4+Z^4\bigr)
 = C\,L_1L_2L_3L_4.
\]
The final equality follows by multiplying four linear factors; explicitly both quartics equal \(-X^4-Y^4-Z^4-X^2Y^2-X^2Z^2-Y^2Z^2\) in \(\mathbf F_3[X,Y,Z]\). The conic is nonsingular, since its three partial derivatives never vanish simultaneously on projective space, and no line is a component of it. Thus the factorization gives exactly five distinct reduced geometric components.

**2. Component intersections and singularity types.** The four rational points of \(C\) are
\[
[1:1:1],\ [1:1:-1],\ [1:-1:1],\ [1:-1:-1].
\]
Their tangent equations, given by \(x_0X+y_0Y+z_0Z=0\), are exactly \(L_1,\ldots,L_4\). Each line meets \(C\) with intersection multiplicity two at its indicated point and nowhere else, by Bezout and the nondegeneracy of the conic. Its local union with \(C\) therefore consists of two smooth branches with contact order two. Since \(2\) is invertible, this is an ordinary \(A_3\) tacnode with \(\delta=2\) and local Tjurina number \(3\).

No three of the four tangent lines concur: their pairwise intersections are the six points \([1:\pm1:0]\), \([1:0:\pm1]\), \([0:1:\pm1]\). At each, \(C=2\ne0\) and exactly two distinct lines vanish, so each point is an ordinary node, with \(\delta=\tau=1\). Components are smooth away from these intersections, hence the ten listed points exhaust the geometric singular locus.

The plane arithmetic-genus formula gives \(p_a=(6-1)(6-2)/2=10\). Summing the singularity contributions gives \(4\cdot2+6\cdot1=14\) for \(\delta\), and \(4\cdot3+6\cdot1=18\) for the Tjurina number. The five components are a smooth conic and four lines defined over \(\mathbf F_3\); hence their normalizations are five copies of \(\mathbf P^1_{\mathbf F_3}\). In particular the genus check \(p_a=\sum g_i+\sum\delta_P-r+1=0+14-5+1=10\) agrees.

**3. Exact arithmetic.** Every component is \(\mathbf F_3\)-rational and has \(q+1\) points over \(\mathbf F_q\). Their only repeated set-theoretic points are the four conic-line contacts and six line-line intersections; all are defined over \(\mathbf F_3\), no three components meet, and each belongs to precisely two components. Inclusion-exclusion thus gives \(5(q+1)-10=5q-5\) for every \(m\ge1\). Substituting these counts into the defining exponential series for the Hasse--Weil zeta function proves the displayed rational expression.

**4. Exact projective stabilizer.** A projectivity preserving \(W_3\) must preserve the unique degree-two irreducible component \(C\) and permute its four distinguished line components. Four lines in general position form a projective frame in the dual plane, so their pointwise stabilizer is trivial. This embeds the projective stabilizer into \(S_4\). Conversely, identify \(C\cong\mathbf P^1\) over \(\mathbf F_3\). The four tangent contacts are exactly \(\mathbf P^1(\mathbf F_3)\). The symmetric-square projective representation of \(\operatorname{PGL}_2(\mathbf F_3)\) preserves the conic and permutes the four rational tangent lines. Its action on the four rational conic points is faithful and has order \(3(3^2-1)=24\), so its image is all \(S_4\). Thus the full geometric projective stabilizer is exactly \(\operatorname{PGL}_2(\mathbf F_3)\cong S_4\).

## Verification
Run the included standard-library-only Python checker using `python3 verify.py`. It performs sparse-polynomial arithmetic modulo three to verify the factorization, enumerates the ten component-intersection points, checks all four tangencies and six nodes over the base field, enumerates the \(24\) projective base-field stabilizers and verifies that they preserve both the conic and the sextic polynomial, and independently enumerates all projective points over \(\mathbf F_3\), \(\mathbf F_9\), and \(\mathbf F_{27}\). It reports respective sextic point counts \(10\), \(40\), and \(130\), followed by `VERIFY_OK`. Finite checks corroborate but do not replace the symbolic proof for all finite extensions or the geometric stabilizer argument over the algebraic closure.

## Relationship to prior work
Giulietti--Kawakita--Lia--Montanucci [1], Remark 3.1, explicitly records reducibility of the same integral Wiman sextic equation in characteristics two and three and rationality in characteristic five. That remark does **not** give its characteristic-three irreducible components, their tangency arrangement, full singularity types, geometric projective stabilizer, or the zeta function. Its proof of full automorphisms in larger characteristics assumes \(p\ge7\), so those statements do not yield this characteristic-three classification. Dolgachev--Farb--Looijenga [2] study the characteristic-zero Wiman--Edge pencil on a quintic del Pezzo surface and its special members; those are different geometric fibers and do not settle this literal reduction. Kawakita [3] constructs and counts finite-field sextics over characteristics at least five in the available tables, not this singular characteristic-three fiber. These comparisons concern implications and exact objects, not title similarity.

## Limitations
This is a fixed-integral-model boundary classification, not a statement about stable reduction or the normalization of a mixed-characteristic generic fiber. It does not classify all possible integral models of the Wiman curve; changing the model can change the literal special fiber. Although the components and incidence are elementary once the factorization is known, the claim is the complete geometric and arithmetic characterization of a published excluded characteristic. The 2017 finite-field sextic paper [3] was accessible in abstract and tables but not full text; an earlier computation elsewhere cannot be categorically excluded. No independent verification is claimed.

## References
1. M. Giulietti, M. Kawakita, S. Lia and M. Montanucci, *An \(\mathbf F_{p^2}\)-maximal Wiman's sextic and its automorphisms*, arXiv:1805.06317, original version 2018-05-15, especially Equation (1) and Remark 3.1. https://arxiv.org/abs/1805.06317
2. I. Dolgachev, B. Farb and E. Looijenga, *Geometry of the Wiman--Edge pencil, I: algebro-geometric aspects*, European Journal of Mathematics 4 (2018), 879--930. https://doi.org/10.1007/s40879-018-0231-3
3. M. Q. Kawakita, *Certain sextics with many rational points*, Advances in Mathematics of Communications 11 (2017), 289--292. https://doi.org/10.3934/amc.2017020

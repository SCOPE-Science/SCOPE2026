# The characteristic-three Wiman sextic is a conic with all four rational tangents

## Finding

Let \(F\in\mathbb Z[X,Y,Z]\) be the classical Wiman sextic polynomial
\[
F=X^6+Y^6+Z^6+(X^2+Y^2+Z^2)(X^4+Y^4+Z^4)-12X^2Y^2Z^2.
\]
Write \(W_3\subset\mathbb P^2_{\mathbb F_3}\) for the coefficientwise reduction \(V(F\bmod 3)\), and \(k\) for an algebraic closure of \(\mathbb F_3\). Put \(Q=X^2+Y^2+Z^2\), and define the four linear forms
\[
L_0=X+Y+Z,\quad L_1=X+Y-Z,\quad
L_2=X-Y+Z,\quad L_3=-X+Y+Z.
\]
Then the *scheme-theoretic* equality over \(\mathbb F_3\) is
\[
\boxed{W_3=V(QL_0L_1L_2L_3).}
\]
The conic \(V(Q)\) is smooth, and the four lines \(V(L_i)\) are exactly its four \(\mathbb F_3\)-rational tangents. Thus the special fibre is reduced, with five geometrically rational irreducible components of degrees \(2,1,1,1,1\).

Over \(k\) its singular set consists of exactly ten distinct \(\mathbb F_3\)-rational points: four ordinary tacnodes (two smooth branches with intersection multiplicity two, analytic type \(A_3\)) where the conic touches a line, and six ordinary nodes at the pairwise line intersections. There are no triple intersections. The total intrinsic Tjurina length is \(18\); the normalization defect is \(14\). In particular,
\[
\operatorname{length}\bigl(\widetilde{\mathcal O}_{W_3}/\mathcal O_{W_3}\bigr)=14
\]
means the *sum of local lengths* at the ten singular points, not a quotient of global section rings. The arithmetic genus is \(10\). For **every integer** \(r\ge1\), the exact finite-field count and Hasse–Weil zeta function of the singular special fibre are
\[
\boxed{\#W_3(\mathbb F_{3^r})=5\cdot3^r-5,\qquad Z(W_3/\mathbb F_3,T)=\frac{(1-T)^5}{(1-3T)^5}.}
\]
In particular, every one of the ten \(\mathbb F_3\)-rational points is singular.

## Assumptions and scope

The claims concern the coefficientwise special fibre of this fixed homogeneous integral sextic equation, first over \(\mathbb F_3\), then geometrically over \(k\). The arithmetic point counts are over all finite extensions of the fixed base field \(\mathbb F_3\). The local singularity and normalization assertions are geometric. They are **not** assertions about the stable model, minimal regular model, or abstract good reduction of the genus-six normalization of the generic Wiman curve.

## Proof

**1. Exact reduction and components.** Set \(S=X^4+Y^4+Z^4\) and \(E=X^2Y^2+Y^2Z^2+Z^2X^2\). Frobenius in characteristic three yields \(X^6+Y^6+Z^6=Q^3\), whereas \(Q^2=S+2E\). Consequently
\[
F\bmod3=Q(Q^2+S)=Q(2S+2E)=-Q(S+E).
\]
Direct multiplication in the integral polynomial ring gives
\[
L_0L_1L_2L_3=-S+2E.
\]
Reduction modulo three changes \(2E\) into \(-E\), so \(L_0L_1L_2L_3=-(S+E)\) modulo three. This proves the asserted polynomial identity, with no loss of scheme structure. The gradient of \(Q\) is \((2X,2Y,2Z)\), so the conic is smooth. The four displayed linear forms are nonproportional and none divides the smooth conic; hence the divisor is reduced.

**2. Rational tangent configuration and singular support.** For a point of \(\mathbb P^2(\mathbb F_3)\), every nonzero square is \(1\). Thus \(Q=0\) holds precisely when all three coordinates are nonzero, and quotienting their eight sign choices by simultaneous sign gives the four points
\[
P_0=[1:1:1],\quad P_1=[1:1:-1],\quad
P_2=[1:-1:1],\quad P_3=[-1:1:1].
\]
Their tangent equations, given by the polarization \(P_i\cdot(X,Y,Z)=0\), are precisely \(L_i=0\). Each tangent has intersection multiplicity two with the conic at its indicated point and has no other geometric conic point, by Bézout. Two distinct such tangents therefore intersect off the conic. Three of them cannot concur: their dual points lie on the smooth dual conic, and three distinct points of that conic cannot lie on a line. Thus the only line-line singularities are six distinct ordinary double crossings. The four contact points are distinct from them and from one another. Away from pairwise component intersections, a product of distinct local smooth factors has nonzero differential, so there are no other geometric singular points.

**3. Local analytic types and lengths.** At a line-line crossing, the local equation is a unit times \(uv\); this is a node with local normalization defect \(\delta=1\) and Tjurina length \(\tau=1\). At each line-conic contact the branches are both smooth with contact order exactly two. Formal local coordinates transform their product into a unit times
\[
f(u,v)=u(u-v^2).
\]
Because \(2\) is invertible, completing the square identifies the germ with an ordinary \(A_3\) tacnode. The Jacobian ideal is
\[
(f,f_u,f_v)=(u(u-v^2),\,2u-v^2,\,-2uv),
\]
and substitution \(u=v^2/2\) leaves the ideal \((v^3)\); hence \(\tau=3\). The normalization consists of the two branches \(u=0\) and \(u=v^2\), whose local coordinate rings are two copies of \(k[[v]]\); the image of the original local ring consists of pairs agreeing modulo \(v^2\). Therefore \(\delta=2\) and the conductor ideal in the local ring is \((u,v^2)\), with colength two. Globally, the singularity basket is \(4A_3+6A_1\), yielding
\[
\sum\delta=4\cdot2+6\cdot1=14,\qquad
\sum\tau=4\cdot3+6\cdot1=18.
\]
Each component normalizes to \(\mathbb P^1_k\). For a connected reduced curve with five irreducible components, the normalization exact sequence gives \(p_a=\sum\delta-5+1=10\); this agrees with \((6-1)(6-2)/2=10\), as required for any plane sextic.

**4. Rational points and the zeta function.** Each of the five components is isomorphic over \(\mathbb F_3\) to \(\mathbb P^1\): each line is, and the conic has the four exhibited rational points. The ten pairwise component intersections are distinct \(\mathbb F_3\)-rational points, each belonging to exactly two components. Inclusion–exclusion therefore gives, for every \(r\ge1\),
\[
\#W_3(\mathbb F_{3^r})=5(3^r+1)-10=5\cdot3^r-5.
\]
The definition \(Z(W_3/\mathbb F_3,T)=\exp(\sum_{r\ge1}\#W_3(\mathbb F_{3^r})T^r/r)\) and the formal logarithm identity imply the claimed rational function. Over \(\mathbb F_3\), the only rational points on the conic are the four contacts, and all other six rational points on the union are line-line crossings, so every rational point is singular. All twenty \(\mathbb F_3\)-rational points of the disjoint normalization lie over those ten singular points.

## Verification

The standalone `verify.py` recomputes the reduction identity coefficientwise in \(\mathbb F_3[X,Y,Z]\); enumerates all thirteen points of \(\mathbb P^2(\mathbb F_3)\); checks the four conic points and tangent equations; and verifies every pairwise line intersection lies off the conic, lies on precisely two lines, and is distinct from all other intersections and tangencies. It also checks the local Tjurina calculation by elementary elimination. Execute `python3 verify.py` from the directory containing this file. The geometric completeness, analytic classification, normalization lengths and all-extension-field point formula are supplied by the proof above, not inferred from finite enumeration.

## Relationship to prior work

Inoue and Kato (2005/2006) study the Wiman sextic and its symmetric plane model but explicitly assume the characteristic is different from \(2,3,5\). Kawakita (2015) treats finite-field point counts and Jacobian decompositions with \(p>5\). Giulietti, Kawakita, Lia and Montanucci (2018 preprint, published later) explicitly state in their Remark 3.1 that the same homogeneous sextic is reducible for \(p=2\) or \(3\). **That reducibility is prior work**, not a new claim here. Their stated result does not specify the conic-plus-all-rational-tangents decomposition, the four tacnodes and six nodes, or the conductor and Tjurina lengths; the present theorem sharpens the degeneration geometrically. A systematic search for alternate modular or projective formulations did not reveal an equivalent full classification, but lack of a match is not a uniqueness proof.

## Limitations

The reduction is a singular divisor on the fixed plane, not a semistable or stable genus-six model. The general-characteristic automorphism group and finite-field maximality results do not extend to this reducible fibre. Any stable reduction, Galois action on the components of a resolved model, or comparison with another integral model requires additional work. Potential equivalent classifications in older modular projective geometry have not been exhaustively ruled out. No claim of independent validation is made.

## References

1. N. Inoue and F. Kato, *On the geometry of Wiman's sextic*, Journal of Mathematics of Kyoto University **45** (2005), 743–757, DOI: 10.1215/KJM/1250281655. Full preprint: https://www.math.kyoto-u.ac.jp/preprint/2005/2inoue.kato.pdf (see pp. 1–2, especially the characteristic restriction).
2. M. Q. Kawakita, *Wiman's and Edge's sextic attaining Serre's bound II*, Contemporary Mathematics **637** (2015), 191–203, DOI: 10.1090/conm/637/12758; author text: https://manypoints.org/upload/687299749.pdf (see §§2–3 and \(p>5\) hypotheses).
3. M. Giulietti, M. Kawakita, S. Lia, M. Montanucci, *An \(\mathbb F_{p^2}\)-maximal Wiman's sextic and its automorphisms*, arXiv:1805.06317 (2018), https://arxiv.org/pdf/1805.06317 (see Remark 3.1, p. 9, concerning prior reducibility).

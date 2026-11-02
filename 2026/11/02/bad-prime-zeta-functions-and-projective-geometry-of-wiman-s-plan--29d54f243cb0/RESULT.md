# Bad-prime zeta functions and projective geometry of Wiman's plane sextic

## Finding
Let \(F\in\mathbb Z[X,Y,Z]\) be the primitive sextic
\[
F=X^6+Y^6+Z^6+(X^2+Y^2+Z^2)(X^4+Y^4+Z^4)-12X^2Y^2Z^2.
\]
For \(p\in\{2,3,5\}\), write \(W_p=V(F\bmod p)\subset\mathbb P^2_{\mathbb F_p}\), retaining its **scheme** structure. For every integer \(n\ge1\), the exact counts of field-valued points are
\[
\begin{array}{c|c|c}
p & \#W_p(\mathbb F_{p^n}) & Z(W_p/\mathbb F_p,T)\\\hline
2&3\cdot2^n+1&[(1-T)(1-2T)^3]^{-1}\\
3&5\cdot3^n-5&(1-T)^5/(1-3T)^5\\
5&5^n+1-4(-1)^n&(1+T)^4/[(1-T)(1-5T)]
\end{array}
\]
with \(Z(X/\mathbb F_p,T)=\exp(\sum_{n\ge1}\#X(\mathbb F_{p^n})T^n/n)\).
The characteristic-five sign alternation is caused by four **nonsplit** rational nodes: their eight geometric branches become individually rational only over \(\mathbb F_{25}\). The characteristic-three and characteristic-five sextics both have full **projective** stabilizer \(S_4\) over the algebraic closure. This is a statement about the displayed integral plane model and its low-characteristic fibres, not about the zeta function of a smooth genus-six normalization.

## Assumptions and scope
Work with the exact displayed equation, with no change of integral model. All geometric singularity statements are over \(\overline{\mathbb F}_p\); the point-count and splitting statements retain the specified \(\mathbb F_p\)-structure. In characteristic two the scheme is nonreduced, while point counts use morphisms from \(\operatorname{Spec}\mathbb F_{2^n}\), which automatically factor through the reduction. The stabilizers mean \(\operatorname{Stab}_{\mathrm{PGL}_3(\overline{\mathbb F}_p)}(W_p)\), rather than abstract automorphisms of a normalization.

## Proof
Put \(Q=X^2+Y^2+Z^2\) and \(P=XYZ\). Exact coefficient reduction of the displayed integral polynomial yields all three identities
\[
\begin{aligned}
F\bmod2&=((X+Y)(Y+Z)(Z+X))^2,\\
F\bmod3&=Q(X+Y+Z)(-X+Y+Z)(X-Y+Z)(X+Y-Z),\\
F\bmod5&=2Q^3+P^2.
\end{aligned}
\]
These are polynomial identities, not merely equalities on finite-field points.

**Characteristic two.** The reduction is a union of three distinct double lines. Their underlying three lines are all defined over \(\mathbb F_2\) and meet at the sole point \([1:1:1]\). For \(q=2^n\), inclusion-exclusion gives \(3(q+1)-2=3q+1\) rational points. Since nilpotents do not affect field-valued points, this also counts \(W_2\).

**Characteristic three.** The conic \(Q=0\) is smooth. Its four \(\mathbb F_3\)-points are precisely the projective sign vectors \([\pm1:\pm1:\pm1]\). The four displayed lines are their distinct tangent lines, because \(\nabla Q=2(X,Y,Z)\). Every pair of lines meets at one of six distinct \(\mathbb F_3\)-points, none on \(Q\), and no three lines are concurrent. Thus the reduced sextic has six ordinary nodes of type \(A_1\) and four tangencies of a line and smooth conic, each of type \(A_3\). In the completed local ring at a tangency, one may take the line equation as \(v=0\) and the conic equation as \(v-u^2=0\), up to units and a regular coordinate change; this gives an \(A_3\) tacnode. The five rational components (one conic and four lines) each have \(q+1\) points over \(\mathbb F_q\), with ten distinct ordinary double-counted intersection points (six nodes and four tangencies). Consequently, \(\#W_3(\mathbb F_q)=5(q+1)-10=5q-5\), for every \(q=3^n\).

**Characteristic five: exhaustive geometric singularities.** From \(F=2Q^3+P^2\) its three derivatives are
\[
F_X=2X(Q^2+Y^2Z^2),\quad
F_Y=2Y(Q^2+X^2Z^2),\quad
F_Z=2Z(Q^2+X^2Y^2).
\]
If a coordinate vanishes, the curve equation forces \(Q=0\). This gives exactly six points, two on each coordinate line: \([0:1:\pm2]\), \([1:0:\pm2]\), and \([1:\pm2:0]\). At each, \((Q,P)\) is a regular parameter pair (their differentials are independent), and the local equation is exactly \(2Q^3+P^2=0\). Hence these six are geometrically unibranch ordinary cusps \(A_2\), all rational over \(\mathbb F_5\).

If \(XYZ\ne0\), vanishing of the three derivatives forces \(X^2=Y^2=Z^2\). The resulting four geometric points are the sign vectors \([\pm1:\pm1:\pm1]\), all \(\mathbb F_5\)-rational. At \([1:1:1]\), set \(X=1+u\), \(Y=1+v\), \(Z=1\). The quadratic term of \(F\) is
\[
2u^2+3uv+2v^2,
\]
whose discriminant is \(3\in\mathbb F_5^\times\), a nonsquare. It is nondegenerate, so the singularity is an ordinary node \(A_1\), with conjugate tangent branches defined over \(\mathbb F_{25}\) but not over \(\mathbb F_5\). Signed coordinate permutations give the same conclusion at each of the other three nodes. The displayed derivative calculation exhausts all geometric singular points.

The curve is geometrically reduced because it has only isolated singularities. Were it geometrically reducible, every intersection between two different components would have to be one of the four ordinary nodes (the six cusps are unibranch). Each node contributes at most one to the intersection between distinct components, so the sum of pairwise intersection numbers would be at most four. Bézout's theorem, however, gives at least five for any partition of a degree-six curve into two or more positive-degree components. This contradiction proves geometric irreducibility. The plane sextic has arithmetic genus ten; its four nodes and six cusps have total \(\delta\)-invariant ten. Its smooth projective normalization is therefore genus zero. The preimage of an \(\mathbb F_5\)-rational geometric cusp is a single \(\mathbb F_5\)-rational point, so the normalization is \(\mathbb P^1_{\mathbb F_5}\).

For \(q=5^n\), normalization supplies \(q+1\) points. Each cusp has exactly one rational preimage and contributes no correction. Each rational nonsplit node has zero rational preimages for odd \(n\), hence adds one point; for even \(n\), it has two rational preimages, hence subtracts one point. The four nodes give total correction \(-4(-1)^n\). This proves the characteristic-five formula.

**Projective stabilizers.** For \(p=3\), the four tacnodes, and for \(p=5\), the four nodes, form a projective frame (no three collinear). Every projective automorphism preserving the curve preserves this intrinsic four-point set and therefore injects into its permutation group \(S_4\). Conversely, all signed coordinate permutations preserve the equation, and their projective image has order \(4\cdot6=24\), permuting the four marked points faithfully. Thus the full projective stabilizer is exactly \(S_4\) in both characteristics. This does not identify the abstract automorphism group of the normalization.

Finally, the three displayed zeta functions follow by exponentiating the three exact point-count formulas term by term.

## Verification
Run `python verify_bad_wiman.py` with Python 3.9 or later. The standalone standard-library program checks all three polynomial identities coefficientwise, the characteristic-five tangent-cone discriminant, all projective rational points over the six fields \(\mathbb F_2,\mathbb F_4,\mathbb F_3,\mathbb F_9,\mathbb F_5,\mathbb F_{25}\), and the ten rational singular-support points in characteristics three and five. The final marker is `WIMAN_BAD_PRIME_EXACT_CHECKS_PASS`. The universal extension-degree formulas and geometric irreducibility rely on the proof above, not on this finite enumeration.

## Relationship to prior work
The Wiman–Edge pencil and its characteristic-zero geometry were studied by Dolgachev, Farb and Looijenga (first submitted 2017-09-26, primary MSC 14H37). Giulietti, Kawakita, Lia and Montanucci (first submitted 2018-05-15) explicitly note reducibility in characteristics two and three and rationality in characteristic five, while studying other automorphism and maximality questions. Inoue and Kato's 2005 construction explicitly assumes characteristic different from two, three and five. The geometric characteristic-five \(4A_1+6A_2\) stratum of generalized Wiman–Edge sextics has also been computed elsewhere; **that geometric basket is not asserted to be new here**. The new arithmetic statement under assessment is the complete three-prime zeta-function calculation, in particular the nonsplit Frobenius branch correction at the four characteristic-five nodes, together with the specified low-prime projective scheme structures.

## Limitations
No claim is made about zeta functions for good-reduction primes, stable models of the smooth genus-six normalization over local fields, conductor exponents, or uniqueness of integral models. The zeta functions pertain to the (possibly singular or nonreduced) projective plane fibres defined by the exact chosen equation. Literature searches and available primary-text comparisons do not rule out an unindexed older calculation of these same zeta functions; priority would need independent scrutiny. This work has not undergone independent mathematical validation.

## References
1. I. Dolgachev, B. Farb, E. Looijenga, *Geometry of the Wiman–Edge pencil, I: algebro-geometric aspects*, arXiv:1709.09256 (initial public submission 2017-09-26), https://arxiv.org/abs/1709.09256 ; European Journal of Mathematics 4 (2018), 879–930.
2. M. Giulietti, M. Kawakita, S. Lia, M. Montanucci, *An \(\mathbb F_{p^2}\)-maximal Wiman's sextic and its automorphisms*, arXiv:1805.06317 (initial public submission 2018-05-15), https://arxiv.org/abs/1805.06317 .
3. N. Inoue, F. Kato, *On the geometry of Wiman's sextic*, J. Math. Kyoto Univ. 45 (2005), 743–757, https://www.math.kyoto-u.ac.jp/preprint/2005/2inoue.kato.pdf .

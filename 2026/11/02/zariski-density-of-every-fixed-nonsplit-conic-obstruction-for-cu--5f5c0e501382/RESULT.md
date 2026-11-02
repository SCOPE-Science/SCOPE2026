# Zariski density of every fixed nonsplit conic obstruction for cubic rational maps

## Finding
Let \(k=\mathbb Q\), let \(\mathcal M_3\) be the coarse moduli variety of degree-three rational self-maps of \(\mathbb P^1\) up to conjugation, and let \(C/k\) be any nonsplit smooth projective conic. Define \(S_C\subset \mathcal M_3(k)\) to consist of moduli points with trivial geometric dynamical automorphism group whose unique obstruction to defining the map over \(k\) on \(\mathbb P^1\) is the class \([C]\in H^1(k,\mathrm{PGL}_2)\). Then

\[
\overline{S_C}^{\,\mathrm{Zar}}=\mathcal M_3.
\]

Thus **each fixed nonsplit conic class**, not just the union of all obstructed classes, is geometrically ubiquitous in cubic rational-map moduli. In particular, every nonempty \(k\)-defined Zariski-open subset of \(\mathcal M_3\) contains a point of \(S_C\). The result concerns Zariski topology, not natural or logarithmic density in height order.

For the Hamilton conic \(C_0:X^2+Y^2+Z^2=0\), an explicit dominating family is
\[
f_P=[P(X,Y):\overline P(Y,-X)],\qquad P\in\mathbb Q(i)[X,Y]_3,
\]
where the bar conjugates coefficients and we omit the proper closed locus of common roots or nontrivial geometric automorphisms. Every remaining member has a rational coarse moduli point, with obstruction exactly \([C_0]\).

## Assumptions and scope
All fields in the theorem have characteristic zero and the base is \(k=\mathbb Q\). A nonsplit conic means a smooth conic with no \(k\)-rational point. The unique descent obstruction is defined on the open stratum of degree-three rational maps with trivial geometric automorphisms; it is the associated \(\mathrm{PGL}_2\)-torsor, equivalently its Severi--Brauer conic. A moduli point is coarse when no representative on \(\mathbb P^1_k\) exists. The parameter space of binary cubic pairs is an affine eight-space before projectivization.

## Proof
**1. A linear form of the conjugation action.** Let \(W=\mathrm{Hom}(\mathrm{Sym}^3 k^2,k^2)\), the eight-dimensional vector space of ordered pairs of homogeneous binary cubics. A nonzero element \(F=(F_0,F_1)\) with nonzero resultant represents a degree-three map \([F_0:F_1]\). For a lift \(g\in\mathrm{GL}_2\) of a projective coordinate change, the formula
\[
\rho(g)F(v)=\det(g)^{-1}g^{-1}F(gv)
\]
is linear in \(F\), and is unchanged if \(g\) is replaced by \(\lambda g\), since \(F\) is cubic and the total scalar is \(\lambda^{-2}\lambda^{-1}\lambda^3=1\). With the appropriate right-action convention, it therefore defines a rational linear \(\mathrm{PGL}_2\)-action on \(W\), whose projectivization is conjugation of rational maps. The nonzero-resultant open \(W^{\mathrm{res}}\) is invariant and maps dominantly to \(\mathcal M_3\).

**2. Twisting by an arbitrary fixed conic.** Let \(T_C=\mathrm{Isom}_k(\mathbb P^1,C)\) be the \(\mathrm{PGL}_2\)-torsor of geometric coordinate systems on \(C\). Twist the eight-dimensional linear representation by this torsor to obtain
\[
W_C=T_C\times^{\mathrm{PGL}_2}W.
\]
Because it is a Galois form of a finite-dimensional *vector space*, \(W_C\) is an eight-dimensional affine \(k\)-space (noncanonically). The nonzero-resultant and trivial-geometric-automorphism conditions descend to a nonempty Zariski-open \(U_C\subset W_C\). Nonemptiness follows after base extension from the corresponding nonempty generic open of \(W\). For independent verification of this nonemptiness in degree three, the explicit example in Step 4 has nonzero resultant and distinct fixed-point multipliers, hence trivial automorphism group.

Every \(u\in U_C(k)\) defines a degree-three morphism \(\phi_u:C\to C\) over \(k\). Its underlying geometric conjugacy class determines \(\pi_C(u)\in\mathcal M_3(k)\). After extending scalars to an algebraic closure, \(\pi_C\) becomes the usual quotient map from the generic part of \(W\), so \(\pi_C:U_C\to\mathcal M_3\) is dominant.

**3. The obstruction is exactly \(C\).** Since the geometric automorphism group of \(\phi_u\) is trivial, an isomorphism between \(\phi_u\) and any other representative of its geometric class, if one exists, is unique. Suppose a conjugate representative \(\psi:\mathbb P^1_k\to\mathbb P^1_k\) existed over \(k\). Over \(\overline k\), there would be a unique dynamical isomorphism \(h:\mathbb P^1_{\overline k}\to C_{\overline k}\) between \(\psi\) and \(\phi_u\). Every Galois conjugate of \(h\) has the same property, and uniqueness forces it to equal \(h\). Thus \(h\) descends to \(k\), contradicting that \(C\) is nonsplit. Moreover, the unique descent torsor is exactly \(T_C\), not merely an unspecified nontrivial class, because \(\phi_u\) is already a model on \(C\). Consequently \(\pi_C(U_C(k))\subseteq S_C\).

**4. Explicit Hamilton instance and a check of the nonempty open.** Take \(L=k(i)\) and the projective involution \(\tau([X:Y])=[-Y:X]\). Its matrix \(J=\left(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\right)\) satisfies \(J^2=-I\); the corresponding nontrivial cocycle represents the quaternion algebra \((-1,-1)_k\) and the real-anisotropic conic \(C_0:X^2+Y^2+Z^2=0\). For any \(P\in L[X,Y]_3\), put \(Q(X,Y)=\overline P(Y,-X)\). Directly,
\[
Q(-Y,X)=\overline P(X,Y),\qquad -P(-Y,X)=\overline Q(X,Y),
\]
so \(\overline{[P:Q]}=\tau^{-1}\circ[P:Q]\circ\tau\). The four \(L\)-coefficients of \(P\) give eight independent \(k\)-coordinates; upon extension to \(\overline k\), these become all eight coordinates of an unrestricted cubic pair. This makes dominance and Zariski density completely explicit for \(C_0\).

For example, choose
\[
P=X^3+(1+i)X^2Y+(2+3i)XY^2+(1-2i)Y^3.
\]
The resultant of \(P(z,1)\) and \(Q(z,1)\) is \(675\). The fixed-point polynomial \(P(z,1)-zQ(z,1)\) has discriminant \(27760\). Up to multiplication by a nonzero constant, the polynomial of its four fixed-point multipliers is
\[
675m^4+920m^3+5658m^2+10984m+9523,
\]
whose discriminant is \(67927190083003088896000\ne0\). Thus all four fixed points are distinct, with pairwise distinct multipliers. Any dynamical automorphism fixes each of them and is therefore the identity.

**5. Density.** Since \(U_C\) is a nonempty open subset of affine eight-space over the infinite field \(k\), \(U_C(k)\) is Zariski dense in \(U_C\). Dominance of \(\pi_C\) shows that \(\pi_C(U_C(k))\), and hence \(S_C\), is Zariski dense in \(\mathcal M_3\). Because \(\dim \mathcal M_3=4\), the set contains infinitely many distinct coarse moduli points. This proves the claim for every fixed nonsplit conic. \(\square\)

## Verification
The standalone `verify.py` uses exact symbolic polynomial arithmetic in \(\mathbb Q(i)\) to confirm the Hamilton family's conjugation identities and the concrete witness's resultant, fixed-point discriminant, multiplier polynomial, and multiplier discriminant. The infinite-family theorem follows from the descent, dominance, and rational-density arguments, not the finite symbolic instance. The prescribed check can be run with `python verify.py` in an environment with SymPy.

## Relationship to prior work
Shaska (2026) proves explicit quaternion splitting criteria on the trivial-automorphism stratum and studies the distribution of fine/coarse rational moduli points by weighted height. West (2014) develops the invariant-theoretic quotient and obstruction conics for cubic rational maps; Hidalgo (2013) proves the existence of a field of definition of degree at most two over the field of moduli. Those results furnish background and some ingredients but do not state the present **fixed-class Zariski-density assertion**. In particular, finite-height census results, a descent criterion at an individual point, and rationality of the untwisted moduli variety do not by themselves assert that *every prescribed nonsplit conic class* is attained on a dense set. The additional argument is the linear \(\mathrm{PGL}_2\)-representation, its twist by arbitrary conic torsors, and the dominant map from each rational twisted affine parameter space.

## Limitations
This gives geometric Zariski density over \(\mathbb Q\), not a height-asymptotic count, a positive natural density of fixed-class points, or a local-global density formula. It is restricted to cubic self-maps with trivial geometric automorphisms, and says nothing about the special automorphism strata. The proof uses standard descent and geometric-quotient facts; an unlocated earlier general twist theorem may subsume this particular application. No independent audit has been performed.

## References
1. T. Shaska, *Fine points of the moduli space of cubic rational maps*, arXiv:2610.33990v1 (first submitted 2026-10-25), §§1–4.
2. L. W. West, *The moduli space of cubic rational maps*, arXiv:1408.3247v1 (2014), §§1–4.
3. R. A. Hidalgo, *A simple remark on the field of moduli of rational maps*, *Quarterly Journal of Mathematics* 65 (2014), 627–635; online 2013, doi:10.1093/qmath/hat012.

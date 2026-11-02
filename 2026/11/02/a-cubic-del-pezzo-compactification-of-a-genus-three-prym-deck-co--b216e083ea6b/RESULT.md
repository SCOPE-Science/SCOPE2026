# A cubic del Pezzo compactification of a genus-three Prym-deck coefficient quotient

## Finding

Borówka and Shatsila's explicit degree-two Prym correspondence for hyperelliptic genus-three curves with involutions (their Proposition 4.6) induces, on its unordered **coefficient cover** with nonzero coefficient sum, a regular fixed-point-free involution. Its affine quotient is the smooth surface
\[
Y=\operatorname{Spec}\left(\mathbb C[q,t,w,(t-4)^{-1},(q^2+4-2w+t)^{-1}]/(w^2-t(q^2+4))\right).
\]
Its closure in ordinary projective three-space is the normal rational cubic del Pezzo surface
\[
S:\qquad W^2Z=T(Q^2+4Z^2),
\]
with **exactly three rational double points**, of analytic types \(2A_1+A_3\). The two \(A_1\) points belong to the branch-collision boundary, while the \(A_3\) point lies at infinity. The divisorial boundary in the affine chart consists of a smooth conic \(t=4\) and a *doubled* rational collision curve \(t=w=q^2+4\); they meet at one geometric point with total local intersection length four (reduced contact order two).

The finite étale degree-two quotient morphism on the smooth coefficient locus extends canonically to a finite degree-two morphism from the normalization of \(S\) in its coefficient function field. This is an **explicit compactification of the lifted coefficient involution**, not an identification of \(S\) with the coarse Prym moduli target and not a full compactification of the Prym morphism on moduli stacks.

## Assumptions and scope

Work over \(k=\mathbb C\) throughout. For coefficients \(a,b\), consider the genus-three family
\[
C_{a,b}:\quad y^2=(x^4+a x^2+1)(x^4+b x^2+1).
\]
Its smooth coefficient locus has \(a\ne b\) and \(a,b\not\in\{-2,2\}\). Interchanging \(a,b\) does not alter the coefficient pair. On the open locus \(a+b\ne0\), use symmetric coordinates \(s=a+b\), \(p=ab\), followed by
\[
u=\frac{s}{4},\qquad v=\frac{p+4}{s}.
\]
These give the following **framed, unordered coefficient chart** (no coarse-moduli identification is assumed):
\[
U=\operatorname{Spec} k[u,u^{-1},v,\{(v^2-4)(u^2-uv+1)\}^{-1}].
\]
Indeed \((a-b)^2=16(u^2-uv+1)\) and \((a^2-4)(b^2-4)=s^2(v^2-4)\). The chart is irreducible, smooth, and nonempty.

The rational operation in Borówka--Shatsila, Proposition 4.6, is represented on this chart by
\[
(a,b)\longmapsto\left(\frac{2b-2a-8}{a+b},\frac{2a-2b-8}{a+b}\right),
\]
which becomes \(\phi(u,v)=(-u^{-1},-v)\). This statement concerns the explicitly supplied transformation on the coefficient cover; the moduli-space equivalences and markings may impose further identifications, which are not asserted away here.

## Proof

### 1. The involution acts regularly without fixed points

The substitution \(\phi\) has order two. It carries \(v^2-4\) to itself and \(c=u^2-uv+1\) to \(c/u^2\). Thus it preserves \(U\) and is a regular automorphism there. A fixed point must satisfy \(u^2=-1\) and \(v=0\), forcing \(c=0\); every such point has been excluded. Hence the action is free on \(U\).

### 2. Invariant ring and exact smooth quotient

Introduce \(q=u-u^{-1}\) and \(z=u+u^{-1}\). The Laurent ring admits the presentation
\[
k[u,u^{-1},v]\simeq k[q,z,v]/(z^2-q^2-4),
\]
where \(u=(q+z)/2\) and \(u^{-1}=(z-q)/2\). Under \(\phi\), \(q\) is fixed, while \(z\) and \(v\) change sign. Taking the even part gives, **as an equality of complete invariant rings**,
\[
k[u,u^{-1},v]^{\langle\phi\rangle}
\simeq k[q,t,w]/(w^2-t(q^2+4)),\qquad
 t=v^2,\quad w=vz.
\]
For example, an invariant polynomial reduces uniquely to an even polynomial in \(v\) with coefficients in \(k[q]\), plus \(zv\) times another even polynomial, because the algebra is free over \(k[q,v]\) with basis \(1,z\).

The two removed divisors descend exactly: \(v^2-4=t-4\) and
\[
q^2+4-2w+t=(z-v)^2=\left(\frac{u^2-uv+1}{u}\right)^2.
\]
Localization at their product commutes with taking invariants (the inverted expression is invariant). Therefore the quotient \(U/\langle\phi\rangle\) is exactly the specified \(Y\), not merely birational to it. Since the action is free and its order is invertible in \(k\), the quotient map \(U\to Y\) is finite étale of degree two. In particular, \(Y\) is smooth.

### 3. Projective closure, irreducibility and normality

Homogenizing \(w^2=t(q^2+4)\) gives
\[
G(Q,T,W,Z)=W^2Z-T(Q^2+4Z^2).
\]
The quotient invariant ring is a domain, hence the affine hypersurface is integral and its projective closure \(S=V(G)\subset\mathbb P^3\) is irreducible. (There is no extra component in \(Z=0\), because \(G\) is not divisible by \(Z\).)

The four partial derivatives are
\[
G_Q=-2TQ,\qquad G_T=-Q^2-4Z^2,\qquad G_W=2WZ,\qquad G_Z=W^2-8TZ.
\]
In the affine chart \(Z=1\), the common vanishing conditions yield exactly the two points
\[
P_\pm=[\pm2i:0:0:1].
\]
At either point \(h=q^2+4\) is a local coordinate because \(h'(\pm2i)\ne0\), and the equation is \(w^2-th=0\): an ordinary \(A_1\) node. On the hyperplane \(Z=0\), the partials force \(Q=W=0\), hence the only singular point there is
\[
P_\infty=[0:1:0:0].
\]
On the chart \(T=1\), the local equation at \(P_\infty\) is \(Q^2+4Z^2-W^2Z=0\). Replacing \(Z\) by \(Z'=Z-W^2/8\), then factoring over \(\mathbb C\), yields
\[
(Q+2iZ')(Q-2iZ')=W^4/16,
\]
the exact analytic \(A_3\) normal form, not just a tangent-cone assertion. There are no other singularities. Since \(S\) is a hypersurface with only isolated singularities, it satisfies \(S_2\) and \(R_1\), so is normal. Adjunction gives \(-K_S\cong\mathcal O_S(1)\), an ample Cartier divisor; thus this is a degree-three (singular) del Pezzo surface. Its minimal resolution is weak del Pezzo.

The surface is rational: on the dense open set where \(t,w\ne0\), put \(\zeta=w/t\), so \(t=(q^2+4)/\zeta^2\) and \(w=(q^2+4)/\zeta\). Hence \(k(S)=k(q,\zeta)\).

### 4. The boundary, including scheme structure and contact

Write \(h=q^2+4\) and \(N=h-2w+t\). The affine boundary in \(S\) is the union of divisors \(t=4\) and \(N=0\). The first is the smooth irreducible affine conic \(w^2=4(q^2+4)\). For the second, setting \(t=2w-h\) in the surface equation gives \((w-h)^2=0\). Thus the **scheme-theoretic** divisor of \(N\) is a doubled rational curve supported on
\[
B:\quad t=w=q^2+4.
\]
The nodes \(P_\pm\) lie on this boundary, so none lies in \(Y\). The conic and \(B\) meet at \((q,t,w)=(0,4,4)\). In the complete scheme intersection \((t-4,N)\), substitution yields \(q^4/4=0\); hence its local length is four. The reduced curve \(B\) has intersection multiplicity two with the conic.

The hyperplane at infinity \(Z=0\) meets \(S\) scheme-theoretically in the line \(T=0\) plus twice the line \(Q=0\), because \(G|_{Z=0}=-TQ^2\). The \(A_3\) point lies on the second line. Thus the three ADE points have a specified location relative to the degeneration boundary.

### 5. Finite projective extension

The inclusion of fields \(k(Y)\subset k(U)\) is separable quadratic and \(S\) is normal and projective. Let \(\overline U\) be the normalization of \(S\) in \(k(U)\). It is finite and projective over \(S\), with an extended involution; restricting to \(Y\) recovers \(U\to Y\), because \(U\) is already normal and finite over \(Y\). This constructs a projective extension of the coefficient involution's quotient map. It does **not** claim that \(\overline U\) or \(S\) equals a canonical coarse-moduli compactification of the Prym map.

## Verification

The accompanying `verify_quotient.py` uses exact SymPy rational arithmetic to verify the source coordinate change, involution, two invariant generators, invariant equation, boundary identities, four partial derivatives, affine and infinity singular candidates, and the exact \(A_3\) coordinate identity. It also exhaustively enumerates the admissible \(\mathbb F_7\) and \(\mathbb F_{13}\) coefficient chart points, demonstrating invariant fibres of size two and no fixed points (these are finite sanity tests, not substitutes for the invariant-ring and geometric proofs). Run `python3 verify_quotient.py`. Its final message is `PRYM_DECK_CUBIC_QUOTIENT_AND_A3_2A1_PASS`.

## Relationship to prior work

Borówka and Shatsila [1, Proposition 4.6] derive the rational deck operation and [1, Theorem 3.10] its generic degree-two Prym interpretation. Their final Section 4 question explicitly asks for compactifications of the moduli spaces and Prym map. Those statements are antecedents and are not presented here as new. The contribution here is the **exact invariant ring and admissible open quotient for that coefficient transformation**, together with a concrete normal cubic del Pezzo compactification, its complete ADE basket, and the doubled collision-boundary scheme and contact calculation. This is a **coefficient-level partial step**, not an answer to the full moduli question. The general classifications of rational double points and cubic del Pezzo surfaces supply standard context but do not by themselves identify this explicit Prym-deck quotient.

## Limitations

All statements are over \(\mathbb C\), restricted to the open \(a+b\ne0\). The degeneration \(a+b=0\), moduli identifications beyond the unordered-coefficient representation, stabilizer data for the actual moduli stack, and the extension of the geometric Prym morphism are not determined. Normalizing \(S\) in the function field is a finite projective extension of the **coefficient quotient**, not a modular interpretation. The quotient cubic is not asserted to be canonical or unique. A prior unindexed computation of the invariant ring or a fuller 2023 thesis/journal treatment could affect priority; independent external audit has not been performed.

## References

1. P. Borówka and A. Shatsila, *Hyperelliptic genus 3 curves with involutions and a Prym map*, arXiv:2308.07038, first submitted 2023-08-14, especially Theorem 3.10, Proposition 4.6 and the concluding open question. https://arxiv.org/abs/2308.07038. Journal version: *Mathematische Nachrichten* **297** (2024), 3080–3094, DOI 10.1002/mana.202300468.
2. A. Shatsila, *Hyperelliptic genus 3 curves with additional involutions and Prym map*, master's thesis, Jagiellonian University, 2023. Repository record https://ruj.uj.edu.pl/handle/item/314933 (only bibliographic record and abstract accessible in this inspection).
3. Standard hypersurface adjunction, Serre normality criterion, and the classical ADE surface singularity normal forms are used in their usual characteristic-zero senses; the specific local equations are proved above.

# Biquadratic bitangent splitting cover and arithmetic profiles of the Ciani pencil

## Finding

For the symmetric pencil
\[
C_\lambda:\quad F_\lambda(X,Y,Z)=X^4+Y^4+Z^4+\lambda(X^2Y^2+Y^2Z^2+Z^2X^2)=0,
\]
the **exact simultaneous bitangent splitting field** over the rational function field \(k=\mathbb Q(\lambda)\) is
\[
L=k\left(\sqrt{-\lambda-1},\sqrt{\lambda+2}\right),\qquad \operatorname{Gal}(L/k)\cong C_2\times C_2.
\]
Its action on the 28 geometric bitangents has orbit lengths \(1^4 2^6 4^3\). The normal (four-sheeted) splitting cover is the rational map
\[
\lambda=-\frac{2(t^4+1)}{(t^2+1)^2};
\]
its only branch values on \(\mathbb P^1\) are \(-2,-1,\infty\), with inertia order two. In particular, the singular parameter \(\lambda=2\) is **unramified** in this cover.

For any \(\lambda\in\mathbb Q\setminus\{-2,-1,2\}\), all 28 bitangents have equations over precisely
\[
L_\lambda=\mathbb Q\left(\sqrt{-\lambda-1},\sqrt{\lambda+2}\right).
\]
Writing \(d=\dim_{\mathbb F_2}\langle[-\lambda-1],[\lambda+2]\rangle\) in \(\mathbb Q^\times/(\mathbb Q^\times)^2\), the degree \([L_\lambda:\mathbb Q]\) equals \(2^d\) and is exactly \(1,2\), or \(4\). All 28 bitangents are rational exactly when
\[
\lambda=-\frac{2(t^4+1)}{(t^2+1)^2},\quad t\in\mathbb Q\setminus\{0,\pm1\}.
\]
For real nonsingular parameters, the real bitangent counts are \(16\) for \(\lambda<-2\), \(28\) for \(-2<\lambda<-1\), and \(4\) for \(\lambda>-1\) (with \(\lambda=2\) excluded).

## Assumptions and scope

The ground field has characteristic zero. A bitangent means a line whose intersection divisor with a smooth quartic is twice a degree-two divisor; hyperflex lines are counted once. The quartic is smooth if and only if \(\lambda\notin\{-2,-1,2\}\). The generic Galois assertions refer to the rational function field \(\mathbb Q(\lambda)\), and the arithmetic specializations refer only to nonsingular rational values of \(\lambda\). A field of definition here is the least field over which **every bitangent line individually** has an equation, not merely the field of definition of the unordered collection, which is already rational.

## Proof

**Smoothness and a complete bitangent presentation.** Differentiation yields
\[
\frac{\partial F_\lambda}{\partial X}=2X\bigl(2X^2+\lambda(Y^2+Z^2)\bigr)
\]
and cyclic analogues. If all three coordinates are nonzero, their squares satisfy a linear system with determinant \(2(2-\lambda)^2(1+\lambda)\) up to a nonzero constant; if exactly two are nonzero, the determinant is \(4-\lambda^2\); if only one is nonzero, the gradient cannot vanish. Conversely the excluded parameters have singular points. Hence precisely \(-2,-1,2\) are singular.

Fix
\[
a^2=-\lambda-1,\qquad b^2=\lambda+2,\qquad s=\frac{1+a}{b}.
\]
For nonsingular parameters these are nonzero as needed, and direct simplification gives
\[
a=\frac{s^2-1}{s^2+1},\quad b=\frac{2s}{s^2+1},\quad
(\lambda+2)(s^4+1)+2\lambda s^2=0.
\]
The following three identities, valid under these relations, certify bitangency:
\[
F_\lambda(sY,Y,Z)=\left(Z^2+\frac\lambda2(s^2+1)Y^2\right)^2,
\]
\[
F_\lambda(X,Y,X+Y)=(\lambda+2)(X^2+XY+Y^2)^2,
\]
\[
F_\lambda(X,Y,aX+Y)=(\lambda+2)(Y^2+aXY-X^2)^2.
\]
Applying coordinate permutations and independent sign changes (modulo simultaneous sign) produces **all** the following distinct lines:

- Twelve axis-type lines \(X_i=s'X_j\), one for each of the three unordered coordinate pairs \(\{i,j\}\) and each \(s'\in\{s,-s,s^{-1},-s^{-1}\}\).
- Four constant lines \(\varepsilon X+\delta Y+Z=0\), where \(\varepsilon,\delta\in\{\pm1\}\).
- Twelve mixed lines \(\varepsilon X_i+\delta X_j+aX_k=0\), one for each choice of distinguished coordinate \(k\) and each \(\varepsilon,\delta\in\{\pm1\}\).

The three families have sizes \(12,4,12\); no two lines coincide because \(a\notin\{0,\pm1\}\), \(s\notin\{0,\pm1,\pm i\}\), and their coefficient-zero patterns distinguish the axis type from the others. By the classical theorem that every smooth characteristic-zero plane quartic has exactly 28 geometric bitangents (including hyperflexes), the list is exhaustive. This formula is used here as a proof instrument; historical bitangent formulas and the Edge parametrization are **not** claimed as discoveries.

**Minimality of the field.** Every displayed line is defined over \(k(a,b)\). Conversely an axis-type line \(X=sY\) fixes the coefficient ratio \(s\) in the field of definition of all lines, and a mixed line \(X+Y+aZ=0\) fixes \(a\). Consequently that field contains \(b=(1+a)/s\). Thus the splitting field is exactly \(L=k(a,b)\), not a smaller field. The rational specialization argument is word-for-word identical; denominators cannot vanish on a smooth member.

**Galois and monodromy.** The functions \(-\lambda-1\) and \(\lambda+2\) have odd valuations at distinct rational places \(\lambda=-1\) and \(\lambda=-2\), so their square classes in \(k^\times/(k^\times)^2\) are independent. The resulting group is \(V_4\). The involution changing \(b\) changes \(s\) to \(-s\) and fixes \(a\); changing \(a\) changes \(s\) to \(s^{-1}\) and sends \(a\) to \(-a\). Thus the 12 axis lines form three orbits of size four, the 12 mixed lines six of size two, and the four constant lines four fixed orbits.

Inverting the expression for \(s\) yields
\[
\lambda=-\frac{2(s^4+1)}{(s^2+1)^2},\qquad
\lambda+2=\frac{4s^2}{(s^2+1)^2},\qquad
-\lambda-1=\frac{(s^2-1)^2}{(s^2+1)^2}.
\]
This degree-four normal cover is ramified at \(s=0,\infty\) above \(\lambda=-2\), at \(s=\pm1\) above \(\lambda=-1\), and at \(s=\pm i\) above \(\lambda=\infty\), each of ramification index two. The derivative
\[
\frac{d\lambda}{ds}=-\frac{8s(s^2-1)}{(s^2+1)^3}
\]
and the local coordinates near infinity exclude any additional branch points. In particular the exceptional quartic parameter \(\lambda=2\) is not a branch value.

**Every rational specialization and real counts.** For rational nonsingular \(\lambda\), the same explicit line presentation and minimality prove \(L_\lambda=\mathbb Q(a,b)\). The elementary classification of composita of quadratic fields gives degree \(2^d\) for the displayed square classes. Full rationality is equivalent to \(a,b\in\mathbb Q\), hence to \(s=(1+a)/b\in\mathbb Q\); conversely any \(s=t\in\mathbb Q\setminus\{0,\pm1\}\) yields a smooth parameter by the displayed formula and makes both \(a,b\) rational. Finally, the two real radical signs show: if \(\lambda<-2\), \(a\) is real and \(b\) purely imaginary, so only the 4 constant and 12 mixed lines are real; if \(-2<\lambda<-1\), both radicals are real and all 28 lines are real; if \(\lambda>-1\), \(a\) is imaginary and \(b\) real, so only the four constant lines are real.

## Verification

The attached `verify_bitangents.py` is an executable exact symbolic verifier (Python 3 plus SymPy). Its assertions check all three square-restriction identities, the relation between \(s,a,b\), pairwise distinctness of 28 lines over \(\mathbb Q(s)\), exact Galois permutations and orbit counts, the derivative, the three branch fibres, the explicit quadratic subfields, and three nonsingular rational specializations. Run `python verify_bitangents.py`; expected terminal messages begin `VERIFY_OK`. The independent geometric steps are the standard characteristic-zero 28-bitangent count, the elementary singularity gradient test, the valuation argument for quadratic independence, and the field-minimality argument above. Exhaustive verification of 28 candidate equations is not substituted for the proof of a statement about infinitely many parameters.

## Relationship to prior work

Janasz–Pokora–Zieliński [1] introduce the same Ciani pencil and compute bitangent-line incidence arrangements for three special complex parameters; the present result instead computes the **least field defining every bitangent**, its biquadratic Galois action and branch structure, for every nonsingular parameter, including all rational specializations and real regimes. Bethea–Brazelton [2, §4] determine complex-automorphism orbits for the symmetric quartic types; their Type IV orbits are not arithmetic Galois orbits, and the distinction matters. Their Remark 4.4 notes that Edge [3, §14] already parametrized this pencil in precisely the displayed variable \(s\) and studied bitangents. Thus the parametrization, the existence of the 28 lines, and special rational examples are **prior art**, not the asserted new result. Bruin–Lewis [4] study descent when all 28 bitangents are rational; the explicit complete condition for this pencil supplies a natural arithmetic input to that framework.

## Limitations

The result concerns simultaneous individual fields of definition of 28 bitangent lines, not the fields of their contact points, the full rational two-torsion structure, or a descent certificate for rational points on any particular quartic. The arithmetic orbit statement \(1^4 2^6 4^3\) is generic; special rational parameters may have smaller Galois groups as explicitly classified by the square classes. The three excluded parameters produce singular plane quartics and are outside the 28-bitangent theorem. Edge's original 1938 article could not be fully inspected despite a lawful access attempt; earlier literature may contain more of the arithmetic consequences than can presently be confirmed. No independence or external peer assessment is asserted.

## References

[1] M. Janasz, P. Pokora, M. Zieliński, *On arrangements of smooth plane quartics and their bitangents*, arXiv:2308.16514 (first posted 2023-08-31), especially §3, Propositions 3.1–3.4. https://arxiv.org/abs/2308.16514

[2] C. Bethea, T. Brazelton, *Bitangents to symmetric quartics*, arXiv:2410.09242 (2024), especially Remark 4.4 and §4.4. https://arxiv.org/abs/2410.09242

[3] W. L. Edge, *Determinantal representations of* \(x^4+y^4+z^4\), *Math. Proc. Cambridge Philos. Soc.* **34** (1938), 6–21, especially §14 (as described and quoted in [2]). DOI: 10.1017/S0305004100019848.

[4] N. Bruin, D. Lewis, *Two-cover descent on plane quartics with rational bitangents*, arXiv:2003.00666 (2020), introductory theory and examples. https://arxiv.org/abs/2003.00666

# Quadratic Frobenius splitting and an exact rational-bitangent census for Ciani's quartic pencil

## Finding
Let \(q\) be an odd prime power, \(k=\mathbb F_q\), and let
\[
C_\lambda:\;X^4+Y^4+Z^4+\lambda(X^2Y^2+X^2Z^2+Y^2Z^2)=0,\qquad \lambda\in k\setminus\{-2,-1,2\}.
\]
The excluded set is interpreted as a set of distinct field elements; in characteristic \(3\) it has two elements. Every such \(C_\lambda\) is geometrically smooth. Write \(\chi=\chi_q\) for the quadratic character, extended by \(\chi(0)=0\), and let \(N_\lambda\) be the number of \(k\)-rational bitangent lines, counting a hyperflex line as a bitangent. Then
\[
N_\lambda=\begin{cases}
4,&\chi(-1-\lambda)=-1,\\
16,&\chi(-1-\lambda)=1,\ \chi(\lambda+2)=-1,\\
28,&\chi(-1-\lambda)=\chi(\lambda+2)=1.
\end{cases}
\]
Every one of the \(28\) geometric bitangents is defined over \(\mathbb F_{q^2}\). In particular the reduced finite étale bitangent locus \(B_\lambda\) has
\[
Z(B_\lambda/k,T)=(1-T)^{-N_\lambda}(1-T^2)^{-(28-N_\lambda)/2}.
\]
The following counts are for literal parameters \(\lambda\in k\), not for geometric isomorphism classes. Put \(\epsilon=\chi(-1)\). If the characteristic is not \(3\), put \(\eta=\chi(-3)\), \(S=(q-4-\eta)/2\), and \(M=(q-4-\epsilon)/4-(1+\eta)/2\). Then exactly \(q-3-S\), \(S-M\), and \(M\) smooth parameters have respectively \(4\), \(16\), and \(28\) rational bitangents. In characteristic \(3\), put \(S=(q-3)/2\), \(M=(q-4-\epsilon)/4\); the three frequencies are \(q-2-S\), \(S-M\), and \(M\), respectively.

## Assumptions and scope
The base field is any finite field of odd characteristic; no characteristic-zero specialization argument is used. A geometric bitangent is a line whose scheme-theoretic intersection with the smooth plane quartic equals twice an effective degree-two divisor over the algebraic closure (including the case of a quadruple contact). Equivalently, the restricted binary quartic is a nonzero scalar multiple of a square of a binary quadratic. The arithmetic counts concern lines defined over the ground field, regardless of whether their contact points are rational. The bitangent locus in the zeta formula is its reduced closed-point scheme.

## Proof
**Smoothness.** The partial derivative with respect to \(X\) is
\[
F_X=2X\bigl((2-\lambda)X^2+\lambda(X^2+Y^2+Z^2)\bigr),
\]
and similarly for \(Y,Z\). The value \(\lambda=2\) gives a doubled conic. At \(\lambda=-2\) there are singular points with one zero coordinate and the other two squares equal. At \(\lambda=-1\) there are singular points with all three coordinate squares equal (in characteristic \(3\), \(-1=2\)). Conversely, a singular point cannot have just one nonzero coordinate. With exactly two nonzero coordinates the derivative and equation force \(\lambda=\pm2\). With all three nonzero and \(\lambda\ne2\), the derivatives force equal coordinate squares, whence \(\lambda=-1\). This is exhaustive over an algebraic closure.

**All geometric bitangents.** In an algebraic closure choose \(\rho,s\) with
\[
\rho^2=-1-\lambda,\qquad s^2=\lambda+2.
\]
Neither is zero and \(\rho^2\ne1\). The following lines form three disjoint groups:

1. Four sign lines \(X\pm Y\pm Z=0\), modulo common sign.
2. Twelve lines with one coefficient \(\rho\), and the other two coefficients \(\pm1\): \(\rho X\pm Y\pm Z=0\) and its two permutations of the distinguished coordinate.
3. Twelve lines with one coefficient zero and ratio between the other two nonzero coefficients in
\[
K=\left\{\pm\frac{1+\rho}{s},\ \pm\frac{1-\rho}{s}\right\};
\]
for example \(Z=\kappa X\), for \(\kappa\in K\), and the analogous lines on the other two coordinate pairs.

These lines are bitangents by explicit identities. On \(Z=-X-Y\), one has
\[
F_\lambda(X,Y,-X-Y)=(\lambda+2)(X^2+XY+Y^2)^2.
\]
On \(Z=-\rho X-Y\), using \(\rho^2=-1-\lambda\), one has
\[
F_\lambda(X,Y,-\rho X-Y)=(\lambda+2)(X^2-\rho XY-Y^2)^2.
\]
Finally, each \(\kappa\in K\) satisfies
\[
(\lambda+2)(\kappa^4+1)+2\lambda\kappa^2=0,
\]
which implies
\[
F_\lambda(X,Y,\kappa X)=\left(Y^2+\frac{\lambda(1+\kappa^2)}2 X^2\right)^2.
\]
The four sign lines have all three coefficients nonzero and equal in square; the twelve mixed lines have precisely one distinct coefficient square \(\rho^2\ne1\); and the coordinate lines have one coefficient zero. The parameter restrictions and odd characteristic make all \(28\) listed lines distinct. By the classical theta-characteristic count, a smooth nonhyperelliptic genus-three plane quartic in characteristic different from \(2\) has exactly \(28\) geometric bitangent lines (with hyperflexes included). Hence the displayed list is complete.

**Frobenius descent.** The first four lines are defined over \(k\). The twelve mixed lines are defined over \(k\) exactly when \(\rho\in k\), equivalently \(\chi(-1-\lambda)=1\). The other twelve lines have ratio \(\kappa\in K\). If \(\rho\in k\), these ratios are in \(k\) precisely when \(s\in k\), since \(1\pm\rho\ne0\). If \(\rho\notin k\), the two distinct values \(\kappa^2\) are Galois-conjugate and none is rational: their discriminant is a nonzero square multiple of \(\rho^2=-1-\lambda\). Thus the coordinate-type lines are rational exactly when both \(-1-\lambda\) and \(\lambda+2\) are squares in \(k\). The three values of \(N_\lambda\) follow. Both quadratic radicals belong to \(\mathbb F_{q^2}\), so all lines descend after a degree-at-most-two extension; the stated zeta function counts the \(N_\lambda\) fixed points and \((28-N_\lambda)/2\) Frobenius two-cycles.

**Parameter frequencies.** Substitute \(d=-1-\lambda\). Smooth parameters correspond to \(d\notin\{0,1,-3\}\); in characteristic \(3\), the excluded set is \(\{0,1\}\). Counting nonzero squares \(d\), while excluding \(d=1\) and (if nonzero square) \(d=-3\), gives the stated \(S\). Before excluding \(d=-3\), the number of nonzero squares \(d\) for which \(1-d\) is also nonzero square equals
\[
\frac{q-4-\chi(-1)}4.
\]
Indeed, the affine conic \(u^2+v^2=1\) has \(q-\chi(-1)\) points, four with \(uv=0\), and every remaining pair of nonzero squares \((u^2,v^2)\) has four preimages. For characteristic other than \(3\), the additionally forbidden \(d=-3\) contributes one to this number precisely when \(\chi(-3)=1\), because then \(1-d=4\) is a nonzero square. This yields \(M\), and subtraction gives the other two frequencies.

## Verification
The dependency-free script `verify_ciani_bitangents.py` enumerates every rational projective line and tests whether its restricted binary quartic is a geometric square, using exact polynomial coefficient identities over finite fields. For each smooth parameter it compares the independent line census with the character formula and compares the full observed parameter-frequency distribution with the theorem. It passed in the \(13\) fields of orders \(3,5,7,9,11,13,17,19,23,25,29,31,49\), across \(204\) smooth parameters; terminal marker: `CIANI_BITANGENT_CLASSIFICATION_PASS`. The algebraic proof, not the finite enumeration, establishes the result for all odd prime powers.

## Relationship to prior work
Janasz--Pokora--Zieliński (arXiv:2308.16514, initial submission 2023-08-31) introduce this exact pencil in their Section 3 and investigate complex bitangent incidence and special highly symmetric members. Bethea--Brazelton, *Bitangents to Symmetric Quartics*, Section 4.4, identify the geometric \(S_4\)-orbit decomposition \(12+12+4\) of the bitangents in the generic octahedral pencil. These geometric decompositions are prior work and are not asserted to be new. Lercier--Ritzenthaler--Rovetta--Sijsling (arXiv:1403.0562) provide finite-field moduli and curve-representative techniques, not the parameter-wise bitangent descent counts here. The contribution assessed here is the all-odd-prime-power quadratic-character descent, complete parameter frequencies and finite étale bitangent zeta function, not the existence of \(28\) bitangents or the geometric orbit structure.

## Limitations
The frequencies count literal \(\lambda\)-coefficients, not isomorphism classes of curves or twists. This does not classify rational contact divisors or rational points on the quartic. The geometric bitangent formulas are classical in character; an alternative derivation of the arithmetic classification in historical or unindexed sources remains a priority risk. Finite numerical checks are supporting evidence only. No independent validation has been performed.

## References
- M. Janasz, P. Pokora, M. Zieliński, *On arrangements of smooth plane quartics and their bitangents*, arXiv:2308.16514 (first posted 2023-08-31), especially Section 3, https://arxiv.org/abs/2308.16514 .
- C. Bethea, T. Brazelton, *Bitangents to Symmetric Quartics*, Section 4.4, https://tbrazel.github.io/assets/papers/bitangents.pdf .
- R. Lercier, C. Ritzenthaler, F. Rovetta, J. Sijsling, *Parametrizing the moduli space of curves and applications to smooth plane quartics over finite fields*, arXiv:1403.0562, https://arxiv.org/abs/1403.0562 .
- I. Bouw, N. Coppola, E. Lorenzo García, A. Somoza, *On the conductor of Ciani plane quartics*, arXiv:2310.10416, https://arxiv.org/abs/2310.10416 .

# Rational singularity types and Frobenius splitting in a plane-filling pencil

## Finding

Let \(q\) be any odd prime power, let \(k\in\mathbb F_q\), and let \(C_k\subset\mathbb P^2_{\mathbb F_q}\) be the plane-filling curve of Asgarli--Ghioca defined by
\[
F_k=X^2(X^qY-XY^q)+Y^2(Y^qZ-YZ^q)+(Z^2+kX^2)(Z^qX-ZX^q)=0.
\]
**Every \(\mathbb F_q\)-rational singularity is either an ordinary node or an ordinary unibranch cusp with \(\delta=1\).** For \(t\in\mathbb F_q^\times\), such a singularity occurs exactly at
\[
P_t=[t^2:t^3:1]\quad\text{for}\quad k=t^3-t^{-4}.
\]
It is a cusp exactly when \(t^7=4\); otherwise it is a node. A rational node has two \(\mathbb F_q\)-rational normalization branches (is *split*) exactly when the quadratic character satisfies
\[
\chi_q\bigl(t(t^7-4)\bigr)=1,
\]
and otherwise has two conjugate branches (is *nonsplit*).

As \(k\) ranges over all \(\mathbb F_q\), the sum of the numbers of rational singular points is exactly \(q-1\). Put
\[
c_q=\#\{t\in\mathbb F_q^\times:t^7=4\},\qquad
S_q=\sum_{t\in\mathbb F_q^\times}\chi_q\bigl(t(t^7-4)\bigr),
\]
where \(\chi_q(0)=0\). The total numbers of cusps, split nodes, and nonsplit nodes across the pencil, counted with their parameter and rational point, are respectively
\[
\boxed{\quad c_q,\qquad\frac{q-1-c_q+S_q}{2},\qquad\frac{q-1-c_q-S_q}{2}.\quad}
\]
If \(7\nmid(q-1)\), these are *explicitly*
\[
\boxed{\quad1,\qquad\frac{q-3}{2},\qquad\frac{q-1}{2}.\quad}
\]
If \(7\mid(q-1)\), then \(c_q\in\{0,7\}\), determined by whether \(4\) is a seventh power in \(\mathbb F_q\). In this regime the smooth genus-three hyperelliptic curve \(H:V^2=U(U^7-4)\) satisfies
\[
S_q=\#H(\mathbb F_q)-q-2,
\]
so its Frobenius point count computes the complete split/nonsplit distribution.

A member \(C_k\) has a rational cusp if and only if
\[
\boxed{256k^7=3^7\quad\text{in }\mathbb F_q.}
\]
When \(\operatorname{char}\mathbb F_q\ne3\), each such member has exactly one rational cusp. In characteristic three, only \(k=0\) has cusps, and it has precisely \(\gcd(7,q-1)\) of them.

## Assumptions and scope

The base field is \(\mathbb F_q\) for an arbitrary odd prime power \(q\ge3\), and the equations are the displayed homogeneous equations, without changing their projective model. A rational singularity means a *geometric singular point whose coordinates belong to* \(\mathbb F_q\). A split node has two separately rational preimages under normalization over the algebraic closure; a nonsplit node has two preimages exchanged by Frobenius. Counts are over all parameter-point pairs \((k,P)\) and do **not** count singularities away from \(\mathbb F_q\). In the hyperelliptic clause, \(7\mid(q-1)\) automatically excludes characteristic seven, ensuring that the polynomial is separable. No global smoothness or geometric irreducibility of all members is asserted.

## Proof

**1. Exact rational singular locus.** Every \(\mathbb F_q\)-point lies on \(C_k\). On \(Z=1\), write its coordinates as \((a,b)\). Differentiation in characteristic dividing \(q\), followed by \(a^q=a\) and \(b^q=b\), yields
\[
(F_k)_X(a,b,1)=1+ka^2-a^2b,\quad
(F_k)_Y(a,b,1)=a^3-b^2,\quad
(F_k)_Z(a,b,1)=b^3-a(1+ka^2).
\]
The first two equations force \(a,b\ne0\), \(b^2=a^3\), and \(1+ka^2=a^2b\); the third follows. Setting \(t=b/a\) gives \(a=t^2\), \(b=t^3\), and \(k=t^3-t^{-4}\). At \(Z=0\), \((F_k)_Y=X^{q+2}\); if \(X=0\), then \((F_k)_Z=Y^{q+2}\). Therefore no rational point at infinity is singular. Equivalently, with \(s=t^{-1}\), the source's singular-point criterion is \(s^7+ks^3-1=0\). This part refines, but does not claim priority over, that criterion.

**2. Complete local two- and three-jets.** Fix a rational singularity \(P_t\), and write \(X=t^2+u\), \(Y=t^3+v\), \(Z=1\). Since \(q\ge3\), the Frobenius terms have order at least three. For \(q=3\), their possible cubic contributions cancel *at a singular point*, using \(a^3=b^2\) and \(1+ka^2=a^2b\). Thus, for every odd \(q\), the exact expansion modulo \((u,v)^4\) is
\[
F_k(t^2+u,t^3+v,1)
=2(-t^{-2}u^2+t^4uv-t^3v^2)
+t^2u^2v-t^{-4}u^3-v^3+O((u,v)^4).
\]
Its quadratic discriminant is \(4t(t^7-4)\). If \(t^7\ne4\), the nondegenerate quadratic tangent cone proves that the singularity is an ordinary node. Its two tangent lines are rational precisely when this discriminant is a nonzero square. This is also the Frobenius splitting criterion for the normalization branches.

If \(t^7=4\), the quadratic term becomes
\[
-2t^3\bigl(v-\tfrac t2u\bigr)^2.
\]
Along the unique tangent \(v=\tfrac t2u\), the cubic term equals \(\tfrac12t^{-4}u^3\ne0\). As two is invertible, Weierstrass preparation and completing the square over an algebraic closure give the completed local equation \(w^2=u^3\) up to formal changes of coordinates and multiplication by units: the coefficient of \(u^3\) is a unit, whose square root exists formally. Thus this is a reduced, unibranch multiplicity-two cusp with \(\delta=1\), including in characteristic three. There are no higher rational singularity types.

**3. Cusp parameters and total incidence.** The map \(t\mapsto k=t^3-t^{-4}\) assigns exactly one parameter to each nonzero \(t\). Therefore there are exactly \(q-1\) rational singular parameter-point pairs. A cusp requires \(t^7=4\), and its parameter then satisfies \(k=3t^{-4}\), whence \(4^4 k^7=3^7\). Conversely, if \(3\ne0\) and \(256k^7=3^7\), the element \(t=9/(4k^2)\) has \(t^7=4\) and \(k=3t^{-4}\); it is the unique cusp parameter preimage. In characteristic three, the equation reduces to \(k=0\), and the cusp roots are precisely \(t^7=1\), of which there are \(\gcd(7,q-1)\). The number of solutions \(t^7=4\) is one if \(7\nmid(q-1)\), and otherwise zero or seven as stated.

**4. Arithmetic distribution.** For a node, the two rational tangent directions are counted by \(\chi_q(t(t^7-4))\). Consequently \(N_{\mathrm{split}}-N_{\mathrm{nonsplit}}=S_q\), while their sum is \(q-1-c_q\), yielding the formulas. If \(7\nmid(q-1)\), substitution \(w=t^7\) is a permutation of \(\mathbb F_q^\times\) and \(\chi_q(t)=\chi_q(w)\) (because seven is odd). Hence
\[
S_q=\sum_{w\in\mathbb F_q}\chi_q(w(w-4))=-1
\]
by the standard nonzero-discriminant quadratic-character identity. If \(7\mid(q-1)\), \(U(U^7-4)\) has eight distinct roots (characteristic is neither two nor seven), so \(H\) is a smooth hyperelliptic genus-three curve. Its monic degree-eight equation has two rational points at infinity, and direct affine point counting gives \(\#H(\mathbb F_q)=q+2+S_q\).

## Verification

The standalone `verify.py` uses only Python's standard library. It enumerates rational singular parameter-point pairs in fourteen prime fields, checks the exact local quadratic and cubic coefficients, matches node splitting with the quadratic character, and verifies the total census. For the five smallest tested primes it also exhaustively checks *all* projective rational points to exclude overlooked rational singularities. Values include \(q=3\) with one cusp and one nonsplit node across the pencil; \(q=7\) with one cusp, two split nodes, and three nonsplit nodes; and \(q=71\) with no cusps, forty-two split nodes, and twenty-eight nonsplit nodes. Finite enumeration corroborates but does not replace the proof for arbitrary prime powers.

## Relationship to prior work

Asgarli and Ghioca, *Plane-filling curves of small degree over finite fields*, arXiv:2307.03072 (first public version 2023-07-06), construct the pencil and prove in Theorem 1.2 that singular rational points exist exactly when \(s^7+ks^3-1\) has an \(\mathbb F_q\)-root; Theorem 1.8 generalizes the existence criterion to higher-degree plane-filling pencils. Their Conjecture 1.5 addresses **global** smoothness, a different question. Neither theorem specifies the ordinary-node/cusp threshold, rational branch splitting, the characteristic-three concentration of cusps, or the genus-three character-sum census. Homma--Kim's earlier minimum-degree plane-filling work treats a different degree-\(q+2\) family. General facts about tangent cones, formal plane cusps, and quadratic character sums are used as standard tools, not claimed as discoveries.

## Limitations

All singularity types and counts are restricted to \(\mathbb F_q\)-rational singular points. The theorem does not rule out geometric singularities in extension fields; it does not settle the original global smoothness conjecture. In the clause \(7\mid(q-1)\), the formula expresses the remaining arithmetic via a genus-three curve but does not supply a uniform elementary closed form for its point count.

## References

1. S. Asgarli and D. Ghioca, *Plane-filling curves of small degree over finite fields*, arXiv:2307.03072v1 (2023-07-06), especially Theorems 1.2 and 1.8 and Sections 3--4. Full text: https://arxiv.org/html/2307.03072v1 .
2. M. Homma and S. J. Kim, *Nonsingular plane filling curves of minimum degree over a finite field and their automorphism groups: supplements to a work of Tallini*, Linear Algebra and its Applications 438 (2013), 969--985; cited as reference [7] in Asgarli--Ghioca.

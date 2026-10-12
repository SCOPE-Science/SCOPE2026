# Smooth and singular Jacobian strata of a characteristic-three even-octic family

## Finding
Let \(k\) be algebraically closed of characteristic \(3\). For all \(a,b\in k\), consider the reduced complete curve \(C_{a,b}\) obtained from
\[
y^2=f_{a,b}(t),\qquad f_{a,b}(t)=t^8+b^3t^6+a^3t^2+1,
\]
by adjoining the two points over \(t=\infty\), in the usual even-degree hyperelliptic completion. Its geometric type and its connected generalized Jacobian admit the following exhaustive classification.

**Smooth stratum.** If \(ab\ne1\), then \(C_{a,b}\) is smooth of genus \(3\); its Jacobian has geometric \(3\)-rank \(2\) and \(a\)-number \(1\). The natural involution quotient
\[
E_{a,b}: z^2=v^4+b^3v^3+a^3v+1
\]
is a supersingular elliptic curve, and the second quotient
\[
D_{a,b}:w^2=v^5+b^3v^4+a^3v^2+v
\]
is a genus-two ordinary curve. The quotient-induced homomorphism \(\operatorname{Jac}(E_{a,b})\times\operatorname{Jac}(D_{a,b})\to\operatorname{Jac}(C_{a,b})\) is an isogeny of degree prime to \(3\).

**Cuspidal boundary.** If \(ab=1\) and \(a^4\ne1\), then \(C_{a,b}\) is integral with exactly two ordinary cusps and no other singularities. Its normalization is the elliptic curve
\[
\widetilde C_{a,b}:w^2=(t^2+a)(t^2+b^3),\qquad w=y/(t^2+a).
\]
There is an exact sequence of connected algebraic groups
\[
0\longrightarrow\mathbf G_a^2\longrightarrow\operatorname{Pic}^0(C_{a,b})\longrightarrow\operatorname{Jac}(\widetilde C_{a,b})\longrightarrow0.
\]
The normalization is supersingular exactly when \(a^4=-1\); it is otherwise ordinary. There are exactly four such supersingular parameters \(a\) on the boundary hyperbola, each with \(b=a^{-1}\).

**Reducible boundary.** If \(ab=1\) and \(a^4=1\), the reduced curve is the union of two rational components meeting in two ordinary tacnodes of intersection multiplicity \(2\), and
\[
\operatorname{Pic}^0(C_{a,b})\simeq\mathbf G_m\times\mathbf G_a^2.
\]
There are precisely four reducible boundary parameters. The two sets of four exceptional parameters are disjoint.

## Assumptions and scope
The base field is **algebraically closed of characteristic exactly \(3\)**, with arbitrary algebraic parameters \(a,b\), not just finite-field values. A reduced curve is intended throughout; scheme-theoretic nonreduced fibers and total-family relative Picard smoothness are not claimed. The projective completion is the two-chart hyperelliptic completion: near infinity set \(s=1/t\) and \(Z=y/t^4\), giving \(Z^2=1+b^3s^2+a^3s^6+s^8\). Its two points at \(s=0\) are smooth for every parameter. The \(3\)-rank of a smooth curve means the \(\mathbf F_3\)-dimension of the geometric étale \(3\)-torsion of its Jacobian; the \(a\)-number is the dimension of the kernel of Cartier on regular differentials. The generalized Jacobian is the identity component of the Picard scheme of a reduced, projective curve.

The even-coefficient restriction is the fixed locus of the extra symmetry \(t\mapsto-t\) of the auxiliary branch polynomial; it is therefore geometrically motivated by the elliptic/genus-two involution quotient, not an arbitrary coefficient slice. The motivation is the even-coefficient subfamily \(a_5=a_7=0\) of the degree-ten auxiliary polynomial \(t^{10}+a_8^3t^8+a_4^3t^4+t^2\) in Katsura's 2026 analysis: after dividing the equation by \(t^2\) birationally, put \(a=a_4\), \(b=a_8\). The singularity classification below concerns these associated degree-eight curves, including boundary parameters; no assertion is made that the associated quasi-elliptic surface retains ten fibers of type \(IV\) on every boundary stratum.

## Proof
**1. Squarefreeness and all singular points.** In characteristic \(3\), direct differentiation gives
\[
f'_{a,b}(t)=-t(t^2+a)^3.
\]
Since \(f_{a,b}(0)=1\), any finite multiple root must satisfy \(t^2=-a\), at which \(f_{a,b}(t)=(1-ab)^3\). Therefore \(f_{a,b}\) is squarefree exactly when \(ab\ne1\). The infinite charts above are uniformly smooth. A squarefree monic polynomial of degree \(8\) gives a smooth connected genus-three hyperelliptic curve.

**2. Exact smooth \(3\)-rank and \(a\)-number.** For a squarefree hyperelliptic equation \(y^2=f(t)\) in characteristic \(3\), the Hasse–Witt matrix in the standard genus-three basis has entries the coefficients of \(t^{3i-j}\) in \(f^{(3-1)/2}=f\), for \(1\le i,j\le3\). Here it equals
\[
H=\begin{pmatrix}a^3&0&1\\0&0&0\\1&0&b^3\end{pmatrix}.
\]
The outer two-by-two block is invertible exactly when \((ab)^3-1\ne0\), equivalently \(ab\ne1\), and the remaining coordinate is killed. Because this stable two-dimensional block is bijective under semilinear Frobenius, the stable Frobenius rank is \(2\). Cartier has rank \(2\), so its kernel dimension is \(3-2=1\). This proves both asserted invariants for every smooth parameter, not merely for generic parameters.

**3. Bielliptic decomposition.** The two nonhyperelliptic involutions \((t,y)\mapsto(-t,y)\) and \((t,y)\mapsto(-t,-y)\) give quotient equations \(E_{a,b}\) and \(D_{a,b}\) by taking \(v=t^2\) and respectively \(z=y\), \(w=ty\). Both are smooth when \(ab\ne1\). Their genera are \(1\) and \(2\). For the quartic defining \(E_{a,b}\), the coefficient of \(v^2\) is zero; the genus-one Hasse invariant in characteristic \(3\) therefore vanishes, so \(E_{a,b}\) is supersingular. The genus-two quotient has Hasse matrix
\[
\begin{pmatrix}a^3&1\\1&b^3\end{pmatrix},
\]
whose determinant is nonzero on the smooth stratum, so it is ordinary. Pullback and norm for the commuting order-two involutions decompose the rational \(3\)-adic Tate module: the two quotient eigenspaces have dimensions \(2\) and \(4\), their sum is the full six-dimensional module, and the corresponding idempotents have denominator a power of \(2\). Thus the induced product-Jacobian isogeny has \(2\)-power degree, prime to \(3\). This independently explains the mixed ordinary/supersingular factors.

**4. Cusps on the boundary.** Under \(ab=1\), elementary expansion in characteristic \(3\) yields
\[
f_{a,b}(t)=(t^2+a)^3(t^2+b^3).
\]
If \(a^4\ne1\), then \(a\ne b^3\); the two quadratic factors have distinct roots. At each of the two roots of \(t^2+a\) the polynomial has precisely a triple root and the complete local equation is the ordinary cusp \(Y^2=X^3\) after multiplying by a local unit and choosing a uniformizer. These are the only singularities. Dividing by the square factor gives the stated smooth quartic normalization. In the normalization's local parameter \(w\), the cusp local subring is \(k[[w^2,w^3]]\subset k[[w]]\), so each cusp has \(\delta=1\) and its local-unit contribution to the connected generalized Jacobian is one \(\mathbf G_a\). There are two independent cusp contributions and no torus contribution because the normalization is connected; the Rosenlicht–Serre normalization sequence yields the displayed exact sequence. The quartic equals
\[
t^4+(a+b^3)t^2+ab^3.
\]
Its characteristic-three Hasse invariant is its \(t^2\)-coefficient, \(a+b^3=(a^4+1)/a^3\) under \(b=a^{-1}\). Hence the normalization is supersingular exactly when \(a^4=-1\). The polynomial \(a^4+1\) has four distinct roots in \(k\), none of which satisfies \(a^4=1\), since \(1\ne-1\) in characteristic \(3\).

**5. Two-component tacnodal boundary.** Under \(ab=1\) and \(a^4=1\), one has \(b^3=a\), so
\[
f_{a,b}(t)=(t^2+a)^4,
\quad C_{a,b}=(y-(t^2+a)^2)(y+(t^2+a)^2)=0.
\]
Each component is a smooth rational graph whose projective normalization is \(\mathbf P^1\). At either of the two roots of \(t^2+a\), the components have the same tangent and intersection multiplicity \(2\); the completed local equation is a transverse pair of smooth branches with contact order two, an ordinary tacnode. At infinity the two components meet distinct points because their asymptotic ratios \(y/t^4\) are \(\pm1\). Gluing two normal components across each length-two intersection supplies local units \((k[\epsilon]/\epsilon^2)^\times\simeq\mathbf G_m\times\mathbf G_a\) for each tacnode. Quotienting the product of these two gluing groups by the one-dimensional relative scalar torus of the two components leaves exactly \(\mathbf G_m\times\mathbf G_a^2\); there are no abelian parts because the normalizations are rational. The polynomial \(a^4-1\) also has four simple roots. This exhausts the boundary and completes the proof.

## Verification
A standalone exact symbolic test, `check.py`, verifies the characteristic-three derivative and factorization identities, the Hasse matrices, the cusp/split parameter equations and the characteristically correct coefficient reductions in a multivariate polynomial ring modulo \(3\). Running it must print `VERIFY_OK`. These algebraic identities are independently reconstructed in the proof; finite samples do not establish the universal geometry. The local normalization/gluing proofs and Hasse–Witt interpretation are mathematical steps, not computationally certified results.

## Relationship to prior work
Katsura, *Mordell–Weil groups of quasi-elliptic surfaces in characteristic 3*, arXiv:2609.23430v1, first public 2026-09-20, §§3–5, establishes the auxiliary degree-ten polynomial and computes stable Frobenius ranks and Mordell–Weil data for his arithmetic-genus-four curves and associated surfaces. His statements do not give the intrinsic genus-three smooth-curve Hasse matrix, normalization p-rank of the two-cusp locus, two-tacnode split locus or connected generalized Jacobians as formulated here. The distinction between the singular arithmetic-genus-four auxiliary model and this separately defined degree-eight normalized model is essential. Ayano's 2025 work studies analytic function reductions of complex bielliptic genus-three curves; its inspected theorems do not calculate characteristic-three Hasse invariants or singular-boundary Picard groups. General Hasse–Witt and Rosenlicht–Serre normalization theory supply techniques but not the specific parameter classification.

## Limitations
The statements hold only over algebraically closed fields of characteristic \(3\). They concern the reduced proper fiber curves; no simultaneous normalization, semiabelian Néron model, integral isogeny kernel, extension-class splitting, Newton polygon beyond the quoted p-ranks, or behavior of the corresponding quasi-elliptic surfaces on boundary parameters is asserted. The exact supersingular isomorphism type and possible isogeny classes of genus-two factors are not classified. Literature coverage is subject to the possibility of implicit specialization of older general formulae, particularly in other work on genus-three bielliptic curves. The quotient-isogeny argument assumes the smooth stratum.

## References
1. T. Katsura, *Mordell–Weil groups of quasi-elliptic surfaces in characteristic 3*, arXiv:2609.23430v1 (2026-09-20), especially §§3–5. https://arxiv.org/html/2609.23430v1
2. T. Ayano, *Reduction of bielliptic hyperelliptic functions of genus 3*, arXiv:2501.03774v1 (2025-01-07). https://arxiv.org/abs/2501.03774
3. Classical Hasse–Witt/Cartier–Manin hyperelliptic matrix formula, as described in Katsura, §§3–4.
4. Classical Rosenlicht–Serre generalized-Jacobian normalization sequence for reduced projective curves, used in its standard form.

# Dynamical-degree trichotomy in a maximal-length quartic Cremona class

## Finding

In a distinguished quartic plane Cremona class with the largest possible ordinary quadratic length, two elementary families of projective-linear postcompositions realize three distinct first dynamical degrees: \(1\), \(2\), and \(4\). The dynamical-degree-one locus even contains quartic birational maps of **every even finite order**.

Specifically, set
\[
\Psi([X:Y:Z])=[Z^2(XZ+Y^2):(XZ+Y^2)^2+YZ^3:Z^4].
\]
For \(a,b\in\mathbb C^*\), write \(D_{a,b}(x,y)=(ax,by)\) and \(S_{a,b}(x,y)=(ay,bx)\) on the affine chart \(Z=1\); each extends to a projective-linear automorphism. Then
\[
\lambda_1(D_{a,b}\circ\Psi)=4,\qquad
\lambda_1(S_{a,b}\circ\Psi)=
\begin{cases}2,&a+b^2\ne0,\\1,&a+b^2=0.\end{cases}
\]
All of these maps have degree \(4\) and ordinary quadratic length \(7\). On \(a=-b^2\), the map \(S_{a,b}\circ\Psi\) has finite order if and only if \(-b^3\) is a root of unity, in which case its exact order is twice the order of that root. Thus every positive integer \(r\) occurs as an example of exact order \(2r\).

## Assumptions and scope

The base field is \(\mathbb C\). Here the first dynamical degree means \(\lambda_1(F)=\lim_{n\to\infty}(\deg F^{\circ n})^{1/n}\), using degree of the reduced projective homogeneous coordinate triple. *Ordinary quadratic length* means the minimum number of standard quadratic transformations \([X:Y:Z]\dashmapsto[YZ:XZ:XY]\) required, with arbitrary projective-linear transformations inserted before, after and between. It differs from de Jonquières length and from the length using nonstandard quadratic maps.

The statement is an exact classification **within** the subgroup of affine monomial postcompositions, consisting of diagonal and antidiagonal linear maps. It is not a classification of every projective-linear postcomposition. Nonzero parameter conditions ensure invertibility.

## Proof

**Step 1: maximal quadratic length.** Theorem 1.3 and equation (3) of Calabri--Giao, arXiv:2610.08416, identify \(\Psi\) as a quartic with ordinary quadratic length \(7\); moreover no quartic of Blanc--Furter length \(2\) has larger ordinary quadratic length. The affine formula is \(\psi(x,y)=(x+y^2,y+(x+y^2)^2)\). Left composition with a projective-linear automorphism preserves ordinary quadratic length exactly, since any factorization can be prefixed or stripped by that automorphism. All the postcomposed maps remain quartic: their homogeneous third component is a nonzero multiple of \(Z^4\), and their degree-four leading terms have no common projective factor.

**Step 2: decomposition and dynamical degree four.** Define the elementary shear \(A(x,y)=(x+y^2,y)\), the swap \(L(x,y)=(y,x)\), and \(B=L\circ A\circ L=(x,y+x^2)\). Direct substitution gives \(\psi=B\circ A\). With \(F=D_{a,b}\circ\psi\) and \((x_0,y_0)=(x,y)\), the iterates satisfy
\[
x_{n}=a(x_{n-1}+y_{n-1}^2),\qquad
y_n=b\bigl(y_{n-1}+(x_{n-1}+y_{n-1}^2)^2\bigr).
\]
For every \(n\ge1\), induction yields \(\deg x_n=2\cdot4^{n-1}\) and \(\deg y_n=4^n\): at each step the squared \(y_{n-1}\) term strictly dominates \(x_{n-1}\), and the resulting square strictly dominates the old \(y_{n-1}\); no leading-term cancellation is possible because \(a,b\ne0\). Consequently \(\deg(F^{\circ n})=4^n\) and \(\lambda_1(F)=4\).

**Step 3: antidiagonal normal form.** For \(G=S_{a,b}\circ\psi\), use \(S_{a,b}=D_{a,b}\circ L\) and \(B=LAL\). An exact conjugation gives
\[
A\circ G\circ A^{-1}=A\circ D_{a,b}\circ A\circ L
=H_{a,b},\qquad H_{a,b}(x,y)=(ay+(a+b^2)x^2,bx).
\]
When \(c=a+b^2\ne0\), this is a degree-two generalized Hénon map. Its first coordinate at step \(n\) has degree \(2^n\), by the strict degree dominance of \(c x^2\) over \(ay\), while the second coordinate has degree \(2^{n-1}\). Thus \(\deg H_{a,b}^{\circ n}=2^n\). Since \(G=A^{-1}\circ H_{a,b}\circ A\), degree submultiplicativity in both directions gives
\[
\tfrac14\,2^n\le\deg(G^{\circ n})\le4\,2^n,
\]
so \(\lambda_1(G)=2\). This argument does not assert the exact finite iterate degrees of \(G\) in this regime.

If instead \(c=0\), the same conjugation gives a linear map \(H_{a,b}(x,y)=(ay,bx)\). Every iterate of \(G\) has degree at most \(4\), because the two shears \(A^{\pm1}\) each have degree \(2\); hence \(\lambda_1(G)=1\). Here \(a=-b^2\) and \(H_{a,b}^{\circ2}=(-b^3)I\). Put \(t=-b^3\). Every even iterate is \(t^k I\); every odd iterate is \(t^k H_{a,b}\), which cannot equal the identity because it interchanges the coordinate axes. Therefore \(G\) has finite order exactly when \(t\) is a root of unity, and its order is \(2\operatorname{ord}(t)\). Any root of unity \(t\) admits \(b\in\mathbb C^*\) with \(-b^3=t\), so all even orders are realized. In particular, \(b=1,a=-1\) gives conjugacy to \((x,y)\mapsto(-y,x)\), of order \(4\). The actual projective iterate degrees are \((4,2,4,1)\): the square of the affine map is \((x,y)\mapsto(-x-2y^2,-y)\), while the cube has degree four, and the fourth is the identity.

## Verification

The accompanying `verify.py` is a standalone Python standard-library exact sparse-polynomial calculation. It verifies the defining shear decomposition, the antidiagonal normal-form identity at five nonzero parameter pairs, degrees \((2,4,8,16)\) of the Hénon iterates in three nondegenerate test cases, degrees \((4,16)\) in three diagonal cases, and the exact four-cycle with projective iterate degrees \((4,2,4,1)\). Run with `python3 verify.py`. The finite tests are separate from the infinite degree inductions above.

## Relationship to prior work

Calabri and Giao, *On plane Cremona maps of degree 4 and length 2* (arXiv:2610.08416, first submitted 6 October 2026), prove the maximal ordinary quadratic length \(7\), list the representative \(\Psi\) in Theorem 1.3, and give quadratic decompositions; the classification and length proofs in their Sections 1 and 7 concern the map as an element of a two-sided projective equivalence class. They do not state this monomial-left-family dynamical degree trichotomy or the even-order realization.

The Friedland--Milnor/Jung--van der Kulk classification of affine polynomial automorphisms, as recalled in Cantat's 2024 discussion, explains why Hénon and elementary/affine maps exhibit different degree-growth regimes. Blanc and Furter treat *de Jonquières length* and its asymptotic dynamical length, which is not the first dynamical degree or the ordinary quadratic length used here. These general ingredients neither identify the new source's maximal-length representative with a parameter locus nor state the resulting complete three-way classification in its affine monomial postcomposition family. The argument combines their frameworks through the explicit conjugacy above.

## Limitations

Novelty is relative to the inspected sources and targeted literature searches, not a proof of nonexistence in all literature. General polynomial-automorphism theory already supplies the Hénon/elementary growth dichotomy, and this result is a specific synthesis rather than a new general classification of polynomial automorphisms. The trichotomy is restricted to invertible complex monomial affine postcompositions of the stated \(\Psi\); it does not address other quartic equivalence classes, all projective automorphisms, real-parameter classification, detailed periodic-orbit dynamics, or algebraic stability beyond degree growth. Independent verification of the mathematical argument has not been performed.

## References

1. A. Calabri and N. T. N. Giao, *On plane Cremona maps of degree 4 and length 2*, arXiv:2610.08416v1 (6 October 2026), especially Theorem 1.3, equation (3), and Section 7. https://arxiv.org/html/2610.08416v1
2. J. Blanc and J.-P. Furter, *Length in the Cremona group*, Annales Henri Lebesgue **2** (2019), 187–257. https://doi.org/10.5802/ahl.18
3. S. Friedland and J. Milnor, *Dynamical properties of plane polynomial automorphisms*, Ergodic Theory and Dynamical Systems **9** (1989), 67–99. https://doi.org/10.1017/S014338570000482X
4. S. Cantat, *Holomorphically conjugate polynomial automorphisms of C2 are polynomially conjugate*, Bulletin of the London Mathematical Society (2024), Introduction §1.1. https://doi.org/10.1112/blms.13164

# Symmetry of the regular strong elementary matrix grading
## Finding
Let \(k\) be a field and \(G\) a finite group. Index the matrix units of \(A=M_{|G|}(k)\) by \(G\times G\), and use the strictly elementary grading
\[
\Gamma_G:\qquad \deg(E_{x,y})=x^{-1}y.
\]
Write
\[
T_G=(k^\times)^G/k^\times.
\]
Let \(\operatorname{Stab}(\Gamma_G)\) be the group of \(k\)-algebra automorphisms that fix every homogeneous component, and let \(\operatorname{Aut}(\Gamma_G)\) be the group of \(k\)-algebra automorphisms that permute the homogeneous components. Then
\[
\operatorname{Stab}(\Gamma_G)\cong T_G\rtimes G,
\qquad
\operatorname{Aut}(\Gamma_G)\cong T_G\rtimes\operatorname{Hol}(G),
\]
where \(\operatorname{Hol}(G)=G\rtimes\operatorname{Aut}(G)\) is realized by the left-affine permutations \(x\mapsto a\alpha(x)\). Hence
\[
W(\Gamma_G):=\operatorname{Aut}(\Gamma_G)/\operatorname{Stab}(\Gamma_G)
\cong\operatorname{Aut}(G).
\]
If \(k=\mathbb F_q\), then
\[
|\operatorname{Stab}(\Gamma_G)|=|G|(q-1)^{|G|-1},
\qquad
|\operatorname{Aut}(\Gamma_G)|=|G|\,|\operatorname{Aut}(G)|(q-1)^{|G|-1}.
\]

## Assumptions and scope
The field is arbitrary; no algebraic closure or characteristic assumption is used. The group \(G\) is finite only so that the full matrix algebra has size \(|G|\). The grading is the representative induced by the injective tuple \((x^{-1})_{x\in G}\). Lundström--Öinert--Orozco--Pinedo prove that a strong strictly elementary \(G\)-grading on a full matrix algebra exists exactly when the matrix size is \(|G|\), and that the corresponding action is equivalent to the regular action. Thus \(\Gamma_G\) is the canonical representative of the newly emphasized extremal case.

The word “Weyl” is used here in the explicit quotient sense above: component-permuting automorphisms modulo componentwise stabilizing automorphisms. This avoids dependence on conventions used for group schemes or fine gradings.

## Proof
The neutral component is
\[
A_e=\bigoplus_{x\in G} kE_{x,x},
\]
the diagonal algebra. Let \(\varphi\in\operatorname{Aut}(\Gamma_G)\). Since \(1\in A_e\) and the grading is a direct sum, the component permutation induced by \(\varphi\) fixes \(e\). Hence \(\varphi(A_e)=A_e\).

The primitive idempotents of \(A_e\) are the \(E_{x,x}\), so there is a unique permutation \(\sigma\in\operatorname{Sym}(G)\) satisfying
\[
\varphi(E_{x,x})=E_{\sigma(x),\sigma(x)}.
\]
For every \(x,y\in G\), the corner \(E_{x,x}AE_{y,y}\) is the one-dimensional space \(kE_{x,y}\). Therefore
\[
\varphi(E_{x,y})=c_{x,y}E_{\sigma(x),\sigma(y)}
\]
for some \(c_{x,y}\in k^\times\). Multiplication of matrix units gives
\[
c_{x,y}c_{y,z}=c_{x,z}.
\]
Fix \(o\in G\) and put \(d_x=c_{x,o}\). Taking \(z=o\) yields
\[
c_{x,y}=d_xd_y^{-1}.
\]
Thus the scalar part of \(\varphi\) is conjugation by the diagonal matrix with diagonal \((d_x)_{x\in G}\), and two such diagonals induce the same conjugation exactly when they differ by a common scalar. This gives the factor \(T_G\).

Now let \(\pi\) be the permutation of degrees induced by \(\varphi\). Since \(E_{x,y}\) has degree \(x^{-1}y\),
\[
\sigma(x)^{-1}\sigma(y)=\pi(x^{-1}y)
\qquad(x,y\in G).
\]
Put \(a=\sigma(e)\). Taking \(x=e\) gives \(\sigma(y)=a\pi(y)\). Substituting \(y=xg\) gives
\[
\pi(xg)=\pi(x)\pi(g).
\]
Hence \(\pi\) is a group automorphism, say \(\alpha\), and
\[
\sigma(x)=a\alpha(x).
\]
Conversely every left-affine permutation of this form, together with any diagonal conjugation, gives a matrix-algebra automorphism sending \(A_g\) onto \(A_{\alpha(g)}\). Therefore the coordinate-permutation factor is exactly \(\operatorname{Hol}(G)\), proving
\[
\operatorname{Aut}(\Gamma_G)\cong T_G\rtimes\operatorname{Hol}(G).
\]
An automorphism fixes every component exactly when \(\alpha=\operatorname{id}_G\), in which case \(\sigma(x)=ax\). Thus
\[
\operatorname{Stab}(\Gamma_G)\cong T_G\rtimes G,
\]
and quotienting gives \(W(\Gamma_G)\cong\operatorname{Aut}(G)\).

For \(k=\mathbb F_q\), the diagonal-conjugation factor has size \((q-1)^{|G|-1}\), which gives the stated orders.

## Verification
The proof uses only matrix-unit multiplication, primitive idempotents in a split diagonal algebra, and the defining degree equation. No finite experiment is used to infer the arbitrary-group theorem.

The accompanying checker enumerates all coordinate permutations for \(C_2\), \(C_3\), \(C_4\), \(C_2\times C_2\), and \(S_3\). For each group it independently tests whether a permutation sends every degree class to a degree class, reconstructs the induced degree permutation, verifies that it is a group automorphism, and verifies the affine formula \(\sigma(x)=\sigma(e)\alpha(x)\). It obtains respectively \(2,6,8,24,36\) weak coordinate symmetries and \(2,3,4,4,6\) componentwise coordinate stabilizers, exactly \(|G|\,|\operatorname{Aut}(G)|\) and \(|G|\). It also checks representative finite-field order formulas and ends with `CHECK_OK`.

## Relationship to prior work
Lundström, Öinert, Orozco, and Pinedo show that strictly elementary gradings correspond to free transitive partial actions, and that the strong case occurs exactly when \(|G|\) equals the matrix size, where the action is regular (arXiv:2608.27414v1, Corollaries 36 and 39). Their classification up to graded algebra isomorphism does not state the component-permuting self-equivalence group or the Weyl quotient.

Diniz and Bezerra study crossed-product elementary gradings in the course of a central-polynomial problem (arXiv:1607.03942v1). Their Proposition 3.9 identifies the permutation subgroup arising from componentwise graded automorphisms with the grading group in the crossed-product case. This agrees with, and is strictly contained in, the permutation part of the stabilizer computed here; it does not compute the weak component-permuting group or identify the quotient with \(\operatorname{Aut}(G)\).

Gordienko and Schnabel's work on weak equivalence of gradings (arXiv:1704.07170v1) supplies the broader motivation for allowing homogeneous components to be permuted, but its results concern finite realizability via universal groups rather than this exact self-equivalence group.

## Limitations
The theorem concerns only the regular strong strictly elementary full-matrix grading. It does not classify weak automorphism groups for arbitrary partial-action gradings or for gradings with repeated tuple entries. The diagonal factor is stated for \(k\)-algebra automorphisms; semilinear field automorphisms are not included.

The closest older crossed-product paper already determines the componentwise coordinate-permutation subgroup. The genuinely additional part here is the complete component-permuting group, its diagonal extension, and the Weyl quotient. A residual literature risk remains that an older treatment of weak automorphisms of crossed-product matrix gradings states the same holomorph formula under different terminology.

## References
1. P. Lundström, J. Öinert, L. Orozco, H. Pinedo, “Very good gradings on structural matrix rings,” arXiv:2608.27414v1, 2026.
2. D. Diniz, C. F. Bezerra Jr., “Primeness property for graded central polynomials of verbally prime algebras,” arXiv:1607.03942v1; Journal of Pure and Applied Algebra 222 (2018), 3541–3556.
3. A. Gordienko, O. Schnabel, “On weak equivalences of gradings,” arXiv:1704.07170v1, 2017.

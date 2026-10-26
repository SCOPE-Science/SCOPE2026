# Projective-and-fiber classification of all two-local automorphisms of the three-dimensional Heisenberg Lie algebra

## Finding

Let \(k\) be **any field** and let \(H(k)=k^2\oplus kz\) be the three-dimensional Heisenberg Lie algebra with bracket
\[
[(v,t),(w,s)]=(0,\det(v,w)),\qquad v,w\in k^2,\quad t,s\in k.
\]
A map \(T:H(k)\to H(k)\), not assumed linear or surjective, is a *two-local automorphism* if for every ordered pair \(x,y\in H(k)\) there exists a Lie-algebra automorphism \(g_{x,y}\) with \(g_{x,y}(x)=T(x)\) and \(g_{x,y}(y)=T(y)\).

**Classification.** Such a map \(T\) is exactly a map of the following form:
\[
T(0,t)=(0,ct),\qquad T(v,t)=(F(v),h_v(t))\quad(v\ne0),
\]
where the data obey all of these conditions:

1. \(c\in k^\times\).
2. \(F:k^2\setminus\{0\}\to k^2\setminus\{0\}\) is homogeneous: \(F(\lambda v)=\lambda F(v)\) for \(\lambda\in k^\times\). Its induced map on the projective line \(\mathbb P^1(k)\) is injective (equivalently, independent pairs are sent to independent pairs).
3. Each \(h_v:k\to k\) is injective, and \(h_{\lambda v}(\lambda t)=\lambda h_v(t)\) for every \(\lambda\in k^\times\), \(v\ne0\), and \(t\in k\).

There are **no further restrictions**. Thus arbitrary projective injections and arbitrary injective central-fiber maps, subject only to the displayed homogeneity, occur.

For \(k=\mathbb F_q\), the projective injection is a permutation of the \(q+1\) directions and each fiber injection is a permutation. Consequently the exact number of all (possibly nonlinear) two-local automorphisms is
\[
\boxed{\mathsf L_2(q)=(q-1)^{q+2}(q+1)!\,(q!)^{q+1}.}
\]
They are automatically bijections and form a finite group under composition, while the ordinary automorphism group has order \(q^2(q^2-1)(q^2-q)\). The exact index of the ordinary automorphism group is
\[
\boxed{\frac{\mathsf L_2(q)}{|\operatorname{Aut}(H(\mathbb F_q))|}
=\frac{(q-1)^q(q!)^{q+2}}{q^3}.}
\]
For \(q=2\), these numbers are \(48\) versus \(24\); for \(q=3\), they are \(995328\) versus \(432\); for \(q=4\), they are \(696570347520\) versus \(2880\).

## Assumptions and scope

The field is arbitrary in the classification theorem, including fields of characteristic two and infinite fields. The cardinality formula uses only the assumption that \(k\) is finite with \(q\ge2\) elements. A two-local map is not assumed additive, linear, continuous, or globally invertible. Finite-field bijectivity follows from the characterization; over an infinite field the theorem permits injective maps that are not surjective.

Each projective point is a one-dimensional \(k\)-subspace of \(k^2\). Choosing one nonzero representative for each such point fixes an unambiguous parametrization of the freely chosen projective and fiber data. Different choices of representatives reparametrize, but do not change, the set of maps.

## Proof

**Automorphism normal form.** The derived algebra and the center of \(H(k)\) both equal \(kz\). Hence any automorphism induces a matrix \(A\in\operatorname{GL}_2(k)\) on \(H(k)/kz\). Bracket preservation forces its action on \(z\) to be multiplication by \(\det A\). Its remaining central component is an arbitrary linear functional \(\ell\in(k^2)^*\). Conversely, every
\[
g_{A,\ell}(v,t)=(Av,\det(A)t+\ell(v))
\]
with \(A\) invertible and \(\ell\) linear is an automorphism. This holds without a restriction on the characteristic.

**Necessity.** Fix a two-local map \(T\). Comparing the pair \((x,\lambda x)\) with an automorphism shows that \(T(\lambda x)=\lambda T(x)\) for every scalar \(\lambda\); in particular \(T(0)=0\). Applying this to \(z\) gives \(T(0,t)=(0,ct)\) for a common \(c\ne0\), because every automorphism preserves \(kz\) and takes \(z\) to a nonzero multiple of itself.

Fix \(v\ne0\) and two scalars \(t,s\). A single witnessing automorphism for \((v,t)\) and \((v,s)\) sends both to elements with the same projected vector \(Av\). Therefore the projected part of \(T(v,t)\) is independent of \(t\), and defines \(F(v)\ne0\). Scalar homogeneity of \(T\) gives \(F(\lambda v)=\lambda F(v)\). If \(v,w\) are linearly independent, a witnessing automorphism sends them to \(Av,Aw\), also independent. Thus the induced projective map is injective.

Write \(T(v,t)=(F(v),h_v(t))\). A witnessing automorphism for \((v,t)\) and \((v,s)\), with \(t\ne s\), has nonzero determinant and gives \(h_v(t)-h_v(s)=\det(A)(t-s)\ne0\). Thus each \(h_v\) is injective. Homogeneity of \(T\) yields \(h_{\lambda v}(\lambda t)=\lambda h_v(t)\), as required.

**Sufficiency.** Suppose the stated data are given and fix any two arguments \((v,t)\) and \((w,s)\). We construct a witnessing \(g_{A,\ell}\).

If \(v,w\ne0\) are independent, then \(F(v),F(w)\) are independent. There is a unique \(A\in\operatorname{GL}_2(k)\) satisfying \(Av=F(v)\), \(Aw=F(w)\). Put \(\delta=\det A\); the two equations
\[
\ell(v)=h_v(t)-\delta t,\qquad \ell(w)=h_w(s)-\delta s
\]
uniquely define a linear functional \(\ell\). The resulting \(g_{A,\ell}\) matches both outputs.

If \(v,w\ne0\) are dependent, write \(w=\lambda v\), \(\lambda\ne0\), and define
\[
r=s-\lambda t,\qquad r'=h_w(s)-\lambda h_v(t).
\]
By homogeneity, \(r'=\lambda(h_v(s/\lambda)-h_v(t))\), so injectivity of \(h_v\) gives \(r'=0\) **if and only if** \(r=0\). If \(r\ne0\), choose \(\delta=r'/r\in k^\times\); if \(r=0\), choose any \(\delta\in k^\times\). Because \(F(v)\ne0\), there exists \(A\in\operatorname{GL}_2(k)\) with \(Av=F(v)\) and \(\det A=\delta\): extend \(v\) to a basis and choose the image of its complement with the required determinant. Choose any linear \(\ell\) satisfying \(\ell(v)=h_v(t)-\delta t\). Then the formula for \(g_{A,\ell}\) matches both outputs, since \(r'=\delta r\).

If exactly one projected vector is zero, say \(v=0\) and \(w\ne0\), prescribe \(\det A=c\) and \(Aw=F(w)\), which can be achieved simultaneously by extending \(w\) to a basis; choose \(\ell(w)=h_w(s)-cs\). This maps the central argument and the noncentral argument correctly. If both projected vectors vanish, any \(A\) of determinant \(c\) and \(\ell=0\) works. Every pair has a witnessing automorphism, finishing the equivalence.

**Finite-field count.** There are \(q+1\) projective directions. Their injective self-map is a permutation, giving \((q+1)!\) choices. Fix representatives \(v_i\) of source directions and \(u_j\) of target directions. Once the projective permutation is specified, \(F(v_i)\) can be any of the \(q-1\) nonzero multiples of the target representative, independently for each \(i\). Homogeneity determines all other values of \(F\). Each freely chosen map \(h_{v_i}\) is a permutation of the \(q\)-element field, giving \(q!\) independent possibilities, and the compatibility identity then uniquely determines the other maps in the same direction. Finally \(c\) has \(q-1\) choices. All parameters are uniquely recoverable from \(T\). Multiplication yields \(\mathsf L_2(q)\).

Every two-local map on a finite set is injective (apply the witnessing automorphism to two distinct inputs), hence bijective. Composing two two-local maps and composing their pairwise witnesses proves closure; for a finite bijective two-local map, taking inverse witnesses on preimage pairs proves that the inverse is also two-local. The automorphism-group order follows from the normal form: \(q^2|\operatorname{GL}_2(\mathbb F_q)|=q^2(q^2-1)(q^2-q)\). Simplification gives the stated index. The quotient is greater than one for every \(q\ge2\), as already witnessed at \(q=2\) and monotonically strengthened by the factorial factors.

## Verification

The standalone file `check_2local.py` reproduces independent pair-orbit checks without using the preceding classification as its two-locality test. It constructs all ordinary automorphisms from the explicit \((A,\ell)\) normal form, partitions ordered pairs into actual automorphism orbits, and tests maps against this necessary-and-sufficient orbit condition.

Over \(\mathbb F_2\), all \(8!=40320\) bijections of the underlying eight-element set were tested. Exactly \(48\) preserve every pair orbit; this is exactly the set of \(48\) maps generated by the theorem's independent parametrization. There are \(24\) ordinary automorphisms and \(11\) ordered-pair orbits.

Over \(\mathbb F_3\), \(120\) seeded pseudorandom classification maps satisfy every one of the \(729\) ordered-pair tests using \(432\) independently enumerated ordinary automorphisms and \(14\) pair orbits. Over \(\mathbb F_4\), \(100\) seeded pseudorandom classification maps satisfy all \(4096\) ordered-pair tests, using \(2880\) ordinary automorphisms and \(17\) pair orbits. The exact finite-field count is a consequence of the proof, **not** of the random tests. The checker prints `HEISENBERG_TWO_LOCAL_OK` when every test passes.

## Relationship to prior work

Ayupov and Kudaybergenov (arXiv:1602.05187v1, first submitted 16 February 2016), Section 3 and Theorems 3.1–3.2, establish existence of nonlinear two-local automorphisms on nilpotent Lie algebras by central perturbations. Their construction is a proper subfamily of the free projective/fiber choices here; it gives neither the converse classification nor the finite-field total. Their Section 2 treats semisimple Lie algebras, not this nilpotent case.

Sheng, Liu and Miao, *Local and Linear 2-local Automorphisms of Heisenberg Lie (Super)algebras* (DOI:10.1007/s11464-023-0061-6), concerns **local and linear two-local** maps according to its accessible title and abstract. The exact nonlinearly parametrized finite-field total is not asserted in those accessible statements. Its full text was not accessible for a complete exclusion of possible overlapping remarks.

The full-text 2024 study of model-filiform Lie superalgebras by Sheng, Liu and Liu (DOI:10.1155/2024/6650997) likewise distinguishes **linear** two-local automorphisms. The model-filiform and Lie-superalgebra results do not imply the specific arbitrary nonlinear Heisenberg classification and finite-field formula. Related work classifying ordinary Heisenberg automorphisms supplies the \((A,\ell)\) input, not the binary-witness classification.

## Limitations

The closed counting expression is for the three-dimensional Heisenberg Lie algebra, not its higher-dimensional counterparts. The arbitrary-field characterization permits nonsurjective maps for infinite fields; only finite-field maps are automatically bijective. Although the exact mathematical deductions are self-contained, originality remains subject to literature-priority uncertainty, particularly because the complete 2024/2025 Heisenberg local-automorphism comparison text was inaccessible. Finite computations do not certify the all-field theorem; that is proved by the case analysis above. There has been no independent mathematical audit.

## References

1. Shavkat Ayupov and Karimbergen Kudaybergenov, *2-Local automorphisms on finite-dimensional Lie algebras*, arXiv:1602.05187v1 (16 February 2016), especially Section 3. https://arxiv.org/pdf/1602.05187
2. Yuqiu Sheng, Wende Liu and Xingxue Miao, *Local and Linear 2-local Automorphisms of Heisenberg Lie (Super)algebras*, *Frontiers of Mathematics*, DOI:10.1007/s11464-023-0061-6. https://link.springer.com/article/10.1007/s11464-023-0061-6
3. Yuqiu Sheng, Wende Liu and Yang Liu, *Local Automorphisms and Local Superderivations of Model Filiform Lie Superalgebras*, *Journal of Mathematics* (2024), DOI:10.1155/2024/6650997. https://onlinelibrary.wiley.com/doi/10.1155/2024/6650997

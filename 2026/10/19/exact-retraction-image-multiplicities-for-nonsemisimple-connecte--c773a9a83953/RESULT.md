# Exact retraction-image multiplicities for nonsemisimple connected Alexander quandles

## Finding
Let \(p\) be prime, \(V\) a nonzero finite-dimensional vector space over \(\mathbb F_p\), and \(T\in\operatorname{GL}(V)\) with \(I-T\) invertible. On \(V\) put \(x\triangleright y=Tx+(I-T)y\). For any prescribed elementary-divisor data of \(T\), including arbitrary nonsemisimple primary powers, the theorem below gives the exact number of idempotent quandle endomorphisms (retractions), classified simultaneously by the isomorphism type and cardinality of their images, together with the multiplicity of retractions onto each specified image.

Write the corresponding \(\mathbb F_p[t]\)-module as
\[
V\cong\bigoplus_{\phi}\bigoplus_{e\ge1}
\bigl(\mathbb F_p[t]/(\phi^e)\bigr)^{m_{\phi,e}},
\]
where \(\phi\) runs over distinct monic irreducible polynomials, excluding \(t\) and \(t-1\). Put \(q_\phi=p^{\deg\phi}\), \(m=(m_{\phi,e})\), and for any finite multiplicity array \(s\) set
\[
\mathcal A(s)=\prod_\phi q_\phi^{\sum_{j\ge1}(\sum_{e\ge j}s_{\phi,e})^2}
\prod_{e\ge1}\prod_{i=1}^{s_{\phi,e}}(1-q_\phi^{-i}).
\]
Empty products equal one. These rational-looking products are positive integers: automorphism-group orders. For an array \(r\) with \(0\le r_{\phi,e}\le m_{\phi,e}\), write \(w=m-r\) and
\[
 u(r)=\sum_{\phi,e}(\deg\phi)e r_{\phi,e},\quad
 v(w)=\sum_{\phi,e}(\deg\phi)e w_{\phi,e},\quad
 h(r,w)=\prod_\phi q_\phi^{\sum_{e,j}r_{\phi,e}w_{\phi,j}\min(e,j)}.
\]
The number of retractions whose images, after translation, have elementary-divisor array \(r\) is exactly
\[
\boxed{N(r)=p^{v(w)}\frac{\mathcal A(m)}{\mathcal A(r)\mathcal A(w)}.}
\]
Each image has \(p^{u(r)}\) points. There are exactly \(\boxed{N(r)/h(r,w)}\) distinct retract image cosets of type \(r\); each specified image admits exactly \(\boxed{h(r,w)}\) retractions onto it. Thus the complete rank/cardinality enumerator is
\[
\boxed{\mathcal R_T(z)=\sum_{0\le r\le m}N(r)z^{p^{u(r)}}.}
\]
Different arrays yielding equal cardinalities contribute additively. Every image is a coset of a \(T\)-invariant direct summand, and every such coset occurs.

In particular, the quandle has precisely \(\boxed{|V|+1}\) retractions if and only if the \(\mathbb F_p[t]\)-module \(V\) is indecomposable. In that case the only retractions are its \(|V|\) constants and the identity. This gives a sharp no-proper-nontrivial-retract criterion across the nonsemisimple class.

## Assumptions and scope
The vector-space dimension is at least one. We count distinct set maps preserving the displayed quandle operation and satisfying \(f\circ f=f\). Neither embeddings up to isomorphism nor retractions modulo automorphisms are identified. We work over the prime field, not over an arbitrarily specified extension field: an additive quandle endomorphism is \(\mathbb F_p\)-linear but need not be linear over a larger presentation field. The exclusion \(\phi=t\) makes \(T\) invertible, and \(\phi=t-1\) makes \(I-T\) invertible. The main quantitative contribution is for arrays having at least one exponent \(e\ge2\), i.e. nonsemisimple \(T\); the formula has the known semisimple boundary as a consistency check.

## Proof
**All quandle self-maps are affine.** Let \(R_y(x)=Tx+(I-T)y\). Every \(R_y\) is invertible. Since \(R_yR_z^{-1}\) is translation by \((I-T)(y-z)\) and \(I-T\) is surjective, every additive translation \(\tau_v\) belongs to the displacement group. If \(f\) is a quandle homomorphism, then \(fR_y=R_{f(y)}f\), and the same holds with inverses because both \(R_y\) and \(R_{f(y)}\) are bijective. Therefore \(f\tau_v=\tau_{L(v)}f\) for some value \(L(v)\), independent of the argument to which the translation is applied. Putting the argument equal to zero yields \(L(v)=f(v)-f(0)\). Varying \(v\) shows \(L\) is additive, hence \(\mathbb F_p\)-linear. Putting the second quandle argument equal to zero gives \(LT=TL\). Conversely, every \(f(x)=a+Lx\) with \(LT=TL\) preserves the operation.

**Idempotents and ordered splittings.** The equation \(f^2=f\) is equivalent to \(L^2=L\) and \(La=0\). For such a \(T\)-linear projection, \(V=U\oplus W\) is an ordered direct sum of \(T\)-stable modules, with \(U=\operatorname{im}L\), \(W=\ker L\). Conversely, every ordered stable splitting gives exactly one projection. Its affine translations \(a\in W\) are distinct, and their images are the affine cosets \(a+U\). Thus each projection of type \(r\) supplies \(|W|=p^{v(w)}\) retractions.

**Counting ordered stable splittings.** The primary decomposition and invariant-factor theorem imply that in an ordered splitting the multiplicity of \(\phi^e\) in \(U\) may be any \(r_{\phi,e}\) between zero and \(m_{\phi,e}\), and that in \(W\) it is \(w_{\phi,e}=m_{\phi,e}-r_{\phi,e}\). The \(\mathbb F_p[t]\)-automorphism group of \(V\) acts transitively on all ordered splittings of those types; the stabilizer is \(\operatorname{Aut}(U)\times\operatorname{Aut}(W)\). Hence their number is the quotient of the three automorphism-group orders.

For a fixed irreducible \(\phi\), write \(Q=p^{\deg\phi}\) and \(s_e\) for the primary block multiplicities. The number of module endomorphisms is
\[
Q^{\sum_{e,j}s_es_j\min(e,j)}
=Q^{\sum_{k\ge1}(\sum_{e\ge k}s_e)^2}.
\]
Indeed the homomorphism space from a cyclic block of length \(e\) to one of length \(j\) has \(Q^{\min(e,j)}\) elements. Reduction on the diagonal equal-length block sectors maps the endomorphism ring onto \(\prod_e M_{s_e}(\mathbb F_Q)\) with nilpotent kernel (the Jacobson radical). An endomorphism is invertible exactly when every diagonal reduction is invertible. Multiplying the resulting unit fractions \(\prod_{e,i}(1-Q^{-i})\) by the endomorphism count proves the displayed formula for \(\mathcal A\). Distinct irreducible primary sectors contribute independently. The orbit-stabilizer formula and the previous affine-translation count now prove \(N(r)\).

**Counting a specified image.** Fix one direct summand \(U\) of type \(r\), choose an arbitrary complement \(W_0\), and fix one coset \(c+U\). All other stable complements of \(U\) are graphs of unique \(\mathbb F_p[t]\)-homomorphisms \(W_0\to U\); there are \(|\operatorname{Hom}(W_0,U)|=h(r,w)\) such graphs, because homomorphisms between distinct primary sectors vanish, and a \(\phi^e\)-to-\(\phi^j\) homomorphism space has size \(q_\phi^{\min(e,j)}\). For each complement there is exactly one translation representative in that complement defining a projection onto \(c+U\). Thus the per-image multiplicity is \(h(r,w)\); division gives the image count. Finally, the only stable idempotents are zero and identity exactly when the module admits no proper nontrivial direct-sum decomposition. In that case there are \(|V|\) constant maps and the identity; in the decomposable case an additional nontrivial projection exists.

## Verification
The standalone `check.py` checks the formulas by independent enumeration of all commuting idempotent matrices for nine small prime-field primary decompositions, including a length-two Jordan block, mixed lengths two and one, irreducible quadratic blocks in characteristic two, a repeated irreducible quadratic, and a genuine square of that irreducible. It independently groups retractions by their exact set-theoretic images in three examples, confirming the per-specified-image multiplicities, and exhaustively checks the quandle-operation-preserving condition for all maps on two very small underlying sets. Exact outputs include:

* For \(p=3\) and \(T\) a single length-two Jordan block with eigenvalue two, the image-dimension profile is \(\{0:9,2:1\}\), i.e. ten retractions; for the scalar matrix with the same eigenvalue and same dimension it is \(\{0:9,1:36,2:1\}\), i.e. forty-six.
* For \(p=3\) and primary Jordan block lengths two and one, the image-dimension counts are \(\{0:27,1:81,2:27,3:1\}\).
* Over \(\mathbb F_2\), two copies of an irreducible quadratic block give \(\{0:16,2:80,4:1\}\), while a single length-two block for the same quadratic has only \(\{0:16,4:1\}\).

Run `python3 check.py` from the directory containing the file. The checker relies only on Python's standard library. These finite tests supplement, but do not replace, the general proof above.

## Relationship to prior work
Jedlička, Pilitowska, Stanovský, and Zamojska-Dzienio study quasi-affine quandles, their subquandles and affine realizations [1]. The structural relationship between Alexander-quandle retractions and split module epimorphisms is explicit in Niebrzydowski–Przytycki [2, Lemma 33 and Corollary 34]; it is prior knowledge, not part of the originality claim. Jedlička–Stanovský study homomorphic images rather than their exact retract-fiber multiplicities [3]. Taniguchi proves results about good involutions and connected Alexander-quandle automorphisms [4], not noninvertible retraction counts. Exact idempotent endomorphism formulas for **semisimple** Alexander operators are prior coverage; that case is intentionally excluded from the claimed contribution. The new claim is the **general arbitrary-primary-power, nonsemisimple quantitative profile** with per-specified-image multiplicities and an exact indecomposable retraction-rigidity boundary.

## Limitations
The theorem assumes finite dimension over the prime field and \(I-T\) invertible; disconnected affine quandles and nonadditive coefficient groups are not covered. The method is structural counting, not a classification of quandles modulo all isomorphisms, nor a result about homology or knot invariants. Counts for semisimple operators are included only to express and check the uniform formula, and no priority is claimed for the underlying module splitting or general finite-module automorphism-order identities. An equivalent exact multiplicity formula in older module or quandle literature remains an originality risk. Independent mathematical validation has not been performed.

## References
[1] P. Jedlička, A. Pilitowska, D. Stanovský, A. Zamojska-Dzienio, *Subquandles of affine quandles*, arXiv:1708.02362v1 (first public 2017-08-08), https://arxiv.org/abs/1708.02362.

[2] M. Niebrzydowski and J. H. Przytycki, *Homology operations on homology of quandles*, arXiv:0907.4732, §5, Lemma 33 and Corollary 34, https://arxiv.org/pdf/0907.4732.

[3] P. Jedlička and D. Stanovský, *Homomorphic images of affine quandles* (2021), https://jedlicka.tf.czu.cz/publications/a/JS2021.pdf.

[4] Y. Taniguchi, *Good involutions of generalized Alexander quandles*, arXiv:2302.11138v1 (2023), https://arxiv.org/html/2302.11138v1.

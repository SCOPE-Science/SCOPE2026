# Joint rank spectra of commuting retractions of free two-step associative algebras

## Finding
Let \(K\) be any field, \(n\ge1\), and \(k\ge2\). Put \(V=K^n\) and let \(N(V)=V\oplus(V\otimes_K V)\) be the **nonunital** free associative algebra with all products of three elements zero, with \((v,w)(v',w')=(0,v\otimes v')\). Every ordered family of \(k\) pairwise commuting composition-idempotent \(K\)-algebra endomorphisms of \(N(V)\) is conjugate by an algebra automorphism to a family induced by commuting projections on \(V\). Its conjugacy class is uniquely determined by the \(2^k\) dimensions of the joint zero/one eigenspaces of those projections.

For every finite field \(\mathbb F_q\), this gives an exact enumerator for the ranks of **all nonempty products** of the endomorphisms. Write \(\Omega=\{0,1\}^k\); take any nonnegative integers \(n_\epsilon\) (\(\epsilon\in\Omega\)) summing to \(n\). For \(\eta\in\Omega\) define
\[
 m_\eta=\sum_{\substack{\epsilon,\delta\in\Omega\\\epsilon\wedge\delta=\eta}}n_\epsilon n_\delta,
 \qquad E=\sum_{\eta\in\Omega}n_\eta m_\eta,
\]
where \(\epsilon\wedge\delta\) is coordinatewise Boolean AND. For every nonempty \(I\subseteq\{1,\ldots,k\}\), define
\[
 r_I=\sum_{\substack{\epsilon\in\Omega\\\epsilon_i=1\ \text{for all }i\in I}} n_\epsilon.
\]
Put \(G_d(q)=\lvert\operatorname{GL}_d(\mathbb F_q)\rvert=\prod_{j=0}^{d-1}(q^d-q^j)\), with \(G_0(q)=1\). Then the exact multivariate enumerator is
\[
 \boxed{\mathcal P_{n,k,q}\bigl((T_I)_{\varnothing\ne I\subseteq[k]}\bigr)
 =\sum_{\substack{(n_\epsilon)_{\epsilon\in\Omega}\ge0\\\sum n_\epsilon=n}}
 \frac{G_n(q)}{\prod_{\epsilon\in\Omega}G_{n_\epsilon}(q)}
 q^{n^3-E}\prod_{\varnothing\ne I\subseteq[k]}T_I^{r_I+r_I^2}.}
\]
The coefficient of \(\prod_I T_I^{d_I}\) is exactly the number of ordered pairwise commuting idempotent algebra endomorphism families \((F_1,\ldots,F_k)\) for which every product \(\prod_{i\in I}F_i\) has \(K\)-linear rank \(d_I\). Repeated rank patterns are aggregated by the sum. The formula holds in every characteristic, including two.

For \(n=k=q=2\), using variables \(U=T_{\{1\}}\), \(W=T_{\{2\}}\), and specializing the product-rank variable to one, the joint-rank polynomial is
\[
 1+96(U^2+W^2)+U^6+W^6+480U^2W^2+96(U^2W^6+U^6W^2)+U^6W^6.
\]
There are exactly \(868\) ordered commuting retraction pairs in this six-dimensional algebra, while it has \(98\) individual retractions. Among the \(480\) pairs whose two individual ranks are both \(2\), exactly \(384\) have product rank zero and \(96\) have product rank \(2\); the full multivariate formula distinguishes these two cases despite their identical individual ranks.

## Assumptions and scope
All endomorphisms are \(K\)-linear and algebra-multiplicative, but are not required to be unital; the displayed algebra has no identity. "Idempotent" refers to composition, not to an element of the algebra. The parameter \(n\) is a positive integer and \(k\ge2\). A product of commuting endomorphisms is taken under composition. The finite-field formula counts **labeled, ordered tuples**, not orbits. The structural normal form holds for arbitrary fields, while counts require finite fields.

## Proof
**1. Endomorphisms of the free two-step algebra.** The square \(N(V)^2\) is exactly \(W=V\otimes V\), and \(WN(V)=N(V)W=0\). Every endomorphism preserves \(W\) and induces a linear map \(A:V=N(V)/W\to V\). Choosing the evident vector-space splitting, its entire action is
\[
 F(v+w)=Av+f(v)+(A\otimes A)w,
 \qquad f\in\operatorname{Hom}_K(V,W).
\]
Conversely, every pair \((A,f)\) defines an algebra endomorphism: the image of the product \(vv'\) equals \(Av\otimes Av'\), which is also the product of their images. Thus no possible algebra endomorphism is missing from this description.

**2. Simultaneous conjugacy.** Suppose \(F_1,\ldots,F_k\) are commuting composition-idempotents, inducing commuting idempotents \(A_i\) on \(V\). They also induce commuting idempotents \(B_i=A_i\otimes A_i\) on \(W\). Since \(t(t-1)\) has two distinct roots over every field, any commuting family of idempotent linear maps splits simultaneously into the direct sum of its joint zero/one eigenspaces. This applies to the full space \(N(V)\), to the invariant subspace \(W\), and to the quotient \(V\). Therefore the short exact sequence \(0\to W\to N(V)\to V\to0\) has a linear section \(s:V\to N(V)\) intertwining all \(A_i\) and \(F_i\): take the complement of \(W\) inside each joint eigenspace. Write \(s(v)=v+h(v)\). Then \(H_h(v+w)=v+w+h(v)\) is an algebra automorphism (multiplication uses only the linear parts) and \(F_i=H_h E_iH_h^{-1}\), where \(E_i(v+w)=A_iv+B_iw\). In particular, all common non-graded lift parameters are exhausted by one shared shear \(h\), rather than independently chosen lift maps for each endomorphism.

**3. Orbit labels and ranks.** Let \(V_\epsilon=\{v:A_iv=\epsilon_iv\text{ for all }i\}\). The ordered decomposition \(V=\bigoplus_{\epsilon\in\Omega}V_\epsilon\) has dimensions \(n_\epsilon\). Every such decomposition defines a canonical family, and any two with the same dimensions are conjugate by some \(P\in\operatorname{GL}(V)\), which lifts to the algebra automorphism \(v+w\mapsto Pv+(P\otimes P)w\). Distinct dimension vectors cannot become conjugate because the quotient action preserves the simultaneous eigenspace dimensions. On a tensor block \(V_\epsilon\otimes V_\delta\), each \(B_i\) has eigenvalue \(\epsilon_i\delta_i\). Consequently the joint eigenspace of \(W\) with label \(\eta\) has dimension \(m_\eta\). For nonempty \(I\), the quotient projection of the composed endomorphism has rank \(r_I\) and its induced action on \(W\) has rank \(r_I^2\); common shear conjugation does not alter rank. Thus the rank is exactly \(r_I+r_I^2\).

**4. Exact multiplicities.** Over \(\mathbb F_q\), a fixed dimension vector \((n_\epsilon)\) admits exactly \(G_n(q)/\prod_\epsilon G_{n_\epsilon}(q)\) ordered joint-eigenspace decompositions of \(V\). Fix one, hence its tuple \((A_i)\). All simultaneous lifts are parametrized surjectively by \(h\in\operatorname{Hom}(V,W)\), a space of dimension \(n^3\). Two shears yield the same full tuple precisely when their difference \(h_0\) intertwines all \(A_i\) with \(B_i\): \(h_0A_i=B_ih_0\) for every \(i\). The intertwiners are exactly \(\bigoplus_\epsilon\operatorname{Hom}(V_\epsilon,W_\epsilon)\), of dimension \(E=\sum_\epsilon n_\epsilon m_\epsilon\). Therefore each quotient decomposition has \(q^{n^3-E}\) distinct lifts. Multiply the two factors and record the ranks to obtain the stated polynomial. This exhausts all tuples, without overcounting. The proof uses neither characteristic-zero assumptions nor algebraic closure.

## Verification
`checker.py` is standalone Python 3 (standard library only). Run `python3 checker.py`. It exhaustively generates all algebra endomorphisms for \(n=1,2\) over \(\mathbb F_2\), checks composition idempotency, enumerates all ordered commuting pairs independently of the formula, and compares their full joint-rank counts against the formula. For \(n=2\), it finds \(98\) single retractions and \(868\) ordered commuting pairs. It also checks nonnegativity and integral counts for a range of symbolic finite-field parameters; those arithmetic checks are not exhaustive enumerations. Output `VERIFY_OK` signals agreement in these finite tests. The all-field theorem rests on the proof above, not on the finite tests.

## Relationship to prior work
Facchini and Heidari Zadeh, *Algebras with a bilinear form, and Idempotent endomorphisms* (arXiv:2210.08230), study weak augmentations, split morphisms, and particular unital idempotent endomorphisms; in particular their Theorem 1.2 treats endomorphisms with scalar image, and their categorical Remark 4.1 discusses general splitting. These facts support the viewpoint that an idempotent endomorphism defines a retract; they do not supply the free two-step nonunital algebra's simultaneous finite-field lift multiplicities or its complete joint product-rank distribution. Kanel-Belov, Berzins and Lipyanski (arXiv:math/0512273) study **automorphisms of the endomorphism semigroup** of an untruncated free associative algebra, a different second-order object. Results on individual retractions in commutative truncated or free two-step Lie algebras involve symmetric or alternating degree-two pieces, and neither their rank formulas nor their single-retraction classifications imply the present simultaneous ordered-tensor calculation. Standard splitting of commuting projections is used explicitly as a prerequisite, not represented as novel.

## Limitations
This theorem is restricted to free, nonunital, associative algebras with vanishing products of length three. It does not classify arbitrary quotients of \(V\otimes V\), noncommuting retractions, or general higher truncations. The affine lift formula is not an independent novelty claim about simultaneous diagonalization; it is an exact count for this specific multiplication functor. The bibliography may be incomplete, and an equivalent finite-field enumeration under another terminology cannot be categorically excluded.

## References
1. A. Facchini and L. Heidari Zadeh, *Algebras with a bilinear form, and Idempotent endomorphisms*, arXiv:2210.08230 (first public 2022-10-15), https://arxiv.org/abs/2210.08230, especially Theorem 1.2, Theorem 3.6, Proposition 3.7 and Remark 4.1.
2. A. Kanel-Belov, A. Berzins and R. Lipyanski, *Automorphisms of the semigroup of endomorphisms of free associative algebras*, arXiv:math/0512273 (first public 2005-12-13), https://arxiv.org/abs/math/0512273.
3. V. Drensky and L. Makar-Limanov, *Locally Nilpotent Derivations of Free Algebra of Rank Two*, arXiv:1909.13262 (first public 2019-09-29), https://arxiv.org/abs/1909.13262.

# Natural-basis moduli and automorphism orbit counts for rank-one evolution algebras

## Finding
Let \(K\) be a field of characteristic different from \(2\). Let \(E\) be a two-dimensional **nondegenerate** evolution algebra with \(\dim_K E^2=1\). Choose \(u\in E^2\setminus\{0\}\) and write the product uniquely as \(xy=B(x,y)u\), where \(B\) is a nondegenerate symmetric bilinear form. Let \(\Delta\in K^\times/(K^\times)^2\) be the determinant square class of \(B\), and let \(\delta=B(u,u)\).

**Complete moduli theorem.** The natural bases of \(E\), modulo scaling individual basis vectors by elements of \(K^\times\) and permuting them, are in canonical bijection with unordered pairs \(\{L,L^\perp\}\) of nonisotropic lines in \(\mathbb P(E)\). Their full automorphism group satisfies
\[
\operatorname{Aut}_K(E)\cong\begin{cases}C_2,&\delta\ne0,\\K^\times,&\delta=0.\end{cases}
\]
Over an infinite field, there are infinitely many inequivalent natural bases in **both** cases. In particular, \(e_1^2=e_1\), \(e_2^2=e_1\), and \(e_1e_2=0\) give a nondegenerate two-dimensional example with infinitely many basis classes but only two automorphisms. No one-dimensional algebra has more than one natural-basis class modulo scaling, so this dimension is optimal.

**Exact finite-field census.** Over \(\mathbb F_q\), for any odd prime power \(q\), write \(\chi\) for the quadratic character (on \(\mathbb F_q^\times\)) and \(\chi(\Delta)\) for the character of any representative. The number of natural-basis classes is
\[
N(E)=\frac{q-\chi(-\Delta)}{2}.
\]
The number of these classes up to the additional action of the algebra automorphism group is
\[
O(E)=\begin{cases}1,&\delta=0,\\\displaystyle\frac{q-\chi(-\Delta)+3+\chi(\Delta)}4,&\delta\ne0.\end{cases}
\]
When \(\delta\ne0\), the nonidentity automorphism fixes exactly \(1+(1+\chi(\Delta))/2\) unordered pairs. When \(\delta=0\), the multiplicative automorphism group acts transitively. Thus the classification distinguishes the size of the natural-basis moduli from the effective action of intrinsic algebraic symmetry.

## Assumptions and scope
An evolution algebra is a commutative, not necessarily associative algebra admitting a basis \(e_1,e_2\) with \(e_1e_2=0\). Nondegeneracy means each natural-basis vector has nonzero square, equivalently \(\operatorname{ann}(E)=0\). Dimension of \(E^2\) means linear dimension of the span of all products. Each equivalence class here forgets both the order of the natural basis and separate nonzero scalar multiples of its members. It does **not** initially identify bases by algebra automorphisms; the integer \(O(E)\) performs that additional quotient. The determinant square class is independent of a change of basis, and changing \(u\) only rescales \(B\), leaving its determinant square class and whether \(\delta\) vanishes unchanged. The theorem applies to arbitrary characteristic-not-two fields for its structural statements; the numerical formulas assume finite fields of odd cardinality, not algebraic closedness.

## Proof
1. **Intrinsic form and projective basis moduli.** In a natural basis choose \(u\) spanning \(E^2\), and write \(e_i^2=b_i u\), where \(b_1,b_2\ne0\). Then \(B\) has diagonal matrix \(\operatorname{diag}(b_1,b_2)\), so it is nondegenerate. Two nonzero independent vectors \(v,w\) constitute a natural basis exactly when \(B(v,w)=0\). For a nondegenerate bilinear form on a two-space, the orthogonal complement of a line is another line; it is distinct precisely when the first line is nonisotropic. Thus the equivalence classes of natural bases are the two-element orbits of the fixed-point-free involution \(L\mapsto L^\perp\) on the nonisotropic lines.

2. **Automorphism constraint.** If \(T\) is an algebra automorphism, it preserves \(E^2=Ku\), so \(T(u)=c u\) for some \(c\ne0\). Multiplicativity is equivalent to the simultaneous equations \(B(Tx,Ty)=c B(x,y)\) for all vectors and \(T(u)=cu\). If \(\delta\ne0\), evaluating on \((u,u)\) yields \(c^2\delta=c\delta\), hence \(c=1\). The orthogonal line \((Ku)^\perp\) is nondegenerate and stable, so \(T\) is the identity on \(Ku\) and multiplies its orthogonal complement by a scalar with square \(1\). In characteristic different from \(2\), the only possibilities are \(1\) and \(-1\). Both preserve multiplication, proving the \(C_2\) case. If \(\delta=0\), choose \(v\) with \(B(u,v)=1\) and replace \(v\) by \(v-B(v,v)u/2\) to obtain \(B(v,v)=0\). Every automorphism has \(T(u)=cu\), \(T(v)=a u+b v\). The similitude equation on \((u,v)\) forces \(b=1\), and that on \((v,v)\) forces \(a=0\). Conversely, every \(c\ne0\) gives an automorphism \(u\mapsto cu\), \(v\mapsto v\). Hence \(\operatorname{Aut}_K(E)\cong K^\times\).

3. **Infinite-field and minimality assertions.** The projective line has infinitely many \(K\)-points when \(K\) is infinite, while a binary nondegenerate form has at most two isotropic projective points. Orthogonal complementation pairs the remaining infinitely many points, proving infinitude. For the displayed multiplication with \(u=e_1\), one has \(B=\operatorname{diag}(1,1)\) and \(B(u,u)=1\), hence exactly two automorphisms. Every natural basis of a one-dimensional algebra is equivalent under scaling, proving minimality.

4. **Finite-field count.** Over odd \(\mathbb F_q\), a nonsingular binary quadratic form has precisely \(1+\chi(-\Delta)\) isotropic projective lines: it has \(2\) when \(-\Delta\) is a square, and none otherwise. Consequently exactly \(q-\chi(-\Delta)\) lines are nonisotropic. Orthogonal complementation acts freely on them, so dividing by \(2\) gives \(N(E)\).

5. **Orbit count in the isotropic case.** When \(\delta=0\), use the hyperbolic basis \(u,v\) of Step 2. All nonisotropic lines are \(L_t=K(u+t v)\) for \(t\in K^\times\), with \(L_t^\perp=L_{-t}\). The automorphism parameter \(c\in K^\times\) sends \(L_t\) to \(L_{t/c}\). It therefore acts transitively on the unordered pairs \(\{L_t,L_{-t}\}\), leaving one orbit.

6. **Orbit count in the anisotropic-\(u\) case.** When \(\delta\ne0\), take an orthogonal basis \(u,v\) with \(B(u,u)=a\ne0\) and \(B(v,v)=b\ne0\). The nonidentity automorphism is the reflection \(v\mapsto-v\). It fixes the unordered pair \(\{Ku,Kv\}\). All other fixed pairs must consist of a line swapped with its orthogonal complement. For \(L=K(u+t v)\) this happens if and only if \(B(u+t v,u-t v)=a-bt^2=0\). There is one additional fixed unordered pair precisely when \(a/b\) is a square, equivalently when \(\chi(ab)=\chi(\Delta)=1\). Thus there are \(F=1+(1+\chi(\Delta))/2\) fixed basis classes. Burnside's lemma gives \(O(E)=(N(E)+F)/2\), exactly the displayed formula. The calculation also establishes integrality and the full orbit-size distribution (\(F\) singleton orbits and \((N-F)/2\) two-element orbits).

These arguments are valid for all odd prime powers in the finite census. There is no induction from computed examples.

## Verification
The standalone script `verify.py` enumerates all invertible two-by-two matrices over the prime fields \(\mathbb F_3,\mathbb F_5,\mathbb F_7,\mathbb F_{11},\mathbb F_{13}\). For each field it checks three nondegenerate rank-one algebras with distinct determinant and isotropy behavior, enumerates all unordered orthogonal pairs directly from the algebra multiplication, enumerates all automorphisms from their multiplicativity equations, and calculates the orbits by explicit group action. All fifteen cases agree with the formulas and the script prints `VERIFY_OK`. The general formulas, including nonprime odd finite fields, are proven symbolically above and are not inferred from those tests.

## Relationship to prior work
Kaygorodov, Martín González and Viruel (2026), Question 14, explicitly ask for natural bases up to permutation and scaling and whether infinitely many are compatible with a finite automorphism group. Their own constructions show infinitude with other automorphism behavior, but do not state this sharp dimension-two finite-automorphism example or the two quadratic-character census formulas. Boudi, Cabrera Casado and Siles Molina (2020), especially Proposition 2.16, provide the previously established bilinear-form and natural-basis extension framework; **that reduction is not claimed as new**. Cabrera Casado and collaborators (2024), Section 2.8, explicitly establish the \(\mu_2\) automorphism group of the algebra \(e_1^2=e_1,\ e_2^2=\alpha e_1\); **the finite automorphism group of this example is also not claimed as new**. The new, delimited content is the exact natural-basis moduli description together with both complete odd-finite-field counts and automorphism-orbit classification, plus their coordinated answer to the specified question.

## Limitations
The theorem does not classify all higher-dimensional or all degenerate evolution algebras, and it excludes characteristic two. The literature already contains the essential bilinear-form reduction and two-dimensional automorphism classifications; the remaining originality risk is that the precise finite-field projective-pair and automorphism-orbit counts may be derivable implicitly or recorded under orthogonal-decomposition terminology elsewhere. Finite-field experiments verify selected prime fields only; they do not certify all field extensions.

## References
1. I. Kaygorodov, C. Martín González and A. Viruel, *Evolution algebras: a survey of results and a list of open problems*, 2026, arXiv:2610.22248v1, Question 14. https://arxiv.org/abs/2610.22248
2. N. Boudi, Y. Cabrera Casado and M. Siles Molina, *Natural families in evolution algebras*, arXiv:2006.14460v1, Proposition 2.16 and Corollary 2.13. https://arxiv.org/abs/2006.14460
3. Y. Cabrera Casado et al., *Hopf algebras and associative representations of two-dimensional evolution algebras*, arXiv:2407.15769v2, Section 2.8 and Table 1. https://arxiv.org/abs/2407.15769

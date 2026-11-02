# A modular conjugacy obstruction and exact census of anti-involutions on free cube-zero algebras

## Finding

For every finite field \(k=\mathbb F_q\), every \(n\geq1\), and the free nonunital associative algebra truncated after words of length two,
\[
 A_n(k)=V\oplus(V\otimes_k V),\qquad V=k^n,
\]
with multiplication \(vw=v\otimes w\) for \(v,w\in V\) and all products involving \(V\otimes V\) equal to zero, all involutive algebra **anti-automorphisms** admit an explicit classification and count. An anti-automorphism is a bijective linear map \(\sigma\) with \(\sigma(ab)=\sigma(b)\sigma(a)\); an anti-involution also satisfies \(\sigma^2=1\). The parameter count differs in odd and even characteristics, and in characteristic two a precise family of nonlinear anti-involutions cannot be conjugated to the linear reversal action by an automorphism acting trivially on \(A_n/A_n^2\).

Write \(G_d(q)=|\operatorname{GL}_d(\mathbb F_q)|=\prod_{j=0}^{d-1}(q^d-q^j)\), with \(G_0(q)=1\).

If \(q\) is odd, the exact total number of anti-involutions is
\[
 \boxed{\displaystyle N_{n,q}=\sum_{r=0}^{n}\frac{G_n(q)}{G_r(q)G_{n-r}(q)}q^{[n^3-n(2r-n)]/2}.}
\]
For a prescribed linear part with eigenvalue \(+1\) of multiplicity \(r\), there are exactly \(q^{[n^3-n(2r-n)]/2}\) anti-involutions, all conjugate by automorphisms inducing the identity on \(A_n/A_n^2\).

If \(q\) is even, put \(r=n-2s\). The exact total is
\[
 \boxed{\displaystyle N_{n,q}=\sum_{s=0}^{\lfloor n/2\rfloor}\frac{G_n(q)}{q^{s^2+2rs}G_s(q)G_r(q)}q^{r n(n+1)/2+s n^2}.}
\]
For each fixed linear involution with \(r\) blocks of size one and \(s\) blocks of size two, the number of anti-involutions is \(q^{r n(n+1)/2+s n^2}\). More strongly, **they split into exactly \(q^{rn}\) conjugacy orbits under the identity-linear automorphism subgroup**, each of size \(q^{n^3-r n(n+1)/2-s n^2}\). Hence every such anti-involution is identity-linearly conjugate to its purely linear model precisely when \(r=0\). When \(r>0\), there are genuinely non-linearizable anti-involutions.

For example, \(N_{2,q}=2q^6-q^4\) in characteristic two, and \(N_{2,q}=q^2+q(q+1)q^4+q^6\) in odd characteristic. Over \(\mathbb F_2\), the six-dimensional algebra \(A_2\) has precisely \(112\) anti-involutions in \(19\) identity-linear conjugacy orbits. Over \(\mathbb F_3\) it has precisely \(1710\) anti-involutions.

## Assumptions and scope

The product is ordinary associative concatenation, *not* symmetric or exterior multiplication. The algebra is nonunital and has \(A_n^3=0\). The invariants classify field-linear anti-involutions and, in the orbit refinement, conjugation by the normal subgroup of algebra automorphisms whose action on \(A_n/A_n^2\) is the identity. The orbit claim is deliberately not a classification up to the full automorphism group. All formulas include \(n=1\), characteristic two, and arbitrary finite extension fields.

## Proof

**1. Normal form and anti-involution equation.** Since \(A_n^2=V\otimes V\) is characteristic, an anti-automorphism induces an invertible \(L\in\operatorname{GL}(V)\). It is uniquely determined by an arbitrary \(h\in\operatorname{Hom}_k(V,V\otimes V)\):
\[
 \sigma(v)=Lv+h(v),\quad \sigma(v\otimes w)=Lw\otimes Lv.
\]
Conversely these prescriptions define an invertible anti-homomorphism, as its block-triangular matrix has invertible diagonal blocks. Let \(\tau(v\otimes w)=w\otimes v\) and \(F=(L\otimes L)\tau\). Squaring on the generators and on \(A_n^2\) gives exactly
\[
 L^2=I_V,\qquad hL+Fh=0.
\]
The second equation is a linear condition once the linear involution \(L\) is fixed.

**2. Odd characteristic.** For odd \(q\), write \(V=V_+\oplus V_-\) with \(\dim V_+=r\), \(\dim V_-=n-r\). Define the involution \(T\) on \(H=\operatorname{Hom}(V,V\otimes V)\) by \(T(h)=FhL\). Because \(L^2=1\) and \(F^2=1\), also \(T^2=1\), and the equation for \(h\) is \(T(h)=-h\). The trace of the flip-twisted tensor operator is \(\operatorname{tr}(F)=\operatorname{tr}(L^2)=n\); this follows in any basis from \(\operatorname{tr}((X\otimes Y)\tau)=\operatorname{tr}(XY)\). On \(H\cong (V\otimes V)\otimes V^*\), \(T\) acts as \(F\otimes L^*\), hence
\[
 \operatorname{tr}(T)=n\operatorname{tr}(L)=n(2r-n).
\]
The negative eigenspace has dimension \([n^3-n(2r-n)]/2\). There are \(G_n/(G_rG_{n-r})\) linear involutions of this type; multiplying their \(h\)-counts and summing gives the odd-characteristic formula.

**3. Characteristic two.** Here \(L^2=I\) is equivalent to \((L-I)^2=0\), so its Jordan type is \(1^r2^s\), \(r+2s=n\). Choose a basis in which \(L\) acts by fixing \(r\) basis vectors and swapping \(s\) disjoint pairs (a swap has the standard size-two unipotent Jordan block over characteristic two). In the basis of ordered tensor words, \(F(v_i\otimes v_j)=L(v_j)\otimes L(v_i)\) is a permutation involution with exactly \(n\) fixed words, namely the words \(v_i\otimes L(v_i)\). Its other \((n^2-n)/2\) orbits are two-cycles. Consequently, as modules over \(k[C_2]\), the domain \(V\) is the direct sum of \(r\) trivial modules and \(s\) free modules of dimension two; the codomain \(V\otimes V\) is the direct sum of \(n\) trivial modules and \((n^2-n)/2\) free modules. The solutions of \(hL=Fh\) are precisely \(k[C_2]\)-module homomorphisms. Maps from one trivial summand have dimension \(n+(n^2-n)/2=n(n+1)/2\), and maps from one free two-cycle have dimension \(n^2\). Therefore the solution space has dimension
\[
 e_{r,s}=\frac{rn(n+1)}2+sn^2.
\]

The centralizer of a linear involution of Jordan type \(1^r2^s\) is the unit group of \(\operatorname{End}_{k[t]/(t^2)}((k[t]/(t^2))^s\oplus k^r)\). Its semisimple quotient is \(M_s(k)\times M_r(k)\); the nilpotent radical has vector dimension \(s^2+2rs\). Hence the centralizer order is \(q^{s^2+2rs}G_s(q)G_r(q)\), giving \(G_n/[q^{s^2+2rs}G_sG_r]\) linear involutions of this type. Multiplying by \(q^{e_{r,s}}\) and summing proves the even-characteristic formula.

**4. The modular conjugacy obstruction.** Let \(U\cong H\) consist of all automorphisms \(u_g(v)=v+g(v)\) inducing identity on \(V=A_n/A_n^2\) (they fix \(A_n^2\)). Conjugation by \(u_g\) changes \(h\) by
\[
 h\longmapsto h+gL-Fg.
\]
Postcomposition with the isomorphism \(g\mapsto gL\) identifies its translation image with \(\operatorname{im}(I-T)\). In odd characteristic, \(\operatorname{im}(I-T)=\ker(I+T)\), so the \(U\)-action is transitive in each fixed-\(L\) fiber. In characteristic two, \(I-T=I+T\), and rank-nullity gives \(\dim\operatorname{im}(I+T)=n^3-e_{r,s}\). The fixed-\(L\) solution fiber has dimension \(e_{r,s}\), so its quotient by translation has dimension
\[
 2e_{r,s}-n^3=rn.
\]
This proves exactly \(q^{rn}\) orbits, each having cardinality \(q^{n^3-e_{r,s}}\). The purely linear anti-involution is the origin of the solution fiber, so all anti-involutions are linearizable by \(U\) if and only if \(rn=0\), which for \(n\ge1\) means \(r=0\).

## Verification

The bundled executable `verify.py` uses Python's standard library. Run `python3 verify.py` from the extracted directory. It independently constructs the original \(n+n^2\)-dimensional multiplication and the full anti-automorphism matrices, enumerates all linear parts and all admissible maps for \(n=2\) over \(\mathbb F_2\) and \(\mathbb F_3\), and directly checks anti-multiplicativity and squaring. Independent linear-equation rank checks also cover \(\mathbb F_4\) and \(n=3\) over \(\mathbb F_2\) and \(\mathbb F_3\); the finite field of order four is implemented as \(\mathbb F_2[t]/(t^2+t+1)\). Direct explicit conjugation for \(n=2\) over \(\mathbb F_2\) checks the \(19\) orbit claim. The output ends in `ANTI_INVOLUTION_CENSUS_AND_IA_ORBITS_OK`. Finite verification is not a proof for all \(n,q\); the structural argument above supplies that proof.

## Relationship to prior work

Involutions of associative algebras are classical; the algebraic notion and general theory are not novel. D. W. Lewis's 2006 survey discusses general results and other families of finite-dimensional associative algebras; its online abstract and contents were accessible but the full text was not, leaving a historical-priority risk. Scott Andrews (2013) and André–Freitas–Neto (2015) study fixed-point groups and supercharacter theories **given** algebraic anti-involutions. Their inspected primary texts do not state the present all-rank finite-field anti-involution census or the characteristic-two identity-linear orbit refinement. The two-step free algebra shares a tensor-grading with broader nilpotent-algebra literature; no universal novelty claim is made beyond the precise formulas and orbit obstruction above.

## Limitations

The theorem is for free nonunital associative algebras of nilpotence index three. It does not enumerate involutions on arbitrary quotients, on higher truncations, or conjugacy classes under the entire automorphism group. The geometric scheme structure of the anti-involution equations is not analyzed. Publication priority requires independent scrutiny, especially because an inaccessible general survey might subsume part of the result. Independent mathematical validation has not been performed.

## References

- D. W. Lewis, *Involutions and Anti-Automorphisms of Algebras*, Bulletin of the London Mathematical Society 38 (2006), 529–545, DOI `10.1112/S002460930601873X`; Cambridge first online date 2006-07-24. Publisher abstract and contents inspected; full text inaccessible.
- S. Andrews, *Supercharacters of unipotent groups defined by involutions*, arXiv:1311.1730 (initial preprint 2013-11-07); full preprint inspected in pertinent sections.
- C. A. M. André, P. J. Freitas, A. M. Neto, *A supercharacter theory for involutive algebra groups*, arXiv:1502.01512 (initial preprint 2015-02-05); full preprint inspected in pertinent sections.

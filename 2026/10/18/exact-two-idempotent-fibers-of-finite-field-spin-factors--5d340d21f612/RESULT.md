# Exact two-idempotent fibers of finite-field spin factors

## Finding

Let \(q\) be any odd prime power, and let \((V,b)\) be a nondegenerate symmetric bilinear space of dimension \(d\geq 3\) over \(\mathbb F_q\). Write \(Q(w)=b(w,w)\), let \(\Delta\) be the determinant square class of \(b\), and set \(c=1/4\). In the associated spin-factor Jordan algebra \(J=\mathbb F_q 1\oplus V\), the primitive idempotents are precisely \(e_u=\frac12 1+u\) with \(Q(u)=c\).

Every product of **two primitive idempotents** has the form
\[
e_u\circ e_v=2Q(w)1+w,\qquad w=(u+v)/2.
\]
For each \(w\in V\), let \(F(w)\) be the number of ordered pairs \((u,v)\) of primitive idempotent parameters having this product. Then the entire fiber profile is
\[
F(w)=\begin{cases}
N_d(\Delta,c), &w=0,\\
N_{d-1}(\Delta/Q(w),c-Q(w)),&Q(w)\ne0,\\
qN_{d-2}(-\Delta,c),&w\ne0,\ Q(w)=0.
\end{cases}
\]
Here \(N_r(\delta,t)\) counts the vectors of quadratic value \(t\) in any nondegenerate \(r\)-dimensional quadratic form of determinant square class \(\delta\). It is explicitly given in the next section, so the formula determines every fiber from \(q,d,\Delta,Q(w)\).

**Sharp image threshold.** For \(d\ge4\), every one of the \(q^d\) points \(2Q(w)1+w\) is attained by a pair of primitive idempotents. For \(d=3\), all \(q^3\) graph points occur when \(\chi(-\Delta)=1\); when \(\chi(-\Delta)=-1\), precisely the \(q^2-1\) points with \(w\ne0\) and \(Q(w)=0\) are missing, leaving exactly \(q^3-q^2+1\) attained points. Here \(\chi\) is the quadratic character of \(\mathbb F_q\).

## Assumptions and scope

The field has **odd** characteristic; \(q\) may be a nonprime prime power. The form \(b\) is symmetric and nondegenerate and \(d\ge3\). The spin-factor product is
\[
(a1+u)\circ(c_01+v)=(ac_0+b(u,v))1+a v+c_0u.
\]
The determinant \(\Delta\) is understood modulo nonzero squares, and expressions such as \(\Delta/Q(w)\) denote square classes. A change of basis does not affect these classes. Only ordered pairs of *nontrivial* (primitive) idempotents are counted; the trivial idempotents \(0\) and \(1\) are not used as factors.

For completeness, for nonzero determinant class \(\delta\), put
\[
N_r(\delta,t)=\begin{cases}
q^{r-1}+(q-1)\varepsilon q^{(r-2)/2},&r\text{ even},\ t=0,\\
q^{r-1}-\varepsilon q^{(r-2)/2},&r\text{ even},\ t\ne0,\\
q^{r-1},&r\text{ odd},\ t=0,\\
q^{r-1}+\chi((-1)^{(r-1)/2}\delta t)q^{(r-1)/2},&r\text{ odd},\ t\ne0,
\end{cases}
\]
where \(\varepsilon=\chi((-1)^{r/2}\delta)\). In particular \(N_1(\delta,c)=1+\chi(\delta)\) because \(c\) is a square.

## Proof

**1. Primitive idempotents and the product graph.** For \(e=a1+u\), idempotency says \(a^2+Q(u)=a\) and \((2a-1)u=0\). If \(u=0\), one has \(e=0\) or \(e=1\). Otherwise \(a=1/2\) and \(Q(u)=1/4=c\). Thus the primitive idempotents are exactly the stated \(e_u\). Write uniquely \(u=w+z\) and \(v=w-z\) with \(w=(u+v)/2\) and \(z=(u-v)/2\). The simultaneous equations \(Q(u)=Q(v)=c\) are equivalent to
\[
b(w,z)=0,\qquad Q(z)=c-Q(w).
\]
The scalar part of \(e_u\circ e_v\) then equals \(c+Q(w)-Q(z)=2Q(w)\), while the vector part is \(w\). Conversely, each such \(z\) determines a unique ordered pair \((u,v)\). The fiber over \(w\) is therefore the exact count of vectors \(z\in w^\perp\) of quadratic value \(c-Q(w)\).

**2. Nondegenerate and degenerate orthogonal complements.** If \(w=0\), the complement is all of \(V\), giving \(N_d(\Delta,c)\). If \(Q(w)\ne0\), the orthogonal sum \(V=\langle w\rangle\perp w^\perp\) has nondegenerate second factor of dimension \(d-1\), determinant square class \(\Delta/Q(w)\), and count \(N_{d-1}(\Delta/Q(w),c-Q(w))\). If \(w\ne0\) and \(Q(w)=0\), choose an isotropic partner \(w'\) with \(b(w,w')=1\) and replace \(w'\) by \(w'-(Q(w')/2)w\), making a hyperbolic plane of Gram determinant \(-1\). The space \(w^\perp\) has radical \(\langle w\rangle\). Its nondegenerate quotient has dimension \(d-2\) and determinant square class \(-\Delta\), since splitting off that hyperbolic plane multiplies the determinant by \(-1\). Every quotient vector has exactly \(q\) lifts to \(w^\perp\) with the same quadratic value. This establishes the third case.

**3. The finite-field quadratic counts.** Diagonalize the relevant nondegenerate form, of dimension \(r\) and determinant \(\delta\), and choose a nontrivial additive character \(\psi\) of \(\mathbb F_q\). For every \(s\ne0\), the quadratic Gauss-sum identity gives
\[
\sum_{x\in\mathbb F_q^r}\psi(sQ(x))
=\chi(s)^r\chi(\delta)G^r,
\quad G=\sum_{a\in\mathbb F_q}\psi(a^2),\quad G^2=\chi(-1)q.
\]
By additive-character orthogonality, \(N_r(\delta,t)=q^{-1}\sum_s\psi(-st)\sum_x\psi(sQ(x))\). When \(r\) is even, the sum over nonzero \(s\) is \(q-1\) for \(t=0\) and \(-1\) otherwise; when \(r\) is odd, its value is zero for \(t=0\) and \(\chi(-t)G\) for nonzero \(t\). Substitution yields exactly the four formulas defining \(N_r\). The identity is valid for every odd prime power, including extension fields.

**4. Sharp image size.** In nondegenerate dimensions \(r\ge2\), the displayed formulas give \(N_r(\delta,t)>0\) for all \(t\). Hence, for \(d\ge4\), the first two cases have positive fibers and the isotropic case has nondegenerate quotient dimension \(d-2\ge2\), likewise positive. For \(d=3\), only the nonzero isotropic case could vanish: its quotient has dimension one and
\[
F(w)=q N_1(-\Delta,c)=q(1+\chi(-\Delta)).
\]
A nondegenerate three-dimensional quadratic form has exactly \(q^2\) zeros, by the odd-rank formula at \(t=0\). There are thus precisely \(q^2-1\) nonzero isotropic vectors, and all other fibers are positive. Since \(w\mapsto 2Q(w)1+w\) is injective, the asserted image sizes follow. Summing the fibers counts all ordered pairs, namely \(N_d(\Delta,c)^2\), providing a consistency identity.

## Verification

The accompanying self-contained `verify.py` performs a separate finite-field enumeration, including explicit quadratic extension-field arithmetic. For every tested nondegenerate diagonal form, it constructs every primitive idempotent, enumerates every ordered pair, computes the resulting vector part, and checks **each** \(F(w)\) against the closed formula; it also checks the excluded-image count and the global pair count. Execute `python3 verify.py`. It reports `VERIFY_OK 20 complete configurations` for dimensions \(3,4\) over \(\mathbb F_3,\mathbb F_5,\mathbb F_7,\mathbb F_{11}\) with both discriminant classes, and dimension \(3\) over \(\mathbb F_9,\mathbb F_{25}\) with both classes. The checker is a finite consistency test, **not** a proof of all field sizes or dimensions; the preceding argument proves the universal statement.

## Relationship to prior work

Gogić and Tomašević, *Idempotent words in finite-dimensional simple Jordan algebras* (arXiv:2609.23581v1, 20 September 2026), §3 and especially Lemma 3.1, identify the algebraic graph relation for products of two idempotents in spin factors over **quadratically closed fields**. Their hypotheses do not imply solvability over finite fields, which are not quadratically closed, and they do not calculate these fiber multiplicities or the discriminant-controlled ternary missing locus. The product-graph relation itself is **not claimed to be new**; the exact finite-field fibers and sharp obstruction are the contribution here. Rowen and Segev, *Associative and Jordan algebras generated by two idempotents* (arXiv:1609.04899), classify algebras generated by two idempotents, a different question from counting pairs producing a prescribed Jordan product. Standard finite-field quadratic-form character sums supply the enumerative ingredient. No uniqueness or first-discovery guarantee is claimed.

## Limitations

The statement concerns two **primitive** idempotent factors in nondegenerate spin factors of vector dimension at least three and in odd characteristic. It does not classify longer idempotent words, factors \(0\) or \(1\), degenerate forms, characteristic two, or Jordan algebras of different types. Quadratic character sums and finite-dimensional orthogonal complements are classical; related counts may occur under the language of orthogonal association schemes or sphere intersections.

## References

1. I. Gogić and M. Tomašević, *Idempotent words in finite-dimensional simple Jordan algebras*, arXiv:2609.23581v1 (first public version 20 September 2026), https://arxiv.org/abs/2609.23581 .
2. L. H. Rowen and Y. Segev, *Associative and Jordan algebras generated by two idempotents*, arXiv:1609.04899 (2016), https://arxiv.org/abs/1609.04899 .
3. R. Lidl and H. Niederreiter, *Finite Fields*, Cambridge University Press: standard quadratic Gauss sums and value distributions for quadratic forms (background, not relied on for an asserted novelty claim).

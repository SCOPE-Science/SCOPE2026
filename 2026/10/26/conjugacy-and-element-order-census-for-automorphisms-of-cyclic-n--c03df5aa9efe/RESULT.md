# Conjugacy and element-order census for automorphisms of cyclic nilpotent Leibniz algebras

## Finding

Let \(q=p^f\) be any prime power, \(n\ge2\), and \(L_n(q)\) the \(n\)-dimensional left Leibniz algebra over \(\mathbb F_q\) with basis \(e_1,\ldots,e_n\), nonzero products \([e_1,e_i]=e_{i+1}\) for \(1\le i<n\), and all other basis products zero. Set \(G_{n,q}=\operatorname{Aut}_{\mathbb F_q}(L_n(q))\). Write \(\varphi\) for Euler's totient, and write \(h_d=\lfloor(n-1)/d\rfloor\) for positive integers \(d\).

**Conjugacy-class census.** The number of conjugacy classes of \(G_{n,q}\) is exactly
\[
 k(G_{n,q})=\frac{1}{q-1}\sum_{d\mid(q-1)}\sum_{e\mid(q-1)}
 \varphi(d)\varphi(e)\,q^{\left\lfloor (n-1)/\operatorname{lcm}(d,e)\right\rfloor}.
\]
More precisely, for an individual multiplier \(a\in\mathbb F_q^\times\) of exact order \(d\), the number of conjugacy classes whose induced map on \(L_n/[L_n,L_n]\) is multiplication by \(a\) equals
\[
 \frac{1}{q-1}\sum_{e\mid(q-1)}\varphi(e)\,q^{\left\lfloor(n-1)/\operatorname{lcm}(d,e)\right\rfloor}.
\]

**Complete element-order census.** For \(d\mid(q-1)\) and \(r\ge0\), define
\[
 B_{d,r}=q^{h_d-\lfloor h_d/p^r\rfloor},\qquad B_{d,-1}=0.
\]
The number of elements of **exact** order \(dp^r\) in \(G_{n,q}\) is
\[
 E_{n,q}(d,r)=\varphi(d)q^{n-1-h_d}\bigl(B_{d,r}-B_{d,r-1}\bigr).
\]
All other exact orders have count zero. In particular \(E_{n,q}(1,0)=1\). These counts add to \(|G_{n,q}|=(q-1)q^{n-1}\). As a further exact consequence, the number of ordered commuting pairs in \(G_{n,q}^2\) is \((q-1)q^{n-1}k(G_{n,q})\).

## Assumptions and scope

The algebra is the unique standard \(n\)-dimensional *nilpotent cyclic* left Leibniz algebra specified by its products; the result does not concern other cyclic Leibniz types or arbitrary nilpotent Leibniz algebras. The ground field is the full \(\mathbb F_q\), the characteristic is the prime \(p\), and the automorphism group consists of field-linear bracket-preserving bijections, not semilinear automorphisms. The order and conjugacy counts are for group elements and group-conjugacy classes, respectively, not for algebra isomorphism classes. The formula includes \(n=2\) and \(q=2\).

## Proof

**1. Normal form and group law.** Identifying \(e_i\) with \(t^i\) as vector-space bases modulo \(t^{n+1}\), an automorphism \(F\) is uniquely specified by
\[
 F(e_1)=a e_1+a u_1e_2+\cdots+a u_{n-1}e_n,
 \quad a\in\mathbb F_q^\times,
\]
where \(u_j\in\mathbb F_q\). Indeed \(F(e_{i+1})=[F(e_1),F(e_i)]\) recursively forces
\[
 F(e_i)=a^i\bigl(e_i+u_1e_{i+1}+\cdots+u_{n-i}e_n\bigr),
\]
and conversely these formulas preserve all brackets and yield triangular invertible matrices. Write \(U(t)=1+\sum_{j=1}^{n-1}u_jt^j\) modulo \(t^n\). Then \(F=F_{a,U}\) acts on \(t f(t)\) by \(a tU(t)f(at)\), with multiplication
\[
 (a,U)(b,V)=(ab,U(t)V(at)).
\]
Thus, setting \(\mathcal U_n=1+t\mathbb F_q[t]/(t^n)\), and \(\tau_a(U)=U(at)\), we have \(G_{n,q}\cong\mathcal U_n\rtimes\mathbb F_q^\times\). Here \(\mathcal U_n\) is an abelian \(p\)-group of size \(q^{n-1}\); the cyclic group \(\mathbb F_q^\times\) acts by scaling.

**2. A coprime-action decomposition.** Fix a multiplier \(a\) of order \(d\mid(q-1)\), and let \(W_d=\mathcal U_n^{\tau_a}\). Coefficient comparison gives
\[
 W_d=\{1+\sum_{j=1}^{h_d}c_j t^{dj}:c_j\in\mathbb F_q\},
 \qquad |W_d|=q^{h_d}.
\]
The norm map \(N_d:\mathcal U_n\to W_d\), \(N_d(U)=\prod_{j=0}^{d-1}\tau_a^j(U)\), is a homomorphism because \(\mathcal U_n\) is abelian. It is surjective: for \(w\in W_d\), the map \(w\mapsto w^d\) is an automorphism of the finite \(p\)-group \(W_d\), since \(p\nmid d\); if \(v^d=w\), then \(N_d(v)=w\). Hence every norm fiber has size \(q^{n-1-h_d}\).

Define \(\delta_a(U)=U/\tau_a(U)\). Its kernel is \(W_d\), so its image has cardinality \(q^{n-1-h_d}\); telescoping shows \(\operatorname{im}\delta_a\subseteq\ker N_d\), and the equal sizes prove equality. If \(w\in W_d\cap\operatorname{im}\delta_a\), then \(w^d=N_d(w)=1\), forcing \(w=1\), again because \(p\nmid d\). Consequently
\[
 \mathcal U_n=W_d\times\operatorname{im}\delta_a
\]
as an internal product of abelian groups, equivariantly for all scalar substitutions \(\tau_b\). This is an actual decomposition, not merely an equality of cardinalities.

**3. Conjugacy classes.** Conjugation of \((a,U)\) by an element in \(\mathcal U_n\) changes its \(U\)-coordinate by a factor from \(\operatorname{im}\delta_a\); scalar conjugation by \(b\in\mathbb F_q^\times\) replaces the remaining coordinate by \(\tau_b(U)\). The multiplier \(a\) itself is conjugacy-invariant. By Step 2, classes over fixed \(a\) correspond exactly to \(\mathbb F_q^\times\)-orbits on \(W_d\). If \(b\) has order \(e\), its fixed elements in \(W_d\) are polynomials supported in degrees divisible by \(\operatorname{lcm}(d,e)\), and their number is \(q^{\lfloor(n-1)/\operatorname{lcm}(d,e)\rfloor}\). Burnside's lemma, with \(\varphi(e)\) choices of \(b\), yields the fixed-multiplier formula. Summing over \(\varphi(d)\) multipliers of order \(d\) gives the displayed total.

**4. Exact orders.** For a multiplier \(a\) of exact order \(d\), the \(d\)-th power of \((a,U)\) is \((1,N_d(U))\). Its exact group order is therefore \(d\) times the \(p\)-power order of \(N_d(U)\). By Step 2, \(N_d(U)\) is uniformly distributed over \(W_d\) as \(U\) ranges over \(\mathcal U_n\), with \(q^{n-1-h_d}\) preimages per target. Substitute \(z=t^d\); the group \(W_d\) is the principal-unit group \(1+z\mathbb F_q[z]/(z^{h_d+1})\). In characteristic \(p\), the identity
\[
 (1+\sum_{j=1}^{h_d}c_jz^j)^{p^r}
 =1+\sum_{j=1}^{h_d}c_j^{p^r}z^{jp^r}
 \pmod{z^{h_d+1}}
\]
shows that this power equals one precisely when \(c_j=0\) for all \(j\le\lfloor h_d/p^r\rfloor\). Because the Frobenius map is injective, there are exactly \(B_{d,r}=q^{h_d-\lfloor h_d/p^r\rfloor}\) such units. Subtraction isolates exact order \(p^r\); multiplying by the norm-fiber size and by \(\varphi(d)\) yields \(E_{n,q}(d,r)\). For \(r=0\), \(B_{d,0}=1\) and \(B_{d,-1}=0\) correctly count the identity of \(W_d\). For sufficiently large \(r\), \(B_{d,r}=|W_d|\), so all counts exhaust \(G_{n,q}\). Finally, the standard class equation for the conjugation action yields \(\#\{(g,h)\in G_{n,q}^2:gh=hg\}=|G_{n,q}|k(G_{n,q})\).

## Verification

A standalone Python program, `verify_cyclic_leibniz.py`, directly enumerates the semidirect product from the coefficient multiplication rule, computes exact element orders by repeated multiplication, and counts commuting ordered pairs to obtain the number of conjugacy classes. It compares these brute-force values to the closed formulas over \(\mathbb F_2,\mathbb F_3,\mathbb F_4,\mathbb F_5\) in eleven \((q,n)\) cases, including \(n=5\) in characteristic two. The finite-field implementation of \(\mathbb F_4\) uses the irreducible polynomial \(x^2+x+1\). The executed checker finishes with `CYCLIC_LEIBNIZ_CENSUS_OK`. The general validity rests on the proof, not on finite enumeration.

Representative checks: \(k(G_{3,3})=9\) for a group of order \(18\); \(k(G_{4,4})=32\) for order \(192\); and \(k(G_{4,5})=38\) for order \(500\). All exact-order histograms agree with the theorem.

## Relationship to prior work

Batten Ray et al. (arXiv:1207.3739, submitted July 2012) and Bugg et al. (arXiv:1402.5821, submitted February 2014) study the basic and nilpotent cyclic Leibniz examples, not the finite-field order and conjugacy statistics. Kurdachenko, Pypka and Subbotin (arXiv:2108.06794, 2021), particularly Section 2 and Theorem 2.11, establish the explicit general automorphism normal forms and the semidirect product by truncated polynomial principal units. This is strong structural prior coverage of Step 1. The present exact simultaneous conjugacy-class and element-order formulas are derived by an additional coprime norm decomposition, fixed-unit orbit analysis and prime-power filtration enumeration; they are not stated in the inspected type-I treatment. The group structure is not claimed as new. It remains possible that equivalent enumerations appear elsewhere or are obtainable from a more general theorem.

## Limitations

No independent mathematical audit has been performed. The formulas count automorphisms of the specified standard nilpotent cyclic left Leibniz algebra over finite fields; they do not determine automorphism statistics for nonnilpotent cyclic types or arbitrary ground fields. No claims are made concerning broader automorphism schemes or the distribution of individual conjugacy-class sizes. The source comparison is bounded and cannot establish absolute publication priority; complete group structure was already known in the cited 2021 work.

## References

1. C. Batten Ray, A. Combs, N. Gin, A. Hedges, J. T. Hird, L. Zack, *Nilpotent Lie and Leibniz algebras*, arXiv:1207.3739, first submitted 2012-07-16. https://arxiv.org/abs/1207.3739
2. K. Bugg, A. Hedges, M. Lee, D. Scofield, S. M. Sullivan, *Cyclic Leibniz Algebras*, arXiv:1402.5821, first submitted 2014-02-24. https://arxiv.org/abs/1402.5821
3. L. A. Kurdachenko, A. A. Pypka, I. Ya. Subbotin, *On the automorphism groups of some Leibniz algebras*, arXiv:2108.06794, first submitted 2021-08-15. https://arxiv.org/abs/2108.06794

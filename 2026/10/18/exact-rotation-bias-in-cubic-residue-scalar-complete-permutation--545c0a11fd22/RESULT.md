# Exact rotation bias in cubic-residue scalar complete permutations

## Finding

Let \(q\) be any prime power with \(q\equiv1\pmod 9\), let \(s=(q-1)/3\), and put \(K=\{a\in\mathbb F_q^*:a^s=1\}\) and \(\mu_3=\{u\in\mathbb F_q^*:u^3=1\}\). Fix any positive integer \(k\). For every function \(c:\mu_3\to K\), let \(C_c(T)\in\mathbb F_q[T]\) be its unique interpolating polynomial of degree at most two and define

\[
 f_c(X)=X^{1+ks} C_c(X^s).
\]

The distinct functions \(c\) parameterize distinct polynomial functions \(f_c\) on \(\mathbb F_q\). Call \(c\) *complete* if both \(f_c\) and \(f_c+X\) permute \(\mathbb F_q\). Every \(f_c\) is already a permutation, so completeness is the condition on the second map.

Choose a multiplicative character \(\chi:\mathbb F_q^*\to\{1,\zeta,\zeta^2\}\) of order three, extended by \(\chi(0)=0\), where \(\zeta=e^{2\pi i/3}\). Choose a primitive cube root \(\omega\in\mathbb F_q\) and identify it with \(\zeta\) by requiring \(\chi(y)=\zeta^j\) when \(y^s=\omega^j\). Label the three fibers by \(x^s=\omega^i\), for \(i=0,1,2\). Reversing this compatible character convention merely interchanges two class counts. Define the classical cubic Jacobi sum

\[
 J=J(\chi,\chi)=\sum_{t\in\mathbb F_q}\chi(t)\chi(1-t),
 \qquad z=J-2,
\]

and the three integers

\[
 N_j=\frac{q-4+\zeta^{-j}z+\zeta^j\overline z}{9},\qquad j=0,1,2.
\]

Then the number \(R_q\) of complete functions whose induced permutation of the three fibers is a rotation (a translation in \(\mathbb Z/3\mathbb Z\)) and the number \(T_q\) whose induced permutation is a transposition are **exactly**

\[
 R_q=N_0^3+N_1^3+N_2^3,
 \qquad T_q=3N_0N_1N_2.
\]

All six induced permutations are realized for every allowed \(q\). The rotation bias has the **strict, exact Jacobi-norm identity**

\[
 \boxed{\ R_q-T_q=\frac{q-4}{27}|J(\chi,\chi)-2|^2>0.\ }
\]

In particular,

\[
 R_q-T_q=\frac{q^2}{27}+O(q^{3/2}),
 \qquad
 \frac{R_q+T_q}{s^3}=\frac29-\frac{5}{3q}+O(q^{-3/2}),
\]

where the implied constants are absolute as \(q\) ranges over allowed prime powers. The complete-family counts have the sharper separate asymptotics

\[
 \frac{R_q}{s^3}=\frac19-\frac1{3q}+O(q^{-3/2}),\qquad
 \frac{T_q}{s^3}=\frac19-\frac4{3q}+O(q^{-3/2}).
\]

The count is independent of \(k\). It counts each input function, equivalently each distinct induced polynomial function, once; it is not the number of syntactically different polynomials of unrestricted degree.

## Assumptions and scope

The field size is a prime power \(q\equiv1\pmod9\); in particular \(q\ge19\). The parameter \(k\ge1\) is fixed but arbitrary. The coefficient function \(c\) takes values only in the cubic-residue subgroup \(K\) of order \(s\), exactly as in the scalar-fiber hypothesis. No statement is made about arbitrary cyclotomic multipliers outside \(K\), or about polynomial shapes with exponents not congruent to one modulo \(s\).

For \(x\neq0\) with \(x^s=u\in\mu_3\), the equality \(u^k\in K\) follows from \(3\mid s\). Thus multiplication by \(u^k\) bijects \(K\) with itself. Write \(a_u=u^k c(u)\in K\). On the fiber \(x^s=u\), one has \(f_c(x)=a_u x\) and \((f_c+X)(x)=(1+a_u)x\).

## Proof

**1. Fiber permutations.** Since all multipliers \(a_u\) are in \(K\), the map \(f_c\) preserves each multiplicative fiber and permutes it by nonzero scalar multiplication. Hence \(f_c\) is a permutation for every \(c\). The second map permutes the field if and only if each \(1+a_u\ne0\) and the induced map \(u\mapsto u(1+a_u)^s\) permutes \(\mu_3\). Necessity follows because a zero scalar collapses a fiber, and two fibers cannot have the same image fiber under a bijection; sufficiency follows because each nonzero scalar bijects its fiber and the three image fibers are disjoint. This is the scalar specialization of the classical cyclotomic-fiber criterion, proved here in both directions.

Since the assignments \(u\mapsto a_u\) and \(u\mapsto c(u)\) are in bijection, the count does not depend on \(k\). For \(j\in\{0,1,2\}\), let \(N_j\) be the number of \(a\in K\) with \(1+a\ne0\) and \(\chi(1+a)=\zeta^j\). If the fiber indices are \(i=0,1,2\), the induced image index is \(i+j_i\pmod3\). Among the six permutations of three indices, the three cyclic translations correspond to constant triples \((j_0,j_1,j_2)=(j,j,j)\), and the three transpositions correspond precisely to the three reorderings of \((0,1,2)\) compatible with a transposition. They therefore contribute \(R_q=\sum_j N_j^3\) and \(T_q=3\prod_jN_j\).

**2. Exact cubic-class populations.** Extend \(\chi\) by zero. Since \(q\equiv1\pmod9\), the group \(\mu_3\) lies in \(K\), and \(-1\in K\) (for odd characteristic, \(2\mid s\); in characteristic two, \(-1=1\)). Thus \(\chi(-1)=1\). The character indicator of \(K\) away from zero is \((1+\chi+\overline\chi)/3\). Set

\[
 S=\sum_{a\in K}\chi(1+a).
\]

The three sums in the indicator expansion are, respectively, \(-1\), \(J(\chi,\chi)\), and \(-1\): the middle equality uses \(\chi(-1)=1\), and the last is the standard mixed Jacobi sum \(J(\overline\chi,\chi)=-\chi(-1)=-1\). Consequently \(3S=J-2=z\). By the order-three character indicator for \(1+a\ne0\),

\[
 3N_j=(s-1)+\zeta^{-j}S+\zeta^j\overline S,
\]

which gives precisely the stated integer formula for \(N_j\). The classical Gauss-sum relation for nontrivial \(\chi\) and \(\chi^2\) gives \(|J(\chi,\chi)|=\sqrt q\). In particular, each

\[
 N_j\ge\frac{q-8-2\sqrt q}{9}>0
\]

because every allowed \(q\ge19>16\). Thus all three rotations and all three transpositions occur.

**3. Exact strict bias.** Put \(B=(q-4)/9\) and \(d_j=N_j-B\). Character orthogonality gives \(\sum_jd_j=0\) and

\[
 \sum_{j=0}^{2}d_j^2=\frac2{27}|z|^2.
\]

The elementary identity

\[
 x^3+y^3+z^3-3xyz
 =(x+y+z)\bigl(x^2+y^2+z^2-xy-yz-zx\bigr)
\]

applied to the three \(N_j\), and \(\sum_jN_j=(q-4)/3\), gives

\[
 R_q-T_q=\frac{q-4}{3}\cdot\frac32\sum_jd_j^2
 =\frac{q-4}{27}|J-2|^2.
\]

Since \(|J|=\sqrt q>2\), \(J\ne2\), so the difference is strictly positive.

**4. Sharp frequency expansion.** The classical estimate \(|J|=\sqrt q\) implies \(|z|\le\sqrt q+2\) and \(|z|^2=q+O(\sqrt q)\). Expanding the symmetric polynomials in \(B\) and \(d_j\), with \(\sum_jd_j^3=O(q^{3/2})\), yields

\[
 R_q=\frac{q^3-6q^2}{243}+O(q^{3/2}),\qquad
 T_q=\frac{q^3-15q^2}{243}+O(q^{3/2}).
\]

Finally \(s^3=(q-1)^3/27\), and elementary division gives all three normalized asymptotics. Directly the bias identity gives \(R_q-T_q=q^2/27+O(q^{3/2})\).

## Verification

The standalone source file `verify.py` enumerates cubic-residue multipliers for \(q=19,37,64,73,109,127,163,199\). It computes the cubic Jacobi sum in the exact Eisenstein-integer representation \(A+B\zeta\), verifies its norm equals \(q\), independently counts \(N_j\), checks the closed formulas, and tests the exact bias. For \(q=19,37,64,73\) it also tests **every** ordered triple of admissible multipliers against actual bijectivity of both maps on every field element, rather than only rechecking the fiber criterion. The \(q=64\) test uses polynomial-basis arithmetic over \(\mathbb F_2\) with modulus \(X^6+X+1\). All calculations are exact integers. Run `python3 verify.py`, expecting the final line `VERIFY_OK`.

These finite tests are not substitutes for the proof for arbitrary prime powers.

## Relationship to prior work

Bouyacoub, El-Baz, and Kihel establish the scalar-fiber complete-permutation criterion (Theorem 5.1) and construct examples using **constant** induced cubic-character shifts (Corollary 5.3). Their paper does not enumerate its coefficient functions or quantify the relative abundance of the nonconstant/transposition patterns. The exact full count and Jacobi-norm *rotation bias* are the present contribution; the criterion and the standard character-sum identities are credited inputs.

Fear and Wanless give the general necessary-and-sufficient cyclotomic orthomorphism test (Lemma 1) and count *near-linear* orthomorphisms of fixed index, but not the restricted full class spectrum enumerated here. Bell's earlier article gives total counts of cyclotomic orthomorphisms of index three for certain field orders. That publication is particularly relevant to novelty; only its bibliographic record and abstract were accessible, and they do not determine whether its full derivation treats the **simultaneous cubic-residue restriction and separate rotation/transposition counts**. Thus exact overlap with Bell's full text remains unresolved. Standard cubic cyclotomic-number and Jacobi-sum formulas supply local input, not an already identified full-permutation type census.

## Limitations

No claim is made for arbitrary index-three cyclotomic mappings without the cubic-residue multiplier condition, or for higher cyclotomic indices. The formulas are exact for functions \(c\) with values in \(K\), and the character \(\chi\) may be replaced by its conjugate without changing the final counts. An earlier article on full index-three orthomorphism enumeration could contain an equivalent restricted calculation, so further external literature examination is desirable.

## References

1. Chahrazade Bouyacoub, Asmae El-Baz, Omar Kihel, *On Permutation Trinomials and Complete Permutation Polynomials via Fiber Criteria over Finite Fields*, arXiv:2603.03368, first posted 2026-03-02, especially Theorem 5.1 and Corollary 5.3. https://arxiv.org/html/2603.03368
2. David Fear, Ian M. Wanless, *Existence results for cyclotomic orthomorphisms*, Journal of Algebraic Combinatorics 46 (2017), arXiv:2101.00859, especially Lemma 1 and Theorem 1. https://arxiv.org/abs/2101.00859
3. Jordan Bell, *Cyclotomic orthomorphisms of finite fields*, Discrete Applied Mathematics 161 (2013), 294–300, DOI 10.1016/j.dam.2012.08.013. Full text not examined; plausible broader overlap.
4. *Ternary cyclotomic numbers and ternary Jacobi sums*, AIMS Mathematics (2024), DOI 10.3934/math.20241292; standard cubic cyclotomic input. https://doi.org/10.3934/math.20241292

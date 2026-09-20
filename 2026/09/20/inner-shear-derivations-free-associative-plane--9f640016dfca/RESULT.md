# Exact isotropy for inner-shear derivations of the free associative plane

Let \(k\) be an algebraically closed field of characteristic zero and let
\[
F=k\langle x,y\rangle.
\]
For \(f,g\in k[y]\), define a derivation \(D_{f,g}\in\operatorname{Der}_k(F)\) by
\[
D_{f,g}(y)=0,\qquad D_{f,g}(x)=f(y)+[x,g(y)].
\]
Equivalently, if \(\delta_f(y)=0\), \(\delta_f(x)=f(y)\), then
\[
D_{f,g}=\delta_f-\operatorname{ad}_{g(y)},
\]
and the two summands commute.

The recent paper of Baltazar--Lopes--Morales, arXiv:2609.19470v1, proves that Pan's converse fails for \(F\) by exhibiting the two derivations
\[
D(y)=0,\quad D(x)=[x,y]
\]
and
\[
D(y)=0,\quad D(x)=1+[x,y].
\]
Both are non-locally-nilpotent while their isotropy groups contain the arbitrary shears \(x\mapsto x+h(y)\). The family above simultaneously contains these examples and admits an exact kernel, local-nilpotence, and isotropy classification.

## Theorem

Assume that \(g\) is nonconstant. Then:

1. The kernel is exactly
   \[
   \ker D_{f,g}=k[y].
   \]

2. \(D_{f,g}\) is neither locally nilpotent nor locally finite. More generally,
   \[
   D_{f,g}\text{ is locally nilpotent}\quad\Longleftrightarrow\quad g\in k.
   \]

3. Every automorphism commuting with \(D_{f,g}\) is triangular. Precisely,
   \[
   \operatorname{Aut}_{D_{f,g}}(F)
   =
   \left\{
   \rho_{a,b,c,h}:
   \begin{array}{l}
   \rho(y)=ay+b,\\
   \rho(x)=cx+h(y)
   \end{array}
   \ \middle|\ 
   \begin{array}{l}
   a,c\in k^\times,\ b\in k,\ h\in k[y],\\
   g(ay+b)-g(y)\in k,\\
   f(ay+b)=c f(y)
   \end{array}
   \right\}.
   \]

In particular, the shear subgroup
\[
U=\{x\mapsto x+h(y),\ y\mapsto y:h\in k[y]\}\cong(k[y],+)
\]
is contained in the isotropy group for every \(f,g\), and it has unbounded degree. Thus every member of the family with nonconstant \(g\) gives a non-locally-finite derivation with isotropy of unbounded degree.

## Proof

Give \(F\) the grading by the number of occurrences of \(x\). The derivation \(\delta_f\) lowers this degree, whereas
\[
T=-\operatorname{ad}_{g(y)},\qquad T(u)=[u,g(y)],
\]
preserves it. If \(u\in\ker D_{f,g}\) has highest \(x\)-degree component \(u_m\), then the highest \(x\)-degree component of \(D_{f,g}(u)\) is
\[
[u_m,g(y)].
\]
Hence \(u_m\) centralizes \(g(y)\).

For nonconstant \(g\), Bergman's centralizer theorem gives
\[
C_F(g(y))=k[z]
\]
for some \(z\in F\). Since \(y\) commutes with \(g(y)\), one has \(y\in k[z]\), so \(z\) commutes with \(y\). The elementary centralizer identity \(C_F(y)=k[y]\) then gives \(z\in k[y]\). Consequently
\[
C_F(g(y))=k[y].
\]
If \(m>0\), this contradicts the positive \(x\)-degree of \(u_m\). Therefore every element of \(\ker D_{f,g}\) belongs to \(k[y]\), and the reverse inclusion is immediate. This proves
\[
\ker D_{f,g}=k[y].
\]

Since \(\delta_f\) and \(T\) commute, \(T(f)=0\), and \(\delta_f^2(x)=0\), for every \(n\ge2\) one has
\[
D_{f,g}^n(x)=T^n(x)
=
\sum_{i=0}^{n}(-1)^i\binom ni g(y)^i x g(y)^{n-i}.
\]
If \(d=\deg g\ge1\) and \(a\) is the leading coefficient of \(g\), the highest total-degree part is
\[
a^n\sum_{i=0}^{n}(-1)^i\binom ni y^{di}xy^{d(n-i)}.
\]
The displayed words are pairwise distinct, so this is nonzero. Its degree is \(1+nd\), so the iterates of \(x\) are linearly independent across infinitely many degrees. Hence \(D_{f,g}\) is neither locally nilpotent nor locally finite. If \(g\) is scalar, the commutator term vanishes and \(D_{f,g}=\delta_f\); repeated application strictly lowers the number of \(x\)'s, so \(D_{f,g}\) is locally nilpotent. This proves the sharp boundary.

Now let \(g\) be nonconstant and let \(\rho\in\operatorname{Aut}_{D_{f,g}}(F)\). Since \(\rho\) preserves the kernel,
\[
\rho(k[y])=k[y],
\]
so
\[
\rho(y)=ay+b
\]
for some \(a\in k^\times\), \(b\in k\). The classical Czerniakiewicz--Makar-Limanov theorem identifies \(\operatorname{Aut}(k\langle x,y\rangle)\) with \(\operatorname{Aut}(k[x,y])\) under abelianization. In the polynomial plane, an automorphism whose second coordinate is \(ay+b\) must have first coordinate \(cx+h(y)\): its Jacobian is \(a\,\partial P/\partial x\), hence \(\partial P/\partial x\in k^\times\). The unique lift therefore has
\[
\rho(x)=cx+h(y),\qquad c\in k^\times,\ h\in k[y].
\]

Comparing \(D_{f,g}\rho(x)\) and \(\rho D_{f,g}(x)\) gives
\[
c f(y)+c[x,g(y)]
=
f(ay+b)+c[x,g(ay+b)].
\]
The \(x\)-degree-zero and \(x\)-degree-one parts must agree separately. Thus
\[
f(ay+b)=c f(y)
\]
and
\[
[x,g(ay+b)-g(y)]=0.
\]
A polynomial in \(y\) commuting with \(x\) is scalar, so the latter condition is exactly
\[
g(ay+b)-g(y)\in k.
\]
Conversely, these two identities make the displayed triangular automorphism commute with \(D_{f,g}\). This proves the isotropy formula.

## Residual affine symmetry

The infinite-dimensional part of the isotropy is exactly visible through the arbitrary parameter \(h\). The remaining affine symmetry can also be classified explicitly.

Assume \(d=\deg g\ge2\), write
\[
g(y)=g_dy^d+g_{d-1}y^{d-1}+\cdots,
\qquad
s=-\frac{g_{d-1}}{d g_d},
\]
and set
\[
G(z)=g(s+z)=\sum_{j=0}^d\alpha_jz^j,
\qquad
m_g=\gcd\{j\ge1:\alpha_j\ne0\}.
\]
Then
\[
\{ay+b:g(ay+b)-g(y)\in k\}
=
\{s+a(y-s):a^{m_g}=1\}.
\]
Indeed, the leading coefficient gives \(a^d=1\). Since the \(z^{d-1}\)-coefficient of \(G\) is zero, comparison of that coefficient forces the translated affine map to fix \(z=0\). The remaining condition is
\[
G(az)-G(z)\in k,
\]
which is equivalent to \(a^j=1\) for every positive exponent in the support of \(G\), hence to \(a^{m_g}=1\). In fact \(G(az)=G(z)\), so the constant difference is zero.

If \(f\ne0\), write
\[
f(s+z)=\sum_j\beta_jz^j
\]
and let
\[
n_f=\gcd\{|i-j|:\beta_i\beta_j\ne0\},
\]
with \(n_f=0\) when the support has at most one exponent. For \(a^{m_g}=1\), the equation \(f(s+az)=c f(s+z)\) holds exactly when all \(a^j\) on the support of \(f(s+z)\) are equal. Equivalently,
\[
a^{n_f}=1,
\]
and then \(c=a^{j_0}\) for any exponent \(j_0\) in the support. Hence the residual affine symmetry is cyclic of order dividing
\[
\gcd(m_g,n_f),
\]
with the convention \(\gcd(m,0)=m\). If \(f=0\), the scalar \(c\) is arbitrary and the residual group is \(\mu_{m_g}\times k^\times\).

For \(\deg g=1\), the condition on \(g\) instead forces \(a=1\), while translations \(y\mapsto y+b\) remain possible subject to \(f(y+b)=c f(y)\).

## Relation to abelianization

The induced derivation on the commutative quotient is simply
\[
\pi_*(D_{f,g})=f(y)\,\partial_x.
\]
Thus the two examples in arXiv:2609.19470v1 are the special cases
\[
(f,g)=(0,y)\quad\text{and}\quad(f,g)=(1,y).
\]
The family shows that the mechanism is stable under an arbitrary triangular locally nilpotent part \(f(y)\partial_x\): adding the commuting inner term \(-\operatorname{ad}_{g(y)}\) with nonconstant \(g\) destroys local nilpotence and local finiteness, while leaving every shear \(x\mapsto x+h(y)\) in the isotropy group.

## Limitations and originality boundary

Bergman's centralizer theorem, the Czerniakiewicz--Makar-Limanov automorphism theorem, and the triangulability of locally nilpotent derivations of the free associative plane are prior art and are used here as inputs. The new claim is limited to the exact kernel/local-nilpotence/isotropy description of the family \(D_{f,g}\), together with the residual affine-symmetry formula, to the best of our knowledge.

The source preprint arXiv:2609.19470v1 was inspected in full in the relevant free-associative-algebra section. Its Propositions 27 and 29 treat the two instances \((f,g)=(0,y)\) and \((1,y)\), but do not state the general family or the exact isotropy formula above. Targeted searches for the same family under inner-derivation, triangular-derivation, centralizer, and isotropy terminology did not locate an equivalent statement. Older literature on derivations and automorphisms of free associative algebras is broad, and a differently phrased equivalent result may have been missed; this is the principal residual originality risk.

## References

- R. Baltazar, S. Lopes, O. Morales, *A Characterization of Local Nilpotence for Derivations of Ore Extensions*, arXiv:2609.19470v1 (2026).
- G. M. Bergman, *Centralizers in free associative algebras*, Trans. Amer. Math. Soc. **137** (1969), 327--344. DOI: 10.1090/S0002-9947-1969-0236208-5.
- S. D. Crode, I. P. Shestakov, *Locally nilpotent derivations and automorphisms of free associative algebra with two generators*, Comm. Algebra **48** (2020), 3091--3098. DOI: 10.1080/00927872.2020.1729363.
- V. Drensky, L. Makar-Limanov, *Locally Nilpotent Derivations of Free Algebra of Rank Two*, SIGMA **15** (2019), 091. DOI: 10.3842/SIGMA.2019.091.

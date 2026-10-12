# The full \(\mathbb F_{s^2}\)-automorphism group of the one-point Hermitian-relative curve

## Finding
For every prime power \(s\ge2\) and \(q=s^2\), choose \(\eta\in\mathbb F_q\setminus\mathbb F_s\). The smooth projective plane curve
\[
 C_\eta:\quad x^{s+1}+\eta y^{s+1}+y^s z+yz^s=0
\]
has the following **full abstract automorphism group over \(\mathbb F_q\)**:
\[
\operatorname{Aut}_{\mathbb F_q}(C_\eta)
 =\{T_{u,v,w}:u\in\mathbb F_q^*,\ v,w\in\mathbb F_q,\ u^{s+1}=1,\ w^s+w=-v^{s+1}\},
\]
where
\[
T_{u,v,w}([x:y:z])=[ux+vy:y:z-uv^sx+wy].
\]
These are all distinct, and composition in this order obeys
\[
(u,v,w)(u',v',w')=(uu',\ uv'+v,\ w+w'-uv^sv').
\]
The group is \(H_s\rtimes\mu_{s+1}\), with \(|H_s|=s^3\), \(|Z(H_s)|=s\), \(H_s/Z(H_s)\cong(\mathbb F_q,+)\), and consequently
\[
\boxed{|\operatorname{Aut}_{\mathbb F_q}(C_\eta)|=s^3(s+1).}
\]
Moreover, \(H_s\) yields a Galois cover of degree \(s^3\) from \(C_\eta\) to \(\mathbb P^1\), branched at exactly one geometric point; in affine coordinates \(X=x/y\), \(Z=z/y\), the invariant map is \(X\mapsto X^q-X\).

## Assumptions and scope
The field is precisely \(\mathbb F_q\) with \(q=s^2\), including characteristic two, and \(\eta\notin\mathbb F_s\). The term automorphism refers to **abstract curve automorphisms defined over this field**, rather than just projective stabilizers or geometric automorphisms over an algebraic closure. Its genus is \(s(s-1)/2\); no assertion about semilinear transformations is included.

## Proof
**Unique rational point and canonical plane embedding.** For \([x:y:z]\in C_\eta(\mathbb F_q)\), the norm terms \(x^{s+1}\) and \(y^{s+1}\), and the trace term \(y^sz+yz^s\), lie in \(\mathbb F_s\). Since \(\eta\notin\mathbb F_s\), this forces \(y=0\), then \(x=0\); thus \(P=[0:0:1]\) is the unique rational point. The partial derivatives of the defining polynomial are \(x^s,\eta y^s+z^s,y^s\), respectively, and have no common projective zero, so the curve is smooth. Its tangent at \(P\) is \(y=0\), and restricting its equation to this line gives \(x^{s+1}=0\). Hence \(\mathcal O_C(1)\simeq\mathcal O_C((s+1)P)\).

Every \(\mathbb F_q\)-automorphism fixes \(P\) and therefore preserves this hyperplane bundle. For \(d=s+1\ge3\), the restriction map \(H^0(\mathbb P^2,\mathcal O(1))\to H^0(C,\mathcal O_C(1))\) is an isomorphism: use the restriction sequence \(0\to\mathcal O_{\mathbb P^2}(1-d)\to\mathcal O_{\mathbb P^2}(1)\to\mathcal O_C(1)\to0\), the standard vanishing \(H^1(\mathbb P^2,\mathcal O(k))=0\), and \(H^0(\mathbb P^2,\mathcal O(1-d))=0\). Thus *every abstract automorphism* extends uniquely to a projective linear transformation, also when \(s=2\) and the curve is elliptic.

**Coefficient comparison.** A projective transformation preserving \(P\) and its unique tangent has shape
\[
x'=ax+by,\qquad y'=dy,\qquad z'=cx+ey+fz,
\]
with \(a,d,f\ne0\), all coefficients in \(\mathbb F_q\). Because the defining polynomial is geometrically irreducible, preservation means \(F(x',y',z')=\lambda F(x,y,z)\) for a nonzero scalar \(\lambda\). Comparing the coefficients of \(x^{s+1}\), \(y^sz\), \(yz^s\), and \(y^{s+1}\) gives
\[
\lambda=a^{s+1}=d^sf=df^s,
\qquad
(\lambda-d^{s+1})\eta=b^{s+1}+d^se+de^s.
\]
The right side of the latter equality and both \(\lambda\) and \(d^{s+1}\) belong to \(\mathbb F_s\). Since \(\eta\notin\mathbb F_s\), \(\lambda=d^{s+1}\); then \(f=d\). Comparing \(xy^s\) gives \(ab^s+d^sc=0\) (the conjugate coefficient agrees automatically). Divide the matrix by \(d\) and put \(u=a/d\), \(v=b/d\), \(w=e/d\). These equations are *exactly*
\[
u^{s+1}=1,\qquad c/d=-uv^s,\qquad w^s+w=-v^{s+1}.
\]
Conversely, the same expansion verifies that every displayed \(T_{u,v,w}\) preserves \(F\). The formula for composition follows by multiplying the three-by-three matrices; the normalized middle diagonal entry is one, so the parameters are unique. The norm-one group has \(s+1\) elements, and for every \(v\in\mathbb F_q\) the field-trace equation for \(w\) has exactly \(s\) solutions. The total is \(s^3(s+1)\).

**Internal group and quotient.** The subgroup \(H_s\) given by \(u=1\) has order \(s^3\), and the matrices with \(v=w=0\) yield the complementary cyclic subgroup \(\mu_{s+1}\). Conjugation sends \((1,v,w)\) to \((1,uv,w)\). The commutator in \(H_s\) is the central trace-zero translation determined by \(v'^s v-v^s v'\). For each nonzero \(v\) there exists \(v'\) with \(v'/v\notin\mathbb F_s\); thus the center consists exactly of \((1,0,w)\) with \(w^s+w=0\), and has \(s\) elements. This establishes the claimed Heisenberg structure.

On \(y=1\), the function field relation is \(Z^s+Z=-(X^{s+1}+\eta)\). The central subgroup translates \(Z\) by the \(s\) trace-zero constants; its invariant field is \(\mathbb F_q(X)\), as the additive equation has degree \(s\) and these are \(s\) distinct deck transformations. The residual translations \(X\mapsto X+v\) have invariant field \(\mathbb F_q(X^q-X)\). Therefore the extension degree is \(s\cdot q=s^3\), with Galois group \(H_s\). No nonidentity element of \(H_s\) fixes an affine geometric point: nonzero \(v\) changes \(X\), and \(v=0\) forces a nonzero translation of \(Z\). All ramification is therefore at the sole point over infinity, namely \(P\), which is fixed by \(H_s\).

## Verification
Run `python3 verify.py` in a directory containing the supplied standalone script. It performs exact arithmetic in \(\mathbb F_4\), \(\mathbb F_9\), and \(\mathbb F_{25}\), checks uniqueness of rational points, polynomial preservation for all predicted matrices, the multiplication law, and exhaustive projective stabilizer enumerations in the first two fields. The expected terminal line is `VERIFY_OK`. Finite tests are not used to prove the universal statement; the preceding coefficient and linear-system arguments do that.

## Relationship to prior work
Homma and Kim's *Rational points and inflexions on Hermitian-relative curves* (2026), Theorem 7, determines the unique-rational-point model and its projective equivalence class, but does not state its full field-defined automorphism group or one-point wild Galois quotient. Their earlier *Relatives of the Hermitian curve* (2024 preprint) proves general geometric equivalence to the Hermitian curve, and outlines the congruence criterion for projective equivalence; these are not mistaken for new results here. Their conference chapter *Classification of Hermitian-Relative Curves up to Projective Equivalence* (first online 31 May 2026) classifies forms by projective equivalence, a neighboring problem; only its public abstract could be inspected. Its full text could conceivably contain or imply an equivalent stabilizer computation, so independent bibliographic confirmation of the specific group law remains warranted.

## Limitations
The answer is for \(\mathbb F_q\)-defined automorphisms and does not classify the much larger geometric automorphism group after extending constants. The Galois quotient is asserted only for the normal subgroup \(H_s\); the theorem does not determine its complete higher ramification filtration. The available preview of the 2026 conference chapter leaves residual priority uncertainty about an unstated but equivalent formula. Exact finite arithmetic checks corroborate, but do not certify, a theorem over every prime power.

## References
1. M. Homma and S. J. Kim, *Rational points and inflexions on Hermitian-relative curves*, arXiv:2610.09672v1, Theorem 7, 7 Oct 2026; https://arxiv.org/html/2610.09672v1.
2. M. Homma and S. J. Kim, *Relatives of the Hermitian curve*, arXiv:2402.14192v3, Section 2; https://arxiv.org/html/2402.14192v3.
3. M. Homma and S. J. Kim, *Classification of Hermitian-Relative Curves up to Projective Equivalence*, WAIFI 2026, LNCS 16611, pp. 95–110; first online 31 May 2026, doi:10.1007/978-3-032-27574-5_7; https://link.springer.com/chapter/10.1007/978-3-032-27574-5_7.

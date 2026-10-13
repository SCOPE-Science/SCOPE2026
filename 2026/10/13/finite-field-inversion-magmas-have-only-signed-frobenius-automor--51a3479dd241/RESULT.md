# Finite-field inversion magmas have only signed Frobenius automorphisms

## Finding
Let \(K=\mathbb F_{p^f}\) be any finite field of order \(q=p^f\). Let \(\iota:K\to K\) fix zero and invert nonzero elements:
\[\iota(0)=0,\qquad\iota(t)=t^{-1}\quad(t\ne0).\]
On the pointed set \((K,0)\), form the magma
\[x\star y=\iota(y-x)-\iota(-x)=\iota(y-x)+\iota(x).\]
Then every pointed-magma automorphism, and no other permutation, is
\[F(t)=c\,t^{p^j},\quad 0\le j<f,\quad c\in K^\times,\quad c^2=1.\]
Consequently
\[\operatorname{Aut}(K,\star,0)\cong
\begin{cases}C_2\times C_f,&p\ne2,\\C_f,&p=2.\end{cases}\]
All the described automorphisms are additive, so their own translation socles are the full field, as anticipated by the mutual-automorphism conjecture of [1]. The translation-additivity socle of the inversion permutation is
\[S_{\iota}=\{u\in K:\iota(t+u)=\iota(t)+\iota(u)\text{ for every }t\in K\}
=\begin{cases}K,&q\in\{2,3,4\},\\\{0\},&q\ge5.\end{cases}\]

## Assumptions and scope
All fields are finite, including non-prime fields and characteristic two. Automorphisms must preserve the displayed binary operation and the point zero. No assumption that \(\iota\) is a magma automorphism or that this magma is a cycle set is made. In fact for \(q\ge5\), \(\iota\) is not a magma automorphism by the classification. The original zero-fixing-permutation construction is due to Byott and Jasko [1]. Their conjecture concerning *mutual* magma automorphisms holds for this specific family because every such automorphism has full additive socle; the conjecture in general is not resolved here.

## Proof
**1. Collision fibers.** Fix \(y\ne0\), and consider \(P_y(x)=x\star y\). For \(x=0\) or \(x=y\), the value is \(y^{-1}\). For \(x\notin\{0,y\}\), direct arithmetic gives
\[P_y(x)=\frac{y}{x(y-x)}.\]
Two interior arguments have the same value precisely when they are equal or add to \(y\). Interior values collide with the boundary value \(y^{-1}\) only if \(r=x/y\) satisfies \(r(1-r)=1\). Put
\[B=\{r\in K:r(1-r)=1\};\qquad |B|\le2,\quad0,1\notin B.\]
If \(x\notin\{0,y\}\) and \(x/y\notin B\), its complete fiber is exactly \(\{x,y-x\}\), with a singleton only in odd characteristic when \(x=y/2\).

**2. Recovering partial subtraction.** Let \(F\) be a pointed-magma automorphism. It maps the fibers of \(P_y\) bijectively to those of \(P_{F(y)}\). A good two-element interior fiber must map to a two-element interior fiber and is therefore paired by subtraction from \(F(y)\). A good singleton fiber must map to the unique interior singleton, namely the midpoint when it exists. The boundary cases \(x=0,y\) are immediate. Thus, for every \(y\ne0\),
\[x/y\notin B\quad\Longrightarrow\quad F(y-x)=F(y)-F(x).\tag{1}\]

**3. Negation.** For \(x\ne0\), choose \(y\notin\{0,x\}\) with \(x/y\notin B\) and \(y/(y-x)\notin B\). Each root of \(B\) excludes at most one \(y\) for each of the latter two requirements. Therefore at most \(2+2|B|\le6\) choices are forbidden, so a choice exists when \(q\ge7\). For \(q=5\), the polynomial defining \(B\) has no root, and a choice again exists. Apply (1) first to \((y,x)\) and then to \((y-x,y)\); this gives
\[F(-x)=F(y-x)-F(y)=-F(x).\tag{2}\]
The same equality holds at zero.

**4. Additivity.** For arbitrary nonzero \(u,v\), seek a \(z\in K\) such that (1) applies to the ordered pairs
\[(v,z),\qquad(u,v-z),\qquad(u-v+z,z).\]
For each \(b\in B\), the first and second pairs each exclude at most one \(z\); for the third, the bad-ratio equation \(z/(u-v+z)=b\) is linear in \(z\) because \(b\ne1\), so again excludes at most one \(z\). A pair with zero first entry already satisfies the desired identity by (2). Altogether at most \(3|B|\le6\) values are forbidden. For \(q\ge7\) some \(z\) works, and chaining the three identities yields
\[F(u-v)=F(u-v+z)-F(z)=F(u)-F(v-z)-F(z)=F(u)-F(v).\]
For \(q=5\), \(B\) is empty and (1) already gives the same identity. Together with (2), this proves additivity for \(q\ge5\).

For \(q=2,3,4\), inversion is additive: it is the identity for the first two fields and the Frobenius square for \(\mathbb F_4\). Then \(x\star y=\iota(y)\), so pointed-magma automorphisms are the permutations fixing zero and commuting with \(\iota\). They are respectively the identity, the two permutations of the two nonzero elements, and the identity or Frobenius involution. In every case these are additive and have the prescribed form.

**5. Recovering multiplication.** Since \(0\star y=\iota(y)\), every automorphism satisfies \(F\circ\iota=\iota\circ F\). Put \(c=F(1)\). It follows that \(c=c^{-1}\), hence \(c^2=1\). Then \(G=cF\) is additive, preserves inversion and fixes one. For nonzero \(x,y\) with \(xy\ne1\), Hua's elementary identity [2] reads
\[x^2y=x-\left(x^{-1}+\left(y^{-1}-x\right)^{-1}\right)^{-1}.\]
Applying \(G\) therefore gives \(G(x^2y)=G(x)^2G(y)\). For fixed \(x\ne0\), the discrepancy as a function of \(y\) is additive, vanishes at zero and every nonzero \(y\ne x^{-1}\), and also vanishes at the omitted point because that point is a sum of two admissible nonzero elements (\(q\ge5\)). Hence
\[G(x^2y)=G(x)^2G(y)\quad\text{for all }x,y\in K.\]
If the characteristic is two, every field element is a square, yielding multiplicativity immediately. Otherwise polarization, \(2ab=(a+b)^2-a^2-b^2\), yields multiplicativity. Thus \(G\) is a field automorphism, necessarily \(G(t)=t^{p^j}\) for some \(0\le j<f\). The small fields were treated directly. Conversely each map \(t\mapsto c t^{p^j}\) with \(c^2=1\) is additive, commutes with inversion, and preserves the displayed magma operation. This proves the automorphism classification.

**6. The socle.** In fields of orders two, three and four, inversion is additive, so the socle is the whole field. For odd characteristic different from three, if \(u\ne0\) were a translation-additivity direction, substituting \(t=u\) would yield \((2u)^{-1}=2u^{-1}\), hence \(4=1\), impossible. For characteristic three with \(q\ge9\), take \(t=\alpha u\) for \(\alpha\notin\mathbb F_3\); the same identity would require \(\alpha^2+\alpha+1=0\), whereas that polynomial is \((\alpha-1)^2\) in characteristic three. In characteristic two with \(q\ge8\), the identical calculation would require \(\alpha^2+\alpha+1=0\) for each \(\alpha\notin\{0,1\}\), impossible as the polynomial has at most two roots and there are at least six choices. Therefore the socle is trivial for all \(q\ge5\).

## Verification
The standalone standard-library `verify.py` constructs fields of orders \(2,3,4,5,7,8,9,16\) by explicit irreducible polynomial reductions. It checks field inverses; enumerates *all pointed permutations* for orders up to nine and compares the exact automorphism sets; checks the predicted automorphisms by every magma-product pair through order sixteen; computes every translation-socle membership; checks collision fibers; and verifies that the three-pair additive-repair witness exists for every nonzero ordered pair through order sixteen. It returns `VERIFY_OK` when these checks pass. The finite checks are consistency tests only; the proof above handles all prime powers.

## Relationship to prior work
Byott and Jasko [1, equation (1.6)] introduced the pointed magma construction. Their Proposition 2.5 proves that any magma automorphism commutes with the distinguished permutation, and Proposition 2.6 describes the case when that permutation is already additive. Their Theorem 3.2 **already covers the prime-field order-five inversion instance**: inversion on \(\mathbb F_5\) is the transposition of the two inverse pairs that differ from their own inverses. Section 6 uses finite searches for more general permutations. The present claim is the **all-prime-power inversion subclass**, including arbitrarily large non-prime fields and infinitely many genuinely nonadditive inversion permutations; the reconstruction of addition from operation fibers and the exact uniform group structure are not conclusions of the cited propositions or transposition theorem. Hua's identity [2] is classical, and is used only after additivity has been proved from the magma structure.

## Limitations
The statement does not classify other permutations \(\tau\), prove the general automorphism conjecture of [1], or assert that \(\iota\) produces a cycle set when its socle is trivial. The exact order-five prime-field case is known from [1], and exhaustive computations in [1] cover finite ranges; neither is claimed as new. A possible equivalent older result formulated as an inversion-difference functional equation or algebraic-incidence automorphism theorem is a residual historical risk. The numerical verifier does not replace the arbitrary-field argument.

## References
[1] Nigel P. Byott and Edgar Jasko, *Magma Automorphisms and Quasi-Linear Cycle Sets*, arXiv:2609.20028v1, first public September 17, 2026. https://arxiv.org/pdf/2609.20028 .

[2] Loo-Keng Hua, *On the Automorphisms of a Sfield*, Proceedings of the National Academy of Sciences 35 (1949), 386–389, DOI:10.1073/pnas.35.7.386. The identity used here is verified directly by field arithmetic.

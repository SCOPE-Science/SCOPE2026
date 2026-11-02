# Modular idempotents in scalar Alexander quandle algebras

## Finding

Let \(p\ge5\) be prime, \(q=p^f\) with \(f\ge1\), \(d\ge1\), and \(\lambda\in\mathbb F_p\setminus\{0,1\}\). Put \(\mu=1-\lambda\) and define the latin Alexander quandle \(Q_{p,d,\lambda}\) on \(V=\mathbb F_p^d\) by
\[
 v\star w=\lambda v+\mu w.
\]
Its quandle algebra \(A=\mathbb F_q[Q_{p,d,\lambda}]\) has basis \(e_v\) and bilinear product \(e_v\star e_w=e_{\lambda v+\mu w}\). Define the set of residues
\[
 S_{p,\lambda}=\{j\in\{1,\ldots,p-2\}:\lambda^j+\mu^j=1\text{ in }\mathbb F_p\},\qquad
 r_{p,\lambda}=|S_{p,\lambda}|,
\]
and put \(L=(p^d-1)/(p-1)\). Then **the exact total number of idempotents, including zero**, is
\[
 \boxed{|\operatorname{Idem}(A)|=1+q^{Lr_{p,\lambda}}.}
\]

There is also an intrinsic complete structural description. Identify the underlying vector space of \(A\) with the *ordinary associative* group algebra \(R=\mathbb F_q[V]\), whose multiplication will be denoted by juxtaposition. Let \(J=\ker\varepsilon\), where \(\varepsilon\) is coefficient-sum augmentation. Set \(U=1+J\), an abelian multiplicative group. For \(a\in\mathbb F_p^\times\), let \(T_a:R\to R\) be the group-algebra automorphism \(T_a(e_v)=e_{av}\), and for \(0\le j\le p-2\) define
\[
 U_j=\{u\in U:T_a(u)=u^{a^j}\text{ for all }a\in\mathbb F_p^\times\}.
\]
The exponent on the right is interpreted modulo \(p\), using the ordinary group-algebra multiplication. Then the nonzero idempotents are exactly
\[
 \boxed{H=\prod_{j\in S_{p,\lambda}}U_j,}
\]
where the product is an internal direct product in \(U\). Every \(U_j\) is an elementary abelian \(p\)-group of order \(q^L\), and the direct-product decomposition is canonical. The nonzero idempotents are closed under \(\star\); as a quandle they are noncanonically isomorphic to
\[
 \boxed{\prod_{j\in S_{p,\lambda}}
 \operatorname{Alex}(\mathbb F_q^L,\lambda^j),}
\]
where the factor indexed by \(j\) has operation \(x\star_j y=\lambda^j x+\mu^j y\). This is a product of latin Alexander quandles, because both scalars are nonzero and sum to one.

For \(p=5\), \(S_{5,\lambda}=\{1\}\) for all three admissible scalars. For \(p=7\), \(r_{7,2}=r_{7,6}=1\), while \(r_{7,3}=r_{7,4}=r_{7,5}=2\). Thus, over \(\mathbb F_7\) with \(d=1\), parameters \(\lambda=2\) and \(\lambda=4\) give exactly \(8\) and \(50\) idempotents, respectively. The latter has \(42\) non-basis nonzero idempotents, while the former has none. The difference persists and grows with \(d\).

## Assumptions and scope

The coefficient field is exactly \(\mathbb F_q\) with characteristic \(p\) and \(q=p^f\). The underlying additive group is \(\mathbb F_p^d\), not \(\mathbb F_q^d\), and \(\lambda,\mu\) lie in the prime subfield. The ring \(R\) is commutative and associative under ordinary group-algebra multiplication; the quandle multiplication \(\star\) is generally nonassociative. An idempotent means \(u\star u=u\). The symbol \(1\) denotes the ordinary group-algebra identity \(e_0\), not a unit asserted for the quandle multiplication. All cardinalities and isomorphisms above hold for every integer \(f,d\ge1\) and every admissible scalar.

## Proof

**Step 1: transport and exclusion of augmentation-zero idempotents.** For basis elements,
\[
 e_v\star e_w=e_{\lambda v+\mu w}=T_\lambda(e_v)T_\mu(e_w).
\]
By bilinearity, \(u\star w=T_\lambda(u)T_\mu(w)\) for all \(u,w\in R\). The augmentation map obeys \(\varepsilon(u\star w)=\varepsilon(u)\varepsilon(w)\). If \(u\star u=u\), its augmentation is therefore either zero or one. Because \(V\) is elementary abelian of exponent \(p\), with \(x_i=e_{v_i}-1\) for a vector-space basis \((v_i)\), there is an isomorphism of ordinary rings
\[
 R\cong \mathbb F_q[x_1,\ldots,x_d]/(x_1^p,\ldots,x_d^p).
\]
In particular \(J^{d(p-1)+1}=0\). If \(u\in J\) satisfies \(u=T_\lambda(u)T_\mu(u)\), then \(u\in J^2\). Applying the same argument inductively yields \(u\in J^{2^k}\) for every \(k\), hence \(u=0\). Every nonzero idempotent therefore belongs to \(U=1+J\), and conversely each element of \(U\) satisfying \(T_\lambda(u)T_\mu(u)=u\) is a nonzero idempotent.

**Step 2: the prime-field scalar action on the ordinary unit group.** Since \(R\) is commutative of characteristic \(p\), every \(z\in J\) satisfies \(z^p=0\): express \(z\) as a linear combination of \(e_v-1\), and use \((e_v-1)^p=e_{pv}-1=0\) and the Frobenius identity. Therefore \((1+z)^p=1\). The ordinary multiplicative group \(U\) is abelian of exponent \(p\), hence an \(\mathbb F_p\)-vector space, using multiplication as vector addition and ordinary integer powers as scalar multiplication. It has order \(q^{p^d-1}\).

The cyclic group \(C=\mathbb F_p^\times\) acts on \(U\) by \(T_a\). Write \(U^{(k)}=1+J^k\). These are \(C\)-stable subgroups and, for \(k\ge1\),
\[
 U^{(k)}/U^{(k+1)}\cong J^k/J^{k+1}
\]
\(C\)-equivariantly, via \(1+z\mapsto z\), because \(J^{2k}\subseteq J^{k+1}\). As \(|C|=p-1\) is invertible in \(\mathbb F_p\), Maschke's theorem splits each short exact sequence of \(\mathbb F_p[C]\)-modules. The \(C\)-module \(U\) is consequently isomorphic (noncanonically) to the additive \(C\)-module \(J\): the two have the same equivariant associated graded pieces.

A basis of \(J\) over \(\mathbb F_q\) is \(\{e_v-1:v\in V\setminus\{0\}\}\). The action \(T_a\) permutes this basis freely in orbits of length \(p-1\); these orbits correspond to the \(L=(p^d-1)/(p-1)\) projective lines in \(V\). As an \(\mathbb F_p[C]\)-module, \(J\) is therefore the direct sum of \(fL\) copies of the regular representation \(\mathbb F_p[C]\). All its characters \(a\mapsto a^j\), for \(0\le j\le p-2\), occur with multiplicity exactly \(fL\). Since all \((p-1)\)-st roots of unity lie in \(\mathbb F_p\), the representation is split. Consequently,
\[
 U=\prod_{j=0}^{p-2} U_j,
 \qquad |U_j|=p^{fL}=q^L,
\]
where \(U_j\) is exactly the simultaneous eigenspace defined in the finding. The decomposition is an internal direct product in the multiplicative notation for the \(\mathbb F_p\)-vector space \(U\).

**Step 3: solve the idempotence equation without losing branches.** Write uniquely \(u=\prod_j u_j\), with \(u_j\in U_j\). The transported identity becomes
\[
 T_\lambda(u)T_\mu(u)=\prod_j u_j^{\lambda^j+\mu^j}.
\]
The equality with \(u\) holds if and only if \(u_j^{\lambda^j+\mu^j-1}=1\) for every \(j\). As each \(U_j\) has exponent \(p\), a nonzero coefficient \(\lambda^j+\mu^j-1\) forces \(u_j=1\), while a zero coefficient imposes no restriction. At \(j=0\) this coefficient is \(1\), so that eigenspace never contributes. Exactly the residues \(S_{p,\lambda}\) remain. This proves \(H=\prod_{j\in S_{p,\lambda}}U_j\), its cardinality \(q^{Lr_{p,\lambda}}\), and the displayed total count after adjoining the zero idempotent.

**Step 4: determine the induced quandle.** Each \(T_a\) preserves every \(U_j\). For \(u_j,v_j\in U_j\), their quandle product in \(R\) is
\[
 u_j\star v_j=u_j^{\lambda^j}v_j^{\mu^j}.
\]
The contributing residues satisfy \(\lambda^j+\mu^j=1\) and both scalars are nonzero. Identifying the elementary abelian group \(U_j\) with the additive group of \(\mathbb F_q^L\) transforms this product into \(x\star_j y=\lambda^j x+\mu^j y\). The factors are independent and closed; hence \(H\) is precisely the stated product Alexander quandle. No assertion is made that the disjoint zero idempotent belongs to this quandle.

**Step 5: small-prime corollaries.** Direct modular exponentiation for \(j\in\{1,\ldots,p-2\}\) gives \(S_{5,\lambda}=\{1\}\) for all admissible \(\lambda\), and \(S_{7,2}=S_{7,6}=\{1\}\), \(S_{7,3}=S_{7,5}=\{1,5\}\), \(S_{7,4}=\{1,4\}\). Substitution establishes the numerical examples. The equation \(j=1\) always contributes because \(\lambda+\mu=1\); no empty-product anomaly occurs.

## Verification

Run `python verify_modular_alexander.py` with Python 3 and NumPy. The checker directly enumerates all \(p^p\) coefficient vectors of the one-dimensional quandle algebra for \(p=5\) and \(p=7\), separately for every admissible scalar. It computes all products by the definition \(e_v\star e_w=e_{\lambda v+\mu w}\), not by the group-algebra eigenspace construction. It independently forms and row-reduces \(T_\lambda+T_\mu-I\) on the *additive* augmentation ideal for selected rank-two examples over \(p=5,7,11\), and verifies closure of all nonzero idempotents under the quandle product for \(p=7\) at parameters \(2\) and \(4\).

The recorded run ended `VERIFY_OK`. In particular, the \(p=7,d=1\) exhaustive counts are \(8,50,50,50,8\) for \(\lambda=2,3,4,5,6\). The dimension-two modular kernel checks agree with the formula, including dimension \(16\) at \(p=7,\lambda=4\). The finite tests are not an all-parameter proof: the preceding argument covers every specified parameter.

## Relationship to prior work

Zhi-Lin Zhang, *Group-ring methods for Alexander quandle rings*, arXiv:2610.08204 (first posted 2026-10-06), gives the transported Alexander product and studies augmentation powers, commutators, integral idempotents and complex Peirce spectra. Its transport formula is used here; its statements do not directly provide the complete positive-characteristic finite-field idempotent count, the character multiplicities of augmentation-one units, or their resulting quandle decomposition. Elhamdadi, Ta and Virgin, *Fourier Analysis and Idempotents in Quandle Algebras*, arXiv:2609.03799 (2026-09-03), principally treats integral and complex coefficient settings. Churchill et al., *A further study of quandles and quandle rings*, arXiv:2608.09149 (2026-08-10), studies several integral idempotent systems and particular small examples, not this general scalar finite-field classification.

The previously studied characteristic-three \(R_3\) case is outside the stated \(p\ge5\) scope and is not claimed as new. The new arithmetic phenomenon at \(p=7\), including the distinction between scalar parameters producing only basis idempotents and those producing additional ones, is not implied by the cited integral classifications. The cited transport identity is acknowledged as previously established.

## Limitations

Only elementary abelian underlying groups of prime-field vector dimension \(d\) and scalar Alexander automorphisms with \(\lambda,1-\lambda\ne0\) are classified. The theorem does not extend as stated to arbitrary linear automorphisms, non-elementary abelian groups, coefficient fields of different characteristic, or positive-characteristic coefficient rings that are not fields. The internal direct product of eigenspaces is canonical, but its identification with coordinate vector spaces is not. No claim of independent mathematical validation or absolute historical priority is made; an undiscovered older modular group-ring treatment could contain an equivalent statement.

## References

1. Zhi-Lin Zhang, *Group-ring methods for Alexander quandle rings*, arXiv:2610.08204, initial submission 2026-10-06, https://arxiv.org/abs/2610.08204.
2. Mohamed Elhamdadi, Luc Ta, Bryce Virgin, *Fourier Analysis and Idempotents in Quandle Algebras*, arXiv:2609.03799, initial submission 2026-09-03, https://arxiv.org/abs/2609.03799.
3. Gregory Churchill, Indu Rasika Churchill, Neranga Fernando, Bhitali Kousik, *A further study of quandles and quandle rings*, arXiv:2608.09149, initial submission 2026-08-10, https://arxiv.org/abs/2608.09149.
4. V. G. Bardakov, I. B. S. Passi, M. Singh, *Zero-divisors and idempotents in quandle rings*, arXiv:2001.06843 (2020), https://arxiv.org/abs/2001.06843.

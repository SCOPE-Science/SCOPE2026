# A left-regular band of group retractions in irreducible scalar Frobenius groups

## Finding
Let \(q=p^d\), \(m>1\) divide \(q-1\), and assume that \(\operatorname{ord}_m(p)=d\). Let \(G=(\mathbb F_q,+)\rtimes\langle\alpha\rangle\), where \(\alpha\in\mathbb F_q^\times\) has order \(m\) and acts by scalar multiplication. Write \(m=\prod_{i=1}^{r}\ell_i^{a_i}\), where the primes \(\ell_i\) are distinct. For \(S\subseteq\{1,\ldots,r\}\), let \(e_S\in\mathbb Z/m\mathbb Z\) be \(1\) modulo \(\ell_i^{a_i}\) for \(i\in S\) and \(0\) otherwise. For nonempty \(S\) and \(t\in\mathbb F_q\), set
\[
R_{S,t}(v,\alpha^j)=\bigl(t(1-\alpha^{je_S}),\,\alpha^{je_S}\bigr).
\]
Every composition-idempotent endomorphism of \(G\) is exactly one of the distinct maps \(0_G\), \(\mathrm{id}_G\), or \(R_{S,t}\), where \(S\ne\varnothing\) and \(t\in\mathbb F_q\). Here \(0_G\) is the trivial group endomorphism, not the zero element of \(G\). Their composition law is
\[
R_{S,t}\circ R_{T,u}=R_{S\cap T,t},
\]
interpreting \(R_{\varnothing,t}=0_G\); \(0_G\) is absorbing and \(\mathrm{id}_G\) is the identity of the composition semigroup. Thus the idempotent endomorphisms themselves form a **left-regular band**, satisfying \(F^2=F\) and \(FGF=FG\) for all members \(F,G\). The band has \(2+q(2^r-1)\) elements, and its isomorphism type depends only on \((q,r)\).

Each \(R_{S,t}\) has image order \(m_S=\prod_{i\in S}\ell_i^{a_i}\). Thus the image-order enumerator is
\[
Z_G(z)=z^{qm}+z+q\sum_{\varnothing\ne S\subseteq\{1,\ldots,r\}}z^{m_S}.
\]
Distinct nonuniversal retractions \(R_{S,t}\) and \(R_{T,u}\) commute exactly when \(S\cap T=\varnothing\) or \(t=u\). Consequently the centralizer of \(R_{S,t}\) **within this band**, for \(|S|=s\ge1\), has cardinality
\[
2+2^r-q+(q-1)2^{r-s}.
\]
The number of ordered commuting pairs in the band is
\[
\boxed{4+4q(2^r-1)+q^2(3^r-2^{r+1}+1)+q(4^r-3^r).}
\]
In particular, this count is \(4+5q\) when \(r=1\), and \(4+19q+2q^2\) when \(r=2\).

## Assumptions and scope
All endomorphisms are group homomorphisms from the specified finite semidirect product to itself; **idempotent** always means under functional composition. The action assumption \(\operatorname{ord}_m(p)=d\) is essential: it makes the nonzero scalar \(\alpha\) act irreducibly on the \(d\)-dimensional \(\mathbb F_p\)-space \(V=(\mathbb F_q,+)\). All indices \(j\) are taken modulo \(m\), and powers \(\alpha^{je_S}\) are therefore unambiguous. The theorem covers every prime power \(q\) and every nontrivial cyclic scalar complement satisfying this irreducibility condition. It does not claim the same band structure for reducible actions, noncyclic complements or all finite groups.

## Proof
**Step 1: restriction to the Frobenius kernel.** The subgroup \(V\) is the unique Sylow \(p\)-subgroup of \(G\) and hence is mapped into itself by every group endomorphism \(F\). The kernel of \(F|_V\) is an \(\langle\alpha\rangle\)-invariant \(\mathbb F_p\)-subspace. Irreducibility implies either \(F(V)=0\) or \(F|_V\) is injective, hence bijective.

**Step 2: the nonzero restriction.** In the second case, the endomorphism induced on \(G/V\cong C_m\) must be injective. Indeed, if a nontrivial \(h\in C_m\) maps to the identity modulo \(V\), its image lies in abelian \(V\) and therefore conjugates \(F(V)=V\) trivially. Since \(F|_V\) is injective, the original \(h\) would conjugate all of \(V\) trivially, contradicting the faithful scalar action. Thus the induced map is an automorphism, and \(F\) is an automorphism. A composition-idempotent automorphism is the identity.

**Step 3: the zero restriction.** If \(F(V)=0\), then \(F\) factors through \(C_m\) and is determined by the image \(F(0,\alpha)=(w,\alpha^a)\), whose order divides \(m\). When \(\alpha^a=1\), this forces \(w=0\), since \(\gcd(m,p)=1\). Otherwise \(1-\alpha^a\ne0\), giving a unique \(t=w/(1-\alpha^a)\in\mathbb F_q\). Taking powers yields
\[
F(v,\alpha^j)=\bigl(t(1-\alpha^{ja}),\,\alpha^{ja}\bigr).
\]
Conversely each such expression is a group endomorphism, since it is the quotient map \(G\to C_m\), followed by the power map \(h\mapsto h^a\), followed by conjugation of the standard complement by \((t,1)\). Composition gives \(R_{a,t}R_{b,u}=R_{ab,t}\) when the product power map is nontrivial, and gives \(0_G\) otherwise. Hence \(F^2=F\) precisely when \(a^2\equiv a\pmod m\). By the Chinese remainder theorem this occurs exactly at the \(2^r\) residues \(e_S\). For \(S=\varnothing\), all \(t\) represent the same trivial map; every nonempty \(S\) gives exactly \(q\) distinct maps, distinguishable by the image of \((0,\alpha)\). The identity from Step 2 is distinct from all of them.

**Step 4: semigroup and rank invariants.** For all nonempty subsets, direct substitution gives
\[
R_{S,t}R_{T,u}=R_{S\cap T,t}.
\]
A second multiplication on the right by \(R_{S,t}\) changes neither the intersection nor the left-hand label, so \(FGF=FG\). The image is the conjugate of the unique subgroup of the complement of order \(m_S\). The trivial map has image size \(1\), and the identity has image size \(qm\), giving \(Z_G(z)\). Two nonuniversal maps commute if the intersection is empty or their left-hand labels agree. For a fixed support \(S\) of size \(s\), there are \(2^{r-s}-1\) nonempty disjoint supports and \(2^r-2^{r-s}\) intersecting supports, so the band centralizer size is \(2+q(2^{r-s}-1)+(2^r-2^{r-s})\). Finally, the number of ordered pairs of **nonempty** disjoint supports is \(3^r-2^{r+1}+1\), and of intersecting supports is \(4^r-3^r\). Such pairs contribute \(q^2\) and \(q\) label choices, respectively. The two universal maps contribute \(4+4q(2^r-1)\) additional ordered pairs. Summing proves the commuting-pair formula.

## Verification
The standalone `verify.py` constructs \(G\) as finite-field element pairs, enumerates all homomorphisms through independently tested group-presentation relations, and identifies composition-idempotent ones by their generator images. It then checks the exact band size, closure, \(FGF=FG\), each band centralizer size and all ordered commuting-pair counts. Eleven cases include \(q\in\{3,4,5,7,8,9,11,13\}\), single- and two-prime complement support patterns, and extension degrees greater than one. Execution result: `ALL_EXACT_CHECKS_PASSED`. These finite tests support but do **not** substitute for the general proof above.

## Relationship to prior work
McCarron's *Frobenius Groups with Perfect Order Classes* (2021) analyzes order distributions in Frobenius groups, not the composition semigroup of their retractions. Chebolu and Lockridge's *Fuchs' problem for endomorphisms of nonabelian groups* (2024) uses retracts and studies liftability of group endomorphisms to ring endomorphisms; its group retract definition and normal-complement criterion are prior groundwork. Neither inspected account presents this explicit two-parameter left-regular band, its image-order enumerator or its commuting-pair census. General semigroup identities and the Chinese remainder theorem are prior knowledge; only their complete realization here is assessed. Published results on group-codegree profiles, Engel graphs and subgroup commutativity of the same or related Frobenius groups investigate different invariants, and their stated results do not imply the formula here.

## Limitations
This classification uses irreducibility and faithful scalar action critically and is not extended to reducible representations or arbitrary Frobenius groups. Its originality assessment is bounded by the indexed and accessible publications inspected: no absolute uniqueness claim is made, and older or unindexed group-endomorphism semigroup literature could contain an equivalent result. Independent mathematical audit has not been performed.

## References
1. James McCarron, *Frobenius Groups with Perfect Order Classes*, arXiv:2103.00425, first public version 2021-02-28, https://arxiv.org/abs/2103.00425.
2. Sunil K. Chebolu and Keir Lockridge, *Fuchs' problem for endomorphisms of nonabelian groups*, arXiv:2408.08195, first public version 2024-08-15, https://arxiv.org/abs/2408.08195.

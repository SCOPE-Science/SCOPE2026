# Commuting Lie retractions: a rational-canonical joint-rank census

## Finding

Let \(K=\mathbb F_q\), let \(V\) be a nonzero finite-dimensional \(K\)-vector space, and let \(N\in\operatorname{GL}_K(V)\). Set \(L=Kt\oplus V\) with alternating Lie bracket \([t,v]=Nv\), \([V,V]=0\), and define a **retraction** to mean an idempotent Lie algebra endomorphism \(F:L\to L\), that is, \(F^2=F\). Two retractions **commute** when their linear compositions commute.

The theorem below determines the complete bivariate rank enumerator
\[\mathcal C_M(U,W)=\sum_{\substack{F,G\in\operatorname{End}_{\rm Lie}(L)\\F^2=F,\ G^2=G,\ FG=GF}}U^{\operatorname{rank}_K F}W^{\operatorname{rank}_K G}\]
from the rational-canonical multiplicities of \(N\), for every prime power \(q\). It counts embedded endomorphisms, not isomorphism orbits. Its zero-map terms are included.

Regard \(M=V\) as a \(K[X]\)-module with \(Xv=Nv\), and let \(d(A)=\dim_K A\) and \(a(A)=|\operatorname{Aut}_{K[X]}(A)|\), also for the zero module (where \(a(0)=1\)). All decomposition sums below are over **tuples of isomorphism classes** of direct summands, not over actual embedded decompositions. Equivalently, distribute each rational-canonical block multiplicity among the labeled components, using all nonnegative possibilities.

Define the one-variable retraction-rank polynomial
\[\mathcal E_M(Z)=1+\sum_{M\simeq A\oplus B}\frac{a(M)}{a(A)a(B)}q^{d(B)}Z^{1+d(A)}.\]
The first component \(A\) is the image of the module projection, and \(B\) is its kernel. Then the complete joint enumerator is
\[\boxed{\mathcal C_M(U,W)=\mathcal E_M(U)+\mathcal E_M(W)-1+\sum_{M\simeq M_{00}\oplus M_{01}\oplus M_{10}\oplus M_{11}}\frac{a(M)}{a(M_{00})a(M_{01})a(M_{10})a(M_{11})}\ q^{d(M)-d(M_{11})}\ U^{1+d(M_{10})+d(M_{11})}W^{1+d(M_{01})+d(M_{11})}.}\]

All the coefficients are explicit integers. Decompose \(M\) into primary modules \(K[X]/(f^j)\) for monic irreducible \(f\in K[X]\), with multiplicities \(m_{f,j}\) and necessarily \(f(0)\ne0\). Put \(Q_f=q^{\deg f}\) and \(s_{f,i}=\sum_{j\ge i}m_{f,j}\). Then
\[\boxed{a(M)=\prod_f Q_f^{\sum_{i\ge1}s_{f,i}^{2}}\prod_{j\ge1}\prod_{h=1}^{m_{f,j}}(1-Q_f^{-h}).}\]
Despite the rational-looking factors, this is the integer order of a finite automorphism group.

**Squarefree corollary.** If the characteristic polynomial of \(N\) is squarefree and its distinct irreducible factors have degrees \(d_1,\ldots,d_s\), then
\[\#\{F:F^2=F\}=1+\prod_{i=1}^{s}(1+q^{d_i}),\]
\[\#\{(F,G):F^2=F,\ G^2=G,\ FG=GF\}=1+2\prod_{i=1}^{s}(1+q^{d_i})+\prod_{i=1}^{s}(1+3q^{d_i}).\]
In particular, for a single irreducible factor of degree \(d\), the two counts are \(q^d+2\) and \(5q^d+4\), respectively. The number of noncommuting ordered retraction pairs is then \(q^{2d}-q^d\), even though *all* idempotent module endomorphisms commute. This isolates an affine obstruction invisible to the induced linear module projections.

## Assumptions and scope

All fields are finite of prime-power order. The operator \(N\) is arbitrary **invertible**, not necessarily semisimple, cyclic, diagonalizable, or of a fixed Jordan shape. The Lie algebra is nonabelian because \(V\ne0\) and \(N\) is invertible. All maps are \(K\)-linear Lie endomorphisms. The distinction between zero retractions and those inducing coefficient one on \(t\) is essential. The assertions concern rank over the base field \(K\), not rank over residue extensions. No assertion is made for singular \(N\), other Lie algebra types, or automorphism-orbit counts.

## Proof

**1. Exact normal form for retractions.** Because \(N\) is invertible, \([L,L]=V\). Every Lie endomorphism \(F\) therefore preserves \(V\), and has the unique form \(F(t)=ct+u\), \(F(v)=Tv\) with \(c\in K\), \(u\in V\), and \(T\in\operatorname{End}_K(V)\). Preserving \([t,v]=Nv\) is equivalent to \(TN=cNT\); this condition is sufficient because \(V\) is abelian. The identity \(F^2=F\) gives \(c^2=c\), \(T^2=T\), and \((c-1)u+Tu=0\). Since \(c\) is a field idempotent, \(c=0\) or \(c=1\). When \(c=0\), \(TN=0\) implies \(T=0\), then \(-u=0\) implies \(u=0\); hence \(F=0\). Otherwise, every nonzero retraction is uniquely
\[F_{T,u}(t)=t+u,\qquad F_{T,u}|_V=T,\qquad T^2=T,\quad TN=NT,\quad Tu=0.\]
Conversely, these displayed conditions imply that the map is an idempotent Lie endomorphism. Its rank is \(1+\dim_K\operatorname{im}T\).

**2. Commutation and the four summands.** Two such nonzero retractions satisfy \(F_{T,u}F_{S,v}=F_{S,v}F_{T,u}\) precisely when \(TS=ST\) and
\[(I-S)u=(I-T)v.\]
For two commuting idempotents in \(\operatorname{End}_{K[X]}(M)\), the four mutually orthogonal idempotents \((I-T)(I-S)\), \((I-T)S\), \(T(I-S)\), \(TS\) sum to the identity. Their images define a unique labeled \(K[X]\)-module decomposition
\[M=M_{00}\oplus M_{01}\oplus M_{10}\oplus M_{11},\]
where the indices indicate the eigenvalues of \(T\) and \(S\). Conversely any such labeled module decomposition determines commuting idempotents \(T,S\). The conditions \(Tu=0\), \(Sv=0\) give \(u\in M_{00}\oplus M_{01}\) and \(v\in M_{00}\oplus M_{10}\). The equation \((I-S)u=(I-T)v\) says that the two \(M_{00}\)-coordinates agree, while the \(M_{01}\)-coordinate of \(u\) and \(M_{10}\)-coordinate of \(v\) are arbitrary. Therefore there are exactly
\[q^{d(M_{00})+d(M_{01})+d(M_{10})}=q^{d(M)-d(M_{11})}\]
choices of \((u,v)\) for each fixed pair \((T,S)\). The ranks are \(1+d(M_{10})+d(M_{11})\) and \(1+d(M_{01})+d(M_{11})\). Likewise, for one idempotent with image \(A\) and kernel \(B\), there are \(q^{d(B)}\) choices of its translation \(u\).

**3. Counting embedded module splittings.** Given any tuple of module isomorphism types whose direct sum is \(M\), the group \(\operatorname{Aut}_{K[X]}(M)\) acts transitively on the corresponding *ordered embedded* direct-sum decompositions. The stabilizer of one decomposition is the direct product of the automorphism groups of its summands. Orbit–stabilizer thus gives exactly
\[\frac{a(M)}{\prod a(M_{ij})}\]
embedded four-component decompositions, and \(a(M)/(a(A)a(B))\) ordered two-component decompositions. This remains valid with equal isomorphism types in different labeled positions: their positions are fixed labels, so no factorial divisor is introduced. Summing the translation counts from Step 2 over these decompositions proves the four-summand contribution. If either retraction is zero it commutes with the other, contributing \(\mathcal E_M(U)+\mathcal E_M(W)-1\), where the common zero pair is counted once. This proves the joint polynomial, provided the automorphism orders are explicit.

**4. Explicit automorphism orders.** Distinct primary parts for irreducible \(f\) have no nonzero \(K[X]\)-homomorphisms between them, so their automorphism orders multiply. Fix one \(f\), write \(Q=q^{\deg f}\) and \(M_f=\bigoplus_j(K[X]/(f^j))^{m_j}\). The space of homomorphisms from a block of length \(j\) to one of length \(k\) has \(K\)-dimension \((\deg f)\min(j,k)\). Therefore its endomorphism ring \(E\) has \(|E|=Q^e\), with
\[e=\sum_{j,k}m_jm_k\min(j,k)=\sum_{i\ge1}(\sum_{j\ge i}m_j)^2.\]
Reducing each diagonal matrix block of equal length modulo \(f\) gives the semisimple quotient \(E/J(E)\cong\prod_j M_{m_j}(\mathbb F_Q)\). To see the radical assertion directly, endomorphisms of a cyclic \(f\)-primary block have local ring \(K[X]/(f^j)\); off-diagonal maps between nonisomorphic block lengths and diagonal maps divisible by \(f\) lie in the radical (any sufficiently long product through unequal lengths or positive \(f\)-valuation acquires arbitrarily high \(f\)-valuation and eventually vanishes). Hence \(|J(E)|=Q^{e-\sum_jm_j^2}\). An endomorphism is invertible exactly when its image in this quotient is invertible, giving
\[|E^\times|=Q^{e-\sum_jm_j^2}\prod_j|\operatorname{GL}_{m_j}(\mathbb F_Q)|=Q^e\prod_j\prod_{h=1}^{m_j}(1-Q^{-h}).\]
Multiplying over \(f\) proves the asserted \(a(M)\) formula. No infinite computation or unproved statistical extrapolation enters the argument.

**5. Squarefree case.** If the characteristic polynomial is squarefree, then \(M\) is a direct sum of pairwise nonisomorphic simple modules \(S_i\) of dimensions \(d_i\). Every labeled split assigns each \(S_i\) to exactly one of the four summands, and there is one embedded such split. For a single retraction, its two locations contribute weights \(1\) and \(q^{d_i}\), giving the product \(\prod_i(1+q^{d_i})\) for nonzero retractions. For a pair of nonzero retractions, the four locations \(00,01,10,11\) contribute weights \(q^{d_i},q^{d_i},q^{d_i},1\), hence \(\prod_i(1+3q^{d_i})\). Adding pairs with a zero retraction gives the corollary. For one simple module the number of ordered noncommuting pairs is \((q^d+2)^2-(5q^d+4)=q^{2d}-q^d\), as claimed.

## Verification

A standalone checker `verify_commuting_retractions.py` reconstructs the Lie brackets from matrices and enumerates **all** \(K\)-linear maps in seven small prime-field cases, filtering directly by the homomorphism and idempotence equations. It then counts commuting pairs by composition and compares the complete bivariate rank distribution to the formula. Additional cases check mixed rational-canonical lengths and distinct eigenvalues, and evaluate larger formula instances without asserting exhaustive verification there. Run with `python3 verify_commuting_retractions.py`. The checker returns `VERIFY_OK`; the exact exhaustive cases, including characteristic two, are printed. This finite testing is corroboration only; Steps 1–5 prove the unbounded assertion for all \(q\), all invertible \(N\), and all dimensions.

## Relationship to prior work

The rational-canonical and Jordan-block organization of almost-abelian Lie algebras, and the underlying general homomorphism descriptions, are established in Avetisyan's 2016 and 2018 works. They are used as structural context, not claimed here. The standard identification of commuting module idempotents with four labeled summands, and classical finite-module automorphism counts, are likewise pre-existing. Matrix-commutation enumeration and finite-ring idempotent-counting literature addresses overlapping component techniques. The **specific new assertion** is the bivariate rank distribution for *commuting idempotent Lie homomorphisms*, with affine translation compatibility and the factor \(q^{d(M)-d(M_{11})}\), for every invertible rational-canonical action. In particular, when \(M\) is simple, the two induced module projections always commute but \(q^{2d}-q^d\) pairs of Lie retractions do not. None of the inspected source statements gives that finite-field Lie-retraction census. See references below and the separate review record for residual originality uncertainty.

## Limitations

The theorem does not extend by this argument to singular \(N\): then \([L,L]\ne V\) and endomorphisms may not preserve the chosen abelian complement, invalidating Step 1. The output counts actual maps and ordered pairs, not conjugacy orbits. The source inspection is not a proof of global novelty; earlier equivalent results under different terminology remain a risk. Exhaustive computations cover finite examples only.

## References

1. Z. Avetisyan, *Jordanable almost Abelian Lie algebras*, arXiv:1811.01252v1 (first posted 2018-11-03), particularly Sections 3–6; primary MSC 17B05.
2. Z. Avetisyan, *The structure of almost Abelian Lie algebras*, arXiv:1610.05365v1 (first posted 2016-10-17), especially Section 4 on homomorphisms; freely accessible version v2 dated 2023-01-09.
3. G. M. Bergman and N. Nahlus, *Homomorphisms on infinite direct product algebras, especially Lie algebras*, arXiv:0910.5181v2, Section 11.1 (projection decompositions in a different setting).
4. Y. Huang, *Commuting matrices via commuting endomorphisms*, arXiv:2404.19483v1 (2024-04-30), Sections 2.4 and 3 (finite modules and matrix enumeration).
5. *Bounds for the number of idempotents in finite rings*, Communications in Algebra, DOI:10.1080/00927872.2021.1929277 (existing single-idempotent matrix-ring counting, not commuting Lie-retraction pairs).

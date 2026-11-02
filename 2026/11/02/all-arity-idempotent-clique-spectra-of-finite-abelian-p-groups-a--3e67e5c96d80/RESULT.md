# All-arity idempotent clique spectra of finite abelian \(p\)-groups and an invisible exponent

## Finding

Let \(p\) be any prime and let \(G\) be a nonzero finite abelian \(p\)-group of type
\[
G=\bigoplus_{a\geq1}(\mathbb Z/p^a\mathbb Z)^{m_a},\qquad n=\sum_a m_a.
\]
Only finitely many \(m_a\) are nonzero. Put
\[
\mathcal A_p(\mathbf m)
=p^{\sum_{a,b\geq1}m_am_b\min(a,b)}
\prod_{a\geq1}\prod_{i=1}^{m_a}(1-p^{-i}),
\]
with \(\mathcal A_p(\mathbf0)=1\). This positive integer is the order of \(\operatorname{Aut}(G)\). Write \(\Gamma(G)\) for the simple graph on all idempotents of \(\operatorname{End}(G)\), including zero and identity, with adjacency between distinct commuting elements.

For every integer \(k\geq0\), put \(b=2^k\) and let \(\mathfrak M_b(\mathbf m)\) consist of all arrays of nonnegative integers \((m_{a,c})_{a\geq1,\,1\leq c\leq b}\) satisfying \(\sum_{c=1}^b m_{a,c}=m_a\). If \(\mathbf m^{(c)}=(m_{a,c})_a\), then the exact number \(T_k(G)\) of ordered pairwise-commuting \(k\)-tuples of idempotents, with repeated entries allowed, is
\[
\boxed{T_k(G)=\sum_{\mathfrak M_b(\mathbf m)}
\frac{\mathcal A_p(\mathbf m)}{\prod_{c=1}^b\mathcal A_p(\mathbf m^{(c)})}.}
\]
The summands are integers. If \(s(k,j)\) denotes the signed Stirling number of the first kind, the number of \(k\)-vertex cliques is exactly
\[
\boxed{c_k(G)=\frac1{k!}\sum_{j=0}^k s(k,j)T_j(G),\quad0\leq k\leq2^n,}
\]
where \(c_0(G)=1\), and there are no larger cliques.

Every inclusion-maximal clique contains exactly \(2^n\) vertices; its elements form the complete Boolean family of projections onto sums of the factors in a direct-sum decomposition of \(G\) into indecomposable cyclic groups. The exact number of inclusion-maximal cliques is
\[
\boxed{M(G)=\frac{\mathcal A_p(\mathbf m)}{\displaystyle\prod_{a\geq1}
 m_a!\bigl(p^a-p^{a-1}\bigr)^{m_a}}.}
\]

**Invisible-exponent theorem.** If \(H\) is a fixed nonzero finite abelian \(p\)-group of exponent \(p^h\), then for every two integers \(b,b'>h\), the groups
\(H\oplus\mathbb Z/p^b\mathbb Z\) and \(H\oplus\mathbb Z/p^{b'}\mathbb Z\) have identical \(T_k\) for every \(k\), identical complete clique polynomials, and identical numbers and sizes of maximal cliques. Their orders and exponents differ when \(b\ne b'\). The conclusion concerns enumerative compatibility statistics; an isomorphism of the entire commuting graphs is not asserted in general.

In particular, if \(1\leq a<b\) and \(m=p^{2a}\), the entire commuting graph for \(G=\mathbb Z/p^a\mathbb Z\oplus\mathbb Z/p^b\mathbb Z\) is \(K_2\vee(mK_2)\), the join of the two central vertices with \(m\) disjoint edges. Thus \(T_k(G)=2^k+m(4^k-2^k)\), \(T_1(G)=2+2m\), and \(M(G)=m\). All these quantities are independent of \(b\) once \(b>a\).

## Assumptions and scope

An idempotent means an additive-group endomorphism \(e:G\to G\) satisfying \(e^2=e\). A clique is an unordered subset of pairwise distinct commuting idempotents. The graph has zero and identity as vertices. All formulas hold for every prime, including \(p=2\), all positive cyclic-exponent multiplicities, and every tuple arity \(k\geq0\); the zero group is excluded solely to keep the stated maximal-clique size convention nondegenerate. A summand in the \(T_k\) formula is a count of **embedded, labeled-color internal decompositions**, not a count of abstract isomorphism classes.

## Proof

**1. Automorphism order.** Each homomorphism \(\mathbb Z/p^a\mathbb Z\to\mathbb Z/p^b\mathbb Z\) has exactly \(p^{\min(a,b)}\) choices. Hence \(|\operatorname{End}(G)|=p^{\sum_{a,b}m_am_b\min(a,b)}\). Order the cyclic summands by increasing exponent. On \(G/pG\), an endomorphism induces a block upper-triangular matrix; its equal-exponent diagonal blocks are arbitrary matrices in \(M_{m_a}(\mathbb F_p)\). The map on \(G\) is invertible precisely when the induced map on \(G/pG\) is invertible: one direction is obvious; the other follows by the finite-module form of Nakayama's lemma. Invertibility of that block upper-triangular matrix holds precisely when each diagonal block is invertible. Multiplication by \(\prod_a |\operatorname{GL}_{m_a}(\mathbb F_p)|/p^{m_a^2}=\prod_a\prod_{i=1}^{m_a}(1-p^{-i})\) therefore yields \(\mathcal A_p(\mathbf m)\).

**2. Commuting tuples and colored summands.** For commuting idempotents \(e_1,\ldots,e_k\), construct the \(2^k\) mutually orthogonal idempotents
\[
P_{\epsilon}=\prod_{i=1}^k\bigl(\epsilon_i e_i+(1-\epsilon_i)(1-e_i)\bigr),
\qquad\epsilon\in\{0,1\}^k.
\]
They sum to the identity. Thus \(G=\bigoplus_{\epsilon}\operatorname{im}P_{\epsilon}\), and \(e_i=\sum_{\epsilon_i=1}P_{\epsilon}\). Conversely every such internally embedded, labeled decomposition gives exactly one ordered commuting tuple. The group type of each colored summand is given by a multiplicity array \(\mathbf m^{(\epsilon)}\), with total \(\mathbf m\), by uniqueness of invariant factors.

For any fixed multiplicity array, \(\operatorname{Aut}(G)\) acts transitively on the set of internal colored decompositions: an isomorphism between corresponding summands extends by direct sum to an automorphism of \(G\). The stabilizer of a chosen ordered colored decomposition consists exactly of the product of the automorphism groups of the individual summands. Orbit-stabilizer gives the displayed quotient and proves the formula for \(T_k(G)\), including \(k=0\).

**3. Clique polynomial.** For any finite set of idempotents, counting all commuting ordered tuples with repeated coordinates and excluding coincidences by Möbius inversion on the lattice of set partitions gives \(D_k=\sum_{j=0}^k s(k,j)T_j\), where \(D_k\) counts ordered commuting tuples with distinct entries. Dividing by \(k!\) proves the clique formula.

**4. Maximal families.** Every finite commuting family of idempotents is contained in the Boolean family of projections afforded by its joint-image decomposition. Refine any decomposable joint-image component into nonzero direct summands and include the resulting coordinate projections. A maximal clique therefore corresponds to a complete indecomposable direct-sum decomposition. The indecomposable nonzero finite abelian \(p\)-groups are exactly the cyclic groups of prime-power order. Each complete decomposition has \(n\) summands and its Boolean family has \(2^n\) distinct projections; conversely its minimal nonzero projections uniquely recover the set of indecomposable summands. Automorphisms act transitively on complete decompositions. The setwise stabilizer permits individual cyclic automorphisms and permutations among the \(m_a\) equal-exponent summands, hence has order \(\prod_a m_a!(p^a-p^{a-1})^{m_a}\). Orbit-stabilizer proves \(M(G)\).

**5. Invisibility of a unique largest exponent.** Expanding the automorphism quotient for any two or more colors gives
\[
\frac{\mathcal A_p(\mathbf m)}{\prod_c\mathcal A_p(\mathbf m^{(c)})}
=p^{2\sum_{c<d}\sum_{a,b}m_{a,c}m_{b,d}\min(a,b)}
\prod_a\frac{\prod_{i=1}^{m_a}(1-p^{-i})}
{\prod_c\prod_{i=1}^{m_{a,c}}(1-p^{-i})}.
\]
If a single exponent \(b\) is strictly larger than every other one, its cyclic summand belongs to one color. In each cross-color term involving it, \(\min(b,a)=a\) is the exponent of the other summand, so increasing \(b\) does not change any exponent in the quotient. Its multiplicity is one, so its multiplicative factor \(1-p^{-1}\) cancels identically. There is a termwise bijection of all allocations after relabeling \(b\) as \(b'\), and every \(T_k\) is unchanged. The formulas in Steps 3 and 4 give the remaining assertions.

**6. Explicit two-factor case.** For \(G=C_{p^a}\oplus C_{p^b}\), \(a<b\), the automorphism formula gives \(|\operatorname{Aut}(G)|/\bigl(|\operatorname{Aut}(C_{p^a})|\,|\operatorname{Aut}(C_{p^b})|\bigr)=p^{2a}\) ordered decompositions with these two distinct types. Each supplies two complementary nontrivial projections; a commuting pair of distinct nontrivial projections must be complementary because their joint decomposition has at most two indecomposable components. Thus the claimed graph is \(K_2\vee(p^{2a}K_2)\). A commuting tuple either uses only the universal vertices, in \(2^k\) ways, or uses a uniquely determined nontrivial complementary pair, in \(p^{2a}(4^k-2^k)\) ways.

## Verification

The accompanying standard-library Python program `verify.py` enumerates **all** endomorphism matrices of six small groups with the exact coefficient divisibility imposed by the cyclic exponents, filters idempotents by direct matrix multiplication, and independently computes commuting pairs, commuting triples, and all maximal cliques. It compares the results against the closed orbit-stabilizer formulas. For \(p=2\), the types \((1,2)\) and \((1,3)\) each give \((T_1,T_2,T_3,M)=(10,52,232,4)\); types \((1,1,2)\) and \((1,1,3)\) each give \((82,1636,18376,48)\). For \(p=3\), types \((1,2)\) and \((1,3)\) each give \((20,112,512,9)\). All checks passed. These finite cases are not a substitute for the proof for arbitrary \(p\), exponents, ranks or arities.

## Relationship to prior work

Goldsmith and Salce (2021) examine the endomorphism-ring structure and full-inertia properties of abelian \(p\)-groups; their results do not give embedded commuting-idempotent clique counts. Edmunds (2014), especially Theorems 5.9–5.10, proves simultaneous diagonalization for commuting idempotent **pairs** on finite abelian groups and counts associated interchange-ring **isomorphism classes** or bounds their number. His diagonalization is a crucial structural predecessor; diagonalizability itself is not asserted here as new. Kosakowska and Schmidmeier (2019) classify direct sums of cyclic subgroup embeddings via tableaux and partial maps, rather than all-arity embedded commuting-projection counts. The present formulas count actual idempotent configurations (not similarity classes), maximal projection families, and exhibit equality of every clique count for nonisomorphic groups obtained by stretching one uniquely largest exponent. A full-matrix idempotent clique formula over a finite local ring handles free homogeneous modules, not the mixed-exponent nonfree groups considered here.

## Limitations

The invariant-collision theorem proves equality of clique polynomials, not general graph isomorphism, equality of endomorphism rings, or an algorithm recovering group invariant factors. Counts of abstract simultaneous-conjugacy classes already have significant prior theory, and no priority claim is made for their classification. The greatest publication-priority risk is a preexisting orbit-count interpretation in the literature of finite-module decompositions or Hall polynomials. The statements concern finite abelian \(p\)-groups; extension to arbitrary finite modules over nonprincipal local rings is not proved. Independent external mathematical validation has not been performed.

## References

1. B. Goldsmith and L. Salce, “Abelian \(p\)-groups with minimal full inertia,” *Periodica Mathematica Hungarica* 85 (2022), 1–13; first online 2021-08-12, DOI: 10.1007/s10998-021-00414-w.
2. C. C. Edmunds, “Interchange Rings,” arXiv:1402.3699 (2014), especially Theorems 5.9 and 5.10.
3. J. Kosakowska and M. Schmidmeier, “Finite direct sums of cyclic embeddings,” arXiv:1905.05688 (2019), especially Sections 2–3.

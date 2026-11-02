# Clique-polynomial universality for commuting idempotents over finite local rings

## Finding
Let \(R\) be a finite commutative local ring, with \(|R|=s\) and residue field \(R/\mathfrak m\cong\mathbb F_q\), and let \(n\ge1\). Form the simple graph \(\Gamma_n(R)\) with **all** idempotent matrices in \(M_n(R)\) as vertices, two distinct vertices adjacent exactly when they commute. The zero and identity matrices are included as vertices.

Put \(g_0=1\) and, for \(j\ge1\),
\[
g_j=\left(\frac{s}{q}\right)^{j^2}\prod_{i=0}^{j-1}(q^j-q^i)=|\operatorname{GL}_j(R)|.
\]
Define \(H(z)=\sum_{j\ge0}z^j/g_j\), and for each integer \(k\ge0\) let
\[
T_{n,k}=g_n[z^n]H(z)^{2^k}.
\]
This integer is **exactly** the number of ordered \(k\)-tuples of pairwise commuting idempotent matrices, with repetitions allowed. Equivalently,
\[
T_{n,k}=\sum_{\substack{(r_\epsilon)_{\epsilon\in\{0,1\}^k}\in\mathbb Z_{\ge0}^{2^k}\\\sum_\epsilon r_\epsilon=n}}
\frac{g_n}{\prod_\epsilon g_{r_\epsilon}}.
\]
Write \(\mathfrak s(k,j)\) for the signed Stirling number of the first kind (\(\mathfrak s(0,0)=1\)). Then the complete clique polynomial, including the empty clique, is
\[
\boxed{\displaystyle
C_{n,R}(x)=\sum_{k=0}^{2^n}\frac{x^k}{k!}
\sum_{j=0}^k\mathfrak s(k,j)T_{n,j}.}
\]
In particular, it depends on \(R\) only through \(s\) and \(q\). Therefore **any two finite commutative local rings with equal cardinalities and equal residue-field orders have the same clique polynomial in every matrix dimension**. This does not assert their entire graphs are isomorphic for dimensions greater than two.

Every inclusion-maximal clique is the full Boolean family of subset-sum projections onto an unordered decomposition of \(R^n\) into \(n\) rank-one free summands. Consequently every maximal clique has exactly \(2^n\) vertices and the exact number of maximal cliques is
\[
\boxed{F_n=\frac{g_n}{n!\,g_1^n}.}
\]
Thus the idempotent-commutation graph is co-well-covered: all inclusion-maximal cliques have the same size. If \(E\) has rank \(r\), the number of idempotents commuting with \(E\), **including itself**, is \(I_rI_{n-r}\), where
\[
I_j=\sum_{a=0}^j\frac{g_j}{g_ag_{j-a}},
\]
and exactly \(F_rF_{n-r}\) maximal cliques contain \(E\), taking \(F_0=1\).

For \(n=2\), set \(N=g_2/g_1^2=(s/q)^2q(q+1)\), which is even. The whole graph has the explicit isomorphism type
\[
\boxed{\Gamma_2(R)\cong K_2\vee\bigl((N/2)K_2\bigr),}
\]
where \(\vee\) is graph join and the second factor is a disjoint union of \(N/2\) edges. Accordingly
\[
\boxed{C_{2,R}(x)=(1+x)^2\bigl(1+Nx+(N/2)x^2\bigr).}
\]

## Assumptions and scope
All rings are finite, commutative, local, and unital. The rank of an idempotent means the free rank of its image, which equals its rank after reduction to \(R/\mathfrak m\). No chain-ring, principal-ideal, characteristic, or field hypothesis is imposed. The theorem covers all \(n\ge1\) and \(k\ge0\); \(g_j\) is evaluated for all \(j\ge0\). The graph is simple and includes zero and identity; changing vertex conventions changes its clique polynomial. The formula uses abstract finite counts and is not an efficient algorithm when \(k\) is large.

## Proof
**(1) Free summands and unit-group orders.** An idempotent \(E\) splits \(R^n=\operatorname{im}E\oplus\ker E\). Both summands are finitely generated projective modules, hence free over the local ring. Reduction modulo \(\mathfrak m\) maps \(\operatorname{GL}_j(R)\) onto \(\operatorname{GL}_j(\mathbb F_q)\): any lift of an invertible residue matrix has unit determinant. Every residue matrix has exactly \(|\mathfrak m|^{j^2}=(s/q)^{j^2}\) lifts. This proves the displayed expression for \(g_j\).

**(2) Classification of commuting tuples.** Given pairwise commuting idempotents \(E_1,\ldots,E_k\), for each bit pattern \(\epsilon\in\{0,1\}^k\) form
\[
P_\epsilon=\prod_{i=1}^k \bigl(\epsilon_iE_i+(1-\epsilon_i)(I-E_i)\bigr).
\]
These are pairwise orthogonal idempotents and their sum is \(I\). Hence \(R^n=\bigoplus_\epsilon\operatorname{im}P_\epsilon\), where each summand is free of rank \(r_\epsilon\) and the ranks sum to \(n\). Conversely, every **ordered, bit-pattern-labeled** direct-sum decomposition into free summands defines uniquely a commuting tuple by \(E_i=\sum_{\epsilon_i=1}P_\epsilon\). For fixed ranks, the \(\operatorname{GL}_n(R)\)-action on these decompositions is transitive and the stabilizer of a reference decomposition is \(\prod_\epsilon\operatorname{GL}_{r_\epsilon}(R)\). Orbit-stabilizer gives \(g_n/\prod_\epsilon g_{r_\epsilon}\). Summing over rank vectors yields \(T_{n,k}\) and its coefficient formulation.

**(3) From tuples to cliques.** Let \(A_{n,k}\) count ordered pairwise-commuting \(k\)-tuples whose entries are all distinct. The partition lattice on their positions records equality constraints: imposing that every block is constant gives \(T_{n,|\pi|}\). Möbius inversion gives
\[
A_{n,k}=\sum_{\pi\in\Pi_k}\mu(\hat0,\pi)T_{n,|\pi|}
=\sum_{j=0}^k\mathfrak s(k,j)T_{n,j}.
\]
Each \(k\)-element clique yields exactly \(k!\) distinct orderings, so the coefficient of \(x^k\) is \(A_{n,k}/k!\). More than \(2^n\) pairwise-distinct commuting idempotents cannot exist: part (2) simultaneously diagonalizes them with \(n\) rank-one coordinates, and there are at most \(2^n\) distinct diagonal \(0/1\) matrices. Thus the sum stops at \(2^n\).

**(4) Classification of maximal cliques.** In any inclusion-maximal commuting family \(S\), both \(0\) and \(I\) occur. It must contain every complement \(I-E\), product \(EF\), and join \(E+F-EF\) of its members: these are commuting idempotents commuting with the entire family. Thus \(S\) is a finite Boolean algebra of commuting projections, with pairwise orthogonal nonzero atoms \(Q_1,\ldots,Q_d\) summing to \(I\). Each \(\operatorname{im}Q_i\) is a nonzero free summand. If it has rank at least two, split it into free rank-one and complementary summands; the new projection commutes with every element of \(S\) but is not in \(S\), contradicting maximality. Hence \(d=n\) and all atoms have rank one. Conversely, all \(2^n\) subset sums of the primitive rank-one projections are mutually commuting and maximal: an idempotent commuting with every primitive projection is diagonal with diagonal entries idempotents of \(R\), hence \(0\) or \(1\). There are \(g_n/g_1^n\) ordered decompositions into rank-one free summands; quotienting by permutations gives \(F_n\). The decomposition is recovered uniquely as the set of Boolean atoms, so there is no overcount.

**(5) Centralizers and dimension two.** Conjugate a rank-\(r\) idempotent to \(\operatorname{diag}(I_r,0)\). Matrices commuting with it are exactly block diagonal matrices. Their idempotents are arbitrary pairs of idempotents in the two diagonal blocks, giving \(I_rI_{n-r}\) commuting partners. A maximal family containing this projection consists of independent rank-one refinements of its image and kernel, giving \(F_rF_{n-r}\). For \(n=2\), the only noncentral idempotents have rank one. Two such idempotents commute if and only if they coincide or are complementary: simultaneous decomposition and the rank-one assumption leave only those two possibilities. Thus distinct rank-one vertices form the perfect matching \(E\leftrightarrow I-E\). Zero and identity are universal, giving the stated graph and clique polynomial.

## Verification
A standalone standard-library Python checker is provided as `verify.py`; run `python verify.py`. It independently enumerates all matrices, tests ring-correct multiplication and idempotence, forms commuting graphs, counts all cliques and maximal cliques, and compares the results with the coefficient formula. It tested \(M_2(\mathbb F_2)\), \(M_2(\mathbb F_3)\), \(M_2(\mathbb Z/4\mathbb Z)\), \(M_2(\mathbb F_2[\varepsilon]/(\varepsilon^2))\), \(M_2(\mathbb F_2[\varepsilon,\delta]/(\varepsilon,\delta)^2)\), and \(M_3(\mathbb F_2)\). This last non-principal local ring test includes a two-dimensional square-zero maximal ideal. The checks returned `VERIFY_OK`; they are finite corroboration, not the proof for arbitrary rings or sizes.

For the two nonisomorphic four-element local rings, the observed clique counts from sizes zero through four were \((1,26,61,48,12)\) in both. The eight-element non-principal local test gave \((1,98,241,192,48)\). For \(M_3(\mathbb F_2)\), the counts from sizes zero through eight were \((1,58,477,1344,1904,1568,784,224,28)\), with 28 maximal cliques of size eight.

## Relationship to prior work
Dolžan's 2021 work, especially Theorem 2.1 and Lemmas 2.2–2.3, supplies established diagonalization and exact **single-idempotent** counts in finite local matrix rings. The specialization \(k=1\) above is already covered by that work and is not claimed as new. Separately, a previously obtained finite-field sandwich-semigroup enumeration specializes to the \(k=2\) ordered commuting-idempotent count for \(M_n(\mathbb F_q)\), which is likewise **excluded** from the originality claim. Existing multi-idempotent counts for incidence algebras also use bit-pattern decompositions, but those algebras and their orbit counts differ from the present full matrix rings. The all-\(k\) **local-ring clique polynomial**, its ring-cardinality universality, and the complete maximal-family classification are the present assessed contribution. They use classical projective-module freeness, Boolean refinement, orbit-stabilizer, and partition-lattice Möbius inversion, none of which is newly claimed.

Mazurek, Nielsen, and Ziembowski (2015) consider lifting commuting idempotents modulo the Jacobson radical and exchange properties, not an enumerative formula of the present type in accessible material. Rattanakangwanwong and Meemark (2024) study a **different** graph on idempotents: adjacency via invertibility of the difference, rather than matrix commutation. Published research records on other commuting graphs do not, in the inspected portions, imply this clique polynomial. See references. Full publication priority across differently worded module-decomposition literature remains open to independent scrutiny.

## Limitations
The theorem neither gives a canonical graph isomorphism for higher-dimensional matrix algebras over nonisomorphic local rings nor asserts that their complete commuting graphs are isomorphic. The graph includes \(0\) and \(I\). The universality claim is for finite **commutative local** rings, not arbitrary semilocal or noncommutative local rings. Graph-clique counts and maximal clique classifications follow from finite projective freeness, and do not classify arbitrary commuting non-idempotent matrices. A different literature source may state an equivalent all-tuple decomposition count, in which case this would not be a new theorem under different wording. No independent audit has been performed.

## References
1. D. Dolžan, *Bounds for the number of idempotents in finite rings*, Communications in Algebra 49 (2021), 4800–4807, DOI 10.1080/00927872.2021.1929277. First available online 2021-05-28. Author-posted full text: https://www.researchgate.net/publication/351960053_Bounds_for_the_number_of_idempotents_in_finite_rings.
2. R. Mazurek, P. P. Nielsen, M. Ziembowski, *Commuting idempotents, square-free modules, and the exchange property*, Journal of Algebra 444 (2015), 52–80, DOI 10.1016/j.jalgebra.2015.07.015.
3. J. Rattanakangwanwong, Y. Meemark, *Subgraph of unitary Cayley graph of matrix algebras induced by idempotent matrices*, Discrete Mathematics 347 (2024), 113739, DOI 10.1016/j.disc.2023.113739.

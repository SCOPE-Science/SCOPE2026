# Degree-multiset rigidity for comaximal graphs of free class-two Lie algebras

## Finding

Let \(q\) be any prime power and \(n\geq 3\). For the free class-two nilpotent Lie algebra \(L=V\oplus\bigwedge^2V\), with \(V=\mathbb F_q^n\) and bracket \([v+z,w+t]=v\wedge w\), consider the simple comaximal graph on its nonzero proper Lie subalgebras: two distinct subalgebras are adjacent when they generate \(L\) as a Lie algebra.

Put \(N=\binom n2\), \(b_k=\binom k2\), and write \({a\brack j}_q\) for the number of \(j\)-dimensional subspaces of \(\mathbb F_q^a\), with value zero for out-of-range indices. For \(0\leq k<n\), define
\[
F_k(q)=\sum_{j=0}^{N-b_k}{N-b_k\brack j}_q\,q^{k(N-b_k-j)}.
\]
For \(1\leq k<n\), define
\[
D_k(q)=\sum_{\ell=n-k}^{n-1}{k\brack k+\ell-n}_q\,q^{(n-k)(n-\ell)}F_\ell(q).
\]
Then the **complete degree multiset** of this graph is
\[
\boxed{\ 0^{\,[F_0(q)-1]},\qquad D_k(q)^{\,[{n\brack k}_qF_k(q)]}\quad(1\leq k<n).\ }
\]
Here \(a^{\,[m]}\) means that the numerical degree \(a\) has multiplicity \(m\), not ordinary exponentiation. In particular, exactly \(F_0(q)-1\) vertices are isolated; \(D_1(q)<D_2(q)<\cdots<D_{n-1}(q)\); and the graph has exactly \(n\) distinct vertex degrees. **Within this family, the unlabelled degree multiset uniquely determines both \(n\) and \(q\), hence the finite-field Lie algebra up to field-preserving isomorphism.**

## Assumptions and scope

All statements hold for every finite field, including even characteristic. The algebra is free of nilpotency class two on \(n\) generators, rather than an arbitrary two-step nilpotent quotient. This distinction matters because its central bracket space is exactly \(\bigwedge^2V\). The definition of comaximal adjacency uses generation as a Lie algebra, not the condition that the vector-space sum of the two subalgebras be all of \(L\). The rigidity assertion compares only algebras belonging to this specified family; it does not assert graph rigidity among arbitrary Lie algebras.

## Proof

**1. Fibers of the projection.** Let \(Z=\bigwedge^2V\) and \(\pi:L\to V\) be the quotient projection. Fix a subspace \(W\leq V\) of dimension \(k\). A Lie subalgebra \(S\leq L\) with \(\pi(S)=W\) has \(T=S\cap Z\) containing \(\bigwedge^2W\), since brackets of lifts of elements of \(W\) span \(\bigwedge^2W\). Conversely, for every \(T\) containing \(\bigwedge^2W\), every linear map \(f:W\to Z/T\) defines exactly one such subalgebra: the inverse image inside \(W\oplus Z\) of the graph of \(f\) in \(W\oplus(Z/T)\). Its brackets lie in \(T\), so closure holds. Writing \(\dim T=b_k+j\), there are \({N-b_k\brack j}_q\) choices for \(T\) and \(q^{k(N-b_k-j)}\) choices for \(f\). Summing gives \(F_k(q)\).

If \(\pi(S)=V\), then \([S,S]=Z\), so \(Z\subseteq S\) and \(S=L\). Hence proper subalgebras have \(k<n\). Those with \(k=0\) are the subspaces of \(Z\), among which the zero subspace is excluded as a vertex; there are \(F_0(q)-1\) such vertices. For each \(1\leq k<n\), there are \({n\brack k}_qF_k(q)\) nonzero proper subalgebras with projection dimension \(k\).

**2. Adjacency.** For subalgebras \(S,U\), the Lie-generated subalgebra projects onto \(\pi(S)+\pi(U)\). If this sum equals \(V\), then choosing lifts of a basis of \(V\) inside the generated subalgebra, their brackets span \(Z\); therefore it contains \(Z\) and every lift and equals \(L\). If the projection sum is proper, generation of \(L\) is impossible. Consequently,
\[
\langle S,U\rangle_{\rm Lie}=L\iff\pi(S)+\pi(U)=V.
\]
In particular every central subalgebra is isolated.

**3. Adjacent quotient subspaces.** Fix \(W\leq V\), \(\dim W=k\), and an integer \(\ell\). The number of \(\ell\)-dimensional subspaces \(U\leq V\) with \(U+W=V\) is zero unless \(n-k\leq\ell\leq n\). When this inequality holds, the intersection has dimension \(s=k+\ell-n\). Choose \(J=U\cap W\), in \({k\brack s}_q\) ways. In the quotient \(V/J\), the subspace \(U/J\) is a complement of \(W/J\); such complements are graphs of linear maps \(V/W\to W/J\) and hence number \(q^{(n-k)(k-s)}=q^{(n-k)(n-\ell)}\). Each quotient subspace \(U\) has \(F_\ell(q)\) subalgebra lifts. The case \(\ell=n\) contributes no proper vertices, and \(\ell=0\) cannot complement positive-dimensional proper \(W\). Thus the degree is precisely \(D_k(q)\). No self-loop subtraction is necessary because \(W+W=W\ne V\).

**4. Distinct degrees.** Choose nested spaces \(0<W_k<W_{k+1}<V\), with respective dimensions \(k\) and \(k+1\). Every subalgebra whose quotient projection spans \(V\) together with \(W_k\) also spans it with \(W_{k+1}\). The containment of neighboring fibers is strict: choose a complement \(U\) of \(W_{k+1}\) in \(V\). Then \(U+W_{k+1}=V\) while \(\dim(U+W_k)=n-1\). A subalgebra projecting onto \(U\) exists because \(F_{n-k-1}(q)\geq1\). As \(\operatorname{GL}(V)\) acts transitively on quotient spaces of fixed dimension, the degree depends only on \(k\), giving \(D_k(q)<D_{k+1}(q)\). This holds for every \(1\leq k\leq n-2\), and each positive degree is nonzero.

**5. Degree-multiset rigidity.** The number of distinct degrees equals \(n\), so the degree multiset recovers \(n\). The least positive degree equals \(D_1(q)=q^{n-1}F_{n-1}(q)\), because an \((n-1)\)-space is the only proper quotient dimension complementary to a line. With \(n\) fixed, each summand in the definition of \(F_{n-1}(q)\) is a product of a Gaussian binomial polynomial (with nonnegative integer coefficients) and a power of \(q\); in particular \(F_{n-1}(q)>0\) and is nondecreasing for positive \(q\). Therefore \(q^{n-1}F_{n-1}(q)\) is strictly increasing for real \(q\geq2\), recovering the prime power \(q\) uniquely. Thus equality of degree multisets forces equality of \((n,q)\); such a pair determines the displayed free class-two Lie algebra.

## Verification

The included standalone `verify.py` constructs every reduced-row-echelon subspace of the underlying vector space over the indicated small prime fields, tests Lie closure using all basis brackets, and computes each graph edge by the rank of the Lie span including cross-brackets (rather than substituting the projection adjacency criterion). Exhaustive computations give: for \((n,q)=(2,2)\), \(10\) vertices and degree multiplicities \((0:1,6:9)\); for \((2,3)\), \(17\) vertices and \((0:1,12:16)\); and, crucially, for \((3,2)\), \(575\) vertices and \((0:15,116:357,378:203)\). The smaller \(n=2\) cases are only sanity checks, not part of the new range. Formula evaluation also gives, for \((n,q)=(3,3)\), degree multiplicities \((0:27,1062:2392,3072:1534)\); this latter case is not independently enumerated. The verifier additionally checks the strict number of degree strata for several parameter choices. It returns `VERIFY_OK`.

## Relationship to prior work

The original comaximal-graph definition, isolation-versus-Frattini correspondence, and three-dimensional classifications are due to Towers, Zuleta, and Gutierrez [1]. Their subsequent paper [2], especially Theorem 6.1, proves a general Frattini-quotient graph blow-up statement; therefore the projection adjacency principle used here is **not claimed as a new abstract graph theorem**. That paper computes quotient-fiber sizes for selected low-dimensional examples including the three-dimensional Heisenberg algebra. The present calculation is the specific all-rank subalgebra-fiber enumerator for the free class-two family with central space \(\bigwedge^2V\), leading to the closed complete degree multiset and the strictly increasing-degree reconstruction argument for every \(n\geq3\). None of these all-rank formulas or the ensuing rank-and-field degree-multiset rigidity is stated in the inspected sections of [1] and [2].

## Limitations

The claim is within the explicitly described family only and gives degree multisets, not a complete classification of all graph automorphisms or possible graph-equivalent Lie algebras outside the family. The finite enumerations independently test only the specified small prime-field instances; the proof, not enumeration, supports arbitrary finite fields. A logically equivalent degree formula elsewhere in the large literature on subalgebra zeta functions, weighted subspace graphs, or quotient blow-ups remains possible. No claim of independent verification or exhaustive historical novelty search is made.

## References

[1] David A. Towers, Yesneri Zuleta, Ismael Gutierrez, *The comaximal graph of a finite-dimensional Lie algebra*, arXiv:2605.09583, first posted 2026-05-10. https://arxiv.org/abs/2605.09583

[2] David Towers, Yesneri Zuleta, Ismael Gutierrez, *Comaximal Graphs of finite-dimensional Lie algebras over finite fields: Triangle counts and structural invariants*, arXiv:2608.16575, first posted 2026-08-17, particularly Section 6, Theorem 6.1 and Example 6.5. https://arxiv.org/abs/2608.16575

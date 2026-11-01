# Complete integral furtherness barcodes of Boolean subset posets

## Finding
Let \(n\ge 2\), and let \(P_n\) be the finite \(T_0\)-space whose points are the nonempty subsets of \([n]=\{1,\dots,n\}\), ordered by inclusion and carrying the lower Alexandrov topology. Fix any point \(S\in P_n\), and write \(s=|S|\). As in Badra and Singh's furtherness filtration, put
\[
\Psi(S,T)=|U_T\setminus U_S|,\qquad
P_n(S;t)=\{T\in P_n:\Psi(S,T)\le t\},\qquad t\in\mathbb R_{\ge0},
\]
where \(U_T=\{R\in P_n:R\subseteq T\}\). Let \(L_S(t)=\Delta(P_n(S;t))\) be the order complex; all structure maps are induced by inclusion.

**Theorem (complete integral persistence).** In every degree, the homology persistence module of \(L_S\) over \(\mathbb Z\) splits as a direct sum of free interval modules. Its only infinite interval is one \([0,\infty)\) in ordinary degree zero. For every
\[
0\le a\le s-1,\qquad 1\le b\le n-s,
\]
there are exactly
\[
\boxed{\binom{s-1}{a}\binom{n-s}{b}}
\]
finite intervals in degree \(a+b-1\), each with birth \(u=2^a(2^b-1)\) and death \(2u=2^{a+1}(2^b-1)\):
\[
\boxed{\left[2^a(2^b-1),\ 2^{a+1}(2^b-1)\right).}
\]
There are no other positive-length intervals. Equivalently, in reduced homology the infinite degree-zero interval is omitted. The decomposition is defined over \(\mathbb Z\), so the same barcode holds after extension of coefficients to any field, and no torsion occurs at any filtration level. The formula remains valid for \(s=n\), when all finite-interval multiplicities are zero and the entire filtration is already contractible at time zero.

In particular **every finite nonzero bar dies at exactly twice its birth time**; this holds in all degrees. The complete multigraded persistence profile of an element depends only on its cardinality \(s\); conversely, its degree-zero profile has exactly \(n-s\) copies of \([1,2)\), so the profile distinguishes all subset cardinalities.

## Assumptions and scope
The empty subset is **not** a point of \(P_n\), but the empty face is permitted in the standard simplicial-complex convention. The order complex uses nonempty, strictly increasing chains of subsets. The parameter \(t\) is real, and filtration inclusion is *inclusive* at each integer threshold: the time interval \([u,2u)\) includes the birth threshold and excludes the death threshold. Ordinary integral singular homology agrees with simplicial homology of the realizations. No field assumption, graph metric, normalization of furtherness, generic-position condition, or asymptotic approximation is used.

## Proof
**1. The exact furtherness weights.** The downset of a nonempty subset \(T\) contains \(2^{|T|}-1\) points. Its intersection with \(U_S\) consists of the nonempty subsets of \(S\cap T\), hence has \(2^{|S\cap T|}-1\) points. Therefore
\[
\Psi(S,T)=2^{|T|}-2^{|S\cap T|}.
\]
Write \(a=|T\cap S|\) and \(b=|T\setminus S|\). The weight is \(w_S(T)=2^a(2^b-1)\). It is nondecreasing under inclusion of subsets. Thus the family
\[
K_S(t)=\{T\subseteq[n]:T\ne\varnothing,\ w_S(T)\le t\}
\]
is an abstract simplicial complex (with the empty face understood). The poset \(P_n(S;t)\) is precisely its nonempty face poset. Consequently \(L_S(t)\) is the barycentric subdivision of \(K_S(t)\), naturally in \(t\). The induced homology persistence modules are canonically isomorphic over \(\mathbb Z\).

**2. Filtered cone-boundary lemma.** Consider any full simplex on a finite vertex set with a nonnegative, inclusion-monotone filtration weight \(w\) on nonempty faces. Fix a vertex \(v\) with \(w(\{v\})=0\). Suppose that for every nonempty face \(\sigma\) not containing \(v\), and every codimension-one face \(\tau\subset\sigma\) (the empty face allowed),
\[
 w(\{v\}\cup\tau)\le w(\sigma).
\]
Then its filtered **ordinary integral chain complex** is a direct sum of the stationary generator \([v]\) in degree zero and elementary two-generator filtered chain complexes indexed by \(\varnothing\ne\sigma\subseteq V\setminus\{v\}\). The first generator is \(c_\sigma=\partial[v,\sigma]\), of dimension \(|\sigma|-1\), born at \(w(\sigma)\); the second is \([v,\sigma]\), of dimension \(|\sigma|\), born at \(w(\{v\}\cup\sigma)\), with
\[
\partial[v,\sigma]=c_\sigma,\qquad \partial c_\sigma=0.
\]
Here \([v,\sigma]\) denotes the oriented simplex with \(v\) first and the remaining vertices in increasing order, even when it is not yet present at the specified filtration level. In that case its *formal boundary* is nevertheless a genuine chain at time \(w(\sigma)\), by the assumed inequality. For a singleton \(\sigma=\{x\}\), the formula is \(c_\sigma=[x]-[v]\).

To prove the lemma, at each level replace the ordinary oriented simplex \([\sigma]\), whenever \(v\notin\sigma\), by \(c_\sigma\), and retain the simplices containing \(v\) along with \([v]\). In each dimension the substitution is triangular with diagonal entries \(+1\):
\[
 c_\sigma=[\sigma]-\sum_{x\in\sigma} (\pm)[v,\sigma\setminus\{x\}].
\]
Every extra face in this expression has weight at most \(w(\sigma)\), so the change of basis **and its triangular inverse** respect the filtration. Its determinant is \(1\) over \(\mathbb Z\). In the resulting basis all differential entries vanish except the unit maps \([v,\sigma]\mapsto c_\sigma\). Therefore the stated direct sum holds as a filtered chain-complex isomorphism, including at tied filtration values. Each pair contributes the half-open interval \([w(\sigma),w(\{v\}\cup\sigma))\) in degree \(|\sigma|-1\), if its length is positive; a tied pair contributes no positive-length bar. The remaining generator \([v]\) contributes \([0,\infty)\) in degree zero.

**3. Verify the lemma's hypothesis for furtherness.** Choose any \(v\in S\), and take \(w=w_S\). Let \(\sigma\) avoid \(v\), and put \(a=|\sigma\cap S|\), \(b=|\sigma\setminus S|\). Its weight is \(u=2^a(2^b-1)\). Appending \(v\) doubles the weight:
\[
 w_S(\sigma\cup\{v\})=2u.
\]
If a codimension-one face \(\tau\) is obtained by removing a vertex of \(\sigma\cap S\), then \(w_S(\tau\cup\{v\})=u\). If it is obtained by removing a vertex outside \(S\), then
\[
 w_S(\tau\cup\{v\})=2^{a+1}(2^{b-1}-1)\le2^a(2^b-1)=u.
\]
The same inequality holds for \(\tau=\varnothing\), since \(w_S(\{v\})=0\). Thus the cone-boundary lemma applies to **every** subset and every filtration time.

**4. Count the intervals.** A nonempty face \(\sigma\subseteq[n]\setminus\{v\}\) containing \(a\) elements of \(S\setminus\{v\}\) and \(b\) elements of \([n]\setminus S\) occurs in exactly \(\binom{s-1}{a}\binom{n-s}{b}\) ways. If \(b=0\), then \(u=0\), so this pair is present and filled simultaneously at time zero; it contributes no nontrivial persistent homology. If \(b\ge1\), then \(u>0\) and the pair contributes precisely \([u,2u)\) in degree \(|\sigma|-1=a+b-1\). Collecting all faces proves the formula and its completeness, with no possible extension or torsion ambiguity because the chain change of basis is integral and unimodular. The coefficient-independent assertion follows by tensoring this explicit free chain decomposition.

**5. An illustrative genuinely higher-degree profile.** For \(n=5\) and \(|S|=2\), there are three degree-zero bars \([1,2)\); six degree-one bars, namely three \([2,4)\) and three \([3,6)\); four degree-two bars, three \([6,12)\) and one \([7,14)\); and one degree-three bar \([14,28)\), in addition to the essential degree-zero bar. All positive-degree classes disappear eventually even though several degrees appear and coexist at intermediate levels.

## Verification
`verify.py` is a standalone Python 3 program using only the standard library. It computes the filtration weights from their cardinality definition and, **without using the coned-boundary splitting in its matrix reduction**, constructs and reduces ordinary integral-simplicial boundary matrices modulo three distinct primes \(2,3,5\) for every \(2\le n\le8\) and \(1\le|S|\le n\). It compares all positive intervals and the essential interval to the exact formula, and checks the crucial filtered basis inequalities for every eligible face. It also reconstructs the **actual order complex of the finite poset**, rather than its unsubdivided face complex, for \(2\le n\le5\) and checks every induced barcode directly modulo \(2\). The successful output is

```
ORDER_COMPLEX_OK cases=14 chains=6086
VERIFY_OK n2..8 cases=35 direct_field_reductions=105 simplices_examined=3549 positive_bars=1291 boundary_primes=(2,3,5)
```

These finite calculations test the definitions and proof's critical inequalities. They do **not** prove the all-parameter theorem or establish integral torsion-freeness independently; those are proved by the explicit unimodular filtered basis above.

## Relationship to prior work
Badra and Singh introduced furtherness for finite topological spaces (arXiv:2603.18580, first posted March 19, 2026), then defined its centered order-complex filtration and studied the resulting **degree-zero** persistence and stability (arXiv:2610.16386, first posted October 12, 2026). Their latter paper's Section 3 gives exactly the filtration used here; Theorem 4.1 concerns births in \(H_0\). The present statement is the complete **all-degree integral persistence module** of a canonical nontrivial family of finite spaces, with explicit higher-degree births and deaths and an integral chain-level splitting. The cited work does not state this Boolean-poset formula, nor does a degree-zero birth theorem imply it.

The published result *Symmetric-group characters and contractible quotients of rank-span-two Boolean complexes* studies a different fixed rank-span restriction of the **proper** Boolean poset. Its chain condition is \(|A_r|-|A_0|\le2\) and has no basepoint or furtherness threshold; it does not imply any of the persistence intervals here. General filtered-chain decomposition theory (Chachólski, Giunti, Jin, and Landi) explains the existence of interval decompositions over fields, but does not identify the present exponentially spaced endpoints, integral splitting, or multiplicities. Searches for Boolean furtherness barcodes and related alias descriptions did not identify a prior equivalent computation; absence of a search result alone cannot establish uniqueness.

## Limitations
The classification is for the **nonempty subset poset of a full Boolean lattice**, not arbitrary posets, proper Boolean sphere posets, weighted Boolean lattices, or an arbitrary distance filtration. It concerns the centered furtherness sublevel filtration exactly as defined and its induced maps; it does not claim a simultaneous equivariant basis under all automorphisms moving the chosen pivot, nor a wedge-of-spheres homotopy equivalence at every time. Search coverage cannot exclude a nonindexed equivalent formula. Independent expert validation has not been performed.

## References
1. A. Badra and H. K. Singh, *Persistence diagrams of finite topological spaces*, arXiv:2610.16386v1, October 12, 2026, https://arxiv.org/abs/2610.16386 .
2. A. Badra and H. K. Singh, *Furtherness in finite topological spaces*, arXiv:2603.18580v1, March 19, 2026, https://arxiv.org/abs/2603.18580 .
3. S. Kayacan, *Finite Topological Space Filtrations: A Topological Framework for Data Analysis*, arXiv:2512.23348, first posted December 29, 2025, https://arxiv.org/abs/2512.23348 . Its filtration of topologies on a fixed data set is different from the centered furtherness filtration.
4. W. Chachólski, B. Giunti, A. Jin, and C. Landi, *Decomposing filtered chain complexes: Geometry behind barcoding algorithms*, Computational Geometry 111 (2023), 101938, https://doi.org/10.1016/j.comgeo.2022.101938 .
5. *Symmetric-group characters and contractible quotients of rank-span-two Boolean complexes*, published research result, https://github.com/Resultary/2026/blob/main/2026/10/11/SCOPE-symmetric-group-characters-and-contractible-quotients-of-rank-sp--a68d321e2fa8/RESULT.md .

# The characteristic-two fixed-class dichotomy in projective matroid homology

## Finding
Let \(q\geq2\) be a prime power, \(r\geq2\), and \(K_{r,q}\) the independence complex of the projective-geometry matroid on the points of \(\mathrm{PG}(r-1,q)\). Let \(G=\mathrm{PGL}_r(\mathbb F_q)\) act on the points, and let \(A\) be **any abelian group**, with trivial \(G\)-action. There is a natural group isomorphism
\[
\widetilde H_{r-1}(K_{r,q};A)^G\ \cong\
\begin{cases}
A[2],&q\text{ even},\\
0,&q\text{ odd},
\end{cases}
\qquad A[2]=\{a\in A:2a=0\}.
\]
For even \(q\), the class corresponding to \(a\in A[2]\) is the chain with coefficient \(a\) on **every projective basis** (every independent \(r\)-set). The construction is independent of orientations because \(a=-a\). For a field \(k\), the fixed top-homology space therefore has dimension one precisely when \(\operatorname{char}k=2\) and \(q\) is even; it has dimension zero otherwise. In particular, all such integral and rational fixed spaces vanish, even when their mod-two reductions contain a nonzero fixed class.

## Assumptions and scope
A projective point is a one-dimensional subspace of \(\mathbb F_q^r\). A subset of points is a face of \(K_{r,q}\) exactly when representative nonzero vectors are linearly independent. The group \(G\) is the **linear projective collineation group**, not a larger semilinear or duality group. The action on \(A\) is trivial. All chains use the usual oriented simplicial boundary and unreduced top-degree chain groups; since \(r\geq2\), reduced and ordinary homology agree in degree \(r-1\). Coefficients may have torsion or be non-finitely generated. No assertion is made about a splitting of the full homology representation or about fixed homology in lower degrees.

## Proof
Fix the independent \(r\)-set of coordinate points \(B=\{\langle e_1\rangle,\ldots,\langle e_r\rangle\}\). Every projective basis is the image of \(B\) under some element of \(G\): lift its members to an ordered vector-space basis and use the corresponding invertible linear map. Thus \(G\) acts transitively on the facets of \(K_{r,q}\).

The stabilizer of the **unordered** set \(B\) contains the invertible linear map that interchanges \(e_1\) and \(e_2\) while fixing all remaining coordinate vectors. Its induced action on the oriented facet \([e_1,\ldots,e_r]\) is multiplication by \(-1\). Hence a \(G\)-invariant top chain must have a coefficient \(a\) on \(B\) with \(a=-a\). Transitivity makes this the only freedom. Conversely, for each \(a\in A[2]\), place coefficient \(a\) on every facet, choosing arbitrary orientations: because \(-a=a\), the resulting chain \(z_a\) is well defined and \(G\)-invariant. Therefore
\[
C_{r-1}(K_{r,q};A)^G\cong A[2],\qquad a\longmapsto z_a.
\]

Let \(F\) be any independent \((r-1)\)-point set. Its span is a projective hyperplane, containing \((q^{r-1}-1)/(q-1)\) projective points, whereas all of \(\mathrm{PG}(r-1,q)\) has \((q^r-1)/(q-1)\) points. Exactly \(q^{r-1}\) points lie outside that hyperplane. These and only these extend \(F\) to a facet. The coefficient of \(F\) in the simplicial boundary \(\partial z_a\) is consequently \(q^{r-1}a\): orientations may contribute signs, but signs disappear on \(A[2]\). Thus
\[
\partial z_a=0\quad\Longleftrightarrow\quad q^{r-1}a=0.
\]
If \(q\) is even this is true for every \(a\in A[2]\). If \(q\) is odd, then \(q^{r-1}\) is odd and \(q^{r-1}a=a\) on \(A[2]\), forcing \(a=0\). Finally, there are no simplices of dimension \(r\) in an independence complex of rank \(r\), so \(C_r=0\) and **no nonzero top cycle can be a boundary**. Hence invariant top cycles are exactly invariant top homology classes, proving the asserted classification without assumptions on lower homology or shellability.

## Verification
The proof is uniform in \(r,q,A\), and does not infer an infinite statement from experiments. An independent finite-field enumerator in `verify_pg_fixed.py` constructs projective points over \(\mathbb F_2,\mathbb F_3,\mathbb F_4\), enumerates independent sets, and verifies the claimed top-face incidence number for \((q,r)=(2,2),(3,2),(4,2),(2,3),(3,3),(4,3),(2,4)\). In particular, the seven-point case has \(28\) facets, with each edge contained in \(4\) facets, while the thirteen-point case has \(234\) facets, with each edge in \(9\). The verifier outputs `VERIFY_OK`; its recorded output is included. The general transitivity and orientation arguments are established above, not inferred from enumeration.

## Relationship to prior work
Björner's matroid-topology treatment supplies the classical shellability framework for independence complexes, but the present invariant calculation does not require shellability. Mnukhin and Siemons investigate modular inclusion-map homology of projective **subspace lattices** and of shellable complexes; their projective-space construction has chains indexed by subspaces rather than by independent **point sets**, and the projective-space main setting assumes coefficient characteristic not dividing \(q\). Moci and Pezzoli give characteristic-zero equivariant comparisons for matroid independence-complex homology, including general duality and lattice-of-flats methods, but not this arbitrary-coefficient fixed-subgroup classification. The previously known seven-point Fano-specific integral representation describes one special case; it does not imply the all-rank, all-prime-power, all-abelian-group dichotomy. The novelty assertion is limited to this complete coefficient-sensitive projective-basis fixed-class criterion.

## Limitations
This theorem concerns the \(G\)-fixed subgroup of **top** homology, not the entire representation; the proof gives no integral module decomposition, no fixed classes for larger groups, and no classification for non-Desarguesian finite planes. For coefficients with nontrivial group action the statement need not hold. Searches and primary-text comparisons did not identify an equivalent published statement, but an unindexed formulation in representation theory or modular matroid topology remains possible. The finite checks are confirmatory only.

## References
1. A. Björner, *The homology and shellability of matroids and geometric lattices*, in *Matroid Applications*, Cambridge University Press (1992), pp. 226–283, DOI: 10.1017/CBO9780511662041.008.
2. V. B. Mnukhin and I. J. Siemons, *On modular homology in projective space*, *Journal of Pure and Applied Algebra* **151** (2000), 51–65, DOI: 10.1016/S0022-4049(99)00053-5.
3. V. B. Mnukhin and I. J. Siemons, *On modular homology of simplicial complexes: Shellability*, *Journal of Combinatorial Theory A* **93** (2001), 350–370, DOI: 10.1006/jcta.2000.3114.
4. L. Moci and G. M. Pezzoli, *Representations of automorphism groups on the homology of matroids*, arXiv:2001.03760 (first posted 11 January 2020), later *European Journal of Combinatorics* **94** (2021), 103312.

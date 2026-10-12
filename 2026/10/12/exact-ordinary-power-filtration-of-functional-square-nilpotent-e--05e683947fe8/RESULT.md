# Exact ordinary-power filtration of functional-square nilpotent evolution algebras
## Finding
Let \(E\) be a finite-dimensional evolution algebra over an arbitrary field \(K\) with natural basis \(B=\{e_v:v\in V\}\). Assume that each basis square has at most one nonzero natural-basis coordinate: for every \(v\), either \(e_v^2=0\), or
\[
e_v^2=c_v e_{\sigma(v)}\qquad(c_v\in K^\times).
\]
Call this the functional-square condition. Let \(\Gamma\) be the attached digraph, with an arrow \(v\to\sigma(v)\) exactly when \(e_v^2\ne0\). Assume \(\Gamma\) is acyclic. For each vertex \(v\), define \(\ell(v)\) to be the largest number of edges in a directed path ending at \(v\).

For ordinary nonassociative powers
\[
E^1=E,\qquad E^k=\sum_{a=1}^{k-1}E^aE^{k-a}\quad(k\ge2),
\]
one has, for every integer \(k\ge1\),
\[
E^k=\operatorname{span}\{e_v:k\le 2^{\ell(v)}\}.
\]
Consequently, if \(L=\max_v\ell(v)\), then the ordinary nilpotency index is exactly
\[
2^L+1,
\]
and the whole dimension profile is
\[
\dim E^k=\#\{v:\ell(v)\ge\lceil\log_2 k\rceil\}.
\]
In particular, within this class the complete ordinary-power filtration is determined by the unweighted digraph; changing the nonzero coefficients \(c_v\) does not change any \(E^k\) as a coordinate subspace.

## Assumptions and scope
An evolution algebra here means a commutative, generally nonassociative algebra admitting a natural basis with \(e_ve_w=0\) whenever \(v\ne w\). The functional-square hypothesis is restrictive: each \(e_v^2\) has support of size at most one. No restriction on the characteristic of \(K\) is used. Acyclicity is equivalent to nilpotency for finite-dimensional evolution algebras by the graph criterion of Elduque and Labra.

The path depth \(\ell(v)\) is measured toward \(v\): sources and isolated vertices have depth \(0\); if \(u\to v\), then \(\ell(v)\ge\ell(u)+1\). Since the graph is finite and acyclic, every depth is finite.

## Proof
We first record a support lemma. Suppose \(U=\operatorname{span}\{e_v:v\in S\}\) and \(W=\operatorname{span}\{e_v:v\in T\}\) are coordinate subspaces. Because distinct natural-basis vectors multiply to zero,
\[
UW=\operatorname{span}\{e_v^2:v\in S\cap T\}.
\]
Under the functional-square hypothesis, every nonzero vector \(e_v^2\) in this spanning set is a nonzero scalar multiple of a single basis vector. Therefore \(UW\) is again a coordinate subspace. Inductively, every ordinary power \(E^k\) is a coordinate subspace.

Let \(S_k=\{v:e_v\in E^k\}\). The preceding observation gives the exact recurrence
\[
S_1=V,\qquad
S_k=\bigcup_{a=1}^{k-1}\sigma(S_a\cap S_{k-a}),
\]
where \(\sigma(X)\) means the set of nonzero-square targets of vertices in \(X\).

We prove by induction on \(d=\ell(v)\) that
\[
e_v\in E^k\quad\Longleftrightarrow\quad 1\le k\le2^d.
\]
If \(d=0\), then no arrow enters \(v\). Hence no product of two coordinate subspaces can have a nonzero \(e_v\)-coordinate, so \(e_v\in E^1\) and \(e_v\notin E^k\) for all \(k\ge2\).

Now let \(d\ge1\). Because \(d\) is the maximum length of a path ending at \(v\), there is a predecessor \(u\to v\) with \(\ell(u)=d-1\). If \(2\le k\le2^d\), choose positive integers \(a,b\) with \(a+b=k\) and \(a,b\le2^{d-1}\). By induction, \(e_u\in E^a\cap E^b\), so
\[
e_u^2=c_u e_v\in E^aE^b\subseteq E^k.
\]
Together with \(e_v\in E^1\), this proves membership for all \(k\le2^d\).

Conversely, suppose \(e_v\in E^k\) with \(k\ge2\). By the coordinate-support recurrence, there are \(a,b\ge1\) with \(a+b=k\) and a predecessor \(u\to v\) such that \(e_u\in E^a\cap E^b\). Every predecessor of \(v\) has depth at most \(d-1\). By induction,
\[
a\le2^{\ell(u)}\le2^{d-1},\qquad b\le2^{\ell(u)}\le2^{d-1},
\]
so \(k=a+b\le2^d\). This proves the equivalence.

Taking all vertices at once gives the displayed formula for \(E^k\). If \(L=\max_v\ell(v)\), a vertex of depth \(L\) lies in \(E^{2^L}\), while no vertex lies in \(E^{2^L+1}\). Thus the nilpotency index is \(2^L+1\). Counting basis vectors in the exact support yields the dimension formula.

## Verification
The accompanying `verify.py` independently reconstructs ordinary-power supports from the defining recurrence for every acyclic partial functional digraph on up to six labeled vertices. It compares each computed support with \(\{v:k\le2^{\ell(v)}\}\), and it checks the predicted terminal nonzero and first zero powers. The exhaustive run covers \(18,248\) acyclic partial functional digraphs and returns `VERIFY_OK cases=18248`.

This computation is a finite stress test, not the proof of the all-dimensional theorem. The proof above supplies the arbitrary-dimension and arbitrary-field argument.

## Relationship to prior work
Casas, Ladra, Omirov, and Rozikov introduced the ordinary-power convention used here and studied exact nilpotency indices of nilpotent evolution algebras. Their 2012 preprint, later published in *Linear Algebra and its Applications*, proves the maximal index \(2^{n-1}+1\) under the nonvanishing consecutive-chain condition and constructs further special index families. The present result recovers the pure directed chain as the case \(L=n-1\), but treats every acyclic functional-square digraph and gives every ordinary power, not only the terminal index.

Elduque and Labra proved that a finite-dimensional evolution algebra is nilpotent exactly when its attached digraph has no oriented cycle. Their graph theorem supplies the qualitative acyclicity criterion used here. Their nilpotency section does not give an ordinary-power index or a path-depth filtration. Hegazi and Abdelwahab study annihilator extensions and low-dimensional classification; Elduque and Labra later develop upper-annihilating-series invariants and low-dimensional classification. These are structurally adjacent but use different filtrations and do not state the functional-square power formula above.

## Limitations
The theorem does not cover a basis square with two or more nonzero coordinates. In that setting, ordinary powers need not stay coordinate subspaces and coefficients can interact, so the support recurrence used in the proof fails. The result is basis-relative: the functional-square property and its attached digraph are properties of the chosen natural basis. No claim is made that the path-depth profile is invariant under arbitrary changes of natural basis outside this class.

The literature comparison is bounded to the primary full texts and targeted database searches described in the accompanying review. Absence of a matching statement in those searches is not a proof of global novelty; later or differently-termed work could contain an equivalent formulation.

## References
1. J. M. Casas, M. Ladra, B. A. Omirov, U. A. Rozikov, *On nilpotent index and dibaricity of evolution algebras*, arXiv:1208.1709; doi:10.1016/j.laa.2013.03.006.
2. A. Elduque, A. Labra, *Evolution algebras and graphs*, arXiv:1312.4685; doi:10.1142/S0219498815501030.
3. A. S. Hegazi, H. Abdelwahab, *Nilpotent evolution algebras over arbitrary fields*, arXiv:1508.06860; doi:10.1016/j.laa.2015.07.041.
4. A. Elduque, A. Labra, *On nilpotent evolution algebras*, arXiv:1602.01590; doi:10.1016/j.laa.2016.04.025.

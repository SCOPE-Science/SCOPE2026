# Complete bipartite graphical groups have Gaussian character enumerators

## Finding

Let \(a,b\ge2\) and let \(q\) be an odd prime power. For the graphical group \(\mathbf G_{K_{a,b}}(\mathbf F_q)\),
\[
\boxed{\operatorname{ch}(K_{a,b},i;q)=q^{a+b-2i}
\frac{\prod_{j=0}^{i-1}(q^a-q^j)(q^b-q^j)}
{\prod_{j=0}^{i-1}(q^i-q^j)}}
\]
for \(0\le i\le\min(a,b)\), and no other irreducible character degrees occur.

Writing
\[
N_{a,b,i}(q)=\#\{M\in\operatorname{Mat}_{a\times b}(\mathbf F_q):\operatorname{rk}(M)=i\},
\]
this is
\[
\boxed{\operatorname{ch}(K_{a,b},i;q)=q^{a+b-2i}N_{a,b,i}(q).}
\]
Thus Rossmann's character-enumeration Question 1.10 has a closed Gaussian-product answer for every non-tree complete bipartite graph.

## Assumptions and scope

The theorem concerns ordinary complex irreducible characters and odd \(q\), the range of the rank formula used below. The restriction \(a,b\ge2\) removes stars, which are already covered by later tree-enumeration results.

Rossmann already computes complete-bipartite conjugacy-class enumerators. The present theorem solves the distinct character-degree problem.

## Proof

Order vertices by the two bipartition classes. The generic commutator matrix is
\[
B_{K_{a,b}}(Y)=
\begin{pmatrix}0&M(Y)\\-M(Y)^{\mathsf T}&0\end{pmatrix},
\]
with \(M(Y)\) the generic \(a\times b\) matrix. If \(\operatorname{rk}(M)=i\), then
\[
\dim\ker B=(a-i)+(b-i),
\]
so \(\operatorname{rk}(B)=2i\).

O'Brien--Voll's Theorem B gives
\[
\operatorname{ch}(K_{a,b},i;q)
=
\#\{M:\operatorname{rk}(M)=i\}
|\mathbf G/\mathbf G'|q^{-2i}.
\]
Here \(|\mathbf G/\mathbf G'|=q^{a+b}\), hence
\[
\operatorname{ch}(K_{a,b},i;q)=q^{a+b-2i}N_{a,b,i}(q).
\]
The standard rectangular rank count is
\[
N_{a,b,i}(q)=
\frac{\prod_{j=0}^{i-1}(q^a-q^j)(q^b-q^j)}
{\prod_{j=0}^{i-1}(q^i-q^j)}.
\]

Finally,
\[
\sum_i\operatorname{ch}(K_{a,b},i;q)q^{2i}
=q^{a+b}\sum_iN_{a,b,i}(q)
=q^{a+b+ab},
\]
which is exactly the graphical-group order.

## Verification

The included checker exhaustively enumerates matrices for
\[
(q,a,b)=(3,2,2),(3,2,3),(3,3,3),(5,2,2),(5,2,3),
\]
checks every rank stratum against the product formula, and verifies the character degree-squared identity.

For \(K_{2,2}\) over \(\mathbf F_3\), the rank counts are \(1,32,48\), giving character multiplicities \(81,288,48\) at degrees \(1,3,9\).

The checker returns `VERIFY_OK`. Finite enumeration is not used in the proof.

## Relationship to prior work

Rossmann's Question 1.10 asks how \(\operatorname{ch}(\Gamma,i;q)\) depends on \(q\), and lists polynomial answers for edgeless graphs, paths, and complete graphs. The same paper treats \(K_{a,b}\) only on the conjugacy-class side in Example 5.3.

O'Brien--Voll's Theorem B supplies the general rank-to-character bridge; the complete-bipartite block form turns its remaining rank locus into the classical rectangular-matrix rank distribution.

Later published findings handle trees, cycles, and a coning recurrence. The tree result covers stars, which are excluded here. Targeted database searches found no explicit formula for \(K_{a,b}\) with \(a,b\ge2\).

## Limitations

The theorem is restricted to odd \(q\). The reduction is short once the general rank framework is available, but it solves a published enumeration problem on a canonical infinite non-tree family.

A later coning result is bibliographically close because it treats \(K_1\vee K_{a,b}\); its published summary does not state the base \(K_{a,b}\) formula. Failed searches do not prove novelty.

## References

1. T. Rossmann, “Enumerating conjugacy classes of graphical groups over finite fields,” arXiv:2107.05564v1, first public version 12 July 2021; *Bulletin of the London Mathematical Society* 54 (2022), 1329–1346, DOI 10.1112/blms.12665. Primary MSC 20D15.
2. E. A. O'Brien and C. Voll, “Enumerating classes and characters of \(p\)-groups,” *Transactions of the American Mathematical Society* 367 (2015), 7775–7796, arXiv:1203.3050, DOI 10.1090/tran/6276.

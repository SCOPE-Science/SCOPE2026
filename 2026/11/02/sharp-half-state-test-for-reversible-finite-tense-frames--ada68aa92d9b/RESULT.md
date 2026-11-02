# Sharp half-state test for reversible finite tense frames

## Finding

Let \(W\) be a labelled nonempty finite set of size \(n\), and let \(f:W\to W\) be a total function. Interpret the forward and backward possibility operators on \(\mathcal P(W)\) by
\[
\mathbf F(X)=f^{-1}(X),\qquad \mathbf P(X)=f(X).
\]
For any nonnegative integer \(k\), put \(C_k=\mathbf F^k\mathbf P^k\) and \(I_k=\mathbf P^k\mathbf F^k\), with composition read right-to-left. The property \(C_k I_k=I_k C_k\) means equality on **every** subset of \(W\), equivalently frame validity under every valuation of the modal formula
\[
\mathbf F^k\mathbf P^k\mathbf P^k\mathbf F^k p
\leftrightarrow
\mathbf P^k\mathbf F^k\mathbf F^k\mathbf P^k p.
\]

**Theorem.** For every \(k\ge1\), write \(g=f^k\) and \(A=g(W)\). The following are equivalent:

1. \(C_k I_k=I_k C_k\) on all subsets;
2. \(A\) is a union of complete fibres of \(g\);
3. \(g(A)\cap g(W\setminus A)=\varnothing\).

If \(f\) is not a permutation, let \(h(f)\) be the largest distance from a vertex of its functional digraph to the eventual directed cycle. Then the three equivalent conditions **fail for every integer** \(k>h(f)/2\). Consequently, for every \(n\ge2\), the least fixed exponent \(K\ge0\) such that commutation at exponent \(K\) forces \(f\) to be a permutation on every \(n\)-point carrier is exactly
\[
\boxed{K_n=\lceil n/2\rceil}.
\]
For each smaller exponent there is a nonpermutation witnessing commutation.

Moreover, the exact number \(M_{n,k}\) of labelled maps \(f:W\to W\) with \(|f(W)|=k\) and \(C_1 I_1=I_1 C_1\) is
\[
M_{n,k}=\begin{cases}
n!,&k=n,\\[2mm]
\displaystyle\binom nk k!\sum_{b=1}^{k-1}
\left\{\begin{matrix}k\\b\end{matrix}\right\}
\left\{\begin{matrix}n-k\\k-b\end{matrix}\right\},&1\le k<n,
\end{cases}
\]
where braces denote Stirling numbers of the second kind, with zero values for impossible surjections. The total one-step counts for \(n=1,\ldots,8\) are
\[
1,\ 2,\ 12,\ 108,\ 1100,\ 13350,\ 194502,\ 3280424.
\]

## Assumptions and scope

The carrier is finite, nonempty and labelled; \(f\) is a single total deterministic successor function. The converse relation is used to interpret the past operator. The theorem concerns the **specific commutation identity** above, not all possible modal axioms characterising permutation frames. For \(n=1\), all maps are permutations, so there is no nonpermutation threshold to determine. The structural equivalence applies to any \(k\ge1\); the formula at \(k=0\) is always true.

## Proof

**Step 1 (adjunction normal form).** For \(g=f^k\), the forward operator is \(g^{-1}\) and the past operator is the direct-image map \(g[-]\). Thus
\[
C_k(X)=g^{-1}(g(X)),\qquad I_k(X)=g(g^{-1}(X))=X\cap A.
\]
The first map is precisely saturation by the equivalence relation \(x\sim_g y\iff g(x)=g(y)\), and the second discards points outside \(A\). If \(A\) is a union of equivalence classes, saturation commutes with intersection with \(A\). Conversely, if some fibre contains \(a\in A\) and \(u\notin A\), then for \(X=\{u\}\) one has \(C_k(I_k(X))=\varnothing\) but \(a\in I_k(C_k(X))\). Hence commutation holds exactly when \(A\) is fibre-saturated. This is equivalent to the disjointness of \(g(A)\) and \(g(W\setminus A)\).

**Step 2 (half-height obstruction).** A finite functional digraph is a disjoint union of directed cycles with in-arborescences. Write \(h\ge1\) for the largest distance of any vertex to its cycle, and fix a path of transient vertices attaining that distance. Let \(k>h/2\). If \(k\le h\), choose a vertex \(u\) on that path at distance \(d=h-k+1\) from its cycle. This satisfies \(1\le d\le k\). If \(k>h\), choose a vertex at distance \(d=1\) from its cycle. In either case \(u\notin g(W)\): otherwise a \(k\)-step predecessor of \(u\) would have distance \(d+k>h\), impossible. Yet \(g(u)\) is a cycle point since \(d\le k\). The map \(g\) permutes each cycle, so every cycle point belongs to \(g(g(W))\), including \(g(u)\). Consequently \(g(u)\in g(W\setminus A)\cap g(A)\), contradicting Step 1.

Every nonpermutation has \(1\le h\le n-1\). Thus \(k=\lceil n/2\rceil\) satisfies \(2k\ge n>h\), while every permutation satisfies commutation at all powers.

**Step 3 (sharpness).** For \(n\ge2\), use the chain-to-fixed-point function on \(W=\{0,\ldots,n-1\}\):
\[
f(i)=\min(i+1,n-1).
\]
For every \(0<k\le\lfloor(n-1)/2\rfloor\), its \(k\)-th power \(g\) has image \(A=\{k,\ldots,n-1\}\), and
\[
g(A)=\{2k,\ldots,n-1\},\qquad
g(W\setminus A)=\{k,\ldots,2k-1\}.
\]
These are disjoint. At \(k=0\) both mixed composites are the identity. This witnesses failure of any smaller uniform exponent. The map is not a permutation.

**Step 4 (exact enumeration).** Fix \(k<n\) and set \(A=f(W)\), so \(|A|=k\). When commutation holds, \(B=f(A)\) and \(f(W\setminus A)\) are nonempty disjoint sets whose union is \(A\). Write \(|B|=b\), hence \(1\le b<k\). Choose \(A\) in \(\binom nk\) ways, then choose \(B\subseteq A\) in \(\binom kb\) ways. The restrictions \(f|_A:A\to B\) and \(f|_{W\setminus A}:W\setminus A\to A\setminus B\) must be surjective. Their numbers are \(b!\left\{\begin{smallmatrix}k\\b\end{smallmatrix}\right\}\) and \((k-b)!\left\{\begin{smallmatrix}n-k\\k-b\end{smallmatrix}\right\}\), respectively. The product of the three factorial/binomial factors for \(B\) reduces to \(k!\). Every such pair of surjections has precisely the prescribed image \(A\), so the construction is bijective. When \(k=n\), the maps are precisely the \(n!\) permutations. This proves the census.

## Verification

Run \(\texttt{python3 checker.py}\) in the directory containing the included source. It exhaustively checks all \(50069\) maps on carriers of sizes \(1\) through \(6\), the rank-refined Stirling count, the half-height obstruction at every relevant iterate, and the universal sharp exponent. It evaluates the modal operator identity directly on every subset for all powers through size \(4\). The sharp chain examples are checked through size \(30\). Its successful terminal line is \(\texttt{ALL_CHECKS_OK}\). This finite testing is supplementary: Steps 1–4 above prove the quantified theorem for arbitrary finite \(n\).

## Relationship to prior work

The conjugate past/future operations and their adjunction are standard in tense Boolean algebras; Figallo–Sarmiento–Pezzini (2026) gives an accessible recent formulation. Sano (2026) establishes uniform interpolation for the basic tense language. Burrieza (2026) studies definability of functional properties in an ordered multiflow semantics, which differs from iterating one deterministic Kripke successor map. Ciraulo–Sambin (2011) studies a general closure/interior Galois connection. None of the inspected relevant statements supplies the half-state power cutoff or the rank-refined count in this deterministic tense setting. General set-theoretic facts about saturated fibres and Stirling surjections are background, not claimed as inventions.

## Limitations

The result does not assert a globally optimal modal depth among **all** formulas: other formulas can characterize invertibility at smaller depth. It is a sharp bound for the specified commutation scheme. It does not cover nondeterministic relations, partial functions, infinite carriers, or arbitrary algebraic tense structures without an underlying total function. The counting formula concerns labelled maps and the exponent-one identity only. An equivalent formulation in transformation-semigroup or closure-operator literature may predate the inspected sources; independent historical-priority review has not occurred.

## References

1. Martín Figallo, Jonathan Sarmiento and Luis Pezzini, *Tense Logic via Truth Degrees: An Algebraic Completeness Result for Kashima's Calculus*, arXiv:2610.01547v1, October 1, 2026. https://arxiv.org/abs/2610.01547
2. Katsuhiko Sano, *Uniform Interpolation of Basic Tense Logic*, arXiv:2606.31887v1, June 30, 2026. https://arxiv.org/abs/2606.31887
3. Alfredo Burrieza, *Definability of Functional Properties in the Basic Modal-Temporal Language over Ordered Frames*, arXiv:2607.01110v1, July 1, 2026. https://arxiv.org/abs/2607.01110
4. Francesco Ciraulo and Giovanni Sambin, *A Constructive Galois Connection between Closure and Interior*, arXiv:1101.5896v1, January 31, 2011. https://arxiv.org/abs/1101.5896

# Exact clique number of the mutual Birkhoff–James orthograph of real \(\ell_\infty^n\)

## Finding
For each integer \(n\geq1\), equip \(X_n=\mathbb R^n\) with the coordinate supremum norm. Write \(x\perp_B y\) if \(\|x+\lambda y\|_\infty\geq\|x\|_\infty\) for every real scalar \(\lambda\). The *mutual Birkhoff–James orthograph* \(\Gamma_n\) has nonzero one-dimensional subspaces \([x]\) as vertices, and two distinct vertices are adjacent precisely when both \(x\perp_B y\) and \(y\perp_B x\).

The exact clique number of the **entire** projective graph, with no restriction on representative coordinates, is
\[
\boxed{\omega(\Gamma_n)=\max_{1\leq k\leq n}\binom nk2^{k-1}
=\binom n{\lfloor 2(n+1)/3\rfloor}2^{\lfloor 2(n+1)/3\rfloor-1}.}
\]
In particular the values for \(n=1,\ldots,8\) are \(1,2,6,16,40,120,336,896\). More structurally, the infinite-vertex graph \(\Gamma_n\) admits a graph retraction onto the finite incomparability graph of nonempty signed subsets of \([n]\), where globally opposite signings are identified. A largest signed-support rank is a maximum clique. The formula also yields \(\omega(\Gamma_n)=(1+O(n^{-1}))3^{n+1}/(4\sqrt{\pi n})\).

## Assumptions and scope
The scalar field is **real**, \(n\) is a positive integer, the norm is the standard supremum norm, and orthogonality is the real-scalar Birkhoff–James relation. Projective vertices identify \(x\) and every nonzero scalar multiple of \(x\). No assumption that the vectors in a clique have coordinates in \(\{-1,0,1\}\) is made. This result determines the maximum cardinality, not the classification of all maximum cliques. The complex-scalar orthograph is outside the present upper-bound claim.

For a nonzero unit vector \(x\), let \(A(x)=\{i:|x_i|=1\}\). Define its *active-coordinate rounding* by
\[
R(x)_i=\begin{cases}\operatorname{sgn}(x_i),&i\in A(x),\\0,&i\notin A(x).\end{cases}
\]
For any nonzero \(x\), normalize first by \(\|x\|_\infty\); thus \([x]\mapsto[R(x/\|x\|_\infty)]\) is well-defined on real projective lines. Its image is the finite set \(P_n\) of nonzero ternary sign vectors modulo common negation. Write \([s]\preceq[t]\) when \(\operatorname{supp}(s)\subseteq\operatorname{supp}(t)\) and \(t\) restricted to the support of \(s\) equals \(s\) or \(-s\). This is a partial order.

## Proof
**1. Exact directed orthogonality test.** For nonzero \(x\), the real convex function \(f(\lambda)=\|x+\lambda y\|_\infty\) has right derivative at zero equal to \(\max_{i\in A(x)}\operatorname{sgn}(x_i)y_i\) and left derivative equal to \(\min_{i\in A(x)}\operatorname{sgn}(x_i)y_i\), after normalizing \(x\) to a unit vector. (The non-active coordinates have a strict gap below one and do not affect either directional derivative at zero.) Since \(f\) is convex, zero is a global minimizer exactly when these derivatives straddle zero. Hence
\[
x\perp_B y\quad\Longleftrightarrow\quad
\min_{i\in A(x)}\operatorname{sgn}(x_i)y_i\leq0\leq
\max_{i\in A(x)}\operatorname{sgn}(x_i)y_i.
\tag{1}
\]

**2. Rounding preserves every mutual edge and distinctness.** If a finite list of real numbers has minimum at most zero and maximum at least zero, replacing an arbitrary subset of its entries by zeros preserves this property: either a zero was already present, or the original list contained opposite signs and every removed sign leaves a zero in its place. In (1), rounding \(y\) replaces some of the values \(\operatorname{sgn}(x_i)y_i\) by zero and leaves the others unchanged. Rounding \(x\) does not alter its active set or its signs there. Thus \(x\perp_B y\) implies \(R(x)\perp_B R(y)\), and the analogous implication applies to the reverse relation.

Further, if \([R(x)]=[R(y)]\), then their active sets coincide and the signs of \(y\) on this common active set agree with those of \(x\) everywhere, up to a common negation. All entries in (1) are consequently strictly of the same sign, so \(x\not\perp_B y\). Therefore **distinct mutually orthogonal lines round to distinct mutually orthogonal ternary lines**. Conversely, rounding fixes every ternary line. This proves that rounding is a graph retraction from \(\Gamma_n\) onto its induced finite ternary subgraph.

**3. The ternary graph is a poset incomparability graph.** For nonzero ternary \(s,t\), formula (1) fails for the directed relation \(s\perp_B t\) precisely when every nonzero coordinate of \(s\) is also nonzero in \(t\) and the products \(s_it_i\), over those coordinates, all have the same strict sign. Equivalently, \([s]\preceq[t]\). Thus distinct ternary vertices fail to be mutually orthogonal if and only if they are comparable in \(P_n\). Cliques correspond exactly to antichains in \(P_n\). Steps 2–3 show that \(\omega(\Gamma_n)\) is **equal** to the width of this finite ranked poset, rather than just bounded below by it.

**4. Sharp signed-subset LYM bound.** For each rank \(1\le k\le n\), the elements of \(P_n\) supported on exactly \(k\) coordinates number
\[
N_k=\binom nk 2^{k-1}.
\tag{2}
\]
Choose uniformly an antipodal class \([\varepsilon]\) of a full sign vector \(\varepsilon\in\{-1,1\}^n\), and independently choose a uniformly random permutation \(\pi\) of \([n]\). The restrictions of \(\varepsilon\) to the first \(k\) coordinates in \(\pi\), modulo global sign, for \(k=1,\ldots,n\), constitute a maximal chain. At rank \(k\) the distribution is uniform among the \(N_k\) signed partial vectors: a specified signed support has probability \(\binom nk^{-1}2^{1-k}=N_k^{-1}\).

A chain contains at most one member of any antichain \(\mathcal A\subseteq P_n\). Taking expectations therefore gives the exact Lubell inequality
\[
\sum_{[s]\in\mathcal A}\frac{1}{N_{|\operatorname{supp}(s)|}}\leq1.
\tag{3}
\]
It follows that \(|\mathcal A|\leq\max_k N_k\). Conversely, all elements of any one rank form an antichain and attain cardinality \(N_k\). Hence the maximum clique number is exactly \(\max_k N_k\).

Finally, \(N_{k+1}/N_k=2(n-k)/(k+1)\) decreases with \(k\), so \(k=\lfloor2(n+1)/3\rfloor\) is a maximizing rank (with a tie between consecutive ranks when \(n\equiv2\pmod3\)). The asymptotic expression follows from \(N_k=(3^n/2)\Pr\{\mathrm{Bin}(n,2/3)=k\}\) and Stirling's formula at the mode. These arguments include the boundary case \(n=1\).

## Verification
The accompanying standalone Python 3 program `verify.py` uses only the standard library. Run `python3 verify.py` from the directory containing this file. It checks, by exact sign comparisons, that mutual orthogonality agrees with incomparability for every pair of ternary projective vectors through dimension six; that active rounding preserves all mutual edges on the projective grid with coordinates in \(\{-2,-1,0,1,2\}\) through dimension four; and that the random-chain construction hits every same-rank object equally often through dimension four. The recorded successful output was:

```
ternary pair/order tests: 74190
rounding edge tests: 15628
uniform-chain checks: 4
VERIFY_OK
```

These finite checks are diagnostic only. The proof of (1)–(3) establishes the unrestricted real finite-dimensional theorem for every \(n\), without relying on exhaustive computation.

## Relationship to prior work
Arambašić, Guterman, Kuzma, Rajić and Zhilina (2021), Example 3.7, gave \(2^{n-1}\) pairwise mutual Birkhoff–James-orthogonal projective vectors of real or complex \(\ell_\infty^n\) and bounded the clique number for arbitrary finite-dimensional norms (Theorems 3.5 and 4.1). They did not provide this supremum-space exact clique number. Guterman, Kuzma, Singla and Zhilina (2024) used directed orthogonality graphs to characterize the supremum norm and finite dimensionality; its clique finiteness results do not calculate this invariant.

A published 2026 result, *Ternary-support cliques of order \(3^n/\sqrt n\) in the Birkhoff–James orthograph of \(\ell_\infty^n\)*, already gives the sharp **lower-bound construction** \(\max_k\binom nk2^{k-1}\) for real and complex scalars, and expressly leaves the true clique number undetermined. The present result does **not** claim that construction as new. Its new assertion is the matching universal **upper bound for all real projective vectors**, obtained through active-coordinate rounding and the signed-subset antichain inequality. The usual Sperner/LYM counting idea alone does not give the upper bound without the graph-retraction reduction from unrestricted vectors.

## Limitations
The proof uses the real scalar field in the sign-straddling test and makes no claim about the exact complex clique number. It does not classify all maximizing cliques, quantify stability, or establish a result for arbitrary norms. As with any bibliographic comparison, an unindexed earlier derivation of the matching bound cannot be completely excluded. The theorem and its diagnostics are not independently audited or independently validated.

## References
1. L. Arambašić, A. Guterman, B. Kuzma, R. Rajić, S. Zhilina, *Symmetrized Birkhoff–James orthogonality in arbitrary normed spaces*, J. Math. Anal. Appl. 502 (2021), 125203, DOI `10.1016/j.jmaa.2021.125203`, especially §§3–4 and Example 3.7. A public index dates the paper 2021-04-06.
2. A. Guterman, B. Kuzma, S. Singla, S. Zhilina, *Birkhoff–James classification of norm’s properties*, Adv. Operator Theory 9 (2024), article 43, DOI `10.1007/s43036-024-00321-0`; arXiv `2402.13416`, first posted 2024-02-20.
3. *Ternary-support cliques of order \(3^n/\sqrt n\) in the Birkhoff–James orthograph of \(\ell_\infty^n\)*, publicly available 2026 lower-bound report, identifier `2026/10/11/SCOPE-ternary-support-cliques-of-order-3-n-sqrt-n-in-the-birkhoff-jame--3cf446af3e2f`, especially Finding, Proof and Limitations.
4. The classical Lubell–Yamamoto–Meshalkin chain-counting argument for Sperner families; the signed-poset specialization and its application to Birkhoff–James cliques are proved above.

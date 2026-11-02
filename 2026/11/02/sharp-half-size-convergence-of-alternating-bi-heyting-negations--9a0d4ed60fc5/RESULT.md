# Sharp half-size convergence of alternating bi-Heyting negations

## Finding

For a finite nonempty poset \(P\) with \(n\) elements, let \(\operatorname{Up}(P)\) be its bi-Heyting algebra of upsets. Let \(\neg U\) be Heyting negation, and \(\sim V\) be the co-Heyting supplement. Starting from any upset \(U\), iterate
\[
F(U)=\sim\neg U.
\]
The least index \(s(P,U)\) for which \(F^{s(P,U)+1}(U)=F^{s(P,U)}(U)\) always satisfies
\[
s(P,U)\leq\left\lfloor\frac n2\right\rfloor.
\]
The inequality is sharp at **every** \(n\geq1\). In particular, for each positive integer \(k\), a height-two poset of size \(2k\) and an upset \(U\) have exactly \(k\) strict growth steps.

There is also an exact metric description. Form an undirected reflexive graph \(G_P\) on \(P\) by joining \(x\) and \(y\) precisely when they possess a common lower bound in \(P\). Then \(F^j(U)\) is the closed graph-distance-\(j\) neighbourhood of \(U\), for every integer \(j\geq0\). The eventual value is the union of all comparability-connected components meeting \(U\). Consequently, the fixed points of \(F\) are exactly the upsets that are also downsets (the complemented elements of \(\operatorname{Up}(P)\)).

## Assumptions and scope

The order \(\leq\) is reflexive, antisymmetric and transitive; \(P\) is finite and nonempty. Both connectives act on *upsets*, so \(U\) is an upset and all subsequent iterates remain upsets. For an arbitrary subset \(A\subseteq P\), put
\[
\uparrow A=\{x:\exists a\in A,\ a\leq x\},\qquad
\downarrow A=\{x:\exists a\in A,\ x\leq a\}.
\]
With the conventional finite-upset operations, \(\neg U=P\setminus\downarrow U\) and \(\sim V=\uparrow(P\setminus V)\). Hence
\[
F(U)=\uparrow\downarrow U.
\]
The graph is reflexive, so distance zero includes \(U\); if \(U\) is empty, all its iterates are empty and \(s(P,U)=0\). When \(U\) meets several components, take the largest finite distance from \(U\) within the components that it meets.

## Proof

**1. Algebraic operation equals graph expansion.** For \(y\in P\),
\[
y\in F(U)\iff \exists x\in U\ \exists a\in P:\ a\leq x\text{ and }a\leq y.
\]
The last condition says that \(y\) is equal or adjacent to some member of \(U\) in \(G_P\). Iterating this equivalence proves that \(F^j(U)\) is exactly the set at graph distance at most \(j\) from \(U\). In particular, every iterate is an upset, as follows independently from its algebraic definition.

**2. Eventual value and fixed points.** Two comparable elements share their lesser element as a lower bound, hence are adjacent in \(G_P\). Conversely, if \(x\) and \(y\) share a lower bound \(a\), then \(x\geq a\leq y\) is a comparability walk. Thus \(G_P\) and the undirected comparability graph have identical connected components. Finite graph expansion eventually fills exactly the components meeting \(U\). A subset is closed under both upward and downward movement precisely when it is a union of comparability components. The latter are also exactly the complemented upsets: both it and its complement are upsets.

**3. The sharp upper bound.** Let \(k=s(P,U)\). If \(k=0\), the claim is immediate. Otherwise, choose a vertex \(u_k\) at graph distance \(k\) from \(U\), and a shortest path
\[
u_0,u_1,\ldots,u_k,\qquad u_0\in U.
\]
Only \(u_0\) is in \(U\), since an intermediate vertex in \(U\) would shorten the path. We claim that \(u_0,\ldots,u_{k-1}\) are \(k\) distinct **nonminimal** elements of \(P\). If \(u_0\) were minimal, the edge \(u_0u_1\) would imply \(u_0\leq u_1\), putting \(u_1\) in the upset \(U\), a contradiction. If \(u_i\) were minimal for an internal index \(1\leq i<k\), its edges to \(u_{i-1}\) and \(u_{i+1}\) would imply \(u_i\leq u_{i-1},u_{i+1}\); hence the two neighbours would be adjacent and the path would not be shortest. Distinctness follows from shortest-path simplicity.

For each edge \(u_{i-1}u_i\), choose a minimal common lower bound \(a_i\) (possible because \(P\) is finite). All \(a_i\), for \(1\leq i\leq k\), are distinct: if \(a_i=a_j\) for \(i<j\), then \(u_{i-1}\) and \(u_j\) share that lower bound, so the segment of \(j-i+1\geq2\) edges can be shortened to a single edge. Finally, these \(k\) minimal elements cannot equal any of the \(k\) nonminimal vertices above. Therefore \(P\) has at least \(2k\) different elements, proving \(k\leq\lfloor n/2\rfloor\).

**4. Sharpness at every order.** For an integer \(k\geq1\), use a height-two poset with minimal points \(a_0,\ldots,a_{k-1}\) and maximal points \(b_0,\ldots,b_{k-1}\). Its only strict comparabilities are
\[
a_i<b_i\ (0\leq i<k),\qquad a_i<b_{i+1}\ (0\leq i<k-1).
\]
Take \(U=\{b_0\}\). The graph \(G_P\) joins consecutive maximal points \(b_i,b_{i+1}\), joins each minimal point to the maximal points directly above it, and has no further edges between distinct minimal points or nonconsecutive maximal points. Hence the terminal minimum \(a_{k-1}\) lies at graph distance exactly \(k\) from \(b_0\). No point lies farther away. Thus \(s(P,U)=k\) for \(n=2k\). For \(n=2k+1\), adjoin one isolated point; the same initial upset retains the index \(k\). For \(n=1\), every upset is fixed at index zero. This completes sharpness.

## Verification

The accompanying standalone Python checker computes \(F\) using Heyting negation and co-Heyting supplementation separately, compares every one-step output with the common-lower-bound graph expansion, and checks the bound on every upset of every transitively closed order arising from upper-triangular comparabilities for carriers of size at most six. Each poset is isomorphic to one compatible with some natural linear extension, so these cases cover all six-point isomorphism types; repetitions are allowed. The checker additionally constructs the height-two witnesses for \(1\leq k\leq50\), both with and without an isolated point. A finite computation is not the proof of the universal sharp bound: that proof is the argument above.

Run `python3 checker.py` with the standard library only. The expected final output ends in `ALL_CHECKS_OK`.

## Relationship to prior work

The interpretation of upsets as a bi-Heyting algebra is standard and explicit in Tasiou's *Profinite bi-Heyting algebras*, Example 2.6. That paper's Definition 2.1 already identifies the **least updownset** containing a subset with comparability (zigzag) connectivity. This underlying fixed-point description is therefore **not** claimed as new. Badia, Kowalski and Olkhovikov (2026) supply contemporary bi-intuitionistic Kripke semantics and expressivity motivation. Stell and Worboys (1997) discuss Heyting and co-Heyting operations in region algebra. The specific contribution assessed here is the **finite sharp \(\lfloor n/2\rfloor\) iteration bound**, its graph-metric derivation and the height-two extremal family. No prior covering statement was found in the inspected sources or targeted literature searches; historical priority is not independently certified.

## Limitations

The statement is restricted to finite posets, upsets, and the specific unary composite \(F=\sim\neg\). It does not assert an optimal lower bound on the *general* formula depth needed to describe the connected-component closure using arbitrary connectives, nor a corresponding finite bound for infinite posets. Graph-distance identities and the upper bound are proved analytically; enumerated examples alone are not a universal proof. General lattice-theoretic closure-iteration results could subsume this special case under different terminology, and independent external review has not been performed.

## References

1. G. Badia, T. Kowalski, G. Olkhovikov, *Definable Classes of Models and Frames in Bi-intuitionistic Logic*, arXiv:2607.18956, first posted 2026-07-21. https://arxiv.org/abs/2607.18956
2. L. Tasiou, *Profinite bi-Heyting algebras*, Algebra Universalis 86, article 16 (2025), https://doi.org/10.1007/s00012-025-00892-w (published 2025-05-09).
3. J. G. Stell, M. F. Worboys, *The Algebraic Structure of Sets of Regions*, COSIT 1997, pp. 163–174, https://doi.org/10.1007/3-540-63623-4_49; lawful author's copy: https://www.worboys.org/publications/cosit1997.pdf.

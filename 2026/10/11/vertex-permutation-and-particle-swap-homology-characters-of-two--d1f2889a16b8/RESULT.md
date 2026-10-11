# Vertex-permutation and particle-swap homology characters of two-point sink configurations on complete graphs

## Finding

For every integer \(m\ge4\), consider two **labeled** particles on the usual one-dimensional realization of the complete graph \(K_m\). Both particles may occupy the same point **only when it is an original graph vertex**. Denote this space by \(Y_m=\operatorname{Conf}^{\mathrm{sink}}_2(K_m,V(K_m))\), write \(E=\binom m2\), and let \(b=E-m+1=\binom{m-1}{2}\). Its integral homology is
\[
H_i(Y_m;\mathbb Z)\cong
\begin{cases}
\mathbb Z,&i=0,\\
\mathbb Z^{2b},&i=1,\\
\mathbb Z^{b^2-E},&i=2,\\
0,&i\ge3.
\end{cases}
\]
In particular there is no integral homology torsion. The labels and vertices determine a commuting action of \(S_m\times C_2\), where the generator \(\tau\) of \(C_2\) exchanges particle labels.

For \(\pi\in S_m\), let \(f(\pi)\) be the number of fixed vertices, let \(t(\pi)\) be the number of cycles of length two in its disjoint-cycle decomposition, and define
\[
p(\pi)=\binom{f(\pi)}2-t(\pi)-f(\pi)+1,
\qquad F(\pi)=\binom{f(\pi)}2+t(\pi).
\]
The complete rational homology characters are
\[
\begin{aligned}
\chi_{H_1}(\pi,1)&=2p(\pi),&\quad
\chi_{H_1}(\pi,\tau)&=0,\\
\chi_{H_2}(\pi,1)&=p(\pi)^2-F(\pi),&
\chi_{H_2}(\pi,\tau)&=F(\pi)-p(\pi^2).
\end{aligned}
\]
For example, the pure label swap has traces \(0\) and \(m-1\) on first and second homology, respectively.

There is also a natural structural description. Let \(U=H_1(K_m;\mathbb Q)\), considered as a subspace of the oriented edge-chain space. If \(Q\) takes two graph cycles, multiplies their oriented-edge coefficients coordinatewise, and extends linearly to \(U\otimes U\), then \(Q:U\otimes U\twoheadrightarrow\mathbb Q^E\) is surjective and
\[
H_2(Y_m;\mathbb Q)\cong\ker Q,\qquad
H_2(Y_m;\mathbb Q)^+\cong\bigwedge^2U,\qquad
H_2(Y_m;\mathbb Q)^-\cong\ker\left(\operatorname{Sym}^2U\longrightarrow\mathbb Q^E\right).
\]
The signs denote eigenvalues of the label swap, **not** parities of vertex permutations. In addition, \(H_1(Y_m;\mathbb Q)\) is the pair of copies of \(U\) exchanged by \(\tau\).

## Assumptions and scope

The graph has exactly the standard \(m\) zero-cells and \(\binom m2\) one-cells, and **every** zero-cell is a sink. Neither interior-edge collisions nor coincidences at newly inserted subdivision points are permitted. The space is **ordered**, not the unlabeled quotient. The group \(S_m\) acts by relabeling vertices; \(\tau\) acts by transposing the particle coordinates. The bound \(m\ge4\) is essential to the proof: every edge requires two distinct additional triangle vertices. For \(m=3\), the graph is a triangle and the analogous sink configuration space has first Betti number four, rather than the continuation of the displayed formula.

## Proof

**1. A natural cellular model.** The discrete sink configuration theorem of Ramos, Definition 3.1 and Theorem 3.2 of [2], identifies the homotopy type with the cubical subcomplex \(Y\subset X=K_m\times K_m\) obtained by deleting precisely the interiors of the \(E\) diagonal squares \(e\times e\), one per graph edge \(e\). The inclusion of this subcomplex in the continuous sink configuration space is equivariant for graph automorphisms and label exchange. All zero-cells and one-cells of \(X\) remain in \(Y\), so \(Y\) is connected and has dimension at most two.

**2. Relative homology and the coefficient map.** Orient each graph edge \(e=\{a,b\}\) from smaller to larger vertex. Since the cellular quotient \(C_*(X)/C_*(Y)\) has only the \(E\) degree-two generators \([e\times e]\), the relevant integral long exact sequence is
\[
0\longrightarrow H_2(Y;\mathbb Z)\longrightarrow
H_1(K_m;\mathbb Z)\otimes H_1(K_m;\mathbb Z)
\xrightarrow{Q}\mathbb Z^E\longrightarrow
H_1(Y;\mathbb Z)\longrightarrow
H_1(K_m;\mathbb Z)^{\oplus2}\longrightarrow0.
\]
Here the Künneth identification is integral: the graph homology groups are free. Write a cycle \(c\) as an integer oriented-edge vector \((c_e)_{e\in E}\). The cellular product cycle \(c\times d\) has coefficient \(c_e d_e\) on the diagonal square \(e\times e\); hence
\[
Q(c\otimes d)=(c_e d_e)_{e\in E}.
\]
This is a map of \(S_m\times C_2\)-modules. Under a graph permutation, a diagonal square receives the *square* of its edge orientation sign and is therefore merely permuted. Under \(\tau\), its two one-dimensional factors are exchanged and its orientation is reversed. Thus \(\mathbb Z^E\) is the signed-by-\(\tau\) permutation module on the unoriented edges.

**3. Integral surjectivity, with an explicit unit witness for each edge.** Take any edge \(e=\{a,b\}\). Because \(m\ge4\), choose distinct vertices \(c,d\) outside \(\{a,b\}\). Let \(z_{abc}\) and \(z_{abd}\) be consistently oriented integral triangle cycles on \(a,b,c\) and \(a,b,d\). Their edge supports intersect **only** at \(\{a,b\}\); their edgewise product is \(\pm\mathbf e_{ab}\). Thus every standard basis vector of \(\mathbb Z^E\) lies in the image of \(Q\), proving integral surjectivity rather than merely rational rank. Exactness now gives \(H_1(Y;\mathbb Z)\cong H_1(K_m;\mathbb Z)^{\oplus2}\) and \(H_2(Y;\mathbb Z)=\ker Q\). Since this is a subgroup of a free abelian group, it is free of rank \(b^2-E\); the first homology has rank \(2b\). Higher homology vanishes by the two-dimensional model.

**4. Equivariant characters.** For \(\pi\in S_m\), the trace on vertex chains \(C_0(K_m;\mathbb Q)\) is \(f(\pi)\). An oriented edge contributes \(+1\) if both endpoints are fixed, contributes \(-1\) if its endpoints form one two-cycle, and contributes zero otherwise. Therefore \(\operatorname{Tr}(\pi\mid C_1)=\binom{f(\pi)}2-t(\pi)\). The cellular exact sequence of a connected graph gives
\[
\operatorname{Tr}(\pi\mid U)=p(\pi).
\]
The vertex group acts diagonally on \(U\oplus U\) and \(U\otimes U\), whereas \(\tau\) exchanges the two degree-one homology summands and acts on \(U\otimes U\) by *minus* the flip (the graded sign for two degree-one factors). The edge-permutation module has trace \(F(\pi)\) for \((\pi,1)\) and \(-F(\pi)\) for \((\pi,\tau)\). Consequently its equivariant short exact sequence gives
\[
\chi_{H_2}(\pi,1)=\operatorname{Tr}(\pi\otimes\pi\mid U\otimes U)-F(\pi)=p(\pi)^2-F(\pi).
\]
The linear-algebra identity \(\operatorname{Tr}((A\otimes A)\operatorname{flip})=\operatorname{Tr}(A^2)\) similarly gives
\[
\chi_{H_2}(\pi,\tau)=-p(\pi^2)+F(\pi).
\]
The corresponding first-homology characters are \(2p(\pi)\) and zero. Finally, because \(Q(c\otimes d)=Q(d\otimes c)\), it vanishes on \(\bigwedge^2 U\), which is the \(\tau=+1\) subspace of \(U\otimes U\); its \(\tau=-1\) subspace is the kernel on \(\operatorname{Sym}^2 U\). This completes the representation statement for every \(m\ge4\).

## Verification

The standalone Python 3 script `verify_sink_complete.py` reconstructs the exact signed cubical boundary formulas, checks \(\partial_1\partial_2=0\), constructs all edge-by-edge triangle-pair unit witnesses, computes ranks over \(\mathbb F_2,\mathbb F_3,\mathbb F_5,\mathbb F_7\), and exhaustively checks signed cellular Lefschetz traces against the claimed characters for every element of \(S_m\times C_2\) when \(m=4,5,6\). Its recorded output is `verification_results.json`. The \(0\)-, \(1\)-, \(2\)-cell counts respectively are \((16,48,30)\), \((25,100,90)\), and \((36,180,210)\); the Betti vectors are \((1,6,3)\), \((1,12,26)\), and \((1,20,85)\). All \(48+240+1440\) group elements pass the Lefschetz check. These finite tests cross-check the **independent all-parameter proof**; they are not substituted for it. Reproduce from a clean directory by running `python3 verify_sink_complete.py` and comparing its JSON output with `verification_results.json`.

## Relationship to prior work

Chettih and Lütgehetmann [1], first publicly posted 2016-12-25, introduce graph sink configuration spaces and calculate cases with trees or single cycles. Ramos [2] establishes the general natural cubical model and studies tree homology and large-particle stability, but does not supply the claimed all-complete-graph integral edgewise product sequence and full \(S_m\times C_2\) characters. González and González [3] calculate cohomology for two particles on complete graphs when **all coincidences are prohibited**, a different configuration space. Ramos and He Yun [4], Theorem 3.8, give stable \(S_m\)-representations for that collision-free space, again not the sink space. The distinction is substantial: for \(K_5\), [3] gives an ordinary collision-free configuration space of a closed genus-six surface, with second Betti number one, whereas the sink configuration space has second Betti number \(26\).

## Limitations

The result is restricted to **two labeled particles**, **complete graphs**, and a sink set consisting of **exactly all original vertices**. It determines integral additive homology and the rational representations, not the fundamental group, integral module isomorphism classes, homology ring, or arbitrary graphs/particle numbers. The finite calculations cover only \(m\in\{4,5,6\}\). The literature comparison is bounded to the sources specified below and cannot certify absolute novelty.

## References

[1] S. Chettih and D. Lütgehetmann, *The homology of configuration spaces of trees with loops*, arXiv:1612.08290v1 (first public 2016-12-25), especially §2; Algebraic & Geometric Topology 18 (2018), 2443–2469; primary MSC 55R80.

[2] E. Ramos, *Configuration spaces of graphs with certain permitted collisions*, arXiv:1703.05535v1 (first public 2017-03-16), Definition 3.1, Theorem 3.2, Remark 3.3, and the tree calculations.

[3] E. J. González and J. González, *An algorithmic discrete gradient field and the cohomology algebra of configuration spaces of two points on complete graphs*, arXiv:2207.07046v1 (first public 2022-07-14).

[4] E. Ramos and C. He Yun, *Computing stable homology representations of graph configuration spaces*, arXiv:2606.13813v1 (first public 2026-06-11), Theorem 3.8 and Table 1 (ordinary collision-free configurations).

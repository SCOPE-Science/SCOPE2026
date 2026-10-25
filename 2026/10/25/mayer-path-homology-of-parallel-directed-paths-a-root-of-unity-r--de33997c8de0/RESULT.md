# Mayer path homology of parallel directed paths: a root-of-unity resonance law

## Finding

A complete formula is obtained for *all* complex Mayer path-homology groups of an arbitrary consistently oriented, multiarm theta digraph. The formula separates two unrelated mechanisms: a root-of-unity congruence among path lengths, which changes the degree-zero and first one-step homology, and parallel two-edge arms, which produce additional second-degree classes for sufficiently large nilpotency order.

Fix integers \(r\ge 3\) and \(\ell_1,\ldots,\ell_r\ge2\). Let \(D(\ell_1,\ldots,\ell_r)\) have two distinguished vertices \(s,t\) joined by \(r\) internally vertex-disjoint directed paths, each oriented entirely from \(s\) to \(t\), of respective lengths \(\ell_i\). There are no additional arcs. Write
\[
E=\sum_{i=1}^r\ell_i,\qquad V=E-r+2,\qquad a=|\{i:\ell_i=2\}|,\qquad h=\max(a-1,0).
\]
Let \(N\ge3\), and let \(\xi\) be a primitive complex \(N\)-th root of unity. Define the order
\[
\rho=\operatorname{ord}(-\xi)=
\begin{cases}2N&N\text{ odd},\\N&4\mid N,\\N/2&N\equiv2\pmod4,\end{cases}
\]
and let \(\delta=1\) if all \(\ell_i\) are congruent modulo \(\rho\), otherwise \(\delta=0\). For every \(1\le q\le N-1\), the dimensions of the *nonaugmented* Mayer path homology over \(\mathbb C\) are
\[
\dim H_0^{N,q}(D)=\begin{cases}
\delta&q=N-1,\\V-h&q=N-2,\\V&1\le q\le N-3,
\end{cases}
\]
\[
\dim H_1^{N,q}(D)=\begin{cases}
r-2+\delta&q=1,\\ E-h&q=N-1,\\ E&2\le q\le N-2,
\end{cases}
\qquad
\dim H_2^{N,q}(D)=\begin{cases}
h&3\le q\le N-1,\\0&q=1,2.
\end{cases}
\]
All groups \(H_d^{N,q}(D)\) in degrees \(d\ge3\) vanish. Empty case ranges are ignored; for example, when \(N=3\), there is no positive degree-two group. The formula applies to every allowed tuple and every primitive \(N\)-th root, with no equal-arm assumption.

## Assumptions and scope

Use the Mayer \(N\)-differential on regular directed paths of Karaguler--Wei, with
\[
\partial[v_0,\ldots,v_d]=\sum_{j=0}^{d}\xi^j[v_0,\ldots,\widehat v_j,\ldots,v_d],\qquad \partial^N=0.
\]
Let \(A_d\) be the complex vector space spanned by allowed directed \(d\)-paths, and \(A_d=0\) for \(d<0\). Let
\[
\Omega_d^N=\bigcap_{j=1}^{N-1}\{x\in A_d:\partial^j x\in A_{d-j}\},
\qquad H_d^{N,q}=\ker(\partial^q:\Omega_d^N\to\Omega_{d-q}^N)/\operatorname{im}(\partial^{N-q}:\Omega_{d+N-q}^N\to\Omega_d^N).
\]
This is the nonaugmented convention \(\Omega_{-1}^N=0\), and all homology is taken over \(\mathbb C\). Every directed path in the specified graph has distinct vertices because the digraph is acyclic. Distinct arms have no common internal vertex.

## Proof

**1. No invariant paths in degrees at least three.** Every allowed \(d\)-path with \(d\ge3\) lies on exactly one arm and is a consecutive subpath of that arm. Removing its second vertex produces a path with a missing shortcut between its first and third vertices; this is a forbidden \((d-1)\)-path. That forbidden face determines the original \(d\)-path uniquely (the named internal vertices cannot lie on two different arms, and the directed chain cannot branch except at \(s\)). Its coefficient in \(\partial\) is \(\xi\ne0\). Thus the projection of \(\partial:A_d\to\) the vector space of forbidden \((d-1)\)-paths has independent columns. Hence \(\Omega_d^N=0\) for all \(d\ge3\), including those \(d\) greater than the longest arm length.

**2. The entire invariant two-chain space.** An allowed two-path has the form \([u,v,w]\), with consecutive arcs on an arm, and
\[
\partial[u,v,w]=[v,w]+\xi[u,w]+\xi^2[u,v].
\]
The middle face \([u,w]\) is not an arc. If the two-path is not a whole arm of length two, its forbidden middle face occurs for no other allowed two-path, so its coefficient must vanish in any invariant chain. For each length-two arm there is one path \(p_i=[s,u_i,t]\). Its forbidden face is always the same \([s,t]\). Thus
\[
\Omega_2^N=\left\{\sum_{\ell_i=2}c_i p_i:\sum_{\ell_i=2}c_i=0\right\},\qquad\dim\Omega_2^N=h.
\]
The space satisfies the higher-invariance conditions because the \(\partial\) of every such chain is an allowed one-chain and its iterated boundaries lie in the zero-chain or zero spaces. In fact,
\[
\partial\sum c_i p_i=\sum c_i\bigl([u_i,t]+\xi^2[s,u_i]\bigr),\quad
\partial^2\sum c_i p_i=(\xi+\xi^2)\sum c_i[u_i].
\]
The \(u_i\) are distinct and \(\xi+\xi^2=\xi(1+\xi)\ne0\) for \(N\ge3\). Therefore both maps \(\partial:\Omega_2^N\to\Omega_1^N\) and \(\partial^2:\Omega_2^N\to\Omega_0^N\) have rank \(h\). The second formula also proves their injectivity without an assumption on \(a\).

**3. Weighted edge incidence and resonance.** The degree-one boundary of an edge is \(\partial[u,v]=[v]+\xi[u]\). Let \(y\) be a linear functional annihilating all degree-one boundaries. For every arc \(u\to v\), its coefficients satisfy \(y_v=-\xi y_u\). Hence along arm \(i\),
\[
 y_t=(-\xi)^{\ell_i}y_s.
\]
Every vertex is determined by its coefficient at \(s\). Such a nonzero functional exists exactly when the \(r\) powers coincide, i.e. exactly when \(\delta=1\). It then spans the left nullspace, so
\[
\operatorname{rank}(\partial:\Omega_1^N\to\Omega_0^N)=V-\delta,\qquad
\dim\ker(\partial:\Omega_1^N\to\Omega_0^N)=E-V+\delta=r-2+\delta.
\]
Because \(-\xi\) has order \(\rho\), the all-equal-power condition is exactly the displayed congruence of lengths, independent of which primitive \(N\)-th root was selected.

**4. Quotients defining each homology group.** We have \(\dim\Omega_0^N=V\), \(\dim\Omega_1^N=E\), \(\dim\Omega_2^N=h\), and no higher chains. In degree zero, the numerator of the Mayer quotient has dimension \(V\). A denominator is present only for \(N-q=1\) (rank \(V-\delta\)) or \(N-q=2\) (rank \(h\)); otherwise it is zero. In degree one, the numerator has dimension \(r-2+\delta\) when \(q=1\), otherwise \(E\); the only nonzero denominator comes from \(N-q=1\), with rank \(h\). In degree two, \(\partial\) and \(\partial^2\) are injective, so the numerator vanishes for \(q=1,2\) and has dimension \(h\) for \(q\ge3\); its denominator always vanishes. This proves every formula and all quantifiers in the finding.

## Verification

A standalone exact modular-linear-algebra program, `verify.py`, enumerates directed allowed paths independently and computes the forbidden-face matrices, the invariant two-chain kernel, all relevant differential ranks, and the resulting dimensions for every \(N,q\) in the tested range. It checks \(2{,}688\) graph/order configurations using \(N\in\{3,4,5,6,7,8,10,12\}\), arm counts \(r=2,3,4\), and individual lengths from \(\{2,3,4,5\}\). The \(r=2\) cases serve as controls; the theorem is stated for \(r\ge3\). Each primitive root is implemented in an exact finite field of characteristic coprime to \(N\), and all assertions pass. The infinite classification rests on the proof above, not on finite-field extrapolation. Execute `python3 verify.py` (Python standard library only) to reproduce the tests and the output in `verify_output.txt`.

## Relationship to prior work

Karaguler and Wei, *Mayer Path Homology* (arXiv:2605.16525v1, first public May 15, 2026), introduce the underlying \(N\)-chain theory, classify general local generator types for invariant two- and three-paths, discuss small directed motifs, and supply general descriptions of first Mayer cycles. Those definitions and results are foundational and **not** asserted to be new. The present result instead computes *all degree/order homology ranks for every multiarm directed theta*, including unequal lengths, the precise order-of-\(-\xi\) resonance, and the independent two-edge-arm correction. The paper's general generator lists do not themselves give this two-parameter rank table. A semantic comparison of accessible mathematical records identified related results for ordinary path homology and complete transitively layered digraphs, not this full Mayer theta classification. This is a bounded priority comparison rather than proof of global uniqueness.

## Limitations

The result is restricted to consistently oriented internally vertex-disjoint multiarm digraphs with no direct pole-to-pole edge, over \(\mathbb C\), with \(N\ge3\) and \(r\ge3\). It does not classify arbitrary overlapping paths or other coefficient rings. The proof concerns dimensions of homology groups, not naturality under arbitrary graph maps, functorial operators, or their multiplicative structure. Independence from the primitive-root choice follows only for the stated dimension formulas. Priority remains subject to unindexed or inaccessible literature, and the computational test is finite.

## References

1. Dilan Karaguler and Guo-Wei Wei, *Mayer Path Homology*, arXiv:2605.16525v1 (submitted May 15, 2026), https://arxiv.org/abs/2605.16525. Definitions of the \(N\)-path complex and the Mayer quotient; Sections 3.1 and 3.2 on allowed generators and first cycles.
2. Dilan Karaguler and Guo-Wei Wei, *Mayer path homology*, *Foundations of Data Science*, early online September 20, 2026, DOI:10.3934/fods.2026025 (journal version of reference 1).

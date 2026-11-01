# Vertex-permutation homology and holonomy resonance for cyclic-layer digraphs

## Finding

Let \(n\ge3\), let \(a_0,\ldots,a_{n-1}\) be positive integers, and let \(G=G(n;\mathbf a)\) be the loopless digraph whose vertex set is a disjoint union \(V_0\sqcup\cdots\sqcup V_{n-1}\), with \(|V_i|=a_i\). There is an arc from every vertex of \(V_i\) to every vertex of \(V_{i+1}\), with subscripts interpreted modulo \(n\), and no other arcs. Fix \(N\ge3\) and a primitive \(N\)-th root of unity \(\xi\in\mathbb C\). Use the regular Mayer path complex and the \(N\)-differential of Karaguler--Wei, with \(q=N-1\).

**Theorem.** The canonical map
\[
\Phi:\mathbb C[V(G)]\longrightarrow H_1^{N,N-1}(G;\mathbb C),\qquad
\Phi([x])=\frac1{a_{i+1}}\sum_{y\in V_{i+1}}[x,y]
\quad(x\in V_i)
\]
is a linear isomorphism, equivariant under every layer-preserving vertex permutation and every cyclic rotation of the layers that preserves the size sequence. In particular,
\[
\dim_{\mathbb C}H_1^{N,N-1}(G)=\sum_{i=0}^{n-1}a_i,
\qquad
\operatorname{tr}\bigl(g\mid H_1^{N,N-1}(G)\bigr)=\#\operatorname{Fix}_{V(G)}(g).
\]
Moreover, if
\[
\nu_N=\frac{2N}{\gcd(N+2,2N)}
=\begin{cases}2N&N\text{ odd},\\N&N\equiv0\pmod4,\\N/2&N\equiv2\pmod4,\end{cases}
\]
then
\[
H_0^{N,N-1}(G;\mathbb C)\cong
\begin{cases}\mathbb C&\nu_N\mid n,\\0&\nu_N\nmid n.\end{cases}
\]
When this degree-zero group is nonzero, the subgroup permuting vertices inside layers acts trivially, while rotation by \(s\) layers acts by the scalar \((-\xi)^s\). These statements are independent of the layer sizes and require no restriction on their growth.

For example, at \(N=3\) the degree-zero group survives exactly when \(6\mid n\), but the degree-one group always has dimension equal to the total number of vertices. When \(a_i=m\) for every \(i\), the latter is the ordinary \(mn\)-dimensional vertex-permutation representation of \(S_m^n\rtimes C_n\).

## Assumptions and scope

The ground field is \(\mathbb C\). The digraph is simple, has no loops, and uses precisely the complete forward arcs between successive layers. Every \(a_i\) is a positive integer, \(n\ge3\), and \(N\ge3\). For an allowed elementary \(p\)-path, the Mayer boundary is
\[
\partial(v_0,\ldots,v_p)=\sum_{j=0}^p\xi^j(v_0,\ldots,\widehat{v_j},\ldots,v_p),
\]
with nonregular terms set to zero. The \(N\)-invariant subspace \(\Omega_p^N\) consists of allowed chains whose successive boundaries through order \(N-1\) remain allowed; all negative-degree chain groups vanish. At \(q=N-1\), the relevant groups are
\[
H_1^{N,N-1}=\Omega_1^N/\partial\Omega_2^N,
\qquad H_0^{N,N-1}=\Omega_0^N/\partial\Omega_1^N,
\]
because \(\partial^{N-1}\) vanishes on degree-one and degree-zero chains. Square brackets on an arrow in \(\Phi\) denote its class modulo \(\partial\Omega_2^N\), not a closed ordinary one-cycle.

## Proof

Write \(W_i=\mathbb C[V_i]\), and let \(\epsilon_i:W_i\to\mathbb C\) sum coordinates. Choose the permutation-invariant vector \(w_i=a_i^{-1}\sum_{v\in V_i}[v]\), so that \(\epsilon_i(w_i)=1\), and put \(U_i=\ker\epsilon_i\). Thus \(W_i=\mathbb Cw_i\oplus U_i\) equivariantly under \(S_{a_i}\).

**Step 1: the invariant two-path space.** Every directed two-path runs from a vertex of \(V_i\), through \(V_{i+1}\), to \(V_{i+2}\). Since \(n\ge3\), no shortcut from \(V_i\) to \(V_{i+2}\) is an arc. The only potentially forbidden term of its boundary is the middle-deletion shortcut, with nonzero coefficient \(\xi\). Distinct ordered endpoint pairs cannot cancel each other's shortcut. Consequently,
\[
\Omega_1^N=\bigoplus_i W_i\otimes W_{i+1},\qquad
\Omega_2^N=\bigoplus_i W_i\otimes U_{i+1}\otimes W_{i+2}.
\]
The extra tests \(\partial^j c\in\mathcal A_{2-j}\) for \(j\ge2\) impose no further conditions in degree two: a second boundary is already a combination of vertices and higher boundaries vanish. This argument covers \(n=3\) without assuming that longer paths avoid returning to a layer.

**Step 2: determine the entire image of the two-path boundary.** The shortcut component is zero on the displayed tensor product. For \(x\in W_i\), \(u\in U_{i+1}\), \(z\in W_{i+2}\), the boundary has precisely two allowed components:
\[
\partial(x\otimes u\otimes z)
=\xi^2\epsilon_{i+2}(z)(x\otimes u)_{E_i}
+\epsilon_i(x)(u\otimes z)_{E_{i+1}},
\]
where \(E_i=W_i\otimes W_{i+1}\) is the vector space of arrows from \(V_i\) to \(V_{i+1}\).

Decompose each \(E_i\) into the four subspaces
\[
\mathbb Cw_i\otimes\mathbb Cw_{i+1},\quad
U_i\otimes\mathbb Cw_{i+1},\quad
\mathbb Cw_i\otimes U_{i+1},\quad
U_i\otimes U_{i+1}.
\]
The boundary image contains every \(U_i\otimes U_{i+1}\), by taking \(x\in U_i\) and \(z=w_{i+2}\). The other use of an augmentation vector, \(x=w_i\) and \(z\in U_{i+2}\), yields the corresponding \(U_{i+1}\otimes U_{i+2}\) summand. Finally, taking both outer vectors normalized yields, for each \(u\in U_{i+1}\), the relation
\[
\xi^2(w_i\otimes u)_{E_i}+(u\otimes w_{i+2})_{E_{i+1}}.
\]
The preceding cases exhaust the tensor products in \(W_i\otimes U_{i+1}\otimes W_{i+2}\). Different \(U_j\)-blocks live in disjoint direct-sum components, so no additional relations exist. The quotient of \(\bigoplus_iE_i\) by \(\partial\Omega_2^N\) is therefore precisely the direct sum of the outgoing spaces
\[
\bigoplus_i\bigl(W_i\otimes\mathbb Cw_{i+1}\bigr).
\]
Under this identification, \(\Phi\) sends \(x\in W_i\) to \(x\otimes w_{i+1}\). Thus it is an isomorphism. All choices were normalized orbit averages and the construction commutes with within-layer permutations and admissible cyclic rotations. This proves the degree-one and character assertions for every \(N\ge3\).

**Step 3: degree zero and resonance.** For an arrow \(x\to y\), the degree-one boundary is \(\partial(x,y)=[y]+\xi[x]\). In the quotient by all such boundaries, every vertex in the same layer has the same class, and the classes in successive layers satisfy \([V_{i+1}]=-\xi[V_i]\). A circuit gives \([V_0]=(-\xi)^n[V_0]\). Hence the quotient is one-dimensional if \((-\xi)^n=1\) and zero otherwise. Write \(\xi=\exp(2\pi i k/N)\) with \(\gcd(k,N)=1\). Then the order of \(-\xi\) is \(2N/\gcd(N+2k,2N)\). The common divisor is \(1\) for odd \(N\), \(2\) for \(N\equiv0\pmod4\), and \(4\) for \(N\equiv2\pmod4\), because any odd common divisor would divide both \(N\) and \(k\). Thus this order is \(\nu_N=2N/\gcd(N+2,2N)\), independent of the primitive root. Rotating by \(s\) layers carries \([V_0]\) to \([V_s]=(-\xi)^s[V_0]\). Within-layer permutations fix it. This completes the proof.

## Verification

The included `verify.py` builds the digraph and all allowed directed two-paths, forms the actual root-of-unity boundary matrices over a finite field, independently obtains \(\Omega_2^N\) as the kernel of the missing-shortcut matrix, and checks both homology dimensions. It also checks that the explicit averaged-outgoing-arc map complements the two-boundary image, and reconstructs the induced quotient characters for layer permutations and admissible rotations.

Executing `python3 verify.py` prints a `VERIFY_OK` line. The fixed test corpus contains 261 parameter cases, including 205 quotient-character cases, with 2,267 vertices, 4,102 arcs, 7,888 two-paths, and 3,786 directly computed basis vectors of invariant two-path spaces in aggregate. These are finite consistency checks; the unrestricted conclusion follows from the three symbolic steps above.

## Relationship to prior work

Karaguler and Wei introduced Mayer path homology and its \(N\)-differential, classified local low-degree invariant-path generators, and characterized weighted degree-one cycles. Their original May 15, 2026 preprint does not state the cyclic-layer quotient module, its full symmetry character, or the degree-zero cyclic holonomy criterion. In particular, knowing possible local generator types is not the same as calculating all global relations in the cyclic blow-up.

Related exact results for transitively layered (acyclic) digraphs concern a different graph family, with no closing layer-to-first-layer arcs. The published ordinary-path-homology classification of forward-shift blow-ups concerns the \(N=2\) theory, not the root-of-unity Mayer quotient here. The present theorem is not asserted to extend those results automatically. Full texts of those two specifically indexed related notes were not available for direct inspection; their indexed mathematical statements were compared, so an unindexed reformulation remains an originality risk.

## Limitations

Only the \(q=N-1\) level and homological degrees zero and one are classified. The theorem does not address the other levels \(q\), higher homological degrees, digraphs with omitted forward arcs, reverse arcs, or non-cyclic layer adjacency. The proof works over \(\mathbb C\), where the integer layer sizes are invertible; no integral or positive-characteristic extension is claimed. The originality assessment is based on accessible full-text sources and indexed statements, not an exhaustive theorem registry.

## References

1. D. Karaguler and G.-W. Wei, *Mayer Path Homology*, arXiv:2605.16525, first posted 2026-05-15; published in *Foundations of Data Science*, DOI 10.3934/fods.2026025 (2026). Definitions 6--8 and Sections 3.1--3.2. https://arxiv.org/abs/2605.16525
2. *Augmentation-block characters of Mayer path homology on layered digraphs*, publicly indexed mathematical finding, 2026-10-11. https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-augmentation-block-characters-of-mayer-path-homology-on-layered--b242671c032d (indexed statement only examined).
3. *Forward-shift blow-ups preserve digraph homotopy type*, publicly indexed mathematical finding, 2026-10-11. https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-forward-shift-blow-ups-preserve-digraph-homotopy-type--1f84401a7952 (indexed statement only examined).

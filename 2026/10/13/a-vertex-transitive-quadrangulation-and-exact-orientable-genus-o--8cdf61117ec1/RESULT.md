# A vertex-transitive quadrangulation and exact orientable genus of the bipartite Kneser graph \(H(8,3)\)

## Finding

The bipartite Kneser graph \(H(8,3)\) has a vertex-transitive cellular orientable quadrangulation. Its orientable genus is
\[
\boxed{\gamma(H(8,3))=85}.
\]
The exhibited embedding has 112 vertices, 560 edges, and 280 faces, each bounded by a simple four-cycle. This sharpens the previously published bounds \(85\le\gamma(H(8,3))\le143\).

## Assumptions and scope

Throughout, graphs are finite, simple, and undirected. For integers \(n>2k\), the bipartite Kneser graph \(H(n,k)\) has two disjoint copies of the \(k\)-subsets of an \(n\)-element set as its vertex classes; two vertices are adjacent precisely when their underlying subsets are disjoint. An orientable rotation system specifies one cyclic order of incident edges at each vertex; it produces an orientable cellular embedding by the standard dart-permutation construction. Its genus is computed by \(V-E+F=2-2g\).

Identify the eight-element ground set with \(\mathbb F_8=\mathbb F_2[t]/(t^3+t+1)\), writing the element \(b_0+b_1t+b_2t^2\) as the integer with binary digits \(b_2b_1b_0\). Thus addition is bitwise exclusive-or and multiplication is polynomial multiplication modulo \(t^3+t+1\). Let \(\Gamma=\{(a,b):a\in\mathbb F_8^\times,\ b\in\mathbb F_8\}\), with \((a,b)(c,d)=(ac,ad+b)\). The pair \((a,b)\) denotes \(x\mapsto ax+b\). Fix \(P=\{0,1,t\}=\{0,1,2\}\).

The 56 elements of \(\Gamma\) carry \(P\) bijectively to all 56 three-subsets of \(\mathbb F_8\); hence \(gP\) uniquely labels one triple. Write \(A_g\) and \(B_g\) for its two graph copies. Define \(S=\{s\in\Gamma:P\cap sP=\varnothing\}\). This set has ten elements, excludes the identity, and is closed under inversion. The edge relation is exactly \(A_g\sim B_{gs}\) for \(s\in S\).

## Proof

**Step 1: explicit rotation certificate.** Encode elements of \(\Gamma\) as the pair \((a,b)\). In the first vertex class choose the following cyclic order \(\rho\) on \(S\), read from left to right and cyclically:

```
(1,4) (1,5) (1,6) (5,6) (3,5)
(1,7) (2,7) (4,7) (7,3) (6,3)
```

These ten entries are distinct and exhaust \(S\). Let \(\iota(s)=s^{-1}\) be inversion in \(\Gamma\) and define \(\rho_B=\iota\rho^{-1}\iota\). Since \(\rho\) is a ten-cycle and inversion is a bijection of \(S\), so is \(\rho_B\). Give \(A_g\) the cyclic order \(B_{g s}\), where \(s\) travels under \(\rho\). Give \(B_g\) the cyclic order \(A_{g s^{-1}}\), where \(s\) travels under \(\rho_B\). Every neighbor appears exactly once, so this is a valid rotation system on \(H(8,3)\).

**Step 2: all faces are simple quadrilaterals.** Every dart is a directed edge \((v,w)\). If \(\operatorname{next}_w(v)\) is the successor of \(v\) in the local order at \(w\), the face permutation is \((v,w)\mapsto(w,\operatorname{next}_w(v))\). The accompanying checker reconstructs the graph from actual three-subsets and enumerates *all 1120 darts*, finding exactly 280 orbits; each orbit has length four and uses four distinct vertices. In addition, the second checker independently verifies the local product-and-closure identities behind the four-step face permutation. Thus the graph has a connected orientable cellular embedding with \(F=280\) simple quadrilateral faces. By Euler's formula its genus is \((2-112+560-280)/2=85\).

For a local algebraic check, fix \(s_0\in S\). Define \(s_1=\rho^{-1}(s_0^{-1})\), \(s_2=\rho(s_1^{-1})\), and \(s_3=\rho^{-1}(s_2^{-1})\). Direct substitution of the displayed ten-cycle into the finite-field group law verifies, for *every* \(s_0\in S\), the two identities
\[
s_0s_1s_2s_3=1_\Gamma,\qquad \rho(s_3^{-1})=s_0.
\]
They ensure that the face permutation closes after four steps. The checker additionally verifies there are no shorter face orbits; in particular all facial walks are simple four-cycles. The exhaustive finite identities are a complete certificate for the explicitly defined 112-vertex graph, not a finite approximation to a claim about unbounded graph order.

**Step 3: vertex transitivity.** Each left multiplication \(A_g\mapsto A_{hg}\), \(B_g\mapsto B_{hg}\) preserves the local cyclic orders, giving a transitive action on each 56-vertex class. Because \(S^{-1}=S\), swapping the classes by \(A_g\leftrightarrow B_g\) preserves adjacency. It reverses local orientation, since the opposite-class cyclic order is \(\iota\rho^{-1}\iota\). These transformations act transitively on the 112 embedded vertices. The embedding is therefore vertex-transitive (orientation-reversing symmetries are allowed).

**Step 4: minimality.** The graph is connected, has \(V=2\binom{8}{3}=112\) vertices and is \(\binom{5}{3}=10\)-regular, so \(E=560\). Its exhibited quadrangulation shows each edge belongs to a simple cycle, hence the graph has no bridges. In any minimum-genus orientable embedding, the embedding is cellular and every face boundary of this simple bridgeless bipartite graph has length at least four. Since each edge contributes two sides, \(4F\le2E\), hence \(F\le280\). Euler's formula gives
\[
2-2\gamma(H(8,3))=112-560+F\le112-560+280=-168,
\]
so \(\gamma(H(8,3))\ge85\). The construction attains this bound.

## Verification

The standard-library programs `verify_rotation.py` and `verify_local.py` are embedded in the accompanying package and run without external data. To reproduce, execute `python3 verify_rotation.py` and `python3 verify_local.py`. The first independently constructs all three-subsets, the affine orbit, the ten generators, the whole graph, cyclic orders, dart permutation, 280 four-cycle faces, and Euler genus. The second checks the ten product-and-closure identities using a separate field multiplication routine. Their exact stdout is embedded as `verify_rotation.out` and `verify_local.out`.

## Relationship to prior work

Metzger and Ulrigg, *The Genus of Bipartite Kneser Graphs*, arXiv:2610.03159v1 (first public 2026-10-02), prove orientable quadrangulations for the different family \(H(h,2)\), with \(h>3\) prime and \(h\equiv3\pmod8\). Their Sections 2–3 introduce the rotation-system approach and its four-step criterion. Their Section 9 explicitly reports only \(85\le\gamma(H(8,3))\le143\), while noting \(H(8,3)\) as an exceptional case admitting a sharply transitive group on its three-subsets. The local rotation formalism is adapted here to that finite affine group; the explicit ten-cycle and genus-85 embedding are the additional result. The source does not state a genus value for this graph.

This construction settles precisely that listed finite graph and does not prove the broader fixed \(k\ge3\) Euler-bound question or the conjecture for general \(H(n,2)\).

## Limitations

The theorem concerns orientable genus only. It does not determine nonorientable genus, other \(H(n,k)\), or a general construction for all prime powers. The finite rotation witness determines a genuine cellular embedding because every dart and face is checked exactly; no analogous assertion is made for untested parameters. The comparison with published literature does not exclude the possibility of an unindexed equivalent embedding.

## References

Metzger, Alexander, and Austin Ulrigg. *The Genus of Bipartite Kneser Graphs*. arXiv:2610.03159v1, posted 2026-10-02. https://arxiv.org/pdf/2610.03159. In particular, Sections 2–3 and 9.

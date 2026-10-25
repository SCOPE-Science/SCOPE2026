# Dihedral orientation of graph Hom circles and cycle-coloring quotients

## Finding

**Theorem 1 (integral dihedral orientation).** Let \(G\) be any finite, connected, simple graph containing at least one edge, let \(k\geq3\) with \(k\neq4\), and let \(X=\operatorname{Hom}(G,C_k)\) denote the usual undirected graph Hom complex. Write \(\mathscr C(G,k)\) for the set of connected components of \(X\) having homotopy type \(S^1\), and let \(\Gamma=\operatorname{Aut}(G)\times D_k\), where the two factors act by precomposition and postcomposition, respectively. There is a natural isomorphism of integral \(\Gamma\)-modules

\[
H_1(X;\mathbb Z)\cong\mathbb Z[\mathscr C(G,k)]\otimes\varepsilon,
\]

where \(\varepsilon(\alpha,\beta)=1\) for every source automorphism and target rotation, while \(\varepsilon(\alpha,\beta)=-1\) for every target reflection. The permutation representation uses the actual action of \(\Gamma\) on the circle components. Other components are contractible, and \(H_j(X;\mathbb Z)=0\) for \(j\geq2\).

**Theorem 2 (all rational Betti numbers of the dihedral color quotient for cycle sources).** For \(m\geq3\), let \(Y_{m,k}=\operatorname{Hom}(C_m,C_k)/D_k\), with \(D_k\) acting on the target only, and define

\[
R(m,k)=\#\{w\in\mathbb Z_{>0}: kw<m\ \text{and}\ kw\equiv m\pmod 2\}.
\]

Then

\[
\dim_{\mathbb Q} H_0(Y_{m,k};\mathbb Q)=R(m,k)+\mathbf1_{2\mid m}+\mathbf1_{k\mid m},
\qquad \dim_{\mathbb Q}H_1(Y_{m,k};\mathbb Q)=R(m,k),
\]

and \(H_j(Y_{m,k};\mathbb Q)=0\) for all \(j\geq2\). A zero right-hand side in degree zero means that the quotient is empty. For example, \(m=20,k=6\) gives the pair of Betti numbers \((4,3)\), while \(m=9,k=3\) gives \((2,1)\).

## Assumptions and scope

The graph \(C_k\) is the simple cycle on \(\mathbb Z/k\mathbb Z\). Thus the case \(k=3\) is a triangle, the case \(k=4\) is deliberately excluded, and every domain cycle has \(m\geq3\). In \(\operatorname{Hom}(G,C_k)\), a cell assigns a nonempty subset of target vertices to each vertex of \(G\), with complete adjacency across the subsets of every source edge. For the first theorem, automorphisms of the domain act by inverse precomposition, with a postcomposition automorphism of the target. All homology in Theorem 1 is **integral**, and Theorem 2 concerns **rational quotient homology**; it does not assert an integral homology classification of the quotient.

## Proof

**1. Covering and its canonical orientation.** The classification and universal-cover construction of Fujii, Iwamasa, Kimura, Nozaki and Suzuki establishes that, for connected \(G\) with an edge, each component of \(\operatorname{Hom}(G,C_k)\) is either contractible or homotopy equivalent to a circle. Their covering model, for a fixed graph homomorphism \(f:G\to C_k\), records lifted integers \(a_v\) satisfying

\[
 p_f(a)(v)\equiv f(v)+2a_v\pmod k.
\]

Put \(q=k/\gcd(k,2)\). On each circle component of the corresponding cover, the positive generator of the deck group is the simultaneous shift \(T(a)=a+q\mathbf1\). The cited covering theorem identifies this deck generator with a positive generator of the fundamental group whenever that component is a circle. Replacing the starting lift or homomorphism changes a basepoint, not this positive direction; simultaneous positive translation is canonically defined in every such cover. Thus each circle component has an oriented integral fundamental class.

Any target dihedral automorphism has the affine form \(\beta(j)=\delta j+t\pmod k\), where \(\delta\in\{+1,-1\}\), and any source automorphism \(\alpha\) acts by permuting the coordinates. In coordinates relative to the transformed base coloring \(\beta\circ f\circ\alpha^{-1}\), its lift is exactly

\[
 F_{\alpha,\beta}(a)_v=\delta a_{\alpha^{-1}(v)}.
\]

It follows **on the nose** that \(F_{\alpha,\beta}\circ T=T^\delta\circ F_{\alpha,\beta}\). Conjugating the generator of the deck group therefore multiplies the oriented integral fundamental class by \(\delta\), and this sign is the same on every circle component, independent of the graph, component or source permutation. A component permutation with this uniform sign gives the asserted module \(\mathbb Z[\mathscr C]\otimes\varepsilon\). The vanishing of higher homology follows from the cited component classification.

**2. Winding and components for a cycle source.** Give \(C_m\) an orientation. Every graph homomorphism \(f:C_m\to C_k\) is determined by its initial color and a sequence of increments \(s_i\in\{+1,-1\}\) with \(\sum_{i=0}^{m-1}s_i=kw\) for some integer winding \(w\). Put \(p=\#\{i:s_i=+1\}\), so \(p=(m+kw)/2\). Exactly the windings with \(|kw|\leq m\) and \(kw\equiv m\pmod2\) occur.

For \(0<p<m\), changes of a single vertex color exchange an adjacent \((+1,-1)\) with \((-1,+1)\). These exchanges connect all increment words with a fixed number \(p\) of plus signs; more precisely, the phase of the starting color changes by multiples of two. Hence there are exactly \(\gcd(2,k)\) connected components for each nonextremal winding, each a circle by the published cycle-to-cycle Hom classification. If \(p=0\) or \(p=m\), no exchange is possible: each extremal winding gives exactly \(k\) isolated homomorphisms, and it occurs exactly when \(k\mid m\).

Target rotations permute the phase classes transitively for each fixed winding. Target reflections reverse every step, therefore send \(w\) to \(-w\). Thus the target-dihedral orbits of connected components comprise exactly one orbit for each permitted absolute nonextremal winding and one additional orbit of isolated points if \(k\mid m\). Among these, the nonextremal positive absolute windings are counted by \(R(m,k)\), and winding zero occurs exactly for even \(m\). It follows that the number of connected quotient components is \(R(m,k)+\mathbf1_{2\mid m}+\mathbf1_{k\mid m}\).

**3. Rational homology of the quotient.** A finite group acts cellularly after equivariant subdivision. With rational coefficients, the homology of its quotient identifies with the invariant part of homology (equivalently, averaging chains yields a transfer isomorphism). Apply Theorem 1. For each orbit of circle components with \(w\neq0\), no target reflection stabilizes a component because it negates winding; its rotation stabilizer preserves orientation. Thus the invariant part over this orbit is one-dimensional. For winding zero, a reflection followed by a suitable color rotation stabilizes each relevant circle component, and acts as minus the identity on its \(H_1\); therefore its invariant part is zero. Point components contribute only to degree zero. This proves the displayed Betti-number formulas, including the empty case and vanishing in higher degrees.

## Verification

The standalone `verify_hom.py` uses the standard finite Hom face model and exact integer arithmetic. It enumerates 50 cycle-source/target parameter pairs, verifying the winding/component-orbit and quotient-component formulas using 48,918 graph-coloring vertices and 281,144 permitted one-vertex moves. Independent binary cellular-chain calculations on 11 cases use 3,348 vertices, 7,626 one-cells and 6,108 square two-cells and verify both the stated first Betti numbers and primitive winding-generator behavior. Additional tests verify target-reflection signs on 15 small general graphs and source-automorphism orientation for 13,240 tested edges. Successful completion markers are printed by the program. These finite verifications are supplementary, not a substitute for the proof of the universal statements.

Run `python3 verify_hom.py` with a standard Python 3 installation. There are no external dependencies.

## Relationship to prior work

Fujii–Iwamasa–Kimura–Nozaki–Suzuki, arXiv:2408.04802 (first posted 2024-08-09), prove the point-or-circle homotopy classification of \(\operatorname{Hom}(G,C_k)\) for connected graph sources, and construct the integer-coordinate covering used in Step 1. Čukić–Kozlov (arXiv:math/0408015, 2004) determine homotopy components for \(\operatorname{Hom}(C_m,C_k)\); the winding-component facts of Step 2 are established there. The contributions here are the natural **integral source-and-target automorphism module** on all circle components and, using it, the closed **full rational quotient-homology classification** under target dihedral recoloring. The results are not claims of discovering point-or-circle homotopy types or winding-number classifications anew.

The related December 2024 studies of Hom complexes with square-free codomains by Fujii–Kimura–Nozaki (arXiv:2412.19039) and Matsushita (arXiv:2412.19144) also study covering spaces and component homotopy, including equivariance of lifts. Their compared theorems and proof discussions do not explicitly supply the complete dihedral color-quotient Betti formula proved here. The possibility of an equivalent formulation elsewhere remains.

## Limitations

The first theorem needs a connected nonempty-edge source, and excludes \(k=4\). The second applies to cycle sources and only **target** dihedral quotients. The finite computational checks do not establish the infinite statements independently; those rely on the stated covering and cycle-component theorems together with the naturality calculation and transfer. The quotient classification is rational; integral torsion, explicit homeomorphism types of quotients, and simultaneous source–target quotient Betti numbers are not determined. Mathematical novelty is qualified by the possibility of differently phrased prior results.

## References

1. S. Fujii, Y. Iwamasa, S. Kimura, N. Nozaki and A. Suzuki, *Homotopy types of Hom complexes of graph homomorphisms whose codomains are cycles*, arXiv:2408.04802v1 (2024-08-09), https://arxiv.org/abs/2408.04802 .
2. S. Lj. Čukić and D. N. Kozlov, *The homotopy type of complexes of graph homomorphisms between cycles*, arXiv:math/0408015 (2004), https://arxiv.org/abs/math/0408015 .
3. S. Fujii, S. Kimura and N. Nozaki, *Hom complexes of graphs whose codomains are square-free*, arXiv:2412.19039 (2024), https://arxiv.org/abs/2412.19039 .
4. T. Matsushita, *Hom complexes of graphs with square-free codomains*, arXiv:2412.19144 (2024), https://arxiv.org/abs/2412.19144 .

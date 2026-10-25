# Complete integral length–Rips persistence of complete bipartite graph metrics

## Finding
Let \(m,n\ge1\) be integers and equip the vertices of \(K_{m,n}\) with its shortest-path metric: distinct vertices in opposite parts have distance \(1\), and distinct vertices in one part have distance \(2\). Let \(L_r\) be the **inclusive symmetrized \(\ell^1\)-Vietoris–Rips simplicial complex**, for \(r\ge0\), whose faces are finite subsets of minimum Hamiltonian-path length at most \(r\). For integers \(s\ge0\) define
\[
E_s=\binom{m}{s+1}\binom{n}{s+1}-\binom{m-1}{s+1}\binom{n-1}{s+1},\qquad
O_s=\binom{m-1}{s+1}\binom{n-1}{s+1},
\]
with all out-of-range binomial coefficients zero. For **every** \(s\ge0\),
\[
|L_{2s}|\simeq\bigvee^{E_s} S^{2s},\qquad
|L_{2s+1}|\simeq\bigvee^{O_s} S^{2s+1}.
\]
A zero-fold wedge means a contractible space; a wedge of \(E_0\) zero-spheres means \(E_0+1\) discrete points. These descriptions apply also when one part has only one vertex. At all noninteger scales, \(L_r=L_{\lfloor r\rfloor}\).

The **complete reduced integral persistence module** is the direct sum of \(E_s\) interval modules supported on \([2s,2s+1)\) in degree \(2s\) and \(O_s\) supported on \([2s+1,2s+2)\) in degree \(2s+1\). Consequently the same formula gives the barcode over every field, and \(L_r\) is contractible for every \(r\ge 2\min(m,n)-1\). In particular, for \(m=n=t\ge2\), the penultimate stage \(L_{2t-2}\) is a single sphere \(S^{2t-2}\), although the ordinary diameter-based Rips complex is already a full simplex at scale \(2\).

## Assumptions and scope
Write the two vertex parts as disjoint sets \(A,B\) of cardinalities \(m,n\). An ordered path through a nonempty subset \(F=\{v_1,\ldots,v_k\}\) has length \(\sum_{i=1}^{k-1} d(v_i,v_{i+1})\). The weight \(w(F)\) is the minimum of these lengths over all orderings, with \(w(\{v\})=0\). The \(\ell^1\)-tuple weight of Ivanov–Xu equals the full path length by the triangle inequality, and symmetrizing over orders gives exactly \(w(F)\). Deleting a vertex cannot increase this weight, so \(L_r\) is a simplicial complex. The **unordered symmetrized complex** must not be conflated with the ordered simplicial set used to define blurred magnitude homology. All scales use \(\le r\), not strict inequality; the empty face is adjoined conventionally.

For a finite set \(A'\) of \(a\) vertices from \(A\) and \(B'\) of \(b\) vertices from \(B\), with \(a+b\ge1\), the exact weight is
\[
w(A'\sqcup B')=\max\{a+b-1,\;2\max(a,b)-2\}.
\]
This also holds if \(a=0\) or \(b=0\). Let \(K_s(A)\) be the complex of all subsets of \(A\) of size at most \(s+1\), including the empty face (and similarly \(K_s(B)\)). Write \(Y_s=K_s(A)*K_s(B)\). Then the **literal equality of abstract simplicial complexes** is
\[
L_{2s+1}=Y_s,\qquad L_{2s}=\operatorname{sk}_{2s}Y_s.
\]
If \(s\ge m-1\) or \(s\ge n-1\), the corresponding factor of \(Y_s\) is a full simplex, not an artificial sphere.

## Proof
**1. Weight.** In any ordering of \(a+b\) selected vertices, there are \(a+b-1\) consecutive pairs; a cross-part pair costs \(1\) and a same-part pair costs \(2\). At least \(\max\{0,|a-b|-1\}\) pairs must have the same part, since only \(\min(a,b)\) vertices can separate the vertices of the larger part with both ends available. Alternating the two parts as far as possible and then placing leftover vertices consecutively attains this lower bound. Therefore
\[
w=a+b-1+\max\{0,|a-b|-1\}
=\max\{a+b-1,2\max(a,b)-2\}.
\]

**2. The exact filtration.** The inequality \(w\le2s+1\) says precisely \(a\le s+1\) and \(b\le s+1\); their sum then automatically is at most \(2s+2\). This is \(Y_s\). Likewise \(w\le2s\) says \(a\le s+1\), \(b\le s+1\), and \(a+b\le2s+1\), which removes exactly the dimension-\(2s+1\) faces of \(Y_s\), giving its \(2s\)-skeleton. All subset weights are integers, proving constancy between consecutive integers.

**3. Odd stages.** For a finite set of \(q\) vertices, its simplex \(s\)-skeleton is homotopy equivalent to a wedge of \(\binom{q-1}{s+1}\) spheres of dimension \(s\), and is contractible if \(s\ge q-1\). This standard identity also holds for \(s=0\) using reduced \(H_0\); it follows, for instance, by induction from deletion and link of one vertex and the shellability of simplex skeleta. The join of two positive-multiplicity wedges of \(s\)-spheres is a wedge of spheres of dimension \(2s+1\), with multiplicities multiplied. A join having a contractible nonempty factor is contractible. Hence \(Y_s\simeq\bigvee^{O_s}S^{2s+1}\), with reduced integral homology free and concentrated in degree \(2s+1\).

**4. Even stages.** The group of top-dimensional integral simplicial chains of \(Y_s\) has rank \(T_s=\binom{m}{s+1}\binom{n}{s+1}\), since a \((2s+1)\)-simplex chooses exactly \(s+1\) vertices from each part. There are no chains in higher dimensions. Since \(\widetilde H_{2s+1}(Y_s;\mathbb Z)\) is free of rank \(O_s\), the boundary from top chains has image of rank \(T_s-O_s=E_s\). As \(\widetilde H_{2s}(Y_s;\mathbb Z)=0\), the kernel of the augmented boundary in degree \(2s\) equals that image. Removing the top simplices yields \(L_{2s}=\operatorname{sk}_{2s}Y_s\), whose reduced integral homology is consequently \(\mathbb Z^{E_s}\) in degree \(2s\) and zero otherwise. This also proves no torsion occurs.

For \(s\ge1\), \(Y_s\) is \(2s\)-connected (a wedge of \((2s+1)\)-spheres or contractible). Attaching only \((2s+1)\)-cells to \(L_{2s}\) recovers \(Y_s\), so \(L_{2s}\) is \((2s-1)\)-connected. It has dimension at most \(2s\). The Hurewicz and Whitehead theorems then identify it with a wedge of \(E_s\) spheres \(S^{2s}\); if \(E_s=0\), it is contractible. For \(s=0\), the even stage consists of \(m+n\) isolated points, and \(E_0=mn-(m-1)(n-1)=m+n-1\), agreeing with the zero-sphere convention.

**5. Inclusion maps and barcode.** At every integer stage the only possible nonzero reduced homology is in that integer's degree. The next integer stage has reduced homology in a different degree (or zero). Hence every inclusion-induced map in any fixed reduced homology degree across successive integer stages is zero. Every nonzero class is born at its integer threshold and dies at the next one, producing exactly the stated intervals, over \(\mathbb Z\) and every field. If \(s\ge\min(m,n)\), both even and odd multiplicities vanish. Already at \(r=2\min(m,n)-1\), one factor of \(Y_s\) is a full simplex, so the filtration is contractible from that scale onward.

## Verification
The standalone program `verification/verify_bipartite.py` independently enumerates Hamiltonian paths for every nonempty subset of \(K_{m,n}\) with \(1\le m,n\le3\), checking **187** weights without using the weight formula. It also computes reduced mod-two simplicial boundary-matrix ranks directly and compares all predicted nonzero Betti numbers at **92** integer-scale stages for \(1\le m,n\le4\). The executed result is `PASS: exhaustive path weights 187 and independent binary homology stages 92`. These checks support the finite examples; the all-parameter and integral assertions are proved in the preceding steps and are not inferred from finite enumeration.

For \(K_{3,3}\), successive reduced homology ranks in degrees \(0,1,2,3,4\) are \(5,4,8,1,1\), and the next stage is contractible. For \(K_{4,4}\), the nonzero ranks at scales \(0,1,2,3,4,5,6\) are \(7,9,27,9,15,1,1\) respectively; the scale-\(7\) complex is contractible.

## Relationship to prior work
Ivanov and Xu introduced the symmetrized finite-subset \(\ell_p\)-Vietoris–Rips complexes and the ordered simplicial-set theory. Their general stability and manifold theorems do not give this graph-family's explicit homotopy and persistence calculation. Blaser, Brun, Gardaa and Salbu develop monoidal Rips filtrations for **ordered simplicial sets** and their stability, not the present unordered-complex classification.

The published calculation *Complete length–Rips persistence of well-separated two-level ultrametrics* also gives binomial sphere-wedge barcodes, but it assumes **within-cluster distance less than intercluster distance** and a substantial separation condition. The shortest-path metric of \(K_{m,n}\) has **within-part distance \(2\)** and **cross-part distance \(1\)**, is not an ultrametric, and fails those hypotheses. Its alternating even–odd join-skeleton filtration is therefore not an instance of that calculation. Conventional diameter-based Rips filtrations are also different: at radius \(2\), the classical complex is the complete simplex, so they do not imply the present high-dimensional length–Rips stages. Available record and literature searches found no statement whose hypotheses imply this classification; this absence does not establish global novelty.

## Limitations
This is a classification of inclusive **unordered** \(\ell^1\)-Rips simplicial complexes for the exact **unit-edge complete bipartite shortest-path metric**. It does not calculate ordered simplicial-set (blurred magnitude) homology, other \(\ell_p\)-norms, arbitrary two-distance metrics, or general bipartite graphs. Standard simplex-skeleton homotopy and CW-complex theorems are used; no independent mathematical audit is asserted. Other unindexed or unpublished equivalent calculations remain possible.

## References
1. Sergei O. Ivanov and Xiaomeng Xu, *On \(\ell_p\)-Vietoris–Rips complexes*, arXiv:2411.01857, first public version 2024-11-04; https://arxiv.org/abs/2411.01857 and https://doi.org/10.1007/s41468-026-00247-x.
2. Nello Blaser, Morten Brun, Odin Hoff Gardaa, and Lars M. Salbu, *Monoidal Rips: Stable Multiparameter Filtrations of Directed Networks*, arXiv:2503.14019 (2025), https://doi.org/10.1007/s41468-026-00237-z.
3. *Complete length–Rips persistence of well-separated two-level ultrametrics*, publicly indexed mathematical research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-complete-length-rips-persistence-of-well-separated-two-level-ult--347c9fe945df.
4. Standard simplicial shellability, the join homotopy formula, and the Hurewicz and Whitehead theorems, in their finite-CW forms.

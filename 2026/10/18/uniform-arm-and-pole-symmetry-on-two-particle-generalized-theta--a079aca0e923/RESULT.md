# Uniform arm and pole symmetry on two-particle generalized theta configurations

## Finding

Let \(m\geq 3\) be an integer. Let \(\Theta_m\) consist of \(m\) length-three paths between two common poles, and let \(X_m=\operatorname{UConf}_2(|\Theta_m|)\) be the **unordered**, collision-free configuration space of two points on its geometric realization. The natural automorphism group is \(S_m\times C_2\): permutations relabel the arms, and the nonidentity pole involution exchanges the two poles while reversing the parameter on every arm. Write \(P_m=\mathbb Q^m\) for the arm-permutation representation and \(\varepsilon\) for the nontrivial rational character of the pole involution.

**Theorem (uniform rational symmetry character).** For every \(m\geq3\),

\[
H_0(X_m;\mathbb Q)=\mathbb Q,\qquad H_1(X_m;\mathbb Q)\cong\bigwedge^2 P_m\boxtimes\varepsilon,\qquad H_i(X_m;\mathbb Q)=0\quad(i\geq2)
\]

as representations of \(S_m\times C_2\), where the degree-zero action is trivial. More explicitly, for \(\sigma\in S_m\), let \(f(\sigma)\) be the number of fixed arms and \(t(\sigma)\) the number of two-cycles of \(\sigma\). For \(\delta\in\{0,1\}\), with \(\delta=1\) indicating pole interchange,

\[
\operatorname{tr}\big((\sigma,\delta)\mid H_1(X_m;\mathbb Q)\big)
=(-1)^\delta\left(\binom{f(\sigma)}2-t(\sigma)\right).
\]

Thus the pole interchange is negative identity on every rational first-homology class, and both quotients \(X_m/S_m\) and \(X_m/C_2\) are rationally acyclic in positive degrees. The novelty asserted is the **all-arm, full group character**, not the previously known nonequivariant Betti number or an integral equivariant classification.

## Assumptions and scope

Define vertices \(u,v,a_i,b_i\) for \(1\leq i\leq m\), and graph edges \(L_i=(u,a_i)\), \(M_i=(a_i,b_i)\), \(R_i=(b_i,v)\), each oriented from \(u\) towards \(v\). The pole involution takes \(u\leftrightarrow v\), \(a_i\leftrightarrow b_i\); consequently it reverses the orientation of each graph edge. All particles are unlabelled and are forbidden from occupying the same point, including graph vertices. The result concerns ordinary rational singular homology and the actual graph automorphism action. It does not assert a natural integral isomorphism with \(\bigwedge^2\mathbb Z^m\), nor any analogous formula for three or more particles.

## Proof

**1. Equivariant finite model.** The graph subdivision has length-three paths between branch vertices, sufficient for the standard two-point discrete-configuration deformation retraction. Its cubical model \(D_m\) has zero-cells given by two distinct vertices, one-cells by a graph edge and a vertex outside its closure, and square cells by an unordered pair of vertex-disjoint edges. The model and its deformation retraction are natural for the arm permutations and pole reversal. Consequently cellular traces on \(D_m\) compute the character of \(X_m\). The counts are

\[
 c_0=\binom{2m+2}2=2m^2+3m+1,\qquad
 c_1=3m(2m)=6m^2,\qquad
 c_2=m+7\binom m2=\frac{7m^2-5m}{2}.
\]

Indeed, in a fixed arm only the two outer edges are mutually disjoint; between two distinct arms exactly seven of the nine edge pairs are disjoint, since the two left edges share \(u\) and the two right edges share \(v\).

**2. Vanishing in degree two, including the integral chain level.** Consider the *ordered* two-particle cubical model \(\widetilde D_m\subset|\Theta_m|\times|\Theta_m|\). The ambient product is a two-dimensional cell complex, so every integral two-cycle represents its own two-homology class. The Künneth identification is

\[
H_2(|\Theta_m|\times|\Theta_m|;\mathbb Z)
=H_1(|\Theta_m|;\mathbb Z)\otimes H_1(|\Theta_m|;\mathbb Z).
\]

The map from the graph cycle lattice to \(\mathbb Z^m\) recording coefficients on \(L_1,\ldots,L_m\) is injective: if all these coefficients vanish, the boundary equations at the degree-two vertices \(a_i,b_i\) force all coefficients on \(M_i,R_i\) to vanish. Since all groups here are free abelian, its tensor square also injects. Hence any ambient integral two-cycle is uniquely determined by the coefficients of the product squares \(L_i\times L_j\), for all ordered \((i,j)\). No such product square belongs to \(\widetilde D_m\), because \(L_i\) and \(L_j\) meet at \(u\). A two-cycle in \(\widetilde D_m\) therefore vanishes identically. The cellular transfer from the unordered model to its twofold ordered cover is injective on two-chains and sends cycles to cycles. Thus \(H_2(D_m;\mathbb Z)=0\). The cubical model has no cells above dimension two, so all higher homology groups vanish as well.

The unordered two-particle configuration space on a connected graph with a cycle is connected. From the cell counts, \(\chi(D_m)=1-\binom m2\). Consequently \(\dim_{\mathbb Q}H_1(X_m;\mathbb Q)=\binom m2\).

**3. Signed fixed-cell traces.** For a permutation \(\sigma\) with \(f\) fixed arms and \(t\) arm transpositions, let \(q=0\) denote no pole interchange and \(q=1\) denote pole interchange. The oriented cellular trace calculation is exactly

\[
\begin{array}{c|ccc}
 &\operatorname{tr} C_0&\operatorname{tr} C_1&\operatorname{tr} C_2\\ \hline
q=0 &\binom{2+2f}2+2t&6f^2&f+7\binom f2-t\\
q=1 &1+f+2t&0&\binom f2-f-3t
\end{array}.
\]

For \(q=0\), the fixed zero-cells are unordered pairs of fixed vertices, together with vertex transpositions; the fixed one-cells require a fixed arm edge and a fixed nonincident vertex. Fixed squares comprise one outer-edge pair on each fixed arm, seven pairs between fixed arms, and the middle-edge pairs exchanged by an arm transposition. The last type contributes a **negative** orientation trace. For \(q=1\), all individual graph edges reverse orientation and no graph vertex is fixed. The fixed zero-cells are exactly transposed vertex pairs (the poles, one on each fixed arm, and two per arm transposition). Fixed squares are pairs of fixed middle edges (positive), left/right pairs exchanged within a fixed arm (negative), and three exchanged edge pairs per transposed arm pair (negative). The square-edge-exchange sign is necessary: ignoring it changes the result.

**4. Lefschetz character and representation.** Since \(H_0\) has trace one and positive-degree homology is concentrated in degree one, the cellular Lefschetz identity gives

\[
\operatorname{tr}(g\mid H_1)=1-\operatorname{tr}(g\mid C_0)+\operatorname{tr}(g\mid C_1)-\operatorname{tr}(g\mid C_2).
\]

Substitution of the table gives \((-1)^q(\binom f2-t)\). On the other hand the exterior-square character identity is

\[
\operatorname{tr}(\sigma\mid\bigwedge^2P_m)
=\tfrac12\big(f^2-(f+2t)\big)
=\binom f2-t.
\]

The equality of characters on the finite group \(S_m\times C_2\), together with semisimplicity over \(\mathbb Q\), proves the claimed rational module isomorphism. The invariant subspace of \(\bigwedge^2P_m\) under all of \(S_m\) is zero for \(m\geq3\): a transposition exchanging the two labels of any prospective basis wedge changes its sign. The pole involution already acts as \(-I\). Rational homology of quotients by finite groups agrees with invariant rational homology (using an equivariant subdivision if necessary), giving the quotient consequence.

## Verification

The bundled `verify_theta.py` uses only the Python standard library. Running `python3 verify_theta.py` independently constructs the cubical cells, computes signed cellular fixed-point traces for every element of \(S_m\times C_2\) for \(m=3,4,5\), and computes mod-two boundary ranks for \(m=3,4,5,6\). These computations reproduce \(\dim H_1=\binom m2\), vanishing degree-two homology in the tested models, and the uniform character formula. They are finite consistency tests, **not** the justification for the universal quantifier; the proof above is uniform.

## Relationship to prior work

Farley and Sabalka's discrete Morse theory and graph braid framework (first preprint 25 October 2004) supplies established graph-configuration topology. Barnett and Farber's two-particle *ordered* graph-configuration study (12 March 2009) addresses integral and rational Betti groups and planar intersection forms; its ordered setting is not the unlabeled automorphism module computed here. Ko and Park's full primary article (first preprint 13 January 2011), especially Lemma 3.14, calculates \(H_1(B_2\Theta_m;\mathbb Z)\cong\mathbb Z^{\binom m2}\) and a Morse model with no critical two-cells. That **nonequivariant** integral rank, and any previously calculated individual four-arm action, are not claimed as new. The contribution is a uniform rational \(S_m\times C_2\) character for arbitrary arm number, including the pole action and consequences for symmetry quotients.

The analogous three-particle generalized-theta calculations concern different configuration spaces and homological degrees; Rips/Čech theta complexes and sink-configuration spaces are not equivalent to the collision-free two-point complex used here.

## Limitations

The equivariant isomorphism is proved over \(\mathbb Q\). Integral module extensions, bases of two-arm cycle representatives for **all** arm counts, group-cohomological torsion of the quotient spaces, and the actions for three or more particles are not determined here. Literature searches are not a proof of absolute publication priority; equivalent representation formulas under different terminology are a residual bibliographic risk. The finite verification examples do not replace the general argument.

## References

1. D. Farley and L. Sabalka, *Discrete Morse theory and graph braid groups*, arXiv:math/0410539v1 (25 October 2004), https://arxiv.org/abs/math/0410539.
2. K. Barnett and M. Farber, *Topology of Configuration Space of Two Particles on a Graph, I*, arXiv:0903.2180v1 (12 March 2009), https://arxiv.org/abs/0903.2180.
3. K. H. Ko and H. W. Park, *Characteristics of graph braid groups*, arXiv:1101.2648v1 (13 January 2011), https://arxiv.org/abs/1101.2648. See Lemma 3.14 and Section 2.

# Reflection characters for independence complexes of cycle–complete-graph products

## Finding

For integers \(r\ge1\) and \(n\ge2\), put \(m=3r\) and consider the independence complex
\[
 X_{r,n}=\operatorname{Ind}(C_m\times K_n)
\]
of the **categorical** product. Write \(D_m=\langle\rho,s\mid\rho^m=s^2=1,\ s\rho s=\rho^{-1}\rangle\); the reflection \(s_t\) sends a graph vertex \((i,a)\) to \((t-i\bmod m,a)\), without changing its color. Let \(\chi_{r,n}(s_t)\) denote its trace on \(\widetilde H_{2r-1}(X_{r,n};\mathbb Q)\). Then
\[
 \boxed{\chi_{r,n}(s_t)=
 \begin{cases}
 0,&r\text{ odd},\\
 0,&r\text{ even and }t\text{ even},\\
 n(n-1)^{r/2},&r\text{ even and }t\text{ odd}.
 \end{cases}}
\]
For even \(r\), even \(t\) means the reflection fixes two opposite cycle vertices, while odd \(t\) means it interchanges both pairs of vertices along two opposite cycle edges. When \(r\) is odd there is only one reflection conjugacy class. The previously established nonequivariant homotopy classification implies that rational reduced homology is concentrated in degree \(2r-1\) (Antolín Camarena–Carnero Bravo, Theorem 22). This new statement determines every reflection trace, not merely the ordinary Betti number.

In particular, if \(B_{r,n}=\dim_{\mathbb Q}\widetilde H_{2r-1}(X_{r,n};\mathbb Q)\), the \(\pm1\)-eigenspace dimensions for a chosen reflection are \((B_{r,n}\pm\chi_{r,n}(s_t))/2\). Thus the two reflection types for even \(r\) have different dimensions of fixed homology, although their action on the underlying cycle has the same order.

## Assumptions and scope

The vertex set of \(C_m\times K_n\) is \((\mathbb Z/m\mathbb Z)\times\{1,\ldots,n\}\). Distinct vertices \((i,a)\) and \((j,b)\) are adjacent precisely when \(j=i\pm1\pmod m\) and \(a\ne b\). A simplex of \(X_{r,n}\) is an independent subset of these vertices. All character statements concern ordinary reduced homology with rational coefficients. The formula includes the triangular case \(m=3\), for which \(C_3=K_3\).

## Proof

**1. Signed fixed-simplex formula.** Let \(g\) be any automorphism of a finite simplicial complex. If a face \(F\) is preserved as a set and the permutation of its vertices has \(o(F)\) cycles, then the orientation sign is \((-1)^{|F|-o(F)}\). The alternating augmented simplicial-chain trace, including the empty face, therefore is
\[
 \sum_{k\ge-1}(-1)^k\operatorname{tr}(g\mid\widetilde C_k)
 =-\sum_{\substack{F\in X\\gF=F}}(-1)^{o(F)}.
\]
By the Hopf trace identity, the left-hand side is the alternating trace on reduced homology. The aforementioned homology-concentration theorem places all nonzero reduced rational homology in degree \(2r-1\), which is odd. Consequently,
\[
 \operatorname{tr}(g\mid\widetilde H_{2r-1})
 =\sum_{\substack{F\in X\\gF=F}}(-1)^{o(F)}.\tag{1}
\]
The empty face contributes \(1\) on the right. An invariant face is a union of vertex orbits of \(g\). Hence the sum in (1) is the independence polynomial at \(-1\) of the quotient graph on those orbits which contain no internal graph edge, with two distinct orbits joined when any pair of their constituent vertices is joined. This statement retains adjacency *within* an orbit of cycle layers and is crucial for folds along edges.

**2. Folded-path model.** For a reflection \(s_t\), its orbits of cycle layers form a path. An ordinary layer-orbit permits any subset of the \(n\) color-orbits, and will be called **free**. If a reflected cycle edge has both endpoints in one layer-orbit, its two endpoints of different colors are adjacent in the original categorical product. At that end of the path, at most one color-orbit may be selected; call that end **capped**. Between successive layer-orbits, nonempty chosen color sets are compatible only when both are the same singleton. This is an exact description of the orbit quotient, including all internal and interorbit adjacency constraints.

For odd \(m=6h+3\), the quotient has \(3h+2\) layers, with one free end and one capped end. For even \(m=6h\), a vertex-axis reflection has \(3h+1\) free layers, while an edge-axis reflection has \(3h\) layers with both ends capped. Here \(h\ge0\) in the odd case and \(h\ge1\) in the even case.

**3. Exact transfer.** Put \(q=n-1\). Accumulate the signed weights of independent orbit selections according as their last layer is empty, a singleton color, or has at least two colors. Let the three signed totals be \((a,b,c)^\mathsf T\), with \(b\) summed over all singleton colors. Appending a free layer transforms this vector by
\[
 M=\begin{pmatrix}1&1&1\\-n&-1&0\\q&0&0\end{pmatrix},
 \qquad
 N=\begin{pmatrix}1&1&1\\-n&-1&0\\0&0&0\end{pmatrix}
\]
when the appended layer is free or capped, respectively. Indeed, the new empty layer may follow any state; a singleton of color \(a\) may follow an empty layer or that same singleton and has weight \(-1\); a multiple-color subset may follow only an empty layer, and its combined signed weight equals \(\sum_{j=2}^n\binom nj(-1)^j=n-1=q\). The initial vector is \(e=(1,0,0)^\mathsf T\); a terminal vector is summed with \(u=(1,1,1)^\mathsf T\). Direct matrix multiplication gives the decisive exact identity
\[
 M^3=qI_3.\tag{2}
\]
Also \(u^\mathsf TMe=0\), \(NMe=0\), and \(u^\mathsf TNMNe=nq\).

**4. Evaluation for every reflection.** If \(m=6h+3\), the free-to-capped quotient gives
\[
 \chi_{r,n}(s_t)=u^\mathsf T N M^{3h+1}e
 =q^h u^\mathsf T NMe=0.
\]
If \(m=6h\), the vertex-axis quotient gives
\[
 \chi_{r,n}(s_t)=u^\mathsf T M^{3h+1}e
 =q^h u^\mathsf T Me=0,
\]
and the edge-axis quotient gives
\[
 \chi_{r,n}(s_t)=u^\mathsf T N M^{3h-2}Ne
 =q^{h-1}u^\mathsf T NMNe=nq^h.
\]
Since \(r=2h\) in the last two cases, this is precisely the asserted \(n(n-1)^{r/2}\). This proves the statement for all \(r\ge1,n\ge2\), not just the parameters used in verification.

## Verification

The standalone `cycle_reflections_checker.py` implements the quotient-orbit graph directly, evaluates its signed independence polynomial by exact integer recursion, and compares it to the separate three-state transfer computation for \(1\le r\le5\), \(2\le n\le5\) and every reflection-axis type. For selected small cases it independently enumerates **all independent faces of the original graph**, tests their setwise invariance and counts their vertex-permutation cycles. The 34 comparisons pass; for \(m=6,n=3\), the two axis traces are respectively \(0\) and \(6\), and for \(m=6,n=4\) they are \(0\) and \(12\). These finite checks supplement, rather than replace, the symbolic identity (2) and the all-parameter proof.

Reproduce with `python3 cycle_reflections_checker.py` using Python's standard library only.

## Relationship to prior work

Antolín Camarena and Carnero Bravo (2023, arXiv:2307.12401, Theorem 22, pp. 24–26) establish the nonequivariant homotopy type of the entire family for cycle lengths divisible by three. That theorem supplies the homology-concentration input used in Step 1 but does **not** determine reflection-induced maps. Goyal, Shukla and Singh (2019, arXiv:1905.06926, Section 3) treat independence complexes of categorical products of complete graphs; that includes the triangular base case but does not give this reflection character for the cycle family. The transfer calculation here addresses symmetry data that homotopy ranks alone do not determine. Knowledge of rotation traces alone also does not determine reflection traces: twisting any dihedral representation by its quotient sign character leaves all rotations unchanged but flips all reflection traces.

## Limitations

The theorem concerns only reflections acting on the cycle coordinate, with the color labels fixed. It does not describe the character at elements combining a nonidentity color permutation with a reflection; no integral group-ring module, integral torsion classification or new nonequivariant homotopy type is asserted. An equivalent reflection formula may exist in literature not reached by the recorded searches; scientific originality should be regarded as conditional on that evidence rather than as a uniqueness certificate. An independent mathematical audit has not been performed.

## References

1. O. Antolín Camarena and A. Carnero Bravo, *Homotopy type of the independence complex of some categorical products of graphs* (first posted 2023-07-23), arXiv:2307.12401, Theorem 22, https://arxiv.org/abs/2307.12401.
2. S. Goyal, S. Shukla and A. Singh, *Homotopy Type of Independence Complexes of Certain Families of Graphs* (2019), arXiv:1905.06926, Section 3, https://arxiv.org/abs/1905.06926.

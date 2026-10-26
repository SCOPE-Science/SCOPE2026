# A Lagrangian quadric of jumping lines for rank-four hyperplane syzygies

## Finding

Let \(V\) be a six-dimensional complex vector space and let \(\omega\in\bigwedge^2V\) be a bivector of rank at least four. Its annihilator
\[
W_\omega=\{\alpha\in\bigwedge^2V^*:\langle\alpha,\omega\rangle=0\}
\]
is fourteen-dimensional. Let \(E_\omega\) be defined on \(\mathbb P(V)\) by the exact sequence
\[
0\longrightarrow E_\omega(-1)\longrightarrow W_\omega\otimes\mathcal O
\overset{\mathrm{Koszul}}\longrightarrow\Omega^1_{\mathbb P(V)}(2)\longrightarrow0.
\]
The bundle has rank nine and \(c_1(E_\omega)=5H\), with \(H\) the hyperplane class.

**Rank/splitting dichotomy.** If \(\operatorname{rank}(\omega)=6\), every projective line \(L\) has
\[
E_\omega|_L\cong\mathcal O_L(1)^5\oplus\mathcal O_L^4.
\]
If \(\operatorname{rank}(\omega)=4\), write \(S=\operatorname{im}(\omega^\sharp)\subset V\), where \(\omega^\sharp:V^*\to V\) is contraction. Then the entire (set-theoretic, reduced) jumping-line locus is
\[
\{\mathbb P(U):U\subset S,\ \dim U=2,\ U\text{ Lagrangian for the inverse alternating form on }S\}
=\operatorname{LG}(2,S)\cong Q^3.
\]
For each jumping line,
\[
E_\omega|_L\cong\mathcal O_L(1)^6\oplus\mathcal O_L^2\oplus\mathcal O_L(-1),
\]
whereas the nonjumping splitting is \(\mathcal O_L(1)^5\oplus\mathcal O_L^4\). Thus among these hyperplane-kernel bundles, uniformity holds exactly at bivector rank six.

**Concrete degeneration of the recent example.** In the fourteen-column matrix \(N\) of Denham--Miró-Roig--Schenck [1, §3, displayed matrix preceding (1)], twelve columns are elementary exterior-Koszul columns (all except the \((x,y)\), \((z,t)\), and \((u,v)\) columns), while the remaining two are respectively the sums \((x,y)+(z,t)\) and \((z,t)+(u,v)\). Its annihilating bivector is proportional to \(\omega=e_x\wedge e_y-e_z\wedge e_t+e_u\wedge e_v\), of rank six. The printed construction is therefore in the uniform rank-six stratum, as claimed in [1]. The one-parameter family \(\omega_\lambda=e_x\wedge e_y-e_z\wedge e_t+\lambda e_u\wedge e_v\) has a rank-four special fibre at \(\lambda=0\), whose complete jumping locus is a smooth Lagrangian three-quadric. This is a degeneration result, not a counterclaim concerning the source's rank-six example.

## Assumptions and scope

The base field is \(\mathbb C\). All lines are projectivizations of two-dimensional vector subspaces of \(V\). The bivector rank is the rank of the alternating map \(\omega^\sharp:V^*\to V\), so the only cases studied are ranks four and six. The jumping locus is asserted as an equality of reduced sets; no nonreduced jumping-scheme structure is claimed. No general claim about all rank-nine uniform bundles is made.

## Proof

**1. Local freeness and Chern data.** The usual Euler--Koszul map
\[
\bigwedge^2V^*\otimes\mathcal O\to\Omega^1_{\mathbb P(V)}(2)
\]
sends a two-form \(\alpha\) at \([x]\in\mathbb P(V)\) to its contraction \(\iota_x\alpha\). It is surjective. Restricting to the hyperplane \(W_\omega\) fails to be surjective at \([x]\) precisely when \(\omega\in x\wedge V\). Every such bivector has rank at most two. Since \(\operatorname{rank}\omega\ge4\), the restricted map is surjective everywhere; its kernel is locally free of rank \(14-5=9\). From \(c_1(\Omega^1(2))=4H\) and twisting the kernel by \(\mathcal O(1)\), obtain \(c_1(E_\omega)=(-4+9)H=5H\).

**2. Restriction to a line.** Fix \(U=\langle x,y\rangle\subset V\) with \(x,y\) independent and write \(L=\mathbb P(U)\). Put \(F_\omega=E_\omega(-1)\). The standard conormal splitting gives
\[
\Omega^1_{\mathbb P(V)}(2)|_L\cong\mathcal O_L\oplus\mathcal O_L(1)^4.
\]
Consequently \(F_\omega|_L\) has rank nine, degree \(-4\), and every Birkhoff--Grothendieck summand has nonpositive degree, because \(F_\omega|_L\subset\mathcal O_L^{14}\).

A constant two-form \(\alpha\in W_\omega\) determines the zero section of \(\Omega^1(2)|_L\) precisely when \(\iota_x\alpha=\iota_y\alpha=0\). Hence
\[
H^0(L,F_\omega|_L)=W_\omega\cap\bigwedge^2\operatorname{Ann}(U),
\]
where \(\dim\bigwedge^2\operatorname{Ann}(U)=\binom42=6\). The hyperplane functional restricts to zero on \(\bigwedge^2\operatorname{Ann}(U)\) precisely when the image of \(\omega\) in \(\bigwedge^2(V/U)\) vanishes, equivalently \(\omega\in U\wedge V\). Thus \(h^0(F_\omega|_L)=6\) in that case, and \(5\) otherwise.

As all nine summand degrees are \(\le0\) and their sum is \(-4\), the number of degree-zero summands uniquely determines the entire splitting:
\[
F_\omega|_L\cong
\begin{cases}
\mathcal O_L^5\oplus\mathcal O_L(-1)^4,&\omega\notin U\wedge V,\\
\mathcal O_L^6\oplus\mathcal O_L(-1)^2\oplus\mathcal O_L(-2),&\omega\in U\wedge V.
\end{cases}
\]
Twisting by \(\mathcal O_L(1)\) proves both displayed splittings of \(E_\omega\).

**3. Geometry of the exceptional condition.** A bivector belonging to \(U\wedge V\), with \(\dim U=2\), is a sum of at most two decomposable bivectors and therefore has rank at most four. Rank-six \(\omega\) has no exceptional lines. For rank-four \(\omega\), any expression \(\omega\in U\wedge V\) must have four-dimensional support spanned by \(U\) and two additional vectors; thus \(U\subset S\). The induced alternating form on \(S\) is nondegenerate. In a symplectic basis, \(\omega=e_1\wedge e_2+e_3\wedge e_4\), and the vanishing of its image in \(\bigwedge^2(S/U)\) is equivalent to the inverse symplectic form vanishing on \(U\); equivalently \(U\) is Lagrangian. Such two-planes form \(\operatorname{LG}(2,4)\), the smooth three-dimensional quadric cut out by the symplectic hyperplane in the Plücker quadric \(\operatorname{Gr}(2,4)\subset\mathbb P^5\). The locus is nonempty and proper, proving nonuniformity at rank four.

**4. Explicit fourteen-column test and rank-four limit.** Read the source's printed columns term-by-term: the first column is the sum of the \((x,y)\) and \((z,t)\) exterior columns; the fourteenth is the sum of the \((z,t)\) and \((u,v)\) exterior columns; and twelve other elementary coordinate-pair columns appear. Orthogonality to both sums forces the annihilating bivector to have nonzero coefficients with pattern \((1,-1,1)\) on those three disjoint coordinate pairs, so its rank is six, not four. Hence that printed kernel has no jumping lines. Replacing the last coefficient by the parameter \(\lambda\) yields a flat family of hyperplane coefficient spaces; at \(\lambda=0\) the bivector has rank four and the line \(\mathbb P\langle e_x,e_z\rangle\) is jumping, while the line \(\mathbb P\langle e_x,e_y\rangle\) is not. The full special-fibre locus is the preceding Lagrangian quadric.

## Verification

Run `python3 verify.py` with SymPy installed. The script constructs exact rational matrices for the bivector ranks and fourteen-dimensional hyperplanes, independently recovers the published fourteen exterior-Koszul columns, and checks two contrasting lines. It also enumerates all \(130\) two-planes in \(\mathbb F_3^4\) and finds precisely \(40\) isotropic planes, agreeing with the finite-geometry count \((3+1)(3^2+1)=40\). These finite checks corroborate the universal, characteristic-zero proof above; they do not replace it.

## Relationship to prior work

[1] constructs a fourteen-section *rank-six* hyperplane kernel and proves uniformity. The present result supplies the rank-dependent, exhaustive line-splitting and jumping-locus criterion for its natural rank-four degeneration. The nondegenerate rank-six case is consistent with the symplectic \(14\times14\) constant-rank construction of Landsberg--Manivel [2, §6.2]; its existence and uniformity are earlier work, not an originality claim here. Manivel--Miró-Roig [3] focuses on constant-matrix-rank classifications up to six; it does not subsume this rank-nine jumping-locus description. The new part is the sharp rank-four locus and its exceptional splitting, not the general Euler--Koszul method.

## Limitations

This does not determine a scheme-theoretic Fitting structure or multiplicities on the jumping locus, nor does it classify more general codimension-two subspaces of \(\bigwedge^2V^*\). The source comparison is limited to inspected portions of the cited papers and discoverable indexed material; an earlier implicit statement of the rank-four description remains possible. The source example itself lies in the rank-six uniform locus; no lack of uniformity is claimed for that example.

## References

1. G. Denham, R. Miró-Roig, H. Schenck, *Uniform non-homogeneous vector bundles: A counterexample to the conjecture of Drézet and Ballico-Ellia*, arXiv:2610.20208v1 (14 October 2026), §3. https://arxiv.org/html/2610.20208v1
2. J. M. Landsberg, L. Manivel, *Equivariant spaces of matrices of constant rank*, arXiv:2212.04228v1 (8 December 2022), §6.2. https://arxiv.org/pdf/2212.04228
3. L. Manivel, R. Miró-Roig, *Matrices of linear forms of constant rank from vector bundles on projective spaces*, arXiv:2304.08055v1 (17 April 2023), introduction and classification theorems. https://arxiv.org/pdf/2304.08055

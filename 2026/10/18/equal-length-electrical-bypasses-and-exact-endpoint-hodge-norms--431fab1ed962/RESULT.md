# Equal-length electrical bypasses and exact endpoint Hodge norms for Steiner pair designs

## Finding

Let \(\mathcal D\) be **any existing simple Steiner \(2\)-\((v,k,1)\) design**, with integers \(2\le k<v\): there are \(v\) points; each block has \(k\) points; each pair of distinct points belongs to exactly one block. The design need not be symmetric, point-transitive, block-transitive, or Desarguesian. Its point–block incidence graph \(G\) has one unweighted edge for every incidence.

Write \(r=(v-1)/(k-1)\), and orient all incidence edges from a point toward a block. Let \(D:\mathbb R^{E(G)}\to\mathbb R^{V(G)}\) be the oriented incidence map (positive at points, negative at blocks), \(L=DD^{\mathsf T}\), and define the canonical real cut and cycle projections
\[
Q=D^{\mathsf T}L^{+}D,\qquad C=I-Q,
\]
where \(L^{+}\) is the Moore–Penrose pseudoinverse in Euclidean coordinates. Put
\[
\rho=\frac{k-1}{v}+\frac1k,\qquad \eta=1-\rho=\frac{(k-1)(v-k)}{kv}>0.
\]

**Electrical path theorem.** Fix **any** incidence edge \(e=(p,B)\). There are exactly \((v-k)(k-1)\) simple paths of length five from \(p\) to \(B\) that avoid \(e\), and no shorter edge-avoiding path. Orient each from \(p\) to \(B\). The unique unit electrical current \(Q\mathbf1_e\) is exactly the following convex combination of path currents:
\[
\boxed{\quad Q\mathbf1_e=\rho\,\mathbf1_e+
\frac1{kv}\sum_{\substack{\gamma:p\leadsto B\\|\gamma|=5,\ e\notin\gamma}}\mathbf1_{\gamma}.\quad}
\]
Here \(\mathbf1_\gamma\in\mathbb R^E\) is the signed edge vector of the directed path, relative to the fixed reference orientation. Every five-edge bypass receives exactly the **same** positive coefficient. The expression is valid without any graph automorphism hypothesis.

**Sharp endpoint operator norms.** Every column of \(Q\) has the same \(\ell_1\)-norm, as does every column of \(C\), and
\[
\boxed{\quad
\|Q\|_{\ell_1(E)\to\ell_1(E)}=
\|Q\|_{\ell_\infty(E)\to\ell_\infty(E)}=5-4\rho,\qquad
\|C\|_{\ell_1(E)\to\ell_1(E)}=
\|C\|_{\ell_\infty(E)\to\ell_\infty(E)}=6(1-\rho).
\quad}
\]
Thus the exact norms depend **only** on the design parameters \((v,k)\), not its isomorphism type. Their comparison is \(\|Q\|-\|C\|=2\rho-1\). Among designs satisfying the stated hypotheses, the cut projection has larger endpoint norm precisely when \(k=2\), or \(k=3\) and \(v\in\{7,9\}\). In every other case the cycle projection is larger; equality never occurs. Both global bounds \(\|Q\|<5\) and \(\|C\|<6\) are optimal, approached as the orders of finite projective planes tend to infinity.

## Assumptions and scope

All edge conductances are exactly one. The graph is the finite bipartite incidence graph of a **Steiner pair design**, not the complete point–block bipartite graph and not a general block design with repeated pair incidences. The projections are **the canonical Euclidean orthogonal projections** acting on the real coordinate edge spaces. No minimum-norm claim among all projections is made; no intermediate-exponent norm is evaluated. A nonexistent parameter design is not asserted to exist.

The incidence graph is connected: any two distinct points share a block, and every block contains points. Its cut space is \(\operatorname{ran}(D^{\mathsf T})\) and its cycle space is \(\ker D\). The path expansion uses the reference orientation point-to-block and signed paths; coefficients are positive and sum to one. A path of length five is a shortest **bypass**, rather than a shortest unconstrained path (the direct edge has length one).

## Proof

**1. Design counts and a zero-sum Laplacian solution.** Every point lies in \(r=(v-1)/(k-1)\) blocks, and the number of blocks is \(b=vr/k\). Let \(N\) be the \(v\times b\) zero–one point–block matrix. Since distinct points share exactly one block,
\[
NN^{\mathsf T}=(r-1)I_v+J_v.
\]
Fix the oriented edge \(e=(p_0,B_0)\) and inject a unit current at point \(p_0\), extracting it at block \(B_0\). Define point potentials
\[
x=\frac{k}{v}\mathbf1_{p_0}-\frac1v\mathbf1_{B_0}\in\mathbb R^v,
\]
where \(\mathbf1_{B_0}\) now denotes the point-indicator of the block, and define block potentials
\[
y=\frac1k(N^{\mathsf T}x-\mathbf1_{B_0}^{\mathrm{block}})\in\mathbb R^b,
\]
where the superscript \(\mathrm{block}\) distinguishes the basis vector of the block-coordinate space. We have \(\sum_p x_p=0\). Since \(r(k-1)+1=v\), the point part of \(L(x,y)\) is
\[
\left(rI-\frac1kNN^{\mathsf T}\right)x+\frac1kN\mathbf1_{B_0}^{\mathrm{block}}
=\frac vkx-\frac1kJx+\frac1k\mathbf1_{B_0}
=\mathbf1_{p_0}.
\]
The block part is \(-N^{\mathsf T}x+ky=-\mathbf1_{B_0}^{\mathrm{block}}\). Thus \((x,y)\) solves the correct unit-source Poisson equation, and its oriented edge gradient \(x_p-y_B\) is the **unique** energy-minimizing unit flow \(Q\mathbf1_e\). Uniqueness follows from connectedness and the orthogonal cut–cycle decomposition.

**2. Entire edge-current table.** The point potentials are \((k-1)/v\) at \(p_0\), \(-1/v\) on \(B_0\setminus\{p_0\}\), and zero outside \(B_0\). Block potentials equal \(-1/k\) at \(B_0\); \((k-1)/(kv)\) on other blocks through \(p_0\); \(-1/(kv)\) on blocks meeting \(B_0\) in a different point; and zero on blocks disjoint from \(B_0\). These four block cases are exhaustive because two distinct blocks in a Steiner pair design intersect in at most one point.

The resulting signed currents, oriented point-to-block, have these disjoint classes:

| Edge class | Number | Current |
| --- | ---: | ---: |
| \((p_0,B_0)\) | \(1\) | \(\rho\) |
| \((z,B_0)\), \(z\in B_0\setminus\{p_0\}\) | \(k-1\) | \((v-k)/(kv)\) |
| \((p_0,B_1)\), \(B_1\ne B_0\) | \(r-1\) | \((k-1)^2/(kv)\) |
| \((x,B_1)\), \(x\notin B_0\), \(p_0\in B_1\ne B_0\) | \(v-k\) | \(-(k-1)/(kv)\) |
| \((z,B_2)\), \(z\in B_0\setminus\{p_0\}\), \(B_2\ne B_0\) | \(v-k\) | \(-(k-1)/(kv)\) |
| \((x,B_2)\), \(x\notin B_0\), \(B_2\cap B_0=\{z\}\), \(z\ne p_0\) | \((v-k)(k-1)\) | \(1/(kv)\) |
| All remaining incidence edges | remaining | \(0\) |

The table uses \((r-1)(k-1)=v-k\); no edge transitivity is assumed.

**3. Uniform shortest-bypass decomposition.** Any path from \(p_0\) to \(B_0\) that avoids the direct edge has odd length. Length three would require a second block containing two distinct points of \(B_0\), impossible by the unique-pair axiom. Every bypass of length five has the unique form
\[
p_0\longrightarrow B_1\longrightarrow x\longrightarrow B_2\longrightarrow z\longrightarrow B_0,
\]
where \(B_1\ni p_0\) differs from \(B_0\), \(x\in B_1\setminus\{p_0\}\), \(z\in B_0\setminus\{p_0\}\), and \(B_2\) is the unique block containing \(x,z\). Conversely every such choice gives one simple bypass. There are \((r-1)(k-1)^2=(v-k)(k-1)\) of them.

Give each bypass weight \(1/(kv)\). Its contribution to the six nonzero classes in the table is, respectively, zero on the direct edge, \((v-k)/(kv)\), \((k-1)^2/(kv)\), \(-(k-1)/(kv)\), \(-(k-1)/(kv)\), and \(1/(kv)\). Thus their sum equals the Poisson electrical flow off the root edge. The direct edge has current \(\rho\), and the path weights sum to
\[
\frac{(v-k)(k-1)}{kv}=1-\rho.
\]
The claimed convex decomposition follows. Since all bypass paths have the same directional current on each used edge, no absolute-value cancellations occur, and
\[
\|Q\mathbf1_e\|_1=\rho+5(1-\rho)=5-4\rho.
\]

**4. Complementary norm and full endpoint equalities.** Because \(Q\) is symmetric and its diagonal entry at the root is \(\rho\), the column of \(C=I-Q\) has \(1-\rho>0\) at the root and the negatives of all off-root electrical currents. Hence
\[
\|C\mathbf1_e\|_1=(1-\rho)+(5-4\rho-\rho)=6(1-\rho).
\]
The source edge was arbitrary, so **every** column has these norms. The operator \(\ell_1\)-norm is the maximum absolute column sum. Because \(Q\) and \(C\) are symmetric matrices, their \(\ell_\infty\)-norms equal their \(\ell_1\)-norms.

**5. Exact dominance boundary and sharp bounds.** Their difference is \(2\rho-1\). For \(k=2\), \(\rho=1/2+1/v>1/2\). For \(k=3\), \(\rho=1/3+2/v\), which exceeds \(1/2\) precisely when \(v<12\); admissible nontrivial Steiner triple orders below twelve are \(7,9\) (necessary arithmetic gives \(v\equiv1,3\pmod6\)). For \(k\ge4\), the identity \(NN^{\mathsf T}=(r-1)I+J\) has rank \(v\), so \(b\ge v\), whence \(r\ge k\) and \(v\ge k(k-1)+1\). Therefore
\[
\rho=\frac1k+\frac{k-1}{v}<\frac2k\le\frac12.
\]
No equality case exists. Finally, \(0<\rho<1\) gives strict universal bounds \(5-4\rho<5\) and \(6(1-\rho)<6\). For the projective plane of prime-power order \(q\), \(k=q+1\), \(v=q^2+q+1\), and \(\rho=q/v+1/(q+1)\to0\), so both bounds are sharp suprema.

## Verification

The companion dependency-free script `verify_steiner_currents.py` constructs five independent finite examples directly from their incidence rules, inverts their grounded graph Laplacians in exact rational arithmetic, and checks **every** edge column against the path decomposition, both endpoint norm formulas, diagonal effective resistance, symmetry, and (for examples of at most \(52\) edges) projector idempotence. The examples are the pair design on five points; projective planes of orders two and three; and affine planes of orders three and five. It passed \(279\) edge-column comparisons involving \(14{,}064\) enumerated bypass paths. Execution: `python3 verify_steiner_currents.py` (Python standard library only).

The exact computations corroborate the proof, but do not establish the assertion for all designs. That quantification follows from the incidence identity and explicit Poisson solution above.

## Relationship to prior work

Dilworth, Kutzarova, and Ostrovskii (2023) study cut/cycle subspaces and invariant/minimal projection problems, focusing on discrete tori and Hamming graphs. Here the projections are the **canonical** orthogonal projections for incidence graphs of arbitrary Steiner pair designs; their norm minimality among all projections is **not** asserted. Schild, Rao, and Srivastava (2017) give general logarithmic electrical-current localization bounds; Gurel-Gurevich, Nachmias, and Sachdeva (2026) improve the general bounds. Neither general bound implies a uniform equal-weight shortest-bypass decomposition or these sharp exact constants.

The symmetric-design/projective-plane special case of the endpoint formulas has appeared in related calculations. The new domain includes nonsymmetric Steiner designs (for example, the affine planes of orders three and five) and identifies an explicit, uniform length-five detour structure without requiring symmetry or a constant block-pair intersection number beyond the Steiner axiom. Related finite-design incidence-graph topology results study different invariants. Full bibliographic equivalence cannot be excluded beyond the inspected material.

## Limitations

The proof addresses real finite-dimensional orthogonal cut/cycle projections at the two endpoint exponents only, for unit-conductance incidence graphs of existing Steiner \(2\)-designs. It does not compute optimal projection constants over all projections, intermediate \(\ell_p\) norms, weighted incidences, nor the case \(\lambda>1\) in a general balanced incomplete block design. The sign-coherent five-edge path decomposition need not survive those modifications. Numerical checks cover only five finite examples. Literature novelty remains subject to independent bibliographic verification; no independent mathematical audit is claimed.

## References

1. S. J. Dilworth, D. Kutzarova and M. I. Ostrovskii, *Cycle spaces: invariant projections and applications to transportation cost*, arXiv:2305.12582v1, first posted 2023-05-21. Section 1 and Sections 2.6–2.7; primary MSC2020 46B04.
2. A. Schild, S. Rao and N. Srivastava, *Localization of Electrical Flows*, arXiv:1708.01632v1, first posted 2017-08-04. Especially Theorems 1.4 and 1.5.
3. O. Gurel-Gurevich, A. Nachmias and S. Sachdeva, *A Tight Bound on Localization of Electrical Flows*, arXiv:2605.24130v1, first posted 2026-05-22. Especially Theorems 1.2–1.4.

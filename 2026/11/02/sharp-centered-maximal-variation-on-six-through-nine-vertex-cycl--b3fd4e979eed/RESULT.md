# Sharp centered maximal variation on six- through nine-vertex cycles

## Finding

For each integer \(n\in\{6,7,8,9\}\), identify the vertices of the unit-edge cycle \(C_n\) with \(\mathbb Z/n\mathbb Z\). Let the **centered graph-ball maximal operator** be
\[
(M_nf)(i)=\max_{0\le r\le\lfloor n/2\rfloor}\frac{1}{|B(i,r)|}\sum_{j\in B(i,r)}|f(j)|,
\quad B(i,r)=\{j:d_{C_n}(i,j)\le r\}.
\]
For real data \(f\), set \(\operatorname{Var}_{C_n}(f)=\sum_{i=0}^{n-1}|f(i+1)-f(i)|\), with indices modulo \(n\). The exact optimal constants, **attained by a one-vertex indicator for each size**, are
\[
\boxed{\sup_{\operatorname{Var}_{C_n}(f)>0}
\frac{\operatorname{Var}_{C_n}(M_nf)}{\operatorname{Var}_{C_n}(f)}
=1-\frac1n,\qquad n=6,7,8,9.}
\]
In order, these constants are \(5/6\), \(6/7\), \(7/8\), and \(8/9\). The claim concerns **only these four cycle sizes**, not all finite cycles.

## Assumptions and scope

Each graph is the simple, undirected, unweighted cycle with counting measure, graph-distance balls (including the zero-radius singleton), and the ordinary edge-sum \(1\)-variation. The operator uses the absolute values of the input before averaging. Input data are arbitrary real-valued functions on the vertices. The initial normalization and all linear-program branch arguments are valid for these definitions; no regularity assumption on the data is required.

## Proof

**1. Reduction to normalized nonnegative data.** Since \(M_nf=M_n|f|\) and \(\operatorname{Var}_{C_n}(|f|)\le\operatorname{Var}_{C_n}(f)\), it suffices to consider \(f\ge0\). Replacing \(f\) by \(f-\min f\) preserves both numerator and denominator, because the maximal operator commutes with addition of a constant to a nonnegative input. Rotation places one minimum at vertex \(0\). If variation is nonzero, positive scaling normalizes \(\operatorname{Var}_{C_n}(f)=1\). Thus every quotient is bounded by the supremum over \(f_0=0\), \(f_j\ge0\) for \(1\le j<n\), and \(\operatorname{Var}_{C_n}(f)\le1\).

**2. Exact finite linear-program decomposition.** Put \(A_{i,r}f=|B(i,r)|^{-1}\sum_{j\in B(i,r)}f_j\). For each sign sequence \(\sigma\in\{-1,1\}^n\),
\[
\sum_i\sigma_i\bigl((M_nf)_{i+1}-(M_nf)_i\bigr)
=\sum_i c_i(M_nf)_i,
\quad c_i=\sigma_{i-1}-\sigma_i.
\]
The maximum over \(\sigma\) is precisely the output variation. For a fixed \(\sigma\), write \(P=\{i:c_i>0\}\) and \(N=\{i:c_i<0\}\). Expand each positive term by independently choosing one radius \(r_i\in\{0,\ldots,\lfloor n/2\rfloor\}\). For each negative term introduce \(z_i\ge A_{i,r}f\) for every radius; its negative coefficient forces the optimum to use \(z_i=(M_nf)_i\). Thus, exactly (without a relaxation gap), each sign/radius branch maximizes
\[
\sum_{i\in P}c_iA_{i,r_i}f+\sum_{i\in N}c_iz_i
\]
subject to \(f_0=0\), \(f_j\ge0\), the majorant constraints on \(z_i\), and auxiliary nonnegative \(t_i\) satisfying
\[
 f_{i+1}-f_i\le t_i,\qquad f_i-f_{i+1}\le t_i,
\qquad\sum_it_i\le1.
\]
All primal variables are nonnegative. There are no missing choices: the sign sequences and selected radii run through their entire Cartesian products. This reduction establishes that the global bound follows from the corresponding finite family of rational linear-program bounds.

**3. Exact dual certificates.** Each branch is of the form \(\max\{o\cdot x:Ax\le b,\ x\ge0\}\), with rational coefficients determined only by the graph balls. The accompanying file `cycles6to9_dual_certificates.json` supplies a sparse nonnegative rational dual vector \(y\) for **every** branch. `verify_cycles6to9.py`, using Python's standard library and integer arithmetic only, reconstructs the ball averages and each matrix from the definitions, checks \(A^\mathsf T y\ge o\), and checks \(b\cdot y\le(n-1)/n\) exactly. Since any feasible \(x\ge0\) satisfies \(o\cdot x\le y^\mathsf T Ax\le y^\mathsf T b\), weak duality proves the asserted upper bound. The verifier also checks that every sign/radius branch occurs exactly once. Its complete run verifies respectively \(730\), \(2186\), \(12032\), and \(38912\) dual certificates for \(n=6,7,8,9\), totalling \(53860\) branches and \(1039232\) exact integer comparisons of dual constraint coordinates.

**4. Sharpness.** Take \(f=\mathbf1_{\{0\}}\). The input variation is \(2\). The output depends only on cyclic distance \(k\) from vertex \(0\) and equals \(1/\min(2k+1,n)\) for \(0\le k\le\lfloor n/2\rfloor\). These values decrease from \(1\) to \(1/n\) along either arc; the output variation telescopes to \(2(1-1/n)\). The quotient is therefore exactly \((n-1)/n\), as required.

## Verification

From the directory containing the two accompanying standalone artifacts, run

```sh
python3 verify_cycles6to9.py cycles6to9_dual_certificates.json
```

The checker requires only the Python standard library. On the delivered certificate it reports four `PASS` lines and the final `PASS ALL` line recording \(53860\) dual certificates, \(1039232\) exact integer inequalities, and four point-mass witnesses. The certificates are proof data, not logs or statistical experiments: exact primal-to-dual reduction plus a verified feasible dual for each finite branch establishes the upper bound for every real input. No floating-point optimizer is trusted during replay.

## Relationship to prior work

Bober, Carneiro, Hughes and Pierce's discrete Tanaka theorem [1] concerns maximal variation on \(\mathbb Z\), including a sharp uncentered theorem and a different centered estimate. González-Riquelme and Madrid [2] provide sharp finite-graph results for complete and star graphs, not this four-case cycle classification. González-Riquelme, Kovač and Madrid [3] establish all four-vertex graph constants and present computational results through five vertices, as well as general complete-graph theorems; their cycle discussion includes \(C_4\), not \(C_6\) through \(C_9\). The related lower-bound statement for arbitrary cycles does not establish the upper-bound half proved here. The present result concerns the first two cycle-diameter strata beyond five vertices; no claim of originality is made for the earlier small-cycle cases.

## Limitations

The exact bound is proved only at \(n=6,7,8,9\). The certificate does not assert, imply, or computationally establish the same formula for any larger cycle or for paths. It does not address nonuniform vertex weights, weighted edge variation, \(p\)-variation for \(p\ne1\), or uncentered graph-ball maxima. Exhaustive verification is finite but exhaustive only over the specifically derived branches for those four vertex counts. Earlier independent equivalent calculations not indexed by the inspected sources remain a publication-priority possibility.

## References

[1] J. Bober, E. Carneiro, K. Hughes, L. B. Pierce, *On a discrete version of Tanaka's theorem for maximal functions*, arXiv:1005.3030 (first public submission 2010-05-17), https://arxiv.org/abs/1005.3030.

[2] C. González-Riquelme, J. Madrid, *Sharp Inequalities for Maximal Operators on Finite Graphs*, arXiv:2005.03146 (first submission 2020-05-06), https://arxiv.org/abs/2005.03146.

[3] C. González-Riquelme, V. Kovač, J. Madrid, *Sharp variational inequalities for the Hardy–Littlewood maximal operator on finite undirected graphs*, arXiv:2603.12462 (first submission 2026-03-12), https://arxiv.org/abs/2603.12462.

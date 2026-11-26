# Independent mathematical audit

## correctness

PASS

Reassessed the replacement RESULT.md. Singularity of a real covariance matrix is exactly the existence of a nonzero constant linear combination of the within-part edge totals on their finite full support. For any i,j with i in the first part and j in the second, put δ_x=w_ix-w_jx for the other vertices and R=A\{i}. Exchanging the two vertices in α W_A+β W_B gives (α+β)sum_R δ_x=β(d_i-d_j). If α+β=0 it forces constant degrees. Otherwise all (k-1)-subset sums of δ agree; k,ell>=2 means one can replace any available vertex with any other, so all δ_x equal. Fixing a reference vertex and using symmetry then yields all w_ij=u_i+u_j, as detailed in the replacement proof; conversely these weights give constant W_A/(k-1)+W_B/(ell-1), while constant degrees give constant W_A-W_B. Binary potentials are either all equal (empty or complete), or pick distinct potentials: the two rows differ by one and force all other potentials to a common c with 2c=0 or 1 (star or its complement). In the complement of a star the isolate lies in either part with positive probability; the possible within-edge vectors differ by (k-1,-(ell-1)), giving rank one. In the balanced case the cut is W-W_A-W_B. The quoted RISE bracket is exactly 2/[(N-1)N] times the frozen bracket and the equal-split variance prefactor for U_w is N^2/[8(N-3)]; rescaling by [4(N-1)/N]^2 gives the retained formula. Solving the normal equations yields the stated projection and unique potentials. Boundaries N=4, both parts of size two, and odd N for the covariance-only result are accounted for.

## originality

PASS

Only the repaired structural correction is credited. The version-read Chen–Friedman theorem explicitly lists regular graphs and stars, while a clique plus an isolate is neither and always gives singular covariance. The inspected Zhou–Chen numerical conditions cover the weighted moment/degeneracy formula, not a correct graph-family list in the read text. The repair identifies that missing family and proves that no other unweighted exceptions occur, for all allowed sizes. The weighted projection and the moment calculations, which are directly covered, are now background. No claim is made that a journal version or an uninspected correction has the same omission.

## value

PASS

The repair corrects a concrete invertibility assertion for the covariance used in a permutation test. It gives an explicit omitted family, an exact proof of all degenerate simple graph cases for unequal as well as equal parts, and a usable structural explanation in terms of weights, rather than treating a prior second moment as new. The balanced trace estimator is a transparent application to the cut-constancy subcase.

The dated certificate retains the supplied scientific assessment, sources and limitations.

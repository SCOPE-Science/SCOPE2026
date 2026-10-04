# Review of Exact \(\Delta\)-constants for every point of \(c_0\)

## Correctness
PASS. The lower bound starts from an arbitrary slice containing \(x\) and proves that its radius \(R\) satisfies the active-coordinate inequality \(\Phi_x(R)\le1\). The proof checks the sign of every active coefficient, the slice slack \(q=1-a(x)\), and the sharp denominator \(R+1-|x_i|\). The upper bound explicitly normalizes a supporting \(\ell_1\)-functional at every feasible radius and bounds every coordinate of the resulting slice. Infinite support is handled because active sets are finite away from \(r=1\), while residual functional mass is placed on an inactive tail coordinate and its value is tracked exactly by \(\tau=a_kx_k\). The accompanying standard-library script recovers the known exact family and checks heterogeneous witnesses.

Risk: the infinite-support upper construction must account for the chosen inactive tail coordinate possibly having nonzero \(x_k\); the proof tracks this exactly through \(\tau=a_kx_k\) rather than assuming a zero coordinate exists.

## Originality
PASS. The closest inspected source is Choi--Jung, arXiv:2307.10647. In its \(c_0\) section, Theorem 3.3 gives lower bounds for arbitrary points and Remark 3.4(3) gives an exact formula only for \(t\sum_{k=1}^n e_k\). Substitution shows that the present active-sum formula recovers that family, while the cited lower bounds do not imply the heterogeneous or infinite-support cases. Targeted semantic searches for exact \(c_0\) \(\Delta\)-constant formulas and the displayed rational threshold found no covering statement. Abrahamsen--Lima--Martiny--Perreau, arXiv:2203.14528, supplies qualitative/asymptotic background but no exact pointwise quantitative formula.

Risk: search coverage is not a proof of novelty, and an equivalent unindexed formulation may exist.

## Value
PASS. The invariant was introduced specifically to quantify how far points are from being \(\Delta\)-points, and the primary source leaves the \(c_0\) case at bounds plus special exact families. The theorem gives an exact coordinate-level answer for every point of \(B_{c_0}\), yields nontrivial heterogeneous values such as \((3+\sqrt{33})/8\), and explains the known equal-coordinate phase transition through an active-set threshold. The result is mathematically natural and not a finite-table recomputation.

Risk: the mechanism depends on remote coordinates of \(c_0\), so no finite-dimensional \(\ell_\infty^N\) analogue is claimed.

## Closest literature and limitations
The primary comparison is G. Choi and M. Jung, *The Daugavet and Delta-constants of points in Banach spaces*, arXiv:2307.10647, especially Definition 2.1 and Section 3.1. The broader background is T. A. Abrahamsen, V. Lima, A. Martiny, and Y. Perreau, *Asymptotic geometry and Delta-points*, arXiv:2203.14528. The proof is for real \(c_0\) only; complex scalars, finite-dimensional \(\ell_\infty^N\), and other sequence spaces remain outside scope.

Same-model review: passed. Independent audit: not yet performed.

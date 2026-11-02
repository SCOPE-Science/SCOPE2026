# Exact distance and nonproximinality of orthogonal positive sums in \(C([0,1])\)

## Finding

For an integer \(k\ge 2\), let \(\mathcal I_k\) be the collection of functions
\[
 g=h_1+\cdots+h_k\in C([0,1]),\qquad
 h_j\ge0,\quad \|h_j\|_\infty=1,\quad h_ih_j=0\quad(i\ne j).
\]
For every positive norm-one \(f\in C([0,1])\), set \(d_k(f)=\inf_{g\in\mathcal I_k}\|f-g\|_\infty\). Then the **exact ordered peak–valley formula** is
\[
 d_k(f)=\inf_{0\le t_1<s_1<t_2<s_2<\cdots<s_{k-1}<t_k\le1}
 \max\left\{\max_{1\le j\le k}\bigl(1-f(t_j)\bigr),
              \max_{1\le j<k}f(s_j)\right\}.\tag{1}
\]
A nearest point in \(\mathcal I_k\) exists **if and only if** the objective in (1) has an ordered configuration with value at most \(d_k(f)\). The set \(\mathcal I_k\) is norm closed, but it is not proximinal: for \(f(t)=t\),
\[
 d_k(f)=\tfrac12\quad\text{for every }k\ge2,
\]
and no nearest point exists.

Furthermore \(d_k(f)\) is nondecreasing in \(k\), and if \(m=\min_{[0,1]}f\), then
\[
 \lim_{k\to\infty}d_k(f)=\max\{\tfrac12,m\}.\tag{2}
\]
For piecewise-affine \(f\) with ordered vertices \(0=x_0<\cdots<x_N=1\) and heights \(v_i=f(x_i)\), (1) admits the exact finite formula
\[
 d_k(f)=\min\left\{\max\{\tfrac12,\min_i v_i\},\quad
 \min_{0\le i_1<j_1<i_2<\cdots<j_{k-1}<i_k\le N}
 \max\left\{\max_{1\le r\le k}(1-v_{i_r}),\
                 \max_{1\le r<k}v_{j_r}\right\}\right\}.\tag{3}
\]
An empty inner minimum is interpreted as \(+\infty\). Thus rational vertex data give an exact rational distance.

## Assumptions and scope

The algebra is the complex commutative unital \(C^*\)-algebra \(C([0,1])\), with pointwise multiplication and the uniform norm. Positive elements are nonnegative real-valued continuous functions. The integer \(k\) ranges over every integer at least two. The input \(f\) satisfies \(0\le f(t)\le1\) everywhere and \(\max f=1\). In (1), all inequalities between adjacent witness points are strict; the first or last peak may lie at an endpoint. The infimum may be unattained. Statements (1), (2), and the nearest-point characterization concern **all** such continuous inputs; formula (3) additionally assumes piecewise-affinity with finitely many vertices.

## Proof

**1. Peaks and separators.** Suppose \(g=\sum_{j=1}^k h_j\in\mathcal I_k\). Each \(h_j\) takes value one somewhere. At any point where \(g>0\), exactly one \(h_j\) is positive, and its index is constant on each connected component of the open set \(\{g>0\}\): the ratios \(h_j/g\) are continuous and take only values zero or one. Therefore the \(k\) norm-one peaks can be selected from \(k\) different components of \(\{g>0\}\), ordered from left to right. Between any two consecutive selected components is a point where \(g=0\). This produces \(t_1<s_1<t_2<\dots<s_{k-1}<t_k\) with \(g(t_j)=1\), \(g(s_j)=0\). For \(\delta=\|f-g\|_\infty\), the peak inequalities \(1-f(t_j)\le\delta\) and valley inequalities \(f(s_j)\le\delta\) yield the lower bound in (1).

**2. Sharp reverse construction.** Conversely, fix a strictly ordered configuration as in (1) and let \(\delta\) be its objective. Define the continuous envelopes
\[
 L(t)=\max\{f(t)-\delta,0\},\qquad U(t)=\min\{f(t)+\delta,1\}.
\]
Because \(0\le f\le1\), one has \(0\le L\le U\le1\) and \(\|f-v\|_\infty\le\delta\) for any continuous \(v\) with \(L\le v\le U\). Choose continuous piecewise-affine \(w:[0,1]\to[0,1]\) with \(w(t_j)=1\) and \(w(s_j)=0\). Put \(g=L+(U-L)w\). The peak hypotheses imply \(U(t_j)=1\), while the separator hypotheses imply \(L(s_j)=0\). Therefore \(g(t_j)=1\), \(g(s_j)=0\), \(0\le g\le1\), and \(\|f-g\|_\infty\le\delta\). Restrict \(g\) to the consecutive closed intervals bounded by the separator points, setting it equal to zero outside each such interval. These \(k\) pieces are continuous (because \(g\) vanishes at every cut), nonnegative, mutually orthogonal, and each has norm one. Thus \(g\in\mathcal I_k\). This proves (1); the same two directions prove the stated nearest-point criterion with \(\delta=d_k(f)\).

**3. Closedness.** If \(g_n\in\mathcal I_k\) converges uniformly, choose the ordered peak and zero witnesses from Step 1. By compactness of \([0,1]^{2k-1}\), along a subsequence all their coordinates converge. The limiting function takes value one at the limiting peaks and zero at the limiting separators. Two adjacent limiting coordinates cannot coincide, since adjacent coordinates have opposite function values. Thus the limiting witnesses remain strictly ordered. The splitting construction of Step 2, applied with \(f=g\) and \(\delta=0\), places the limit in \(\mathcal I_k\). Hence \(\mathcal I_k\) is norm closed.

**4. Nonattainment.** Let \(f(t)=t\). In any ordered configuration, \(t_1<s_1\); therefore \(\max\{1-t_1,s_1\}>1/2\). Taking all ordered points arbitrarily close to \(1/2\) makes the objective tend to \(1/2\). Equation (1) gives \(d_k(f)=1/2\) but no configuration attains this objective. By Step 2, no nearest point in \(\mathcal I_k\) exists. This is nonproximinality even though the set is closed.

**5. Large-\(k\) upper bound.** Merging any two orthogonal norm-one summands gives another nonnegative norm-one summand, so \(\mathcal I_{k+1}\subseteq\mathcal I_k\) and \(d_{k+1}(f)\ge d_k(f)\). Let \(m=\min f\). Since \(f([0,1])=[m,1]\), one can choose a point at which \(\max\{1-f(t),f(t)\}\) is minimal, and this minimum is \(\max\{1/2,m\}\). For any fixed \(k\), one can place \(2k-1\) strictly ordered points arbitrarily close to that point, from the available side when it is an endpoint. Continuity of \(f\) and (1) give
\[
 d_k(f)\le\max\{1/2,m\}.\tag{4}
\]

**6. Large-\(k\) lower bound.** Every \(g\in\mathcal I_k\) vanishes somewhere, hence \(d_k(f)\ge m\). Fix \(\delta<1/2\). If an ordered witness had objective at most \(\delta\), each adjacent high/low pair would exhibit a change of at least \(1-2\delta>0\) in the value of \(f\). Uniform continuity gives a length \(\eta>0\) below which such a change is impossible. In particular the \(k-1\) distinct intervals \([t_j,s_j]\) would each have length at least \(\eta\), so \(k-1\le1/\eta\). Thus for all sufficiently large \(k\), every witness objective exceeds \(\delta\), and (1) gives \(d_k(f)\ge\delta\). Letting \(\delta\uparrow1/2\) proves \(\liminf_kd_k(f)\ge1/2\). Combining this with \(d_k(f)\ge m\) and (4) proves (2).

**7. Exact finite formula.** The clustering argument in Step 5 yields the first candidate \(\delta_0=\max\{1/2,\min_i v_i\}\) in (3); any strict vertex witness yields the second candidate. Hence the right side of (3) is at least \(d_k(f)\). For the converse, there is nothing to show if \(d_k(f)=\delta_0\). If \(d_k(f)<\delta_0\), then \(\min_i v_i\le1/2\), because \(d_k(f)\ge\min f\), and hence \(\delta_0=1/2\). Pick any \(\delta\) strictly between \(d_k(f)\) and \(1/2\). By (1) there is a witness with peaks at values greater than \(\delta\), indeed at least \(1-\delta>\delta\), and with separating valleys at values at most \(\delta\). The peaks belong to distinct ordered components of the superlevel set \(\{f>\delta\}\). In each selected component, a maximum is attained at a piecewise-affine vertex with value at least the original peak value. Between two chosen high vertices, a minimum is attained at a vertex and is at most the original separator value. Thus there are strictly ordered high and low **vertices** whose objective is at most \(\delta\). Taking \(\delta\downarrow d_k(f)\) proves (3). No passage from a finite grid to a proof for arbitrary continuous functions is made.

## Verification

The standalone `checker.py` uses only Python's standard library and performs deterministic finite consistency tests on exact rational piecewise-affine functions. Run `python3 checker.py` to obtain `PASS: 940 rational finite consistency checks`. It compares the rational vertex formula with independently refined-grid witness bounds, checks monotonicity in \(k\), tests the identity-function distance, and explicitly constructs envelope interpolants with prescribed peaks/zeros at sample points. All asserted equalities in the theorem are proved in Steps 1–7; finite checks only guard against algebraic and implementation mistakes.

## Relationship to prior work

Taghavi [1, Theorem 3.2] establishes norm closedness of the **two-summand** locus \(\mathcal I(C(X))\) for compact locally path-connected spaces and characterizes its membership using components of the complement of a zero set. He also determines the distance of the identity element to that locus. The present result retains those established facts and studies a different quantitative problem: the full point-to-set distance from arbitrary positive norm-one functions, existence of nearest points, and the entire hierarchy of \(k\) orthogonal norm-one summands. Formula (1) recovers the known membership condition at distance zero for \(k=2\), but the sharp distance, nonattainment example, and asymptotic law (2) are distinct statements.

The earlier note [2] studies positive zero divisors and the distance of the identity to their normalized orthogonal sums; it does not compute the uniform approximation distance of a general input or an all-\(k\) hierarchy. The finite-vertex expression (3) is not a claim about a previously published numerical table. Biswas, Cultrera di Montesano, Edelsbrunner, and Saghafian [3] characterize critical-pair persistence and variation for one-dimensional maps. Their persistence-pair and total-variation results do not determine the distance to normalized, pairwise-annihilating positive summands or its failure of nearest-point attainment. General Chebyshev equioscillation for polynomial approximation concerns a linear approximating space, unlike the nonlinear, nonproximinal locus here.

## Limitations

These results are for the interval algebra and positive norm-one inputs, not for all compact spaces, arbitrary signed functions, or noncommutative algebras. Formula (3) requires piecewise-affinity. The infimum in (1) need not be attained; no canonical global metric projection is asserted. The large-\(k\) limit has no rate claim without additional regularity of \(f\). The literature comparison is best-knowledge rather than a proof of publication priority; equivalent descriptions in older nonlinear approximation or zero-dimensional persistence literature remain a residual risk.

## References

[1] Ali Taghavi, *On the set of orthogonal positive sums in a \(C^*\)-algebra*, arXiv:2610.15167, initially submitted 2026-10-10. In particular, Theorems 3.1–3.2 and their proofs. https://arxiv.org/abs/2610.15167

[2] Ali Taghavi, *A Note on Positive Zero Divisors in \(C^*\)-Algebras*, arXiv:1301.3129, initially submitted 2013-01-13. https://arxiv.org/abs/1301.3129

[3] Ranita Biswas, Sebastiano Cultrera di Montesano, Herbert Edelsbrunner, and Morteza Saghafian, *Geometric characterization of the persistence of 1D maps*, Journal of Applied and Computational Topology 8 (2024), 1101–1119; publicly available in 2023. https://pmc.ncbi.nlm.nih.gov/articles/PMC11639680/

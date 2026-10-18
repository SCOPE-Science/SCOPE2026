# Monotone sorting-bottleneck relocation and a four-species cusp

## Finding

The sorting-time variational formula for a finite-speed multispecies totally asymmetric exclusion process has a non-reentrance property under variation of its slowest speed. Let \(K\geq3\) and hold \(0=v_1<v_2<\cdots<v_{K-1}\) fixed while setting \(v_0=-a\), \(a>0\). Write \(C_m(a)\) for the deterministic contribution of the cut between species \(m-1\) and \(m\), for \(1\leq m<K\). Then, for every pair \(1\leq m<\ell<K\),

\[
\frac{d}{da}\bigl(C_m(a)-C_\ell(a)\bigr)<0.
\]

Consequently any maximizing cut can move only from lower indices to higher indices as \(a\) increases; there is no reentrance, every pair of cut curves crosses at most once, and each actual change in the maximizing cut creates a strictly upward jump in the derivative of the limiting sorting-time coefficient.

A complete nontrivial instance occurs for four species with speeds \((-a,0,1,2)\), \(0<a\leq1\). There exists a unique \(a_*\in(467/500,187/200)\) such that the maximizing cut is exactly cut \(1\) for \(0<a<a_*\), cuts \(1\) and \(2\) tie at \(a=a_*\), and cut \(2\) is uniquely maximal for \(a_*<a\leq1\). Cut \(3\) is never maximal in this range. The asymptotic sorting-time coefficient has a genuine transverse corner at \(a_*\). In particular, for \(a\in(a_*,1)\) the *smallest adjacent speed gap* is \(a\), but the bottleneck is the *second*, larger gap of size \(1\).

## Assumptions and scope

There are \(n\) particles of each of \(K\) species, initially arranged in reverse increasing-speed order on a line. Adjacent particles of types \(i>j\) exchange at rate \(v_i-v_j\); slower particles do not overtake faster particles. Speeds are real and strictly increasing. Let \(T_{Kn}\) denote the completion time. Maga and Tóth [1, Theorem 1.2] establish, under these fixed-speed assumptions, the almost-sure limit

\[
\lim_{n\to\infty}\frac{T_{Kn}}{Kn}=G(a):=\max_{1\leq m<K}C_m(a),
\qquad C_m(a)=\frac1K\min_{v_{m-1}<z<v_m}F_m(a,z),
\]

where

\[
F_m(a,z)=\sum_{0\leq j<m}\frac1{z-v_j}
             +\sum_{m\leq j<K}\frac1{v_j-z}.
\]

This established limit formula is an input, not a new result. Here the novelty is the global organization of its maximizing cut as one speed varies and the exact four-species transition. The species count \(K\) and speeds other than \(v_0\) stay fixed before the particle multiplicity \(n\) tends to infinity.

## Proof

**Unique minimizers and ordered locations.** For each cut, the function \(F_m(a,\cdot)\) tends to \(+\infty\) at both endpoints of its defining gap and has

\[
\partial_z^2F_m(a,z)=2\sum_{j<m}(z-v_j)^{-3}
            +2\sum_{j\geq m}(v_j-z)^{-3}>0.
\]

Thus it has a unique minimizer \(z_m(a)\in(v_{m-1},v_m)\). The first derivative of \(F_m\) is strictly increasing from \(-\infty\) to \(+\infty\), so \(z_m(a)\) is smooth in \(a\) by the implicit function theorem. Since its location lies in the \(m\)-th adjacent gap, \(z_1(a)<z_2(a)<\cdots<z_{K-1}(a)\).

**Strict single-crossing.** In every \(F_m\), the term containing \(v_0=-a\) is \((z+a)^{-1}\), on the left of the cut. Differentiating the optimized value (the envelope theorem, or the chain rule using \(\partial_zF_m(a,z_m(a))=0\)) gives

\[
C_m'(a)=-\frac{1}{K(z_m(a)+a)^2}.
\]

All denominators are positive. The strict ordering of the \(z_m\)'s therefore yields

\[
C_1'(a)<C_2'(a)<\cdots<C_{K-1}'(a)<0.
\]

Hence \(C_m-C_\ell\) is strictly decreasing for each \(m<\ell\). If \(a<b\) and a maximizer at \(a\) has index \(m\), no maximizer at \(b\) can have index strictly less than \(m\), since this would reverse the strict pairwise difference inequality. Each cut-pair can tie at most once. At an actual change in the upper envelope \(G\), all active curves have distinct slopes ordered by their indices. The left derivative of a finite maximum is the minimum slope among active curves and the right derivative is their maximum slope. The slope jump is therefore strictly positive. These assertions hold without any genericity or transversality assumptions on the remaining speeds.

**Why four species are minimal.** With only three species and speeds \((-a,0,b)\), where \(a,b>0\), reflection at \(a=b\) gives \(C_1(b)=C_2(b)\). The already-proved strict decrease of \(C_1(a)-C_2(a)\) shows that the first cut dominates exactly for \(a<b\), the second exactly for \(a>b\), and they tie at equality. Thus for two or three species the narrowest adjacent speed gap always identifies a maximizing cut; a disagreement requires at least four species.

**Four-species phase diagram.** Now take \(K=4\) and \(v=(-a,0,1,2)\) with \(0<a\leq1\). At \(a=1\), the symmetry of the middle gap shows that \(z_2(1)=1/2\) and direct substitution gives \(C_2(1)=4/3\). Trial points \(z_1=-1/2\) and \(z_3=3/2\) give

\[
C_1(1)\leq19/15,\qquad C_3(1)\leq19/15<4/3=C_2(1).
\]

Since \(C_2(a)-C_3(a)\) is strictly decreasing with \(a\), it follows that \(C_2(a)>C_3(a)\) throughout \(0<a\leq1\). Meanwhile, in the first gap \((-a,0)\), retaining only the two nearest pole terms gives

\[
C_1(a)\geq\frac14\min_{-a<z<0}\left(\frac1{z+a}+\frac1{-z}\right)=\frac1a.
\]

The second-cut value \(C_2(a)\) remains bounded as \(a\downarrow0\) (evaluate its objective at \(z=1/2\)). Thus \(C_1(a)-C_2(a)\to+\infty\) as \(a\downarrow0\), while \(C_1(1)-C_2(1)<0\). The difference is continuous and strictly decreasing, so a unique zero \(a_*\in(0,1)\) exists. Combined with \(C_2>C_3\), this proves the complete three-regime classification and the strict corner.

**Certified rational interval for the transition.** For a gap of width \(d=v_m-v_{m-1}\), the two nearest poles give the global strong-convexity bound

\[
\partial_z^2F_m(a,z)\geq\frac{32}{d^3}=:\mu_m.
\]

At any interior rational trial point \(z\), strong convexity gives an explicit two-sided enclosure:

\[
\frac{F_m(a,z)-[\partial_zF_m(a,z)]^2/(2\mu_m)}4
\leq C_m(a)\leq\frac{F_m(a,z)}4.
\]

A 22-step rational bisection on the sign of \(\partial_zF_m\) locates a trial point in each relevant gap. The bundled exact-rational checker verifies \(C_1(467/500)>C_2(467/500)\) and \(C_1(187/200)<C_2(187/200)\), establishing the stated enclosure of \(a_*\) without floating-point assumptions.

## Verification

Run the standalone standard-library Python file `verify.py` with `python3 verify.py`. It uses rational arithmetic (`fractions.Fraction`) for all variational evaluations, stationary-point bisections, convexity enclosures, and endpoint inequalities. Its output reports both exact-rational interval comparisons; decimal displays are illustrative only. The proof of strict single-crossing, the four-species classification, and the unlimited-particle asymptotic is analytic and does not rest on finite numerics.

As a supplementary non-certified location estimate, solving the two scalar minimization problems numerically gives \(a_*\approx0.9341680315\). Neither this decimal nor finite-particle simulations are needed for any theorem statement.

## Relationship to prior work

Maga and Tóth [1] provide the original sorting process, the reduction to a maximum over cuts, the last-passage representation, and the exact variational formula for each cut. Those results are neither reproved as original nor claimed as new. They do not state the ordered parameter sensitivity, no-reentrance principle, or four-species cusp/incorrect-smallest-gap classification derived here.

General results on inhomogeneous directed last-passage shapes [2] provide background for the variational structure, and permutation invariance results for inhomogeneous last-passage models [3] address different parameter symmetries. Neither treatment, in the inspected material, analyzes which contiguous speed cut maximizes the sorting time when one extreme speed varies. The present result is a structural analysis of a known variational formula, not a new last-passage limit theorem.

## Limitations

The no-reentrance assertion concerns variation of the *slowest* speed while all other speeds are fixed, not arbitrary simultaneous perturbations of species speeds. The explicit phase diagram covers only the specified four-species family with \(0<a\leq1\). It proves limiting sorting-time behavior as \(n\to\infty\), not finite-\(n\) transition points or fluctuation laws. The original variational formula is an essential external hypothesis. Earlier undiscovered analyses of parametric cut optimization might give another route to the same conclusion; the literature comparison does not certify exclusive priority.

## References

[1] Balázs Maga and Bálint Tóth, *Microscopic sorting in a multispecies exclusion process*, arXiv:2610.08135v1 (publicly submitted 2026-10-06), https://arxiv.org/abs/2610.08135 . Theorem 1.2 and the examples following it.

[2] Elnur Emrah, Christopher Janjigian and Timo Seppäläinen, *Flats, spikes and crevices: the evolving shape of the inhomogeneous corner growth model*, arXiv:1908.09319, https://arxiv.org/abs/1908.09319 . Shape-theorem background and variational structure.

[3] Erik Bates, Elnur Emrah, James B. Martin, Timo Seppäläinen and Evan Sorensen, *Permutation invariance in last-passage percolation and the distribution of the Busemann process*, arXiv:2506.12641, https://arxiv.org/abs/2506.12641 . Permutation invariance in related inhomogeneous models.

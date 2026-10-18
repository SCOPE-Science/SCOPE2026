# Exact margin and robustness laws for the tetrahedral spherical Voronoi partition

## Finding
Let \(v_1=(1,1,1)/\sqrt3\), \(v_2=(1,-1,-1)/\sqrt3\), \(v_3=(-1,1,-1)/\sqrt3\), and \(v_4=(-1,-1,1)/\sqrt3\). Independently choose \(U\) with uniform surface-area distribution on the unit sphere \(S^2\), and order the four cosine similarities \(U\cdot v_i\) as \(X_{(1)}<X_{(2)}<X_{(3)}<X_{(4)}\) (ties occur with probability zero). Define the nonnegative winner-to-runner-up margin
\[
\Delta=X_{(4)}-X_{(3)}.
\]
Set \(\kappa=\sqrt{8/3}\), \(s=t/\kappa\), \(\alpha=\arctan(1/\sqrt2)\), and
\[
H(s)=\arccos\!\left(\frac{s}{\sqrt{3(1-s^2)}}\right)-\alpha,
\qquad 0\le s\le\sqrt{2/3}.
\]
Then \(\Delta\) has support \([0,4/3]\), with no endpoint atoms, and its **complete density** is
\[
f_\Delta(t)=\frac6{\pi\kappa}H(t/\kappa),\qquad 0<t<4/3,
\]
zero outside that interval. Its **complete distribution function** is
\[
F_\Delta(t)=\frac6\pi\left[sH(s)+\arctan\sqrt3-\arctan\sqrt{3-4s^2}\right],
\qquad s=t/\kappa,\quad 0\le t\le4/3,
\]
with \(F_\Delta(t)=0\) for \(t<0\), and \(F_\Delta(t)=1\) for \(t>4/3\). The density is strictly decreasing on its support. The first two moments are
\[
\mathbb E\Delta=\frac{2\sqrt6}{\pi}\arcsin\frac13,
\qquad
\mathbb E\Delta^2=\frac89-\frac8{3\pi\sqrt3}.
\]

The same law exactly determines the **geodesic stability radius** of tetrahedral nearest-vertex classification. Let \(\mathcal B\) be the union of great-circle arcs forming the boundaries of the four spherical Voronoi cells of \(\{v_i\}\), and define \(R=\operatorname{dist}_{S^2}(U,\mathcal B)\). Then pointwise away from ties,
\[
R=\arcsin(\Delta/\kappa).
\]
In particular, the fraction of uniform directions whose nearest tetrahedral vertex remains unchanged under **every** spherical perturbation of angular size below \(r\) is
\[
\Pr(R>r)=1-F_\Delta(\kappa\sin r),\qquad
0\le r\le\arctan\sqrt2.
\]
The endpoint \(\arctan\sqrt2\) is the maximal geodesic stability radius.

## Assumptions and scope
Everything takes place in Euclidean three-space with the four explicitly normalized vertices above, or in any rotated copy. The query direction is sampled uniformly in spherical surface area; no Gaussian or coordinate-biased sampling is used. All probabilities refer to this random direction alone, not to collision events between two correlated directions. The angular radius is measured along shorter great-circle arcs on \(S^2\). A point exactly on a Voronoi boundary has radius zero; boundary ties have surface measure zero.

## Proof
**1. Coordinate order and parity.** Partition the sphere, excluding a measure-zero set, according to the permutation of \((|U_1|,|U_2|,|U_3|)\) and its three coordinate signs. Let \(a>b>c>0\) be those ordered absolute values, satisfying \(a^2+b^2+c^2=1\), and let \(\epsilon\) be the product of the coordinate signs. The 48 signed-permutation chambers have equal area \(\pi/12\); sign parity is independent of \((a,b,c)\), and each parity has probability \(1/2\). Directly sorting the four tetrahedral dot products yields
\[
\Delta=\frac2{\sqrt3}\begin{cases}
b+c,&\epsilon=+1,\\
b-c,&\epsilon=-1.
\end{cases}
\]
These identities do not require a probabilistic approximation.

**2. Exact angular slices.** Work in the spherical chamber \(T=\{a\ge b\ge c\ge0\}\). Define \(s_+=(b+c)/\sqrt2\) and \(s_-=(b-c)/\sqrt2\); in either case \(\Delta=\kappa s_\pm\). Put \(w=\sqrt{1-s^2}\). For \(s_+\), use spherical coordinates
\[
(a,b,c)=\left(w\cos\phi,\frac{s+w\sin\phi}{\sqrt2},\frac{s-w\sin\phi}{\sqrt2}\right).
\]
The inequalities \(b\ge c\ge0\) and \(a\ge b\) give
\[
0\le\phi\le\min\left\{\arcsin(s/w),H(s)\right\}
\]
with the first bound interpreted as vacuous when \(s\ge w\). The chamber exists exactly for \(0\le s\le\sqrt{2/3}\). The two angular bounds cross at \(s=1/2\). Thus the angular slice length of \(s_+\) is \(\arcsin(s/w)\) on \([0,1/2]\) and \(H(s)\) on \([1/2,\sqrt{2/3}]\).

For \(s_-\), instead use
\[
(a,b,c)=\left(w\cos\phi,\frac{s+w\sin\phi}{\sqrt2},\frac{w\sin\phi-s}{\sqrt2}\right).
\]
The chamber constraints become \(\arcsin(s/w)\le\phi\le H(s)\), possible exactly when \(0\le s\le1/2\). This slice has length \(H(s)-\arcsin(s/w)\). For both parametrizations the spherical surface element is precisely \(d\phi\,ds\).

**3. Cancellation and density.** Divide the slice lengths by the spherical chamber area \(\pi/12\). Averaging the two independent parity cases with weights \(1/2\), the parts involving \(\arcsin(s/w)\) cancel exactly on \([0,1/2]\), while only the positive-parity slice contributes for \(1/2<s<\sqrt{2/3}\). Consequently the unconditional density of \(s\) is \(6H(s)/\pi\) throughout \([0,\sqrt{2/3}]\), which under \(t=\kappa s\) gives the asserted \(f_\Delta\). In particular there is **no spurious change of formula at the parity-slice crossing**.

**4. Integration and moments.** Direct differentiation gives
\[
H'(s)=-\frac1{(1-s^2)\sqrt{3-4s^2}},
\qquad H(\sqrt{2/3})=0.
\]
Integrating by parts and substituting \(z=\sqrt{3-4s^2}\) gives
\[
\int_0^s H(u)\,du=sH(s)+\arctan\sqrt3-\arctan\sqrt{3-4s^2},
\]
hence the displayed CDF, including \(F_\Delta(4/3)=1\). For any integer \(k\ge0\),
\[
\mathbb E\Delta^k
=\frac{6\kappa^k}{\pi(k+1)}
\int_0^{\sqrt{2/3}}\frac{s^{k+1}\,ds}{(1-s^2)\sqrt{3-4s^2}}.
\]
For \(k=1\), substituting \(s=(\sqrt3/2)\sin\theta\) evaluates the integral as \(\arcsin(1/3)\). For \(k=2\), the substitution \(z=\sqrt{3-4s^2}\) evaluates it as \(\pi/6-1/(2\sqrt3)\). These yield the stated moments. Since \(H'<0\) and \(H>0\) in the open interval, the density is strictly decreasing.

**5. Geodesic robustness.** On a nearest-vertex Voronoi cell with winner \(v_i\), the three inequalities \(U\cdot(v_i-v_j)\ge0\) define its boundaries. All six tetrahedral edge vectors have the same norm \(\|v_i-v_j\|=\kappa\). For a point satisfying the inequalities, its spherical distance to their union's first crossing is the minimum of the distances to these three great circles, namely
\[
\min_{j\ne i}\arcsin\frac{U\cdot(v_i-v_j)}\kappa
=\arcsin\frac\Delta\kappa.
\]
The nearest-point angular stability law follows by a strictly increasing change of variable, and the maximum radius follows from \(\Delta\le4/3\).

## Verification
Running `python checker.py` requires only Python's standard library. It independently computes the four score values over all 48 signed permutations of a strictly ordered coordinate triple, checks 89 distinct CDF thresholds against numerical density integration, compares normalized mass and the first two moments against their closed forms, and checks 180,000 directly sampled uniform-sphere directions against six CDF thresholds. It also compares the margin-angle formula with distances computed separately from all competing decision great circles. An observed successful execution printed:

```
TETRAHEDRAL_VORONOI_MARGIN_OK deterministic=48 cdf_checks=89 sample=180000
integral=1 mean=0.529939502485 second_moment=0.398818759625 max_angle_error=0
empirical_mean=0.530696354461 empirical_second=0.399982340878 max_CDF_discrepancy=0.001059
```

The exact all-direction theorem is established by the analytic chamber proof, not by the finite numerical comparisons.

## Relationship to prior work
Andoni, Indyk, Laarhoven, Razenshteyn, and Schmidt (arXiv:1509.02897, first posted 2015-09-09) analyze angular nearest-neighbor hashing by regular polytopes. Their multiprobe discussion ranks coordinate scores for cross-polytope codes, but does not give this tetrahedral score-gap distribution or the exact tetrahedral stability law. Laarhoven (arXiv:1907.04628, first posted 2019-07-10) explicitly studies spherical Voronoi quantization with the tetrahedron and obtains a six-dimensional Gaussian orthant expression for the collision probability of **two correlated queries**, not the one-query winner-to-runner-up gap distribution. Related spherical-cap union measurements concern the maximum score alone, which does not determine the joint highest-two-score gap. Existing normal-distance or shadow results for other polyhedral codes do not imply the tetrahedral formula.

## Limitations
This theorem treats exactly one specified four-word spherical code and a single uniform query direction. It does not characterize arbitrary spherical codes, nonuniform input distributions, classification noise under a specified stochastic perturbation, or two-query collision probabilities. Its angle-stability statement is adversarial (all angular perturbations up to a radius), not a stochastic noise model. Literature overlap searches do not prove historical priority; general inner-parallel-area formulae for spherical polygons may offer an equivalent derivation. No independent mathematical audit has been performed.

## References
1. A. Andoni, P. Indyk, T. Laarhoven, I. Razenshteyn, and L. Schmidt, *Practical and Optimal LSH for Angular Distance*, arXiv:1509.02897 (first posted September 9, 2015), https://arxiv.org/abs/1509.02897.
2. T. Laarhoven, *Polytopes, lattices, and spherical codes for the nearest neighbor problem*, arXiv:1907.04628 (first posted July 10, 2019), https://arxiv.org/abs/1907.04628.

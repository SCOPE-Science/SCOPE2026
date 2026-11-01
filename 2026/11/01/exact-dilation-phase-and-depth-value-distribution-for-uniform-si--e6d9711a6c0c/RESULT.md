# Exact dilation phase and depth-value distribution for uniform simplices

## Finding

Let \(d\ge2\), let \(S\subset\mathbb R^d\) be any nondegenerate simplex, and let \(\mu\) be uniform probability on \(S\). For \(t>0\), consider the translative depth introduced for convex testing bodies,
\[
\mathsf d_t(y)=1-\sup\{\mu(tS+x):y\notin tS+x,\ x\in\mathbb R^d\}.
\]
A translation of the testing simplex, not its position relative to the coordinate origin, is optimized. Write \(\lambda_0(y),\ldots,\lambda_d(y)\) for the affine barycentric coordinates of \(y\) and \(m(y)=\min_i\lambda_i(y)\). **For every scale and every location**,
\[
\boxed{\mathsf d_t(y)=\begin{cases}
1-\min\{t,1-m(y)\}^d,&y\in S,\\
1-\min\{t,1\}^d,&y\notin S.
\end{cases}}
\]
Set \(t_c=d/(d+1)\), \(b_t=1-\min\{t,1\}^d\), and \(a_d=1-t_c^d\). The exact maximum and all maximizers have a sharp transition:
\[
\boxed{\max_y\mathsf d_t(y)=1-\min\{t,t_c\}^d.}
\]
For \(0<t\le t_c\), every point of \(\mathbb R^d\) maximizes the depth (the function is identically its baseline \(b_t\)). For \(t>t_c\), the unique maximizer is the centroid of \(S\), and the maximum is independent of \(t\).

For \(b_t<\alpha\le a_d\), whenever this interval is nonempty, its depth region is exactly the inner homothetic simplex
\[
\boxed{D_{\alpha,t}=\left\{y:\lambda_i(y)\ge\eta_\alpha\ \text{for all }i\right\},\qquad
\eta_\alpha=1-(1-\alpha)^{1/d}.}
\]
Its homothety ratio about the centroid is \(1-(d+1)\eta_\alpha\); this ratio is **independent of \(t\)**. At levels \(0<\alpha\le b_t\), the depth region is all of \(\mathbb R^d\); at \(\alpha>\max\{a_d,b_t\}\) it is empty. When \(t\le t_c\), these are the only two possibilities, since \(b_t\ge a_d\).

For a fresh uniform observation \(X\in S\), the complete nonbaseline depth-value survival law is
\[
\boxed{\Pr\{\mathsf d_t(X)\ge\alpha\}=
\left(1-(d+1)\left[1-(1-\alpha)^{1/d}\right]\right)^d,\qquad b_t<\alpha\le a_d.}
\]
For \(t_c<t<1\), its baseline atom has probability
\[
\boxed{\Pr\{\mathsf d_t(X)=b_t\}=1-((d+1)t-d)^d,}
\]
while for \(t\le t_c\) the depth is deterministic and for \(t\ge1\) there is no baseline atom. Thus the positive-mass nonbaseline core is born at the sharp threshold \(t_c\), with its mass growing as \(((d+1)t-d)^d\) until \(t=1\).

Finally, for every \(t\ge1\), dilation does not change the depth at any point. At the centroid \(c\), Grünbaum's sharp halfspace-depth bound for simplices gives
\[
\boxed{\mathsf d_t(c)-\operatorname{HD}(c;\mu)=1-2\left(\frac{d}{d+1}\right)^d>0\quad(d\ge2,\ t\ge1).}
\]
The gap tends to \(1-2/e\) as \(d\to\infty\). It supplies an exact quantitative example of persistent polyhedral tangent-cone depth distinct from halfspace depth.

## Assumptions and scope

The simplex \(S\) is full-dimensional in \(\mathbb R^d\); it need not be regular. Uniform probability is normalized Lebesgue measure. The scale \(t\) is any positive real number. Depth is the complementary maximum probability of a translate **missing** the query point, including the strict noncontainment convention; suprema rather than maxima are needed on boundary configurations. When \(y\notin S\), the point is allowed to lie anywhere in the ambient space. The upper levels \(D_{\alpha,t}\) are defined for \(\alpha>0\); the formula \(D_{\alpha,t}=\mathbb R^d\) at/below the baseline is part of the definition rather than a bounded-support convention.

## Proof

**Barycentric translate parametrization.** Identify \(S\) affinely with the probability simplex \(\{\lambda_i\ge0,\sum_{i=0}^d\lambda_i=1\}\). For each translate of \(tS\) there is a unique vector \(\delta\in\mathbb R^{d+1}\) satisfying \(\sum_i\delta_i=1-t\) such that
\[
 tS+x=\{z:\lambda_i(z)\ge\delta_i\text{ for }0\le i\le d\}.
\]
Conversely every such \(\delta\) comes from exactly one translate of \(tS\). The intersection of this translate with \(S\) has inequalities \(\lambda_i\ge\max\{0,\delta_i\}\). Put \(q(\delta)=\sum_i(\delta_i)_+\). Translating the barycentric variables by these lower bounds leaves a simplex with total barycentric mass \(1-q(\delta)\). Therefore its normalized volume is
\[
\mu(tS+x)=\bigl(1-q(\delta)\bigr)_+^d.
\]
This identity holds with no regularity or generic-position assumptions and covers empty intersections.

**Optimal missed mass inside \(S\).** Let \(y\in S\), put \(m=\min_i\lambda_i(y)\) and \(s=1-t\). A translate misses \(y\) precisely when \(\delta_i>\lambda_i(y)\) for at least one index \(i\). As \(\lambda_i(y)\ge0\), any such translate has \(q(\delta)\ge\delta_i>\lambda_i(y)\ge m\); also \(q(\delta)\ge\sum_i\delta_i=s\). Consequently \(q(\delta)\ge\max\{s,m\}\) in the infimum sense.

For the reverse bound, choose an index \(i\) realizing \(m\), choose \(j\ne i\), and set \(\delta_i=m+\varepsilon\), \(\delta_j=s-m-\varepsilon\), with all other entries zero. This translate misses \(y\) and has
\[
q(\delta)=\max\{s,m+\varepsilon\}.
\]
Let \(\varepsilon\downarrow0\). The exact supremal missed probability is
\[
\bigl(1-\max\{s,m\}\bigr)^d=\min\{t,1-m\}^d.
\]
Here \(m\le1/(d+1)\) and \(s<1\), so there is no negative-volume boundary complication.

**Exterior points.** The largest mass of any translated \(tS\) is \(\min\{t,1\}^d\), by volume comparison; the bound is attained by placing the smaller simplex inside the larger one. If \(y\notin S\), some barycentric coordinate \(\lambda_i(y)\) is negative. Choose \(\delta_i=0\), \(\delta_j=1-t\) for any \(j\ne i\), and all other \(\delta\)'s zero. Then \(\delta_i>\lambda_i(y)\), so the translate misses \(y\), while \(q(\delta)=(1-t)_+\) and its mass is exactly \(\min\{t,1\}^d\). This proves both branches of the depth formula.

**Phase, levels, and depth distribution.** Since \(m(y)\le1/(d+1)\) for all \(y\in S\), with equality only at the centroid, the maximum formula and its complete equality classification follow immediately. If \(\alpha>b_t\), any point in \(D_{\alpha,t}\) must belong to \(S\). The inequality \(1-\min\{t,1-m\}^d\ge\alpha\) then reduces to \(m\ge1-(1-\alpha)^{1/d}=\eta_\alpha\). This set is empty if \(\eta_\alpha>1/(d+1)\) and otherwise a homothetic copy of \(S\) with ratio \(1-(d+1)\eta_\alpha\). At/below the baseline every ambient point qualifies. Finally the probability under uniform \(\mu\) of any barycentric inner simplex of ratio \(r\) is exactly \(r^d\). The survival formula and baseline-atom probability follow by substituting \(r=1-(d+1)\eta\), with cutoff \(\eta=1-t\) when \(t<1\).

**Comparison to halfspace depth.** For a uniform simplex, Grünbaum's centroid inequality says every centroid-containing halfspace has mass at least \((d/(d+1))^d\). Equality is attained by the hyperplane through the centroid parallel to any facet, on the smaller, vertex-facing side. Thus \(\operatorname{HD}(c;\mu)=(d/(d+1))^d\). In contrast the derived translative depth at \(c\) for all \(t\ge1\) is \(1-(d/(d+1))^d\), giving the gap. Strict positivity follows from \((1+1/d)^d>2\) for \(d\ge2\). The limit follows from the classical exponential limit.

## Verification

Execute `python3 verify.py` from the extracted package directory. It uses exact rational arithmetic and checks the translate-overlap formula, the universal missed-translate upper bound on a large deterministic family, constructive near-attainment of the supremum, exterior-case maximizers, and cutoff identities in dimensions \(2,3,4\). It prints `PASS: 11900 exact-rational translate and threshold checks`. No numerical test is used to infer the infinite-dimensional, all-scale, or all-point assertions; those are consequences of the preceding analytic argument.

## Relationship to prior work

Molchanov and Nagy introduce translative \(K\)-depth and establish its erosion representation, baseline, and large-dilation tangent-cone limit. Their general results give no closed full-scale, all-dimensional simplex value distribution; the explicit section for uniform testing bodies treats an interval as its elementary example. The present exact all-scale law, sharp \(d/(d+1)\) phase, emergent baseline atom, and nonzero limiting halfspace gap are computed for the canonical nonsmooth simplex family.

Schütt, Werner and Yalikun introduce the corresponding \(C\)-ball floating-body construction for \(C\)-convex bodies and develop relative affine surface area. Their primary results concern general definitions and smooth curvature asymptotics, not an evaluated simplex depth/dilation law. Grünbaum's inequality supplies the already-known sharp centroid halfspace bound used solely for comparison. The barycentric covariogram computation is elementary and not presented as an independent generic theorem about covariograms.

## Limitations

The explicit simplification uses both a uniform distribution and the \(d+1\) facet inequalities of a simplex. For general polytopes, covariograms and depth regions need not be homothetic; the theorem makes no such claim. The asymptotic halfspace difference applies to the simplex and does not contradict the source's convergence theorem for smooth testing bodies. Priorities in literature on polyhedral floating bodies and translated-simplex covariograms may be incompletely indexed; an equivalent formula under older terminology remains a possible bibliographic risk. There has been no independent mathematical audit.

## References

1. I. Molchanov and S. Nagy, *Depth based on translates of a convex body: geometry, floating bodies, and empirical theory*, arXiv:2610.26108v1, first public 19 October 2026. In particular §§2.2, 5.1 and 6.1–6.3.
2. C. Schütt, E. M. Werner and D. Yalikun, *Floating bodies for ball-convex bodies*, arXiv:2504.15488v1, first public 21 April 2025, later J. London Math. Soc. 112 (2025), e70387.
3. B. Grünbaum, *Partitions of mass-distributions and of convex bodies by hyperplanes*, Pacific J. Math. 10 (1960), 1257–1261.

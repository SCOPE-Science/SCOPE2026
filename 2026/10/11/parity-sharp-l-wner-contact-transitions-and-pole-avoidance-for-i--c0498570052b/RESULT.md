# Parity-sharp Löwner contact transitions and pole avoidance for isocanted cubes

## Finding
For each integer \(d\ge2\) and real \(0<\delta<2\), let
\[
P_{d,\delta}=\{x\in\mathbb R^d:|x_i|\le1\ (1\le i\le d),\ |x_i-x_j|\le\delta\ (i\ne j)\}.
\]
This is the centered isocanted cube \(\mathcal I_d(\ell,a)\) after multiplication by \(2/\ell\), with \(\delta=2(\ell-a)/\ell\) and \(0<a<\ell\). All assertions below are in the ordinary ambient Euclidean metric. Put \(h=d^{-1/2}(1,\ldots,1)\), \(H=hh^{\mathsf T}\), and \(J=I-H\).

**Inscribed ellipsoid.** The unique maximum-volume inscribed (John) ellipsoid is
\[
E_J=\{x:x^{\mathsf T}(uH+vJ)^{-1}x\le1\},\qquad
v=\min\{1,\delta^2/2\},\quad u=d-(d-1)v.
\]
Its diagonal and transverse squared semiaxes are \(u\) and \(v\), respectively.

**Circumscribed ellipsoid and its complete contact set.** Let \(m=\lceil d/2\rceil\). For every integer \(m\le k\le d\), define
\[
A_k=d\left(1-\delta+\frac{\delta k}{d}\right)^2,
\qquad B_k=\frac{\delta^2 k(d-k)}d.
\]
The unique minimum-volume enclosing (Löwner) ellipsoid is
\[
E_L=\{x:t\|Hx\|^2+s\|Jx\|^2\le1\},
\qquad s>t>0.
\]
Here \((t,s)\) is specified *exactly* by the following finite formula, involving at most \(2d\) elementary candidates and no optimization oracle:

For each \(m\le k<d\), form a **one-layer candidate**
\[
(t,s)=\left(\frac1{dA_k},\frac{d-1}{dB_k}\right).
\]
Keep it if \(s>t\) and \(A_jt+B_js\le1\) for all \(m\le j\le d\).
For each \(m\le k<d\), put \(\Delta_k=A_kB_{k+1}-A_{k+1}B_k\). When \(\Delta_k\ne0\), form a **two-layer candidate**
\[
 t=\frac{B_{k+1}-B_k}{\Delta_k},\quad
 s=\frac{A_k-A_{k+1}}{\Delta_k},
 \quad
 \lambda=\frac{B_{k+1}/t-(d-1)A_{k+1}/s}{\Delta_k},\quad
 \mu=\frac{(d-1)A_k/s-B_k/t}{\Delta_k}.
\]
Keep it if \(s>t>0\), all \(A_jt+B_js\le1\), and \(\lambda,\mu\ge0\). Every kept candidate has the **same** pair \((t,s)\), and at least one is kept. Thus the formulas constitute a closed, finite, exactly verifiable determination of the unique ellipsoid. For rational \(\delta\), all candidate comparisons and coefficients are rational.

For each nonempty \(S\subseteq[d]\), define \(w_S\) by \((w_S)_i=1\) for \(i\in S\), and \((w_S)_i=1-\delta\) otherwise. The vertices of \(P_{d,\delta}\) are precisely \(\pm w_S\). Every contact vertex of \(E_L\) is exactly one of the \(\pm w_S\) with
\[
 |S|\in\mathcal K=\{k:m\le k\le d,\ A_kt+B_ks=1\}.
\]
The nonempty set \(\mathcal K\) is either a singleton or two consecutive integers. There are precisely \(2\sum_{k\in\mathcal K}\binom dk\) contact vertices.

**First sharp contact transition.** Put \(m=\lceil d/2\rceil\) and
\[
\sigma_d=\sqrt{d-\frac{(d-1)(m+1)(d-m-1)}{m(d-m)}},\qquad
\tau_d=\frac{d(\sigma_d-1)}{1+(d-m)(\sigma_d-1)}.
\]
Then \(0<\tau_d<2\). Precisely for \(0<\delta<\tau_d\), the only contact layer is \(\mathcal K=\{m\}\); at \(\delta=\tau_d\), it is \(\{m,m+1\}\); and above \(\tau_d\), \(\mathcal K\ne\{m\}\). The thresholds have different parity limits:
\[
\lim_{h\to\infty}\tau_{2h}=1,\qquad
\lim_{h\to\infty}\tau_{2h+1}=\frac43.
\]

**Avoidance of the two longest-radius vertices.** The two diagonal vertices \(\pm\mathbf1\) lie strictly inside \(E_L\) for **every** \(d\ge4\) and \(0<\delta<2\). For \(d=2,3\), they lie on \(\partial E_L\) exactly when \(\delta\ge d-\sqrt d\). By contrast, \(\pm\mathbf1\) are exactly the two vertices on the minimum enclosing *Euclidean sphere* for all \(0<\delta<2\). This is a qualitative difference between minimal-radius spheres and minimal-volume ellipsoids.

## Assumptions and scope
The parameter domain \(d\ge2\), \(0<\delta<2\) is strict. In particular the degeneracy at \(\delta=0\) and the limiting cube at \(\delta=2\) are not included; at the latter point all cube vertices become cotangent. All ellipsoids are considered among arbitrary translated, arbitrarily oriented, full-dimensional ellipsoids, not merely ellipsoids restricted in advance by symmetry. Normalizing a general isocanted cube by the common scalar \(2/\ell\) is an honest Euclidean similarity; multiply each resulting semiaxis by \(\ell/2\) to undo it.

## Proof
**1. All vertices.** If no coordinate constraint is active at a point of \(P_{d,\delta}\), translation by a small multiple of \(\mathbf1\) in both directions preserves every inequality, so the point is not extreme. At any extreme point having some coordinate \(x_i=1\), all other coordinates lie in \([1-\delta,1]\). Every coordinate strictly between the two endpoints can be perturbed while fixing those at the endpoints; more formally, partition the coordinates into equality components of the active difference constraints: because \(\delta>0\) and all coordinates lie in one interval of width \(\delta\), only endpoint classes can be linked by active differences. Any interior coordinate class is free, contradicting extremality. Hence every coordinate is either \(1\) or \(1-\delta\); a nonempty class equals \(1\). Each \(w_S\) is extreme: fix one coordinate at \(1\), fix other coordinates in \(S\) by their active upper bounds, and each outside coordinate by its active difference equality to that fixed coordinate. These are \(d\) independent equations. Reflecting at the origin covers points with coordinate \(-1\), and completes the vertex list.

**2. Symmetry and reduction to two positive scalars.** John and Löwner ellipsoids of a full-dimensional body exist and are unique. Since \(P_{d,\delta}\) is invariant under the full coordinate-permutation group and central reflection, each such ellipsoid is centered at the origin and its quadratic matrix commutes with all permutations. Such symmetric matrices are exactly \(\alpha H+\beta J\). Both scalar eigenvalues must be positive. For an inscribed ellipse with shape \(uH+vJ\), the coordinate facets impose \((u+(d-1)v)/d\le1\) and difference facets impose \(2v\le\delta^2\). The volume is proportional to \(\sqrt{uv^{d-1}}\). For fixed \(v\), maximize \(u\) at \(u=d-(d-1)v\); its product with \(v^{d-1}\) increases up to \(v=1\) and decreases thereafter. Consequently \(v=\min(1,\delta^2/2)\), proving the John formula.

**3. The linear orbit inequalities.** The squared projection lengths of the vertex \(w_S\), \(|S|=k\), are exactly \(A_k\) and \(B_k\) as defined above. Thus an origin-centered containing ellipse with inverse shape matrix \(tH+sJ\) exists exactly when \(t,s>0\) and \(A_kt+B_ks\le1\) for every \(1\le k\le d\); its volume is proportional to \(t^{-1/2}s^{-(d-1)/2}\). For \(k<d/2\),
\[
A_{d-k}-A_k=\delta(d-2k)(2-\delta)>0,\qquad B_{d-k}=B_k.
\]
Therefore the lower layers \(1\le k<m\) are strictly redundant. Maximizing the strictly concave \(\log t+(d-1)\log s\) subject to the remaining linear inequalities gives the unique optimal \((t,s)\).

**4. Strict spectral anisotropy and consecutive contacts.** The pole inequality gives \(t\le1/d\). Any feasible \(t,s\) with \(s\le t\) has \(ts^{d-1}\le d^{-d}\). But \((1/d,1/d+\varepsilon)\) is feasible for some \(\varepsilon>0\), because every vertex except the two poles has Euclidean norm strictly less than \(\sqrt d\) when \(0<\delta<2\). This point has larger determinant. Hence the optimum has \(s>t\). For such \(t,s\), the expression
\[
A_kt+B_ks=d(1-\delta)^2t +2\delta(1-\delta)kt+\frac{\delta^2}{d}\bigl(k^2t+k(d-k)s\bigr)
\]
is a *strictly concave quadratic function of the real variable* \(k\), with leading coefficient \(\delta^2(t-s)/d<0\). Its maximum over integers \(m\le k\le d\) is attained at one integer or two neighboring integers, proving the contact assertion. By differentiability and strict concavity of the determinant objective, its stationary optimality conditions are sufficient and necessary: one active constraint leads exactly to the one-layer formulas; two active constraints lead by Cramer's rule to the two-layer formulas. The displayed \(\lambda,\mu\) are precisely the nonnegative stationary multipliers. The active set cannot be exclusively \(k=d\), since the objective could increase \(s\) without affecting that constraint. Thus the candidate list is exhaustive and has a unique solution.

**5. The initial phase boundary.** At a single active layer \(k=m\), the gradient equations force \(t=1/(dA_m)\) and \(s=(d-1)/(dB_m)\). Strict concavity in \(k\) makes all other inequalities equivalent to the next-layer test \(A_{m+1}t+B_{m+1}s\le1\). Rearranging yields
\[
\frac{A_{m+1}}{A_m}\le d-(d-1)\frac{B_{m+1}}{B_m}=\sigma_d^2.
\]
Both square roots of \(A_{m+1}\) and \(A_m\) are positive because \(m\ge d/2\) and \(\delta<2\). Solving the boundary equation gives exactly \(\delta=\tau_d\). The corresponding one-layer \(s>t\) condition holds through the boundary; it follows, for example, by writing \(q=2m+1-d\in\{1,2\}\), using \(\sigma_d^2-1=(d-1)q/[m(d-m)]\), and bounding \((\sigma_d-1)^2<(d-1)/[m(d-m)]\). Consequently the first contact transition has the stated exact open, boundary, and beyond cases. Elementary leading-term expansion of the displayed algebraic formula gives the two parity limits.

**6. Pole-avoidance criterion.** The diagonal pole has squared projection length \(A_d=d\) and \(B_d=0\), hence lies on the ellipsoid exactly when \(t=1/d\). If this constraint is active, the best feasible \(s\) must be
\[
s_* =\frac1d+\frac{2-\delta}{\delta(d-1)},
\]
because substitution in each nonpole inequality gives \(s\le 1/d+(2-\delta)/(\delta k)\), whose most restrictive index is \(k=d-1\). Thus only the two inequalities at \(d-1,d\) are active. The stationary multiplier of the pole inequality is nonnegative if and only if \(A_{d-1}\le1\), and is in fact \(d(1-A_{d-1})/(d-A_{d-1})\). Since \(A_{d-1}=d(1-\delta/d)^2\), this is equivalent to \(\delta\ge d-\sqrt d\). For \(d\ge4\), the threshold is at least \(2\), outside the permitted interval. For \(d=2,3\), it is inside. Uniqueness of the concave program gives the claimed strict-contact dichotomy. Finally, \(\|w_S\|^2<d\) for every proper \(S\) and \(0<\delta<2\), while \(\|w_{[d]}\|^2=d\). The origin-centered sphere of radius \(\sqrt d\) encloses the polytope; central symmetry forces every minimum enclosing sphere's center to be zero, proving the last comparison.

## Verification
The included pure-standard-library verifier `verify_isocanted_ellipsoids.py` uses exact rational arithmetic. Run `python3 verify_isocanted_ellipsoids.py`. It checks 348 pairs of dimensions \(2\le d\le30\) and twelve rational parameter values in \((0,2)\), including all candidate KKT conditions, inequality feasibility, layer adjacency, John facet constraints and strict pole exclusion for \(d\ge4\). It also checks all explicit vertices for \(2\le d\le7\) and tests rational brackets on either side of every dimension's sharp transition. Expected final line:

`VERIFY_OK exact_rational_cases=348 single_candidates=206 pair_candidates=142 explicit_vertices_checked=5904 pole_checks=324 john_facets=yes threshold_brackets=yes`

These finite checks support but do not replace the all-dimensional proof above.

## Relationship to prior work
De la Puente and Clavería's 2020 foundational construction computes the face lattice and exact vertex count of isocanted alcoved polytopes (arXiv:2009.13858v1, §3). Their 2024 paper (arXiv:2406.01565v1, §§1,3,6,7) determines volumes of the bodies and their polars, as well as the corresponding Mahler product. Neither provides the two extremal Euclidean ellipsoids, the sharp Hamming-layer contact transitions, nor pole avoidance. The standard general John–Löwner existence/uniqueness principle is an ingredient in the proof, but it does not imply this explicit orbit optimization without the sharp contact analysis. In particular, minimum Euclidean enclosing spheres and scalar inradii do not determine minimum-volume ellipsoids or their contact layers. Our formulas concern these distinct invariants. See also Henk's survey for the general theorem.

## Limitations
The results hold for the entire stated open parameter interval, not for the degenerate endpoints. The finite selection formula is an exact determination of the Löwner shape but is not asserted to be a single elementary closed radical valid in all dimensions; higher contact transitions are encoded by the stated candidate inequalities. Only contact *vertices* of the outer ellipsoid are enumerated; no independent classification of all facet contacts for the inner ellipsoid is claimed. A later 2025 study of isocanted incidence data was available as an abstract but was not read in full; potential unnoticed coverage remains a literature risk. Independent external verification has not been performed.

## References
1. M. J. de la Puente and P. L. Clavería, *Isocanted alcoved polytopes*, arXiv:2009.13858v1 (first public version September 29, 2020), §3. https://arxiv.org/html/2009.13858v1
2. M. J. de la Puente and P. L. Clavería, *The volume of an isocanted cube is a determinant*, arXiv:2406.01565v1 (first public version June 3, 2024), §§1, 3, 6–7. https://arxiv.org/html/2406.01565v1
3. M. Henk, *Löwner–John Ellipsoids*, in *Optimization Stories*, Documenta Mathematica Extra Volume ISMP (2012), pp. 95–106; DOI 10.4171/DMS/6/15.
4. M. J. de la Puente and P. L. Clavería, *Isocanted cube: the lower Lebesgue volumes, incidence numbers and symmetries of this d-dimensional tile*, Extracta Mathematicae 40 (2025); abstract: https://revista-em.unex.es/index.php/EM/article/view/2605-5686.40.1.1

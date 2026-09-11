# Three distinct W2 geodesics delta_o -> delta_c on the unit-tetrahedron surface

## Context

On Alexandrov spaces with curvature bounded below, optimal-map uniqueness
(Bertrand 2008; Rajala-Schultz 2018/2021) requires a diffuse source:
absolutely continuous w.r.t. Hausdorff measure, resp. purely
(n-1)-unrectifiable. Dirac masses sit on 0-dimensional (hence rectifiable)
support, outside every such hypothesis, and whether any diffuseness can be
dropped is explicitly open. A Dirac pair reduces W2-geodesic branching to
cut-locus multiplicity of the base. The vertex-to-opposite-centroid pair on
the regular tetrahedron is fixed by an order-3 isometry, forcing a symmetric
triple-or-rigid alternative: a precise auditable probe of where uniqueness
survives on a genuinely singular (conical-vertex, CBB(0) polyhedral) base.

## Definitions

- X: intrinsic-length surface of the regular tetrahedron of edge-length 1,
  compact 2D polyhedral Alexandrov space of curvature >= 0.
- o = V0 (apex vertex); F = conv(V1,V2,V3) opposite closed face (equilateral,
  side 1); c = centroid of F.
- mu0 = delta_o, mu1 = delta_c in P2(X).
- L0 = 2*sqrt(3)/3 = 1.154700538379..., L0^2 = 4/3.
- Coordinates: F in z=0 with V1=(0,0,0), V2=(1,0,0), V3=(1/2,sqrt3/2,0);
  c=(1/2,sqrt3/6,0); o=(1/2,sqrt3/6,H), H=sqrt(2/3).
  Face altitude a=sqrt3/2, inradius r=sqrt3/6, circumradius 1/sqrt3.

## Result

There are three distinct minimizing geodesics gamma_k : o -> c (k=1,2,3),
each of length L0 = 2*sqrt(3)/3, cyclically permuted by the order-3 rotation
about the axis o--c, with pairwise distinct midpoints m_k = gamma_k(1/2)
satisfying d_X(m_k,m_l) in [1/3, sqrt(3)/3] (hence >= 1/3 > 0) for k != l.
Their displacement interpolations mu^(k)_t = delta_{gamma_k(t)} are three
distinct constant-speed W2 geodesics from mu0 to mu1. Hence the W2 geodesic
between these Dirac masses is not unique, while the optimal plan
delta_o x delta_c is trivially unique. Exact scale: d_X(o,c) = 2*sqrt(3)/3,
squared 4/3.

## Proof / evidence

Lemma A (chordal bound; in-face equality). For x,y in X,
d_X(x,y) >= |x-y| (extrinsic chord), since a surface path is an R^3 curve.
If x,y lie in a common closed face, equality holds via the in-face straight
segment.

Lemma B (first-entry split). Let gamma:[0,1]->X be continuous o->c.
With t* = inf{t : gamma(t) in interior(F)} and r = gamma(t*) in dF,
length(gamma) >= d_X(o,r)+d_X(r,c) >= |o-r|+|r-c|.

Lemma C (edge profile). For r in dF, |o-r|+|r-c| >= L0 with equality only
at the three edge midpoints of F: o projects orthogonally to c at height H,
so |o-r|^2 = H^2+|r-c|^2 = 2/3+t^2; on one edge r=(midpoint)+u*tau,
|r-c|^2=1/12+u^2, |o-r|^2=3/4+u^2, h(u)=sqrt(3/4+u^2)+sqrt(1/12+u^2) even
strictly increasing in |u|, minimum h(0)=sqrt3/2+sqrt3/6=L0.

Hence d_X(o,c) >= L0. Three strips achieve L0: for each edge e_k of F with
side face S_k, unfold S_k union F flat across e_k (shared edge on x-axis);
apex image O=(0,sqrt3/2), centroid image c_F=(0,-sqrt3/6); segment O->c_F is
vertical of length L0 crossing e_k transversely at its midpoint at arc
fraction 3/4 from o. Folding back gives gamma_k straight in each face and
meeting the edge orthogonally (equal angles pi/2; Snell), hence a genuine
geodesic; length equals the global lower bound so minimizing; thus
d_X(o,c)=L0 exactly. Distinct via three distinct edge-midpoint crossings.

Midpoints: L0/2 < (3/4)L0 so m_k lies on the first leg at fraction
(L0/2)/(sqrt3/2)=2/3 of the altitude from o: the centroid of side face S_k,
q1=(0.5,0.096225,0.272166), q2=(0.666667,0.384900,0.272166),
q3=(0.333333,0.384900,0.272166). Pairwise extrinsic chords exactly 1/3
(e.g. q1-q2=(V1-V3)/3), so d_X(m_k,m_l) >= 1/3 by Lemma A. Rhombus unfolding
of two adjacent side faces gives d_X(m_k,m_l) <= sqrt3/3 (centroids at
(1/2,+/-sqrt3/6), segment crossing shared edge interiorly).

Symmetry: rotation R through 2pi/3 about o--c permutes V1->V2->V3,
preserves edges, fixes o,c, restricts to an isometry of X permuting the
three strips: R circ gamma_k = gamma_{k+1}.

Wasserstein lift: only coupling of delta_o,delta_c is delta_o x delta_c
(unique optimal plan) with cost L0^2=4/3. mu^(k)_t=delta_{gamma_k(t)}
(constant-speed gamma_k) satisfies
W2(mu^(k)_s,mu^(k)_t)=d_X(gamma_k(s),gamma_k(t))=L0|t-s|: constant-speed W2
geodesics (dynamical plans Pi_k=delta_{gamma_k}); at t=1/2,
mu^(k)_{1/2}=delta_{m_k} pairwise distinct with separation >=1/3.

## Limitations

Classification of ALL o->c minimizers (uniqueness of the triple up to
symmetry) is not proved; only three distinct minimizers plus the exact
distance. Midpoint separation is the interval [1/3, sqrt3/3], not exact
values. No statement about other Dirac pairs or diffuse sources.

## Reproducibility

`python3 output/artifacts/verify_target.py` (stdlib only): model identities
(M1), strip length L0^2=4/3 and breakpoint 3/4 (S1), lower-bound profile
monotonicity with g(0)=L0 (G1), midpoint-centroid identities and chord 1/9
(M2), rhombus bound sqrt3/3 (M3), symmetry data (SYM), W2 identities (W2).
All 25 checks pass.

## References

- Bertrand, Existence and uniqueness of optimal maps on Alexandrov spaces,
  Adv. Math. 2008. https://doi.org/10.1016/j.aim.2008.06.008
- Rajala-Schultz, Optimal transport maps on Alexandrov spaces revisited,
  arXiv:1803.10023.
- Davis-Dods-Traub-Yang, Geodesic trajectories on regular polyhedra,
  arXiv:1508.03546 (Thm 3.6/Cor 3.7 parametric point-to-vertex description;
  no minimizing census, distance, midpoints, or W2 lift).
- Davis, Geodesic complexity of a tetrahedron, arXiv:2306.11059 (expanded cut
  locus; vertex-centroid pair parked in discrete E4 with arbitrary selector).
- Itoh-O'Rourke-Vilcu, Source unfoldings of convex polyhedra via certain
  closed curves, arXiv:1205.0963 (general star-unfolding method).

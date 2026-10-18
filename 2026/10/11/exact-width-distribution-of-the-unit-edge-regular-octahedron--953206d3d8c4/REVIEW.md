# Independent mathematical audit

## correctness

PASS

Octahedron O=conv{+-e_i/sqrt2, i=1,2,3} has edges sqrt[(1/2)+(1/2)]=1. Its support function h(u)=max_i|u_i|/sqrt2, so directional width W=sqrt2 M, M=max_i|U_i| for uniform spherical U. From sum Ui²=1, M in [1/sqrt3,1]. Event M<=m is complement of six signed coordinate spherical caps {+-Ui>m}, each area 2pi(1-m). For m>=1/sqrt2, caps are disjoint, so F_M(m)=1-6*2pi(1-m)/(4pi)=3m-2. For m in [1/sqrt3,1/sqrt2], triple-cap positive area is impossible (sum of three squared components would exceed 1); 12 pair intersections of distinct axes remain, giving F_M=3m-2+(3/pi)A2(m). Two cap centers are separated by pi/2, cap radius arccos m. Spherical cosine rule gives alpha=acos[m/sqrt(1-m²)], beta=acos[m²/(1-m²)] where beta=pi-gamma of the isosceles spherical triangle. Sector-minus-triangle lens area A2=2beta-4m alpha, yielding exact lower CDF under m=w/sqrt2. Endpoints F(sqrt(2/3))=0, F(1)=3/sqrt2-2, F(sqrt2)=1 match continuously, with support endpoints determined by vertex/equal-coordinate directions. Independently integrated the spherical-longitude event and lens at interior m=0.6,0.65,0.8,0.95; agreement ~1e-10 is CONSISTENCY only, since rigorous proof uses cap inclusion-exclusion and spherical geometry. No chord distribution inference.

## originality

PASS

The exact complete elementary CDF for the 3D regular-octahedron directional width is narrower than the general crosspolytope Gaussian maximum/moment representation but more explicit than an implicit law or moments. An arbitrary finite collection of moments would not give this formula; the full moment sequence implicitly determines compact-support distribution but does not state spherical-lens piecewise elementary evaluation. Finch's actual 2011/2016 full source computes cube/tetrahedron widths; a 2026 Abas general polytope density theory covers the TYPE of object and may imply law in principle, but abstract advertises different evaluated examples; its full text was inaccessible. Significant risk of unindexed stereology/calliper/Feret diameter exact table remains.

## value

PASS

Random-direction width is a standard support-function invariant, and the regular octahedron is a canonical Platonic solid. Its complete elementary finite-dimensional CDF is a natural unknown exact invariant with a real geometrically explained transition at w=1 from disjoint caps to overlapping lenses; it can be needed for calibration, exact moments and stereology. The result supplies a complete classification of the distribution—not merely a numerically sampled histogram—and is not a recomputation of the distinct chord table. It remains valuable as a self-contained specific-shape evaluation even when general integral/coarea theorems exist.

The dated certificate retains the supplied scientific assessment, sources and limitations.

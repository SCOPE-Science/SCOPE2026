# Independent mathematical audit

## correctness

PASS

For E=A S^{d-1}, A positive diagonal with smallest axis b and largest a, use Rad(A^{-1}S)<=t/b. A sphere subset enclosed by radius r<1 lies in a spherical cap, so any hull point has norm>=sqrt(1-r^2). This gives h_E(t)<=a(1-sqrt(1-t^2/b^2)) on [0,b]. The two boundary points a sqrt(1-t^2/b^2)e +- t f have Rad=t and midpoint on major axis. Direct constrained minimization of |xe-Av| over sphere, using b in the orthogonal part, shows nearest boundary distance a-x for x>=a-b^2/a, otherwise b sqrt(1-x^2/(a^2-b^2)). Equality thus persists exactly to t_star=(b^2/a)sqrt(2-b^2/a^2); compactness and equality rigidity give strict inequality to affine bound for nonround t>t_star. An antipodal minor-axis pair attains defect b at t=b, and the distance throughout the filled ellipsoid is <=b. Sphere a=b correctly joins regimes at t=b. Independent axis-witness tests on 20 cases corroborate threshold and strictness; proof controls all d and all (possibly infinite) subsets via compact Caratheodory.

## originality

PASS

QUALIFIED PASS: The Attali-Lieutier-Salinas convexity defect and Berenfeld-Harvey-Hoffmann-Shankar reach expansion are prior results. The full accessible Berenfeld source proves general h(t)=t^2/(2R_l)+O(t^4) and local reach circle bounds, but not the ellipsoid-specific exact initial interval t<=t_star, its maximal endpoint, the actual fourth-order coefficient a/(8b^4), or the t>=b plateau. A general circular reach bound is different in coefficient and scale. No closer prior exact ellipsoid profile was located.

## value

PASS

The ellipsoid boundary is the canonical anisotropic test manifold for scale-dependent convexity defect; an exact initial profile and sharp transition quantify the difference between local focal curvature and global scale-hull geometry. Intermediate axes cancel, giving dimension-free sharp data needed when calibrating reach/defect estimators. The unknown intermediate interval (t_star,b) is acknowledged rather than falsely claimed complete.

The dated certificate retains the supplied scientific assessment, sources and limitations.

# Independent mathematical audit

## correctness

PASS

R is intersection of radius-one disks centered at generating equilateral triangle vertices A=(0,1/sqrt3), B=(-1/2,-1/(2sqrt3)), C=(1/2,-1/(2sqrt3)), width 1 and area A0=(pi-sqrt3)/2. The maximizer of uniform area halfspace depth for a planar convex body is uniquely defined by the classical center-of-area/halfspace-depth theorem; every dihedral symmetry must preserve it, forcing the origin. For center-line angle theta, left halfplane area F(theta)=(1/2) integral_theta^(theta+pi) rho(phi)^2 dphi. Threefold symmetry gives F'(theta)=(rho(theta+pi/3)^2-rho(theta)^2)/2. Dihedral symmetries reduce unoriented center cuts to theta in [0,pi/6]. In that interval both rays at theta and theta+pi/3 hit the disk centered B; the positive ray root is g(c)=c+sqrt(2/3+c²), c(phi)=cos(phi-7pi/6)/sqrt3, strictly increasing in c. Exact trigonometry yields c(theta+pi/3)-c(theta)=sin(theta)/sqrt3>=0, strictly for positive theta. Thus F increases on the fundamental interval and all minimizing center-line orientations are precisely the three side-parallel directions (with smaller halfplane chosen). The smaller area s0 is twice the explicit circular-segment integral over x in [0,sqrt33/6-1/2], leading exactly to acos(1/(2sqrt3))-pi/6-(sqrt11+sqrt3)/12. Dividing by A0 gives depth 0.473390433801114..., and (A0-s0)/s0 gives Winternitz imbalance 1.112421224844882.... Independent integration of radial cuts and circular segment reproduced s0=0.3336318129743325 and strict angular trend; finite checks are only consistency, analytic derivative proves all angles. No claim about diameter-restricted Groemer-Wallen cuts or higher Reuleaux polygons.

## originality

PASS

This is the uniform area Tukey/halfspace-depth (Winternitz) invariant on a canonical nonpolygonal constant-width body, with exact elementary center cut, not the much larger diameter-constrained Groemer-Wallen ratio. Rousseeuw-Ruts 1999 developed population-depth formulae for uniform regular polygons, but a curved Reuleaux intersection of disks is not one of those polygon cases; general depth theory fixes the center but not exact depth value. Exact numeric/symbolic searches and aliases remain incomplete due semantic search outage and historically extensive geometry sources; best-of-knowledge PASS subject to real residuals.

## value

PASS

The Reuleaux triangle is the archetypal nonpolygonal constant-width shape; its exact maximal halfspace depth / Winternitz imbalance is a natural classical convexity invariant, not an arbitrary slice. The result pins down the unique center, all worst center-cut directions, and a nontrivial closed segment-area expression, thereby separating arbitrary-depth center-line asymmetry from diameter-restricted constant-width asymmetry. Even without a general constant-width extremality theorem, a precise previously unverified invariant of this canonical body is plausibly reusable in quantitative convexity and robust depth comparisons. General uniqueness of the center alone does not render the exact 0.47339 calculation a textbook rebranding.

The dated certificate retains the supplied scientific assessment, sources and limitations.

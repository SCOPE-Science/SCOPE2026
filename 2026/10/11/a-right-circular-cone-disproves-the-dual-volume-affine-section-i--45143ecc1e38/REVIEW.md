# Independent mathematical audit

## correctness

PASS

The cone has 0<=z<=1 and r<=z; p=(0,0,33/50), q=(0,0,23/35) are interior with q<p. Any plane through both contains the axis, hence each axial section is a congruent triangle. The radial ray hits the top for theta<=atan(1/(1-c)) and lateral boundary afterwards; the resulting two integrals J(c), K(c) have differentiable matching transition. Independent high-precision evaluation of exact derivatives gives J'(23/35)=-0.13409911686953<0 and K'(33/50)=+0.05086738320383>0; verified the original rational enclosure code uses series tail and interval endpoints. Herburt--Moszynska--Peradzynski (2005), Theorem 2.1, proves strict concavity of the radial integral for phi(t)=t in dimensions 2 and 3. Tangent-line inequalities then imply J(p)<J(q) for every required plane but K(p)>K(q) globally. The result is restricted to d=3 and the first radial moment, and proves neither all-powers nor all-body statements.

## originality

PASS

Best-of-knowledge PASS. The published Banach Center 2009 Problem 7 poses exactly the hyperplane-to-whole-body implication. The 2005 strict-concavity theorem supplies a central proof tool but does not, by itself, produce opposite-order points or a conical counterexample. Explicit rational witness heights and their competing derivative signs establish the missing negative answer. A related positive one-section criterion for Euclidean balls concerns different bodies and does not dominate this cone. The contemporaneous indexed copy of this very result is not independent prior art.

## value

PASS

PASS. A concrete counterexample resolves a named geometric implication about dual volume and affine sections, separating sectional from global radial-center order in a natural rotationally symmetric convex body. The exact two-height witness and transferable strict-concavity mechanism provide a mathematically motivated boundary, beyond an arbitrary numeric slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.

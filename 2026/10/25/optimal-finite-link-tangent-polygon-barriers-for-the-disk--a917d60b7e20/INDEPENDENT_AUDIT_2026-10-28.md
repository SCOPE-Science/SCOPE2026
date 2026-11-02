# Independent mathematical audit

## correctness

PASS

At every convex tangent polygon vertex, the two outgoing tangency segments have lengths tan x_i, with half exterior angle x_i∈(0,π/2) and ∑x_i=π. Total k retained side lengths are weighted convex objective F=tan x1+tan x_{k+1}+2∑_{i=2}^{k}tan x_i. Strict convexity of tan on positive half interval plus Lagrange multipliers give endpoints a, others b, sec²a=2sec²b, and unique interior root, hence unique global optimum (including boundary infima). Adjacent normal gaps 2x_i give a valid strictly convex circumscribed polygon. Splitting any interior angle b halves its contribution with 4tan(b/2)<2tan b, proving strict improvement in k. At q=k−1, Taylor solve b=π/(2q)+O(q^-3), a=π/4+b²/2+O(b4), giving L_k=π+2+π³/(12q²)+O(q^-4). Projection of connected chain is an interval equal to its convex-hull projection, and its convex hull is the circumscribed polygon containing the disk, hence it hits every disk-intersecting line. Independent constrained SLSQP minimization k=2..11 recovers the angle pattern, exact k2/k3 and asymptotic trend.

## originality

PASS

The classical connected-disk opaque barrier benchmark π+2 and theories of curves whose convex hull covers a disk are prior, and a minimum Hamiltonian path of the vertices of a *fixed* convex polygon does not solve simultaneous optimization of variable tangent side angles at prescribed k. Full Dumitrescu–Jiang–Pach Opaque sets and accessible Nikonorov descriptions lack this specific equal-two-endpoint and shared-interior-angle optimization. Faber–Mycielski–Pedersen (1984), the strongest historical connected-disk-barrier paper, was inaccessible in full even after authorized attempt; no whole-document noncoverage is asserted. Best-of-knowledge PASS with this specific residual risk.

## value

PASS

Finite k connected polygonal barriers provide a natural geometric approximation hierarchy to the classical π+2 connected-disk barrier. Exact classification of all strict convex tangent polygon optimizers at each k, plus the sharp inverse-square excess constant, makes a motivated restricted geometric extremal result. Restriction to tangential polygons with one side omitted is essential, and no unproved unrestricted barrier claim is smuggled in.

The dated certificate retains the supplied scientific assessment, sources and limitations.

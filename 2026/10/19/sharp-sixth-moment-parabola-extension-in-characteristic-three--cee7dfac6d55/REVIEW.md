# Independent mathematical audit

## correctness

PASS

Character orthogonality gives q^(-4) times the squared triple-fiber norm with the stated counting measure, so the unnormalized coefficient is q+1−1/q. For each nonzero sum s there are q translation orbits of ordered triples and translating by h changes the square sum by −hs; each orbit contributes exactly once to every square sum. Thus the generic fibers have size q. At s=0, the unique ordered parametrization (a−d,a,a+d) gives square sum −d². The d=0 fiber has size q and the nonempty nonzero-square-sum fibers have size 2q; C_d=C_{−d} gives |C_0|²+2Σ_{d≠0}|C_d|². After spending one q-term Cauchy–Schwarz estimate per d against the exceptional contribution excluded from the generic estimate, the remainder is Σ_{d≠0}|C_d|². Cauchy–Schwarz against the central factor and the bijection (a,d)↦(a−d,a+d) bound this by F(F²−Σ|f|⁴). The last Cauchy–Schwarz bound is sharp only for constant modulus when F>0. Independently counting the flat moment gives q⁴+q³−q², yielding 99, 7209 and 550395 at q=3,9,27, respectively. Quadratic phases translate (X,Y), preserving the norm. There is no claim of a full equality-phase classification. The reviewed verify.py (arithmetic and fiber enumeration, lines 12–56; test chain, lines 58–104) and verify_output.txt corroborate the finite cases; the complex sample tests use tolerances, and neither they nor the recorded run are used as proof. Replay: python verify.py from the package; not executed as part of this review.

## originality

PASS

The supported distinct contribution is the unrestricted characteristic-three theorem for extension fields q≥9. The q=3 case itself is covered by an earlier three-mode result, and the identical coefficient and necessary modulus condition are known in characteristic >3. The frozen text explicitly distinguishes both overlaps; no inspected result establishes the unrestricted theorem on the remaining fields.

## value

PASS

The result fills the explicit exceptional-characteristic gap in a sharp parabola restriction problem, on arbitrarily large fields and for every complex input. It explains how to recover the sharp coefficient despite the factor-two critical fibers and gives necessary optimizer structure. This is materially stronger than tabulating the flat energy or testing local stability.

The dated certificate retains the supplied scientific assessment, sources and limitations.

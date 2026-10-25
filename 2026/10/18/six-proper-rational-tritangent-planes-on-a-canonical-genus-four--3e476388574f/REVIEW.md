# Independent mathematical audit

## correctness

PASS

Fix F2 and the singular quadric Q:XZ+Y²=0. A canonical smooth genus-4 section is Q intersect a homogeneous cubic in X,Y,Z,W, considered modulo multiples of Q. With nonzero W³ coefficient normalize to one, giving exactly 2^15=32768 coefficient masks; all smooth sections avoid the cone vertex. Smoothness can be checked geometrically on two affine charts by eliminating partial derivatives of w³+a(t)w²+b(t)w+c(t) and requiring gcd(D=ab+c,E=(a'b+c')²+b(b')²)=1; this detects geometric singular points, not merely F2-rational ones. Proper rational planes are all 15 F2-planes except the four vertex planes whose Q-sections split into geometric ruling lines; the remaining eleven comprise three rational tangent-to-Q planes and eight transverse planes. Ruling-tangent restriction gives a cubic; contact divisor 2D with reduced D iff cubic squarefree, discriminant AD+BC=1. A transverse plane restricts to degree-six binary form; it must be the square of a squarefree cubic, tested by vanishing odd coefficients and AD+BC=1. My independent bit-polynomial implementation scanned all 32768 masks and reproduced precisely 12288 smooth, counts (0:448,1:2392,2:4536,3:3512,4:1016,5:240,6:144). Independently rebuilt the 48 linear automorphisms of Q (6 PGL2(F2) transformations x8 W-translations) and substituted polynomials in the 16-dimensional cubic quotient; the action yields 752 total and 274 smooth orbits and precisely three size-48 orbits attaining six proper rational planes. This proves the stated maximum within this exact binary quadric-cone family, not a claim about all genus-four curves or the full algebraic-closure theta-characteristic count.

## originality

PASS

A rational finite-field sextic-on-singular-quadric plane-counting problem, distinct from the 120 odd-theta tritangents convention on a smooth quadric. Kulkarni–Ren–Sayyary Namin–Sturmfels arXiv:1712.06274 explicitly explain that singular quadrics possess infinitely many geometric tangent planes and adopt a different convention for the finite 120 odd-theta set; this claim instead explicitly defines proper rational F2 planes and counts them, so conflating definitions would be incorrect. Xarles arXiv:2007.07822 gives genus-four F2 curve census, not this rational plane spectrum. No exact six/274/three-extremal-orbit table appeared in these inspected primary texts. The original source-defined plane convention must remain explicit for meaningful originality.

## value

PASS

The exact tritangent contact spectrum, sharp six-plane bound, and complete optimizer-orbit classification are natural projective invariants of canonical genus-four curves over the smallest field. The calculation resolves every smooth model on a fixed canonical quadric-cone stratum, with a mathematical gcd smoothness certificate, rather than reporting an arbitrary handful of examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.

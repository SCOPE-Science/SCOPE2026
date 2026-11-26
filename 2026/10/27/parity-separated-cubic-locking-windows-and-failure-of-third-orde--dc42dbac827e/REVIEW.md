# Independent mathematical audit

## correctness

PASS

The coordinate H(x)=integral_0^x 1/v takes each step to h+O(h²) uniformly, and H(x)−Lx is bounded, giving L rho(h)=h+O(h²). For the crossing calculation set z=1/q, h=Lz+gamma z³ and k=q/2+d. The order-z coefficient of (1+h)^k/(3/2) is dL−L²/4, and that of (1−h)^k/(2/3) is −dL−L²/4. Strict signs at consecutive steps give first crossings with d=1/2 or 1 from 0 (odd or even), and d=1/2 or 0 from 1/2. For the formal remaining branch segments the computed qth endpoints are 1+O(z²) and 3/2+O(z²); the penultimate points are below those breakpoints by h+O(z²) and (3/2)h+O(z²), respectively. Monotonicity within each branch therefore justifies using those affine segments up to the final evaluation. The uniform order-z² coefficients for the two endpoint displacements, after division by 1 or 3/2 respectively, are gamma+L³/3−dL²+(dL−L²/4)² and gamma+L³/3+dL²−(dL+L²/4)². Substituting the appropriate d gives exactly gamma−a_p and gamma−b_p. With a fixed positive epsilon the strict signs of the leading terms persist throughout each stated gamma interval; continuity produces a lifted q-cycle with displacement 1. Comparing the two interval endpoints in a putative third-order expansion leaves the nonzero term L^-1(W_p−2 epsilon)q^-3, since the squared and cubed differences have smaller orders. Replay: affine identities and expansions in frozen RESULT.md lines 26–53; separate direct-velocity midpoint checks for q=41,42 are described in /workspace/branches/78972f2f-f3c4-445e-a9c4-dee3e1869e4c/record-2-check.txt. They are diagnostics, not the proof. The provided checker and recorded output were inspected; the uploaded checker was not executed. No exact maximal tongue boundary is certified.

## originality

PASS

The map itself is not new: the two branches are exactly on a parameter path in Herman's family as displayed by Glendinning–Ma–Montaldi. The supported distinct content is the singular large-denominator asymptotic for this path, including explicit odd/even cubic-scale interior windows and the third-order identity obstruction. The closest inspected fixed-rational results do not give estimates uniform in q or determine these two constants. No claim of first discovery of the family or comprehensive priority is made.

## value

PASS

A natural positive-velocity path through the identity has a well-defined first-order rotation rate, yet its large-denominator plateaus preclude a third-order approximation. Explicit parity-sensitive coefficients make this an effective witness, not merely a qualitative assertion that rational plateaus occur. The distinction between a fixed-resonance perturbation and the singular identity limit matters for interpreting rotation-number regularity.

The dated certificate retains the supplied scientific assessment, sources and limitations.

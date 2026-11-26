# Independent mathematical audit

## correctness

PASS

The convex Euclidean covering strip realizes the two nearest deck-image distances, one per parity. Fixing target height v, one squared candidate increases and the other decreases with longitudinal position. Their minimum is maximized at the crossing clipped to [0,L]. Symmetry permits v>=0. Before the crossing clips, the maximized value grows with v^2. After clipping it is the convex function L^2+(v-u)^2 of v, so only the clipping boundary and top edge remain. This gives the entire stated profile including u=0 and uw=L^2/4. For w>L/2 put c=L^2/4 and u0=c/w. On [u0,w], the difference A^2-B^2=(2u-w-c/u)(w-c/u) gives one interior branch switch at u*=(w+sqrt(w^2+2L^2))/4 in (L/2,w). B decreases to the switch and A then strictly increases. The first piece increases away from the core, leaving exactly 0 and u* as minimum candidates. The derivative of their eccentricity difference is strictly positive for w>=L/2, and substitution gives the unique tie at w=7sqrt(15)L/30, radius 4L/sqrt(15), off-core height sqrt(15)L/6 and slopes 7/8 and 2/13. Both signed off-core levels form one circle in the quotient. For the contextual diameter proof, the earlier distance law has diameter as its support endpoint by continuity and full area support. At fixed horizontal separation a, the feasible absolute sums and differences of the transverse coordinates form a triangle with sum at most H. The saturation threshold increases after the second deck constraint becomes available because (C-a)/V>=a/U; before that threshold decreases. This gives the two stated formulas for saturation and hence the diameter. Its normalized squared profile is reciprocal and one-variable minimization gives the two stated ratios; distinct core lengths at fixed area are distinguished intrinsically by the systole. The analytic proof checks the universal conclusions; the frozen numerical code was inspected but not used to establish them.

## originality

PASS

PASS for the repaired focus on conditional eccentricity and the Chebyshev center set. The original diameter section cannot be credited as an independent new result: the earlier exact two-point distance law provides the diameter as its support endpoint, with a short branch computation, and the reciprocal inequality and equality ratios follow routinely. Those statements remain correct and are retained only as attributed context. A distinct later catalogue record explicitly gives the same conditional profile, radius and center transition after parameter conversion; this is genuine overlap, not evidence of prior coverage of the November 2 record. Neither the inspected earlier aggregate formulas nor the inspected primary passages establish the repaired conditional minimax result.

## value

PASS

For the conditional problem the location of a covering center is not encoded in the support endpoint of a random-pair distance law. The full pointwise profile answers that metric minimax question exactly: there are two competing source loci, both optimal at an explicit coexistence width, with a positive optimizer jump and distinct slopes of the continuous optimal value. This is a meaningful exact benchmark for intrinsic farthest-point and covering-center calculations on a nonorientable surface. The diameter optimization is useful context but not the basis for this pass.

The dated certificate retains the supplied scientific assessment, sources and limitations.

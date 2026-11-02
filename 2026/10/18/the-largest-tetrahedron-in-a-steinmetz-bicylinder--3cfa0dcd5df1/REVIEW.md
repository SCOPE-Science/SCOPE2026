# Independent mathematical audit

## correctness

PASS

Read the assigned RESULT.md and independently verified all four proof steps. For R=1, u=(x+y)/2, v=(x-y)/2 yield D={(u,v,z):(|u|+|v|)^2+z^2<=1}=conv(D_u union D_v), where D_u,D_v are centered perpendicular unit disks and affine map back has determinant magnitude 2. The signed four-vertex determinant is separately affine in every vertex, so some optimum lies on the two generating rim circles. Single-circle choices are degenerate, while a 3+1 split has triangle area <=3sqrt(3)/4 and height <=1, giving volume <=sqrt(3)/4<8/(9sqrt(3)) in D. For 2+2, independently expanded the trigonometric chord determinant to exactly 4 sin(alpha)sin(beta)(sin(psi)cos(alpha)-sin(phi)cos(beta)); writing a=cos(alpha), b=cos(beta) in [0,1], its absolute value is at most 4(a+b)(1-(a+b)^2/4)<=16/(3sqrt(3)), with equality only a=b=1/sqrt(3) and sin(psi)=-sin(phi)=+/-1. This yields D-volume 8/(9sqrt(3)) and bicylinder-volume 16/(9sqrt(3)). The strict support-functional computation for each canonical vertex (e.g. n=(2/sqrt(3),0,sqrt(2/3)), plane n dot x=-sqrt(2)/3) gives unique absolute-distance maximum at the intended rim point; reverse multiaffine replacements exclude hidden interior/noncanonical maximizers. Independently checked the exact coordinate determinant and support heights via SymPy, and 7000 rational point-circle splits via Fraction (3500 2+2; 3500 3+1) with no inequality violation. A separate 20000-sample two-chord test stayed under the analytic maximum. These finite tests corroborate but do not imply global optimization. Bicylinder horizontal sections have area 4(1-z^2), so body volume 16/3 and fraction 1/(3sqrt(3)). Scaling by R^3 and degeneracies R>0 are explicit.

## originality

PASS

Qualified best-of-knowledge originality. The identical convex body is classical, and Finch obtained its disk-hull volume 8/3; the bicylinder ambient volume 16/3 is also classical. New scientific content assessed is the globally sharp contained-tetrahedron volume and all-maximizer classification. Fresh semantic Resultary queries, published full RESULT files, targeted exact-string/alias searches and substantive primary-paper reading did not reveal a dominating theorem or table; general center-containment and convexity facts are acknowledged as prior tools, not rediscovered. Inaccessible/unindexed historical geometry could affect priority; no negative search is treated as proof of global priority.

## value

PASS

For a canonical classical convex body, the volume of the largest contained tetrahedron and its dimensionless ratio to ambient volume are intrinsic affine-invariant measures of approximation by a minimal-vertex polytope. The target exact 1/(3sqrt(3)) fraction is not a table recomputation of ambient volume, not a contrived parameter slice, and not mechanically implied by standard center-inclusion or surface-measure theorems. Strict equality classification rules out all asymmetric/interior alternatives and supplies a concrete sharp geometric benchmark. A future worker studying four-point approximation or contained-simplex volume ratios could need this precise extremal value and optimizer structure; no theorem for oblique/unequal/translated cylinder intersections is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.

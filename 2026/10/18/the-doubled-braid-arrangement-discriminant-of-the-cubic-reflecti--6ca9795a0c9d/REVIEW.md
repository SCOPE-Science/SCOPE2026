# Independent mathematical audit

## correctness

PASS

Checked the homogeneous gradient determinant and the reductions to x=0 and x=y by the common coordinate/parameter permutation. The rank-drop test puts every singular point on those six source lines; the two gradient restrictions force respectively a=0 and a=b in the representatives. Conversely the explicit line factors give singularity there. Off their intersections, the two representative residual conics have nonzero determinants and distinct roots on the component line, so both intersections are nodes. The four triple and three double parameter points account for all 15 unordered pairs of parameter lines (4*3+3); representative factorizations give a triangle at [1:1:0] and distinct concurrent lines at [0:0:1] and [1:1:1]. The universal discriminant near two ordinary nodes has independently smooth branches: the first-order smoothing maps are evaluations at the two nodes, independent on cubic forms, and the ordinary-node Hessians are invertible. Both branches vanish along each generic arrangement line. Each line therefore contributes at least two to the degree-12 nonzero specialized polynomial; the product exhausts its degree. As a separate exact symbolic check, on projection from [0:0:1] with y=1, t=x/y, the quadratic in z has branch quartic (a-b*t^2)^2-4*(b*t-a)*c*t*(t-1). Its exact univariate discriminant is 4096[abc(a-b)(a-c)(b-c)]^2; replay with a symbolic polynomial discriminant in t and factor over Q[a,b,c]. This is corroboration, not an identification by fiat of the plane-cubic discriminant with a projection discriminant. Off the arrangement a smooth plane cubic is geometrically integral by Bézout and of genus one. All arguments use characteristic zero. The frozen script was inspected, not executed; its seven-point test checks listed incidences, whereas exhaustion here uses the line-pair count.

## originality

PASS

The net and its reflection-arrangement context are already known. The supported distinct claim is the scheme multiplicity and complete stratification for the original plane cubic equations over the whole parameter plane. Neither the closest primary statements nor the closely related indexed double-plane model supplies that plane-cubic result. This is a bounded statement-level assessment, not a global priority guarantee.

## value

PASS

This is the cubic case of a pre-existing natural reflection net, not an arbitrary slice. The precise multiplicity separates a reduced support description from the discriminant divisor used in degeneration calculations. The stratification distinguishes two nodes along a generic discriminant line, a triangle at one intersection type and an ordinary triple point at the other; those distinctions inform which degenerations a pencil in this net can encounter. This is an exact, useful plane-geometry invariant beyond the prior freeness and double-plane branch descriptions.

The dated certificate retains the supplied scientific assessment, sources and limitations.

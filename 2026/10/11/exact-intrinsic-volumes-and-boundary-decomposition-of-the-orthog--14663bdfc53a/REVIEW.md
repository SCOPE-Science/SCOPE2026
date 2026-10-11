# Scientific review: orthogonal three-disk hull

## Correctness — PASS

For a normal in Euclidean three-space, maximizing over the three input disks gives the exact support function as the square root of the squared normal length minus its smallest squared coordinate. This splits supporting faces into one-point faces, segments occurring when two least absolute coordinates tie, and eight triangles occurring when all three tie. The parametrization of each of the twenty-four ruled patches is explicitly supported by its computed normal. The area integral on one patch is \(1/2-\sqrt3/4+\pi/12\), and its divergence flux is \(1-1/\sqrt2\). Adding the eight triangular faces gives both closed forms without uncontrolled approximation. The squared-coordinate support minimum proves the centered inradius; central symmetry proves its global optimality. Separate numerical convex-hull approximations support the calculations but cannot certify the continuous proof.

## Originality — PASS, with risks

Finch's arXiv:1211.4514 treats configurations of *two* orthogonal disks and proves a different two-disk pair of volume and area formulas. Nash–Pir–Sottile–Ying (arXiv:1612.09382) develop the face structure of hulls of *two* circles, while Wu–Gupta–Kurzeja–Rossignac (doi:10.1016/j.cad.2020.102903) restrict their cospherical-circle construction to disjoint cap circles; three great circles do not lie in that class. The known tricylinder formula describes the *polar* of the present hull, not its volume or surface area. Alias, numerical-constant and published-research searches yielded no statement demonstrably implying the present exact two-invariant and surface-stratification result. Search failure alone is not a novelty certificate. Some historical full text remains inaccessible, and an independently derived special-case formula may exist under another name.

## Value — PASS

Three pairwise perpendicular centered disks form the first symmetric disk family that is not covered by the common-axis arrangement, and their convex hull is the polar dual of the canonical tricylinder. The result supplies exact closed intrinsic volumes for this natural geometric solid, identifies previously nontrivial eight triangular facets and twenty-four developable boundary patches, and gives a complete proof using supporting faces and divergence flux. These are distinct measurements and a complete boundary classification, not a routine substitution into the older two-disk calculations or a merely numerical recomputation.

## Sources and limitations

Principal inspected sources: Finch, arXiv:1211.4514, especially Examples 1–3 and Section 1; Nash–Pir–Sottile–Ying, arXiv:1612.09382, especially Theorem 2.1, Section 4 and Section 5. The 2019 public CHoCC poster and the 2020 article abstract were available, but full text of the latter was not. The result does not determine mean width or extend beyond the exact disk geometry specified. Independent external assessment has not occurred.

Same-model review: passed. Independent audit: not yet performed.

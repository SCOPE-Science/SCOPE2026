# Independent mathematical audit

## correctness

PASS

Away from θ=0,π, eliminating the two point equations with positive radial factors u,v gives z=α(u+r)/(uv−r²), and the analogous w; unit length and primality imply u≠v and u+v=−2cosθ. With s=|sinθ| and q=1−uv this forces cosθ<0 and s²<q<1. Conversely a root of Q(q)=q²−(α²+4s²)q+4s² in that range gives two positive normalizers and distinct unit points satisfying both original equations, so the roots count unordered cycles. Q(s²)>0 and Q(1)>0 around the low-sine regime, and Q(2s)=2s[4s(1−s)−α²] locates the two interior roots or the double edge root. In the other nonnegative-discriminant regime s≥(1+√(1−α²))/2, the vertex is beyond one and Q(1)>0, ruling out extra branches. At θ=0 there are fixed points and no two-cycle by circle order. At θ=π, if uv≠1 the eliminated equations imply real z,w and give {1,−1}; if uv=1 they force u=v=1 and z+w=α, giving the conjugate pair exactly. The angular derivative is positive; its product gives the displayed multiplier, with sign of Λ−1 equal to the sign of q−2s. The central multipliers follow by direct substitution. No F-fixed point can coexist with a primitive two-cycle, so all F² fixed points are the stated cycle points. Monotone iteration on the complementary intervals between them proves the basin assertions, including convergence to the neutral edge cycle as a set. The discriminant derivative at s_α is −32s_α√(1−α²), yielding the coefficient and exponent; Taylor expansion gives the weak-forcing width. As a separate bounded edge check, α=√3/2, s=1/4 gives q=1/2, u,v=(√15±√7)/4; direct normalization interchanged the two reconstructed points to floating-point precision and the direct derivative product was 1 to about 2.5×10⁻¹⁵. Inspected the supplied checker in checks/ (missed by the baseline path list); its frozen four symbolic and 90 numerical tests were not executed and do not replace the all-angle proof.

## originality

PASS

The sharp angular boundary and off-center classification are supported as distinct contributions relative to the earlier inspected work. Prior central-angle classification and local persistence are expressly covered. A distinct, later Resultary record states the very same sharp boundary and two/one/zero classification, which is exact overlap, not uniqueness evidence. Its later catalogue publication does not establish earlier coverage or provenance. The frozen global-basin clause and branch-gap formula are explicit additions relative to that particular statement; both are deductions once the exact cycle or root structure is known, not substitutes for establishing novelty of the core result against earlier sources.

## value

PASS

The exact locking domain closes a natural open quantitative part of the earlier local-persistence classification for this circle family. Its all-strength boundary and change in number and stability of primitive two-cycles give a usable phase diagram, including why the edge is sharp and the relevant square-root coalescence. These are motivated quantities, not a tiny parameter slice; other rotation numbers and invariant statistics are outside scope.

The dated certificate retains the supplied scientific assessment, sources and limitations.

# Independent mathematical audit

## correctness

PASS

For all p of degree 2 the sole derivative zero is the sole critical-level root. For cubic p with a double derivative zero the centered normal form is a pure cube. With distinct derivative zeros b±u, the general normal form p(b+t)=a(t^3-3u^2t)+c factors at each critical value as a(t-u)^2(t+2u) or a(t+u)^2(t-2u), yielding collinear segments [b-2u,b+u] and [b-u,b+2u] whose intersection is [b-u,b+u]. For the specific quartic, p′=4(z+8/5)(z^2+1), so its derivative hull is in Re z<=0. The exact three critical-level factorizations contain w=2/21 through convex combinations with weights 89/112, 9/14 and 5/14; the positive real witness lies outside the derivative hull. An independent SymPy program checked all three polynomial factorizations, all three barycentric identities, and both generic cubic polynomial identities, with no inference from finite examples to the universal claim.

## originality

PASS

Best-of-knowledge PASS. The claimed finite critical-value sampling threshold is not implied by the inspected Gauss-Lucas variants, the withdrawn all-shifts formula, the fixed-shift equality characterization or the 2014 triangle-location theorem. The relevant 2026 JMAA journal article was identified and its abstract compared; full text could not be inspected, leaving a named priority risk. An unsuccessful search alone is not treated as novelty proof.

## value

PASS

The critical values are a canonical finite family of shifts when attempting to recover the derivative-zero convex hull from fiber-zero convex hulls. Proving the exact low-degree success and providing the first rational quartic obstruction identifies a motivated sharp boundary that is useful when deciding whether that finite sampling shortcut is valid. The result does not classify quartic failures, cover degrees above four, or resolve an arbitrary-shifts intersection identity.

The dated certificate retains the supplied scientific assessment, sources and limitations.

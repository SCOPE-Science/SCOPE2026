# Orientation obstruction to a fixed-ball perturbation lemma
## Finding
For the standard circle \(S^1\) equipped with its geodesic metric, consider the reflection
\[
f(e^{i\theta})=e^{-i\theta}.
\]
It is a Lipschitz homeomorphism and fixes \(p=1\). There is no homeomorphism \(\widetilde f:S^1\to S^1\) satisfying both \(d_{C^0}(f,\widetilde f)<\pi\) and the requirement that \(\widetilde f\) equal the identity on a positive-radius closed ball centered at \(p\).

Therefore Theorem 4.9 of Arbieto, Britto, and Rego, in arXiv:2607.09394v1, is false as stated. The theorem is a perturbation lemma used in the paper's proof of its \(C^0\)-density result for finite-entropy homeomorphisms with phase transitions. The obstruction below concerns that perturbation lemma and the cited proof route; it does not imply that the density theorem itself is false.

## Assumptions and scope
The counterexample uses the connected orientable manifold \(S^1\) with geodesic distance normalized so that antipodal points are at distance \(\pi\). A "closed ball" is understood in the positive-radius sense used in the source proof, where an entire neighborhood is made pointwise fixed.

The claim applies to the version first posted as arXiv:2607.09394v1 on 2026-07-10. No assertion is made about a later corrected version unless it contains the same statement.

## Proof
The reflection \(f(e^{i\theta})=e^{-i\theta}\) has degree \(-1\). Suppose that a circle homeomorphism \(\widetilde f\) is the identity on a nondegenerate closed arc. An orientation-reversing circle homeomorphism cannot fix two distinct points in the interior of one lifted interval: a lift of an orientation-reversing homeomorphism is strictly decreasing, while the identity relation at two ordered points would force the opposite order. Hence \(\widetilde f\) is orientation preserving and has degree \(+1\).

Now assume \(d_{C^0}(f,\widetilde f)<\pi\). For every \(x\in S^1\), the points \(f(x)\) and \(\widetilde f(x)\) are joined by a unique shortest geodesic. Because the distance stays strictly below the antipodal threshold, these shortest geodesics depend continuously on \(x\). Traversing them gives a homotopy from \(f\) to \(\widetilde f\), so their degrees must agree. This contradicts \(\deg f=-1\) and \(\deg\widetilde f=+1\).

The failure is also visible inside the source's displayed interpolation. In a local angular coordinate around \(p\), the reflection is \(\theta\mapsto-\theta\). Formula (4.3) then becomes
\[
g_0(\theta)=\bigl(1-2\rho(|\theta|)\bigr)\theta.
\]
The source chooses \(\rho\) continuously with value \(0\) on an inner region and value \(1\) at the outer region. Hence some radius \(s>0\) satisfies \(\rho(s)=1/2\), and then \(g_0(s)=g_0(-s)=0\). The interpolation is therefore not injective in this example.

## Verification
The degree obstruction and the explicit local formula are independent checks. The first uses only orientation of circle homeomorphisms and homotopy invariance of degree. The second substitutes the reflection directly into the source's formula (4.3) and exhibits two distinct points with the same image.

The source statement, its construction, and its later use in the proof of Theorem E were inspected in the full text. Exact-claim searches for an orientation correction or an already-published version of this counterexample found no matching result. Searches of prior scientific findings using the source title, theorem number, authors, orientation reversal, and fixed-ball language found no overlapping claim.

## Relationship to prior work
Arbieto, Britto, and Rego state Theorem 4.9 for an arbitrary Lipschitz homeomorphism with a fixed point and claim an arbitrarily small perturbation that becomes the identity on a ball while retaining an entropy bound. Their proof uses a straight-line interpolation in local coordinates and asserts that the resulting curves are pairwise disjoint. The circle reflection shows that this cannot hold without an orientation-compatible hypothesis or a different perturbation mechanism.

The paper's Theorem A, which produces phase transitions from failure of chain transitivity, is not challenged here. The issue is isolated to the later local perturbation step used for the \(C^0\)-density argument.

## Limitations
This finding does not decide whether the paper's final \(C^0\)-density theorem is true by another argument. It also does not rule out a corrected fixed-ball lemma inside an orientation-preserving component, nor a replacement construction for orientation-reversing maps that preserves the relevant homotopy class. The exact obstruction proved here is the impossibility of the stated identity-on-a-ball perturbation for the reflection on \(S^1\) at sufficiently small \(C^0\) distance.

## References
1. Alexander Arbieto, Walter Britto, Elias Rego, “On the Abundance of Phase Transitions in Dynamical Systems,” arXiv:2607.09394v1, first posted 2026-07-10. Theorem 4.9, formula (4.3), Lemma 4.10, and the proof of Theorem E were inspected in the available full text.
2. Standard circle topology facts used in the proof: orientation-preserving homeomorphisms have degree \(+1\), orientation-reversing homeomorphisms have degree \(-1\), and uniformly non-antipodal maps are homotopic by shortest-geodesic interpolation.

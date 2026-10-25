# Branch-order rigidity in synchronized motion planning on the Riemann sphere

## Finding

**Theorem.** For arbitrary positive integers \(a,b\), let \(P_a,P_b\colon \mathbb{CP}^{1}\to\mathbb{CP}^{1}\) be the power maps \(P_a(z)=z^{a}\) and \(P_b(z)=z^{b}\) in the finite complex chart, with \(P_a(\infty)=P_b(\infty)=\infty\). In the normalized definitions of García-Calcines and Vilches Alarcón [1], the pair is pointwise synchronizable and
\[
 \operatorname{TC}_{H}(P_a,P_b)=2,\qquad
 \operatorname{TC}(P_a,P_b)=
 \begin{cases}2,&a=b,\\ \infty,&a\ne b.\end{cases}
\]
In particular, both maps are surjective with equal images and equal branch-value sets when \(a,b\ge2\), yet unequal positive exponents force an infinite strict complexity.

## Assumptions and scope

All spaces carry their usual compact Hausdorff topologies. A *synchronized motion* for endpoints \((x,y)\) is a pair of continuous paths \(\alpha,\beta:[0,1]\to\mathbb{CP}^{1}\) such that \(\alpha(0)=x\), \(\beta(1)=y\), and \(P_a(\alpha(t))=P_b(\beta(t))\) for every \(t\in[0,1]\). A local strict planner is a continuous assignment of synchronized motions to \((x,y)\) on an open subset of \(\mathbb{CP}^{1}\times\mathbb{CP}^{1}\), using compact-open path topologies. The normalized strict invariant is the least number of such open sets minus one, or infinity if no finite such cover exists.

The homotopy-invariant version is the normalized homotopic distance between the maps \(F=P_a\circ\operatorname{pr}_1\) and \(G=P_b\circ\operatorname{pr}_2\) from \(\mathbb{CP}^{1}\times\mathbb{CP}^{1}\) to \(\mathbb{CP}^{1}\). The convention is \(\operatorname{TC}(S^2)=2\), corresponding to three local ordinary planners. No claim is made about arbitrary degree-\(a\) and degree-\(b\) continuous maps: the strict classification concerns these specified branched power-map representatives.

## Proof

**1. Synchronizability.** Form the equality fibre product
\[
 W_{a,b}=\{(u,v)\in\mathbb{CP}^{1}\times\mathbb{CP}^{1}:u^{a}=v^{b}\},
\]
where the equality at infinity is interpreted by the maps \(P_a,P_b\). Both projections from \(W_{a,b}\) onto \(\mathbb{CP}^{1}\) are surjective: every finite complex value has a root of every positive integral order, and the infinite value has preimage infinity.

This fibre product is path connected. Indeed, each finite solution \((u,v)\) admits a path \(t\mapsto(t^{b}u,t^{a}v)\) for \(0\le t\le1\), joining \((0,0)\) to \((u,v)\). The remaining point \((\infty,\infty)\) is connected to \((1,1)\) by the continuous path \(t\mapsto(t^{-b},t^{-a})\), \(0<t\le1\), extended at \(t=0\) by \((\infty,\infty)\). Thus each endpoint pair \((x,y)\) can be joined by a path inside \(W_{a,b}\) from some point over \(x\) to some point over \(y\). Its coordinate paths constitute a synchronized motion. Note that path connectedness is weaker than existence of any continuously varying planner.

**2. Local ramification-order obstruction.** Suppose a strict continuous local planner existed on an open neighborhood \(U\) of \((0,0)\). Choose \(\varepsilon>0\) so the disks \(\{(z,0):|z|<\varepsilon\}\) and \(\{(0,z):|z|<\varepsilon\}\) lie in \(U\). Let \((\alpha_{x,y},\beta_{x,y})\) be its assigned paths. By continuity of endpoint evaluations, the map \(h(x)=\beta_{x,0}(0)\) is continuous on the first disk and satisfies
\[
 h(x)^{b}=P_b(h(x))=P_a(\alpha_{x,0}(0))=x^{a}.
\]
Since \(h(0)=0\), it takes finite complex values near the origin. It is nonzero away from the origin. Restrict to a sufficiently small positively oriented circle. Winding numbers about zero satisfy \(b\operatorname{wind}(h)=a\); hence \(b\mid a\).

Similarly, along the second disk the continuously varying terminal coordinate \(k(y)=\alpha_{0,y}(1)\) satisfies
\[
 k(y)^{a}=P_a(k(y))=P_b(\beta_{0,y}(1))=y^{b}.
\]
Consequently \(a\mid b\). Since \(a,b\) are positive, both divisibilities imply \(a=b\). Therefore for \(a\ne b\) *no* open neighborhood of \((0,0)\) admits a strict planner. Every proposed open cover of the entire endpoint space would have to contain that point in a planner domain, which is impossible; hence \(\operatorname{TC}(P_a,P_b)=\infty\).

**3. The equal-exponent case.** If \(a=b\), take any ordinary path-planning cover of \(\mathbb{CP}^{1}\cong S^2\) with three open sets and continuous ordinary planners \(\sigma_{x,y}\) from \(x\) to \(y\). Assign \(\alpha_{x,y}=\beta_{x,y}=\sigma_{x,y}\) on each set. Because \(P_a=P_b\), these are synchronized local planners, giving \(\operatorname{TC}(P_a,P_a)\le2\).

**4. Homotopy-invariant lower and upper bounds.** Over \(\mathbb{Q}\), let \(u,v\in H^2(\mathbb{CP}^{1}\times\mathbb{CP}^{1};\mathbb{Q})\) be the respective positive generators. If \(\omega\in H^2(\mathbb{CP}^{1};\mathbb{Q})\) is the positive generator, then
\[
 F^{*}\omega=a u,\qquad G^{*}\omega=b v,\qquad
 (F^{*}\omega-G^{*}\omega)^2=-2ab\,uv\ne0.
\]
Here \(u^2=v^2=0\) and \(uv\) generates degree-four rational cohomology. On any open set on which \(F\) and \(G\) are homotopic, their cohomology homomorphisms agree, so the class \(F^{*}\omega-G^{*}\omega\) restricts to zero. If two such open sets covered the product, the standard relative cup-product argument would force its square to vanish. Thus any homotopic-distance cover has at least three open sets and \(\operatorname{TC}_H(P_a,P_b)\ge2\).

Conversely, pull back the standard three-set local motion-planning cover of \(\mathbb{CP}^{1}\cong S^2\) along \((x,y)\mapsto(P_a(x),P_b(y))\). On each pulled-back open set, the ordinary path from \(P_a(x)\) to \(P_b(y)\) gives a homotopy from \(F\) to \(G\). Hence \(\operatorname{TC}_H(P_a,P_b)\le2\). This establishes the asserted equality for all positive \(a,b\), and the same lower bound applies to strict planners in the equal-exponent case, closing the proof. \(\square\)

## Verification

The divisibility argument uses only continuity of endpoint evaluation and the integer winding number of a map from a circle into \(\mathbb{C}\setminus\{0\}\). Both directions, \(b\mid a\) and \(a\mid b\), are essential: a one-sided divisibility is not by itself an obstruction to one of the endpoint slices. The scale path \(t\mapsto(t^b u,t^a v)\) is checked directly by \((t^b u)^a=t^{ab}u^a=t^{ab}v^b=(t^a v)^b\); the infinity path has the same property in reciprocal coordinates. The cohomological square is nonzero for every positive \(a,b\), including \(a=b=1\).

Reproduction needs no numerical computation or external certificates: check the two displayed power-map equalities, winding-number divisibility on a small positive circle, and the cup-product identity in the ring \(\mathbb{Q}[u,v]/(u^2,v^2)\). The exact requirement that planner domains be open is decisive, as it forces a neighborhood of \((0,0)\) to belong to some domain.

## Relationship to prior work

García-Calcines and Vilches Alarcón [1] introduce and compare strict bivariate topological complexity with its homotopy-invariant version. Their Example 3.4 derives a cohomological lower bound for degrees two and three on the two-sphere, while their examples also treat nonsynchronizable pairs and unbranched circle covers. The theorem here makes a different exact comparison for the specified *branched power maps*: all endpoint pairs admit synchronized motions, but unequal ramification indices make even a local planner around the common branch-value pair impossible. The degree-two/degree-three power-map instance therefore has infinite strict complexity although its homotopy-invariant value is two. This does not claim the definitions, cup-length principle, or the classical sphere motion-planning calculation as new.

Related finite-space studies of sphere-map classes and divisibility, and affine-torus synchronization formulas, apply to different source/target spaces or unbranched maps; neither implies the two-sided branch-order obstruction here.

## Limitations

The strict classification is for the *specific* maps \(P_a\) and \(P_b\), not all continuous maps of degrees \(a,b\). Equivariant, parametrized, higher-arity, or relative variants are not addressed. The only scientific novelty assertion is the combined pointwise-synchronizability/strict-infinity dichotomy with the exact homotopy-invariant comparison; known general facts are identified as inputs. Literature searching does not exclude every possible equivalent prior formulation. No independent audit has been performed.

## References

[1] J. M. García-Calcines and J. A. Vilches Alarcón, *Bivariate topological complexity: a framework for coordinated motion planning*, arXiv:2601.16059v1, first publicly available 2026-01-22, https://arxiv.org/abs/2601.16059. See definitions and examples in Sections 2–3 and the cohomological lower-bound discussion.

[2] M. Farber, *Topological complexity of motion planning*, Discrete and Computational Geometry **29** (2003), 211–221, doi:10.1007/s00454-002-0760-9. Classical computation of normalized sphere topological complexity after subtracting one from the original unreduced convention.

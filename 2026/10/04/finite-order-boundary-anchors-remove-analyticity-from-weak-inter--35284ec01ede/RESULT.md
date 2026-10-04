# Finite-order boundary anchors remove analyticity from weak-interconnection transitivity
## Finding
Let \(F(x,t)=(f(x),\phi_x(t))\) be a \(C^\infty\) boundary-preserving partially hyperbolic skew-product diffeomorphism on a thickened nilmanifold, with Anosov base and weak boundary interconnection in the sense of Li and Xia. After possibly exchanging the two boundary components, suppose the lower boundary contains a central sink-type periodic point \(p_-\) and a central source-type periodic point \(p_+\) whose fiber return germs at \(t=0\) have finite order: for a return map \(\Phi\), set \(\operatorname{ord}_0(\Phi)=1\) when \(\Phi'(0)\ne1\), and otherwise take the least \(m\ge2\) with \(\Phi^{(m)}(0)\ne0\), if such an \(m\) exists. Then \(F\) is totally topologically transitive. No nonflatness is required of the other periodic fiber return germs: they may be infinitely flat at the boundary.

## Assumptions and scope
The phase space is a thickened nilmanifold \(N\times[0,1]\). The map is a \(C^\infty\) boundary-preserving partially hyperbolic skew product \(F(x,t)=(f(x),\phi_x(t))\), where \(f\) is Anosov. Weak boundary interconnection is exactly the geometric condition introduced by Li and Xia. After exchanging the boundary components if necessary, assume that on \(N\times\{{0\}}\) there is at least one sink-type periodic return germ and one source-type periodic return germ with finite boundary order as defined in the finding. Other periodic return germs may be flat to every order.

## Proof
Write \(\Phi_p\) for the fiber return map at a boundary periodic point. Give a smooth return germ finite order \(1\) when \(\Phi_p'(0)\ne1\), finite order \(m\ge2\) when the derivatives through order \(m-1\) agree with the identity jet and \(\Phi_p^{(m)}(0)\ne0\), and order \(\infty\) when every derivative agrees with the identity jet. By hypothesis there are finite-order sink and source germs, so the sets of their finite orders have minima. Choose a sink \(p_0\) and a source \(q_0\) with minimal finite orders.

The topological stable/unstable-set lemmas in Li--Xia do not use analyticity. Their one-dimensional reparameterization \(\tau_\Phi(x)=\int_x^\delta (u-\Phi(u))^{-1}\,du\) only requires \(C^1\) regularity. The only analytic input in their bounded-distortion lemma is the finite Taylor alternative. For the selected smooth finite-order germs that same alternative is available: in the hyperbolic case \(x-\Phi(x)=(1-\alpha)x+O(x^2)\), while in the parabolic case \(x-\Phi(x)=a x^m+O(x^{m+1})\) with \(a>0\). Substitution into their exact logarithmic-derivative identity
\[
\left(\log(T_\Phi'\circ\tau_\Phi)\right)'=
\left(\log\frac{x-\Phi(x)}{\Phi(x)-\Phi^2(x)}\right)'+\frac{\Phi''(x)}{\Phi'(x)}
\]
shows the derivative is bounded near \(0\); hence the fundamental-domain distortion estimate remains valid.

The proof of the Li--Xia one-dimensional intersection proposition then carries over verbatim for these two selected germs. Its remaining local inputs are precisely the same finite Taylor expansions and the standard iterate scales: exponential in the hyperbolic case and \(n^{-1/(m-1)}\) for a parabolic germ of finite order \(m\). Thus the corresponding interval-length scale is \(n^{-m/(m-1)}\).

It remains to check the periodic-orbit bookkeeping used in the global proof. Any periodic return germ whose first nonidentity jet has order below \(n=\min\{\operatorname{ord}_0(\Phi_{p_0}),\operatorname{ord}_0(\Phi_{q_0})\}\) would itself be locally sink-type or source-type, contradicting minimality. Therefore every periodic return map has the identity jet through order \(n-1\). The Li--Xia Livšic normalization of these lower jets therefore works in the smooth category. Infinitely flat germs simply contribute zero to every finite jet used in that normalization. The density-of-Birkhoff-sums step then produces the same finite-order periodic anchors used in the three order-comparison cases of their proof, and the previously established one-dimensional intersection estimate gives \(U^*\cap V^*\ne\varnothing\) for arbitrary nonempty open \(U,V\). Hence \(F\) is topologically transitive.

Finally, every positive iterate preserves weak boundary interconnection. A positive iterate of a finite-order sink or source return germ has the same finite order (with its first nonzero coefficient multiplied by a positive integer in the parabolic case), so each positive iterate still satisfies the finite-anchor hypothesis. Applying the argument to every positive iterate proves total transitivity.

## Verification
The proof was checked against the complete Li--Xia argument, including their reparameterization lemma, bounded-distortion lemma, one-dimensional intersection proposition, finite-jet Livšic normalization, three order-comparison cases, and final passage to positive iterates. The regularity replacement is local: every place where analyticity enters is supplied by a finite Taylor expansion of one of the selected finite-order germs or by finite jet data. No conclusion is drawn from numerical experiments.

## Relationship to prior work
Li and Xia prove total transitivity under analytic central regularity and explicitly note that analyticity is used only in the center direction. Their proof permits arbitrarily high finite parabolic order but, in the smooth category, analyticity is what rules out a nonidentity germ that is flat to every order. The present statement shows that global analyticity is unnecessary: it is enough to have one finite-order sink anchor and one finite-order source anchor on the same boundary, while every other periodic return germ may be infinitely flat.

Earlier smooth results impose stronger dynamical hypotheses. Li--Shi--Xia characterize \(C^k\)-robust transitivity using the stronger boundary-interconnection condition, and Kan-type mixing/transitivity results treat more restrictive north--south fiber configurations. Those results do not imply the weak-boundary-interconnection statement above.

## Limitations
The theorem does not cover the case in which, on each boundary available to the weak-interconnection argument, every sink-type germ or every source-type germ is infinitely flat. It also does not assert topological mixing. The argument uses smooth finite jets and therefore does not claim a sharp finite differentiability threshold.

## References
W. Li and M. Xia, “On the Topological Transitivity of Interval Extensions of Anosov Diffeomorphisms,” arXiv:2609.24437v1, 2026.

W. Li, Y. Shi, and M. Xia, “Robust Transitivity of Partially Hyperbolic Diffeomorphisms with Interval Central Leaves,” arXiv:2509.21954, 2025.

M. Xia, “Topological transitivity of Kan-type partially hyperbolic diffeomorphisms,” Discrete and Continuous Dynamical Systems 44 (2024), 585--599.

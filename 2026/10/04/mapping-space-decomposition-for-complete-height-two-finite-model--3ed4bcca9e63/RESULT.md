# Mapping-space decomposition for complete height-two finite models
## Finding
For integers \(p,q,r,s\ge 2\), write
\[
P_{p,q}=A_p\oplus B_q,\qquad P_{r,s}=C_r\oplus D_s,
\]
where each displayed level is an antichain and every lower-level point is below every upper-level point. Let \(\operatorname{Map}(P_{p,q},P_{r,s})\) be the finite poset of order-preserving maps with the pointwise order.

Exactly
\[
I=(r^p-r)(s^q-s)
\]
maps are isolated points of this map poset. They are precisely the level-preserving maps \(f=(\alpha,\beta)\) for which both \(\alpha:A_p\to C_r\) and \(\beta:B_q\to D_s\) are nonconstant. Every other map belongs to one component \(K\). The order complex of \(K\) strongly deformation retracts onto the constant-map copy of \(P_{r,s}\). Therefore
\[
|K|\simeq |\mathcal K(P_{r,s})|=|K_{r,s}|\simeq \bigvee^{(r-1)(s-1)}S^1,
\]
and
\[
\left|[P_{p,q},P_{r,s}]\right|=1+(r^p-r)(s^q-s).
\]
The total number of continuous maps is
\[
|\operatorname{Map}(P_{p,q},P_{r,s})|
=r^p s^q+s\big((r+1)^p-r^p\big)+r\big((s+1)^q-s^q\big).
\]
Thus the source parameters control the number of rigid singleton components, while the unique nontrivial component has the homotopy type of the target height-two model itself.

## Assumptions and scope
All spaces are finite \(T_0\)-spaces, identified with their specialization posets, and continuity means order preservation. The four parameters satisfy \(p,q,r,s\ge2\). The assertion about strong deformation retraction concerns the geometric realization of the order complex of the component \(K\); it does not assert that \(K\) itself beat-point retracts to the constant-map subspace. Homotopy classes are unbased homotopy classes of continuous maps of finite spaces.

## Proof
Let \(f:P_{p,q}\to P_{r,s}\) be monotone. There are three mutually exclusive forms.

First, \(f\) may preserve the two levels, in which case it is an arbitrary pair \((\alpha,\beta)\) with \(\alpha:A_p\to C_r\) and \(\beta:B_q\to D_s\). Second, if some point of \(A_p\) is sent to a maximal point \(d\in D_s\), then monotonicity forces every point of \(B_q\) to be sent to that same \(d\), while each point of \(A_p\) may be sent to any point of \(C_r\cup\{d\}\). Third, dually, if some point of \(B_q\) is sent to a minimal point \(c\in C_r\), then every point of \(A_p\) is sent to \(c\), while each point of \(B_q\) may be sent to any point of \(D_s\cup\{c\}\). Counting these disjoint cases gives the displayed total-map formula.

Consider a level-preserving map \(f=(\alpha,\beta)\) with both restrictions nonconstant. If \(g\ge f\), then each maximal-level value of \(g\) must equal the corresponding value of \(\beta\), because points of \(D_s\) are maximal. If some lower-level value of \(g\) entered \(D_s\), it would have to be below every value of the nonconstant map \(\beta\), which is impossible in the antichain \(D_s\). Hence \(g=f\). The dual argument gives \(g=f\) whenever \(g\le f\). Thus these maps are isolated. There are exactly \((r^p-r)(s^q-s)\) of them.

Every other map is comparable to a constant map. If a level-preserving map has \(\alpha\) constant at \(c\in C_r\), then \(\operatorname{const}_c\le f\); if \(\beta\) is constant at \(d\in D_s\), then \(f\le\operatorname{const}_d\). The two off-level forms above satisfy the corresponding comparison as well. The constant maps form a copy of \(P_{r,s}\), which is connected because every \(c\in C_r\) is below every \(d\in D_s\). Hence all nonisolated maps lie in one component \(K\), and no isolated map lies in it.

It remains to identify the topology of \(K\). Let \(i:P_{r,s}\to K\) send a point to the corresponding constant map. Define \(\rho:K\to P_{r,s}\) by
\[
\rho(f)=
\begin{cases}
c,&f(A_p)=\{c\}\text{ for some }c\in C_r,\\
d,&\text{otherwise},
\end{cases}
\]
where in the second case the classification above and membership in \(K\) imply \(f(B_q)=\{d\}\) for a unique \(d\in D_s\). Plainly \(\rho i=\operatorname{id}\).

The map \(\rho\) is order preserving. If \(f\le g\) and \(\rho(f)=d\in D_s\), then \(f(B_q)=\{d\}\), so maximality forces \(g(B_q)=\{d\}\); moreover \(g(A_p)\) cannot be a singleton in \(C_r\), hence \(\rho(g)=d\). If \(\rho(f)=c\in C_r\), then either \(\rho(g)=c\) or \(\rho(g)\in D_s\), in both cases \(\rho(f)\le\rho(g)\).

For each \(f\in K\), either \(i\rho(f)\le f\) when \(\rho(f)\in C_r\), or \(f\le i\rho(f)\) when \(\rho(f)\in D_s\). More strongly, if \(f_0<\cdots<f_t\) is any chain in \(K\), then the union of that chain with \(i\rho(f_0),\ldots,i\rho(f_t)\) is again a chain. Indeed the order-preserving sequence \(\rho(f_j)\) is either constant in one target level or changes once from a single \(c\in C_r\) to a single \(d\in D_s\); comparability across the change forces \(\operatorname{const}_c\le f_j\le\operatorname{const}_d\) for the relevant terms. Thus the simplicial maps induced by \(\operatorname{id}_K\) and \(i\rho\) are contiguous on every simplex, and the contiguity is relative to \(i(P_{r,s})\). Their realizations give a strong deformation retraction of \(|\mathcal K(K)|\) onto \(|\mathcal K(P_{r,s})|\).

Finally, \(P_{r,s}\) has order complex the complete bipartite graph \(K_{r,s}\), whose first Betti number is \(rs-r-s+1=(r-1)(s-1)\). The formula for homotopy classes follows from the standard finite-space correspondence between homotopy classes and connected components of the pointwise map space.

## Verification
The included `verify.py` independently enumerates all monotone maps for five parameter tuples, checks the total-map formula, isolates exactly the predicted maps, computes the comparability components, verifies the retraction \(\rho\) on the main component, and checks the pairwise chain condition needed for contiguity on every comparable pair. The replay output ends in `VERIFY_OK`.

The checked tuples are \((2,2,2,2)\), \((2,2,2,3)\), \((2,3,2,2)\), \((2,3,3,2)\), and \((3,2,2,3)\). Their total-map counts are respectively \(36,65,80,143,143\), and their component counts are \(5,13,13,37,37\). These finite checks support the symbolic proof but are not used to infer the universal statement.

## Relationship to prior work
Barmak and Minian identify finite \(T_0\)-spaces with finite posets and develop minimal finite graph models; their first public arXiv version is dated 2006-11-06 and lists MSC 55P10 and 55P15. Stong's mapping-space results, as recorded by May, identify homotopy classes with components of the appropriate finite function space and provide the general comparable-map framework. Speed studies the same componentwise-ordered poset \(\operatorname{Hom}(P,Q)\) for arbitrary finite posets, but the inspected paper computes its Möbius function rather than the component topology treated here.

A previous result for the self-map case \(P_{p,q}\to P_{p,q}\) already gives the corresponding component count in its stated range. That special case is not counted as new here. The present statement allows independent source and target parameters and, more importantly, determines the homotopy type of the unique nonisolated component via an explicit target-valued retraction.

## Limitations
The theorem does not classify map spaces for arbitrary height-two posets with missing comparabilities, for weak orders of larger height, or for parameters below the stated range. It determines the order-complex homotopy type of the nonisolated component, not its complete finite-poset isomorphism type. The literature search cannot exclude an unindexed or differently phrased earlier computation of this exact family; the closest inspected Hom-poset and finite-space mapping-space sources did not state it.

## References
1. J. A. Barmak and E. G. Minian, *Minimal Finite Models*, arXiv:math/0611156v1, first submitted 2006-11-06.
2. T. P. Speed, *On the Möbius function of Hom(P,Q)*, Bulletin of the Australian Mathematical Society 29 (1984), 39-46, DOI:10.1017/S0004972700021250.
3. J. P. May, *Finite Spaces and Simplicial Complexes*, Section 7, recording Stong's mapping-space results.

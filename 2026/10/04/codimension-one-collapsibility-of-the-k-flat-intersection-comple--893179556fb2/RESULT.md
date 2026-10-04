# Codimension-one collapsibility of the \(k\)-flat intersection complex

## Finding

For every integer \(d\ge 1\) and every finite family \(\mathcal F\) of closed convex subsets of \(\mathbb R^d\), each containing an affine hyperplane, the hyperplane-intersection complex \(N_{d-1}(\mathcal F)\) is \(1\)-collapsible. More precisely, after separating the universal vertices \(F=\mathbb R^d\), every proper member is a generalized closed slab perpendicular to a unique normal line; no face can contain proper members with two different normal lines; and each fixed-normal block is the ordinary nerve of closed intervals, which admits an explicit vertex-by-vertex \(1\)-collapse order.

This settles the codimension-one case \(k=d-1\) of the collapsibility question posed for the complexes \(N_k(\mathcal F)\) in Ludwigson--Soberón, arXiv:2608.27189v1.

## Assumptions and scope

Let \(d\ge 1\). The family \(\mathcal F\) is finite, and every \(F\in\mathcal F\) is a closed convex subset of \(\mathbb R^d\) containing at least one affine hyperplane. A face of \(N_{d-1}(\mathcal F)\) is a subfamily whose intersection contains an affine hyperplane.

A generalized closed slab means the inverse image of a nonempty proper closed interval of the extended line under a nonzero linear functional. Thus hyperplanes, ordinary slabs, and closed half-spaces are included.

## Proof

First classify a single proper member. Let \(F\subsetneq\mathbb R^d\) be closed and convex and suppose that it contains an affine hyperplane \(H=a+V\), where \(V\) has dimension \(d-1\). For every \(x\in F\) and \(v\in V\), choose \(t\in(0,1)\) and set \(h_t=a+v/t\in H\). Convexity gives
\[
(1-t)x+t h_t=x+v+t(a-x)\in F.
\]
Letting \(t\downarrow 0\) and using closedness gives \(x+v\in F\). Replacing \(v\) by \(-v\) shows \(F+V=F\).

Choose a nonzero linear functional \(\varphi\) with kernel \(V\). Since \(F\) is \(V\)-invariant,
\[
F=\varphi^{-1}(I)
\]
for \(I=\varphi(F)\). The same invariance lets one choose representatives on a fixed transverse line, so closedness and convexity of \(F\) imply that \(I\) is a nonempty closed interval in the extended line. Because \(F\neq\mathbb R^d\), \(I\neq\mathbb R\). Hence \(F\) is a generalized closed slab.

The direction \(V\) is unique for a proper \(F\). Indeed, if \(F\) contained hyperplanes with two distinct direction spaces \(V\) and \(W\), the argument above would give invariance under both \(V\) and \(W\). Since two distinct hyperplanes through the origin span \(\mathbb R^d\), \(F\) would be invariant under all translations and therefore equal \(\mathbb R^d\), a contradiction.

Now split the proper members of \(\mathcal F\) into classes according to this unique direction \(V\), and let \(U\) be the subfamily of universal members \(F=\mathbb R^d\). If a subfamily contains proper members with two distinct directions, its intersection cannot contain a hyperplane: a hyperplane contained in a proper generalized slab must be parallel to that slab. Thus every nontrivial face outside \(U\) lies in a single direction class.

Fix one direction class \(C\), choose \(\varphi\) with kernel \(V\), and write each \(F\in C\) as \(F=\varphi^{-1}(I_F)\) for a closed interval \(I_F\). For a subfamily \(\mathcal A\subseteq C\),
\[
\bigcap_{F\in\mathcal A}F
=
\varphi^{-1}\!\left(\bigcap_{F\in\mathcal A}I_F\right).
\]
Therefore \(\mathcal A\) is a face of \(N_{d-1}(\mathcal F)\) exactly when the intervals \(I_F\) have nonempty intersection. So the induced complex on \(C\) is the ordinary nerve of a finite interval family.

It remains to give an explicit \(1\)-collapse order for an interval nerve. If some remaining interval has finite right endpoint, choose one \(I\) with minimal right endpoint \(r\). Every remaining interval that intersects \(I\) contains \(r\): its left endpoint is at most \(r\), while minimality gives its right endpoint at least \(r\). Hence all vertices adjacent to \(I\) form, together with \(I\), one face; equivalently, \(I\) lies in a unique maximal face. Deleting \(I\) is therefore an elementary \(1\)-collapse. If no remaining interval has finite right endpoint, all remaining intervals are right-unbounded and have a common point, so the remaining block is a simplex and any vertex is \(1\)-collapsible.

Apply this deletion independently in every direction class. Universal vertices in \(U\) belong to every face extension, so they are simply included in the unique maximal face containing each deleted block vertex and do not spoil freeness. After all proper vertices are removed, the simplex on \(U\) is removed vertex by vertex. This reduces \(N_{d-1}(\mathcal F)\) to the empty complex by elementary \(1\)-collapses.

## Verification

The proof is symbolic and uses no finite experiment. The two points most vulnerable to hidden assumptions were checked directly: closedness is used exactly when passing \(x+v+t(a-x)\to x+v\), and the unbounded-interval case is handled separately rather than treating \(+\infty\) as an ordinary point.

The definition of \(1\)-collapsibility used here is the standard one: a vertex is removable when it is contained in a unique maximal face. Matoušek--Tancer, arXiv:0803.3520v1, gives the same definition and records the classical implication from representable nerves to collapsibility.

## Relationship to prior work

Ludwigson--Soberón, arXiv:2608.27189v1, define \(N_k(\mathcal F)\), ask whether it is \((d-k)\)-collapsible, and state that the general question is open; they note that such collapsibility would strengthen their fractional and selection-structure results. Their paper does not discuss the specialization \(k=d-1\), slabs, interval nerves, or a codimension-one collapse argument.

A targeted search of published-finding corpus and the public web for the combinations “\(N_k(\mathcal F)\) collapsible”, “codimension one De Santis”, “hyperplane-containing convex sets slabs interval nerve”, and “\(1\)-collapsible interval nerve” found no source stating this codimension-one theorem. The closest literature located was the general open problem above and standard background on collapsibility of ordinary nerves.

## Limitations

This argument is specific to codimension one. The classification by a unique normal line fails for lower-dimensional \(k\)-flats, where a proper convex set can contain many nonparallel \(k\)-flats without being all of \(\mathbb R^d\). Accordingly, the proof gives no direct progress on \(2\)- or higher-codimensional cases.

The literature search was targeted rather than exhaustive across every historical terminology for affine-flat intersection complexes. The result should therefore be read as a proved theorem with a residual bibliographic novelty risk, not as a claim that every possible older source has been ruled out.

## References

1. Sarah Ludwigson and Pablo Soberón, “Helly and Radon theorems for convex intersections containing \(k\)-flats,” arXiv:2608.27189v1, first posted 27 August 2026.
2. Jiří Matoušek and Martin Tancer, “On the gap between representability and collapsibility,” arXiv:0803.3520v1, first posted 25 March 2008.

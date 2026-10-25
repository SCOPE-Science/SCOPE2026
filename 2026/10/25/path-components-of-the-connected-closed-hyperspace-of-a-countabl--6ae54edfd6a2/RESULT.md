# Path components of the connected-closed hyperspace of a countable metric star

## Finding

Let \(S=\bigvee_{i\in\mathbb N}[0,\infty)_i\) be the countable star formed by identifying all ray origins to a point \(o\), with the path metric. Let \(\mathcal C(S)\) be the space of all nonempty closed connected subsets of \(S\), equipped with the extended Hausdorff distance, which is allowed to equal \(\infty\). The connected components of \(\mathcal C(S)\) coincide with its path-connected components and are exactly the equivalence classes for \(A\sim B\) if and only if \(d_H(A,B)<\infty\). For sets containing \(o\), write

\[
A(a)=\bigcup_{i\in\mathbb N}[0,a_i]_i,\qquad a=(a_i)_{i\in\mathbb N}\in[0,\infty]^{\mathbb N},
\]

where \([0,\infty]_i\) denotes the entire \(i\)-th ray. Then \(A(a)\) and \(A(b)\) lie in the same component exactly when their infinite-coordinate sets agree and their finite endpoint profiles differ by a bounded amount:

\[
\{i:a_i=\infty\}=\{i:b_i=\infty\},\qquad \sup_{i:a_i<\infty}|a_i-b_i|<\infty.
\]

There are exactly \(2^{\aleph_0}\) components. In particular, continuum many distinct components already occur among profiles with every coordinate finite, so component structure is not determined solely by which individual rays are unbounded.

## Assumptions and scope

The base space has countably infinitely many rays attached at one common origin, each ray parametrized by \([0,\infty)\) with unit speed. The topology on \(\mathcal C(S)\) comes from the extended Hausdorff distance

\[
d_H(A,B)=\max\{\sup_{x\in A}d(x,B),\sup_{y\in B}d(y,A)\}\in[0,\infty].
\]

Only nonempty closed connected subsets are included; they may be unbounded. This is not the Vietoris topology and is not the hyperspace restricted to compact subsets. The result is specific to the countable star and does not assert a classification for arbitrary infinite trees or for sets with more than one connected component.

## Proof

**1. Classification of the underlying closed connected sets.** If \(A\in\mathcal C(S)\) contains \(o\), then its intersection with each ray is an initial closed interval \([0,a_i]_i\), where \(a_i\in[0,\infty]\). Indeed, connectedness in a tree forces the arc from \(o\) to any point of \(A\) to lie in \(A\), and closedness makes each endpoint interval closed. Conversely, every such profile defines a closed connected subset: a convergent sequence that visits infinitely many different rays can converge only to \(o\), which belongs to the subset. If \(A\) does not contain \(o\), connectedness forces it to lie in a single ray; closedness then makes it either a bounded interval \([u,v]\), with \(0<u\le v<\infty\), or a tail \([u,\infty)\), with \(u>0\).

**2. Hausdorff distance between profiles.** For two origin-containing sets, the path metric gives

\[
d_H(A(a),A(b))=\sup_{i\in\mathbb N}|a_i-b_i|,
\]

with the convention that \(|\infty-c|=\infty\) for finite \(c\), and \(|\infty-\infty|=0\). Hence the distance is finite exactly when the infinite-coordinate sets agree and the finite-coordinate differences are uniformly bounded.

**3. A finite-distance class cannot be crossed by a path.** The relation \(A\sim B\iff d_H(A,B)<\infty\) is an equivalence relation by the extended triangle inequality. Each equivalence class is open: a finite-radius Hausdorff ball about any of its members stays in that class. Its complement is a union of other such open classes, so every class is also closed. A connected path image cannot meet two distinct classes. Therefore each path component lies in one finite-distance class.

**4. Every finite-distance class is path-connected.** If profiles \(a,b\) have finite Hausdorff distance, their infinite coordinates agree. Keep those coordinates equal to \(\infty\), and linearly interpolate every finite coordinate, setting \(a_i(t)=(1-t)a_i+tb_i\). The resulting profile path satisfies

\[
d_H(A(a(s)),A(a(t)))=|s-t|\sup_{i:a_i<\infty}|a_i-b_i|,
\]

so it is continuous. Every other member of \(\mathcal C(S)\) is at finite Hausdorff distance from a profile: a bounded interval can be contracted linearly to \(\{o\}\), and a tail \([u,\infty)\) on ray \(i\) can be moved continuously to the full ray \([0,\infty)_i\). These paths remain connected and closed throughout. Thus every finite-distance class is path-connected. Since the classes are clopen, they are exactly the connected components as well.

**5. Exact number of components.** The space \(S\) is second-countable, so it has at most continuum many closed subsets and hence at most \(2^{\aleph_0}\) components. For each real \(r\in[0,1]\), consider the profile \(a^{(r)}_i=ri\). Every coordinate is finite. If \(r\ne s\), then \(\sup_i|ri-si|=\infty\), so these profiles lie in distinct components. There are continuum many such parameters, giving the matching lower bound.

## Verification

The proof is direct and uses no finite enumeration or numerical experiment. The key distance formula follows ray-by-ray from the path metric. The path constructions are explicit and remain inside \(\mathcal C(S)\). The profiles \(a_i=ri\) provide a family of pairwise distinct components, while second-countability supplies the upper bound. As a boundary check, with only finitely many rays every finite endpoint-profile difference is automatically bounded, and the classification reduces to the familiar finite set of unbounded-direction choices.

## Relationship to prior work

Norah Esty's *The Hyperspaces \(C_n(X)\) for finite ray-graphs* proves that for a finite connected ray-graph with \(k\) rays, the Hausdorff hyperspace \(C_n(X)\) has exactly \(2^k\) path-connected components, classified by unbounded ray directions. That result is the motivating finite-ray case, but it does not cover a countably infinite star, where endpoint lengths can grow without any single ray being unbounded. R. Cauty's theorem on Hausdorff hyperspaces concerns all nonempty closed subsets of a connected proper geodesic metric space; the countable star is not proper, and the present space is the subspace of connected closed subsets. D. W. Curtis's work on noncompact hyperspaces studies compact-subset hyperspaces and does not classify the unbounded closed connected subsets considered here.

## Limitations

The theorem does not classify components of the full hyperspace of all closed subsets, does not extend the result to arbitrary countable metric trees, and does not address \(C_n(S)\) for \(n\ge2\). The metric star is not locally compact at \(o\): points at distance \(1/2\) from \(o\) on distinct rays form an infinite uniformly separated set in a bounded ball. Literature searches found no exact prior statement of the profile classification, but the search was not exhaustive; independent mathematical review remains necessary.

## References

1. N. Esty, “The Hyperspaces \(C_n(X)\) for finite ray-graphs,” arXiv:1012.1578, first publicly posted 2010-12-07. https://arxiv.org/abs/1012.1578
2. R. Cauty, “On non-separable components of hyperspaces with the Hausdorff metric,” *Matematychni Studii* 35 (2011), 91–105. https://doi.org/10.30970/ms.35.1.91-105
3. D. W. Curtis, “Hyperspaces of noncompact metric spaces,” *Compositio Mathematica* 40 (1980), 139–152. https://www.numdam.org/item/CM_1980__40_2_139_0/

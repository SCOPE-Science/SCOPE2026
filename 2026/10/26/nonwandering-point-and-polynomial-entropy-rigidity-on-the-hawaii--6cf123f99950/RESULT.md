# Nonwandering-point and polynomial-entropy rigidity on the Hawaiian earring

## Finding
Let the **Hawaiian earring** be the compact planar continuum
\[
H=\bigcup_{m=1}^{\infty} C_m,\qquad
C_m=\bigl\{(u,v)\in\mathbb R^2:(u-1/m)^2+v^2=1/m^2\bigr\},
\]
whose circles meet only at the origin \(o=(0,0)\). For every homeomorphism \(T:H\to H\),
\[
\boxed{\Omega(T)=\operatorname{Per}(T).}
\]
Moreover, the following are equivalent:

1. \(T\) has no wandering points.
2. Every point of \(H\) is periodic under \(T\).
3. The iterates \(\{T^j:j\in\mathbb Z\}\) are equicontinuous.
4. \(h_{\mathrm{pol}}(T)=0\).

In every other case \(h_{\mathrm{pol}}(T)=1\). Thus the complete polynomial-entropy spectrum of homeomorphisms of \(H\) is \(\{0,1\}\), both values being realized.

There is also an explicit *petal-cycle criterion*: each homeomorphism fixes \(o\) and permutes the circles \(C_m\). Write this permutation as \(\sigma\). The zero-entropy case occurs precisely if every \(\sigma\)-orbit is finite and, on a cycle of length \(q\), the circle return map \(g=T^q|_{C_m}\) has \(g=\mathrm{id}\) when orientation preserving, or \(g^2=\mathrm{id}\) when orientation reversing. In the latter case the return is an involution fixing \(o\).

## Assumptions and scope
The underlying metric is the ordinary Euclidean subspace metric. A point is *wandering* if it has a neighborhood \(U\) with \(T^n(U)\cap U=\varnothing\) for every positive integer \(n\). The nonwandering set \(\Omega(T)\) is its complement. The periodic-point set is \(\operatorname{Per}(T)=\{x:\exists n\ge1,\ T^nx=x\}\). Equicontinuity is required for all integer iterates. Polynomial entropy is defined from the Bowen metrics
\[
d_N(x,y)=\max_{0\le j<N}d(T^jx,T^jy),\qquad
h_{\mathrm{pol}}(T)=\lim_{\varepsilon\downarrow0}\limsup_{N\to\infty}
\frac{\log\operatorname{sep}(N,\varepsilon)}{\log N}.
\]
Here \(\operatorname{sep}(N,\varepsilon)\) is the maximal cardinality of a subset with pairwise Bowen distance at least \(\varepsilon\).

The continuum \(H\) is a regular curve: sufficiently small Euclidean-ball neighborhoods have finite boundary relative to \(H\), because all sufficiently small circles are contained in the ball and only finitely many large circles intersect its boundary. It is **not** a local dendrite: every neighborhood of \(o\) contains an entire simple closed curve. Therefore the known local-dendrite entropy dichotomy does not directly apply.

## Proof
**1. The circle permutation.** The origin \(o\) is the unique cut point of \(H\): deleting it leaves the infinitely many connected components \(C_m\setminus\{o\}\), whereas deleting any other point leaves a connected space (the punctured circle still connects through \(o\) to every other circle). Hence \(T(o)=o\). A homeomorphism permutes the connected components of \(H\setminus\{o\}\), and so determines a permutation \(\sigma\) of the circles. The restriction of every iterate to a return circle is a circle homeomorphism fixing \(o\).

**2. Nonperiodic points on infinite petal cycles wander.** Suppose \(x\ne o\) lies on a petal whose \(\sigma\)-orbit is infinite. Since its petal minus \(o\) is open in \(H\setminus\{o\}\), choose a small open arc \(U\ni x\) contained in that petal and avoiding \(o\). Every positive iterate of \(U\) lies in a different petal. Hence \(U\) is wandering.

**3. Nonperiodic points on finite petal cycles wander.** Suppose the petal of \(x\) has cycle length \(q\ge1\), and put \(g=T^q|_{C_m}\). The homeomorphism \(g\) fixes \(o\). If it preserves orientation, cut the circle at \(o\) to obtain an increasing homeomorphism of an interval fixing its endpoints. For any nonfixed point, one has strict monotone drift on the connected component of the complement of the fixed-point set. A sufficiently short fundamental subinterval gives a wandering open arc. Such a point cannot have any period, since an increasing interval homeomorphism has no periods other than one.

If \(g\) reverses orientation, it has two fixed points and interchanges the two open arcs bounded by them. Then \(g^2\) is increasing on either arc. Every point not fixed by \(g^2\) has a small open neighborhood wandering under \(g^2\), by the same monotone-drift argument. All odd iterates of this neighborhood lie in the other arc and so are disjoint from it. Thus it is wandering under \(g\). Finally, a neighborhood inside the original petal cannot meet its images under powers of \(T\) not divisible by \(q\); therefore an arc wandering under \(g\) is wandering under \(T\). Consequently every nonperiodic point of \(H\) wanders, and all periodic points are nonwandering, proving \(\Omega(T)=\operatorname{Per}(T)\).

**4. Classification of pointwise periodic maps.** If all points are periodic, no circle can belong to an infinite \(\sigma\)-orbit. On each finite petal cycle the return homeomorphism \(g\) is pointwise periodic. If \(g\) preserves orientation, its interval model has only fixed periodic points, hence \(g=\mathrm{id}\). If it reverses orientation, \(g^2\) preserves orientation and is pointwise periodic, hence \(g^2=\mathrm{id}\). Conversely, if all petal cycles are finite and their returns satisfy these conditions, every point on each circle has period dividing \(2q\) under \(T\). This proves the stated petal criterion.

**5. Pointwise periodicity forces uniform equicontinuity.** Fix \(\varepsilon>0\), and choose \(M\) so that every petal \(C_m\), \(m>M\), has diameter less than \(\varepsilon/4\). Under pointwise periodicity, the union \(K\) of the finitely many complete \(\sigma\)-cycles meeting \(C_1,\ldots,C_M\) is a **finite** invariant union of circles. By step 4 there is an integer \(L\ge1\) such that \(T^L|_K=\mathrm{id}|_K\). Define a continuous retraction \(r:H\to K\) that is the identity on \(K\) and collapses every remaining petal to \(o\); it commutes with \(T\) because \(K\) and its complement are invariant and \(T(o)=o\). For all \(x\in H\) and \(j\in\mathbb Z\),
\[
d(T^jx,T^jr(x))<\varepsilon/4,
\]
since every omitted petal has diameter less than \(\varepsilon/4\). The finitely many maps \(T^0|_K,\ldots,T^{L-1}|_K\) are uniformly equicontinuous on compact \(K\). Uniform continuity of \(r\), plus the triangle inequality and the estimate above, yields a common \(\delta>0\) for all \(T^j\), \(j\in\mathbb Z\). Thus \(T\) is equicontinuous.

Conversely, an equicontinuous compact homeomorphism has no wandering points. Indeed, the compatible metric \(d_*(x,y)=\sup_{j\in\mathbb Z}d(T^jx,T^jy)\) makes \(T\) an isometry and is compact; any orbit has arbitrarily close two forward terms, so a positive difference of their indices returns the initial point arbitrarily close to itself in \(d_*\). Each point is recurrent, hence none wanders. Step 3 then forces all points to be periodic.

**6. Polynomial entropy.** Equicontinuity makes \(\operatorname{sep}(N,\varepsilon)\) bounded uniformly in \(N\) for each fixed \(\varepsilon>0\); hence polynomial entropy is zero. If \(T\) has a wandering point, then polynomial entropy is at least one: for a wandering neighborhood \(U\) of \(x\), choose \(\varepsilon>0\) such that \(B(x,\varepsilon)\subset U\). The \(N\) points \(T^{-i}x\), \(0\le i<N\), are pairwise \((N,\varepsilon)\)-separated by comparing their forward images at an appropriate time. For the matching upper bound we use Đorić and Katić's theorem that **every homeomorphism of any regular curve** has polynomial entropy at most one (arXiv:2602.19256v1, Corollary 4). Hence every map with a wandering point has polynomial entropy exactly one. Together with steps 3–5, this proves all equivalences.

**7. Both values occur.** The identity map on \(H\) has polynomial entropy zero. For polynomial entropy one, choose any nonidentity orientation-preserving circle homeomorphism fixing \(o\) on \(C_1\), and set \(T\) to the identity on all other petals. This pastes to a homeomorphism of \(H\). Nonfixed points on \(C_1\) wander, so step 6 gives entropy one.

## Verification
The proof uses no numerical approximation, infinite enumeration, or computer-dependent lemma. The critical complete cases are: finite versus infinite circle permutation orbits; orientation-preserving versus orientation-reversing circle returns; every integer iterate in the equicontinuity estimate; and both entropy boundary values. In step 5 the invariant finite core includes **whole permutation cycles**, not just the finitely many geometrically large circles, ensuring the collapse retraction commutes with every iterate. The analytic proof verifies all these cases directly. Independent validation has not been performed.

## Relationship to prior work
Đorić and Katić (2026, arXiv:2602.19256v1) establish the universal regular-curve upper bound and the entropy-one criterion for a wandering point, and prove a zero–one dichotomy on **local dendrites**. Their closing Question 1 concerns **regular curves that are not local dendrites**. The theorem here supplies the exact classification on the canonical Hawaiian earring, which is outside their local-dendrite hypothesis, but does **not** resolve their general existence question for other regular curves.

Naghmouchi (2018 preprint; 2020 journal) proves that the nonwandering set equals the recurrent set for every regular-curve homeomorphism; the present stronger conclusion that it consists only of periodic points depends on the shrinking-petal geometry. Roth, Roth and Snoha (2021 preprint; 2024 journal) discuss nonzero polynomial entropy on countable disjoint circle-rotation bundles. That mechanism uses circles with persistent macroscopic size and is not available when petal diameters converge to zero and all petals meet at a fixed cut point. Marinho, de Paula and de Souza discuss properly discontinuous homeomorphisms of the Hawaiian earring in the setting of **generalized entropy**, but do not classify all its homeomorphisms by ordinary polynomial entropy. A 2026 flexibility paper by Đorić, Katić and Perić constructs pointwise-periodic homeomorphisms with positive polynomial entropy on different continua; its full text could not be inspected, so that comparison carries bibliographic risk.

## Limitations
The result applies to homeomorphisms, not arbitrary continuous self-maps, and to the shrinking-petal Hawaiian earring, not arbitrary infinite graph wedges, general non-local-dendrite regular curves, or inverse limits. It uses the published general upper bound on polynomial entropy. The priority assessment is based on the accessible primary texts and the source comparisons stated above; a yet-unidentified equivalent result remains possible. No claim of independent audit is made.

## References
1. M. Đorić and J. Katić, *Polynomial entropy on regular curves*, arXiv:2602.19256v1 (first posted 2026-02-22), https://arxiv.org/html/2602.19256v1 .
2. I. Naghmouchi, *Dynamics of homeomorphisms of regular curves*, arXiv:1807.00222 (2018); *Colloquium Mathematicum* 162 (2020), 263–277, DOI:10.4064/cm7825-9-2019.
3. S. Roth, Z. Roth and Ľ. Snoha, *Rigidity and Flexibility of Polynomial Entropy*, arXiv:2107.13695v1 (2021); *Advances in Mathematics* 443 (2024), 109591.
4. M. Đorić, J. Katić and M. Perić, *A flexibility result for polynomial entropy of pointwise periodic homeomorphisms*, arXiv:2606.28283v1 (first posted 2026-06-26). Full-text comparison not completed.
5. F. Marinho, H. de Paula and L. H. R. de Souza, *Entropy for generalized parabolic dynamics*, DOI:10.3934/dcds.2026019 (2025/2026), Section 6.3.

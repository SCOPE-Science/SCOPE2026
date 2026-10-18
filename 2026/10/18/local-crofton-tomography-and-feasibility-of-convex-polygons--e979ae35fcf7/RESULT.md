# Local Crofton tomography and feasibility of convex polygons

## Finding

Let \(P\) be a strictly convex Euclidean polygon with \(n\ge3\) genuine vertices \(v_0,\ldots,v_{n-1}\) in cyclic order, and sides \(e_i=[v_i,v_{i+1}]\), where indices are cyclic. Sample an **unoriented affine line** from Euclidean-motion-invariant measure \(d\varphi\,dt\), with \(0\le\varphi<\pi\), conditioned on intersecting \(P\). Record only the labeled one-side probabilities \(m_i=\Pr(\ell\cap e_i\ne\varnothing)\) and the labeled **adjacent-side joint probabilities** \(q_i=\Pr(\ell\cap e_i\ne\varnothing,\ \ell\cap e_{i+1}\ne\varnothing)\). Intersections through vertices have measure zero.

**Inverse theorem.** These \(2n\) local probabilities determine \(P\) up to similarity, including a possible reflection. In fact, writing \(L=\operatorname{per}(P)\), all side lengths and two-step vertex distances divided by \(L\) are
\[
 a_i:=\frac{\lVert v_{i+1}-v_i\rVert}{L}=\frac{m_i}{2},\qquad
 b_i:=\frac{\lVert v_{i+2}-v_i\rVert}{L}=\frac{m_i+m_{i+1}}{2}-q_i.
\]
Consequently, the interior angle at \(v_{i+1}\) is reconstructed by
\[
 \theta_{i+1}=\arccos\left(\frac{a_i^2+a_{i+1}^2-b_i^2}{2a_i a_{i+1}}\right).
\]
Starting from one side, the ordered side lengths and positive external turns \(\pi-\theta_i\) reconstruct all vertices.

**Exact feasibility criterion.** Conversely, two cyclic real arrays \((m_i)\) and \((q_i)\) arise from a strictly convex polygon if and only if all the following hold:

1. \(m_i>0\) for every \(i\) and \(\sum_i m_i=2\).
2. With \(a_i=m_i/2\) and \(b_i=a_i+a_{i+1}-q_i\), one has \(|a_i-a_{i+1}|<b_i<a_i+a_{i+1}\) for every \(i\). Put \(\gamma_{i+1}=\pi-\arccos((a_i^2+a_{i+1}^2-b_i^2)/(2a_i a_{i+1}))\).
3. The turns satisfy \(\sum_{j=1}^{n}\gamma_j=2\pi\). Setting \(\phi_0=0\) and \(\phi_k=\sum_{j=1}^{k}\gamma_j\) for \(1\le k<n\), the complex closure equation holds:
\[
 \sum_{i=0}^{n-1}a_i e^{\mathrm i\phi_i}=0.
\]

On any family whose normalized side lengths are bounded away from zero and whose interior angles are bounded away from \(0\) and \(\pi\), this inverse is locally Lipschitz for normalized vertex-pair distances. In the **equilateral** subclass, \(m_i=2/n\), so the \(n\) adjacent-side probabilities \((q_i)\) alone determine the polygon up to similarity.

## Assumptions and scope

Strict convexity here means that every interior angle lies strictly between \(0\) and \(\pi\), all side lengths are positive, and the labeled vertices occur in their given cyclic order. There is no restriction to regular or centrally symmetric polygons. The line distribution is the motion-invariant Crofton model, **not** sampling a random pair of uniform interior points or choosing independent uniform boundary endpoints. The data are labeled by physical side index; no statement of uniqueness is made for unlabeled statistics. The inverse recovers the shape, not the absolute perimeter, because conditional line probabilities are scale-invariant.

## Proof

**1. Normalization of line measure.** For \(0\le\varphi<\pi\), write \(n_\varphi=(\cos\varphi,\sin\varphi)\), and represent a line as \(\{x:n_\varphi\cdot x=t\}\). At fixed \(\varphi\), the offsets hitting a compact convex set form its projection interval. Cauchy's perimeter formula therefore gives
\[
 \mu\{\ell:\ell\cap P\ne\varnothing\}
 =\int_0^\pi \operatorname{width}_P(n_\varphi)\,d\varphi=L.
\]
For a segment of length \(s\), its projected interval has length \(s|\cos(\varphi-\alpha)|\) in a suitable reference angle, so its total line-hit measure is \(2s\). Hence \(m_i=2\lVert v_{i+1}-v_i\rVert/L\), proving the first inverse formula and \(\sum_i m_i=2\).

**2. Joint measure for adjacent sides.** Take the two sides \([A,B]\) and \([B,C]\) of their nondegenerate triangle \(T=\operatorname{conv}\{A,B,C\}\). Apart from a null set of tangent/vertex lines, every line meeting \(T\) meets at least one of these two segments: it cannot meet only the remaining base twice. Conversely every line meeting either segment meets \(T\). Thus the union of their line-hit events has measure \(\operatorname{per}(T)=\lVert A-B\rVert+\lVert B-C\rVert+\lVert A-C\rVert\). Inclusion-exclusion and the segment formula yield
\[
 \mu\{\ell:\ell\cap[A,B]\ne\varnothing,\ \ell\cap[B,C]\ne\varnothing\}
 =\lVert A-B\rVert+\lVert B-C\rVert-\lVert A-C\rVert.
\]
Since the two segments are sides of \(P\), a line meeting both has its two polygon-boundary intersections there, almost surely. Divide by \(L\) to obtain \(q_i=a_i+a_{i+1}-b_i\). Strict triangle inequalities imply \(q_i>0\). The ordinary cosine law now recovers every interior angle.

**3. Uniqueness.** Normalize the perimeter to one and put the first side along the positive horizontal axis. The external turn at each vertex is \(\gamma_i=\pi-\theta_i\in(0,\pi)\). A strictly convex polygon traversed counterclockwise has these positive turns in the given order. Thus its side vectors are exactly
\[
 a_i(\cos\phi_i,\sin\phi_i),\qquad
 \phi_0=0,\quad \phi_k=\sum_{j=1}^k\gamma_j.
\]
Summing them from the initial vertex determines all vertices. The clockwise traversal produces the reflected copy. No other similarity class can share the data.

**4. Necessity and sufficiency of feasibility conditions.** Necessity follows from the first three steps, turning-number one, and closure of the boundary. For sufficiency, the strict triangle inequalities produce angles \(\gamma_i\in(0,\pi)\). The given sum-turn and closure conditions produce a closed polygonal chain with positive lengths and strictly increasing directed edge angles through one full turn. For any fixed edge, rotate coordinates until that edge points right. The vertical increments along subsequent edges are nonnegative until their directions pass the opposing horizontal direction, then nonpositive; the partial vertical sums start and end at zero. Every other vertex therefore lies strictly on the left side of the supporting line of the fixed edge. Repeating for each edge shows the chain is a strictly convex polygon with the prescribed cyclic order. Step 1 and Step 2 then reproduce exactly the input probabilities. Thus the stated conditions are sufficient as well as necessary.

**5. Stability and equilateral specialization.** On a compact nondegenerate family, the formulas for \(a_i\), \(b_i\) and \(\theta_i\) have bounded first derivatives: denominators are bounded below by the minimum normalized side length and the derivative of \(\arccos\) is bounded by the minimum sine of the interior angles. Finite summation of reconstructed edge vectors is therefore Lipschitz, which also controls all normalized pairwise vertex distances. If every side length is equal, its normalized value is \(1/n\), giving \(m_i=2/n\); the adjacent joint probabilities alone recover the two-step chords, hence all turns and the polygon.

## Verification

The package's standalone `verify.py` (Python standard library only) checks 21 strictly convex polygon configurations, with \(3,4,5,6,7,10,13\) sides and three irregular choices per size. It compares the formulas independently against numerical quadrature over unoriented line directions and reconstructs all normalized vertex distances and polygon closure. It also checks five regular examples and a perturbed locally admissible data set that fails global closure. The actual successful output is:

```text
ADJACENT_CROFTON_TOMOGRAPHY_OK polygon_cases=21 regular_cases=5 exact_distance_and_quadrature_checks=1162
```

The proof, not finite quadrature or a sample, establishes the result for every polygon in the stated domain. To reproduce: run `python verify.py` in the directory containing this file and the checker. No external packages, data files, or network are required.

## Relationship to prior work

The segment-hit normalization and Cauchy–Crofton perimeter formula are classical and are **not** claimed as new. Harutyunyan–Ohanyan (2009), Section 2, explicitly decomposes random chord distributions into events indexed by pairs of polygon sides; its main theorem evaluates chord-length distributions of regular polygons. Bäsel (2012), Sections 1–5, gives explicit random chord-length and point-distance laws for regular polygons. Neither inspected main result states that only one-edge marginals and **adjacent** two-edge probabilities reconstruct an arbitrary labeled strictly convex polygon, nor gives the stated global feasibility test.

Other polygon-identification theorems from random-chord **length** distributions, orientation-dependent chord functions/covariograms, or directional X-ray probes use different and generally richer observables. They do not, by themselves, imply that the present sparse, unoriented, side-indexed incidence data suffice. The elementary relation between these local incidences, two-step chords, and turning angles is the exact constructive distinction; no claim is made to invent the cosine law or perimeter formula.

## Limitations

The observables require the ordered side labels and the Crofton sampling convention. Without that label information, the inverse assertion is not established. Reflection cannot be distinguished. The local Lipschitz guarantee requires nondegeneracy bounds and is not a finite-sample statistical recovery theorem. Historical priority remains provisional, particularly regarding older combinatorial-integral-geometry treatments of side-pair incidence. The result does not claim identification of arbitrary smooth convex bodies from finitely many unmarked chord statistics.

## References

1. U. Bäsel, *Random chords and point distances in regular polygons*, arXiv:1204.2707, first posted 12 April 2012, https://arxiv.org/abs/1204.2707.
2. H. S. Harutyunyan and V. K. Ohanyan, *The chord length distribution function for regular polygons*, Advances in Applied Probability 41 (2009), 358–366, https://doi.org/10.1239/aap/1246886615.
3. J. Gates, *Recognition of triangles and quadrilaterals by chord length distribution*, Journal of Applied Probability 19 (1982), 873–879, https://doi.org/10.2307/3213843.
4. W. Nagel, *Orientation-dependent chord length distributions characterize convex polygons*, Journal of Applied Probability 30 (1993), 730–736, https://doi.org/10.2307/3214779.
5. H. Edelsbrunner and S. S. Skiena, *Probing convex polygons with X-rays*, SIAM Journal on Computing 17 (1988), 870–882, https://doi.org/10.1137/0217054.

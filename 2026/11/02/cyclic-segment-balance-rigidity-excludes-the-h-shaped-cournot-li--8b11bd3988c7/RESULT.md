# Cyclic segment-balance rigidity excludes the H-shaped Cournot limit

## Finding

**Theorem (finite axis-segment skeleton rigidity).** Fix an integer \(n\geq2\). For each \(i\in\{1,\ldots,n\}\), let \(f_i:[0,1]\to[0,1]\) be continuous, and define the cyclic coordinate map
\[
F(x_1,\ldots,x_n)=(f_n(x_n),f_1(x_1),\ldots,f_{n-1}(x_{n-1})).
\]
Let \(K\subseteq[0,1]^n\) be nonempty and compact, with \(F(K)=K\). Suppose that \(K\) is a finite union of nondegenerate closed line segments each parallel to a coordinate axis, together with finitely many singleton points. For every coordinate direction \(i\), let \(\mathcal S_i(K)\) denote the set of inclusion-maximal nondegenerate coordinate-axis-parallel segments in \(K\) with direction \(i\), and put \(N_i=|\mathcal S_i(K)|\). Then
\[
N_1=N_2=\cdots=N_n.
\]
More precisely, \(F\) maps every segment in \(\mathcal S_i(K)\) **onto** exactly one segment in \(\mathcal S_{i+1}(K)\), with cyclic indices, and the induced map \(\mathcal S_i(K)\to\mathcal S_{i+1}(K)\) is a bijection. Thus \(F\) permutes the finite set of maximal segments, every permutation cycle has length divisible by \(n\), and the induced permutation may be empty if \(K\) is finite.

**Corollary (the H-shape obstruction).** If \(f_1,f_2:[0,1]\to[0,1]\) are arbitrary continuous maps, the Cournot map \(F(x,y)=(f_2(y),f_1(x))\) has no point whose omega-limit set is
\[
H=(\{0,1\}\times[0,1])\cup([0,1]\times\{1/2\}).
\]
Indeed, \(H\) has exactly two maximal vertical segments and one maximal horizontal segment, contradicting the theorem. This resolves the explicit H-shaped-set question in García Guirao's 2026 paper without any periodic-coordinate, smoothness, nonsingularity, or metric-regularity assumption.

## Assumptions and scope

A nondegenerate coordinate segment is \(\{c_1\}\times\cdots\times\{c_{i-1}\}\times[a,b]\times\{c_{i+1}\}\times\cdots\times\{c_n\}\), with \(a<b\). Such a segment is inclusion-maximal if no strictly larger nondegenerate segment in \(K\) parallel to the same axis contains it. Since \(K\) is a finite union of axis segments and points, the maximal nondegenerate segments form a finite collection. Distinct maximal segments parallel to the same axis cannot meet unless they lie on different coordinate lines, in which case they are disjoint; on the same line, meeting segments would merge into a larger segment of \(K\). A singleton in the representation need not be isolated in the topology of \(K\); the proof only uses that there are finitely many residual points outside the maximal segments.

The hypothesis is **strong invariance** \(F(K)=K\), not merely forward invariance \(F(K)\subseteq K\). It is automatic for omega-limit sets of a continuous map on a compact space. The theorem does not assert that every skeleton satisfying the numerical equality is realizable as an omega-limit set.

## Proof

**1. Finite geometry.** Combine collinear intersecting segments in any finite representation of \(K\) until each nondegenerate remaining coordinate segment is inclusion-maximal. This is finite because there are finitely many input segments; no union of segments on differing axis lines creates a new nondegenerate straight axis segment except through an already represented collinear component. Let \(\mathcal S=\bigcup_{i=1}^n\mathcal S_i(K)\), and let \(E\subset K\) be the finite set of points of \(K\) not in any segment in \(\mathcal S\). Then \(K=E\cup\bigcup_{S\in\mathcal S}S\).

**2. Orientation of images.** Fix \(S\in\mathcal S_i(K)\). On \(S\), only the \(i\)-th coordinate varies. By the coordinate form of \(F\), only coordinate \(i+1\) of \(F(S)\) may vary (indices modulo \(n\)). By continuity, the image of the varying interval is an interval. Hence \(F(S)\) is either a point or a nondegenerate closed coordinate segment of direction \(i+1\), contained in \(K\). If it is nondegenerate, it lies in a unique member of \(\mathcal S_{i+1}(K)\): any two maximal collinear members containing a common nondegenerate interval would merge, contradicting maximality.

**3. Every target segment has a source of the preceding orientation.** Fix \(T\in\mathcal S_{i+1}(K)\). Since \(F(K)=K\), the segment \(T\) is covered by the finite family \(F(E)\) and \(F(S)\) as \(S\) ranges over all maximal segments. Every image of a source segment whose orientation is *not* \(i\) is either a point or a segment of direction different from that of \(T\); its intersection with \(T\) therefore has at most one point. The finite set \(F(E)\) also has only finitely many points of intersection with \(T\). A nondegenerate interval cannot be covered by finitely many points, so some source \(S\in\mathcal S_i(K)\) has a nondegenerate image contained in \(T\).

For a fixed source \(S\in\mathcal S_i(K)\), its image can be contained in **at most one** maximal segment of direction \(i+1\) when nondegenerate. Thus the relation above defines, for each target, at least one distinct source (choose one); in particular \(N_{i+1}\leq N_i\).

**4. Equality, permutation, and exact images.** Cyclically apply these inequalities:
\[
N_1\geq N_2\geq\cdots\geq N_n\geq N_1.
\]
All are equal. The map associating a source segment to the unique maximal target containing its nondegenerate image is now a bijection: every target is reached, and the domain and codomain are finite of the same size. No source segment can have collapsed image, because then fewer than \(N_i=N_{i+1}\) sources could cover the \(N_{i+1}\) targets.

We prove surjectivity **on each target segment**, not just on the finite segment labels. Let \(T\in\mathcal S_{i+1}(K)\), with unique source \(S\in\mathcal S_i(K)\) associated to it. The set \(F(S)\) is a closed interval contained in \(T\). Every image from a different source segment of orientation \(i\) is contained in a different maximal target segment and hence disjoint from \(T\) except possibly in an endpoint (indeed distinct maximal same-direction segments are disjoint). Every image from a source segment of another orientation meets \(T\) in at most one point, and \(F(E)\) is finite. If \(F(S)\) were a proper subinterval of \(T\), the nonempty relative open interval \(T\setminus F(S)\) would contain infinitely many points not covered by any of those finitely many exceptional intersections, contradicting \(K=F(K)\). Thus \(F(S)=T\).

The union of the direction-by-direction bijections is a permutation of \(\mathcal S\). Each application increments the direction modulo \(n\), so a permutation cycle returns to its original direction only after a multiple of \(n\) steps.

**5. Omega-limit sets.** If \(z\in[0,1]^n\) and \(K=\omega_F(z)\), continuity and compactness give \(F(K)=K\): forward inclusion follows by continuity of limits, and for every limit \(w=\lim_{k\to\infty}F^{m_k}(z)\) with \(m_k\to\infty\), a convergent subsequence of its predecessors \(F^{m_k-1}(z)\) has a limit \(u\in K\) satisfying \(F(u)=w\). Apply the theorem to such \(K\) when it has the stated finite segment structure.

**6. Direct H-shape check.** With \(I=[0,1]\), the two vertical bars of \(H\) have images \(f_2(I)\times\{f_1(0)\}\) and \(f_2(I)\times\{f_1(1)\}\), both horizontal (possibly points). The horizontal bar has image \(\{f_2(1/2)\}\times f_1(I)\), which is at most one vertical segment. Consequently \(F(H)\) has at most one nondegenerate vertical component, whereas \(H\) has two disjoint nondegenerate vertical bars. Therefore \(F(H)\neq H\) for all continuous \(f_1,f_2\), and \(H\) cannot be an omega-limit set.

## Verification

The logical checks are exact and require no floating-point computation. The principal potential failure points were checked separately: (i) the target coverage in step 3 explicitly excludes all transverse images, which meet a given segment in only finitely many points; (ii) cyclicity, not an independent count assumption, forces equality of all orientation counts; (iii) finiteness of the segment collection is essential in excluding coverage by infinitely many intersections; (iv) full target coverage in step 4 uses both strong invariance and the just-established uniqueness of the source orientation; and (v) the independently derived direct formula for \(F(H)\) reproduces the obstruction without requiring the general segment bookkeeping.

As a boundary example, for \(f_i=\mathrm{id}\) the union of the \(n\) coordinate-axis segments from the origin to the standard unit vectors is invariant and the segment permutation is one \(n\)-cycle. This confirms that the equality restriction and cycle divisibility can be attained for invariant skeletons; this identity-map example is **not** asserted to be an omega-limit set. Independently, the motivating source constructs realized lattice omega-limit sets with equal numbers of vertical and horizontal segments.

## Relationship to prior work

García Guirao, *Connected omega-limit sets of Cournot maps: periodic orbits, realization and almost every point*, arXiv:2610.27229v1 (public 19 October 2026), proves conditional lattice and comb classifications. Its Corollary D establishes segment-count balance when a coordinate composite has a finite omega-limit set; its Theorem E imposes a metric-regularity hypothesis for almost-everywhere assertions. Section 11, Problem 2, explicitly asks whether the H-shaped set can be an omega-limit set without those restrictions. The theorem above requires neither restriction and therefore rules out that shape globally. It also gives the cyclic-coordinate \(n\)-dimensional finite-skeleton statement, beyond the two-coordinate conditional classification. Source constructions establish that balanced lattices can occur; the present statement is a *necessary* invariant-set rigidity, not a replacement for the source's realization theorem.

Linero-Bas and Muñoz-Guillermo, *A Full Description of omega-Limit Sets of Cournot Maps Having Non-Empty Interior and Some Economic Applications*, Mathematics 9 (2021), 452, studies nonempty-interior omega limits and selected empty-interior examples including equal-cardinality lattices. Its inspected introduction and Section 5 do not state the general finite-skeleton necessary condition or settle the H obstruction for arbitrary continuous Cournot maps.

## Limitations

The result only applies when the invariant set is a **finite** union of straight axis-parallel segments plus finitely many points. It does not address infinitely many segments, curved graph pieces, fractal or Cantor fibers, sets containing two-dimensional rectangles, or the full connectedness conjecture for Cournot omega-limit sets. Equality of segment counts is necessary, not sufficient, for realization. No classification of all admissible segment permutations or dynamical stability is claimed. The proof is analytical; there is no independent mathematical audit. Historical priority outside the inspected sources cannot be ruled out by search absence alone.

## References

1. J. L. García Guirao, *Connected omega-limit sets of Cournot maps: periodic orbits, realization and almost every point*, arXiv:2610.27229v1, 19 October 2026. https://arxiv.org/html/2610.27229v1 . Relevant: Theorem C, Corollary D, Theorem E, Section 7, Section 8 and Section 11, Problems 2 and 5.
2. A. Linero-Bas and M. Muñoz-Guillermo, *A Full Description of omega-Limit Sets of Cournot Maps Having Non-Empty Interior and Some Economic Applications*, *Mathematics* **9** (2021), article 452, https://doi.org/10.3390/math9040452 . Relevant: introduction, Section 5 examples and concluding questions.

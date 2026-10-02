# A genus-zero one-descendant relative invariant of bidegree (3,4) equals 352

## Finding

For each fixed position \(p\), the connected relative stationary descendant invariant is \(352\).

| Fixed descendant position | Nonzero diagrams | Weighted invariant |
|---|---:|---:|
| 0 | 43 | 352 |
| 1 | 37 | 352 |
| 2 | 37 | 352 |
| 3 | 43 | 352 |

There are 160 nonzero diagrams when all four different descendant vectors are collected. Their total weight is \(1408=4\cdot352\), which is not the value of a single fixed descendant problem.

An exact stationary descendant coefficient is a reproducible benchmark for the Hirzebruch floor-diagram/Fock formalism. The fixed data below have four labeled stationary insertions and one psi power. Evaluating the actual relative vertex invariants is essential: a bare product of edge weights is not, in general, the required geometric multiplicity.

## Assumptions and scope

Let \(F_0=\mathbb P^1\times\mathbb P^1\), with class \(3B+4F\), genus zero, four labeled ordinary marks, ordered labeled fixed relative contacts \(\phi=(-2,-2,1,3)\), and no moving global contacts \(\mu=()\). Use the conventions of CJMR Notation 2.2 and Definitions 2.5, 4.1, 4.3, and 4.4. The descendant vector is \(k_p=1\) at a fixed position \(p\in\{0,1,2,3\}\), and \(k_i=0\) otherwise. All ordinary insertions are point classes; no line insertion is substituted. The dimension equation is \(0+2\cdot3+0-1=4+1=5\).

A connected floor diagram is an ordered tree on four vertices, with the four distinct relative labels attached to vertices, positive compact-edge weights, vertex sizes, and one thickened half per compact edge. Balance is signed compact-edge weight plus signed attached-contact weight equal to zero. For each vertex, the thick count is \(k_i+2-2s_i\). Nonnegative sizes sum to three, so exactly three sizes are one and one is zero. Diagram multiplicity is the product of compact-edge weights times the actual local one-point relative descendant invariants.

## Proof

### Exact partial-relative conventions

CJMR Definition 2.5 inserts a boundary point class at each fixed relative mark but none at a moving relative mark. Definition 4.3 makes normal flags fixed and thick flags moving. Definition 4.1(6)-(7) marks all global ends by their parts; our two equal negative contacts have distinct labels, with no division by permutations. All global ends are normal because \(\mu=()\), so thick flags come only from compact edges. Definition 4.4 multiplies compact-edge weights and the genuine local invariants without an additional labeling factorial.

For each local calculation set \(X=\mathbb P^1_t\times\mathbb P^1_u\), relative only to \(D=\mathbb P^1_t\times\{0,\infty\}\). This is CJMR's partial relative pair, not the fully toric logarithmic pair. The size \(a\) is the first degree. Normal relative marks fix generic coordinates \(t_i\); thick marks leave those coordinates free. The ordinary mark maps to \((t_0,u_0)\), with \(u_0\notin\{0,\infty\}\) and all fixed coordinates distinct from \(t_0\) and each other. Signed contact orders sum to zero.

### Comparison with the genuine virtual theory

Abramovich--Marcus--Wise (AMW), Definition 1.1.1 and Theorem 1.1.2, compare proper relative theories of a smooth pair with arbitrary fixed contact partitions by virtual pushforward. Corollary 1.1.3 and Section 2.3 include evaluations and descendants pulled from unexpanded stable maps. The disconnected divisor \(D\) is smooth because its components are disjoint. Orders 2,3,4 are allowed: no primitive-contact hypothesis is used.

On the stationary incidence locus the ordinary component cannot be contracted on collapsing an expansion, since contracted components map into \(D\) but the ordinary image is interior. Its cotangent line therefore agrees with the unexpanded-map cotangent line. AMW compares the actual relative descendant with the partial-pair logarithmic calculation below. No transverse base-boundary contacts are added; CJMR Remark 2.4 and a primitive fully toric descendant theorem are not needed.

For this pair,
\[
T_X(-\log D)=\mathcal O(2,0)\oplus\mathcal O.
\]
On every component of a genus-zero source tree these summands have degrees \(2a_j\ge0\) and zero. A line bundle of componentwise nonnegative degree on a rational tree has vanishing first cohomology: the normalization sequence and successive removal of leaves use surjectivity of evaluation at each leaf's attachment. Thus \(H^1(C,f^*T_X(-\log D))=0\). AMW Section 3.5 identifies this as the map deformation obstruction. The basic logarithmic map stack is logarithmically smooth of expected dimension, and its virtual class is its fundamental class.

Minimal saturated charts are toroidal, so their trivial-log open is dense in every component. The stack is proper and finite type for fixed data. For \(a=1\), the smooth first projection is an isomorphism: a map is determined by distinct labeled relative coordinates, the ordinary coordinate and one nonzero scale for its second projection. Prescribed zeros and poles determine that function. This open is irreducible and generically has no source automorphism. For \(a=0\), it is marked-source configuration times a fiber choice and a nonzero scale, also irreducible. Density proves irreducibility of the relevant full partial-pair stack.

### Incidence-cut virtual cycle, not merely ambient irreducibility

For \(a=1\), write \(N\) for the number of normal relative marks. There are also one thick mark and one ordinary mark. Expected dimension is \(N+3\), whereas the evaluation target \(Y=(\mathbb P^1)^N\times X\) has dimension \(N+2\). Every proper boundary stratum has dimension at most \(N+2\), and there are finitely many strata. If its evaluation is nondominant, a general point of \(Y\) avoids it; if dominant, its general fiber has dimension at most zero. Hence no one-dimensional incidence-cut component is boundary-supported.

The smooth graph fiber computed below is generically reduced and one-dimensional, so its closure with multiplicity one is exactly the incidence-cut virtual one-cycle. Refined point pullback is transverse at its generic point; isolated or embedded points do not contribute to that cycle. For \(a=0\), three thick contacts and one ordinary mark give expected dimension three, while ordinary evaluation has target dimension two. The same argument excludes a boundary-supported one-dimensional incidence component. This is the separate proper-intersection argument that ambient irreducibility alone does not supply.

### Size zero

If any normal flag occurs, the connected first projection is constant. Ordinary incidence fixes it to \(t_0\), while the normal flag requires \(t_i\ne t_0\). The entire incidence-cut moduli is empty, including expansions, and the local invariant is zero. This excludes eight formerly counted diagrams with total edge product 56.

If no normal flag occurs, the thick-count equation gives three relative marks. On a smooth four-marked rational source the three prescribed signed orders define a degree-zero divisor and a unique rational function up to scale. Its value \(u_0\) at the fourth mark fixes the scale, and the fiber is \(t_0\). Proper forgetting therefore maps the incidence curve generically one-to-one to \(\overline M_{0,4}\); generic stack degree is one.

The ordinary component survives stabilization: a nonconstant second projection needs distinct special points over zero and infinity, in addition to the ordinary mark; a constant component is already stable. Contracting an adjacent unstable chain replaces its node by the surviving marking or node. Thus the ordinary cotangent line is pulled back from \(\overline M_{0,4}\). The incidence virtual one-cycle pushes forward to its fundamental class and
\[
\operatorname{mult}(V)=\int_{\overline M_{0,4}}\psi_p=1.
\]
Higher contact orders give no extra contact factor or factorial: the function and its scale are fixed and the generic labeled four-marked source has trivial automorphism.

### Size one

There is exactly one thick relative mark of signed order \(m\ne0\), with moving first coordinate \(r\). Let the normal signed orders at \(t_i\) be \(m_i\), so \(m+\sum_i m_i=0\). The smooth map is the graph
\[
u(t)=c(t-r)^m\prod_i(t-t_i)^{m_i}.
\]
Stationary incidence \(u(t_0)=u_0\) uniquely fixes \(c\). The incidence curve has function field \(\mathbb C(r)\), coarse normalization \(\mathbb P^1_r\) and generic stack degree one. Its actual virtual one-cycle is the graph closure proved above.

The first-projection differential at the ordinary mark, after trivializing the fixed vector space \(T^*_{t_0}\mathbb P^1\), gives a global section of the cotangent line. Its zeros occur precisely when the ordinary component has zero first degree. A connected vertical subtree containing the ordinary mark lies over \(t_0\), so it contains no normal relative marking. It must contain an external relative marking: otherwise contact balancing on its tree forces every second degree to zero, leaving an unstable tree carrying only the ordinary mark and one backbone attachment. Hence it contains the unique thick mark, necessarily with \(r=t_0\).

Write \(\epsilon=r-t_0\) and \(z=(t-t_0)/\epsilon\). On the limiting ordinary component,
\[
u(z)=u_0\left(\frac{z-1}{-1}\right)^m.
\]
Its three distinct special points are the ordinary mark at zero, the thick mark at one and the backbone attachment at infinity. It has no automorphism fixing them. Since \(dt=\epsilon\,dz\), the cotangent section has a simple zero in the coarse smoothing coordinate, independent of \(|m|\). Collisions \(r=t_i\) or \(r=\infty\) are away from the ordinary coordinate and yield no additional zero there.

If a minimal logarithmic chart extracts a root \(\epsilon=\delta^e\), the zero order becomes \(e\) and the stack integration degree is \(1/e\), whose product is one. Proper degree-one stack pushforward preserves this divisor degree. No extra expansion or contact-order factor is inserted. Therefore every occurring size-one local \(\tau_1(\mathrm{pt})\) invariant is one.

### Exhaustive global enumeration

Primary size-one factors are one by CJMR Remark 6.2. The primary size-zero factor vanishes unless its only two flags are thick, oppositely directed, and of equal weight; in that case it is one. The preceding descendant calculations, not Remark 6.2, supply the one-psi factors.

There are \(4^{4-2}=16\) labeled trees. The enumeration checks all \(4^4\) labeled-contact attachments, all four size patterns, and all \(2^3\) thickening choices. For a tree, balance determines compact weights uniquely: deleting one edge gives a cut, and its signed weight is the signed sum of the end contacts on either side. Since the total positive and negative masses are both four, every positive compact weight is at most four. Thus a separate bounded brute-force search over weights 1 through 4 is also exhaustive.

The first implementation solves the tree balance equations by exact rational elimination. The second, independently written implementation tries bounded weights directly and uses a different loop order, with no shared solver. Both apply the local zero criterion and produce the table above. The machine-readable ledger contains every nonzero diagram. A third checker validates its balance, size sum, thick count, primary and descendant local rules, multiplicity, distinctness, and equality with the exhaustive first enumeration.

CJMR Theorem 4.9 gives the degeneration correspondence, and its connected version is Corollary 4.10. The latter identifies the correctly weighted connected floor sum with the connected relative descendant invariant. Consequently each fixed-position invariant is 352. Equality of the four values is also required by symmetry of the labeled ordinary insertions.

## Verification

Run the Python 3 standard-library scripts in `artifacts`: `enumerate.py`, `recount2.py`, and `verify.py`. The latter two print `RECOUNT2_CORRECTED_OK` and `VERIFY_CORRECTED_OK`. No network, external package, or random seed is required.

### Auxiliary quantum graph statistic

Replacing each compact weight by its quantum integer defines a graph statistic only. In \(t=q^{1/2}\), the coefficients at exponents \(-9,-8,\ldots,9\), for the sum over the four positions, are
\(4,2,18,12,54,42,132,110,236,188,236,110,132,42,54,12,18,2,4\).
They are symmetric and sum to 1408. No refined descendant Gromov--Witten correspondence is claimed.

## Relationship to prior work

The CJMR framework defines this invariant but does not evaluate its exact coefficient. The inspected Corey--Markwig--Ranganathan definition counts primary point insertions without psi; AMW supply comparison and deformation theory, not the coefficient352 or a universal unit-weight descendant formula. The contribution is the exact natural coefficient, explicit local calculation and full reproducible ledger. Originality remains best-of-knowledge with bounded source searches.

## Limitations

The former 168/1464 census assigned weight one to every descendant vertex. Eight size-zero descendant diagrams contain normal fixed flags and have local invariant zero; their edge-product contribution is 56. Excluding them changes the totals to 160/1408. The old per-position values 352,376,384,352 are superseded. Historical computations are evidence of the former convention, not of the corrected invariant. The direct partial-pair proof also replaces an unjustified primitive fully toric theorem reduction and supplies the missing incidence-cut proper-intersection argument. No claim that the original geometric1464 was established survives.

The claimed contribution is this exact coefficient and its explicit local-weight proof and reproducible complete ledger, not a new general correspondence theorem. The quantum polynomial is only auxiliary. The partition by an attached end, if used, is an internal decomposition and not an independent recursion. Originality is best-of-knowledge: the inspected prior framework includes the problem but does not supply this exact descendant coefficient.

## References

- Cavalieri--Johnson--Markwig--Ranganathan, *Counting curves on Hirzebruch surfaces: tropical geometry and the Fock space*, [arXiv:1706.05401](https://arxiv.org/html/1706.05401), Definitions 2.5, 4.1, 4.3, 4.4; Theorem 4.9 and Corollary 4.10; Remark 6.2.
- Corey--Markwig--Ranganathan, *Counting Tropical Curves in P1 x P1: Computation and Polynomiality Properties*, [IMRN 2025, rnaf221](https://doi.org/10.1093/imrn/rnaf221), Section 2.1 and Definition 2.1.1. The latter counts primary point insertions, not this descendant coefficient.
- Abramovich--Marcus--Wise, *Comparison theorems for Gromov--Witten invariants of smooth pairs and smooth degenerations*, [arXiv:1207.2085](https://arxiv.org/html/1207.2085), Definition 1.1.1, Theorem 1.1.2, Corollary 1.1.3 and Sections 2.3, 3.5.

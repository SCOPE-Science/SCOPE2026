# Exact two-rainbow pushability of affine-regular octagons and the individual-balance gap

## Finding
Let \(P\) be any invertible linear image of a regular octagon centred at the origin. For the two-rainbow pushability introduced in [1],
\[
\boxed{\pi_2(P)=\frac{26-7\sqrt2}{32}=0.503140783230885\ldots.}
\]
If both vertex distributions are required to have mean zero separately, rather than only their means summing to zero, the sharp probability is exactly \(1/2\). Thus allowing nonzero but opposing individual means produces a strict, explicitly quantified improvement \((10-7\sqrt2)/32\), even for a centrally symmetric polygon. The result holds for all affine-regular octagons by affine invariance; it does not claim the same value for arbitrary octagons.

## Assumptions and scope
Label the regular octagon's vertices \(v_j=(\cos(j\pi/4),\sin(j\pi/4))\), \(0\le j<8\). Two independent random vertices have laws \(p=(p_0,\ldots,p_7)\) and \(q=(q_0,\ldots,q_7)\). They are *collectively balanced* when \(p_j,q_j\ge0\), each law sums to one, and
\[
\sum_{j=0}^7(p_j+q_j)v_j=0.
\]
Two vertices lie in a common facet (edge) precisely if they are identical or adjacent modulo eight. Accordingly, the objective is the bilinear polynomial
\[
F(p,q)=\sum_{i,j=0}^7M_{ij}p_iq_j,\qquad
M_{ij}=\mathbf1\{i-j\equiv-1,0,1\pmod8\}.
\]
The main invariant is the maximum of \(F\) under collective balance. The comparison invariant \(\pi_2^{\rm sep}(P)\) is the same maximum with the additional constraints \(\sum_jp_jv_j=\sum_jq_jv_j=0\). The distributions remain independent throughout.

## Proof
**1. A three-point reduction.** Compactness gives an optimizer. With \(q\) fixed, the constraints on \(p\) are its unit mass and two prescribed mean coordinates; maximizing \(F\) is a linear program. An extreme optimizer has at most three positive coordinates. Holding that \(p\) fixed and reoptimizing \(q\) likewise gives a global optimizer with at most three positive coordinates in each law. This does not assume the two laws are individually balanced.

**2. Finite exact critical-point principle.** Fix nonempty support sets \(I,J\subset\{0,\ldots,7\}\), each of cardinality at most three. Restricted to these supports, the two normalization equations and two collective-balance equations cut out an affine subspace. Its dimension, if consistent, is at most two; its intersection with the nonnegative orthant is compact. Choose affine coordinates \(t\). Then \(F=c+g^{\mathsf T}t+\frac12t^{\mathsf T}Ht\). A maximum in the relative interior either has negative-definite Hessian \(H\), or can be moved to a smaller support without decreasing its value: positive curvature forbids an interior local maximum; in the negative-semidefinite singular case, stationarity and a zero-curvature direction give a constant segment reaching the boundary. Consequently it suffices to examine strictly positive affine solutions when the dimension is zero, and feasible stationary solutions with negative-definite Hessian when the dimension is one or two. All omitted boundary cases occur among smaller supports.

The dihedral symmetries of the octagon reduce the first support to the ten representatives
\[
\{0\},\{0,1\},\{0,2\},\{0,3\},\{0,4\},
\{0,1,2\},\{0,1,3\},\{0,1,4\},\{0,2,4\},\{0,2,5\}.
\]
The second support can be any of the \(92=\binom81+\binom82+\binom83\) nonempty subsets of size at most three. Thus there are exactly \(920\) support-pair cases.

**3. Exact certificate for the upper bound.** The included `verify_octagon.py` performs Gaussian elimination and quadratic stationary-point tests entirely in \(\mathbb Q(\sqrt2)\). It compares the resulting values by exact rational-square sign tests (no floating-point acceptance threshold). Of the 920 support-pair cases, 126 yield strictly positive, negative-definite or zero-dimensional stationary candidates. The largest values for the ten first-support classes are as follows:

| First support | Largest interior stationary value |
|---|---|
| \(\{0\}\) | \(0\) |
| \(\{0,1\}\) | none; only boundary cases |
| \(\{0,2\}\) | \(\frac12-\frac{\sqrt2}4\) |
| \(\{0,3\}\) | \(\frac12\) |
| \(\{0,4\}\) | \(\frac{26-7\sqrt2}{32}\) |
| \(\{0,1,2\}\) | \(\frac14-\frac{\sqrt2}8\) |
| \(\{0,1,3\}\) | \(\frac{11-6\sqrt2}{14}\) |
| \(\{0,1,4\}\) | \(\frac{4\sqrt2-3}{7}\) |
| \(\{0,2,4\}\) | \(\frac{181\sqrt2-53}{527}\) |
| \(\{0,2,5\}\) | \(\frac{26-7\sqrt2}{32}\) |

The verifier derives these bounds, rather than trusting the table. The critical-point principle then yields \(F\le(26-7\sqrt2)/32\) for all collectively balanced independent laws.

**4. Attainment.** Put \(c=\sqrt2/2\) and \(b=(1+3c)/(4(1+c))=\sqrt2/2-1/4\). Give \(p\) mass
\[
p_0=\frac{1-c+(1+c)b}{2},\qquad p_4=1-p_0,
\]
and give \(q\) mass \(q_4=b\), \(q_1=q_7=(1-b)/2\), all other masses zero. The two mean vectors are opposite because \(v_1+v_7=2cv_0\) and \(v_4=-v_0\). Direct substitution gives
\[
F=p_0(1-b)+(1-p_0)b=\frac12+\frac{(1-c)^2}{16(1+c)}
=\frac{26-7\sqrt2}{32}.
\]
All masses are strictly positive on their displayed supports, so the maximum is attained.

**5. Individual-balance comparison.** The polytope of probability laws on these eight vertices with mean zero has 12 vertices: four equal-weight antipodal-pair laws and eight positive three-vertex laws. Indeed its three independent affine equations force every extreme support to have at most three elements. The verifier solves the corresponding exact linear systems for all 92 potential supports, retaining precisely these 12 extremes, and evaluates all \(12^2=144\) extreme law-pairs. Because \(F\) is bilinear, its maximum on the product of the two individual-balance polytopes occurs at such a pair. All 144 values are at most \(1/2\); taking both distributions uniform on \(\{v_0,v_4\}\) attains \(1/2\). Thus \(\pi_2^{\rm sep}(P)=1/2\).

## Verification
Run `python3 verify_octagon.py` using a standard Python 3 installation. It requires no third-party packages and terminates with `PASS` only after proving all exact comparisons, the witness normalization and balance identities, the 920-case maximum, and the 144-case separately balanced maximum. The supporting code contains the exact field representation, elimination, nonnegative feasibility tests, Hessian test, and objective evaluations. Its expected result is 126 admissible stationary candidates and the exact value \((26-7\sqrt2)/32\). An additional independent numerical constrained-optimization search over random initial laws found the same candidate in the regular octagon; that numerical search is not the proof.

## Relationship to prior work
Martínez-Sandoval and Olvera-Sampieri [1], Definition 3.1, introduce rainbow pushability as a maximum over *collectively* balanced independent vertex laws. Their Theorem 4.1 supplies a facet-depth upper bound for all centered polytopes, Corollary 4.2 specializes it to centrally symmetric ones, and their cube computation is exact. Their later discussion explicitly asks for exact computations on further centered polytopes. Those general bounds do not give the displayed octagonal value or the strict collective-versus-individual balance gap. Earlier exact computations for pentagonal, hexagonal, and cross-polytopal objects concern different polytopes and do not imply the octagonal result. No assertion is made that searches exhaust all unindexed or unpublished results.

## Limitations
This establishes an exact result for two independent laws, the regular octagon and its centered invertible linear images. No formula for general octagons or larger numbers of laws is derived, and all optimal law-pairs in the unrestricted support space are not classified. The finite critical-point enumeration is exhaustive because of the analytic support and boundary reductions; an arbitrary sample or a truncated enumeration alone would not suffice. Novelty assessments remain subject to independently located literature. There has been no independent audit.

## References
[1] L. Martínez-Sandoval and A. Olvera-Sampieri, *Pushed colorful polytopal KKMS Theorem and orthogonal star transversals*, arXiv:2610.17157v1 (first publicly posted October 12, 2026), Sections 3, 4, and 7. https://arxiv.org/abs/2610.17157

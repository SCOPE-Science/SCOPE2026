# Frobenius orbit spectra and rational incidence obstructions for Pascal–Kirkman flags

## Finding

Let \(k=\mathbb F_q\) have characteristic \(p\ge 7\), and let \(D\) be a reduced, Frobenius-stable degree-six divisor on a nonsingular plane conic over \(k\). Suppose its geometric six-point configuration is *incidence-generic*: all sixty Pascal lines and all sixty Kirkman points defined below are distinct, and there are no additional incidences between a Pascal line and a Kirkman point beyond the classical ones. The finite reduced incidence scheme \(\mathcal F_D\) consisting of pairs (Pascal line, incident Kirkman point) has 180 geometric points. Its Frobenius orbit spectrum, and therefore its complete zeta function and its rational-point counts over every finite extension, depend only on the Frobenius cycle partition \(\lambda\vdash6\) of \(D\).

Write \(d:c\) for \(c\) Frobenius cycles of length \(d\). Let \(\mathcal H_D\) denote the sixty-element scheme of Pascal lines (the sixty Kirkman points have the same orbit spectrum). The complete classification is:

| Frobenius partition \(\lambda\) | Pascal lines / Kirkman points, orbit spectrum | 180 incident flags, orbit spectrum |
|---|---|---|
| \((6)\) | \(1:1,\ 2:1,\ 3:5,\ 6:7\) | \(3:8,\ 6:26\) |
| \((5,1)\) | \(5:12\) | \(5:36\) |
| \((4,2)\) | \(2:2,\ 4:14\) | \(2:2,\ 4:44\) |
| \((4,1,1)\) | \(2:2,\ 4:14\) | \(2:2,\ 4:44\) |
| \((3,3)\) | \(1:3,\ 3:19\) | \(3:60\) |
| \((3,2,1)\) | \(6:10\) | \(6:30\) |
| \((3,1,1,1)\) | \(3:20\) | \(3:60\) |
| \((2,2,2)\) | \(1:16,\ 2:22\) | \(1:24,\ 2:78\) |
| \((2,2,1,1)\) | \(1:4,\ 2:28\) | \(1:4,\ 2:88\) |
| \((2,1,1,1,1)\) | \(2:30\) | \(2:90\) |
| \((1,1,1,1,1,1)\) | \(1:60\) | \(1:180\) |

Consequently, rational Pascal lines and rational Kirkman points exist but **no rational incident Pascal–Kirkman pair exists** if and only if \(\lambda=(6)\) or \(\lambda=(3,3)\). The respective numbers of rational Pascal lines and rational Kirkman points are one and three, whereas the numbers of rational incidence flags are zero in both cases.

If \(c_d(\lambda)\) is the number of \(d\)-cycles in the third column, then, for every integer \(n\ge1\),
\[
\#\mathcal F_D(\mathbb F_{q^n})=\sum_{d\mid n}d\,c_d(\lambda),
\qquad
Z(\mathcal F_D,T)=\prod_{d\ge1}(1-T^d)^{-c_d(\lambda)}.
\]
The minimal extension over which all 180 incident flags are rational has degree \(\operatorname{lcm}(\lambda)\).

## Assumptions and scope

All geometric points of \(D\) are pairwise distinct. Label them by \(\{0,1,2,3,4,5\}\). For a cyclic ordering \((a,b,c,d,e,f)\), the Pascal line is the line through the three intersections of the opposite side pairs \((ab,de)\), \((bc,ef)\), \((cd,fa)\). Reversal and cyclic shift yield the same line. As a set of labels, these are the sixty unoriented Hamiltonian cycles in the complete graph on six vertices.

Let \(\mathcal H\) be that set of sixty cycles, interpreted as six-cycles in \(S_6\) modulo inversion, and write \(E(h)\) for the six undirected edges of a cycle \(h\). Kirkman's classical concurrence theorem associates to each \(k\in\mathcal H\) a point \(K_k\), at which precisely the three Pascal lines indexed by cycles \(h\) satisfying \(E(h)\cap E(k)=\varnothing\) concur. Under the stated genericity conditions the sixty \(K_k\) are distinct and no other Pascal–Kirkman incidence occurs. These hypotheses avoid special coincidence loci and define the reduced configuration, not a nonreduced degenerating incidence scheme.

The claim is conditional on the existence of such a configuration over the specified finite field. It does not claim that each Frobenius partition can be realized in the incidence-generic locus over every small finite field. A concrete exact witness described below proves that this locus is nonempty in characteristic zero and in at least one permitted positive characteristic.

## Proof

**1. Equivariant combinatorial model.** A six-cycle has exactly twelve representations under rotation and reversal, giving \(6!/12=60\) unoriented hexagons. The edge-disjointness rule defines the set
\[
\mathcal F=\{(h,k)\in\mathcal H\times\mathcal H:E(h)\cap E(k)=\varnothing\}.
\]
For any fixed cycle \(k\), exactly three unoriented Hamiltonian cycles have no edge in common with \(k\), verified directly by the exhaustive finite construction in `verify_hexagrammum.py`. Hence \(|\mathcal F|=60\cdot3=180\). Classical Kirkman concurrence identifies this combinatorial relation with the actual geometric Pascal–Kirkman incidence relation; the concrete independent projective construction in the verifier additionally checks this identification exactly for one incidence-generic sextuple. Both point and line configurations are functorial for relabeling of the six original points.

**2. Descent to a single conjugacy type.** The geometric Frobenius of \(k\) acts on \(D\) by a permutation \(\sigma\in S_6\), unique up to conjugacy. On the two sets of sixty objects it sends \(h\) to \(\sigma h\sigma^{-1}\), understood modulo inversion, and on flags it sends \((h,k)\) to \((\sigma h\sigma^{-1},\sigma k\sigma^{-1})\). Consequently the orbit spectra depend only on the eleven conjugacy classes of \(S_6\), equivalently on \(\lambda\vdash6\).

**3. Exhaustive classification.** The supplementary standalone verifier constructs all \(720\) permutations of six labels, selects each permutation having one six-cycle as an unoriented hexagon, and constructs all 180 edge-disjoint ordered pairs. For each of the eleven cycle types it iterates the actual permutation action on these two sets until every orbit is exhausted. It verifies the displayed integer multiplicities by independently computing fixed points of every power of a representative and comparing them with the orbit-cycle formulas. Finally it checks the rational fixed-point counts for all 720 permutations, so the complete tabulation does not rely upon a sample of Frobenius permutations. The algorithm uses only finite exact integer operations; the full source is supplied with this result.

**4. Rational-incidence obstruction.** A finite étale configuration object is \(k\)-rational precisely if its label is fixed by \(\sigma\). The table shows that the only cycle types having at least one fixed Pascal and fixed Kirkman but no fixed flag are \((6)\) and \((3,3)\). There is an intrinsic explanation in both cases. For a six-cycle \(\sigma\), its only fixed unoriented hexagon is the cycle of \(\sigma\) itself, whose edge set cannot be disjoint from itself. For a product of two disjoint three-cycles, there are exactly three fixed unoriented hexagons; every pair of these shares three edges, so none is incident under the edge-disjointness rule. The other nine cases, including those with no fixed individual lines or points, are exhausted by the complete orbit table.

**5. Extension fields and zeta function.** A Frobenius orbit of length \(d\) contributes exactly \(d\) rational points over \(\mathbb F_{q^n}\) if and only if \(d\mid n\). Its contribution to the zeta function is \((1-T^d)^{-1}\). Multiplication over the 180 points gives the two formulas. The least \(n\) divisible by every orbit length in each row is exactly the least common multiple of the entries of \(\lambda\), giving the splitting-degree assertion.

## Verification

Running `python3 verify_hexagrammum.py` with Python 3.9 or newer requires only the standard library. The supplied `verification_output.txt` records the exact observed run ending with `VERIFY_OK`. The verifier reconstructs the sixty hexagons, all 180 incident pairs, all eleven spectra, and the fixed-point checks for all 720 permutations; it asserts all eleven displayed rows.

As an independent geometric normalization check, it takes six points \((1:t:t^2)\) on the nonsingular conic \(XZ=Y^2\), with \(t\in\{0,1,3,9,25,64\}\). Using exact projective cross products, it constructs all sixty Pascal lines and all sixty Kirkman points, checks the three defining concurrences, and confirms that **exactly** the 180 combinatorially prescribed incidences occur, with no coinciding lines or Kirkman points. The same computation succeeds over \(\mathbb Q\) and modulo \(10007\), giving an explicit positive-characteristic example. The group-theoretic classification, not these two examples, proves the claimed formulas for every incident-generic configuration over every field within the stated scope.

## Relationship to prior work

The sixty Pascal lines, sixty Kirkman points, and their three-regular incidence are classical. Conway and Ryba describe the combinatorial structure of the hexagrammum mysticum; Chipalkatti studies coincidences among Pascal lines, and Chipalkatti–Ryba's *Absolute Projectivities in Pascal's Multimysticum* (especially §§2.1–2.7) describes the full relabeling-invariant incidence structure. These sources establish the geometric framework and provide much of the combinatorial input; this result claims no new construction of Kirkman points or proof of their classical concurrence theorem.

The specific arithmetic output given here is the full eleven-type Frobenius orbit classification of the **180 incident flags**, its zeta functions and extension-field counts, and the precise two partitions exhibiting rational non-incidence. The inspected primary works discuss complex-projective geometry and other invariants; no such full finite-field arithmetic table was located in them. Since the table is computable from their \(S_6\)-equivariant data, unpublished computations or less directly titled tables could anticipate it; novelty is limited to the explicit arithmetic classification, not the underlying combinatorics.

## Limitations

The result is about the reduced finite configuration in incidence-generic characteristic \(p\ge7\); it does not include non-generic sextuples, arbitrary extra coincidences, nonreduced incidence schemes, or characteristics two, three, and five. It is conditional, not an existence theorem for every finite field and splitting pattern. The exact group computation and projective witness are reproducible; an independent scientific audit has not been performed. The 2012–2013 Conway–Ryba papers are important antecedents; the complete text of those papers was not available for direct comparison, creating a specific residual literature-priority risk.

## References

- J. Chipalkatti, *On the coincidence of Pascal lines*, arXiv:1407.1447, first version dated 2014-07-06, https://arxiv.org/abs/1407.1447.
- J. Chipalkatti, *When are the Cayley-Salmon lines conjugate?*, arXiv:1505.07144, first version dated 2015-05-26, https://arxiv.org/abs/1505.07144.
- J. Chipalkatti and A. Ryba, *Absolute Projectivities in Pascal's Multimysticum*, International Journal of Geometry 9 (2020), 114–136; arXiv:2007.04315, https://arxiv.org/abs/2007.04315.
- J. H. Conway and A. Ryba, *The Pascal Mysticum Demystified*, The Mathematical Intelligencer 34 (2012), 4–8; and *Extending the Pascal Mysticum*, The Mathematical Intelligencer 35 (2013), 44–51. Cited for the established geometric permutation framework; their complete texts were not inspected here.

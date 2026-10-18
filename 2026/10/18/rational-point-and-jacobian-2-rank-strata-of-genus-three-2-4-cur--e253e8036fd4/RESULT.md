# Rational-point and Jacobian \(2\)-rank strata of genus-three \((2,4)\) curves over \(\mathbf F_2\)

## Finding
Let \(Q=\mathbf P^1_{\mathbf F_2}\times\mathbf P^1_{\mathbf F_2}\), and consider the nonzero bihomogeneous sections \(F\in H^0(Q,\mathcal O_Q(2,4))\). There are \(2^{15}-1=32{,}767\) such sections, with no nontrivial scalar identification over \(\mathbf F_2\). Let \(C_F=V(F)\), and restrict to **geometrically smooth** curves. They have genus three and their projection onto the degree-two ruling is a separable hyperelliptic double cover.

Write \(N(C_F)=\#C_F(\mathbf F_2)\) and \(f(C_F)\) for the \(2\)-rank of the Jacobian. Then there are **exactly \(9{,}216\) smooth sections, forming \(294\) orbits** under the ruling-preserving group \(G=\operatorname{PGL}_2(\mathbf F_2)\times\operatorname{PGL}_2(\mathbf F_2)\). Their complete joint distribution is below. Each entry is **number of equations (number of \(G\)-orbits)**.

| \(N\) | \(f=0\) | \(f=1\) | \(f=2\) | \(f=3\) |
|---:|---:|---:|---:|---:|
| 0 | 0 | 6 (1) | 0 | 27 (2) |
| 1 | 72 (2) | 0 | 36 (1) | 144 (6) |
| 2 | 0 | 414 (14) | 0 | 495 (20) |
| 3 | 432 (12) | 0 | 468 (13) | 720 (23) |
| 4 | 0 | 1,314 (41) | 0 | 1,557 (52) |
| 5 | 648 (18) | 0 | 504 (14) | 1,296 (38) |
| 6 | 0 | **282 (11)** | 0 | **801 (26)** |

In particular, precisely \(1{,}083\) smooth sections have the largest possible rational-point count, \(N=6\); they form \(37\) ambient projective orbits. Their Jacobians have **only \(2\)-ranks \(1\) and \(3\)**, with \(282\) and \(801\) equations respectively, and \(11\) and \(26\) corresponding orbits. This stratification is the main result; the elementary bound \(N\le6\) for a degree-two map over \(\mathbf F_2\) is not asserted as a new discovery.

## Assumptions and scope
Coordinates on \(Q\) are \(([U:V],[S:T])\), with bidegree two in \((U,V)\) and four in \((S,T)\). We write uniquely
\[
F=U^2A(S,T)+UVB(S,T)+V^2C(S,T),
\]
where \(A,B,C\) are binary quartics over \(\mathbf F_2\). A coefficient mask \(a\in\{0,\ldots,31\}\) represents \(\sum_{i=0}^{4}a_iS^{4-i}T^i\), with \(a_i\in\{0,1\}\) the \(i\)-th binary digit of \(a\). The same convention applies to \(b,c\).

The classification is of **embedded divisors** modulo the specified \(36\)-element rational automorphism group. Because the bidegrees differ, exchanging the factors is not allowed. These orbit counts are **not** claims about abstract isomorphism classes of genus-three curves. The unique degree-two ruling is the hyperelliptic map; the other ruling provides a distinguished degree-four pencil.

## Proof
**1. Exact geometric smoothness test.** Over characteristic two, the derivatives of \(F\) in the fiber coordinates are \(VB\) and \(UB\). Thus, a singularity can occur only over a geometric zero of \(B\). In an affine chart of the base, put \(a(t)=A(1,t)\), \(b(t)=B(1,t)\), and \(c(t)=C(1,t)\). Above a zero of \(b\), the fiber equation is \(aU^2+cV^2=0\). If \((a,c)\ne(0,0)\), it has one geometric root, and differentiating with respect to the base coordinate gives the exact singularity criterion
\[
D(a,b,c):=(ca'+ac')^2+ac(b')^2=0.
\]
Indeed, in the chart \(U=1\), substitute \(v^2=a/c\) into \(a'+b'v+c'v^2\), square, and multiply by \(c^2\). The result also holds when \(a=0\) or \(c=0\) by using the other fiber chart. If \(a=c=0\), then \(D=0\) automatically and the entire fiber is present, so the divisor is singular. Consequently the divisor is geometrically smooth precisely when \(b\ne0\) and the polynomial gcd of \(b\) and \(D\) is one **in both standard base charts** \(S=1\) and \(T=1\). In the latter chart the five coefficients of every quartic are reversed. This tests all geometric points, including those over extensions of \(\mathbf F_2\), with no point-search cutoff.

**2. Rational points and \(2\)-rank.** The three rational base values are \([1:0]\), \([1:1]\), \([0:1]\). The rational fiber has exactly as many points as the zeros of the ternary evaluation list \(A, C, A+B+C\) at that base value, corresponding to \([1:0]\), \([0:1]\), and \([1:1]\) in the fiber. Evaluating all three fibers computes \(N\) exactly.

For a geometrically smooth divisor, \(B\) is nonzero and its geometric zeros are exactly the branch locus of the separable double cover to the base. The Deuring–Shafarevich formula for an Artin–Schreier double cover of \(\mathbf P^1\) gives
\[
f(C_F)=r-1,
\]
where \(r\) is the number of **distinct geometric zeros** of the homogeneous quartic \(B\). To find \(r\), factor the affine \(B(1,t)\) in \(\mathbf F_2[t]\), count distinct roots with their irreducible-factor degrees, and include the point at infinity if its leading homogeneous coefficient vanishes. This includes repeated factors with their correct support sizes.

If \(N=6\), all three rational fibers split into two rational points, so \(B\) cannot vanish at any rational base point. Exactly four homogeneous binary quartics satisfy this: the masks \(19,21,25,31\). Masks \(19,25,31\) are irreducible quartics (four geometric branch points, hence \(f=3\)); mask \(21\) equals \((S^2+ST+T^2)^2\) (two geometric branch points, hence \(f=1\)). This proves the \(2\)-rank **exclusion** for maximal-point curves conceptually; exhaustive enumeration supplies the sharp multiplicities.

**3. Complete finite classification.** The algorithm enumerates all \(32^3-1=32{,}767\) triples of coefficient masks and applies the two-chart smoothness test. Exactly \(9{,}216\) pass. Direct rational-fiber evaluation and branch-factorization give the equation counts in the table.

There are six invertible \(2\times2\) binary matrices acting on each factor. For every surviving section, all \(36\) transformations are evaluated by exact polynomial substitution. The resulting orbits partition the smooth coefficient set into \(294\) classes, with the orbit counts in the table. The complete representatives and sizes appear in `data/orbit_representatives.csv`; every orbit has size dividing \(36\). The algorithms verify the entire coefficient set and do not infer uniqueness merely from a partition of literature searches.

**4. Extremal witnesses.** With the mask convention above, the two equations with triples \((a,b,c)=(6,21,1)\) and \((6,19,1)\) are geometrically smooth and each has six rational points. Explicitly they are
\[
U^2(S^3T+S^2T^2)+UV(S^4+S^2T^2+T^4)+V^2S^4=0
\]
and
\[
U^2(S^3T+S^2T^2)+UV(S^4+S^3T+T^4)+V^2S^4=0.
\]
They have \(2\)-ranks \(1\) and \(3\), respectively. Their orbit sizes are both \(18\). In either case, the three rational base fibers contain exactly two rational points each.

## Verification
`verify.py` (Python standard library) carries out the complete \(32{,}767\)-coefficient scan, the ambient coordinate-group orbit partition, the rational-point counts, and the branch-count calculation. It checks the resulting counts against `data/joint_table.json` and verifies each of the \(294\) entries in `data/orbit_representatives.csv`. Run `python verify.py` in the directory containing the files and the `data` subdirectory.

`crosscheck.py` (requires SymPy) independently tests geometric smoothness using Gröbner bases for \((F,F_u,F_t)\) on the four affine charts. The complete coefficient space is partitioned into projective orbits, and **every orbit representative, singular or smooth**, is checked; the two smoothness tests agree. For each of the \(294\) smooth orbit representatives, the same script independently counts points over \(\mathbf F_2\), \(\mathbf F_4\), and \(\mathbf F_8\); Newton identities recover the genus-three zeta polynomial, whose degree modulo two is the Jacobian \(2\)-rank. Those ranks agree with the branch formula for all representatives. Run `python crosscheck.py`. No finite-extension point search is used as a substitute for the algebraically exact geometric smoothness criterion.

## Relationship to prior work
Nart and Sadornil (2004) classify **abstract \(\mathbf F_q\)-isomorphism classes** of genus-three hyperelliptic curves in characteristic two by their Artin–Schreier ramification divisors. Their classification and its branch-type analysis are foundational prior work, not new claims here. In particular, the formula relating \(2\)-rank to branch support is known; see also Booher and Pries (first publicly available in 2020). The present table instead classifies **bidegree-\((2,4)\) embeddings with both ruling morphisms distinguished** and jointly refines the exact rational-point count, Jacobian \(2\)-rank, and embedding orbit.

Existing work on bidegree-\((3,3)\) canonical genus-four curves on the same split quadric studies a different moduli stratum: those curves are not the genus-three hyperelliptic double covers considered here. No inspected prior result supplies or logically states the \(9{,}216\)/\(294\) table or the \(1{,}083\)/\(37\) maximal-point refinement. This is a best-knowledge comparison rather than a proof of worldwide publication priority.

## Limitations
All exact counts are specific to the field \(\mathbf F_2\), the bidegree \((2,4)\), and the **ruling-preserving rational projective** equivalence relation. An abstract isomorphism-class classification is not asserted. The arithmetic \(2\)-rank formula is standard, and the general six-point bound is elementary; the distinct contribution is the complete *embedded joint incidence/arithmetic census* and its orbit stratification. The computations are fully finite and their exhaustiveness follows from coefficient-space coverage; no extension to larger fields is claimed. Previously unpublished or unindexed equivalent embedded classifications remain a priority risk. There has been no independent external audit.

## References
1. Jeremy Booher and Rachel Pries, *Realizing Artin–Schreier covers of curves with minimal Newton polygons in positive characteristic*, arXiv:2003.09027, first public version March 19, 2020; Journal of Number Theory (2020), DOI 10.1016/j.jnt.2020.04.010. See Section 2.1 for the Deuring–Shafarevich \(p\)-rank formula.
2. Enric Nart and Daniel Sadornil, *Hyperelliptic curves of genus three over finite fields of even characteristic*, Finite Fields and Their Applications **10** (2004), 198–220, DOI 10.1016/j.ffa.2003.08.002. See Sections 1–4 for ramification divisors, rational Artin–Schreier normal forms, and abstract isomorphism classification.

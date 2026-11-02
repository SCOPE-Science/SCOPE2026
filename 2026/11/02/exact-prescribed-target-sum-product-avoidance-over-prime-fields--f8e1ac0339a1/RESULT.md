# Exact prescribed-target sum-product avoidance over prime fields

## Finding
For every prime \(p\ge5\) and \(c\in\mathbb F_p^\times\), define
\[
\alpha_p(c)=\max\{|A|:A\subseteq\mathbb F_p,\ c\notin(A+A)\cup(AA)\}.
\]
Let \(h_c\) be the projective transformation \(x\mapsto c-c/x\), with \(h_c(0)=\infty\) and \(h_c(\infty)=c\), and let \(d_c\) denote its order in \(\mathrm{PGL}_2(\mathbb F_p)\). Then
\[
\alpha_p(c)=\begin{cases}(p-3)/2,&\text{if }c\text{ is a nonzero square and }d_c\text{ is even},\\(p-1)/2,&\text{otherwise}.\end{cases}
\]
Write \(\varepsilon_p=(-1|p)\in\{-1,1\}\), \(L=p-\varepsilon_p\), and \(v=\nu_2(L)\). Among the \(p-1\) nonzero targets, exactly
\[
E_p=\frac12\left(\frac L2-\frac{L}{2^v}-1\right)
\]
attain the smaller value \((p-3)/2\), while the remaining \(p-1-E_p\) attain \((p-1)/2\). For example, modulo \(17\) precisely the targets \(2,8,13\) have extremum \(7\), and every other nonzero target has extremum \(8\).

## Assumptions and scope
All operations are in the prime field \(\mathbb F_p\), with \(p\ge5\). Both \(A+A\) and \(AA\) allow repeated elements (so \(2a=c\) and \(a^2=c\) individually forbid \(a\)). The maximum is over all subsets, including the empty set. The theorem classifies nonzero targets only; it does not assert the corresponding formula for target zero or general finite rings. The order \(d_c\) is an ordinary finite projective transformation order, not the order of a chosen matrix representative.

## Proof
**1. Conflict graph and projective completion.** On \(\mathbb F_p\), join distinct \(x,y\) if \(x+y=c\) or \(xy=c\), and put a loop at \(x\) if \(2x=c\) or \(x^2=c\). Its independent sets are exactly the admissible subsets. Extend to \(\mathbb P^1(\mathbb F_p)\) by using the involutions
\[
s(x)=c-x,\qquad m(x)=c/x,
\]
where \(s(\infty)=\infty\), \(m(0)=\infty\) and \(m(\infty)=0\). The original graph is obtained by deleting \(\infty\) and its incident edges, retaining the fixed-point loops. Each connected component of the two-colored projective graph is an alternating even cycle, an alternating path with a fixed-point loop at each endpoint, or the degenerate two-point component on which both involutions exchange the same pair. A degenerate two-point component has independence number one.

**2. Projective orbits.** Put \(h=sm\), represented by \(\begin{pmatrix}c&-c\\1&0\end{pmatrix}\), with trace \(c\), determinant \(c\), and discriminant \(c(c-4)\). If \(c\ne4\), this is semisimple. All nonfixed projective points have \(h\)-orbit length exactly \(d=d_c\), as follows by diagonalizing over \(\mathbb F_{p^2}\) and considering the ratio of the two eigenvalues. Two rational fixed points of \(h\), if present, form one two-point component: indeed \(s\) and \(m\) exchange them, since a common fixed point of \(s,m\) could occur only when \(c=4\). All other components consist either of two distinct \(h\)-orbits joined into an even cycle of length \(2d\), or one \(h\)-orbit preserved by \(s\), making a path of length \(d\) vertices with the \(s\)- and \(m\)-fixed points at its ends. The even cycles and the two-point component contribute precisely half their number of vertices to an independent set.

The involution \(s\) has exactly two projective fixed points, \(\infty\) and \(c/2\). The involution \(m\) has two fixed points precisely when \(c\) is a square, and none otherwise. No fixed point is shared if \(c\ne4\). On a preserved \(h\)-orbit of odd length, the two endpoints are fixed by different involutions; on one of even length, both endpoints are fixed by the same involution. Consequently the noncyclic components are determined completely by \(c\) being a square and by the parity of \(d\):

* If \(c\) is nonsquare, there is one even-length \(s\)-to-\(s\) path, of \(d\) projective vertices; thus \(d\) is even. Removing its endpoint \(\infty\) leaves \(d-1\) vertices and a loop at the other endpoint, with maximum independent size \((d-2)/2\). The other \(p+1-d\) projective vertices contribute \((p+1-d)/2\), giving \(\alpha_p(c)=(p-1)/2\).
* If \(c\) is square and \(d\) is odd, there are two \(s\)-to-\(m\) paths of \(d\) vertices each. One contains \(\infty\), whose deletion leaves a \((d-1)\)-vertex path with one loop; its independence number is \((d-1)/2\). The other, with loops at both ends, also contributes \((d-1)/2\). The other \(p+1-2d\) projective vertices contribute half, giving \((p-1)/2\).
* If \(c\) is square and \(d\) is even, there are two paths of \(d\) vertices, one \(s\)-to-\(s\) containing \(\infty\), the other \(m\)-to-\(m\). Removing \(\infty\) from the former yields independence number \((d-2)/2\); the latter likewise has independence number \((d-2)/2\). The remaining \(p+1-2d\) projective vertices contribute half, yielding \((p-3)/2\).

If \(c=4\), the map \(h\) is nontrivial unipotent of order \(p\) and has a single projective fixed point \(2\), fixed by both involutions and hence looped. The other \(p\) projective vertices form one alternating path between \(\infty\) and \(-2\). Deleting \(\infty\) leaves \(p-1\) vertices with one loop, of independence number \((p-1)/2\). This proves the extremal formula in every case.

**3. Counting exceptional targets.** For \(c\ne0,4\), let \(z\) be the ratio of the eigenvalues of \(h\). Its trace and determinant give
\[
c=z+2+z^{-1}=\frac{(z+1)^2}{z},\qquad d_c=\operatorname{ord}(z).
\]
If the discriminant is square, \(z\) belongs to \(\mathbb F_p^\times\), cyclic of order \(p-1\). Otherwise \(z\) belongs to the norm-one torus \(U=\{u\in\mathbb F_{p^2}^\times:u^{p+1}=1\}\), cyclic of order \(p+1\). In either case \(c\) is a square in \(\mathbb F_p\) if and only if \(z\) is a square in the corresponding cyclic torus: if \(z=u^2\), then \(c=(u+u^{-1})^2\) with \(u+u^{-1}\in\mathbb F_p\); conversely, writing \(c=w^2\) makes \(u^2-wu+1=0\) split over \(\mathbb F_p\) in the split case and produce an element of \(U\) in the nonsplit case.

Exactly one of the cyclic groups of orders \(p-1\) and \(p+1\) has order divisible by four: it has order \(L=p-(-1|p)\) and \(2\)-adic valuation \(v\ge2\). In the other cyclic group, every square has odd order. Thus exceptional targets correspond exactly to even-order elements \(z\) of the square subgroup of the cyclic group of order \(L\), excluding \(z=-1\) (which would give forbidden \(c=0\)). This square subgroup has \(L/2\) elements, and its subgroup of odd-order elements has \(L/2^v\) elements. Among its even-order elements, \(-1\) is present and excluded; all others occur in inverse pairs \(\{z,z^{-1}\}\), with each pair yielding one distinct nonzero target. Therefore their number is \(\big(L/2-L/2^v-1\big)/2\), as stated.

## Verification
The accompanying standard-library Python program `verify.py` independently constructs the finite conflict graph, computes exact component independence numbers, and compares them against the projective-order criterion for all 4,178 nonzero targets in the 44 prime fields \(5\le p<200\). For the 48 targets in prime fields \(p\le17\), it also independently enumerates all subsets by bitmask; it checks the exceptional-target count at each prime. Successful output is `VERIFY_OK prime_fields=44 target_cases=4178 exhaustive_bitmasks=48`. These finite checks are evidence for implementation and edge-case accuracy; the infinite assertion follows from the preceding proof, not the finite computation.

## Relationship to prior work
Quanyu Tang, *A counterexample to a conjecture of Sárközy on sums and products modulo a prime*, arXiv:2603.29992, first submitted 2026-03-31, proves the sharp value \((p-1)/2\) for the **single target \(c=1\)** and introduces its six-element anharmonic orbit via \(x\mapsto1-x\) and \(x\mapsto1/x\). Here the two involutions for arbitrary \(c\) may generate larger dihedral groups, with variable projective order and square-dependent loop arrangements. In fact \(c=1\) has projective order three and always belongs to the larger-extremum case, so the earlier construction does not yield the target-dependent exceptional spectrum. Sárközy's original 2001 problem concerns simultaneous covering by sums and products; it does not determine the present targetwise exact invariant. Related real-field sum-product growth results address the sizes of \(A+A\) and \(AA\), rather than the membership of a specified residue.

## Limitations
The result concerns prime fields of odd characteristic at least five and nonzero target residues; it does not classify extremal sets themselves, composite rings, or arbitrary extension fields. It gives an exact maximum and the number of exceptional targets, not an enumeration of all maximizing subsets. An earlier implicit treatment via dihedral permutation graphs or Möbius involutions cannot be ruled out by available literature searches, so independent priority assessment remains appropriate. No independent mathematical audit is claimed.

## References
1. Q. Tang, *A counterexample to a conjecture of Sárközy on sums and products modulo a prime*, arXiv:2603.29992v1 (2026-03-31), https://arxiv.org/html/2603.29992.
2. A. Sárközy, *Unsolved problems in number theory*, Periodica Mathematica Hungarica 42 (2001), 17–35, Conjecture 65 (bibliographic reference discussed by Tang).
3. T. Bloom, W. Sawin, C. Schildkraut, D. Zhelezov, *The sum-product conjecture is false for real numbers*, arXiv:2605.28781 (2026-05-27), https://arxiv.org/abs/2605.28781 (related but different growth problem).

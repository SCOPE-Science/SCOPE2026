# Exact exponential ambiguity fibers for composite ordered periodic cycles

## Finding
Let \(m,r\ge2\) be integers, let \(n=mr\), and let \(X=\{0,1,\ldots,n-1\}\) carry its natural linear order. For an \(n\)-cycle \(f\) on \(X\), its *complete left-right orbit signature* is
\[
\mathcal L_f(x,t)=\operatorname{sgn}(f^t(x)-x),\qquad x\in X,\quad 1\le t<n.
\]
There is an explicitly given signature \(\mathcal L_{m,r}\) whose fiber among **all single \(n\)-cycles** has exactly
\[
\boxed{\#\{f:\ f\text{ is an }n\text{-cycle and }\mathcal L_f=\mathcal L_{m,r}\}=r^{m-1}.}
\]
In fact, this entire fiber consists of the block translations described below; no other cycles realize that signature. Consequently, for every even \(n\ge4\), some complete orbit signature is shared by exactly \(2^{n/2-1}\) distinct single \(n\)-cycles. Thus even knowing every point's left-right relation to itself at every non-return time can leave exponentially many possible cyclic orders.

## Assumptions and scope
Fix consecutive ordered blocks \(B_j=\{jr,jr+1,\ldots,jr+r-1\}\) for \(0\le j<m\), and write a point as \(jr+u\) with \(0\le u<r\). Choose shifts \(a_j\in\mathbb Z/r\mathbb Z\) with
\[
\sum_{j=0}^{m-1}a_j=1\quad\text{in }\mathbb Z/r\mathbb Z.
\]
Define
\[
f_a(jr+u)=r((j+1)\bmod m)+((u+a_j)\bmod r).
\]
All modular expressions on the right are represented by their unique residues in the displayed index ranges. Let \(\mathcal L_{m,r}\) denote the signature of \(f_a\), which is independent of the admissible shift vector \(a\). This is a statement about permutations on one finite, linearly ordered periodic orbit. It makes no assertion that the complete periodic-orbit spectra of two *global* interval maps coincide.

## Proof
**1. Existence and common signature.** After \(m\) applications, the block index returns and the internal coordinate increases by the total shift, so
\[
f_a^m(jr+u)=jr+((u+1)\bmod r).
\]
Starting from any point, visits to successive blocks have period \(m\) and each return advances by one step on an internal \(r\)-cycle. Thus \(f_a\) is a single cycle of length \(mr\).

For a time \(t\) not divisible by \(m\), the target lies in the block numbered \((j+t)\bmod m\), different from \(j\). Therefore the sign of \(f_a^t(jr+u)-(jr+u)\) depends only on whether the new block index is above or below \(j\), and not on \(a\). For \(t=km\) with \(1\le k<r\),
\[
f_a^{km}(jr+u)=jr+((u+k)\bmod r),
\]
whose sign likewise does not depend on \(a\). Every admissible vector consequently gives the same complete signature. Choosing the first \(m-1\) shifts freely determines the final shift uniquely, yielding \(r^{m-1}\) distinct cycles in the fiber.

**2. Recovering the internal return permutation from the signs.** Conversely, suppose \(f\) is any single \(n\)-cycle with this signature, and put \(g=f^m\). As a power of a single \(mr\)-cycle, \(g\) has exactly \(m\) disjoint cycles, each of length \(r\). Its comparison signs (the signature at time \(m\)) assert
\[
g(jr+u)>jr+u\quad(0\le u<r-1),\qquad
g(jr+r-1)<jr+r-1.
\]
Thus the entire set of descending points \(\{x:g(x)<x\}\) is precisely
\[
D=\{r-1,2r-1,\ldots,mr-1\}.
\]
Every cycle of a permutation on a finite ordered set has at least one descending point: the largest element in that cycle maps to a smaller one. Here there are exactly \(m\) cycles and exactly \(m\) descending points, so each cycle has precisely one descending point, necessarily its maximum.

The cycle whose maximum is \(r-1\) contains \(r\) points and is contained in \(\{0,\ldots,r-1\}\), hence equals \(B_0\). Inductively, after removing \(B_0,\ldots,B_{j-1}\), the cycle whose maximum is \((j+1)r-1\) must comprise precisely the next \(r\) points \(B_j\). Consequently, the cycles of \(g\) are exactly the consecutive blocks. On each block all nonmaximal points map strictly right. Since \(g\) is a permutation of that block, the second-highest point must map to the highest, the third-highest to the second-highest, and so on; the highest maps to the lowest. Therefore
\[
g(jr+u)=jr+((u+1)\bmod r)
\]
for every \(j,u\). Notice that this identifies **the full return permutation**, not just its cycle supports.

**3. Recovering the block transition.** Because \(f\) commutes with \(g=f^m\), it permutes the \(g\)-cycles, hence maps each entire block \(B_j\) bijectively onto some \(B_{\sigma(j)}\). Comparing at time \(1\), every point of \(B_j\) moves strictly right when \(j<m-1\), while every point of the last block moves strictly left. No block can map to itself under a bijection having all pointwise displacements of one strict sign. Hence
\[
\sigma(j)>j\quad(0\le j<m-1),\qquad\sigma(m-1)<m-1.
\]
Since \(\sigma\) is a permutation, descending induction forces \(\sigma(m-2)=m-1,\sigma(m-3)=m-2,\ldots,\sigma(0)=1\), and then \(\sigma(m-1)=0\). Therefore \(\sigma(j)=(j+1)\bmod m\).

The intertwining relation \(fg=gf\) on each block now says that the bijection \(f:B_j\to B_{j+1}\) commutes with the standard cyclic rotations of the internal \(r\) coordinates. Such a bijection is necessarily an additive cyclic shift \(u\mapsto u+a_j\pmod r\). As \(f^m=g\), the total shift is \(\sum_j a_j=1\pmod r\). Thus \(f=f_a\) for exactly one admissible shift vector. This proves the upper bound matching Step 1 and establishes the exact fiber count.

**4. Exponential specialization.** When \(n=2m\), choose \(r=2\). The exact fiber size becomes \(2^{m-1}=2^{n/2-1}\). Distinguishing all candidates by any additional yes/no observations requires at least \(m-1\) binary answers in the worst case by cardinality.

The cycles may also be realized as finite periodic orbits of continuous interval maps: linearly interpolate the prescribed values \(f_a(j)\) at consecutive integers on \([0,n-1]\). All interpolated values remain in that interval, and the integers form the designated \(n\)-periodic orbit. No equivalence of other orbits or of global interval dynamics is asserted.

## Verification
The standalone `check_composite_cycle_signatures.py` independently forms the full \(n\)-cycle space for \(n\in\{4,6,8,9,10\}\) and counts the signature fibers for eight factorizations. It obtains exactly the predicted \(r^{m-1}\) in each case. It also enumerates every admissible shift vector for all sixteen pairs \(2\le m,r\le5\), verifying distinctness, a common full signature, and the actual orbit length. The exact output is saved in `CHECK_OUTPUT.txt`. These bounded computations are checks, not substitutes for the unbounded converse proved above.

## Relationship to prior work
Fuhrmann, Gröger and Passeggi (arXiv:2610.07435v1, Section 2) introduced the ordered-periodic-orbit left-right reconstruction problem. Their Lemma 2.1 proves uniqueness for cycles of prime length and their discussion immediately preceding it notes the existence of nonuniqueness for composite lengths, including an example on four points. They do not give this exact composite-length fiber family or the full converse classification. The published note *Quadratic-time reconstruction of prime cycles from left-right orbit signatures* gives a faster reconstruction algorithm in the prime case but does not address composite exact ambiguity. Classical work enumerating permutations with a specified one-step excedance set provides related combinatorial background, but equality of excedance data for **all powers simultaneously** is a stronger inverse datum than the one-step set.

## Limitations
The formula gives the exact fiber size for **one explicit signature at each chosen factorization**, not the largest possible fiber over all signatures and not the distribution of all fibers. It assumes the entire complete time-by-point signature is observed and that candidate maps are single \(n\)-cycles. It does not classify unordered orbital data without time labels, global continuous maps with the same period spectrum, or the topological types of interval extensions. Priority with respect to every older specialized enumeration theorem remains subject to independent assessment.

## References
1. G. Fuhrmann, M. Gröger, and A. Passeggi, *Period spectrum and rigidity of interval maps*, arXiv:2610.07435v1 (first posted 5 October 2026), especially Section 2 and Lemma 2.1. https://arxiv.org/html/2610.07435v1
2. *Quadratic-time reconstruction of prime cycles from left-right orbit signatures*, public research note (2026), full proof concerning prime lengths only.
3. R. Ehrenborg and E. Steingrímsson, *The excedance set of a permutation*, Advances in Applied Mathematics **24** (2000), 284–299, doi:10.1006/aama.1999.0671.
4. *Equivalence classes of permutations modulo excedances*, Journal of Combinatorics **5** (2014), 453–469, doi:10.4310/joc.2014.v5.n4.a4.

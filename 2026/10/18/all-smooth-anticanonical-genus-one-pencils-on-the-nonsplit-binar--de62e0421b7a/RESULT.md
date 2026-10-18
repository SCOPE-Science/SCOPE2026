# All-smooth anticanonical genus-one pencils on the nonsplit binary quadric

## Finding
Let \(Q\subset\mathbf P^3_{\mathbf F_2}\) be the nonsplit smooth quadric
\[
Q:\quad X_0X_1+X_2^2+X_2X_3+X_3^2=0.
\]
Let \(V=H^0(Q,-K_Q)=H^0(Q,\mathcal O_Q(2))\), a nine-dimensional vector space over \(\mathbf F_2\). Call a two-dimensional \(\mathbf F_2\)-subspace \(W\subset V\) *all-smooth* if each of the three nonzero sections in \(W\) defines a geometrically smooth divisor on \(Q\). These divisors are genus-one curves of degree four. Let \(b(W)\) be the number of \(\mathbf F_2\)-rational points in the scheme-theoretic base locus of \(W\).

Exactly **4,020** all-smooth pencils exist. They form **36** orbits under \(\operatorname{Aut}_{\mathbf F_2}(Q)\), of order \(120\). The complete joint distribution, distinguishing whether the length-eight base scheme is geometrically reduced, is:

| \(b(W)\) | Pencils | Automorphism orbits | Reduced base | Nonreduced base |
|---:|---:|---:|---:|---:|
| 0 | 1,440 | 13 | 1,200 | 240 |
| 1 | 1,920 | 16 | 1,680 | 240 |
| 2 | 540 | 6 | 260 | 280 |
| 3 | **120** | **1** | **120** | **0** |
| **Total** | **4,020** | **36** | **3,260** | **760** |

In particular, **\(b(W)\le 3\)** is sharp. The 120 equality pencils form a *single free orbit*, so their stabilizers in \(\operatorname{Aut}(Q)\) are trivial. Each equality pencil has three rational reduced base points and a single additional closed base point of degree five, giving the geometric Frobenius pattern \((1,1,1,5)\).

One equality pencil is spanned by
\[
F=X_1^2+X_0X_2,\qquad
G=X_1^2+X_2X_3+X_0X_3+X_1X_2.
\]
The three nonzero sections are \(F\), \(G\), and \(F+G\), and the common rational zeros on \(Q\) are \([1:0:0:0]\), \([1:1:1:0]\), and \([1:1:1:1]\).

## Assumptions and scope
Everything is defined over the field with two elements. Sections differing by a multiple of the defining quadratic equation of \(Q\) are identified. A curve is *geometrically smooth* only when its base change to an algebraic closure is smooth; testing rational points alone is insufficient. Distinct pencils are distinct two-dimensional vector subspaces, **not** pairs of chosen generators and **not** isomorphism classes of abstract genus-one curves. The three rational members alone must be smooth; singular members over field extensions are allowed. The base scheme is the complete intersection of \(Q\), \(F\), and \(G\), with scheme length eight by the intersection formula \((-K_Q)^2=8\).

## Proof
**Coordinate space.** The ten degree-two monomials in four variables, modulo the single relation \(X_0X_1=X_2^2+X_2X_3+X_3^2\), give a nine-dimensional space. The certificate uses the ordered basis
\[
(X_0^2,X_1^2,X_2^2,X_2X_3,X_3^2,X_0X_2,X_0X_3,X_1X_2,X_1X_3).
\]
A section is encoded as a nine-bit mask. Thus there are exactly \(2^9-1=511\) nonzero sections.

**Exact smoothness test.** Write \(q\) for the defining equation of the quadric and \(f\) for one of the 511 sections. The quadric is geometrically smooth. By the Jacobian criterion, \(Q\cap\{f=0\}\) is singular at a geometric point exactly when \(q=f=0\) and all six two-by-two minors of \((\nabla q,\nabla f)\) vanish. The four affine charts \(X_i=1\) cover projective three-space. On each chart, the corresponding ideal is the unit ideal over \(\mathbf F_2\) if and only if it has no common zero over the algebraic closure. Exact Gröbner-basis calculations over \(\mathbf F_2\) therefore decide geometric smoothness, not a bounded extension-field approximation. Precisely 240 of the 511 sections pass.

**Pencil census.** For distinct nonzero vectors \(a,b\) over \(\mathbf F_2\), their two-dimensional span has exactly the three nonzero vectors \(a,b,a+b\). The enumerator tests all pairs of geometrically smooth sections and retains the pair precisely when the third section is also smooth. Sorting the triple avoids duplicate generators. There are exactly 4,020 such triples. The five rational points of the nonsplit quadric, in four-bit projective coordinates, are \(1,2,7,11,15\), meaning respectively \([1:0:0:0]\), \([0:1:0:0]\), \([1:1:1:0]\), \([1:1:0:1]\), and \([1:1:1:1]\). The common zero tests at these five points give the first two numeric columns of the table.

**Projective orbit and reduced-base tests.** Exhaust all ordered bases of \(\mathbf F_2^4\) and retain precisely those linear changes preserving the quadratic polynomial \(q\). Equality can be checked from the four basis-vector values and six pairwise-sum values, which determine a homogeneous quadratic form over \(\mathbf F_2\). Exactly 120 transformations pass. They act on the nine-dimensional quotient of quadrics. Applying all 120 to every pencil representative partitions the 4,020 pencils into 36 orbits, with the displayed counts; the unique orbit with three rational base points has length 120. Base schemes are reduced exactly when the Jacobian of the three equations \(q,f,g\) has rank three at every geometric base point. The unit-ideal Gröbner tests for its four three-by-three minors, on the four affine charts, give the reduced/nonreduced columns, independently for all 36 orbit representatives.

**Geometric bound without the large census.** The five rational points constitute an ovoid: each rational plane section through three of them is a smooth conic. The four-dimensional kernel of evaluation of \(V\) at all five points has fifteen nonzero sections. Their exact representatives are the fifteen products of pairs of distinct rational secant planes whose three-point subsets together cover all five points. Every such section is reducible, hence singular. Consequently, a smooth section never vanishes at all five rational points. If two distinct smooth sections \(f,g\) both vanish at four rational points, they each take value \(1\) at the fifth, and their sum vanishes at all five, so \(f+g\) is singular. An all-smooth pencil therefore cannot have four or five rational base points. The displayed pair \(F,G\) proves sharpness at three.

**Residual degree-five point.** On the affine chart \(X_0=1\) for the displayed \(F,G\), lexicographic elimination of \((q,F,G)\) yields the univariate consequence
\[
X_3(X_3+1)(X_3^5+X_3^2+1)=0.
\]
The quintic factor is irreducible over \(\mathbf F_2\); exact Jacobian tests establish reducedness. Direct evaluation gives exactly the three listed rational base points. By the complete-intersection degree eight and reducedness, the remaining five points form one degree-five Galois orbit. The full 120-element automorphism group carries this residual Frobenius pattern to every maximal pencil.

## Verification
Run `python3 verify.py` in the package directory, with SymPy installed. The script derives every coefficient mask, performs all exact four-chart geometric Jacobian tests, exhausts the smooth-pencil set, enumerates the complete automorphism group, computes its orbits, certifies geometric reducedness, proves the fifteen-section ovoid-kernel decomposition, and verifies the extremal degree-five factor. It compares the full 36-orbit table and all aggregate counts to `data/expected.json` and exits with a nonzero status if any assertion fails. No arbitrary search cutoff or sampled finite extension substitutes for the exact Gröbner tests.

## Relationship to prior work
Asgarli and Ghioca's 2022 study of all-smooth pencils (first posted March 14, 2022) establishes general existence statements and constructs pencils of smooth quadric **surfaces** in projective three-space. That is not a census of pencils of smooth anticanonical **curves on one fixed nonsplit quadric**, and neither its existence statement nor its explicit construction determines the orbit, rational base-point or reducedness distributions above. Their earlier 2020 Bertini-pencil paper studies common transverse hyperplanes to hypersurface pencils, a different incidence problem. The present classification is about a fixed nonsplit degree-eight del Pezzo surface and the complete incidence geometry of its genus-one anticanonical pencils. Searches for equivalent formulations and small-field elliptic-quadric classifications did not identify the enumerated result; search absence does not establish publication priority.

## Limitations
The classification concerns only this nonsplit quadric over \(\mathbf F_2\), the chosen anticanonical linear system, and pencils whose three rational members are all geometrically smooth. It does not assert that all geometric members are smooth, classify all abstract genus-one pencils, or generalize the counts to other finite fields. The computation is finite but exhaustive, and priority against unindexed work is not independently certified. Base-scheme Frobenius patterns away from the maximal orbit are not classified; the general table distinguishes reducedness, not every finer scheme type.

## References
1. Shamil Asgarli and Dragos Ghioca, *Smoothness in Pencils of Hypersurfaces over Finite Fields*, arXiv:2203.07169, first posted 2022-03-14, Section 1 and Section 3. https://arxiv.org/abs/2203.07169
2. Shamil Asgarli and Dragos Ghioca, *A Bertini Type Theorem for Pencils over Finite Fields*, arXiv:2004.03479, first posted 2020-04-07, Introduction and Section 3. https://arxiv.org/abs/2004.03479
3. A. Melle-Hernández and C. T. C. Wall, *Pencils of Curves on Smooth Surfaces*, Proceedings of the London Mathematical Society 83 (2001), 257–278, DOI:10.1112/plms/83.2.257 (general context; only abstract inspected).

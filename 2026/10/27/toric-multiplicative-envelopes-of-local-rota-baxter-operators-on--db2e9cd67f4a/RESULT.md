# Toric multiplicative envelopes of local Rota–Baxter operators on maximal-nilindex evolution algebras

## Finding
Let \(E\) be any complex maximal-nilindex evolution algebra in the reduced normal form below, of dimension \(n\geq3\), and let \(\mathcal L\) be its set of **local weight-zero Rota–Baxter linear operators**. Let \(\mathcal S=\langle\mathcal L\rangle_\circ\) denote the semigroup of nonempty finite compositions, without adjoining an identity.

Write \(r\) for the final source index of a long-range square coefficient, taking \(r=0\) if no such coefficient occurs. Then the Zariski closure of \(\mathcal S\) is a pure-dimensional algebraic semigroup with **exactly \(n-r-2\) irreducible components**, all of dimension \(n+2\). The components are products of affine \(n\)-space with affine cones over rational normal curves. If there are at least two components, **every pair meets in the same affine \((n+1)\)-space**. The local-operator locus itself has dimension \(n+1\), so composition followed by algebraic closure increases the dimension by exactly one.

More explicitly, write an endomorphism in matrix-column convention as \(T(e_i)=d_i e_i+c_i e_n\) for \(i<n\), \(T(e_n)=c_n e_n\). The closure is \(\bigcup_{k=r+1}^{n-2}X_k\), where \(c_1,\ldots,c_n\) are arbitrary, \(d_i=0\) for \(i<k\), and, with \(h=n-k\) and \(y_j=d_{n-j}\) for \(1\leq j\leq h\), the remaining coordinates obey **all** equations
\[
 y_i y_{j+1}=y_{i+1}y_j\qquad(1\leq i<j\leq h-1).
\]
There are no other equations. In particular, for \(n=4\) and \(r=0\), the two components are the quadric \(d_1d_3=d_2^2\) and the linear component \(d_1=0\), with free last-row parameters and common intersection \(d_1=d_2=0\).

## Assumptions and scope
Work over \(K=\mathbb C\) and fix \(n\geq3\). The evolution algebra has a natural basis \(e_1,\ldots,e_n\), with \(e_i e_j=0\) for \(i\ne j\), and squares
\[
 e_i^2=e_{i+1}+\sum_{j=i+2}^{n-1}a_{ij}e_j\ (1\leq i\leq n-3),\quad e_{n-2}^2=e_{n-1},\quad e_{n-1}^2=e_n,\quad e_n^2=0.
\]
An empty sum is zero. Define \(I=\{(i,j):1\leq i\leq n-3,\ i+2\leq j\leq n-1,\ a_{ij}\ne0\}\) and \(r=0\) when \(I\) is empty, otherwise \(r=\max\{i:(i,j)\in I\}\). Thus \(0\leq r\leq n-3\).

A weight-zero Rota–Baxter map \(R:E\to E\) satisfies \(R(x)R(y)=R(R(x)y+xR(y))\) for all \(x,y\). A linear map \(T\) is *local* if, for every \(x\), some such \(R_x\) satisfies \(T(x)=R_x(x)\). Composition is ordinary composition of linear maps, unrelated to the evolution-algebra multiplication. We **do not** claim that compositions are again local Rota–Baxter maps. All dimensions and closures refer to the Zariski topology over \(\mathbb C\).

## Proof
**Step 1: independently recover the published local normal form.** The weight-zero classification of Qaralleh–Mukhamedov–Khakimov implies that an ordinary non-annihilator-valued Rota–Baxter map has a first diagonal index \(k>r\) and diagonal coefficients \(2^{n-i}\alpha\) for \(k\leq i\leq n\), with \(\alpha\ne0\); an annihilator-valued map sends everything into \(\mathbb C e_n\). For any local map, evaluating at basis vectors forces its image columns to contain only the original basis vector and \(e_n\). Evaluating at \(e_i+e_j\) for \(i<j<n\) forces nonzero diagonal indices to form a final interval and forces all ratios \(d_i/2^{n-i}\) on that interval to agree. Conversely, for any proposed final interval and arbitrary last-row coefficients, one can match its value at each vector \(x\) by an ordinary map: select as threshold the first nonzero \(x_i\) in that interval and adjust that threshold's free \(e_n\)-coefficient (or use an annihilator-valued map if the interval has no nonzero coordinates in \(x\)). This reconstructs Theorem 3.4 of the June 2026 source, including the sufficiency needed here:
\[
 \mathcal L=\{D(0)+e_nc^\mathsf T:c\in\mathbb C^n\}
 \ \cup\ \bigcup_{k=r+1}^{n-1}\{D(k,1,\alpha)+e_nc^\mathsf T:\alpha\in\mathbb C^\times,\ c\in\mathbb C^n\},
\]
where \(D(k,\ell,\alpha)\) is diagonal, its last entry is zero, and its entry in position \(i<n\) is \(0\) for \(i<k\) and \(\alpha2^{\ell(n-i)}\) for \(i\geq k\). Also \(D(0)=0\).

**Step 2: classify *every finite product*, including its free parameters.** For \(A=D+e_nc^\mathsf T\) and \(B=D'+e_nb^\mathsf T\) with final diagonal entries zero,
\[
 AB=DD'+e_n\bigl(c^\mathsf TD'+c_nb^\mathsf T\bigr).
\]
The diagonal part of any product of \(\ell\geq1\) factors with nonzero diagonal parts and thresholds \(k_1,\ldots,k_\ell\) is exactly \(D(k,\ell,\alpha)\), with \(k=\max k_s\) and \(\alpha=\prod_s\alpha_s\). If any factor has zero diagonal part, so does the product. No other matrix entries can occur. Conversely, fix any \(k,\ell,\alpha\) and desired final row \(c^\mathsf T\). Take \(\ell\) factors all with threshold \(k\), with scalar parameters \(\alpha,1,\ldots,1\); give the first \(\ell-1\) factors final row \(e_n^\mathsf T\) and the last factor final row \(c^\mathsf T\). Since \(e_n^\mathsf T A\) is the final row of \(A\), their product has exactly the prescribed final row. Therefore
\[
 \mathcal S=\{e_nc^\mathsf T:c\in\mathbb C^n\}
 \ \cup\ \bigcup_{k=r+1}^{n-1}\ \bigcup_{\ell\geq1}
 \{D(k,\ell,\alpha)+e_nc^\mathsf T:\alpha\in\mathbb C^\times,\ c\in\mathbb C^n\}.
\]
This is an exact, non-asymptotic description of the generated composition semigroup.

**Step 3: compute each toric closure.** For a fixed \(k\leq n-2\), the nonzero diagonal tail in the preceding display has \(h=n-k\geq2\) entries. In reverse order it is
\[
 (y_1,\ldots,y_h)=(\alpha t,\alpha t^2,\ldots,\alpha t^h),\qquad t=2^\ell.
\]
Because \(\{2^\ell:\ell\geq1\}\) is infinite, it is Zariski dense in \(\mathbb C^\times\). Allowing \(\alpha\) to vary in \(\mathbb C^\times\), the parameter pairs \((\alpha,t)\) used by finite products are dense in the two-dimensional torus. The closure of their diagonal images is the affine cone over the degree-\((h-1)\) rational normal curve, with the stated quadratic Hankel-minor equations.

For completeness, these equations generate the *entire* defining ideal: replace any monomial factor \(y_a y_b\) with \(b-a\geq2\) by \(y_{a+1}y_{b-1}\). Each replacement is a displayed minor relation, preserves total degree and the sum of indices, and decreases the sum of squared indices. It terminates in a product supported on at most two consecutive indices, uniquely determined by those two conserved quantities. Under \(y_j\mapsto s^{h-j}t^{j-1}\), two monomials map to the same monomial exactly when those quantities agree. Hence the quadratic relations generate the kernel of this parametrization and define its irreducible two-dimensional image closure. All final rows remain independent, giving \(X_k\cong\mathbb A^n\times C(\nu_{h-1}(\mathbb P^1))\) and \(\dim X_k=n+2\). The support \(k=n-1\) contributes only a final-diagonal axis, already contained in every \(X_k\) with \(k\leq n-2\); annihilator-valued maps are contained there too. Finite unions of closed sets are closed, so their union is exactly \(\overline{\mathcal S}^{\mathrm{Zar}}\).

**Step 4: identify all irreducible components and intersections.** Every \(X_k\) contains a point with \(d_k\ne0\) and \(d_i=0\) for \(i<k\), while any \(X_l\) with \(l>k\) has \(d_k=0\). If \(l<k\), a point of \(X_k\) with its entire nonzero tail cannot belong to \(X_l\): in \(X_l\), vanishing of its leading tail coordinate \(d_l\) forces \(d_{l+1},\ldots,d_{n-2}\) to vanish successively via the minor equations. Thus no \(X_k\) contains another; all are irreducible components. For \(k<l\), the same argument from \(d_k=0\) shows that in \(X_k\cap X_l\), \(d_1=\cdots=d_{n-2}=0\), while \(d_{n-1}\) and all \(c_i\) are free. This gives the common intersection \(\mathbb A^{n+1}\). There are \(n-r-2\) possible values of \(k\). The published local-operator normal form is a finite union of \((n+1)\)-dimensional affine families, yielding the asserted one-dimensional dimension jump.

## Verification
Run `python3 verify.py` from this directory. The verifier uses `fractions.Fraction`, exact integer/rational matrix products, and no numerical tolerance. It checks 2,658 nontrivial product cases for dimensions \(3\) through \(7\), all admissible obstruction thresholds, lengths through five, nonzero scalar parameters, vanishing of off-shape entries, the exact diagonal length formula, and every Hankel minor. It also checks free final-row realization through dimension eight and the explicit three-dimensional nonclosure witness \(\operatorname{diag}(4,2,0)^2=\operatorname{diag}(16,4,0)\). The expected success line begins `VERIFY_OK product_cases= 2658`. The infinite-density argument, prime ideal identification, and all-dimensional component theorem are proved above, not inferred from finite tests.

## Relationship to prior work
Qaralleh, Mukhamedov and Khakimov (January 2026, arXiv:2601.08669) classify **individual ordinary** weight-zero and weight-one Rota–Baxter maps on these maximal-nilindex algebras. Their June 2026 paper (arXiv:2606.22623), especially Theorem 3.4 and Proposition 5.1, classifies **individual local** weight-zero maps and their quasi-affine parameter strata. These classifications supply the input and fix the admissible threshold \(r\). Neither studied result determines the semigroup of all compositions, its algebraic multiplicative closure, its rational-normal-cone components, or their common intersection. Those are the present theorem's distinct conclusions.

Galuppi and Stanojkovski (2020/2021, arXiv:2002.02713), especially their Theorem 2 and Example 3, study Zariski closures of **cyclic** matrix semigroups and identify toric components. The present semigroup is generated by an **entire infinite family** of typically singular local operators with unrestricted last-row parameters and several threshold strata, not by powers of one matrix. A fixed-threshold diagonal sequence resembles their toric cyclic examples, but their results do not identify this full semigroup, the number of its components, their free row factors, or their common intersection. The rational-normal-curve minor ideal itself is standard. The contribution is its forced appearance, with complete component and intersection formulas, as the smallest Zariski-closed multiplicative envelope of the recently classified local operators. Published literature and indexed mathematical records were searched under composition-semigroup, geometric-tail, local Rota–Baxter, and toric-envelope formulations. No equivalent theorem was identified; lack of a match is not proof of global novelty.

## Limitations
The result is for the reduced maximal-nilindex class in characteristic zero over \(\mathbb C\); it does not cover positive characteristic, nonzero Rota–Baxter weights, arbitrary nilpotent evolution algebras, or operator addition closures. The exact finite-product set is generally not itself Zariski closed. The proof builds on the published classification of individual local maps, and does not reassert that classification as new. Relevant work not indexed or available during the literature check could reduce the originality assessment. Finite reproducibility checks do not certify general algebraic-geometry statements independently.

## References
- I. Qaralleh, F. Mukhamedov, O. Khakimov, *Local Rota--Baxter operators of weight zero on nilpotent evolution algebras with maximal nilindex*, first posted 2026-06-21, arXiv:2606.22623. https://arxiv.org/abs/2606.22623
- I. Qaralleh, F. Mukhamedov, O. Khakimov, *Rota--Baxter operators of nilpotent evolution algebras with maximal nilindex*, first posted 2026-01-13, arXiv:2601.08669. https://arxiv.org/abs/2601.08669
- F. Galuppi, M. Stanojkovski, *Toric varieties from cyclic matrix semigroups*, first posted 2020-02-07, arXiv:2002.02713; journal version 2021. https://arxiv.org/abs/2002.02713

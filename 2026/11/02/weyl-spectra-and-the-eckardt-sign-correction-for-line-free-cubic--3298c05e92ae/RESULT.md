# Weyl spectra and the Eckardt sign correction for line-free cubic surfaces

## Finding
Let \(S/\mathbb F_q\) be an arbitrary smooth cubic surface, \(B\) the reduced union of its 27 geometric lines, and \(U=S\setminus B\). Let \(w\in W(E_6)\) denote the action of geometric Frobenius on the set of lines and the geometric Picard group. Let \(L\) be the 27 lines, \(E\) the 135 unordered pairs of meeting lines, and \(F\) the 270 incidences of one line with one pair containing it. Denote by \(\ell_d,e_d,f_d\) the multiplicity of \(d\)-cycles of \(w\) on \(L,E,F\), respectively.

For every closed Eckardt point \(P\), write \(d_P=[\kappa(P):\mathbb F_q]\) and let \(\epsilon_P\in\{1,-1\}\) be the sign of the permutation on its three meeting geometric lines induced by \(w^{d_P}\). Then the **full rational zeta function** is
\[
Z(U,T)=\frac{\prod_{d\ge1}(1-T^d)^{\ell_d+e_d-f_d}(1-q^dT^d)^{\ell_d}}{(1-T)(1-q^2T)\det(1-qT w\mid\operatorname{Pic}(\overline S)\otimes\mathbb Q_\ell)}\prod_{P\text{ Eckardt closed}}(1-\epsilon_P T^{d_P}).
\]
In particular, the first-field point count in the absence of rational Eckardt points is the quadratic polynomial
\[
\#U(\mathbb F_q)=q^2+(\operatorname{tr}(w\mid\operatorname{Pic})-L_1)q+1-L_1+E_{11}-E_{\leftrightarrow},
\]
where \(L_1\) counts individually fixed lines; \(E_{11}\) counts intersecting unordered pairs whose two constituent lines are fixed; and \(E_{\leftrightarrow}\) counts intersecting pairs of lines swapped by Frobenius. In the presence of rational Eckardt points, subtract the sum of the signs of their three-line Frobenius permutations. No nonrational Eckardt point contributes to the first-field count.

Exact enumeration of all \(51{,}840\) elements of \(W(E_6)\) supplies all 25 conjugacy-class baseline spectra, represented by the attached `open_cubic_spectra.csv`. The 25 classes produce 25 distinct formal all-extension zeta sequences for the Eckardt-free baseline and 15 distinct quadratic polynomials for the first-field point count. This is a classification by possible Frobenius classes, not a claim that every class is realized by an Eckardt-free cubic over every finite field.

For the identity Weyl class, the formula specializes to
\[
\#U(\mathbb F_q)=q^2-20q+109-e,
\]
where \(e\) is the number of rational Eckardt points. For \(q=17\), two explicit split examples yield \(e=1\) and \(e=3\), hence respectively \(57\) and \(55\) rational points off all 27 geometric lines. Their ambient surfaces have the same Picard Frobenius and the same \(409\) rational points, but their open complements have different zeta functions.

## Assumptions and scope
All smooth cubic surfaces over any finite field are permitted, including characteristics two and three. The divisor \(B\) is the **reduced geometric union** of all 27 lines, not merely the union of individually rational lines. The zeta function means \(Z(U,T)=\exp(\sum_{n\ge1}\#U(\mathbb F_{q^n})T^n/n)\). Each geometric Eckardt point is incident with precisely three lines. The Picard action is on the rank-seven lattice, and the formal product in the displayed formula has finite support in \(d\).

The 25 Weyl classes are *possible* Galois actions; for any surface their actual Eckardt orbits must separately be supplied. The table does not claim independent realizability of every baseline class at every \(q\).

## Proof
**1. Smooth-surface contribution.** For a smooth cubic surface, the Tate-type point-count formula gives \(\#S(\mathbb F_{q^n})=q^{2n}+q^n\operatorname{tr}(w^n\mid\operatorname{Pic}(\overline S))+1\), hence
\[
Z(S,T)=\frac{1}{(1-T)(1-q^2T)\det(1-qTw\mid\operatorname{Pic}(\overline S)\otimes\mathbb Q_\ell)}.
\]
The identity is independent of the auxiliary prime \(\ell\ne\operatorname{char}(\mathbb F_q)\).

**2. The virtual double-point normalization model.** There are 135 unordered intersecting pairs of geometric lines. Replace each such pair formally by a distinct node and record its two incidences with lines, creating a finite 135-point scheme \(E\) and a 270-point scheme \(F\). This model has union-zeta ratio
\[
Z(B_{\mathrm{virtual}},T)=\prod_{d\ge1}(1-q^dT^d)^{-\ell_d}(1-T^d)^{-\ell_d-e_d+f_d}.
\]
Indeed, normalization is a disjoint union of \(27\) projective lines, grouped into Frobenius orbits, whose zeta is \(\prod_d[(1-T^d)(1-q^dT^d)]^{-\ell_d}\). For each finite singular-support point, normalization replaces its one value with its branches, giving the additional factor \(Z(E)/Z(F)\). This proves the expression if no Eckardt points occur.

**3. The local Eckardt correction.** At an Eckardt point, the virtual model has three pairwise intersections and six formal branches, whereas the actual divisor has one point and three branches. Consider the \(S_3\)-representations of the sets of the three lines, their three pairs, and the six oriented incidences. Their character combination for the actual-minus-virtual point counts is the **sign** representation: for the identity, a transposition, and a 3-cycle the respective differences are \(+1,-1,+1\). Explicitly, the character identity is \([\mathrm{one\ point}]+[\mathrm{six\ flags}]-[\mathrm{three\ lines}]-[\mathrm{three\ pairs}]=\mathrm{sgn}\). Thus the actual divisor has one extra \(\epsilon_P\) point-count term whenever an Eckardt orbit of degree \(d_P\) is fixed by Frobenius power \(d_P\). Its local zeta multiplier for the divisor is \((1-\epsilon_PT^{d_P})^{-1}\), and hence the multiplier for the *open* complement is \(1-\epsilon_PT^{d_P}\). Multiplying over closed Eckardt orbits establishes the general formula. This also handles the case where Frobenius permutes the three lines above a rational Eckardt point.

**4. Exact finite Weyl calculation.** Represent the 27 exceptional-curve classes on a blow-up of six points by the six exceptional classes, the 15 transforms of joining lines, and the six transforms of conics through five points. Their intersection form produces precisely 135 meeting pairs. Six simple-root reflections generate a group of exactly 51,840 permutations. Explicit conjugation by these generators yields exactly 25 conjugacy classes. The attached verifier computes cycles on all three sets, exact integral Picard matrices, characteristic polynomials, group orders and class sizes. Its class-size, element-order, and Picard-trace multiset exactly matches the independently published 25-class table of Banwait–Fité–Loughran. For every class it checks extension counts through degree 24 by two algebraically different computations (Frobenius-power fixed points and orbit-length sums). The first 24 extension coefficients separate all 25 formal baseline zeta sequences; first-extension polynomials have only 15 distinct values.

**5. Two explicit split examples.** Blow up \(\mathbb P^2_{\mathbb F_{17}}\) at the first five points
\[
(1:0:0),\ (0:1:0),\ (0:0:1),\ (1:1:1),\ (2:3:1)
\]
and take the sixth to be respectively \((6:4:1)\) and \((3:7:1)\). In both cases all six are distinct, no three are collinear, and no conic contains all six; therefore the anticanonical model is a smooth split cubic. On the complement of the exceptional curves, being off the 27 geometric lines is equivalent to avoiding the fifteen planar join-lines and six conics through five points. Exact evaluation over all 307 points of \(\mathbb P^2(\mathbb F_{17})\) gives 57 and 55 allowed points respectively. Independently, triple concurrence counts away from the six centers give zero and one Eckardt points; coincidences of two tangent directions on the exceptional components give one and two more. The totals are one and three, and \(58-e\) gives exactly 57 and 55. This proves that the Weyl action alone does not determine the open zeta function.

## Verification
Run `python3 verify_open_cubic.py --write-table open_cubic_spectra.csv` using Python 3 and its standard library only. The program regenerates its Weyl group, 135 edges, 270 flags and 25 classes, checks all displayed group-theoretic assertions, reproduces the explicit finite-field examples, compares the computed class multiset to the published class table, and ends with `VERIFY_OK`. A separately packaged CSV records the complete 25 evaluated formal spectra. The machine-check is a finite exhaustive verification of the named Weyl representation; the general point-count and local sign identities above provide the nonfinite mathematical proof.

## Relationship to prior work
Banwait, Fité and Loughran establish the Frobenius/Picard classification of cubic surfaces over finite fields, including the 25 conjugacy classes of \(W(E_6)\), traces, and line orbit types. The present result uses those facts; its distinguishing content is the evaluated zeta of the **complement of all 27 geometric lines**, the systematic orbit treatment of the 135 intersecting pairs and 270 pair-flags, and the signed correction for colliding pair-intersections at Eckardt points. Betten, Hirschfeld and Karaoglu give explicit line and Eckardt geometry in a split finite-field case, and Swinnerton-Dyer's classical work concerns the *ambient* surface zeta. The normalization formula itself is classical. All these components are acknowledged rather than claimed original in isolation.

## Limitations
This formula does not classify which Eckardt configurations occur in every Weyl class over every field. The 25-tabulated baselines are formal Frobenius classes; actual open-surface zeta functions also depend on Eckardt orbit data. For fixed small field sizes, distinct formal zeta signatures can numerically coincide. The two explicit surfaces are presented via blow-ups rather than cubic equations in four projective variables. The assessment of novelty is qualified by the possibility of implicit derivation from classical equivariant normalization results; it is not an independent audit or certification.

## References
1. B. Banwait, F. Fité, and D. Loughran, *Del Pezzo surfaces over finite fields and their Frobenius traces*, first public arXiv version 2016-06-01, arXiv:1606.00300, especially Section 7 and Table 7.1; https://arxiv.org/abs/1606.00300.
2. A. Betten, J. W. P. Hirschfeld, and R. Karaoglu, *Classification of cubic surfaces with twenty-seven lines over finite field of order thirteen*, 2017, DOI:10.1007/s40879-017-0182-0.
3. H. P. F. Swinnerton-Dyer, *The zeta function of a cubic surface over a finite field*, 1967, DOI:10.1017/S0305004100040895. The bibliographic abstract was consulted; full text was not available in this review.

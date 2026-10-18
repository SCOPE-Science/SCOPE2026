# Exact Minkowski symmetry of a rank-one fidelity cap in the semidefinite trace-one body

## Finding
Let \(d\ge 2\), let \(\mathbb F\in\{\mathbb R,\mathbb C\}\), let \(P=uu^*\) be a rank-one orthogonal projector on \(\mathbb F^d\), and let \(0<\delta<1\). Consider the spectrahedral cap
\[
\mathcal K_{d,\delta}(P)=\left\{X=X^*\succeq0:\operatorname{Tr}X=1,\ \operatorname{Tr}((I-P)X)\le\delta\right\}.
\]
Its optimized Minkowski reflection factor, defined by
\[
\operatorname{sym}(\mathcal K)=\max\left\{\alpha\ge0:\exists Z\in\mathcal K\ \forall X\in\mathcal K,\ (1+\alpha)Z-\alpha X\in\mathcal K\right\},
\]
is exactly
\[
\boxed{\operatorname{sym}(\mathcal K_{d,\delta}(P))
=\frac{\sqrt{(d-1-d\delta)^2+4(d-1)(1-\delta)}-(d-1-d\delta)}{2(d-1)}.}
\]
In particular, the value does not depend on the choice of \(P\) or on whether the matrices are real symmetric or complex Hermitian. Denoting the displayed value by \(\alpha_*\), an explicit Minkowski center is
\[
Z_*=(1-q_*)P+\frac{q_*}{d-1}(I-P),\qquad q_*=\frac{\delta}{1+\alpha_*}.
\]
The value increases strictly with \(\delta\). At \(\delta=(d-1)/d\) it is \(1/\sqrt{d(d-1)}\); as \(\delta\uparrow1\) it tends to \(1/(d-1)\), the symmetry of the unrestricted trace-one positive-semidefinite body. At the opposite singular limit,
\[
\lim_{\delta\downarrow0}\operatorname{sym}(\mathcal K_{d,\delta}(P))
=\frac{\sqrt{(d-1)(d+3)}-(d-1)}{2(d-1)}>0.
\]
This last limit is a limit of full-dimensional caps; at \(\delta=0\) the set reduces to the singleton \(\{P\}\) and the same full-dimensional symmetry definition is inapplicable.

## Assumptions and scope
All matrices are finite-dimensional. \(\mathbb F\) is either the real or complex field; \(X^*\) is transpose or conjugate transpose accordingly. \(d\) is an arbitrary integer at least two, \(P\) is any rank-one orthogonal projector, and \(0<\delta<1\) is arbitrary. The positive-semidefinite relation uses the Hermitian ordering. The set is viewed as a convex body in the *real* affine space of trace-one Hermitian matrices, of dimension \(d(d+1)/2-1\) for \(\mathbb R\) and \(d^2-1\) for \(\mathbb C\). It has nonempty relative interior since a positive-definite trace-one matrix can have strictly less than \(\delta\) weight on \(P^\perp\). No uniqueness of the Minkowski center is claimed.

## Proof
**1. The extreme points are pure states.** The cap is compact and convex. If \(X\) has rank \(r\ge2\), real self-adjoint perturbations \(H\) supported on \(\operatorname{ran}X\) form a space of dimension at least \(r(r+1)/2\ge3\), including in the complex case. The two linear conditions \(\operatorname{Tr}H=0\) and \(\operatorname{Tr}((I-P)H)=0\) therefore admit a nonzero solution. For sufficiently small \(\varepsilon>0\), both \(X\pm\varepsilon H\) remain positive semidefinite and satisfy the two trace constraints, so \(X\) is not extreme. Rank-one projectors are extreme even in the larger trace-one positive-semidefinite body. Consequently, by finite-dimensional compact convexity, the cap is the convex hull of the rank-one matrices \(vv^*\) with \(\|v\|=1\) and \(t:=\operatorname{Tr}((I-P)vv^*)\in[0,\delta]\).

**2. Reduce every possible optimum to an invariant center.** For a fixed \(\alpha\), the set of admissible centers satisfying \((1+\alpha)Z-\alpha X\in\mathcal K\) for all \(X\in\mathcal K\) is convex and invariant under conjugation by the orthogonal or unitary stabilizer of \(P\). Averaging over that compact group gives another admissible center of the form
\[
Z_q=(1-q)P+\frac{q}{s}(I-P),\qquad s=d-1,\quad 0\le q\le\delta.
\]
Applying the cap inequality to the reflected point obtained from \(X=P\) gives the necessary condition \((1+\alpha)q\le\delta\). For \(\alpha>0\), positive-semidefinite domination of all feasible rank-one projectors forces \(q>0\), because feasible pure states have nonzero transverse components.

**3. Positive-semidefinite domination is a scalar extremal inequality.** Reflection is positive semidefinite exactly when \(Z_q\succeq \beta X\) for each \(X\in\mathcal K\), where \(\beta=\alpha/(1+\alpha)\). For \(q\in(0,1)\), the rank-one determinant lemma (or the Sherman–Morrison criterion) yields
\[
Z_q\succeq \beta vv^*
\quad\Longleftrightarrow\quad
\beta\,v^*Z_q^{-1}v\le1,
\]
with
\[
v^*Z_q^{-1}v=\frac{1-t}{1-q}+\frac{s t}{q}.
\]
When \(q\le s/(s+1)\), this is increasing in \(t\), and the worst feasible vector has \(t=\delta\). Define
\[
G(q)=\frac{1-\delta}{1-q}+\frac{s\delta}{q}.
\]
For such \(q\), positive-semidefinite reflection for every point is equivalent to \(G(q)\le (1+\alpha)/\alpha\); the reduction from all points to pure states uses Step 1.

**4. Construct an attaining center.** Let \(\alpha_*\) be the unique positive root of
\[
s\alpha^2+(s-(s+1)\delta)\alpha-(1-\delta)=0.
\]
The polynomial at \(\alpha=\delta/s\) equals \(-(1-\delta)^2\), so \(\alpha_*>\delta/s\). It follows that \(q_*=\delta/(1+\alpha_*)<s/(s+1)\). Substitution of \(q_*\) into the formula of Step 3 and cancellation of the common positive denominators gives the *identity*
\[
G(q_*)=\frac{1+\alpha_*}{\alpha_*},
\]
precisely because the displayed quadratic vanishes. Hence every pure state, and then every member of the cap, satisfies \((1+\alpha_*)Z_*-\alpha_* X\succeq0\). The cap inequality follows from \((1+\alpha_*)q_*=\delta\), since for general \(X\) its reflected transverse weight equals \(\delta-\alpha_*\operatorname{Tr}((I-P)X)\le\delta\). The trace remains one. Thus \(Z_*\) attains at least \(\alpha_*\).

**5. Exclude every larger factor.** The strictly convex scalar function \(G\) has its unique minimum at
\[
q_{\mathrm{crit}}=
\frac{\sqrt{s\delta}}{\sqrt{1-\delta}+\sqrt{s\delta}}.
\]
Elementary squaring shows that \(q_{\mathrm{crit}}\ge\min\{\delta,s/(s+1)\}\): for \(\delta\le s/(s+1)\) it is at least \(\delta\), while for \(\delta\ge s/(s+1)\) it is at least \(s/(s+1)\). Step 4 gives \(q_*<\min\{\delta,s/(s+1)\}\), so \(G\) is strictly decreasing throughout \((0,q_*]\). If \(\alpha>\alpha_*\) were feasible, Step 2 would yield an invariant center with \(0<q\le\delta/(1+\alpha)<q_*\). Since \(q<s/(s+1)\), the pure states at transverse weight \(\delta\) require
\[
\frac{1+\alpha}{\alpha}\ge G(q)>G(q_*)=\frac{1+\alpha_*}{\alpha_*}.
\]
But the leftmost expression is strictly *smaller* than the rightmost for \(\alpha>\alpha_*\), a contradiction. This proves optimality.

**6. Boundary and monotonicity statements.** The quadratic has exactly one positive root because its constant term is negative. Substituting \(\delta=(d-1)/d\) makes its linear coefficient vanish. Taking the limits \(\delta\downarrow0\) and \(\delta\uparrow1\) gives the stated expressions. At \(\alpha=1/d\), the defining polynomial equals \(-1/d^2<0\), so \(\alpha_*>1/d\). Implicit differentiation therefore gives
\[
\frac{d\alpha_*}{d\delta}=\frac{d\alpha_*-1}{2(d-1)\alpha_*+(d-1)-d\delta}>0,
\]
where the denominator is the positive derivative of the quadratic at its positive root.

## Verification
The attached `check.py` independently evaluates the defining quadratic, the active reflection equality, and the two-dimensional boundary-block determinant at numerous integer dimensions and rational cap widths using 70-digit decimal arithmetic. It also checks the impossibility inequality at nearby larger candidate factors by a finite grid. The script runs as `python3 check.py` using the standard library only. These numerical tests are corroboration, **not** an infinite-dimensional or all-parameter proof; the proof above supplies the unrestricted quantifiers. The crucial pure-state reduction, symmetrization, rank-one PSD inequality, and scalar monotonicity are proved symbolically above, not inferred from tests.

## Relationship to prior work
Xiong and Freund's 2026 study introduces the optimized Minkowski reflection factor and proves a general symmetry-dependent ellipsoidal rounding theorem for arbitrary convex bodies. Its theorem does not evaluate that factor for the rank-one spectral expectation cap. The present exact formula supplies the input for the general bound: with the appropriate real affine dimension \(N\), an ellipsoidal rounding with factor \(\sqrt{N/\alpha_*}\) follows from their theorem, without a new claim of optimality for this ellipsoid factor. Belloni and Freund's earlier work develops general properties and center characterization; den Hertog, Pauphilet, and Soali formulate robust optimization procedures for Minkowski centers, including polyhedral and two-ellipsoid examples. Neither of those general treatments states the displayed all-dimensional positive-semidefinite cap formula in the inspected material. A two-dimensional real cap is affinely equivalent to a circular disk cut by a halfspace, but the theorem also covers non-ball spectrahedra of arbitrary size and complex Hermitian caps.

## Limitations
The result concerns a single rank-one spectral fidelity constraint and the *optimized Minkowski reflection factor*; it is not a formula for the John ellipsoid, Löwner ellipsoid, optimal rounding factor, or arbitrary multi-observable semidefinite sections. The singular endpoint \(\delta=0\) changes the affine dimension and is excluded. The result does not claim uniqueness of all centers. General convex geometry and semidefinite optimization literature is large; an equivalent specialized cap computation could exist outside the inspected sources. The numerical script is an independent reproducibility aid, not a replacement for the proof or independent expert audit.

## References
1. Zikai Xiong and Robert M. Freund, *Symmetry-dependence in Rounding of a Convex Body*, initially public 2026-08-31, arXiv:2608.30876, https://optimization-online.org/wp-content/uploads/2026/08/arxiv-sep23.pdf. The source identifies MSC2020 90C25 as its primary code.
2. Alexandre Belloni and Robert M. Freund, *On the Symmetry Function of a Convex Set*, Mathematical Programming 111 (2008), 57–93, DOI:10.1007/s10107-006-0074-4, https://doi.org/10.1007/s10107-006-0074-4.
3. Dick den Hertog, Jean Pauphilet, and Mohamed Yahya Soali, *Minkowski Centers via Robust Optimization: Computation and Applications*, Operations Research 72 (2024), 2135–2152, earliest online 2023, DOI:10.1287/opre.2023.2448, https://optimization-online.org/wp-content/uploads/2022/01/Minkowski_Final-1.pdf.

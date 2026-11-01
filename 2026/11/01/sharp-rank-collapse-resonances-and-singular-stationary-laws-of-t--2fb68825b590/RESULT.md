# Sharp rank-collapse resonances and singular stationary laws of the three-dimensional infinite-collapse map

## Finding

For real nonzero parameters \(a,b,c\), consider the three-dimensional reciprocal-sine map introduced by Yan, Jiang, Huang and Ding [1]:
\[
F_{a,b,c}(x,y,z)=\bigl(\sin(a/x)\sin(b/y)\sin(c/z),\ \sin(b/y)\sin(c/z),\ \sin(c/y)\sin(b/z)\bigr).
\]
Write \(\Omega=\{(x,y,z)\in\mathbb R^3:xyz\ne0\}\), \(\Delta=\{(x,y,z)\in\Omega:y=z\}\), and \(\Omega_\infty=\{p\in\Omega:F^n(p)\in\Omega\text{ for every }n\ge0\}\). Iteration and invariant probabilities are restricted to \(\Omega_\infty\); this avoids assigning a value to \(\sin(s/0)\).

**Theorem.** The following three statements are equivalent:

1. \(b^2=c^2\).
2. \(F_{a,b,c}(\Omega)\) is contained in the coordinate plane \(y=z\).
3. The full \(3\times3\) Jacobian determinant of \(F_{a,b,c}\) vanishes identically on \(\Omega\).

At these, and only these, parameter resonances the entire three-dimensional image collapses in one step. If \(c=\sigma b\), where \(\sigma\in\{-1,1\}\), the dynamics on \(\Delta\) are the exact triangular map
\[
(x,t)\longmapsto\bigl(\sigma\sin(a/x)\sin^2(b/t),\ \sigma\sin^2(b/t)\bigr).
\]
Every invariant Borel probability measure for the forward-defined dynamics on \(\Omega_\infty\) is supported on \(\Delta\), hence is singular with respect to three-dimensional Lebesgue measure. Every finite-time derivative \(D F^n\), for \(n\ge1\) along a forward-defined orbit, has rank at most two; it therefore has one identically zero singular value. There cannot be three positive finite Lyapunov exponents at resonance. These assertions are nonvacuous: there are infinitely many distinct fixed points in \(\Omega_\infty\) for every nonzero \(a,b\) and both signs \(\sigma\).

Conversely, if \(b^2\ne c^2\), the Jacobian has rank three on an open dense subset of \(\Omega\) whose complement has three-dimensional Lebesgue measure zero. In particular the resonant surfaces are the **entire** parameter locus on which the map is everywhere rank-deficient; generic nonresonant local dimension is three.

## Assumptions and scope

The parameters \(a,b,c\) are real and individually nonzero, as in equation (2) of [1]. The statements about rank and one-step images concern the open domain \(\Omega\), not its undefined zero-coordinate boundary. The measure statements concern Borel probability measures invariant under the well-defined self-map of \(\Omega_\infty\). No existence of an absolutely continuous invariant probability is asserted off resonance. Singular values, not a possibly ambiguous ordering of eigenvalues of a nonnormal derivative product, are used for the rank consequence. The parameter \(a\) is arbitrary and may coincide with either of the other parameters.

## Proof

Put \(U(t)=\sin(b/t)\) and \(V(t)=\sin(c/t)\). The second and third output coordinates are
\[
F_2(y,z)=U(y)V(z),\qquad F_3(y,z)=V(y)U(z).
\]
The plane \(\Delta\) is invariant for all parameters, because \(F_2(t,t)=F_3(t,t)\). If \(c=\sigma b\), then \(V=\sigma U\) everywhere and \(F_2=F_3=\sigma U(y)U(z)\) for all inputs. The displayed triangular map follows by substituting \(y=z=t\) into the first output as well. This proves \(1\Rightarrow2\Rightarrow3\).

For the converse and the generic rank assertion, define \(A(t)=U'(t)V(t)\) and \(B(t)=U(t)V'(t)\). Since the lower-left two entries of \(DF\) are zero, direct expansion along its first column gives
\[
\det DF(x,y,z)
=-\frac{a}{x^2}\cos(a/x)U(y)V(z)
\bigl(A(y)A(z)-B(y)B(z)\bigr).
\]
Along \(x=y=z=t\) with \(t\to+\infty\), Taylor expansion at the origin gives
\[
A(t)-B(t)=\frac{bc(b^2-c^2)}{3t^5}+O(t^{-7}),
\qquad A(t)+B(t)=-\frac{2bc}{t^3}+O(t^{-5}),
\]
so
\[
\det DF(t,t,t)=\frac{2ab^3c^3(b^2-c^2)}{3t^{12}}+O(t^{-14}).
\]
If \(b^2\ne c^2\) this is nonzero for all sufficiently large \(t\). The same conclusion holds at the points \((\varepsilon_x t,\varepsilon_y t,\varepsilon_z t)\) for every choice \(\varepsilon_x,\varepsilon_y,\varepsilon_z\in\{-1,1\}\): \(U,V\) are odd, their derivatives are even, and the two sign factors in the determinant cancel. On each of the eight open orthants of \(\Omega\), the determinant is real analytic and not identically zero. The zero set of a nonzero real-analytic function on a connected open set has empty interior and Lebesgue measure zero. Thus \(DF\) has full rank on an open dense full-measure subset of every orthant. In particular, \(3\Rightarrow1\), completing the equivalence.

At resonance the image of each point is in \(\Delta\). For an invariant probability \(\mu\) on \(\Omega_\infty\), invariance and the one-step inclusion imply
\[
\mu(\Delta)=\mu(F^{-1}(\Delta))=\mu(\Omega_\infty)=1.
\]
The plane has three-dimensional Lebesgue measure zero, so \(\mu\) is singular. The chain rule implies \(\operatorname{rank}D F^n\le2\) for all positive \(n\), proving the singular-value assertion without assuming smooth extensions to zero coordinates.

To exhibit infinitely many forward-defined fixed points, fix a sign \(\sigma\). The scalar equation for a diagonal fixed coordinate \(t=\sigma r\), with \(0<r<1\), is
\[
r=\sin^2(b/r).
\]
For sufficiently large integers \(k\), the continuous left-minus-right expression is positive at \(r_k=|b|/(k\pi)\), where the sine vanishes, and negative at \(s_k=|b|/((k+\tfrac12)\pi)\), where its square is one and \(s_k<1\). Consequently there are infinitely many positive roots \(r\) tending to zero. For any such \(r\), the first-coordinate fixed-point equation is
\[
x=\sigma r\sin(a/x).
\]
For arbitrarily small positive \(x\), the right side alternates between \(+r\) and \(-r\), with intervening zeros, so the intermediate value theorem supplies infinitely many solutions \(x\in(0,r)\). Each \((x,\sigma r,\sigma r)\) is nonzero and fixed by the full map, hence belongs to \(\Omega_\infty\). This completes the proof.

## Verification

The accompanying `verify.py` checks both resonant identities symbolically with SymPy, computes the displayed Laurent coefficients exactly and checks 200 numerical resonant evaluations and 12 fixed-point witnesses. Its successful output is `VERIFICATION_OK`. The proof above, including the real-analytic zero-set argument and the infinite fixed-point construction, is not inferred from finite tests.

## Relationship to prior work

Yan et al. [1] introduce exactly the three-coordinate map and investigate numerical attractors, Lyapunov exponents, sample entropy and an image-encryption application. The present theorem makes no claim of originality for the map, for its componentwise sine definition, or for generic numerical observations. Cao, Mao and Zhou [2] previously introduced the two-coordinate reciprocal-sine subsystem, which appears here exactly in the final two coordinates. In particular, simply observing that equal sine parameters make those two outputs agree is an immediate algebraic consequence of that earlier formula and is not, by itself, asserted as a novel mechanism. The evaluated contribution is the **sharp if-and-only-if global Jacobian-rank classification for the three-dimensional extension**, together with its complete stationary-support consequence and explicit nonvacuity via infinitely many fixed points.

A later treatment of the two-dimensional model in [3] restates its componentwise formula but does not imply the full-rank alternative or the three-dimensional stationary-support classification. The original article [1] was examined in full-text HTML; relevant definition, parameter evaluation and conclusions were compared. The mathematical definition and parameter discussion in [2] were examined in an available author-hosted PDF text extraction; its page-image retrieval was unavailable and it remains a residual inspection risk. Searches did not establish priority against all unindexed studies.

## Limitations

The map is undefined at zero coordinates; no extension through those singularities is assumed. Off resonance, an almost-everywhere nonzero Jacobian does not prove the existence of any three-dimensionally absolutely continuous invariant probability or any positive Lyapunov exponent. On resonance, rank loss does not rule out two positive Lyapunov exponents within the reduced triangular dynamics. There is no statement about finite-precision encryption security, chaotic mixing, or all initial data with finite-time singular orbits. The fixed-point construction does not classify all fixed points or all invariant measures on the diagonal. Independent mathematical review has not been performed.

## References

[1] W. Yan, Z. Jiang, X. Huang and Q. Ding, *A Three-Dimensional Infinite Collapse Map with Image Encryption*, Entropy 23 (2021), article 1221; published 2021-09-17. DOI: https://doi.org/10.3390/e23091221 . Full text: https://pmc.ncbi.nlm.nih.gov/articles/PMC8472400/ .

[2] W. Cao, Y. Mao and Y. Zhou, *Designing a 2D infinite collapse map for image encryption*, Signal Processing 171 (2020), 107457; first available online 2020-01-11. DOI: https://doi.org/10.1016/j.sigpro.2020.107457 . Author-hosted text: https://www.fst.um.edu.mo/personal/wp-content/uploads/2026/04/Designing2Dinfinite.pdf .

[3] X. Tang et al., *An image layered scrambling encryption algorithm based on a novel discrete chaotic map*, IET Image Processing (2023), DOI: https://doi.org/10.1049/ipr2.12651 , Section 2.3 (the two-dimensional infinite-collapse formula).

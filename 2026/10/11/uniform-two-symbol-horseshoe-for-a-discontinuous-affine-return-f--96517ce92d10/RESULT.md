# Uniform two-symbol horseshoe for a discontinuous affine return family

## Finding

Consider the discontinuous piecewise-affine map
\[
F_a(t)=\begin{cases}
(1+a)t-1,&t\geq0,\\
-(1+a)(a-1)^2t-(a^2+3a+3),&t<0.
\end{cases}
\]
For **every** real parameter in the explicit closed interval
\[
-\frac13-10^{-6}\leq a\leq-\frac13+10^{-6},
\]
there exists a compact invariant set \(K_a\) for \(F_a^{13}\) on which \(F_a^{13}\) is topologically conjugate to the one-sided full shift on two symbols. Every orbit on \(K_a\) avoids the discontinuity during its first thirteen steps, and hence throughout its evolution. With
\[
X_a=\bigcup_{j=0}^{12}F_a^j(K_a),
\]
the restriction \(F_a|_{X_a}\) is a continuous self-map of a compact space and satisfies
\[
h_{\mathrm{top}}(F_a|_{X_a})\geq\frac{\log 2}{13}>0.
\]
In particular \(F_a^{13n}\) has at least \(2^n\) distinct fixed points for every integer \(n\geq1\). This provides a finite exact-rational certificate for persistent symbolic chaos in the specific scalar map; no assertion about a corresponding invariant subsystem in an ambient two-dimensional map is made.

## Assumptions and scope

The family \(F_a:\mathbb R\to\mathbb R\) is defined exactly by the displayed formula, with the value at \(t=0\) taken from its nonnegative branch. It is the formal scalar map printed as Corollary 4.2 of Tikjha, *Noninvertibility and Bifurcation Phenomena in a Four-Partitions Piecewise Linear Map*, arXiv:2607.13519v1 (2026), §4.2. In that source the negative branch is obtained under additional partition-itinerary assumptions in the parent planar map. Consequently the present theorem is an unconditional assertion for the scalar formula, not a theorem lifting this invariant set to the planar map.

Define rational intervals
\[
J=[-21/10,-4/5],\quad C_0=[-1023/500,-1791/1000],\quad C_1=[-197/200,-841/1000].
\]
Both \(C_0\) and \(C_1\) lie in the interior of \(J\), are disjoint, and have rational endpoints. Symbols \(L\) and \(R\) indicate negative and nonnegative inputs, respectively. Set
\[
W_0=LRL^{11},\qquad W_1=L^{13}.
\]
The two words have length thirteen. All referenced sets and maps are compact metric objects in their inherited Euclidean topology; topological entropy is used only for the continuous restriction \(F_a|_{X_a}\), not for the globally discontinuous map on \(\mathbb R\).

## Proof

**1. Exact affine branches and center certificate.** At \(a=-1/3\) the branches reduce to
\[
L(t)=-\frac{32}{27}t-\frac{19}{9},\qquad R(t)=\frac23t-1.
\]
The interval \(I=[-19/9,95/243]\) is forward invariant at this central parameter: the closure of the image of its negative part under \(L\) is \(I\) (the endpoint \(t=0\) itself uses the right branch), and its nonnegative part maps strictly inside \(I\) under \(R\). In particular \(J\subset\operatorname{int}I\). (Forward invariance of this fixed \(I\) for perturbed parameters is not asserted or needed.)

Direct rational composition gives the following certified facts. For every \(t\in C_0\), the first thirteen branch choices are \(W_0\), and the affine map \(F_{-1/3}^{13}|_{C_0}\) has slope
\[
s_0=\frac23\left(\frac{32}{27}\right)^{12}>5.
\]
For every \(t\in C_1\), the corresponding word is \(W_1\), and the slope is
\[
s_1=-\left(\frac{32}{27}\right)^{13}<-5.
\]
Every intermediate input, from time zero to twelve, has absolute value greater than \(1/200\), so the asserted branch words are unambiguous. In both cases the image \(F_{-1/3}^{13}(C_i)\) contains \(J\) in its interior, extending beyond both ends by more than \(1/500\). The exact rational endpoints, inverse images of \(J\), and all inequalities are recomputed from the elementary affine rules by the attached standalone script `verify_horseshoe.py`.

**2. Uniform parameter certificate, without numerical sampling.** Use closed rational interval arithmetic on
\[
A=[-1/3-1/1000000,-1/3+1/1000000].
\]
For each of the thirteen steps and each word \(W_i\), the code encloses the image of the entire rational domain \(C_i\) under *every* parameter in \(A\). Each enclosure remains strictly on its designated side of zero before applying the next branch. Separately propagating each rational endpoint of \(C_i\) produces rational enclosures with the following strict outcomes throughout \(A\): for \(i=0\), the left endpoint maps below the left endpoint of \(J\) and the right endpoint maps above the right endpoint of \(J\); for \(i=1\), these two inequalities hold with endpoints reversed. An independent rational enclosure of each affine branch derivative verifies absolute slope greater than five throughout the closed band.

Every interval computation uses the four exact rational corner-products for multiplication and straightforward rational interval addition; it therefore remains an enclosure even when expressions reuse the same uncertain parameter. No random samples, floating-point bounds, or unproved computer-algebra simplifications enter. Since the chosen branch words are strict at every step, \(F_a^{13}\) is a continuous affine bijection from each \(C_i\) onto its image for each \(a\in A\), and the image contains \(J\) strictly.

**3. Symbolic repeller.** For each \(a\in A\), define \(D_i(a)=(F_a^{13}|_{C_i})^{-1}(J)\). The preceding facts make these two disjoint closed nonempty subintervals of \(\operatorname{int}C_i\), and each restriction \(F_a^{13}:D_i(a)\to J\) is an affine homeomorphism. Its inverse branch \(g_i:J\to D_i(a)\) contracts distances by a factor smaller than \(1/5\). For every infinite symbol sequence \(\omega\in\{0,1\}^{\mathbb N}\), the nested compact intervals
\[
g_{\omega_0}\circ\cdots\circ g_{\omega_{n-1}}(J)
\]
have diameters tending to zero uniformly and intersect in exactly one point \(\pi_a(\omega)\). Their images for distinct first symbols belong to separated \(C_0,C_1\); hence \(\pi_a\) is injective, continuous, and a homeomorphism onto its compact image \(K_a\). The identity
\[
F_a^{13}\circ\pi_a=\pi_a\circ\sigma
\]
proves topological conjugacy with the one-sided full two-symbol shift. All intermediate iterates of \(K_a\) avoid zero because they lie in the certified strictly signed images of \(C_i\). Consequently the union \(X_a\) is compact and invariant and \(F_a|_{X_a}\) is continuous. Entropy monotonicity and the identity \(h_{\rm top}(f^{13})=13h_{\rm top}(f)\) for a continuous compact-map restriction give the stated lower bound. Every period-\(n\) symbolic word provides a distinct fixed point of \(F_a^{13n}\), giving the fixed-point estimate.

## Verification

Run `python3 verify_horseshoe.py` from the folder containing that embedded file. It needs only the Python standard library. It recomputes the center-parameter branch compositions exactly, checks every stage against zero, verifies explicit image and inverse-image inequalities, and then checks the whole parameter band with outward-exact rational interval enclosures. The program reports **124 exact-rational assertions passed**. The proof above explains why those finite certificates imply an infinite symbolic subsystem; a finite numerical orbit by itself would not imply this result.

## Relationship to prior work

Tikjha (2026), §4.2 and Corollary 4.2, supplies the scalar piecewise-affine formula. Its Proposition 4.4 discusses an absorbing interval, Example 4.1 illustrates the negative-parameter case \(a=-0.3417\), and Remark 4.5 explains that the precise topology of the observed chaotic behavior rests on numerical evidence. These statements do not supply the two disjoint thirteen-step covering branches, an exact explicit parameter neighborhood, a two-shift conjugacy, or a quantitative entropy lower bound. This theorem supplies those additional claims for the printed scalar formula.

General horseshoe theory, symbolic coding by separated inverse branches, and entropy bounds are established standard tools, not claimed as new results. The specificity here is the exact rational construction and its uniform certificate for this recently studied return family. A full-text comparison of the publicly accessible 2026 preprint was made; the later journal version was not accessible in full, so a subsequently added overlapping argument cannot be excluded.

## Limitations

The theorem guarantees a compact symbolic *repeller*, not an attractor, unique physical measure, dense chaotic interval, full entropy of the ambient discontinuous map, or universal chaos for all negative parameters. The explicit rational parameter band is sufficient, not claimed maximal. In particular the derivation of the scalar negative branch from the parent planar system assumes a certain intermediate quadrant itinerary; that condition has **not** been established on the newly constructed horseshoe, so no two-dimensional lifting claim follows. Independent mathematical validation has not been performed.

## References

1. W. Tikjha, *Noninvertibility and Bifurcation Phenomena in a Four-Partitions Piecewise Linear Map*, arXiv:2607.13519v1, posted 15 July 2026, §4.2, Corollary 4.2, Proposition 4.4, Remark 4.5. https://arxiv.org/abs/2607.13519 . Full preprint available at https://www.researchgate.net/publication/410158976_Noninvertibility_and_Bifurcation_Phenomena_in_a_Four-Partitions_Piecewise_Linear_Map .
2. P. Glendinning and M. R. Jeffrey, *An Introduction to Piecewise Smooth Dynamics*, Springer, 2019, chapter 2, *Piecewise-smooth Maps*, DOI:10.1007/978-3-030-23689-2_2 (background on piecewise-smooth symbolic dynamics).

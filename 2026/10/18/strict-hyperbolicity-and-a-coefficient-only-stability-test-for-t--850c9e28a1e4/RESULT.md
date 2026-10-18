# Strict hyperbolicity and a coefficient-only stability test for three-strip Hamiltonian crossing cycles

## Finding

Every isolated transverse four-crossing periodic orbit of a planar system made of three affine Hamiltonian vector fields on the vertical strips has a strictly positive Floquet multiplier different from one. Its attraction or repulsion is decided by the **sign of a difference of two computable normal-velocity offsets**, independent of the travel times, the local center-versus-saddle types, and the quadratic coefficients in the second differential equation.

Specifically, with the definitions in the next section, put

\[
\mu=\frac{(A-b_C D)(B+b_C E)}{(B-b_C E)(A+b_C D)}.
\]

Then \(\mu>0\), \(\mu\ne1\), and

\[
\boxed{0<\mu<1\ \Longleftrightarrow\ A>B,
\qquad \mu>1\ \Longleftrightarrow\ A<B.}
\]

In particular, every such isolated crossing orbit is hyperbolic. A parameter-only algebraic reconstruction of \(D,E\), and hence of \(\mu\), is given below.

## Assumptions and scope

Partition the plane into \(x<-1\), \(-1<x<1\), and \(x>1\), labelled \(L,C,R\). In strip \(j\in\{L,C,R\}\), assume the *autonomous real affine Hamiltonian* field

\[
(\dot x,\dot y)=
(a_j x+b_j y+\alpha_j,\ c_j x-a_j y+\beta_j),
\quad
H_j(x,y)=\frac{b_j}{2}y^2-\frac{c_j}{2}x^2
+a_jxy+\alpha_jy-\beta_jx.
\]

No common choice of coefficients across strips, no globally crossing (sewing) assumption, and no spectral restriction on any strip's linearization is required. We only assume there is a **nonconstant, isolated, transverse periodic Filippov crossing orbit** with precisely four switches per period, in the cyclic order

\[
(1,y_0)\ (C\to R),\quad
(1,y_1)\ (R\to C),\quad
(-1,y_2)\ (C\to L),\quad
(-1,y_3)\ (L\to C).
\]

All four normal velocities from both adjacent strips are strictly nonzero and point in the designated crossing direction; between switches the trajectory stays strictly in the named strip. The four-crossing qualification matters: the statement is not a claim about trajectories with extra switches, grazing or sliding, or nonisolated periodic annuli.

Define the outer section midpoints and signed half-gaps by

\[
r=-\frac{a_R+\alpha_R}{b_R},\qquad
\ell=\frac{a_L-\alpha_L}{b_L},\qquad
D=\frac{y_0-y_1}{2},\qquad E=\frac{y_3-y_2}{2},
\]

and the *central normal-velocity offsets* by

\[
A=a_C+\alpha_C+b_C r,\qquad
B=-a_C+\alpha_C+b_C\ell.
\]

The hypothesis itself forces \(b_L,b_C,b_R\) to be nonzero and to have the same sign. In particular, \(b_C D>0\) and \(b_C E>0\). The transverse multiplier refers to the derivative of the local first-return map on \(x=1\) near the orbit, and not to the trivial tangent Floquet multiplier of the full planar monodromy.

## Proof

**1. Normal-velocity signs and outer involutions.** On each fixed vertical section, the corresponding Hamiltonian is quadratic in \(y\) and its derivative is exactly the normal velocity \(\dot x\). The two intersections at \(x=1\) must have opposite normal speeds for both the right and the central fields. Thus \(b_R\ne0\), \(b_C\ne0\), and, because the central speed is positive at \(y_0\) and negative at \(y_1\), \(b_C D>0\). The analogous argument at \(x=-1\) gives \(b_L\ne0\), \(b_C E>0\). Consequently the three \(b_j\) have the same sign. Conservation of the outer Hamiltonians and distinct intersection heights force

\[
y_0=r+D,\quad y_1=r-D,\quad
y_2=\ell-E,\quad y_3=\ell+E.
\]

Indeed, the outer half-return map in the \(y\) coordinate is locally exactly the affine reflection \(y\mapsto2r-y\) at the right interface and \(y\mapsto2\ell-y\) at the left interface. Each has derivative \(-1\).

**2. Matching the two central Hamiltonian flights.** Let \(K=H_C(1,r)-H_C(-1,\ell)\). Conservation on the right-to-left and left-to-right central excursions gives

\[
0=H_C(1,r-D)-H_C(-1,\ell-E)
=K-AD+BE+\tfrac12 b_C(D^2-E^2),
\]

\[
0=H_C(1,r+D)-H_C(-1,\ell+E)
=K+AD-BE+\tfrac12 b_C(D^2-E^2).
\]

Subtracting and averaging yield respectively

\[
AD=BE,\qquad
K+\frac{b_C}{2}(D^2-E^2)=0.
\tag{1}
\]

If \(A=0\), then (because \(D,E\ne0\)) \(B=0\), and conversely. In that case the second equation in (1) imposes a single relation on two nonzero signed gaps. In a neighborhood of the given transverse orbit, it yields a one-parameter family of actual closed crossing trajectories. This follows by the implicit function theorem: the gradient of \(D^2-E^2\) is \((2D,-2E)\ne(0,0)\), and strict first-hit transversality persists under small changes of the initial point.

If \(A=B\ne0\), (1) gives \(D=E\), and its second equation requires \(K=0\). Small nearby choices with \(D=E\) then also solve both matching conditions and, by the same transverse continuation, produce an annulus of periodic orbits. Neither exceptional case can occur for an isolated orbit. Thus \(A,B\ne0\), \(A\ne B\), and \(A/B=E/D>0\). It follows that \(A,B\) have the same sign and

\[
E=\frac{A}{B}D,\qquad
D^2=\frac{2[H_C(-1,\ell)-H_C(1,r)]}
{b_C(1-A^2/B^2)}.
\tag{2}
\]

The sign of \(D\) is uniquely specified by \(b_C D>0\). Formula (2) is an algebraic reconstruction for an orbit already known to exist; its positivity alone is **not** a sufficient existence or correct-itinerary criterion.

**3. Exact Poincaré derivative.** Each central first-hit map from a vertical section to the other is locally differentiable by the nonvanishing normal speed. Differentiating the equality of its initial and terminal Hamiltonian levels shows that its derivative in the vertical coordinate equals \(\dot x\) at the input divided by \(\dot x\) at the output. For the two central flights these factors are respectively

\[
\frac{A-b_CD}{B-b_CE}
\quad\text{and}\quad
\frac{B+b_CE}{A+b_CD}.
\]

The two outer reflection derivatives contribute \((-1)^2=1\), giving the stated return multiplier. By the direction of crossing, the four central speeds satisfy

\[
A+b_CD>0,\quad A-b_CD<0,\quad
B-b_CE<0,\quad B+b_CE>0.
\tag{3}
\]

Thus both numerator and denominator of \(\mu\) are negative and \(\mu>0\). Finally, algebra and (1) give

\[
\mu-1=
\frac{2b_C(AE-BD)}{(B-b_CE)(A+b_CD)}
=
\frac{2b_CD(A-B)(A+B)}{B(B-b_CE)(A+b_CD)}.
\tag{4}
\]

By (3), \((B-b_CE)(A+b_CD)<0\); by the first step \(b_CD>0\); and by \(A/B>0\), \((A+B)/B>0\). Therefore the sign of \(\mu-1\) is the negative of the sign of \(A-B\). Since isolated orbits require \(A\ne B\), the multiplier cannot equal one. The one-dimensional hyperbolic fixed-point theorem now gives local attraction for \(A>B\) and repulsion for \(A<B\).

## Verification

The accompanying `check.py` carries out exact-rational coefficient reductions for all six published examples (CCC, SCC, SCS, CSC, SSS and SSC) in Pessoa–Ribeiro, Section 4, and checks the ordering of their \(A,B\) offsets. All six have \(A<B\), predicting repulsion independently of residence time or the local equilibrium types. For their CCC Example 5,

\[
A=\frac23,\quad B=\frac{31}{24},\quad b_C=2,\quad
D=\frac{31}{48}\sqrt{\frac{1259}{235}},\quad
E=\frac13\sqrt{\frac{1259}{235}},
\]

and the exact formula yields \(\mu\approx7.1636898251743\). Numerical integration of the four named affine flows with event localization produces a return-map finite-difference derivative near \(7.1636898\), as reproduced by the checker when NumPy and SciPy are installed. Reversing the time direction in the same CCC example swaps \(A\) and \(B\) by common sign reversal and replaces \(\mu\) by its reciprocal, providing an attracting example. These finite checks are supplementary, **not** the proof of the theorem for infinitely many coefficients.

Reproduce with `python check.py`; optional numerical integration uses Python packages `numpy` and `scipy`. The exact-rational checks use only the standard library.

## Relationship to prior work

Pessoa and Ribeiro (2021, Theorem 4 and Section 4) establish at most one isolated crossing cycle for the three-zone Hamiltonian center/saddle configurations and construct six examples; their displayed results and the inspected full text do not establish the universal strict hyperbolicity, explicit transverse multiplier, or coefficient-only attraction criterion here. In particular, an upper bound of one on periodic cycles does not rule out an isolated neutral multiple fixed point.

Llibre and Valls (2021, Theorem 4, Section 6) treat the triple-saddle three-zone existence/uniqueness problem; the inspected article gives no corresponding coefficient-only Floquet classification. Carmona, Fernández-Sánchez and Novaes (2022 preprint, 2023 journal publication, Theorem A) prove hyperbolicity and a coefficient stability condition for **two-zone** sewing systems with a single switching line. Their theorem cannot cover a three-strip return with two distinct interfaces and locally possible sliding regions outside the cycle; neither their assumptions nor their dynamics imply this result. Three-zone existence works with some degenerate pieces, such as Fonseca–Llibre–Mello (2020) and Llibre–Valls (2022), overlap in objects but their accessible abstracts concern cycle counts rather than this transverse multiplier. Missing full-text comparisons for those two works remain a priority caveat.

## Limitations

This is a conditional structural classification: it does not claim a criterion for the existence of the four-crossing orbit, any global basin statement, any conclusion for grazing/sliding cycles, or a result for arbitrary itineraries with extra switches. The check uses a locally defined Filippov crossing flow. The proof handles arbitrary affine Hamiltonian piecewise fields under the stated transverse itinerary, without assuming all isolated equilibria, but does not establish a global uniqueness theorem beyond the literature's domain. Literature priority is assessed against inspected texts and search results; uninspected or inaccessible full texts may contain equivalent statements. Independent external audit has not been performed.

## References

1. C. Pessoa and R. Ribeiro, *Limit Cycles from Planar Piecewise Linear Hamiltonian Differential Systems with Two or Three Zones*, arXiv:2106.04638v1 (first public 2021-06-08), Theorem 4 and Section 4; https://arxiv.org/html/2106.04638v1 .
2. J. Llibre and C. Valls, *Limit Cycles of Planar Piecewise Differential Systems with Linear Hamiltonian Saddles*, *Symmetry* **13** (2021), 1128, Theorem 4 and Section 6; https://doi.org/10.3390/sym13071128 .
3. V. Carmona, F. Fernández-Sánchez and D. D. Novaes, *Uniqueness and Stability of Limit Cycles in Planar Piecewise Linear Differential Systems without Sliding Region*, arXiv:2207.14634 (2022), Theorem A; https://arxiv.org/pdf/2207.14634 .
4. A. F. da Fonseca, J. Llibre and L. F. Mello, *Limit Cycles in Planar Piecewise Linear Hamiltonian Systems with Three Zones Without Equilibrium Points*, *International Journal of Bifurcation and Chaos* **30** (2020), 2050157, DOI 10.1142/S0218127420501576 (abstract consulted).
5. J. Llibre and C. Valls, *Limit Cycles of Piecewise Differential Systems with Linear Hamiltonian Saddles and Linear Centres*, *Dynamical Systems* **37** (2022), 262–279, DOI 10.1080/14689367.2022.2037519 (abstract consulted).

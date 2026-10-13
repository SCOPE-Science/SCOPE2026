# Exactly seven transverse exceptional curves at both Desjardins–Winter non-torsion points

## Finding
Let \(S_j\), for \(j\in\{3.1,3.3\}\), be either of the two degree-one del Pezzo surfaces in Desjardins–Winter, Examples 3.1 and 3.3: each is the blow-up over \(\mathbb Q\) of eight specified rational points \(P_1,\ldots,P_8\) in \(\mathbb P^2\). Let \(Q=[0:0:1]\), regarded as a point of \(S_j\) away from the exceptional divisors, and let \(D_j\) be the reduced union of *all* \(240\) exceptional \((-1)\)-curves on \((S_j)_{\mathbb C}\).

In **both** examples, the complete set of components of \(D_j\) through \(Q\) consists of precisely the seven strict transforms
\[
L_{1,2},\quad L_{3,4},\quad L_{5,6},\quad L_{7,8},\quad C_{1,2},\quad C_{3,4},\quad Q_{2,6,7}.
\]
They are smooth at \(Q\) and have pairwise distinct tangent lines. Therefore the local germ \((D_j,Q)\) is an **ordinary sevenfold point**, with
\[
\delta_Q(D_j)=\binom{7}{2}=21,\qquad \mu_Q(D_j)=(7-1)^2=36.
\]
In particular, for these two fixed explicitly marked non-torsion points, no eighth exceptional curve passes through \(Q\).

## Assumptions and scope
All calculations take place over \(\mathbb Q\) or \(\mathbb C\) (characteristic zero); no claim about reduction modulo a prime is made. For each example the eight \(P_i\) are **exactly** the ordered homogeneous triples given in `verify.py`, transcribed from the primary source. The marked \(Q=[0:0:1]\) is distinct from all eight \(P_i\), so its blow-up neighborhood is unchanged. The source establishes the non-torsion property of \(Q\) on the relevant smooth elliptic fiber; the calculation below independently establishes only the complete exceptional-curve incidence and local tangent type. The definition of \(D_j\) includes every geometric exceptional curve, not only those rationally defined or listed in the source's example.

By the standard degree-one del Pezzo classification (Desjardins–Winter, Theorem 2.1), the \(240\) curves comprise the \(8\) blow-up exceptional divisors and \(232\) unique strict transforms of plane curves. The latter consist of:
\[
\begin{array}{c|c|l}
\text{degree}&\text{number}&\text{base-point multiplicities}\\\hline
1&28&1\text{ at a chosen pair}\\
2&56&1\text{ at a chosen five}\\
3&56&2\text{ at one},0\text{ at another},1\text{ elsewhere}\\
4&56&2\text{ at a chosen triple},1\text{ elsewhere}\\
5&28&2\text{ at a chosen six},1\text{ elsewhere}\\
6&8&3\text{ at one},2\text{ at the other seven}
\end{array}
\]
Here the source's label \(Q_{2,6,7}\) denotes a **quartic**, not the marked point \(Q\).

## Proof
For each of these \(232\) plane-curve multiplicity classes, form the homogeneous linear conditions on degree-\(d\) forms imposed by the indicated base-point jets. Use monomials \(x^iy^jz^{d-i-j}\) with \(i,j\geq0\), \(i+j\leq d\). At a homogeneous point \((a:b:c)\) with \(c\ne0\), the row imposing the affine Taylor coefficient of order \((u,v)\) (where \(u+v<m\)) has coefficient
\[
\binom{i}{u}\binom{j}{v}a^{i-u}b^{j-v}c^{d-i-j+u+v}
\]
for \(i\ge u,j\ge v\), and zero otherwise. This is the usual Taylor jet after clearing the common nonzero denominator. Append the single row evaluating the form at \(Q\); that row extracts the coefficient of \(z^d\).

All \(232\) possible multiplicity classes are considered; the \(8\) blow-up divisors cannot meet \(Q\). For each of the two examples, the appended matrix has full column rank over \(\mathbb F_{1000003}\) for exactly \(225\) classes. An integer minor nonzero modulo this prime remains nonzero over \(\mathbb Q\), and hence no complex form in any of these \(225\) classes can contain \(Q\). This finite-field step is therefore an exact characteristic-zero *exclusion certificate*, not an inference from samples.

For each of the remaining \(7\) classes, exact rational row reduction gives a one-dimensional base-jet kernel whose generating polynomial has vanishing \(z^d\) coefficient. These are precisely the seven displayed classes. Their nonzero linear Taylor terms at \(Q\), normalized as gradient pairs \((\partial_x f,\partial_y f)\) up to a scalar, are
\[
\begin{array}{c|rrrrrrr}
&L_{1,2}&L_{3,4}&L_{5,6}&L_{7,8}&C_{1,2}&C_{3,4}&Q_{2,6,7}\\\hline
\text{Example 3.1}&(1,0)&(0,1)&(1,-1)&(1,1)&(7,-6)&(6,-7)&(2,-1)\\
\text{Example 3.3}&(1,0)&(0,1)&(1,-1)&(1,1)&(33,52)&(52,33)&(13,4)
\end{array}
\]
Each row has seven nonzero pairwise nonproportional vectors. Because the blow-up is an isomorphism near \(Q\), these are exactly the tangent lines of the corresponding strict transforms. Thus the seven smooth local branches have distinct tangents; standard plane-curve singularity formulas yield the asserted \(\delta\) and \(\mu\).

As an independent check on the use of the classification, the verifier establishes general position by full-rank modular tests for all triples on a line, six-tuples on a conic, and the cubic systems with one double point. The degree-by-degree counts through \(Q\) in either example are
\[
(4/28,\ 0/56,\ 2/56,\ 1/56,\ 0/28,\ 0/8).
\]
The numerator counts curves through \(Q\); the denominator counts all degree-\(d\) classes.

## Verification
Run `python3 verify.py` using Python 3 standard library only. This regenerates the two source eight-point inputs, performs the complete \(232\)-class jet-rank census in each case, constructs exact rational generators for all seven admissible linear systems, and verifies pairwise distinct tangents. The completion marker is `VERIFY_OK examples=2 exceptional_curves=240 unique_through_Q=7 each ordinary_sevenfold=2 all_225_plane_exclusions_per_example_mod_1000003=PASS`. The listed prime is used only as a one-way proof of full rational rank for excluded linear systems; admitted curves and their tangents are checked with exact rational arithmetic.

## Relationship to prior work
Desjardins and Winter explicitly construct seven concurrent exceptional curves at each marked point and verify that both points are non-torsion; their Theorem 2.1 gives the full \(240\)-curve classification. The distinction here is the *complete* inclusion/exclusion of **every** exceptional class at those two marked points together with the pairwise-transverse local analytic type of the *entire* reduced exceptional divisor. Their investigation of whether eight exceptional curves can concur at a non-torsion point makes exactness at these natural boundary examples mathematically relevant. The van Luijk–Winter global upper bound and abstract weighted-clique data do not decide the full incidence of this pair of marked points with all \(240\) curves.

## Limitations
This is a classification for exactly two marked points on two explicit characteristic-zero surfaces, not a global upper bound on exceptional-curve concurrency, nor a decision of the open non-torsion eight-curve problem. Source-established non-torsion is not independently recertified by this arithmetic verifier. The local statement concerns the **reduced** divisor, not scheme-theoretic singularities of the product of all defining equations under arbitrary base change. Literature overlap outside the inspected open primary papers and indexed records remains possible; no independent audit has been performed.

## References
1. J. Desjardins and R. Winter, *Torsion points and concurrent exceptional curves on del Pezzo surfaces of degree one*, arXiv:2210.11659, first posted 21 October 2022; *Canadian Mathematical Bulletin* 68 (2025), 634–652, doi:10.4153/S0008439524000936. Relevant: Theorem 2.1, Examples 3.1 and 3.3, Section 5.
2. R. van Luijk and R. Winter, *Concurrent lines on del Pezzo surfaces of degree one*, arXiv:1906.03162 (global upper bounds and intersection configurations; not the marked census).

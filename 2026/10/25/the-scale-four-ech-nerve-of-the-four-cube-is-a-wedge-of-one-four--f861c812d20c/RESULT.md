# The scale-four Čech nerve of the four-cube is a wedge of one four-sphere and ten six-spheres

## Finding

The four-dimensional binary hypercube \(Q_4\), with Hamming shortest-path metric, has at Čech scale four the homotopy type

\[
\mathcal N(Q_4,4)\simeq S^4\vee\bigvee^{10}S^6.
\]

In particular, its degree-four Steenrod square \(\operatorname{Sq}^2:H^4(-;\mathbb F_2)\to H^6(-;\mathbb F_2)\) vanishes. This resolves the first previously tabulated even-scale homotopy-type case at \((n,r)=(4,4)\) in the natural wedge-of-spheres question of Adams, Shukla, and Singh. The previously published integral Betti numbers alone do not imply the wedge statement: the suspended Hopf attachment \(S^4\cup_{\eta_4}e^6\) has the same free homology pattern as \(S^4\vee S^6\), but its degree-two Steenrod square is nonzero.

## Assumptions and scope

The simplicial complex has vertices the binary words of length four, indexed by integers 0 through 15. For every vertex \(u\), set \(B_2(u)=\{v: \operatorname{wt}(u\oplus v)\le 2\}\), where \(\operatorname{wt}\) is Hamming weight. A subset is a face exactly when it lies in some \(B_2(u)\). Each of the sixteen generating facets contains eleven vertices. The scale convention agrees with closed balls of radius \(r/2=2\) in the geometric realization of the graph; this is not the scale-four Vietoris–Rips complex.

The only new homotopy claim is for this single natural complex. No claim is made about other cube dimensions or scales.

## Proof

**(1) Connectivity and integral homology.** Enumerating the sixteen radius-two balls yields the numbers of simplices of cardinalities one through eleven, respectively,

\[
(16,120,560,1780,3808,5272,4640,2560,880,176,16).
\]

In particular the complete two-skeleton on sixteen vertices is contained in \(X\), so \(X\) is simply connected. Adams–Shukla–Singh, Table 1, determined the *integral* reduced homology of this precise complex: \(\widetilde H_4(X;\mathbb Z)\cong\mathbb Z\), \(\widetilde H_6(X;\mathbb Z)\cong\mathbb Z^{10}\), and all other reduced groups vanish. Successive applications of the Hurewicz theorem show that \(X\) is three-connected. Independently, the supplied exact binary boundary calculation gives mod-two Betti vector \((1,0,0,0,1,0,10,0,0,0,0)\) in unreduced degrees zero through ten.

**(2) The Steenrod obstruction.** Work over \(\mathbb F_2\), using the fixed ascending order 0 through 15 on vertices and indexing every simplex of a given size by the increasing numerical value of its 16-bit vertex-set mask. The attached JSON certificate specifies a degree-four cocycle \(a\), a degree-four cycle \(z\), and a degree-five cochain \(b\) by their complete support-index lists. Their respective support cardinalities are 108, 24, and 116. Exact finite arithmetic verifies

\[
\delta a=0,\qquad \partial z=0,\qquad \langle a,z\rangle=1,\qquad \delta b=a\smile_2a.
\]

The cup-two product is evaluated using the normalized simplicial formula of Medina-Mardones, independently equivalent to the four-interval formula: on a six-simplex, sum over four-element subsets \(U\) of its seven ordered vertex positions, partitioning its elements \(u_j\) by the parity of \(u_j+j\), and evaluating \(a\) on the two faces obtained by deleting the respective parts. Only pairs leaving five vertices in each factor contribute. The computed square cochain has support 81; the attached checker verifies the entire 4,640-coordinate equality \(a\smile_2a=\delta b\), not merely an asserted zero rank. Thus \(\operatorname{Sq}^2[a]=0\). Since the published integral homology shows \(H^4(X;\mathbb F_2)\cong\mathbb F_2\), this is the full zero Steenrod-square operation.

**(3) Wedge-type conclusion.** Apply the standard low-dimensional Whitehead exact sequence for a three-connected CW complex, in this range:

\[
\pi_6(X)\longrightarrow H_6(X;\mathbb Z)\xrightarrow{\omega}H_4(X;\mathbb Z)\otimes\mathbb Z/2\longrightarrow\pi_5(X)\longrightarrow H_5(X;\mathbb Z)\longrightarrow0.
\]

The homomorphism \(\omega\) is dual modulo two to the primary Hopf attaching obstruction measured by \(\operatorname{Sq}^2:H^4(X;\mathbb F_2)\to H^6(X;\mathbb F_2)\). Hence the vanishing square forces \(\omega=0\) and \(\pi_6(X)\twoheadrightarrow H_6(X;\mathbb Z)\). By four-connectivity up to degree three, the Hurewicz isomorphism \(\pi_4(X)\cong H_4(X;\mathbb Z)\) gives a map \(S^4\to X\) representing the generator. Choose ten maps \(S^6\to X\) lifting a basis of \(H_6(X;\mathbb Z)\). Their wedge defines

\[
S^4\vee\bigvee^{10}S^6\longrightarrow X
\]

inducing an isomorphism on integral homology in every degree. Since both spaces are simply connected CW complexes, the homological Whitehead theorem makes this map a homotopy equivalence. This proves the stated complete homotopy type.

## Verification

Run `python verify_q4_cech_sq2.py` in the same directory as `q4_cech_sq2_certificate.json`, using Python 3.8 or newer. It reconstructs every face from sixteen radius-two balls, computes all mod-two simplicial boundary ranks, recomputes the cup-two square using a normalized independent subset-partition formula, verifies the cocycle and cycle, and compares all 4,640 coefficients of the square against the coboundary of the supplied five-cochain. Its exact success line is `Q4_CECH_SQ2_CERTIFICATE_OK`. Its numerical checks were executed on the contents of the attached artifact.

The computation is finite and exhaustive for this precisely specified sixteen-vertex simplicial complex. Integral homology in Step 1 is supplied by the cited original published computation, not inferred solely from mod-two ranks. The wedge inference in Step 3 is mathematical, using standard homotopy theory rather than a finite homotopy enumeration.

## Relationship to prior work

Adams, Shukla, and Singh introduced the precise Čech scale convention and tabulated the integral homology of \(\mathcal N(Q_4,4)\), but explicitly placed its *homotopy type* among the unknown entries and asked in Question 7.1 whether all such hypercube Čech nerves are wedges of spheres. The new homotopy conclusion supplies the missing operation-level information. Existing published classifications at scale three for \(Q_4\) and \(Q_6\) address different complexes and do not imply this result; neither do the known scale-two classifications. The explicit cup-two formula is standard rather than a new operation.

## Limitations

This establishes one specific case, not the general conjecture. The obstruction calculation is over \(\mathbb F_2\), and is sufficient only because this complex has integral homology in precisely the verified two dimensions, separated by two. The external integral homology result is used as an established premise; an independent integer Smith certificate is not supplied. The absence of a discovered equivalent statement in searchable records does not guarantee global novelty, and independent mathematical audit has not been performed.

## References

1. H. Adams, S. Shukla, A. Singh, *Čech complexes of hypercube graphs*, arXiv:2212.05871 (first publicly posted 12 December 2022), especially Section 3, Table 1, and Question 7.1, https://arxiv.org/abs/2212.05871.
2. U. Lupo, A. M. Medina-Mardones, G. Tauzin, *Persistence Steenrod modules*, Journal of Applied and Computational Topology **6** (2022), 475–502, Section 3.2, https://doi.org/10.1007/s41468-022-00093-7.
3. G. W. Whitehead, *Elements of Homotopy Theory*, Springer, 1978: homology and homotopy exact sequences for highly connected spaces; homological Whitehead theorem.

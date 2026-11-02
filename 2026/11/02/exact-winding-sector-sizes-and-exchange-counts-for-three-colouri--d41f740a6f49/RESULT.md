# Exact winding-sector sizes and exchange counts for three-colourings of circular ladders

## Finding

Let \(P_n=C_n\square K_2\) be the labelled circular ladder (prism) with \(n\ge3\), with upper and lower vertices \(u_i,v_i\) for \(i\in\mathbb Z/n\mathbb Z\). Let \(\mathcal R_n\) contain every proper colouring of \(P_n\) by the three *named* colours \(0,1,2\), with an edge when exactly one vertex changes colour and the result remains proper. Unused colours are allowed (although no proper colouring of an odd prism uses fewer than three).

Write \(\sigma(a,b)=1\) if \(b-a\equiv1\pmod3\), and \(\sigma(a,b)=-1\) otherwise, for distinct colours \(a,b\). For a colouring \(c\), its winding is
\[
w(c)=\frac13\sum_{i\in\mathbb Z/n\mathbb Z}\sigma(c(u_i),c(u_{i+1})).
\]
The numerator is divisible by three. Put \(T(z)=z^{-1}+1+z\), \(t_m(s)=[z^s]T(z)^m\), and
\[
\mathcal W_n=\{w\in\mathbb Z:\ |3w|\le n,\ w\equiv n\pmod2\}.
\]
For every \(w\in\mathcal W_n\), exactly \(N_n(w)=6t_n(3w)\) proper colourings have winding \(w\). Their induced recolouring subgraph has precisely
\[
E_n(w)=6n\bigl(t_{n-1}(3w)+t_{n-2}(3w)\bigr)
\]
edges. No other winding occurs. The complete connected-component classification is:

* If \(|3w|<n\), the entire winding sector is **one connected component**, of order \(N_n(w)\) and size \(E_n(w)\).
* If \(|3w|=n\), which is possible only for \(3\mid n\), the sector consists of exactly **six isolated colourings**.

Thus \(\mathcal R_n\) has \(|\mathcal W_n|+10\mathbf1_{\{3\mid n\}}\) connected components. The total number of proper three-colourings is the previously known chromatic-polynomial specialization \(3^n+1+2(-2)^n\); the sectorwise sizes, edge counts and resulting full component census are the claims of interest. For example, for \(n=8\), its three components have \((N,E)=(216,384),(6642,25632),(216,384)\) at respective windings \(-2,0,2\).

## Assumptions and scope

All graphs are finite simple graphs; the cyclic prism is defined for each integer \(n\ge3\) (so the triangular prism is included). The two rims are distinguished and oriented by increasing cyclic index solely to define the *signed* winding; the component census is independent of the choice of rim or orientation. The colour labels remain distinguished, including in the six singleton configurations at extremal winding. \([z^s]\) denotes an ordinary Laurent-polynomial coefficient, not a generating-function limit. The reconfiguration move changes **one vertex colour**, not a Kempe-chain interchange, an edge colouring, or a simultaneous recolouring.

The coefficient is computable without symbolic algebra by
\[
t_m(s)=\sum_{\substack{|s|\le j\le m\\j\equiv s\ (\mathrm{mod}\ 2)}}\binom{m}{j}\binom{j}{(j+s)/2},
\]
with \(t_m(s)=0\) if \(|s|>m\). Thus every count in the statement is a finite integer expression for arbitrary \(n\).

## Proof

**1. Winding invariant.** A proper three-colouring of a directed edge has weight \(+1\) or \(-1\) according to its increment modulo three. Its oriented sum on any closed cycle is divisible by three. A legal recolouring of a vertex requires all of its neighbours to carry the same colour; the two edge weights on an oriented cycle through this vertex therefore sum to zero both before and after recolouring. Hence the oriented cycle weights, in particular \(3w\), are invariant. Each quadrilateral side face of the prism has weight zero: its four signs sum to a multiple of three and have even parity, so their sum must be zero. Accordingly the two rims have the same winding, and every cycle weight is determined by the top-rim winding, since face boundaries together with one rim generate the integral cycle space of the cylindrical embedding.

**2. Component classification from the established general three-colouring criterion.** Cereceda, van den Heuvel and Johnson's fixed-vertex/weight characterization (their Proposition 3 and Theorem 7) says that two three-colourings are connected if they agree on all fixed vertices and preserve cycle weights and weights of paths between fixed vertices. Their Proposition 3 places every fixed vertex on a consistently cyclically coloured directed cycle or on a consistently coloured path between such cycles. Here a contractible prism cycle has weight zero, so cannot be consistently directed. Every noncontractible *simple* prism cycle winds once around the cylinder and has length at least \(n\); its signed weight is \(\pm3w\). Thus, when \(|3w|<n\), no consistently directed cycle exists and the fixed-vertex set is empty. Any two colourings with this winding then have equal weights on every cycle and meet the general characterization, proving their connectivity. In the extremal case \(|3w|=n\), every sign on both rims is the same; every vertex lies on a consistently directed rim and is frozen. The transfer count below shows there are exactly six such colourings for each extremal winding, each an isolated vertex. This step **uses** the general reachability theorem and does not claim it as new.

**3. Exact sector cardinalities.** At each rung write \(a_i=c(u_i)\in\mathbb Z/3\mathbb Z\) and \(\epsilon_i\in\{-1,+1\}\) with \(c(v_i)=a_i+\epsilon_i\pmod3\). Let \(s_i=\sigma(a_i,a_{i+1})\). If \(\epsilon_{i+1}=\epsilon_i\), either \(s_i=+1\) or \(-1\) is allowed. If \(\epsilon_{i+1}=-\epsilon_i\), the single legal choice is \(s_i=\epsilon_i\). With rows/columns indexed by \(+1,-1\), the Laurent-weighted transition matrix is
\[
B(z)=\begin{pmatrix}z+z^{-1}&z\\z^{-1}&z+z^{-1}\end{pmatrix}.
\]
A closed walk in the two orientation states with exponent \(s\equiv0\pmod3\) yields exactly three colourings, one for each initial upper colour. Therefore the winding-\(w\) count is \(3[z^{3w}]\operatorname{tr}B(z)^n\). The eigenvalues of \(B\) are \(z+z^{-1}+1\) and \(z+z^{-1}-1\). On the coefficient of \(z^{3w}\), the two eigenvalue powers contribute equally when \(3w\equiv n\pmod2\), and cancel otherwise, giving \(N_n(w)=6t_n(3w)\). This also proves the asserted set of possible windings and six extremal states.

**4. Exact exchange counts.** A vertex has exactly one legal recolouring if and only if its three neighbours all have the same colour. Fix an upper vertex at rung \(i\). Its recolourability forces the two upper horizontal increments to equal \(-\epsilon_i\) and \(+\epsilon_i\), respectively. Sum over the two possible central orientations. The marked two-transition matrix between the orientation states before and after rung \(i\) is consequently \(M=2J\), where \(J\) is the two-by-two all-ones matrix; both horizontal weights multiply to \(z^0\). Thus the number of colourings at winding \(w\) in which this specified upper vertex is recolourable equals
\[
R_n(w)=3[z^{3w}]\operatorname{tr}\bigl(MB(z)^{n-2}\bigr).
\]
With \(a=z+z^{-1}\), the trace is
\[
\operatorname{tr}(MB^{n-2})=(a+2)(a+1)^{n-2}+(2-a)(a-1)^{n-2}.
\]
For \(w\in\mathcal W_n\), the two terms have equal \(z^{3w}\)-coefficients, and \(a+2=T(z)+1\), whence \(R_n(w)=6(t_{n-1}(3w)+t_{n-2}(3w))\). By row-exchange and cyclic symmetry, the total degree sum in the winding sector is \(2nR_n(w)\). Every recolouring is counted at its two ends, so \(E_n(w)=nR_n(w)\). All edges remain within their winding sector by Step 1, completing the classification.

## Verification

The standalone scripts `check_components.py` and `check_transfer.py` use only the Python standard library. Run each with `python3 <filename>`. The first generates all proper named three-colourings by admissible explicit rung pairs and constructs every one-vertex recolouring edge. It computes full connected components and their winding labels for all \(3\le n\le10\). The second independently multiplies Laurent-polynomial transfer matrices, checks the component-size and marked-recolourability coefficient identities for \(3\le n\le30\), and also compares against a separate six-state transfer model for \(3\le n\le9\). Both passed on the distributed source files. These computations corroborate, but do not substitute for, the proof for all integer \(n\ge3\).

Representative direct exhaustive counts are: \(n=3\): twelve singletons; \(n=4\): one component with \((114,240)\); \(n=6\): one \((846,2520)\) component plus twelve singletons; \(n=8\): \((216,384),(6642,25632),(216,384)\); \(n=10\): \((3690,11520),(53718,254760),(3690,11520)\).

## Relationship to prior work

The general fixed-vertex and cycle-weight connectivity criterion for all proper three-colourings is due to Cereceda, van den Heuvel and Johnson. In particular, the winding *obstruction* and the ability to determine reachability in any fixed graph are **known**, not part of the originality claim. Their broader mixing work also treats bipartite graphs and three-chromatic graphs. Earlier prism chromatic-polynomial formulas determine the total number of colourings but not, in the inspected treatments, the exact numbers of vertices and edges in each single-vertex-recolouring component.

The contribution isolated here is the simultaneous **closed component order and edge enumeration at every admissible winding**, together with the sharp identification of the twelve extremal singleton configurations when the period is a multiple of three. This is a componentwise refinement of chromatic enumeration rather than another solution of the general reachability decision problem. Kempe-chain recolouring is a different, less restrictive move and cannot be substituted for the single-vertex operation in the theorem.

## Limitations

This result is specific to three named colours and circular ladders; it does not assert analogous formulas for wider cylindrical grids, four-colouring graphs, Kempe components, reconfiguration diameters or mixing times. Historical sources may contain an equivalent winding-refined count under height-function/three-state Potts terminology. The standard general connectivity characterization provides the crucial qualitative ingredient; without it, the enumeration alone would not establish connectedness. The full text of some auxiliary historical colour-mixing papers was not accessible, and originality is therefore subject to comparison with such sources. No independent scholarly audit has been performed.

## References

1. L. Cereceda, J. van den Heuvel, M. Johnson, *Finding Paths Between 3-Colourings*, research report LSE-CDAM-2007-31 (December 2007, day of initial public posting not established); *Journal of Graph Theory* **67** (2011), 69–82; DOI: 10.1002/jgt.20514. Author-posted full-text presentation: https://www.researchgate.net/publication/220266583_Finding_Paths_Between_3-Colourings . Publisher first-online date: 2010-12-16.
2. L. Cereceda, J. van den Heuvel, M. Johnson, *Mixing 3-Colourings in Bipartite Graphs*, *European Journal of Combinatorics* **30** (2009), 1593–1606; DOI: 10.1016/j.ejc.2009.03.011.
3. R. C. Brewster, J. A. Noel, *Mixing Homomorphisms, Recolorings, and Extending Circular Precolorings*, *Journal of Graph Theory* **80** (2015), 173–198; DOI: 10.1002/jgt.21846.
4. J. Allagan, V. Voloshin, V. Deriglazov, R. N. Lopez-Bonilla, *Explicit Equimodular Curves for Prism-Graph Chromatic Polynomials and the Beraha–Kahane–Weiss Limit Set*, *American Journal of Computational Mathematics* **16** (2026), 14–26; DOI: 10.4236/ajcm.2026.161002. This later article concerns chromatic polynomials and their roots, not reconfiguration-component orders or edges.
5. P. Bonsma, L. Cereceda, J. van den Heuvel, M. Johnson, *Finding Paths between Graph Colourings: Computational Complexity and Possible Distances*, *Electronic Notes in Discrete Mathematics* **29** (2007), 463–469; DOI: 10.1016/j.endm.2007.07.073. Public publication date 2007-08-15, as recorded by Durham University’s repository. This earlier study supplies background for the three-colour reachability question, not componentwise enumeration.

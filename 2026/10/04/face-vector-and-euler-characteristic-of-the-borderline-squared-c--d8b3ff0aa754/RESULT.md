# Face vector and Euler characteristic of the borderline squared-cycle cut complexes
## Finding
For every integer \(k\ge 3\), put \(n=k+5\) and let \(W_n=C_n^2\) be the square of the cycle on \(n\) vertices. The ordinary \(k\)-cut complex \(\Delta_k(W_n)\) has face vector
\[
(f_0,f_1,f_2,f_3,f_4)=\left(n,\binom n2,\binom n3,\frac{nk(k+2)}2,\frac{nk(k-1)}2\right).
\]
Consequently,
\[
\widetilde\chi(\Delta_k(W_n))=\frac{k^3-19k+24}{6}.
\]
If the homotopy-shape conjecture \(\Delta_k(W_{k+5})\simeq S^3\vee\bigvee^{\beta(k)}S^4\) holds, then necessarily
\[
\beta(k)=\frac{(k-3)(k-2)(k+5)}6
\]
for every \(k\ge3\). Thus the numerical formula reported from computations for \(3\le k\le15\) follows formally from that homotopy shape once the exact Euler characteristic above is known.

## Assumptions and scope
The graph \(W_n\) has vertex set \(\mathbb Z/n\mathbb Z\), with two vertices adjacent when their cyclic distance is one or two. By definition, a facet of \(\Delta_k(W_n)\) is the complement of a disconnected induced \(k\)-vertex subgraph. Since \(n=k+5\), every facet has five vertices and the complex is four-dimensional.

For a subset \(S\subseteq\mathbb Z/n\mathbb Z\), a run means a maximal nonempty block of cyclically consecutive vertices of \(S\). The argument below concerns the five-vertex facet set \(S\); its complement is the induced \(k\)-vertex graph whose disconnectedness defines the facet.

## Proof
First observe the following run criterion. Contract each maximal run of vertices outside \(S\) to one vertex. Two consecutive outside-runs are joined in \(W_n[V\setminus S]\) exactly when the intervening run of \(S\) has length one: a single missing cycle vertex is bridged by a distance-two edge, whereas a missing run of length at least two leaves cyclic distance at least three across that gap. Hence \(W_n[V\setminus S]\) is disconnected exactly when at least two runs of \(S\) have length at least two.

For a five-set \(S\), the only run partitions satisfying this criterion are \((3,2)\) and \((2,2,1)\). In type \((3,2)\), choose the initial vertex of the unique three-run in \(n\) ways and split the \(k\) retained vertices into two positive cyclic gaps in \(k-1\) ways. In type \((2,2,1)\), choose the unique singleton in \(n\) ways and split the \(k\) retained vertices into three positive cyclic gaps in \(\binom{k-1}{2}\) ways. Therefore
\[
f_4=n\left((k-1)+\binom{k-1}{2}\right)=\frac{nk(k-1)}2.
\]

A four-set is a face exactly when one more vertex can be added to obtain one of those five-set facet types. Its run partition must therefore be one of \((3,1)\), \((2,2)\), or \((2,1,1)\). Conversely, each of these three types extends to a facet: because \(n=k+5\ge8\), the positive cyclic gaps have enough total length to extend an appropriate run without merging the two separating long runs. The counts are, respectively,
\[
nk,\qquad \frac{nk}{2},\qquad n\binom{k}{2}.
\]
Indeed, for type \((3,1)\) there are \(n\) choices for the three-run and \(k\) positive two-gap compositions of \(k+1\); for type \((2,2)\) the same marked-run count is divided by two because the two runs are equal; and for type \((2,1,1)\) the unique two-run gives \(n\) choices followed by \(\binom{k}{2}\) positive three-gap compositions of \(k+1\). Thus
\[
f_3=n\left(k+\frac{k}{2}+\binom{k}{2}\right)=\frac{nk(k+2)}2.
\]

Every three-set is a face. If its run type is \((3)\), add a nonadjacent vertex to obtain type \((3,1)\). If its run type is \((2,1)\), the two positive complementary gaps contain \(k+2\ge5\) vertices in total, so one can extend the two-run on a side whose gap has length at least three and obtain type \((3,1)\). If its run type is \((1,1,1)\), its three positive complementary gaps contain \(k+2\ge5\) vertices, so one gap has length at least two; adding an endpoint of that gap gives type \((2,1,1)\). Downward closure then gives every one-set and two-set as a face as well. Consequently
\[
f_0=n,\qquad f_1=\binom n2,\qquad f_2=\binom n3.
\]

Substitution into the reduced Euler sum gives
\[
\widetilde\chi=-1+n-\binom n2+\binom n3-\frac{nk(k+2)}2+\frac{nk(k-1)}2
=\frac{k^3-19k+24}{6}.
\]
If \(\Delta_k(W_{k+5})\simeq S^3\vee\bigvee^{\beta(k)}S^4\), then its reduced Euler characteristic is \(-1+\beta(k)\). Hence
\[
\beta(k)=1+\widetilde\chi=\frac{k^3-19k+30}{6}=\frac{(k-3)(k-2)(k+5)}6.
\]

## Verification
The accompanying `verify.py` independently constructs \(W_{k+5}\), tests induced connectivity for every five-subset, generates the entire cut complex from its facets, and checks the stated face vector and Euler characteristic for every \(3\le k\le14\). It also checks, on every tested five-set, the proof's run criterion against direct graph connectivity. The replay ends with `SQUARED_CYCLE_FACE_VERIFY_OK`.

These finite computations are cross-checks only. The theorem for all \(k\ge3\) is established by the run classification and counting argument above, not by finite enumeration.

## Relationship to prior work
Bayer, Denker, Jelić Milutinović, Rowlands, Sundaram, and Xue introduced the relevant cut-complex framework and, for squared cycles, conjectured that \(\Delta_k(W_{k+5})\) has homotopy type \(S^3\vee\bigvee^{\beta(k)}S^4\) for \(k\ge3\). Their computations for \(3\le k\le15\) led to the displayed closed formula for \(\beta(k)\). The exact all-\(k\) face vector and Euler characteristic proved here are not stated there; they show that the numerical formula is forced by the conjectured homotopy shape.

Chauhan, Shukla, and Vinayak subsequently proved shellability results for the three-cut complex of squared cycles and formulated broader homotopy conjectures in a different parameter range. Their squared-cycle theorem fixes the cut size at three, while their higher-cut conjecture assumes \(n\ge2k+3\); the present borderline family has \(n=k+5\) and therefore lies outside that higher-cut range for \(k\ge4\). A later sequel by Bayer and collaborators gives explicit face-polynomial formulas for disjoint unions and studies squared paths and grids; its accessible abstract does not state a squared-cycle face formula.

## Limitations
This result does not prove the conjectured wedge decomposition and does not determine integral homology or attaching maps. The implication for \(\beta(k)\) is conditional on the published homotopy-shape conjecture. The originality comparison includes full-text inspection of the primary squared-cycle source and the later three-cut squared-cycle paper, plus the accessible abstract of the later sequel; a formula hidden in inaccessible or non-indexed material remains a residual bibliographic risk.

## References
1. M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram, and L. Xue, *Topology of Cut Complexes of Graphs*, arXiv:2304.13675; SIAM Journal on Discrete Mathematics 38 (2024), 1630–1675, DOI 10.1137/23M1569034.
2. P. Chauhan, S. Shukla, and K. Vinayak, *Shellability of 3-Cut Complexes of Squared Cycle Graphs*, arXiv:2406.01979; Journal of Homotopy and Related Structures 20 (2025), 163–193.
3. M. Bayer, M. Denker, M. Jelić Milutinović, S. Sundaram, and L. Xue, *Topology of Cut Complexes II*, SIAM Journal on Discrete Mathematics 39 (2025), 1123–1157, DOI 10.1137/24M1676077.

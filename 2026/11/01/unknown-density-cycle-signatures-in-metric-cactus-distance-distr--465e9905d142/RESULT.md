# Unknown-density cycle signatures in metric cactus distance distributions

## Finding

**Theorem (complete jump support and weighted cycle formula).** Let \(G\) be a finite connected **metric cactus graph**: each edge has strictly positive real length and every biconnected block is either a single bridge or a simple cycle. Endow its edges with arclength \(d\ell\). Let \(w\in L^\infty(G)\) be any nonnegative sampling density satisfying \(\int_G w\,d\ell=1\). For independent \(X,Y\) with distribution \(w\,d\ell\), set \(D=d_G(X,Y)\), the intrinsic shortest-path distance.

The law of \(D\) is absolutely continuous. It has a density \(f\), uniquely specified away from finitely many radii by the continuous representatives in the proof. On \((0,\infty)\) the *only possible* discontinuities of that density are downward jumps at half-circumferences \(q=\ell(C)/2\) of simple cycle blocks. The exact jump is

\[
J(q):=f(q^-)-f(q^+)=2\sum_{C:\,\ell(C)=2q}\int_0^{\ell(C)}w_C(s)w_C(s+\ell(C)/2)\,ds.\tag{1}
\]

Here \(s\) is arclength modulo the cycle circumference, and \(w_C\) is the restriction of \(w\) to \(C\). There are **no other positive-radius jumps**, and each quantity in (1) is nonnegative. The origin limit is

\[
\lim_{r\downarrow0}f(r)=2\int_Gw^2\,d\ell.\tag{2}
\]

In particular, if \(\operatorname{ess\,inf}_Gw>0\), every cycle contributes strictly positively. Thus **an unknown, bounded, strictly positive sampling bias cannot hide any distinct cycle circumference**: the set of lengths \(\{\ell(C):C\text{ a simple cycle}\}\), without multiplicities, is exactly twice the set of downward-jump positions in the distance density. The graph is a tree exactly when the positive-radius distance density has no jumps. If cycle circumferences are pairwise distinct, the number of jumps also equals the cycle rank \(\dim H_1(G;\mathbb R)\). When circumferences repeat, the jump at their common half-length sums their antipodal autocorrelations; positions alone do not identify their multiplicities.

Under the more general nonnegative density assumption, a cycle of circumference \(2q\) is visible in the jump exactly when its antipodal autocorrelation integral is positive (or, for repeated circumferences, at least one such integral is positive). This is the sharp condition on sampling support, not a requirement of smoothness.

## Assumptions and scope

Finite metric graphs carry the intrinsic path metric with each edge isometric to a real interval. Bivalent subdivision vertices may be inserted or suppressed without changing the metric or probability law. A cactus is allowed to have arbitrary articulation vertices, attached bridges, and multiple cycles (possibly with equal circumferences), but no two simple cycles share an edge. All statements concern the exact distance distribution of two independent samples, not fixed vertex-vertex or combinatorial edge-count distances. Values of \(w\) at vertices and other arclength-null sets are irrelevant. In the visibility corollary \(w\ge\delta>0\) almost everywhere for some unspecified positive \(\delta\).

## Proof

**Step 1: block decomposition.** Delete vertices as measure-zero events and partition \(G\) into its finitely many open blocks. A connected cactus has a block-cut incidence graph that is a tree. Split the density of \(D\) into contributions from ordered sample pairs in the same block and from ordered pairs in distinct blocks.

**Step 2: a cycle with both endpoints inside it.** Fix a cycle \(C\) of circumference \(c>0\), with circular arclength parameter \(s\in[0,c)\). Paths external to \(C\) cannot shorten an arc between two points of \(C\): any external shortcut between distinct cycle vertices would create a second cycle sharing edges with \(C\), contradicting the cactus property (equivalently, the block-cut tree has no alternative route). Hence the intrinsic distance between two points in \(C\) equals their shorter circular separation. The contribution to the density at \(0<r<c/2\) is

\[
 f_{C,C}(r)=2\int_0^c w_C(s)w_C(s+r)\,ds,
\]

and \(f_{C,C}(r)=0\) for \(r>c/2\). Translations are continuous in \(L^1\) on a circle and multiplication against bounded \(w_C\) is a continuous bilinear pairing, so the displayed autocorrelation is continuous on \([0,c/2]\). At \(r=c/2\) it ends abruptly with positive left limit \(2\int_0^c w_C(s)w_C(s+c/2)\,ds\); there is no atomic mass at that endpoint.

**Step 3: a bridge with both endpoints inside it.** On a bridge of length \(a\), parameterize the endpoints by \(s,t\in(0,a)\). Their geodesic distance is \(|s-t|\), giving for \(0<r<a\)

\[
f_{e,e}(r)=2\int_0^{a-r}w_e(s)w_e(s+r)\,ds.
\]

This function is continuous in \(r\) by extension of \(w_e\) by zero to the real line and translation continuity in \(L^1\). It tends to zero as \(r\uparrow a\), with bound \(2\|w\|_\infty^2(a-r)\), and is zero above \(a\). Thus bridges create no positive-radius jump.

**Step 4: distinct blocks.** For any pair of distinct blocks \(B,B'\), the block-cut tree determines a unique exit articulation point \(v\) of \(B\), a unique entry articulation point \(v'\) of \(B'\), and a fixed intermediate geodesic distance \(k=d_G(v,v')\ge0\). For \(x\in B,y\in B'\),

\[
d_G(x,y)=d_B(x,v)+k+d_{B'}(v',y).
\]

If \(B\) is a bridge, the pushforward under \(x\mapsto d_B(x,v)\) has bounded compactly supported density \(g_B\) given by a translated or reflected copy of \(w_e\). If \(B\) is a cycle, its pushforward has density \(g_B(r)=w_C(v+r)+w_C(v-r)\) for \(0<r<c/2\) and zero otherwise (interpreting circular arguments modulo \(c\)). All these \(g_B\) lie in \(L^1\cap L^\infty\) and have compact support. The contribution from the two orders of sample blocks is

\[
 f_{B,B'}(r)=2(g_B*g_{B'})(r-k),
\]

where functions vanish at negative arguments. The convolution of two compactly supported \(L^1\cap L^\infty\) functions is continuous: translating one in \(L^1\) and pairing with the bounded other proves this directly. In particular, no cross-block pair creates a jump, even if its shortest route passes through additional cycles.

**Step 5: identify all jumps.** Summing the finitely many contributions from Steps 2–4 gives an almost-everywhere density. Use their continuous representatives on their natural open intervals. All summands are continuous except for cycle self-pair terms at their half-circumferences, so the only discontinuities are precisely the jumps (1); no cancellation is possible, since all have the same downward sign. If \(w\ge\delta>0\) almost everywhere, each cycle's contribution is at least \(2c\delta^2>0\). For a general nonnegative density, the positivity of the antipodal integral is exactly the visibility condition.

**Step 6: near-zero normalization.** In Steps 2–3, continuity of autocorrelation gives \(f_{B,B}(0^+)=2\int_Bw^2\,d\ell\). Each cross-block term tends to zero at \(r=0\): for \(k>0\) it vanishes identically near zero, and for \(k=0\), \(|(g_B*g_{B'})(r)|\le r\|g_B\|_\infty\|g_{B'}\|_\infty\). Summation gives (2). Finally, for a connected cactus, the number of cycle blocks equals its first Betti number. Under distinct cycle lengths each block yields a separate jump, proving the last assertion. \(\square\)

## Verification

The standalone `checker.py` constructs an exact weighted two-cycle barbell, checks normalization and its three characteristic density statistics using rational arithmetic, integrates its full density, and checks the cumulative distribution against an independent simulated shortest-path metric. The two cycles have lengths \(2\) and \(3\), joined by a bridge of length \(1\), with piecewise-constant probability densities \(1/10\), \(1/5\), and \(1/5\), respectively. It finds jumps \(J(1)=1/25\) and \(J(3/2)=6/25\), and \(f(0^+)=9/25\). A separate nonuniform circle check uses \(w(s)=(1+\cos(\pi s)/2)/2\) on a circle of circumference \(2\) and confirms the analytic density \(f(r)=1+\cos(\pi r)/8\) on \((0,1)\), with jump \(7/8\) at \(1\). These experiments do not certify the theorem on all graphs; the proof above supplies that universal argument.

## Relationship to prior work

Mémoli and Needham, *Distance distributions and inverse problems for metric measure spaces* (first available as arXiv:1810.09646 on 2018-10-23), study the discriminatory power of distance histograms. Their discussion of metric graphs specifically connects uniform-arclength distance-histogram jumps to geodesic loops and derives homotopy consequences under cycle-basis hypotheses. This is substantial prior coverage of the **uniform** case and is not claimed as new here. The present statement concerns arbitrary **unknown essentially bounded nonuniform sampling**, proves the exact weighted antipodal-autocorrelation jump formula, classifies invisible cycles when density vanishes, and gives the zero-radius collision-density identity. These weighted assertions are not among the inspected primary statements; they are a specialization with an additional nonuniform-measure theorem, not a proof of general inverse uniqueness.

Devriendt and collaborators' arXiv:2008.09155 treats probabilistic graph distances and variance through effective resistance in a different setup, not these continuous weighted arclength distance-histogram jumps. Historical priority for the weighted theorem remains provisional.

## Limitations

Unknown positive density does not permit reconstruction of the attachment tree, the positions of cycles, or the number of cycles of each repeated circumference from jump positions alone. Even though jumps are mathematically identifiable from exact population distributions, finite samples need not resolve their sizes reliably when \(\operatorname{ess\,inf}w\) is very small. For general metric graphs with overlapping cycles, the block-cut decomposition used here does not apply, and no assertion is made about their full singularity sets. A former uniform-sampling jump principle is already present in prior literature; the new contribution is explicitly restricted to the stated nonuniform weighted classification.

## References

1. F. Mémoli and T. Needham, *Distance distributions and inverse problems for metric measure spaces*, arXiv:1810.09646 (first posted 2018-10-23); later *Studies in Applied Mathematics* 149 (2022), 943–1001, DOI 10.1111/sapm.12526.
2. K. Devriendt et al., *arXiv:2008.09155* (first posted 2020-08-20), on probabilistic graph distance and effective-resistance formulations.

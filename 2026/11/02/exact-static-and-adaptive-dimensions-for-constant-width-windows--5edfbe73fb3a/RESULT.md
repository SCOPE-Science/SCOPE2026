# Exact static and adaptive dimensions for constant-width windows on paths and cycles

## Finding

Fix integers \(n\ge2\) and \(1\le k\le n\). On the ordered vertex set \(P_n=\{0,\ldots,n-1\}\), let \(\mathcal W^{\mathrm{path}}_{n,k}\) consist of all sets of \(k\) consecutive vertices, with no empty concept. Put \(m=n-k+1\). Then

\[
\operatorname{Ldim}(\mathcal W^{\mathrm{path}}_{n,k})
=\min\!\left\{\lfloor\log_2 m\rfloor,\;1+\lfloor\log_2 k\rfloor\right\},
\]

and its VC dimension is \(0\) when \(m=1\), is \(2\) when \(k\ge2\) and \(m\ge k+2\), and is \(1\) otherwise.

For \(1\le k<n\), let \(\mathcal W^{\mathrm{cyc}}_{n,k}\) comprise all \(n\) cyclic translates of the length-\(k\) arc \(\{0,\ldots,k-1\}\) in \(\mathbb Z/n\mathbb Z\). Then

\[
\operatorname{Ldim}(\mathcal W^{\mathrm{cyc}}_{n,k})
=\min\!\left\{\lfloor\log_2 n\rfloor,\;1+\lfloor\log_2\min(k,n-k)\rfloor\right\},
\]

and its VC dimension is \(2\) exactly when \(2\le k\le n-2\), and \(1\) otherwise.

These identities hold for all indicated \(n,k\), including powers of two and all boundary cases. They yield arbitrarily large gaps between adaptive and static shattering dimensions even when the VC dimension is \(1\): on a path with \(n=2k-1\), the VC dimension is \(1\), whereas the Littlestone dimension equals \(\lfloor\log_2 k\rfloor\). On cycles with \(n=2k\), the VC dimension is \(2\) for \(k\ge2\), while the Littlestone dimension is \(\lfloor\log_2(2k)\rfloor\).

## Assumptions and scope

A concept is a subset of the fixed finite vertex domain. Queries are individual vertex-membership bits, and an adaptive-shattered tree is a complete binary tree whose internal nodes are labeled by queried vertices and for which every root-to-leaf Boolean trace is realized by at least one concept. The Littlestone dimension is its maximal depth. The VC dimension is the maximal size of a nonadaptive shattered set of vertices. All logarithms are base two. A one-concept family has Littlestone and VC dimensions zero. The full-arc cyclic case \(k=n\) is omitted because it is a singleton with both dimensions zero.

The path has \(m\) different windows, indexed by starting positions \(0,\ldots,m-1\). The cycle has \(n\) distinct windows because \(1\le k<n\). No assumptions on relative primality of \(n\) and \(k\) are needed.

## Proof

**1. General upper bounds for adaptive depth.** A shattered binary tree of depth \(d\) needs \(2^d\) distinct concepts. This gives \(d\le\lfloor\log_2 m\rfloor\) on paths and \(d\le\lfloor\log_2 n\rfloor\) on cycles. At a vertex-membership query, at most \(k\) path windows answer yes. On a cycle, exactly \(k\) answer yes and \(n-k\) answer no. If \(d\ge1\), both root branches of a shattered depth-\(d\) tree require \(2^{d-1}\) distinct concepts. Therefore \(2^{d-1}\le k\) on paths, and \(2^{d-1}\le\min(k,n-k)\) on cycles. These are exactly the stated upper bounds.

**2. Consecutive-block splitting lemma.** Let a block of \(2^t\) consecutive possible starting positions be indexed from \(a\) to \(a+2^t-1\). On a path, if \(2^t\le k\), query the vertex \(x=a+2^{t-1}-1\); exactly the first half of those windows contain \(x\). Indeed for a start \(s\le x\), one has \(0\le x-s<k\), while for \(s>x\) the window lies strictly after \(x\). On a cycle, the same statement holds whenever \(2^t\le\min(k,n-k)\), with all positions interpreted modulo \(n\): starts after \(x\) cannot wrap around to \(x\), since their clockwise distance backwards is at least \(n-(2^t-1)\ge k+1\). Thus a block of \(2^t\) such starts has a complete depth-\(t\) shattered tree via repeated midpoint queries; the leaf starts are distinct explicit witnesses.

**3. Sharp path construction.** Let
\[
d=\min\!\left\{\lfloor\log_2 m\rfloor,1+\lfloor\log_2 k\rfloor\right\}.
\]
If \(d=0\), the claim is immediate. Otherwise, \(2^d\le m\) and \(h=2^{d-1}\le k\). Restrict the concepts to the \(2^d\) windows with consecutive starts \(0,\ldots,2^d-1\). Query vertex \(h-1\) at the root. Exactly the first \(h\) windows answer yes and the last \(h\) answer no. Each resulting consecutive block of \(h\) starts is split recursively by the lemma, since \(h\le k\). The resulting tree has depth \(d\), matching the upper bound.

**4. Sharp cycle construction.** Define
\[
d=\min\!\left\{\lfloor\log_2 n\rfloor,1+\lfloor\log_2\min(k,n-k)\rfloor\right\}.
\]
Then \(d\ge1\), and \(h=2^{d-1}\le\min(k,n-k)\). Query cyclic vertex \(k-1\) at the root. Its positive starting positions are exactly \(0,\ldots,k-1\); the negative starting positions are \(k,\ldots,n-1\). Retain the \(h\) starts \(0,\ldots,h-1\) in the positive branch and the \(h\) starts \(k,\ldots,k+h-1\) in the negative branch. Both are consecutive blocks of \(h\le\min(k,n-k)\) starts. Apply the splitting lemma inside each block for a depth-\(d\) tree. All selected starts are distinct, so the root-to-leaf witnesses are valid.

**5. Path VC dimension.** No three ordered vertices are shattered: if \(a<b<c\), no interval has trace \((1,0,1)\) on them. If \(m=1\), there is one concept and VC dimension zero. For \(m\ge2\), vertex \(0\) realizes both membership labels and gives dimension at least one. For a shattered pair \(x<y\), define the intervals of possible start indices
\[
I_x=[\max(0,x-k+1),\min(x,m-1)]\cap\mathbb Z,\qquad
I_y=[\max(0,y-k+1),\min(y,m-1)]\cap\mathbb Z.
\]
The four patterns require a common index, an index in each of the differences \(I_x\setminus I_y\) and \(I_y\setminus I_x\), and one index outside their union. Since \(x<y\) and both differences are nonempty, \(I_x\) starts strictly earlier and ends strictly earlier than \(I_y\). Their union is a contiguous interval. If the zero-zero start lies before this union, then \(\min I_x\ge1\), so \(x\ge k\); and the nonempty right difference forces \(\max I_x<m-1\), hence \(m\ge x+2\ge k+2\). If the zero-zero start lies after the union, reflection of the path gives the same inequality. The joint-one pattern requires \(k\ge2\). Conversely, if \(k\ge2\) and \(m\ge k+2\), take queried vertices \(x=k\), \(y=k+1\). Starts \(0,1,2,k+1\) realize respectively \((0,0),(1,0),(1,1),(0,1)\). This proves the stated sharp criterion.

**6. Cycle VC dimension.** For each vertex, the set of starts of cyclic windows containing it is one contiguous length-\(k\) arc of the cyclic starting-position set. As the start traverses the cycle, each of three queried membership bits changes at most twice. Therefore the three-bit trace takes at most six distinct values and cannot realize all eight patterns. Thus VC dimension is at most two. If \(k=1\), distinct singleton windows cannot realize the positive-positive pattern on two vertices. If \(k=n-1\), the windows omit exactly one vertex, preventing the zero-zero pattern. For \(2\le k\le n-2\), two adjacent vertices have all four traces: a length-\(k\) cyclic window containing both; one containing each but not the other (by shifting one position across either endpoint); and one excluding both, supplied by the complementary arc of length \(n-k\ge2\). Hence the VC dimension is two in exactly this range and one otherwise.

## Verification

The standalone standard-library program `verify_windows.py` independently computes every VC dimension by enumerating all one-, two-, and three-query supports, and every Littlestone dimension via the exact recursive restriction formula, without using the proposed closed forms in either calculation. It additionally generates and checks the explicit midpoint-splitting witness trees. The checked domain comprises every \(2\le n\le16\) and every permitted width, totaling \(255\) path/cycle parameter cases and \(1090\) distinct generated leaf-witness occurrences across the certificates. The resulting deterministic output appears in `verification_output.txt`. These finite checks are corroboration; the theorem for arbitrary \(n,k\) follows from the preceding proof.

To reproduce, place the two additional files alongside this document and execute `python3 verify_windows.py` with a standard Python 3 interpreter.

## Relationship to prior work

Guingona, Kolesnikov, Nierwinski and Soucy (arXiv:2109.04805v1, Theorem 3.10) determine both dimensions for *complete zero-set families of nonzero linear combinations* of linearly independent functions. Such families have equal VC and Littlestone dimensions. The constant-width translated-window class here is not asserted to satisfy that complete linear-combination hypothesis, and its arbitrarily large strict dimension gaps preclude obtaining the claim by directly applying that theorem. Chase, Freitag and Reyzin (arXiv:2310.04812v1, Sections 2--4) develop general query-learning bounds from Littlestone dimension, including an example involving mutually disjoint intervals, but do not analyze equal-width translated windows or cyclic arcs. Classical VC bounds for unrestricted intervals give only the coarse static ceiling two; they do not yield the sharp finite-width and boundary thresholds or adaptive formulas.

The comparison involves mathematical implication, not merely terminology. No inspected primary source, searched published record, or accessible earlier finding was found to imply the four displayed all-parameter formulas. This is an accessible-search statement rather than a claim of exhaustive priority; older notes on finite-domain online learning may remain relevant.

## Limitations

The result concerns one contiguous block of a prescribed *exact* cardinality, not arbitrary intervals, arbitrary connected subsets, unions of windows, or noisy/query-adaptive window lengths. The cyclic formula does not cover the singleton full-circle concept at \(k=n\), whose dimensions are both zero. The computation checks only \(n\le16\), and historical priority beyond inspected and searchable sources remains unverified. The work has not undergone independent scientific validation.

## References

1. V. Guingona, A. Kolesnikov, J. Nierwinski and R. Soucy, *Littlestone and VC-dimension of families of zero sets*, arXiv:2109.04805v1, first public September 10, 2021. https://arxiv.org/abs/2109.04805
2. H. Chase, J. Freitag and L. Reyzin, *Applications of Littlestone dimension to query learning and to compression*, arXiv:2310.04812v1, first public October 7, 2023. https://arxiv.org/abs/2310.04812

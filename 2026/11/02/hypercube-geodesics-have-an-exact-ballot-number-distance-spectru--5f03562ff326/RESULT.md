# Hypercube geodesics have an exact ballot-number distance spectrum

## Finding

Let \(Q_d\) be the graph of binary words of length \(d\ge1\), adjacent when they differ in one coordinate. If \(P\) is **any geodesic of length** \(k\), with \(0\le k\le d\), put
\[
F_{d,P}(z)=\sum_{v\in V(Q_d)}z^{\operatorname{dist}(v,V(P))}.
\]
Then the following **complete distance-shell identity** holds independently of the endpoints and coordinate order of \(P\):
\[
\boxed{F_{d,P}(z)=(1+z)^{d-k}\sum_{r=0}^{\lfloor k/2\rfloor}(k-2r+1)\left(\binom{k}{r}-\binom{k}{r-1}\right)z^r.}
\]
Here \(\binom{k}{-1}=0\). In particular, every length-\(k\) geodesic has eccentricity
\[
\boxed{\operatorname{ecc}_{Q_d}(P)=d-\lceil k/2\rceil.}
\]
Thus the minimum eccentricity over all geodesics is \(\lfloor d/2\rfloor\). For odd \(d\), its attaining paths are exactly the length-\(d\) antipodal geodesics; for even \(d\), they are exactly the length-\(d\) and length-\((d-1)\) geodesics. Counting *unoriented, labelled* nontrivial paths, their respective totals are
\[
\boxed{2^{d-1}d!\quad(d\text{ odd}),\qquad 2^d d!\quad(d\text{ even}).}
\]

## Assumptions and scope

All distances are ordinary unweighted graph distances and \(\operatorname{dist}(v,V(P))\) is the minimum distance to a vertex on \(P\). A geodesic is a simple shortest path between its own endpoints. For \(k=0\), it is a singleton vertex; the distance-shell identity includes this case, but counting paths below concerns lengths \(k\ge1\). The path count treats a path and its reversal as the same path and keeps hypercube vertex labels fixed. The inequalities \(d\ge1\), \(0\le k\le d\) are exhaustive.

## Proof

**Reduction.** A geodesic in a cube flips each of \(k\) distinct coordinates once. Translation by a binary vector followed by a coordinate permutation is an automorphism of \(Q_d\); therefore every such path is carried to the canonical chain
\[
P_k:\quad 0^k,\ 10^{k-1},\ 110^{k-2},\ldots,1^k
\]
in the first \(k\) coordinates, with the remaining \(d-k\) coordinates fixed to zero. The latter coordinates contribute an independent Hamming-weight distance, giving the factor \((1+z)^{d-k}\). It suffices to compute the distance shells of \(P_k\) inside \(Q_k\).

**Ballot-distance lemma.** For a binary word \(x\in\{0,1\}^k\), let \(t\) be its total number of ones, \(u_j\) the number of ones among its first \(j\) coordinates, and \(S_j=2u_j-j\). The distance to the \(j\)-th chain vertex is \(t+j-2u_j=t-S_j\); hence
\[
\operatorname{dist}(x,P_k)=t-M(x),\qquad M(x)=\max_{0\le j\le k}S_j.
\]
Thus \(S_j\) is a walk starting at zero with \(t\) upward and \(k-t\) downward steps. For \(m\ge\max\{0,2t-k\}\), the reflection principle at the first visit to height \(m+1\) gives
\[
\#\{x:|x|=t,\ M(x)\le m\}
=\binom{k}{t}-\binom{k}{t-m-1}.
\]
The subtraction removes the paths crossing height \(m+1\). Reflection sends such a path to a length-\(k\) walk ending at height \(2(m+1)-(2t-k)\), and the number of reflected walks is \(\binom{k}{t-m-1}\). Treat an out-of-range binomial coefficient as zero.

Taking the difference of successive height bounds, and putting \(r=t-m\), shows that the number of words with exactly \(t\) ones and distance exactly \(r\) from the chain is
\[
\binom{k}{r}-\binom{k}{r-1}
\]
provided \(r\le t\le k-r\), and zero otherwise. This also holds at the endpoint-height boundary because the lower height bound contains no walks. There are exactly \(k-2r+1\) allowable values of \(t\) when \(0\le r\le\lfloor k/2\rfloor\). Summing over them gives the ballot-number factor in the displayed shell polynomial. Restoring the untouched coordinates proves the complete formula.

**Radius and equality.** The top nonzero exponent in the shell polynomial is
\[
(d-k)+\lfloor k/2\rfloor=d-\lceil k/2\rceil,
\]
because the top ballot coefficient is strictly positive. This proves the eccentricity statement without extrapolating finite data. The expression decreases with \(\lceil k/2\rceil\); the minimum is \(\lfloor d/2\rfloor\), reached precisely at \(k=d\) if \(d\) is odd, and at \(k\in\{d-1,d\}\) if \(d\) is even.

**Counting optimal paths.** For \(1\le k\le d\), the number of unordered endpoint pairs at Hamming distance \(k\) is \(2^{d-1}\binom{d}{k}\). Between each fixed unordered pair there are exactly \(k!\) geodesics, determined by the order in which the differing coordinates are flipped. Their path lengths identify disjoint classes, so the preceding optimal-length classification gives \(2^{d-1}d!\) paths for odd \(d\), and twice that number for even \(d\).

## Verification

The standalone `verify.py` reconstructs every distance shell directly by enumerating all binary vertices. It compares the direct counts to the ballot formula for every \(1\le d\le12\) and \(0\le k\le d\). Separately, it checks every oriented rooted geodesic for dimensions \(1\le d\le6\) (all starts and all ordered coordinate subsets). Finally it checks the optimal-geodesic count formula in dimensions \(1\le d\le10\). All these finite checks passed on the packaged source. They corroborate, but do not replace, the reflection-principle proof for arbitrary dimension.

## Relationship to prior work

The general minimum-eccentricity shortest-path (ESP) problem and its structural parameter complexity are developed by Babu, Jacob, Kumar, and Sandeep (arXiv:2610.20769, first public 2026-10-14). Their inspected primary text does not state a hypercube geodesic distance-shell polynomial or the enumeration of all optimum paths. The literature on dominating paths in hypercubes, including Blass–Honkala–Karpovsky–Litsyn (2001) and Dvořák–Havel–Mollard (2003), concerns the size or existence of more general dominating paths and cycles; an arbitrary dominating path need not be geodesic. Their accessible abstracts do not establish the current exact fixed-geodesic shell formula. The complete text of those older papers was not available for direct comparison, so historical priority is not independently established.

## Limitations

This theorem applies to the ordinary unweighted binary hypercube and **shortest paths**. It does not give a full distance distribution for arbitrary non-geodesic paths, for distance-weighted cube graphs, or for optimum collections of several geodesics. Full-text historical coverage remains an originality uncertainty; the scientific claim is conditional on the stated definitions, not on uniqueness of publication.

## References

1. A. Babu, A. Jacob, H. Kumar, and R. B. Sandeep, *Eccentricity Shortest Path: the structural parameter landscape*, arXiv:2610.20769 (first public 2026-10-14), https://arxiv.org/abs/2610.20769 .
2. F. F. Dragan and A. Leitert, *On the minimum eccentricity shortest path problem*, Theoretical Computer Science, 2017, https://doi.org/10.1016/j.tcs.2017.07.004 .
3. U. Blass, I. Honkala, M. G. Karpovsky, and S. Litsyn, *Short Dominating Paths and Cycles in the Binary Hypercube*, Annals of Combinatorics 5 (2001), https://doi.org/10.1007/PL00001292 .
4. T. Dvořák, I. Havel, and M. Mollard, *On paths and cycles dominating hypercubes*, Discrete Mathematics 262 (2003), 121–129, https://doi.org/10.1016/S0012-365X(02)00524-1 .

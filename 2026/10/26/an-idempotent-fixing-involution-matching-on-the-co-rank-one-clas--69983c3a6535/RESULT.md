# An idempotent-fixing involution matching on the co-rank-one class of isotone maps

## Finding
For each integer \(n\ge2\), the rank-\(n-1\) Green \(\mathcal D\)-class \(D_{n-1}\) of the order-preserving transformation monoid \(\mathcal O_n\) admits an involution \(J_n\) assigning a mutual inverse to every map and fixing precisely the idempotents. It has \(2(n-1)\) fixed points and \((n-1)(n-2)/2\) two-cycles. An explicit constant-time formula on canonical coordinates is given below.

## Assumptions and scope
Let \([n]=\{1,\ldots,n\}\) carry its ordinary chain order. An element of \(\mathcal O_n\) is an isotone map \(f:[n]\to[n]\). The \(\mathcal D\)-class \(D_{n-1}\) consists of those with image size exactly \(n-1\). Every such map has one non-singleton kernel block, necessarily \(\{i,i+1\}\) for a unique \(i\in\{1,\ldots,n-1\}\), and its image omits a unique point \(t\in[n]\). Conversely, the pair \((i,t)\) determines exactly one isotone map. Thus \(D_{n-1}\) is bijective with the \(n(n-1)\)-cell rectangle \(\{1,\ldots,n-1\}\times[n]\).

Two maps \(f,g\) are mutual semigroup inverses when \(fgf=f\) and \(gfg=g\). An inverse matching is a bijection of this class that sends every element to a mutual inverse; an involution matching also squares to the identity.

## Proof
Define \(J_n\) by the following piecewise formula on the coordinates \((i,t)\):
\[
J_n(i,t)=\begin{cases}
(t-1,i),&t\ge i+2,\\
(t,i+1),&t\le i-1,\\
(i,t),&t=i\text{ or }t=i+1.
\end{cases}
\]
All output coordinates are within the stated rectangle. The first case maps \((i,t)\) with \(t\ge i+2\) to \((t-1,i)\), which satisfies the second-case inequality \(i\le (t-1)-1\); applying the second rule maps it back to \((i,t)\). The second case is similarly reversed by the first, and the final cases are fixed. Therefore \(J_n^2=\mathrm{id}\), in particular \(J_n\) is bijective.

For the pair \((i,t)\), its kernel consists of the block \(\{i,i+1\}\) and singleton blocks elsewhere. Its image \([n]\setminus\{t\}\) meets every kernel block exactly once if and only if \(t\in\{i,i+1\}\). Thus its idempotents are exactly the fixed points in the last branch.

We verify mutual inverse conditions. For any two elements with coordinates \((i,t)\) and \((j,u)\), both composites are inverse composites exactly when the image of each is a transversal of the other's kernel. Equivalently,
\[
u\in\{i,i+1\},\qquad t\in\{j,j+1\}.
\]
To see this without any outside theorem: each rank-\(n-1\) map restricts to an increasing bijection from any transversal of its kernel onto its image, and the equations \(fgf=f\) and \(gfg=g\) are equivalent to the two transversality conditions. Alternatively the relations can be checked by direct substitution in the coordinate formula for the maps. If \(t\ge i+2\), then \((j,u)=(t-1,i)\), so \(u=i\in\{i,i+1\}\) and \(t=j+1\in\{j,j+1\}\). If \(t\le i-1\), then \((j,u)=(t,i+1)\), so \(u=i+1\) and \(t=j\). In the remaining case \(J_n(i,t)=(i,t)\), and the map is an idempotent, hence its own inverse. Therefore every image under \(J_n\) is a mutual inverse.

There are two fixed points for each of the \(n-1\) possible merged pairs, so exactly \(2(n-1)\) fixed points. The remaining \(n(n-1)-2(n-1)=(n-1)(n-2)\) elements form two-cycles. This proves the claimed count.

## Verification
The standalone Python checker `check_corank_one_involution.py` implements the coordinate involution independently from the semigroup composition test. For every \(2\le n\le9\), it enumerates all \(n(n-1)\) maps in \(D_{n-1}\), confirms that the formula is an involution, verifies both mutual inverse identities by explicit map composition, verifies the idempotent-only fixed points and checks the cycle counts. It prints `VERIFY_OK`. The finite test is supplementary; the preceding argument proves the statement for all \(n\ge2\).

## Relationship to prior work
Higgins's 2026 paper (arXiv:2610.01912v1) proves that the entire monoid \(\mathcal O_n\) has a **permutation** inverse matching for every \(n\), using balanced weightings. It does not assert that the matching is an involution. Its Section 3 identifies ranks, kernel/image labels and the transversal criterion, which we use as established context. Higgins (2019) constructs an involution matching for the larger orientation-preserving-cycle monoid, but the canonical matching there does not restrict to \(\mathcal O_n\), as the 2026 paper notes. The present result supplies an explicit involution on one naturally distinguished nontrivial Green class for **every** \(n\), with all idempotents fixed. Finite computational verification of a whole-monoid involution for \(n\le8\), if available, covers only finitely many instances of this all-\(n\) theorem.

## Limitations
The conclusion is restricted to rank \(n-1\); it neither constructs a simultaneous involution matching on other ranks nor proves one exists for all of \(\mathcal O_n\). The proof does not assert uniqueness of this matching. Earlier uncatalogued explicit pairings of the co-rank-one class are a bibliographic originality risk. No independent mathematical audit has been performed.

## References
1. P. M. Higgins, *Balanced weightings and permutation matchings applied to the monoid of order-preserving mappings*, arXiv:2610.01912v1 (first posted 2026-10-01), especially Sections 1–3, https://arxiv.org/abs/2610.01912.
2. P. M. Higgins, *Involution matchings, the semigroup of orientation-preserving and orientation-reversing mappings, and inverse covers of the full transformation semigroup*, *Semigroup Forum* 98 (2019), 669–689, doi:10.1007/s00233-019-10018-z; accepted manuscript https://repository.essex.ac.uk/24377/.
3. P. M. Higgins, *Permutations of a semigroup that map to inverses*, *Semigroup Forum* 89 (2014), 169–182, as cited in [1,2].

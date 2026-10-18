# Sharp cyclic closure cutoff for 123-avoiding bounded-jump permutations

## Finding

For integers \(m\ge1\) and \(n\ge3\), consider permutations \(\pi=(\pi_1,\ldots,\pi_n)\) of \([n]\) satisfying both:

1. **Classical pattern avoidance:** no indices \(i<j<k\) satisfy \(\pi_i<\pi_j<\pi_k\).
2. **Cyclic jump restriction:** \(|\pi_i-\pi_{i+1}|\le m\) for \(1\le i<n\), and \(|\pi_n-\pi_1|\le m\).

Such a permutation exists **if and only if** \(m\ge2\) and \(n\le3m+1\). Moreover, at the sharp boundary \(n=3m+1\), **every** admissible permutation satisfies the four forced positions
\[
\pi_1=2m+1,\qquad \pi_2=3m+1,\qquad
\pi_{n-1}=1,\qquad \pi_n=m+1.
\]

Equivalently, the \(m\)-th power of a path on \(n\) labeled vertices has a Hamiltonian cycle whose vertex order, read from a distinguished starting position, avoids the classical pattern \(123\) if and only if \(m\ge2\) and \(3\le n\le3m+1\). The pattern condition is imposed on the displayed linear listing, **not** on every cyclic rotation.

## Assumptions and scope

The path power has vertex set \([n]\) and joins distinct vertices precisely when their absolute difference is at most \(m\). The same graph may have many ordinary Hamiltonian cycles outside the parameter range; the nonexistence statement concerns the added global pattern restriction. Pattern \(123\) means a subsequence at arbitrary positions, not three consecutive positions. All permutations are position-rooted, with no identification under cyclic rotation or reversal. The case \(n<3\) is deliberately excluded because simple Hamiltonian cycles require at least three distinct vertices.

## Proof

**Endpoint lemma.** Let \(\pi\) avoid \(123\) and obey the linear adjacency restrictions \(|\pi_i-\pi_{i+1}|\le m\), with no cyclic condition yet. Then
\[
\pi_1\ge n-m,\qquad \pi_n\le m+1.
\]
Indeed, put \(a=\pi_1\). If \(a=n\), the first bound is immediate. Otherwise, let \(j>1\) be the first index with \(\pi_j>a\). If \(\pi_j<n\), the later occurrence of \(n\) would give an increasing triple \((a,\pi_j,n)\), impossible. Thus \(\pi_j=n\). By the choice of \(j\), \(\pi_{j-1}\le a\), and the adjacent-jump restriction gives \(n-\pi_{j-1}\le m\). Consequently \(n-a\le m\). The reversed-complemented permutation \(\rho_i=n+1-\pi_{n+1-i}\) has exactly the same avoidance and jump properties. Applying the established first-entry bound to \(\rho\) yields \(n+1-\pi_n\ge n-m\), proving the second bound.

**Upper bound.** If the cyclic closing edge also obeys \(|\pi_n-\pi_1|\le m\), then
\[
n-2m-1\le\pi_1-\pi_n\le|\pi_1-\pi_n|\le m,
\]
so necessarily \(n\le3m+1\). For \(m=1\) and \(n\ge3\), the underlying graph is the original path and has no Hamiltonian cycle, so there are no admissible permutations.

**Construction at equality.** For each \(m\ge2\), form the explicit word, with every indicated interval read in descending order,
\[
W_m=\bigl(2m+1\ ;\ 3m+1,3m,\ldots,2m+2\ ;\ 2m,2m-1,\ldots,m+2\ ;\ m,m-1,\ldots,1\ ;\ m+1\bigr).
\]
An interval whose upper endpoint is below its lower endpoint is empty. The five blocks partition \([3m+1]\). Their internal adjacent differences equal one; between successive blocks the absolute differences are respectively \(m\), \(2\), \(2\), and \(m\), and the closing difference equals \(m\). The empty-interval boundary for \(m=2\) is also valid by direct substitution, giving \((5,7,6,4,2,1,3)\). All values after the first block and before the last form a decreasing sequence, except that the initial value \(2m+1\) is followed by larger decreasing values. Every ascent starts either at that first value or at the final minimum \(1\); neither can belong to an increasing triple. Hence \(W_m\) avoids \(123\) and is admissible.

**All intermediate orders.** Fix \(n\ge5\), \(m\ge2\), and \(n\le3m+1\). Put \(r=\lceil(n-1)/3\rceil\), so \(2\le r\le m\) and \(t=3r+1-n\) lies in \(\{0,1,2\}\). Construct \(W_r\) and delete its largest \(t\) values, retaining the order of all others. Those deleted values occur at the beginning of the descending high block. The resulting word is a permutation of \([n]\), and it continues to avoid \(123\) because deletion preserves pattern avoidance. Every old surviving consecutive pair retains its jump bound. The only possibly new adjacent pair is from \(2r+1\) to the first remaining high-block value, or, if that block vanishes, to \(2r\). Its difference is at most \(r\); the closing pair is unchanged. Thus the resulting permutation has cyclic jumps at most \(r\le m\). For \(n=3\) and \(n=4\), use \((1,3,2)\) and \((2,4,3,1)\), valid for every \(m\ge2\). This proves existence throughout the asserted interval.

**Boundary rigidity.** Suppose \(n=3m+1\) and an admissible permutation exists. The endpoint lemma and closing jump produce
\[
\pi_1\ge2m+1,\qquad \pi_n\le m+1,
\qquad \pi_1-\pi_n\le m.
\]
All inequalities must be equalities, giving the first and last positions in the claim. Consider the first later value exceeding \(\pi_1\) in the endpoint-lemma proof. It must be \(n\), and the element preceding it must be at least \(n-m=\pi_1\). Since that element cannot exceed \(\pi_1\), it equals \(\pi_1\), so the maximum appears immediately in position two. Apply the same argument to the reversed complement to obtain \(\pi_{n-1}=1\). This completes the proof.

## Verification

The self-contained script `verify.py` directly tests classical pattern avoidance and cyclic adjacency, without assuming either endpoint inequality. It cross-checks exact permutation enumeration with a separately implemented memoized recursion over \(24\) small parameter combinations, checks eight further near-boundary counts, and validates all three construction residues for \(2\le m\le40\). The near-boundary counts for \(m=2,3,4,5\) at \(n=3m+1\) are respectively \(1,4,35,338\); at \(n=3m+2\), each is zero. These counts are *finite corroboration only* and are not an asserted all-parameter enumeration formula.

Run `python3 verify.py` from the directory containing the script. Its expected output is included as `verify_output.txt`. The unrestricted existence and rigidity statements follow from the preceding proof, not from any finite experiment.

## Relationship to prior work

Nadler's October 2026 preprint introduces classical \(123\)-avoidance coupled with a *linear* bounded-adjacent-difference condition. It proves localization near the reverse diagonal and describes constrained Hamiltonian **paths** in powers of paths. The endpoint lemma above is compatible with, and essentially implicit in, that localization; it is not independently claimed as novel. The new question adds the closing edge and asks for the precise existence boundary for pattern-compatible Hamiltonian **cycles** together with the forced endpoint structure. The cyclic-closure threshold, its explicit all-residue construction, and four-position boundary rigidity are the claim here.

Bóna and Cory study permutations that are single cycles in the permutation-theoretic sense and avoid two classical patterns; this is a different cyclicity notion. Ehrenborg treats cyclically *consecutive-pattern* avoidance, rather than classical avoidance with bounded differences. Neither abstract establishes the present extremal endpoint configuration.

## Limitations

The main October 2026 preprint's full text was not accessible in this examination; its public abstract and metadata were read, and attempted preprint/open-access full-text retrieval did not succeed. Thus it remains possible that its body contains an unadvertised cyclic-closure consequence or a stronger theorem. Bibliographic priority and independent mathematical verification are not established. The finite counts of extremal permutations do not imply a general enumeration formula, which is not claimed. The result does not address pattern invariance under rotations or other avoidance patterns.

## References

1. Nathaniel Nadler, *123-Avoiding permutations with an adjacency constraint*, arXiv:2610.02526, first posted October 1, 2026, https://arxiv.org/abs/2610.02526 .
2. Miklós Bóna and Michael Cory, *Cyclic permutations avoiding pairs of patterns of length three*, Discrete Mathematics & Theoretical Computer Science 21(2), 2019, DOI:10.23638/DMTCS-21-2-8, https://dmtcs.episciences.org/articles/5909 .
3. Richard Ehrenborg, *Cyclically Consecutive Permutation Avoidance*, SIAM Journal on Discrete Mathematics 30(3), 2016, pp. 1385–1390, DOI:10.1137/130946848, https://doi.org/10.1137/130946848 .

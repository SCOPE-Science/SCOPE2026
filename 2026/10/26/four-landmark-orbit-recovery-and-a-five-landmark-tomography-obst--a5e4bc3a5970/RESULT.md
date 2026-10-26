# Four-landmark orbit recovery and a five-landmark tomography obstruction in quaternary Hamming graphs

## Finding

**Theorem (sharp one-neighbour distance-tomography threshold).** Let \(d\ge1\) and let \(1\le r\le4\) distinct vertices of the Hamming graph \(H(d,4)\) be individually coloured, with every other vertex given one common initial colour. Synchronous ordinary counting colour refinement has the pointwise-marker-stabilizer orbit partition by round \(d+1\). For an explicit formula for the orbit classes and their sizes, see below.

The linear map that reconstructs coordinate-status profiles from marker equality-pattern totals, the distance vector to the markers, and the multiset of changes in that distance vector along **all single-edge neighbours** has full column rank for \(r=1,2,3,4\), but its kernel for \(r=5\) has dimension exactly \(5\). An explicit pair of distinct stabilizer orbits in \(H(12,4)\) has identical data under this one-neighbour tomography map. This last statement is **not** a claim that stable colour refinement fails for five markers; it is a sharp obstruction only to this local reconstruction method.

## Assumptions and scope

Here \(H(d,4)\) has vertex set \(\{0,1,2,3\}^{d}\), two words adjacent precisely when they differ in one coordinate. Fix ordered, pairwise distinct marker words \(a^{1},\ldots,a^{r}\). Their initial colours are distinct, and the unmarked words have a common colour. The update replaces each current colour by the pair consisting of that colour and the multiset of neighbour colours. Round zero denotes the initial partition.

For each coordinate \(t\), let \(\pi_t\) be the restricted-growth-string encoding of the set partition of \([r]\) defined by \(i\sim j\iff a^i_t=a^j_t\), so its first block is labelled \(0\), the next new block \(1\), and so on. Let \(k_\pi\) be its number of blocks and let \(n_\pi=|\{t:\pi_t=\pi\}|\). At a vertex \(x\), its status at coordinate \(t\) is the block index of \(x_t\) if it equals a marked symbol, or a single extra status \(\star\) if it is an unrepresented alphabet symbol; \(\star\) is available exactly when \(k_\pi<4\). Write \(u_{\pi,\sigma}(x)\) for the number of coordinates with pattern \(\pi\) and status \(\sigma\), and \(m_\pi=k_\pi+\mathbf 1_{k_\pi<4}\).

Two words lie in the same orbit of the pointwise stabilizer of all markers exactly when their full arrays \(u_{\pi,\sigma}\) agree. Consequently the exact number of orbits is

\[
\prod_{\pi}\binom{n_\pi+m_\pi-1}{m_\pi-1},
\]

where the product ranges over the marker equality-patterns occurring in the given tuple. The orbit with a specified feasible profile has size

\[
\prod_\pi \frac{n_\pi!}{\prod_\sigma u_{\pi,\sigma}!}
 (4-k_\pi)^{u_{\pi,\star}},
\]

with the last factor omitted if \(k_\pi=4\). For every \(\pi\), the profile variables are nonnegative integers summing to \(n_\pi\).

## Proof

**1. Orbit classification.** The full Hamming-graph automorphism group is the wreath product \(S_4^d\rtimes S_d\): coordinate permutations and independent symbol permutations. An automorphism fixing all marked words must take a coordinate of marker pattern \(\pi\) to another coordinate with the same \(\pi\), mapping the represented symbols blockwise, and may freely permute unrepresented symbols. Hence exactly the counts \(u_{\pi,\sigma}\) classify its orbits. Conversely, matching those counts supplies a coordinate permutation for each pattern and the required symbol bijections. Weak compositions give the class count, and multinomial counting and the choice of an unrepresented symbol at each \(\star\)-coordinate give the class sizes.

**2. A finite linear tomography map.** Let \(h_j(x)\) be the Hamming distance from \(x\) to marker \(a^j\), and let

\[
N_x(\delta)=|\{y:y\sim x,\ (h_1(y)-h_1(x),\ldots,h_r(y)-h_r(x))=\delta\}|,
\qquad \delta\in\{-1,0,1\}^r.
\]

For fixed \(r\) and alphabet size four, define an integer matrix \(T_r\). Its columns are all \((\pi,\sigma)\) with \(\pi\) a restricted-growth partition of \([r]\) into at most four blocks and \(\sigma\) a represented block or the available \(\star\). Its rows consist of all \(3^r\) displacement vectors \(\delta\), all marker-coordinate pattern totals \(n_\pi\), and all \(r\) distances \(h_j\). Identify \(\star\) with symbol index \(k_\pi\) after a local relabelling of represented symbols to \(0,\ldots,k_\pi-1\). In a displacement row \(\delta\), the \((\pi,\sigma)\) column is

\[
\mu_{\pi,\sigma}(\delta)
=\sum_{z\in\{0,1,2,3\}\setminus\{\sigma\}}
\mathbf 1\!\left[\delta_j=
\mathbf 1_{z\ne\pi_j}-\mathbf 1_{\sigma\ne\pi_j}\ 
\text{for every }j\right].
\]

In a pattern-total row \(\pi'\) its entry is \(\mathbf1_{\pi=\pi'}\), and in the distance row \(j\) its entry is \(\mathbf1_{\sigma\ne\pi_j}\). Thus **exactly**, for every possible \(x\),

\[
 T_r u(x)=((N_x(\delta))_{\delta},(n_\pi)_{\pi},(h_j(x))_{j}).
\]

The matrix is universal: it does not depend on \(d\) or the choice of markers.

**3. Exact rank certificate.** Over the field \(\mathbb F_{1000003}\), direct specified-row Gaussian elimination on these explicitly defined integer matrices gives

\[
\begin{array}{c|rrrrr}
r&1&2&3&4&5\\\hline
\text{columns}&2&5&15&51&187\\
\text{rank modulo }1000003&2&5&15&51&182
\end{array}
\]

The script `verify.py` constructs all rows using only integer arithmetic and recomputes each modular rank, including the \(51\)-column full-rank test. Because nonzero minors modulo a prime are nonzero integer minors, \(T_r\) has full rank over \(\mathbb Q\) for \(r\le4\). At \(r=5\), five explicit, linearly independent integer null vectors are encoded in `kernel_basis.json`. `verify.py` checks every one of their \(299\) row equations *over the integers*, verifies that these five vectors are independent, and checks modular rank \(182\). Hence the rational rank at \(r=5\) is exactly \(182\), with kernel dimension exactly \(5\). The certificate needs no heuristic, floating-point calculation or external solver.

**4. From local recovery to counting refinement.** After at most \(d\) rounds, counting colour refinement encodes the distance from each vertex to each individually coloured marker. This follows by induction on distance: a new layer is first characterized by having a neighbour in the previous marker-distance layer, while its more distant successors do not; the initial marked singleton starts the induction. One additional round therefore distinguishes vertices with different neighbour distance-vector distributions. The totals \(n_\pi\) are fixed by the markers, so two vertices of equal colour by round \(d+1\) have the same \(T_ru\). For \(r\le4\), full column rank gives the same \(u\), hence the same stabilizer orbit. Conversely all automorphism orbits are colour-homogeneous at every round. The two partitions coincide, proving the uniform \(d+1\) upper bound and the counting formulas.

**5. A genuine five-marker collision.** The first 24-term integer null vector in `kernel_basis.json` has, for each of twelve distinct coordinate patterns, exactly one coefficient \(+1\) and one coefficient \(-1\) on two different statuses. Give the five markers these twelve coordinate patterns; let \(x\) choose the \(+1\)-status and \(y\) the \(-1\)-status in each coordinate. `verify.py` lists the five explicit twelve-letter markers and the two words. It checks directly in the graph, without relying on matrix multiplication, that both distance vectors equal \((12,12,9,9,9)\) and all \(36\) neighbour displacement counts agree. Every coordinate pattern occurs only once and the chosen statuses differ, so no automorphism fixing the markers can send \(x\) to \(y\). This demonstrates the claimed obstruction at five markers and only at the stated one-neighbour tomography level.

## Verification

Run `python3 verify.py` from a directory containing `kernel_basis.json`. It checks all five modular ranks, five independent integer null certificates, and the direct twelve-coordinate collision, and prints `ALL_TESTS_PASS`. Run `python3 check_graph.py` to verify the orbit-refinement implication directly on all marked configurations of dimensions one and two, together with reproducible marker samples in dimensions three and four. The expected transcripts are `verification.log` and `graph_check.log`; they were recomputed from the source files. All arithmetic certifying the rank claim is finite and exact.

## Relationship to prior work

The structure of Hamming-graph automorphisms and adjacent error neighbourhoods is standard; for example, Gillespie and Praeger describe the wreath-product automorphism action in their 2014 work on neighbour-transitive codes. Kersting, Mladenov, Garnett and Grohe (2014) analyse general counting colour refinement and equitable partitions, without the marker-tomography rank calculation. More recent general work on individualization-refinement and orbit partitions provides an abstract viewpoint on the property, but does not supply these quaternary marker-specific ranks or the twelve-coordinate collision. The results here are a finite sharp identifiability threshold and its graph-theoretic consequence, not a claim of a wholly new colour-refinement method.

## Limitations

The assertion for four or fewer markers is proved only for alphabet size four. The five-marker example shows only noninjectivity of the specified *one-neighbour distance-tomography map*; it does **not** show that full iterative colour refinement fails at five markers, nor does it establish an optimal iteration bound for four markers. Modular ranks and kernel vectors are finitely certified and reproducible, but independent mathematical audit and an exhaustive priority search have not been performed. Other approaches could reconstruct five-marker orbits from further rounds.

## References

- S. Klavžar, *Characterizing subgraphs of Hamming graphs*, Journal of Graph Theory 49 (2005), 302–312, DOI: 10.1002/jgt.20084 (public online date 2005-04-08).
- N. I. Gillespie and C. E. Praeger, *Characterisation of a family of neighbour transitive codes*, arXiv:1405.5427v1 (first public 2014-05-21), especially Sections 1–2 and their Hamming automorphism description.
- K. Kersting, M. Mladenov, R. Garnett and M. Grohe, *Power Iterated Color Refinement*, AAAI 2014, DOI: 10.1609/aaai.v28i1.8992 (public 2014-06-21).
- S. Bhattacharjee, A. Panse and J. Sarma, *A Hierarchy of Tinhofer Graphs: Separations and Membership Testing*, arXiv:2605.19702v1 (2026), general orbit-refinement characterization.

# Exact inverse-list distribution for one deleted overlapping read

## Finding
Let \(q\ge2\), \(\ell\ge2\), \(n\ge\ell+1\) be integers. For a word \(x\in\Sigma_q^n\), form its ordered overlapping \(\ell\)-read vector
\[
R_\ell(x)=(x_1\cdots x_\ell,x_2\cdots x_{\ell+1},\ldots,x_{n-\ell+1}\cdots x_n).
\]
The channel deletes **exactly one** whole \(\ell\)-mer from this vector; it does not delete a symbol from the source word. Let \(P(y)\) be the set of distinct length-\(n\) parent words producing the received ordered vector \(y\) of \(n-\ell\) reads.

A vector \(y\) is *consistent* if every consecutive pair of reads overlaps in its \(\ell-1\) boundary symbols. Such a vector determines a unique length-\(n-1\) word \(z\) by overlapping its reads. Let \(s=\ell-1\), and let \(J_s(z)\) count **maximal runs strictly between the first and last runs of \(z\)** whose lengths are at least \(s\). Then:

1. If \(y\) is consistent and \(z\) is constant, \(|P(y)|=2q-1\); otherwise if \(y\) is consistent, \(|P(y)|=2q+J_s(z)\).
2. If \(y\) is inconsistent, \(|P(y)|\le1\). Every attainable inconsistent vector has exactly one parent.
3. The sharp worst-case inverse-list size is
\[
\boxed{\max_{y:P(y)\ne\varnothing}|P(y)|=2q+\left\lfloor\frac{n-3}{\ell-1}\right\rfloor.}
\]
For \(n\ge\ell+2\), all attained list sizes are exactly \(1\), \(2q-1\), and \(2q+k\) for integers \(0\le k\le\lfloor(n-3)/(\ell-1)\rfloor\). For \(n=\ell+1\), the singleton value \(1\) does not occur.
4. The *entire nonconstant consistent-receiver histogram* is the coefficient polynomial
\[
F_{q,\ell,n}(t)=q(q-1)[u^{n-1}]\,
\frac{u^2}{(1-u)\bigl(1-qu-(q-1)(t-1)u^{\ell-1}\bigr)}.
\]
In detail, \([t^k]F_{q,\ell,n}(t)\) is the number of distinct consistent received vectors with exactly \(2q+k\) parents. There are exactly \(q\) consistent received vectors with \(2q-1\) parents.
5. The number of *attainable inconsistent received vectors*, each having one parent, is
\[
H_{q,\ell,n}=q^n(n-\ell-1)-(n-\ell)q^{n-\ell}+q-q(q-1)^2\sum_{j=0}^{n-\ell-2}(j+1)q^j,
\]
where an empty sum is zero. All other received vectors have zero parents. Thus the equations give the complete inverse-list distribution over every feasible received vector.

## Assumptions and scope
The channel is unpadded: no first or last \(\ell\)-mer is protected by a known adapter, and any of the \(n-\ell+1\) reads may be deleted. The read symbols are full ordered \(\ell\)-tuples, not their Hamming weights or compositions. Parent words and received vectors are counted as distinct objects, so repeated deletion positions causing the same received vector are counted once. There are no probabilistic assumptions.

## Proof
**Step 1: reconstruct a consistent receiver.** If \(y=(w_1,\ldots,w_m)\) is consistent with \(m=n-\ell\), the common overlapping symbols reconstruct exactly one word \(z\) of length \(\ell+m-1=n-1\). Reinserting a missing read at the beginning appends an arbitrary source symbol at the left of \(z\); there are \(q\) choices. Reinserting at the end appends an arbitrary symbol at the right; there are \(q\) choices. These two sets of parents overlap only when \(z\) is constant, and then in exactly one word.

**Step 2: classify interior reinsertions.** Inserting a read \(w\) between consecutive consistent reads \(a,b\) requires its prefix and suffix of length \(\ell-1\) to be the same overlap \(a_2\cdots a_\ell=b_1\cdots b_{\ell-1}\). A length-\(\ell\) word whose first and last \(\ell-1\) entries coincide must be constant. Thus the common overlap must be a constant run of length \(\ell-1\), and \(w\) is uniquely determined. In terms of \(z\), such an insertion extends by one symbol a maximal constant run containing that overlap. Every strictly interior maximal run of length at least \(s=\ell-1\) contributes one genuinely new parent, independent of how many positions within that run can be used. An eligible run meeting either end of \(z\) gives a parent already counted by a boundary insertion. This proves the first formula without double-counting.

**Step 3: inconsistent receivers.** Deleting a single read from a valid read vector can create an inconsistency only across the two formerly nonadjacent reads. If \(y\) has an inconsistent adjacent pair, the missing-read position is therefore forced. Both overlap conditions uniquely determine the inserted read when \(\ell\ge2\); either the reconstruction works and gives one parent, or there is no parent. If multiple inconsistent adjacent pairs occur, there is no parent. This proves the second formula.

**Step 4: sharp maximum and spectrum.** The interior \(n-3\) positions of \(z\) contain pairwise disjoint witness blocks of \(s\) symbols for every counted interior run. Hence \(J_s(z)\le\lfloor(n-3)/s\rfloor\). Conversely, alternate two distinct alphabet symbols in consecutive interior constant runs of length \(s\), place a different single symbol at each end, and absorb unused length into an end run. This attains the upper bound for \(q\ge2\). The same construction attains every intermediate run count. A constant \(z\) realizes \(2q-1\), while a nonconstant \(z\) with no sufficiently long strictly interior run realizes \(2q\). For \(n\ge\ell+2\), deleting an interior read from an appropriate nonconstant word gives one inconsistent received vector, establishing the singleton value as well.

**Step 5: full consistent-receiver generating function.** For a maximal run of unrestricted positive length use \(B(u)=u/(1-u)\). For an interior maximal run use the bivariate weight
\[
C_s(u,t)=\sum_{d=1}^{s-1}u^d+t\sum_{d=s}^{\infty}u^d=\frac{u+(t-1)u^s}{1-u}.
\]
A nonconstant word has two boundary runs and a (possibly empty) ordered sequence of interior runs. The first run's letter has \(q\) choices and each following run's letter \(q-1\) choices. Summing over the number of interior runs gives
\[
\sum_{N\ge2}u^N\sum_{\substack{z\in\Sigma_q^N\\z\text{ nonconstant}}}t^{J_s(z)}
=\frac{q(q-1)B(u)^2}{1-(q-1)C_s(u,t)}
=\frac{q(q-1)u^2}{(1-u)(1-qu-(q-1)(t-1)u^s)}.
\]
Extracting \(u^{n-1}\) proves the full consistent-receiver histogram.

**Step 6: count attainable inconsistent receivers.** The number of *distinct* one-read-deletion outputs of a given read vector equals its number of maximal runs of identical consecutive reads. Over all \(q^n\) input words, this yields the total incidence count \(q^n\bigl(1+(n-\ell)(1-q^{-\ell})\bigr)\), because two consecutive \(\ell\)-reads coincide precisely when the intervening \(\ell+1\) symbols of the source are all equal. The sum of parent multiplicities over consistent outputs is \(2q^n-q+S\), where
\[
S=\left.\frac{d}{dt}F_{q,\ell,n}(t)\right|_{t=1}
=q(q-1)^2\sum_{j=0}^{n-\ell-2}(j+1)q^j.
\]
Each feasible inconsistent output has one parent by Step 3. Subtracting the consistent incidence count gives precisely \(H_{q,\ell,n}\).

## Verification
A standalone enumerator constructs every source word and every distinct received vector, independently computes its parent set, and compares every positive multiplicity with the run formula. It also verifies the sharp maximum, the coefficient distribution of the rational generating function, and the count of inconsistent singleton receivers. Its actual output is included as `check.out`; replay with `python3 check.py`. The run tested \(q\in\{2,3\}\), \(\ell\in\{2,3,4,5\}\), and all available \(n\) up to \(9\) for binary or \(7\) for ternary alphabets. It checked \(36{,}924\) nonempty received configurations and \(66{,}820\) distinct parent incidences. The infinite theorem is proved by the preceding argument, not inferred from enumeration.

## Relationship to prior work
Ye and Ge (2026) study deletion-correcting codes for overlapping \(\ell\)-mer read vectors **with known end adapters**. Their Lemma II.1 characterizes how a deleted read can turn into a deletion inside a periodic substring after consistency restoration. That local structural mechanism is closely related to Step 2, and is credited as prior background. Their published results concern code constructions and redundancy rather than the exact inverse-list distribution for an unpadded vector with unprotected endpoint reads. Xie and Chen (2026) study another adapter-based adversarial nanopore channel. Banerjee, Yehezkeally, Wachter-Zeh and Yaakobi (2024) use Hamming-weight read vectors, which lose information present in the full \(\ell\)-mer model. These differences do not rule out an equivalent unpublished or differently phrased counting result.

## Limitations
The theorem does not apply to adapter-protected receivers, Hamming-weight reads, multiple read deletions, missing read-position metadata with unordered output, or source-symbol deletion channels. The full first-hand text inspected most closely was Ye and Ge's accessible HTML full-text transcription; it contains the main channel definitions and relevant structural proofs, but this is not a line-by-line verification of every other paper in the literature. No claim of independent expert validation or code-design rate improvement is made.

## References
1. Z. Ye and G. Ge, *Deletion-Correcting Codes for the \(\ell\)-Symbol Read Channel*, arXiv:2606.26434, first public 2026-06-24. https://arxiv.org/abs/2606.26434 . Accessible full-text transcription: https://www.researchgate.net/publication/408107340_Deletion-Correcting_Codes_for_the_ell-Symbol_Read_Channel .
2. H. Xie and Z. Chen, *Deletion-correcting codes for an adversarial nanopore channel*, arXiv:2601.21236 (2026). https://arxiv.org/abs/2601.21236 .
3. A. Banerjee, Y. Yehezkeally, A. Wachter-Zeh and E. Yaakobi, *Correcting a Single Deletion in Reads from a Nanopore Sequencer*, arXiv:2401.15939 (2024). https://arxiv.org/abs/2401.15939 .

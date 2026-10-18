# Exact complement spectra for alternating binary deletions

## Finding
Let \(a\ne b\) be two letters and let \(0\le k\le n\) be integers. Write \(r=n-k\), \(w=(ab)^n\), and \(u=(ab)^k\). An embedding of \(u\) in \(w\) selects positions spelling \(u\) in increasing order; its *complement* is the word left after deleting those positions. Let \(C(w,u)\) be the set of **distinct** complements, not the number of embeddings.

For \(z=z_1\cdots z_r\in\{0,1\}^{r}\), put \(D(z)=d_1\cdots d_r\), where \(d_i=ab\) for \(z_i=0\) and \(d_i=ba\) for \(z_i=1\). Let \(s(z)\) count maximal nonempty runs of the symbol \(1\) in \(z\), with \(s(\varepsilon)=0\). Then
\[
\boxed{C((ab)^n,(ab)^k)=\{D(z):z\in\{0,1\}^{r},\ s(z)\le k\}.}
\]
In particular, with out-of-range binomial coefficients interpreted as zero,
\[
\boxed{\left|C((ab)^n,(ab)^k)\right|=\sum_{j=0}^{k}\binom{r+1}{2j}=\sum_{j=0}^{2k}\binom rj.}
\]
Every one of the \(2^r\) domino encodings occurs exactly when \(r\le2k\), or equivalently \(n\le3k\). For fixed \(k\) and \(r\) tending to infinity, the count is asymptotic to \(r^{2k}/(2k)!\); the case \(k=0\) gives the single unchanged complement.

## Assumptions and scope
The source and deleted words both begin with \(a\), alternate letters, and end with \(b\); the empty word is permitted when \(k=0\) or \(r=0\). The alphabet may contain other letters, but they play no role. Complements are distinguished as words, not as subsets of source positions. The statement is for all integers \(n\ge0\), \(0\le k\le n\), without randomization or an asymptotic restriction.

## Proof
**(1) The pairing invariant.** Index the \(2n\) source positions from zero. Suppose an embedding chooses \(p_1<\cdots<p_{2k}\). Since both \(w\) and the chosen word \(u\) begin with \(a\) and alternate, the letter at \(p_j\) forces \(p_j\equiv j-1\pmod2\). There are exactly \(p_j-(j-1)\) *unselected* letters preceding \(p_j\), so this count is even. Thus no selected letter can lie between the odd- and even-numbered letters of a paired complement: a selected letter there would have an odd number of unselected predecessors. The complement is therefore a concatenation of \(r\) pairs of consecutive source letters, each either \(ab\) or \(ba\). This determines a unique encoding \(z\).

**(2) A lower bound on selected letters.** Immediately before a complement pair, the source position has parity equal to the number of selected letters already read (the number of previous complement letters is even). Hence the pair is \(ab\) when that count is even and \(ba\) when it is odd. The parity starts even and ends even because the embedding selects exactly \(2k\) letters. Consider the extended type string \(0z_1\cdots z_r0\). Each change of type forces at least one selected letter between its adjacent complement pairs (including before the first and after the last pair). There are precisely \(2s(z)\) such changes: entering and leaving each maximal run of ones. Therefore \(2s(z)\le2k\), or \(s(z)\le k\). This proves one inclusion.

**(3) Sufficiency and an explicit embedding.** Given any encoding \(z\) with \(s=s(z)\le k\), build an interleaving of \(u\) and \(D(z)\) as follows. Start with zero selected letters. For each requested pair, if its type differs from the parity of the selected-letter count, select the next letter of \(u\) first; then retain the requested two-letter pair. After the final pair, select one further letter if needed to return to even parity; finally select the remaining \(2(k-s)\) letters of \(u\). Exactly one selected letter has been used at each of the \(2s\) type changes, and all unselected letters occur in the prescribed order. Whenever a letter is selected the number of preceding unselected letters is even, so that letter agrees with the next letter of \((ab)^k\). Whenever a pair is retained, its phase matches the current selected-letter parity. Hence the resulting entire interleaving is precisely the alternating source \((ab)^n\). This produces an embedding with complement \(D(z)\) and proves the reverse inclusion.

**(4) Counting.** A binary type word of length \(r\) with exactly \(j\) maximal runs of ones is uniquely specified by its \(2j\) start/end boundaries among the \(r+1\) gaps, so there are \(\binom{r+1}{2j}\) such words. Summing over \(j\le k\) yields the first formula. Pascal's identity \(\binom{r+1}{2j}=\binom r{2j}+\binom r{2j-1}\) yields the second. The maximal number of one-runs in length \(r\) is \(\lceil r/2\rceil\); all \(2^r\) words are admitted exactly when \(k\ge\lceil r/2\rceil\), equivalent to \(r\le2k\). For fixed \(k\), the highest-degree term of the binomial sum is \(r^{2k}/(2k)!\). These arguments also cover the empty-word boundary cases. \(\square\)

## Verification
The bundled `check.py` directly enumerates all position embeddings for all \(0\le k\le n\le10\), forms the distinct resulting complements and compares their **entire sets** with the run characterization and their sizes with the binomial sum. All 66 parameter pairs pass. `check_dp.py` uses an independently written shuffle-membership dynamic program to test 7,151 candidate pairs with \(n\le14\) and \(r\le9\); all agree with the run condition. Recorded outputs are bundled. Either script can be run with Python 3 and no external dependencies. Finite tests support but do not replace the proof for unrestricted parameters.

## Relationship to prior work
Adamson, Fleischmann and Huch (2026) introduced complement scattered factors, gave general algorithms, studied uniqueness and self-shuffles, and explicitly left exact formulas for special classes as an open direction (Section 5). Their general finite algorithms compute individual instances but do not state this two-parameter description, run-language characterization, or saturation threshold. The standard binomial sequence for the \(k=1\) specialization coincides numerically with OEIS A000124; that numerical coincidence is not a published identification with complement sets. Related work on deleting \(a^kb^k\) from an alternating source concerns a different deleted subsequence and does not imply the present characterization.

## Limitations
The result is confined to a perfectly alternating source and an alternating deleted subsequence with the same starting phase. It does not supply a universal bound for arbitrary \(w,u\), nor does it classify complements of arbitrary periodic source words. Prior-art searches cannot exclude every unpublished or unindexed equivalent formula. No independent scientific audit has been performed.

## References
1. D. Adamson, P. Fleischmann, A. Huch, “(Sets of) Complement Scattered Factors,” arXiv:2603.20790v1, publicly submitted 2026-03-21. https://arxiv.org/html/2603.20790
2. OEIS Foundation, “A000124: Central polygonal numbers,” https://oeis.org/A000124 (numerical comparison for one specialization only).

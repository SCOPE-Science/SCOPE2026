# Sharp cyclic \(k\)-mer reconstruction thresholds for three-marker binary words

## Finding

**Theorem (exact minimal identifying read length).** Let \(w\) be a cyclic binary word with exactly three ones and length \(n\ge3\). Moving around the circle in its fixed orientation, write the numbers of zeros between consecutive ones as \((g_0,g_1,g_2)\), and write their sorted values as \(0\le a\le b\le c\). Thus \(n=a+b+c+3\). Define the oriented circular \(k\)-spectrum \(\mathcal{D}_k(w)\) as the **multiset**, with multiplicities, of the \(n\) cyclic factors of length \(k\) starting at the \(n\) positions. Let \(\kappa(w)\) be the least integer \(k\in\{1,\ldots,n\}\) for which any binary cyclic word of length \(n\) with the same \(k\)-spectrum must be a rotation of \(w\). Then

\[
\kappa(w)=\begin{cases}
a+b+3,&a<b<c,\\
a+1,&a=b=c,\\
a+1,&a=b<c=a+1,\\
a+2,&a=b<c,\ c\ge a+2,\\
b+1,&a<b=c.
\end{cases}
\]

This includes zero-length gaps and the all-one cycle of length three. In the pairwise-distinct case the sharp threshold is \(n-c\), the size of the shortest contiguous circular arc containing all three ones. With repeated gap values, identification can occur strictly earlier.

## Assumptions and scope

A rotation, but **not** a reversal, is regarded as the same cyclic word. Reads are ordered binary factors, and their multiplicities are retained; the theorem does not concern deletion subsequences, unordered binary compositions, or sets of distinct reads. The reconstruction competitor is any binary circular word of the same total length, not one assumed in advance to have three ones. All three gaps are nonnegative integers and every \(n\ge3\) is permitted. A shorter spectrum is determined by a longer spectrum: count the length-\(h\) prefix of each length-\(k\) read for \(h<k\), preserving multiplicities.

A length-\(k\) spectrum also forces the number of ones in the circle, since summing the ones across all \(n\) reads counts each source one exactly \(k\) times. Therefore all competing words in the proof necessarily have three ones.

## Proof

**1. General upper bound.** The circular arc covering all three ones and omitting the zero gap of length \(c\) gives a consecutive factor of length \(n-c=a+b+3\) containing all three ones. Any competing word with the same spectrum has three ones globally and contains that very same factor. It therefore places every one at the three positions dictated by the factor; the residual zero gap of length \(c\) is forced. Hence the competitor is a rotation. This gives \(\kappa(w)\le n-c\) without restrictions on equal gaps.

**2. Distinct gaps: sharp reversal obstruction.** Suppose \(a<b<c\). The circular reverse \(w^{\mathrm{rev}}\) is not a rotation of \(w\), since reversal reverses the cyclic order of three pairwise distinct gaps and no rotation of a triple has that effect. We prove \(\mathcal D_k(w)=\mathcal D_k(w^{\mathrm{rev}})\) for every \(k\le n-c-1=a+b+2\).

No such length-\(k\) factor has three ones, because even the shortest arc containing all three ones has length \(a+b+3\). A zero-only factor has count \(\sum_{g\in\{a,b,c\}}\max(g-k+1,0)\), unchanged by reversal. For exactly one one, a factor is \(0^u1 0^v\), where \(u,v\ge0\) and \(u+v=k-1\). Its occurrence count is the number of consecutive ordered gap pairs \((h,h')\) around the circle for which \(h\ge u\) and \(h'\ge v\). If \(\min(u,v)\le a\), this equals the number of gaps of length at least \(\max(u,v)\), a symmetric expression in \(u,v\). Otherwise \(u,v\ge a+1\), and \(u+v\le a+b+1\) implies \(u,v\le b\). Exactly the gaps \(b,c\) qualify on both sides; as they are consecutive in precisely one ordered adjacency, the count is one, again symmetric in \(u,v\).

For exactly two ones, every factor is \(0^u1 0^g1 0^v\) with \(u,v\ge0\) and \(u+v=k-g-2\), where \(g\) is one of the three actual inter-one gaps. For \(g=a\), the total \(u+v\) is at most \(b\), the smaller of the other gaps; for \(g=b\), it is at most \(a\); and for \(g=c\), it is at most \(a+b-c\le a\). Thus whenever this factor has a nonnegative required sum, both exterior zero tails fit between the other two ones for **every** choice of the split \(u+v\). The occurrence count is exactly the multiplicity of the gap \(g\), independent of the order of the exterior tails. Counts of every factor with zero, one, or two ones are consequently invariant under reversal, proving equality of the whole oriented \(k\)-spectra. Reversal supplies a genuinely different word through length \(a+b+2\). Together with Step 1, \(\kappa(w)=a+b+3\).

**3. A short-spectrum obstruction for repeated gaps.** We use the following observation. If a cyclic word has three ones and all three zero gaps are at least \(k-1\), every length-\(k\) factor contains at most one one. For each \(0\le u<k\), the factor \(0^u1 0^{k-1-u}\) then occurs exactly three times, one per marker; any other factor is \(0^k\). Hence its entire \(k\)-spectrum depends only on \(n\) and \(k\), not on the individual zero gaps. If two different gap triples with equal sum satisfy this lower bound, they cannot be distinguished at read length \(k\).

**4. Two equal shortest gaps.** Suppose \(a=b<c\). If \(c=a+1\), then at length \(k=a+1\) the absence of a factor containing two ones forces all three gaps to be at least \(a\). (When \(a=0\), this is automatic.) Since the gap sum is \(3a+1\), the multiset of gaps must be \(\{a,a,a+1\}\), with only one cyclic ordering up to rotation. Thus \(\kappa(w)\le a+1\). If \(a\ge1\), at length \(a\) the two distinct gap triples \((a,a,a+1)\) and \((a-1,a+1,a+1)\) both have gaps at least \(a-1\); Step 3 makes their spectra equal. If \(a=0\), no length below one is admissible. Consequently \(\kappa(w)=a+1\).

If instead \(c\ge a+2\), length \(k=a+2\) determines from factors \(1 0^h 1\) with \(h<k-1\) the exact multiplicity of every gap \(h\le a\), by projecting the spectrum to the shorter factor length. In particular the competing word must have **exactly two** zero gaps equal to \(a\) and none smaller; its remaining gap is forced to be \(c\), so it is the same cyclic word. At length \(a+1\), the distinct triples \((a,a,c)\) and \((a,a+1,c-1)\) have the same total gap sum, and all gaps at least \(a=k-1\). Step 3 makes their spectra equal. Hence \(\kappa(w)=a+2\).

**5. Three equal gaps.** Suppose \(a=b=c\). At length \(k=a+1\), the absence of a factor with two ones forces all gaps to be at least \(a\); the fixed sum \(3a\) forces equality of every gap. If \(a\ge1\), the distinct triples \((a,a,a)\) and \((a-1,a,a+1)\) both have all gaps at least \(a-1\), making their length-\(a\) spectra identical by Step 3. At \(a=0\), the length-one spectrum already suffices. Thus \(\kappa(w)=a+1\).

**6. Two equal longest gaps.** Suppose \(a<b=c\). At length \(k=b+1\), the projected counts of factors \(1 0^h 1\) for \(h\le b-1\) force exactly one gap of length \(a\), no other gap shorter than \(b\), and total gap sum \(a+2b\). The two remaining gaps are therefore both exactly \(b\). Thus \(\kappa(w)\le b+1\).

For sharpness at length \(b\), compare the distinct cyclic gap triples \((a,b,b)\) and \((a,b-1,b+1)\), where \(a\le b-1\). In both words the two gaps other than the first are at least \(b-1\), so there are no factors of length \(b\) with three ones. Any factor with two ones must span the gap \(a\), since spanning either other gap requires at least \(b+1\) positions. If \(a+2\le b\), every factor \(0^u1 0^a1 0^v\) of length \(b\) (with \(u+v=b-a-2\)) occurs exactly once: both exterior tails fit in either word's other gaps. If \(a+2>b\), there are no two-one factors. For a one-one factor \(0^u1 0^v\) with \(u+v=b-1\), the count in **both** words is

\[
1+\mathbf1_{u\le a}+\mathbf1_{v\le a},
\]

because one of the three markers is between the two long gaps, and the other two are adjacent to the short gap on opposite sides. The zero-only factor count follows from subtraction from the common total \(n\) once all other factors have been counted. Therefore the two length-\(b\) spectra agree, while the two circular words are distinct. Hence \(\kappa(w)=b+1\).

Finally, the projection observation in the assumptions ensures that non-identifiability at the displayed lower length also rules out every still shorter read length. The five cases are exhaustive. \(\square\)

## Verification

`CHECK.py` independently enumerates every rotation class of binary cyclic words containing exactly three ones for all lengths \(3\le n\le30\). At every relevant read length it constructs oriented factor multisets directly, groups words by equal spectra, and compares singleton membership with the theorem. It additionally checks the reversal obstruction for distinct gaps, and independently constructs each read by modular position indexing at the predicted threshold. A successful run prints:

`THREE_MARKER_K_SPECTRUM_PASS n=3..30 necklace_classes=1360 distinct_gap=1150 repeated_gap=210 uniqueness_decisions=20626`

The exhaustive computation is a finite consistency check; the proof above establishes the result for all lengths.

## Relationship to prior work

Ota and Manada's reconstruction framework for circular binary strings supplies general conditions using substrings, minimal absent words, and weighted automata; it does not give the present explicit least read length as a five-case function of three circular zero gaps. Bresler, Bresler, and Tse derive broad repeat-based criteria for shotgun assembly, which motivate the role of repeated and interleaved arrangements but do not state the three-marker spectrum classification. Work on succinct \(k\)-spectra chiefly treats distinct-factor indexing, rather than the multiplicity-sensitive reconstruction threshold here. The new theorem is a closed structural resolution for the first sparse binary necklace family exhibiting orientation-distinguishable reversals. General reconstruction criteria may imply the statement only after further specialized analysis.

## Limitations

No claim is made for four or more ones, for factor sets without multiplicity, for unknown orientation/reversal identification, or for noisy reads. The novelty assessment is relative to inspected and searched material; an equivalent theorem in unindexed work cannot be categorically excluded. The computational checks do not establish the infinite theorem independently of the proof.

## References

1. T. Ota and A. Manada, *A Reconstruction of Circular Binary String Using Substrings and Minimal Absent Words*, IEICE Trans. Fundamentals, advanced online publication 2023-09-05, DOI: 10.1587/transfun.2023TAP0015. https://doi.org/10.1587/transfun.2023TAP0015
2. G. Bresler, M. Bresler, and D. Tse, *Optimal assembly for high throughput shotgun sequencing*, BMC Bioinformatics 14 (Suppl. 5), S18 (2013), DOI: 10.1186/1471-2105-14-S5-S18. https://doi.org/10.1186/1471-2105-14-S5-S18
3. J. Alanko, M. Biagi, and S. J. Puglisi, *Longest Common Prefix Arrays for Succinct k-Spectra*, arXiv:2306.04850 (2023). https://arxiv.org/abs/2306.04850

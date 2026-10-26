# Dyck height and near-maximal subsequence universality

## Finding

For every integer \(n\ge1\), let \(D_n\) denote the Dyck words over the fixed binary alphabet \(\{0,1\}\), with \(0\) an opening step and \(1\) a closing step. For \(w\in D_n\), let \(H(w)\) be its maximal prefix excess of \(0\)'s over \(1\)'s and let \(\iota(w)\) be the greatest \(k\) such that **every** binary word of length \(k\) embeds in \(w\) as a scattered subsequence.

**Theorem.** The sharp height–universality inequality is
\[
\iota(w)\le n-H(w)+1.
\]
For every \(n\ge1\) and \(1\le h\le n\), equality is attained at \(w=0^h1^h(01)^{n-h}\), which has height exactly \(h\).

Moreover,
\[
\iota(w)\ge n-1\quad\Longleftrightarrow\quad H(w)\le2.
\]
The high-index spectrum is exact:
\[
\#\{w\in D_n:\iota(w)=n\}=1,\qquad
\#\{w\in D_n:\iota(w)=n-1\}=2^{n-1}-1,
\]
with the second formula interpreted as zero when \(n=1\). Hence \(2^{n-1}\) Dyck words of semilength \(n\) are at least \((n-1)\)-universal. For \(n\ge2\), those of index exactly \(n-1\) have the unique representation
\[
w=(01)^a\,001\,u_1\cdots u_b\,1,\qquad
a,b\ge0,\quad a+b=n-2,\quad u_j\in\{01,10\}.
\]

## Assumptions and scope

The alphabet is exactly \(\{0,1\}\), independent of the symbols appearing in a target subsequence. A Dyck word of semilength \(n\) has \(n\) opening and \(n\) closing steps and every prefix has nonnegative excess. The empty word is excluded. Indexed words, not rotation classes, are counted. The universality index is for all length-\(k\) binary **scattered** subsequences, not contiguous factors. No claim concerns arbitrary balanced words that dip below zero or alphabets larger than two.

## Proof

**1. Greedy arches.** Reading a binary word left to right, terminate an arch at the first occurrence of the symbol opposite its first symbol; restart after that position. Each full arch has the form \(0^{d+1}1\) or \(1^{d+1}0\) with integer \(d\ge0\). After \(k\) arches remains a (possibly empty) monochromatic suffix of length \(r\). This greedy number of arches equals \(\iota(w)\). Indeed, any length-\(k\) binary target embeds by selecting its successive symbols from the \(k\) complete arches. Conversely, write \(b_i\) for the final, newly appearing symbol of arch \(i\), and choose \(c\) absent from the monochromatic remainder (choose either symbol if the remainder is empty). The target \(b_1\cdots b_kc\) cannot embed: its earliest possible \(b_1\) is the end of the first arch, inductively the earliest possible \(b_i\) after those choices is the end of the \(i\)-th arch, and no \(c\) follows the last one. Thus no \((k+1)\)-universality is possible.

**2. Height inequality.** For a Dyck word of length \(2n\), write the arch lengths as \(2+d_1,\ldots,2+d_k\) and the monochromatic remainder length as \(r\). Then
\[
2(n-k)=d_1+\cdots+d_k+r.
\]
At arch boundaries, the height changes by \(+d_i\) for an arch \(0^{d_i+1}1\) and by \(-d_i\) for an arch \(1^{d_i+1}0\). The remainder changes height by \(+r\), \(-r\), or \(0\). Since a Dyck word ends at height zero, its total upward boundary changes equal its total downward boundary changes; therefore the sum of positive boundary changes (including the final remainder endpoint) equals \(n-k\). Every boundary height is at most \(n-k\). A \(0^{d+1}1\) arch reaches at most one level above its ending boundary; a \(1^{d+1}0\) arch reaches no higher than its starting boundary; and a monochromatic remainder reaches no higher than one of its endpoints. Consequently \(H(w)\le n-k+1\), or \(k\le n-H(w)+1\).

For sharpness at height \(h\), use \(w=0^h1^h(01)^{n-h}\). If \(n=h\), the first arch is \(0^h1\) and the remaining closing symbols form a non-universal suffix, giving index \(1\). If \(n>h\), the arch decomposition starts with \(0^h1\), continues with \(1^{h-1}0\) when \(h\ge2\), and then has \(n-h-1\) arches \(10\) and one trailing \(1\); its index is \(n-h+1\). The case \(h=1\) has exactly \(n\) arches \(01\). In all cases the maximal height is \(h\).

**3. The height-two converse.** Assume \(H(w)\le2\). At a complete-arch boundary the height can only be \(0\) or \(1\): this follows inductively because a negative-length-excess arch \(1^{d+1}0\) with \(d\ge1\) would require starting height at least \(2\), whereas a positive-length-excess arch \(0^{d+1}1\) with \(d\ge1\) must be exactly \(001\), starting at height \(0\), and ends at height \(1\). Neutral arches \(01\) or \(10\) preserve boundary height. Thus either all arches are neutral at height zero and \(w=(01)^n\), or there is a unique positive-excess arch \(001\). Before this exceptional arch, neutrality at height zero forces arches \(01\); afterward, neutrality at height one allows exactly \(01\) or \(10\), and a final \(1\) returns to height zero. This proves the stated unique normal form and yields \(k=n-1\) in the latter case. Conversely, the height inequality gives \(\iota(w)\ge n-1\Rightarrow H(w)\le2\).

**4. Exact count.** The all-neutral case is uniquely \((01)^n\). For the index-\(n-1\) case and any \(a+b=n-2\), the \(b\) following neutral arches may independently be \(01\) or \(10\); all such words stay between heights zero and two, and their greedy decompositions are distinct. Hence the exact number is
\[
\sum_{b=0}^{n-2}2^b=2^{n-1}-1.
\]
The total follows by adding the one maximal-index word. In particular, since \(|D_n|=\frac1{n+1}\binom{2n}{n}\), the proportion of near-maximal words is asymptotic to \(\sqrt{\pi}\,n^{3/2}/2^{n+1}\): the near-maximal property is exponentially rare within the Catalan family.

## Verification

Run `python3 verify.py` using Python's standard library. This script enumerates all \(290{,}511\) Dyck words of semilengths \(1\) through \(12\) and checks the height inequality, the exact high-index counts, the unique normal form and the sharp witnesses. On the \(2{,}055\) words of semilength at most \(8\), it also calculates universality directly by testing the embeddings of every candidate binary target, independently of greedy arch counting. The expected output begins `DYCK_UNIVERSALITY_PASS`. These finite checks test the proof's claims at sampled sizes; the all-length theorem rests on the argument above.

## Relationship to prior work

Hébrard's arch factorization, used in the universality literature, provides the greedy-index characterization. Adamson [1] counts and ranks unrestricted \(k\)-subsequence-universal words; Schnoebelen and Veron [2] study arch-jumping functions and circular/compressed-word universality. Neither inspected text states a bound in terms of Dyck height, the height-two equivalence, or this exact restricted near-maximal spectrum. Mol, Rampersad, and Shallit [3] study Dyck nesting levels and Dyck factors of automatic words, rather than subsequence universality. The elementary count \(2^{n-1}\) of height-at-most-two Dyck words is classical and is **not** claimed as a new enumeration in isolation: the asserted contribution is the sharp link between Dyck height and universality and the complete near-maximal arch normal form. A formulation under another language or Dyck-path statistic may already exist; this limitation is not removed by negative search results.

## Limitations

No full joint distribution of \(H(w)\) and \(\iota(w)\) is claimed. For height above two, the upper bound can be strict. The counting formulas concern full Dyck words and fixed binary alphabet only. Finite program results alone are not proofs, and identification with an equivalent theorem in unlocated literature remains possible.

## References

[1] D. Adamson, *Ranking and Unranking k-subsequence universal words*, arXiv:2304.04583v1 (2023-04-10), https://arxiv.org/html/2304.04583v1.

[2] Ph. Schnoebelen and J. Veron, *On arch factorization and subword universality for words and compressed words*, arXiv:2304.11932v1 (2023-04-24), https://arxiv.org/html/2304.11932v1.

[3] L. Mol, N. Rampersad, and J. Shallit, *Dyck Words, Pattern Avoidance, and Automatic Sequences*, arXiv:2301.06145v1 (2023-01-15), https://ar5iv.labs.arxiv.org/html/2301.06145.

[4] D. Adamson et al., *k-Universality of Regular Languages*, arXiv:2311.10658 (2023-11-17), https://arxiv.org/abs/2311.10658.

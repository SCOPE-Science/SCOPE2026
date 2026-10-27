# Sharp all-factor subsequence-universality discrepancy in the regular paperfolding word

## Finding
Let \(p=p_0p_1\cdots\) be the binary regular paperfolding word in the convention
\[
p_n=\begin{cases}0,&\operatorname{odd}(n+1)\equiv1\pmod4,\\1,&\operatorname{odd}(n+1)\equiv3\pmod4,\end{cases}\qquad n\ge0,
\]
where \(\operatorname{odd}(t)=t/2^{\nu_2(t)}\) is the odd part of a positive integer. This convention is the binary complement of another standard paperfolding convention; the results are complement-invariant.

For a finite binary word \(v\), let \(\iota(v)\) be the largest \(k\ge0\) such that every binary word of length \(k\) is a scattered subsequence of \(v\). **For every starting position \(a\ge0\) and length \(N\ge1\)**,
\[
\boxed{-11\le 8\iota(p_a\cdots p_{a+N-1})-3N\le7.}
\]
Both integer constants are optimal. Equality at the lower end is attained by the factor \(p_7\cdots p_{23}=\mathtt{00011011000100111}\) of length \(17\) with index \(5\); equality at the upper end is attained by \(p_2\cdots p_{12}=\mathtt{10011000110}\) of length \(11\), also with index \(5\). Therefore \(\iota(v)/|v|\to3/8\) uniformly over factors \(v\) whose length tends to infinity.

More precisely, for every \(J\ge1\),
\[
\boxed{\iota(p_0\cdots p_{8J-1})=3J-p_{J-1}.}
\]
In particular, for each \(m\ge3\) and \(j\ge0\), the aligned factor of length \(2^m\) beginning at \(2^m j\) has index \(3\cdot2^{m-3}-p_j\).

## Assumptions and scope
Every universality index uses the fixed binary alphabet \(\{0,1\}\); it is not taken relative to the letters that happen to occur in the factor. Intervals have integer, zero-based positions and are contiguous. The theorem concerns the regular paperfolding word, not arbitrary instruction sequences generating generalized paperfolding words. The symbols \(\emptyset,0,1\) below denote the three states of the greedy arch scanner.

## Proof
**Arch scanner.** Read a word left-to-right, holding \(q=\emptyset\) if the current incomplete arch is empty, or \(q\in\{0,1\}\) if it has seen exactly that letter. Reading \(x\in\{0,1\}\) changes \(\emptyset\) to \(x\), leaves \(q=x\) unchanged, and changes \(q\ne x\) to \(\emptyset\) while adding one complete arch. The final number of arches equals \(\iota(v)\), by the standard shortest-rich-prefix characterization of subsequence universality.

**Block lemma.** For each \(j\ge0\), the length-eight block is
\[
B_j=p_{8j}\cdots p_{8j+7}=\mathtt{001}\,(j\bmod2)\,\mathtt{011}\,p_j.
\]
Indeed the residues of the odd parts of \(8j+r+1\) for \(r=0,\ldots,7\) give the first seven entries, with the fourth depending on parity of \(j\), while \(\operatorname{odd}(8j+8)=\operatorname{odd}(j+1)\) gives the last. Thus there are only four possible blocks, namely \(\mathtt{00100110},\mathtt{00100111},\mathtt{00110110},\mathtt{00110111}\).

Checking each of these four words by the explicit scanner rules yields, for any initial state \(q\in\{\emptyset,0,1\}\), the exact transfer
\[
\boxed{\mathcal T(B_j;q)=\big(3-p_j+\mathbf1_{\{q=1\}},\;q_j\big),\qquad q_j=\begin{cases}\emptyset,&p_j=0,\\1,&p_j=1.\end{cases}}
\]
Here the first coordinate is the number of newly completed arches and the second is the final scanner state. Crucially, the transfer is independent of \(j\bmod2\). Its verification consists of twelve elementary cases, all included in the standalone verifier.

**Telescoping.** After one full block the state is \(q_j\), so consecutive complete blocks \(B_\ell\cdots B_h\), numbering \(K=h-\ell+1\), have the transfer
\[
\boxed{\mathcal T(B_\ell\cdots B_h;q)=\big(3K-p_h+\mathbf1_{\{q=1\}},\;q_h\big).}
\]
This follows by summing \(3-p_\ell+\mathbf1_{\{q=1\}}\) for the first block and \(3-p_j+p_{j-1}\) for subsequent blocks. Starting empty at \(\ell=0\) gives the prefix formula. For an aligned dyadic factor of length \(2^m\), take \(K=2^{m-3}\) and note \(p_{(j+1)K-1}=p_j\), since multiplication of \(j+1\) by a power of two leaves its odd part unchanged.

**Sharp factor bound.** Every nonempty interval may be cut at multiples of eight. If it is within one block, exhaust the four possible block words and all \(0\le r<s\le8\). The resulting integer \(8\iota(v)-3|v|\) is between \(-10\) and \(6\). If it meets exactly two adjacent blocks, take the suffix of one and prefix of the next, exhausting the four choices for each and all \(0\le r<8\), \(1\le s\le8\); the range is \([-11,7]\).

Finally, suppose the interval includes \(K\ge1\) complete blocks between its two partial endpoint blocks. Let \((c,q)\) be the scanner result on the initial suffix, started empty; let \(\eta\in\{0,1\}\) be the last bit of the final complete middle block; and let \(t\) be the arch count when scanning the terminal prefix starting with state \(\emptyset\) if \(\eta=0\), and state \(1\) if \(\eta=1\). If the partial lengths are \(8-r\) and \(s\), the telescoping lemma yields
\[
8\iota(v)-3|v|=8\big(c+\mathbf1_{\{q=1\}}-\eta+t\big)-3(8-r+s).
\]
The \(3K\) contribution cancels exactly against the middle length \(8K\). Enumerate four possible words for each endpoint, two values of \(\eta\), and the same finite ranges of \(r,s\); the resulting range is precisely \([-11,7]\). These are *universal finite case reductions*, not experiments on a long prefix: every conceivable interval falls into one of the three exhaustive regimes, and every endpoint block belongs to the four proved shapes. The provided standalone code implements and checks all three finite tables from the scanner definition.

The two literal factors in the finding have arch count \(5\); substituting their lengths gives the lower and upper equalities. Dividing the inequality by \(8N\) proves the uniform limit.

## Verification
Run `python3 verify.py` from this directory. The verifier checks the twelve block-transfer cases and the complete finite endpoint reductions (one block, adjacent blocks, at least one complete interior block). It separately constructs the first \(4096\) letters from the odd-part definition and checks the block identity, prefix formula, and bound for every factor wholly contained in that prefix. It checks the two sharpness witnesses. The full infinite proof relies on the block identity, transfer/telescoping, and exhaustive finite endpoint cases, not on finite-prefix induction.

## Relationship to prior work
Schnoebelen and Veron (2023) give the general greedy-arch characterization of subsequence universality and methods for composing universality signatures. Shallit and Xu (2023) investigate repetition factorizations in paperfolding and other automatic sequences, rather than subsequence universality. Adamson and collaborators (2023) study subsequence universality in regular languages via automata. The finding applies the arch concept to the regular paperfolding word to obtain an exact all-factor sharp discrepancy and dyadic-prefix law; these quantitative results do not follow as stated from the cited general algorithms or the distinct repetition-factorization theorems.

## Limitations
The fixed source is a single regular paperfolding word (or its bitwise complement); generalized paperfolding sequences with arbitrary fold instructions are not covered. The theorem gives a sharp interval for the universality index, not the complete distribution of factor indices at each fixed length. No assertion of uniqueness against all unindexed literature is made.

## References
1. Philippe Schnoebelen and Julien Veron, *On arch factorization and subword universality for words and compressed words*, arXiv:2304.11932v1 (first posted 2023-04-24), https://arxiv.org/abs/2304.11932.
2. Jeffrey Shallit and Xinhao Xu, *Repetition factorization of automatic sequences*, arXiv:2311.14961 (first posted 2023-11-25), https://arxiv.org/abs/2311.14961.
3. Duncan Adamson, Pamela Fleischmann, Annika Huch, Tore Koß, Florin Manea, and Dirk Nowotka, *k-Universality of Regular Languages*, arXiv:2311.10658v1 (first posted 2023-11-17), https://arxiv.org/abs/2311.10658.

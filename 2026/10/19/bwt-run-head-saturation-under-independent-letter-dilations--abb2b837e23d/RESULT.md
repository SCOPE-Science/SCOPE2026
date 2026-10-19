# BWT run-head saturation under independent letter dilations

## Finding

Let \(\Sigma\) be any finite totally ordered alphabet, and let \(w\in\Sigma^+\). For an integer vector \(\mathbf h=(h_a)_{a\in\Sigma}\), with every \(h_a\ge2\), define the letter-dilation morphism
\[
\Psi_{\mathbf h}(a)=a^{h_a}.
\]
For a nonempty word \(v\), let \(\operatorname{BWT}(v)\) be the last column of its **lexicographically sorted cyclic rotations without a sentinel**, counting all starting positions even when some rotations coincide. For a word \(v\), write \(\operatorname{heads}(v)\) for its run-length-encoding word of successive distinct symbols, and \(r(v)=|\operatorname{heads}(v)|\).

**Theorem (run-head saturation).** For every nonempty \(w\) and every such \(\mathbf h\),
\[
\operatorname{heads}\!\left(\operatorname{BWT}(\Psi_{\mathbf h}(w))\right)
=\operatorname{heads}\!\left(\operatorname{BWT}(\Psi_{\mathbf 2}(w))\right),
\qquad \mathbf 2=(2,\ldots,2).
\]
In particular, the **exact linear BWT run count** does not depend on any dilation exponent once all exponents are at least two. This is stronger than mere equality of counts for binary words: even over arbitrarily large ordered alphabets, the entire sequence of BWT run labels stabilizes.

There is an explicit all-parameter decomposition of the *whole transformed word*, not only its run labels, given below. The lower bound two is sharp: \(\operatorname{BWT}(01)=10\), whereas \(\operatorname{BWT}(0011)=1010\). More specifically, with \(\Psi(0)=0\), \(\Psi(1)=11\), the BWT has two runs, but with both letter exponents equal to two it has four.

## Assumptions and scope

The alphabet is finite and totally ordered, the word is nonempty, and the BWT convention is **cyclic and sentinel-free**, not the suffix BWT with a unique end marker. Repeated cyclic rotations are included with multiplicity. Their tie ordering cannot change BWT because identical cyclic rotations necessarily have the same preceding symbol. Run count refers to the linear last-column word, not circular run count. All exponents associated with letters that actually appear in \(w\) must be integers at least two. No primitivity, balance, sparsity, aperiodicity, or binary-alphabet assumption is required.

For the decomposition, assume \(w\) contains at least two distinct symbols; for a monochromatic word both sides of the theorem are the same one-letter run. Regard \(w\) circularly and list its maximal circular runs \(\rho\). Write \(a_\rho\) for a run symbol, \(L_\rho\ge1\) for its length, \(c_\rho\ne a_\rho\) for its preceding symbol, and \(b_\rho\ne a_\rho\) for the symbol following it. Let \(t_\rho\) denote the infinite periodic word beginning immediately after the run, read in the *unexpanded* circular \(w\).

For each symbol \(a\), sign \(\varepsilon\in\{-,+\}\), and integer \(q\ge1\), define \(\mathcal R_{a,-}(q)\) to be the set of circular maximal \(a\)-runs with \(b_\rho<a\) and \(L_\rho\ge q\), and \(\mathcal R_{a,+}(q)\) analogously with \(b_\rho>a\). Let \(R_{a,\varepsilon}(q)=|\mathcal R_{a,\varepsilon}(q)|\). Define \(B_{a,\varepsilon}(q)\) by sorting the runs in \(\mathcal R_{a,\varepsilon}(q)\) according to the lexicographic order of \(t_\rho\), then listing, for each run, \(c_\rho\) if \(L_\rho=q\), and \(a\) otherwise. Identical \(t_\rho\) yield identical listed symbols, so the sort is unambiguous. Write \(M_{a,\varepsilon}=\max\{L_\rho:b_\rho\lessgtr a,\ a_\rho=a\}\), or zero for the empty set. Concatenation over an empty range is the empty word.

## Proof

**Lemma 1 (rotation order).** In \(\Psi_{\mathbf h}(w)\), every cyclic rotation starts within a uniquely specified maximal dilated run \(\rho\) of some letter \(a\). It has an initial block of \(a\)'s of length \(t\), where \(1\le t\le h_aL_\rho\), and this block is followed by the first different symbol \(b_\rho\). Among the rotations starting with \(a\), those with \(b_\rho<a\) precede all those with \(b_\rho>a\). In the first group the values of \(t\) are in increasing order; in the second group they are in decreasing order. For fixed \(t\), the rotation order is the lexicographic order of the dilated infinite continuations \(\Psi_{\mathbf h}(t_\rho)\), equivalently of \(t_\rho\).

To prove this, compare two rotations at their first different position. For unequal initial-run lengths, the one whose run ends first shows \(b_\rho\ne a\) against the still continuing \(a\), fixing the comparison by whether \(b_\rho<a\) or \(b_\rho>a\). The same argument handles a lower-following versus higher-following rotation regardless of lengths. If the lengths agree, compare the next infinite continuations. Every letter-dilation \(a\mapsto a^{h_a}\) preserves lexicographic order on distinct infinite sequences because it replaces their shared prefix by the same expanded prefix and the first different characters remain different in the same order. If two after-run continuations are identical, their circular run lengths and preceding symbols coincide (they are shifts of the same periodic word), so tie ordering makes no difference. The finite cyclic rotations compare in the same way as their periodic continuations; identical full rotations again have identical preceding symbols.

**Lemma 2 (last-column decomposition).** For each \(a\), its contiguous block in the BWT is
\[
\mathcal C_a(\mathbf h)=
\left[\prod_{q=1}^{M_{a,-}}
 a^{(h_a-1)R_{a,-}(q)}B_{a,-}(q)\right]
\left[\prod_{q=M_{a,+}}^{1}
 B_{a,+}(q)a^{(h_a-1)R_{a,+}(q)}\right].
\]
Products denote concatenation in the displayed order. Consequently,
\[
\operatorname{BWT}(\Psi_{\mathbf h}(w))
=\prod_{a\in\operatorname{alph}(w)\ \mathrm{in\ ascending\ order}}
\mathcal C_a(\mathbf h).
\]

Indeed, a run \(\rho\) contributes exactly one rotation for every integer initial \(a\)-run length \(t\in[1,h_aL_\rho]\). Its preceding symbol, recorded by BWT, is \(c_\rho\) only when \(t=h_aL_\rho\), and is \(a\) otherwise. For \((q-1)h_a<t<qh_a\), exactly \(R_{a,\varepsilon}(q)\) rows in the relevant sign group occur at each \(t\), and all of their preceding letters are \(a\). There are \(h_a-1\) such lengths, giving \(a^{(h_a-1)R_{a,\varepsilon}(q)}\). At the remaining value \(t=qh_a\), the preceding letters, in the order from Lemma 1, are precisely \(B_{a,\varepsilon}(q)\). The lower-following blocks occur with increasing \(q\), the higher-following blocks with decreasing \(q\). This accounts for every starting position once and proves both identities.

**Conclusion.** Every \(q\) in either displayed product satisfies \(R_{a,\varepsilon}(q)\ge1\). If \(h_a\ge2\), every occurrence of \(a^{(h_a-1)R_{a,\varepsilon}(q)}\) is therefore a **nonempty** monochromatic block. All words \(B_{a,\varepsilon}(q)\), their order, and the sequence of inserted block symbols are independent of the vector \(\mathbf h\). Replacing the length of each positive monochromatic block by another positive length cannot alter the run-head sequence of the concatenation, including at its boundaries. Thus the run-head sequence is exactly the one at \(\mathbf h=\mathbf2\), proving the theorem. The one-letter case was handled above. The example \(w=01\) proves the threshold cannot in general be lowered.

## Verification

The standalone program `verify.py` constructs the BWT independently by directly sorting every cyclic rotation and constructs the predicted BWT from circular runs and their post-run continuations. It compares the **entire strings**, not merely their run counts. It exhaustively checks all mixed binary words of lengths two through nine, ternary words of lengths two through seven, and quaternary words of lengths two through six, against four dilation vectors for each word: 38,792 expanded-word comparisons in total. An independent cyclic suffix-doubling BWT algorithm additionally checks 220 seeded random inputs (lengths 15 through 100, alphabets of size two through six and independent letter exponents between two and eight). The script also verifies the sharp one-letter counterexample. The observed output is:

`VERIFY_OK full_multialphabet_BWT_decomposition exhaustive_cases=38792 randomized_suffix_doubling_cases=220 sharp_h1=01`

These are finite cross-checks of the claimed structural formula. The unrestricted theorem is proved above; it is not inferred from the tests.

## Relationship to prior work

Burrows and Wheeler introduced the underlying cyclic-rotation transform in their 10 May 1994 technical report. Mantaci, Restivo, Rosone, Sciortino, and Versari (2017), Theorem 3.3 and Proposition 3.9, bound the transformed run count by twice the source run count and show that **expanding one letter cannot decrease the BWT run count**. Neither inequality determines whether the count stabilizes after every letter has been duplicated. The present theorem gives exact equality for all further **independent** dilations and, more strongly, equality of the entire run-head sequence; its proof refines the rotation partition by initial run length and by the direction of the next different symbol. For example, for \(w=00110\), the doubled word has four BWT runs, so the count is not forced to the general upper bound of six.

Frosini, Mancini, Rinaldi, Romana, and Sciortino (2022) study growth bounds for the BWT run count of families generated by iterated morphisms, with particular results for binary purely morphic words. Their asymptotic bounds do not provide this arbitrary-parent, arbitrary-alphabet, finite one-step stabilization or explicit decomposition. Related exact BWT evaluations for special automatic and morphic families likewise do not imply it without further arguments.

## Limitations

The result is for cyclic BWT **without a unique sentinel**; no statement is made for a sentineled suffix transform or bijective BWT. Exponents are constant per letter but may differ between letters; distinct occurrences of the same letter must receive the same expansion length. The condition that every present letter exponent is at least two is essential as a uniform universal guarantee. The theorem does not assert that the run lengths of the resulting BWT are invariant—only their ordered run symbols and their count. Exhaustive experiments cover only finite words and do not certify novelty; earlier equivalent formulas under different terminology remain a residual possibility.

## References

1. M. Burrows and D. J. Wheeler, *A Block-sorting Lossless Data Compression Algorithm*, Digital Equipment Corporation Systems Research Center Research Report 124, 10 May 1994, https://www.cl.cam.ac.uk/teaching/2425/Bioinfo/papers/burrows_wheeler.pdf.
2. S. Mantaci, A. Restivo, G. Rosone, M. Sciortino, and L. Versari, *Measuring the clustering effect of BWT via RLE*, Theoretical Computer Science **698** (2017), 79–87, https://doi.org/10.1016/j.tcs.2017.07.015; lawful author postprint https://pages.di.unipi.it/rosone/Papers/MRRSV_TCS2017.pdf.
3. A. Frosini, I. Mancini, S. Rinaldi, G. Romana, and M. Sciortino, *Logarithmic equal-letter runs for BWT of purely morphic words*, arXiv:2202.02609, first posted 5 February 2022, https://arxiv.org/abs/2202.02609.

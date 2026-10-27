# Exactly five minimal unique substrings in every nontrivial Mephisto–Waltz iterate

## Finding

Let \(\varphi(0)=001\), \(\varphi(1)=110\), and \(W_m=\varphi^m(0)\). A **minimal unique substring** (MUS) of a finite word is a factor occurring precisely once whose one-symbol left and right deletions both occur at least twice. All positions below are zero-based.

**Theorem.** For every integer \(m\ge2\), put \(r=3^{m-2}\). The complete MUS set of \(W_m\) consists of exactly five occurrences; each has length \(r+2\), and their starting positions are precisely
\[
\{2r-1,\;3r-1,\;5r-1,\;6r-1,\;7r-1\}.
\]
In particular, the shortest unique factor length is \(r+2\), and the number of minimal unique factors is independent of the iterate order.

## Assumptions and scope

The alphabet is exactly \(\{0,1\}\); the morphism is applied in parallel, starting from the single letter \(0\). The theorem concerns finite iterates \(W_m\), not all finite factors of the infinite fixed point. Occurrences are intervals rather than distinct factor values; each claimed MUS value has exactly one occurrence. A word of length one may be an MUS if unique, but the claimed iterates have neither unique one-letter nor unique two-letter factors.

## Proof

**1. Exact base case.** The word \(W_2=001001110\). Each of \(00,01,10,11\) occurs exactly twice. Among its seven length-three factors, \(001\) occurs twice, while the five factors beginning at positions \(1,2,4,5,6\) occur exactly once. All five are therefore MUSs. Every length-four factor contains one of those five unique triples: a length-four factor beginning at position \(0\) or \(3\) contains a unique triple beginning one position later, while all other length-four starts already have a unique initial triple. Hence no length-four (or longer) factor is minimal unique. This proves the theorem at \(m=2\).

**2. Unique image-phase decoding.** Each aligned length-three image block is either \(001\) or \(110\). Directly inspecting the four possible two-block concatenations \(001001,001110,110001,110110\), neither image block starts at offset one or two modulo three. Every factor \(F\) of \(\varphi(w)\) with length at least five contains a complete aligned image block: at worst its first symbol is the last symbol of one image and the next three symbols form an entire image. Consequently \(F\) determines its starting phase \(e\in\{0,1,2\}\) modulo three uniquely.

Moreover, any nonempty prefix or suffix of \(001\) distinguishes it from the corresponding prefix or suffix of \(110\). Thus, once its phase is fixed, the factor \(F\) uniquely determines the **covering source factor** \(u\) formed by all source symbols whose images meet \(F\). If \(F\) starts at \(3i+e\) and has length \(\ell\), its covering source length is
\[
q=\left\lceil\frac{e+\ell}{3}\right\rceil.
\]
Each occurrence of \(u\) in \(w\) produces an occurrence of \(F\) in \(\varphi(w)\) at the corresponding phase, including occurrences near the ends. Conversely, phase recognition and fragment decoding show that every occurrence of \(F\) comes from an occurrence of \(u\). Therefore, for \(\ell\ge5\), occurrences of \(F\) and of \(u\) are in exact bijection. For shorter \(F\), we only use the always-valid forward implication: if the covering source factor repeats, then \(F\) repeats. These statements hold for every finite binary source word, without any recurrence assumption.

**3. All shortest unique factors lift with phase two.** Assume inductively that all MUSs of \(W_m\) have length \(r+2\) and start at the five asserted positions. It follows that no factor of \(W_m\) of length at most \(r+1\) occurs uniquely. (Any unique factor contains a minimal unique factor, obtained by repeatedly removing a removable endpoint.) Put \(V=\varphi(W_m)=W_{m+1}\).

For any factor of \(V\) with length at most \(3r+1\), its covering source factor has length at most \(r+1\), because its starting phase is at most two. The latter repeats, so the image factor repeats. Thus \(V\) has no unique factor shorter than \(3r+2\).

At length exactly \(3r+2\), factors starting in phases zero and one cover \(r+1\) source letters, hence repeat. A factor beginning in phase two covers exactly \(r+2\) letters. By the occurrence bijection, it is unique precisely if its covering source factor is unique. Every unique factor of \(W_m\) of this minimal length is one of its five MUSs, so there are exactly five unique factors of length \(3r+2\) in \(V\), at starts \(3i+2\), where \(i\) ranges over the five old MUS starts. They are MUSs because all shorter factors repeat. The new parameter is \(r'=3r\), and
\[
3(ar-1)+2=ar'-1\qquad(a\in\{2,3,5,6,7\}).
\]

**4. No longer MUS can arise.** Let \(F\) be any MUS of \(V\) of length at least six. By the occurrence bijection its covering source factor \(u\) is unique. The two one-symbol deletions of \(F\) are repeated and have length at least five. If the starting phase of \(F\) were zero or one, deleting its first symbol would leave a nonempty part of the first image, still distinguishing that source symbol, and would therefore leave the same unique covering source factor \(u\). By the occurrence bijection the shortened factor would remain unique—a contradiction. Hence the first symbol of \(F\) is the *last* symbol of its first image block (phase two).

Likewise, if its last image block contributed at least two symbols, removing the final character would still leave the same unique covering source factor \(u\), contradicting minimal uniqueness. Therefore the last symbol of \(F\) is the *first* symbol of its last image block (ending phase zero). Write \(q=|u|\). These two boundary phases force \(|F|=3q-4\).

Dropping the first character of \(F\) now removes its initial source block entirely, while dropping its last character removes its final source block entirely. Applying the bijection to these repeated shortened image factors shows that both length-\((q-1)\) endpoint deletions of \(u\) repeat in \(W_m\). As \(u\) itself is unique, \(u\) is an MUS of \(W_m\). The induction hypothesis forces \(q=r+2\), so \(|F|=3r+2\). Thus *every* MUS of \(V\) is one of the five already constructed. This completes induction.

## Verification

`checker.py` performs three independently framed finite checks: it verifies all eight nonaligned length-three crossing windows; calculates the exact MUS lists from suffix-array/LCP data for every \(2\le m\le9\); and independently enumerates *all* nonempty substrings with a frequency counter for every \(2\le m\le5\). All outputs are recorded in `checker_output.txt`. Run with `python3 checker.py`; it requires only the Python standard library. The finite checks corroborate the base case and deductions; the induction proves the unbounded quantifier.

## Relationship to prior work

Kishi, Guo, Urbina, and Bannai (2026), *On Occurrence-Preserving Morphisms*, list the Mephisto–Waltz substitution as strongly interference-free (Corollary 16), characterize occurrence-preserving morphisms, and derive MUS classifications for **Fibonacci** and **Thue–Morse** words. Their full-text treatment does not supply the exact five-MUS spectrum of the Mephisto–Waltz iterates; their conclusion identifies fixed points of strongly interference-free morphisms as a further natural direction. The proof here does not need to invoke their characterization: its source-occurrence bijection is derived directly from the two image blocks, and the endpoint argument establishes the complete MUS spectrum.

## Limitations

The classification is restricted to finite iterates of the specified binary length-three morphism with seed zero, starting at iterate two. It does not assert an analogous formula for arbitrary strongly interference-free morphisms, alternative initial words, arbitrary sliding factors of the infinite word, or net occurrences. Historical novelty is assessed against the primary sources and available indexed records, not independently certified against all literature.

## References

1. K. Kishi, P. Guo, C. Urbina, H. Bannai, *On Occurrence-Preserving Morphisms*, arXiv:2605.18034v1, first public 2026-05-18, especially Corollary 16, Section 5 and Section 6. https://arxiv.org/html/2605.18034v1
2. OEIS A064990, Mephisto–Waltz binary sequence (background identification). https://oeis.org/A064990

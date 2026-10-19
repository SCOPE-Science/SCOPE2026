# Exact cyclic and sentinel Burrows–Wheeler transforms of Zimin words

## Finding
For each integer \(n\ge1\), let \(Z_1=1\) and \(Z_n=Z_{n-1}\,n\,Z_{n-1}\) for \(n\ge2\). Equip its alphabet with the order \(1<2<\cdots<n\). Let \(C_n\) be the **sentinel-free cyclic Burrows–Wheeler transform** of \(Z_n\), and let \(B_n\) be the last column obtained by sorting the suffixes of \(Z_n0\), where \(0\) is a unique terminal symbol smaller than all other symbols, and recording the cyclic predecessor of each suffix start.

The transforms have complete closed forms. For every \(n\ge1\),
\[
B_n=(1\,2\,\cdots\,n)\,0\,\operatorname{concat}_{j=n-1,n-2,\ldots,1}j^{\,2^{n-j}-1},
\]
and for every \(n\ge2\),
\[
C_n=(2\,3\,\cdots\,n)\,1\,\operatorname{concat}_{j=n-1,n-2,\ldots,2}j^{\,2^{n-j}-1}\,1^{\,2^{n-1}-1}.
\]
Each \(\operatorname{concat}\) symbol denotes **concatenation of constant-letter blocks in the displayed descending index order**; an empty index list denotes the empty word. Also \(C_1=1\). Consequently, counting maximal equal-letter runs in the **linear output word**,
\[
r(C_1)=1,\qquad r(C_2)=2,\qquad r(C_n)=2n-1\quad(n\ge3).
\]
The input has \(2^n-1\) linear runs, so \(r(C_n)/r(Z_n)=(2n-1)/(2^n-1)\to0\) as \(n\to\infty\) for \(n\ge3\).

## Assumptions and scope
All words are finite and use the explicitly specified order on the integer alphabet. The superscript on a letter denotes repetition; \(j^e\) is a word consisting of \(e\) copies of the symbol \(j\), **not** integer exponentiation. The transform \(C_n\) sorts all \(2^n-1\) length-\(2^n-1\) cyclic rotations and records each rotation's preceding symbol. The sentinel transform \(B_n\) sorts all \(2^n\) suffixes of \(Z_n0\) (equivalently all rotations of \(Z_n0\)), recording predecessors with wraparound. Thus \(B_n\) includes the terminal symbol and differs from \(C_n\). The recurrence for Zimin words implies that \(Z_n\) has one occurrence of its greatest symbol and so its rotations are distinct. All claims have the quantifiers stated above, with separate small cases.

## Proof
**Step 1: parity decomposition.** Put \(W=Z_{n-1}\) and \(m=|W|=2^{n-1}-1\). The recursion gives
\[
Z_n=1\,(W_1+1)\,1\,(W_2+1)\cdots1\,(W_m+1)\,1.
\]
Every odd position of \(Z_n\) carries \(1\); every even position carries a symbol at least \(2\). The final symbol is \(1\).

**Step 2: an exact recursion with a sentinel.** Let \(\alpha\) act letterwise by \(\alpha(0)=0\) and \(\alpha(a)=a+1\) for positive symbols. The suffix of \(Z_n0\) beginning at the odd position \(2i+1\), for \(0\le i\le m\), is the image of the suffix of \(W0\) beginning at index \(i\) under the length-two, order-preserving morphism \(a\mapsto 1\alpha(a)\). Indeed, the image of the unique terminal \(0\) is \(10\); for other letters it is \(1\,(a+1)\). Since the first character is always \(1\) and the second is strictly increasing with the parent letter (including \(0\)), the lexicographic ordering of these odd-start suffixes is exactly that of the parent suffixes.

The suffix starting with terminal \(0\) comes first and has preceding letter \(1\). All suffixes starting at even positions begin with symbols at least \(2\), come last, and have preceding letter \(1\). Inside the middle group of odd-start suffixes, the predecessor is \(\alpha\) of the predecessor at the corresponding parent suffix start: at the first starting position both are \(0\), and at every other odd position this follows from the parity decomposition. Hence, with \(B_1=10\),
\[
B_n=1\,\alpha(B_{n-1})\,1^{m}\qquad(n\ge2).
\]

**Step 3: cyclic rotations and the closing seam.** Define the letter map \(\beta(0)=1\), \(\beta(a)=a+1\) for positive \(a\). All odd-start cyclic rotations begin with \(1\) and precede all even-start rotations; all even-start rotations have predecessor \(1\). We claim that the order of odd-start rotations agrees with the order of suffixes of \(W0\). Compare two different parent suffixes. At their first differing symbol, two ordinary symbols \(a,b\ge1\) become \(a+1,b+1\) at the corresponding even offset after the common \(1\); this preserves the comparison. If one suffix instead reaches the terminal \(0\), the corresponding cyclic rotation first reaches the seam after the final \(1\) of \(Z_n\), immediately followed by the initial \(1\). Its comparison symbol at that offset is therefore \(1\), which is smaller than any competing \(b+1\ge2\). This again agrees with the order \(0<b\). No further letters are needed, because the parent suffixes ending in their unique terminal \(0\) have a first difference before or at that terminal. Thus the odd-start order is the parent suffix order.

The predecessor in the odd-start group is \(\beta\) of the predecessor of the associated parent suffix: the parent start at its beginning has preceding \(0\), replaced by the final \(1\) of \(Z_n\), whereas all other predecessors increase by one. The \(m\) even-start rotations contribute only \(1\). Therefore
\[
C_n=\beta(B_{n-1})\,1^{m}\qquad(n\ge2).
\]

**Step 4: solve the recurrences.** The base \(B_1=10\) and \(B_n=1\alpha(B_{n-1})1^m\) give inductively the stated \(B_n\) formula: prefix \(1,2,\ldots,n,0\), then descending constant blocks \(j^{2^{n-j}-1}\) for \(j=n-1,\ldots,1\). Applying \(\beta\) to \(B_{n-1}\) and appending \(1^{2^{n-1}-1}\) gives exactly the stated formula for \(C_n\). This proves **all output symbols in their exact order**, not just the run count.

**Step 5: boundary cases and runs.** Directly \(C_1=1\) and \(C_2=211\), so the run counts are \(1\) and \(2\). For \(n\ge3\), the displayed block list of \(C_n\) has \(n-1\) singleton blocks \(2,3,\ldots,n\), then one \(1\) block, then \(n-2\) nonempty descending blocks \(n-1,n-2,\ldots,2\), and one final nonempty \(1\) block. All neighbors differ, yielding \((n-1)+1+(n-2)+1=2n-1\) runs. The input alternates odd-position \(1\) with even-position symbols at least \(2\), so every adjacent pair of its \(2^n-1\) symbols differs. This proves the input run count and the ratio.

## Verification
The standalone Python 3 script `verify.py` uses only the standard library. It constructs Zimin words independently via the dyadic valuation identity \(Z_n[t]=1+\nu_2(t)\), using one-based positions. It compares both formulas with direct sorts of the full cyclic rotations and full suffixes through \(n=9\), and with independently implemented circular and linear suffix-doubling sorts through \(n=16\). It also checks the exact odd-rotation/sentinel-suffix ordering at each level from \(2\) through \(16\), the boundary cases, and the run counts. Its observed output is:

```text
VERIFY_OK zimin_BWT direct_cyclic=9 direct_sentinel=9 independent_doubling_levels=16 odd_rotation_suffix_order_levels=15 max_level=16 max_word_length=65535 max_cyclic_runs=31
```

These are finite consistency checks, not an infinite computational certificate. The unrestricted result follows from the displayed symbolic recursion proof.

## Relationship to prior work
Burrows and Wheeler's original 1994 technical report defines the cyclic transform and its relationship with suffix sorting. Rytter and Shur (2014), and Cooper and Rorabaugh (2014), examine Zimin patterns in other contexts. Berstel's survey (2007) discusses the simple BWT of binary Sturmian words, while Ferenczi and Zamboni (2023) characterize *clustering* (a transform with one contiguous block per alphabet symbol) in Arnoux–Rauzy and certain episturmian languages. For \(n\ge3\), the present Zimin transform has \(2n-1>n\) runs and therefore is not a clustering transform in that sense. Frosini and collaborators (2022) analyze general run growth of fixed-alphabet purely morphic words; their asymptotic coverage does not supply the present ordered closed form for a recursively expanding alphabet. The precise formulas and simultaneous sentinel/cyclic comparison have not been identified in the inspected materials; this is an evidence-bounded originality assessment, not a uniqueness claim.

## Limitations
The alphabet size increases with \(n\), and the letter order \(1<\cdots<n\) is essential. The result does not claim that every Zimin-like word, every alphabet order, or any finite-alphabet coding has this BWT. The cyclic BWT and suffix/sentinel BWT differ and must not be interchanged. Run counts refer to **linear** runs in the output string. There is no claimed downstream compression bit-cost guarantee, since encoding an alphabet of growing size has its own cost. Independent external audit has not been performed.

## References
- M. Burrows and D. J. Wheeler, *A Block-sorting Lossless Data Compression Algorithm*, SRC Research Report 124, dated 1994-05-10. https://www.mit.edu/~6.454/www_fall_2002/bwt/burrowswheeler94.pdf
- W. Rytter and A. Shur, *On Searching Zimin Patterns*, arXiv:1409.8235, first version 2014. https://arxiv.org/abs/1409.8235
- J. Cooper and D. Rorabaugh, *Bounds on Zimin Word Avoidance*, arXiv:1409.3080, 2014. https://arxiv.org/abs/1409.3080
- J. Berstel, *Sturmian and Episturmian Words*, CAI 2007, survey. https://igm.univ-mlv.fr/~berstel/Articles/2007SturmianThessalonique.pdf
- S. Ferenczi and L. Q. Zamboni, *Clustering and Arnoux–Rauzy Words*, arXiv:2305.18986, 2023. https://arxiv.org/abs/2305.18986
- A. Frosini et al., *Logarithmic Equal-Letter Runs for BWT of Purely Morphic Words*, arXiv:2202.02609, 2022. https://arxiv.org/abs/2202.02609

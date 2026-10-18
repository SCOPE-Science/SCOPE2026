# Two-letter circular overhang without a square in a ternary morphic word

## Finding

Let the morphism \(h\) on \(\{0,1,2\}\) be defined by
\[
h(0)=01,\qquad h(1)=21,\qquad h(2)=0,
\]
and let \(p=h^{\omega}(0)=0121021010210121\cdots\) be its one-sided fixed point. For \(a\in\{0,1\}\) and each integer \(k\geq3\), put \(u_{k,a}=h^k(a)\) and \(m_{k,a}=|u_{k,a}|\). For a finite nonempty word \(u\), define its **two-letter circular overhang spectrum**
\[
\mathcal C_2(u)=\{(u^\omega)[i\ldots i+|u|+1]:0\le i<|u|\},
\]
where \(u^\omega\) is the infinite periodic repetition of \(u\), and positions are zero-based.

**Theorem.** For both choices \(a=0,1\), and for every \(k\ge3\),
\[
\boxed{\mathcal C_2(u_{k,a})\subseteq\operatorname{Fact}_{m_{k,a}+2}(p),
\qquad u_{k,a}u_{k,a}\notin\operatorname{Fact}_{2m_{k,a}}(p).}
\]
Thus each cyclic rotation of \(u_{k,a}\), followed by its first two wraparound letters, occurs contiguously in \(p\), even though two successive copies of the prescribed word never occur. In particular, the Lie complexity \(L_p(m)\), which counts cyclic-conjugacy classes all of whose elements are factors of \(p\), is positive at the infinitely many distinct lengths \(m=m_{k,a}\).

## Assumptions and scope

A **factor** is a contiguous finite subword. The notation \(\operatorname{Fact}_n(p)\) denotes the set of length-\(n\) factors of \(p\); cyclic overhangs refer to the periodic continuation of the *finite candidate word*, not to a periodic continuation of \(p\). No assertion is made that every square or every cyclic rotation's square is absent, or that these are the only lengths at which \(L_p\) is nonzero.

The theorem has no probability or numerical tolerance assumptions. All letter indices are zero-based in the finite certificates below. Both families include all iterates from \(k=3\) onward, not just the checked finite values.

## Proof

**1. A two-letter lifting lemma.** Suppose \(u\) is a nonempty word with no occurrence of \(22\) when viewed cyclically, and \(\mathcal C_2(u)\subseteq\operatorname{Fact}(p)\), where the right-hand side is the union of factor sets of all lengths. Then
\[
\mathcal C_2(h(u))\subseteq\operatorname{Fact}(p).
\]
Indeed, take an arbitrary starting position of a window of length \(|h(u)|+2\) in \((h(u))^\omega\). It lies at offset \(s\in\{0,1\}\) inside the image \(h(u_i)\) of some cyclic letter \(u_i\). Take the circular two-letter overhang of \(u\) starting at position \(i\): it is the cyclic rotation \(u_i\cdots u_{i+|u|-1}\), followed by \(u_i u_{i+1}\). By hypothesis that entire word is a factor of \(p\), hence its image under \(h\) is also a factor of \(p=h(p)\). This image consists of one full cyclic rotation of \(h(u)\), followed by \(h(u_i)h(u_{i+1})\). Because the cyclic pair \(u_i u_{i+1}\) is not \(22\),
\[
|h(u_i)|+|h(u_{i+1})|\ge3\ge s+2.
\]
Starting at offset \(s\), therefore, leaves at least \(|h(u)|+2\) letters, exactly the required circular window of \(h(u)\). This proves the lemma, including positions inside two-letter images.

Every image word \(h(u)\) contains no cyclic \(22\): each image block ends in \(0\) or \(1\), and the only \(2\) occurs as the first letter of \(h(1)=21\), immediately followed by \(1\). Consequently, the lifting lemma may be iterated indefinitely.

**2. Exact finite seed certificates.** The third iterates are
\[
u_{3,0}=0121021,\qquad u_{3,1}=01021,
\]
and the sixth iterate of \(0\), which is a prefix of \(p\), is
\[
h^6(0)=0121021010210121010210121021012101021.
\]
For cyclic starting positions \(i=0,\ldots,6\) of \(u_{3,0}\), the corresponding length-nine overhangs occur in that prefix at zero-based positions
\[
(0,22,23,8,18,19,20),
\]
respectively. For cyclic starting positions \(i=0,\ldots,4\) of \(u_{3,1}\), the length-seven overhangs occur at positions
\[
(7,3,4,5,6),
\]
respectively. The exact strings and all cited positions are checked by the accompanying standalone script. These twelve explicit finite witnesses establish both seed inclusions, with no inference from sampling. Applying the lifting lemma inductively proves the overhang inclusion for every \(a\in\{0,1\}\) and \(k\ge3\).

**3. Exclusion of the prescribed squares.** Four length-two factors are forbidden in \(p\):
\[
00,\quad11,\quad20,\quad22.
\]
To see this directly, each occurrence of \(2\) in \(p=h(p)\) is the first letter of the block \(21=h(1)\), so \(20\) and \(22\) do not occur. Each occurrence of \(1\) is the final letter of an image block; the following image starts with \(0\) or \(2\), so \(11\) does not occur. An occurrence of \(00\) can only cross an image-block boundary. Its left block would have to be \(h(2)=0\) and the next block would have to be \(h(0)\) or \(h(2)\), requiring the factor \(20\) or \(22\) in the preimage \(p\). Both are already excluded, so \(00\) is absent as well.

The three codewords \(\{01,21,0\}\) form a **suffix code**: none is a proper suffix of another. Thus any factor of \(h(p)\) that ends at an image-block boundary and is itself a concatenation of these codewords decodes uniquely right-to-left to a factor of \(p\). For every \(a\in\{0,1\}\) and \(k\ge1\), the word \(h^k(a)\) ends in \(1\). If \(h^k(a)h^k(a)\) were a factor of \(p\), it would end at an image-block boundary, since every \(1\) in \(p\) ends a block. Unique suffix decoding would then give \(h^{k-1}(a)h^{k-1}(a)\) as a factor of \(p\). Repeating this argument \(k\) times would give \(aa=00\) or \(aa=11\), both forbidden. Hence none of these prescribed squares occurs.

**4. Unbounded lengths.** Every \(h^k(a)\) with \(k\ge3\) contains a letter from \(\{0,1\}\). Applying \(h\) increases length by the number of \(0\)s and \(1\)s, which is at least one, so the lengths \(m_{k,a}\) strictly increase with \(k\). Every cyclic rotation of \(u_{k,a}\) is the first \(m_{k,a}\) letters of a certified overhang, so its full cyclic class occurs among the factors of \(p\). This proves the Lie-complexity conclusion and the theorem. \(\square\)

## Verification

Run `python3 verify_cyclic_overhang.py` with Python 3 and no third-party packages. It checks each of the twelve listed seed positions exactly; enumerates all cyclic overhang phases for both families through \(k=8\) in a length-\(17991\) prefix; checks the absence of the prescribed squares in that prefix; and independently checks the four forbidden length-two factors in that prefix. All checks passed. The unlimited statement follows from the preceding lifting lemma and suffix-code argument, not from finite exploration.

## Relationship to prior work

Currie, Ochem, Rampersad and Shallit introduced and studied this specific ternary fixed point, establishing its complexity, repetition properties, balance, bispecial lengths and forbidden-factor characterization. Their explicit forbidden-factor theorem supports the context, but the present proof does not assume it. The inspected material does not give the simultaneous two-letter cyclic-overhang property.

Bell and Shallit introduced Lie complexity, proving general bounds and computing examples including a different ternary squarefree morphic word. In particular, Lie-complexity positivity without squares is already known in other words and is **not** presented as new here. The added content is the precise all-iterate two-letter overhang theorem for the present fixed point, with its explicit disjointness from the prescribed root squares. De Luca and Fici treated Sturmian words; this word is ternary and not Sturmian.

## Limitations

This does not determine the exact Lie-complexity function, the complete set of admissible lengths, multiplicities of conjugacy classes, or higher cyclic-overhang radii. The proof excludes squares of the indicated words themselves, not the squares of every one of their rotations. Searches of accessible records and primary papers do not rule out unindexed equivalent literature; there has been no independent audit.

## References

1. J. Currie, P. Ochem, N. Rampersad, and J. Shallit, *Properties of a Ternary Infinite Word*, arXiv:2206.01776v1 (first public posting 2022-06-03), https://arxiv.org/abs/2206.01776.
2. J. P. Bell and J. Shallit, *Lie Complexity of Words*, arXiv:2102.03821v1 (2021), https://arxiv.org/abs/2102.03821.
3. A. De Luca and G. Fici, *On the Lie Complexity of Sturmian Words*, arXiv:2206.00995 (2022), https://arxiv.org/abs/2206.00995.
4. J. Cassaigne, G. Fici, M. Sciortino, and L. Q. Zamboni, *Cyclic Complexity of Words*, arXiv:1402.5843 (2014), https://arxiv.org/abs/1402.5843.

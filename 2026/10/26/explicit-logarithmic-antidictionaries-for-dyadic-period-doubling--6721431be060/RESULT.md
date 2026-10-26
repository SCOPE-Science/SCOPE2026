# Explicit logarithmic antidictionaries for dyadic period-doubling prefixes

## Finding

Define the binary morphism \(\mu(0)=01\), \(\mu(1)=00\), and its dyadic words \(W_k=\mu^k(0)\) of length \(2^k\). A **minimal absent factor** of a finite binary word is a binary word of length at least two which does not occur contiguously, although both its proper prefix and proper suffix of length one less do occur. Let \(\operatorname{MAW}(W_k)\) denote the set of such words.

**Theorem.** For every integer \(k\ge3\), the set \(\operatorname{MAW}(W_k)\) contains at least \(2k-1\) distinct words. In fact, the following \(2k-1\) words are pairwise distinct minimal absent factors:

\[
11;\qquad \Psi^j(0000),\ \Psi^j(1001)\quad(0\le j\le k-3);\qquad
c_{k-2}W_{k-2}0,\quad c_{k-1}W_{k-1},
\]
where \(\Psi(v)=\mu(v)[1:]\) removes the initial symbol from \(\mu(v)\), and \(c_r\) is the last symbol of \(W_r\). Here \(\Psi^0\) is the identity.

The final two words are **finite-prefix boundary obstructions**: they are distinct from the two morphic towers of words forbidden in the infinite fixed point. This theorem is a lower bound, not an assertion that no other minimal absent factors exist.

## Assumptions and scope

All words are binary and positions are indexed from zero. For a nonempty finite word \(v\), write \(v[:-1]\) for deletion of its final symbol and \(v[1:]\) for deletion of its initial symbol; thus \(\Psi(v)=\mu(v)[1:]\). A minimal absent factor of length two is permitted, and its one-letter prefix and suffix must occur. The theorem concerns the particular one-sided substitution prefixes \(W_k\) for integers \(k\ge3\); it does not assert a classification of all minimal absent factors or extend to arbitrary morphisms.

## Proof

**Step 1: substitution identities and a factor-occurrence lemma.** The words satisfy
\[
W_k=W_{k-1}W_{k-2}W_{k-2}\quad(k\ge2),
\]
because \(\mu^{k-1}(1)=W_{k-2}^2\). Also \(c_{r+1}=1-c_r\), since the final symbol of \(\mu(a)\) is the complement of \(a\). The words \(W_r\) and \(W_{r-1}W_{r-1}\) differ exactly in their last symbol for every \(r\ge1\): this holds for \(r=1\), since \(01\) and \(00\) differ only at the end, and is preserved by \(\mu\), as \(\mu(0)\) and \(\mu(1)\) differ only in their last symbol. Consequently,
\[
W_r[:-1]=(W_{r-1}W_{r-1})[:-1].
\]

We claim that for each \(k\ge3\), \(W_{k-2}\) occurs in \(W_k\) at **exactly** the positions
\[
0,\qquad 2^{k-1},\qquad 3\cdot2^{k-2}.
\]
At \(k=3\) this is checked directly from \(W_3=01000101\) and \(W_1=01\): the starts are \(0,4,6\). In the infinite fixed point \(p=\mu^\omega(0)\), we have \(p_{2n}=0\) and \(p_{2n+1}=1-p_n\). Since \(W_{k-2}\) begins with \(01\), no occurrence can begin at an odd index: its second symbol would be a \(1\) at an even absolute index. Every occurrence therefore begins at an even position \(2i\), where letterwise injectivity of \(\mu\) shows that it corresponds exactly to an occurrence of \(W_{k-3}\) at position \(i\) in \(W_{k-1}\). Doubling the three positions from the inductive case proves the claim.

In particular, \(W_{k-1}\) occurs in \(W_k\) only at position zero for each \(k\ge3\): apply the preceding lemma at \(k+1\) to the longer word \(W_{k+1}\), then restrict occurrences to its length-\(2^k\) prefix \(W_k\).

**Step 2: the two boundary obstructions.** Put \(U=W_{k-2}\), \(m=|U|\), and \(b=c_{k-2}\). Then \(W_k=W_{k-1}UU\), and the occurrence lemma says that the three occurrences of \(U\) start at \(0,2m,3m\). The preceding symbol at \(2m\) is \(c_{k-1}=1-b\), while that at \(3m\) is \(b\). Hence \(bU\) occurs exactly once, as the suffix of \(W_k\). The word \(bU0\) is absent, its length-one-shorter prefix \(bU\) occurs, and its length-one-shorter suffix \(U0\) occurs at the start of \(W_k\) (the symbol following the initial \(U\) is the initial zero of \(\mu^{k-2}(1)\)). Thus \(c_{k-2}W_{k-2}0\) is a minimal absent factor.

Next put \(V=W_{k-1}\) and \(c=c_{k-1}\). Since \(V\) occurs in \(W_k\) only at position zero, \(cV\) is absent. Its suffix \(V\) occurs at position zero. Its prefix \(cV[:-1]\) occurs starting at \(2^{k-1}-1\), since the end of the initial \(V\) is \(c\), followed by \(W_{k-2}^2\), whose length-one-shorter prefix equals \(V[:-1]\) by Step 1. Therefore \(c_{k-1}W_{k-1}\) is also a minimal absent factor.

**Step 3: two towers of globally forbidden words.** The infinite fixed point has no \(11\) because all even-indexed symbols are zero, and no \(1001\) because its two ones would lie at indices of different parity. It also has no \(0000\). Indeed, four consecutive zeros would force two consecutive odd-position symbols to be zero, hence two consecutive preimage symbols to be one, contradicting avoidance of \(11\). The one-letter word \(1\) occurs in every \(W_k\) with \(k\ge1\), so \(11\) is a minimal absent factor of each such prefix.

Suppose a binary word \(v\) contains a zero and is absent from the infinite fixed point. Every second-symbol position of \(\mu(v)\) records the complement of a symbol of \(v\), and \(\Psi(v)=\mu(v)[1:]\) therefore contains a \(1\) at some even relative position. Since all even absolute positions of the infinite fixed point are zero, any occurrence of \(\Psi(v)\) would have to start at an odd absolute position \(2i+1\). Reading its even relative positions would then recover the symbols of \(v\) at positions \(i,\ldots,i+|v|-1\), a contradiction. Thus \(\Psi\) preserves global absence on such words. Both \(\Psi(0000)\) and \(\Psi(1001)\), and all their successors, contain zeros; hence every word in the two towers is globally absent.

It remains to prove minimality within a finite prefix. At level \(j=0\), both \(0000\) and \(1001\) are minimal absent factors of \(W_3=01000101\): for \(0000\), the three-symbol prefix and suffix \(000\) both occur at position \(2\); for \(1001\), prefix \(100\) occurs at position \(1\) and suffix \(001\) at position \(3\). Their prefix occurrences have at least one following symbol.

For any word \(v\),
\[
\Psi(v)[:-1]=\mu(v[:-1])[1:]0,\qquad
\Psi(v)[1:]=\mu(v[1:]).
\]
If \(v[:-1]\) occurs at position \(s\) in \(W_h\) with at least one symbol following that occurrence, then \(\Psi(v)[:-1]\) occurs at \(2s+1\) in \(W_{h+1}\); if \(v[1:]\) occurs at position \(t\), then \(\Psi(v)[1:]\) occurs at \(2t\). Inductively, at level \(j\) the prefix and suffix of \(\Psi^j(0000)\) occur in \(W_{j+3}\) at positions \(3\cdot2^j-1\) and \(2^{j+1}\), respectively; those of \(\Psi^j(1001)\) occur at \(2^{j+1}-1\) and \(3\cdot2^j\), respectively. Each tower word has length \(3\cdot2^j+1\), so the required prefix occurrences always leave a following symbol in the length-\(8\cdot2^j\) word. These proper-prefix and proper-suffix occurrences persist in every longer \(W_k\), while the words themselves are globally absent. Thus for all \(0\le j\le k-3\), both tower words are minimal absent factors of \(W_k\).

**Step 4: distinctness and count.** At each tower level \(j\), the two words have length \(3\cdot2^j+1\) and distinct initial symbols (the initial symbol is complemented by each application of \(\Psi\)). Different levels have different lengths. The first boundary word has length \(2^{k-2}+2\), and the second has length \(2^{k-1}+1\). For \(k\ge4\), the first boundary length is even and at least six, whereas the tower length at level zero is four and all higher tower lengths are odd; the second boundary length cannot equal a tower length because \(2^{k-1}=3\cdot2^j\) has no integer solution. The two boundary lengths differ. For \(k=3\), the first boundary word is \(1010\), distinct from \(0000\) and \(1001\), and the second has length five. All are different from \(11\). Counting gives \(1+2(k-2)+2=2k-1\) distinct minimal absent factors, completing the proof.

## Verification

The bundled `verification.py` directly constructs \(W_k\), verifies the three-position occurrence lemma and all \(2k-1\) exhibited minimal absent factors for \(3\le k\le11\), and separately enumerates all minimal absent factors for \(3\le k\le8\). The finite enumerations yield totals \(5,7,9,11,13,15\) at these six levels; **the theorem does not claim these totals for every level**. The proof for all integers \(k\ge3\) is the substitution induction above, not an extrapolation from these computations. Run the code with `python verification.py` using only Python's standard library.

## Relationship to prior work

Minimal absent words (also called minimal forbidden factors or antidictionary entries) are standard objects for string algorithms and compression. Pinho–Ferreira–Garcia–Rodrigues (2009) define and enumerate them, with their convention excluding length two; the present theorem explicitly includes the nontrivial missing factor \(11\) of length two. Barton–Héliou–Mouchard–Pissis (2014) improve generic enumeration algorithms, without a specialized dyadic period-doubling formula. Currie (2023) analyzes forbidden factors and patterns of the **infinite** period-doubling word via a desubstitution theorem; the globally forbidden tower is compatible with those methods, but the present finite-prefix statement additionally constructs two boundary obstructions per dyadic level and counts explicit minimal absent factors in finite prefixes. These comparisons are about implications and scope, not claims that a general factor-enumeration algorithm cannot compute finite examples.

## Limitations

The theorem supplies \(2k-1\) explicit distinct minimal absent factors; it **does not prove** that the entire antidictionary contains exactly \(2k-1\) entries for every \(k\). Equality has been checked only for \(3\le k\le8\). The construction is specific to the binary morphism \(0\mapsto01\), \(1\mapsto00\), to its canonical fixed-point prefixes, and to contiguous factors rather than scattered subsequences. Literature-overlap searches cannot establish uniqueness of this result across all publications.

## References

1. A. J. Pinho, P. J. S. G. Ferreira, S. P. Garcia, and J. M. O. S. Rodrigues, “On finding minimal absent words,” *BMC Bioinformatics* 10 (2009), article 137, first published 2009-05-08, DOI: 10.1186/1471-2105-10-137.
2. C. Barton, A. Héliou, L. Mouchard, and S. P. Pissis, “Linear-time computation of minimal absent words using suffix array,” *BMC Bioinformatics* 15 (2014), article 388, DOI: 10.1186/s12859-014-0388-9.
3. J. D. Currie, “The Analog of Overlap-Freeness for the Period-Doubling Sequence,” *Journal of Integer Sequences* 26 (2023), article 23.8.2, arXiv:2303.14539; https://cs.uwaterloo.ca/journals/JIS/VOL26/Currie/currie16.pdf.

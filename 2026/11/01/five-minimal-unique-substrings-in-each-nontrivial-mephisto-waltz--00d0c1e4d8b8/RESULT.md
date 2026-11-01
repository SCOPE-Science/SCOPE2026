# Five minimal unique substrings in each nontrivial Mephisto–Waltz iterate

## Finding

Let \(\sigma\) be the binary morphism \(\sigma(0)=001\), \(\sigma(1)=110\), and let \(W_n=\sigma^n(0)\). All positions below are **zero-based**, with half-open factor intervals \([a,b)\). A *minimal unique substring* (MUS) is a factor occurring exactly once in its finite host word, for which deleting either its first or its last letter yields a factor occurring at least twice.

**Theorem.** For every integer \(n\geq2\), put \(m=3^{n-2}\). The entire MUS set of \(W_n\), as occurrence intervals, is
\[
\operatorname{MUS}(W_n)=\left\{[jm-1,(j+1)m+1):j\in\{2,3,5,6,7\}\right\}.
\]
In particular there are exactly five MUSs, all of length \(m+2\). These are *all* MUSs in the finite word, not just the shortest unique factors or the MUSs at selected block boundaries. For \(n=1\), the two MUS intervals are \([0,2)\) and \([2,3)\); that exceptional base case is not used in the main induction.

## Assumptions and scope

The alphabet is exactly \(\{0,1\}\); occurrences are contiguous and overlapping occurrences count separately. A factor \(W[a:b]\) comprises indices \(a,\ldots,b-1\). The morphism is iterated on the initial letter \(0\), not on arbitrary initial words. The claimed complete classification holds for all integer iterates \(n\ge2\), without a finite search cutoff.

## Proof

**1. Four-symbol synchronization.** Every image block has the form \(\sigma(c)=cc\bar c\), where \(\bar c=1-c\). For any binary word \(v\), four-symbol factors of \(\sigma(v)\) beginning in residues \(0,1,2\) modulo \(3\), respectively, have the following possible values:

\[
\begin{aligned}
\mathcal A_0&=\{0010,0011,1100,1101\},\\
\mathcal A_1&=\{0100,0111,1000,1011\},\\
\mathcal A_2&=\{0001,0110,1001,1110\}.
\end{aligned}
\]
These sets are pairwise disjoint. Indeed a four-symbol factor starts either at the beginning of \(\sigma(c)\), at its second symbol, or at its third symbol, and the next block begins with \(\sigma(d)=dd\bar d\). The three forms are \(cc\bar c d\), \(c\bar cdd\), and \(\bar cdd\bar d\). The listed disjointness follows from the four choices of \((c,d)\).

Consequently, any factor of \(\sigma(v)\) of length at least \(4\) can occur **only** at starting positions of one residue modulo \(3\), determined by its first four symbols.

**2. Exact occurrence transfer.** Take an interval \([i,j)\) in \(\sigma(v)\) of length at least \(4\). Let \(a=\lfloor i/3\rfloor\), \(b=\lfloor(j-1)/3\rfloor\), and write its covering parent factor as \(g=v[a:b+1]\). Among positions with the same starting residue, equality of the output factors is equivalent to equality of the corresponding covering parent factors: every sampled nonempty portion of \(\sigma(c)\) identifies \(c\), because \(\sigma(0)=001\) and \(\sigma(1)=110\) disagree at each of the three coordinates. Together with Step 1, this gives the exact identity
\[
\operatorname{occ}_{\sigma(v)}\bigl(\sigma(v)[i:j]\bigr)
=\operatorname{occ}_{v}(g).
\]
Here the occurrences on the right all yield valid corresponding output factors, including at the endpoints of \(v\). Thus uniqueness of a factor of length at least \(4\) is equivalent to uniqueness of its covering parent factor.

**3. MUS lifting.** Let \([a,b)\) be a MUS in \(v\) with length \(\ell=b-a\ge3\). Define its *boundary lift* in \(\sigma(v)\) by
\[
\Lambda([a,b))=[3a+2,3b-2).
\]
It consists of the last symbol of \(\sigma(v[a])\), the complete images of the intervening \(\ell-2\) letters, and the first symbol of \(\sigma(v[b-1])\); its length is \(3\ell-4\ge5\). By Step 2 it occurs exactly as often as the parent MUS, hence exactly once. Its proper suffix, obtained by dropping the first symbol, has covering parent factor \(v[a+1:b]\), which repeats by minimality of the parent MUS. Its proper prefix likewise has covering parent factor \(v[a:b-1]\), which repeats. Each repeated parent occurrence produces a corresponding repeated output factor at the same residue. Thus \(\Lambda([a,b))\) is a MUS.

Conversely, let \(F\) be any unique factor of \(\sigma(v)\) of length at least \(4\). By Step 2 its covering parent \(g\) is unique in \(v\). Every unique finite factor contains a minimal unique subfactor: shorten its interval while uniqueness remains, until no further shortening is possible. Suppose that subfactor is \(v[a:b]\) in the parent interval. Then the lifted interval \([3a+2,3b-2)\) lies inside the interval of \(F\): the start of \(F\) lies no later than the last symbol of its first covering block, and its end lies later than the first symbol of its last covering block. Therefore **every** unique output factor of length at least \(4\) contains a lifted parent MUS, provided the parent MUSs have length at least \(3\). Since a MUS cannot properly contain another unique factor, any output MUS of length at least \(4\) is precisely one of these lifts.

**4. The base case and exclusion of shorter output MUSs.** Directly, \(W_2=001001110\). Every factor of length \(1\) or \(2\) occurs at least twice. Its length-three factors occurring once are exactly the five factors starting at indices \(1,2,4,5,6\). The six length-four factors are `0010`, `0100`, `1001`, `0011`, `0111`, and `1110`; each contains one of those unique length-three factors. Thus the complete MUS set of \(W_2\) consists of the five intervals \([j-1,j+2)\) for \(j\in\{2,3,5,6,7\}\).

Moreover \(W_3=\sigma(W_2)\) contains **all eight** binary length-three factors at least twice: their multiplicities for `000`, `001`, `010`, `011`, `100`, `101`, `110`, `111` are respectively \(2,5,2,4,4,2,4,2\). Since the morphism fixes the first letter \(0\), its iterates are nested prefixes: \(W_3\) is a prefix of every \(W_n\) for \(n\ge3\). Thus no \(W_n\) with \(n\ge3\) has a unique factor of length at most \(3\).

**5. Induction and positions.** From Steps 3–4, for each \(n\ge2\) the complete MUS set of \(W_{n+1}\) is precisely the lift of the complete MUS set of \(W_n\). The mapping transforms \([jm-1,(j+1)m+1)\) into
\[
[3(jm-1)+2,\;3((j+1)m+1)-2)
=[j(3m)-1,(j+1)(3m)+1).
\]
The base case has \(m=1\), and each iteration multiplies \(m\) by \(3\). This proves the claimed interval classification for every \(n\ge2\). \(\square\)

## Verification

The complete standalone program `verify_mephisto.py` builds the words through \(n=8\) (length \(6561\)). It computes MUSs by suffix-array neighbor longest common prefixes and checks the exact five intervals for each iterate. Independently, for \(n\le5\) it enumerates all distinct factors and their occurrence counts and verifies the same intervals. For \(n=2,3,4\) it additionally checks the occurrence-transfer identity on every output interval of length at least \(4\), totaling \(3402\) comparisons. Run `python3 verify_mephisto.py`; expected output is in `verification_output.txt`. These finite checks corroborate, but are not substitutes for, the all-iterate proof above.

## Relationship to prior work

Kishi, Guo, Urbina, and Bannai introduced interference-free morphisms in their May 18, 2026 manuscript [1]. Their Corollary 16 identifies this exact morphism as strongly interference-free. Their principal structural results give sufficient conditions for preserving factor occurrence counts, and they give exact MUS descriptions for Fibonacci and Thue–Morse words, not for the Mephisto–Waltz iterates treated here. Their conclusion explicitly invites study of fixed points of strongly interference-free morphisms. The present finite-iterate MUS classification requires the separate four-symbol phase synchronization, boundary-lift equivalence, and base classification; it is not a restatement of their occurrence-preservation theorem.

The general MUS definitions, algorithms, and extremal bounds in [2] and [3] do not imply the positions and lengths in the displayed formula. Standard descriptions of the Mephisto–Waltz sequence [4,5] specify the morphism and other combinatorial features but do not supply an MUS classification. These comparisons are evidence about inspected work, not a guarantee that no independently discovered equivalent result exists.

## Limitations

The proof applies to the specified finite morphic iterates starting from \(0\), not arbitrary factors of the infinite fixed point or other three-uniform substitutions. It does not classify shortest-unique-substring queries for arbitrary text positions, nor minimal absent *subsequences*. No independent mathematical review or exhaustive publication-priority certification is claimed.

## References

1. K. Kishi, P. Guo, C. Urbina, and H. Bannai, *On Occurrence-Preserving Morphisms*, arXiv:2605.18034v1 (first public May 18, 2026), Sections 3–6. https://arxiv.org/html/2605.18034v1
2. H. Fujimaru, T. Mieno, and S. Inenaga, *On the number of MUSs crossing a position*, arXiv:2508.16092v1 (August 22, 2025). https://arxiv.org/html/2508.16092v1
3. T. Mieno et al., *Minimal Unique Substrings and Minimal Absent Words in a Sliding Window*, arXiv:1909.02804 (2019). https://arxiv.org/abs/1909.02804
4. *Mephisto Waltz Sequence*, Wolfram MathWorld. https://mathworld.wolfram.com/MephistoWaltzSequence.html
5. *OEIS A064990*, Mephisto Waltz sequence. https://oeis.org/A064990

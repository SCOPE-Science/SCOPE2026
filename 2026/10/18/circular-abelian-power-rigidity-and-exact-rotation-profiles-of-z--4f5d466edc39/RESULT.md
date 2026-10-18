# Circular Abelian-power rigidity and exact rotation profiles of Zimin words

## Finding

Let \(Z_1=1\), \(Z_{n+1}=Z_n(n+1)Z_n\), and \(N=|Z_n|=2^n-1\). Index positions from \(0\) to \(N-1\). A *circular Abelian square* with start \(i\) and half-length \(d\) consists of the \(2d\) cyclically consecutive letters beginning at \(i\), divided into two length-\(d\) blocks with the same Parikh vector. Require \(1\le 2d\le N\), so an occurrence never traverses a position twice.

**Theorem.** For every integer \(n\ge1\), the complete set of circular Abelian-square occurrences is
\[
\mathcal A(Z_n)=\{(N-d,d):1\le d\le (N-1)/2\}.
\]
Thus *each allowable half-length occurs at exactly one starting position*, centered on the cut between the last and first symbols. There are exactly \((N-1)/2=2^{n-1}-1\) such occurrences, and no circular Abelian cube, or any higher Abelian power, of total length at most \(N\).

For the linear cyclic rotation \(Z_n^{(c)}\) starting at original position \(c\), where \(0\le c<N\), the number of ordinary (nonwrapping) Abelian-square **occurrences** is precisely
\[
L_n(c)=\min\{c,N-c\}.
\]
Consequently the original \(Z_n\) is the unique Abelian-squarefree rotation. For every integer \(j\) with \(1\le j\le (N-1)/2\), exactly two rotations have \(j\) Abelian-square occurrences; no other counts occur. When \(n=1\), the occurrence set is empty and the sole rotation has count zero.

## Assumptions and scope

The alphabet is the labeled set \(\{1,\ldots,n\}\), with distinct symbols; their numeric labels do not undergo identification. A Parikh vector records the count of each symbol. The circle is the fixed word \(Z_n\) with positions indexed and a distinguished original cut, not a set of linear words under arbitrary symbol permutations. A circular occurrence is a pair \((i,d)\), not merely the distinct content of its factor; its total length is at most the circumference. A rotation is the linear word obtained from a specific cut position, and every occurrence counted in a rotation must fit inside that linear word. For \(n=1\), the empty square spectrum is included by convention.

## Proof

**Ruler description, palindrome, and linear absence.** For \(1\le j\le N\), the \(j\)-th (one-based) letter of \(Z_n\) equals \(1+\nu_2(j)\), where \(\nu_2\) is the valuation of an integer at the prime two. This follows directly by induction from the recursion. Because \(\nu_2(2^n-j)=\nu_2(j)\) for \(1\le j<2^n\), the word is a palindrome.

Every nonempty linear factor of the ruler sequence has a *unique largest symbol*. Indeed, if two positions attained its largest two-adic valuation \(a\), they would be distinct odd multiples of \(2^a\). Between them would occur an even multiple of \(2^a\), having strictly larger valuation. This contradicts maximality. An Abelian square would require the largest symbol to appear equally often in each half, which is impossible if it appears once in the entire factor. Hence \(Z_n\) is linearly Abelian-squarefree. This fact is classical, but the argument here is independent of an appeal to the literature.

**Existence of all claimed circular occurrences.** Let \(1\le d\le (N-1)/2\). The circular length-\(2d\) factor beginning at zero-based position \(N-d\) is the last \(d\) letters followed by the first \(d\) letters. Because \(Z_n\) is a palindrome, the suffix of length \(d\) is the reversal of the prefix of length \(d\). Those two blocks have identical Parikh vectors. Thus \((N-d,d)\in\mathcal A(Z_n)\).

**No other occurrences.** Any circular Abelian square must cross the original cut, since a noncrossing one would be a linear Abelian square. Suppose it crosses the cut off center. Reversal of the palindrome preserves Abelian squares and reflects the cut, so without loss of generality the cut lies strictly *inside the second half*. Write \(d=x+y\), with integers \(x,y\ge1\), where exactly \(x\) symbols of the second half lie before the cut and \(y\) symbols after it. Its start is then \(N-(d+x)\).

Let \(P(t)\) be the Parikh vector of the first \(t\) letters, with \(P(0)=0\). Palindromicity says that the last \(t\) letters also have Parikh vector \(P(t)\). The first length-\(d\) block has vector \(P(d+x)-P(x)\), while the second has vector \(P(x)+P(y)\). Equality implies
\[
P(y+2x)-P(y)=2P(x).
\]
The left side is the Parikh vector of a contiguous factor of \(Z_n\) of length \(2x\), at one-based positions \(y+1,\ldots,y+2x\); those indices are within \(1,\ldots,N\), because this factor describes a genuine occurrence. Put \(r=\lfloor\log_2 x\rfloor+1\). The entire prefix of length \(x\) uses only letters at most \(r\), since \(x<2^r\). But **every interval of \(2x\) consecutive integer indices contains a multiple of \(2^r\)**, since \(2^r\le2x\). Its ruler-sequence factor therefore contains a letter at least \(r+1\), contradicting the displayed Parikh-vector equality. This excludes every off-center crossing, proving the complete occurrence formula.

**Rotation profile.** For a fixed \(d\), the unique circular occurrence occupies positions from \(N-d\) through \(N-1\) and from \(0\) through \(d-1\). It becomes a nonwrapping factor after cutting at \(c\) exactly when \(d\le c\le N-d\). Therefore the number of admissible half-lengths is the number of integers \(d\) with \(1\le d\le\min\{c,N-c\}\), namely \(L_n(c)=\min\{c,N-c\}\). Since \(N\) is odd, the values are zero only for \(c=0\), while each positive integer up to \((N-1)/2\) occurs at exactly the two cuts \(c=j\) and \(c=N-j\).

**No Abelian powers beyond squares.** An Abelian cube consisting of three consecutive equal-length anagram blocks would induce two circular Abelian-square occurrences of the same half-length: one starting at its first block and one starting one block later. Their starts are distinct modulo \(N\), contradicting the uniqueness just proved. Every higher Abelian power contains such a cube, so none occurs within the permitted length range. \(\square\)

## Verification

The included standalone `verify.py` builds the words recursively, checks the ruler identity, enumerates every circular pair \((i,d)\) through order eight with **two different algorithms** (direct `Counter` comparison and Parikh-prefix arrays), and checks every rotation with a direct linear scan. It also searches all admissible circular Abelian cubes. The observed results are precisely the theorem's formulas, including the base case; they are finite checks, not the infinite proof.

For clarity about why the two-adic structure matters, there exist Abelian-squarefree palindromes for which centered circular squares are **not** unique. One explicit example is `012301021242120103210` (length 21): it has no linear Abelian squares, but circular Abelian squares of half-length seven start at positions \(11\), \(14\), and \(17\) (zero-based). The special prefix/ruler bound in the proof is therefore substantive, not a consequence of palindrome symmetry plus linear avoidance alone.

To reproduce: run `python3 verify.py` in the directory containing that file. It uses only the Python standard library and makes no downloads or network calls.

## Relationship to prior work

Cummings and Mays (2001, Section 2) recall the Zimin recursion and the classical maximal Abelian-squarefree property of *linear* Zimin words. Bullock (2004, introduction) uses the same construction to benchmark short maximal Abelian-squarefree words. Glen, Halldórsson, and Kitaev (2010, introduction) discuss Zimin words in the theory of crucial Abelian-power-free words. These treatments address linear avoidance and maximality, rather than the indexed circular occurrence spectrum, the exact tent-shaped distribution over rotations, or cyclic Abelian cubes.

Earlier work on *ordinary* circular squares of Zimin words counts exact tandem repeats, which is a strictly stronger condition on two blocks than Parikh-vector equality. Its classification of ordinary squares does not exclude additional Abelian squares. The present argument derives the Abelian restriction independently using a short-block-versus-prefix valuation obstruction; none of the claimed Abelian-square bounds is inferred merely from ordinary-square counts.

## Limitations

The result applies specifically to the finite, distinctly labeled, recursively defined Zimin words. It does not extend to arbitrary Abelian-squarefree palindromes, as the explicit counterexample shows. It counts occurrences with total length at most one complete circuit; longer traversals or an alternative convention counting nonprimitive winding powers are outside scope. The analysis is a same-model mathematical proof and reproducible finite check, not independent expert validation; priority over every unindexed source is not established.

## References

1. L. J. Cummings and M. Mays, *A One-Sided Zimin Construction*, Electronic Journal of Combinatorics **8** (2001), R27, DOI `10.37236/1571` (publicly published 2001-07-23). Full open-access article: `https://www.combinatorics.org/ojs/index.php/eljc/article/download/v8i1r27/pdf/`.
2. Evan M. Bullock, *Improved Bounds on the Length of Maximal Abelian Square-Free Words*, Electronic Journal of Combinatorics **11** (2004), R17, DOI `10.37236/1770`, open-access PDF: `https://www.combinatorics.org/ojs/index.php/eljc/article/download/v11i1r17/pdf/`.
3. Amy Glen, Bjarni V. Halldórsson, and Sergey Kitaev, *Crucial Abelian k-Power-Free Words*, Discrete Mathematics & Theoretical Computer Science **12** (2010), 83–96, DOI `10.46298/dmtcs.513`, open-access PDF: `https://dmtcs.episciences.org/513/pdf`.

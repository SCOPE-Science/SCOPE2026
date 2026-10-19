# Lacunary minimal absent factors of the regular paperfolding word

## Finding

Let \(f=f_0f_1\cdots\) be the regular binary paperfolding word, with zero-based indexing, defined by
\[
f_{2t}=t\bmod 2,\qquad f_{2t+1}=f_t\quad(t\ge 0).
\]
Equivalently, \(f_i=1\) precisely when the odd part of \(i+1\) is \(3\pmod 4\). A **minimal absent factor** is a finite binary word absent as a contiguous factor of \(f\), although all of its proper contiguous factors occur in \(f\). Let \(A_f(n)\) denote the number of distinct minimal absent factors of length \(n\).

**Theorem.** For every integer \(n\ge9\),
\[
 A_f(n)=\begin{cases}
 4,&n=2^j+1\text{ for some integer }j\ge3,\\
 0,&\text{otherwise}.
 \end{cases}
\]
Thus the long-word antidictionary has precisely four new members at lengths \(9,17,33,65,\ldots\), and no members at intervening lengths. In particular, for every integer \(N\ge9\),
\[
 \sum_{n=9}^{N}A_f(n)=4\bigl(\lfloor\log_2(N-1)\rfloor-2\bigr).
\]
The four length-nine words are `001100010`, `001110010`, `101100011`, and `101110011`.

## Assumptions and scope

The alphabet is exactly \(\{0,1\}\), factors are **contiguous**, and an occurrence may begin at any nonnegative index of the infinite one-sided word. Distinct absent words, not occurrences or symmetry classes, are counted. The theorem concerns every \(n\ge9\); it makes no assertion in the theorem about shorter lengths. The paperfolding normalization above fixes the sequence; complementing every bit gives a bijective equivalent version.

For a factor \(u\), define its left and right extension alphabets \(L(u),R(u)\subseteq\{0,1\}\) and its two-sided extension relation
\[
 E(u)=\{(a,b)\in\{0,1\}^2: aub\text{ is a factor of }f\}.
\]
Call \(u\) *bispecial* if \(|L(u)|=|R(u)|=2\). All finite factors recur arbitrarily late: for an occurrence in positions bounded by \(B\), choose \(2^h>B+1\) and shift the positive indices by \(2^{h+2}\). Their odd parts remain unchanged modulo four, so this produces a later occurrence.

## Proof

**1. A minimal absent word is a missing two-sided extension of a bispecial factor.** A binary word \(aub\) of length \(n\ge3\), with inner word \(u\) of length \(n-2\), is minimal absent exactly when \(a\in L(u)\), \(b\in R(u)\), but \((a,b)\notin E(u)\). Indeed, its length-\((n-1)\) prefix \(au\) and suffix \(ub\) then occur, implying all proper factors occur. If either extension alphabet is a singleton, every product pair appears: each occurrence of \(u\) has a left and right neighboring letter (using late recurrence), and the uniquely prescribed neighbor is present with every occurrence of the other neighbor. Consequently, missing pairs can occur only at bispecial factors, and
\[
 A_f(n)=\sum_{\substack{|u|=n-2\\u\text{ bispecial}}}\bigl(4-|E(u)|\bigr).
\]

**2. Every long factor has a unique occurrence parity.** The binary words `0101` and `1010` do not occur in \(f\). At any starting position, one of the two parity tracks of a length-four window is made of consecutive even-indexed symbols, which are opposite by \(f_{2t}=t\bmod2\), whereas in either alternating word those two symbols would be equal. Suppose a factor \(u\) of length at least eight occurs starting at both an even and an odd index. At either occurrence, one local parity track consists of four or more consecutive symbols of \(f\) and must therefore be nonalternating; at the other occurrence that same local parity track consists of even-indexed symbols of \(f\) and is strictly alternating. This contradiction proves uniqueness.

**3. Restrictions on bispecial lengths.** An odd-start factor has a uniquely determined preceding bit: it is the complement of its bit at local position one. Thus no such factor of length at least eight is left-special. An even-start factor of even length has a uniquely determined succeeding bit: the complement of its last locally even-positioned bit. Thus no such factor is right-special. By Step 2, every bispecial factor of length at least eight has odd length and occurs only at even indices.

**4. A degree-preserving dyadic lifting.** For \(m\ge8\), consider a factor \(v\) of length \(m\) occurring at \(t\ge1\). Form \(\Phi_m(v)\) as the length-\((2m+1)\) block starting at \(2t\): its odd local coordinates are the \(m\) symbols of \(v\); its even local coordinates alternate, beginning with \(t\bmod2\). Step 2 applied to \(v\) shows that \(t\bmod2\) is uniquely determined by \(v\), so this definition does not depend on the selected occurrence. Conversely, every even-start factor of length \(2m+1\) arises in this manner, and \(\Phi_m\) is injective because \(v\) is recovered from its odd local coordinates.

At the displayed occurrence, the immediately preceding and succeeding bits satisfy
\[
 f_{2t-1}=f_{t-1},\qquad f_{2t+2m+1}=f_{t+m}.
\]
Hence the full two-sided extension relation and both one-sided extension alphabets of \(\Phi_m(v)\) are **identical** to those of \(v\). The late-recurrence argument permits all choices of left and right extensions with \(t\ge1\). Every bispecial word of length \(2m+1\) occurs at even positions by Step 3, hence arises from a unique bispecial \(v\) of length \(m\). Thus for \(m\ge8\), the map \(\Phi_m\) is a bijection on bispecial factors, preserving \(|E(u)|\).

**5. An exact finite base.** Allouche proved \(|F_f(r)|=4r\) for every \(r\ge7\), where \(F_f(r)\) is the set of length-\(r\) factors [1]. Generate the first \(256\) symbols using the defining recurrence, and for each \(7\le r\le18\) enumerate its distinct length-\(r\) factors. There are exactly \(4r\) in every case; Allouche's theorem proves that these are the **complete infinite factor sets**, not merely observations in a finite prefix. Determine all one-sided and two-sided extension relations for inner lengths \(7\le r\le16\) by memberships in the complete sets of lengths \(r+1\) and \(r+2\). The resulting exact table is:

| Inner factor length | Bispecial factors | Two-sided extension relation |
| --- | --- | --- |
| \(7\) | `0010011`, `0011011` | all four pairs for each |
| \(7\) | `0110001`, `0111001` | only \((0,1),(1,0)\) for each |
| \(8,\ldots,14\) | none | — |
| \(15\) | `001001100011011`, `001001110011011` | all four pairs for each |
| \(15\) | `001101100010011`, `001101110010011` | only \((0,1),(1,0)\) for each |
| \(16\) | none | — |

The standalone verifier independently reconstructs the finite table; it needs no unrecorded input data.

**6. Induction and count.** For inner lengths \(r\ge17\), Steps 3–4 either rule out bispecial factors (when \(r\) is even) or reduce their complete extension profiles to those at \((r-1)/2\) (when \(r\) is odd). Together with the base table, it follows inductively that the only bispecial lengths \(r\ge7\) are \(r=2^j-1\), for integers \(j\ge3\). At each such length there are four bispecial factors, two with four extension pairs and two with only the opposite-letter pairs. Therefore the sum in Step 1 is four precisely when \(n-2=2^j-1\), and zero otherwise. This proves the theorem and its cumulative-count corollary.

## Verification

The self-contained `verify_paperfolding_maw.py` implements two independent definitions of \(f\), checks agreement for \(2048\) symbols, and extracts complete factor sets for lengths \(7\) through \(130\). Their observed sizes equal the **published proven** values \(4r\), which therefore independently certify completeness of these finite sets. The script checks the entire small bispecial table, direct minimal-absent counts for lengths \(9\) to \(128\), and preservation of one- and two-sided extension relations under the dyadic lifting for \(8\le m\le63\). It also checks explicit length-nine and length-seventeen absent words. Run `python3 verify_paperfolding_maw.py`; the output begins `VERIFY_OK` only if all assertions succeed. These finite checks do not replace the all-length induction or reprove Allouche's factor-complexity theorem.

## Relationship to prior work

Allouche [1] establishes exact ordinary factor complexity; the factor-size theorem is used here to certify the finite base. Allouche and Bousquet-Mélou [2] study canonical positions and recurrence of paperfolding factors; their published abstract does not assert the present minimal-absent length spectrum, but their complete text could not be assessed. Cassaigne, Fici, Sciortino, and Zamboni [3] analyze cyclic factor complexity of paperfolding and introduce minimal-forbidden complexity as a related but distinct statistic; their inspected treatment does not give this exact spectrum. The novelty claim is **only** the all-length minimal-absent enumeration and bispecial-extension lifting, not classical factor complexity or parity synchronization.

## Limitations

The result concerns the one specific regular paperfolding normalization and contiguous factors, not arbitrary instruction-folding sequences, finite prefixes, or absent scattered subsequences. The proof relies on Allouche's published factor-complexity theorem for exhaustive verification of the small base; the supporting checker independently reconstructs that base but does not itself prove factor-complexity for arbitrary lengths. A potentially relevant 1994 canonical-position paper was accessible only through its abstract, leaving a residual originality risk; no general priority or independence certification is claimed. The day-verified literature anchor [3] was publicly submitted on 2014-02-24, while [1] and [2] are older print works with no verified first-public online-release date.

## References

1. J.-P. Allouche, *The number of factors in a paperfolding sequence*, Bulletin of the Australian Mathematical Society **46** (1992), 23–32. DOI: 10.1017/S0004972700011655. Full paper inspected.
2. J.-P. Allouche and M. Bousquet-Mélou, *Canonical positions for the factors in paperfolding sequences*, Theoretical Computer Science **129** (1994), 263–278. DOI: 10.1016/0304-3975(94)90028-0. Abstract inspected; full text not obtained.
3. J. Cassaigne, G. Fici, M. Sciortino, L. Q. Zamboni, *Cyclic Complexity of Words*, arXiv:1402.5843, first public version 2014-02-24, MSC 68R15. Accessible manuscript inspected, especially its paperfolding discussion.

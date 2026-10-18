# Initial non-repetitive complexity of the regular paperfolding word

## Finding

Let \(f=f_0f_1\cdots\) be the zero-indexed binary word defined by \(f_i=1\) exactly when the odd part of \(i+1\) is congruent to \(3\) modulo \(4\). This is a bit-complement of one common convention for the regular paperfolding word; complementing every letter does not change equality of factors.

For each integer \(n\ge1\), let \(R(n)\) be the smallest \(r\ge1\) for which there is a \(q<r\) with
\[
 f_rf_{r+1}\cdots f_{r+n-1}=f_qf_{q+1}\cdots f_{q+n-1}.
\]
Equivalently, the length-\(n\) factors beginning at positions \(0,1,\ldots,R(n)-1\) are pairwise distinct, and the next one repeats. For all \(n\ge8\), with \(k=\lfloor\log_2 n\rfloor\),
\[
\boxed{R(n)=3\cdot2^k.}
\]
In fact, at the first repeated occurrence, the unique earlier matching starting index is \(q=2^k\). At the seven shorter lengths the complete \((n,R(n),q)\) table is
\[
 (1,1,0),\ (2,3,0),\ (3,3,0),\ (4,8,3),\ (5,8,3),\ (6,12,4),\ (7,12,4).
\]
In particular,
\[
 \liminf_{n\to\infty}\frac{R(n)}n=\frac32,
 \qquad
 \limsup_{n\to\infty}\frac{R(n)}n=3.
\]
Combining this with the established ordinary factor complexity \(p_f(n)=4n\) for \(n\ge7\), the fraction of distinct length-\(n\) factors encountered before the first repetition has lower and upper limit \(3/8\) and \(3/4\), respectively.

## Assumptions and scope

All starting indices are nonnegative and all factors are contiguous. Equality means exact equality of binary words, not equality under rotations or an abelian equivalence. The integer \(k\) in the main formula is the unique integer with \(2^k\le n<2^{k+1}\). The statement concerns the one-sided regular paperfolding word with all folding instructions equal; no corresponding formula is asserted for arbitrary generalized paperfolding instructions.

The digit definition is equivalent to the recurrences
\[
 f_{2j}=j\bmod2,\qquad f_{2j+1}=f_j\qquad(j\ge0),
\]
with \(f_0=0\). Thus its prefix begins `00100110001101100010011100110110`.

## Proof

**1. Alternating obstruction and parity recognition.** An alternating binary word of length four has identical first and third letters and identical second and fourth letters. No factor of \(f\) of length four is alternating: when its first position is even, its first and third letters are successive terms of \((f_{2j})_{j\ge0}\) and are different; when its first position is odd, its second and fourth letters are successive such terms and are different.

Fix \(n\ge8\). A factor starting at \(2i\) has alternating letters at offsets \(0,2,4,\ldots\), whereas its letters at offsets \(1,3,5,\ldots\) form a contiguous factor of \(f\), which cannot have an alternating four-letter segment. A factor starting at \(2i+1\) has the opposite property: its even-offset letters form a nonalternating factor of \(f\), and its odd-offset letters alternate. Both offset subsequences have at least four letters. Therefore no length-\(n\) factor starting at an even position equals one starting at an odd position.

The same conclusion applied to factors of length \(m\ge8\) gives a useful strengthening: if two length-\(m\) factors starting at \(i\) and \(j\) are equal, then \(i\equiv j\pmod2\).

**2. Exact decimation.** For \(n\ge16\), write \(a=\lfloor n/2\rfloor\) and \(b=\lceil n/2\rceil\), so both are at least eight. By the defining recurrences, a factor of length \(n\) starting at \(2i\) is interleaved from the alternating letters \(i\bmod2,(i+1)\bmod2,\ldots\) and the length-\(a\) factor \(f_i\cdots f_{i+a-1}\). Hence, for all \(i,j\ge0\),
\[
 f_{2i}\cdots f_{2i+n-1}=f_{2j}\cdots f_{2j+n-1}
 \quad\Longleftrightarrow\quad
 f_i\cdots f_{i+a-1}=f_j\cdots f_{j+a-1}.
\]
The reverse implication uses the same-start-parity conclusion of Step 1 for length \(a\), which ensures the alternating letters have the same phase.

Similarly, a factor starting at \(2i+1\) interleaves the length-\(b\) factor beginning at \(i\) with alternating letters. For all \(i,j\ge0\),
\[
 f_{2i+1}\cdots f_{2i+n}=f_{2j+1}\cdots f_{2j+n}
 \quad\Longleftrightarrow\quad
 f_i\cdots f_{i+b-1}=f_j\cdots f_{j+b-1}.
\]
The absence of mixed-parity collisions then yields an exact recurrence for the first repetition position: a collision among even starting indices first occurs at \(2R(a)\), and one among odd starting indices first occurs at \(2R(b)+1\). Since \(R\) is nondecreasing—two distinct length-\(a\) factors remain distinct when extended to length \(b\ge a\)—we have
\[
 R(n)=\min\{2R(a),2R(b)+1\}=2R(\lfloor n/2\rfloor),\qquad n\ge16.
\]
Furthermore, if the first repeated factor of length \(a\) has unique earlier matching index \(Q(a)\), then the first repeated factor of length \(n\) has unique earlier matching index \(Q(n)=2Q(a)\). Uniqueness follows because all earlier factors of length \(a\) are distinct.

**3. Finite base with a complete certificate.** The following are the length-eight factors starting at positions \(0\) through \(23\), in that order:

```
 0 00100110    1 01001100    2 10011000    3 00110001
 4 01100011    5 11000110    6 10001101    7 00011011
 8 00110110    9 01101100   10 11011000   11 10110001
12 01100010   13 11000100   14 10001001   15 00010011
16 00100111   17 01001110   18 10011100   19 00111001
20 01110011   21 11100110   22 11001101   23 10011011
```

These twenty-four words are pairwise distinct. On the other hand, the length-fifteen factors starting at positions \(8\) and \(24\) both equal `001101100010011`. Thus for **every** \(8\le n\le15\), \(R(n)=24\) and the unique earlier match at position \(24\) begins at \(8\). The seven shorter cases in the finding follow by the same direct factor comparison using the displayed digit recurrence; the certificate program reproduces every one of these finite checks.

**4. Induction.** Let \(n\ge16\) and let \(k=\lfloor\log_2 n\rfloor\). Then \(\lfloor n/2\rfloor\) lies in \([2^{k-1},2^k)\). Starting from Step 3, Step 2 and induction give
\[
 R(n)=2R(\lfloor n/2\rfloor)=2\cdot3\cdot2^{k-1}=3\cdot2^k,
\qquad Q(n)=2Q(\lfloor n/2\rfloor)=2^k.
\]
This proves the theorem for all positive \(n\).

**5. Limits.** On each interval \(2^k\le n<2^{k+1}\), \(R(n)/n=3\cdot2^k/n\), with maximum exactly \(3\) and minimum tending to \(3/2\) as \(k\to\infty\). Allouche's established factor count \(p_f(n)=4n\) for \(n\ge7\) gives the two stated limits for \(R(n)/p_f(n)\).

## Verification

Execute `python3 verify.py` in the same directory as this document. The checker implements the paperfolding word twice (odd-part digit arithmetic and the decimation recurrence), and checks their agreement on the first 25,000 indices. It computes first factor collisions with exact integer encodings of whole binary factors, not approximate fingerprints or random hashing. It verifies all positive lengths through \(320\) and seventeen additional dyadic-boundary and transition lengths, including \(8191\). The recorded output is `VERIFY_OK lengths_checked 337 max_n 8191 prefix_bits 25000`.

The finite checker is a regression certificate only; Steps 1–4 constitute the proof for arbitrarily large \(n\).

## Relationship to prior work

Nicholson and Rampersad introduced systematic study of initial non-repetitive complexity and computed it for Thue–Morse, Fibonacci, and Tribonacci words. Their paper does not include the regular paperfolding word. Allouche determined the **ordinary** factor complexity of paperfolding sequences, and Allouche with Bousquet-Mélou studied canonical positions containing representatives of all factors. Burns later computed the **appearance** function, namely the first prefix covering every factor; that endpoint does not determine the *first duplicate* in the initial factor scan. None of those results, as inspected, supplies this full first-collision law or the matching-position classification. The 1994 canonical-positions article was available only at abstract level during this review, so this comparison has a residual literature-access risk.

## Limitations

Only the regular paperfolding sequence (or its global bit complement) is covered. The result counts the first repeated contiguous factor, not every factor's first occurrence, and it does not provide a full distribution of return times.

## References

1. J. Nicholson and N. Rampersad, *Initial non-repetitive complexity of infinite words*, first arXiv version 29 July 2015, arXiv:1507.08206, https://arxiv.org/abs/1507.08206.
2. J.-P. Allouche, *The number of factors in a paperfolding sequence*, Bulletin of the Australian Mathematical Society **46** (1992), 23–32, https://doi.org/10.1017/S0004972700011655.
3. J.-P. Allouche and M. Bousquet-Mélou, *Canonical positions for the factors in paperfolding sequences*, Theoretical Computer Science **129** (1994), 263–278, https://doi.org/10.1016/0304-3975(94)90028-0.
4. R. Burns, *The appearance function for paper-folding words*, arXiv:2210.14719, https://arxiv.org/abs/2210.14719.
5. OEIS A337120, ordinary factor complexity of the regular paperfolding sequence, https://oeis.org/A337120.

# Exact initial non-repetitive complexity of the Rudin–Shapiro word

## Finding
Let \(r=r_0r_1\cdots\) be the zero-indexed binary Rudin–Shapiro word: \(r_j\) is the parity of the number of overlapping occurrences of `11` in the canonical base-two expansion of \(j\), and \(r_0=0\). For each integer \(n\ge1\), let \(I_r(n)\) be the number of pairwise distinct length-\(n\) factors encountered from the origin before the first repeated length-\(n\) factor. Equivalently, it is the least integer \(j\ge1\) for which there exists \(0\le i<j\) with \(r[i,i+n)=r[j,j+n)\).

**Theorem.** For every positive integer \(n\),
\[
I_r(n)=\begin{cases}
1,&n=1,2,\\
4,&n=3,4,5,\\
4\cdot 2^{\lfloor\log_2(n-1)\rfloor},&n\ge6.
\end{cases}
\]
At the first collision, the earlier starting position is uniquely \(0\) whenever \(n\ge6\). In addition,
\[
\liminf_{n\to\infty}\frac{I_r(n)}n=2,
\qquad
\limsup_{n\to\infty}\frac{I_r(n)}n=4.
\]

## Assumptions and scope
Indices are nonnegative and factors \(r[i,i+n)\) use a half-open interval. A repeated factor means exact letterwise equality, not abelian equivalence or cyclic conjugacy. No assumption is made on the location of the earlier occurrence. The theorem concerns the one-sided binary Rudin–Shapiro word with the zero symbol assigned to even adjacent-`11` count; the complementary coding has identical complexity. All stated classifications range over infinitely many positive lengths.

## Proof
**1. A four-letter lift and its synchronization.** Define the length-two substitution \(\sigma\) on \(\{0,1,2,3\}\) by
\[
\sigma(0)=01,\quad \sigma(1)=02,\quad
\sigma(2)=31,\quad \sigma(3)=32.
\]
Let \(s=\sigma^\omega(0)\) and code \(0,1\) as binary \(0\) and \(2,3\) as binary \(1\). The result is \(r\). Indeed the elementary adjacent-`11` parity identities are
\[
r_{2j}=r_j,\qquad r_{2j+1}=r_j\mathbin{\mathrm{xor}}(j\bmod2).
\]
The letters of \(s\) encode the pair \((r_j,j\bmod2)\): at even indices one has \(0\) or \(3\), and at odd indices one has \(1\) or \(2\). Checking the four possible pairs against \(\sigma\) verifies the coding identity by induction, starting with \(s_0=0\).

The complete adjacent-pair language of \(s\) is
\[
\mathcal P=\{01,02,10,13,20,23,31,32\}.
\]
For exhaustiveness, begin with `01` in \(\sigma(0)\), then repeatedly include every adjacent pair inside \(\sigma(a)\sigma(b)\) for any currently included pair `ab`. The closure stabilizes at precisely the eight displayed pairs; hence it contains every adjacent pair of the infinite fixed point (and each member is attained at a finite substitution stage).

For each `ab` in \(\mathcal P\), code \(\sigma^3(a)\sigma^3(b)\) into binary and extract its eight windows of length eight beginning at offsets \(0,\ldots,7\). The complete sets from even offsets and odd offsets have cardinalities \(24\) and \(32\), respectively, and empty intersection. Thus **equal length-eight binary factors can only begin at positions of the same parity**. This is a genuinely exhaustive finite check: any length-eight factor starts at one of these offsets inside two consecutive length-eight substitution images. The complete enumeration is reproduced by `verify.py`.

A second synchronization observation concerns the four-letter word. If equal factors of \(s\) have length at least \(2^h-1\), their starting positions are congruent modulo \(2^h\), for every integer \(h\ge1\). At \(h=1\), every even position has a letter in \(\{0,3\}\), whereas every odd position has one in \(\{1,2\}\). For induction, equal factors of length at least \(2^{h+1}-1\) already start at equal parity. Removing at most one letter at each end leaves at least \(2^h-1\) complete aligned images of individual source letters, independently of the starting parity. All four words \(\sigma(a)\) are distinct, so equality of the images yields equality of the corresponding source factors. The induction hypothesis makes their source starting indices congruent modulo \(2^h\), and the original indices are therefore congruent modulo \(2^{h+1}\).

Consequently, for every power of two \(B\ge8\), equal binary factors of length \(B+1\) must begin at indices congruent modulo \(B\). They have length at least eight and thus equal starting parity; the four-letter lift can then be recovered letter by letter, and the preceding congruence lemma applies with \(B=2^h\).

**2. Dyadic blocks.** Fix a power of two \(B=2^h\ge8\), put \(A=r[0,B)\), and let \(H\) denote the binary word of length \(B\) consisting of \(B/2\) zeros followed by \(B/2\) ones. The adjacent-`11` definition implies
\[
r[B+t]=r_t\mathbin{\mathrm{xor}}H_t\quad(0\le t<B).
\]
Write \(C=A\mathbin{\mathrm{xor}}H\) and let \(\overline C\) denote its bitwise complement. The first five aligned length-\(B\) blocks of \(r\) are exactly
\[
A\;C\;A\;\overline C\;A.
\]
In fact the first \(2B\) symbols repeat at position \(4B\): for \(0\le t<2B\), the new bit at place \(2^{h+2}=4B\) has no adjacent set bit below it, giving \(r_{4B+t}=r_t\).

**3. No earlier duplicate of length \(B+1\).** Suppose two such factors start at indices strictly below \(4B\). Synchronization from Step 1 requires the indices to have the same residue \(t\), \(0\le t<B\), modulo \(B\). If the indices lie in different length-\(B\) blocks, the relevant factor is the length-\(B+1\) window of the concatenation of one of the following adjacent block pairs:
\[
(A,C),\quad(C,A),\quad(A,\overline C),\quad(\overline C,A).
\]
For each fixed offset \(t\), their corresponding windows are pairwise distinct:

- Comparing the first and third pairs, their source blocks are both \(A\), but their successor blocks \(C\) and \(\overline C\) are complementary. Every window extends into the successor.
- Comparing the second and fourth pairs, source blocks \(C\) and \(\overline C\) are complementary, so they differ before the boundary.
- A source \(A\) versus a source \(C\) always differs in the last half of its source block, which every suffix starting at \(t<B\) meets.
- A source \(A\) versus a source \(\overline C\) differs in the first half of its source block. If \(t<B/2\), the source suffix detects this. If \(t\ge B/2\), the successors differ somewhere among their first \(t+1\) symbols: \(C\) versus \(A\) differs at offset \(B/2\), and \(\overline C\) versus \(A\) differs at offset zero.

These comparisons cover all six unordered pairs of distinct source blocks \(0,1,2,3\). There cannot be equal windows at different offsets, by the residue lemma. Thus the factors starting at \(0,1,\ldots,4B-1\) are all pairwise distinct. On the other hand, the factor starting at \(4B\) repeats the factor at zero for every length up to \(2B\), by Step 2. Therefore
\[
I_r(n)=4B\qquad(B+1\le n\le2B,\quad B\ge8).
\]
The repeating predecessor at \(4B\) is uniquely index zero because all preceding length-\(n\) factors are distinct.

**4. Initial lengths and asymptotics.** Direct evaluation of the first few symbols gives the complete initial table
\[
\begin{array}{c|cccccccc}
n&1&2&3&4&5&6&7&8\\\hline
I_r(n)&1&1&4&4&4&16&16&16\\
\text{first earlier index}&0&0&1&1&1&0&0&0.
\end{array}
\]
These finite cases, recomputed by the bundled verifier, close the range not covered by Step 3. Since every \(n\ge9\) belongs to a unique interval \(B+1\le n\le2B\) for some power of two \(B\ge8\), the displayed formula follows. On these intervals \(I_r(n)/n=4B/n\). Taking the sequence \(n=2B\) gives limit \(2\); taking \(n=B+1\) gives limit \(4\). Every intermediate ratio lies between those endpoints, proving the two extremal limits.

## Verification
Run `python3 verify.py` in a directory containing the standalone checker. It uses only the Python standard library. It verifies the four-letter and arithmetic definitions on \(65{,}536\) symbols, reconstructs the complete eight-pair language and length-eight parity certificate, checks the five-block decomposition and uniqueness of the first \(4B\) factors for powers of two \(B=8,16,\ldots,1024\), and directly computes each first collision and unique predecessor for lengths \(1\) through \(384\). These are reproducibility checks; the unrestricted quantifiers are proved above rather than inferred from finite runs.

## Relationship to prior work
Nicholson and Rampersad introduced explicit formulas for initial non-repetitive complexity of the Thue–Morse, Fibonacci and Tribonacci words; their Theorems 6, 10 and 16 concern those different words. For example, their Thue–Morse formula has a different plateau coefficient and is proved using that word's factor structure. The present result supplies the corresponding complete formula for the binary Rudin–Shapiro word, using a separate parity-recognizability certificate and five-block comparison. Sun and Winterhof investigated maximum order complexity of Rudin–Shapiro, which detects repeated contexts with incompatible following symbols; that quantity is not initial non-repetitive complexity and its stated formulas do not determine the first occurrence of an arbitrary repeated factor. The standard Rudin–Shapiro digit recurrence and its four-letter presentation are existing tools and are not claimed as new.

## Limitations
The result treats origin-anchored factors, not factors read from an arbitrary starting point. It determines the first collision and its predecessor but not the full return-time distribution or the complete multiplicity of later repeats. Mathematical priority cannot be certified solely from literature searching; a differently indexed prior derivation remains possible. 

## References
1. J. Nicholson and N. Rampersad, *Initial non-repetitive complexity of infinite words*, arXiv:1507.08206 (first public version July 29, 2015), especially Theorems 6, 10 and 16. https://arxiv.org/pdf/1507.08206
2. J.-P. Allouche and J. Shallit, *Automatic Sequences: Theory, Applications, Generalizations*, Cambridge University Press, 2003, discussion of the Rudin–Shapiro word.
3. Z. Sun and A. Winterhof, *On the maximum order complexity of the Thue–Morse and Rudin–Shapiro sequence*, arXiv:1910.13723 (2019), DOI: 10.2478/udt-2019-0012. https://arxiv.org/abs/1910.13723

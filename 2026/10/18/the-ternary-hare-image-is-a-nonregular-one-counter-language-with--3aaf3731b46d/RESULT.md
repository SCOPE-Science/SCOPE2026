# The ternary hare image is a nonregular one-counter language with exact fibers

## Finding
Let \(H\) denote the Defant–Kravitz hare stack-sorting operator over the ordered alphabet \(\{0,1,2\}\). For a binary word \(v\), write \(d(v)\) for its number of adjacent occurrences of \(10\). The complete image of the hare operator is
\[
\operatorname{Im}(H)=\bigl\{v2^k:v\in\{0,1\}^*,\ k\ge d(v)\bigr\}.
\]
This language is deterministic one-counter and is not regular. Moreover, for every \(v2^k\) in the image, its complete preimage multiplicity is
\[
\left|H^{-1}(v2^k)\right|=\sum_{\substack{v=v_0v_1\cdots v_k\\v_i\in0^*1^*}}\prod_{i=0}^{k}\binom{|v_i|}{|v_i|_0},
\]
where the sum is over ordered factorizations allowing empty pieces and \(|v_i|_0\) is the number of zeros in piece \(v_i\). The value is zero for outputs outside the described image.

Writing \(a_n\) for the number of distinct length-\(n\) outputs (equivalently, hare-equivalence classes of ternary inputs), we have the exact expressions
\[
 a_n=\sum_{k=0}^{n}\sum_{d=0}^{\min\{k,\lfloor(n-k)/2\rfloor\}}\binom{n-k+1}{2d+1},\qquad
 \sum_{n\ge0}a_nz^n=\frac1{(1-z)(1-2z+z^2-z^3)}.
\]
Thus \((a_0,a_1,\ldots)=(1,3,6,11,20,36,64,113,199,350,615,\ldots)\) and, for \(n\ge4\),
\[
 a_n=3a_{n-1}-3a_{n-2}+2a_{n-3}-a_{n-4}.
\]
In particular \(a_n\sim c\lambda^n\), where \(\lambda\approx1.754877666246693\) is the largest positive real root of \(\lambda^3-2\lambda^2+\lambda-1=0\), \(r=\lambda^{-1}\), and \(c=1/[r(1-r)(2-2r+3r^2)]\approx2.223851198222568\). Hence the proportion of length-\(n\) ternary inputs represented by distinct images decays exponentially.

## Assumptions and scope
The alphabet is the fixed totally ordered three-letter alphabet \(0<1<2\), not an alphabet of variable size. All words are finite; the empty word is included. The map preserves word length and content. The hare operator is defined recursively by \(H(\varepsilon)=\varepsilon\), and, when the greatest letter \(m\) of a nonempty word occurs \(k\ge1\) times with \(w=A_0mA_1m\cdots mA_k\), by
\[
 H(w)=H(A_0)H(A_1)\cdots H(A_k)m^k.
\]
All \(A_i\) contain letters smaller than \(m\), and may be empty. This is the map defined in Defant and Kravitz (2020, Definition 1.1), with letters shifted to zero-based notation. Each preimage is a ternary word of the same length as its output.

## Proof
**Binary restriction.** For \(u\in\{0,1\}^*\), the maximum-letter recursion, with all interleaving pieces strings of zeros, gives \(H(u)=0^{|u|_0}1^{|u|_1}\). Thus every binary hare output has the form \(0^a1^b\), and precisely \(\binom{a+b}{a}\) binary inputs map to it.

**Exact image.** If a ternary input contains \(k\) copies of \(2\), write it uniquely as \(A_0 2 A_1 2\cdots 2 A_k\). Its output is \(v2^k\), where \(v=H(A_0)\cdots H(A_k)\) is a concatenation of \(k+1\) nondecreasing binary pieces. A descent \(10\) can occur only between two consecutive pieces; therefore \(d(v)\le k\). Conversely, split any binary \(v\) at every adjacent \(10\). This gives exactly \(d(v)+1\) nondecreasing pieces. For \(k\ge d(v)\), add \(k-d(v)\) empty pieces, interleave \(k\) copies of \(2\), and apply the recursion. Because each nondecreasing piece is fixed by binary hare, the output is \(v2^k\). This proves the image equality, including \(v=\varepsilon\) and \(k=0\).

**Complete fibers.** A fixed output \(v2^k\) has a preimage precisely when there is a decomposition \(v=v_0\cdots v_k\) with each piece nondecreasing; the pieces are forced as the images of the \(k+1\) uniquely determined segments cut by the \(2\)'s in the input. For a particular decomposition the segment choices are independent, and a segment with \(a\) zeros and \(b\) ones has exactly \(\binom{a+b}{a}\) preimages under binary hare. Distinct decompositions give different input placements of the \(2\)'s. Multiplying and summing yields the stated exact fiber formula without overcounting.

**Language boundary.** A deterministic one-counter recognizer scans the binary prefix of the input, increments its counter at each occurrence of adjacent \(10\), then reads the final block of \(2\)'s while decrementing until zero; surplus \(2\)'s are allowed and binary symbols after a \(2\) are forbidden. The last binary symbol requires only finite-state memory, so the language is deterministic one-counter. To prove nonregularity, intersect with the regular language \((10)^*2^*\). The resulting language is \(\{(10)^j2^k:k\ge j\}\). The prefixes \((10)^j\) are pairwise Myhill–Nerode inequivalent: if \(i<j\), the suffix \(2^i\) is accepted after \((10)^i\) but not after \((10)^j\). Thus even this intersection, hence the original image language, is not regular.

**Enumeration and growth.** A binary word with exactly \(d\) descents has the unique decomposition \(0^{a_0}1^{b_0}\cdots0^{a_d}1^{b_d}\), with \(a_i\ge1\) for \(1\le i\le d\), \(b_i\ge1\) for \(0\le i<d\), and all other exponents nonnegative. Its length generating series is \(z^{2d}/(1-z)^{2d+2}\), giving \(\binom{L+1}{2d+1}\) such words of length \(L\). For each, the number of terminal \(2\)'s can be any \(k\ge d\). Summation over \(d\) gives
\[
\sum_{d\ge0}\frac{z^{2d}}{(1-z)^{2d+2}}\frac{z^d}{1-z}
=\frac{1}{(1-z)^3}\frac1{1-z^3/(1-z)^2}
=\frac1{(1-z)((1-z)^2-z^3)}.
\]
Coefficient extraction proves the formula, initial terms, and recurrence. The cubic denominator \(1-2z+z^2-z^3\) has a unique root of smallest modulus \(r\approx0.569840290998053\) (its reciprocal is the unique positive root of \(\lambda(\lambda-1)^2=1\)); the other two roots have larger modulus since their reciprocal roots form a conjugate pair of modulus \(\lambda^{-1/2}<\lambda\). The simple pole at \(r\) contributes \(c\lambda^n\) with the displayed \(c\). The pole at \(1\) and the other cubic roots contribute only lower-order terms.

## Verification
The included standalone `checker.py` implements the defining recursive hare map, enumerates all \(3^n\) inputs for \(0\le n\le10\), and independently compares every output word's predicted image membership and complete fiber multiplicity with actual counts. It checks 88,573 ternary candidate output words in total, as well as the sum of all fibers and the rational generating-function recurrence. The recorded execution output appears in `computation.txt`; both files are included alongside this report. The inductive decomposition above, not the finite tests, establishes the infinite theorem.

## Relationship to prior work
Defant and Kravitz (2020) define the hare map, develop general fertility tools, and study sorting to the nondecreasing word. Campbell and Rampersad (2026) study hare/tortoise equivalence as a complexity notion for factors of specific infinite binary words, including Thue–Morse and paperfolding. Neither inspected material reports an explicit complete image language with nonregularity and full fibers for **all** ternary inputs of each length; full text of the 2026 manuscript was unavailable, so its coverage is not excluded by full-document inspection. The numerical sequence and its rational generating function are already present as OEIS A077855 under other interpretations: **only the hare-image identification, language-theoretic boundary, and exact fiber classification are advanced here as new**.

## Limitations
The theorem is restricted to a fixed ordered three-letter alphabet and to one application of the hare operator. It does not classify images on four or more letters, tortoise images, iterated hare maps, or distributions of fiber size. No independent scientific audit has been performed. An equivalent characterization could occur in unindexed literature or in uninspected portions of the 2026 paper. The OEIS sequence, recurrence, and numerical asymptotic in isolation are previously known and not claimed as new.

## References
1. Colin Defant and Noah Kravitz, *Stack-sorting for words*, Australasian Journal of Combinatorics **77** (2020), 51–68, Definition 1.1 and Sections 3–5. https://ajc.maths.uq.edu.au/pdf/77/ajc_v77_p051.pdf . Earliest arXiv version: arXiv:1809.09158.
2. John M. Campbell and Narad Rampersad, *Subword enumeration up to stack-sorting equivalence*, arXiv:2604.25811v1, first public 2026-04-28. https://arxiv.org/abs/2604.25811 .
3. OEIS Foundation, A077855, previously tabulated rational generating function and sequence, https://oeis.org/A077855 .

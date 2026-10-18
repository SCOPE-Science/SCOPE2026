# Parity resonance and common divisors of palindromic Zeckendorf integers

## Finding

Let \(F_0=0\), \(F_1=1\), and \(F_{j+2}=F_{j+1}+F_j\). A **canonical Zeckendorf word** of length \(L\ge1\) is a binary word \(b_1\cdots b_L\) with \(b_1=1\), no occurrence of \(11\), and numerical value
\[
N(b)=\sum_{j=1}^{L}b_jF_{L+2-j}.
\]
Let \(\mathcal P_L\) consist of these words that are palindromes. Write \(E_L\) and \(O_L\) for the numbers of words in \(\mathcal P_L\) whose **integer values** are even and odd, respectively. Put \(T_L=E_L+O_L\) and \(D_L=E_L-O_L\).

**Exact parity law.** For all \(L\ge1\),
\[
T_L=\begin{cases}
F_{(L+1)/2},&L\text{ odd},\\
F_{L/2-1},&L\text{ even}.
\end{cases}
\]
For \(3\mid L\), all the represented integers are even, so \(D_L=T_L\). For \(3\nmid L\), the imbalance is bounded and exactly periodic in \(L\), with the following residue table:

| \(L\bmod12\) | 1 | 2 | 4 | 5 | 7 | 8 | 10 | 11 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| \(D_L\) | -1 | 0 | 1 | 0 | -1 | -2 | 1 | 2 |

In particular, the **exact** counts are \(E_L=(T_L+D_L)/2\) and \(O_L=(T_L-D_L)/2\). Thus all admissible palindromes have even numerical value whenever \(3\mid L\); at every other growing length, the parity classes are asymptotically equipopulous, with absolute count discrepancy at most \(2\).

**Exact common divisor.** For \(L\ne2\), let \(G_L\) be the gcd of the positive integer values of the words in \(\mathcal P_L\). The complete exceptional range is
\[
(G_1,G_3,G_4,G_5,G_6)=(1,4,6,3,14).
\]
For every \(L\ge7\),
\[
\boxed{G_L=\begin{cases}2,&3\mid L,\\1,&3\nmid L.\end{cases}}
\]
There are no two-digit canonical palindromes, so \(G_2\) is undefined.

## Assumptions and scope

All words are canonical: no leading zeros and no adjacent ones. Digits are indexed from the most significant Fibonacci weight \(F_{L+1}\) down to \(F_2\). Length is **word length**, not ordinary binary length or the number of decimal digits. Each admissible word represents a different positive integer by Zeckendorf uniqueness. The empty length-two family is explicitly excluded from gcd statements; its parity counts are both zero.

## Proof

### Cardinalities

For \(L=2h\), a palindromic word has two equal central digits, which must be zero. Its first \(h\) digits begin in one and end in zero, with no adjacent ones. There are \(F_{h-1}\) such prefixes (including zero when \(h=1\)). For \(L=2h+1\) with \(h\ge1\), the first \(h\) digits begin in one and avoid adjacent ones. There are \(F_h\) such prefixes, of which \(F_{h-1}\) end in zero. A central zero is always permitted, while a central one is permitted exactly for the latter prefixes. This gives \(F_{h+1}\). For \(L=1\), the only word is \(1\), giving the same formula.

### Three-divisibility resonance

Fibonacci parity has period three: \(F_j\equiv0\pmod2\) precisely for \(3\mid j\). The symmetric positions corresponding to Fibonacci indices \(k\) and \(L+3-k\) have total weight \(F_k+F_{L+3-k}\). If \(3\mid L\), these two terms have equal parity because their indices are negatives modulo three, where the Fibonacci parity pattern is \((0,1,1)\). Their sum is therefore even. If \(L\) is odd, the one unpaired central position has index \((L+3)/2\), which is divisible by three when \(3\mid L\) and \(L\) is odd. Every value is then even.

### Exact bounded imbalance

For \(L\ge3\) set \(h=\lfloor L/2\rfloor\). Take the first \(h\) digits, with first digit one, and let \(A_j\) and \(B_j\) be their signed enumeration according to whether the \(j\)-th digit is zero or one, weighting each partial palindrome by \((-1)\) raised to its numerical contribution modulo two. A pair of symmetric positions at distance \(j\) from the first position contributes
\[
w_j=F_{L+2-j}+F_{j+1},\qquad s_j=(-1)^{w_j}.
\]
The exact transfer recurrence is
\[
\begin{pmatrix}A_j\\B_j\end{pmatrix}
=\begin{pmatrix}1&1\\s_j&0\end{pmatrix}
\begin{pmatrix}A_{j-1}\\B_{j-1}\end{pmatrix},
\qquad (A_1,B_1)=(0,s_1).
\]
For even \(L=2h\), the central pair must be zero, so \(D_L=A_h\). For odd \(L=2h+1\), the central bit has signed weight \(t=(-1)^{F_{h+2}}\), whence
\[
D_L=(1+t)A_h+B_h.
\]
The exceptional lengths \(1\) and \(2\) have signed counts \(-1\) and \(0\), respectively.

If \(L\equiv1\pmod3\), the periodic signs \((s_2,s_3,s_4)\) are \((-1,-1,1)\), and the transfer product for these three positions is
\[
\begin{pmatrix}-1&0\\0&1\end{pmatrix}.
\]
If \(L\equiv2\pmod3\), the signs are \((-1,1,-1)\), and the product is
\[
\begin{pmatrix}1&2\\0&-1\end{pmatrix}.
\]
Each matrix squares to the identity. Since the signs repeat every three positions, transfer across any six consecutive positions beginning after the forced first digit is exactly the identity. Replacing \(L\) by \(L+12\) increases \(h\) by six without changing its sign pattern or the center sign (Fibonacci parity is three-periodic). Hence \(D_{L+12}=D_L\) whenever \(3\nmid L\), with \(L=1,2\) verified directly against the first admissible successors. Evaluating \(L=1,2,4,5,7,8,10,11\) by the recurrence yields the displayed table. The parity counts then follow from \(E_L+O_L=T_L\) and \(E_L-O_L=D_L\).

### Gcd upper bound

For \(L\ge13\), the word with only its two endpoint digits equal to one is admissible, with value
\[
B_L=F_{L+1}+1.
\]
For each \(k\in\{4,5,6,7\}\), additionally setting the two symmetric Fibonacci-index positions \(k\) and \(L+3-k\) to one yields another admissible palindrome. The difference between its value and \(B_L\) is
\[
P_k=F_k+F_{L+3-k}.
\]
By the Fibonacci recurrence,
\[
P_4-P_5-P_6=(3-5-8)+0=-10,
\qquad
P_5-P_6-P_7=(5-8-13)+0=-16.
\]
Every common divisor of all length-\(L\) palindrome values therefore divides \(\gcd(10,16)=2\).

The previous resonance argument supplies the factor two for \(3\mid L\). For \(L\equiv2\pmod3\), \(B_L\) is odd because \(3\mid L+1\). For \(L\equiv1\pmod3\), the witness \(B_L+P_4\) is odd because \(F_{L+1}+1\) is even, whereas \(P_4=3+F_{L-1}\) is odd (here \(3\mid L-1\)). Thus the gcd is exactly one outside the divisible-by-three lengths.

Direct finite enumeration handles \(7\le L\le12\), giving gcds \((1,1,2,1,1,2)\). At \(L=1,3,4,5,6\) the gcds are \((1,4,6,3,14)\) from the values \(\{1\},\{4\},\{6\},\{9,12\},\{14\}\). This completes the infinite classification.

## Verification

Run `python3 verify.py` with Python 3 and its standard library. This independently enumerates every admissible word through length \(25\), compares all counts and gcds with the theorem, and enumerates ordinary integers and reconstructs their Zeckendorf words independently through length \(22\). It also checks the signed transfer recurrence through length \(1000\) and the four universal witness identities over an extended range. Successful execution prints `ZECKENDORF_PALINDROME_EXACT_OK`. The infinite steps are the recurrence and witness identities in the proof, not the finite tests.

## Relationship to prior work

Ron Knott's OEIS sequence A094202, originally submitted on May 25, 2004, catalogs exactly the integers with palindromic canonical Zeckendorf representations. His mathematical exposition gives examples and discusses palindromic Fibonacci numeration. OEIS A349238 identifies the same set as the fixed points of Zeckendorf digit reversal. These catalogued objects and reversal equivalence are prior work; the present result concerns the complete **fixed-length parity distribution and gcd law**, neither of which is stated in the inspected sources. The result does not claim a new enumeration of the underlying palindromic set or a new proof of the Zeckendorf representation theorem.

## Limitations

The theorem concerns parity and the full-value gcd at each fixed canonical length. It makes no claim about distribution modulo arbitrary odd moduli, primality, density among all positive integers, or other digit representations. The literature comparison covers the inspected catalog records and accessible expositions; an earlier non-indexed derivation of the same parity or gcd formulas cannot be ruled out. The proof is ordinary mathematical reasoning supplemented by finite checks, not independent certification.

## References

1. Ron Knott, "Integers whose Zeckendorf representation is palindromic," OEIS A094202 (original author entry dated May 25, 2004), https://oeis.org/A094202 .
2. Kevin Ryde, "Reverse the digits in the Zeckendorf representation," OEIS A349238 (original entry dated November 11, 2021), https://oeis.org/A349238 .
3. Ron Knott, "Number Palindromes," section "Fibonacci Numbers," https://fibonacci-numbers.surrey.ac.uk/IntegerReps/palindromes.html .
4. C. G. Lekkerkerker, "Voorstelling van natuurlijke getallen door een som van getallen van Fibonacci," Simon Stevin 29 (1952), 190–195; historical basis for canonical uniqueness (not re-proved here).

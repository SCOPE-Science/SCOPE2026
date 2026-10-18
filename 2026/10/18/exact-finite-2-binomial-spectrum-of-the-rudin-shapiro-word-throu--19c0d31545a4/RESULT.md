# Exact finite 2-binomial spectrum of the Rudin–Shapiro word through length \(4096\)

## Finding

Let \(r=r_0r_1\cdots\) be the binary Rudin–Shapiro word, where \(r_i\) is the parity of the number of overlapping occurrences of \(11\) in the binary expansion of \(i\). Let \(b_r^{(2)}(n)\) be the number of 2-binomial equivalence classes among its length-\(n\) contiguous factors (two words are equivalent when they have equal counts of every scattered subsequence of length at most two).

**Finite exact classification.** The accompanying `spectrum.csv` gives \(b_r^{(2)}(n)\), the corresponding abelian complexity, and the minimum and maximum number of ones in a factor, **for each integer \(1\le n\le4096\)**. The table is exhaustive, by the finite-cover theorem below and the supplied reproducing implementation. The file `dyadic_weights.csv` further gives the exact number of 2-binomial classes at each possible number of ones for all powers of two at most \(4096\). In particular, at lengths \(1,2,4,8,16,32,64,128,256,512,1024,2048,4096\) the 2-binomial complexities are respectively

\[
2,4,15,38,89,158,377,622,1549,2426,6221,9558,24783.
\]

At length \(4096\), there are precisely \(24783\) 2-binomial classes, spread across \(191\) possible weights, from \(1953\) through \(2143\) ones.

**Universal exact reduction.** For every \(n\ge1\), let \(h=\lceil\log_2 n\rceil\), \(L=2^h\), and let \(\varphi\) be the four-letter substitution
\[
\varphi(0)=01,\qquad\varphi(1)=03,\qquad\varphi(2)=23,\qquad\varphi(3)=21,
\]
with coding \(\tau(0)=\tau(1)=0\) and \(\tau(2)=\tau(3)=1\). Define
\[
E=\{(0,1),(0,3),(1,0),(1,2),(2,1),(2,3),(3,0),(3,2)\}.
\]
For a binary word \(u=u_0\cdots u_{n-1}\), define its weight and first positional moment by
\[
W(u)=\sum_{j=0}^{n-1}u_j,\qquad T(u)=\sum_{j=0}^{n-1}j u_j.
\]
The following is an exact, **all-length formula**, with no finite-cutoff assumption:
\[
 b_r^{(2)}(n)=\left|\left\{\bigl(W(v),T(v)\bigr): v=\tau\bigl(\varphi^h(a)\varphi^h(b)\bigr)[s:s+n],\ (a,b)\in E,\ 0\le s<L\right\}\right|.
\]
The interval notation means the length-\(n\) contiguous segment beginning at offset \(s\). This formula specifies at most \(8L\) candidate profiles, is exact at **every** positive integer \(n\), and establishes a finite computation for any requested length. It does not assert a simpler closed form for the numerical complexity at arbitrary lengths.

## Assumptions and scope

Indices are zero-based; scattered-subsequence counts count strictly increasing index choices. The word is the classical binary Rudin–Shapiro coding, not its signed variant. All statements hold for the infinite fixed point of \(\varphi\) beginning in state \(0\). The displayed complete numeric census is asserted only for \(1\le n\le4096\). The universal reduction, factor-language cover, and complement symmetry hold without a bound on \(n\).

## Proof

**1. A four-state presentation.** Write \(r_i\) for the parity of the number of adjacent \(11\) pairs in the base-two digits of \(i\), and let \(p_i\equiv i\pmod2\). Appending a zero bit creates no new \(11\); appending a one bit creates such a pair exactly when \(p_i=1\). Thus
\[
 r_{2i}=r_i,\quad r_{2i+1}=r_i\mathbin{\mathrm{xor}}p_i,\quad p_{2i}=0,\quad p_{2i+1}=1.
\]
The state \(2r_i+p_i\) therefore evolves under the above \(\varphi\). Its fixed point starts at state \(0\), and its \(\tau\)-coding is exactly \(r\).

**2. The complete adjacent-pair set.** All eight pairs in \(E\) occur as adjacent states in \(\varphi^4(0)\). Applying \(\varphi\) to a word having only adjacent pairs in \(E\) creates only pairs in \(E\): the within-letter pairs are \((0,1),(0,3),(2,3),(2,1)\), and each boundary pair is \((\varphi(a)_1,\varphi(b)_0)\) for an element \((a,b)\in E\). Direct checking gives the same eight-member set. Induction therefore shows that the infinite fixed point has **exactly** the adjacent-pair set \(E\).

**3. Exhaustive finite cover, for any length.** Choose \(h\) and \(L\) as above, so \(n\le L\). Every contiguous length-\(n\) factor of the fixed point starts inside an aligned block of length \(L\); it is contained in this block together with the immediately next block. Those two blocks are \(\varphi^h(a)\varphi^h(b)\) for some adjacent pair \((a,b)\in E\), with starting offset \(0\le s<L\). Conversely, every pair in \(E\) occurs in the fixed point, so its substituted concatenation occurs, and every proposed segment is a genuine factor. Hence the displayed finite cover is an equality, not merely an upper bound. An equivalent fixed-prefix certificate for all lengths at most \(2^h\) is \(\tau(\varphi^{h+4}(0))\): its \(2^h\)-block parent prefix contains all eight adjacent pairs.

**4. Reduction of scattered-subsequence counts.** For a binary word \(u\) of length \(n\), let \(w=W(u)\). The number of scattered \(11\)'s is \(\binom{w}{2}\), and that of \(00\)'s is \(\binom{n-w}{2}\). Each one at position \(j\) has \(n-1-j\) later positions, of which the later ones contribute to \(\binom{w}{2}\); hence
\[
 \#10=w(n-1)-T(u)-\binom{w}{2},\qquad \#01=w(n-w)-\#10.
\]
Consequently, for two fixed-length binary words, agreement of all scattered-subsequence counts through length two is **equivalent** to agreement of the ordered pair \((W,T)\). Applying this fact to the exact factor cover proves the universal formula.

**5. Reproducibility of the finite census.** The program `enumerate.cpp` builds all eight substituted adjacent-pair blocks with \(h=12\) and, for each \(1\le n\le4096\), maintains \((W,T)\) through each of the \(4096\) shifts. The recurrences are
\[
W_{s+1}=W_s-u_s+u_{s+n},\quad
T_{s+1}=T_s-W_s+u_s+(n-1)u_{s+n}.
\]
It deduplicates the full exact integer pairs, writes the complete numeric spectrum and all dyadic weight profiles. The finite-cover lemma proves that these enumerated profiles include **all** factors, not just all factors of a sampled prefix. The independent direct-digit implementation `verify_independent.cpp` checks every numeric row from an explicit \(65536\)-symbol prefix; this long prefix is also exhaustive for the claimed range by Step 3. Each arithmetic statistic fits in its exact integer type for the present cutoff.

**6. Complement symmetry.** The involution \(a\mapsto a\mathbin{\mathrm{xor}}2\) commutes with \(\varphi\), preserves \(E\), and exchanges coded zeros and ones. Thus the factor language is closed under complement and its complete profile sets are centrally symmetric:
\[
(W,T)\mapsto\left(n-W,\frac{n(n-1)}2-T\right).
\]
This serves as an additional exact structural check on the stated weight-resolved classification.

## Verification

Compile and run with a C++17 compiler from the directory containing the four packaged artifacts:

```sh
g++ -O2 -std=c++17 -Wall -Wextra -Werror enumerate.cpp -o enumerate
./enumerate regenerated_spectrum.csv regenerated_dyadic_weights.csv
cmp spectrum.csv regenerated_spectrum.csv
cmp dyadic_weights.csv regenerated_dyadic_weights.csv
g++ -O2 -std=c++17 -Wall -Wextra -Werror verify_independent.cpp -o verify_independent
./verify_independent spectrum.csv dyadic_weights.csv
```

The first executable checks the eight-pair closure, compares the four-state coding with the digit definition for all \(65536\) initial symbols, and enumerates the exact profile sets. The second executable uses only the digit definition, enumerates every possible start within the same \(65536\)-letter prefix, and checks each of the \(4096\) rows plus every dyadic weight count. Both emitted `VERIFY_OK` on the included data. The mathematical proof of exhaustive coverage, not the prefix length alone, supports the completeness claim.

## Relationship to prior work

Rigo and Salimov (2015) introduced binomial equivalence and its complexity functions and gave general results, notably for certain morphic words. Their inspected definitions and general theorems do not supply the Rudin–Shapiro numerical spectrum or the eight-pair profile census here. Lü, Chen, Wen, and Wu (2016) studied the **abelian** complexity of the Rudin–Shapiro word, which records \(W\) but not \(T\): their results therefore do not determine the 2-binomial classes in this census. Lü and collaborators' later study of generalized Thue–Morse 2-binomial complexity treats a different automatic-word family. The present classification is an explicit finite exact data set for Rudin–Shapiro with a full all-length substitution reduction. The inspected literature does not establish the claimed complete table; this does not exclude an unindexed equivalent table or proof.

## Limitations

The complete numerical table stops at length \(4096\); neither a general closed-form numerical sequence nor an asymptotic law for \(b_r^{(2)}(n)\) is claimed. The eight-pair exact formula applies for all \(n\) but may require fresh enumeration to evaluate. Source comparison cannot eliminate the possibility of inaccessible or unindexed equivalent finite tables. The verification programs and tabulation give reproducibility, not independent human audit.

## References

1. Michel Rigo and Pavel Salimov, *Another generalization of abelian equivalence: binomial complexity of infinite words* (public author version available 26 February 2015), `hdl:2268/178703`, https://orbi.uliege.be/bitstream/2268/178703/1/binomial_TCS_final.pdf.
2. Xiao-Tao Lü, Jin Chen, Zhi-Xiong Wen, and Wen Wu, *On the abelian complexity of the Rudin–Shapiro sequence* (arXiv version dated 22 June 2016), `arXiv:1606.06935`, https://arxiv.org/abs/1606.06935.
3. Xiao-Tao Lü, Jin Chen, Zhi-Xiong Wen, and Wen Wu, *On the 2-binomial complexity of generalized Thue–Morse words* (2021 preprint), `arXiv:2112.05347`, https://arxiv.org/abs/2112.05347.

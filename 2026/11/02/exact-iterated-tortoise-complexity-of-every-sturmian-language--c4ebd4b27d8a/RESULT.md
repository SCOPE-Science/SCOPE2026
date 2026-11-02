# Exact iterated tortoise complexity of every Sturmian language

## Finding
Let \(\mathbf x\) be a binary Sturmian word in which the limiting frequency of \(1\) is the irrational number \(\alpha\in(0,1)\). For integers \(k\ge1\) and \(n\ge1\), let \(T\) be the Defant–Kravitz binary tortoise map and count its distinct \(k\)-fold images on length-\(n\) factors:
\[
C_{\alpha,k}(n)=\left|\{T^k(w): w\in\mathcal L_n(\mathbf x)\}\right|.
\]
Then the **exact complete formula**, uniform in every irrational slope and every number of iterations, is
\[
\boxed{C_{\alpha,k}(n)=n+1-\min\left\{n-1,\left\lfloor\frac{k}{\alpha}\right\rfloor\right\}
=\max\left\{2,n+1-\left\lfloor\frac{k}{\alpha}\right\rfloor\right\}.}
\]
Consequently the last length at which the \(k\)-tortoise and Abelian complexity functions agree is precisely
\[
\boxed{\operatorname{abel}_{\mathbf x}(k)=\left\lfloor\frac{k}{\alpha}\right\rfloor+1.}
\]
In particular, the first discrepancy is at length \(\lfloor k/\alpha\rfloor+2\), with a strictly positive discrepancy at every greater length.

## Assumptions and scope
The alphabet is ordered \(0<1\). A *factor* is a contiguous finite subword; two factors are considered equivalent when their images under exactly \(k\) iterations of the same tortoise operator coincide. The binary tortoise map \(T\) removes the leftmost \(1\) of a word and appends it at the right; it fixes an all-zero word. If a word contains at most \(k\) ones, \(T^k\) is its sorted word \(0^a1^b\); if it contains more than \(k\) ones, \(T^k\) deletes the first \(k\) ones in their original positions and appends \(k\) ones. The exponent \(k\) is an iteration count, not a subword length and not the parameter of \(k\)-Abelian equivalence.

A Sturmian word has factor complexity \(n+1\), and its factor language is that of an irrational mechanical rotation coding; all intercepts for a fixed irrational letter frequency share the same language. More explicitly, for \(0\le\beta<1\), the phase-coded factor at length \(n\) is
\[
w_\beta(i)=\lfloor\beta+(i+1)\alpha\rfloor-\lfloor\beta+i\alpha\rfloor,\quad 0\le i<n.
\]
As \(\beta\) traverses its unit interval, these factors run through the full \(n+1\)-element length-\(n\) factor language. No restriction on the continued fraction of \(\alpha\), the intercept, or the starting position is imposed.

## Proof
**Mechanical-factor partition.** Define for \(1\le j\le n\) the discontinuity phase \(b_j=1-\{j\alpha\}\). Irrationality makes these phases distinct and strictly internal to \((0,1)\). For each phase \(\beta\) the initial \(j\) letters of its mechanical factor sum to \(\lfloor\beta+j\alpha\rfloor\). Consequently exactly one prefix-sum coordinate jumps at each \(b_j\), and the entire word is constant in each of the \(n+1\) complementary intervals. The successive distinct words are the full Sturmian length-\(n\) language by density of irrational rotations. The convention with floors makes the word at a discontinuity equal the word immediately to its right; no extra endpoint words exist.

**Local behavior at a discontinuity.** Suppose first that \(1\le j<n\). When \(\beta\) crosses \(b_j\) upward, the affected adjacent letters change from \(01\) to \(10\): there exist binary words \(u,v\) such that the transition is
\[
u01v\longrightarrow u10v.
\]
Let \(r=|u|_1+1\) be the ordinal position of the changing \(1\) when the ones of either word are counted from left to right. The two \(k\)-tortoise images are identical **if and only if** \(r\le k\). Indeed, both inputs have the same ordered list of all other ones. If the swapped one belongs to the first \(k\), both outputs remove that one together with the other first \(k\) ones and append the same \(k\) ones. If it does not, deletion of the first \(k\) ones leaves the indicated \(01\)-to-\(10\) swap in the common remaining context, so the right image is strictly greater in lexicographic order. This argument also applies when \(k\) exceeds the total number of ones, because the two words then have the same sorted image.

For the special crossing \(j=n\), only the final letter changes, \(u0\longrightarrow u1\). The corresponding \(k\)-tortoise images are *always strictly increasing* in lexicographic order. To see this, delete the first \(k\) ones if \(u\) contains at least \(k\) ones; the common residual prefix is followed by final \(0\) versus \(1\), and then a common string of appended ones. If \(u\) contains fewer than \(k\) ones, the two sorted outputs contain unequal numbers of ones, with \(u0\) having fewer, so again the right image is greater.

**Rank of the critical one.** Just before the crossing \(b_j\), the first \(j\) mechanical letters comprise \(\lfloor j\alpha\rfloor\) ones: indeed
\[
\lim_{\beta\uparrow b_j}\lfloor\beta+j\alpha\rfloor=\lfloor j\alpha\rfloor.
\]
At the left phase the critical \(1\) stands at position \(j+1\) (when positions are counted starting at one), immediately after this prefix. Its rank is therefore exactly
\[
r_j=\lfloor j\alpha\rfloor+1.
\]
It follows from the local lemma that the crossing at \(j<n\) is erased under \(T^k\) precisely when \(\lfloor j\alpha\rfloor<k\), equivalently \(j\alpha<k\). Irrationality prevents equality for integer \(j\ge1\). Hence the number of erased crossings is
\[
E=\#\{1\le j<n:j\alpha<k\}=\min\left\{n-1,\left\lfloor\frac{k}{\alpha}\right\rfloor\right\}.
\]
Every crossing is nondecreasing under \(T^k\); the non-erased crossings are *strictly* increasing, including the final crossing at \(j=n\). Thus images at two separated phase intervals cannot coincide unless every intervening crossing was erased. There are exactly \(n+1-E\) distinct images, proving the first formula.

**Abelian threshold.** At each fixed length, the \(1\)-counts of Sturmian factors are precisely the two integers \(\lfloor n\alpha\rfloor\) and \(\lceil n\alpha\rceil\), so Abelian complexity equals two for every \(n\ge1\). The displayed formula gives \(C_{\alpha,k}(n)=2\) exactly when \(n\le\lfloor k/\alpha\rfloor+1\); the next length has complexity three. This proves the stated exact threshold.

## Verification
Two independent, standalone Python programs accompany the proof. `verify_local.py` directly applies the tortoise map to binary contexts and checks the adjacent-swap equivalence/strict-order dichotomy in 266,253 cases plus 26,611 terminal-change comparisons. `verify_rotations.py` enumerates exact rational mechanical cyclic factors of slopes with reduced denominators through 96; its 973,080 length/iteration tests agree with the formula. These tests concern finite words or rational analogues and are **not** substitutes for the irrational, all-length proof above. Both are reproducible with the Python standard library: `python3 verify_local.py` and `python3 verify_rotations.py`.

## Relationship to prior work
Campbell and Rampersad introduced \(k\)-tortoise complexity as a complexity function, established results for paperfolding and Thue–Morse, and explicitly raised the problem of Sturmian variants in their conclusion [1, §§3–7]. They prove a general bounded-deficit statement for one iteration on certain low-complexity words, but not this exact slope- and iteration-dependent function. The binary operation comes from Defant and Kravitz [2]. Standard irrational-rotation descriptions of Sturmian factor languages are recalled in [3]. The present theorem refines the general bounded-deficit behavior to a complete formula for every Sturmian language, every iteration count, and every positive factor length. Restricted-slope, one-iteration cases are special instances of this wider formula and are not independent claims of novelty.

## Limitations
This result concerns the binary tortoise map and Sturmian languages of irrational slope. It does not enumerate fibers, their individual cardinalities, the hare operation on larger alphabets, or tortoise complexity of non-Sturmian low-complexity words. A finite verification cannot establish the irrational all-length statement; the proof relies instead on rotation discontinuities and the local image lemma. No independent review or priority determination beyond the cited comparisons has been performed.

## References
[1] J. M. Campbell and N. Rampersad, “Subword enumeration up to stack-sorting equivalence,” arXiv:2604.25811, first public version 2026-04-28, full text https://arxiv.org/html/2604.25811v2 (especially Definitions 1–2, Section 3, and Section 7).

[2] C. Defant and N. Kravitz, “Stack-sorting for words,” arXiv:1809.09158, original version 2018-09-24, published in the Australasian Journal of Combinatorics 77 (2020); full text https://ajc.maths.uq.edu.au/pdf/77/ajc_v77_p051.pdf.

[3] M. Andrieu, “Infinite Words with very Low Factor Complexity: an introduction to Combinatorics on Words,” arXiv:2603.07816, 2026; https://arxiv.org/abs/2603.07816.

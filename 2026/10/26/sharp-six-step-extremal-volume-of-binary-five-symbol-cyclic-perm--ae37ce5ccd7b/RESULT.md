# Sharp six-step extremal volume of binary five-symbol cyclic-permutation balls

## Finding

For every integer \(n\ge 5\) and binary word \(x\in\{0,1\}^n\), let \(B_5(x)\) contain \(x\) and every distinct word obtainable by applying **one** cyclic rotation by one, two, three, or four positions to any contiguous block of exactly five bits. Blocks do not wrap around the word's endpoints. Write \(M_5(n)=\max_{x\in\{0,1\}^n}|B_5(x)|\). Then

\[
M_5(n)=\begin{cases}
5,&n=5,\\
3n-9+\left\lfloor\dfrac{n-4}{6}\right\rfloor,&n\ge6.
\end{cases}
\]

For every \(n\ge6\), the length-\(n\) prefix of the six-periodic infinite binary word \((001101)^\infty\) attains the bound. In particular \(M_5(n+6)=M_5(n)+19\) for all \(n\ge6\). This is an exact worst-case radius-one ball volume, not a statement about maximum code cardinality.

## Assumptions and scope

The alphabet is binary, the received word has the same length as the transmitted word, exactly one window of length five may undergo any power of its cyclic five-cycle, and the unchanged received word is included. A nontrivial rotation yielding an identical word contributes no extra output. Distinct windows and distinct rotations producing the same received word are counted only once. The codeword itself is allowed; no cyclic wraparound of the ambient length-\(n\) word is allowed. The result treats precisely this channel and makes no claim for different error lengths, multiple errors, or a larger alphabet.

## Proof

**1. Canonical fresh-window decomposition.** Number windows from \(i=0\) to \(i=n-5\). Let \(R_i(x)\) be the set of nonidentity received words obtained by rotating the length-five block starting at \(i\) through its four nontrivial cyclic powers. Define \(c_i(x)=|R_i(x)\setminus\bigcup_{0\le j<i}R_j(x)|\). Thus, exactly,

\[
|B_5(x)|=1+\sum_{i=0}^{n-5}c_i(x).
\]

If \(i-j\ge5\), the windows are disjoint, so \(R_i(x)\cap R_j(x)=\varnothing\): every member of \(R_i(x)\) differs from \(x\) in a nonempty subset of the \(i\)-window, while any member of \(R_j(x)\) differs in a disjoint nonempty subset. Consequently \(c_i(x)\) compares \(R_i(x)\) only with the four preceding windows and depends solely on the at-most-nine-letter segment \(x_{\max(0,i-4)}\cdots x_{i+4}\). This locality is an exact set-theoretic identity, independent of the computation below.

**2. An exact finite-state upper certificate.** Let \(S=\{0,1\}^8\). For every nine-bit word \(u\), define \(g(u)\) as the number of new nonidentity outcomes contributed by its rightmost length-five window relative to its four preceding windows. This is obtained by computing at most four rotations in each of five windows and taking set differences; there are only \(512\) arguments \(u\).

For \(n\ge8\) and suffix \(s\in S\), define \(V_n(s)\) to be the maximum of \(\sum_i c_i(x)\), over binary length-\(n\) words \(x\) having final eight bits \(s\). In particular \(V_8(s)\) is the sum of the four exact initial window gains for the single word \(s\). If \(s=s_1\cdots s_8\) and \(b\in\{0,1\}\), append one bit along the directed edge

\[
s\ \longrightarrow\ s_2\cdots s_8b,\qquad \text{weight }g(s_1\cdots s_8b).
\]

The exact dynamic-programming update is therefore

\[
V_{n+1}(t)=\max_{\substack{s\in S,\,b\in\{0,1\}\\s_2\cdots s_8b=t}}\bigl(V_n(s)+g(sb)\bigr).
\]

The attached standalone `verify.py` constructs all \(256\) states, all \(512\) transition weights, and the initial vector directly from the stated channel operations, using exact integers and no imported certificates. It exhaustively checks the following **componentwise identity** (not merely equality of maxima):

\[
V_{18}(s)=V_{12}(s)+19\qquad\text{for all }s\in S.
\]

It independently verifies the same identity at each of the six successive base indices \(12,13,14,15,16,17\). The update operator commutes with the addition of a common constant to every component. Applying the operator repeatedly to the identity at index \(12\) gives

\[
V_{n+6}(s)=V_n(s)+19\qquad(n\ge12,\ s\in S).
\]

Direct exact enumeration for lengths \(5,6,7\), followed by the same finite-state recurrence for lengths \(8,\ldots,17\), gives the maximum-ball profile

\[
5,9,12,15,18,22,25,28,31,34,37,41,44
\]

at \(n=5,\ldots,17\). Its six values at \(n=12,\ldots,17\), combined with the componentwise six-step identity, certify that for **every** \(n\ge6\),

\[
|B_5(x)|\le3n-9+\left\lfloor\frac{n-4}{6}\right\rfloor.
\]

This is an infinite proof with a completely specified finite integer certificate; the limited brute-force checks alone are not used to infer the infinite conclusion.

**3. Explicit sharpness construction.** Consider the prefix of \((001101)^\infty\). Direct examination of the first two windows gives gains \(c_0=c_1=4\). For every later window, the gain is \(3\) except when the start index is congruent to \(5\) modulo \(6\), when it is \(4\). This last assertion reduces to inspecting the six possible nine-bit periodic blocks; it follows from the locality proved in step 1. The verifier checks the two boundary cases and each periodic residue class by the same exact set operations. For \(m=n-4\ge2\) windows the gain sum is \(3m+2+\lfloor m/6\rfloor\). Therefore

\[
|B_5(x)|=1+3(n-4)+2+\left\lfloor\frac{n-4}{6}\right\rfloor=3n-9+\left\lfloor\frac{n-4}{6}\right\rfloor,
\]

attaining the bound. For \(n=5\), a nonconstant five-bit word has five distinct rotations because five is prime, while no window has more than five rotations. This completes the proof.

## Verification

Run `python3 verify.py` using Python 3 and only its standard library. The checker performs full set-based enumeration for every binary word at lengths \(5\) through \(14\), checks the dynamic-programming profile through length \(23\), and checks the six componentwise max-plus identities on every one of the \(256\) states. It also reconstructs the periodic witness and independently verifies further lengths through \(60\). The output ends in `VERIFY_OK`; the included `verify_output.txt` is the actual replay output. The reproducible finite certificate is the complete source of `verify.py`, not the recorded output by itself.

## Relationship to prior work

Chen and Milenkovic define exact-length cyclic-substring permutation errors over binary words and prove general coding-redundancy estimates and constructions, with their cyclic lower bound stated for \(k\ge9\). Sections I, III, and IV of their full arXiv version do not present this exact all-length radius-one ball maximum at \(k=5\). Their model's general window-counting estimates alone do not imply the six-step extremal law. Other burst-correcting and adjacent-transposition settings differ either in which symbols may be altered or in the permissible permutations. The present result identifies a specific missing sharp finite-block ball-volume invariant of the same error channel; it does not strengthen all of their code-size theorems.

## Limitations

The result concerns the binary, fixed-five, single-error, no-wraparound channel only. It does not classify all maximizing words, compute average ball sizes, establish code-size optima, or extend the formula to other window lengths. The proof is computer-assisted: the infinite conclusion depends on the correct finite exact-integer implementation of the explicitly defined 256-state max-plus recurrence. Source coverage and indexing are not exhaustive; an independently reported equivalent result could exist.

## References

- Y.-P. Chen and O. Milenkovic, *Correcting Burst Errors with Applications to DNA-Based Data Storage*, arXiv:2610.15701v1, first publicly submitted 2026-10-11, especially Definition 3, Section III (cyclic permutation errors), and Section IV (ball upper bounds). https://arxiv.org/html/2610.15701v1

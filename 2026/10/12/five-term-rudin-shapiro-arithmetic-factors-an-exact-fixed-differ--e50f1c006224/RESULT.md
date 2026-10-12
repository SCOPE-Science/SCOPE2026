# Five-term Rudin–Shapiro arithmetic factors: an exact fixed-difference dichotomy
## Finding
Let \(r:\mathbb N_0\to\{0,1\}\) be the binary Rudin–Shapiro sequence: \(r(n)\) is the parity of the number of possibly overlapping occurrences of \(11\) in the binary expansion of \(n\). For every fixed integer \(d\ge1\), define its **five-term arithmetic factor set**
\[
\mathcal A_d^{(5)}=\{(r(n),r(n+d),r(n+2d),r(n+3d),r(n+4d)):n\ge0\}.
\]
The exact classification is
\[
|\mathcal A_d^{(5)}|=\begin{cases}
24,&d\text{ is a power of }2,\\
32,&d\text{ is not a power of }2.
\end{cases}
\]
When \(d\) is a power of two, exactly the following eight words are **absent**:

`00000`, `11111`, `00110`, `11001`, `01010`, `10101`, `01100`, `10011`.

If \(d\) is not a power of two, **every** binary word of length five occurs along a progression with precisely that difference. Consequently every fixed positive difference admits all sixteen binary four-term arithmetic patterns.

## Assumptions and scope
Indices and differences are nonnegative integers, with \(d\ge1\) fixed before the starting position \(n\) is chosen; all five sampled positions must have exactly that common difference. Patterns are **ordered** words, not frequency classes or words up to complement. Binary expansions have finitely many nonzero digits, with leading zeros allowed in digit recurrences.

The claim concerns existence of five-term patterns, not their limiting frequencies or maximal lengths of longer monochromatic progressions. It does not assert that every length-six word occurs at every non-dyadic difference. A **relative signature** of a five-term pattern \(t_0t_1t_2t_3t_4\) is the four-bit integer with bits \(t_j\mathbin{\mathrm{xor}}t_0\), for \(1\le j\le4\), listed in increasing order of \(j\).

## Proof
### Binary addition and the relative-signature machine
Write the binary digits of \(n\) and \(d\) least significant first, with digits \(x_h,e_h\in\{0,1\}\). At bit position \(h\) let \(c_j\) be the addition carry for \(n+jd\), for \(j=1,2,3,4\); take \(c_0=0\). The digit of \(n+jd\) is
\[
z_j=(x_h+j e_h+c_j)\bmod2,
\quad c'_j=\left\lfloor(x_h+j e_h+c_j)/2\right\rfloor
\qquad(1\le j\le4),
\]
while \(z_0=x_h\). Let \(b_j\) be the preceding lower binary digit of \(n+jd\), including \(j=0\). The Rudin–Shapiro parity is the XOR of products of adjacent digits. Therefore if \(q_j\) records the relative parity difference accumulated so far, the exact digit update is
\[
q'_j=q_j\mathbin{\mathrm{xor}}(b_jz_j)\mathbin{\mathrm{xor}}(b_0z_0)
\qquad(1\le j\le4).
\]
Replace the previous-bit vector by \((z_0,\ldots,z_4)\), and initialize carries, previous bits, and relative parities to zero. All carries remain in \(\{0,1,2,3,4\}\); the machine has a finite explicitly coded state space. Each input bit \(e_h\) of \(d\) allows **both** choices of \(x_h\), so this is a nondeterministic finite-state machine projecting away the starting position.

After the last nonzero digit of \(d\), only input digits \(e_h=0\) remain, while the higher digits \(x_h\) of \(n\) are unrestricted. A relative signature \(q\) is achievable from a machine state **if and only if** some finite string of such zero-difference transitions reaches a state with all four carries zero and relative register \(q\). For necessity, take enough leading zeros to finish every addition. For sufficiency, set any remaining high digits of \(n\) to zero; they then cause no new adjacent-one contributions.

### Exhaustive finite-state closure (all differences at once)
The standalone `verify.py` constructs the reachable machine, computes these terminal signatures by a least fixed point, then determinizes over the two possible digits of \(d\). The finite computation has precisely **864 reachable nondeterministic states** and **1302 reachable determinized states**. A determinized state is a set of nondeterministic states; its output mask is the bitwise union of their achievable terminal-signature masks. The verifier checks all transitions and all reachable states, including cycles.

Let \(h\) denote the number of \(1\)-digits of the processed difference, truncated at two. For **every** reachable determinized state, the checked output mask is exactly
\[
M(h)=\begin{cases}
\mathtt{0x0001},&h=0,\\
\mathtt{0xff96},&h=1,\\
\mathtt{0xffff},&h=2.
\end{cases}
\]
The numbers of reachable states carrying those three labels are respectively \(2,13,1287\). The verifier checks that each state has a **consistent** label, both input transitions update the label by \(h\mapsto\min(2,h+e_h)\), and its output equals the displayed mask; the initial state has \(h=0\). This is a finite inductive certificate for **all finite binary representations of all** \(d\), not an extrapolation from a bound on \(d\).

For a positive \(d\), the number of \(1\)-digits is exactly one precisely when \(d\) is a power of two. Thus its attainable four-bit relative signatures have mask \(\mathtt{0xff96}\) in that case and \(\mathtt{0xffff}\) otherwise. The four signatures missing from \(\mathtt{0xff96}\) are \(q=0,3,5,6\).

### Recovering the absolute starting bit
For every fixed \(n,d\), choose a sufficiently large bit position \(K\) such that the binary expansions of all \(n+jd\) have zero digits at positions \(K-1\) and above. Replacing \(n\) by \(n+3\cdot2^K\) appends a separated high-order binary block \(11\) to each of the five sampled numbers. This contributes **exactly one** additional occurrence of \(11\) to each parity, hence complements all five values simultaneously without changing the relative signature or the difference.

Consequently each attainable relative signature gives **both** five-bit patterns corresponding to the two possible values of \(r(n)\). The two sets are disjoint. Hence the attainable pattern counts are twice the number of set bits in the mask: \(2\cdot12=24\) or \(2\cdot16=32\). Translating the missing signatures \(0,3,5,6\) gives exactly the eight words listed above. Finally, each four-bit word can be extended to a five-bit word occurring at the same difference; for dyadic differences, direct inspection of the eight omitted five-bit words shows that every four-bit prefix is still represented. This proves the final consequence.

## Verification
Run `python3 verify.py` next to `certificate.json` with Python 3.8 or later; it requires no third-party packages. The verifier independently regenerates all digit transitions from their arithmetic definitions, computes the terminal-output least fixed point, builds all reachable determinized subset states, checks the output-mask invariant and both transitions at every state, and confirms the exceptional patterns.

As an independent **regression test only**, it constructs the Rudin–Shapiro sequence directly via \(r(n)=r(\lfloor n/2\rfloor)\mathbin{\mathrm{xor}}((n\bmod2)(\lfloor n/2\rfloor\bmod2))\) and enumerates factors for every \(1\le d\le128\) and starting positions below \(131072\). The proof of the infinite statement is the exhaustive finite-state closure and induction, not this sampled enumeration.

The replay result is `VERIFY_OK nfa_states=864 dfa_states=1302 classes=2,13,1287 relative_masks=0x0001,0xff96,0xffff missing=00000,11111,00110,11001,01010,10101,01100,10011 direct_d=1..128 direct_patterns=4032`.

## Relationship to prior work
Jugé and Marcovici study correlations of block-additive automatic sequences, including Golay–Shapiro-type sequences. Their definitions involve arbitrary fixed tuples of offsets and limiting **frequencies**, and their theorems classify uncorrelatedness across families; they do not assign the zero/nonzero support of every individual **five-term arithmetic** pattern for the original Rudin–Shapiro sequence at every prescribed difference.

Sobolewski analyzes maximal **monochromatic** arithmetic progressions in the Rudin–Shapiro and related pattern sequences, including progressions at specified differences. Those results concern lengths of constant runs (in particular for special differences) rather than the entire set of 32 possible ordered five-symbol patterns. The present classification determines all nonconstant patterns as well, with a sharp dyadic-versus-nondyadic split.

Konieczny and Müllner classify **arithmetical subword complexity**, which asks whether a word appears for **some** common difference (the difference is existentially quantified), and the asymptotic length dependence. That does not imply the stronger universal-in-difference classification here. The Gowers-uniformity literature yields global progression-count estimates; it need not exclude fixed-difference zero-pattern obstructions, which are essential in the present theorem.

## Limitations
The classification concerns exactly five sampled positions and the ordinary binary Rudin–Shapiro sequence. It does not determine densities of the occurring five-term patterns, nor characterize spectra at lengths six or above. A complete state-closure proof is provided as executable finite mathematics; the explicit 1302-state transition table is regenerated rather than reproduced in print. Earlier or unindexed fixed-difference support calculations remain an originality risk despite targeted comparisons.

## References
1. Vincent Jugé and Irène Marcovici, “Finding automatic sequences with few correlations,” *Pure Mathematics and Applications* 30 (2022), 75–81, DOI:10.2478/puma-2022-0012, first publicly published 2022-06-18.
2. Bartosz Sobolewski, “On Monochromatic Arithmetic Progressions in Binary Words Associated with Pattern Sequences,” arXiv:2204.05287v1, 2022-04-11 (revised 2023).
3. Jakub Konieczny and Clemens Müllner, “Arithmetical Subword Complexity of Automatic Sequences,” arXiv:2309.03180v1, 2023-09-06 (revised 2024).
4. Jakub Byszewski, Jakub Konieczny, and Clemens Müllner, “Gowers Norms for Automatic Sequences,” arXiv:2002.09509v1, 2020-02-21; *Discrete Analysis* (2023), 4.

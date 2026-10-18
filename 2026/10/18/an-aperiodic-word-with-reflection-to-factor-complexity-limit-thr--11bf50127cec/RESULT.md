# An aperiodic word with reflection-to-factor complexity limit three quarters

## Finding

There exists a right-infinite **aperiodic** word \(x\) over a fixed alphabet of thirteen symbols for which the reflection complexity \(r_x(n)\) and ordinary factor complexity \(C_x(n)\) satisfy

\[
C_x(n)=6\cdot2^n+O(n^2),\qquad
r_x(n)=\frac92\,2^n+O(2^{n/2}+n^2),\qquad
\lim_{n\to\infty}\frac{r_x(n)}{C_x(n)}=\frac34.
\]

Thus *aperiodicity alone* does not enforce the dichotomy \(\{\frac12,1\}\) proposed for the asymptotic reflection-to-factor complexity ratio. This addresses the aperiodic formulation stated as Conjecture 35 in Blažek–Dvořáková–Pelantová (2026), which restates the repair of Conjecture 29 discussed by Dvořáková–Pelantová (2026). The example is **not recurrent** and does not challenge known uniformly recurrent or reversal-closed cases.

## Assumptions and scope

For a right-infinite word \(x\), write \(L_n(x)\) for its distinct contiguous length-\(n\) factors. Define \(C_x(n)=|L_n(x)|\). Words \(u,v\in L_n(x)\) are reflectively equivalent when \(u=v\) or \(u\) is the reversal of \(v\). Let \(r_x(n)\) be the number of equivalence classes meeting \(L_n(x)\). Aperiodic means *not eventually periodic*.

Let the alphabet be the disjoint union of \(\{a,b\},\{c,d\},\{e,f\},\{g,h\},\{i,j\},\{k,l\},\{\#\}\). The first three pairs are three independent full-binary components. The last three pairs represent phases \(0,1,2\) of one directed ternary-phase component.

For each positive integer \(t\), choose the standard lexicographically generated cyclic binary de Bruijn sequence \(d_t\) of order \(t\), with length \(2^t\). Its cyclic length-\(t\) factors are all \(2^t\) binary words exactly once. Let \(d_t^{\langle t-1\rangle}\) denote the first \(t-1\) bits of \(d_t\); it is empty if \(t=1\).

Define \(W_{s,t}\) for \(s=0,1,2\) by encoding the binary string

\[0^t\,d_t\,d_t^{\langle t-1\rangle}\,0^t\]

in the \(s\)-th letter pair, translating bits \(0,1\) to \(a,b\), \(c,d\), or \(e,f\), respectively.

To define \(V_t\), put \(p_t=3\lceil t/3\rceil\), \(H_t=d_t d_t d_t\,d_t^{\langle t-1\rangle}\), and

\[q_t=p_t+\bigl(-|H_t|\bmod3\bigr),\qquad z_t=0^{p_t}H_t0^{q_t}.\]

In \(z_t\), encode bit \(b\) at zero-based position \(j\) using the \(b\)-letter from the phase pair \(\{g,h\}\), \(\{i,j\}\), or \(\{k,l\}\), according as \(j\bmod3=0,1,2\). Denote the resulting word by \(V_t\). Its length is divisible by three and both end padding regions contain at least \(t\) zeros, with phase positions fixed relative to the respective endpoints.

Finally set the right-infinite word to the explicit concatenation

\[
x=\prod_{t=1}^{\infty}\left(W_{0,t}\,\#^t\,W_{1,t}\,\#^t\,W_{2,t}\,\#^t\,V_t\,\#^t\right).
\]

The encoding uses thirteen distinct symbols regardless of \(t\), and each displayed block is finite and nonempty.

## Proof

**1. Aperiodicity.** The word has arbitrarily long runs of \(\#\) because the separators at stage \(t\) have length \(t\). It also has infinitely many symbols other than \(\#\). An eventually periodic word with arbitrarily long runs of one letter must be eventually constant in that letter: a nonconstant periodic tail has bounded same-letter run lengths. Thus \(x\) is not eventually periodic. In fact it is not recurrent: the factor `a#c` appears exactly once, crossing the length-one separator from \(W_{0,1}\) to \(W_{1,1}\); every later separator has length at least two, and all other separators have different neighboring alphabets.

**2. Exact unmarked factors.** Fix \(n\ge2\). An unmarked length-\(n\) factor avoids \(\#\) and hence lies wholly in one of the six disjoint letter-pair components. It cannot cross component blocks because a separator intervenes.

Each of the three \(W\) components contains every binary length-\(n\) word: use stage \(t=n\), where the de Bruijn cycle plus its first \(n-1\) symbols linearizes all its cyclic length-\(n\) factors. Thus each yields exactly \(2^n\) factors, with pairwise-disjoint alphabets.

Every unmarked length-\(n\) factor in \(V_t\) advances one phase modulo three at each letter. There are exactly \(3\cdot2^n\) possible phase-compatible words. All occur in \(V_n\): for any binary length-\(n\) word \(w\), find its cyclic starting offset \(r\in\{0,\ldots,2^n-1\}\) in \(d_n\). Inside three consecutive copies of \(d_n\), \(w\) occurs at starts \(r\), \(r+2^n\), and \(r+2\cdot2^n\). The length-\(n-1\) copied prefix handles wraparound at the last occurrence. As \(2^n\) is relatively prime to three, these starts represent all three phases. The initial pad is divisible by three. Consequently, the unmarked factor count is exactly

\[
U_n=3\cdot2^n+3\cdot2^n=6\cdot2^n.
\]

**3. Reflection classes of unmarked factors.** Within each binary full-shift component, reversal pairs all nonpalindromes and fixes exactly \(2^{\lceil n/2\rceil}\) palindromes. Thus each contributes \((2^n+2^{\lceil n/2\rceil})/2\) reflection classes.

A phase-compatible word in the directed component has successive phases \(s,s+1,\ldots\pmod3\). Its reversal would begin with phases \(s+n-1,s+n-2\pmod3\), and these decrease by one rather than increase by one. As \(n\ge2\) and \(1\not\equiv-1\pmod3\), no reversed length-\(n\) directed word occurs in the directed component. Nor can it occur in a different component, whose alphabet is disjoint. Hence its \(3\cdot2^n\) factors represent \(3\cdot2^n\) separate reflection classes. Different components never merge under reversal. The exact number of unmarked reflection classes is therefore

\[
T_n=3\frac{2^n+2^{\lceil n/2\rceil}}2+3\cdot2^n
=\frac92\,2^n+\frac32\,2^{\lceil n/2\rceil}.
\]

**4. Marked factors contribute only polynomially.** Let \(E_n\) be the number of distinct length-\(n\) factors containing at least one \(\#\). First consider separators at stages \(t<n\). There are exactly \(4(n-1)\) such separators. A separator of length \(t<n\) can meet fewer than \(n+t\le2n\) starting positions of length-\(n\) factors. Therefore at most \(8n(n-1)\) distinct factors meeting any short separator exist.

At stages \(t\ge n\), every separator has length at least \(n\). A length-\(n\) factor cannot span such a separator. If it meets both a separator and an adjacent component, it consists of a nonempty piece of separator and a nonempty piece of at most one adjacent component. Every component begins and ends with at least \(n\) zero-bit positions in a fixed encoding: for \(W\) this is the repeated zero letter; for \(V\) it is a periodic phase pattern with phase fixed relative to both ends because \(|V_t|\equiv0\pmod3\). There are only four possible component types on each side, hence at most eight boundary templates, each permitting at most \(n-1\) splits. The all-separator factor adds one. This gives the explicit bound

\[
0\le E_n\le8n(n-1)+8(n-1)+1=8n^2-7<8n^2+1.
\]

Let \(F_n\) be the number of reflection classes represented by marked factors. Reversal preserves whether a factor contains \(\#\), so none of these classes merges with an unmarked class and \(0\le F_n\le E_n\). Therefore

\[
C_x(n)=U_n+E_n=6\cdot2^n+O(n^2),
\]

\[
r_x(n)=T_n+F_n=\frac92\,2^n+O(2^{n/2}+n^2).
\]

Division by \(6\cdot2^n\) and passage to the limit yield \(3/4\). This completes the infinite proof.

## Verification

The accompanying standalone `verify.py` generates cyclic de Bruijn words using the Lyndon-word algorithm, constructs finite prefixes through stage \(n+2\), enumerates every distinct length-\(n\) factor and its reversal equivalence class, and checks the two *exact* unmarked formulas for \(2\le n\le9\). The computed counts are reproduced in `check_output.txt`. In particular, at length nine, \(3072\) unmarked factors form exactly \(2352\) unmarked reflection classes, matching the proof; marker-containing factors are counted separately.

The finite computation checks implementation details and is not used to infer an infinite identity. The infinite theorem follows from the exhaustive analytic description of the unmarked languages and the polynomial bound on marked factors.

## Relationship to prior work

Allouche, Campbell, Li, Shallit, and Stipulanti introduced reflection complexity, posed Conjecture 29, and proved results for special classes; in their paper, the uniformly recurrent case has a strong reversal-versus-nonreversal dichotomy. Dvořáková and Pelantová (first publicly posted 15 November 2025) observed that the original conjecture fails for periodic words, cited the periodic ratio \(2/3\), and discussed an aperiodicity repair. Blažek, Dvořáková, and Pelantová (posted 10 October 2026) formulated the aperiodic version explicitly as Conjecture 35 and proved analogous results for a larger symmetry group under additional hypotheses.

Their conjectures do not present an aperiodic word realizing \(3/4\). The construction here has positive-entropy language components and an unbounded-length separator mechanism; its language is neither recurrent nor reversal-closed. Therefore it does not contradict published uniform-recurrence or reversal-closed positive cases. Unlike the known periodic \(2/3\) counterexample, it satisfies the precise aperiodicity requirement of the later conjecture.

## Limitations

The word uses thirteen symbols, has exponential factor complexity, and is not recurrent. This result does not settle whether the proposed dichotomy holds for recurrent words, for binary or other small fixed alphabets, or under additional dynamical hypotheses. The asymptotic error bounds are explicit but not optimized. A literature search and self-review do not replace independent mathematical validation; differently phrased earlier constructions may exist.

## References

1. L. Dvořáková and E. Pelantová, *Reflection on the reflection complexity*, arXiv:2511.12358 (first posted 2025-11-15), Section 6; open-access journal version, *Theory of Computing Systems* 70 (2026), article 35. https://arxiv.org/abs/2511.12358 ; https://doi.org/10.1007/s00224-026-10278-7
2. A. Blažek, L. Dvořáková, and E. Pelantová, *Generalized reflection complexity*, arXiv:2610.14637 (first posted 2026-10-10), Section 6.3, Conjecture 35. https://arxiv.org/abs/2610.14637
3. J.-P. Allouche, J. M. Campbell, S. Li, J. Shallit, and M. Stipulanti, *The reflection complexity of sequences over finite alphabets*, arXiv:2406.09302 (first posted 2024-06-13), original Conjecture 29 and uniformly recurrent results. https://arxiv.org/abs/2406.09302

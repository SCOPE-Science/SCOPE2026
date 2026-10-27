# Infinite four-pseudoperiod family and shift-64 census for the Rudin–Shapiro word

## Finding
Let \(r\colon\mathbb N_0\to\{0,1\}\) be the Rudin–Shapiro word: \(r(n)\) is the parity of the number of occurrences (overlaps allowed) of `11` in the ordinary binary expansion of \(n\). Four positive, strictly increasing integers \(a<b<c<d\) constitute a *four-pseudoperiod* when
\[
\forall n\ge0,\qquad r(n)\in\{r(n+a),r(n+b),r(n+c),r(n+d)\}.
\]

**Theorem.** (i) For every integer \(m\ge1\), the tuple
\[
\boxed{(1,8m-1,8m,8m+1)}
\]
is a four-pseudoperiod of \(r\). (ii) Among all \(\binom{64}{4}=635376\) tuples \(1\le a<b<c<d\le64\), exactly **24** are four-pseudoperiods, and they are exactly the tuples listed in `census.tsv`. The unique one with largest shift at most five is \((2,3,4,5)\). The complete finite list includes seven members of the family in (i).

## Assumptions and scope
The indexing begins at \(n=0\) and equality is of binary symbols, not of signed Rudin–Shapiro coefficients (equivalently, the signed coefficients may be substituted because coding is injective). The universal quantifier ranges over the *infinite* fixed word. The census imposes an inclusive maximum shift of \(64\), and does not use finite-prefix pseudoperiodicity as a substitute for the infinite condition.

## Proof
Write \(\oplus\) for exclusive-or. Counting adjacent `11` pairs on binary input gives
\[
r(2t)=r(t),\qquad r(2t+1)=r(t)\oplus(t\bmod2),
\]
and hence, for all \(t\ge0\),
\[
\begin{aligned}
r(4t)&=r(4t+1)=r(t),\\
r(4t+2)&=r(t)\oplus(t\bmod2),\\
r(4t+3)&=r(t)\oplus(t\bmod2)\oplus1.
\end{aligned}
\tag{1}
\]

To prove (i), put \(Q=8m\), so \(Q=4s\) with \(s=2m\) even, and fix \(n=4t+j\). If \(j=0\), the shift \(1\) matches by (1). If \(j=1\) and \(t\) is even, shift \(1\) again matches. If \(j=1\) and \(t\) is odd, the values at shifts \(Q\) and \(Q+1\) are respectively \(r(t+s)\) and \(r(t+s)\oplus1\), because \(t+s\) is odd. If \(j=2\), the values at shifts \(Q\) and \(Q+1\) are respectively \(r(4(t+s)+2)\) and \(r(4(t+s)+3)\), which are complementary. If \(j=3\), those at shifts \(Q-1\) and \(Q\) are respectively \(r(4(t+s)+2)\) and \(r(4(t+s)+3)\), again complementary. In each case either shift \(1\) already matches \(r(n)\) or a displayed pair is complementary, forcing one of its binary values to match \(r(n)\). This proves (i) for every \(m\ge1\) and every \(n\ge0\).

For (ii), introduce a four-letter alphabet with states \(A=(0,0)\), \(B=(0,1)\), \(C=(1,1)\), \(D=(1,0)\); the coordinates denote \((r(n),n\bmod2)\). The recurrence above implies the length-two substitution
\[
\sigma(A)=AB,\quad\sigma(B)=AC,\quad\sigma(C)=DB,\quad\sigma(D)=DC
\]
and the output coding \(\tau(A)=\tau(B)=0\), \(\tau(C)=\tau(D)=1\). Indeed, from each state \((r(n),n\bmod2)\), the two substituted states encode the corresponding states at indices \(2n\) and \(2n+1\); induction proves \(r=\tau(\sigma^{\omega}(A))\).

Let \(U=\sigma^{10}(A)\), of length \(1024\), and let \(F\) be the set of its length-\(65\) factors. Exact enumeration gives \(|F|=512\) and the *closure certificate*
\[
\bigcup_{v\in F}\operatorname{Fac}_{65}(\sigma(v))\subseteq F.
\tag{2}
\]
The inclusion is verified by \(512\cdot66=33792\) substring-membership checks in `verify.py`. It implies by induction that every length-\(65\) factor of every later iterate belongs to \(F\): a length-\(65\) window of a substituted word spans at most \(33\) source letters, which can be extended to a length-\(65\) source factor since each iterate has at least \(65\) letters. Conversely, \(U\) is a prefix of the infinite fixed point, so every factor in \(F\) actually occurs in it. Hence \(F\) is *exactly* its full length-\(65\) factor set, not merely a sample. Its coded image \(\tau(F)\) contains exactly \(512\) binary factors and is the complete length-\(65\) factor set of \(r\).

For each \(f\in\tau(F)\) define the matching-shift set \(E(f)=\{j\in\{1,\ldots,64\}:f_0=f_j\}\). A quadruple with maximum shift \(\le64\) is a pseudoperiod if and only if it intersects \(E(f)\) for **every** \(f\in\tau(F)\). The exact standard-library enumeration in `verify.py` loops over all \(635376\) tuples, representing each shift's matching factors by a bitset, and retains precisely the 24 tuples of `census.tsv`. This finite exhaustive check, combined with (2), proves the classification for all indices of the infinite word.

## Verification
Run `python3 verify.py` with Python 3. The program verifies the substitution state model against the independent binary-digit definition, the complete-factor closure, all \(635376\) four-shift candidates, and the exact 24-tuple list. It also independently performs a non-bitset brute-force comparison of all \(\binom{32}{4}=35960\) tuples through shift 32, obtaining nine pseudoperiods, and tests the infinite family on finite sample ranges. The infinite family is proved by the symbolic residue argument, not by its samples. The finite classification is exhaustive because the length-\(65\) factor language is proved complete.

Expected terminal prefix: `RUDIN_SHAPIRO_FOUR_PSEUDOPERIOD_PASS`.

## Relationship to prior work
Meleshko, Ochem, Shallit, and Shan established that the Rudin–Shapiro sequence is four-pseudoperiodic but not three-pseudoperiodic, giving \((2,3,4,5)\) as a witness (Theorem 28 of [1]). Their result does not list the four-pseudoperiods through a finite shift bound or state the unbounded arithmetic family above. The general decidability framework for automatic sequences in [1] supplies a method in principle, not the explicit classification or symbolic family. Rampersad and Shallit [2] develop automata for Rudin–Shapiro *summatory functions*; their object and claims differ from pseudoperiod classifications. The single previously reported witness is included, not presented as novel.

## Limitations
The all-shift classification of Rudin–Shapiro four-pseudoperiods is not established here. The exact census applies only to largest shift at most \(64\); beyond that range the proof guarantees the displayed arithmetic family but makes no completeness claim. No asymptotic count of all valid quadruples is asserted.

## References
[1] J. Meleshko, P. Ochem, J. Shallit, and S. L. Shan, *Pseudoperiodic Words and a Question of Shevelev*, first arXiv posting 2022-07-20, arXiv:2207.10171, published in Discrete Mathematics & Theoretical Computer Science 25:2 (2023), DOI 10.46298/dmtcs.9919. https://arxiv.org/abs/2207.10171

[2] N. Rampersad and J. Shallit, *Rudin-Shapiro Sums Via Automata Theory and Logic*, Theory of Computing Systems 69:9 (2025), DOI 10.1007/s00224-025-10214-1. https://doi.org/10.1007/s00224-025-10214-1

# Exact state complexity and residual classification for a fixed scattered-pair count

## Finding

For every integer \(k\ge1\), let \(N_{01}(w)\) be the number of pairs of indices \(i<j\) in a finite binary word \(w\) with \(w_i=0\) and \(w_j=1\). The minimal **complete** deterministic finite automaton recognizing
\[
E_k=\{w\in\{0,1\}^{*}:N_{01}(w)=k\}
\]
has exactly
\[
\boxed{\operatorname{sc}(E_k)=\left\lfloor k^{2}/4\right\rfloor+\left\lceil k/2\right\rceil+3}
\]
states. In addition, all Myhill–Nerode residuals are explicitly classified below. The exact-count condition, unlike an occurrence-threshold condition, distinguishes a new family of one-further-one residuals from those allowing two or more ones.

## Assumptions and scope

The input alphabet is precisely \(\{0,1\}\), the count concerns **scattered** copies of \(01\), and \(k\) is any positive integer, without a bound on input length. The empty word and arbitrary leading ones are allowed. A complete automaton includes a rejecting sink. For a prefix \(u\), put \(q=|u|_0\), \(r=N_{01}(u)\) and, when \(r<k\), \(t=k-r\). The residual of \(u\) is \(u^{-1}E_k=\{v:uv\in E_k\}\). Distinct residuals are exactly the states of the minimal complete DFA.

## Proof

**1. Exact continuation identity.** Every \(01\)-pair in \(uv\) lies in \(u\), lies in \(v\), or has its zero in \(u\) and its one in \(v\). Thus, for every pair of binary words,
\[
N_{01}(uv)=r+q|v|_1+N_{01}(v).
\tag{1}
\]
Consequently, the residual condition is \(q|v|_1+N_{01}(v)=t\), provided \(r\le k\). The three exceptional residuals are: the initial residual \(E_k\) whenever \(q=0\) (necessarily \(r=0\)); the residual \(0^*\) if \(r=k\) and \(q\ge1\); and the empty residual if \(r>k\) or \(r<k\) and \(q>t\). The last assertion holds because zero suffix-ones increase the count by zero, while at least one suffix-one increases it by at least \(q>t\).

**2. Every other residual falls into precisely two types.** Assume \(r<k\) and \(1\le q\le t\). If \(2q>t\), a completing suffix cannot contain two ones. It must have precisely one, with exactly \(d=t-q\) preceding zeros. Therefore its residual is the **single-one type**
\[
R_d=0^d1\,0^*, \qquad d=t-q\ge0.
\tag{2}
\]
If \(2q\le t\), the residual is the **multiple-one type**
\[
Q_{q,t}=\{v:N_{01}(v)+q|v|_1=t\},\quad
1\le q\le\lfloor t/2\rfloor,\quad 1\le t\le k.
\tag{3}
\]
Every pair in (3) is reachable: the prefix \(0\,1^{k-t}0^{q-1}\) has precisely \(q\) zeros and \(k-t\) occurrences of \(01\). Every \(R_d\) with \(0\le d\le\lfloor(k-1)/2\rfloor\) is reachable by taking \(t=2d+1\), \(q=d+1\), and the same prefix construction. The initial, \(0^*\), and empty residuals are reached by \(\varepsilon\), \(01^k\), and \(01^{k+1}\), respectively. No larger \(d\) occurs because \(q\le t<2q\) implies \(d=t-q<q\) and hence \(2d<t\le k\).

**3. Distinguishing all residuals.** Every nonempty residual in (2) or (3) has a completing suffix \(0^{t-q}1\) with exactly one one. Thus none equals the empty residual or \(0^*\), and \(0^*\) alone contains the empty suffix \(\varepsilon\). The suffix \(01^k\) belongs to the initial residual \(E_k\), but belongs to none of the active types: since \(q\ge1\), its increase in (1) is \(k(q+1)>t\).

For both active types, exactly one-one suffixes are allowed precisely when they have \(d=t-q\) leading zeros. Hence classes with different \(d\) are distinguished by \(0^d1\). For the same \(d\), each multiple-one type \(Q_{q,t}\) accepts the two-one suffix \(1\,0^{t-2q}1\), which no \(R_d\) accepts. Two multiple-one types \(Q_{q,t}\) and \(Q_{q',t'}\) with the same \(d=t-q=t'-q'\) but \(q\ne q'\) are distinguished by \(1\,0^{t-2q}1\): its counted increment for \(Q_{q',t'}\) differs from \(t'\) by \(q'-q\ne0\). Thus all listed residuals are distinct.

**4. Counting.** The single-one indices are exactly \(d=0,\ldots,\lfloor(k-1)/2\rfloor\), giving \(\lceil k/2\rceil\) states. The multiple-one indices number
\[
\sum_{t=1}^{k}\left\lfloor\frac{t}{2}\right\rfloor
=\left\lfloor\frac{k^2}{4}\right\rfloor.
\]
Adding the three exceptional residuals proves the formula. In particular, \(k=1\) gives four states; no unmentioned boundary state is required.

## Verification

The standalone Python file `verify_exact01.py` constructs, for each \(1\le k\le60\), a reachable saturated-counter DFA tracking zero counts and scattered-pair counts; it then independently minimizes that complete automaton by iterative right-transition partition refinement. The minimized sizes agree with the formula for all 60 thresholds. It also verifies that every raw state maps to exactly one listed residual type and that these types coincide with minimized state classes. Additionally, direct index-count evaluations for all binary words of lengths \(0\) through \(11\) independently verify the counter transitions for thresholds \(1\) through \(6\). The exact general theorem follows from the proof, not the finite experiment. Run with `python3 verify_exact01.py` using only the Python standard library.

## Relationship to prior work

Mansour, Rastegar, and Roitershtein (2019), Section 2.2, construct finite automata for bounded counts of scattered word patterns. Their equivalence (4) compares all continuation counts \(0,\ldots,r\) simultaneously. It is finer than the single-membership Myhill–Nerode relation for the **exactly** \(k\)-occurrences language here: specifically, suffix behavior for wrong counts below \(k\) may be merged. Their general automata are a valuable starting point but the inspected paper does not give formula (4) of this note or classify the minimal exact-count quotient for binary \(01\). Leroy, Rigo, and Stipulanti (2017) study binomial coefficients of words and generalized Pascal arrays; Renard, Rigo, and Whiteland (2024) develop \(q\)-deformed versions and Parikh matrices. These motivate counting scattered patterns but neither inspected text gives this finite-automaton quotient. Renard, Rigo, and Whiteland (2024), in a separate article, also display a minimal automaton for the congruence language of a deformed word-binomial coefficient modulo a polynomial; such a finite-field congruence does not test equality to an unbounded integer parameter. No claim is made about other occurrence patterns or larger alphabets.

## Limitations

Novelty is assessed against the inspected primary literature and available searchable records, not an exhaustive index of all published work. An equivalent theorem might be present in an unindexed source or derived from a general automaton-minimization construction. The proof supplies the exact state count and residual characterization only for the binary scattered pattern \(01\) and positive integral \(k\). Computational checks cover only finitely many \(k\).

## References

1. J. Leroy, M. Rigo, M. Stipulanti, *Generalized Pascal triangle for binomial coefficients of words*, preprint first posted 2017-05-23, https://arxiv.org/abs/1705.08270.
2. T. Mansour, R. Rastegar, A. Roitershtein, *Finite automata, probabilistic method, and occurrence enumeration of a pattern in words and permutations*, preprint first posted 2019-05-14, https://arxiv.org/abs/1905.05646, especially Section 2.2.
3. A. Renard, M. Rigo, M. A. Whiteland, *q-Parikh Matrices and q-deformed binomial coefficients of words*, preprint first posted 2024-02-08, https://arxiv.org/abs/2402.05657.
4. A. Renard, M. Rigo, M. A. Whiteland, *Introducing q-deformed binomial coefficients of words*, preprint first posted 2024-02-08, https://arxiv.org/abs/2402.05838, especially Section 6.2.

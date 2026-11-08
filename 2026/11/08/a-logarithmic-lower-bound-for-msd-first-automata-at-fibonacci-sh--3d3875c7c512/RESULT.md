# A logarithmic lower bound for MSD-first automata at Fibonacci shifts

## Finding
Let \(F_0=0\), \(F_1=1\), \(F_{j+1}=F_j+F_{j-1}\), and let \(f=0100101001001\cdots\) be the infinite Fibonacci word, fixed by \(0\mapsto01\) and \(1\mapsto0\). For each integer \(k\ge4\), define the shifted sequence \(g_k(n)=f(n+F_k)\). Let \(s_k\) denote the minimum number of states of an MSD-first deterministic finite automaton with output (DFAO) that computes \(g_k\) on valid canonical Zeckendorf representations.

For every integer \(k\ge4\),
\[
\min\{n\ge0:f(n+F_k)\ne f(n)\}=F_{k+1}-2.
\]
Moreover,
\[
 s_k\ge\left\lceil\frac{k}{8}\right\rceil.
\]
Combined with the known MSD-first \(O(\log c)\) upper bound of Moradi, Popoli, Shallit, and Vukusic, this gives \(s_k=\Theta(k)=\Theta(\log F_k)\). In particular the logarithmic MSD-first upper bound is attained in order along the Fibonacci shifts.

## Assumptions and scope
The number \(n\ge1\) is written as its unique Zeckendorf digit string \((n)_F\), most significant digit first, using positions with weights \(F_j\) for \(j\ge2\), without adjacent ones or leading zeros. The representation of zero may be \(0\). A DFAO's outputs must be correct on these canonical inputs; the bound therefore applies also to the more restrictive model requiring correct behavior under arbitrary leading-zero padding. Invalid strings are irrelevant. This is a statement about deterministic MSD-first machines, not minimal LSD-first machines.

## Proof
**Finite-word near-commutation.** Define \(W_2=0\), \(W_3=01\), and \(W_j=W_{j-1}W_{j-2}\) for \(j\ge4\). Then \(|W_j|=F_j\), and every \(W_j\) is a prefix of \(f\). For all \(j\ge3\), the two words \(W_jW_{j-1}\) and \(W_{j-1}W_j\) agree at their first \(F_{j+1}-2\) positions and have different final two symbols. For \(j=3\) they are \(010\) and \(001\), which proves the base case. For the induction step use
\[
 W_jW_{j-1}=W_{j-1}(W_{j-2}W_{j-1}),\qquad
 W_{j-1}W_j=W_{j-1}(W_{j-1}W_{j-2}).
\]
The parenthesized pair is the pair at index \(j-1\), in reversed order. Prepending the same \(W_{j-1}\) preserves the property of differing in exactly their last two positions. This establishes the claim by induction, including the last-two-symbol mismatch.

**First shifted disagreement.** Because \(W_{k+2}=W_kW_{k-1}W_k\), the first \(F_{k+1}\) positions of \(f\) equal \(W_kW_{k-1}\), while the \(F_{k+1}\) positions starting at offset \(F_k\) equal \(W_{k-1}W_k\). By near-commutation, the sequences \(f(n)\) and \(f(n+F_k)\) coincide for \(0\le n<F_{k+1}-2\) and disagree at \(n=F_{k+1}-2\). This proves the exact first-disagreement identity, not merely a finite observed bound.

**Encoding length.** Let \(N=F_{k+1}-2\). For \(k\ge4\), \(F_k\le N<F_{k+1}\). Thus the largest Zeckendorf weight appearing in \((N)_F\) is \(F_k\), and \((N)_F\) has exactly \(k-1\) digits. No positive integer with a shorter canonical representation can be a disagreement, by the preceding paragraph. Zero is not a disagreement, either, because \(f(0)=f(F_k)=0\) for \(k\ge4\).

**Automaton lower bound.** Suppose an MSD-first DFAO \(A\) for \(g_k\) has \(s\) states. The unshifted Fibonacci word has a two-state MSD-first DFAO \(B\), since \(f(n)\) is the last digit of \((n)_F\): the state records the most recently read digit, and its output is that digit. A complete four-state DFA \(V\) recognizes the regular language of positive canonical Zeckendorf representations: one start state, two states remembering a valid last digit, and one rejecting dead state. Take the direct product \(A\times B\times V\), with no more than \(8s\) states, and accept exactly when \(V\) accepts and the outputs of \(A\) and \(B\) disagree. If \(A\) was only specified on canonical inputs, arbitrarily complete its transitions elsewhere; the validity component prevents invalid words from affecting this language.

The product recognizes a nonempty regular language with shortest accepted word of length exactly \(k-1\). A deterministic finite automaton accepting a nonempty language whose shortest word has length \(\ell\) needs at least \(\ell+1\) states: the states seen after the \(\ell+1\) successive prefixes of a shortest accepted word must be distinct, because an equal pair could be removed to yield a shorter accepted word. Therefore \(8s\ge k\), or \(s\ge\lceil k/8\rceil\).

**Upper bound.** Theorem 4.1 of Moradi–Popoli–Shallit–Vukusic supplies MSD-first DFAOs of \(O(\log c)\) states for the \(c\)-shift of \(f\). Set \(c=F_k\) and use exponential growth of Fibonacci numbers to obtain \(s_k=O(k)\). Together with the proved lower bound this establishes the final asymptotic assertion.

## Verification
Run \(\texttt{python3 verify.py}\) using Python 3 and no external dependencies. The script builds an independent morphic prefix, compares the first disagreement for \(4\le k\le20\), verifies Zeckendorf lengths and the near-commutation identity, and checks 25,000 values against independently computed canonical final digits. These finite tests guard arithmetic and indexing only; the infinite assertions follow from the induction and automaton argument above.

## Relationship to prior work
Moradi, Popoli, Shallit, and Vukusic (arXiv:2603.18858v1, March 19, 2026) prove a logarithmic MSD-first state **upper** bound in Theorem 4.1, and give an exact **LSD-first** state formula in Theorem 3.2. Neither result states an MSD-first lower bound at the Fibonacci shifts. Their introduction also discusses a weaker general counting lower bound along unspecified shifts, which does not imply a linear-in-\(k\) lower bound specifically at \(F_k\). Moradi, Rampersad, and Shallit (arXiv:2603.21645v1, March 23, 2026) provide other arithmetic and shift constructions and upper bounds, not this sharp-family lower bound. The elementary almost-commutation of finite Fibonacci words is classical; the contribution here is its quantitative connection to minimal MSD-first shift automata through the first-disagreement language.

## Limitations
The bound \(\lceil k/8\rceil\) is not an exact state count and the constant may be improvable. The \(\Theta(\log c)\) conclusion is established along \(c=F_k\), not for every shift. The proof does not provide a lower bound for nondeterministic automata, or a new LSD-first formula. No claim of exclusive historical priority or independent validation is made.

## References
1. D. Moradi, P. Popoli, J. Shallit, and I. Vukusic, *State Complexity of Shifts of the Fibonacci Word*, arXiv:2603.18858v1 (first publicly posted 2026-03-19), https://arxiv.org/html/2603.18858v1. In particular Definition 2, Theorems 3.2 and 4.1.
2. D. Moradi, N. Rampersad, and J. Shallit, *Complexity of Linear Subsequences of Fibonacci-Automatic Sequences*, arXiv:2603.21645v1 (first publicly posted 2026-03-23), https://arxiv.org/html/2603.21645v1. Background on representation and shifts.

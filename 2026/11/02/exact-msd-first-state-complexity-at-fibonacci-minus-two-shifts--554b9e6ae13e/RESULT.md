# Exact MSD-first state complexity at Fibonacci-minus-two shifts

## Finding
Let \(F_0=0\), \(F_1=1\), and \(F_{j+2}=F_{j+1}+F_j\). Let \(f=0100101001001\cdots\) be the infinite Fibonacci word, indexed from zero, and put \(c_k=F_k-2\). For every integer \(k\ge5\), the **minimum number of states** of a deterministic finite automaton with output (DFAO) reading valid Zeckendorf representations most-significant-digit first and returning \(f(n+c_k)\) is **exactly \(k\)**. Leading zeroes may be accepted without changing the value. No claim is made here for other shifts.

## Assumptions and scope
A valid Zeckendorf representation is a binary string with no consecutive ones and numerical value \(\sum_{i\ge2} a_iF_i\), its rightmost digit corresponding to \(F_2=1\). The empty word and leading zeroes may represent zero. The DFAO must be correct on every valid input, with no required behavior on invalid representations. The count concerns the minimal accessible DFAO states under this convention, not states of a specific construction.

Write \(\varphi=(1+\sqrt5)/2\), \(\gamma=\varphi^{-2}=2-\varphi\), and let \(\{x\}\) denote the fractional part. The Fibonacci-word rotation criterion is
\[f(n)=1\quad\Longleftrightarrow\quad \{n\varphi\}\in(\gamma,2\gamma),\qquad n\ge0.\]
The exact endpoints cannot occur for nonnegative \(n\), since they correspond to negative integer multiples of the irrational \(\varphi\).

## Proof
**Upper bound.** Moradi--Popoli--Shallit--Vukusic, arXiv:2603.18858v1, Definition 3, Lemma 5, and proof of Theorem 3, construct an MSD-first DFAO with one state for each interval cut out by the union of the two finite endpoint chains associated with the negative integers \(-c-1\) and \(-c-2\). This follows from the proved consistency of their interval partitions under valid Zeckendorf digit appending; the output interval is bounded by those two endpoints.

For \(c=F_k-2\), the two negative integers are \(-(F_k-1)=-F_k+F_2\) and \(-F_k\). Applying the stated negative-representation right-shift rule, their endpoint chains are respectively
\[ -(F_k-1),\ -F_{k-1},\ -F_{k-2},\ldots,-F_2\]
and
\[-F_k,\ -F_{k-1},\ -F_{k-2},\ldots,-F_2.\]
The union contains precisely \(k\) distinct integer indices. Since \(\varphi\) is irrational, their fractional-part endpoints are distinct, giving exactly \(k\) circular intervals. The cited construction therefore supplies a valid DFAO with at most \(k\) states. This step uses the published interval-consistency lemma; it does not assume that the published construction is minimal.

**A rotation computation.** The classical identity
\[F_t\varphi-F_{t+1}=(-1)^{t+1}\varphi^{-t}\]
holds for every \(t\ge2\). Set \(\eta=\varphi^{-k}\). Consequently, modulo one,
\[\{(F_k-2+F_t)\varphi\}=\{2\gamma+(-1)^{k+1}\eta+(-1)^{t+1}\varphi^{-t}\}.\]
Checking the position relative to \((\gamma,2\gamma)\) gives, for every integer \(t\ge2\):
\[ f(F_k-2+F_t)=\begin{cases}
1,&k\text{ odd},\ t\text{ even},\ 2\le t<k,\\
0,&k\text{ odd},\ \text{otherwise},\\
0,&k\text{ even},\ t=2\text{ or }(3\le t<k\text{ odd}),\\
1,&k\text{ even},\ \text{otherwise}.
\end{cases}\tag{1}\]
For completeness, when \(k\) is odd the perturbation \(+\eta\) places the unmodified point immediately above the right endpoint; an even-index perturbation \(-\varphi^{-t}\) moves it into the interval precisely for \(t<k\), including \(t=2\), whereas an odd-index perturbation stays outside (possibly wrapping below \(\gamma\) when \(t=3\)). When \(k\) is even the perturbation is \(-\eta\); odd \(t<k\) moves outside, even \(t\ge4\) stays inside, and all \(t\ge k\) stay inside. The sole exceptional index is \(t=2\), where the point is \(\gamma-\eta\).

Now define \(q_k=F_4+F_2=4\) for odd \(k\) and \(q_k=F_5+F_2=6\) for even \(k\). Write \(S_j(n)\) for the integer obtained by appending \(j\) zero digits to a valid Zeckendorf expansion of \(n\). Thus \(S_j(F_i)=F_{i+j}\), while
\[ S_j(q_k)=\begin{cases}F_{j+4}+F_{j+2},&k\text{ odd},\\F_{j+5}+F_{j+2},&k\text{ even}.\end{cases}\]
A second application of the same rotation identity yields
\[f(c_k+S_j(q_k))=f(c_k+F_{j+2})\qquad(j\ge1),\tag{2}\]
but the two values are opposite at \(j=0\): \(f(c_k+q_k)=0\ne1=f(c_k+F_2)\) for odd \(k\), and \(f(c_k+q_k)=1\ne0=f(c_k+F_2)\) for even \(k\).

Here are explicit strict inequalities supporting (2), rather than an appeal to finite experimentation. Put \(t=j+2\ge3\). For odd \(k\), the extra \(F_{t+2}\) changes the signed perturbation \((-1)^{t+1}\varphi^{-t}\) into \((-1)^{t+1}(1+\gamma)\varphi^{-t}\). For even \(t\), \((1+\gamma)\varphi^{-t}>\eta\) exactly when \(t<k\), within the parity-permitted values, since \(1+\gamma<\varphi\), and the maximal downward displacement at \(t=4\) is less than \(\gamma\). For odd \(t\), both perturbed points are above \(2\gamma\) or, only at \(t=3\), wrap to below \(\gamma\). For even \(k\), the extra \(F_{t+3}\) changes the signed perturbation into \((-1)^{t+1}(1-\varphi^{-3})\varphi^{-t}\). Even \(t\ge4\) stays in the interval because \(\varphi^{-6}+\varphi^{-4}<\gamma\). For odd \(t\), the new point is above \(2\gamma\) exactly when \(t<k\), because \(\varphi(1-\varphi^{-3})>1\); at \(t>k\), both points are inside. This proves (2) in all cases.

**Lower bound.** Consider the \(k\) distinct valid MSD-first input prefixes representing
\[0,\ F_2,F_3,\ldots,F_{k-1},\ q_k.\]
For each prefix, append \(j\) zeroes, where \(j\) can be any nonnegative integer. Set \(b_k=0\) when \(k\) is odd and \(b_k=1\) when \(k\) is even. The prefix for zero gives the constant output \(b_k\). By (1), for every \(2\le i\le k-1\), the output sequence for prefix \(F_i\) has **last** disagreement with \(b_k\) at exactly \(j=k-1-i\). These \(k-2\) last-disagreement indices are pairwise distinct. By (2), the prefix for \(q_k\) agrees with the prefix for \(F_2\) for every \(j\ge1\) but disagrees at \(j=0\), and therefore is distinct from all other prefixes as well. Hence the \(k\) prefixes have pairwise different right residual output functions, distinguishable using valid unary-zero suffixes alone. The Myhill--Nerode principle for output automata forces at least \(k\) states. Combined with the upper bound, the minimum is exactly \(k\). \(\square\)

## Verification
The included `check_integer.py` computes Fibonacci-word symbols using greedy Zeckendorf digits and checks all \(k=5,\ldots,100\), including every witness pair and the rotation-classification predictions. The independent `check_rotation.py` computes symbols using 150-digit fractional parts of \(n\varphi\) and checks \(k=5,\ldots,70\). Both completed successfully. These finite tests corroborate, but do not replace, the arbitrary-\(k\) proof. Reproduce using `python check_integer.py` and, run `python check_rotation.py`.

## Relationship to prior work
Theorem 3 of Moradi--Popoli--Shallit--Vukusic (March 19, 2026) gives an \(O(\log c)\)-state MSD-first construction for every shift; it does **not** assert minimality or this exact infinite-family count. Its Theorem 2 is an exact LSD-first formula and is not a statement about MSD-first minimality. The new part here is an explicit matching lower bound for the natural Fibonacci-minus-two sequence of shifts. The paper on linear subsequences arXiv:2512.10017 studies indexed subsequences and general base-\(k\) operations, not this particular Zeckendorf-shift count. Accessible mathematical research summaries concerning Fibonacci antipowers or Fibonacci-shift entropy do not imply this exact DFAO state count.

## Limitations
The theorem establishes the exact value only at shifts \(F_k-2\), for \(k\ge5\); no general formula for all shifts is proved. Behavior on invalid Zeckendorf representations is unconstrained. The upper bound depends on the cited, published interval-consistency construction. Neither mathematical priority nor independent audit is certified. Finite numerical tests are not proofs of the infinite claim.

## References
1. D. Moradi, P. Popoli, J. Shallit, and I. Vukusic, *State Complexity of Shifts of the Fibonacci Word*, arXiv:2603.18858v1, first posted 2026-03-19, especially Theorem 3, Definition 3, Lemmas 4--5 and Appendix B. https://arxiv.org/pdf/2603.18858
2. D. Moradi, N. Rampersad, and J. Shallit, *Complexity of Linear Subsequences of k-Automatic Sequences*, arXiv:2512.10017v1, first posted 2025-12-10. https://arxiv.org/abs/2512.10017

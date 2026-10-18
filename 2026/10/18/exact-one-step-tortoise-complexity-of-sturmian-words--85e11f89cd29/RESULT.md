# Exact one-step tortoise complexity of Sturmian words

## Finding

Let \(x\) be any one-sided binary Sturmian word of slope \(\alpha\in(0,1)\setminus\mathbb Q\), with the frequency of the symbol 1 equal to \(\alpha\). For a finite binary word \(w\), let \(T(w)\) delete the first occurrence of 1 and append 1 to the end; if the word contains no 1, let \(T(w)=w\). Write \(F_n(x)\) for the set of distinct length-\(n\) contiguous factors. Then for every integer \(n\ge1\),

\[
\rho_x^T(n):=\big|\{T(w):w\in F_n(x)\}\big|=n+1-\min\left\{n-1,\left\lfloor\frac1\alpha\right\rfloor\right\}=\max\left\{2,n+1-\left\lfloor\frac1\alpha\right\rfloor\right\}.
\]

For the empty factor, \(\rho_x^T(0)=1\). In particular, this is an exact evaluation rather than only a bound on the difference from ordinary factor complexity: for \(n\ge1\),

\[
(n+1)-\rho_x^T(n)=\min\left\{n-1,\left\lfloor\frac1\alpha\right\rfloor\right\}.
\]

## Assumptions and scope

The alphabet is ordered \(0<1\), and the operator removes the first **1**, not an arbitrary occurrence or the first 0. The parameter \(\alpha\) is the frequency of ones; the formula is consequently sensitive to exchanging the two symbols. All intercepts realizing the same irrational Sturmian slope have the same factor language. The result is for one application of \(T\), not repeated applications, the hare operator, or arbitrary binary sequences. The formula includes every positive factor length, with the empty case stated separately.

The standard mechanical representation for a Sturmian language is obtained from the coding

\[
b_i(t)=\lfloor t+(i+1)\alpha\rfloor-\lfloor t+i\alpha\rfloor,
\qquad 0\le i<n,\quad 0\le t<1.
\]

As \(t\) ranges over the circle, the resulting blocks \(B_n(t)=b_0(t)\cdots b_{n-1}(t)\) give exactly \(F_n(x)\). This follows from the usual irrational-rotation representation: the orbit of any phase is dense, so every nonempty phase interval occurs among factors of any Sturmian word of that slope. Endpoint conventions do not create extra factors; the floor coding takes the adjacent right-hand value.

## Proof

Fix \(n\ge1\). Set \(S_j(t)=\lfloor t+j\alpha\rfloor\), for \(0\le j\le n\). Inside the phase interval \([0,1)\), the only discontinuities of \(S_j\), for \(j\ge1\), occur at

\[
t_j=\lceil j\alpha\rceil-j\alpha\in(0,1).
\]

The phases \(t_1,\ldots,t_n\) are pairwise distinct, since \(\alpha\) is irrational. Hence these phases divide the circle cut at 0 into exactly \(n+1\) nonempty intervals, on each of which \(B_n(t)\) is constant. At the threshold \(t_j\), exactly \(S_j\) increases by one. Therefore, for \(j<n\), the neighboring length-\(n\) blocks differ only in positions \(j-1,j\), changing \(01\) to \(10\); for \(j=n\), their final bit changes \(0\) to \(1\). In each case the block strictly increases in lexicographic order. Thus all \(n+1\) blocks are distinct, giving the entire Sturmian factor language in lexicographic order.

Next compare the tortoise images of the two blocks adjacent to a threshold. For \(j<n\), there are two cases. If the common prefix of length \(j-1\) consists only of zeros, the changed \(01\)/\(10\) pair contains the first 1 in both words; deleting that first 1 and appending it produces the same image from both blocks. If the common prefix already contains a 1, the first deleted 1 is identical in both blocks and occurs before the changed pair. Consequently, the changed \(01\) versus \(10\) survives deletion (shifted one position left), and the tortoise image strictly increases lexicographically. At the threshold \(j=n\), the final-bit change \(0\) to \(1\) also makes the tortoise image strictly increase: if there is an earlier 1, the differing final bit survives deletion before the common appended 1; otherwise the images are \(0^n\) and \(0^{n-1}1\).

The common prefix just before or after the internal threshold \(t_j\), \(j<n\), has exactly

\[
S_{j-1}(t_j)=\lfloor t_j+(j-1)\alpha\rfloor
=\lfloor\lceil j\alpha\rceil-\alpha\rfloor
=\lceil j\alpha\rceil-1
\]

ones: the initial cumulative sum has \(S_0(t)=0\) for \(0\le t<1\). Since \(0<\alpha<1\), this prefix has no ones if and only if \(\lceil j\alpha\rceil=1\), equivalently \(j\alpha<1\). Writing \(q=\lfloor1/\alpha\rfloor\), and using the irrationality of \(\alpha\), these are exactly the internal threshold labels \(j=1,\ldots,\min\{n-1,q\}\).

The tortoise images are nondecreasing, with equality **only** at those internal thresholds. A nondecreasing finite sequence with \(m\) adjacent equalities has its number of distinct entries reduced by exactly \(m\). Starting from the \(n+1\) different length-\(n\) factors, precisely \(\min\{n-1,q\}\) pairs of neighboring images merge, yielding the stated formula. For \(n=1\), there are no internal thresholds and two images; for \(n=0\), the sole image is the empty word. This concludes the proof.

## Verification

The proof is independent of finite computation. For regression checks, run `python3 sturmian_tortoise_check.py` with the Python 3 standard library; the resulting output should match `CHECK_OUTPUT.txt`. The script samples every mechanical-cylinder interval for five algebraic irrational slopes and all lengths \(1\le n\le100\). It independently enumerates factors from a 25,000-symbol irrational-rotation orbit for \(1\le n\le60\); it checks factor-language size, image cardinalities and the precise threshold labels at which images merge. Its decimal precision and finite ranges cannot certify the theorem for arbitrary irrational slopes or infinitely many lengths; the symbolic proof above supplies that quantification.

## Relationship to prior work

Defant and Kravitz introduced the tortoise operator on words [1]. Campbell and Rampersad [2, Definitions 1–2] introduced the associated complexity of factors of infinite words. Their Theorem 1 gives a bounded difference from ordinary complexity for binary words of linear factor complexity with bounded gaps of ones, but neither its bound nor their exact results for paperfolding and Thue–Morse determine the exact loss for Sturmian slopes. Their conclusion explicitly raises further questions concerning tortoise complexity for Sturmian sequences. The exact slope-dependent defect here fills this gap.

The exact Lie complexity formula for Sturmian words in [3] concerns cyclic conjugacy classes **all** of whose rotations occur as factors, not equality of the first-one-moving tortoise images. The reflection complexity in [4] identifies factors under reversal, not under \(T\). Neither equivalence relation implies the present cardinality formula. Standard Sturmian factor complexity alone supplies \(n+1\) inputs but not the number of tortoise-image identifications; the threshold analysis is essential.

## Limitations

The result does not cover rational mechanical slopes, non-Sturmian binary languages, other alphabets, the effect of repeatedly applying tortoise, or the hare operation. The formula distinguishes the symbol 1 from 0; a complemented word has a different slope parameter. External independent validation has not been performed. The finite computational checks are supporting tests, not an exhaustive mathematical certificate.

## References

1. C. Defant and N. Kravitz, *Stack-sorting for Words*, Australasian Journal of Combinatorics **77** (2020), 51–68; arXiv:1809.09158. DOI-independent authorized full text: https://ajc.maths.uq.edu.au/pdf/77/ajc_v77_p051.pdf.
2. J. M. Campbell and N. Rampersad, *Subword enumeration up to stack-sorting equivalence*, arXiv:2604.25811, first posted 2026-04-28, v2 2026-10-05; https://arxiv.org/abs/2604.25811.
3. A. De Luca and G. Fici, *On the Lie complexity of Sturmian words*, arXiv:2206.00995, https://arxiv.org/abs/2206.00995.
4. J.-P. Allouche, J. M. Campbell, S. Li, J. Shallit and M. Stipulanti, *The reflection complexity of sequences over finite alphabets*, arXiv:2406.09302, https://arxiv.org/abs/2406.09302.

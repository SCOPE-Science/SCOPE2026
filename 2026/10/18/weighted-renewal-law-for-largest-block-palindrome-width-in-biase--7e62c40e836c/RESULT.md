# Weighted renewal law for largest block-palindrome width in biased random words

## Finding

Let \(\Sigma\) be a finite alphabet with at least two symbols and let \(\boldsymbol\pi=(\pi_a)_{a\in\Sigma}\) be a strictly positive, **nonuniform** probability vector. Let \(W_n\) be a length-\(n\) word sampled independently with letter distribution \(\boldsymbol\pi\). Write \(H_n\) for the width (number of nonempty blocks) of its *largest block-palindrome factorization*, and set \(H_0=0\).

For \(\ell\geq1\), let \(\mathcal U_\ell\) be the set of unbordered words of length \(\ell\), and define
\[
 b_\ell=\sum_{u\in\mathcal U_\ell}\prod_{i=1}^\ell\pi_{u_i}^{\,2},\qquad
 s=\sum_{a\in\Sigma}\pi_a^2,\qquad
 B(z)=\sum_{\ell\ge1}b_\ell z^{2\ell},\qquad h=B(1).
\]
Then \(0<h<1\), and the **exact joint length/width probability generating function** is
\[
 \boxed{\displaystyle
 \sum_{n\ge0}z^n\mathbb E[t^{H_n}]
 =\frac{1+t\,(z-B(z))/(1-z)}{1-t^2B(z)}.}
\]
Furthermore, if \(J\) has the geometric distribution \(\Pr(J=j)=(1-h)h^j\), for \(j=0,1,2,\ldots\), then there exist \(C<\infty\) and \(\alpha>1\), depending only on \(\boldsymbol\pi\), such that
\[
 \boxed{\displaystyle
 d_{\rm TV}\big(\mathcal L(H_n),\mathcal L(1+2J)\big)
 \le C\alpha^{-n}\quad(n\ge1).}
\]
Every fixed positive integer moment converges at an exponential rate. In particular,
\[
 \boxed{\displaystyle
 \lim_{n\to\infty}\mathbb E H_n=\frac{1+h}{1-h},\qquad
 \lim_{n\to\infty}\operatorname{Var}(H_n)=\frac{4h}{(1-h)^2}.}
\]

The parameters admit an exact multivariate recurrence. For arbitrary nonnegative letter weights \(\mathbf w=(w_a)_{a\in\Sigma}\), put
\[
 U_r(\mathbf w)=\sum_{u\in\mathcal U_r}\prod_{i=1}^r w_{u_i},
 \qquad S(\mathbf w)=\sum_a w_a,
 \qquad \mathbf w^{\odot2}=(w_a^2)_a.
\]
With the empty word counted once,
\[
 \boxed{\begin{aligned}
 U_0(\mathbf w)&=1,\quad U_1(\mathbf w)=S(\mathbf w),\\
 U_{2m+1}(\mathbf w)&=S(\mathbf w)U_{2m}(\mathbf w)\quad(m\ge0),\\
 U_{2m}(\mathbf w)&=S(\mathbf w)U_{2m-1}(\mathbf w)-U_m(\mathbf w^{\odot2})\quad(m\ge1).
 \end{aligned}}
\]
Thus \(b_\ell=U_\ell((\pi_a^2)_a)\) is computable exactly for rational letter probabilities, and truncating \(h\) at \(L\) terms incurs error at most \(s^{L+1}/(1-s)\).

For the nonuniform Bernoulli source \(\boldsymbol\pi=(1/4,3/4)\), this yields
\[
 h=0.8028150445695221\ldots,\qquad
 \lim_{n\to\infty}\mathbb E H_n=9.142761630235764\ldots.
\]

## Assumptions and scope

A *border* of a finite word is a nonempty proper prefix equal to a suffix. A word is *unbordered* when it has no border. A block-palindrome factorization is a decomposition into pairwise equal outer blocks, moving inward, with a possibly empty central block. Its *width* is the number of nonempty blocks. The standard greedy characterization identifies the largest-width factorization by repeatedly removing the shortest nonempty border from both ends, stopping on an unbordered word or an empty word; see [1,2]. We use this characterization as the definition of the width statistic.

The alphabet is fixed and finite, \(|\Sigma|\ge2\). Its probabilities are strictly positive, sum to one, and are not all equal. The conclusion concerns the original letter probability distribution, not a uniformly sampled word and not a Markov source. The theorem holds for every integer \(n\ge1\); the formula for the empty word uses \(H_0=0\). The variance assertion is for the same \(H_n\) variable.

## Proof

**1. A shortest-border kernel.** Every nonempty border of a word of length \(n\) has a shortest one of length at most \(\lfloor n/2\rfloor\). Indeed, a border longer than half the word overlaps and induces a shorter nonempty border. That shortest border \(u\) must be unbordered: any border of \(u\) would also border the whole word. Conversely, if \(n\ge2\ell\) and both ends of a length-\(n\) word equal some unbordered \(u\) of length \(\ell\), then no shorter border is possible, so \(u\) is its shortest border.

These cases are disjoint over distinct shortest lengths \(\ell\) and over distinct \(u\) at fixed length. Independence of the two nonoverlapping outer blocks gives exactly \(b_\ell\) as the probability that the shortest border has length \(\ell\), whenever \(n\ge2\ell\). After removing the border copies, the central word is a fresh independent sample. Hence, for every \(n\ge1\),
\[
 \Pr(H_n=1)=1-\sum_{\ell=1}^{\lfloor n/2\rfloor}b_\ell,
 \qquad
 \mathbb E[t^{H_n}]
 =t\!\left(1-\sum_{\ell=1}^{\lfloor n/2\rfloor}b_\ell\right)
 +t^2\sum_{\ell=1}^{\lfloor n/2\rfloor}b_\ell\,\mathbb E[t^{H_{n-2\ell}}].
\]
For \(n=0\), \(\mathbb E[t^{H_0}]=1\). Sum this recurrence against \(z^n\) to obtain
\[
 G(z,t)=1+\frac{t(z-B(z))}{1-z}+t^2B(z)G(z,t),
\]
which proves the stated bivariate generating function as an identity of formal power series.

**2. Weighted unbordered-word recursion.** In a nonempty word, its shortest border, when present, is nonoverlapping. Inserting a freely chosen letter at the middle of an unbordered word of even length \(2m\) produces an unbordered word of length \(2m+1\), and removing that central letter reverses the operation. The inserted letter multiplies total weight by \(S(\mathbf w)\). This proves the odd-length relation.

Similarly, inserting a freely chosen letter after the first \(m-1\) positions of an unbordered word of length \(2m-1\) produces a word of length \(2m\) with no border shorter than \(m\). The only possible failure is a border of length \(m\), meaning the resulting word is a square \(uu\). Removing its last letter in the first copy leaves \(u_1\cdots u_{m-1}u\), which is unbordered exactly when \(u\) is unbordered. Such exceptional squares contribute total weight \(\sum_{u\in\mathcal U_m}\prod_i w_{u_i}^2=U_m(\mathbf w^{\odot2})\). Subtract this from the weighted insertion total to get the even-length recurrence. Both initial values are immediate. This gives the exact computation of each \(b_\ell\).

**3. The parameter is strictly between zero and one.** Because every \(\pi_a>0\) and at least two letters occur, \(0<s<1\) and \(b_1=s>0\). For each \(\ell\), dropping the unbordered constraint gives \(b_\ell\le s^\ell\), so \(h\le s/(1-s)<\infty\). To show \(h<1\), take independent infinite letter streams \(X_1,X_2,\ldots\) and \(Y_1,Y_2,\ldots\), both with law \(\boldsymbol\pi\). For any distinct letters \(a,b\), condition on \(X_1=a\), \(Y_1=b\), an event of probability \(\pi_a\pi_b>0\). No one-letter match can occur. For every \(\ell\ge2\), the probability of the symmetric match \(X_1\cdots X_\ell=Y_\ell\cdots Y_1\), conditional on this event, is \(\pi_a\pi_b s^{\ell-2}\). By the union bound, the conditional probability of *any* match is at most \(\pi_a\pi_b/(1-s)\le1/2\), because \(1-s=\sum_{c\ne d}\pi_c\pi_d\ge2\pi_a\pi_b\). Thus an infinite pair of streams has no symmetric match with positive probability. The first possible match has probability mass \(b_\ell\) at length \(\ell\), and their disjoint union has mass \(h\). Therefore \(0<h<1\).

**4. Infinite renewal coupling.** Form a length-\(n\) random word by taking \(X_1\cdots X_{\lceil n/2\rceil}\) followed by \(Y_{\lfloor n/2\rfloor}\cdots Y_1\). All these letters are independent, so this realizes the law of \(W_n\). Starting with the two infinite inward streams, repeatedly seek the least \(\ell\ge1\) with
\[
 X_1\cdots X_\ell=Y_\ell\cdots Y_1.
\]
When this least match exists, remove \(\ell\) letters from each stream and repeat. If no match exists at a stage, stop. A successful step has length distribution with (defective) masses \(b_\ell\), and the untouched tails are independent copies of the original streams. Consequently the number \(J\) of successful steps before the first failure obeys \(\Pr(J=j)=(1-h)h^j\).

Let \(\ell_1,\ldots,\ell_J\) be its successful step lengths and \(S_* =\ell_1+\cdots+\ell_J\). For any \(\alpha>1\) sufficiently close to one, the power series \(B(\alpha)\) is finite and less than one: its convergence radius is at least \(s^{-1/2}>1\), while \(B(1)=h<1\). By summing all sequences of successful steps,
\[
 \mathbb E[\alpha^{2S_*}]
 =\frac{1-h}{1-B(\alpha)}<\infty.
\]
On the event \(2S_*<n\), the finite word executes exactly the same successful peelings and stops with a nonempty unbordered center. Thus \(H_n=1+2J\) on that event. The coupling inequality and Markov's bound give
\[
 d_{\rm TV}\big(\mathcal L(H_n),\mathcal L(1+2J)\big)
 \le\Pr(2S_*\ge n)
 \le \frac{1-h}{1-B(\alpha)}\alpha^{-n}.
\]
Every finite greedy peeling is an initial segment of the infinite sequence of successes; in particular \(0\le H_n\le1+2J\) under this coupling. For any fixed positive integer \(r\),
\[
 \mathbb E\big[(1+2J)^r\alpha^{2S_*}\big]
 =(1-h)\sum_{j\ge0}(1+2j)^rB(\alpha)^j<\infty.
\]
The same error-event bound therefore gives exponential convergence of the \(r\)-th moment. Evaluating the mean and variance of \(1+2J\) proves the stated constants.

**5. Certified truncation.** From \(b_\ell\le s^\ell\), for every positive integer \(L\),
\[
 0\le h-\sum_{\ell=1}^{L}b_\ell\le\frac{s^{L+1}}{1-s}.
\]
For the stated Bernoulli example, \(s=5/8\). The exact weighted recurrence through \(L=100\) gives the displayed decimal estimates with rigorous truncation error at most \((5/8)^{101}/(3/8)<6.46\cdot10^{-21}\) for \(h\).

## Verification

The included standalone `verify.py` evaluates the weighted unbordered recurrence in exact rational arithmetic, independently enumerates unbordered words, exhaustively computes all word probabilities by direct greedy factorization, and checks the generating-function coefficient recurrence through length \(12\) for three binary sources (including two strictly biased sources) and through length \(8\) for a ternary source. It additionally checks the weighted recurrence for arbitrary, not necessarily probability-normalized, letter weights and certifies the \((1/4,3/4)\) numerical parameter interval through degree \(100\). Run `python verify.py`. Exact finite checks support, but do not prove, the infinite coupling and limit assertions; those are proved above.

## Relationship to prior work

Goto, I, Bannai, and Inenaga [1] established the greedy shortest-border characterization and studied algorithmic block-palindrome structure. Gabrić and Shallit [2], Theorem 2, derived exact counts for largest-factorization widths **when all words of a fixed length are equally likely**, and their Theorem 4 establishes existence of the corresponding uniform-source limiting mean. Those uniform results are not claimed as new here, and the present theorem does **not** settle their separate power-series conjecture.

The present result concerns an independently sampled **nonuniform** alphabet, where words have unequal probabilities. The exact weighted kernel requires a multivariate unbordered-word recurrence, rather than substitution of a fractional alphabet size into the uniform enumerator. The new asserted contribution is the joint weighted probability law together with an explicit *geometric* limit, exponential total-variation bound, moment convergence, and certified parameter computation for every strictly biased full-support source. Holub and Shallit [3] concern distributions of period and **longest** border statistics of uniformly random words, not repeated shortest-border peelings under a biased source.

## Limitations

The probability source must be iid, finite, and full-support; correlated or Markov input is not covered. The exponential convergence constants depend on the source distribution and need not be uniform as a letter probability tends to zero. The theorem does not give a closed elementary expression for \(h\), but the recurrence and geometric tail give a certified evaluation. Previous literature already covers uniform finite-length counts, so neither their uniform consequences nor the general greedy algorithm are claimed as original. Undetected equivalent results in related probability or weighted-word literature remain possible. No independent review or independent certification is asserted.

## References

[1] K. Goto, T. I, H. Bannai, and S. Inenaga, *Block Palindromes: A New Generalization of Palindromes*, arXiv:1806.00198, first public version 2018-06-01; Theorem 1 and Section 3. https://arxiv.org/abs/1806.00198.

[2] D. Gabrić and J. Shallit, *Smallest and Largest Block Palindrome Factorizations*, arXiv:2302.13147, first public version 2023-02-25; Theorems 2 and 4, and Conjecture 5. https://arxiv.org/abs/2302.13147.

[3] Š. Holub and J. Shallit, *Periods and Borders of Random Words*, arXiv:1509.05240, first public version 2015-09-17; STACS 2016, DOI 10.4230/LIPIcs.STACS.2016.44. https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.STACS.2016.44.

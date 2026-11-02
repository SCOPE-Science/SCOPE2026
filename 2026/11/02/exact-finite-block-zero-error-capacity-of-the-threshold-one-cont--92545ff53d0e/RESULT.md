# Exact finite-block zero-error capacity of the threshold-one contextual deletion channel

## Finding

For every integer alphabet size \(q\ge2\) and every input length \(n\ge1\), let \(T_q\) delete the first symbol of every maximal constant-symbol run of the input **except the initial run**. All deletion locations are determined on the original word, before performing deletions. Write \(M_q(n)\) for the maximum cardinality of a length-\(n\) zero-error code for this deterministic channel.

The exact optimum, for every such \(q,n\), is
\[
\boxed{M_q(n)=\sum_{\substack{m,r\ge1\\r\le m,\;m+r-1\le n}}q(q-1)^{r-1}\binom{m-1}{r-1}.}
\]
Its ordinary generating function is
\[
\boxed{\sum_{n\ge1} M_q(n)z^n=\frac{qz}{(1-z)(1-z-(q-1)z^2)}.}
\]
Equivalently, with \(U_0=0\), \(U_1=1\) and \(U_j=U_{j-1}+(q-1)U_{j-2}\) for \(j\ge2\),
\[
M_q(n)=q\sum_{j=1}^{n}U_j.
\]
The finite-block optimum has an explicit representative for each distinct output, and the limiting zero-error information rate exists:
\[
\boxed{\lim_{n\to\infty}\frac{\log_2 M_q(n)}n
=\log_2\left(\frac{1+\sqrt{4q-3}}2\right).}
\]
For the binary alphabet, this specializes to \(M_2(n)=2(F_{n+2}-1)\), where \(F_0=0,F_1=1\), and the rate is \(\log_2\bigl((1+\sqrt5)/2\bigr)\). The first eight binary optima, at input lengths \(1,\ldots,8\), are \(2,4,8,14,24,40,66,108\). For the four-letter DNA alphabet the rate is \(\log_2((1+\sqrt{13})/2)\) bits per input symbol.

A stronger normal-form statement underlies the count: every nonempty output \(y\) with \(m\) symbols and \(r\) maximal constant runs has minimum possible preimage length exactly \(m+r-1\), and it has **one and only one** preimage of that minimum length.

## Assumptions and scope

The input is a nonempty word \(x\in\Sigma_q^n\) with \(|\Sigma_q|=q\ge2\); the channel is deterministic and performs exactly one deletion at the beginning of each original noninitial run, regardless of the run's length. The receiver observes the resulting variable-length word without deletion locations. There is no adversarial or probabilistic choice of errors, and each codeword has the same prescribed input length \(n\). A zero-error code \(\mathcal C\subseteq\Sigma_q^n\) satisfies \(T_q(x)\ne T_q(x')\) for distinct \(x,x'\in\mathcal C\).

Write the run decomposition of \(x\) uniquely as
\[
x=a_1^{\ell_1}a_2^{\ell_2}\cdots a_s^{\ell_s},\qquad
\ell_i\ge1,\quad a_i\ne a_{i+1}.
\]
The superscripts represent repetition counts, not numerical exponentiation of alphabet symbols. The channel output is the concatenation of \(a_1\) repeated \(\ell_1\) times and, for \(i\ge2\), \(a_i\) repeated \(\ell_i-1\) times; empty contributions are omitted, and adjacent surviving contributions may merge. This is the threshold-one, deletion-probability-one endpoint of the contextual channel defined by Chen, Milenkovic, Ribeiro and Sima.

## Proof

**1. Necessary minimum preimage length.** If the input has \(s\) runs, precisely \(s-1\) of its symbols are removed, so an output of length \(m\) satisfies \(n=m+s-1\). Deleting symbols cannot increase the number of runs: each original run contributes either one constant block or the empty word, and concatenating blocks can only merge, not split, constant blocks. Thus if the output has \(r\) runs, then \(s\ge r\), giving \(n\ge m+r-1\).

**2. A unique minimum-length preimage.** Express the output as its run decomposition
\[
y=b_1^{d_1}b_2^{d_2}\cdots b_r^{d_r},\quad d_i\ge1,\quad b_i\ne b_{i+1}.
\]
Construct
\[
x_*(y)=b_1^{d_1}b_2^{d_2+1}\cdots b_r^{d_r+1}.
\]
It has length \(m+r-1\), and the channel deletes the first symbol from every run after the first, returning \(y\). If another preimage has this length, it has exactly \(r\) original runs by step 1. Since its output also has \(r\) runs, no original run can disappear or merge with a different surviving run. Its ordered run letters therefore equal those of \(y\); the first run length equals \(d_1\), while every subsequent original run length equals \(d_i+1\). Hence that preimage is \(x_*(y)\), proving uniqueness.

**3. Achieving every larger source length.** For any \(n\ge m+r-1\), start with \(x_*(y)\) and append \(n-(m+r-1)\) singleton runs, each with a symbol different from the immediately preceding symbol. Such a choice is always possible because \(q\ge2\). Every newly appended run is noninitial and has length one, so its sole symbol is deleted by \(T_q\); all previously determined deletion locations remain unchanged. The resulting length-\(n\) word maps to \(y\). Thus an output occurs at block length \(n\) if and only if \(m+r-1\le n\).

**4. Exact image count and optimal code.** For fixed \(m,r\) the number of \(q\)-ary words with exactly \(r\) runs equals
\[
q(q-1)^{r-1}\binom{m-1}{r-1}.
\]
Choose the first run letter in \(q\) ways, each next run letter in \(q-1\) ways, and the \(r-1\) change locations among \(m-1\) boundaries. Combining this with step 3 gives the finite formula. Every zero-error code injects under the deterministic map into its image, giving \(|\mathcal C|\le|T_q(\Sigma_q^n)|\). Equality is attained by choosing, for every possible output \(y\), the explicitly padded word constructed in step 3. No two selected words can coincide because their outputs differ. Therefore \(M_q(n)=|T_q(\Sigma_q^n)|\).

**5. Generating function.** First enumerate outputs according to their *minimum* feasible source length. For any \(r\ge1\), using the standard composition identity,
\[
\sum_{m\ge r}\binom{m-1}{r-1}z^m=\left(\frac{z}{1-z}\right)^r,
\]
so the generating function \(A_q(z)\) of outputs whose minimum source length is \(j\) is
\[
\begin{aligned}
A_q(z)&=\sum_{r\ge1}q(q-1)^{r-1}z^{r-1}
\left(\frac{z}{1-z}\right)^r\\
&=\frac{qz}{1-z-(q-1)z^2}.
\end{aligned}
\]
Each output with minimum length \(j\) occurs at **every** block length \(n\ge j\), so the generating function for the cumulative image count is \(A_q(z)/(1-z)\), giving the displayed rational expression. Its coefficients yield \(M_q(n)=q\sum_{j=1}^nU_j\) with the stated recurrence. For \(q=2\), the sequence \(U_j\) is Fibonacci and the usual partial-sum identity gives \(M_2(n)=2(F_{n+2}-1)\).

**6. Capacity.** The polynomial \(\lambda^2-\lambda-(q-1)=0\) has the positive root \(\lambda_q=(1+\sqrt{4q-3})/2>1\) and a negative root of smaller absolute value. The standard solution of the order-two recurrence therefore gives \(U_j=\Theta_q(\lambda_q^j)\) and \(M_q(n)=\Theta_q(\lambda_q^n)\). Taking base-two logarithms, dividing by \(n\), and passing to the limit yields the asserted rate. No multiblock assumption is required for this finite-block limit.

## Verification

`verify.py` implements the channel from its definition, the canonical inverse, the exact binomial count, and the independent recurrence. It exhaustively processes all inputs for \(q=2\) at lengths through 12, \(q=3\) through length 8, and \(q=4\) through length 7. It checks image cardinalities, canonical recovery and shortest-preimage uniqueness at their minimum input lengths. It additionally compares both exact formulas for all \(2\le q\le19\) and \(1\le n\le150\), and checks the binary Fibonacci specialization. Its recorded output is in `verification_output.txt`. These finite tests corroborate rather than replace the all-length proof above.

## Relationship to prior work

Chen, Milenkovic, Ribeiro and Sima introduce the contextual deletion mechanism motivated by nanopore readout in arXiv:2602.05072, with the original first public version dated 2026-02-04. Their extremal-channel analysis in Section V explicitly begins with \(k\ge2\), and the article provides constrained-code capacity bounds rather than this exact threshold-one image enumeration. The threshold-one endpoint and the all-\(q\) finite-block optimum are the contributions here. The binary Fibonacci appearance resembles familiar run-length-limited sequence counts, but this theorem concerns the image of a deterministic, synchronized run-boundary deletion map, not a maximum-run-length constrained language.

The run-length-limited constructions in Nguyen and collaborators (arXiv:2001.02839) and the adversarial deletion threshold problem of Kash, Mitzenmacher, Thaler and Ullman (arXiv:1102.0040) concern distinct mechanisms; neither supplies the above image/preimage equivalence. No claim of exhaustive worldwide publication priority is made.

## Limitations

The result is for the fully deterministic extremal case, threshold exactly one, a fixed alphabet of at least two symbols, and simultaneous deletions identified from the original word. It does not determine capacity for higher thresholds, nontrivial deletion probabilities, bounded numbers of adversarial deletions, or a channel in which deletion locations are recomputed dynamically after each deletion. It proves finite-block optimal cardinality and asymptotic rate, not constraints on practical encoder complexity or sequencing chemistry. Equivalent unindexed earlier work on a run-boundary deletion transducer cannot be excluded.

## References

1. Y.-P. Chen, O. Milenkovic, J. Ribeiro and J. Sima, *Correcting Contextual Deletions in DNA Nanopore Readouts*, arXiv:2602.05072; first publicly posted 2026-02-04. https://arxiv.org/abs/2602.05072 . Section I-A (model) and Section V (constant-threshold extremal channel; \(k\ge2\)).
2. T. T. Nguyen et al., *Capacity-Approaching Constrained Codes with Error Correction for DNA-Based Data Storage*, arXiv:2001.02839, first publicly posted 2020-01-09. https://arxiv.org/abs/2001.02839 . Run-length-limited coding comparison.
3. I. Kash, M. Mitzenmacher, J. Thaler and J. Ullman, *On the Zero-Error Capacity Threshold for Deletion Channels*, arXiv:1102.0040, 2011. https://arxiv.org/abs/1102.0040 . Adversarial deletion-channel comparison.

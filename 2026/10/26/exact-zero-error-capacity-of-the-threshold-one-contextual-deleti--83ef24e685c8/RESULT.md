# Exact zero-error capacity of the threshold-one contextual deletion channel

## Finding
For every alphabet size \(q\ge 2\) and input length \(n\ge 1\), consider the deterministic contextual deletion channel that removes the first symbol of each noninitial constant run, with deletion locations determined in the *original* input. Its output range is exactly
\[
\mathcal R_q(n)=\{y\in\Sigma_q^m:1\le m\le n,\;m+t(y)\le n\},
\]
where \(t(y)\) counts symbol changes between consecutive positions of \(y\). The maximum number \(M_q(n)\) of distinguishable length-\(n\) codewords therefore equals
\[
M_q(n)=q\sum_{m=1}^{n}\sum_{t=0}^{\min\{m-1,n-m\}}\binom{m-1}{t}(q-1)^t,
\qquad
\sum_{n\ge1}M_q(n)z^n=\frac{qz}{(1-z)(1-z-(q-1)z^2)}.
\]
The exact asymptotic zero-error information rate, measured in \(q\)-ary symbols per input symbol, is
\[
\lim_{n\to\infty}\frac{\log_q M_q(n)}n
=\log_q\!\left(\frac{1+\sqrt{4q-3}}2\right).
\]
For binary alphabets this specializes to \(M_2(n)=2(F_{n+2}-1)\), with the standard Fibonacci sequence \(F_0=0,F_1=1\). In the four-letter case the capacity is \(\log_4((1+\sqrt{13})/2)\), approximately \(0.6016869272\).

## Assumptions and scope
Fix an integer \(q\ge2\), an alphabet \(\Sigma_q=\{0,1,\ldots,q-1\}\), and \(n\ge1\). For an input \(x=x_1\cdots x_n\), define \(D_q(x)\) by simultaneously removing **exactly** each input symbol at position \(i\ge2\) for which \(x_i\ne x_{i-1}\). The comparison \(x_i\ne x_{i-1}\) always uses the original input, not the already-shortened output. Thus the first input symbol survives, and the first symbol of each subsequent maximal constant run is deleted. This is the \(k=1,p=1\) extremal contextual deletion model for binary alphabets in the cited source, extended here by the same rule to arbitrary finite alphabets.

A block code \(C\subseteq\Sigma_q^n\) has zero decoding error for this deterministic channel precisely when \(D_q\) is injective on \(C\). Define \(M_q(n)\) to be the largest size of such a code; output lengths are observed and may vary. For any nonempty word \(y=y_1\cdots y_m\), define \(t(y)=\#\{j:2\le j\le m,\;y_j\ne y_{j-1}\}\). No adversarial, randomized, or partial-deletion model is covered by the result.

## Proof
**1. Exact range.** The input has \(t(x)\) changes and one symbol is deleted at the start of every new run. Hence \(|D_q(x)|=n-t(x)\). For every subsequence \(y\) of \(x\), the number of changes cannot increase: any pair of consecutive retained symbols spans a disjoint interval of the input, and if the pair differs, that interval contains at least one original change. Therefore \(t(y)\le t(x)\), giving \(|y|+t(y)\le n\).

Conversely, suppose \(y\ne\varepsilon\) has \(m=|y|\) and \(m+t(y)\le n\). Write its constant-run decomposition as \(y=c_1^{\ell_1}c_2^{\ell_2}\cdots c_r^{\ell_r}\), with adjacent run symbols unequal. Then \(r-1=t(y)\) and the length-\(m+t(y)\) word
\[
x_0=c_1^{\ell_1}c_2^{\ell_2+1}\cdots c_r^{\ell_r+1}
\]
satisfies \(D_q(x_0)=y\): the initial run is retained, and from each later run precisely its first symbol is deleted. To reach any prescribed length \(n\), repeatedly append one symbol distinct from the current last input symbol. Each appended singleton run's first symbol is deleted, preserving the output. Such a choice exists for \(q\ge2\). Therefore \(y\in\mathcal R_q(n)\), proving the asserted range equality including \(n=1\).

**2. Optimal code size.** A deterministic channel has at most one codeword per output in every zero-error code. Conversely, choosing one input preimage of length \(n\) for every member of \(\mathcal R_q(n)\) yields a zero-error code of size \(|\mathcal R_q(n)|\). Thus \(M_q(n)=|\mathcal R_q(n)|\).

**3. Exact enumeration.** Among length-\(m\) output words with precisely \(t\) changes, choose the initial symbol in \(q\) ways, the \(t\) change locations among \(m-1\) boundaries, and the new symbol at every change in \(q-1\) ways. This gives \(q\binom{m-1}t(q-1)^t\) words. Retaining only \(m+t\le n\) yields the displayed double sum. Equivalently, charge one input position for the initial output symbol, one for each unchanged next output symbol, and two for each changed next output symbol. Summing these minimal-cost output words gives
\[
\sum_{y\ne\varepsilon}z^{|y|+t(y)}
=\frac{qz}{1-z-(q-1)z^2}.
\]
Since each such word occurs in the output range at every \(n\) at least its minimal cost, cumulative counting contributes \(1/(1-z)\), proving the generating function.

**4. Asymptotic capacity.** Put \(U_0=0,U_1=1\) and \(U_s=U_{s-1}+(q-1)U_{s-2}\) for \(s\ge2\). The coefficient of \(z^s\) in the minimal-cost enumerator is \(qU_s\); consequently \(M_q(n)=q\sum_{s=1}^nU_s\). The characteristic roots are
\[
\lambda_q=\frac{1+\sqrt{4q-3}}2,
\qquad \mu_q=\frac{1-\sqrt{4q-3}}2.
\]
For every \(q\ge2\), one has \(\lambda_q>1\) and \(|\mu_q|<\lambda_q\). Therefore \(M_q(n)\) grows as a positive constant times \(\lambda_q^n\), which proves the capacity limit. At \(q=2\), \(U_s=F_s\) and \(\sum_{s=1}^nF_s=F_{n+2}-1\).

## Verification
The accompanying standalone `verify.py` exactly implements the original-input deletion rule and, for every tested input, compares its output with the proposed range criterion. It counts admissible outputs both by exhaustive enumeration and by the closed formula, and verifies explicit preimages for short lengths. It returned `VERIFY_OK` for \(q=2\) through \(n=14\), \(q=3\) through \(n=9\), \(q=4\) through \(n=7\), and \(q=5\) through \(n=6\). In particular the binary sizes begin \(2,4,8,14,24,40,66\); four-letter sizes begin \(4,8,24,52,128,288,676\). These finite checks supplement, and do not replace, the all-length proof.

## Relationship to prior work
Chen, Milenkovic, Ribeiro and Sima introduce contextual deletion channels and study the extremal case \(p=1\), providing capacity bounds for constant run-length thresholds and constructions for bounded errors. The exact output-range characterization, all-length zero-error optimum, and capacity at the boundary threshold \(k=1\) are not stated in the relevant examined sections, which emphasize \(k\ge2\). Their binary channel definition is the starting point; the extension to \(q\ge2\) is explicit here. Con and Ribeiro's broader study of input-correlated synchronization errors considers a distinct run-length-dependent deletion mechanism and provides a general capacity framework, not this exact deterministic boundary calculation. At \(k=1\), the source's baseline construction that avoids binary patterns 010 and 101 already gives a rate of \(\log_2((1+\sqrt5)/2)\); the binary numerical asymptotic rate alone is not claimed as new. The principal conclusion here is the exact all-length image, optimal finite code size, and uniform alphabet extension. General run-length-limited enumerators use related recurrence techniques, but they alone do not identify which variable-length outputs are realizable from *exactly* \(n\) input symbols under this channel.

## Limitations
This theorem only concerns simultaneous deterministic deletions of every noninitial run's first symbol (the threshold-one, probability-one endpoint); its formula must not be interpreted as a bound for positive-noise, adversarial-subset, or higher-threshold channels. The proof is elementary and an earlier equivalent treatment under other terminology may exist; no universal novelty or literature-exhaustiveness assertion is made. The asymptotic rate is a zero-error block-code rate with variable-length channel output, not a fixed-output-length entropy per received symbol.

## References
1. Yuan-Pon Chen, Olgica Milenkovic, João Ribeiro, Jin Sima, *Correcting Contextual Deletions in DNA Nanopore Readouts*, arXiv:2602.05072 (first public version 2026-02-04), https://arxiv.org/abs/2602.05072 .
2. Roni Con, João Ribeiro, *Channels with Input-Correlated Synchronization Errors*, arXiv:2504.14087 (first public version 2025-04-18), https://arxiv.org/abs/2504.14087 .

# Exact binomial length spectrum of minimal absent subsequences in alternating binary words

## Finding

For every integer \(m\geq 1\), let \(w_m=(01)^m\), and let \(H_m(\ell)\) be the number of **distinct minimal absent scattered subsequences** of \(w_m\) having length \(\ell\). Then, for every integer \(j\geq0\),
\[
H_m(m+1+j)=
\begin{cases}
\displaystyle\binom{m+2-j}{2j+1},&0\leq j\leq\lfloor(m+1)/3\rfloor,\\
0,&j>\lfloor(m+1)/3\rfloor,
\end{cases}
\]
and all other lengths have count zero. In particular, the shortest length is \(m+1\), with exactly \(m+2\) minimal absent subsequences; the longest length is exactly \(m+1+\lfloor(m+1)/3\rfloor\).

The full bivariate generating function, where \(x\) marks \(m\) and \(z\) marks the length, is
\[
F(x,z)=\sum_{m\geq1}\sum_{\ell\geq1}H_m(\ell)x^m z^\ell
=\frac{xz^2(3-2xz+xz^2+2x^2z^3)}{(1-xz)^2-x^3z^4}.
\]
Consequently, if \(A_m=\sum_\ell H_m(\ell)\), then
\[
\sum_{m\geq1}A_m x^m
=\frac{x(3-x+2x^2)}{1-2x+x^2-x^3},
\qquad
(A_1,A_2,A_3,A_4,A_5,A_6)=(3,5,9,16,28,49).
\]
For every \(m\geq4\), \(A_m=2A_{m-1}-A_{m-2}+A_{m-3}\); the growth is \(\Theta(\lambda^m)\), where \(\lambda=1.754877666\ldots\) is the unique real root greater than one of \(\lambda^3-2\lambda^2+\lambda-1=0\).

## Assumptions and scope

The alphabet is the fixed binary alphabet \(\{0,1\}\); \(m\) is any positive integer. A word \(u\) is a scattered subsequence of \(w\) when an increasing sequence of positions in \(w\) spells \(u\). The word \(u\) is minimal absent when it is not a scattered subsequence of \(w\), but deletion of any single position of \(u\) yields a scattered subsequence. Because the subsequence relation is transitive, this is equivalent to every proper scattered subsequence occurring. Distinct words are counted once, not their distinct embeddings. Absent contiguous factors are a different notion.

## Proof

**1. Exact greedy embedding cost.** For any nonempty binary word \(u=u_1\cdots u_\ell\), define
\[
c(u)=\ell-\sum_{i=1}^{\ell-1}{\mathbf{1}}_{(u_i,u_{i+1})=(0,1)}.
\]
The leftmost greedy embedding of \(u\) into the infinite alternating word \(010101\cdots\) uses exactly \(c(u)\) consecutive \(01\) blocks. Indeed, the first letter takes a position in the first block; consecutive letters \(01\) can share a block, whereas transitions \(00\), \(10\), and \(11\) each force the next block. By the standard leftmost-embedding exchange argument, no subsequence embedding can use fewer blocks. Hence
\[
u\preceq(01)^m\quad\Longleftrightarrow\quad c(u)\leq m.
\]

**2. Characterization of minimality.** Deleting a single letter decreases \(c\) by at most one. Deleting the first or last letter decreases \(c\) by zero precisely when the discarded adjacent pair is \(01\). Deleting an internal letter decreases \(c\) by zero precisely when its three-letter neighborhood is \(010\) or \(101\); otherwise it decreases \(c\) by one. These assertions follow directly by comparing the counts of adjacent \(01\) pairs, including the new pair created at an internal deletion. Since both letters appear in \((01)^m\), an absent word has length at least two. Therefore \(u\) is minimal absent precisely when
\[
 c(u)=m+1,
\quad u_1u_2\ne01,
\quad u_{\ell-1}u_\ell\ne01,
\quad\text{and no length-three factor is }010\text{ or }101.
\]
Necessity of the first equation follows because deleting any one symbol must bring the cost down to at most \(m\); sufficiency follows from the exact deletion-cost cases.

**3. Four-state transfer.** Retain the last two letters in state order \((00,01,10,11)\), forbid internal triples \(010\) and \(101\), and forbid initial and terminal state \(01\). Give an initial two-letter state weight \(xz^2\), where the exponent of \(x\) records \(c(u)-1\). Every added letter contributes \(z\), and contributes an additional \(x\) unless the resulting last two letters are \(01\). The weighted transition matrix and allowed-state vector are
\[
T=\begin{pmatrix}
xz&z&0&0\\
0&0&0&xz\\
xz&0&0&0\\
0&0&xz&xz
\end{pmatrix},\qquad
v=\begin{pmatrix}1\\0\\1\\1\end{pmatrix}.
\]
All words meeting the local minimality conditions are counted by the formal power series
\[
 F(x,z)=xz^2v^{\mathsf T}(I-T)^{-1}v
 =\frac{xz^2(3-2xz+xz^2+2x^2z^3)}{(1-xz)^2-x^3z^4}.
\]
The variable \(x\) records exactly \(m\), by the first condition in step 2. Matrix inversion is over the ring of formal power series, so the expression is valid without convergence assumptions.

**4. Coefficient extraction.** Put \(t=xz\). The same rational function decomposes as
\[
F(x,z)=\frac{zt(3-2t)}{(1-t)^2}
+\sum_{j\geq1}\frac{z^{j+1}t^{3j-1}}{(1-t)^{2j+2}}.
\]
The first term has coefficient \(m+2\) at \(x^m z^{m+1}\). For \(j\geq1\), the binomial expansion
\[
(1-t)^{-2j-2}=\sum_{r\geq0}\binom{2j+1+r}{2j+1}t^r
\]
gives coefficient \(\binom{m+2-j}{2j+1}\) at \(x^m z^{m+1+j}\); this coefficient is nonzero precisely when \(m\geq3j-1\). No other terms occur. This proves the complete length spectrum and both length endpoints.

**5. Total enumeration.** Set \(z=1\) in the rational expression and equate coefficients to obtain the displayed recurrence and initial values. The denominator has the unique dominant positive zero at \(\lambda^{-1}\) corresponding to the real root \(\lambda=1.754877666\ldots\); its other two reciprocal roots have smaller modulus. The numerator does not vanish there, proving the exponential growth statement.

## Verification

The included standalone standard-library program `verify.py` performs direct greedy membership tests of every binary candidate word at each \(1\leq m\leq8\), including each one-position deletion. It compares those tests with the local characterization and exact binomial counts. In total it examines 349,504 distinct candidate words and identifies 347 minimal absent words across these parameters. A separate four-state dynamic-programming implementation independently checks all length distributions for \(1\leq m\leq50\). Its actual output is in `verify_output.txt`. To reproduce, run `python3 verify.py` in the artifact directory.

These finite checks corroborate, but do not replace, the formal proof for all positive integers \(m\).

## Relationship to prior work

Manea, Ringleb, Siemer and Winkler (2025) give general optimal algorithms to enumerate shortest and minimal absent scattered subsequences and find a longest minimal absent subsequence. Kosche, Koß, Manea and Siemer (2021/2022) establish general canonical-embedding characterizations. Adamson and collaborators (2024) study counts of **all** absent subsequences at a specified length. The present statement is instead a fully explicit distribution of **minimal** absent scattered subsequences by length for every alternating binary word, together with the corresponding rational generating function and exponential total-growth law. The inspected primary works did not exhibit this exact formula; general algorithms alone do not state the closed form. A plausible 2023 paper by Troníček gives methods for counting minimal absent subsequences; its complete text was unavailable for comparison, leaving a material publication-priority risk.

## Limitations

The theorem is only about the binary, even-length alternating family \((01)^m\), not all periodic words, all binary words or alphabets of higher size. This is an exact mathematical enumeration; it is not an improved worst-case enumeration algorithm. Claims of novelty are provisional pending independent bibliographic review, especially of the inaccessible 2023 counting paper. No independent mathematical audit has been performed.

## References

1. F. Manea, T. Ringleb, S. Siemer and M. Winkler, *Efficiently Finding All Minimal and Shortest Absent Subsequences in a String*, arXiv:2504.21471, first public April 30, 2025. https://arxiv.org/abs/2504.21471
2. M. Kosche, T. Koß, F. Manea and S. Siemer, *Absent Subsequences in Words*, arXiv:2108.13968. https://arxiv.org/abs/2108.13968
3. D. Adamson et al., *Tight Bounds for the Number of Absent Subsequences*, arXiv:2407.18599. https://arxiv.org/abs/2407.18599
4. Z. Troníček, *On Problems Related to Absent Subsequences*, COCOA 2023, DOI:10.1007/978-3-031-49614-1_26. https://doi.org/10.1007/978-3-031-49614-1_26

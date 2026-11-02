# Exact second moments for shortest absent subsequences of random minimal universal words

## Finding
Fix integers \(q\geq2\) and \(k\geq1\), and a labeled alphabet \(\Sigma\) of cardinality \(q\). Independently choose uniform permutations \(P_1,\ldots,P_k\) of \(\Sigma\), form \(W=P_1\cdots P_k\), and let \(S_{q,k}\) be the number of distinct shortest absent subsequences of \(W\). This is the uniform distribution on all shortest-length \(k\)-subsequence-universal words (length \(qk\)). Put \(h_q=(q+1)/2\).

Then
\[
\mathbb E S_{q,k}=q h_q^k.
\]
The exact second moments \(v_{q,k}=\mathbb E S_{q,k}^2\), extended formally to \(k=0\) by \(S_{q,0}=q\), satisfy
\[
\begin{split}
v_{q,0}&=q^2,\\
v_{q,1}&=q^2h_q^2,\\
v_{q,k+2}&=\frac{(q+1)(3q+4)}{12}\,v_{q,k+1}
-\frac{(q+1)^2(q+2)}{72}\,v_{q,k}\quad(k\ge0).
\end{split}
\]
In particular, \(\operatorname{Var}(S_{q,k})=v_{q,k}-q^2h_q^{2k}\) is determined exactly for all \(q,k\). The two eigenvalues of the second-moment transfer are
\[
\lambda_\pm(q)=\frac{q+1}{24}\left(3q+4\pm\sqrt{q(9q+16)}\right).
\]
There is a positive constant \(C_q\), depending only on \(q\), for which
\[
\frac{\operatorname{Var}(S_{q,k})}{(\mathbb E S_{q,k})^2}
\sim C_q\left(\frac{3q+4+\sqrt{q(9q+16)}}{6(q+1)}\right)^k
\qquad(k\to\infty).
\]
The displayed base is strictly greater than one for every \(q\ge2\): **the relative variance grows exponentially** even in this minimal-length, fully universal ensemble.

## Assumptions and scope
A word \(u\) is a subsequence of \(w\) if its symbols may be read from increasing positions of \(w\), with gaps allowed. A word is \(k\)-universal if it contains every member of \(\Sigma^k\) as a subsequence. The shortest absent subsequences of a \(k\)-universal, non-\((k+1)\)-universal word are the absent words of length \(k+1\), counted as distinct words, **not** by multiplicity of embeddings.

Any \(k\)-universal word has at least \(k\) disjoint greedy complete-alphabet arches, each of length at least \(q\), so length at least \(qk\). Equality forces each arch to be a permutation and leaves no suffix. Conversely, any concatenation of \(k\) permutations is \(k\)-universal, but not \((k+1)\)-universal because each symbol occurs only \(k\) times. Hence the ensemble is precisely the set of all \((q!)^k\) labeled minimal-length universal words, each equally likely. The formal zero-block case is used only to state the second-moment recurrence uniformly.

## Proof
**1. Exact absence criterion.** For a permutation \(P\), let \(r_P(a)\in\{1,\ldots,q\}\) be the position of symbol \(a\). Define its \(q\)-by-\(q\) matrix
\[
H_P(a,b)=\mathbf1\{r_P(a)\ge r_P(b)\}.
\]
For a proposed subsequence \(x_1\cdots x_{k+1}\), greedy left-to-right matching within the first permutation always matches \(x_1\). It matches \(x_2\) in that block as well precisely when \(r_{P_1}(x_1)<r_{P_1}(x_2)\); equality cannot match twice because there is just one occurrence. If it matches two or more letters in any block, the remaining blocks each match at least one further letter, so by the end of block \(k\) the target has been completed. Conversely, if no block matches two letters, exactly one is matched per block and the final target letter remains absent. Therefore
\[
x_1\cdots x_{k+1}\text{ is absent from }W
\iff \bigwedge_{i=1}^{k}r_{P_i}(x_i)\ge r_{P_i}(x_{i+1}).
\]
It follows that
\[
S_{q,k}=\mathbf1^{\mathsf T}H_{P_1}\cdots H_{P_k}\mathbf1.
\]
This also proves that the matrix model counts different target words exactly once.

**2. Mean.** For different symbols \(a,b\), a random permutation puts \(a\) after \(b\) with probability one-half, while \(H_P(a,a)=1\). Thus
\[
\mathbb EH_P=\frac12(I+J),\qquad
(\mathbb EH_P)\mathbf1=h_q\mathbf1.
\]
Independence gives \(\mathbb ES_{q,k}=q h_q^k\).

**3. Second moment and invariant pair classes.** Set \(K=\mathbb E(H_P\otimes H_P)\). The tensor-product identity gives
\[
v_{q,k}=(\mathbf1\otimes\mathbf1)^{\mathsf T}K^k
(\mathbf1\otimes\mathbf1).
\]
Simultaneously relabeling both coordinates leaves \(K\) invariant. Consequently, vectors whose values depend only on whether an ordered pair of symbols \((a,c)\) is diagonal (\(a=c\)) or off-diagonal (\(a\ne c\)) form an invariant subspace. In the ordered basis (diagonal value, off-diagonal value), the induced transfer is
\[
T_q=
\begin{pmatrix}
\dfrac{q+1}{2}&\dfrac{q^2-1}{3}\\[3pt]
\dfrac{q+1}{3}&\dfrac{(q+1)(3q-2)}{12}
\end{pmatrix}.
\]
For completeness, each row sum can be checked directly. Write \(R_a=r_P(a)\) for a random rank. When \(a=c\), the sum over all \((b,d)\) of \(H_P(a,b)H_P(a,d)\) is \(R_a^2\), and the sum over just \(b=d\) is \(R_a\). Hence the expected diagonal and off-diagonal sums are \((q+1)/2\) and \((q^2-1)/3\). When \(a\ne c\), the full sum is \(R_aR_c\), whose expectation is \((q+1)(3q+2)/12\). Its diagonal part is \(\min(R_a,R_c)\), with expectation \((q+1)/3\); subtracting gives the other entry \((q+1)(3q-2)/12\). These rank expectations follow by summing the integers \(1,\ldots,q\) and their squares, or by ordering two distinct uniformly sampled ranks.

There are \(q\) diagonal pairs and \(q(q-1)\) off-diagonal pairs, so
\[
v_{q,k}=(q,\,q(q-1))T_q^k\binom11.
\]
The trace and determinant are exactly
\[
\operatorname{tr}T_q=\frac{(q+1)(3q+4)}{12},\qquad
\det T_q=\frac{(q+1)^2(q+2)}{72}.
\]
Cayley–Hamilton yields the stated recurrence. Since \(T_q(1,1)^{\mathsf T}\) has entries whose weighted sum equals \(q^2h_q^2\) at \(k=1\), the two initial values hold. Solving the quadratic characteristic equation gives the stated eigenvalues.

**4. Relative fluctuations.** For every \(q\ge2\), all entries of \(T_q\) are positive. Perron–Frobenius theory therefore implies
\[
v_{q,k}=A_q\lambda_+(q)^k+O_q(\lambda_-(q)^k),\qquad A_q>0.
\]
Here \(0<\lambda_-<\lambda_+\). Also
\[
\lambda_+(q)>h_q^2
\iff \sqrt{q(9q+16)}>3q+2,
\]
which holds because the difference of the squares is \(4(q-1)>0\). Dividing the variance by \(q^2h_q^{2k}\) gives the asserted asymptotic with \(C_q=A_q/q^2>0\). This finishes the proof.

## Verification
The supplied self-contained `verify.py` uses only the Python standard library (`fractions`, `itertools`). It computes the full \(q^2\)-by-\(q^2\) tensor transfer independently for \(q=2,3,4,5\), verifies every entry of its two-class reduction, and checks the moment recurrence through exponent eight. Separately, for \(q=2\) through six blocks, \(q=3\) through three blocks, and \(q=4\) through two blocks, it exhausts every concatenation of permutations and **independently tests all** candidate length-\(k+1\) subsequences using a literal greedy matching routine. It compares those direct counts with the proposed matrix formula and their exact rational first and second moments. Execute `python verify.py` from the directory containing the verifier; expected last line: `VERIFY_OK`.

Examples: for \((q,k)=(2,2)\), \(\mathbb ES=9/2\), \(\mathbb ES^2=41/2\), so \(\operatorname{Var}(S)=1/4\). For \((q,k)=(3,2)\), the corresponding values are \(12\), \(146\), and \(2\). The all-parameter conclusion relies on the exact rank-moment proof, not on this finite verification.

## Relationship to prior work
Kosche, Koß, Manea, and Siemer (arXiv:2108.13968, first public 31 August 2021) establish fundamental characterizations and arch-factorization tools for shortest absent subsequences and optimize their counts for fixed universality index. Adamson, Fleischmann, Huch, and Wiedenhöft (arXiv:2407.18599v1, 26 July 2024) characterize extremal *minimum and maximum* counts for absent scattered factors, including minimal perfect universal words. Neither inspected paper evaluates mean or second moment in the **uniform ensemble of all minimal-length universal words**. The related published Fibonacci-extremal binary finding (published-finding corpus identifier `2026/10/4/SCOPE-fibonacci-extremals-for-shortest-absent-subsequences-of-binary-w--1a6556f14d28`) determines a *maximum*, not a distributional second moment. Existing transfer methods motivate the derivation; the new assertion is the exact distributional moment hierarchy and exponential relative-variance consequence, not novelty of transfer matrices themselves.

## Limitations
The theorem concerns the **uniform permutation-arch ensemble**, not uniform unrestricted random words of length \(qk\). It gives the first two moments and relative-variance asymptotics, not the full distribution, higher moments, large deviations, or a central limit theorem. Growing relative variance alone does not prove any particular tail shape. The closest accessible literature was compared by claims, but an equivalent statement in unindexed work remains a possible priority risk. All computational checks are finite; the mathematical proof is independent of their cutoff.

## References
1. M. Kosche, T. Koß, F. Manea, and S. Siemer, *Absent Subsequences in Words*, arXiv:2108.13968v1, first public 31 August 2021; full text arXiv:2108.13968v6, https://arxiv.org/html/2108.13968v6.
2. D. Adamson, P. Fleischmann, A. Huch, and M. Wiedenhöft, *Tight Bounds for the Number of Absent Scattered Factors*, arXiv:2407.18599v1, first public 26 July 2024, https://arxiv.org/html/2407.18599v1.
3. *Fibonacci extremals for shortest absent subsequences of binary words*, published research record, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-fibonacci-extremals-for-shortest-absent-subsequences-of-binary-w--1a6556f14d28.

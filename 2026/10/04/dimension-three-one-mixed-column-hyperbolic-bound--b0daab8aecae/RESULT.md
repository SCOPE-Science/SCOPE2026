# Dimension-three one-mixed-column hyperbolic bound
## Finding
Let \(G\) be a systematic \([n,3]\) linear code over an arbitrary finite field. Partition its information space as \(F_1\oplus F_2\) with \(\dim F_1=1\) and \(\dim F_2=2\). If exactly one nonzero column of \(G\) is mixed, meaning that it lies in neither \(F_1\) nor \(F_2\), then the expected uniform-with-replacement file-retrieval times satisfy
\[
\frac{1}{E_1(G)}+\frac{2}{E_2(G)}\le 1.
\]
The same statement holds after swapping the two files. Zero columns, if present, do not invalidate the inequality.

## Assumptions and scope
Sampling is uniform with replacement from the \(n\) code coordinates. File \(F_i\) is recovered once the span of the sampled generator columns contains the whole file subspace \(F_i\). The code is systematic relative to the file partition, so each file has a pure basis among the columns. A nonzero column is *mixed* when both of its file projections are nonzero. The result treats total information dimension three and exactly one mixed nonzero column; it makes no claim for two or more mixed columns.

Zero columns can be removed first. If \(z\) columns are zero and \(G'\) is obtained by deleting them, then useful nonzero draws are obtained from the original sampler by geometric thinning, so
\[
E_i(G)=\frac{n}{n-z}E_i(G').
\]
Consequently the left-hand side for \(G\) is \((n-z)/n\) times the corresponding left-hand side for \(G'\). It therefore suffices to prove the theorem when every column is nonzero.

## Proof
Apply an invertible change of basis separately within \(F_1\) and \(F_2\), and rescale columns by nonzero field elements. These operations preserve every span-containment recovery event. Write \(F_1=\langle e_1\rangle\), identify \(F_2\) with a two-dimensional plane, and normalize the unique mixed column to
\[
m=e_1+w,
\]
where \(0\ne w\in F_2\).

Let \(a\ge1\) be the number of pure \(F_1\) columns. Among the pure \(F_2\) columns, let \(L_0=\langle w\rangle\) have multiplicity \(c\ge0\), and let the other occupied projective lines \(L_1,\ldots,L_r\) have positive multiplicities \(x_1,\ldots,x_r\). Put
\[
d=\sum_{j=1}^r x_j,\qquad b=c+d,\qquad n=a+b+1.
\]
Systematicity of the two-dimensional file implies \(d\ge1\): pure \(F_2\) columns cannot all lie on \(L_0\).

For \(F_1\), failure after \(t\ge1\) draws occurs when no pure \(F_1\) column has appeared and either the mixed column has not appeared, or it has appeared while the sampled pure \(F_2\) columns do not span \(w\). In a two-dimensional plane, the latter means that no \(L_0\) column has appeared and all sampled non-\(L_0\) pure columns lie on at most one \(L_j\). Summing the resulting failure probabilities over \(t\) gives the exact formula
\[
E_1=rac{n}{a+1}+
\sum_{j=1}^r\frac{n}{(n-x_j-1)(n-x_j)}-rac{r-1}{n-1}.
\]
Equivalently,
\[
E_1=rac{n}{a+1}+rac{1}{n-1}+
\sum_{j=1}^r\phi(x_j),
\]
where
\[
\phi(x)=\frac{n}{(n-x-1)(n-x)}-\frac{1}{n-1}.
\]

For \(F_2\), failure occurs when the sampled pure \(F_2\) columns span at most one projective line. If that line is \(L_0\), recovery is impossible. If it is \(L_j\ne L_0\), recovery succeeds exactly when both a pure \(F_1\) column and the mixed column have appeared, because their difference supplies \(w\), which together with \(L_j\) spans \(F_2\). The same failure-probability summation yields
\[
E_2=rac{n}{d}+
\sum_{j=1}^r\left[
\frac{n}{(n-x_j-1)(n-x_j)}+
\frac{n x_j}{(n-a-x_j)(n-a)}-
\frac{1}{n-1}
\right].
\]
Thus
\[
E_2=rac{n}{d}+
\sum_{j=1}^r\psi(x_j),
\qquad
\psi(x)=\phi(x)+\frac{n x}{(n-a-x)(n-a)}.
\]

Both correction functions are superadditive on the positive integers. Indeed, their convergent power-series forms are
\[
\phi(x)=\sum_{t\ge1}
\frac{(x+1)^t-x^t-1}{n^t},
\]
and
\[
\psi(x)=\phi(x)+
\sum_{t\ge1}\frac{(a+x)^t-a^t}{n^t}.
\]
For every fixed \(t\), each numerator is a nonnegative convex sequence in \(x\) that vanishes at \(x=0\); hence it is superadditive on \(\mathbb Z_{\ge0}\). Therefore
\[
\phi(x)\ge x\phi(1),\qquad
\psi(x)\ge x\psi(1).
\]
Using
\[
\beta=\phi(1)=\frac{2}{(n-2)(n-1)},
\qquad
\psi(1)=\beta+\frac{n}{b(b+1)},
\]
we obtain the lower bounds
\[
E_1\ge E_1^*=rac{n}{a+1}+rac{1}{n-1}+d\beta,
\]
\[
E_2\ge E_2^*=rac{n}{d}+d\left(\beta+\frac{n}{b(b+1)}\right).
\]
It remains only to prove
\[
\frac{1}{E_1^*}+\frac{2}{E_2^*}\le1.
\]
Set \(A=a+1\), so \(A\ge2\), and note \(n=A+b\). Clearing the positive denominators gives the polynomial inequality
\[
\mathcal P(A,b,d)\ge0,
\]
where \(\mathcal P\) is the numerator of
\[
E_1^*E_2^*-E_2^*-2E_1^*.
\]
Write \(A=u+2\), \(d=v+1\), and \(b=d+c=v+w+1\), with \(u,v,w\ge0\). These substitutions encode exactly the whole parameter domain. There are two exhaustive cases. If \(u\ge v\), write \(u=v+z\); if \(v\ge u\), write \(v=u+z\). In the first case the exact expansion of \(\mathcal P\) has 143 monomials and in the second it has 148 monomials, and every coefficient is a positive integer. Hence \(\mathcal P\ge0\) in both cases. The accompanying verifier constructs \(\mathcal P\) from the displayed rational formulas using integer polynomial arithmetic and checks these coefficient certificates directly; this is a parametric algebraic certificate, not a finite search over parameters.

Because reciprocals decrease when their positive denominators increase,
\[
\frac{1}{E_1}+\frac{2}{E_2}
\le
\frac{1}{E_1^*}+\frac{2}{E_2^*}
\le1,
\]
which proves the claim.

## Verification
The standalone verifier performs three independent checks. First, it reconstructs the cleared polynomial certificate using only integer polynomial arithmetic and confirms that both exhaustive parameter substitutions have strictly positive coefficients. Second, it evaluates the exact formulas over many multiplicity patterns using rational arithmetic and confirms the superadditive lower bounds and final inequality. Third, it builds the sampled-span Markov chain directly over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_5\) for five representative one-mixed-column codes and confirms that the Markov expectations equal the closed formulas exactly. Running `python3 verify_one_mixed.py` prints `VERIFY_OK`.

The finite-field checks are supplementary. The proof for all finite fields and all lengths is supplied by the failure-probability formulas, superadditivity argument, and the symbolic nonnegative-coefficient certificate.

## Relationship to prior work
Bar-Lev introduced the two-file block-retrieval model and conjectured the hyperbolic inequality for every linear code whenever at least one file has dimension at least two. The March 2026 paper proves the inequality when there are no mixed columns and leaves mixed columns as the main obstruction.

A later September 2026 preprint by Vlachos and Bar-Lev proves the conjecture whenever the total information dimension \(k\) and number of mixed columns \(m_{\mathrm{mix}}\) satisfy \(k\ge2m_{\mathrm{mix}}+2\). For one mixed column that theorem starts at \(k\ge4\), so it does not imply the present \(k=3\), file-dimension \((1,2)\) case. Focused literature and semantic-database searches found no statement covering this remaining one-mixed-column boundary case.

## Limitations
The proof uses the fact that the larger file has dimension exactly two: failure of its pure columns to span the file is then described by a single projective line, which makes the multiplicity formulas one-dimensional. The argument does not establish the conjecture for total dimension three with two or more mixed columns, nor does it replace the higher-dimensional mixed-column theorem. Literature searches reduce but cannot eliminate the possibility of an unindexed equivalent result.

## References
1. D. Bar-Lev, “Coded Information Retrieval for Block-Structured DNA-Based Data Storage,” arXiv:2603.17154v1, 17 March 2026; revised as v2 on 19 July 2026.
2. C. V. A. Vlachos and D. Bar-Lev, “A Hyperbolic Bound for File Retrieval in DNA-Based Data Storage,” arXiv:2609.36067v1, 28 September 2026.

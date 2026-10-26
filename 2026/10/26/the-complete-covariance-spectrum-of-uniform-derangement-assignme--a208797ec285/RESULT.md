# The complete covariance spectrum of uniform derangement assignment scores

## Finding

Let \(\Pi\) be a uniformly chosen fixed-point-free permutation of \([n]\), for any integer \(n\ge 3\). The \(n(n-1)\)-dimensional vector of off-diagonal permutation-matrix indicators \(X_{ij}=\mathbf 1\{\Pi(i)=j\}\), \(i\ne j\), has a covariance matrix with **exactly two possible positive eigenvalues**. For \(n\ge 4\), the complete spectrum, including multiplicities, is

\[
\begin{array}{c|c}
\text{eigenvalue}&\text{multiplicity}\\\hline
0&2n-1\\
\lambda_+=\frac{1}{n-1}+\frac{1}{(n-1)^2}+\frac{nD_{n-3}}{(n-1)D_n}+\frac{2D_{n-4}}{D_n}&\frac{n(n-3)}2\\
\lambda_-=\frac{1}{n-1}+\frac{1}{(n-1)^2}+\frac{nD_{n-3}}{(n-1)D_n}&\frac{(n-1)(n-2)}2.
\end{array}
\]

Here \(D_m\) counts derangements of \(m\) objects, with \(D_0=1\) and \(D_1=0\). The eigenvectors for \(\lambda_+\) are symmetric zero-diagonal matrices with every row sum zero; those for \(\lambda_-\) are skew-symmetric zero-diagonal matrices with every row sum zero. The zero eigenspace is precisely the row/column-potential space \(A_{ij}=u_i+v_j\). For \(n=3\), the zero eigenvalue has multiplicity five and the sole positive eigenvalue is \(3/2\), of multiplicity one.

In particular, for \(n\ge4\),

\[
\lambda_+-\lambda_-=\frac{2D_{n-4}}{D_n},
\]

so the nontrivial covariance is a scalar multiple of the identity **if and only if \(n=5\)**; in that case both eigenvalues equal \(15/44\), on an \(11\)-dimensional space. For \(n=4\) and every \(n\ge6\), symmetric scores have strictly larger variance per unit squared norm than skew-symmetric scores. The spectral gap is asymptotic to \(2/n^4\).

Equivalently, if \(A\) is any real zero-diagonal matrix with every row and column sum zero and \(A_+=(A+A^\top)/2\), \(A_-=(A-A^\top)/2\), then the exact assignment-score variance is

\[
\operatorname{Var}\!\left(\sum_{i=1}^n A_{i,\Pi(i)}\right)
=\lambda_+\|A_+\|_F^2+\lambda_-\|A_-\|_F^2,
\]

where the symmetric term is absent when \(n=3\). Arbitrary score matrices reduce to this formula after orthogonally removing their row/column-potential component.

## Assumptions and scope

The probability space consists of all \(D_n\) derangements of \([n]\), with equal weights and \(n\ge3\). The covariance matrix is indexed by ordered pairs of **different** labels \((i,j)\). Diagonal entries of the permutation matrix are identically zero and excluded. All assertions are finite-dimensional and exact; no asymptotic assumption is needed except for the quoted eigenvalue-gap estimate.

## Proof

**1. Counting one and two prescribed edges.** The standard recurrence is \(D_m=(m-1)(D_{m-1}+D_{m-2})\) for \(m\ge2\), with \(D_0=1,D_1=0\). Simultaneous relabeling makes every off-diagonal edge equiprobable, hence \(p:=\mathbb E X_{ij}=1/(n-1)\). For two distinct edges in different rows and columns, let \(h\) be the number of distinct numerical labels among their four endpoints. Removing their two prescribed rows and columns leaves an \((n-2)\)-square board with exactly \(n-h\) forbidden diagonal cells, in distinct rows and columns. Inclusion-exclusion yields

\[
B_h=\sum_{t=0}^{n-h}(-1)^t\binom{n-h}{t}(n-2-t)!.
\]

Reorganizing by the missing forbidden cells gives \(B_2=D_{n-2}\), \(B_3=D_{n-2}+D_{n-3}\), and \(B_4=D_{n-2}+2D_{n-3}+D_{n-4}\) (only physically possible values of \(h\) are used). Define

\[
r=\frac{D_{n-3}}{(n-1)D_n},\qquad s=\frac{D_{n-4}}{D_n}\quad(n\ge4).
\]

From \(D_n=(n-1)^2D_{n-2}+(n-1)(n-2)D_{n-3}\), the covariances for different indicators become: \(-p^2\) if the two edges share a row or a column; \(-(n-2)r\) if they form a reciprocal two-cycle; \(r\) if they form a directed two-edge chain on three labels; and \(nr+s\) if their four numerical labels are distinct. Each diagonal covariance is \(p(1-p)\). For \(n=3\), the last class is absent and no \(s\) is needed.

**2. The deterministic kernel.** In every derangement, each row and column contains exactly one selected edge. Thus any coefficient matrix \(A\) of the form \(A_{ij}=u_i+v_j\) makes \(\sum_i A_{i,\Pi(i)}\) constant. The potential subspace \(U\) has dimension \(2n-1\) for \(n\ge3\). Its perpendicular complement \(W\) consists exactly of zero-diagonal matrices with zero row and column sums. The direct symmetric/skew decomposition \(W=W_+\oplus W_-\) has dimensions \(n(n-3)/2\) and \((n-1)(n-2)/2\), because the unsigned complete-graph incidence map has rank \(n\), while the oriented incidence map has rank \(n-1\).

**3. Covariance action on \(W\).** Fix \((i,j)\) with \(i\ne j\) and \(A\in W\). The sum of coefficients at edges sharing a row or column with \((i,j)\), except itself, equals \(-2A_{ij}\). The unique reciprocal edge contributes \(A_{ji}\); the two chain classes have aggregate coefficient \(-2A_{ji}\); and the remaining disjoint-label edges have aggregate coefficient \(A_{ij}+A_{ji}\). Substituting the four covariance values gives the **exact operator identity**

\[
(\Sigma A)_{ij}=\left(p+p^2+nr+s\right)A_{ij}+sA_{ji}.
\]

Thus \(\Sigma\) acts by \(\lambda_+=p+p^2+nr+2s\) on \(W_+\), and by \(\lambda_-=p+p^2+nr\) on \(W_-\). Both are positive, so there are no further kernel vectors. For \(n=3\), \(W_+\) has dimension zero and direct substitution gives \(\lambda_-=3/2\). Frobenius orthogonality proves the variance formula.

**4. Exceptional isotropy and asymptotics.** For \(n\ge4\), the gap is \(2s\). It vanishes exactly when \(D_{n-4}=0\), i.e. when \(n-4=1\) and \(n=5\); all other derangement numbers with nonnegative indices are positive. Directly \(D_5=44\) and \(D_2=1\), giving \(\lambda_+=\lambda_-=15/44\). Since \(D_m/m!\to e^{-1}\), the gap \(2D_{n-4}/D_n\sim 2/[n(n-1)(n-2)(n-3)]\sim 2/n^4\).

## Verification

The included `check.py` exhaustively enumerates every derangement for sizes \(3\le n\le8\), independently counts all one- and two-edge incidences with rational arithmetic, and compares the resulting covariances with the formulas by row/column/reciprocal/chain/disjoint class. It also tests the covariance-operator eigen-equations against independent symmetric and skew score matrices. Exactly **3,771 assertions** passed. This finite verification does not replace the all-size proof above.

## Relationship to prior work

The model is motivated by da Silva, Jamshidpey and Tavaré (2022), which treats biased derangement generation, cycle structures and limit laws, rather than the full incidence covariance operator. The unrestricted rook-theoretic prescribed-prefix count is established by Kagey (2022), especially Corollary 22; accordingly the prescribed-edge counts here are treated as consequences of prior counting techniques, **not** as separately original. Diaconis, Graham and Holmes (2001) study restricted permutations and permutation-test statistics in broad generality and provide the relevant statistical framework. The contribution here is the full two-eigenvalue covariance classification, exact symmetric/skew score-variance law and unique \(n=5\) isotropy phenomenon; these are not asserted by the inspected sources.

## Limitations

No claim of priority for rook inclusion-exclusion, the derangement count, or elementary one-edge expectations is made. The theorem is specific to the uniform measure on permutations with every diagonal assignment forbidden. It does not give a Gaussian approximation, concentration bound, or weighted restricted-permutation spectrum. Historical priority of the spectral classification requires independent checking. A finite computational check cannot establish the unrestricted theorem by itself.

## References

1. Poly H. da Silva, Arash Jamshidpey, and Simon Tavaré, *Markov chains arising from biased random derangements* (first public 2022-11-24), arXiv:2211.13831, https://arxiv.org/abs/2211.13831 .
2. Peter Kagey, *Ranking and Unranking Restricted Permutations* (first public 2022-10-31), arXiv:2210.17021, especially Corollary 22, https://arxiv.org/abs/2210.17021 .
3. Persi Diaconis, Ronald Graham, and Susan P. Holmes, *Statistical problems involving permutations with restricted positions*, Institute of Mathematical Statistics Lecture Notes–Monograph Series **36** (2001), pp. 195–222, DOI 10.1214/lnms/1215090070, https://dornsife.usc.edu/sergey-lototsky/wp-content/uploads/sites/211/2023/06/euclid.lnms_.1215090070.pdf .

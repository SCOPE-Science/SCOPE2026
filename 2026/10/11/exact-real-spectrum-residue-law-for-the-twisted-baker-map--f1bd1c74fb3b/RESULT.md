# Exact real-spectrum residue law for the twisted baker map

## Finding
For every integer dimension \(M\geq2\) and every integer \(n\geq1\), consider the nontrivial fixed points of the \(n\)-th iterate of the twisted baker map. If \(k\geq1\) is the number of visits to its right branch in a length-\(n\) symbolic itinerary, then **every eigenvalue of the iterate Jacobian is real if and only if \(M\mid k\)**. Otherwise at least one conjugate pair of eigenvalues is nonreal.

Writing \(R_M(n)\) for the number of nontrivial fixed points of the \(n\)-th iterate with entirely real Jacobian spectrum, and \(C_M(n)\) for those with nonreal spectrum, the exact counts are
\[
R_M(n)=\sum_{\substack{0\leq j\leq n\\j\equiv0\pmod M}}\binom{n}{j}-1,\qquad
C_M(n)=2^n-\sum_{\substack{0\leq j\leq n\\j\equiv0\pmod M}}\binom{n}{j}.
\]
For every fixed \(M\geq2\), they satisfy
\[
\lim_{n\to\infty}\frac{R_M(n)}{2^n-1}=\frac1M,\qquad
\lim_{n\to\infty}\frac{C_M(n)}{2^n-1}=\frac{M-1}{M}.
\]
More sharply, for every \(n\geq1\),
\[
\left|R_M(n)-\left(\frac{2^n}{M}-1\right)\right|
\leq \frac{M-1}{M}\left(2\cos\frac{\pi}{M}\right)^n.
\]
For \(M=2\), the error vanishes identically.

The complete characteristic-polynomial structure is also explicit. For the above point put \(g=\gcd(k,M)\) and \(\ell=M/g\). There are nonnegative integers \(a_1,\ldots,a_g\), determined by the particular itinerary and satisfying \(\sum_{h=1}^g a_h=n\), such that
\[
\det(\lambda I-D F^n(x))=
\prod_{h=1}^{g}\left(\lambda^{\ell}-(-1)^{k/g}2^{a_h}\right).
\]
The real-versus-nonreal criterion does not require knowing those integers.

## Assumptions and scope
Fix \(M\geq2\) and set \(X=[-1,1]\times[0,1]^{M-1}\). The map \(F:X\to X\) is the piecewise-affine map
\[
F(x_1,\ldots,x_M)=
\begin{cases}
(1+2x_1,x_2,\ldots,x_M),&x_1<0,\\
(1-2x_M,x_1,\ldots,x_{M-1}),&x_1\geq0.
\end{cases}
\]
Let \(N=\{x\in X:x_1=-1\}\); this is the nonisolated fixed-point face. In keeping with the originating formulation, \(\operatorname{Fix}(n)=\{x\in X\setminus N:F^n(x)=x\}\) counts *fixed points of the iterate*, not only points of least period \(n\). Derivatives at partition faces use the one-sided derivative selected by the branch convention. The terms **real-spectrum** and **nonreal-spectrum** refer to the spectrum of \(D F^n(x)\), counting complex eigenvalues with algebraic multiplicity.

## Proof
**Step 1: symbolic fixed points.** Denote the left and right branches by \(L\) and \(R\). Their inverse affine branches, on their natural rectangles, are
\[
G_L(y_1,\ldots,y_M)=\left(\frac{y_1-1}{2},y_2,\ldots,y_M\right),\qquad
G_R(y_1,\ldots,y_M)=\left(y_2,\ldots,y_M,\frac{1-y_1}{2}\right).
\]
For a binary word of length \(n\) containing at least one \(R\), a repeated inverse itinerary rotates every coordinate through a halving coordinate; in particular its \(M\)-fold repetition is contracting in the maximum norm. Consequently the infinite periodic itinerary determines a unique nontrivial fixed point of \(F^n\). The symbolic-coding theorem and the absence of nontrivial periodic boundary ambiguities are proved in Saiki–Takahasi–Yorke, Lemmas 2.4–2.6. Thus the binary words containing at least one \(R\) biject with \(\operatorname{Fix}(n)\), giving \(\#\operatorname{Fix}(n)=2^n-1\). The excluded word \(L^n\) corresponds to the fixed face \(N\), rather than to an additional isolated periodic point.

**Step 2: a signed monomial cocycle.** Relative to the standard coordinate vectors \(e_j\), the branch Jacobians satisfy
\[
D F_L=\operatorname{diag}(2,1,\ldots,1),\qquad
D F_R e_j=\begin{cases}
e_{j+1},&1\leq j<M,\\-2e_1,&j=M.
\end{cases}
\]
Thus the iterate Jacobian \(A=D F^n(x)\) is a signed monomial matrix. The underlying permutation is addition of \(k\) modulo \(M\) (each right visit advances a coordinate index once, and each left visit preserves it). This permutation decomposes into \(g=\gcd(k,M)\) disjoint cycles, each of length \(\ell=M/g\).

For a fixed permutation cycle, follow a coordinate vector through \(\ell\) applications of the full length-\(n\) itinerary. It makes \(\ell k\) right advances and hence exactly \(\ell k/M=k/g\) complete wraps; each wrap contributes precisely one minus sign. Each branch Jacobian contributes a single factor of magnitude two to the determinant of the full iterate, so the positive product of the weights on a cycle is an integer power of two. Write that magnitude as \(2^{a_h}\). The product over all cycles has magnitude \(|\det A|=2^n\), whence \(a_h\geq0\) and \(\sum_h a_h=n\). The characteristic polynomial of a weighted \(\ell\)-cycle is its monomial polynomial, proving the displayed factorization.

**Step 3: exhaustive real-spectrum criterion.** If \(M\mid k\), then \(\ell=1\); the matrix is diagonal, with nonzero real eigenvalues. Suppose \(M\nmid k\), so \(\ell\geq2\). If \(\ell\geq3\), the equation \(\lambda^{\ell}=c\) for any nonzero real \(c\) has nonreal roots. If \(\ell=2\), then \(k/g\) is odd, because \(\gcd(k/g,\ell)=1\). Consequently every cycle has polynomial \(\lambda^2+2^{a_h}\) and a nonreal conjugate pair. These alternatives prove both directions for every \(M\) and every possible residue of \(k\).

**Step 4: exact counting and asymptotics.** There are \(\binom nk\) binary length-\(n\) words with exactly \(k\) right symbols. Count those with \(M\mid k\), removing the all-left word once, to obtain \(R_M(n)\); the complementary count is \(C_M(n)\). For \(\zeta=e^{2\pi i/M}\), the roots-of-unity filter gives
\[
\sum_{\substack{0\leq j\leq n\\M\mid j}}\binom nj
=\frac1M\sum_{s=0}^{M-1}(1+\zeta^s)^n.
\]
Since \(|1+\zeta^s|\leq2\cos(\pi/M)<2\) for \(1\leq s<M\) when \(M>2\), the error bound and both limiting proportions follow. For \(M=2\), the nonprincipal term is zero for \(n\geq1\), giving the asserted exact equality.

## Verification
The mathematical proof covers all integers \(M\geq2\) and \(n\geq1\), not just a finite sample. As independent finite consistency checks, `check_spectrum.py` constructs each non-all-left word for \(2\leq M\leq6\) and \(1\leq n\leq6\), solves the corresponding affine periodic-point equations with exact rational arithmetic, verifies the actual branch itinerary and return, checks the full characteristic-polynomial factorization, and matches the exact binomial residue counts. It prints `CHECK_OK`. Run `python -m pip install -r requirements.txt` and then `python check_spectrum.py`.

## Relationship to prior work
Saiki, Takahasi and Yorke introduced this map and established the coding, the total \(2^n-1\) count, and the real/nonreal distinction. Their Lemmas 2.2 and 2.3 prove real spectra when the twist count is divisible by \(M\) and nonreal spectra for the two adjacent nonzero residue classes. Their Proposition 2.7 gives only lower limiting proportions. The present signed-cycle argument resolves every remaining residue (notably the additional cases present when \(M\geq4\)) and supplies exact counts and sharp exponential convergence, rather than only lower asymptotic bounds. Related heterochaos baker-map periodic-point distributions studied by Takahasi in 2024 concern a different family and do not give this signed cyclic Jacobian criterion.

## Limitations
This statement concerns only the specified piecewise-affine twisted baker map and nontrivial fixed points of its iterates. It does not classify fine Lyapunov-exponent distributions, least-period orbit counts, or the periodic-point spectra of general baker maps. The proof uses established coding for the exact correspondence between itinerary words and periodic points; finite symbolic checks do not independently certify that correspondence for unbounded dimensions. Priority comparisons identify no equivalent classification in the inspected works but cannot rule out unindexed equivalent deductions from general signed-permutation matrix theory.

## References
1. Y. Saiki, H. Takahasi, and J. A. Yorke, *The twisted baker map*, arXiv:2202.04304, first posted 9 February 2022, revised version 3 of 13 January 2023; journal DOI: 10.1088/1361-6544/acb4d3. In particular Sections 2.1–2.3, Lemmas 2.1–2.6, and Proposition 2.7.
2. H. Takahasi, *Distributions of periodic points for the Dyck shift and the heterochaos baker maps*, arXiv:2409.01261, first posted 2 September 2024, especially the introduction and main periodic-point distribution statements.

# Exact biased-binary second moments of distinct scattered-subsequence counts

## Finding
For independent binary symbols with \(\Pr(1)=p\in(0,1)\), the number \(C_n\) of *distinct scattered subsequences*, **including the empty word**, has an exact rational second-moment generating function and an exponentially increasing squared coefficient of variation. Set \(t=p(1-p)\), \(s=\sqrt t\), and define the shifted count \(H_n=C_n+1\). Then
\[
\mathbb E H_n=\mu_n=\left(1+\frac1{2s}\right)(1+s)^n+\left(1-\frac1{2s}\right)(1-s)^n.
\]
The second moment \(M_n=\mathbb E H_n^2\) satisfies
\[
M_0=4,\qquad M_1=9,\qquad M_2=16+18t,
\]
\[
M_{n+3}=3M_{n+2}-(3-5t)M_{n+1}+(1-3t)M_n\quad(n\ge0),
\]
and hence
\[
\sum_{n\ge0}M_nz^n=\frac{4-3z+(1-2t)z^2}{1-3z+(3-5t)z^2-(1-3t)z^3}.
\]
Thus \(\operatorname{Var}(C_n)=M_n-\mu_n^2\), while \(\mathbb E C_n=\mu_n-1\).

Writing \(\rho(p)\) for the largest real root of \(\lambda^3-3\lambda^2+(3-5t)\lambda-(1-3t)\), one has
\[
\rho(p)>(1+\sqrt t)^2,\qquad
\frac{\operatorname{Var}(C_n)}{(\mathbb E C_n)^2}=\Theta_p\!\left(\left[\frac{\rho(p)}{(1+\sqrt t)^2}\right]^n\right)\xrightarrow[n\to\infty]{}\infty.
\]
In particular, normalized distinct-subsequence counts do not concentrate in relative \(L^2\) about their means. At \(p=1/2\), the simplified formula is
\[
\operatorname{Var}(C_n)=\left(2+\frac8{\sqrt{17}}\right)\left(\frac{5+\sqrt{17}}4\right)^n+\left(2-\frac8{\sqrt{17}}\right)\left(\frac{5-\sqrt{17}}4\right)^n-4\left(\frac94\right)^n.
\]

## Assumptions and scope
The sample is a binary word \(W_n\) of length \(n\ge0\) with mutually independent letters, probability \(p\) of \(1\), and probability \(1-p\) of \(0\). Two subsequences are distinguished by their resulting symbol strings, *not* by selecting different index sets. The empty word is counted; omitting it changes \(C_n\) by a constant and leaves variance unchanged. The infinite asymptotic statement holds for each fixed \(0<p<1\), not uniformly as \(p\) approaches either endpoint. For \(p=0\) or \(1\) the count is deterministic \(n+1\), so variance is zero.

## Proof
For a deterministic prefix, let \(A\) and \(B\) denote the numbers of distinct *nonempty* subsequences ending in \(0\) and \(1\), respectively. Initially \(A=B=0\). Appending \(0\) replaces \(A\) by \(1+A+B\) and does not change \(B\), because exactly one fresh word is formed for every previous subsequence (including the empty one) by appending \(0\). Appending \(1\) gives the symmetric update. Put \(U=A+1\) and \(V=B+1\). Initially \((U,V)=(1,1)\), the two updates are
\[
0:(U,V)\mapsto(U+V,V),\qquad1:(U,V)\mapsto(U,U+V),
\]
and \(C_n=U+V-1\), so \(H_n=U+V\).

Put \(q=1-p\). By independence of the next letter, the expectation vector obeys
\[
\binom{\mathbb E U_{n+1}}{\mathbb E V_{n+1}}=\begin{pmatrix}1&q\\p&1\end{pmatrix}\binom{\mathbb E U_n}{\mathbb E V_n}.
\]
The matrix eigenvalues are \(1\pm s\), and the sum of components equals \(2\) at \(n=0\) and \(3\) at \(n=1\). Solving these two scalar initial conditions gives the asserted \(\mu_n\).

Let \(X_n=\mathbb E U_n^2\), \(Y_n=\mathbb E(U_nV_n)\), and \(Z_n=\mathbb E V_n^2\). Squaring the two updates gives
\[
\begin{pmatrix}X_{n+1}\\Y_{n+1}\\Z_{n+1}\end{pmatrix}=T_p\begin{pmatrix}X_n\\Y_n\\Z_n\end{pmatrix},\qquad
T_p=\begin{pmatrix}1&2q&q\\p&1&q\\p&2p&1\end{pmatrix},\qquad(X_0,Y_0,Z_0)=(1,1,1).
\]
Consequently \(M_n=X_n+2Y_n+Z_n\), \(M_0=4\), \(M_1=9\), and \(M_2=16+18t\) (the last follows also by distinguishing equal and unequal adjacent letters). Direct expansion yields
\[
\det(\lambda I-T_p)=\lambda^3-3\lambda^2+(3-5t)\lambda-(1-3t).
\]
The Cayley–Hamilton identity, applied to the initial column and then the output row, proves the stated order-three recurrence. The standard generating-function calculation produces the displayed rational function. Shifting by one does not change variance, hence \(\operatorname{Var}(C_n)=\operatorname{Var}(H_n)=M_n-\mu_n^2\).

It remains to verify the strict exponential inequality, rather than infer it from finite experiments. All entries of \(T_p\) are strictly positive for \(p\in(0,1)\). Perron–Frobenius therefore gives a simple positive dominant eigenvalue \(\rho(p)\) with positive left and right eigenvectors. As the initial vector and output row are strictly positive, \(M_n=K_p\rho(p)^n(1+o(1))\) with \(K_p>0\). Let \(s=\sqrt t\), so \(0<s\le1/2\), and evaluate the characteristic polynomial at \(r=(1+s)^2\):
\[
\det(rI-T_p)=s^2(s^4+6s^3+7s^2-2s-2).
\]
For \(0<s\le1/2\), the parenthesis \(f(s)=s^4+6s^3+7s^2-2s-2\) is negative: \(f\) is strictly convex since \(f\prime\prime(s)=12s^2+36s+14>0\), whereas \(f(0)=-2\) and \(f(1/2)=-7/16\). Every value between these endpoints is bounded above by their negative secant interpolation. Therefore the real cubic, positive for sufficiently large arguments, has a real root strictly above \(r\); the Perron eigenvalue bounds the modulus of every eigenvalue, giving \(\rho(p)>r\). Meanwhile \(\mu_n\sim(1+1/(2s))(1+s)^n\); this proves the exponential relative-variance claim. The equiprobable closed form follows by the factorization \(\det(\lambda I-T_{1/2})=(\lambda-1/2)(\lambda^2-(5/2)\lambda+1/2)\) and the displayed initial values; its \(1/2\) eigenmode cancels in \(M_n\).

## Verification
A standalone verifier `verify.py` constructs full sets of scattered subsequences independently of the moment matrices for each binary string of length through \(10\). It weights each word exactly by the rational Bernoulli probabilities \(1/4\), \(1/3\), \(2/5\), \(1/2\), and \(3/4\), and compares exact means, second moments, and variances with the theorem. It also checks the characteristic identity symbolically when SymPy is available. Successful finite checks do not establish the theorem for arbitrary length; that follows from the word-update identities and Cayley–Hamilton argument above.

## Relationship to prior work
Collins (arXiv:1310.7288, 2013) proved the unbiased mean \(\mathbb E C_n=2(3/2)^n-1\). Biers-Ariel, Godbole, and Kelley (arXiv:1704.08661, initial release April 27, 2017) generalized means to biased binary sources and explicitly identified concentration widths as a further problem (their Section 4(c)). Neither treatment in the inspected primary text computes these second moments. Stanley (arXiv:1901.04647, January 15, 2019) gives moment recurrences for the unweighted Stern triangle and closely related arrays; it covers the underlying symmetric-sum phenomenon and is a significant antecedent to the \(p=1/2\) specialization. The present claimed contribution is the **complete Bernoulli-biased exact second moment and the strict all-bias relative-variance growth**. Stern-triangle recurrences must not be mistaken for an independent novelty claim. Other weighted Stern-tree moment formulas, if discovered, could supersede this specialization.

## Limitations
These are exact annealed second moments of the **total** number of distinct scattered subsequences. They do not give pointwise limiting distributions, high-probability concentration bounds, or results for specified subsequence lengths or Markov-dependent sources. Divergence of the relative second moment is not, by itself, proof of failure of convergence in probability of the relative count to \(1\). Source comparison has residual risk from weighted Stern-tree literature and results not identified by the available searches. No independent mathematical audit has been conducted.

## References
1. Y. Biers-Ariel, A. Godbole and E. Kelley, *Expected Number of Distinct Subsequences in Randomly Generated Binary Strings*, arXiv:1704.08661v1 (2017), Sections 2 and 4(c).
2. M. J. Collins, *The Number of Distinct Subsequences of a Random Binary String*, arXiv:1310.7288v1 (2013), Section 1.2.
3. R. P. Stanley, *Some Linear Recurrences Motivated by Stern's Diatomic Array*, arXiv:1901.04647v1 (2019), Section 2 and Remark 2.

# Exponential mutual Birkhoff–James cliques in real \(\ell_1^n\)

## Finding
For every integer \(n\ge1\), let \(\omega_n\) denote the maximum number of distinct one-dimensional real subspaces of \(\ell_1^n\) for which any two distinct representatives are Birkhoff–James orthogonal in both directions. Then
\[
\boxed{\displaystyle
\omega_n\ge
\left\lceil\frac{(1-2^{-n/2})^2}{4(\sqrt2-\tfrac12)^n}\right\rceil.}
\]
Consequently,
\[
\boxed{\displaystyle\liminf_{n\to\infty}\omega_n^{1/n}
\ge\frac{1}{\sqrt2-\frac12}
=\frac{4\sqrt2+2}{7}=1.093836321356\ldots.}
\]
The bound applies to a finite induced subgraph whose vertices are represented by nonzero ternary vectors. The exponential base is the best obtainable by optimizing the one-coordinate Chernoff factor in the symmetric independent ternary-product construction described below; no claim of optimality among all cliques is made.

## Assumptions and scope
Work over the real field and use the norm \(\|x\|_1=\sum_{i=1}^n|x_i|\). For nonzero \(x,y\), write \(x\perp_B y\) if \(\|x+\lambda y\|_1\ge\|x\|_1\) for all real \(\lambda\). Mutual orthogonality means both \(x\perp_B y\) and \(y\perp_B x\). Each projective line is counted once; parallel or antiparallel vectors cannot represent two vertices in a clique. The convention \(\omega_1=1\) is consistent with the bound.

For a ternary vector \(x\in\{-1,0,1\}^n\setminus\{0\}\), all its norming functionals \(f\in(\ell_1^n)^*=\ell_\infty^n\) have coordinates \(f_i=x_i\) when \(x_i\ne0\), and arbitrary \(f_i\in[-1,1]\) when \(x_i=0\). It follows, without any generic-position assumption, that
\[
\boxed{\displaystyle x\perp_B y\quad\Longleftrightarrow\quad
\left|\sum_{i:x_i\ne0}x_iy_i\right|\le\sum_{i:x_i=0}|y_i|.}
\tag{1}
\]
Indeed a support functional annihilating \(y\) exists precisely when the prescribed sum lies in the interval swept out by the free coordinates.

## Proof
Fix \(0<\rho<1\) and let \(X,Y\in\{-1,0,1\}^n\) be independent. Coordinates are independent, and each coordinate is zero with probability \(1-\rho\) and equals \(+1\) or \(-1\) with probability \(\rho/2\) each. Put
\[
A(X,Y)=\sum_{i:X_i\ne0}X_iY_i,\qquad B(X,Y)=\sum_{i:X_i=0}|Y_i|.
\]
By (1), failure of \(X\perp_B Y\) means either \(A>B\) or \(-A>B\). For the first event define independent coordinate variables
\[
T_i={\boldsymbol1}_{\{X_i\ne0\}}X_iY_i-{\boldsymbol1}_{\{X_i=0\}}|Y_i|.
\]
A direct enumeration gives
\[
\Pr(T_i=1)=\rho^2/2,\quad
\Pr(T_i=-1)=\rho(2-\rho)/2,\quad
\Pr(T_i=0)=1-\rho.
\]
For every \(u\ge0\), Markov's inequality and independence imply
\[
\Pr(A>B)=\Pr\!\left(\sum_iT_i>0\right)
\le\bigl(1-\rho+\tfrac{\rho^2}2e^u+
\tfrac{\rho(2-\rho)}2e^{-u}\bigr)^n.
\]
The minimizing parameter satisfies \(e^{2u}=(2-\rho)/\rho\), which is permitted since \(\rho<1\); hence
\[
\Pr(A>B)\le\vartheta(\rho)^n,\qquad
\vartheta(\rho)=1-\rho+\rho\sqrt{\rho(2-\rho)}.
\tag{2}
\]
Replacing \(Y\) by \(-Y\) gives the same bound for \(\Pr(-A>B)\). Interchanging \(X,Y\) gives the two reverse-direction bounds. The union bound therefore shows
\[
\Pr\bigl(X\not\perp_B Y\text{ or }Y\not\perp_B X\bigr)
\le4\vartheta(\rho)^n.
\tag{3}
\]
Here the notation of a failed direction is interpreted by (1) even if one sampled vector is zero; a failure cannot occur when either is zero. The probability that both vectors are nonzero is exactly \((1-(1-\rho)^n)^2\). Condition on that event and replace each nonzero vector by its projective line. Two such lines count as compatible only if they are mutually orthogonal; if the same projective line is sampled twice, it is incompatible. Consequently, for two independent draws from the resulting finite distribution on projective ternary lines, the incompatibility probability satisfies
\[
q_n(\rho)\le\frac{4\vartheta(\rho)^n}{(1-(1-\rho)^n)^2}.
\tag{4}
\]

For completeness, any probability distribution on the vertices of a finite simple graph of clique number \(\omega\) has incompatibility probability at least \(1/\omega\), where a vertex is considered incompatible with itself. To prove this, maximize its ordered-edge probability \(F(p)=\sum_{v\sim w}p_vp_w\). If two nonadjacent vertices have positive masses, transferring their combined mass wholly to one endpoint leaves all other masses fixed and cannot decrease \(F\), since \(F\) depends affinely on this transfer parameter. Repeating reduces the support to a clique of size \(r\le\omega\). Then
\[
F\le1-\sum_{j=1}^{r}p_j^2\le1-\frac1r\le1-\frac1\omega,
\]
proving the assertion. Applied to the ternary-line graph, this implies \(1/\omega_n\le q_n(\rho)\). Combining with (4) yields, for all \(0<\rho<1\),
\[
\omega_n\ge\frac{(1-(1-\rho)^n)^2}{4\vartheta(\rho)^n}.
\tag{5}
\]

Finally minimize the exponential factor \(\vartheta\) within this product family. Let \(t=1-\rho\in(0,1)\), \(s=\sqrt{1-t^2}\), and \(\Theta(t)=t+(1-t)s\). Differentiation gives the exact factorization
\[
s\,\Theta'(t)=(s-t)(1-s-t).
\]
Since \(s+t>1\) in the open interval, the derivative is negative for \(t<1/\sqrt2\) and positive for \(t>1/\sqrt2\). Thus the unique minimizer is \(t_*=1/\sqrt2\), equivalently \(\rho_*=1-1/\sqrt2\), and
\[
\vartheta_* = \sqrt2-\tfrac12<1,
\qquad(1-\rho_*)^n=2^{-n/2}.
\]
Substitution in (5) and integrality of \(\omega_n\) prove the finite-dimensional inequality. Taking \(n\)-th roots gives the stated exponential lower growth bound. This proves the claim.

## Verification
The self-contained script `CHECK.py` uses exact fractions to enumerate every ordered pair of nonzero ternary vectors through dimension five, checks equivalence of (1) with direct norm minimization at \(\lambda=\pm\frac12\), and evaluates conditional weighted incompatibility probabilities for \(\rho=\frac14\). It also tests the Chernoff bounds and the optimized algebraic constant numerically. Replay command: `python3 CHECK.py`. Observed output:

`VERIFY_OK exact_pairs=65708 exact_weighted_dimensions=5 rho=1/4 unique_chernoff_bias_checked=1 asymptotic_base=1.093836321356`

These finite tests are sanity checks, **not** the proof for unbounded dimension. The infinite-family statement follows from the preceding analytic argument.

## Relationship to prior work
Arambašić, Guterman, Kuzma, Rajić, and Zhilina (2021), Section 3 and Example 3.7, establish at least \(n\) mutual Birkhoff–James orthogonal directions in every real \(n\)-dimensional space and give an exponential construction of size \(2^{n-1}\) for \(\ell_\infty^n\), not \(\ell_1^n\). Their dimension-only universal upper bound does not imply an exponential lower bound for the specific \(\ell_1^n\) norm. Guterman, Kuzma, Singla, and Zhilina (2024) classify properties encoded by projective orthodigraphs, including dimension and smoothness; the inspected claims and relevant sections do not supply this explicit \(\ell_1^n\) growth rate. The 2021 preprint on what Birkhoff–James orthogonality knows about a norm concerns dimension and preserver structure, not a comparable lower exponent.

The proof here derives an \(\ell_1^n\)-specific clique from a balance-of-signed-mass inequality and a weighted finite-graph clique lemma. A prior exponential construction for the dual \(\ell_\infty^n\) does not transfer by linear duality, since Birkhoff–James orthogonality of primal vectors is not generally transported to the dual graph.

## Limitations
The result is an existential lower bound and does not determine the actual clique numbers \(\omega_n\), the optimal exponential growth exponent, or an explicit deterministic list of maximizing vectors. The Chernoff parameter is optimal only within the stated symmetric independent ternary family. A related 2022 survey chapter on orthogonality graphs was bibliographically identified but could not be inspected in full; possible equivalent unindexed coverage remains an originality risk. No independent scientific audit has been performed.

## References
1. L. Arambašić, A. Guterman, B. Kuzma, R. Rajić, S. Zhilina, *Symmetrized Birkhoff–James orthogonality in arbitrary normed spaces*, Journal of Mathematical Analysis and Applications 502 (2021), article 125203, DOI: 10.1016/j.jmaa.2021.125203. Section 3, Example 3.7.
2. A. Guterman, B. Kuzma, S. Singla, S. Zhilina, *Birkhoff–James classification of norm's properties*, arXiv:2402.13416v1 (20 February 2024), https://arxiv.org/abs/2402.13416.
3. L. Arambašić, A. Guterman, B. Kuzma, R. Rajić, S. Zhilina, *What does Birkhoff–James orthogonality know about the norm?*, arXiv:2109.09414v1 (2021), https://arxiv.org/abs/2109.09414.
4. L. Arambašić, A. Guterman, B. Kuzma, S. Zhilina, *Birkhoff–James Orthogonality: Characterizations, Preservers, and Orthogonality Graphs*, 2022 survey chapter, DOI: 10.1007/978-3-031-02104-6_8 (abstract and metadata consulted; full chapter unavailable).

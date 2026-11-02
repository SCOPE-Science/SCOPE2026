# Four-phase reversible mixing and an isolated Metropolis optimum on biased multipartite graphs

## Finding
For every integer \(r\ge4\), every part size \(m\ge2\), and every distinguished mass \(0<a<1\), the exact fastest-mixing reversible transition matrix problem on the balanced complete \(r\)-partite graph has the four-phase optimal second-largest eigenvalue modulus
\[
\mu_*(a,r)=\begin{cases}
\dfrac{1-2a}{(2r-3)(1-a)},&0<a\le\dfrac1{2r-1},\\[2mm]
\dfrac{1-a}{2r-3+a},&\dfrac1{2r-1}\le a\le\dfrac1r,\\[2mm]
\dfrac{a}{2-a},&\dfrac1r\le a\le\dfrac23,\\[2mm]
\dfrac{2a-1}{a},&\dfrac23\le a<1.
\end{cases}
\]
All endpoints agree between adjacent expressions. The optimum does not depend on the common part size \(m\) (provided \(m\ge2\)). Its uniquely forced **total stationary flow** from the distinguished part to all other parts, even for nonsymmetric optimizing kernels, is
\[
x_* =\begin{cases}
a,&a\le1/(2r-1),\\[1mm]
\dfrac{2(r-1)a(1-a)}{2r-3+a},&1/(2r-1)\le a\le1/r,\\[2mm]
\dfrac{2a(1-a)}{2-a},&1/r\le a\le2/3,\\[2mm]
1-a,&a\ge2/3.
\end{cases}
\]
In particular, for \(a\ge2/3\) **every** global optimizer assigns zero probability to every edge joining two ordinary parts: a sharp global edge-screening phenomenon. The ordinary uniform-neighbor-proposal Metropolis–Hastings kernel is globally optimal **if and only if** \(a=1/(2r-1)\). The optimal SLEM, as a function of \(a\), is strictly decreasing until \(a=1/r\), then strictly increasing, attaining the exact minimum \(1/(2r-1)\) at equal total part masses.

## Assumptions and scope
The graph is \(K_{m,\ldots,m}\) with \(r\) independent vertex parts of size \(m\), and every cross-part edge and each self-loop is allowed. Every vertex in distinguished part \(A\) has prescribed stationary probability \(a/m\). Every vertex in each other part has probability \((1-a)/((r-1)m)\). We optimize the second-largest eigenvalue modulus (SLEM), the operator norm of the centered transition operator on \(L^2(\pi)\), over **all** real, entrywise nonnegative, row-stochastic, \(\pi\)-reversible kernels with these supports. Edge transition probabilities are independent decision variables; symmetry is not imposed on competitors. The claim does not extend to nonreversible kernels or a different objective.

## Proof
Put \(b=1-a\), \(T=2r-3\). For a reversible kernel \(P\), the symmetrized matrix \(\operatorname{diag}(\pi)^{1/2}P\operatorname{diag}(\pi)^{-1/2}\) is symmetric. Its centered spectral norm is convex in \(P\). Averaging over permutations within parts and permutations of the \(r-1\) ordinary parts preserves prescribed \(\pi\), feasibility, the total distinguished-to-ordinary flow \(x\), and cannot increase SLEM. Thus a globally optimal invariant kernel exists, while any lower bound obtained after averaging is valid for all feasible kernels.

Write \(x\) for the total undirected stationary flow from \(A\) to its complement. Write \(y\) for the undirected stationary flow between each unordered pair of distinct ordinary parts, and set \(t=(r-1)^2y/b\). Feasibility is exactly
\[
0\le x\le\min(a,b),\qquad 0\le t\le\frac{r-1}{r-2}\left(1-\frac{x}{b}\right).
\]
All \(m^2\) cross edges from \(A\) to any specified ordinary part carry equal stationary flow \(x/((r-1)m^2)\); cross edges between any two ordinary parts carry flow \(bt/((r-1)^2m^2)\). Diagonal entries uniquely fill the remaining row mass.

The invariant eigenspace decomposition has exactly four nonstationary eigenvalues, with the following multiplicities:
\[
\begin{array}{lll}
\lambda_A=1-x/a &\text{(within }A\text{)}&m-1,\\
\lambda_B=1-x/b-\frac{r-2}{r-1}t &\text{(within ordinary parts)}&(r-1)(m-1),\\
\lambda_C=1-x/b-t &\text{(ordinary-part contrasts)}&r-2,\\
\lambda_D=1-x/(ab) &\text{(distinguished-mass contrast)}&1.
\end{array}
\]
These four eigenspaces and the stationary constant vector have total dimension \(rm\). Their signs and multiplicities therefore give **all** eigenvalues, including every zero/degeneracy boundary.

For a fixed feasible \(x\), put \(u=1-x/b\ge0\). Since the two ordinary-part terms are \(u-(r-2)t/(r-1)\) and \(u-t\), their maximum absolute value is minimized by balancing them with opposite signs. The feasible minimizer is
\[
t_*(x)=\frac{2(r-1)}{2r-3}u,
\qquad \min_t\max(|\lambda_B|,|\lambda_C|)=\frac{u}{2r-3}.
\]
It indeed lies in the stated feasible interval, because \(2(r-2)<2r-3\). The full minimization consequently reduces **exactly** to
\[
\min_{0\le x\le\min(a,b)}f(x),\qquad
f(x)=\max\left\{1-\frac{x}{a},\ \left|1-\frac{x}{ab}\right|,\ \frac{1-x/b}{2r-3}\right\}.
\]
Here \(1-x/a\) and \((1-x/b)/T\) are nonnegative. Define the strictly decreasing envelope \(L(x)=\max\{1-x/a,1-x/(ab),(1-x/b)/T\}\) and the strictly increasing branch \(U(x)=x/(ab)-1\). Then \(f(x)=\max\{L(x),U(x)\}\) has a **unique** minimizer, either where these branches meet or at the allowed right endpoint. Direct comparison gives the four consecutive regimes. For \(a\le1/(2r-1)\), the capacity boundary \(x=a\) is optimal, with value \((1-2a)/(Tb)\). Between \(1/(2r-1)\) and \(1/r\), solve \((1-x/b)/T=x/(ab)-1\), yielding \(x=ab(T+1)/(T+a)\) and \(\mu=b/(T+a)\). Between \(1/r\) and \(2/3\), solve \(1-x/a=x/(ab)-1\), yielding \(x=2ab/(2-a)\) and \(\mu=a/(2-a)\). For \(a\ge2/3\), the right boundary \(x=b\) is optimal, with \(\mu=(2a-1)/a\). Substitution proves all branch inequalities and equality at the displayed thresholds. Taking \(t=t_*(x_*)\) constructs an exact globally feasible attaining kernel.

For an arbitrary (not necessarily invariant) global optimizer, group averaging leaves its total flow \(x\) unchanged. Its averaged kernel must also be globally optimal, so uniqueness of the reduced minimizer forces \(x=x_*\) for the original kernel. If \(a\ge2/3\), then \(x_*=b\) exhausts the total stationary mass of all ordinary vertices. All other ordinary-to-ordinary off-diagonal stationary flows and their holding flows are nonnegative, hence must be zero, proving universal edge deletion.

For the ordinary equal-neighbor-proposal Metropolis–Hastings kernel, every vertex has \((r-1)m\) available neighbors. Its parameters are \(x_{\mathrm{MH}}=\min(a,b/(r-1))\) and \(t_{\mathrm{MH}}=1\). In the low-mass regime, matching the forced optimum \(x_*=a\) is insufficient: \(\lambda_B\) exceeds \(\mu_*\) unless \(a=1/(2r-1)\). In the second regime \(x_{\mathrm{MH}}>x_*\); in the third, equality of total flows can only occur at \(a=2/(2r-1)\), where the Metropolis ordinary-part contrast has absolute eigenvalue \(1/(r-1)\), twice the optimum \(1/(2r-2)\); in the fourth, \(x_{\mathrm{MH}}<x_*\). At \(a=1/(2r-1)\), the Metropolis parameters coincide with \(x_*\) and \(t_*(x_*)=1\), proving the if-and-only-if. Finally, differentiating each of the four elementary value branches shows the unique minimum at \(a=1/r\), with value \(1/(2r-1)\).

## Verification
Run `python3 verify.py`, requiring Python 3 and NumPy. The checker independently constructs exact-rational full transition matrices for \(r=4,\ldots,8\), \(m=2,3,4\), and nine rational bias values per pair. It verifies row stochasticity, nonnegativity, detailed balance, representative eigenvectors for each of the four invariant eigenspaces, the claimed exact SLEM, and 101 exact-rational scalar-comparison points per instance (135 instances). It also tests 900 seeded asymmetric feasible matrices with numerical symmetric eigensolvers and 56 exact-rational Metropolis comparisons. These finite checks do **not** prove the all-parameter theorem: the preceding averaging, eigenspace and scalar-monotonicity arguments do.

## Relationship to prior work
Boyd, Diaconis and Xiao (2004) established the convex semidefinite formulation for fastest reversible mixing with prescribed stationary measure, and described Metropolis–Hastings comparisons. Boyd, Diaconis, Parrilo and Xiao (2009, §5.4.2) explicitly block-diagonalized complete multipartite chains with symmetric transition matrices and uniform stationary law; their displayed closed formula is for the complete bipartite specialization. Thus the block-decomposition technique and the uniform-stationary boundary case are prior art. A three-part biased classification is also not claimed: this theorem deliberately restricts to at least four vertex parts. The reported contribution is the four-regime **nonuniform** optimization over at least four classes, its forced aggregate flow for every nonsymmetric optimizer, universal ordinary-edge deletion at high bias, and the isolated exact Metropolis optimum. A general SDP or related special-case formula alone does not state these parameter-wide conclusions, although a different specialist derivation may exist.

## Limitations
The theorem assumes balanced part cardinalities and one distinguished total stationary mass, with all remaining total part masses equal. It concerns reversible discrete-time kernels, permitted self-loops and the SLEM objective, not nonreversible optimization, all-optimizer uniqueness, mixing-time constants, or arbitrary stationary profiles. The explicit invariant construction need not be the only global optimizer. The originality assessment is limited by the accessible literature and cannot exclude unlocated equivalent formulations. Independent mathematical evaluation is outside the scope of the theorem.

## References
- S. Boyd, P. Diaconis, L. Xiao, *Fastest Mixing Markov Chain on a Graph*, SIAM Review 46 (2004), 667–689, DOI: 10.1137/S0036144503423264. Public PDF: https://web.stanford.edu/~boyd/papers/pdf/fmmc.pdf (published electronically 2004-10-29).
- S. Boyd, P. Diaconis, P. A. Parrilo, L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, SIAM J. Optim. 20 (2009), 792–819, §5.4.2, DOI: 10.1137/070689413. Public PDF: https://web.stanford.edu/~boyd/papers/pdf/fast_mix_symm.pdf.
- S. Jafarizadeh, *Fastest Mixing Markov Chain on Symmetric K-Partite Network* (2010), arXiv:1008.2588; analyzes an adjacent-part symmetric network rather than the complete multipartite nonuniform case. https://arxiv.org/abs/1008.2588.

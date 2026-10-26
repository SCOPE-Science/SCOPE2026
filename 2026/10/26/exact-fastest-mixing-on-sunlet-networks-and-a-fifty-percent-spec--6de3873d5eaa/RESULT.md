# Exact fastest mixing on sunlet networks and a fifty-percent spectral-gap gain

## Finding

For every integer \(n\ge3\), let \(S_n=C_n\circ K_1\) be the *sunlet*: an \(n\)-cycle with one private pendant vertex attached to each cycle vertex. Its vertices are \(v_0,\ldots,v_{n-1}\) and \(w_0,\ldots,w_{n-1}\), with subscripts modulo \(n\); edges are \(\{v_i,v_{i+1}\}\) and \(\{v_i,w_i\}\). The problem is to minimize the second-largest eigenvalue modulus (SLEM) among **all** symmetric, entrywise nonnegative row-stochastic matrices supported off the diagonal on these edges (self-loops are allowed).

Put
\[
 u_n=\sqrt{1-\cos(2\pi/n)}=\sqrt2\sin(\pi/n),\qquad H_n=u_n^2+2u_n+2.
\]
Then the global optimum is
\[
 \boxed{\mu_n^*=\frac{2(u_n+1)}{H_n}},\qquad
 \boxed{1-\mu_n^*=\frac{u_n^2}{H_n}}.
\]
One globally optimal matrix is obtained by putting probability
\[
 \boxed{a_n=\frac{u_n+2}{2H_n}}
\]
on every cycle edge and probability
\[
 \boxed{b_n=\frac{u_n(u_n+1)}{H_n}}
\]
on each pendant edge, and filling the diagonal to make every row stochastic. The cycle-vertex diagonal is exactly zero; the pendant-vertex diagonal is \(1-b_n=2a_n\). This is the **unique rotation-and-reflection-invariant optimum**. Global uniqueness without invariance is not claimed.

For the maximum-degree and uniform-target Metropolis weighting prescriptions, the cycle and pendant edge probabilities both equal \(1/3\), and their common SLEM is exactly
\[
 \mu_n^{\mathrm{heur}}=\frac{2-u_n^2+\sqrt{1+u_n^4}}3.
\]
Their spectral-gap disadvantage has the precise limit
\[
 \boxed{\lim_{n\to\infty}\frac{1-\mu_n^*}{1-\mu_n^{\mathrm{heur}}}=\frac32}.
\]
In particular, the optimally tuned ring-and-leaf chain has asymptotically a 50% larger absolute spectral gap than either standard prescription. For the eight-vertex sunlet \(S_4\), the optimal weights are exactly \(a_4=3/10\), \(b_4=2/5\), with \(\mu_4^*=4/5\).

## Assumptions and scope

All \(n\) are integers at least three, all transition probabilities are real, the uniform distribution is stationary, and off-diagonal transitions must follow graph edges. Allowed matrices need not respect any graph symmetry and may assign probability zero to an available edge. The SLEM equals \(\mu(P)=\|P-J_{2n}\|_2\), where \(J_{2n}=\mathbf1\mathbf1^{\mathsf T}/(2n)\). No claims are made for nonsymmetric chains, nonuniform stationary measures, or optimization of finite-time total-variation mixing in place of SLEM.

## Proof

**1. Global symmetry reduction.** The dihedral automorphisms of the cycle act simultaneously on the cycle and pendant vertices and preserve the feasible set. Conjugating a feasible \(P\) by a graph automorphism leaves \(\|P-J_{2n}\|_2\) unchanged. Averaging over these automorphisms cannot increase this convex norm. Therefore a globally optimal matrix exists with common cycle-edge probability \(a\) and pendant-edge probability \(b\), constrained by
\[
 a\ge0,\quad b\ge0,\quad 2a+b\le1.
\]
Its cycle and pendant diagonal probabilities are respectively \(1-2a-b\) and \(1-b\). This reduction proves the lower bound for the full, *unrestricted* optimization, not just for invariant matrices.

**2. Every Fourier mode.** With \(\theta_j=2\pi j/n\) and \(\delta_j=1-\cos\theta_j\), the Fourier transform along the cycle converts \(P\) into the \(n\) symmetric blocks
\[
 B_j=\begin{pmatrix}1-b-2a\delta_j&b\\b&1-b\end{pmatrix},
\quad
 \lambda_\pm(\delta_j)=1-b-a\delta_j\pm\sqrt{b^2+a^2\delta_j^2}.
\]
For \(j=0\), the eigenvalues are \(1\) and \(1-2b\). For the other modes, \(\delta_j\ge r\), where \(r=1-\cos(2\pi/n)=u_n^2\). The function \(\lambda_+(\delta)\) is nonincreasing in \(\delta\), while \(\lambda_-(\delta)\) is decreasing. Thus \(\mu(P)\ge\lambda_+(r)\) for every invariant feasible matrix.

**3. A unique scalar lower envelope.** For fixed \(b>0\), \(\lambda_+(r)\) strictly decreases with \(a\), since
\[
 \frac{\partial\lambda_+(r)}{\partial a}=-r+\frac{ar^2}{\sqrt{b^2+a^2r^2}}<0.
\]
Consequently the best value of this lower bound at fixed \(b\) is at \(a=(1-b)/2\). If \(b=0\), the same lower bound is one, so such points cannot be optimal. The remaining strictly convex function is
\[
 g(b)=\frac{(1-b)(2-r)}2+
 \sqrt{b^2+\frac{(1-b)^2r^2}{4}},\qquad0\le b\le1.
\]
Its second derivative, wherever the square root is positive, is
\[
 g''(b)=\frac{r^2/4}{\left(b^2+(1-b)^2r^2/4\right)^{3/2}}>0.
\]
Differentiation gives its unique minimizer
\[
 b^*=\frac{u(u+1)}{u^2+2u+2},\qquad a^*=\frac{u+2}{2(u^2+2u+2)},\quad u=\sqrt r.
\]
Indeed \(2a^*+b^*=1\), \(\sqrt{(b^*)^2+(a^*r)^2}=u/2\), and substitution yields \(g(b^*)=2(u+1)/(u^2+2u+2)=\mu_n^*\). These identities verify stationarity and the stated global lower bound.

**4. The lower bound is attained, including all negative modes.** For the proposed weights, the maximal positive nontrivial eigenvalue is \(\lambda_+(r)=\mu_n^*\). Furthermore, for \(0\le\delta_j\le2\), monotonicity gives
\[
 \lambda_-(\delta_j)\ge\lambda_-(2)
 =-\sqrt{(b^*)^2+(1-b^*)^2}.
\]
The identity
\[
 (\mu_n^*)^2-\bigl[(b^*)^2+(1-b^*)^2\bigr]
 =\frac{u(u+2)(2-u^2)}{(u^2+2u+2)^2}>0
\]
holds because \(0<u^2\le3/2<2\) for all \(n\ge3\). Also \(0<1-2b^*<\mu_n^*\). Hence **every** eigenvalue other than one lies in \([-\mu_n^*,\mu_n^*]\), so the lower bound from step 3 is actually the global SLEM optimum. Strict convexity and strict decrease with \(a\) at the optimum prove uniqueness among invariant matrices. The global averaging argument proves the minimum over unrestricted matrices; it does not prove uniqueness of all unrestricted minimizers.

**5. Exact heuristic and asymptotics.** A cycle vertex has degree three and a leaf degree one; both maximum-degree and uniform-target Metropolis therefore assign \(a=b=1/3\). Fourier modes give \(\lambda_+(r)=(2-r+\sqrt{1+r^2})/3\). Every negative mode is at least \(-\sqrt5/3\); since \(r\le3/2\), the positive mode is at least \((1+\sqrt{13})/6>\sqrt5/3\), and exceeds the other nontrivial positive modes. Thus this is the exact heuristic SLEM, not merely an upper bound. Finally \(u_n\sim\sqrt2\pi/n\); the proved gap expressions yield
\[
 1-\mu_n^*\sim\frac{\pi^2}{n^2},\qquad
 1-\mu_n^{\mathrm{heur}}\sim\frac{2\pi^2}{3n^2},
\]
which proves the ratio \(3/2\).

## Verification

Run `python verify.py` after installing the packages in `requirements.txt`. The program independently assembles the full \(2n\)-by-\(2n\) stochastic matrices, compares their dense spectra to the Fourier blocks for all \(3\le n\le50\), rechecks the symbolic optimality and negative-mode identities, tests feasible invariant and noninvariant perturbations, and verifies the exact heuristic formula and asymptotic gap ratio. Its actual successful output is recorded in `VERIFICATION.md`. Finite calculations are checks, **not** the universal proof, which consists of the displayed identities, monotonicities and strict inequalities.

## Relationship to prior work

Boyd, Diaconis and Xiao (2004) introduced the convex SLEM minimization and compared the maximum-degree and Metropolis prescriptions. Boyd, Diaconis, Parrilo and Xiao (arXiv:0709.0955, initially public 2007-09-06; later 2009) proved automorphism averaging and treated pure cycles and wheel graphs explicitly, as well as other symmetric examples. Their ring with added triangular bumps is distinct from a ring with one pendant vertex at **every** cycle vertex, and its reported numerical behavior does not supply the present closed-form solution. The preceding general SDP framework makes finite instances solvable numerically, but does not give this all-orders exact minimizer, all-mode attainment certificate, or limiting improvement factor.

A related exact result for complete-core leaf coronas concerns \(K_m\circ K_1\): it has a different core spectrum and a nonvanishing limiting optimal SLEM. The sunlet's sparse cyclic core instead yields \(\mu_n^*\to1\) with an exactly quantified optimal spectral gap; the prior complete-core formula alone does not verify its entire sequence of cyclic Fourier modes. Olesker-Taylor and Zanetti (2024) study general geometric bounds and mixing-time characterizations, not the exact SLEM and edge weights for sunlets. Specialized results on ring-and-pendant stochastic chains that are incompletely indexed remain a possible overlap risk.

## Limitations

The result assumes symmetric doubly stochastic matrices and evaluates asymptotic convergence via SLEM, not finite-time total variation. Full unrestricted uniqueness is unresolved here. No statement is made for different numbers of leaves, weighted stationary distributions, or varying ring edge availability. Direct inspection of relevant general primary works did not reveal this sunlet classification, but no literature search certifies universal novelty. The numerical examples do not stand in for the analytic proof.

## References

1. S. Boyd, P. Diaconis and L. Xiao, *Fastest Mixing Markov Chain on a Graph*, SIAM Review 46 (2004), 667–689, DOI: 10.1137/S0036144503423264. Author-posted PDF: https://web.stanford.edu/~boyd/papers/pdf/fmmc.pdf .
2. S. Boyd, P. Diaconis, P. A. Parrilo and L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, arXiv:0709.0955 (first public version 2007-09-06), later SIAM Journal on Optimization 20 (2009), 792–819. https://arxiv.org/pdf/0709.0955 .
3. S. Olesker-Taylor and L. Zanetti, *Geometric Bounds on the Fastest Mixing Markov Chain*, Probability Theory and Related Fields 188 (2024), 1017–1062. DOI: 10.1007/s00440-023-01257-x. https://link.springer.com/article/10.1007/s00440-023-01257-x .

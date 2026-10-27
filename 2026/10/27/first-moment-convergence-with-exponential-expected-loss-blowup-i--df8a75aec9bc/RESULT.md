# First-moment convergence with exponential expected-loss blowup in exact SPAM

## Finding

For every real parameter \(10<b<9+4\sqrt6\), consider the two equiprobable, strictly convex scalar clients \(f_1(x)=x^2/2\) and \(f_b(x)=b x^2/2\). Run exact SPAM with stepsize \(\gamma=1\), refresh probability \(p=1/2\), independently sampled clients, and initialization \(x_{-1}=x_0=1\), \(g_{-1}=0\). The full optimizer-state first moment converges geometrically to zero, and either deterministic frozen-client update is Schur stable. Nevertheless, the expected squared iterate and the expected objective diverge along even iterates:
\[
\mathbb E[x_{2n}^2]\ge\frac{1}{(b-1)^2(b+2)^2}\left(\frac{(b-2)^2}{64}\right)^n\longrightarrow\infty
\]
for all sufficiently large integers \(n\). In particular, the method can be stable in first moments and under either frozen client, yet exponentially unstable in expected loss.

At the explicit integer choice \(b=14\), the full mean transition has spectral radius less than one, while
\[
\mathbb E[x_{2n}^2]\ge\frac{1}{43264}\left(\frac94\right)^n\qquad(n\ge3).
\]

## Assumptions and scope

The client indices are independent across steps and choose \(c_k=1\) and \(c_k=b\) with probability \(1/2\) each. Both client functions share the unique minimizer \(0\). The scalar proximal subproblem is solved exactly; there is no process, communication, or additive gradient noise. The SPAM gradient-estimator recursion and shifted proximal update are
\[
g_k=c_k x_k+\tfrac12(g_{k-1}-c_k x_{k-1}),\qquad
x_{k+1}=\operatorname{prox}_{f_{c_k}}(x_k+c_kx_k-g_k)
=x_k-\frac{g_k}{1+c_k}.
\]
The physical objective is \(f(x)=\frac{1+b}{4}x^2\). Here first-moment stability means convergence of \(\mathbb E(x_k,x_{k-1},g_{k-1})\), not convergence of second moments or almost-sure sample paths. Only the declared open heterogeneity interval is claimed.

## Proof

With \(z_k=(x_k,x_{k-1},g_{k-1})^{\mathsf T}\), substitution into the exact update yields \(z_{k+1}=A_{c_k}z_k\), where
\[
A_c=\begin{pmatrix}
(1+c)^{-1}&c/[2(1+c)]&-1/[2(1+c)]\\
1&0&0\\ c&-c/2&1/2
\end{pmatrix}.
\]
For each fixed positive \(c\), its characteristic polynomial is \(\lambda(\lambda-1/2)(\lambda-(1+c)^{-1})\); both frozen-client operators are Schur stable (a repeated root is harmless). Independence gives \(\mathbb E z_k=\bar A^k z_0\), with \(\bar A=(A_1+A_b)/2\). Direct determinant expansion factors as
\[
\det(\lambda I-\bar A)=(\lambda-\tfrac12)
\left(\lambda^2-\frac{b+3}{4(b+1)}\lambda+\frac{(b-1)^2}{16(b+1)}\right).
\]
The two nontrivial roots satisfy the strict real quadratic Jury criterion. Indeed, the constant term is less than one exactly when \((b-1)^2<16(b+1)\); the other two Jury expressions are strictly positive for \(b>1\) (they are \(1-(b+3)/[4(b+1)]+(b-1)^2/[16(b+1)]>0\) and \(1+(b+3)/[4(b+1)]+(b-1)^2/[16(b+1)]>0\)). On \(10<b<9+4\sqrt6\), this condition holds, proving geometrically vanishing first moments.

Now consider the event \(E_n\) on which the first \(2n\) sampled curvatures follow the exact repeating sequence \(1,b,1,b,\ldots,1,b\). This event has probability \(4^{-n}\). The two-step map \(P=A_b A_1\) has eigenvalues \(0\), \(r=-(b-2)/4\), and \(s=b/[2(b+1)]\), with \(|r|>2\) and \(0<s<1/2\). Direct diagonalization of the first coordinate of \(P^nz_0\), with \(z_0=(1,1,0)^{\mathsf T}\), gives for every \(n\ge1\)
\[
x_{2n}|E_n=-\frac{2}{(b-1)(b+2)}r^n
+\frac{b(b+1)}{(b-1)(b+2)}s^n.
\]
Since \(|s/r|<1\) and the leading coefficient is nonzero, for all sufficiently large \(n\), \(|x_{2n}|\ge |r|^n/[(b-1)(b+2)]\) on \(E_n\). Multiplying its square by \(\Pr(E_n)=4^{-n}\) yields the asserted lower bound. Because \((b-2)^2/64>1\) for \(b>10\), the second moment diverges exponentially; multiplying by \((b+1)/4\) yields the same conclusion for expected objective.

At \(b=14\), \(r=-3\), \(s=7/15\), and the exact event iterate is \(x_{2n}|E_n=-(-3)^n/104+(105/104)(7/15)^n\). For \(n\ge3\), \(105(7/45)^n\le1/2\). Thus \(|x_{2n}|\ge3^n/208\), implying \(\mathbb E x_{2n}^2\ge (9/4)^n/43264\). Here the averaged characteristic roots are \(1/2\) and \((17\pm i\sqrt{9851})/120\), with modulus \(13/(4\sqrt{15})<1\).

## Verification

The companion `verify.py` uses only the Python standard library and exact rational arithmetic to construct both SPAM transition matrices, expand selected matrix products and test the stated characteristic polynomials and event-iterate formulas for several integer parameters and multiple horizons. A successful finite checker does not establish the all-parameter result, which follows from the symbolic factorization, quadratic Jury criterion and rare-event lower bound above. The program can be run as `python3 verify.py`.

## Relationship to prior work

Karagulyan, Shulgin, Sadiev, and Richtárik introduced SPAM, its gradient-estimator and exact-proximal updates, and proved sufficient convergence bounds subject to their assumptions. Their experiments observe sensitivity to the refresh probability. A published exact scalar first-moment calculation already gives a Schur-stability criterion; no claim to that criterion is made here. The present contribution is a distinct open parameter family where first-moment and both frozen-client stability coexist with exponentially increasing expected objective. The first-moment result does not imply, exclude, or quantify such mean-square divergence. Other scalar stochastic-optimization stability results for Loopless SVRG and PAGE involve different update matrices and do not directly cover this SPAM example.

## Limitations

This is a two-client, scalar, exactly-proximal, independent-sampling counterexample; it is not a full mean-square stability phase diagram for SPAM. It proves divergence of the expected loss along the even subsequence, not almost-sure divergence or divergence for every initial state. The heterogeneous centered quadratic family does not satisfy a global uniform bounded-gradient-variance condition often imposed for general convergence guarantees, and the displayed stepsize is outside the conservative guarantees of the motivating source. The result therefore does not contradict those guarantees. The proof uses exact arithmetic; practical floating-point consequences are not quantified.

## References

1. A. Karagulyan, E. Shulgin, A. Sadiev, and P. Richtárik, *SPAM: Stochastic Proximal Point Method with Momentum Variance Reduction for Non-convex Cross-Device Federated Learning*, arXiv:2405.20127v1, posted 2024-05-30. https://arxiv.org/abs/2405.20127
2. *Exact first-moment stability frontier for two-client scalar SPAM*, publicly archived technical result (2026). https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-exact-first-moment-stability-frontier-for-two-client-scalar-spam--170ca03b5dee

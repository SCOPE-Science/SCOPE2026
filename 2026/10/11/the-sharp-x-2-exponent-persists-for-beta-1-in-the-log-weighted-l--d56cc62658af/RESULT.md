# The sharp \(X_2\) exponent persists for \(\beta>1\) in the log-weighted Leray–Trudinger inequality
## Finding
Let \(N\ge2\), let \(\Omega\subset\mathbb R^N\) be a bounded domain containing the origin, put \(R_\Omega=\sup_{x\in\Omega}|x|\), \(X_1(r)=(\log(e/r))^{-1}\), \(X_2=X_1\circ X_1\), \(N' = N/(N-1)\), and fix \(\beta>1\). Define \(w_\beta=X_1(|x|/R_\Omega)^{-\beta(N-1)}\), \(a=(\beta-1)/N'\), and the weighted Hardy defect \[I_{\beta,\Omega}[u]=\int_\Omega |\nabla u|^Nw_\beta\,dx-a^N\int_\Omega \frac{|u|^N}{|x|^N}X_1(|x|/R_\Omega)^{N-(N-1)\beta}\,dx.\] For every real \(q<2\), \[\inf_{0\ne u\in C_c^\infty(\Omega\setminus\{0\})}\frac{I_{\beta,\Omega}[u]}{\int_\Omega \frac{|u|^N}{|x|^N}X_1^{N-(N-1)\beta}X_2^q\,dx}=0.\] Consequently the exponent \(1/(N-1)\) of \(X_2\) in Theorem 1.4 of arXiv:2610.03668v1 is optimal also for \(\beta>1\): if \(\theta<1/(N-1)\) and \(\alpha>0\), then \[\sup_{I_{\beta,\Omega}[u]\le1}\int_\Omega \exp\!\left(\alpha |u|^{N'}X_1^{-\beta}X_2^{\theta}\right)\,dx=\infty.\] Thus the source theorem’s positive \(\beta>1\) embedding has the same sharp logarithmic correction exponent as its \(\beta<1\) regime.

## Assumptions and scope
Throughout, \(N\ge2\), \(\Omega\subset\mathbb R^N\) is bounded and contains the origin, and \(\beta>1\). Write \(R_\Omega=\sup_{x\in\Omega}|x|\), \(X_1(r)=(\log(e/r))^{-1}\), \(X_2=X_1\circ X_1\), and \(N'=N/(N-1)\). The weighted Hardy defect is the one in Theorem 1.4 of arXiv:2610.03668v1, with the sharp Hardy coefficient \(((\beta-1)/N')^N\). The test functions below lie in \(C_c^\infty(\Omega\setminus\{0\})\), so no completion or trace issue is used.

The conclusion concerns the exponent on \(X_2\), not the largest admissible exponential coefficient \(\alpha\). It also does not assert a positive \(X_2^2\) remainder for \(\beta>1\); it proves only the sharp obstruction below power \(2\), which is exactly what is needed for the exponent-optimality consequence.

## Proof
Set \(a=(\beta-1)/N'>0\). Choose \(r_* >0\) with \(B_{r_*}\subset\Omega\). For \(0<r<r_*\), define
\[
t=\log\!\left(\frac{eR_\Omega}r\right),\qquad s=\log t.
\]
Choose a fixed \(\phi\in C_c^\infty((0,3))\) with \(0\le\phi\le1\) and \(\phi=1\) on \([1,2]\). Fix \(S\) sufficiently large that all annuli generated below lie in \(B_{r_*}\), and for \(L\ge1\) put
\[
v_L(s)=\phi\!\left(\frac{s-S}L\right),\qquad
u_L(r)=t^{-a}v_L(s).
\]
Extend \(u_L\) radially by zero outside its annular support. Because \(\phi\) is compactly supported and smooth, every \(u_L\) belongs to \(C_c^\infty(\Omega\setminus\{0\})\).

Let \(\omega_{N-1}\) be the surface measure of the unit sphere. Direct radial substitution gives three exact identities:
\[
\int_\Omega |\nabla u_L|^Nw_\beta\,dx
=\omega_{N-1}\int |a v_L-v_L'|^N\,ds,
\]
\[
a^N\int_\Omega \frac{|u_L|^N}{|x|^N}X_1^{N-(N-1)\beta}\,dx
=\omega_{N-1}a^N\int |v_L|^N\,ds,
\]
and, for every real \(q\),
\[
D_q[u_L]:=\int_\Omega \frac{|u_L|^N}{|x|^N}X_1^{N-(N-1)\beta}X_2^q\,dx
=\omega_{N-1}\int |v_L(s)|^N(1+s)^{-q}\,ds.
\]
The exponent cancellation behind the first two formulas is
\[
-N(a+1)+\beta(N-1)=-1,
\]
and \(dt/t=ds\); moreover \(X_2=1/(1+s)\).

For \(x\ge0\) and \(y\in\mathbb R\), the standard Taylor remainder bound for the convex function \(z\mapsto |z|^N\) gives
\[
\bigl||x-y|^N-x^N+N x^{N-1}y\bigr|
\le C_N\bigl(x^{N-2}y^2+|y|^N\bigr).
\]
Apply this with \(x=a v_L\) and \(y=v_L'\). The linear term integrates to zero because
\[
\int v_L^{N-1}v_L'\,ds=\frac1N\int (v_L^N)'\,ds=0.
\]
Hence
\[
0\le I_{\beta,\Omega}[u_L]
\le C_{N,a}\int\left(v_L^{N-2}|v_L'|^2+|v_L'|^N\right)ds
\le \frac{C_{N,a,\phi}}L.
\]
The initial nonnegativity is the sharp weighted Hardy inequality, which arXiv:2610.03668v1 proves for every \(\beta\ne1\).

On the plateau \(S+L\le s\le S+2L\), one has \(v_L=1\). Therefore, for every fixed \(q<2\),
\[
D_q[u_L]\ge \omega_{N-1}\int_{S+L}^{S+2L}(1+s)^{-q}\,ds
\asymp_q L^{1-q},
\]
where for \(q=1\) the right scale is a positive constant. Consequently
\[
0\le\frac{I_{\beta,\Omega}[u_L]}{D_q[u_L]}
\le C L^{q-2}\longrightarrow0.
\]
This proves the sharp subquadratic-remainder obstruction.

It remains to pass from this obstruction to the Leray–Trudinger exponent. Suppose first that \(0<\theta<1/(N-1)\), and set \(\gamma=\theta/N'\), so \(0<\gamma<1/N\). Choose \(1<\rho<2-N\gamma\) and put \(q=N\gamma+\rho<2\). The Young-factorization calculation in equations (6.16)–(6.17) of arXiv:2610.03668v1 uses only the assumed exponential estimate and the finiteness of its auxiliary integral \(K\); that calculation is independent of the sign of \(1-\beta\). Thus an exponential estimate with correction \(X_2^\theta\) and any \(\alpha>0\) would imply a uniform bound \(D_q[u]\le C\) whenever \(I_{\beta,\Omega}[u]\le1\). By degree-
\(N\) homogeneity this would give \(D_q[u]\le C I_{\beta,\Omega}[u]\) for every nonzero test function, contradicting the ratio limit above.

If \(\theta\le0\), choose any \(\theta_0\) with \(0<\theta_0<1/(N-1)\). Since \(0<X_2\le1\), one has \(X_2^\theta\ge X_2^{\theta_0}\), so failure for \(\theta_0\) implies failure for \(\theta\). Hence every exponent below \(1/(N-1)\) fails for \(\beta>1\).

## Verification
The proof was checked at three levels. First, the radial change of variables was recomputed from \(dt/dr=-1/r\) and \(ds/dt=1/t\), yielding the exact power cancellation \(-N(a+1)+\beta(N-1)=-1\). Second, the cutoff scaling was checked directly: the quadratic Taylor remainder contributes order \(L^-1\), while the \(X_2^q\) mass on the plateau has order \(L^{1-q}\), giving ratio order \(L^{q-2}\). Third, the source’s equations (6.16)–(6.17) were reread in full text: the only place where its published optimality proof restricts to \(\beta<1\) is the appeal to Propositions 5.2 and 5.3 for the condition \(q\ge2\); the Young-factorization step itself is parameter-sign independent. The new cutoff argument supplies precisely the missing \(\beta>1\) obstruction.

No finite experiment is used to infer an infinite statement. The argument is analytic for every \(N\ge2\), every \(\beta>1\), every real \(q<2\), and every bounded domain containing the origin.

## Relationship to prior work
Ghosh, arXiv:2610.03668v1, proves the weighted Hardy constant for every \(\beta\ne1\) and proves the Leray–Trudinger bound of Theorem 1.4 for every such \(\beta\), but states exponent optimality only for \(\beta<1\). Its proof explicitly invokes remainder-optimality propositions only in the ranges \(0<\beta<1\) and \(\beta<0\). The present argument fills that exact \(\beta>1\) gap.

Adimurthi–Ghosh–Mallick, arXiv:2604.06853v1, treats \(\beta>1\) for a logarithmically weighted gradient norm and proves exponential integrability on the punctured-domain completion, together with failure on the larger unpunctured space. That constraint is not the Hardy defect \(I_{\beta,\Omega}\), and the paper does not provide the \(X_2\)-exponent threshold asserted here. Di Blasio–Pisante–Psaradakis, arXiv:2208.05430v1, and Mallick–Tintarev, arXiv:1601.03194v1, determine the corresponding correction threshold for the classical unweighted Leray energy; they do not cover the \(\beta>1\) log-weighted defect.

Targeted semantic-index searches for the \(\beta>1\) weighted remainder, the \(X_2^q\) threshold, and the Leray–Trudinger exponent found no implication-equivalent result. The closest indexed Hardy–Rellich logarithmic obstruction concerns a different differential operator and a different critical-weight mechanism.

## Limitations
The result identifies the correction exponent but not the best positive exponential coefficient in Theorem 1.4. It also does not establish a positive sharp \(X_2^2\) remainder for \(\beta>1\); only the impossibility of every power below \(2\) is proved. The focal preprint is very recent, so indexing lag and an equivalent unpublished or differently worded argument remain residual originality risks.

## References
1. S. Ghosh, “On improved Hardy-type inequalities in Log-Weighted Sobolev Spaces,” arXiv:2610.03668v1, 2 Oct 2026.
2. Adimurthi, S. Ghosh, A. Mallick, “Leray-Trudinger Type Exponential Integrability in Log-Weighted Sobolev Spaces,” arXiv:2604.06853v1, 8 Apr 2026.
3. G. Di Blasio, G. Pisante, G. Psaradakis, “The optimal Leray-Trudinger inequality,” arXiv:2208.05430v1; Indiana Univ. Math. J. 74 (2025), 819–833.
4. A. Mallick, C. Tintarev, “An improved Leray-Trudinger inequality,” arXiv:1601.03194v1; Commun. Contemp. Math. 20 (2018), 1750034.

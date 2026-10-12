# Four seasons are necessary and sufficient for interior-optimal dispersal in a two-patch periodic model

## Finding
Consider a positive linear population model with two patches and a periodic sequence of \(k\) fitness environments. A fixed fraction \(d\in[0,1]\) joins an equally redistributed migrant pool after reproduction in each season. Let \(G_k(d)\) be the spectral radius of one full-period population propagator. Then, for every positive sequence of fitnesses and every \(k\in\{1,2,3\}\),
\[
\max_{0\le d\le1}G_k(d)=\max\{G_k(0),G_k(1)\}.
\]
For \(k=4\), the assertion fails: there are strictly positive integer fitnesses for which every global maximizer of \(G_4\) lies strictly between zero and one. Four is therefore the smallest number of fitness phases in which an interior dispersal choice can strictly outperform both complete retention and complete redistribution. The same conclusion holds if one maximizes the per-season growth factor \(G_k(d)^{1/k}\), because taking a positive root preserves comparisons.

## Assumptions and scope
Fix an integer \(k\ge1\) and strictly positive numbers \(a_t,b_t\), for \(t=1,\ldots,k\). Reproduction precedes dispersal, and seasonal population abundances obey
\[
N_{t+1}=M(d)F_tN_t,\qquad
M(d)=\begin{pmatrix}1-d/2&d/2\\ d/2&1-d/2\end{pmatrix},\quad
F_t=\operatorname{diag}(a_t,b_t).
\]
The seasonal fitness sequence repeats periodically and the *same* fraction \(d\) is used every season. No movement costs, density dependence, stochastic fluctuations, or fitness feedbacks are assumed. Define
\[
P_k(d)=M(d)F_k\cdots M(d)F_1,\qquad G_k(d)=\rho(P_k(d)).
\]
All numerical inequalities and minimax assertions range over the *closed interval* \(0\le d\le1\). The endpoint \(d=1\) is complete mixing into two equally likely destinations; the exchange probability is \(d/2\), not \(d\).

## Proof
**Step 1: normalize the two-patch matrices.** For each season set \(u_t=(a_t+b_t)/2>0\), \(r_t=(a_t-b_t)/(a_t+b_t)\in(-1,1)\), \(U=\prod_{t=1}^k u_t\), and \(x=1-d\in[0,1]\). In the symmetric/antisymmetric patch basis \((1,1),(1,-1)\), the scaled fitness is
\[
B_t=\begin{pmatrix}1&r_t\\r_t&1\end{pmatrix},
\]
and the mixing matrix is \(N(x)=\operatorname{diag}(1,x)\). Consequently, \(P_k(d)/U\) is similar to
\[
Q_k(x)=N(x)B_k\cdots N(x)B_1.
\]
For \(k\in\{2,3\}\), write \(T_k(x)=\operatorname{tr}Q_k(x)\), \(D_k(x)=\det Q_k(x)\), and \(q=\prod_{t=1}^{k}(1-r_t^2)\), so \(0<q\le1\). Multiplication yields the identities
\[
\begin{array}{lll}
k=2:&T_2(x)=1+2s x+x^2,&D_2(x)=q x^2,\quad s=r_1r_2,\\[2pt]
k=3:&T_3(x)=1+s(x+x^2)+x^3,&D_3(x)=q x^3,\quad s=r_1r_2+r_2r_3+r_3r_1.
\end{array}
\]
The characteristic polynomial is \(\chi_x(z)=z^2-T_k(x)z+D_k(x)\). At \(x=0\), the eigenvalues of \(Q_k(0)\) are \(1,0\); at \(x=1\) they are \(\prod_t(1+r_t)\) and \(\prod_t(1-r_t)\). Let \(L\) denote their larger value. Thus the normalized endpoint spectral radii are \(1\) and \(L\), and \(\chi_1(1)=-(2s+1-q)\) for both \(k=2,3\). In particular,
\[
L\le1\iff 2s\le -(1-q),\qquad L\ge1\iff 2s\ge -(1-q).
\]
This equivalence uses the fact that the product of the two positive endpoint eigenvalues is \(q\le1\). All matrices \(P_k(d)\) have nonnegative entries and nonnegative determinant for \(0\le d\le1\), so their two eigenvalues are real and nonnegative. Moreover \(D_k(x)\le1\); therefore the *smaller* eigenvalue is at most one. It follows that, for \(z\ge1\), a nonnegative value \(\chi_x(z)\ge0\) implies the larger eigenvalue is at most \(z\).

**Step 2: rule out strictly superior intermediate mixing for two phases.** If \(L\le1\), then for every \(0\le x\le1\),
\[
\chi_x(1)=-x\bigl[2s+(1-q)x\bigr]\ge0.
\]
If \(L\ge1\), use \(2s\ge -(1-q)\) to obtain
\[
\begin{aligned}
\chi_x(L)&-\chi_1(L)\\
&=(1-x)\bigl[(L-q)(1+x)+2Ls\bigr]\\
&\ge(1-x)\bigl[q(L-1)+x(L-q)\bigr]\ge0.
\end{aligned}
\]
Since \(\chi_1(L)=0\), either case bounds the spectral radius by \(\max\{1,L\}\).

**Step 3: rule out strictly superior intermediate mixing for three phases.** If \(L\le1\), then \(s\le-(1-q)/2\) and
\[
\chi_x(1)=-x\bigl[s(1+x)+(1-q)x^2\bigr]\ge0,
\]
because \(x^2\le(1+x)/2\) on \([0,1]\). If \(L\ge1\), use \(s\ge-(1-q)/2\), \(L-q\ge L(1-q)\), and \(1+x+x^2\ge(2+x)/2\) to conclude
\[
\begin{aligned}
\chi_x(L)&-\chi_1(L)\\
&=(1-x)\bigl[(L-q)(1+x+x^2)+Ls(2+x)\bigr]\\
&\ge(1-x)L(1-q)\left(\frac{x}{2}+x^2\right)\ge0.
\end{aligned}
\]
As before, both cases bound the spectral radius by \(\max\{1,L\}\). All inequalities include the endpoints and possible equalities.

**Step 4: one phase.** When \(k=1\), \(M(d)\) is column stochastic, and hence \(G_1(d)\le \|M(d)F_1\|_1=\max\{a_1,b_1\}=G_1(0)\).

**Step 5: exact four-phase witness.** Choose
\[
F_1=\operatorname{diag}(1,2),\quad
F_2=\operatorname{diag}(1,3),\quad
F_3=\operatorname{diag}(5,1),\quad
F_4=\operatorname{diag}(6,1).
\]
At no dispersal, \(G_4(0)=30\). At complete redistribution, the full-period product has rank one and \(G_4(1)=(3/2)\cdot2\cdot3\cdot(7/2)=63/2\). But at \(d=24/25\), exact rational multiplication gives
\[
P_4(24/25)=\frac1{390625}
\begin{pmatrix}4161198&8647704\\3926052&8159046\end{pmatrix},
\]
with \(\operatorname{tr}P_4=12320244/390625\) and \(\det P_4=36/78125\). Its characteristic polynomial at \(63/2\) is
\[
\left(\frac{63}{2}\right)^2-
\frac{12320244}{390625}\frac{63}{2}+
\frac{36}{78125}
=-\frac{1959399}{1562500}<0.
\]
For this positive matrix the sign is negative precisely between its two real eigenvalues, so its Perron root exceeds \(63/2\). The function \(G_4\) is continuous on the compact interval \([0,1]\); therefore its global maximum is attained, and every global maximizer is interior. This completes the sharp minimal-phase classification.

## Verification
The accompanying `verify_mixing.py` uses standard-library exact rational arithmetic. Run `python verify_mixing.py`. It checks the displayed two- and three-phase characteristic identities and endpoint inequalities over 750 rational cases, and verifies the four-phase matrix, trace, determinant, and strict negative characteristic-polynomial evaluation exactly. Its expected terminal result is `VERIFY_OK exact_traces_determinants_endpoint_characteristic=750 witness_negative_polynomial=1`. These finite checks are **not** used to infer the unrestricted two- or three-phase theorem; Steps 1–4 above prove that theorem for every allowed fitness choice.

## Relationship to prior work
The matrix model is a standard unconditional-dispersal metapopulation formulation. Kirkland, Li, and Schreiber (2006) prove a slower-disperser advantage under *time-independent* patch fitnesses. Schreiber (2010) derives stochastic partial-mixing growth approximations and exhibits intermediate dispersal benefits for a multi-patch ecological network. Schreiber and Li (2010 preprint; 2011 journal publication) analyze evolutionary dispersal in periodically varying environments, with key analytic conclusions under two-period structural hypotheses. Their objectives, parameter coverage, and results do not state or imply the sharp universal endpoint statement for all one-, two-, and three-phase *positive fitness sequences* and its exact four-phase counterexample. The comparison here concerns a spectral-growth optimization theorem, not a result about invasion equilibria, evolutionary stability, or stochastic persistence. Searches for period-three/period-four two-patch endpoint optimization and equivalent stochastic-matrix products did not locate this exact classification; this is evidence of non-overlap with inspected material, not proof that no equivalent result exists.

## Limitations
Only two patches, symmetric complete-pool redistribution, positive local growth factors, constant dispersal fraction across seasons, and deterministic linear dynamics are covered. The result does not say that any *particular* intermediate fraction is uniquely optimal, does not extend to more than two patches without additional proof, and does not assert an ecological fitness advantage under stochastic fluctuations or density dependence. The four-phase witness proves existence and minimality, not a universal four-phase interior optimum. Possible equivalent classifications in earlier, differently indexed dispersal or positive-matrix literature remain a residual originality risk. Independent validation has not been performed.

## References
1. Kirkland, S., Li, C.-K., and Schreiber, S. J. (2006). "On the evolution of dispersal in patchy landscapes." *SIAM Journal on Applied Mathematics* 66(4):1366–1382. DOI: 10.1137/050628933. Author-hosted full text: https://schreiber.faculty.ucdavis.edu/wp-content/uploads/sites/568/2022/09/050628933.pdf.
2. Schreiber, S. J. (2010). "Interactive effects of temporal correlations, spatial heterogeneity and dispersal on population persistence." *Proceedings of the Royal Society B* 277:1907–1914. DOI: 10.1098/rspb.2009.2006. Open full text: https://pmc.ncbi.nlm.nih.gov/articles/PMC2871869/.
3. Schreiber, S. J., and Li, C.-K. (2010). "Evolution of unconditional dispersal in periodic environments." arXiv:1007.5267v1 (first posted July 29, 2010); subsequently *Journal of Biological Dynamics* 5:120–134 (2011). DOI: 10.1080/17513758.2010.525667.

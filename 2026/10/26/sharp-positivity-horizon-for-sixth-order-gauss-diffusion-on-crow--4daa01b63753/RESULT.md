# Sharp positivity horizon for sixth-order Gauss diffusion on crown networks

## Finding
For every integer \(n\ge3\), let \(G_n=K_{n,n}\setminus\{(i,i'):1\le i\le n\}\) be the crown graph, with unit edge conductances and combinatorial graph Laplacian \(L_n\). The completed three-stage Gauss–Legendre (sixth-order diagonal Padé) step for \(\dot u=-L_nu\) is \(T_n(h)=P(hL_n)Q(hL_n)^{-1}\), where
\[
P(z)=120-60z+12z^2-z^3,\qquad Q(z)=120+60z+12z^2+z^3.
\]
There exists a unique \(H_n>0\) such that \(T_n(h)\) is entrywise nonnegative **exactly** for \(0\le h\le H_n\). The threshold is the unique positive solution of
\[
1+R((2n-2)h)+(n-1)\bigl(R(nh)+R((n-2)h)\bigr)=0,\qquad R=P/Q.
\]
Every off-diagonal entry of \(T_n(h)\) is strictly positive for every \(h>0\); only its diagonal entries can become negative. Despite this, \(T_n(h)\) is a symmetric, row-stochastic-in-the-algebraic-sense spectral contraction (row sums equal one and Euclidean operator norm equal one) for all \(h\ge0\). Its positivity horizon obeys
\[
\lim_{n\to\infty} nH_n=\rho=4.64437070925217\ldots,
\]
where \(\rho\) is the unique positive root of \(P(\rho)=0\).

## Assumptions and scope
Vertices are \(a_1,\ldots,a_n,b_1,\ldots,b_n\); \(a_i\) joins \(b_j\) exactly when \(i\ne j\). All edges have conductance one and there are no other edges. The step size \(h\) is nonnegative. Entrywise nonnegativity is a property of the **completed step**, not of its internal Gauss stages. The graph Laplacian acts on the standard Euclidean coordinate space. For all nonnegative \(z\), \(Q(z)>0\), so the matrix step is well-defined.

## Proof
Write \(r_t=R(th)\). The four orthogonal spectral sectors are the constants (eigenvalue \(0\)), the between-halves antisymmetric constants (eigenvalue \(2n-2\)), the within-half equal-sign zero-sum vectors (eigenvalue \(n-2\)), and the within-half opposite-sign zero-sum vectors (eigenvalue \(n\)). The nonzero eigenvalues have multiplicities \(1,n-1,n-1\), respectively. Put \(a=r_n\), \(b=r_{n-2}\), \(c=r_{2n-2}\). Exact spectral projection gives four matrix entries: diagonal \(d\), distinct same-half \(w\), opposite-half deleted matching \(m\), and opposite-half existing edge \(e\):
\[
2nd=1+c+(n-1)(a+b),\quad 2nw=1+c-a-b,
\]
\[
2nm=1-c+(n-1)(a-b),\quad 2ne=1-c-a+b.
\]
We establish strict positivity of \(w,m,e\) simultaneously for all integers \(n\ge3\) and real \(h>0\) by an exact polynomial certificate. Substitute \(u=n-2\ge1\) into these expressions and multiply each by the positive common denominator \(Q(nh)Q((n-2)h)Q((2n-2)h)\). After substituting \(n=u+2\), each resulting polynomial in \((u,h)\) has **only positive integer coefficients**: respectively 40, 32, and 48 nonzero monomials, with smallest powers of \(h\) equal to \(2,3,1\). The complete multiplication and coefficient checks are replayed in the self-contained `crown_verify.py` file; no numerical sampling is used to establish these universal coefficient claims. As \(u\ge1,h>0\), the three entries are strictly positive. This finite exact-identity certificate is sufficient for their global signs because every rational denominator is strictly positive.

Direct differentiation gives
\[
R'(z)=-\frac{24\bigl(z^4-30z^2+600\bigr)}{Q(z)^2}<0
\]
for \(z\ge0\), since \(z^4-30z^2+600=(z^2-15)^2+375\). Thus \(d(h)\) is strictly decreasing, with \(d(0)=1\) and \(\lim_{h\to\infty}d(h)=-(n-1)/n<0\), since \(R(0)=1\) and \(R(+\infty)=-1\). Consequently it has exactly one zero \(H_n>0\), and the sign of every entry of the matrix is now classified. Also \(Q(z)-P(z)=2z(z^2+60)>0\) and \(Q(z)+P(z)=24(z^2+10)>0\) for \(z>0\), whence \(|R(z)|<1\). Along with the constant-mode multiplier one and symmetry, this proves \(\|T_n(h)\|_2=1\), while constant preservation gives row sums one.

For the scaling limit, fix \(x\ge0\). From the displayed diagonal formula,
\[
\lim_{n\to\infty}d(x/n)=R(x)
\]
locally uniformly in \(x\), because both \(nh\) and \((n-2)h\) tend to \(x\), and the remaining \(1/(2n)\)-weighted term vanishes. The function \(R\) is strictly decreasing from \(1\) to \(-1\), so it has exactly one positive zero \(\rho\). Bracketing each unique zero of \(d\) between \((\rho-\varepsilon)/n\) and \((\rho+\varepsilon)/n\) proves \(nH_n\to\rho\).

## Verification
Run `python3 crown_verify.py` in the same directory. The standard-library checker implements sparse integer-polynomial multiplication and asserts strict positivity of **every** coefficient of the three cleared-denominator polynomials in the independent formal variables \(u,h\); reports 40, 32, and 48 positive monomials and smallest time orders 2, 3, and 1. It independently forms actual rational Laplacian matrices, evaluates \(P(hL)Q(hL)^{-1}\) using exact Gauss–Jordan inversion, and compares all entries to the four spectral formulas for \(n=3,\ldots,8\) at six step sizes (36 full-matrix checks). Bisection numbers are illustrations only. The coefficient identities and monotonicity argument prove the infinite-parameter theorem.

## Relationship to prior work
The general theory of monotonicity constraints for time integration is developed by Spijker (2006). Strong-stability-preserving time discretizations are surveyed by Gottlieb, Ketcheson and Shu; Conde, Gottlieb, Grant and Shadid develop implicit SSP schemes, with objectives different from this exact graph-specific completed Gauss map. Klee and Stamps analyze crown-graph Laplacian eigenvalues but not high-order time-step entrywise positivity. The statement is also different from previously indexed analyses of two-stage Padé methods on Markov generators and from combinatorial studies of crowns. The novelty comparison concerns the **exact [3/3] crown positivity horizon, off-diagonal positivity for all positive steps, and large-graph scaling**, not the known spectrum or Padé formula by itself.

## Limitations
Only simple unweighted crown graphs with \(n\ge3\), uniform timestep, the completed sixth-order Gauss map, and coordinatewise positivity are covered. The result does not guarantee stage positivity, physical-time sampling accuracy, or identical thresholds for weighted or perturbed graphs. A known graph spectrum and rational stability function are used; other specialized prior work might imply this closed classification. The review is self-review only; independent validation has not been performed.

## References
- M. N. Spijker, *Stepsize conditions for general monotonicity in numerical initial value problems*, Leiden mathematical report 2006-08, listed June 3, 2006. https://www.math.leidenuniv.nl/reports/
- S. Gottlieb, D. I. Ketcheson and C.-W. Shu, *High Order Strong Stability Preserving Time Discretizations*, survey (2008), publicly accessible full text.
- S. Conde, S. Gottlieb, Z. Grant and J. Shadid, *Implicit and Implicit-Explicit Strong Stability Preserving Runge–Kutta Methods with High Linear Order*, https://arxiv.org/abs/1702.04621 (2017).
- S. Klee and M. T. Stamps, *Eigenvalues of Graph Laplacians Via Rank-One Perturbations*, *Quarterly Journal of Mathematics* 73 (2022), DOI: 10.1093/qmath/haab045, https://academic.oup.com/qjmath/article/73/2/609/6432406.

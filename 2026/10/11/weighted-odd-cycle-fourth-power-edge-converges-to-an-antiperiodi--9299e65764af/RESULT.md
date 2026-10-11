# Weighted odd-cycle fourth-power edge converges to an antiperiodic Sturm–Liouville eigenvalue

## Finding
Let \(a:\mathbb R/\mathbb Z\to(0,\infty)\) be a positive continuously differentiable one-periodic real function. For an integer \(n\ge3\), define \(a_j=a((j-1)/n)\) and \(b_j=(a_{j-1}+a_j)/2\), with indices understood modulo \(n\). For \(x\in\mathbb R^n\setminus\{0\}\), put
\[
R_{n,a}(x)=\frac{\sum_{j=1}^na_j|x_j-x_{j+1}|^4}{\sum_{j=1}^nb_j|x_j|^4},\qquad \Lambda_{n,a}=\max_{x\ne0}R_{n,a}(x),\quad x_{n+1}=x_1.
\]
Define the lowest antiperiodic weighted Sturm–Liouville Rayleigh value
\[
\mu(a)=\min_{\substack{W\in H^1(0,1),\;W(1)=-W(0)\\ W\ne0}}
\frac{\int_0^1a(t)|W'(t)|^2\,dt}{\int_0^1a(t)|W(t)|^2\,dt}.
\]
Then \(0<\mu(a)<\infty\), every even \(n\) satisfies \(\Lambda_{n,a}=16\), every odd \(n\) satisfies \(\Lambda_{n,a}<16\), and the **sharp weighted odd-cycle limit** is
\[
\boxed{\lim_{\substack{n\to\infty\\n\ \mathrm{odd}}}n^2(16-\Lambda_{n,a})=6\mu(a).}
\]
The coefficient is a genuinely variable-coefficient spectral invariant: for constant \(a\), \(\mu(a)=\pi^2\), while varying edge conductances replaces the constant by the corresponding weighted antiperiodic eigenvalue.

## Assumptions and scope
Equivalently, \(\Lambda_{n,a}^{1/4}\) is the operator norm of the cyclic difference between the weighted real \(\ell_4^n(b)\) and \(\ell_4^n(a)\) spaces. The graph is the cyclic arrangement of \(n\) real vertices with positive edge weights sampled from a fixed \(C^1\) periodic profile. The vertex masses \(b_j\) are exactly the average of incident edge weights. These masses are essential: they normalize the bipartite upper bound to \(16\). The result concerns the highest fourth-power graph Rayleigh quotient, not the smallest signless eigenvalue, and no statement is asserted for discontinuous profiles, other exponents, or multidimensional graphs.

For odd \(n\), write \(x_j=(-1)^j u_j\) and impose \(u_{n+1}=-u_1\). Then the numerator is \(\sum_j a_j(u_j+u_{j+1})^4\). Let \(\Phi(u)=u|u|\) and
\[
e(u,v)=8(u^4+v^4)-(u+v)^4=6(u^2-v^2)^2+(u-v)^4.
\]
For all real \(u,v\), \(e(u,v)\ge4|\Phi(u)-\Phi(v)|^2\), while if \(uv\ge0\), \(e(u,v)\ge6|\Phi(u)-\Phi(v)|^2\). For opposite signs \(A=|u|\), \(B=|v|\), the difference from the lower bound with coefficient four factors as \((A-B)^2(A+3B)(3A+B)\ge0\).

## Proof
**Exact normalized defect and parity.** Since the \(j\)-th vertex belongs to edges with weights \(a_{j-1}\) and \(a_j\), direct collection of the quartic terms gives
\[
16\sum_jb_ju_j^4-\sum_ja_j(u_j+u_{j+1})^4=\sum_ja_je(u_j,u_{j+1}). \tag{1}
\]
All terms on the right are nonnegative. Equality throughout requires \(u_{j+1}=u_j\) and is incompatible with the antiperiodic boundary for odd \(n\) unless \(u=0\). For even \(n\), constant-magnitude alternating \(x\) attains the upper bound \(16\). Thus the parity assertions hold for every admissible profile.

**Compactness and lower bound.** Along odd \(n\), choose a maximizing vector, normalize \(n^{-1}\sum_j b_j u_j^4=1\), and set \(w_j=\Phi(u_j)\). Define its defect \(E_n=\sum_j a_je(u_j,u_{j+1})=n(16-\Lambda_{n,a})\). The recovery construction below shows \(\limsup nE_n\le6\mu(a)\); in particular the sequence \(nE_n\) is bounded. The global coercive inequality and \(\inf a>0\) imply
\[
n\sum_j(w_{j+1}-w_j)^2=O(1),\qquad w_{n+1}=-w_1.\tag{2}
\]
Let \(W_n\) be the piecewise-linear interpolation of these nodes on the uniform mesh. It has antiperiodic endpoints and \(\int_0^1|W_n'|^2=n\sum_j(w_{j+1}-w_j)^2\). Weighted normalization, uniform positive lower and upper bounds on the weights, and the derivative estimate imply a uniform \(H^1\) bound. As the mesh weights \(b_j\) converge uniformly to \(a\), the piecewise-linear and step interpolants differ uniformly by \(O(n^{-1/2})\); therefore \(\int_0^1 aW_n^2\to1\). After passage to a subsequence, \(W_n\to W\) uniformly and weakly in \(H^1(0,1)\), with \(W(1)=-W(0)\) and \(\int aW^2=1\).

On every compact subinterval of \(\{t:W(t)\ne0\}\), neighboring samples \(u_j,u_{j+1}\) eventually have the same sign. The stronger local defect bound, uniform convergence of \(a_j\) to the edge profile, and weak lower semicontinuity give, by exhaustion of the nonzero set,
\[
\liminf_{n\to\infty}nE_n\ge6\int_{\{W\ne0\}}a|W'|^2=6\int_0^1a|W'|^2\ge6\mu(a). \tag{3}
\]
The middle equality uses the fact that the weak derivative of an absolutely continuous function vanishes almost everywhere on its zero set.

**Recovery and upper bound.** The antiperiodic Rayleigh minimum is attained by compactness of the embedding \(H^1(0,1)\hookrightarrow L^2(0,1)\) and positivity of \(a\). A normalized minimizer \(W\) solves \(-(aW')'=\mu(a)aW\), is \(C^2\), and is not identically zero. Its zeros in the compact interval are finite and simple: otherwise uniqueness for the second-order ODE would force the solution to vanish identically. Put \(u(t)=\operatorname{sgn}(W(t))\sqrt{|W(t)|}\) and sample \(u_j=u((j-1)/n)\) with \(u_{n+1}=-u_1\). Weighted Riemann sums give \(n^{-1}\sum b_j u_j^4\to\int aW^2=1\). Identity (1) yields
\[
E_n^{\mathrm{trial}}=6\sum_ja_j\bigl(|W(t_j)|-|W(t_{j+1})|\bigr)^2+\sum_ja_j\bigl(u(t_j)-u(t_{j+1})\bigr)^4.
\]
The first sum satisfies \(n\sum_j a_j(\Delta|W|)^2\to\int_0^1a|W'|^2=\mu(a)\), since \(|W|\in H^1\) and is piecewise continuously differentiable. Near each simple zero, the modulus of \(u\) has square-root behavior. The increment on the \(k\)-th mesh interval from a zero is bounded by \(Cn^{-1/2}(k+1)^{-1/2}\); hence the sum of all fourth powers of these increments is \(O(n^{-2})\). Away from the finitely many zeros the increments are \(O(n^{-1})\). Therefore \(nE_n^{\mathrm{trial}}\to6\mu(a)\). Dividing by the trial denominator (which is asymptotic to \(n\)) proves \(\limsup n^2(16-\Lambda_{n,a})\le6\mu(a)\), matching (3).

The weighted antiperiodic Rayleigh minimizer has positive eigenvalue: a constant function satisfying antiperiodic endpoints must vanish. This completes the proof.

## Verification
The supplied script `verify_weighted.py` checks the exact defect identity for rational vertex values and rational positive cyclic edge weights, and checks that the even-cycle alternating pattern gives the precise normalized upper bound. It also verifies the constant-weight cosine recovery numerically. Run `python3 verify_weighted.py` with a standard Python 3 installation. These checks verify finite algebra only; the uniform spectral limit relies on the compactness/localization and recovery arguments above.

## Relationship to prior work
Keller–Mugnolo [1] prove graph \(p\)-Laplacian Cheeger inequalities rather than sharp highest weighted-cycle spectral-edge asymptotics. Tudisco–Hein [2] give nodal-domain and higher-order Cheeger bounds. Borba–Schwerdtfeger [3] compute the largest *signless* \(p\)-eigenvalue on odd cycles and bound the smallest signless eigenvalue, but neither assertion controls the greatest ordinary weighted fourth-power difference Rayleigh quotient. Ge–Qin [4] develop signed-graph eigenpair algorithms without this variable-coefficient continuum limit. The antiperiodic Sturm–Liouville problem here is the genuine effective weighted continuum limit of the nonlinear discrete extremal problem, not the original nonlinear \(p\)-Laplacian continuum limit.

## Limitations
The proof requires positive periodic \(C^1\) conductance profiles and normalized vertex masses \(b_j\) as defined. It determines the sharp leading asymptotic only. It does not classify the finite-dimensional maximizers, give a closed form for \(\mu(a)\) for arbitrary weights, or address complex scalars or different powers. An unindexed equivalent weighted spectral-limit result may exist.

## References
1. M. Keller and D. Mugnolo, *General Cheeger inequalities for \(p\)-Laplacians on graphs*, arXiv:1509.06062, first public 2015-09-20, https://arxiv.org/abs/1509.06062.
2. F. Tudisco and M. Hein, *A nodal domain theorem and a higher-order Cheeger inequality for the graph \(p\)-Laplacian*, arXiv:1602.05567, first public 2016-02-17, https://arxiv.org/abs/1602.05567.
3. E. M. Borba and U. Schwerdtfeger, *Eigenvalue bounds for the signless \(p\)-Laplacian*, arXiv:1610.01357, first public 2016-10-05, https://arxiv.org/abs/1610.01357.
4. C. Ge and O. Qin, *Computing the \(p\)-Laplacian eigenpairs of signed graphs*, arXiv:2501.07929, first public 2025-01-14, https://arxiv.org/abs/2501.07929.

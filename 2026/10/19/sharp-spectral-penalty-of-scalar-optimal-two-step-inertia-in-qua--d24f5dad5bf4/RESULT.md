# Sharp spectral penalty of scalar-optimal two-step inertia in quadratic proximal iterations

## Finding
Let \(0<q<1\). For a self-adjoint proximal contraction with spectrum contained in \([0,q]\), apply the constant-parameter two-step inertial iteration
\[
 y_n=x_n+\theta(x_n-x_{n-1})+\delta(x_{n-1}-x_{n-2}),\qquad x_{n+1}=Ty_n.
\]
For the single scalar mode \(T=qI\), the smallest spectral radius among **all real** \((\theta,\delta)\) is uniquely attained at
\[
 t=1-(1-q)^{1/3},\qquad
 \theta_\star=\frac{3t}{q}-1,\qquad
 \delta_\star=-\frac{t^3}{q},
\]
where the modal characteristic polynomial is \((z-t)^3\). Nevertheless, with these *same* parameters frozen, the exact worst-case asymptotic spectral radius over **all** modes \(s\in[0,q]\) is
\[
 \boxed{\displaystyle\max_{0\le s\le q}\rho_s=\frac{2}{\sqrt3}\,t},
\]
and the unique maximizing mode is \(\boxed{s=8q/9}\). Thus the faster-contracting mode has a strictly slower asymptotic iteration rate than the scalar mode used for tuning, by the exact universal factor \(2/\sqrt3\).

There is an explicit strongly convex quadratic realization *inside* the cited three-operator method's strict sufficient convergence regime: take
\[
 f(x)=\frac12x^{\mathsf T}\operatorname{diag}(1,5/4)x,\quad
 A=\nabla f,\quad B=C=0,\quad\gamma=\rho=1.
\]
Then \(T=(I+A)^{-1}=\operatorname{diag}(1/2,4/9)\). With \(q=1/2\), the preceding tuning is admissible under Condition 3.2 of Iyiola–Jolaoso–Shehu with \(\eta=2\), but the second eigenmode is asymptotically slower: its rate is \(0.2382141137\ldots\), versus \(0.2062994740\ldots\) for the tuned mode.

As a separate exact consequence for the **formal constant-parameter recurrence** (not an extension of that source's sufficient parameter regime), the uniformly tuned iteration converges on every self-adjoint \(T\) with spectrum in \([0,q]\) exactly when
\[
 q<1-\left(1-\frac{\sqrt3}{2}\right)^3=0.9975952641\ldots.
\]
At equality a possible interior mode has characteristic roots of modulus one; above it a possible interior mode has modulus greater than one.

## Assumptions and scope
All statements concern exact arithmetic and fixed scalar parameters. For the first two assertions, \(0<q<1\), \(s\in[0,q]\), and the scalar modal recurrence is understood as a linear evolution on the lifted state \((x_n,x_{n-1},x_{n-2})\). Its rate means the spectral radius of the associated \(3\times3\) companion matrix, not a uniform bound of the form \(C t^n\) at a defective root. For the quadratic example, the spatial dimension is two and all three initial vectors can be arbitrary. For the uniform convergence statement, the result holds for every finite-dimensional self-adjoint linear operator with spectrum in \([0,q]\). The zero operator, empty active modal subspaces, and special initial states may converge faster; the spectral-rate conclusions concern the operator itself and generic nonzero modal data.

## Proof
**1. Exact scalar optimum and its uniqueness.** The scalar characteristic polynomial for eigenvalue \(s\) of \(T\) is
\[
 p_s(z)=z^3-s(1+\theta)z^2+s(\theta-\delta)z+s\delta.
\]
For the tuned eigenvalue \(s=q\), one has \(p_q(1)=1-q\), independently of inertia. Write its three complex roots, with multiplicity, as \(r_1,r_2,r_3\). Let \(R=\max_i|r_i|\). If \(R\ge1\), then \(R>t\). If \(R<1\), then
\[
 1-q=|p_q(1)|=\prod_{i=1}^{3}|1-r_i|
 \ge\prod_{i=1}^{3}(1-|r_i|)\ge(1-R)^3.
\]
Hence \(R\ge1-(1-q)^{1/3}=t\). If equality holds, equality in the reverse triangle inequalities forces all three \(r_i\) to be the positive real number \(t\). Thus \(p_q(z)=(z-t)^3\). Comparing its quadratic and constant coefficients forces the stated unique \(\theta_\star,\delta_\star\). The linear coefficient then agrees because \(q=3t-3t^2+t^3\), an identity equivalent to the definition of \(t\). This proves attainable global scalar optimality over **all** real parameters, without imposing the source's sufficient convergence conditions during the minimization.

**2. Sharp complete modal envelope.** Freeze the optimal parameters and set \(s=kq\) with \(0\le k\le1\). Substitution of \(z=tu\) gives
\[
 \frac{p_{kq}(tu)}{t^3}=u^3-3ku^2+3ku-k.
\]
At \(k=0\) its roots are zero; at \(k=1\) they all equal one. For \(0<k<1\), its derivative in \(u\) equals \(3[(u-k)^2+k(1-k)]>0\). It therefore has exactly one real root \(u\in(0,1)\) and a conjugate pair. Rearranging the real-root equation gives
\[
 k=\frac{u^3}{D(u)},\qquad D(u)=3u^2-3u+1>0.
\]
This map is strictly increasing from zero to one because its derivative is \(3u^2(u-1)^2/D(u)^2>0\) for \(0<u<1\). By Vieta, the squared modulus of each nonreal root is \(k/u=u^2/D(u)\). Since \(D(u)=3(u-1/2)^2+1/4\le1\) on \([0,1]\), the nonreal root modulus \(u/\sqrt{D(u)}\) is at least the real-root modulus \(u\). Therefore the complete modal spectral radius is
\[
 \rho_s=t\,\frac{u}{\sqrt{D(u)}}.
\]
The derivative of its squared normalized factor is
\[
 \frac{\mathrm d}{\mathrm du}\frac{u^2}{D(u)}
 =\frac{u(2-3u)}{D(u)^2}.
\]
It has a unique maximum at \(u=2/3\), where \(D=1/3\), \(k=u^3/D=8/9\), and \(u/\sqrt D=2/\sqrt3\). Continuity handles both endpoints. This proves the exact unique worst mode and factor, for every \(0<q<1\).

**3. Quadratic realization and sufficient-parameter compatibility.** With \(A=\operatorname{diag}(1,5/4)\), \(B=C=0\), \(\gamma=\rho=1\), the complete Davis–Yin update is exactly \(x_{n+1}=\operatorname{prox}_f(y_n)=(I+A)^{-1}y_n\); its eigenvalues are \(1/2\) and \(4/9=(8/9)(1/2)\). At \(q=1/2\), \(t=1-2^{-1/3}\), so \(\theta=6t-1\), \(\delta=-2t^3\), and \(\eta=2\) yields the cited averagedness constant \(\beta=4/7\). All of Condition 3.2 holds strictly. For a reproducible *rational* proof, cubing positive rational bounds gives \(20629/100000<t<20631/100000\). Thus \(2377/10000<\theta<238/1000\) and \(-18/1000<\delta<-17/1000\). The upper allowable \(\theta\) is \(\min\{1/2,3/11\}=3/11\), so condition (i) holds, and \(0<\rho=1<7/4\) proves (ii). For (iii), its first strict lower bound is \(-1+11\theta/3<-0.018<\delta\); the numerator of the second lower bound, \(L=(4/7)\theta(1+\theta)-(3/7)(1-\theta)^2\), satisfies \(L<-0.07\), and hence \(L/(1+\theta)<-0.07/1.238<-0.018<\delta\). Finally the remaining required inequality is \(L<R\), where \(R=(2\theta-4/7+2)\delta-(1/7)\delta^2\). Using \(2\theta-4/7+2<2\) and \(-0.018<\delta<0\) gives \(R>-0.036-(0.018)^2/7>-0.07>L\). Every cited strict inequality is proved by rational bounds, independently of floating point calculation.

**4. Uniform convergence threshold.** For finite-dimensional self-adjoint \(T\), orthogonally decompose by eigenmodes. Its lifted iteration is a direct sum of companion blocks. Every lifted state converges to zero exactly when their maximum spectral radius is below one; the sharp worst radius derived above is \(2t/\sqrt3\). Solving \(2t/\sqrt3<1\) gives the displayed \(q\)-threshold. At equality the interior mode has nonreal characteristic roots on the unit circle, and above it that mode is unstable. Neither conclusion relies on the sufficient parameter restrictions of the motivating splitting paper.

## Verification
The accompanying standalone `verify.py` uses exact SymPy identities to reproduce the repeated-root polynomial, modal factorization, monotone parameter map, and unique maximizer. It checks rational brackets for admissibility, samples 8,008 scalar mode matrices across eight base contractions, and compares 100 direct proximal updates against the two-dimensional matrix recurrence. The numerical checks are diagnostics, **not** a substitute for the analytic infinite-range arguments above. Run `python verify.py` with SymPy and NumPy installed. The file is complete and independent of all historical packages.

## Relationship to prior work
Suantai, Inkrong and Cholamjiak (2023) study double-inertial forward–backward–forward solvers in numerical mathematics (their listed primary MSC is 65Y05), emphasizing weak convergence and empirical performance. Their subscription full text was not accessible, so no whole-document noncoverage is inferred from its abstract. Iyiola, Jolaoso and Shehu (arXiv:2410.01099v1, 2024) supply the **exact** three-operator extrapolation and parameter regime used in the explicit quadratic example; their first listed primary MSC is 47H05, so that work is treated as adjacent supporting literature, not as a source of the present numerical-optimization classification. Its available complete HTML sections on the algorithm, Condition 3.2, theoretical convergence, and numerical illustrations were checked; they do not state the exact scalar-optimal triple-root characterization or the universal interior-mode penalty. Standard root-radius bounds, Vieta's formula, and spectral decompositions are prior mathematical tools. Closest recorded comparisons concern two-stage Richardson safety, three-mode steepest-descent sensitivity, and two-row Kaczmarz defective-root transient behavior; none supplies a theorem about the specific cubic inertial proximal recurrence and its \(8/9\) interior maximizer.

## Limitations
The theorem does not assert uniform optimality of these inertia parameters on \([0,q]\), nor that all initial states attain the spectral radius. It does not analyze variable steps, nonsymmetric or nonnormal operators, stochastic updates, nonlinear local maps, or floating-point effects. For large \(q\), the scalar-optimal parameters may violate published sufficient conditions; the robust-stability corollary is about the formally defined linear recurrence. The complete subscription text of the 2023 numerical method could not be examined. Exact priority against all possible older multistep spectral analyses is not established; these are documented literature-access and potential equivalence risks, not claims of novelty proof from unsuccessful searches.

## References
1. S. Suantai, P. Inkrong and P. Cholamjiak, *Forward–backward–forward algorithms involving two inertial terms for monotone inclusions*, Computational and Applied Mathematics 42 (2023), article 255. DOI: 10.1007/s40314-023-02388-6. Publicly published 18 July 2023; listed first MSC 65Y05.
2. O. S. Iyiola, L. O. Jolaoso and Y. Shehu, *Three-Operator Splitting Method with Two-Step Inertial Extrapolation*, arXiv:2410.01099v1, 1 October 2024. Algorithm (17), Condition 3.2, Sections 3–4.
3. P. L. Combettes and J.-C. Pesquet, *Proximal splitting methods in signal processing*, in Fixed-Point Algorithms for Inverse Problems in Science and Engineering, 2011 (standard proximal background only; not an originality comparison).

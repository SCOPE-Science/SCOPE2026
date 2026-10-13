# Exact run-length stability law and unbounded finite-time cancellation for periodically stale gradient descent

## Finding

For the scalar strongly convex objective \(f(x)=a x^2/2\), with \(a>0\), consider the constant-stepsize delayed-gradient recurrence
\[
 x_{k+1}=x_k-\eta a\,x_{k-d_k},\qquad d_k\in\{0,1\},\quad \eta>0,
\]
where the deterministic delay word repeats with a finite period \(q\ge1\). Put \(t=\eta a\). Suppose the period contains at least one zero-delay update, and list the lengths \(L_1,\ldots,L_m\ge0\) of all consecutive one-delay runs between successive zero-delay updates around the cyclic word; thus \(m\ge1\) and \(q=m+\sum_iL_i\). Define polynomials by
\[
 p_0(t)=1-t,\qquad p_1(t)=1-2t,\qquad
 p_{L+2}(t)=p_{L+1}(t)-t p_L(t).
\]
**Exact all-pattern classification:** Every initial pair \((x_{-1},x_0)\in\mathbb R^2\) converges to zero if and only if
\[
 \left|\prod_{i=1}^m p_{L_i}(t)\right|<1.
\]
When equality holds, at least one nonzero initial pair fails to converge. When the product vanishes, **every initial pair is annihilated after at most two complete periods** (measuring periods from the specified initial phase). Thus the closed-form asymptotic contraction factor per update is \(\left|\prod_i p_{L_i}(t)\right|^{1/q}\), with factor zero interpreted as finite termination.

The run polynomials have the exact product factorization
\[
 p_L(t)=\prod_{j=1}^{\lfloor(L+2)/2\rfloor}
 \left(1-4t\cos^2\frac{j\pi}{L+3}\right),
\]
so their positive simple roots are
\[
 t_{L,j}=\frac{1}{4\cos^2(j\pi/(L+3))},\qquad
 1\le j\le\lfloor(L+2)/2\rfloor.
\]
Consequently, the schedule consisting of one fresh update followed by \(L\) stale updates terminates from **every** initial pair in at most \(2(L+1)\) updates whenever \(t=t_{L,j}\). The largest such root satisfies
\[
 t_{L,\max}\sim
 \begin{cases}
 (L+3)^2/\pi^2,&L\text{ even},\\[2pt]
 (L+3)^2/(4\pi^2),&L\text{ odd},
 \end{cases}
\]
so there is **no finite upper bound on the stepsizes admitting some periodic binary-delay schedule with finite-time termination**. This does **not** mean any fixed schedule is stable at arbitrarily large stepsizes.

Already the shortest reentrant example, the word \((0,1,1)\), has
\[
 p_2(t)=t^2-3t+1,\qquad
 \text{stability exactly for }\ t\in(0,1)\cup(2,3).
\]
At \(t=(3+\sqrt5)/2>2\), the state is annihilated after two periods although a single fresh-gradient step of that size is unstable.

## Assumptions and scope

The recurrence is exact arithmetic, deterministic, and noise-free; there is one scalar curvature \(a>0\), one fixed stepsize \(\eta>0\), and a known periodic delay schedule taking only zero and one. Stability means convergence to the minimizer \(0\) for **every** initial pair, not monotonic decrease at individual updates or robustness to changing the prescribed schedule. The zero-delay-containing condition is essential to the rank-one reduction. For the all-one delay word, the time-independent characteristic polynomial is \(\lambda^2-\lambda+t\), and the Schur-stability interval is instead \(0<t<1\). All statements include boundaries: the strict inequality is required for convergence from every initial pair.

## Proof

Write \(s_k=(x_k,x_{k-1})^{\mathsf T}\). The two update matrices are
\[
 T_0(t)=\begin{pmatrix}1-t&0\\1&0\end{pmatrix},\qquad
 T_1(t)=\begin{pmatrix}1&-t\\1&0\end{pmatrix}.
\]
The first matrix is rank one: \(T_0=v e_1^{\mathsf T}\), where \(v=(1-t,1)^{\mathsf T}\) and \(e_1=(1,0)^{\mathsf T}\). For any run of \(L\) delayed updates following a zero-delay update, the block matrix is
\[
 B_L=T_1^L T_0=(T_1^L v)e_1^{\mathsf T}.
\]
Its nonzero eigenvalue (possibly zero) is \(e_1^{\mathsf T}T_1^L v=p_L(t)\). Indeed, its first coordinate obeys the displayed two-term recurrence with first values \(1-t\) and \(1-2t\). A cyclic rotation of the period preserves the characteristic polynomial of the monodromy matrix: for square factors \(A,B\), the products \(AB\) and \(BA\) have the same characteristic polynomial. We may therefore rotate to a zero-delay update and group the monodromy into blocks \(B_{L_m}\cdots B_{L_1}\).

Products of rank-one blocks satisfy
\[
 B_{L_m}\cdots B_{L_1}
 =(T_1^{L_m}v)\biggl(\prod_{i=1}^{m-1}p_{L_i}(t)\biggr)e_1^{\mathsf T}.
\]
Hence its determinant is zero and its trace is \(\prod_{i=1}^{m}p_{L_i}(t)\); its two characteristic roots are zero and that product. Floquet reduction for the finite period now proves the strict stability criterion. At modulus one, an eigenvector for the unit-modulus root gives a nondecaying trajectory at period boundaries. At a vanishing product, trace and determinant are zero, so Cayley–Hamilton gives \(M^2=0\); thus every state is zero after two periods. Intermediate states are zero thereafter as well.

For the root formula, let \(A_{L+2}\) be the symmetric adjacency matrix of a path on \(L+2\) vertices and set \(D_r(t)=\det(I_r-\sqrt t\,A_r)\). Cofactor expansion at the endpoint yields \(D_0=D_1=1\) and \(D_r=D_{r-1}-tD_{r-2}\). Thus \(D_{L+2}=p_L\). The elementary sine eigenvectors of the path adjacency matrix have simple eigenvalues \(2\cos(j\pi/(L+3))\) for \(j=1,\ldots,L+2\). Pairing their positive and negative eigenvalues gives precisely the claimed factorization. Positive cosines decrease strictly as \(j\) increases in the stated range, so all listed roots are positive and simple.

The largest root corresponds to the angle closest below \(\pi/2\). When \(L\) is even, that angle has gap \(\pi/[2(L+3)]\), yielding
\[
 t_{L,\max}=\frac{1}{4\sin^2(\pi/[2(L+3)])}.
\]
When \(L\) is odd, the gap is \(\pi/(L+3)\), giving
\[
 t_{L,\max}=\frac{1}{4\sin^2(\pi/(L+3))}.
\]
The stated quadratic asymptotics follow from \(\sin u\sim u\) as \(u\to0\). At any root, one-block monodromy is rank at most one with trace zero, hence its square vanishes. Since its largest root tends to infinity, finite-time convergence occurs at arbitrarily large stepsizes as the run length varies.

Finally, for \(L=2\) the recurrence gives \(p_2=t^2-3t+1\). The two strict inequalities \(-1<p_2<1\) reduce to \((t-1)(t-2)>0\) and \(0<t<3\), whose intersection is \((0,1)\cup(2,3)\). Its largest zero is \((3+\sqrt5)/2\). This completes the proof.

## Verification

The accompanying `verify.py` executes exact symbolic checks of every cyclic binary delay word of length at most eight that contains a zero (502 words), comparing its monodromy trace to the product of the prescribed run polynomials and checking zero determinant. It checks path-polynomial recurrences and their trigonometric root evaluations for short runs and the exact nilpotence and reentrant threshold for the period-three word. These finite checks are consistency tests; the proof of all periods, all initial data, and arbitrary run lengths is the analytical rank-one and path-spectrum argument above.

Run `python verify.py` with Python 3 and SymPy installed. No external data, third-party packages beyond SymPy, or numerical tolerances are used in the proof.

## Relationship to prior work

Duman, Çelik Kızılkan, and Aydın (2016) give generic Schur-stability and sensitivity tools for linear periodic difference equations. Their monodromy criterion is used conceptually here, but does not itself list the binary-delay run-length multipliers, their path-spectrum roots, or the unbounded finite-time cancellation construction. Mitliagkas and collaborators (arXiv:1605.09774, first submitted 2016-05-31) model asynchronous gradient staleness and identify a momentum effect for random delays; the present exact deterministic periodic delay law addresses a different regime. McMahan and Streeter (NeurIPS 2014) analyze delayed online learning with adaptive learning rates and regret bounds, not a sharp deterministic Floquet classification. The classical constant-lag stability-switch literature concerns autonomous recurrences with a varying fixed integer lag, rather than a periodically switching zero/one lag. Classical path-adjacency eigenvalues and Floquet theory are premises, not claimed discoveries.

## Limitations

The stability windows can be extremely fragile around high-stepsize cancellation roots. The large-stepsize assertion allows the schedule length to grow with the stepsize, and finite termination requires exactly tuned arithmetic and curvature. It is not a recommendation to use oversized steps in noisy, variable-curvature or uncontrolled-asynchrony optimization. The all-one delay word is excluded from the product theorem and treated separately. Earlier literature on periodically varying difference equations may contain an equivalent specialized reduction not detected in the surveyed sources; no claim of exhaustive historical novelty or independent external validation is made.

## References

1. A. Duman, G. Çelik Kızılkan, K. Aydın, *Sensitivity of Schur stability of systems of linear difference equations with periodic coefficients*, New Trends in Mathematical Sciences 4(2), 159–173 (first publicly online 2016-04-18). DOI: 10.20852/ntmsci.2016217826. Full text: https://dergipark.org.tr/en/download/article-file/636264.
2. I. Mitliagkas, C. Zhang, S. Hadjis, C. Ré, *Asynchrony begets Momentum, with an Application to Deep Learning*, arXiv:1605.09774 (first submitted 2016-05-31). https://arxiv.org/abs/1605.09774.
3. H. B. McMahan, M. Streeter, *Delay-Tolerant Algorithms for Asynchronous Distributed Online Learning*, NeurIPS 27 (2014), 2915–2923. Full text: https://papers.nips.cc/paper_files/paper/2014/file/0f41d814a243c98c672bdbfabaa40f5e-Paper.pdf.
4. J. Čermák, J. Jánský, *Stability switches in linear delay difference equations*, Applied Mathematics and Computation (2014). Background only: autonomous constant-lag systems (publisher abstract https://www.sciencedirect.com/science/article/abs/pii/S0096300314009084).

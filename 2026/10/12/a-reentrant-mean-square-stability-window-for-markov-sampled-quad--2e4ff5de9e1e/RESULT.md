# A reentrant mean-square stability window for Markov-sampled quadratic descent

## Finding

Consider the two convex quadratic component functions \(f_1(x)=x^2/2\) and \(f_2(x)=3x^2\). Their average is the strongly convex function \(f(x)=7x^2/4\). A fixed-step stochastic gradient update samples the component index from a two-state Markov chain instead of independently:

\[
 x_{k+1}=x_k-\eta f_{I_k}'(x_k),\qquad
 P=\begin{pmatrix}p&1-p\\1-p&p\end{pmatrix},
 \qquad p\in[0,1],\quad \eta>0.
\]

The step is called *mean-square stable* if \(\mathbb E[x_k^2]\to0\) for **every** deterministic \(x_0\in\mathbb R\) and either deterministic initial component \(I_0\). No assumption of a stationary initial component is necessary. Here \(p\) is the probability of repeating the preceding component, so small \(p\) describes anti-persistent sampling.

Put

\[
C_p(z)=(72p-36)z^3+(84-168p)z^2+(85p-61)z+14(1-p),
\]
\[
G(p)=23675p^3-38914p^2+803p+36.
\]

Let \(p_*\) be the unique zero of \(G\) in \((0,1/2)\). Its numerical value is \(p_*=0.0431898824670018\ldots\). The **complete stability classification** is:

1. For \(0\le p<p_*\), \(C_p\) has three distinct positive roots \(r_1(p)<r_2(p)<r_3(p)\), and precisely the two disjoint intervals \((0,r_1(p))\) and \((r_2(p),r_3(p))\) are mean-square stable.
2. At \(p=p_*\), the two larger roots coincide at an unstable double-root boundary. Only \((0,r_1(p_*))\) is stable.
3. For \(p_*<p<1/2\), \(C_p\) has one real root, positive, and exactly the interval below it is stable.
4. For \(1/2\le p\le1\), stability again holds on precisely one open interval starting at zero. Its right endpoint is the unique positive solution of \(\rho(M)=1\), for \(M\) below. In particular it is \(14/37\) at \(p=1/2\) and \(1/3\) at \(p=1\).

At strict alternation \(p=0\), the exact stable set is

\[
 (0,1/2)\;\cup\;(2/3,7/6).
\]

This is **reentrant stability**: increasing the step can first destroy and then restore mean-square convergence. It persists for positive, but sufficiently small, Markov staying probability.

## Assumptions and scope

The component curvatures are exactly one and six; there is no additive gradient noise, no projection and no varying stepsize. The component chain is time-homogeneous and independent of the current iterate conditional on its preceding component. Both deterministic starting components and all scalar starting values are allowed. The result concerns the decay of expected squared error, not sample-path convergence rates, finite-time objective monotonicity, or high-dimensional systems. The range \(p=0\) is included although the component chain is periodic, and \(p=1\) is included although it is reducible.

The paper deliberately studies the simple first integer curvature contrast above the deterministic-alternation threshold \(3+2\sqrt2\), so that the topology of the admissible-stepsize set, rather than a generic spectral-radius bound, can be completely identified.

## Proof

**1. Exact second-moment transfer.** Let \(A=(1-\eta)^2\) and \(B=(1-6\eta)^2\). The conditional squared moments \(v_{k,i}=\mathbb E[x_k^2\mathbf1_{\{I_k=i\}}]\) satisfy \(v_{k+1}=P^{\mathsf T}\operatorname{diag}(A,B)v_k\). Its transfer matrix has the same spectrum as

\[
 M=\operatorname{diag}(A,B)P
 =\begin{pmatrix}pA&(1-p)A\\(1-p)B&pB\end{pmatrix}.
\]

The entries are nonnegative. Since the nonnegative transfer powers control the sum of the two conditional moments, decay for every deterministic scalar initial state and either initial component is equivalent to \(\rho(M)<1\). Necessity also holds at a zero multiplier: if the transfer powers decay for both basis vectors, the matrix powers decay, forcing all eigenvalues to have modulus strictly below one. The two eigenvalues are real, and the spectral radius is

\[
\rho(M)=\frac{p(A+B)+\sqrt{p^2(A-B)^2+4(1-p)^2AB}}{2}.
\]

**2. Determinant and cubic reduction.** Direct multiplication gives

\[
\det(I-M)=1-p(A+B)+(2p-1)AB=\eta C_p(\eta).
\]

When \(0\le p<1/2\), \(\det(I-M)>0\) implies \(p(A+B)<1\), hence \(\operatorname{tr}M<1\) and \(\rho(M)<1\). Conversely \(\rho(M)<1\) implies \(\det(I-M)>0\). Therefore in this parameter range, and only for strictly positive \(\eta\), stability is equivalent to \(C_p(\eta)>0\).

For \(p=0\), the cubic factors exactly:

\[
 C_0(z)=-36(z-1/2)(z-2/3)(z-7/6).
\]

Thus all three roots are positive and simple, and the intervals stated at alternation follow from the leading sign.

**3. The exact persistence threshold.** The discriminant of the cubic is

\[
\operatorname{Disc}_z C_p=-144(2p-1)G(p).
\]

On the closed interval \([0,1/2]\), \(G''(p)=142050p-77828<0\), while \(G(0)=36>0\) and \(G(1/2)=-50653/8<0\). Concavity makes the superlevel set of \(G\) an interval, so there is exactly one zero \(p_*\in(0,1/2)\). Exact rational evaluations show \(43/1000<p_*<44/1000\).

For \(0\le p<p_*\), the discriminant is positive, so there are three simple real roots. Their positivity follows by continuous dependence from the three positive roots at \(p=0\): no root can cross zero because \(C_p(0)=14(1-p)>0\), and no root can escape through infinity because its leading coefficient \(36(2p-1)\) remains nonzero. Hence the sign intervals are exactly those in the finding.

At \(p=p_*\), the discriminant is zero. A root of \(C_p\) always lies in \((1/10,1/2)\), because \(\rho(M)<1\) at \(\eta=1/10\) (both squared multipliers are below one) while

\[
 \det(I-M)\big|_{\eta=1/2}=-9p/4<0
\]

for \(p>0\). Consequently the two larger roots, not the smallest, coalesce at \(p_*\). At the coalesced root \(\rho(M)=1\), so it is excluded. For \(p_*<p<1/2\), the discriminant is negative, leaving one real root. Its positivity follows from \(C_p(0)>0\) and the negative leading coefficient; the cubic is positive exactly before that root.

**4. The remaining persistence range.** For \(p\ge1/2\), the symmetric Markov transition matrix \(P\) is positive semidefinite. The transfer has the same eigenvalues as

\[
 S(\eta)=P^{1/2}\operatorname{diag}((1-\eta)^2,(1-6\eta)^2)P^{1/2}.
\]

The matrix \(S\) is positive semidefinite and matrix-convex in \(\eta\), since its second derivative is \(2P^{1/2}\operatorname{diag}(1,36)P^{1/2}\succeq0\). Thus \(\lambda_{\max}(S(\eta))=\rho(M(\eta))\) is convex in \(\eta\). At zero it equals one; its right derivative is negative (equal to \(-7\) for \(p<1\), and \(-2\) at \(p=1\)); it diverges as \(\eta\to\infty\). Its strict sublevel set below one is therefore exactly one interval beginning at zero. Direct substitution gives the endpoints \(14/37\) for \(p=1/2\) and \(1/3\) for \(p=1\). All points where the spectral radius is one are excluded from mean-square convergence from every initial mode.

## Verification

The included `verify.py` checks the transfer determinant, the exact cubic, its discriminant, root factorization at zero persistence, the critical-root bracket, and two rational witness points. It also tests 520 rational pairs of persistence and stepsize against the exact trace-and-determinant spectral criterion; it prints `VERIFY_OK` when all checks pass. The general theorem rests on the preceding algebra and convexity arguments, not on a finite parameter scan.

For example, at \(p=1/50\) and \(\eta=3/5\), \(\det(I-M)=-5523/31250<0\), while at the *larger* step \(\eta=9/10\), \(\det(I-M)=53343/125000>0\). The full stable intervals for this \(p\) are numerically about \((0,0.4823497996)\) and \((0.7424615355,1.1085219983)\). These decimal root approximations are illustrations; all boundaries are defined exactly by the cubic.

## Relationship to prior work

The necessary-and-sufficient spectral-radius test for mean-square stability of Markov jump linear systems is classical. In particular, Gray, González and Patilkulkarni (2000) treat scalar jump-perturbed systems, and Ling and Deng (2012) provide a full real-state necessity proof for the general discrete-time case. Lee, Halder and Bhattacharya (2014) develop a further mean-square stability framework. None of these generic criteria is claimed as new here.

The specialized contribution is the *exact connectivity transition* of the admissible learning-rate set for the natural two-curvature Markov-sampled gradient iteration: explicit three-root reentrant intervals, an algebraic persistence threshold, the coalescing-root boundary, and the full connected regime. A relevant older scalar jump-system conference paper was available only as an abstract and bibliographic record, not complete text; this leaves a genuine risk of a previously observed equivalent specialized phenomenon.

## Limitations

This is a fixed two-component benchmark with curvature ratio six, not a characterization of arbitrary component counts, nonsymmetric transition matrices, or additive-noise stationary errors. General jump-linear-system results already entail computable matrix spectral criteria, so the contribution is not a new stability operator. No independent audit or external certification has been performed. The closed-form discriminator does not imply a new asymptotic rate-optimality theorem, and the disconnected stepsize windows are not advice to use large steps on arbitrary objectives.

## References

1. Q. Ling and H. Deng, “A New Proof to the Necessity of a Second Moment Stability Condition of Discrete-Time Markov Jump Linear Systems with Real States,” *Journal of Applied Mathematics* (2012), Article 642480, DOI: 10.1155/2012/642480 (first published 10 June 2012).
2. K. Lee, A. Halder and R. Bhattacharya, “Mean Square Stability for Stochastic Jump Linear Systems via Optimal Transport,” arXiv:1403.2471 (11 March 2014).
3. W. S. Gray, O. R. González and S. Patilkulkarni, “Stability of Digital Control Systems Subject to Jump Linear Random Perturbations,” *Proceedings of the IEEE Conference on Decision and Control* (2000), DOI: 10.1109/CDC.2000.912010 (bibliographic record and abstract inspected; complete text not accessible).
4. W. Hou and collaborators, “Spectral Perspective on the Stability of Discrete-Time Markov Jump Systems with Multiplicative Noise,” *Mathematical Problems in Engineering* (2014), DOI: 10.1155/2014/769302.

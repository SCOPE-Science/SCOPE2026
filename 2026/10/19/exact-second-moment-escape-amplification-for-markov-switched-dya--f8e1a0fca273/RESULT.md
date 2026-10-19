# Exact second-moment escape amplification for Markov-switched dyadic holes

## Finding
Let \(T(x)=2x\bmod 1\) on \([0,1)\), with Lebesgue initial probability. At each observation time select one of the two holes \(H_0=[0,1/4)\) and \(H_1=[3/4,1)\) using a stationary, symmetric two-state Markov environment with retention probability \(p\in[0,1]\), independent of the initial point. For an environmental realization \(E=(E_j)_{j\ge0}\), write \(Q_n(E)\) for the Lebesgue measure of points avoiding \(H_{E_j}\) at every time \(0\le j<n\), with \(Q_0=1\).

Put \(a_n=\mathbb E_E Q_n\) and \(b_n=\mathbb E_E Q_n^2\). For every \(n\ge0\) and \(p\in[0,1]\), both moments have *exact* transfer descriptions:
\[
 a_n=\begin{pmatrix}\tfrac12&\tfrac12\end{pmatrix}
 \begin{pmatrix}\tfrac12&\tfrac12\\[2pt]\tfrac p2&\tfrac{1-p}{2}\end{pmatrix}^{n}
 \binom11,
\qquad
 b_n=\begin{pmatrix}\tfrac14&\tfrac12&\tfrac14\end{pmatrix}
 \begin{pmatrix}
 \tfrac14&\tfrac12&\tfrac14\\[2pt]
 \tfrac p4&\tfrac14&\tfrac{1-p}{4}\\[2pt]
 \tfrac p4&0&\tfrac{1-p}{4}
 \end{pmatrix}^{n}
 \begin{pmatrix}1\\1\\1\end{pmatrix}.
\]
For \(0<p\le1\), let
\[
 \Delta_p=\sqrt{p(p+4)},\qquad
 q_\pm(p)=\frac{2-p\pm\Delta_p}{4},\qquad
 C_\pm(p)=\frac{\Delta_p\pm(1+p)}{2\Delta_p}.
\]
Then \(a_n=C_+(p)q_+(p)^n+C_-(p)q_-(p)^n\) for every \(n\ge0\); at \(p=0\), this continuous-in-\(p\) formula has the Jordan-block limit
\[
 a_n=\frac{n+2}{2^{n+1}}.
\]
The escape factor \(q_+(p)\) increases strictly from \(1/2\) at \(p=0\) to \((1+\sqrt5)/4\) at \(p=1\); at \(p=1/2\) the annealed law is exactly \(a_n=(3/4)^n\).

The principal second-moment result is **strict exponential amplification of relative environmental fluctuations at every interior retention probability**. Let \(\Lambda_p\) be the Perron eigenvalue of the displayed three-by-three second-moment matrix. It is the largest positive real root of
\[
 P_p(t)=64t^3+(16p-48)t^2+(12-20p)t+2p-1.
\]
For every \(0<p<1\), one has
\[
 \boxed{\Lambda_p>q_+(p)^2},
 \qquad
 \boxed{\lim_{n\to\infty}
 \left(\frac{\mathbb E_E[Q_n(E)^2]}{(\mathbb E_E Q_n(E))^2}\right)^{1/n}
 =\frac{\Lambda_p}{q_+(p)^2}>1}.
\]
More precisely there exists \(D_p>0\) such that \(b_n/a_n^2\sim D_p(\Lambda_p/q_+(p)^2)^n\); hence the same exponential rate holds for \(\operatorname{Var}_E(Q_n)/a_n^2\). At the two deterministic environmental endpoints \(p=0\) and \(p=1\), however, \(\operatorname{Var}_E(Q_n)=0\) identically for every \(n\).

## Assumptions and scope
Binary expansion turns \(T\) into the left shift of independent fair bits, modulo a null set of dyadic points. The environmental chain is initialized at its symmetric stationary law, so \(\Pr(E_0=0)=\Pr(E_0=1)=1/2\), and makes the same-state transition with probability \(p\) and the opposite-state transition with probability \(1-p\). The environment is shared across all starting points in the definition of \(Q_n(E)\); the second moment is *not* the survival probability of a single trajectory with an independently resampled environment. Observations occur at integer times \(0,\ldots,n-1\). All intervals are half-open to make the binary coding unambiguous away from a null set.

## Proof
**1. First moment.** Write the binary digits of a uniform initial point as independent fair bits \(B_0,B_1,\ldots\). The event \(T^j x\in H_{E_j}\) is exactly \(B_j=B_{j+1}=E_j\). Track the indicator \(m_j=\mathbf1_{\{B_j=E_j\}}\) on surviving paths. Given \(m_j=0\), no restriction is placed on \(B_{j+1}\), so the new match indicator has two equiprobable outcomes. Given \(m_j=1\), survival forces \(B_{j+1}=1-E_j\) (probability \(1/2\)); it then matches the next environment precisely if the environment flips (probability \(1-p\)). This yields the first matrix above, acting from the right on the row distribution \((1/2,1/2)\). Summation over final match states gives \(a_n\) exactly.

The first-moment matrix has characteristic equation
\[
 4t^2-(4-2p)t+(1-2p)=0.
\]
For \(p>0\) its eigenvalues are \(q_\pm\), and solving the two initial conditions \(a_0=1\), \(a_1=3/4\) gives \(C_\pm\). For \(p=0\), the matrix is a size-two Jordan block at eigenvalue \(1/2\), giving the exact displayed \((n+2)/2^{n+1}\) expression. For \(p=1/2\) its row sums are \(3/4\). The derivative \(q_+'(p)=(-1+(p+2)/\sqrt{p(p+4)})/4\) is strictly positive for \(p>0\), since \((p+2)^2-p(p+4)=4\). For \(p=1\) the leading root is \((1+\sqrt5)/4\). Since \(|q_-(p)|<q_+(p)\) for \(0<p\le1\), \(a_n\sim C_+(p)q_+(p)^n\) there.

**2. Shared-environment second moment.** Draw two independent initial points with fair bit streams, but subject both to the same chain \(E\). Conditional on \(E\), their survival events are independent, so the probability both survive after averaging over \(E\) is exactly \(b_n\). Track \(k_j\in\{0,1,2\}\), the number of their current bits matching \(E_j\), starting with binomial probabilities \((1/4,1/2,1/4)\). If \(k_j=0\), the next pair of fair bits yields \((1/4,1/2,1/4)\). If \(k_j=1\), survival requires one specified next bit (weight \(1/2\)); accounting for persistence and the other fair bit gives \((p/4,1/4,(1-p)/4)\). If \(k_j=2\), both next bits are prescribed (weight \(1/4\)); persistence yields \(k_{j+1}=0\) and switching yields \(k_{j+1}=2\), giving \((p/4,0,(1-p)/4)\). These are exactly the three rows of the second matrix, proving its all-horizon formula. Direct determinant expansion gives \(P_p(t)\) above.

**3. Strict Perron gap.** Fix \(0<p<1\) and write \(q=q_+(p)\). The second-moment matrix is primitive: its first row is strictly positive, every state reaches the first state, and the first state reaches every state. Hence its Perron eigenvalue \(\Lambda_p>0\) is algebraically simple, and \(b_n=\beta_p\Lambda_p^n(1+o(1))\) for some \(\beta_p>0\). Using the characteristic relation \(4q^2-(4-2p)q+1-2p=0\), direct polynomial reduction yields the *exact identity*
\[
 P_p(q^2)=4p(p-1)q(q-1)(4q^2-3).
\]
Here \(1/2<q<(1+\sqrt5)/4<\sqrt3/2\), so all three factors \(p(p-1)\), \(q(q-1)\), and \(4q^2-3\) are strictly negative. Consequently \(P_p(q^2)<0\). Since \(P_p(t)\to+\infty\) as \(t\to+\infty\), it has a positive real root greater than \(q^2\). The Perron eigenvalue dominates the modulus of every eigenvalue, so \(\Lambda_p>q^2\). Combining \(b_n\sim\beta_p\Lambda_p^n\) with \(a_n\sim C_+(p)q^n\) yields the claimed exponential relative second moment with \(D_p=\beta_p/C_+(p)^2>0\). Subtracting one gives the same rate for relative variance.

**4. Deterministic environmental endpoints.** At \(p=1\), the chain is either constantly zero or constantly one; at \(p=0\), it alternates with either of two possible phases. Under the bitwise-complement map \(B_j\mapsto1-B_j\), the two environmental realizations in each case have identical surviving Lebesgue mass. Thus \(Q_n(E)\) is deterministic as a function of the allowed random environment, giving zero variance for every horizon. No continuity of the positive interior exponential gap to either endpoint is asserted.

## Verification
The accompanying standalone \(\texttt{verify.py}\) uses only Python's standard library. It independently enumerates all environmental words and binary starting cylinders of length \(n+1\) for every \(1\le n\le7\) and all seven rational persistence values \(p\in\{0,1/10,1/4,1/2,3/4,9/10,1\}\). All \(49\) independently counted first- and second-moment pairs agree exactly with the two matrix formulas. It also checks the endpoint formulas and the fair-switching law, and tests the factorization and strict sign numerically at \(999\) interior parameter values. The analytic identities, Perron theorem, and infinite asymptotic statements are proved above rather than inferred from these finite tests.

## Relationship to prior work
Bahsoun, Schmeling, and Vaienti study random holes for expanding interval maps; their principal stochastic model uses independent hole radii centered at a fixed point, and their discrete examples also select holes independently, rather than with Markov persistence. Their work develops annealed transfer-operator escape theory but does not evaluate a shared-environment second moment for this two-hole Markov protocol. Livorati, Georgiou, Dettmann, and Leonel study periodically moving holes in the doubling map; a prescribed periodic oscillation does not imply the stochastic finite-state moment matrix or its strict Perron gap. Bódai, Altmann, and Endler distinguish shared random perturbations from independently noisy trajectories and investigate statistical dispersion, but do not state the present exact second-moment law for two Markov-selected dyadic holes. The already-understood independent fair-selection first-moment baseline \(a_n=(3/4)^n\) is expressly retained as the specialization \(p=1/2\), not presented as a new discovery. The new quantitative assertion is the joint exact all-parameter second-moment law and its universal strict relative-variance growth for \(0<p<1\).

## Limitations
The claim concerns only this symmetric stationary environment and the two specified length-two binary-cylinder holes. It does not identify an almost-sure (quenched) escape exponent, a distributional limit for a normalized survival mass, asymmetric environmental chains, or general moving-hole families. The known two-track transfer method could be applied to other finite-state random open systems, but the resulting strict Perron inequality is not asserted outside the stated family. Historical priority beyond the inspected sources is not independently certified.

## References
- W. Bahsoun, J. Schmeling, S. Vaienti, *On Transfer Operators and Maps with Random Holes*, arXiv:1405.0361 (first public version 2014-05-02), https://arxiv.org/abs/1405.0361 .
- A. L. Livorati, O. Georgiou, C. P. Dettmann, E. D. Leonel, *Escape through a time-dependent hole in the doubling map*, arXiv:1312.7030 (first public version 2013-12-25), https://arxiv.org/abs/1312.7030 .
- T. Bódai, E. G. Altmann, A. Endler, *Stochastic perturbations in open chaotic systems: random versus noisy maps*, arXiv:1211.0698 (first public version 2012-11-04), https://arxiv.org/abs/1211.0698 .

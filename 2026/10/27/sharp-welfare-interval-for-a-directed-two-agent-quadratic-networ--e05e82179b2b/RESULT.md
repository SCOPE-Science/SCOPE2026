# Sharp welfare interval for a directed two-agent quadratic network game

## Finding

Consider a one-way positive-spillover network of two agents with different, arbitrary positive quadratic effort-cost coefficients. The price of anarchy has an **exact attainable interval** over all nonnegative nonzero vectors of direct incentives. Although its strategic-response matrix has spectral radius zero, its worst-case and even its best-case inefficiency diverge as the weighted directed spillover approaches the strict welfare-concavity boundary.

**Theorem.** Let \(\gamma_1,\gamma_2,g>0\) satisfy \(g^2<\gamma_1\gamma_2\), and write \(t=g/\sqrt{\gamma_1\gamma_2}\). For \(b_1,b_2\ge0\), not both zero, each player selects a nonnegative effort to maximize
\[
 u_1(x_1,x_2)=b_1x_1-\frac{\gamma_1}{2}x_1^2+g x_1x_2,
 \qquad
 u_2(x_1,x_2)=b_2x_2-\frac{\gamma_2}{2}x_2^2.
\]
Let \(W=u_1+u_2\); write \(x^{\mathrm{NE}}\) for the unique Nash equilibrium and \(x^{\mathrm{opt}}\) for the unique maximum of \(W\) over the nonnegative quadrant. Then their welfare ratio is well defined and strictly greater than one, and
\[
 \boxed{\frac{1}{1-t^4}\le
 \frac{W(x^{\mathrm{opt}})}{W(x^{\mathrm{NE}})}
 \le\frac{1}{1-t^2}.}
\]
The lower equality holds precisely when \(b_1=0<b_2\); the upper equality precisely when \(b_2=0<b_1\). All values of this closed interval occur as the nonzero nonnegative incentive vector varies. If both incentives are required to be strictly positive, the attainable set is exactly the **open** interval with the same two sharp infimum and supremum, neither attained. In particular, both bounds diverge as \(t\uparrow1\), while the best-response matrix has two zero eigenvalues for **every** \(t\):
\[
 M=\begin{pmatrix}0&g/\gamma_1\\0&0\end{pmatrix},
 \qquad M^2=0,\qquad \rho(M)=0.
\]
If \(g^2\ge\gamma_1\gamma_2\) and incentives are nonnegative and nonzero, social welfare is unbounded above on the nonnegative quadrant; hence the strict concavity restriction is sharp for the finite-planner comparison. Two agents are minimal for this directed-edge phenomenon: with one agent, Nash effort is socially optimal.

## Assumptions and scope

The strategies are deterministic, simultaneous, continuous and unbounded above, constrained only by \(x_i\ge0\). The sole directed link enters player 1's private payoff; player 2 is unaffected by player 1's effort. Both private quadratic costs are strictly positive and need not agree. The two direct incentive coefficients are individually nonnegative with at least one positive. The price of anarchy here is the optimum-to-equilibrium **welfare** ratio for this unique-equilibrium game, not a cost ratio and not an expectation. When we refer to its attainable interval, the cost and edge parameters are held fixed and the direct incentives vary. The parameter \(t\) is dimensionless and lies strictly between zero and one.

## Proof

**Normalization.** Set \(v_i=\sqrt{\gamma_i}\,x_i\) and \(y_i=b_i/\sqrt{\gamma_i}\). Because these substitutions are bijections of the nonnegative quadrant, they preserve equilibria, feasible optima, and their welfare ratio. The normalized payoff functions become
\[
 u_1=y_1v_1-\frac12v_1^2+t v_1v_2,
 \qquad
 u_2=y_2v_2-\frac12v_2^2,
\]
with \(0<t<1\), \(y_1,y_2\ge0\) and \(y_1+y_2>0\).

**Nash equilibrium.** Player 2's unique best response is \(v_2=y_2\), independent of the other action. Player 1's unique best response is \(v_1=y_1+t v_2\). These are automatically nonnegative and give the only Nash equilibrium:
\[
 v^{\mathrm{NE}}=(y_1+t y_2,y_2).
\]
At a best response each player's private payoff equals one-half the square of their own normalized effort. Thus, with \(D=(y_1+t y_2)^2+y_2^2>0\),
\[
 W(v^{\mathrm{NE}})=\frac D2.
\]

**Planner optimum.** The aggregate welfare is
\[
 W(v)=y_1v_1+y_2v_2-\frac12(v_1^2+v_2^2)+t v_1v_2
      =y^{\mathsf T}v-\frac12v^{\mathsf T}Hv,
 \qquad
 H=\begin{pmatrix}1&-t\\-t&1\end{pmatrix}.
\]
The eigenvalues of \(H\) are \(1-t\) and \(1+t\), both positive. Therefore \(W\) is strictly concave and coercive. The unconstrained maximizer \(H^{-1}y\) lies in the nonnegative quadrant, since every entry of
\[
 H^{-1}=\frac{1}{1-t^2}\begin{pmatrix}1&t\\t&1\end{pmatrix}
\]
is nonnegative. Hence it is also the unique constrained maximizer, with
\[
 v^{\mathrm{opt}}=\frac1{1-t^2}(y_1+t y_2,t y_1+y_2),
 \quad W(v^{\mathrm{opt}})=\frac{y_1^2+2t y_1y_2+y_2^2}{2(1-t^2)}.
\]

**Exact ratio and sharp endpoints.** The identity
\[
 y_1^2+2t y_1y_2+y_2^2=D-t^2 y_2^2
\]
yields
\[
 \operatorname{PoA}=
 \frac{y_1^2+2t y_1y_2+y_2^2}{(1-t^2)D}
 =\frac1{1-t^2}-\frac{t^2y_2^2}{(1-t^2)D}.
\]
The differences from the proposed bounds factor exactly:
\[
 \operatorname{PoA}-\frac{1}{1-t^4}
  =\frac{t^2y_1(y_1+2ty_2)}{(1-t^4)D}\ge0,
 \qquad
 \frac1{1-t^2}-\operatorname{PoA}
  =\frac{t^2 y_2^2}{(1-t^2)D}\ge0.
\]
For \(t>0\), the first difference vanishes if and only if \(y_1=0\); the second vanishes if and only if \(y_2=0\). These equivalences also give the precise equality cases in the original incentives. Both bounds exceed one, since \(0<t<1\), and the ratio is positive and finite. Its restriction to the compact path \((y_1,y_2)=(s,1-s)\) with \(0\le s\le1\) is continuous, takes the lower and upper endpoints, and stays inside their interval. The intermediate value theorem therefore proves that the entire interval, with no gaps, is attained.

**Zero spectrum and blowup.** The unnormalized best responses are
\[
 x_2=\frac{b_2}{\gamma_2},\qquad
 x_1=\frac{b_1}{\gamma_1}+\frac{g}{\gamma_1}x_2.
\]
The off-diagonal response matrix \(M\) displayed in the theorem squares to zero, even as \(g/\sqrt{\gamma_1\gamma_2}=t\uparrow1\). Thus \(\rho(M)=0\) while the minimum price of anarchy across all nonzero nonnegative direct incentives equals \(1/(1-t^4)\to\infty\). In particular, no finite upper bound depending **only** on \(\rho(M)\) can hold for this directed one-link class.

**Sharp planner boundary and minimality.** At \(t=1\), along \(v_1=v_2=s\) the quadratic term of \(W\) vanishes and \(W=s(y_1+y_2)\to\infty\). At \(t>1\), the same ray yields \(W=s(y_1+y_2)+(t-1)s^2\to\infty\). Finally, a one-agent game has \(W=u_1\); its unique privately optimal effort necessarily maximizes welfare, so its price of anarchy equals one.

## Verification

The included `verify.py` uses only the Python standard library and exact rational arithmetic. Execute `python verify.py` from the directory containing this file; success prints `VERIFY_OK 945 exact rational parameter configurations`. In each configuration the script constructs the equilibrium and planner solution directly in unnormalized coordinates; checks best-response and planner first-order conditions, nonnegativity and positive welfare; evaluates the raw payoff-based welfare ratio; checks both closed-form factorization identities, sharp inequalities, and equality cases; and tests a concrete heterogeneous-cost example and several diverging lower bounds at zero spectral radius. Rational tests do not, by themselves, establish the theorem's universal quantifiers; those follow from the preceding algebraic proof.

For instance \(\gamma_1=4\), \(\gamma_2=9\), \(g=18/5\), \(b_1=2\), \(b_2=3\) give \(t=3/5\) and
\[
 W(v^{\mathrm{NE}})=\frac{89}{50},\quad
 W(v^{\mathrm{opt}})=\frac52,\quad
 \operatorname{PoA}=\frac{125}{89},\quad
 \frac{625}{544}<\frac{125}{89}<\frac{25}{16}.
\]

## Relationship to prior work

Golub's *Eigenvalues in microeconomics* (first public version 17 February 2025; revised as *Spectral Methods in Microeconomics*) derives a spectral-radius formula for price of anarchy when agents have homogeneous quadratic costs and a symmetric interaction matrix, and explicitly motivates relaxing both assumptions in its “Toward Open Questions” paragraph. The present theorem gives an exact solution on the smallest **directed**, heterogeneous-cost network; the graph's response spectrum remains identically zero despite arbitrarily large welfare inefficiency. It is not an alternative proof of Golub's symmetric result, because the admissible matrix here is strictly asymmetric.

Iwanaga and Kobayashi (2026), *Welfare bounds for linear-quadratic network games*, compute welfare bounds for an **undirected binary symmetric** adjacency matrix and uniform own-quadratic coefficients. Their spectral reduction does not imply the directed one-way sharp interval. Rokade, Jain, Parise, Krishnamurthy and Tardos (2025), *Asymmetric Network Games: α-Potential Function and Learning*, treat welfare suboptimality of particular approximate Nash equilibria obtained from an α-potential construction under different action and parameter restrictions; their welfare statement does not specialize to the exact equilibrium's complete incentive-dependent interval above. Chen, Chen and Lu (2016) demonstrate directed-graph inefficiency in **opinion formation** objectives, not this productive-spillover quadratic effort game. These distinctions concern hypotheses and logical implications, not just titles or terminology.

## Limitations

The result concerns exactly two agents, one unreciprocated positive cross-payoff term, additive utilitarian welfare, nonnegative direct incentives, and unconstrained-above nonnegative continuous actions. It does not claim universal bounds for larger directed networks, negatively signed interactions, bounded strategy sets, or other welfare conventions. The proof is self-contained; historical novelty remains subject to independent bibliographic assessment, especially possible implications from general asymmetric quadratic-game welfare literature. The computation supplies finite reproducibility checks and is not an independent scientific audit.

## References

1. B. Golub, *Eigenvalues in microeconomics*, arXiv:2502.12309v1 (first publicly posted 2025-02-17), revised as *Spectral Methods in Microeconomics* (2026), especially “The Welfare Theory of Network Games” and “Toward Open Questions”. https://arxiv.org/abs/2502.12309 and https://arxiv.org/pdf/2502.12309
2. Y. Iwanaga and T. Kobayashi, *Welfare bounds for linear-quadratic network games*, *Economics Letters* **260** (2026), 112824, Sections 2–3. https://doi.org/10.1016/j.econlet.2026.112824 ; openly accessible text: https://da.lib.kobe-u.ac.jp/da/kernel/0100499600/0100499600.pdf
3. K. Rokade, A. Jain, F. Parise, V. Krishnamurthy and E. Tardos, *Asymmetric Network Games: α-Potential Function and Learning*, arXiv:2508.06619 (2025), Section 3.3 and relevant appendix. https://arxiv.org/html/2508.06619
4. P.-A. Chen, Y.-L. Chen and C.-J. Lu, *Bounds on the Price of Anarchy for a More General Class of Directed Graphs in Opinion Formation Games* (2016), available via https://arxiv.org/abs/1602.02527

# A sharp self-appraisal threshold for perpetual weighted-median switching on a three-agent path

## Finding
For synchronous weighted-median opinion updates on the three-agent path, a sharp switching threshold occurs at \(s=2/3\). With the neighbor-influence matrix
\[
W=\begin{pmatrix}0&1/2&1/2\\1&0&0\\1&0&0\end{pmatrix},
\]
and common adjustment parameter \(0<s<1\), every trajectory reaches consensus. Yet the identity of the hub's selected weighted median eventually becomes constant for **every** initial opinion vector when \(0<s\le 2/3\), whereas **for every** \(2/3<s<1\), a nonempty open set of initial vectors has strict alternation between the two leaves at every time forever, while still converging to consensus.

More precisely, label the hub opinion \(x_t\) and the leaf opinions \(a_t<b_t\); put \(m_t=(a_t+b_t)/2\), \(d_t=(b_t-a_t)/2\), and \(z_t=(x_t-m_t)/d_t\). When \(s>2/3\), every initial condition satisfying
\[
|z_0|>\frac{s}{3s-2}
\]
remains strictly outside the leaf-opinion interval and switches the selected leaf at every step. For these trajectories the exact consensus value is
\[
c_\infty=\frac{x_0+m_0}{2}+\frac{s\,\operatorname{sgn}(x_0-m_0)d_0}{2(2-s)}.
\]
In particular, \(s=3/4\), \((a_0,b_0,x_0)=(2/5,3/5,9/10)\) produces perpetual alternating median choices and consensus \(c_\infty=73/100\).

## Assumptions and scope
The graph is a three-vertex undirected path, with equal influence weight \(1/2\) from each leaf to the hub and full influence from the hub to each leaf. Opinions are real numbers in \([0,1]\); initially \(a_0<b_0\) and \(x_0\in[0,1]\). All nodes update simultaneously as in Mohr–Hjorth–Porter:
\[
x_{t+1}=(1-s)x_t+sM_t,\quad
 a_{t+1}=(1-s)a_t+sx_t,\quad
 b_{t+1}=(1-s)b_t+sx_t.
\]
Crucially, the weighted-median selection convention is the projection onto the **entire weighted-median interval**: \(M_t=\min\{b_t,\max\{a_t,x_t\}\}\). Thus when the hub lies between its leaves, its own opinion is a valid weighted median and is selected; the rule does **not** always choose the nearer endpoint. A change of median branch means a change among the lower-leaf, interior, and upper-leaf branches. If the leaves initially coincide, all statements about the normalized gap are inapplicable; the hub and leaves then converge under a linear two-state update.

## Proof
First \(b_{t+1}-a_{t+1}=(1-s)(b_t-a_t)\), so \(d_t=(1-s)^td_0>0\). Moreover
\[
m_{t+1}=m_t+s(x_t-m_t),\qquad
x_{t+1}-m_{t+1}=(1-2s)(x_t-m_t)+s(M_t-m_t).
\]
The median projection belongs to \([a_t,b_t]\), hence \(|M_t-m_t|\le d_t\). As \(|1-2s|<1\), summing the resulting geometric-convolution bound proves \(\sum_{t\ge0}|x_t-m_t|<\infty\). It follows that \(m_t\) converges, \(x_t-m_t\to0\), and \(d_t\to0\); all three opinions converge to one consensus value.

If \(|z_t|\le1\), then \(M_t=x_t\) and \(x_{t+1}=x_t\). Both leaves move toward this unchanged hub value, so \(|z_{t+1}|=|z_t|\le1\) and the interior branch is permanently selected. If \(|z_t|>1\), write \(\sigma_t=\operatorname{sgn}(z_t)\). The projection is \(M_t=m_t+\sigma_td_t\), and consequently
\[
z_{t+1}=\frac{(1-2s)z_t+s\sigma_t}{1-s}.
\]
For \(0<s<1/2\), the right side preserves the sign and remains strictly beyond \(\pm1\); indeed for \(z_t>1\) it equals \(1+\frac{1-2s}{1-s}(z_t-1)>1\). At \(s=1/2\), the next state is exactly \(z_{t+1}=\sigma_t\), entering the interior branch. Thus no repeated median-branch changes are possible for \(s\le1/2\).

Now assume \(s>1/2\), and define
\[
\lambda=\frac{2s-1}{1-s}>0,\qquad B=\frac{s}{1-s},\qquad B-\lambda=1.
\]
Outside the leaf interval the map is \(z_{t+1}=-\lambda z_t+B\operatorname{sgn}(z_t)\). If \(z_t>1\), then \(z_{t+1}=1-\lambda(z_t-1)<1\); symmetrically if \(z_t<-1\), then \(z_{t+1}>-1\). Therefore every step from outside either enters the invariant interior interval or jumps strictly outside on the *opposite* side. During the latter event the outer distance \(R_t=|z_t|\) satisfies \(R_{t+1}=\lambda R_t-B\).

For \(1/2<s\le2/3\), \(\lambda\le1\). On every outer-side switch, \(R_{t+1}\le R_t-B\), so there can only be finitely many such switches before the invariant interior interval is reached. This proves eventual stabilization for all initial vectors at and below the threshold, including exact boundary and tie cases.

For \(2/3<s<1\), \(\lambda>1\) and \(B/(\lambda-1)=s/(3s-2)>1\). If \(R_0>B/(\lambda-1)\), then \(R_{t+1}=\lambda R_t-B>R_t>1\), and the sign reverses strictly at each iteration. Induction yields permanent alternation, and the strict inequality defines a nonempty open set of admissible initial vectors.

Finally, in this region \(\sigma_t=(-1)^t\sigma_0\). Adding the hub and leaf-mean updates gives \(x_{t+1}+m_{t+1}=x_t+m_t+s\sigma_td_t\). As \(d_t=(1-s)^t d_0\), the absolutely convergent geometric sum equals \(s\sigma_0d_0/(2-s)\). Since \(x_t,m_t\to c_\infty\), division by two proves the stated consensus formula.

## Verification
The rational witness has \(m_0=1/2\), \(d_0=1/10\), \(z_0=4\), while its outer-switching threshold is \(3\). The initial normalized displacements are \(4,-5,7,-11,19,-35,\ldots\), and the consensus formula gives \(73/100\). The accompanying exact-rational Python checker reproduces the projection update, these displacements, the strict alternating signs, and the exact limiting value. These finite checks are illustrative; the arbitrary-time and all-parameter assertions are proved algebraically above, not inferred from simulations.

## Relationship to prior work
Mohr, Hjorth, and Porter introduced the synchronous self-appraised weighted-median model and its precise interval-projection convention (arXiv:2406.17552, first submitted 25 June 2024); their principal analyses concern simulated final distributions and mean-field approximations. Mei and collaborators analyze asynchronous weighted-median dynamics (arXiv:2212.08808), and Han and collaborators analyze continuous-time median dynamics (arXiv:2404.16318), neither of which gives this synchronous branch-switch threshold. Zhang and collaborators include predispositions (arXiv:2408.01899). Cheng and Mei's later mixed discrete-time framework (arXiv:2610.16406) proves general convergence and consensus criteria; this is compatible with the present construction but does not imply eventual stabilization of the selected median or the sharp \(2/3\) boundary. The present claim concerns *which median branch is selected*, not merely whether opinions converge.

## Limitations
The exact threshold pertains to the specified symmetric three-node path and common adjustment coefficient. It is not a universal threshold on general graphs or with unequal leaf weights, prejudices, or asynchronous updates. For \(s>2/3\), the proof establishes a nonempty open alternating region, not a complete classification of all initial states. The limiting consensus formula applies only to the stated alternating region. The source literature comparison does not constitute a proof of worldwide uniqueness, and independently validating literature overlap remains useful.

## References
1. L. Mohr, P. G. Hjorth and M. A. Porter, *A Weighted-Median Model of Opinion Dynamics on Networks* (original title), arXiv:2406.17552, first submitted 2024-06-25; later titled *Long-Time and Short-Time Dynamics in a Weighted-Median Opinion Model on Networks*. https://arxiv.org/abs/2406.17552
2. W. Mei et al., *Convergence, Consensus and Dissensus in the Weighted-Median Opinion Dynamics*, arXiv:2212.08808. https://arxiv.org/abs/2212.08808
3. Y. Han et al., *The Continuous-Time Weighted-Median Opinion Dynamics*, arXiv:2404.16318. https://arxiv.org/abs/2404.16318
4. X. Zhang et al., *Convergence Analysis of Weighted-Median Opinion Dynamics with Prejudice*, arXiv:2408.01899. https://arxiv.org/abs/2408.01899
5. J. Cheng and W. Mei, *Equilibria and consensus in discrete-time opinion dynamics with mixed weighted-averaging and weighted-median mechanisms*, arXiv:2610.16406. https://arxiv.org/abs/2610.16406

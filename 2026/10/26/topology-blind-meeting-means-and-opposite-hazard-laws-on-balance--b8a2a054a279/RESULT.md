# Topology-blind meeting means and opposite hazard laws on balanced multipartite networks

## Finding
Let \(G=K_{m,\ldots,m}\) be the complete balanced \(r\)-partite graph, with \(r\ge2\), \(m\ge1\), \(N=rm\ge3\), and common degree \(d=N-m\). Two independent continuous-time simple random walkers, each jumping at total rate one, are removed when they first meet. Write \(T\) for that first-meeting time. For distinct starting vertices, type S means in the *same* part (requiring \(m\ge2\)), and type D means in *different* parts.

For every \(s\ge0\), the **complete conditional meeting-time transforms** are
\[
\mathbb E[e^{-sT}\mid S]=\frac4{d s^2+2Ns+4},\qquad
\mathbb E[e^{-sT}\mid D]=\frac{2(s+2)}{d s^2+2Ns+4}.
\]
They imply the exact conditional first and second central moments
\[
\begin{array}{c|cc}
&\mathbb E[T]&\operatorname{Var}(T)\\\hline
S&N/2&(N^2-2d)/4\\
D&(N-1)/2&(N^2-2d-1)/4.
\end{array}
\]
At fixed \(N\), the *means are partition-independent*, but each variance increases by \(1/2\) for each unit increase in the part size \(m\). Thus distinct topologies have identical means while retaining different collision fluctuations and laws.

Write
\[
\lambda_\pm=\frac{N\pm\sqrt{N^2-4d}}d,\qquad 0<\lambda_-<\lambda_+.
\]
The S distribution is the sum of independent exponentials of rates \(\lambda_-\) and \(\lambda_+\), so its hazard is strictly increasing from zero to \(\lambda_-\). For \(m>1\), the D distribution is a mixture of exponentials with those two rates and respective weights
\[
 w_- = \frac{\lambda_+-2/d}{\lambda_+-\lambda_-},\qquad
 w_+ = \frac{2/d-\lambda_-}{\lambda_+-\lambda_-};
\]
both weights are strictly positive, so its hazard is strictly decreasing to \(\lambda_-\). When \(m=1\), the graph is complete and D is exactly exponential of rate \(2/(N-1)\), with constant hazard.

## Assumptions and scope
All graphs are simple, finite, undirected and unweighted. Each walker runs an independent exponential clock of rate one and, at each clock ring, chooses uniformly among the \(d\) adjacent vertices. In particular, the per-edge jump rate is \(1/d\); replacing it by rate one per edge changes the time scales. The two walkers are distinguishable for the derivation, but collision time does not depend on labels. The initial vertices are distinct, and no further conditioning is imposed. One may equivalently coalesce the walkers at their first meeting.

## Proof
Classify nonabsorbed configurations as S if the two walkers occupy distinct vertices of one part, and D if they occupy different parts. Given S, either walker moves into a different part, making an S-to-D transition at total rate \(2\), and an immediate meeting is impossible. Given D, either walker jumps directly to the other at rate \(1/d\), yielding absorption at total rate \(2/d\). Each walker also has \(m-1\) choices in the other walker's part without landing on it, giving a D-to-S rate \(2(m-1)/d\). The remaining moves are D-to-D and are irrelevant to the reduced generator. Thus the transient, lumped generator in order (S,D) is
\[
 Q=\begin{pmatrix}-2&2\\2(m-1)/d&-2m/d\end{pmatrix},
 \qquad q_{\mathrm{abs}}=\begin{pmatrix}0\\2/d\end{pmatrix}.
\]
The absorbing chain is finite and absorption occurs almost surely: every transient state has a path to absorption, and the underlying graph is connected. For \(\phi_X(s)=\mathbb E[e^{-sT}\mid X]\), first-step conditioning gives
\[
(s+2)\phi_S=2\phi_D,\qquad
(s+2m/d)\phi_D=\frac2d+\frac{2(m-1)}d\phi_S.
\]
Eliminating \(\phi_S\), using \(m+d=N\), yields exactly the stated rational transforms. These transforms are valid even when S does not occur, because D remains well defined at \(m=1\).

Differentiating each transform once and twice at \(s=0\) gives all four moment expressions. Since \(d=N-m\), at fixed order the variance rises affinely with \(m\), whereas the means contain only \(N\). The polynomial factors as \(d(s+\lambda_-)(s+\lambda_+)\). Its discriminant equals \(N^2-4d=(N-2)^2+4(m-1)>0\) because \(N\ge3\), so the positive rates are distinct. The S transform is \(\lambda_-\lambda_+/((s+\lambda_-)(s+\lambda_+))\), establishing its two-stage convolution law. A convolution of two distinct exponentials has strictly increasing hazard: its survival is proportional to \(\lambda_+e^{-\lambda_-t}-\lambda_-e^{-\lambda_+t}\) and direct differentiation of the logarithmic derivative gives a positive hazard derivative for all \(t>0\).

Partial fractions turn the D transform into a mixture of exponential transforms with the stated weights. For \(m>1\), evaluating the denominator's monic factor at \(2/d\) gives \(4(1-m)/d^2<0\). Hence \(\lambda_-<2/d<\lambda_+\), proving both weights are positive. Its survival is \(w_-e^{-\lambda_-t}+w_+e^{-\lambda_+t}\). Differentiating its hazard gives \(-w_-w_+(\lambda_+-\lambda_-)^2e^{-(\lambda_-+\lambda_+)t}/(w_-e^{-\lambda_-t}+w_+e^{-\lambda_+t})^2<0\). For \(m=1\), \(\lambda_-=2/(N-1)\), \(\lambda_+=2\), and \(w_+=0\), proving the claimed exponential boundary. All claims follow.

## Verification
A separate pure-Python program, `meeting_checker.py`, constructs the full killed generator on *ordered distinct vertex pairs*, without using the two-state reduction. Gaussian elimination with exact rational arithmetic solves the first- and second-moment equations and three Laplace-resolvent equations. For eight graph families and every ordered initial pair it verifies 1,190 exact identities. Run `python3 meeting_checker.py` with Python 3; no third-party packages are needed. This finite verification corroborates, but does not substitute for, the all-parameter analytical proof above.

## Relationship to prior work
Oliveira (2011) studies coalescing-walk regimes on finite graphs; Cooper, Elsässer, Ono and Radzik (2013) bound multi-particle coalescence times on general graphs. Ohwa (2015) gives general exact backward-equation methods for meeting times, including examples on complete graphs, cycles and stars. Zhang, Tan and Krishnamachari (2014) study synchronous *discrete-time* meeting on regular graphs. Pickering and Lim (2014) examine voter-model consensus on complete bipartite networks. The basic resolvent/backward-equation method and the complete-graph boundary case are not claimed as new. The present evaluated result concerns every balanced complete multipartite graph under independent rate-one continuous-time clocks: its two conditional rational transforms, topology-independent mean versus topology-dependent variance, and opposite strict hazard laws. The inspected sources do not present this complete specialization. A broader, previously overlooked exact meeting-time theorem may subsume it.

## Limitations
The result concerns **two** independent walkers before first encounter, equal-size parts, uniform neighbor selection, exponential clocks and no additional sources, sinks, or drift. It does not classify unbalanced multipartite graphs, full coalescence from all vertices, first-encounter time for three or more walkers, or the jump-count process. Absence of a matching formula in the inspected literature is not a proof of worldwide priority.

## References
- R. I. Oliveira, *Mean field conditions for coalescing random walks*, arXiv:1109.5684v1 (first posted 2011-09-26), https://arxiv.org/abs/1109.5684 .
- C. Cooper, R. Elsässer, H. Ono, T. Radzik, *Coalescing Random Walks and Voting on Connected Graphs*, SIAM J. Discrete Math. 27 (2013), doi:10.1137/120900368.
- T. Ohwa, *Exact computation for meeting times and infection times of random walks on graphs*, Pacific J. Math. Ind. 7 (2015), doi:10.1186/s40736-015-0016-2, https://link.springer.com/article/10.1186/s40736-015-0016-2 .
- T. Zhang, T. Tan, B. Krishnamachari, *On the Meeting Time for Two Random Walks on a Regular Graph*, arXiv:1408.2005v1 (2014), https://arxiv.org/abs/1408.2005 .
- W. Pickering, C. Lim, *Solution of the Voter Model by Spectral Analysis*, arXiv:1408.2130v1 (2014), https://arxiv.org/abs/1408.2130 .

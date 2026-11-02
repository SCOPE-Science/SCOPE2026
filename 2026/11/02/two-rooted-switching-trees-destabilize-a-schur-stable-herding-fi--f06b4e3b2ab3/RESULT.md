# Two rooted switching trees destabilize a Schur-stable herding filter

## Finding
Consider the four-state proxy–auxiliary–transport (PAT) recursion for two followers, with a stationary leader at the origin and an *externally prescribed* alternating predecessor schedule. At one step follower 1 follows the leader and follower 2 follows follower 1; at the next follower 2 follows the leader and follower 1 follows follower 2. Every instantaneous predecessor graph is a tree rooted at the leader.

Set the PAT parameters to \(\lambda=1/2\), \(\mu=\delta=1/4\), \(\gamma=1\), and \(\alpha=\beta>0\). **For every \(75/32<\beta<25/8\), each four-state follower filter and each of the two frozen eight-state rooted-tree systems is Schur stable, yet alternating the two trees produces a positive real two-step Floquet multiplier strictly greater than one.** Thus some prescribed-schedule solutions diverge exponentially even with an immobile leader.

The two-step monodromy \(P_\beta\) has the exact determinant identity
\[
\det(I_8-P_\beta)=\frac{\beta^2(32\beta-75)(64\beta-225)}{4096}<0.
\]
At \(\beta=75/32\), the two-step system has multiplier \(1\), whereas its frozen systems remain Schur stable. At the rational example \(\beta=3\), the determinant equals \(-6237/4096\).

## Assumptions and scope
The scalar-coordinate PAT state of follower \(i\) is \(w_i=(p_i,a_i,t_i,r_i)^\top\in\mathbb R^4\); two spatial coordinates, if desired, evolve independently. A follower with predecessor position \(h_i(n)\) obeys \(w_i(n)=A_\beta w_i(n-1)+B_\beta h_i(n)\), where
\[
A_\beta=\begin{pmatrix}
1/2&0&0&0\\
1/2&1/4&0&-1\\
\beta/2&\beta/4&1/4&-\beta\\
\beta/2&\beta/4&1/4&1-\beta
\end{pmatrix},\qquad
B_\beta=\begin{pmatrix}1/2\\1/2\\\beta/2\\\beta/2\end{pmatrix},\qquad e=(0,0,0,1)^\top.
\]
If the predecessor is follower \(j\), the input is its preceding position \(h_i(n)=e^\top w_j(n-1)\); if it is the leader, the input is zero. This is the position-update convention of Kamimoto's PAT model, with prescribed rather than geometrically chosen predecessors. In the first mode \(S_\beta\), follower 1 follows the leader and follower 2 follows follower 1. In the second mode \(T_\beta\), the roles reverse. The modes alternate, so the two-step map is \(P_\beta=T_\beta S_\beta\).

**The prescribed predecessor schedule is not proved to arise from Kamimoto's distance-based selection rule.** This is a result about the arbitrary-predecessor-history extension of the PAT recursion, not a counterexample to the self-selected herd or its asserted spatial-measure results. The source's finite-depth operator identity is compatible with this result; no universal decay of its remainder is claimed there.

## Proof
Write \(U_\beta=B_\beta e^\top\) and let \(0_4\) be the four-by-four zero matrix. The frozen system matrices in follower order are
\[
S_\beta=\begin{pmatrix}A_\beta&0_4\\U_\beta&A_\beta\end{pmatrix},\qquad
T_\beta=\begin{pmatrix}A_\beta&U_\beta\\0_4&A_\beta\end{pmatrix}.
\]
Both are block triangular, so their spectra consist of two copies of the spectrum of \(A_\beta\).

Direct calculation gives
\[
\det(zI_4-A_\beta)=(z-1/2)\bigl(z^3+(\beta-3/2)z^2+(9/16)z-1/16\bigr).
\]
For the monic cubic \(f(z)=z^3+a z^2+b z+c\), here \(a=\beta-3/2\), \(b=9/16\), \(c=-1/16\). Its Schur reduction \((f(z)-c z^3 f(1/z))/z\) is
\[
\frac{255z^2+(256\beta-375)z+(16\beta+120)}{256}.
\]
The real quadratic Schur conditions become \(135-16\beta>0\), \(272\beta>0\), and \(750-240\beta>0\). Together with \(|c|<1\), they hold for all \(0<\beta<25/8\). Thus \(A_\beta\), \(S_\beta\), and \(T_\beta\) are Schur stable throughout the claimed interval.

Let \(J=\begin{psmallmatrix}0_4&I_4\\I_4&0_4\end{psmallmatrix}\) swap follower blocks, and set \(K_\beta=J S_\beta\). Then \(T_\beta=J S_\beta J\), hence \(P_\beta=K_\beta^2\). Exact block-determinant elimination yields
\[
\det(I_8-K_\beta)=\frac{\beta(75-32\beta)}{64},\qquad
\det(I_8+K_\beta)=\frac{\beta(225-64\beta)}{64}.
\]
Multiplying gives the stated determinant for \(I_8-P_\beta\). If \(75/32<\beta<25/8\), one factor \(32\beta-75\) is positive and the other \(64\beta-225\) is negative. Therefore \(\det(I_8-P_\beta)<0\). The monic real polynomial \(\det(zI_8-P_\beta)\) is negative at \(z=1\) and tends to positive infinity as \(z\to+\infty\); by continuity it has a real root \(z>1\). An eigenvector for this multiplier produces exponentially growing two-step trajectories. At \(\beta=75/32\), the determinant vanishes, giving multiplier \(1\) while \(75/32<25/8\).

## Verification
The standalone `verify.py` reconstructs \(A_\beta\), \(B_\beta\), the two frozen matrices, follower-swap symmetry, and the monodromy symbolically over the rationals. It checks the characteristic polynomial, Schur reduction, both determinant factors, the complete monodromy determinant, and the rational example. Run `python verify.py` with Python 3 and SymPy. Nine exact symbolic identities passed on the delivered artifact. The Schur inequalities and the existence of a real root above one are established analytically, not inferred from eigenvalue sampling.

## Relationship to prior work
Kamimoto, *Mathematics of Herding*, arXiv:2610.23992v1, first submitted October 14, 2026, gives the original PAT matrices, the single-follower Schur condition, an exact finite-depth operator identity for prescribed predecessor histories, and finite termination for fixed rooted trees. The present calculation identifies a specific open parameter interval where the time-dependent prescribed-tree operator is unstable despite each frozen tree being stable. It does **not** assert a flaw in any conclusion proved under the source's stated remainder or geometry hypotheses.

Liberzon and Morse (1999) already explain that switching between individually stable systems can be unstable. Maadani, Butcher, and Yucelen (2018) apply Floquet analysis to periodically switched multi-agent consensus. These general facts and methods are prior art; the contribution claimed here is the exact two-follower PAT-specific determinant and parameter window, not the generic possibility of switching instability. Olfati-Saber and Murray (2004) study different consensus protocols and switching settings. Maadani and Butcher (2020/2021) address more general Floquet stability but no matching PAT threshold was identified in accessible material.

## Limitations
No conclusion is made for the self-consistent distance-selected switching trajectories of the original moving-leader model. The precise destabilization interval is a proven sufficient open interval, **not** a complete stability classification for the alternating system outside it. The threshold \(75/32\) is an exact crossing of the unit multiplier, but no absence of other instabilities below it is asserted. The theorem considers no stochastic noise or additional communication constraints. Historical priority for the PAT-specific parameter calculation remains subject to independent examination, particularly because the complete 2020/2021 Floquet article was inaccessible.

## References
1. S. Kamimoto, *Mathematics of Herding*, arXiv:2610.23992v1, submitted 2026-10-14. https://arxiv.org/html/2610.23992v1
2. D. Liberzon and A. S. Morse, *Basic Problems in Stability and Design of Switched Systems*, IEEE Control Systems Magazine 19 (1999), 59–70. https://www.eng.yale.edu/controls/1999/basic.pdf
3. M. Maadani, E. A. Butcher, and T. Yucelen, *Periodically Switched Communication Topology in Multi-agent Consensus Control: Stability and Floquet Theory*, ACC (2018), DOI:10.23919/ACC.2018.8431606. https://www.researchgate.net/publication/327084336_Periodically_Switched_Communication_Topology_in_Multi-agent_Consensus_Control_Stability_and_Floquet_Theory
4. R. Olfati-Saber and R. M. Murray, *Consensus Problems in Networks of Agents with Switching Topology and Time-Delays*, IEEE TAC 49 (2004), 1520–1533. https://authors.library.caltech.edu/records/t2gnt-vd720
5. M. Maadani and E. A. Butcher, *Consensus Stability in Multi-agent Systems with Periodically Switched Communication Topology Using Floquet Theory*, TIMC 43 (2021), 1239–1254; first online 2020-12-09. https://doi.org/10.1177/0142331220969055

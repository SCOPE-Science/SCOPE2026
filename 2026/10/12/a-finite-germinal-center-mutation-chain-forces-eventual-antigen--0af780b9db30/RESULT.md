# A finite germinal-center mutation chain forces eventual antigen clearance

## Finding

Consider the non-mutating-antigen germinal-center ODE system (model (1)) of Erwin and Ciupe with a finite mutation chain \(B_0,B_1,\ldots,B_n\), where **\(n\ge2\)**. Assume all the source's rates are strictly positive, \(N(0)>0\), \(B_0(0)>0\), and \(V(0)>0\), while the other compartments initially vanish. Its terminal equations are
\[
\dot P=\kappa B_n,\qquad \dot V=-\mu VP.
\]
Then the unique nonnegative solution is global and bounded. For every \(t>0\),
\[
H(t),G(t),B_i(t),P(t)>0\quad(1\le i\le n),
\]
and the antigen concentration obeys
\[
V(t)\le V(t_0)\exp\{-\mu P(t_0)(t-t_0)\}\qquad(t\ge t_0>0).
\]
In particular, \(V(t)\to0\) as \(t\to\infty\).

Therefore, within this exact deterministic non-mutating-antigen model, a finite \(n=50\) mutation chain does **not** produce a positive asymptotic antigen level. A nearly constant finite-window numerical trace may nevertheless have a biologically long or numerically unresolved transient.

## Assumptions and scope

The assertion concerns the source's model (1) with \(n\ge2\) and strictly positive constants \(s_N,d_N,\alpha_N,d_H,\gamma,d_G,\eta,d,\sigma,\alpha,\kappa,\mu\). The conditions on initial data are those specified above. The equations of model (1) distinguish an intermediate \(B_1\) equation from a terminal \(B_n\) equation; when \(n=1\) these are both equations for the same compartment and are not simultaneously a well-defined ODE without an extra convention. Accordingly, **no \(n=1\) result is asserted**.

The claim does not address stochastic discrete cell counts, clearance on a biologically short timescale, or any of the source's later mutating-antigen models.

## Proof

The relevant model (1) equations, for \(n\ge2\), are
\[
\begin{aligned}
\dot N&=s_N-d_NN-\alpha_NVN,\\
\dot H&=\alpha_NVN-d_HH-\gamma HB_0,\\
\dot G&=\gamma HB_0-d_GG-\eta G\sum_{i=1}^n B_i,\\
\dot B_0&=-dB_0-\sigma B_0H,\\
\dot B_1&=\alpha\sigma B_0H-(d+\sigma G)B_1,\\
\dot B_i&=\alpha\sigma B_{i-1}G-(d+\sigma G)B_i\quad(2\le i\le n-1),\\
\dot B_n&=\alpha\sigma B_{n-1}G-(d+\kappa)B_n,\\
\dot P&=\kappa B_n,\\
\dot V&=-\mu VP.
\end{aligned}
\]
For \(n=2\), the range \(2\le i\le n-1\) is empty. Every equation is quasi-positive on the nonnegative cone; standard uniqueness and the nonnegative variation-of-constants formulas therefore preserve nonnegativity.

First prove boundedness. Set
\[
Q=B_0+\sum_{i=1}^n\alpha^{-i}B_i+\alpha^{-n}P.
\]
Every maturation gain cancels the immediately preceding clone's loss after multiplication by its weight, and \(\kappa B_n\) cancels the terminal plasma-cell flux. Thus
\[
\dot Q=-d\left(B_0+\sum_{i=1}^n\alpha^{-i}B_i\right)\le0.
\]
All clones and \(P\) are bounded. With \(T=N+H+G\), the recruitment, activation, and differentiation terms cancel appropriately:
\[
\dot T=s_N-d_NN-d_HH-d_GG-\eta G\sum_{i=1}^nB_i
\le s_N-mT,
\]
where \(m=\min\{d_N,d_H,d_G\}>0\). Hence \(N,H,G\) are bounded. Since \(\dot V\le0\), \(0\le V(t)\le V(0)\). Local existence plus these uniform bounds implies global existence.

For finite time, the exact antigen equation gives
\[
V(t)=V(0)\exp\left(-\mu\int_0^tP(s)\,ds\right)>0.
\]
Because \(N(0)>0\) and its forcing \(s_N\) is positive, \(N(t)>0\) for every \(t\ge0\). Thus \(\alpha_N V N\) forces \(H(t)>0\) for every \(t>0\). Also
\[
B_0(t)=B_0(0)\exp\left(-\int_0^t(d+\sigma H(s))\,ds\right)>0.
\]
It follows that \(\gamma HB_0\) forces \(G(t)>0\) for \(t>0\), and \(\alpha\sigma B_0H\) forces \(B_1(t)>0\). Inductively, the positive input \(\alpha\sigma B_{i-1}G\) forces every later clone \(B_i(t)>0\) for \(2\le i\le n\) and all \(t>0\), including the terminal clone. Each conclusion follows directly from the corresponding scalar variation-of-constants integral; no uniform-in-\(n\) lower bound is needed.

Since \(\dot P=\kappa B_n>0\) for \(t>0\) and \(P(0)=0\), \(P(t)>0\) and is strictly increasing. Fix \(t_0>0\). Then \(P(t)\ge P(t_0)>0\) for \(t\ge t_0\). Integrating \(\dot V=-\mu VP\) from \(t_0\) gives the stated exponential upper bound and \(V(t)\to0\).

## Verification

The conservation/dissipation identity for \(Q\) follows by cancelling each transition \(B_{i-1}\to B_i\) with weights \(\alpha^{-i}\), including the special \(B_0\to B_1\) transition through \(H\), and cancelling \(B_n\to P\). The \(N+H+G\) bound is obtained by direct addition. These symbolic identities and positivity arguments apply for every **\(n\ge2\)**; finite numerical experiments are neither needed nor an infinite-time proof.

## Relationship to prior work

Erwin and Ciupe's *Germinal center dynamics during acute and chronic infection* (*Mathematical Biosciences and Engineering* 14 (2017), 655–671, DOI 10.3934/mbe.2017037) develops this finite one-way model and interprets its \(n=50\) numerical run as failing to reach the terminal clone and exhibiting chronic antigen persistence. Under the paper's exact ODE, the terminal clone and plasma cells are strictly positive for every positive time and \(P\) has no removal term, so this numerical interpretation does not imply a positive long-time antigen limit. General positivity of cooperative cascades and scalar comparison are standard; the finding is their source-specific consequence for this published asymptotic interpretation.

Other germinal-center models with affinity selection or evolving antigen, including Meyer-Hermann et al. (2012, DOI 10.1016/j.celrep.2012.05.010) and De Boer and Perelson (2017, DOI 10.1128/JVI.00983-17), have different equations and do not themselves determine the limit in this finite non-mutating cascade.

## Limitations

All statements concern exact nonnegative real concentrations, **\(n\ge2\)**, and the source's non-mutating-antigen model (1). No uniform clearance-time estimate, terminal-clone detection threshold, or mutating-antigen conclusion follows. The unusual \(n=1\) boundary requires a separately specified model and is deliberately excluded.

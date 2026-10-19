# An exact renewal-clock initialization reversal on a directed three-agent opinion cycle

## Finding
Consider a three-person directed voter cycle, in which \(A\) copies \(B\), \(B\) copies \(C\), and \(C\) copies \(A\) on their respective activation times. Initially all three opinions are different. The activation intervals of \(A\) have an arbitrary strictly positive distribution with mean one, while \(B\) and \(C\) activate independently at unit-rate Poisson times.

Define the Laplace quantities
\[
\phi=\mathbb E[e^{-T}],\qquad m=\mathbb E[T e^{-T}],\qquad K=1-\phi+m,\qquad h=\frac{(1-\phi)^2}{K}.
\]
Let the outcome vector list the probabilities that the eventual common opinion is, respectively, the original opinion of \(A\), \(B\), or \(C\). If the first activation interval of \(A\) has the full interarrival law \(T\) (fresh initialization), the exact outcome vector is
\[
\boxed{\mathbf p_{\mathrm F}=\frac1K\big((1-\phi)^2,\ \phi(1-\phi),\ m\big).}
\]
If instead the renewal clock is in equilibrium at time zero, independently of the opinions, then
\[
\boxed{\mathbf p_{\mathrm S}=(1-2h,\ h,\ h).}
\]
In particular the initial opinions of \(B\) and \(C\) have equal stationary-start fixation probabilities for every such renewal law, whereas their fresh-start probabilities need not agree.

For \(T\) Erlang with shape two and rate two, \(\phi=4/9\) and \(m=8/27\), and hence
\[
\boxed{\mathbf p_{\mathrm F}=(25,20,24)/69,\qquad \mathbf p_{\mathrm S}=(19,25,25)/69.}
\]
At all-Poisson updating the probability for each initial opinion is \(1/3\). Thus merely changing the initialization of the same mean-one Erlang clock reverses whether the original opinion of \(A\) wins more or less often than the Poisson benchmark.

## Assumptions and scope
The underlying directed graph has exactly the three arcs \(A\to B\), \(B\to C\), and \(C\to A\), interpreted as copying sources. Each node has no self-loop. The initial opinions \((a,b,c)\) are mutually distinct symbols or real numbers; clocks are independent of them. Upon its own activation a node immediately adopts its indicated neighbor's current opinion, and subsequently retains this opinion until its next activation. The clock of \(A\) has i.i.d. strictly positive intervals \(T\) with \(\mathbb ET=1\); the other two clocks have independent exponential intervals of mean one. In the fresh protocol \(A\)'s first interval is an independent draw from \(T\). In the stationary protocol \(A\)'s first forward residual \(R\) satisfies
\[
\Pr(R>t)=\int_t^\infty\Pr(T>u)\,du,\qquad t\ge0,
\]
and all subsequent \(A\) intervals have law \(T\). Both protocols initialize the Poisson clocks in their memoryless state. All real-time statements concern this finite asynchronous voter process; these formulas are not an approximation, nor a statement about arbitrary directed graphs.

## Proof
**Almost-sure absorption.** At every activation of \(A\), immediately afterward \(A\) and \(B\) share one opinion. In the next interval until \(A\) reactivates, if \(C\)'s first Poisson activation occurs before \(B\)'s first and before \(A\)'s next activation, \(C\) copies \(A\) and consensus is attained (or it was present already). Conditional on the post-\(A\)-activation state, the probability of this event is
\[
q=\mathbb E\!\left[\int_0^T e^{-2t}\,dt\right]=\frac{1-\mathbb E[e^{-2T}]}2>0.
\]
The event uses a fresh independent renewal interval and the memoryless Poisson clocks, so each subsequent \(A\)-renewal interval supplies a new conditional chance at least \(q\). The renewal process produces infinitely many activations almost surely because \(T>0\) and \(\mathbb ET=1\). Consequently the probability of failing to attain consensus after \(n\) such opportunities is at most \((1-q)^n\), proving almost-sure finite-time consensus. Consensus is absorbing.

**Embedded two-coordinate dynamics.** Immediately after any \(A\) activation, the opinions are \((u,u,v)\). During the next \(A\)-interarrival of length \(t\), \(A\) remains fixed. The conditional expectations satisfy \(\dot x_C=x_A-x_C\), \(\dot x_B=x_C-x_B\), hence
\[
\mathbb E[x_C(t)\mid u,v]=u+(v-u)e^{-t},\qquad
\mathbb E[x_B(t)\mid u,v]=u+(v-u)t e^{-t}.
\]
Upon \(A\)'s next activation the new \(A\) and \(B\) opinions both equal the preceding \(B\) opinion, so the expected new pair \((u',v')\), conditional on the starting pair, is the linear image
\[
\mathbb E\begin{bmatrix}u'\\v'\end{bmatrix}
=\begin{bmatrix}1-m&m\\1-\phi&\phi\end{bmatrix}
\begin{bmatrix}u\\v\end{bmatrix}.
\]
Its probability row vector invariant under right multiplication is \(((1-\phi)/K,m/K)\), because \(m>0\), \(1-\phi>0\), and their sum is \(K\). Therefore the weighted post-event opinion \(((1-\phi)u+mv)/K\) is a bounded martingale at \(A\) activation times for indicator-valued opinions. Almost-sure consensus and bounded convergence imply that its initial expectation is the probability of the final opinion of a chosen initial label.

**First-interval reduction.** Before the first \(A\) activation, hold its initial opinion \(a\) fixed. For an arbitrary first-interval length \(t\) the Poisson evolution gives
\[
\mathbb E[x_B(t)\mid a,b,c]=a+(b-a)e^{-t}+(c-a)t e^{-t},\quad
\mathbb E[x_C(t)\mid a,b,c]=a+(c-a)e^{-t}.
\]
At the first activation \(A\) copies \(B\). Let \(L=\mathbb E[e^{-U}]\), \(J=\mathbb E[Ue^{-U}]\), with \(U\) the protocol-specific first \(A\) interval. The invariant weighted mean after that event is
\[
 a+\frac{(1-\phi)L}{K}(b-a)
 +\frac{(1-\phi)J+mL}{K}(c-a).
\]
Read the coefficients of \(a,b,c\) by assigning one initial opinion the indicator value one and the others zero. Under a fresh start \((L,J)=(\phi,m)\). This yields
\[
 p_B=\frac{\phi(1-\phi)}K,\quad p_C=\frac{m}K,\quad
 p_A=1-p_B-p_C=\frac{(1-\phi)^2}K.
\]

**Equilibrium-clock identity.** For the unit-mean equilibrium residual \(R\), Fubini's theorem gives, for \(s>0\),
\[
\mathbb E[e^{-sR}]=\frac{1-\mathbb E[e^{-sT}]}s.
\]
Evaluation at \(s=1\) and differentiation (justified by the boundedness of \(t e^{-st}\) near \(s=1\)) give \(L=1-\phi\) and \(J=1-\phi-m\). Substitution into the first-interval formula yields
\[
 p_B=p_C=\frac{(1-\phi)^2}{K}=h,\qquad p_A=1-2h.
\]
The probability vectors are normalized by construction. For Erlang-2 rate-two intervals, \(\mathbb E[e^{-T}]=(2/3)^2=4/9\), and \(\mathbb E[Te^{-T}]=(2/3)^3=8/27\); the rational vectors in the finding follow. The uniform rate-one Poisson case has \((\phi,m)=(1/2,1/4)\), giving three probabilities \(1/3\), which proves the stated strict reversal for the specified Erlang law.

## Verification
The included standalone Python program `verify.py` uses exact rational arithmetic to solve generator-harmonic equations for Erlang activation clocks of shapes \(1\) through \(12\). This finite-phase method is independent of the renewal-epoch proof: each Erlang clock is represented by a cyclic Markov chain of exponential stages, and the resulting exact consensus probabilities are compared against both protocols' formulas. The program checks all omitted generator equations and probability normalization, reproduces the stated rational vectors, and independently runs seeded Monte Carlo trajectories under each protocol. Run `python3 verify.py` with a standard Python 3 interpreter. Exact finite-phase calculations confirm a countable set of instances; they do not establish the theorem for arbitrary waiting-time laws, which is proved analytically above.

## Relationship to prior work
Chu and Porter [1] establish a general family of non-Markovian opinion-copying models on temporal networks; their published primary text considers heterogeneous clocks, discusses a two-node first-event phenomenon, and studies consensus analytically and numerically. It does not state the present three-node renewal-epoch winner law, the protocol-complement formula, or the stationary equality of two distinct initial opinions. Their model supplies the natural interpretation of asynchronous vertex-copying dynamics and its primary MSC classification. Takaguchi and Masuda [2] explicitly distinguish equilibrium initial interevent laws from ordinary renewal intervals, but their activation is attached to edges and a disagreeing edge changes a uniformly selected endpoint, whereas here a single vertex copies its directed successor. The equilibrium residual formula is classical and is not itself claimed to be new. Masuda, Gibert, and Redner [3] study heterogeneous voter update rates in a Markovian setting; a memoryless clock has no fresh-versus-equilibrium distinction. The present claim is the joint exact fixation law and its initialization reversal on the smallest directed cycle for which one update need not create consensus.

## Limitations
The theorem is a three-agent result; it does not classify larger graphs or clocks dependent on the opinions. The exact equality of the two Poisson-node winner probabilities depends on equal Poisson rates and equilibrium initialization of the other renewal clock. This is a mathematical result for a specified process, not a claim of empirical social-network accuracy. Established renewal identities and Markov-chain martingale ideas are used; priority for the combined three-agent identity has been checked against accessible closely related sources but is not independently certified.

## References
[1] W. Chu and M. A. Porter, *Non-Markovian Models of Opinion Dynamics on Temporal Networks*, SIAM Journal on Applied Dynamical Systems 22 (2023), 2624–2647. DOI 10.1137/22M151858X. First public preprint 2022-08-26, arXiv:2208.12787.

[2] T. Takaguchi and N. Masuda, *Voter Model with Non-Poissonian Interevent Intervals*, Physical Review E 84 (2011), 036115. DOI 10.1103/PhysRevE.84.036115.

[3] N. Masuda, N. Gibert, and S. Redner, *Heterogeneous Voter Models*, Physical Review E 82 (2010), 010103(R). arXiv:1003.0768.

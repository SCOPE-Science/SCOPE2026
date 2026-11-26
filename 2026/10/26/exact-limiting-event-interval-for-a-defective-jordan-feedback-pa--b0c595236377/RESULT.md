# Exact limiting event interval for a defective Jordan feedback pair

## Finding

Fix \(a,\gamma>0\) and set
\[
J=\begin{pmatrix}-a&\gamma\\0&-a\end{pmatrix}.
\]
Consider the plant \(\dot x=u\) with feedback \(u=J\hat x\), where \(\hat x(t)=x_k:=x(t_k)\) is held constant on \([t_k,t_{k+1})\). The next event is the first time \(s\ge T\) for which
\[
\|x_k-x(t_k+s)\|_2\ge\sigma\|x(t_k+s)\|_2,
\]
where \(\sigma>0\) and \(T\ge0\) is a minimum wait. Put \(L=\|J\|_2\) and \(m=\sigma_{\min}(J)>0\). Assume
\[
0<\delta<\min\{a^{-1},L^{-1}\},\qquad
0<\sigma<\frac{\delta m}{1+\delta L},\qquad 0\le T<\delta.
\]
Then every nonzero initial state generates infinitely many events without Zeno accumulation, and
\[
\lim_{k\to\infty}(t_{k+1}-t_k)=\max\left\{T,\frac{\sigma}{a(1+\sigma)}\right\}.
\]
The limit is independent of the shear \(\gamma\). With \(T=0\), it equals \(\sigma/a-\sigma^2/a+O(\sigma^3)\) as \(\sigma\downarrow0\) for fixed \(a,\gamma\).

## Assumptions and scope

All norms are Euclidean. The zero initial state is excluded. The hypotheses on the parameters are sufficient and are not asserted to be necessary. The plant and trigger are part of the hypotheses; assuming only that an ideal continuous-feedback matrix is a defective Hurwitz matrix does not specify the held-input flow.

## Proof

**Uniform control of the threshold crossing.** For a held sample \(x\ne0\), the state at elapsed time \(s\) is \((I+sJ)x\). On \([0,\delta]\) it is nonzero since \(\|(I+sJ)x\|_2\ge (1-sL)\|x\|_2>0\). Write
\[
g_x(s)=\frac{s\|Jx\|_2}{\|(I+sJ)x\|_2}.
\]
This function starts at zero and is strictly increasing on that interval: its derivative is
\[
g_x'(s)=\frac{\|Jx\|_2(\|x\|_2^2+s x^\top Jx)}{\|(I+sJ)x\|_2^3}>0,
\]
using \(x^\top Jx\ge-L\|x\|_2^2\). Put
\[
c=\frac{\sigma}{L(1+\sigma)},\qquad s_+=\frac{\sigma}{m-\sigma L}.
\]
The hypotheses imply \(m-\sigma L>0\) and \(s_+<\delta\). For \(s<c\), the upper estimate \(g_x(s)\le sL/(1-sL)\) is strictly less than \(\sigma\); at \(s=s_+\), the lower estimate \(g_x(s_+)\ge s_+m/(1+s_+L)\) is \(\sigma\). It follows by continuity and strict increase that the unique crossing \(\rho_\sigma(x)\) in \([0,\delta]\) belongs to \([c,s_+]\). As \(T<\delta\), the first admissible event interval is \(\tau_k=\max\{T,\rho_\sigma(x_k)\}\). Therefore \(c\le\tau_k<\delta\).

**Sampled directions.** Put \(p_k=1-a\tau_k\), \(q_k=\gamma\tau_k\). The update is
\[
x_{k+1,1}=p_k x_{k,1}+q_k x_{k,2},\qquad x_{k+1,2}=p_k x_{k,2}.
\]
Since \(0<p_k<1\), the update is invertible and every nonzero sample yields another nonzero sample. If \(x_{0,2}=0\), the trajectory stays on the eigenline at all sample times. Otherwise \(x_{k,2}\ne0\) for every \(k\), so the reciprocal slope \(v_k=x_{k,1}/x_{k,2}\) is defined even at a vertical direction, and
\[
v_{k+1}=v_k+\frac{q_k}{p_k}\ge v_k+\gamma c.
\]
Hence \(v_k\to+\infty\) and the directions converge projectively to the eigenline \(\mathbb R e_1\), where \(e_1=(1,0)^\top\). This also covers the case of a trajectory starting on that line, where the projective direction is constant.

**Limit and completeness.** The crossing depends only on the projective direction, and it is continuous there. Indeed, for converging directions choose converging unit representatives up to sign. Every subsequential limit of the crossing times in the compact interval \([c,s_+]\) solves the limit-direction threshold equation by joint continuity of \(g_x(s)\); that equation has exactly one root on the interval. On the eigenline, \(g_{e_1}(s)=as/(1-as)\) on \([0,\delta]\), so the crossing is \(\sigma/[a(1+\sigma)]\). Taking the limit of \(\max\{T,\rho_\sigma(x_k)\}\) proves the formula, including equality of the two alternatives. There is an event from every nonzero sample and \(\tau_k\ge c>0\), so there are infinitely many events with no finite accumulation time.

Under these hypotheses the states also decay exponentially. In a product of \(k\) update matrices the diagonal entries are bounded by \((1-ac)^k\); because each strictly upper-triangular contribution can occur at most once in a nonzero product term, the upper off-diagonal entry is bounded by \(k\gamma\delta(1-ac)^{k-1}\). This is exponential in \(k\); the bound \(\tau_k<\delta\) and bounded between-event flow give exponential decay in continuous time as well.

## Verification

The proof uses the exact held-input flow, uniform two-sided crossing bounds, and a two-case projective argument. On the eigenline the interval is already the claimed limit. Off the eigenline the reciprocal slope has a uniformly positive increment, including when the first coordinate passes through zero. No finite trajectory simulation is used to infer convergence.

## Relationship to prior work

Postoyan, Sanfelice, and Heemels analyze periodicity and convergence of inter-transmission times in planar linear event-triggered systems. Their time-regularized analysis treats distinct real eigenvalues and a semisimple repeated real eigenvalue; it leaves the defective repeated-eigenvalue case as a conjecture with a limit near \(\max\{T,\sigma/a\}\) at small \(\sigma\). In the integrator realization above, the exact affine held-input map permits a direct proof of convergence and gives the exact crossing, including the correction to the leading term and the regularization crossover. This is not a resolution for arbitrary defective closed-loop systems.

## Limitations

The calculation does not classify other plant realizations, nonlinear plants, noisy measurements, or other trigger rules. In particular the factor \((1+\sigma)^{-1}\) is derived using the exact affine sample-and-hold flow and should not be transferred to other flows without proof.

## References

1. R. Postoyan, R. G. Sanfelice, and W. P. M. H. Heemels, “Inter-event Times Analysis for Planar Linear Event-triggered Controlled Systems,” 2019 IEEE Conference on Decision and Control, pp. 1662–1667. DOI: 10.1109/CDC40024.2019.9028888.
2. R. Postoyan, R. G. Sanfelice, and W. P. M. H. Heemels, “Explaining the ‘Mystery’ of Periodicity in Inter-Transmission Times in Two-Dimensional Event-Triggered Controlled Systems,” IEEE Transactions on Automatic Control 68(2), 912–927, 2023. DOI: 10.1109/TAC.2022.3147009.

# Exact modal gap for sparse event-triggered control

## Finding

Let \(A,C\in\mathbb R^{n\times n}\) be real symmetric matrices satisfying \(AC=CA\) and \(C\succ0\). During each control pulse of prescribed length \(\epsilon>0\), let the state obey \(\dot x=-Cx\); during the following zero-input interval let it obey \(\dot x=Ax\). Take \(V(x)=\|x\|_2^2\), and start the next pulse at the first post-pulse time when

\[
V(x(t))=V(x(t_k))e^{-\lambda(t-t_k)},\qquad 0<\lambda<2\lambda_{\min}(C).
\]

Because \(A\) and \(C\) are symmetric and commute, there is a common orthonormal eigenbasis with eigenvalue pairs \((a_i,c_i)\), where \(c_i>0\). The exact infimum of all zero-input gaps over nonzero states is

\[
d_*=\epsilon\min_{i:\,2a_i+\lambda>0}\frac{2c_i-\lambda}{2a_i+\lambda}.
\]

If no index satisfies \(2a_i+\lambda>0\), or if a particular state is supported only on modes with \(2a_i+\lambda\le0\), the trigger is never reached after the pulse: every active off-phase mode decays at least as fast as the exponential threshold. Otherwise, every trajectory with a nonzero component in a trigger-capable mode has a finite next trigger and its gap is at least \(d_*\). Equality holds exactly when the state is supported on the common eigenmodes attaining the displayed minimum.

## Assumptions and scope

The matrices are finite-dimensional, real symmetric, commute, and have exact known entries. The pulse duration \(\epsilon\) is fixed and positive. The pulse generator is \(-C\), the zero-input generator is \(A\), and the threshold uses the Euclidean quadratic \(V(x)=\|x\|_2^2\). The rate satisfies \(0<\lambda<2\lambda_{\min}(C)\), so the threshold falls more slowly than the Lyapunov function during every pulse. No disturbance, model uncertainty, saturation, sampling delay, or measurement noise is included. A state supported only on modes with \(2a_i+\lambda\le0\) requires no further pulse and has no finite next trigger.

## Proof

Since \(A\) and \(C\) are real symmetric and commute, an orthogonal change of coordinates diagonalizes both. Write the coordinates at the beginning of a pulse as \(x_{k,i}\). After the pulse, and then after an additional zero-input time \(d\ge0\), the \(i\)-th coordinate is

\[
x_i(t_k+\epsilon+d)=e^{-c_i\epsilon+a_i d}x_{k,i}.
\]

Let \(p_i=x_{k,i}^2/\|x_k\|_2^2\), so \(p_i\ge0\) and \(\sum_i p_i=1\) for a nonzero state. The trigger equality is equivalent to

\[
G(d):=\sum_i p_i\exp\!\left(-(2c_i-\lambda)\epsilon+(2a_i+\lambda)d\right)=1.
\]

Set \(\alpha_i=2c_i-\lambda>0\) and \(\beta_i=2a_i+\lambda\). If \(\beta_i\le0\), then \(e^{-\alpha_i\epsilon+\beta_i d}<1\) for every \(d\ge0\). If \(\beta_i>0\), that term first reaches one at

\[
d_i=\frac{\alpha_i\epsilon}{\beta_i}
=\epsilon\frac{2c_i-\lambda}{2a_i+\lambda}.
\]

When the set of positive \(\beta_i\) is nonempty, put \(d_*=\min_{\beta_i>0}d_i\). For every \(0\le d<d_*\), every summand's exponential factor is strictly below one, hence \(G(d)<1\); no convex combination can trigger earlier. A state supported on any minimizing mode has \(G(d_*)=1\), proving sharpness. For a state with positive weight on at least one mode satisfying \(\beta_i>0\), \(G(d)\to\infty\) as \(d\to\infty\), so continuity gives a finite crossing. Equality at \(d_*\) occurs precisely when all positive state weights lie on minimizing modes. If every \(\beta_i\le0\), all summands remain strictly below one for every finite \(d\), so there is no next trigger. These arguments prove the claimed classification and exact infimum.

For comparison with the generic lower bound in Banno, Azuma, Ariizumi, and Asai, choose \(P^*=I\) and \(Q=2C\). Then \(\lambda^*=2c_{\min}\), and their bound is \(\tau_{\min}=(2c_{\min}-\lambda)\epsilon/[2(2|a_{\max}|+\lambda)]\), where \(a_{\max}=\max_i a_i\). Whenever a finite trigger-capable mode exists,

\[
d_*\ge\frac{(2c_{\min}-\lambda)\epsilon}{2a_{\max}+\lambda}
\ge 2\tau_{\min}.
\]

Thus the exact modal gap is at least twice that generic bound in this commuting-symmetric class; the modal formula, not the factor-two comparison, is the principal claim.

## Verification

The proof uses only simultaneous orthogonal diagonalization, exact solutions of scalar linear ODEs, and the first trigger equality. The standalone standard-library script `verify_gap.py` checks a three-mode example: a pure minimizing mode triggers at the formula's value, a mixed state triggers later, and a state supported only on non-trigger-capable modes has no finite trigger. It also checks the factor-two comparison for that example. The computation is a consistency check, not a substitute for the proof.

## Relationship to prior work

Banno, Azuma, Ariizumi, and Asai introduce the same pulse/off architecture and exponential Lyapunov threshold. Their 2022 full-text article's Theorem 1 proves global asymptotic stability and a positive generic lower bound for the zero-input interval, but does not state the exact minimum over initial directions, the common-eigenmode equality cases, or the no-trigger classification above. The article identifies a 2021 American Control Conference paper as a preliminary version; its full text was not accessible, so that version remains a residual comparison risk. The present claim does not claim their framework or stability theorem as new; it solves the trigger equation exactly in the commuting-symmetric subclass and identifies the worst mode. Wang, Azuma, Ariizumi, and Asai (2018) also study intermittently actuated control and report a lower bound on inter-triggering time, but the accessible abstract describes a piecewise-constant held input \(u(t)=Fx(t_k)\), not the continuously state-dependent pulse \(u(t)=Fx(t)\) analyzed here. The full text of that conference paper was not accessible during this check, so it remains another residual comparison risk.

## Limitations

The exact formula relies on the common eigenbasis. It does not classify noncommuting or nonsymmetric generators, disturbances, uncertain matrices, actuator saturation, delayed measurements, or state-dependent pulse lengths. The no-trigger case means the open-loop state already decays at least as fast as the chosen threshold; it is not an instability or a failure of the formula. No independent audit or empirical validation is claimed.

## References

1. I. Banno, S. Azuma, R. Ariizumi, and T. Asai, “Data-driven sparse event-triggered control of unknown systems,” 2021 American Control Conference, DOI: 10.23919/ACC50511.2021.9482910. The public bibliographic record gives 27 May 2021; the full text was not accessible during this check.
2. I. Banno, S. Azuma, R. Ariizumi, and T. Asai, “Sparse event-triggered control of linear systems,” *International Journal of Robust and Nonlinear Control* 33(1), 134–158. First published 15 July 2022. DOI: 10.1002/rnc.6278. Theorem 1 and equations (5)–(8), (18)–(23).
3. H. Wang, S. Azuma, R. Ariizumi, and T. Asai, “Event-triggered control of intermittently-actuated systems,” 62nd Annual Conference of the Institute of Systems, Control and Information Engineers, 2018. Only the abstract was accessible; it describes a lower bound on inter-triggering time for a piecewise-constant intermittent controller.

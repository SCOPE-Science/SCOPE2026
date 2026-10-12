# A valid equilibrium enclosure replaces an undefined derivative-inverse bound in an adaptive vaccination game
## Finding

Consider the adaptive vaccination dynamics
\[
\dot P=f(P):=-r-\epsilon\pi'(P)(1-P)+\pi(P),
\]
with \(0<r<1\), \(0<\epsilon<1\), and the convex assumptions used in Theorem 3.2(ii) of Balabanova and Duong: \(\pi(0)=1\), \(\pi\) is decreasing and convex on \([0,p_*]\), and \(\pi(P)=0\) for \(P\ge p_*\). Let \(P_0\) denote the unique equilibrium.

The theorem prints the upper endpoint
\[
\pi'^{-1}\left(\frac{{1-r}}{{\epsilon}}\right).
\]
That expression is not a valid bound under the theorem's own hypotheses. Indeed,
\[
\frac{{1-r}}{{\epsilon}}>0,
\qquad
\pi'(P)\le0,
\]
so the proposed argument lies outside the range of \(\pi'\). Moreover, convexity makes \(\pi'\) nondecreasing, not necessarily strictly increasing, so \(\pi'^{-1}\) need not exist as an ordinary inverse even for values in its range.

A valid replacement is
\[
\pi^{-1}(r)<P_0\le\bar P\le\min\{p_*,U\},
\]
where \(\bar P\) is the unique solution in \((0,p_*)\) of
\[
1-\frac{{P}}{{p_*}}-r-\epsilon\pi'(P)(1-P)=0
\]
and
\[
U=\frac{{1-r-\epsilon\pi'(0)}}{{1/p_*-\epsilon\pi'(0)}}.
\]
The last explicit bound can be attained. If \(p_*=1\) and \(\pi(P)=1-P\), then
\[
P_0=U=1-\frac{{r}}{{1+\epsilon}}.
\]
Thus the correction does not merely delete an undefined term: it supplies a computable equilibrium enclosure, with an exact admissible equality case.

## Assumptions and scope

The claim concerns the scalar adaptive dynamics and the convex case of Theorem 3.2(ii). Smoothness is only used to interpret \(\pi'\) and to ensure that the flat continuation \(\pi=0\) beyond \(p_*\) has the expected endpoint derivative. The argument does not modify the paper's existence, uniqueness, stability, or comparative-statics conclusions. It corrects only the stated upper enclosure and the final inversion step used to obtain it.

The strict lower bound uses that \(\pi'(P)<0\) at \(P=\pi^{-1}(r)\), which holds in the strictly decreasing interior regime considered by the model. If a more general non-strictly decreasing function were allowed, the corresponding lower relation should be written non-strictly.

## Proof

Convexity and the endpoint values \(\pi(0)=1\), \(\pi(p_*)=0\) imply that the graph of \(\pi\) lies below its endpoint chord:
\[
\pi(P)\le 1-\frac{{P}}{{p_*}},
\qquad 0\le P\le p_*.
\]
Define
\[
h(P)=1-\frac{{P}}{{p_*}}-r-\epsilon\pi'(P)(1-P).
\]
Then \(f(P)\le h(P)\) on \([0,p_*]\). Also
\[
h'(P)=-\frac1{{p_*}}-\epsilon\pi''(P)(1-P)+\epsilon\pi'(P)<0.
\]
At the endpoints,
\[
h(0)=1-r-\epsilon\pi'(0)>0,
\]
and \(h(p_*)=-r<0\), because either \(p_*=1\) or smooth flat continuation gives \(\pi'(p_*)=0\). Hence \(h\) has a unique root \(\bar P\in(0,p_*)\).

The source already proves that \(f\) is strictly decreasing in the convex case, hence its unique root is \(P_0\). Since
\[
0=f(P_0)\le h(P_0),
\]
and \(h\) is strictly decreasing with zero at \(\bar P\), it follows that
\[
P_0\le\bar P.
\]

For an explicit bound, convexity also gives \(\pi'(P)\ge\pi'(0)\). Therefore
\[
h(P)\le H(P):=1-\frac{{P}}{{p_*}}-r-\epsilon\pi'(0)(1-P).
\]
The affine function \(H\) is strictly decreasing and has its unique zero at
\[
U=\frac{{1-r-\epsilon\pi'(0)}}{{1/p_*-\epsilon\pi'(0)}}.
\]
If \(U<p_*\), then \(h(U)\le0\), hence \(\bar P\le U\); if \(U\ge p_*\), then \(\bar P<p_*\). Thus in all cases
\[
\bar P\le\min\{p_*,U\}.
\]

For the lower bound, let \(P_r=\pi^{-1}(r)\). Then
\[
f(P_r)=-\epsilon\pi'(P_r)(1-P_r)>0,
\]
so strict decrease of \(f\) gives \(P_0>P_r\).

Finally, take \(p_*=1\) and \(\pi(P)=1-P\). The equilibrium equation becomes
\[
-r+\epsilon(1-P)+(1-P)=0,
\]
so
\[
P_0=1-\frac{{r}}{{1+\epsilon}}.
\]
Since \(\pi'(0)=-1\), this equals \(U\). This admissible equality case proves that the explicit replacement bound can be sharp.

## Verification

The accompanying `verification/verify.py` checks the algebraic equality case over a grid of \(r\) and \(\epsilon\), verifies the enclosure numerically for convex families \(\pi(P)=(1-P)^k\) with \(k=1,2,3,4\), and confirms that the printed inverse argument is positive while the derivative range is nonpositive. These computations are reproducibility checks; the proof above is analytic and does not depend on finite sampling.

## Relationship to prior work

Balabanova and Duong introduce this adaptive dynamics, prove uniqueness and stability in the convex case, and derive the lower endpoint \(\pi^{-1}(r)\). Their accepted manuscript and published article both display the upper endpoint \(\pi'^{-1}((1-r)/\epsilon)\). The full proof first obtains a valid comparison equation for an implicit upper root, but its final step compares the negative derivative \(\pi'(\bar P)\) with the positive number \((1-r)/\epsilon\) and then applies an inverse of \(\pi'\). That last inversion is the failure corrected here.

The classic vaccination game of Bauch and Earn characterizes equilibrium through the infection-risk curve and relative vaccination risk, but it does not contain this adaptive derivative term or the source-specific convex upper enclosure. Searches of the published-result database for the source title, derivative-inverse expression, convex vaccination equilibrium bounds, and equivalent formulations returned no result stating this correction or the replacement enclosure.

## Limitations

The result is a theorem-level correction for the one-dimensional convex regime, not a new epidemiological calibration and not a claim about the paper's nonconvex multi-equilibrium examples. The bound \(U\) uses the initial slope \(\pi'(0)\); when it exceeds \(p_*\), the simpler endpoint bound \(P_0<p_*\) is stronger. The implicit bound \(\bar P\) is always valid under the stated assumptions and can be tighter than \(U\).

No independent audit has been performed.

## References

1. N. A. Balabanova and M. H. Duong, “Adaptive dynamics for individual payoff game-theoretic models of vaccination,” arXiv:2411.09519, first public 2024-11-14; Journal of Dynamics and Games, DOI: 10.3934/jdg.2025037.
2. C. T. Bauch and D. J. D. Earn, “Vaccination and the theory of games,” Proceedings of the National Academy of Sciences 101 (2004), 13391–13394, DOI: 10.1073/pnas.0403823101.

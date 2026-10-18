# An exact exchange-cycle window for two repulsive full-attention tokens

## Finding

For every dimension \(d\ge 2\) and softmax sharpness \(0<\kappa\le 1/3\), the two-token, self-inclusive, normalized negative-value attention map defined below has a complete global phase diagram on noncollinear initial configurations. Its two sharp relaxation transitions occur at
\[
\eta_{\mathrm a}=\frac{2}{1+\tanh\kappa},\qquad \eta_{\mathrm c}=2.
\]
For \(0<\eta\le\eta_{\mathrm a}\), every noncollinear pair approaches an antipodal *fixed* pair (at \(\eta=1\), in one step). For \(\eta_{\mathrm a}<\eta<2\), every noncollinear pair approaches a prime period-two **exchange orbit** with limiting correlation
\[
c_*(\eta,\kappa)=1-\frac{2}{\kappa}\operatorname{arctanh}\left(\frac2\eta-1\right).
\]
At \(\eta=2\), the two tokens approach a common vector but alternate its sign on successive steps. Both boundary values have universal algebraic rates for every noncollinear initial pair:
\[
\lim_{n\to\infty}n\bigl(1+x_{1,n}\cdot x_{2,n}\bigr)=\frac{1}{2\kappa(1+\tanh\kappa)}\quad(\eta=\eta_{\mathrm a}),
\]
\[
\lim_{n\to\infty}n\bigl(1-x_{1,n}\cdot x_{2,n}\bigr)=\frac{1}{2\kappa}\quad(\eta=2).
\]
The interior exchange orbit is exponentially attracting in the relative-angle coordinate, and the two critical boundaries are only algebraically attracting. There are no additional periodic points beyond these exchange two-cycles, the antipodal fixed pairs, and the exceptional fixed or sign-flipping consensus pairs classified below.

## Assumptions and scope

Let \(d\ge2\), \(0<\kappa\le 1/3\), and \(0<\eta\le2\). Two unit vectors \(x_1,x_2\in S^{d-1}\) evolve by **full self-attention**, including the two diagonal attention entries:
\[
A_{ij}(x_1,x_2)=\frac{\exp(\kappa x_i\cdot x_j)}{\exp(\kappa x_i\cdot x_1)+\exp(\kappa x_i\cdot x_2)},
\qquad
x_i^+=\frac{x_i-\eta\sum_{j=1}^{2}A_{ij}x_j}{\left\|x_i-\eta\sum_{j=1}^{2}A_{ij}x_j\right\|}.
\]
This is the normalized residual attention rule with identity query and key, and value matrix \(-I\). Its normalization is the Euclidean norm of each token separately. The map is well defined for all pairs unless \(\eta=1\) and \(x_1=x_2\), where both numerators vanish. Claims of attraction concern **noncollinear pairs**, \(-1<x_1\cdot x_2<1\); the excluded endpoints are classified separately. The parameter \(\eta=0\), higher token counts, masked-out self-attention, and \(\kappa>1/3\) are not covered by the global phase classification.

At consensus \(x_1=x_2=x\), the pair is fixed when \(\eta<1\), undefined when \(\eta=1\), and alternates exactly between \((x,x)\) and \((-x,-x)\) when \(\eta>1\). At antipodality \(x_1=-x_2\), the pair is fixed for the entire claimed parameter range. These endpoint solutions are exceptional and are not included in the universal asymptotic-rate assertions.

## Proof

**Exact two-mode reduction.** Given a noncollinear pair, put
\[
c=x_1\cdot x_2,\quad t=\frac{1-c}{1+c}>0,\quad U=\frac{x_1+x_2}{\|x_1+x_2\|},\quad V=\frac{x_1-x_2}{\|x_1-x_2\|}.
\]
Because both tokens have unit norm, \(U\perp V\), and
\[
x_1=\frac{U+\sqrt t\,V}{\sqrt{1+t}},\qquad x_2=\frac{U-\sqrt t\,V}{\sqrt{1+t}}.
\]
Writing \(a=A_{11}=A_{22}\), \(b=A_{12}=A_{21}\), gives \(a+b=1\) and
\[
a-b=\tanh\left(\frac{\kappa(1-c)}2\right)=\tanh\left(\frac{\kappa t}{1+t}\right)=:\tau(t).
\]
The unnormalized outputs, in the orthogonal basis \((U,V)\), are
\[
y_1=\frac{(1-\eta)U+(1-\eta\tau(t))\sqrt t\,V}{\sqrt{1+t}},\qquad
y_2=\frac{(1-\eta)U-(1-\eta\tau(t))\sqrt t\,V}{\sqrt{1+t}}.
\]
They have equal positive norm. For all stated parameters, \(0<\tau(t)<\tanh\kappa<1/3\), so \(1-\eta\tau(t)>0\). The \(V\)-direction never changes sign, and the \(U\)-direction changes sign at each step exactly when \(\eta>1\). When \(\eta\ne1\), the complete relative dynamics is the scalar recurrence
\[
t_{n+1}=G(t_n):=t_n\left(\frac{1-\eta\tau(t_n)}{|1-\eta|}\right)^2.
\]
When \(\eta=1\), the \(U\)-component disappears in one step and the pair becomes antipodal.

**Monotonicity in the nontrivial step range.** For \(1<\eta\le2\), differentiate \(G\):
\[
G'(t)=\left(\frac{1-\eta\tau(t)}{\eta-1}\right)^2\left(1-\frac{2\eta t\tau'(t)}{1-\eta\tau(t)}\right).
\]
Here \(t\tau'(t)=\kappa t(1+t)^{-2}\operatorname{sech}^2(\kappa t/(1+t))\le\kappa/4\), hence \(2\eta t\tau'(t)\le\kappa\). On the other hand,
\[
1-\eta\tau(t)>1-2\tanh\kappa>1-2\kappa\ge\kappa
\]
for \(\kappa\le1/3\). Thus \(G'(t)>0\) on \((0,\infty)\), including at both endpoints of the specified sharpness range. Also \(\tau(t)\) increases strictly from \(0\) to \(\tanh\kappa\).

**Global alternatives and exact cycles.** For \(0<\eta<1\), the factor in \(G(t)/t\) is strictly greater than one, so every positive \(t_n\) increases without bound. The case \(\eta=1\) was resolved exactly above. For \(1<\eta<\eta_{\mathrm a}\), the factor is again greater than one at every finite \(t\); for \(\eta=\eta_{\mathrm a}\) it is greater than one at every finite \(t\) and tends to one at infinity. Thus all these sequences tend to infinity and \(c_n=(1-t_n)/(1+t_n)\to-1\).

For \(\eta_{\mathrm a}<\eta<2\), \(G(t)/t\) decreases strictly through one at the unique \(t_*>0\) satisfying \(\tau(t_*)=2/\eta-1\). Equivalently,
\[
t_*=\frac{u_*}{\kappa-u_*},\qquad u_*=\operatorname{arctanh}(2/\eta-1).
\]
Strict monotonicity of \(G\) shows that an iterate initially below \(t_*\) increases but cannot overshoot it, while an iterate above it decreases without crossing. Both sequences converge to \(t_*\). At this fixed relative angle, \(U\) flips and \(V\) does not, so each labeled pair undergoes the exact prime two-cycle \((x_1,x_2)\mapsto(-x_2,-x_1)\mapsto(x_1,x_2)\). The same sign rule and convergence of \(t_n\) establish convergence of the full original token vectors along their even and odd subsequences, not just convergence of the correlation. Moreover \(0<G'(t_*)<1\), giving exponential relative-angle convergence. At \(\eta=2\), \(G(t)/t=(1-2\tau(t))^2<1\), so \(t_n\downarrow0\); the \(U\)-direction flips, resulting in a consensus sign-flip two-cycle. Since \(G\) is strictly increasing, it has no nontrivial scalar cycles; with the fixed \(U,V\) directions, this proves the stated periodic-point classification.

**Critical asymptotic constants.** At \(\eta=\eta_{\mathrm a}\) and \(t\to\infty\), with \(s=\tanh\kappa\),
\[
\tau(t)=s-\frac{\kappa(1-s^2)}{t}+O(t^{-2}),\qquad
G(t)-t=4\kappa(1+s)+O(t^{-1}).
\]
Since \(t_n\to\infty\), Stolz--Cesaro (or averaging increments) yields \(t_n/n\to4\kappa(1+s)\), and \(1+c_n=2/(1+t_n)\) gives the first critical law. At \(\eta=2\), expansion as \(t\to0\) gives
\[
G(t)=t-4\kappa t^2+O(t^3),\qquad \frac1{G(t)}-\frac1t=4\kappa+O(t).
\]
Thus \(1/(n t_n)\to4\kappa\), and \(1-c_n=2t_n/(1+t_n)\) gives the second critical law. Every step uses exact identities or controlled asymptotics; no finite computation is substituted for an infinite argument.

## Verification

The standalone `verify.py` recomputes the two-token update independently from softmax weights, checks the exact scalar conjugacy on deterministic sample pairs in several ambient dimensions, checks the stepwise exchange identity, tests monotonicity and the analytic limiting angle, and numerically probes both critical coefficients. It uses Python's standard library only. These finite tests are diagnostics; the proof above establishes the quantifiers over all permitted dimensions, parameters and noncollinear initial configurations.

## Relationship to prior work

Altafini's *Asymptotic Analysis of Discrete-Time Self-Attention Dynamics in Transformers* (2026, arXiv:2610.13518v1), Section II Eq. (1), studies the **self-inclusive** normalized residual attention system but works principally under a value-matrix hypothesis with a positive simple top eigenvalue. The present result fixes \(V=-I\), violating that hypothesis, and completely classifies the repulsive two-token dynamics including its exact thresholds, exchange-periodic attractor and critical rates. The existing full-attention identity-value two-token metastability result concerns attractive feedback and does not imply the negative-value bifurcations.

Gao, Yang and Chen's *Nonequilibrium Phases of Repulsive Self-Attention* (2026, arXiv:2609.28448v1), Sections II and III and its appendices, analyze \(V=-I\) but explicitly **remove diagonal attention entries**, so that with two tokens each row routes to the other token with probability one. Its repulsive phase results therefore do not determine the softmax-sharpness-dependent two-token thresholds proved here. The source treats larger token counts, regular polygons and many-body behavior. General normalized-map, projective-dynamics, and flip-bifurcation results remain potential sources of an equivalent indirect formulation.

## Limitations

The phase diagram is for exactly two tokens, includes diagonal self-attention, and assumes an isotropic negative value map with \(0<\kappa\le1/3\) and \(0<\eta\le2\). The sufficient sharpness range is not claimed optimal. The two step-size thresholds are exact within this range. For stronger softmax sharpness, the scalar map can develop folds and other behavior; none of that is classified here. A mathematical benchmark does not by itself predict training or inference behavior in realistic transformers. The fixed/periodic exceptional endpoint pairs and the undefined consensus point at \(\eta=1\) have been listed explicitly. No independent audit has been performed.

## References

1. C. Altafini, *Asymptotic Analysis of Discrete-Time Self-Attention Dynamics in Transformers*, arXiv:2610.13518v1, submitted 2026-10-09; full HTML, especially Sections II, IV and V.
2. Q. Gao, Z. Yang and X. Chen, *Nonequilibrium Phases of Repulsive Self-Attention: Chaos, Attention Condensation, and Emergent Locality*, arXiv:2609.28448v1, submitted 2026-09-23; full preprint, especially the diagonal-masking convention in Section II.
3. C. Altafini, *Multistability of Self-Attention Dynamics in Transformers*, arXiv:2511.11553v1, submitted 2025-11-14; continuous-time positive-eigenvalue comparison.

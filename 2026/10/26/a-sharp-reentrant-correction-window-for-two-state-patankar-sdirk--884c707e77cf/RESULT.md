# A sharp reentrant correction window for two-state Patankar SDIRK21

## Finding

Consider the two-species conservative exchange equation \(y'=Qy\), with
\[
Q=\begin{pmatrix}-a&b\\a&-b\end{pmatrix},\qquad a,b>0,
\]
and initial mass-one state \(y_0=(x,1-x)^{\mathsf T}\), \(0\le x\le1\). Apply the classical L-stable, stiffly accurate two-stage SDIRK21 method, followed by the **final-stage-only** positivity correction of Nurkhametova et al. (2026), their equations (21) and (25). The componentwise Patankar-weight denominator is floored at \(\varepsilon>0\).

Let \(x^+_\varepsilon\) be the first component after this corrected step and write
\[
\gamma=1-1/\sqrt2,\quad s=h(a+b),\quad \pi=\frac{b}{a+b},\quad
R(s)=\frac{1+(2\gamma-1)s}{(1+\gamma s)^2}.
\]
For **every** \(a,b,h>0\) and \(x\in[0,1]\), at fixed \(a,b,h,x\) the singular-floor limit is exactly
\[
\boxed{\lim_{\varepsilon\downarrow0}x^+_\varepsilon
=\min\{1,\max\{0,\pi+R(s)(x-\pi)\}\}.}
\]
Thus the limiting positivity correction equals the **simplex projection of the two-state SDIRK predictor**, not necessarily the true continuous-time evolution. In each positive-floor step both components are strictly positive, sum to one, and solve the stated corrected linear system.

The phenomenon has an exact reentrant stiffness window for the natural pure-first-species start \(x=1\). Set
\[
\pi_\star=3-2\sqrt2,\qquad s_\star=4+3\sqrt2.
\]
The uncorrected first-component predictor is **negative for some positive step size** if and only if \(0<\pi<\pi_\star\). In that case, it is negative **exactly** for \(s_-<s<s_+\), where
\[
s_\pm=\frac{1-2\gamma-\pi\ \pm\
\sqrt{(1-2\gamma-\pi)^2-4\pi\gamma^2}}{2\pi\gamma^2}.
\]
Consequently \(x^+_\varepsilon\to0\) throughout this open interval, although the exact first component \(\pi+(1-\pi)e^{-s}\) is strictly greater than \(\pi\). At \(\pi=\pi_\star\), the negative interval collapses to the single zero-predictor point \(s=s_\star\); for \(\pi>\pi_\star\) no negative predictor occurs from \(x=1\).

For an exact numerical witness take \(a=9\), \(b=1\), \(h=4/5\), and \(x=1\), so \(s=8\), \(\pi=1/10\), and
\[
v=\frac{593-1152\sqrt2}{12005}<0,\qquad
\lim_{\varepsilon\downarrow0}x^+_\varepsilon=0,
\qquad x_{\rm exact}(h)=\frac1{10}+\frac9{10}e^{-8}>\frac1{10}.
\]
For sufficiently small \(\varepsilon\) the positive corrected output is \(O(\varepsilon)\), so the one-step error has a nonzero limit even as the denominator floor vanishes. This is a **fixed-step** statement, not a claim about timestep refinement or long-run numerical stationary distributions.

## Assumptions and scope

Everything is in exact arithmetic. The reaction rates \(a,b\), timestep \(h\), and cutoff \(\varepsilon\) are strictly positive and finite; \(x\) lies in the closed unit interval. The generator \(Q\) has nonnegative off-diagonal entries and zero column sums. The method's two-stage Butcher matrix has entries \(A_{11}=A_{22}=\gamma\), \(A_{21}=1-\gamma\), \(A_{12}=0\), and weights \((1-\gamma,\gamma)\). Only the **last** output is corrected: the predictor stages themselves are the unmodified SDIRK stages. The source algorithm uses
\[
\Sigma_{Y/Z}=\operatorname{diag}_i
\left(\frac{\max(Y_i,0)}{\max(Z_i,\varepsilon)}\right),\qquad
\bar Q=\sum_{j=1}^{2}b_j\,Q\Sigma_{Y_j/Y_2},\quad
 y^+_\varepsilon=(I-h\bar Q)^{-1}y_0.
\]
Because \(Q\) is constant, stage-argument clipping inside \(Q\) has no effect, while clipping inside the ratio is essential. Do not substitute the all-stage correction from the source paper for this last-stage-only algorithm.

## Proof

**1. The two predictor stages.** Conservation implies each stage is determined by its first component. Writing \(u=(Y_1)_1\) and \(v=(Y_2)_1\), direct solution of the SDIRK equations gives
\[
u=\pi+\frac{x-\pi}{1+\gamma s},\qquad
v=\pi+\frac{1+(2\gamma-1)s}{(1+\gamma s)^2}(x-\pi).
\]
Since \(a,b,h>0\), \(0<\pi<1\), \(1+\gamma s>1\), and \(x\in[0,1]\), the first stage satisfies \(0<u<1\), including both endpoint initial states.

**2. Exact reduction of the corrector.** Its averaged generator has the form
\[
\bar Q=\begin{pmatrix}-aL&bM\\aL&-bM\end{pmatrix}
\]
with nonnegative weights
\[
L=(1-\gamma)\frac{u}{\max(v,\varepsilon)}
 +\gamma\frac{\max(v,0)}{\max(v,\varepsilon)},\quad
M=(1-\gamma)\frac{1-u}{\max(1-v,\varepsilon)}
 +\gamma\frac{\max(1-v,0)}{\max(1-v,\varepsilon)}.
\]
For any positive cutoff, \(L,M>0\) since the stage-one components are strictly positive. Inverting the two-by-two matrix yields
\[
\boxed{x^+_\varepsilon=
\frac{x+hbM}{1+h(aL+bM)}.}
\]
The other component is \(1-x^+_\varepsilon\); both are strictly between zero and one. This also proves exact conservation and positivity without appealing to computational experiments.

**3. The singular-floor limit.** If \(0<v<1\), for every sufficiently small \(\varepsilon\), all the ratios are ordinary ratios. Then \(\bar QY_2=\sum_jb_jQY_j\), so the unmodified predictor \(Y_2\) satisfies the corrected equation and is the unique output: \(x^+_\varepsilon=v\). If \(v\le0\), the weight \(L=(1-\gamma)u/\varepsilon\to+\infty\), whereas \(M\) remains finite and positive; hence \(x^+_\varepsilon\to0\). If \(v\ge1\), \(M=(1-\gamma)(1-u)/\varepsilon\to+\infty\) while \(L\) remains finite and positive; hence \(x^+_\varepsilon\to1\). These three cases include the two boundary equalities and establish the asserted pointwise limit for the full simplex.

**4. Sharp phase diagram.** For \(x=1\), put \(v(s)=\pi+(1-\pi)R(s)\). Differentiate:
\[
R'(s)=\frac{-1+(1-2\gamma)\gamma s}{(1+\gamma s)^3}.
\]
The unique positive critical point is \(s_\star=1/[\gamma(1-2\gamma)]=4+3\sqrt2\), and
\[
R(s_\star)=\frac{1-\sqrt2}{2},\quad R(0)=1,
\quad\lim_{s\to\infty}R(s)=0^-.
\]
Thus \(v(s)<0\) for some \(s>0\) precisely if \(\pi+(1-\pi)(1-\sqrt2)/2<0\), equivalent to \(\pi<3-2\sqrt2\). Since \(1+\gamma s>0\), the inequality \(v(s)<0\) is equivalent to
\[
\pi\gamma^2s^2+(\pi+2\gamma-1)s+1<0.
\]
For \(0<\pi<\pi_\star\), the quadratic has two distinct positive roots \(s_\pm\) displayed in the finding, and its negative set is exactly their open interval. At equality the roots coalesce; beyond it there is no negative set. The exact solution follows by solving the scalar relaxation equation \(x'=b-(a+b)x\). The explicit algebraic witness follows by substituting \(s=8\) and \(\pi=1/10\). No infinite theorem is deduced from finite tests.

**5. First-order boundary layer (additional quantitative consequence).** For a fixed configuration with \(v<0\), for sufficiently small \(\varepsilon\),
\[
\lim_{\varepsilon\downarrow0}\frac{x^+_\varepsilon}{\varepsilon}
=\frac{x+hb\left[(1-\gamma)(1-u)/(1-v)+\gamma\right]}{ha(1-\gamma)u}.
\]
This strictly positive constant quantifies the sharp \(O(\varepsilon)\) descent of the corrected first component to the wrong simplex face.

## Verification

The included standalone `verify.py` constructs both predictor stages by independent two-by-two matrix inversions and the corrected generator by explicit column scaling, separately evaluates the scalar closed forms, and checks positivity, conservation, the critical rate ratio, the exact example, and the predicted boundary-layer coefficient. It passed **9,020 deterministic numerical assertions**. The exact inequalities and all-parameter quantifiers are proven above; finite checks are ancillary.

To rerun, extract `verify.py` from this finding's embedded package and execute `python verify.py` in an environment with Python 3 and the standard library. No external datasets or internet connections are required.

## Relationship to prior work

Nurkhametova, Gomillion, Subrahmanya and Sandu (2026), arXiv:2602.15271, define the final-stage predictor-corrector with the denominator cutoff in equations (21) and (25), and analyze positivity/conservation and small-step order. Those are imported definitions and known structural guarantees, not new claims here. Their Section 4.2.1 specifies the SDIRK21 tableau. The present result instead proves the **exact full-simplex vanishing-cutoff map at a fixed (possibly stiff) step**, its sharp reversible-exchange rate-ratio window, and its first-order boundary layer. Neither a general statement of positivity nor an ordinary small-step order estimate implies this fixed-step discontinuous limit.

Torlo, Öffner and Ranocha (2022), arXiv:2108.07347, analyze oscillations and loss of order for earlier modified Patankar families on two-state exchange systems. Their full article (Sections 2–5) concerns different discretizations and does not establish this 2026 SDIRK21 correction map. More generally, a fixed-positive-cutoff **timestep-refinement limit** asks a distinct question: an \(h\downarrow0\) statement cannot decide the present \(\varepsilon\downarrow0\) behavior at fixed \(h\).

## Limitations

The result covers only linear two-state conservative exchange, classical SDIRK21, and final-stage-only correction. It does not treat source algorithms correcting every stage, higher-dimensional kinetics, nonlinear matrices \(G(y)\), finite precision, global-in-time convergence, or adaptive step selection. The width and location of the negative interval are about the *unmodified predictor*; the corrected output is positive for every cutoff. The original source's convergence-order theorem applies in its small-step regime and is not contradicted. A complete historical-priority assessment of all modified Patankar variants remains an outstanding external check.

## References

1. K. Nurkhametova, R. J. Gomillion, A. N. Subrahmanya and A. Sandu, *A Patankar predictor-corrector approach for positivity-preserving time integration*, arXiv:2602.15271 (first public version 2026-02-17), equations (21), (25), and Section 4.2.1. https://arxiv.org/abs/2602.15271
2. D. Torlo, P. Öffner and H. Ranocha, *Issues with Positivity-Preserving Patankar-type Schemes*, arXiv:2108.07347 (first public version 2021-08-16; revised 2022), especially Sections 2–5. https://arxiv.org/abs/2108.07347

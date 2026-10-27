# Catalan first-return law and critical crossover for a Fibonacci-map Markov model

## Finding

The auxiliary affine Markov model used in the study of piecewise-linear Fibonacci bimodal dynamics has an **exact, all-time return law** to its distinguished finite core, including a square-root critical tail and an explicit critical-window scaling profile.

Write \(C_m=\frac{1}{m+1}\binom{2m}{m}\). For the normalized Lebesgue initial distribution on the core described below, define
\[
A(\lambda)=\frac{\lambda^4+\lambda^6-2\lambda^7}{1-\lambda^4},\qquad
\beta(\lambda)=\frac{A(\lambda)}{\lambda}.
\]
The first-return time \(\tau\) obeys, for every \(0<\lambda<1\),
\[
\Pr_\lambda(\tau=1)=1-A(\lambda),\qquad
\Pr_\lambda(\tau=n)=\beta(\lambda)C_{n-1}\lambda^{n-1}(1-\lambda)^n\quad(n\ge2).
\]
The probability of no return is
\[
\Pr_\lambda(\tau=\infty)=
\begin{cases}0,&0<\lambda\le\frac12,\\
A(\lambda)(2\lambda-1)/\lambda^2,&\frac12<\lambda<1.
\end{cases}
\]
For \(\lambda<1/2\), \(\mathbb E_\lambda[\tau]=1+A(\lambda)/(1-2\lambda)\); at \(\lambda=1/2\) this mean is infinite. Exactly at criticality,
\[
\Pr_{1/2}(\tau>n)=\frac{2}{15}\frac{\binom{2n}{n}}{4^n},\qquad n\ge1.
\]
Moreover, for any fixed \(u\in\mathbb R\) and \(\lambda_n=\frac12+\frac{u}{2\sqrt n}\in(0,1)\),
\[
\boxed{\lim_{n\to\infty}\sqrt n\,\Pr_{\lambda_n}(\tau>n)
=\frac{2}{15}\left(\frac{e^{-u^2}}{\sqrt\pi}+u(1+\operatorname{erf}(u))\right).}
\]

## Assumptions and scope

Fix a real \(\lambda\in(0,1)\). Set \(V_j=(\lambda^j,\lambda^{j-1}]\) for \(j\ge1\). The **auxiliary map** \(T_\lambda:(0,1]\to(0,1]\) introduced by Ji and Ma is the affine map
\[
T_\lambda(x)=\frac{x-\lambda^j}{d_j}\qquad(x\in V_j),\quad
 d_j=\begin{cases}
1-\lambda,&j=1,\\
\lambda(1-\lambda),&j=2,\\
\lambda^2(1-\lambda),&j=3,4,\\
\lambda(1-\lambda),&j\ge5.
\end{cases}
\]
The branch images are, respectively, \((0,1]\) for \(j=1,2,3\), \((0,\lambda]\) for \(j=4\), and \((0,\lambda^{j-2}]\) for \(j\ge5\). The natural finite core is \(B=V_1\cup V_2\cup V_3\cup V_4=(\lambda^4,1]\): the transition law above level four is spatially homogeneous in the level index. The random starting point \(x\) has the law \(dx/(1-\lambda^4)\) restricted to \(B\). Define \(\tau=\inf\{n\ge1:T_\lambda^n(x)\in B\}\), with \(\inf\varnothing=\infty\). All probabilities and expectations here refer exclusively to this starting law, and the clock counts iterates of \(T_\lambda\).

## Proof

**1. Transition kernel and exit weight.** Because each branch is affine with constant nonzero slope, conditioning on a finite admissible level itinerary leaves a uniform distribution in the current level. Consequently the level indices form a Markov chain. Its transition probabilities from level \(j\) are
\[
\Pr(J_{t+1}=i\mid J_t=j)
=\begin{cases}(1-\lambda)\lambda^{i-L_j},&i\ge L_j,\\0,&i<L_j,
\end{cases}\qquad
L_j=\begin{cases}1,&1\le j\le3,\\2,&j=4,\\j-1,&j\ge5.\end{cases}
\]
In particular, after a one-step exit from \(B\), the index is \(5+K\), with \(\Pr(K=k)=(1-\lambda)\lambda^k\) for \(k\ge0\). The normalized initial core masses are \(w_j=(1-\lambda)\lambda^{j-1}/(1-\lambda^4)\). The one-step exit probability is
\[
A=\sum_{j=1}^4w_j\Pr(J_1\ge5\mid J_0=j)
=\frac{\lambda^4(1-\lambda^3)+\lambda^6(1-\lambda)}{1-\lambda^4}
=\frac{\lambda^4+\lambda^6-2\lambda^7}{1-\lambda^4}.
\]
All endpoints are null under these Lebesgue-based laws.

**2. Exact hitting-time series.** Above the core, one step reduces the level by one and then adds an independent geometrically distributed \(K\): the increment is \(K-1\). Because the walk cannot jump downward more than one, the first core state it reaches is level four. Let \(r(z)=\sum_{n\ge1}r_nz^n\) be the (possibly defective) generating function of the first hitting time of level four when starting from level five. The first step gives the functional equation
\[
r(z)=z\frac{1-\lambda}{1-\lambda r(z)}
\]
(the \(K\) successive one-level descents must all occur), with the solution analytic at the origin
\[
r(z)=\frac{1-\sqrt{1-4\lambda(1-\lambda)z}}{2\lambda}.
\]
The Catalan generating identity yields \(r_n=C_{n-1}\lambda^{n-1}(1-\lambda)^n\). With \(K\) geometric, the complete core first-return generating function is
\[
H(z)=z(1-A)+zA\sum_{k\ge0}(1-\lambda)\lambda^k r(z)^{k+1}
=z(1-A)+A r(z)^2
=\left(1-\frac A\lambda\right)z+\frac A\lambda r(z).
\]
The equality \(z\sum_{k\ge0}(1-\lambda)\lambda^kr^{k+1}=r^2\) follows from the defining equation of \(r\). The displayed finite-time law follows coefficient by coefficient.

**3. Recurrence, escape, and mean.** By the square-root formula, \(r(1)=1\) if \(\lambda\le1/2\) and \(r(1)=(1-\lambda)/\lambda\) otherwise. Thus \(1-H(1)=A(2\lambda-1)/\lambda^2\) in the latter regime and zero otherwise. For \(\lambda<1/2\), differentiation gives \(r'(1)=(1-\lambda)/(1-2\lambda)\), hence \(H'(1)=1+A/(1-2\lambda)\). At equality, the square-root singularity forces infinite first moment. When \(\lambda=1/2\), the exit weight is \(A=1/15\), \(A/\lambda=2/15\), and \(r(z)=1-\sqrt{1-z}\). The binomial identity \(\sum_{k>n}[z^k]r(z)=\binom{2n}{n}/4^n\) establishes the asserted **exact**, not merely asymptotic, critical survival law.

**4. Critical-window crossover.** For fixed \(u\in\mathbb R\) put \(\lambda_n=1/2+u/(2\sqrt n)\), so \(4\lambda_n(1-\lambda_n)=1-u^2/n\). The Catalan coefficients satisfy \(C_{k-1}\sim4^{k-1}/(\sqrt\pi k^{3/2})\). For \(k/n\) in a compact subset of \((0,\infty)\),
\[
n^{3/2}r_{\lambda_n,\lfloor nt\rfloor}\to \frac{e^{-u^2t}}{2\sqrt\pi\,t^{3/2}}.
\]
The universal bound \(r_{\lambda_n,k}\le Ck^{-3/2}\) for all large \(n\) and \(k\ge1\) (because \(4\lambda(1-\lambda)\le1\)) controls the tail uniformly. The Riemann-sum limit gives
\[
\sqrt n\sum_{k>n}r_{\lambda_n,k}\to\frac1{2\sqrt\pi}
\int_1^\infty t^{-3/2}e^{-u^2t}\,dt.
\]
The escape probability of the one-level descent is \(1-r_{\lambda_n}(1)=\max(0,(2\lambda_n-1)/\lambda_n)\), whose product by \(\sqrt n\) tends to \(2\max(u,0)\). Since \(A(\lambda_n)/\lambda_n\to2/15\), the exact identity
\[
\Pr_{\lambda_n}(\tau>n)=\frac{A(\lambda_n)}{\lambda_n}
\left(1-r_{\lambda_n}(1)+\sum_{k>n}r_{\lambda_n,k}\right)
\]
reduces the limit to elementary integration by parts:
\[
\frac1{2\sqrt\pi}\int_1^\infty t^{-3/2}e^{-u^2t}\,dt+2\max(u,0)
=\frac{e^{-u^2}}{\sqrt\pi}+u(1+\operatorname{erf}(u)).
\]
This proves the claimed crossover for all fixed real \(u\).

## Verification

Run `python3 verify_return.py` with Python's standard library. It directly intersects exact rational affine branch images with partition intervals and recursively enumerates finite-length core returns, rather than assuming the Catalan representation. It tests five rational parameters, eleven return lengths, forty exact central-binomial tail cases at criticality, and fifteen numerical critical-window comparisons. In the packaged version the script reports 934 successful assertions. These finite calculations corroborate but do not replace the infinite proof.

## Relationship to prior work

Ji and Ma [1, section 5.1 and Lemma 5.1] construct \(T_\lambda\), establish its transition matrix, and analyze invariant-measure and conservative/dissipative phase behavior. They do not state an all-time first-return distribution to the core \((\lambda^4,1]\), the exact critical central-binomial tail, or the parameter-dependent finite-time crossover. Their own text states \(T_\lambda\) is **not semiconjugate** to their induced map \(F_\lambda\); thus this finding is restricted to their auxiliary model. Classical first-passage and branching-process methods [2] account for why the square-root Catalan kernel is tractable, but their bounded-jump models are not this affine map and do not supply the core exit weight or this crossover. Branching survival near criticality [3] describes survival across *generations*, whereas the present observable is total first-passage *steps*. The quantitative distinction is essential: the present window has scale \(n^{-1/2}\) and the tail is of order \(n^{-1/2}\) at criticality.

## Limitations

The result does not assert return times, physical-time mixing, or wild-attractor statistics for the original Fibonacci bimodal system \(f_\lambda\) or induced map \(F_\lambda\). No distributional limit for conditioned long excursions, optimal uniform-in-\(u\) remainder, or finite-time asymptotics outside the stated fixed-\(u\) window is proved. Classical random-walk enumeration is not claimed new. Novelty of this **map-specific identification and exact crossover** is assessed against inspected accessible sources, not guaranteed against all unindexed literature.

## References

[1] H. Ji and W. Ma, *Phase transition for piecewise linear fibonacci bimodal map*, AIMS Mathematics 8 (2023), 8403–8430, doi:10.3934/math.2023424, published 2023-02-03. Full text: https://www.aimspress.com/aimspress-data/math/2023/4/PDF/math-08-04-424.pdf.

[2] H. Wang, *On total progeny of multitype Galton-Watson process and the first passage time of random walk with bounded jumps*, arXiv:1209.6429 (2012), https://arxiv.org/pdf/1209.6429.

[3] J. Garcia-Millan, F. Font-Clos and A. Corral, *Finite-size scaling of survival probability in branching processes*, arXiv:1411.2817 (2014), https://arxiv.org/pdf/1411.2817.

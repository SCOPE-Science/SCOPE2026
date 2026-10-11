# Exact mean-sensitive exponential Bellman function for dyadic lower oscillation

## Finding

Let \(\mathcal D\) be the standard binary dyadic subintervals of \(I_0=(0,1)\). For real-valued \(f\in L^1(I_0)\), put
\[
 B(f)=\sup_{J\in\mathcal D}\left(\langle f\rangle_J-\operatorname{ess\,inf}_J f\right),
 \qquad \langle f\rangle_J=\frac1{|J|}\int_J f(t)\,dt.
\]
Fix \(0<\lambda<\log2\), assume \(0<B(f)<\infty\), and, for each \(J\in\mathcal D\), write \(a_J=(\langle f\rangle_J-\operatorname{ess\,inf}_J f)/B(f)\in[0,1]\). Then the **sharp local-mean-sensitive exponential estimate** is
\[
 \boxed{\quad
 \frac1{|J|}\int_J\exp\!\left(\lambda\frac{f(t)-\operatorname{ess\,inf}_J f}{B(f)}\right)dt
 \;\le\;1+a_J\frac{e^\lambda-1}{2-e^\lambda}.\quad}
\]
At the root, for **each** prescribed \(a\in[0,1]\), this right-hand side is the exact supremum over \(B(f)\le1\), \(\operatorname{ess\,inf}_{I_0}f=0\), and \(\langle f\rangle_{I_0}=a\). The complete boundary convention is
\[
 \boxed{\quad \mathcal B(\lambda,a)=
 \begin{cases}
  1+a\dfrac{e^\lambda-1}{2-e^\lambda},&0<\lambda<\log2,\\
  1,&\lambda\ge\log2,\ a=0,\\
  +\infty,&\lambda\ge\log2,\ 0<a\le1.
 \end{cases}\quad}
\]
Thus the optimal exponential-integrability threshold for binary dyadic bounded lower oscillation is exactly \(\log2\). This is a lower-centered estimate of the function itself, rather than an estimate of its dyadic maximal function.

## Assumptions and scope

The dyadic intervals are \((j2^{-n},(j+1)2^{-n})\) for integers \(n\ge0\) and \(0\le j<2^n\), with endpoints ignored as null sets. Essential infima are finite on such intervals when \(B(f)<\infty\) and \(f\in L^1\). At \(B(f)=0\) the function is essentially constant on \(I_0\), and the normalized inequality is read as the trivial value \(1\). The Bellman supremum uses all measurable integrable real functions with dyadic seminorm at most one, not the narrower class with constraints over arbitrary nondyadic intervals. The parameter \(a\) is a dimensionless local oscillation excess, not a free translation of the function.

## Proof

**1. The exact one-step envelope.** Scale so that \(B(f)\le1\). For a dyadic interval \(J\), let \(m_J=\operatorname{ess\,inf}_Jf\) and \(a_J=\langle f\rangle_J-m_J\in[0,1]\). Put \(q=e^\lambda\in(1,2)\) and \(C=(q-1)/(2-q)>0\). For a step function constant on sufficiently fine dyadic atoms, induct on the remaining tree depth to prove
\[
 \langle e^{\lambda(f-m_J)}\rangle_J\le1+Ca_J.
\]
At a terminal atom equality holds since \(a_J=0\). For the two children, relabel so that their essential infima are \(m_J\) and \(m_J+d\) with \(d\ge0\), and denote their own mean excesses by \(a_0,a_1\in[0,1]\). The parent relation is
\[
 a_J=\frac{a_0+a_1+d}{2}\le1,
 \quad 0\le d\le2,\quad a_1\le\min(1,2-d).
\]
By the inductive hypothesis the parent exponential mean is at most
\[
 \frac{1+Ca_0+q^d(1+Ca_1)}2.
\]
It remains to show \((q^d-1)(1+Ca_1)\le Cd\). If \(0\le d\le1\), convexity of \(t\mapsto q^t\) gives \(q^d-1\le(q-1)d\); moreover, \((q-1)(1+C)=C\). If \(1\le d\le2\), use \(a_1\le2-d\). The required estimate reduces algebraically to
\[
 q^{d-1}\bigl(1-(q-1)(d-1)\bigr)\le1.
\]
Writing \(t=d-1\in[0,1]\), this follows from \(\log q\le q-1\) and \(\log(1-u)\le-u\) at \(u=(q-1)t\in[0,1)\). This proves the dyadic two-child Bellman induction.

**2. Passage to arbitrary integrable functions.** Let \(f_N=\mathbb E[f\mid\mathcal D_N]\), the stepwise mean on the level-\(N\) dyadic partition. Then \(B(f_N)\le B(f)\): on every coarser dyadic interval \(J\), its mean is unchanged and its essential infimum cannot decrease; on every finer interval \(f_N\) is constant. Fix \(J\), and let \(m_{J,N}=\operatorname{ess\,inf}_Jf_N\). For sufficiently large \(N\), \(m_{J,N}\) is nonincreasing and bounded below by \(m_J\). Dyadic differentiation implies \(m_{J,N}\downarrow m_J\): for each \(\varepsilon>0\), the positive-measure set \(\{f<m_J+\varepsilon\}\cap J\) contains a differentiation point, whose conditional averages eventually fall below \(m_J+\varepsilon\). Consequently, \(f_N-m_{J,N}\to f-m_J\) almost everywhere on \(J\). The finite-tree bound, the inequality \(\langle f_N\rangle_J-m_{J,N}\le\langle f\rangle_J-m_J\), and Fatou's lemma prove the asserted estimate. Apply this to \(f/B(f)\) for the original normalization.

**3. Sharpness at every local mean excess.** On a dyadic interval \(H\), define the geometric staircase \(s_H\) to equal the integer \(k\ge0\) on the right-hand half of its \(k\)-fold iterated left child. Then
\[
 \operatorname{ess\,inf}_H s_H=0,\qquad
 \langle s_H\rangle_H=\sum_{k\ge0}k2^{-k-1}=1,
 \qquad B_H(s_H)=1.
\]
Indeed, every proper dyadic interval in \(H\) is either a constant-value shell or an iterated left child, where the normalized mean exceeds the local minimum by exactly one. The exponential mean is
\[
 \langle e^{\lambda s_H}\rangle_H
 =\sum_{k\ge0}2^{-k-1}e^{\lambda k}
 =\frac1{2-e^\lambda}\quad(0<\lambda<\log2),
\]
and diverges when \(\lambda\ge\log2\).

For any \(a\in(0,1)\), decompose \((0,a)\) into its countably many maximal dyadic subintervals \(H\), place a copy of \(s_H\) on each, and put zero elsewhere. Any dyadic interval is either contained in one staircase block (local excess at most one) or is a union of whole blocks and zero regions (mean at most one and minimum zero). Hence the resulting \(f\) satisfies \(B(f)=1\), \(m_{I_0}=0\), and \(\langle f\rangle_{I_0}=a\), while
\[
 \langle e^{\lambda f}\rangle_{I_0}=(1-a)+a\langle e^{\lambda s_H}\rangle_H
 =1+a\frac{e^\lambda-1}{2-e^\lambda}.
\]
For \(a=1\) take a single staircase on \(I_0\); for \(a=0\) take the zero function. If \(\lambda\ge\log2\) and \(a>0\), every active block already has infinite exponential integral. This establishes all sharpness and boundary assertions.

## Verification

The proof is analytic for arbitrary depth and arbitrary integrable \(f\). The accompanying `verify_dyadic_blo.py` independently enumerates small finite dyadic trees, numerically checks the exact child-envelope inequality across its two natural regimes, and computes finite geometric-staircase moments by exact rational arithmetic. The program is supplementary and does not replace the induction, dyadic differentiation, or infinite geometric-series argument.

## Relationship to prior work

Zhang, arXiv:2608.10892v1 (11 August 2026), proves sharp one-sided John–Nirenberg distribution constants for ordinary interval BLO and supplies a local-mean-dependent tail Bellman bound; that continuous-interval hypothesis is stricter than a fixed dyadic filtration, and no direct affine exponential Bellman law on dyadic trees is stated in its inspected sections. Osękowski (2014) already proves the exact scalar constant \(1/(2-e^\lambda)\) and threshold \(\log2\) for a **different observable**, the dyadic maximal function centered at the root mean, and uses a geometric staircase for sharpness. These already-known scalar constants, threshold, and staircase mechanism are not claimed as discoveries. Osękowski (2013) gives sharp bounds for mean-centered absolute oscillation in ordinary BLO. The distinct assertion here is the full sharp \(a\)-dependent value for the directly lower-centered function \(f-m_J\), including every \(0\le a\le1\).

## Limitations

This is for the binary dyadic one-dimensional filtration; no arbitrary-interval, higher-dimensional, or general nonbinary-tree extension is asserted. No classification of all equality cases is claimed. The exact maximal-operator constant and geometric staircase are historical ingredients rather than new claims. Although the available primary texts do not state the affine local-mean Bellman identity, closely related older sharp-inequality literature raises residual risk of an equivalent formulation, particularly the 1996 article available only by abstract; an independent audit remains outstanding.

## References

1. Chao Zhang, *Sharp constants in the one-sided John–Nirenberg inequality for functions of bounded lower oscillation*, arXiv:2608.10892v1, first submitted 11 August 2026. https://arxiv.org/abs/2608.10892
2. Adam Osękowski, *Maximal inequalities for functions of bounded lower oscillation*, Kyushu Journal of Mathematics 68 (2014), 297–305, DOI: 10.2206/kyushujm.68.297. https://www.jstage.jst.go.jp/article/kyushujm/68/2/68_297/_pdf
3. Adam Osękowski, *Sharp estimates for functions of bounded lower oscillation*, Bulletin of the Australian Mathematical Society 87 (2013), 68–81, DOI: 10.1017/S0004972712000226.
4. Antonia Passarelli di Napoli, *Sharp inequalities for BLO in one dimension*, Atti Seminario Matematico e Fisico Università di Modena 44 (1996), 465–477; abstract and bibliography inspected, complete text unavailable.

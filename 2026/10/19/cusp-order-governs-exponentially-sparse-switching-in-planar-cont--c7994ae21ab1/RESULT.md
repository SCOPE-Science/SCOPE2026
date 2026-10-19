# Cusp order governs exponentially sparse switching in planar contractions

## Finding
Consider a planar piecewise-affine contraction, switching across the power cusp \(y=x^p\). Although all positive-height trajectories visit the upper branch infinitely often, the visits become exponentially sparse. The exponent is determined exactly by the contact order of the switching curve, not by the contraction strength.

**Theorem.** Fix real \(p>1\) and \(0<\lambda<1\) such that \(\lambda<(1-\lambda)^p\). Let \(F:[0,1]^2\to[0,1]^2\), away from the curve \(y=x^p\), be defined by
\[
F(x,y)=\begin{cases}(\lambda x,\lambda y),&y<x^p,\\(1-\lambda x,\lambda y),&y>x^p.\end{cases}
\]
Take any \((x_0,y_0)\in[0,1]^2\) with \(y_0>0\) whose forward orbit never touches \(y=x^p\). List in increasing order the times \(\tau_0<\tau_1<\cdots\) at which \(y_{\tau_j}>x_{\tau_j}^p\). Then every \(\tau_j\) exists and, with \(R_p=p/(p-1)\), there is a constant \(C=C(p,\lambda,x_0,y_0)>0\) such that
\[
\tau_j=C R_p^j+O(1),\qquad
\lim_{j\to\infty}\frac{\tau_{j+1}}{\tau_j}=R_p,\qquad
\#\{0\le n\le T:y_n>x_n^p\}=\frac{\log T}{\log R_p}+O(1)
\]
as \(j,T\to\infty\), respectively. The constants in the error terms may depend on the initial point and parameters, but not on \(j\) or \(T\).

For the **original parabolic switch** \(p=2\), an additional exact arithmetic rigidity holds: for all sufficiently large \(j\),
\[
\boxed{\tau_{j+1}=2\tau_j+2+\left\lceil\log_{1/\lambda}(1/y_0)\right\rceil.}
\]
Thus the successive switching times eventually form a geometric progression after one fixed translation. The integer offset depends on initial height but not on the initial horizontal coordinate.

## Assumptions and scope
The upper branch means the strict region \(y>x^p\), and the lower branch means \(y<x^p\). The map need not be specified on the switching curve: all statements exclude trajectories hitting that curve. Boundary points of the square away from the curve are included. No invariant measure or genericity assumption is imposed. The bound \(\lambda<(1-\lambda)^p\) ensures that every upper-branch point maps strictly into the lower branch; no statement is made for parameters beyond this sufficient separation regime. The limit coefficient \(C\) need not be universal.

## Proof
Put \(q=1/\lambda>1\). Since \(F\) multiplies the second coordinate by \(\lambda\) on both pieces, \(y_n=\lambda^n y_0>0\) for every \(n\).

**1. Visits exist and are isolated.** If \((x,y)\) is in the upper region, its image has horizontal coordinate \(1-\lambda x\ge1-\lambda\) and vertical coordinate \(\lambda y\le\lambda<(1-\lambda)^p\). Hence its image is strictly in the lower region. Conversely, a point in the lower region with positive height cannot stay there indefinitely: while it remains below the curve, the ratio \(y/x^p\) is multiplied at each step by \(\lambda^{1-p}>1\). The horizontal coordinate is necessarily positive in that region. Therefore another upper-region visit occurs in finite time. Repeating gives an infinite increasing sequence \(\tau_j\), with \(\tau_{j+1}\ge\tau_j+2\) and \(\tau_j\to\infty\).

**2. Exact first-return equation.** Set \(a_j=1-\lambda x_{\tau_j}\). Immediately after the \(j\)-th upper visit the state is \((a_j,\lambda^{\tau_j+1}y_0)\); it then undergoes consecutive lower-branch contractions until the next upper visit. After \(m\ge0\) such contractions the putative state is
\[
(\lambda^m a_j,\lambda^{\tau_j+1+m}y_0).
\]
The inequality for entering the upper branch is equivalent to
\[
(p-1)m>\tau_j+1+\log_q(a_j^p/y_0).
\]
The right-hand threshold is positive, since the state immediately after the upper visit lies strictly below the switch. The no-boundary hypothesis excludes equality at integer \(m\). Consequently the first such integer is \(m_j=1+\lfloor[\tau_j+1+\log_q(a_j^p/y_0)]/(p-1)\rfloor\). Thus
\[
\tag{1}\tau_{j+1}=\tau_j+2+\left\lfloor\frac{\tau_j+1+\log_q(a_j^p/y_0)}{p-1}\right\rfloor.
\]
This is an exact formula, not an asymptotic approximation.

**3. Uniformly bounded return error.** As \(0\le x_{\tau_j}\le1\), we have \(1-\lambda\le a_j\le1\). Hence \(\log_q(a_j^p/y_0)\) lies in a fixed bounded interval. The identity (1) implies
\[
\tag{2}\tau_{j+1}=R_p\tau_j+e_j,\quad |e_j|\le K
\]
for some finite \(K\) depending only on the parameters and \(y_0\). In particular \(\tau_{j+1}/\tau_j\to R_p\).

**4. Sharp exponential growth and frequency.** Define \(w_j=\tau_j/R_p^j\). Equation (2) gives \(w_{j+1}-w_j=e_j/R_p^{j+1}\), a summable series. Thus \(w_j\to C\ge0\). To prove strict positivity, select \(J\) so large that \(\tau_J>K/(R_p-1)\), possible since \(\tau_j\to\infty\). For every \(k\ge0\), the lower estimate in (2) yields
\[
\frac{\tau_{J+k}}{R_p^k}\ge\tau_J-\frac{K}{R_p-1}>0,
\]
so \(C>0\). Summing the tail of the series for \(w_j\) gives \(|\tau_j-CR_p^j|\le K/(R_p-1)\). Inverting the resulting increasing sequence establishes the visit-count formula with an additive bounded error.

**5. Exact eventual recurrence at \(p=2\).** In the upper region \(x_{\tau_j}^2<y_{\tau_j}=\lambda^{\tau_j}y_0\), so \(x_{\tau_j}\to0\). For all \(j\ge1\), \(x_{\tau_j}>0\), because an upper visit is followed by a reset to positive horizontal coordinate. Hence \(a_j<1\) and \(a_j\to1\). Put \(c=\log_q(1/y_0)\) and \(c_j=\log_q(a_j^2/y_0)\). Then \(c_j<c\) and \(c_j\to c\), which forces \(\lfloor c_j\rfloor=\lceil c\rceil-1\) for every sufficiently large \(j\), including when \(c\) is an integer. Setting \(p=2\) in (1) and using that \(\tau_j\) is integral gives \(\tau_{j+1}=2\tau_j+3+\lfloor c_j\rfloor=2\tau_j+2+\lceil c\rceil\), as claimed. \(\square\)

## Verification
The standalone Python checker `verify.py` tests exact rational trajectories for \(p=2\), including logarithmic-height resonance cases where \(\log_q(1/y_0)\) is an integer. It also tests logarithmic-coordinate trajectories for several other powers, comparing late switching-time ratios with \(R_p\). These are falsification tests only: the infinite-time statements follow from the analytical inequalities and recurrence above.

To run: `python3 verify.py`. The expected final line is `VERIFY_OK`. No nonstandard Python dependencies are needed.

## Relationship to prior work
Catsigeras, Guiraud, Meyroneinc and Ugalde (arXiv:1108.1501, first submitted August 6, 2011) construct the case \(p=2\) and prove a countably infinite limit set with stable ghost-orbit behavior (Example 4.2 and Proposition 4.2 in their revised manuscript). In particular, the existence of infinitely many upper-region visits and the attractor description are **not new**. The quantitative renormalization \(R_p=p/(p-1)\), logarithmic visit-count law, and eventual exact dyadic timing for the parabolic case are the distinct claims here. Existing general periodicity results for piecewise contractions away from discontinuities do not supply these exceptional-boundary time scales. The original work is used as motivation, not as a proof of the new quantitative estimates.

## Limitations
The theorem concerns specified piecewise-affine branches and a strict power-law switching boundary, not arbitrary piecewise contractions. It neither asserts invariant-measure properties nor classifies the full attractor for \(p\ne2\). Equality-hitting trajectories and the parameter endpoint are deliberately excluded. No independent external mathematical audit has been conducted, and an equivalent treatment in other switching-systems literature remains a bibliographic possibility.

## References
1. E. Catsigeras, P. Guiraud, A. Meyroneinc and E. Ugalde, *On the Asymptotic Properties of Piecewise Contracting Maps*, arXiv:1108.1501 (first version August 6, 2011; revised version April 1, 2014), especially Example 4.2 and Proposition 4.2. https://arxiv.org/abs/1108.1501
2. E. Catsigeras, P. Guiraud and A. Meyroneinc, *Complexity of injective piecewise contracting interval maps*, arXiv:1702.03599 (2017), for related one-dimensional symbolic-complexity questions with a different phase space. https://arxiv.org/abs/1702.03599
3. S. Jain and C. Liverani, *Piecewise Contractions*, arXiv:2404.02371 (2024), for generic periodicity and topological stability results, in contrast to the exceptional recurrent-switching regime here. https://arxiv.org/abs/2404.02371

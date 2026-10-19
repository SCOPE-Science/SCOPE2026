# Sharp near-vacuum Wigner-negativity asymptotic for an even Gaussian cat

## Finding
Let \(g(x)=\pi^{-1/4}e^{-x^2/2}\), and, for every \(a>0\), set
\[
\psi_a(x)=\frac{g(x-a)+g(x+a)}{\sqrt{2(1+e^{-a^2})}}.
\]
Use the Wigner convention
\[
W_a(q,p)=\frac1{2\pi}\int_{\mathbb R}\psi_a(q+y/2)\overline{\psi_a(q-y/2)}e^{-ipy}\,dy,
\qquad
\mathcal N(a)=\int_{\mathbb R^2}(-W_a(q,p))_+\,dq\,dp.
\]
Then the **integrated negative part** (not twice that integral) obeys the exact equivalent
\[
\boxed{\displaystyle
\mathcal N(a)\sim\frac{2^{7/4}e^{-1/2}}{\pi^3}\,a^{9/2}
\exp\!\left(-\frac{\pi^2}{4a^2}+\frac{\pi}{\sqrt2\,a}\right)
\quad(a\downarrow0).}
\]
In particular, \(\mathcal N(a)>0\) for every \(a>0\), but it vanishes faster than every power of \(a\) at the Gaussian limit. Both exponential scales, the fractional power, and the positive leading constant are determined.

## Assumptions and scope
All variables and integrals are real; \(a>0\) is the half-separation of the two oscillator-scale Gaussian packets in position coordinates. The Wigner convention has \(\hbar=1\) and \(\int_{\mathbb R^2}W_a=1\). The asymptotic concerns \(a\downarrow0\), without a momentum displacement or relative phase. The result is for the exact infinite-dimensional normalized coherent superposition, not a truncated Hermite expansion. The symbol \(\sim\) means that the ratio of the two positive quantities tends to one.

## Proof
**1. Exact Wigner formula and sign locus.** Gaussian integration and the overlap \(\langle g(\cdot-a),g(\cdot+a)\rangle=e^{-a^2}\) give
\[
W_a(q,p)=\frac{e^{-q^2-p^2}}{\pi(1+e^{-a^2})}
\left(e^{-a^2}\cosh(2aq)+\cos(2ap)\right).
\tag{1}
\]
Put \(E_a=e^{-a^2}\), \(\beta_a=\arccos(E_a)\), and
\[
t_a=\frac{\pi-\beta_a}{2a},\qquad
b_a=\frac{\pi+\beta_a}{2a}.
\]
Since \(0<E_a<1\) and \(\cosh\ge1\), the negative set can occur only in the disjoint momentum intervals
\[
\left(\frac{(2k+1)\pi-\beta_a}{2a},
\frac{(2k+1)\pi+\beta_a}{2a}\right),\qquad k=0,1,\ldots,
\]
and their reflections. In each interval, the admissible position coordinates satisfy
\(E_a\cosh(2aq)<-\cos(2ap)\). The closest positive lobe begins at \(p=t_a\); it is genuinely negative immediately to the right of \(t_a\) at \(q=0\), proving strict negativity for every \(a>0\).

**2. Negligibility of distant lobes.** The negative-set condition gives
\(\lvert q\rvert\le\operatorname{arcosh}(e^{a^2})/(2a)=O(1)\) as \(a\downarrow0\). The bracket in (1) has absolute value at most two wherever it is negative. Outside the two closest lobes \(\pm(t_a,b_a)\), every negative point has \(\lvert p\rvert\ge t_a+\pi/a\). Its contribution is therefore bounded by a fixed multiple of
\[
\int_{t_a+\pi/a}^{\infty}e^{-p^2}\,dp
=O\!\left(\frac{e^{-(t_a+\pi/a)^2}}{t_a+\pi/a}\right),
\]
which is \(o(a^2t_a^{-5/2}e^{-t_a^2})\). The two nearest lobes contribute equally by \(p\mapsto-p\).

**3. First-lobe blow-up.** In the positive nearest lobe write \(p=t_a+u\), with \(0<u<\beta_a/a\). Its negative bracket is
\[
B_a(q,u)=\cos(\beta_a-2au)-E_a\cosh(2aq).
\]
Introduce \(v=2t_au\) and \(w=\sqrt{2t_a}\,q\). Since
\(\beta_a/a\to\sqrt2\), \(t_a\to\infty\), and \(\sin\beta_a/a\to\sqrt2\), Taylor's formula, for each fixed \((v,w)\), gives
\[
\frac{t_a}{a^2} B_a\left(\frac{w}{\sqrt{2t_a}},\frac{v}{2t_a}\right)
\longrightarrow\sqrt2\,v-w^2.
\tag{2}
\]
Also
\[
\frac{e^{-q^2-p^2}}{e^{-t_a^2}}\longrightarrow e^{-v},
\qquad dq\,dp=(2t_a)^{-3/2}\,dw\,dv.
\]
Here the moving \(v\)-range tends to \((0,\infty)\). For completeness, the pointwise convergence can be integrated: for all sufficiently small \(a\) and all \(0<u<\beta_a/a\), the elementary estimate
\[
0<B_a(q,u)\le B_a(0,u)
=\cos(\beta_a-2au)-\cos\beta_a\le C a^2u
\]
forces \(\lvert q\rvert^2\le C'u\), using \(\cosh(2aq)-1\ge2a^2q^2\). Thus the rescaled integrand is bounded by
\(C''e^{-v}v\mathbf1_{\{|w|\le C''\sqrt v\}}\), an integrable majorant. Dominated convergence applied to the positive part in (2) gives the *unnormalized* negative mass of the first positive lobe as
\[
\begin{aligned}
&\frac{a^2e^{-t_a^2}}{(2t_a)^{3/2}t_a}
\left[\int_0^\infty e^{-v}\int_{\mathbb R}(\sqrt2v-w^2)_+\,dw\,dv+o(1)\right]\\
&=\frac{a^2e^{-t_a^2}}{(2t_a)^{3/2}t_a}
\left[2^{3/4}\sqrt\pi+o(1)\right],
\end{aligned}
\tag{3}
\]
because the inner integral is \(\frac43(\sqrt2v)^{3/2}\) and \(\Gamma(5/2)=3\sqrt\pi/4\).

**4. Normalize and expand the edge.** Divide (3) by \(\pi(1+E_a)\), include the equal negative-momentum lobe, and use Step 2. One obtains
\[
\mathcal N(a)=\frac{2^{-3/4}}{\sqrt\pi}\,
 a^2t_a^{-5/2}e^{-t_a^2}(1+o(1)).
\tag{4}
\]
Elementary inversion of the cosine expansion yields
\[
\beta_a=\sqrt2\,a-\frac{\sqrt2}{6}a^3+O(a^5),\qquad
 t_a=\frac\pi{2a}-\frac1{\sqrt2}+O(a^2),
\]
so
\[
t_a^2=\frac{\pi^2}{4a^2}-\frac\pi{\sqrt2a}+\frac12+O(a),\qquad
t_a^{-5/2}=\left(\frac{2a}\pi\right)^{5/2}(1+O(a)).
\]
Substituting into (4) gives the boxed equivalent, including its exact constant. \(\square\)

## Verification
The standalone numerical checker `checks/check_cat.py` uses `mpmath` at 75 decimal digits. It verifies (1) against the defining Wigner integral at three phase-space points, evaluates the first two nearest lobes by an exact error-function integration in \(q\), and checks convergence of the resulting normalized asymptotic ratios at \(a=0.35,0.25,0.20,0.15\), respectively approximately \(0.82843218,0.88846332,0.91572889,0.94071501\). The program deliberately does not infer the negligibility of higher lobes or the infinite limit from finite quadrature; those are established in the proof. Run `python checks/check_cat.py` from the directory containing the package files, with Python 3 and `mpmath` available.

## Relationship to prior work
Kenfack and Życzkowski (2004) introduced and evaluated integrated Wigner negativity for cat-like superpositions; their equations (3.1)–(3.8) give the standing-cat Wigner formula and discuss numerical values and an upper approximation. Equation (1) above is an algebraic specialization of their already-known formula, **not** an originality claim. The present claim is the sharp \(a\downarrow0\) equivalent not established by the inspected primary literature for the exact integrated negative part: it requires resolving an escaping Gaussian fringe edge together with a shrinking transverse boundary layer. Fiurášek and Ježek (2013) treat homodyne-fidelity witnesses for cat states, not this small-separation integrated-volume law. No claim of established publication priority or independent validation is made.

## Limitations
The equivalent holds only for the specified even, standing Gaussian superposition as \(a\downarrow0\). It is not a uniform theorem for arbitrary relative phases, loss channels, squeezings, or multimode states. The script checks finitely many parameters; the proof alone establishes the asymptotic. Existing literature may contain an equivalent result under different quantum-optics normalization; publication priority remains a residual risk.

## References
1. A. Kenfack and K. Życzkowski, *Negativity of the Wigner function as an indicator of nonclassicality*, arXiv:quant-ph/0406015v1 (first public preprint: 2004-06-02), especially Section III and equations (3.1)–(3.8). https://arxiv.org/abs/quant-ph/0406015
2. J. Fiurášek and M. Ježek, *Witnessing negativity of Wigner function by estimating fidelities of cat-like states from homodyne measurements*, arXiv:1306.0508v1 (2013-06-03), especially Sections I–II. https://arxiv.org/abs/1306.0508

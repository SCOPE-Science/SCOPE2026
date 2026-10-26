# Exact logarithmic Wiener growth and arithmetic resonance for piecewise-affine circle phases

## Finding

The Wiener-algebra norm of powers of a piecewise-affine circle map has a **sharp logarithmic coefficient determined by the arithmetic of its segment lengths**, provided the segment slopes are distinct integers. More precisely, write \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\) and normalize Fourier coefficients by
\[
\widehat h(k)=\frac1{2\pi}\int_0^{2\pi}h(x)e^{-ikx}\,dx,
\qquad \|h\|_{A(\mathbb T)}=\sum_{k\in\mathbb Z}|\widehat h(k)|.
\]
Let \(0=a_0<a_1<\cdots<a_J=2\pi\) with \(J\ge2\). Let \(\phi:[0,2\pi]\to\mathbb R\) be continuous and affine on each \([a_{j-1},a_j]\), with **pairwise distinct integer slopes** \(s_j\), and assume \(\phi(2\pi)-\phi(0)\in2\pi\mathbb Z\). Thus \(F(x)=e^{i\phi(x)}\) is a continuous unimodular circle function. Set \(L_j=a_j-a_{j-1}\). Choose any constant
\[
0<\delta<\frac13\min_{j\ne\ell}|s_j-s_\ell|.
\]
Then, as positive integers \(n\) tend to infinity,
\[
\boxed{\ \|F^n\|_{A(\mathbb T)}
=\frac{2}{\pi}\sum_{j=1}^J\sum_{m=1}^{\lfloor\delta n\rfloor}
 \frac{|\sin(mL_j/2)|}{m}+O_{\phi,\delta}(1).\ }
\tag{1}
\]
Define for \(0<\theta<1\)
\[
\mu(\theta)=\begin{cases}
 \displaystyle\frac1q\cot\frac{\pi}{2q},&\theta=p/q\text{ in lowest terms},\\[5pt]
 \displaystyle\frac2\pi,&\theta\notin\mathbb Q.
\end{cases}
\]
The limit exists and is
\[
\boxed{\ \lim_{n\to\infty}\frac{\|F^n\|_{A(\mathbb T)}}{\log n}
=\frac2\pi\sum_{j=1}^J\mu\left(\frac{L_j}{2\pi}\right).\ }
\tag{2}
\]
In particular, it is strictly positive. If all normalized lengths are rational, the difference between \(\|F^n\|_A\) and the leading coefficient times \(\log n\) remains bounded.

**Arithmetic resonance corollary.** For \(0<t<\pi\), define the real periodic plateau-tent phase
\[
\phi_t(x)=\begin{cases}
-x,&0\le x\le t,\\
-t,&t\le x\le 2\pi-t,\\
x-2\pi,&2\pi-t\le x\le2\pi.
\end{cases}
\]
It has slopes \(-1,0,1\). Its sharp coefficient is
\[
\mathcal C(t)=\frac2\pi\left[2\mu\left(\frac{t}{2\pi}\right)
+\mu\left(1-\frac t\pi\right)\right].\tag{3}
\]
For every irrational \(t/\pi\), \(\mathcal C(t)=12/\pi^2\). For every rational \(t/\pi\in(0,1)\), \(\mathcal C(t)<12/\pi^2\); for instance,
\[
\mathcal C(\pi/2)=\frac{2+\sqrt2}{\pi},\qquad
\mathcal C(2\pi/3)=\frac{2\sqrt3}{\pi}.
\]
The function \(t\mapsto\mathcal C(t)\) is continuous at irrational \(t/\pi\) and discontinuous at every rational \(t/\pi\). Thus the leading norm-growth constant has a dense arithmetic set of downward resonances despite uniform continuity of the underlying phases in the parameter.

## Assumptions and scope

The theorem concerns powers with **positive integer** exponent \(n\); the integer-slope and distinct-slope assumptions isolate noninterfering Fourier frequency clusters. The real lift \(\phi\) may have nonzero winding number, since only the endpoint condition modulo \(2\pi\) is required. There is no regularity assumption on the derivative at breakpoints. Each \(F^n\) is piecewise continuously differentiable and belongs to \(W^{1,2}(\mathbb T)\subset A(\mathbb T)\). The coefficients \(\mu\) depend on normalized arc lengths, not on the absolute slope values, within this restricted class. No claim is made for repeated slopes, noninteger slopes, arbitrary smooth phases, or any uniform error bound while the breakpoints vary.

## Proof

Write \(\phi(x)=s_jx+c_j\) on \([a_{j-1},a_j]\). Direct integration for \(k\in\mathbb Z\) gives
\[
\widehat{F^n}(k)=\frac1{2\pi}\sum_{j=1}^J e^{inc_j}
\begin{cases}
\displaystyle\frac{e^{i(ns_j-k)a_j}-e^{i(ns_j-k)a_{j-1}}}{i(ns_j-k)},&k\ne ns_j,\\[5pt]
L_j,&k=ns_j.
\end{cases}
\tag{4}
\]
Here the braces are interpreted separately for each summand. All resonance centers \(ns_j\) are integers. With \(\delta\) as in the statement, the windows \(W_{j,n}=\{k\in\mathbb Z:|k-ns_j|\le\delta n\}\) are pairwise disjoint. Inside \(W_{j,n}\), the sum of the contributions from the other intervals has magnitude \(O_{\phi,\delta}(1/n)\), uniformly in \(k\). There are \(O(n)\) integers in a window, hence the triangle inequality \(\big||u+v|-|u|\big|\le|v|\) allows these terms to be omitted from the \(\ell^1\)-sum at cost \(O(1)\). At \(k=ns_j\), the main interval contributes \(L_j/(2\pi)\). For \(k=ns_j+m\), \(m\ne0\), its magnitude is precisely
\[
\frac1{2\pi}\frac{|e^{-ima_j}-e^{-ima_{j-1}}|}{|m|}
=\frac{|\sin(mL_j/2)|}{\pi|m|}.\tag{5}
\]
Summing (5) over both signs of \(m\) gives the part of (1) from the resonance windows, up to \(O(1)\).

We show that all remaining frequencies contribute \(O(1)\). Fix \(C>2+2\max_j|s_j|\). For \(|k|\le Cn\) outside every \(W_{j,n}\), each denominator in (4) is of size at least \(\delta n\); thus \(|\widehat{F^n}(k)|\le C_\phi/n\). There are \(O(n)\) such frequencies. For \(|k|>Cn\), expand
\[
\frac1{ns_j-k}=-\frac1k+O_\phi\left(\frac n{k^2}\right).
\]
The numerator endpoints of the \(-1/k\) terms telescope to zero: continuity of \(F^n\) cancels adjacent interval endpoints, and its circle periodicity cancels the endpoints \(0\) and \(2\pi\) because \(k\in\mathbb Z\). Hence \(|\widehat{F^n}(k)|\le C_\phi n/k^2\). Summing over \(|k|>Cn\) yields \(O(1)\) and proves (1).

To obtain (2), put \(\theta=L_j/(2\pi)\) and \(a_m=|\sin(\pi m\theta)|\). If \(\theta=p/q\) in lowest terms, \(a_m\) has period \(q\), and multiplication by \(p\) permutes its residues. Therefore its Cesàro mean equals
\[
\frac1q\sum_{r=1}^{q-1}\sin\frac{\pi r}{q}
=\frac1q\cot\frac\pi{2q}.
\]
If \(\theta\) is irrational, Weyl equidistribution of \(m\theta\pmod1\) and the continuity of \(|\sin\pi x|\) imply that its Cesàro mean is \(\int_0^1|\sin\pi x|\,dx=2/\pi\). For any bounded sequence with Cesàro mean \(\mu\), summation by parts shows \(\sum_{m\le N}a_m/m=\mu\log N+o(\log N)\). In the rational periodic case the error is \(O(1)\). Insert this into (1), noting \(\log\lfloor\delta n\rfloor/\log n\to1\), to conclude.

For (3), the segment lengths of \(\phi_t\) are \(t,2\pi-2t,t\), so (2) applies. When \(t/\pi\) is irrational all three normalized lengths are irrational. When it is rational, each normalized length is rational with denominator \(q\ge2\), and \(q^{-1}\cot(\pi/(2q))<2/\pi\) because \(\cot u<1/u\) for \(0<u<\pi/2\). The displayed evaluations follow from the cases \(q=2,3,4\). Finally, if rational \(p_k/q_k\to\theta\notin\mathbb Q\) in lowest terms, then \(q_k\to\infty\) and \(q_k^{-1}\cot(\pi/(2q_k))\to2/\pi\). Together with the constant irrational value, this proves continuity at irrationals and, by comparison with nearby irrational parameters, the stated discontinuity at rationals.

## Verification

Equation (4) is an exact finite sum; no numerical approximation is used in the proof. The standalone `check_wiener.py` evaluates (4) with a finite frequency cutoff, compares independent interval quadrature for selected low-order Fourier coefficients, and checks the rational coefficients in (3). Finite computations are diagnostic only: the tail estimate, equidistribution argument, and harmonic summation establish the infinite limiting claims. For example, with \(t=2\pi/3\), the predicted coefficient is \(2\sqrt3/\pi\), and the diagnostic finite-frequency sums for \(n=500,2000,8000\) show stabilization of \(\|F^n\|_A-\mathcal C(t)\log n\) near \(2.45\). These truncations are not used as proof of convergence.

## Relationship to prior work

Ohrysko's 2026 proof of Kahane's conjecture establishes the rigidity threshold \(o(\log n)\). Its Example 8.1 gives the tent function \(e^{i|x|}\), an explicit coefficient formula, and the two-sided order \(\|F^n\|_A\asymp\log n\), but not a general distinct-integer-slope leading constant or its rational/irrational length dependence. Kahane's earlier work proves the logarithmic order for nonaffine continuous piecewise-linear phases, as quoted by both Ohrysko and Lebedev. Lebedev's 2012 papers concern quantitative rigidity and \(U(\mathbb T)\) bounds; the inspected relevant statements do not assert (1)–(3). The new result is an exact resonant decomposition for an entire natural class and shows an arithmetic discontinuity of its leading coefficient. This comparison does not exclude an unindexed equivalent in older literature.

## Limitations

Pairwise distinct **integer** slopes are essential hypotheses of the stated proof. Repeated slopes can create interactions within one resonance window; arbitrary real slopes can move resonances off the Fourier integer lattice. Equation (1) has an \(O(1)\) error for each fixed phase; it is not a uniform statement across breakpoints. The logarithmic coefficient describes the \(A(\mathbb T)\) norm only, not the uniform-Fourier \(U(\mathbb T)\) norm or a classification of every circle map with logarithmically bounded powers. The original Kahane monograph's full relevant chapter was not accessible for a complete historical priority comparison.

## References

1. P. Ohrysko, *A proof of Kahane's conjecture in the Wiener algebra*, arXiv:2610.14981v1 (first public 2026-10-10), especially Theorem 1.1 and Example 8.1. https://arxiv.org/html/2610.14981v1
2. V. Lebedev, *On uniform convergence of Fourier series*, arXiv:1203.6703v1 (2012), especially the introduction, theorem and proof. https://arxiv.org/html/1203.6703v1
3. V. Lebedev, *Absolutely convergent Fourier series. An improvement of the Beurling–Helson theorem*, arXiv:1112.4892v3 (2012), introductory review. https://arxiv.org/html/1112.4892v3
4. J.-P. Kahane, *Séries de Fourier absolument convergentes*, Springer-Verlag, 1970, Chapter VI, §2 (order-of-growth result as cited in the three sources above; chapter not inspected in full).

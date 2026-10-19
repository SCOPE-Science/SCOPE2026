# A sharp inverse-degree radial law for Landau's binomial sections

## Finding

For each integer \(n\ge1\), let
\[
 a_k=\frac{\binom{2k}{k}}{4^k},\qquad
 P_n(z)=\sum_{k=0}^{n}a_k z^k,\qquad
 r_n=\min\{|z|:P_n(z)=0\}.
\]
Define the entire function and its zero-distance constant
\[
 H(w)=\frac1{\sqrt\pi}\int_0^1 t^{-1/2}e^{wt}\,dt
      =\frac2{\sqrt\pi}\int_0^1 e^{wu^2}\,du,
 \qquad c_* =\min_{H(w)=0}\operatorname{Re}w.
\]
The zero set of \(H\) is nonempty, all its zeros are simple and have strictly positive real part, and the displayed minimum exists with \(0<c_*<\infty\). Moreover,
\[
 \boxed{\displaystyle r_n=1+\frac{c_*}{n}+O(n^{-2})\quad(n\to\infty).}
\]
Thus \(\lim_{n\to\infty} n(r_n-1)=c_*\), answering the asymptotic question in Open Problem 5.7 of Technau (2026). The constant is specified exactly by an entire-function zero minimum; no elementary closed form or certified decimal evaluation is asserted.

## Assumptions and scope

The polynomial \(P_n\) is the partial sum of \((1-z)^{-1/2}\) through degree \(n\), with the principal binomial coefficients \(a_k>0\). Its minimum zero modulus is over all complex zeros, counted without restricting their arguments. The constant in the \(O(n^{-2})\) remainder is absolute and need not be effective. The theorem concerns the original zero-radius sequence, not any partial-sum coefficient norm or the zeros of another binomial truncation.

## Proof

**1. Exact summation and scaling.** Set \(S_k=\sum_{j=0}^k a_j\). The recursion \(a_k/a_{k-1}=(2k-1)/(2k)\) gives the exact telescoping identity
\[
 S_k=(2k+1)a_k.
\]
Wallis/Stirling estimates imply \(S_k=2\sqrt{k/\pi}+O((k+1)^{-1/2})\), valid also at \(k=0\) with the stated error. Summation by parts yields
\[
 P_n(z)=S_nz^n+(1-z)\sum_{k=0}^{n-1}S_kz^k.
\]
For each fixed \(R>0\), insert \(z=e^{w/n}\), uniformly for \(|w|\le R\). The bounded-variation Riemann-sum estimate for \(t\mapsto\sqrt t\,e^{wt}\) gives
\[
 \sum_{k=0}^{n-1}S_ke^{wk/n}
 =\frac{2n^{3/2}}{\sqrt\pi}\int_0^1\sqrt t\,e^{wt}\,dt+O_R(\sqrt n).
\]
As \(S_n=2\sqrt{n/\pi}+O(n^{-1/2})\) and \(1-e^{w/n}=-w/n+O_R(n^{-2})\), integration by parts proves the locally uniform estimate
\[
 \frac{P_n(e^{w/n})}{\sqrt n}
 =\frac2{\sqrt\pi}\left(e^w-w\int_0^1\sqrt t\,e^{wt}\,dt\right)+O_R(n^{-1})
 =H(w)+O_R(n^{-1}).\tag{1}
\]

**2. The limiting zeros.** For \(x\le0\), \(t^{-1/2}e^{xt}\) is strictly decreasing. Integration by parts using \((1-\cos yt)/y\), with the integrable singularity at \(t=0\), shows
\[
 \int_0^1 t^{-1/2}e^{xt}\sin(yt)\,dt>0\quad(y>0).
\]
For \(y=0\) the defining integral is positive. Consequently \(H\) has no zero in \(\operatorname{Re}w\le0\). The integral has exponential type at most one. If it were zero-free, Hadamard factorization would force \(H(w)=e^{aw+b}\), which contradicts \(H(-R)\asymp R^{-1/2}\) as \(R\to\infty\). Thus it has a zero. Also, integration of \(\frac{d}{dt}(\sqrt t\,e^{wt})\) gives
\[
 H(w)+2wH'(w)=\frac{2e^w}{\sqrt\pi},
\]
so every zero is simple. For \(y\to\pm\infty\), elementary oscillatory integration (subtracting the value of \(e^{xt}\) at zero, then integrating by parts) gives, uniformly for \(0\le x\le C\),
\[
 H(x+iy)=\frac{e^{i\operatorname{sgn}(y)\pi/4}}{\sqrt{|y|}}+O_C(|y|^{-1}).\tag{2}
\]
Thus any bounded real-part strip has only finitely many zeros. The strictly positive real parts and existence of a zero now imply the minimum defining \(c_*\) is attained and positive.

**3. Excluding distant roots at inverse-degree radial scale.** Put \(d_k=a_{k-1}-a_k=a_{k-1}/(2k)>0\), and
\[
 Q_n(z)=1-\sum_{k=1}^nd_kz^k.
\]
Then \((1-z)P_n(z)=Q_n(z)-a_nz^{n+1}\). For \(|u|=1\), the binomial series \((1-u)^{1/2}=1-\sum_{k\ge1}d_ku^k\) converges absolutely, so
\[
 |Q_n(u)-(1-u)^{1/2}|\le\sum_{k>n}d_k=a_n.
\]
Take any fixed \(C>0\) and any zero \(z=\rho u\) with \(1\le\rho\le1+C/n\), \(|u|=1\). Since
\[
 \sum_{k=1}^n k d_k=\frac12 S_{n-1}=O(\sqrt n),\qquad
 \rho^{n+1}=O_C(1),
\]
we have \(|Q_n(\rho u)-Q_n(u)|\le O_C(n^{-1/2})\), while the zero equation gives \(|Q_n(\rho u)|\le a_n\rho^{n+1}=O_C(n^{-1/2})\). Hence \(|1-u|^{1/2}=O_C(n^{-1/2})\), or
\[
 |1-u|=O_C(n^{-1}),\qquad |z-1|=O_C(n^{-1}).\tag{3}
\]
The principal scaled logarithms \(w=n\log z\) of every such zero therefore stay in a bounded set, depending only on \(C\). All roots of \(P_n\) have \(|z|>1\) by the Eneström–Kakeya theorem and the strict coefficient ratios.

**4. Selecting the closest root.** By (1), simplicity of zeros of \(H\), and a standard analytic perturbation/Rouché argument, every fixed zero \(w_0\) of \(H\) has a nearby zero \(w_n=w_0+O(n^{-1})\) of \(P_n(e^{w/n})\). For one with \(\operatorname{Re}w_0=c_*\), this gives
\[
 r_n\le1+c_*/n+O(n^{-2}).\tag{4}
\]
Let \(z_n\) be any minimum-modulus zero of \(P_n\). Equation (4), Eneström–Kakeya, and (3) show that \(v_n=n\log z_n\) is bounded. Estimate (1) implies \(H(v_n)=O(n^{-1})\). Since the zeros of \(H\) in a fixed compact neighborhood are finitely many and simple, their local linear bounds give \(\operatorname{dist}(v_n,Z(H))=O(n^{-1})\). Therefore \(\operatorname{Re}v_n\ge c_*-O(n^{-1})\). Combining with (4) and \(|z_n|=\exp(\operatorname{Re}v_n/n)\) proves the boxed expansion.

## Verification

The accompanying `checker.py` verifies the exact partial-sum and difference identities using rational arithmetic, evaluates a simple zero of \(H\) at high precision, checks the differential identity, and computes nearby zeros of several \(P_n\) by independent polynomial evaluation. These finite tests support the normalization and the \(n^{-1}\) localization mechanism. They are not a proof that the numerically detected zero globally minimizes the real part, nor a substitute for Steps 1–4.

## Relationship to prior work

Technau, *Shapiro's problem on polynomials with large partial sums of coefficients* (first posted March 25, 2026), §5.4, proves \(r_n-1\gg n^{-1}\) and \(r_n-1\ll(\log n)/n\), and explicitly asks in Open Problem 5.7 for an asymptotic formula. The present theorem closes that logarithmic gap with a sharp constant and a second-order radial error. The proof uses standard binomial asymptotics, Eneström–Kakeya, and elementary convergence of scaled analytic functions; those underlying tools are not claimed as new. Talbot (1974) proves positivity of the real part of precisely these binomial sections in the unit disk, a stronger zero-exclusion fact than Eneström–Kakeya but without any nearest-root asymptotic. Janson–Norfolk (2009) treats sections with coefficients \(\binom{N}{k}\) for a *varying integer* exponent, not the fixed exponent \(-1/2\). Vargas (2012) studies predominantly sections of entire exponential-integral functions, not the closest zeros of these finite-radius sections. A specific previously published implication of the boxed asymptotic was not identified.

## Limitations

The exact constant is characterized implicitly via zeros of an entire function, not evaluated in elementary terms; no proof is given identifying which numbered zero realizes the minimum. No uniform description of all \(n\) polynomial zeros, and no improvement to Shapiro's full coefficient-optimization problem, is asserted. Historical-priority risk remains from older section-zero literature whose full text was not available for implication comparison.

## References

1. M. Technau, *Shapiro's problem on polynomials with large partial sums of coefficients*, arXiv:2603.24405 (v1, March 25, 2026), subsequently *Forum of Mathematics, Sigma* 14 (2026), e69, especially §5.4 and Open Problem 5.7. https://arxiv.org/abs/2603.24405 ; https://doi.org/10.1017/fms.2026.10213 .
2. A. R. Vargas, *Zeros of Sections of Some Power Series*, arXiv:1208.5186 (2012), for broader section-zero asymptotic context. https://arxiv.org/abs/1208.5186 .
3. E. R. Love, *On the Zeros of Partial Sums of a Certain Power Series*, *Journal of the London Mathematical Society* s1-24 (1949), 112–120. https://doi.org/10.1112/jlms/s1-24.2.112 . (Full-text comparison not completed.)

4. A. Talbot, *The Zeros of Partial Sums of a Maclaurin Expansion*, Brunel TR/46 (October 1974), full text: https://bura.brunel.ac.uk/bitstream/2438/1958/1/TR_46.pdf .
5. S. Janson and T. S. Norfolk, *Zeros of Sections of the Binomial Expansion*, ETNA 36 (2009), 27–38, arXiv:0903.3866. https://arxiv.org/abs/0903.3866 .

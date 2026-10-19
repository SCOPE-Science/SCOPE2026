# Sharp variance of escape rates over equal-sized Markov holes and its periodic-orbit allocation

## Finding

Fix an integer alphabet size \(q\ge 2\). For the expanding interval map \(T_q(x)=qx\pmod 1\), choose a Markov hole \(H_w\) uniformly among the \(q^n\) basic \(q\)-adic cylinders indexed by words \(w\in\{0,\ldots,q-1\}^n\), \(n\ge3\). The hole is then held **fixed** at every time. Write \(\gamma_n(w)\) for the exponential Lebesgue-survival escape rate and \(h_n=q^{-n}\) for the measure of the hole. Define the normalized escape rate and its average by
\[
Y_n(w)=\frac{\gamma_n(w)}{h_n},\qquad
\overline Y_n=q^{-n}\sum_{w}Y_n(w).
\]

Let \(\mu\) be the number-theoretic Möbius function and let \(a_q(p)=\sum_{d\mid p}\mu(d)q^{p/d}\), the number of primitive \(q\)-ary blocks of length \(p\). Then
\[
\boxed{\lim_{n\to\infty}q^n\operatorname{Var}_{w}(Y_n(w))=K_q}
\quad\text{where}\quad
\boxed{K_q=\sum_{p=1}^{\infty}\frac{a_q(p)}{q^{2p}}
=\sum_{d=1}^{\infty}\frac{\mu(d)q}{q^{2d}-q}.}
\]
Both series converge absolutely and \(0<K_q<\infty\). In particular, \(K_2=0.823295689936509\ldots\) and the standard deviation of the normalized rate is asymptotic to \(\sqrt{K_q}\,q^{-n/2}\).

There is also a limiting **allocation of this variance among primitive orbits**. Define the least proper self-overlap period of \(w\) as
\[
r_n(w)=\min\{1\le p<n: w_0\cdots w_{n-p-1}=w_p\cdots w_{n-1}\},
\]
putting \(r_n(w)=n\) when no such period exists. Assign each word the weight
\[
\pi_n(w)=\frac{(Y_n(w)-\overline Y_n)^2}{\sum_v(Y_n(v)-\overline Y_n)^2}.
\]
For every fixed positive integer \(p\),
\[
\boxed{\lim_{n\to\infty}\sum_{w:r_n(w)=p}\pi_n(w)
=\frac{a_q(p)q^{-2p}}{K_q}.}
\]
The limiting weights sum to one. Although holes covering low-period orbits are exponentially rare, they asymptotically account for **all** the variance in escape rates across hole locations.

## Assumptions and scope

The invariant initial distribution is Lebesgue measure on \([0,1)\), and the cylinder \(H_w\) is a half-open interval of length \(q^{-n}\). The survival probability is the measure of initial points whose first \(m\) iterates avoid the same fixed hole; its escape rate is \(\gamma_n(w)=\lim_{m\to\infty}-m^{-1}\log\mathbb P(\text{survive }m\text{ iterates})\). The symbolic coding of \(T_q\) under Lebesgue measure is an i.i.d. uniform \(q\)-ary sequence, apart from a null set of nonunique endpoints. Taking the event of having no occurrence of \(w\) at any of the first \(m\) starting positions changes the usual count by at most a fixed \(n\)-step shift and therefore gives the same exponential escape rate.

The parameter \(q\) is fixed before \(n\to\infty\); no uniform-in-\(q\) claim is made. Variance is taken over the **one-time uniform selection** of the hole, not over iterates of a randomly moving hole or random initial conditions at fixed hole.

## Proof

**1. Exact escape-rate equation.** For a word \(w\) of length \(n\), define its set of proper periods
\[
P(w)=\{1\le p<n: w_i=w_{i+p}\text{ for }0\le i<n-p\},
\qquad C_w(z)=1+\sum_{p\in P(w)}z^p.
\]
Let \(A_m\) count words of length \(m\) avoiding \(w\), with \(A_0=1\), and let \(A(z)=\sum_{m\ge0}A_mz^m\). Let \(B_m\) count length-\(m\) words whose *first* occurrence of \(w\) ends at position \(m\), and put \(B(z)=\sum_mB_mz^m\). Partitioning all words by the absence or first ending position of \(w\) gives \((1-qz)A(z)=1-B(z)\). Appending \(w\) to an avoiding prefix, and decomposing according to the first occurrence of \(w\) in the enlarged word, gives \(z^nA(z)=C_w(z)B(z)\); the second factor records exactly the possible suffix-prefix overlaps. Elimination yields the rational generating function
\[
A(z)=\frac{C_w(z)}{(1-qz)C_w(z)+z^n}.
\]
Let \(h=q^{-n}\), and write \(\lambda_n(w)=\exp(-\gamma_n(w))\). Equivalently \(1/(q\lambda_n(w))\) is the first positive pole of \(A(z)\). Replacing \(z\) by \((q\lambda)^{-1}\) in the denominator yields
\[
(1-\lambda)\lambda^{n-1}C_w((q\lambda)^{-1})=h. \tag{1}
\]
For \(n\ge3\) the left side minus \(h\) is positive at \(\lambda=1-2h\) because \(2(1-2h)^{n-1}>1\), and negative at \(\lambda=1\). All terms \((1-\lambda)\lambda^{n-1-p}\) for \(p\in P(w)\cup\{0\}\) are strictly decreasing on \([1-2h,1]\): indeed \(2h<1/n\), and the derivative of \((1-\lambda)\lambda^k\) is negative for \(\lambda>k/(k+1)\), with \(0\le k\le n-1\). Thus (1) has a unique solution in this interval. The generating-function denominator is positive for \(0<z\le1/q\); its first positive zero lies in the corresponding interval just above \(1/q\). By nonnegative coefficients and Pringsheim's theorem, this determines the exponential growth of the avoiding-word count and hence the required escape rate. In particular \(1-\lambda=O(h)\) uniformly in \(w\).

**2. Uniform reduction to an overlap polynomial.** Since every \(C_w\) has coefficients zero or one, \(C_w(1/q)\) stays in \([1,q/(q-1)]\). Moreover, uniformly for \(\lambda\in[1-2h,1]\),
\[
C_w((q\lambda)^{-1})=C_w(q^{-1})+O_q(h),
\qquad \lambda^{1-n}=1+O_q(nh).
\]
For the first estimate, the termwise derivative is bounded by the convergent series \(\sum_{p\ge1}p\,r^{p-1}\) for any \(r\) between \(1/q\) and \(1/[q(1-2h)]<1\), uniformly for \(n\ge3\). From (1), \((1-\lambda)/h=\lambda^{1-n}/C_w((q\lambda)^{-1})\); also \(-\log\lambda=(1-\lambda)+O(h^2)\). Therefore
\[
\boxed{Y_n(w)=C_w(q^{-1})^{-1}+O_q(nq^{-n})}\tag{2}
\]
with an error independent of the word.

**3. Square-summable concentration at short periods.** Put \(D_n(w)=C_w(q^{-1})^{-1}-1\). If \(r=r_n(w)<n\), then
\[
|D_n(w)|\le\sum_{p\in P(w)}q^{-p}\le\frac{q^{-r}}{1-q^{-1}}.\tag{3}
\]
Every word of length \(n\) with period \(r\) is uniquely determined by its first \(r\) symbols, so at most \(q^r\) words have least period \(r\). Words with no proper period have \(D_n=0\). Consequently, uniformly in \(n\),
\[
\sum_{w:r_n(w)>R}D_n(w)^2\le\frac{1}{(1-q^{-1})^2}\sum_{r>R}q^{-r},
\quad \sum_w|D_n(w)|=O_q(n),\quad \sum_wD_n(w)^2=O_q(1). \tag{4}
\]

**4. Contribution of one primitive period.** Fix \(p\ge1\) and take \(n\ge2p\). Exactly \(a_q(p)\) words of length \(n\) have least period \(p\): repeat a primitive block of length \(p\) and truncate at length \(n\). If this word also had some period \(r<p\), comparing its first \(p\) letters with letters shifted by \(r\) (possible since \(n\ge2p\)) would make its infinite periodic extension \(r\)-periodic, contradicting the primitivity of the block. Conversely, every least-period-\(p\) word arises this way. Its periods include all positive multiples of \(p\) strictly below \(n\). Any other possible period \(r\) must exceed \(n-p\), since an overlap at shift \(r\le n-p\) tests a complete primitive block and hence forces \(r\) to be divisible by \(p\). Their total contribution to \(C_w(q^{-1})\) is \(O_q(q^{-(n-p)})\). Hence, uniformly within this fixed-period class,
\[
C_w(q^{-1})\longrightarrow\frac1{1-q^{-p}},
\qquad D_n(w)\longrightarrow-q^{-p}. \tag{5}
\]
Thus the total squared contribution from least period \(p\) tends to \(a_q(p)q^{-2p}\). The uniform tail estimate (4) allows the fixed-period limits to be summed, showing
\[
\lim_{n\to\infty}\sum_wD_n(w)^2=\sum_{p\ge1}a_q(p)q^{-2p}=K_q. \tag{6}
\]

**5. Exact variance normalization and allocation.** Write \(E_n(w)=Y_n(w)-1-D_n(w)\). By (2), \(\sup_w|E_n(w)|=O_q(nh)\). From (4),
\[
\left|\sum_w(Y_n(w)-1)^2-\sum_wD_n(w)^2\right|
\le 2\sup|E_n|\sum_w|D_n|+q^n\sup|E_n|^2
=O_q(n^2h)=o(1). \tag{7}
\]
Also \(\sum_w|Y_n(w)-1|=O_q(n)\), hence \(\overline Y_n=1+O_q(nh)\). The centering correction is
\[
\sum_w(Y_n(w)-\overline Y_n)^2
=\sum_w(Y_n(w)-1)^2-q^n(\overline Y_n-1)^2
=K_q+o(1). \tag{8}
\]
Since \(\operatorname{Var}_w(Y_n)=q^{-n}\sum_w(Y_n(w)-\overline Y_n)^2\), this proves the variance theorem. For each fixed \(p\), there are exactly \(a_q(p)\) terms in its class and (2),(5) give their centered squares tending to \(q^{-2p}\); division by (8) proves the displayed allocation limit. Equation (4) makes the total limiting mass one.

**6. Möbius form and positivity.** Primitive blocks are counted by Möbius inversion: \(a_q(p)=\sum_{d\mid p}\mu(d)q^{p/d}\). Because \(0\le a_q(p)\le q^p\), the defining series for \(K_q\) is absolutely convergent. Rearrange the absolutely convergent double sum by writing \(p=dk\):
\[
K_q=\sum_{d\ge1}\mu(d)\sum_{k\ge1}q^{k-2dk}
=\sum_{d\ge1}\frac{\mu(d)q}{q^{2d}-q}.
\]
The contribution from period one alone equals \(q^{-1}\), so \(K_q>0\).

## Verification

Run `python checker.py` in the directory containing this result. The standard-library-only checker prints `VERIFY_OK` if finite exact avoidance counts agree with the rational generating function, escape-root solutions have the required branch and uniform approximation, and the two independent finite-sum expressions for \(K_2\) agree. It enumerates small alphabets and word lengths; the all-\(n\) result follows from steps 1–6, not enumeration. The observed binary values \(2^n\operatorname{Var}_w(Y_n)\) at \(n=9\) and \(n=14\) are approximately \(0.7918\) and \(0.8196\), consistent with the limit \(0.8232956899\ldots\), but nonmonotonicity at smaller \(n\) is possible and no monotonicity is claimed.

## Relationship to prior work

Georgiou, Dettmann and Altmann (2012), especially Sections III–IV of *Faster than expected escape for a class of fully chaotic maps*, establish Markov-hole spectral formulas, average escape rates over positions, and primitive-orbit counting. Those are fundamental inputs and are not presented here as new. The theorem above instead determines the **second centered moment** over positions at the sharp scale \(q^{-n}\), with a distinct convergent constant and a probability law allocating variance among least-overlap periods. The cited work's average formula does not by itself supply this statement: one needs a uniform overlap-polynomial approximation and square-summable domination to interchange the full-hole second-moment sum with the short-period limit.

Bonanno, Cristadoro and Lenci (2021), *Maximal escape rate for shifts*, treat precisely the equivalent full-shift one-forbidden-word framework: their Proposition 2.4 and Appendix A give the general autocorrelation-polynomial escape equation, and their Theorems 3.4–3.5 classify maximizers. They do not determine the ensemble variance, its sharp \(q^{-n}\) scale or its variance-weighted least-period distribution. Bunimovich and Yurchenko (2008/2011) establish how individual escape rates depend on period and hole placement, not an asymptotic variance law over all fixed equal-sized holes. Dettmann (2011) studies small-hole asymptotics at fixed positions, including fractal dependence on location, rather than the ensemble second moment. McGoff (2018) studies random subshifts with many independently retained/removed words, which is a genuinely different random-hole ensemble. No independence or other certification is asserted for the present theorem.

## Limitations

This is a theorem about piecewise-full-branch integer-slope maps and **basic q-adic cylinder holes** with a fixed uniform selection among positions. It does not describe arbitrary interval holes, continuous distributions of hole centers, distorted maps, randomly relocated holes, non-Lebesgue invariant measures, or simultaneous growing-alphabet limits. The finite checker cannot certify infinite limits. The 2012 foundational article contains powerful enough formulas to make the new constant derivable with additional analysis; the possibility of earlier unindexed or differently phrased second-moment calculations remains a bibliographic priority risk. Independent mathematical and historical assessment has not been performed.

## References

1. O. Georgiou, C. P. Dettmann, E. G. Altmann, *Faster than expected escape for a class of fully chaotic maps*, arXiv:1207.7000 (first submitted 2012-07-30), https://arxiv.org/abs/1207.7000. Especially Sections III–IV and the mean escape-rate formulas.
2. L. A. Bunimovich, A. Yurchenko, *Where to place a hole to achieve a maximal escape rate*, arXiv:0811.4438 (first submitted 2008-11-26), https://arxiv.org/abs/0811.4438.
3. C. P. Dettmann, *Open circle maps: Small hole asymptotics*, arXiv:1112.5390 (first submitted 2011-12-22), https://arxiv.org/abs/1112.5390.
4. C. Bonanno, G. Cristadoro, M. Lenci, *Maximal escape rate for shifts*, arXiv:2112.14248 (first submitted 2021-12-28), https://arxiv.org/abs/2112.14248. Proposition 2.4, Theorems 3.4–3.5 and Appendix A.
5. K. McGoff, *Pressure for random subshifts of finite type*, arXiv:1809.05586 (first submitted 2018-09-14), https://arxiv.org/abs/1809.05586. Used solely to distinguish hole-selection ensembles, not as the archival source.

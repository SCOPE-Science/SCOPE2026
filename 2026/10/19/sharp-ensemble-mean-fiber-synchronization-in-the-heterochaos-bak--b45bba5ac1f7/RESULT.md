# Sharp ensemble-mean fiber synchronization in the heterochaos baker map

## Finding
Consider the two-dimensional heterochaos baker map of Saiki, Takahasi, and Yorke, with its ternary expanding base. While almost every entire vertical fiber shrinks, its **ensemble-mean width** decays at the sharp rate \(\rho=2\sqrt2/3\), multiplied by \(n^{-3/2}\), and admits a nonzero alternating parity correction at leading order. This decay is strictly slower than the almost-everywhere vertical Lyapunov rate \(2^{-1/3}\).

Precisely, define \(L_n(x)\), \(a_n\), and \(E_n\) below. For every integer \(n\ge0\),
\[
E_n=\frac13\sum_{j=n}^{\infty}a_j,
\quad
\sum_{n=0}^{\infty}a_nw^n
=\frac{2}{1-2w/3+\sqrt{1-8w^2/9}}.
\]
With \(\rho=2\sqrt2/3\) and \(d_\pm=1\mp1/\sqrt2\), as \(n\to\infty\),
\[
\boxed{\displaystyle
E_n=\frac{\sqrt2}{3\sqrt\pi}\frac{\rho^n}{n^{3/2}}
\left(\frac{1}{d_+^2(1-\rho)}
+(-1)^n\frac{1}{d_-^2(1+\rho)}+O(n^{-1})\right).}
\]
The constants in the two parity subsequences are strictly positive, so this is a sharp two-sided asymptotic, including \(\lim_{n\to\infty}E_n^{1/n}=\rho\).

## Assumptions and scope
Let \(F:[0,1]^2\to[0,1]^2\) act at the interiors of its continuity domains by
\[
F(x,z)=\begin{cases}
(3x,z/2),&0\le x<1/3,\\
(3x-1,(z+1)/2),&1/3\le x<2/3,\\
(3x-2,2z\bmod 1),&2/3\le x<1.
\end{cases}
\]
For the last branch, the two halves of the vertical interval use their respective affine branches. On boundaries use any conventional assignment; exceptional boundary itineraries have zero Lebesgue base measure and do not affect the claim.

For each \(n\ge0\) and almost every \(x\in[0,1]\), define \(I_n(x)\) to be the vertical image of \(\{x\}\times[0,1]\) under \(F^n\), interpreted up to its finitely many discarded boundary points. Set \(L_n(x)=\operatorname{Leb}_1(I_n(x))\), \(K_n(x)=-\log_2L_n(x)\), \(a_n=\operatorname{Leb}_1\{x:K_n(x)=0\}\), and \(E_n=\int_0^1L_n(x)\,dx\). The base is uniform Lebesgue measure, **not** a distribution over arbitrary initial vertical intervals. This is the original map, without a tunable parameter.

## Proof
**1. Exact interval dynamics.** The initial vertical image is the dyadic cell \([0,1]\). The two left base branches send a dyadic cell of depth \(k\) to one of depth \(k+1\); the right base branch doubles its length when \(k\ge1\), sending it to a dyadic parent, and preserves the full interval at \(k=0\). Induction shows that every image remains one dyadic cell, up to boundaries, so \(L_n=2^{-K_n}\) and
\[
K_{n+1}=\begin{cases}K_n+1,&b_{n+1}\in\{0,1\},\\ \max(K_n-1,0),&b_{n+1}=2,\end{cases}
\]
where \(b_j\) are the ternary digits of \(x\). These digits are independent and uniform under Lebesgue measure. Therefore the depth is a reflecting birth-and-death chain with upward probability \(p=2/3\) and downward probability \(q=1/3\).

**2. Mean-width defect and return renewal.** If \(K_n=k\ge1\),
\[
\mathbb E(2^{-K_{n+1}}\mid K_n=k)
=2^{-k}\bigl(p/2+2q\bigr)=2^{-k}.
\]
At \(k=0\) the conditional mean is \(p/2+q=2/3\). Thus \(E_0=1\) and the **exact finite-time identity** \(E_{n+1}=E_n-a_n/3\) holds. Let \(T(w)\) be the generating function for the first time, starting from depth one, to hit zero. First-step decomposition gives
\[
T(w)=qw+pwT(w)^2,\qquad
T(w)=\frac{1-\sqrt{1-4pqw^2}}{2pw}.
\]
A renewal at zero consists either of a single holding step of weight \(qw\), or of an upward step followed by a return of weight \(pwT(w)\). Therefore the return probability generating function is
\[
A(w):=\sum_{n\ge0}a_nw^n
=\frac1{1-qw-pwT(w)}
=\frac2{1-2qw+\sqrt{1-4pqw^2}}.
\]
The branch of the square root is positive at \(w=0\). Since \(A(1)=3\), summing the mean-width defect proves \(\lim_nE_n=0\) and
\[
E_n=\frac13\sum_{j=n}^{\infty}a_j.
\]
This also gives \(\sum_{n\ge0}E_nw^n=(1-wA(w)/3)/(1-w)\), with a removable singularity at \(w=1\).

**3. Two singularities and sharp asymptotics.** Put \(R=3/(2\sqrt2)=\rho^{-1}\). The two closest singularities of \(A(w)\) are its square-root branch points at \(w=R\) and \(w=-R\). Indeed the return-renewal denominator has no zero on \(|w|\le R\): its nonnegative first-return coefficients imply \(|qw+pwT(w)|\le qR+pRT(R)=1/2+1/(2\sqrt2)<1\). Analytic continuation to small slit neighborhoods of each point permits ordinary square-root coefficient transfer.

Near \(w=R\), with \(d_+=1-1/\sqrt2\),
\[
A(w)=\frac2{d_+}-\frac{2\sqrt2}{d_+^2}\sqrt{1-w/R}+O(1-w/R).
\]
Near \(w=-R\), replace \(d_+\) with \(d_-=1+1/\sqrt2\) and \(1-w/R\) with \(1+w/R\). The standard binomial coefficient identity
\[
[w^n]\sqrt{1-w/R}
=-\frac{R^{-n}}{2\sqrt\pi\,n^{3/2}}\bigl(1+O(n^{-1})\bigr)
\]
with the analogous alternating coefficient at the negative branch point gives
\[
a_n=\frac{\sqrt2}{\sqrt\pi}\frac{\rho^n}{n^{3/2}}
\left(d_+^{-2}+(-1)^nd_-^{-2}+O(n^{-1})\right).
\]
The next nonanalytic Puiseux powers are order \(3/2\), so this remainder is uniform over both parities. Summing over \(j\ge n\) multiplies the positive-branch amplitude by \((1-\rho)^{-1}\), and the alternating-branch amplitude by \((1+\rho)^{-1}\), with relative corrections \(O(n^{-1})\); this yields the asserted formula for \(E_n\). Positivity is immediate because the nonalternating coefficient is larger than the absolute alternating one.

## Verification
The standalone file `check_fiber.py` directly propagates **every** one of the \(3^n\) ternary digit words for \(0\le n\le8\), maintaining exact rational dyadic image intervals without assuming the depth recurrence. It compares these to independently calculated reflected-walk probabilities and moments. It also verifies the renewal coefficient identity through order 22 and evaluates the sharp asymptotic formula at 500, 800, and 1300 steps. Run `python check_fiber.py` using the standard Python library. All assertions passed, ending with `DYADIC_FIBER_EXACT_AND_ASYMPTOTIC_CHECKS_OK`. Finite verification is not the proof of the asymptotic law; Step 3 is.

## Relationship to prior work
Saiki–Takahasi–Yorke, arXiv:1811.01009, Section 3.1, Proposition 3.1, proves qualitative almost-everywhere contraction of the entire leaf, and states the three cases of central image-length evolution used in Step 1. Section 3.3 gives the typical central Lyapunov number \(2^{-1/3}\). Those qualitative and almost-sure statements do not determine the **ensemble mean**, its exact return renewal, or its sharp parity-sensitive asymptotic.

Takahasi–Yamamoto (arXiv:2209.04905) studies coding and maximal-entropy measures, Takahasi (arXiv:2307.08119) obtains mixing properties, Saiki–Takahasi–Yamamoto–Yorke (arXiv:2401.00836) surveys map dynamics, and Takahasi–Tsujii (arXiv:2408.16618) analyzes polynomial mixing in a different, mostly neutral parameter regime. Their inspected relevant sections do not state this exact mean-vertical-fiber width law. The random-walk first-return calculation is classical, but its application here is to a specific dynamical observable not established by those papers. Absolute literature priority beyond the inspected sources is not claimed.

## Limitations
The result concerns the **mean length of the image of a whole initial fiber**, not the diameter of a typical random pair of trajectories, a general parameter family, or the correlation decay rate. The factor \(\rho\) exceeds the typical exponent because rare ternary itineraries dominate the mean. Exceptional switching-boundary or triadic-expansion ambiguities are null sets in the base. The analytical argument assumes the exact affine original map; nonlinear perturbations and higher-dimensional generalizations are not covered. Publication novelty outside the identified literature is not independently certified.

## References
Saiki, Y., Takahasi, H., and Yorke, J. A., *Piecewise-linear maps with heterogeneous chaos*, arXiv:1811.01009 (first public preprint 2018-11-02), Section 3.1 Proposition 3.1 and Section 3.3. https://arxiv.org/pdf/1811.01009

Takahasi, H., and Yamamoto, K., *Heterochaos baker maps and the Dyck system: maximal entropy measures and a mechanism for breakdown of entropy approachability*, arXiv:2209.04905. https://arxiv.org/pdf/2209.04905

Takahasi, H., *Exponential mixing for heterochaos baker maps and the Dyck system*, arXiv:2307.08119. https://arxiv.org/pdf/2307.08119

Saiki, Y., Takahasi, H., Yamamoto, K., and Yorke, J. A., *The dynamics of the heterochaos baker maps*, arXiv:2401.00836. https://arxiv.org/pdf/2401.00836

Takahasi, H., and Tsujii, M., *Polynomial rate of mixing for heterochaos baker maps with mostly neutral center*, arXiv:2408.16618. https://arxiv.org/pdf/2408.16618

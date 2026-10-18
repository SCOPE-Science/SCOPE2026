# Sharp quadratic heterogeneity cost at the gap-two Poisson–binomial crossover

## Finding

For each integer \(k\ge1\), the critical binomial distribution for the two-step point-probability crossover has a strictly positive, isotropic second-order loss under every mean-preserving perturbation of its Bernoulli parameters. Its exact loss under an opposite perturbation of two coordinates persists all the way to the admissible endpoints. The associated *mean compensation* needed to restore equality of the two compared masses has an exact coefficient, asymptotic to \(2\sqrt{2/k}\).

More precisely, put
\[
 d=\max\!\left\{2,\left\lfloor(9+\sqrt{8k+33})/8\right\rfloor\right\},\quad
 m=k+d,\quad
 t=\sqrt{\frac{(k+1)(k+2)}{d(d-1)}},\quad q=\frac{t}{1+t}.
\]
Let \(b_j=\Pr(\operatorname{Bin}(m-2,q)=j)\), interpreted as zero outside its support, and let \(c=\Pr(\operatorname{Bin}(m,q)=k)>0\). Define
\[
 \alpha_k=b_{k+2}-2b_{k+1}+2b_{k-1}-b_{k-2},\qquad
 B_k=(d-2)(d-3)+\frac{4(k-d+2)}{t}-\frac{k(k-1)}{t^2}.
\]
Then \(\alpha_k>0\) and
\[
 \frac{\alpha_k}{c}=\frac{(1+t)^2 B_k}{m(m-1)}.
\]
If \(S_z\) is the sum of \(m-2\) independent \(\operatorname{Bernoulli}(q)\) variables and two further independent Bernoulli variables with parameters \(q+z\) and \(q-z\), then for every real \(z\) with \(|z|\le\min\{q,1-q\}\),
\[
 \Pr(S_z=k)-\Pr(S_z=k+2)=\alpha_k z^2.
\]
For any fixed real vector \(v=(v_1,\ldots,v_m)\) satisfying \(\sum_i v_i=0\), and independent Bernoulli variables with parameters \(q+\varepsilon v_i\), the corresponding sum \(S_\varepsilon\) obeys, as \(\varepsilon\to0\),
\[
 \Pr(S_\varepsilon=k)-\Pr(S_\varepsilon=k+2)
 =\frac{\alpha_k}{2}\varepsilon^2\sum_{i=1}^m v_i^2+O_{k,v}(|\varepsilon|^3).
\]
To make the two masses equal again, shift every success probability further by \(h/m\), thereby increasing the total mean by exactly \(h\). There is a unique local analytic equality solution \(h=h_k(\varepsilon,v)\) with \(h_k(0,v)=0\), satisfying
\[
 h_k(\varepsilon,v)=C_k\varepsilon^2\sum_{i=1}^m v_i^2+O_{k,v}(|\varepsilon|^3),\qquad
 C_k=\frac{\alpha_k m q(1-q)}{4c}=\frac{tB_k}{4(m-1)}>0.
\]
The coefficient has a sharp universal large-level limit:
\[
 \lim_{k\to\infty}\sqrt{k}\,C_k=2\sqrt2.
\]

## Assumptions and scope

All Bernoulli variables are independent; only integer levels \(k\ge1\) are covered. The number of active trials is fixed at \(m=k+d\), where \(d\) is the staircase integer above. The base probability \(q\) is strictly between zero and one. Directions \(v\) are fixed for each \(k\), with \(\sum v_i=0\); parameters and the compensating shift must remain within \([0,1]\). Limits in \(\varepsilon\) are taken at fixed \(k,v\), while the final limit varies \(k\) using the stated staircase \(d\). The opposite-pair identity, unlike the local Taylor laws, holds on the entire feasible segment.

The externally established input is Kleiner's sharp threshold and *uniqueness of boundary ties* for \(k\ge1\) (Theorem 1 and Proposition 7 of reference [1]). Those theorems assert that the binomial law \(\operatorname{Bin}(m,q)\) is a tie at the smallest mean permitting an eventual strict two-step reversal, and that no heterogeneous vector at that mean can tie. The quantitative coefficients, compensation law, and its asymptotic constant are derived below.

## Proof

**1. Boundary and sign.** Set \(F(p_1,\ldots,p_m)=\Pr(S=k+2)-\Pr(S=k)\) for the associated Bernoulli sum. By [1, Theorem 1], \(F(q,\ldots,q)=0\). By [1, Proposition 7], every vector at the same sum \(mq\) has \(F\le0\), with equality only at the homogeneous vector, after ignoring zero trials. This implication follows from the extremal fixed-mean comparison and the full boundary-tie classification in [1, Sections 2, 5, 6]. The restriction \(k\ge1\) is indispensable because the boundary-tie classification is not rigid at \(k=0\).

**2. Exact pair sensitivity.** Let \(R\) be the sum of the other \(m-2\) independent Bernoulli variables, all with parameter \(q\). Its generating polynomial is \(G(u)=\sum_j b_j u^j\). For arbitrary pair parameters \(x,y\),
\[
 \mathbb E[u^{R+X+Y}]=G(u)\{1+(x+y)(u-1)+xy(u-1)^2\}.
\]
The coefficient of \(xy\) in \(F\) is
\[
 [u^{k+2}]G(u)(u-1)^2-[u^k]G(u)(u-1)^2
 =b_{k+2}-2b_{k+1}+2b_{k-1}-b_{k-2}=\alpha_k.
\]
Put \(x=q+z\) and \(y=q-z\). Their sum remains \(2q\), and their product becomes \(q^2-z^2\). Since the unperturbed difference is zero, \(F=-\alpha_k z^2\) identically on the feasible segment. If \(\alpha_k\le0\), a sufficiently small nonzero \(z\) would yield \(F\ge0\), contradicting either the sharp boundary inequality (strictly positive case) or unique boundary tie (zero case) from step 1. Thus \(\alpha_k>0\), proving the exact identity and strictness.

**3. Algebraic coefficient certificate.** With \(m=k+d\) and \(t=q/(1-q)\), compare \(b_j\) to \(c=\Pr(\operatorname{Bin}(m,q)=k)\). The binomial coefficient ratios give
\[
 \frac{b_{k+2}}c=\frac{(1+t)^2(d-2)(d-3)}{m(m-1)},\quad
 \frac{b_{k+1}}c=\frac{(1+t)^2(d-2)(k+2)}{m(m-1)t},
\]
\[
 \frac{b_{k-1}}c=\frac{(1+t)^2 kd}{m(m-1)t},\quad
 \frac{b_{k-2}}c=\frac{(1+t)^2 k(k-1)}{m(m-1)t^2}.
\]
These formulas remain valid at support boundaries by the convention \(b_j=0\). Combining with step 2 proves the asserted expression \(\alpha_k/c=(1+t)^2B_k/[m(m-1)]\).

**4. Isotropic constrained Hessian.** The functional \(F\) is symmetric and separately affine in each parameter. At the all-\(q\) point all first partial derivatives coincide, all pure second derivatives vanish, and each off-diagonal second partial derivative equals \(\alpha_k\) by step 2. For \(p_i=q+\varepsilon v_i\), therefore,
\[
 F(p)=\varepsilon L\sum_i v_i+\alpha_k\varepsilon^2\sum_{i<j}v_iv_j+O_{k,v}(|\varepsilon|^3).
\]
The mean-preserving constraint kills the linear term, and \(2\sum_{i<j}v_iv_j=-\sum_i v_i^2\) gives the second-order formula. For a pure opposite-pair direction all terms of degree three and above vanish exactly, as already proved.

**5. Compensating mean.** Let \(H(\varepsilon,h)=F(q+\varepsilon v_1+h/m,\ldots,q+\varepsilon v_m+h/m)\). At the base point, \(H(0,0)=0\). At homogeneous parameter \(q\), the ratio of binomial atoms is
\[
 \frac{\Pr(\operatorname{Bin}(m,q)=k+2)}{\Pr(\operatorname{Bin}(m,q)=k)}
 =\frac{(m-k)(m-k-1)}{(k+1)(k+2)}\left(\frac{q}{1-q}\right)^2=1.
\]
Differentiating this ratio at equality, and recalling that increasing \(h\) increases each success probability by \(h/m\), gives
\[
 \partial_hH(0,0)=\frac{2c}{mq(1-q)}>0.
\]
The analytic implicit-function theorem supplies a unique analytic local root \(h_k(\varepsilon,v)\). Its constant and linear terms vanish. Matching second-order coefficients in steps 4 and 5 gives \(h=\alpha_kmq(1-q)\varepsilon^2\sum_i v_i^2/(4c)+O_{k,v}(|\varepsilon|^3)\). Substituting the identity from step 3 and \(q(1-q)=t/(1+t)^2\) yields \(C_k=tB_k/[4(m-1)]>0\).

**6. Large-level coefficient.** From the integer staircase in [1, Lemma 6], \(d=\sqrt{k/8}+O(1)\). Write \(A=\sqrt{(k+1)(k+2)}\), \(H=\sqrt{d(d-1)}\), so \(1/t=H/A\). As \(k\to\infty\), \(d\asymp\sqrt k\), and the elementary expansions
\[
 H=d-\frac12-\frac1{8d}+O(d^{-2}),\qquad A=k+\frac32+O(k^{-1})
\]
imply
\[
 \frac{4(k-d+2)}t=4d-2-\frac{4d^2}{k}+O(k^{-1/2}),\qquad
 \frac{k(k-1)}{t^2}=d^2-d-\frac{4d^2}{k}+O(k^{-1/2}).
\]
Substitute these into the definition of \(B_k\) to obtain \(B_k=4+O(k^{-1/2})\). Meanwhile \(t=A/H\sim\sqrt{8k}\) and \(m-1\sim k\), hence
\[
 C_k=\frac{tB_k}{4(m-1)}\sim\sqrt{\frac8k},
\]
which yields the stated limit. The cancellation of the order-\(d^2\) and order-\(d\) terms is essential: replacing the staircase by a fixed excess trial count would give the wrong scaling. This completes the proof.

## Verification

The standalone \(\texttt{check.py}\) uses 80-digit decimal arithmetic to construct binomial distributions by convolution. It checks the boundary tie, positivity, exact opposite-pair identity, coefficient-ratio formula, and mean-compensation coefficient at 85 successive levels. It also checks finite directional-Hessian approximations at five levels and the large-level scaling at four additional levels, for a total of 438 passing assertions. Execute with Python 3.10 or later using \(\texttt{python check.py}\), without additional packages. The numerical checks are reproducibility aids; no finite sample of parameter values substitutes for the proof, and the inherited uniqueness statement is a cited theorem rather than a numerical inference.

## Relationship to prior work

Kleiner [1] supplies the **critical mean, staircase extremizer, and uniqueness of boundary ties**. In particular its equality classification entails strict heterogeneity loss qualitatively. The present result identifies the exact finite perturbation law along opposite pairs, the isotropic constrained Hessian, the exact compensating mean coefficient, and the sharp large-level constant. These quantitative claims are not asserted to appear in [1]. Gnedin [2, Section 7] studies changing modes by *adding new random increments* to a fixed base law; that optimization differs from preserving the number and total mean of the active Bernoulli coordinates. Pitman [3] is relevant background for real-rooted polynomial coefficient inequalities; full-text equivalence to the quantitative expansion has not been excluded.

## Limitations

The claimed penalty is exact globally only along one opposite-pair segment. For general heterogeneous directions it is a local expansion with nonuniform constants in \(k\) and \(v\). The compensating equality crossing exists and is unique only locally; no global optimizer under a prescribed variance or diversity constraint is determined. No claim is made for \(k=0\), where the predecessor's uniqueness is false, for growing direction vectors, or for arbitrary gap sizes. Originality is qualified by the possibility of a classical equivalent quantitative sensitivity formula not uncovered in the literature comparison.

## References

[1] I. Kleiner, *Why Distance Two Is Exceptional for Poisson–Binomial Point Probabilities*, arXiv:2610.10664v1 (first public 2026-10-07), Theorem 1, Lemma 6, Proposition 7, and Sections 5–7. https://arxiv.org/html/2610.10664v1

[2] A. Gnedin, *Cross Modality of the Extended Binomial Sums*, arXiv:2408.06477v1 (2024), especially Section 7 on breaking the mode. https://arxiv.org/html/2408.06477v1

[3] J. Pitman, *Probabilistic bounds on the coefficients of polynomials with only real zeros*, Journal of Combinatorial Theory Series A 77 (1997), 279–303.

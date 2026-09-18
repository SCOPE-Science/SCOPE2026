# Compactness rigidity for Arazy divided-difference Schur multipliers

## Statement

Let \(0<\alpha,r<\infty\), \(0<p,q\le\infty\), and use \(1/\infty=0\). Let
\(f\in C^1([-1,1])\) satisfy
\[
f(0)=0,\qquad |f'(t)|\le C_f |t|^\alpha\quad(-1\le t\le1),
\]
and let \(\lambda=(\lambda_j)_{j\ge1}\in \ell^r\) be real with
\(\|\lambda\|_\infty\le1\). Put \(H_\lambda e_j=\lambda_j e_j\), and define the
divided-difference matrix
\[
\Psi_{f,\lambda}(j,k)=
\begin{cases}
\dfrac{f(\lambda_j)-f(\lambda_k)}{\lambda_j-\lambda_k},&\lambda_j\ne\lambda_k,\\[1ex]
f'(\lambda_j),&\lambda_j=\lambda_k.
\end{cases}
\]
Assume the sharp Huang--Sukochev boundedness condition
\[
\frac1p\le \frac{\alpha}{r}+\min\!\left\{1,\frac1q\right\}.
\tag{1}
\]
Then the bounded Schur multiplier
\[
S_{\Psi_{f,\lambda}}:\mathcal S^q\longrightarrow \mathcal S^p
\]
is compact if and only if
\[
\boxed{f(H_\lambda)=0,}
\tag{2}
\]
equivalently \(f(\lambda_j)=0\) for every \(j\).

Moreover, for every index \(i\) with \(\lambda_i\ne0\),
\[
\boxed{\ \|S_{\Psi_{f,\lambda}}\|_{\mathrm{ess}}
   \ge \left|\frac{f(\lambda_i)}{\lambda_i}\right|,\ }
\tag{3}
\]
where the essential distance is taken in the operator (quasi-)norm from
\(\mathcal S^q\) to \(\mathcal S^p\). Hence
\[
\|S_{\Psi_{f,\lambda}}\|_{\mathrm{ess}}
\ge \sup_{\lambda_i\ne0}\left|\frac{f(\lambda_i)}{\lambda_i}\right|.
\tag{4}
\]

Here \(\mathcal S^\infty=\mathcal K(\ell^2)\), in the convention of the source
paper.

## Proof

### Necessity and the essential-norm obstruction

Suppose \(f(\lambda_i)\ne0\) for some \(i\). Since
\(\lambda\in\ell^r\), one has \(\lambda_k\to0\), and a nonzero value
\(\lambda_i\) can occur only finitely often. Therefore, along all sufficiently
large \(k\),
\[
\Psi_{f,\lambda}(i,k)
 =\frac{f(\lambda_i)-f(\lambda_k)}{\lambda_i-\lambda_k}
 \longrightarrow \frac{f(\lambda_i)}{\lambda_i}=:c\ne0.
\tag{5}
\]
Let \(x_k=e_{ik}\). Each \(x_k\) has \(\mathcal S^q\)-norm \(1\), while
\[
S_{\Psi_{f,\lambda}}x_k=\Psi_{f,\lambda}(i,k)e_{ik}.
\]
For \(k\ne\ell\), the operator
\(a e_{ik}-b e_{i\ell}\) has exactly one nonzero singular value,
\((|a|^2+|b|^2)^{1/2}\). Thus the images of a tail of \((x_k)\) are uniformly
separated in every \(\mathcal S^p\), and the multiplier is not compact.

The same argument gives (3). If \(K:\mathcal S^q\to\mathcal S^p\) is compact,
choose a subsequence for which \(Kx_k\) converges. On differences along this
subsequence,
\[
\frac{\|(S_{\Psi_{f,\lambda}}-K)(x_k-x_\ell)\|_p}
     {\|x_k-x_\ell\|_q}
\longrightarrow |c|,
\]
because both numerator and denominator contributed by the Schur multiplier have
the common rank-one factor \(\sqrt2\), whereas
\(\|Kx_k-Kx_\ell\|_p\to0\). Taking the infimum over compact \(K\) proves (3).

Consequently compactness forces \(f(\lambda_j)=0\) for every \(j\).

### Sufficiency

Assume now \(f(\lambda_j)=0\) for all \(j\). If
\(\lambda_j\ne\lambda_k\), then \(\Psi_{f,\lambda}(j,k)=0\).
For each distinct nonzero value \(t_m\) taken by \(\lambda\), let \(P_m\) be
the coordinate projection onto \(\{j:\lambda_j=t_m\}\) and put
\(d_m=f'(t_m)\). Every \(P_m\) has finite rank, because
\(\lambda\in\ell^r\). Also \(f'(0)=0\). Hence
\[
S_{\Psi_{f,\lambda}}(A)=\sum_m d_m P_m A P_m.
\tag{6}
\]

Set
\[
s=\begin{cases}\max\{q,1\},&q<\infty,\\ \infty,&q=\infty.\end{cases}
\]
The inclusion \(\mathcal S^q\hookrightarrow\mathcal S^s\) is contractive, and
the block pinching
\[
\mathcal E(A)=\sum_m P_mAP_m
\]
is contractive on \(\mathcal S^s\) (and on \(\mathcal K\) when \(s=\infty\)).
Let
\[
D=\sum_m |d_m|P_m,\qquad
V=\sum_m \operatorname{phase}(d_m)P_m.
\]
Then
\[
S_{\Psi_{f,\lambda}}(A)
   = V D^{1/2}\mathcal E(A)D^{1/2}.
\tag{7}
\]

If \(p<s\), define \(t>0\) by
\[
\frac1t=\frac1p-\frac1s.
\]
Condition (1) is exactly \(1/t\le\alpha/r\), so \(\alpha t\ge r\). Since
\(|\lambda_j|\le1\),
\[
\operatorname{Tr}(D^t)
 =\sum_j |f'(\lambda_j)|^t
 \le C_f^t\sum_j|\lambda_j|^{\alpha t}<\infty.
\tag{8}
\]
Thus \(D\in\mathcal S^t\). Schatten Hölder gives
\[
\|D^{1/2}\mathcal E(A)D^{1/2}\|_p
 \le \|D\|_t\,\|\mathcal E(A)\|_s.
\tag{9}
\]
Truncating \(D\) to finitely many of the finite-dimensional spectral blocks
produces finite-rank maps, and (9) applied to the tail shows convergence in the
operator quasi-norm \(\mathcal S^q\to\mathcal S^p\). Hence the multiplier is
compact.

If \(p\ge s\), then either only finitely many nonzero values \(t_m\) occur, or
\(t_m\to0\). In the latter case
\[
|d_m|=|f'(t_m)|\le C_f|t_m|^\alpha\longrightarrow0.
\]
After truncation to finitely many blocks, the tail satisfies
\[
\left\|\sum_{m>N}d_mP_mAP_m\right\|_p
 \le \sup_{m>N}|d_m|\,\|A\|_s
 \le \sup_{m>N}|d_m|\,\|A\|_q,
\tag{10}
\]
using pinching contractivity and \(\mathcal S^s\hookrightarrow\mathcal S^p\).
Again the finite-block truncations are finite-rank maps and the tail norm tends
to zero. This proves compactness.

Combining the two directions proves (2).

## Interpretation

Huang and Sukochev recently completed the sharp boundedness classification:
for every admissible \(f\) and \(\lambda\), the multiplier
\(\mathcal S^q\to\mathcal S^p\) is bounded exactly in the exponent region (1).
The theorem above shows that compactness inside that entire region is instead
rigid and spectral: it occurs exactly when \(f\) vanishes on the spectrum of
\(H_\lambda\) (with multiplicity irrelevant).

The obstruction is not failure of the symbol to decay when both indices go to
infinity. A single nonzero spectral point produces an asymptotically constant
row through (5), and this fixed row alone prevents compactness. Conversely,
when \(f(H_\lambda)=0\), all off-block divided differences disappear and the
multiplier collapses to a weighted finite-spectral pinching; the same exponent
boundary supplies precisely the Schatten summability needed for compact
approximation.

For example,
\[
f(t)=\frac{t|t|^\alpha}{\alpha+1}
\quad\text{satisfies}\quad f'(t)=|t|^\alpha.
\]
For every nonzero \(\lambda\in\ell^r\), the corresponding multiplier is bounded
throughout (1) but is never compact.

## Relation to prior work

Huang--Sukochev (2026) prove the sharp boundedness classification used in
(1), extending the earlier Arazy and Potapov--Sukochev--Tomskova results to all
quasi-Banach Schatten indices. Their inspected v1 formulates the problem and
main theorem in terms of boundedness; a full-text search for compactness finds
background/reference occurrences but no compactness classification for this
divided-difference family.

There is substantial older theory of compact Schur multipliers in other
settings. Hladnik (2000) characterizes compact Schur multipliers on
\(B(H)\) using \(c_0\otimes_h c_0\); Stout (1981) relates compact Schur
multiplication in suitable bases to essential numerical range; Andersson (2005)
gives a factorization theorem for compact Schur multipliers. These results are
important prior-art risks, especially for the endpoint \(\mathcal S^\infty\),
but the located statements do not give the fixed-basis, unequal-exponent
Schatten/quasi-Schatten divided-difference criterion above.

## Limitations

The result assumes the Huang--Sukochev universal boundedness region (1).
Outside that region a particular pair \((f,\lambda)\) can still define a bounded
multiplier, and no complete compactness classification for all such exceptional
pairs is claimed. The theorem concerns ordinary compactness of the linear map;
it does not claim complete compactness. It also concerns the discrete
Schatten setting of a compact diagonal \(H_\lambda\), not the atomless
semifinite extension discussed in the source paper.

## References

1. J. Huang and F. Sukochev, *Arazy's conjecture concerning Schur multipliers:
   revisited and resolved*, arXiv:2609.17144v1 (2026).
   https://arxiv.org/abs/2609.17144
2. D. Potapov, F. Sukochev, A. Tomskova, *On the Arazy conjecture concerning
   Schur multipliers on Schatten ideals*, Adv. Math. 268 (2015), 404--422.
   https://doi.org/10.1016/j.aim.2014.09.021
3. M. Hladnik, *Compact Schur multipliers*, Proc. Amer. Math. Soc. 128 (2000),
   2585--2591. https://doi.org/10.1090/S0002-9939-00-05708-7
4. Q. F. Stout, *Schur products of operators and the essential numerical
   range*, Trans. Amer. Math. Soc. 264 (1981), 39--47.
   https://doi.org/10.1090/S0002-9947-1981-0597865-2
5. M. E. Andersson, *Integrable factors in compact Schur multipliers*,
   Proc. Amer. Math. Soc. 133 (2005), 1469--1473.
   https://doi.org/10.1090/S0002-9939-04-07670-1
6. F. Sukochev and A. Tomskova, *\( (E,F) \)-Schur multipliers and
   applications*, Studia Math. 216 (2013), 111--129.
   https://doi.org/10.4064/sm216-2-2
7. A. B. Aleksandrov and V. V. Peller, *Schur multipliers of
   Schatten--von Neumann classes \(S_p\)*, J. Funct. Anal. 279 (2020),
   108683. https://doi.org/10.1016/j.jfa.2020.108683

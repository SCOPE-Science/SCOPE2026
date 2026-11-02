# Sharp spectral-projection growth for compact generalized Cesàro operators on \(\ell^p\)

## Finding
For \(0\le t<1\), let \(C_t\) on complex \(\ell^p(\mathbb N_0)\), \(1\le p<\infty\), be defined by
\[
(C_tx)_n=\frac{1}{n+1}\sum_{j=0}^n t^{n-j}x_j.
\]
The eigenvalue \(\lambda_m=1/(m+1)\), for \(m=0,1,\ldots\), is simple, and its rank-one Riesz spectral projection \(P_m\) has the **exact norm**
\[
\|P_m\|_{p\to p}
=\left(\sum_{j\ge0}\binom{m+j}{m}^{p}t^{pj}\right)^{1/p}
\left(\sum_{k=0}^{m}\binom{m}{k}^{q}t^{q(m-k)}\right)^{1/q},
\qquad \frac1p+\frac1q=1.
\]
Interpret the second factor as a maximum when \(p=1\), hence \(q=\infty\). At \(t=0\), all these projection norms equal \(1\). For every **fixed** \(0<t<1\), the sharp large-index law is
\[
\boxed{\displaystyle
\|P_m\|_{p\to p}\sim
\frac{p^{-1/(2p)}q^{-1/(2q)}}{\sqrt{2\pi mt}}
\left(\frac{1+t}{1-t}\right)^{m+1/p},\quad m\longrightarrow\infty,}
\]
with the convention \(\infty^{-1/\infty}=1\). This law is also valid for \(p=\infty\), using the supremum in the first factor and \(q=1\). For \(p=1\) specifically,
\[
\|P_m\|_{1\to1}=(1-t)^{-(m+1)}
\max_{0\le k\le m}\binom{m}{k}t^{m-k}.
\]
For every \(1\le p<\infty\), the eigenvectors are complete and minimal, but when \(t>0\) they fail to be a Schauder basis in **any ordering**. At \(t=0\), they are the canonical basis. Thus simplicity and completeness of the point spectrum coexist with exponentially ill-conditioned spectral projections.

## Assumptions and scope
The underlying field is \(\mathbb C\), the Banach norm on \(\ell^p\) is the standard coordinate norm, the coordinate index begins at zero, and the fixed parameter \(t\) is real in \([0,1)\). When an exponent equals infinity, its corresponding sum-norm is the supremum norm. No asymptotic uniformity in \(p\) or \(t\) is asserted. The stated completeness and Schauder-basis dichotomy concern \(1\le p<\infty\); the norm formula and asymptotic additionally hold on \(\ell^\infty\).

## Proof
**1. Compactness and nonzero eigenvalues.** Write \(S\) for the unilateral right shift and \(D\) for the diagonal map \((Dx)_n=x_n/(n+1)\). Then \(C_t=D(I-tS)^{-1}\), where the inverse is a norm-convergent Neumann series. Since \(D\) is compact on all the stated sequence spaces, so is \(C_t\). If an eigenvector has its first nonzero coordinate at \(m\), the triangular matrix yields eigenvalue \(1/(m+1)\), and the later coordinates are uniquely determined. The nonzero spectrum is therefore precisely the listed eigenvalues.

**2. Right and left eigenvectors.** The binomial convolution identity, or a coefficient comparison in \((1-tz)^{-(m+1)}\), verifies that
\[
v^{(m)}_n=\begin{cases}\binom nm t^{n-m},&n\ge m,\\0,&n<m,\end{cases}
\qquad
w^{(m)}_k=\begin{cases}\binom mk(-t)^{m-k},&k\le m,\\0,&k>m,\end{cases}
\]
satisfy \(C_tv^{(m)}=\lambda_mv^{(m)}\) and \(w^{(m)}C_t=\lambda_mw^{(m)}\), where \(w^{(m)}\) is a bounded coordinate functional. Their pairing equals \(1\), since the only overlapping coordinate is \(m\). Distinct eigenvalues force \(w^{(m)}(v^{(j)})=0\) for \(j\ne m\).

The eigenspace is one-dimensional. A nontrivial Jordan chain of length two would require \((C_t-\lambda_mI)u=v^{(m)}\); applying \(w^{(m)}\) gives \(0=1\). Therefore \(\lambda_m\) has algebraic multiplicity one and the Riesz spectral projection is exactly \(P_mx=w^{(m)}(x)v^{(m)}\).

**3. Exact norm.** Rank-one operator duality gives \(\|P_m\|=\|v^{(m)}\|_p\|w^{(m)}\|_q\), including the endpoint interpretations. Inserting the coordinates proves the two-factor identity. For \(p=1\), use the negative-binomial series \(\sum_{j\ge0}\binom{m+j}{m}t^j=(1-t)^{-(m+1)}\). When \(t=0\), the two vectors are coordinate vectors, so the norm is \(1\).

**4. Sharp Gaussian constant.** Assume fixed \(t\in(0,1)\). Set
\[
\pi_m(j)=(1-t)^{m+1}\binom{m+j}{m}t^j,
\quad
\beta_m(k)=(1+t)^{-m}\binom mk t^{m-k}.
\]
These are, respectively, the negative-binomial probability law counting failures before \(m+1\) successes (success probability \(1-t\)) and the binomial law with \(m\) trials and success probability \(1/(1+t)\). Their variances are
\[
\sigma_{\pi,m}^2=\frac{(m+1)t}{(1-t)^2},\qquad
\sigma_{\beta,m}^2=\frac{mt}{(1+t)^2}.
\]
For either lattice law \(a_m\), with variance \(\sigma_m^2\to\infty\) and these fixed parameters, Stirling's formula yields a uniformly Gaussian central window. Standard exponential tail estimates dominate the complement. Consequently, for any fixed \(1\le r<\infty\),
\[
\left(\sum_j a_m(j)^r\right)^{1/r}
=(2\pi\sigma_m^2)^{-(r-1)/(2r)}r^{-1/(2r)}(1+o(1)),
\]
where for \(r=1\) the assertion is exactly normalization. The maximum atom (\(r=\infty\)) is \((2\pi\sigma_m^2)^{-1/2}(1+o(1))\). Since \(\|v^{(m)}\|_p=(1-t)^{-(m+1)}\|\pi_m\|_p\) and \(\|w^{(m)}\|_q=(1+t)^m\|\beta_m\|_q\), multiplying these estimates, using \(1/p+1/q=1\) and \(m+1\sim m\), gives the boxed asymptotic exactly, including its \(p\)-dependent leading coefficient. The growth factor is strictly larger than one for \(t>0\).

**5. Complete but not Schauder.** For \(1\le p<\infty\), suppose \(y\in\ell^q\) annihilates every \(v^{(m)}\). Its generating function \(F(z)=\sum_{n\ge0}y_nz^n\) is analytic in \(|z|<1\) by Hölder's inequality (also when \(q=\infty\)). For each \(m\), the equality \(F^{(m)}(t)/m!=\langle y,v^{(m)}\rangle=0\) holds. Thus \(F\equiv0\), so \(y=0\); Hahn–Banach proves completeness. The biorthogonal finite coordinate functionals \(w^{(m)}\) prove minimality. In any Schauder basis, the one-coordinate projections are uniformly bounded by twice its basis constant. But these same unique coordinate projections equal \(P_m\), whose norms diverge exponentially for \(t>0\). Hence no ordering is a Schauder basis.

## Verification
The included standard-library script `check.py` checks finite-section eigenvalue equations, left and right eigenvectors, commutation, projection idempotence and endpoint rank-one norms using exact fractions for all \(1\le N\le8\), all \(0\le m<N\) and five rational parameters. It also provides selected finite-size comparisons to the asymptotic formula. Run `python3 check.py`. The finite-section checks are not a substitute for the general analytic proof or the local-limit estimates.

## Relationship to prior work
Albanese, Bonet and Ricker (2023) explicitly derive the same right eigenvectors and dual eigenvectors, and establish compactness and point spectra; those facts are **not** claimed as new. Yıldırım and Durna (2017) establish compactness and spectral results on \(\ell^p\). The specific added claim here is the complete sharp \(p\)-dependent family of Riesz-projection norm asymptotics, including the exponential prefactor and complete-but-non-Schauder eigenvector behavior. This compares quantitative spectral conditioning, not just eigenvalues or eigenvector formulas. The accessible 2020 treatment of neighboring endpoint spaces did not allow a whole-text implication comparison; see limitations.

## Limitations
No independence certification or external mathematical assessment has been performed. The local-limit proof covers fixed positive \(t\) and fixed exponent only, and does not address \(t\) tending to zero with \(m\). In \(\ell^\infty\) the eigenvectors lie in \(c_0\), so the density claim is intentionally excluded. Earlier equivalent eigenbasis or spectral-projection norm estimates under binomial-transform, terraced-matrix or Pascal-operator terminology could exist. In particular, the full text of Sawano–El-Shabrawy (2020), on closely related endpoint spaces, was not available for comparison.

## References
1. A. A. Albanese, J. Bonet, W. J. Ricker, *Spectral properties of generalized Cesàro operators in sequence spaces*, RACSAM 117 (2023), article 140, https://doi.org/10.1007/s13398-023-01470-2 ; earliest preprint https://arxiv.org/abs/2305.04805 (8 May 2023). See §§3 and 6 for eigenvectors and dual eigenvectors.
2. M. Yıldırım, N. Durna, *The spectrum and some subdivisions of the spectrum of discrete generalized Cesàro operators on* \(\ell^p\), J. Inequal. Appl. 2017 (2017), 193, https://doi.org/10.1186/s13660-017-1464-2 .
3. Y. Sawano, S. R. El-Shabrawy, *Fine spectra of the discrete generalized Cesàro operator on Banach sequence spaces*, Monatsh. Math. 192 (2020), 185–224, https://doi.org/10.1007/s00605-020-01376-w (abstract and accessible preview inspected; full text not inspected).

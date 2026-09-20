# Square-root Rankin–Cohen independence for quadratic twists

## Result

Let \(D\) be a fixed odd fundamental discriminant, with \(D=1\) permitted, and let
\[
\mathcal F^{(D)}_{\ell,e}
=\operatorname{Tr}^{|D|}_1 [G_{\ell-2e,D},G_{\ell-2e,D}]_{2e}
\in S_{2\ell}(\mathrm{SL}_2(\mathbb Z)).
\]
Assume \((-1)^\ell D>0\). Put
\[
V_{\ell,D}=\operatorname{Span}_{\mathbb C}\{f\in\mathcal B_{2\ell}:L(f\otimes\chi_D,\ell)\ne0\},
\]
where \(\mathcal B_{2\ell}\) is the normalized level-one Hecke eigenbasis.

**Theorem.** For every fixed
\[
0<c<(2\pi e|D|)^{-1/2},
\qquad r_\ell=\lfloor c\sqrt\ell\rfloor,
\]
the forms
\[
\mathcal F^{(D)}_{\ell,1},\ldots,\mathcal F^{(D)}_{\ell,r_\ell}
\]
are linearly independent for all sufficiently large admissible \(\ell\). Consequently
\[
\dim V_{\ell,D}\ge r_\ell
\]
and therefore
\[
\boxed{
\liminf_{\substack{\ell\to\infty\\(-1)^\ell D>0}}
\frac{\#\{f\in\mathcal B_{2\ell}:L(f\otimes\chi_D,\ell)\ne0\}}{\sqrt\ell}
\ge \frac1{\sqrt{2\pi e|D|}}.}
\]

Takloo-Bighash proved the same linear independence for every *fixed* number \(r\) of brackets. The theorem above lets the number of brackets grow at the square-root scale and gives an explicit lower constant.

## Proof

Write \(k_e=\ell-2e\). If
\[
\mathcal F_{D,k,e}(z)=\sum_{n\ge1}A_{D,k,e}(n)q^n,
\qquad B_{k,e}=\binom{k+2e-1}{2e},
\]
Takloo-Bighash's Proposition 3.1 gives, with \(M=n|D|\),
\[
\left|
\frac{A_{D,k,e}(n)}{B_{k,e}L_D(1-k)}
-n^{2e}\sigma_{k-1,D,1}(n)
\right|
\le
\frac{\zeta(2)}2\nu(D)C_eM^{2e+1}|D|^{1/2}
\frac{(2\pi M^2/|D|)^k}{\Gamma(k)},
\]
where
\[
C_e=\left(\frac{2e+3}{2}\right)^{2e}.
\]
The point is that this explicit inequality can be used uniformly when \(e\) and the Fourier index grow with \(\ell\).

For \(1\le e,n\le r\), form the normalized coefficient matrix
\[
M_{\ell,r}(e,n)
=
\frac{A_{D,k_e,e}(n)}{\binom{\ell-1}{2e}L_D(1-k_e)}
=E_{e,n}+R_{e,n}.
\]
The endpoint term is
\[
E_{e,n}=n^{2e}\sigma_{k_e-1,D,1}(n)
=\sum_{ab=n}\chi_D(a)a^{\ell-1}b^{2e}.
\]
Thus, with the completely multiplicative function
\[
a_\ell(d)=\chi_D(d)d^{\ell-1},
\]
we have \(E_e=a_\ell*\operatorname{id}^{2e}\) as a Dirichlet convolution. Its Dirichlet inverse is
\[
b_\ell(d)=\mu(d)\chi_D(d)d^{\ell-1}.
\]
This remains true at primes dividing \(D\), where \(\chi_D\) vanishes.

Apply the triangular column transformation
\[
\widetilde C_n=\sum_{d\mid n}b_\ell(d)C_{n/d},\qquad 1\le n\le r.
\]
Its diagonal entries are \(b_\ell(1)=1\), so its determinant is one. Dirichlet inversion gives the exact transformed endpoint matrix
\[
W_r=(n^{2e})_{1\le e,n\le r}.
\]
In particular,
\[
\det W_r
=\left(\prod_{n=1}^r n^2\right)
\prod_{1\le i<j\le r}(j^2-i^2)\ne0.
\]
The advantage over a fixed-prime determinant limit is that the arithmetical divisor term has disappeared exactly before any perturbation estimate is made.

We now bound the transformed error. From the explicit estimate above, after multiplying the error at \(n/d\) by \(|b_\ell(d)|\), the power of \(d\) is
\[
d^{\ell-1-(2\ell-2e+1)}=d^{-k_e-2}.
\]
Hence the divisor sum is bounded by \(\zeta(k_e+2)\). For fixed \(D\), whenever \(k_e\ge4\), there is a constant \(K_D>0\) such that, uniformly for \(1\le e,n\le r\),
\[
|\widetilde R_{e,n}|
\le
\eta_{\ell,r}:=
K_D\,r\left(\frac{2r+3}{2}\right)^{2r}
\frac{(2\pi |D|r^2)^\ell}{\Gamma(\ell-2r)}.
\tag{1}
\]

It remains to control the inverse of \(W_r\) without paying a determinant-sized condition-number loss. Put \(x_n=n^2\) and write
\[
W_r=V_r\operatorname{diag}(x_1,\ldots,x_r),
\qquad (V_r)_{e,n}=x_n^{e-1}.
\]
The entries of \(V_r^{-1}\) are coefficients of the Lagrange polynomials
\[
L_n(x)=\prod_{m\ne n}\frac{x-x_m}{x_n-x_m}.
\]
Therefore every such entry is at most
\[
\frac{\prod_{m\ne n}(1+m^2)}{\prod_{m\ne n}|n^2-m^2|}
\le 2^r(r!)^2.
\]
Since \(x_n^{-1}\le1\),
\[
\|W_r^{-1}\|_\infty\le r\,2^r(r!)^2.
\tag{2}
\]
The transformed error matrix has \(\infty\)-norm at most \(r\eta_{\ell,r}\). Thus
\[
\|W_r^{-1}\widetilde R\|_\infty
\le r^2 2^r(r!)^2\eta_{\ell,r}.
\tag{3}
\]

Take \(r=\lfloor c\sqrt\ell\rfloor\). The prefactor in (3), together with \(C_r\), contributes only \(\exp(O(\sqrt\ell\log\ell))\). Stirling's formula applied to (1) gives
\[
\frac1\ell\log\eta_{\ell,r}
\le
\log(2\pi |D|r^2)-\frac1\ell\log\Gamma(\ell-2r)+o(1)
=
\log(2\pi e|D|c^2)+o(1).
\]
If \(c<(2\pi e|D|)^{-1/2}\), the last quantity is negative by a fixed amount. Hence the right-hand side of (3) tends to zero exponentially in \(\ell\). For all sufficiently large admissible \(\ell\),
\[
\|W_r^{-1}\widetilde R\|_\infty<1,
\]
so \(I+W_r^{-1}\widetilde R\) is invertible. Consequently \(W_r+\widetilde R\), and hence the original coefficient matrix \(M_{\ell,r}\), is nonsingular. This proves the growing linear independence.

Finally, the Petersson formula used by Kayath--Lane--Neifeld--Ni--Xue and Takloo-Bighash has the form
\[
\langle \mathcal F^{(D)}_{\ell,e},f\rangle
=C_{D,\ell,e}L(f,2\ell-2e-1)L(f\otimes\chi_D,\ell),
\qquad C_{D,\ell,e}\ne0.
\]
Thus every \(\mathcal F^{(D)}_{\ell,e}\) lies in \(V_{\ell,D}\). The \(r\) independent brackets force \(\dim V_{\ell,D}\ge r\), completing the proof.

## Context and significance

Takloo-Bighash's September 2026 theorem fixes \(r\) while \(\ell\to\infty\), and its effective determinant argument chooses a fixed set of prime Fourier indices. The present argument instead uses all indices \(1,\ldots,r\) and a determinant-preserving Möbius transform that exactly strips off the divisor-sum endpoint. This converts the main matrix to an ordinary Vandermonde and allows the explicit Fourier-coefficient error estimate to remain usable when \(r\) grows like \(\sqrt\ell\).

Kayath--Lane--Neifeld--Ni--Xue describe the broader problem of understanding the dimension of the subspace generated by eigenforms with nonvanishing twisted central values and discuss a conjectural linear-size Rankin--Cohen family. The square-root theorem above does not reach that conjectural linear regime, but it gives a quantitative growing family for every fixed odd fundamental discriminant covered here.

For \(D=1\), Luo's 2015 theorem already gives the stronger nonvanishing count \(\dim V_{\ell,1}\gg\ell\). Thus the new quantitative nonvanishing consequence is principally relevant for nontrivial fixed \(D\); for \(D=1\), the new content is the square-root linear independence of this explicit Rankin--Cohen family.

## Verification

`artifacts/verify_mobius_vandermonde.py` checks the exact Dirichlet-inversion column identity and the Vandermonde determinant over the integers for both the trivial character and the quadratic character modulo 5, including indices divisible by 5 where the character vanishes. `artifacts/verification.txt` records its deterministic output. These checks corroborate the exact algebraic step; the asymptotic conclusion uses the proof above.

## Limitations

The discriminant \(D\) is fixed and odd. The result does not give uniformity as \(|D|\) grows, does not reach a positive proportion of the full weight-\(2\ell\) eigenbasis, and does not claim that the constant \((2\pi e|D|)^{-1/2}\) is optimal. It uses the explicit error estimate of Takloo-Bighash and therefore naturally encounters a square-root barrier when the largest Fourier index is comparable with \(\sqrt\ell\). The result does not settle the full linear-independence conjectures discussed by Kayath--Lane--Neifeld--Ni--Xue.

Originality is asserted only to the best of our knowledge. The motivating preprint is very recent, so unindexed concurrent work remains a residual risk.

## References

1. R. Takloo-Bighash, *Simultaneous nonvanishing of quadratic twists via Rankin-Cohen brackets*, arXiv:2609.19649v1 (2026). https://arxiv.org/abs/2609.19649
2. J. Kayath, C. Lane, B. Neifeld, T. Ni, H. Xue, *Subspaces spanned by eigenforms with nonvanishing twisted central L-values*, Canadian Journal of Mathematics (2025), DOI 10.4153/S0008414X25101697. https://arxiv.org/abs/2407.00532
3. T. Ni, H. Xue, *Twisted periods of modular forms*, Nagoya Mathematical Journal 261 (2026), e18, DOI 10.1017/nmj.2026.10099. https://arxiv.org/abs/2507.17041
4. W. Luo, *Nonvanishing of the central L-values with large weight*, Advances in Mathematics 285 (2015), 220--234, DOI 10.1016/j.aim.2015.08.009.

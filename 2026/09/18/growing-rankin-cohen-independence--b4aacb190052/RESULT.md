# A growing block of traced Rankin--Cohen brackets is linearly independent

## Statement

Fix an odd fundamental discriminant \(D\), with \(D=1\) permitted. For every integer \(\ell\) satisfying
\[
(-1)^\ell D>0,
\]
and every \(e\ge 1\) with \(\ell-2e\ge4\), write
\[
\mathcal F^{(D)}_{\ell,e}
=
\operatorname{Tr}_1^{|D|}
[G_{\ell-2e,D},G_{\ell-2e,D}]_{2e}
\in S_{2\ell}(\mathrm{SL}_2(\mathbb Z)).
\]
Let \(r=r(\ell)\) be an integer-valued function such that
\[
 r\log(2r)=o(\sqrt\ell).
\]
Then, for all sufficiently large admissible \(\ell\), the forms
\[
\mathcal F^{(D)}_{\ell,1},\ldots,
\mathcal F^{(D)}_{\ell,r}
\]
are linearly independent.

Equivalently, the fixed-\(r\) theorem of Takloo-Bighash remains valid uniformly for a block whose length tends to infinity almost as fast as \(\sqrt\ell/\log\ell\). In particular, for every fixed \(\delta>0\), one may take
\[
r(\ell)=\left\lfloor
\frac{\sqrt\ell}{(\log\ell)^{1+\delta}}
\right\rfloor,
\]
and, for every fixed \(0<\varepsilon<1/2\), one may take
\[
r(\ell)=\lfloor \ell^{1/2-\varepsilon}\rfloor.
\]

By the Petersson formula used by Kayath--Lane--Neifeld--Ni--Xue and Takloo-Bighash, this also implies
\[
\#\{f\in\mathcal B_{2\ell}:
L(f\otimes\chi_D,\ell)\ne0\}\ge r(\ell)
\]
for the same admissible \(\ell\). For \(D=1\), stronger linear lower bounds for the number of nonvanishing forms are already known; the new content here is the growing-block linear independence of these explicit Rankin--Cohen forms.

## Quantitative determinant asymptotic

Let
\[
p_1<p_2<\cdots<p_r
\]
be the first \(r\) primes not dividing \(D\), put \(P=p_r\), and write
\[
\mathcal F^{(D)}_{\ell,e}(z)
=
\sum_{n\ge1}A_{D,\ell-2e,e}(n)q^n.
\]
Consider the normalized coefficient matrix
\[
M_{\ell,r}
=
\left(
\frac{A_{D,\ell-2e,e}(p_j)}
{\binom{\ell-1}{2e}L_D(1-\ell+2e)}
\right)_{1\le e,j\le r}.
\]
For \(x_j=p_j^2\), set
\[
w_j=(x_j,x_j^2,\ldots,x_j^r)^T,
\qquad
\mathbf1=(1,\ldots,1)^T,
\]
and
\[
\Delta_r=
\det(w_1,\ldots,w_{r-1},\mathbf1).
\]
Then, under \(r\log(2r)=o(\sqrt\ell)\),
\[
\boxed{
\det M_{\ell,r}
=
\chi_D(P)P^{\ell-1}\Delta_r\,(1+o(1)).
}
\]
Since \(\Delta_r\ne0\), this proves the theorem.

## Proof

Takloo-Bighash's explicit Fourier-coefficient estimate gives, with
\(k_e=\ell-2e\),
\[
\frac{A_{D,k_e,e}(p_j)}
{\binom{\ell-1}{2e}L_D(1-k_e)}
=
\chi_D(p_j)p_j^{\ell-1}+p_j^{2e}
+\epsilon_{e,j},
\]
where, writing \(M=p_j|D|\),
\[
|\epsilon_{e,j}|
\le
\frac{\zeta(2)}2\nu(D)C_eM^{2e+1}|D|^{1/2}
\frac{(2\pi M^2/|D|)^{k_e}}{\Gamma(k_e)},
\qquad
C_e=\left(\frac{2e+3}{2}\right)^{2e}.
\]
Although the asymptotic statement in that paper fixes \(e\) and \(p_j\), this displayed bound is explicit and can be estimated uniformly.

Let
\[
\eta_\ell=\max_{1\le e,j\le r}|\epsilon_{e,j}|.
\]
The prime number theorem gives
\[
P=O_D(r\log(2r)).
\]
Hence the hypothesis implies \(P^2=o(\ell)\). Uniformly for \(e,j\le r\), the displayed error estimate and Stirling's formula give
\[
\log\eta_\ell
\le
-\ell\log\frac{\ell}{P^2}
+O_D(\ell+r\log\ell+r\log P).
\]
Because \(\ell/P^2\to\infty\), this tends to \(-\infty\) faster than any error of size \(\exp(O(r^2\log P))\).

Now put
\[
v_j=\chi_D(p_j)p_j^{\ell-1}.
\]
The \(j\)-th column of \(M_{\ell,r}\) is
\[
v_j\mathbf1+w_j+\epsilon_j,
\]
where every coordinate of \(\epsilon_j\) has absolute value at most \(\eta_\ell\). If the \(\epsilon_j\) are temporarily omitted, multilinearity gives
\[
\det(w_1+v_1\mathbf1,\ldots,w_r+v_r\mathbf1)
=
\det(w_1,\ldots,w_r)
+
\sum_{j=1}^rv_j\Delta_j,
\]
where
\[
\Delta_j=
\det(w_1,\ldots,w_{j-1},\mathbf1,w_{j+1},\ldots,w_r).
\]
All terms containing two or more \(v_j\mathbf1\) vanish because they contain repeated columns.

The determinants \(\Delta_j\) are explicit Vandermonde determinants. In absolute value,
\[
|\Delta_j|
=
\left(\prod_{i\ne j}x_i\right)
\left(\prod_{\substack{a<b\\a,b\ne j}}|x_b-x_a|\right)
\left(\prod_{i\ne j}|x_i-1|\right).
\]
In particular \(\Delta_r\) is a nonzero integer, so \(|\Delta_r|\ge1\). For every \(j<r\), direct cancellation of the common Vandermonde factors yields
\[
\left|\frac{\Delta_j}{\Delta_r}\right|
=
\frac{x_r}{x_j}
\frac{x_r-1}{x_j-1}
\prod_{\substack{i<r\\i\ne j}}
\frac{|x_r-x_i|}{|x_j-x_i|}
\le P^{2r}.
\]
Similarly,
\[
\left|
\frac{\det(w_1,\ldots,w_r)}{\Delta_r}
\right|
=
x_r\prod_{i<r}\frac{x_r-x_i}{x_i-1}
\le P^{2r}.
\]
Consequently the determinant with the \(\epsilon_j\) omitted, divided by
\(v_r\Delta_r\), differs from \(1\) in absolute value by at most
\[
P^{2r-(\ell-1)}
+
rP^{2r}
\left(\frac{p_{r-1}}P\right)^{\ell-1}.
\]
Since \(p_{r-1}\le P-1\), the second term is at most
\[
r\exp\left(2r\log P-\frac{\ell-1}{P}\right).
\]
The condition \(r\log(2r)=o(\sqrt\ell)\), together with \(P=O_D(r\log(2r))\), implies
\[
\frac{\ell}{Pr\log P}\to\infty,
\]
so both error terms tend to zero.

It remains to restore the coefficient errors. A telescoping determinant expansion and Hadamard's inequality show that replacing any collection of the \(w_j\) by \(w_j+\epsilon_j\) changes each auxiliary determinant by at most
\[
\eta_\ell\exp(O(r^2\log P+r\log r)).
\]
The logarithmic estimate for \(\eta_\ell\) and
\(r^2(\log(2r))^2=o(\ell)\) show that this quantity is \(o(1/r)\). After multiplication by the \(v_j\), its total contribution remains \(o(|v_r\Delta_r|)\), because \(|\Delta_r|\ge1\). This proves the determinant asymptotic and hence linear independence.

## Context and significance

Kayath--Lane--Neifeld--Ni--Xue construct these traced Rankin--Cohen forms as an explicit spanning family for the subspace generated by Hecke eigenforms with nonvanishing twisted central values. Their Discussion formulates a much stronger basis conjecture extending to \(e\le\lfloor\ell/6\rfloor\), and notes computational verification in finite ranges. Takloo-Bighash subsequently proves linear independence for every fixed initial block \(1\le e\le r\), while explicitly keeping \(r\) fixed and not optimizing its dependence on \(\ell\).

The theorem above is a quantitative intermediate result: the provably independent initial block can grow with the weight, to size
\[
\frac{\sqrt\ell}{(\log\ell)^{1+\delta}}
\]
for every fixed \(\delta>0\). It remains far below the conjectural linear-size block \(\asymp\ell\), so it does not settle the basis conjecture.

## Limitations

The result fixes \(D\). No uniformity in a growing discriminant is claimed. The condition \(r\log(2r)=o(\sqrt\ell)\) is sufficient for the present argument, not claimed optimal. The proof uses Takloo-Bighash's explicit coefficient bound and the Kayath--Lane--Neifeld--Ni--Xue Petersson framework as established inputs. The nonvanishing corollary is not claimed to improve the best known counting theorem in every special case; in particular, for \(D=1\) the literature already contains a linear lower bound for the dimension of the nonvanishing subspace. No claim is made for the full conjectural range \(r\asymp\ell\).

## References

1. R. Takloo-Bighash, *Simultaneous nonvanishing of quadratic twists via Rankin--Cohen brackets*, arXiv:2609.19649v1 (2026).
2. J. Kayath, C. Lane, B. Neifeld, T. Ni, H. Xue, *Subspaces spanned by eigenforms with nonvanishing twisted central L-values*, Canadian Journal of Mathematics, online 3 October 2025, DOI 10.4153/S0008414X25101697.
3. T. Ni, H. Xue, *Twisted periods of modular forms*, Nagoya Mathematical Journal 261 (2026), e18.
4. W. Luo, *On simultaneous nonvanishing of the central L-values*, Proc. Amer. Math. Soc. 145 (2017), 4227--4231.

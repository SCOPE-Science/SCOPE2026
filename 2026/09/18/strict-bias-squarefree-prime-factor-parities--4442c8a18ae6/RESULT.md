# Strict bias for squarefree prime-factor parity vectors

## Statement

Let \(M\ge 3\), put \(m=\varphi(M)\), and assume \(m\ge 3\). Let
\(\rho_1,\dots,\rho_m\) be the reduced residue classes modulo \(M\). For a
squarefree integer \(N\) coprime to \(M\), let \(n_i(N)\) be the number of prime
divisors of \(N\) that are congruent to \(\rho_i\pmod M\).

Consider Tang's binary congruence setting: after reindexing, let
\(l_1=\cdots=l_h=2\) and \(l_{h+1}=\cdots=l_m=1\), with \(h\ge1\). For
\(a=(a_1,\dots,a_h)\in\mathbf F_2^h\), define
\[
 A_a(x)=\{N\le x:N\text{ squarefree},\ (N,M)=1,\ n_i(N)\equiv a_i\pmod2
 \text{ for }1\le i\le h\}.
\]

Because \(m=\varphi(M)\ge3\), in fact \(m\ge4\) and \(m\) is even.

**Theorem.** For every distinct \(a,b\in\mathbf F_2^h\), there exist integers
\[
 1\le r<\frac m2,\qquad \nu\ge0,
\]
and a nonzero real constant \(C_{a,b}\) such that
\[
 |A_a(x)|-|A_b(x)|
 \sim C_{a,b}\,x(\log x)^{-2r/m-\nu}.
\]
Consequently the sign of \(|A_a(x)|-|A_b(x)|\) is eventually constant for every
pair \(a\ne b\). Since there are only finitely many parity vectors, the family
\(\{A_a(x)\}_{a\in\mathbf F_2^h}\) is eventually strictly totally ordered. This
proves the binary strict-bias conjecture posed in Tang [1].

The exponent is moreover quantized: every pairwise bias has leading logarithmic
exponent \(2r/m+\nu\), with \(1\le r<m/2\) and \(\nu\in\mathbf Z_{\ge0}\).

A useful explicit consequence is a Boolean-lattice monotonicity law. If
\(a_i\le b_i\) for every \(i\) and \(a\ne b\), then
\[
 |A_a(x)|-|A_b(x)|
 \sim
 \frac{2^{1-h}}{\Gamma(1-2/m)}
 \left(\sum_{i:a_i=0,\ b_i=1} g_i\right)
 x(\log x)^{-2/m}>0,
\]
where \(g_i>0\) is the normalized value at \(s=1\) of the weight-one Euler
product defined below. Thus changing any collection of prescribed prime-factor
parities from even to odd strictly lowers the counting function for all
sufficiently large \(x\).

## Proof

For \(j=(j_1,\dots,j_h)\in\mathbf F_2^h\), extend \(j_i=0\) for \(i>h\), and set
\[
 F_j(s)=\prod_{i=1}^m\prod_{p\equiv\rho_i\,(M)}
 \left(1+(-1)^{j_i}p^{-s}\right).
\]
Tang's Fourier decomposition gives, for \(\Re s>1\),
\[
 D_a(s):=\sum_{N\in A_a}N^{-s}
 =2^{-h}\sum_{j\in\mathbf F_2^h}(-1)^{a\cdot j}F_j(s).
\]
The same Euler-product analysis used in [1] shows that \(F_j\) has Selberg--Delange
pole order
\[
 z_{|j|}=1-\frac{2|j|}{m}.
\]
Write
\[
 F_j(s)=\zeta(s)^{z_{|j|}}G_j(s),
\]
where \(G_j\) is holomorphic in the zero-free region used by the
Selberg--Delange argument in [1].

Fix distinct \(a,b\), and put
\[
 \lambda_j=(-1)^{a\cdot j}-(-1)^{b\cdot j}.
\]
Then \(\lambda_0=0\) and
\[
 D_a(s)-D_b(s)=2^{-h}\sum_{j\ne0}\lambda_jF_j(s).
\]
The pole orders satisfy the exact resonance relation
\[
 z_{r+m/2}=z_r-1.
\]
For \(1\le r<m/2\), define the holomorphic function
\[
 H_r(s)=
 \sum_{|j|=r}\lambda_jG_j(s)
 +\zeta(s)^{-1}\sum_{|j|=r+m/2}\lambda_jG_j(s),
\]
with an empty sum interpreted as zero. Hence
\[
 D_a(s)-D_b(s)
 =2^{-h}\left(
 \sum_{1\le r<m/2}\zeta(s)^{z_r}H_r(s)+E(s)
 \right),
\]
where \(E\) consists only of the layers \(|j|=m/2\) and, when present,
\(|j|=m\). Their pole orders are respectively \(0\) and \(-1\).

The key point is that \(H_1\) cannot vanish identically. We first note that the
Dirichlet series \(\{F_j:j\in\mathbf F_2^h\}\) are linearly independent. For each
\(v\in\mathbf F_2^h\), choose distinct primes \(p_i\equiv\rho_i\pmod M\) for the
indices with \(v_i=1\), and put \(n_v=\prod_{v_i=1}p_i\). Dirichlet's theorem on
primes in arithmetic progressions supplies these primes. The coefficient of
\(n_v^{-s}\) in \(F_j\) is
\[
 (-1)^{j\cdot v}.
\]
Thus a relation \(\sum_j c_jF_j=0\) would give
\[
 \sum_jc_j(-1)^{j\cdot v}=0\qquad(v\in\mathbf F_2^h),
\]
and invertibility of the Walsh--Hadamard matrix forces every \(c_j=0\).

Now multiply \(H_1\) by \(\zeta^{z_1}\). Since
\(z_{1+m/2}=z_1-1\),
\[
 \zeta(s)^{z_1}H_1(s)
 =\sum_{|j|=1}\lambda_jF_j(s)
 +\sum_{|j|=1+m/2}\lambda_jF_j(s).
\]
As \(a\ne b\), some coordinate \(i\) satisfies \(a_i\ne b_i\), and for the
weight-one vector \(e_i\) one has \(\lambda_{e_i}=\pm2\). Linear independence of
the \(F_j\) therefore implies \(H_1\not\equiv0\).

For every \(r\) with \(H_r\not\equiv0\), let
\[
 \nu_r=\operatorname{ord}_{s=1}H_r(s)\in\mathbf Z_{\ge0},
 \qquad
 \beta_r=z_r-\nu_r=1-\frac{2r}{m}-\nu_r.
\]
The numbers \(\beta_r\) are pairwise distinct. Indeed, if \(r\ne r'\), equality
would imply
\[
 \frac{2(r'-r)}m=\nu_r-\nu_{r'},
\]
but the left side is a nonzero real number of absolute value strictly less than
\(1\), while the right side is an integer. Let \(r_*\) be the unique index for
which \(\beta_r\) is maximal.

Apply Tang's Selberg--Delange lemma to each grouped Dirichlet series
\(\zeta(s)^{z_r}H_r(s)\). If \(H_r\) vanishes to order \(\nu_r\) at \(1\), the
first nonzero Selberg--Delange coefficient occurs exactly at that order, giving
\[
 \sum_{n\le x}[n^{-s}]\,\zeta(s)^{z_r}H_r(s)
 \sim
 \frac{H_r^{(\nu_r)}(1)}{\nu_r!\,\Gamma(z_r-\nu_r)}
 x(\log x)^{z_r-\nu_r-1}.
\]
Here \(z_r-\nu_r\) is never an integer, so the gamma factor is finite and
nonzero. The layers in \(E\), whose orders are nonpositive integers, contribute
less than \(x(\log x)^{-A}\) for every fixed \(A>0\): in the same
Selberg--Delange expansion every algebraic coefficient is killed by the zeros of
\(1/\Gamma(z-k)\). Consequently the unique maximal \(\beta_{r_*}\) supplies the
leading term
\[
 |A_a(x)|-|A_b(x)|
 \sim C_{a,b}\,x(\log x)^{-2r_*/m-\nu_{r_*}},
\]
with
\[
 C_{a,b}=
 2^{-h}\frac{H_{r_*}^{(\nu_{r_*})}(1)}
 {\nu_{r_*}!\,\Gamma(z_{r_*}-\nu_{r_*})}\ne0.
\]
All coefficients are real on the real axis \(s>1\), so \(C_{a,b}\) is real.
This proves eventual sign stability.

For the Boolean-lattice corollary, suppose \(a_i\le b_i\) coordinatewise. Then
for weight-one \(e_i\), \(\lambda_{e_i}=2\) exactly when \(a_i=0,b_i=1\), and is
zero otherwise. Tang proves that
\[
 g_i:=G_{e_i}(1)>0.
\]
The paired \(|j|=1+m/2\) part of \(H_1(1)\) is multiplied by
\(\zeta(1)^{-1}=0\), hence
\[
 H_1(1)=2\sum_{i:a_i=0,b_i=1}g_i>0.
\]
Thus \(\nu_1=0\), and every \(r\ge2\) has smaller pole order, yielding the
stated explicit asymptotic and positive sign.

## Relation to prior work

Tang [1] proves equidistribution of the sets \(A_a(x)\), identifies the binary
pole spectrum \(1-2|j|/m\), proves positivity of the weight-one constants, and
proves only the two extremal comparisons: the all-zero parity vector eventually
has the largest count and the all-one vector the smallest. The paper then
conjectures pairwise strict bias for every two distinct binary vectors. The
argument above resolves the missing cancellation issue by grouping pole orders
that differ by integers and using Walsh--Hadamard linear independence to rule out
complete cancellation of the first fractional family.

Porritt [2] studies races for the scalar quantity \(\omega(n)\) modulo an integer;
that setting does not impose a vector of prime-factor parities across individual
reduced residue classes modulo \(M\), and does not supply the pairwise result
above.

## Limitations

Originality is asserted only to the best of our knowledge. The motivating
preprint [1] is very recent, so contemporaneous work not yet indexed remains a
material residual risk. The proof uses the analytic continuation and
Selberg--Delange framework established in [1]; those standard analytic inputs
are not reproved from first principles here. No independent validation or formal
proof-assistant verification is asserted.

## References

[1] Wuji Tang, *Distribution of squarefree integers with double congruence
conditions*, arXiv:2609.16716v1 (2026), https://arxiv.org/abs/2609.16716.

[2] Sam Porritt, *Residue races of the number of prime divisors function*,
Journal of Number Theory 190 (2018), 241--253; arXiv:1806.01585,
https://arxiv.org/abs/1806.01585.

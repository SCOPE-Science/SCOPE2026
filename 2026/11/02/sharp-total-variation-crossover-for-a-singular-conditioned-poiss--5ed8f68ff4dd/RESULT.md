# Sharp total-variation crossover for a singular conditioned-Poisson table

## Finding

Let \(n\ge 1\) and \(z_n>0\). Start with four independent Poisson variables whose mean matrix is
\[
\Lambda_n=\begin{pmatrix}\sqrt{z_n}/n&1\\1&\sqrt{z_n}/n\end{pmatrix}.
\]
Condition on both row sums and both column sums being \(n\). The resulting table equals \(\bigl(\begin{smallmatrix}K_n&n-K_n\\n-K_n&K_n\end{smallmatrix}\bigr)\). Its diagonal count has distribution
\[
Q_{n,z_n}(k)=\frac{\binom nk^2(z_n/n^2)^k}{\sum_{j=0}^n\binom nj^2(z_n/n^2)^j},\qquad 0\le k\le n.
\]
Define a reference distribution \(B_z\) on nonnegative integers by
\[
B_z(k)=\frac{z^k}{(k!)^2 I_0(2\sqrt z)},\quad
I_0(2\sqrt z)=\sum_{j=0}^{\infty}\frac{z^j}{(j!)^2}.
\]
Assume \(z_n\to\infty\) and \(z_n=o(n^2)\). If \(z_n/n^{4/3}\to c\in[0,\infty)\), then
\[
\boxed{\lim_{n\to\infty}\|Q_{n,z_n}-B_{z_n}\|_{\mathrm{TV}}
=2\Phi\!\left(\frac{c^{3/4}}{\sqrt2}\right)-1.}
\]
If instead \(z_n/n^{4/3}\to\infty\), while still \(z_n=o(n^2)\), then the limit is \(1\). Here \(\Phi\) is the standard normal cumulative distribution function and total variation is one-half the sum of absolute probability-mass differences. In particular, for diverging \(z_n\) the exact cutoff scale for the Bessel approximation is \(n^{4/3}\), with a nontrivial continuous transition profile at that scale.

## Assumptions and scope

All Poisson means are strictly positive at every finite \(n\); the conditioning event has positive probability. The table is exactly \(2\times2\), with equal row and column margins \(n\). The singularity is in the odds ratio \(z_n/n^2\to0\), not in a zero-valued Poisson mean at finite \(n\). The theorem covers every positive sequence satisfying the stated growth limits, including \(c=0\), each finite positive \(c\), and the supercritical case. It does not assert a uniform convergence rate over arbitrary such sequences.

## Proof

**1. Exact conditional law and change of measure.** For \(k\in\{0,\ldots,n\}\), the only feasible table is \(\bigl(\begin{smallmatrix}k&n-k\\n-k&k\end{smallmatrix}\bigr)\). The product-Poisson mass, after canceling the common exponential, is proportional to \((z_n/n^2)^k/[k!^2(n-k)!^2]\). This gives the displayed law. Put \(\mu=\sqrt z\), and define
\[
h_n(k)={\bf1}_{\{k\le n\}}\left(\frac{n(n-1)\cdots(n-k+1)}{n^k}\right)^2.
\]
The identity \(\binom nk^2(z/n^2)^k=z^k h_n(k)/(k!)^2\) gives the *exact* likelihood ratio
\[
Q_{n,z}(k)=\frac{B_z(k)h_n(k)}{\mathbb E_{B_z}h_n(K)}.
\tag{1}
\]
The factor \(h_n(k)\) is nonincreasing in \(k\), so \(Q_{n,z}\) is stochastically dominated by \(B_z\).

**2. Concentration lemma valid even outside the critical window.** Write \(\omega=z/n^2\) and
\(P_n(\omega)=\sum_{k=0}^n\binom nk^2\omega^k\). The elementary Legendre identity
\[
P_n(\omega)=(1-\omega)^n L_n\!\left(\frac{1+\omega}{1-\omega}\right)
\tag{2}
\]
holds for \(\omega\ne1\), and extends polynomially to \(\omega=1\). It follows directly from Rodrigues' formula and Leibniz's rule, which give
\[
L_n(x)=2^{-n}\sum_{j=0}^n\binom nj^2(x-1)^j(x+1)^{n-j}.
\]
All roots of \(L_n\) lie in \((-1,1)\). Consequently \(P_n\) has exclusively negative real roots, so the generating function \(P_n(\omega t)/P_n(\omega)\) is that of a sum of independent Bernoulli variables. In particular,
\[
\operatorname{Var}_{Q_{n,z}}(K)\le\mathbb E_{Q_{n,z}}K\le\mathbb E_{B_z}K<\mu.
\tag{3}
\]
The final strict inequality follows from \(\mathbb E_{B_z}K=\mu I_1(2\mu)/I_0(2\mu)<\mu\), using the integral representation of modified Bessel functions.

The exact consecutive-mass relation yields
\[
\mathbb E_QK^2=\frac{\mu^2}{n^2}\mathbb E_Q(n-K)^2.
\tag{4}
\]
When \(\mu<n\), put \(k_0=n\mu/(n+\mu)\) and \(d=k_0-\mathbb E_QK\). Apply (4) to the convex polynomial \(f(k)=k^2-(\mu/n)^2(n-k)^2\), whose positive zero is \(k_0\) and whose derivative there is \(2\mu\). Jensen's inequality gives \(d\ge0\), and expanding at \(k_0\) gives
\[
2\mu d=\left(1-\frac{\mu^2}{n^2}\right)(d^2+\operatorname{Var}_QK).
\tag{5}
\]
Since \(0\le d\le k_0\le\mu\) and (3) holds, equation (5) implies \(d\le1\). We have therefore proved
\[
\frac{n\mu}{n+\mu}-1\le\mathbb E_Q K\le\frac{n\mu}{n+\mu},
\qquad\operatorname{Var}_Q(K)<\mu,
\tag{6}
\]
for every \(\mu<n\). These are deterministic, nonasymptotic statements.

**3. The Bessel reference is asymptotically normal.** Under \(B_{\mu^2}\), the moment generating function is
\[
\mathbb E e^{tK}=\frac{I_0(2\mu e^{t/2})}{I_0(2\mu)}.
\tag{7}
\]
The classical asymptotic \(I_0(x)=e^x/\sqrt{2\pi x}\,(1+O(x^{-1}))\) implies
\[
S_\mu:=\frac{K-\mu}{\sqrt{\mu/2}}\Rightarrow N(0,1),
\quad \mathbb E_{B_{\mu^2}}K=\mu-\tfrac14+O(\mu^{-1}),
\quad \operatorname{Var}_{B_{\mu^2}}(K)=\tfrac\mu2+O(1).
\tag{8}
\]
Moreover, for each fixed real \(v\), \(\sup_{\mu\text{ large}}\mathbb E\exp(v S_\mu)<\infty\); this also follows by applying (7) at \(t=v\sqrt{2/\mu}\).

**4. The critical Gaussian tilt.** Suppose \(z_n/n^{4/3}\to c<\infty\). Then \(\mu=O(n^{2/3})\), and
\[
\delta_n:=\frac{\sqrt2\mu^{3/2}}n\longrightarrow\delta:=\sqrt2c^{3/4}.
\]
For any fixed \(R>0\), and integers \(k\) with \(|(k-\mu)/\sqrt{\mu/2}|\le R\), summing the increments
\(\log h_n(k+1)-\log h_n(k)=2\log(1-k/n)\) gives, uniformly on that window,
\[
\log\frac{h_n(k)}{h_n(\lfloor\mu\rfloor)}
=-\delta_n\frac{k-\mu}{\sqrt{\mu/2}}+o(1).
\tag{9}
\]
To justify passing to expectations, note that the monotone increments also imply, for \(\mu=o(n)\),
\[
0\le\frac{h_n(k)}{h_n(\lfloor\mu\rfloor)}
\le \exp\left(C\frac\mu n\bigl(|k-\mu|+1\bigr)\right)
\tag{10}
\]
with an absolute constant \(C\) and sufficiently large \(n\) (the ratio is zero for \(k>n\)). The right side has uniformly bounded moments of some order greater than one under \(B_{\mu^2}\), by (7), since \(\mu^{3/2}/n\) is bounded. Thus (8)--(10) imply convergence in \(L^1(B_{\mu^2})\), in the asymptotic sense, of the normalized likelihood ratio (1) to the Gaussian likelihood ratio
\[
\exp(-\delta S-\delta^2/2),\quad S\sim N(0,1).
\]
Its total-variation distance from unity is
\[
\frac12\mathbb E|e^{-\delta S-\delta^2/2}-1|
=2\Phi(\delta/2)-1
=2\Phi(c^{3/4}/\sqrt2)-1,
\]
which proves the finite-\(c\) cases.

**5. The supercritical regime.** If \(\mu^{3/2}/n\to\infty\) while \(\mu=o(n)\), the two means are separated by
\[
\mathbb E_B K-\mathbb E_Q K
=\frac{\mu^2}{n+\mu}+O(1),
\]
which is much larger than \(\sqrt\mu\). The variances of both laws are at most order \(\mu\), by (3) and (8). At the midpoint between the means, Chebyshev's inequality gives an event whose probabilities under \(B_{\mu^2}\) and \(Q_{n,\mu^2}\) tend to \(1\) and \(0\), respectively. Hence total variation tends to \(1\), as required.

## Verification

The standalone standard-library program `check.py` checks the exact Legendre identity, conditional mass ratios, second-moment identity, and concentration squeeze using rational arithmetic over small instances. It separately enumerates the two probability laws with logarithmic weights, verifies convergence of finite-size TV values toward three predicted crossover constants, and demonstrates supercritical separation. The recorded output is in `check_output.txt`. Finite computation is evidence only for the algebra and numerical behavior; the infinite-dimensional limits follow from the argument above.

## Relationship to prior work

The conditional-Poisson construction and broad asymptotic theory are discussed by Duan, Lyu, and Powell (2026). Their Assumptions A and B require bounded limiting cost and a growing number of rows and columns, respectively, unlike the present fixed \(2\times2\), vanishing-odds regime. Their Section 8.5 also concerns cloned margins with a fixed positive prior matrix, rather than singular odds. Fisher's noncentral hypergeometric formula and the Bessel-reference law are classical objects; neither the conditional mass formula nor the standard Bessel normal approximation is claimed as new. The contribution assessed here is the exact \(n^{4/3}\) total-variation breakdown scale, its nontrivial Gaussian-shift profile, and the complete supercritical separation within \(z_n=o(n^2)\). A general asymptotic approximation theorem for singular Fisher noncentral hypergeometric laws might imply this profile and remains a priority risk.

## Limitations

No assertion is made for \(z_n\) comparable to or larger than \(n^2\), for unequal table margins, for arbitrary higher-dimensional tables, for non-Gaussian corrections to the limiting profile, or for sharp finite-size error bounds. The result is a self-reviewed derivation, not an independently validated publication or an exhaustive priority certification.

## References

1. D. Duan, H. Lyu, W. Powell, *Poisson contingency tables, Gibbs permutations, and entropic optimal transport*, arXiv:2610.14616 (first public October 10, 2026), https://arxiv.org/abs/2610.14616 .
2. A. Fog, *Sampling Methods for Wallenius' and Fisher's Noncentral Hypergeometric Distributions*, Communications in Statistics—Simulation and Computation (2008); numerical/sampling context, not a source for the crossover theorem.
3. Standard Legendre-polynomial Rodrigues identity and modified-Bessel integral/asymptotic identities; classical formulas used explicitly in the proof above.

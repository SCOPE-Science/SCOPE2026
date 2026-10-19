# Uniform square-root rigidity for punctured-subgroup Fourier measures and Kakeya near-pencils
## Finding
Let \(G\) be any finite abelian group of size \(N\), and let \(H\) be a proper nontrivial subgroup of order \(h\ge2\) and index \(m=N/h\ge2\). Set \(K=(G\setminus H)\cup\{0\}\). For a probability measure \(\mu\) supported on \(K\), define its nontrivial Fourier bias
\[
D(\mu)=\max_{\chi\in\widehat G\setminus\{1\}}|\widehat\mu(\chi)|,
\qquad \widehat\mu(\chi)=\sum_{x\in G}\mu(x)\overline{\chi(x)}.
\]
The known sharp bias value \(r=1/(2m-1)\) is attained by the probability measure
\[
\mu_*(0)=r,\qquad
\mu_*(x)=\frac{2}{h(2m-1)}\quad(x\notin H),\qquad
\mu_*(x)=0\quad(x\in H\setminus\{0\}).
\]
The new assertion is the following **uniform quantitative rigidity theorem**. For every such \(\mu\), put \(\varepsilon=D(\mu)-r\ge0\). Then
\[
-\frac{m-1}{m}\,\varepsilon
\le\mu(0)-r\le\varepsilon,
\tag{1}
\]
and
\[
\boxed{
\|\mu-\mu_*\|_{\mathrm{TV}}
\le\frac12\sqrt{2(h-1)\varepsilon+(N-1)\varepsilon^2}.}
\tag{2}
\]
Here total variation is half the sum of absolute pointwise mass differences. In particular, \(\mu_*\) is the **unique** optimizer. Both inequalities in (1) are attained by suitable measures for their permitted bias deficits.

For every finite field \(\mathbb F_q\), let \(G=\mathbb F_q^2\), let \(H\) be a one-dimensional subspace, and set \(K=(G\setminus H)\cup\{0\}\). This \(K\) is a Kakeya set: it contains an affine line of every direction. If
\[
D(\mu)\le\frac{1+\eta}{2q-1},\qquad\eta\ge0,
\]
then the **field-size-independent** estimate
\[
\boxed{\|\mu-\mu_*\|_{\mathrm{TV}}
\le\frac12\sqrt{\eta+\eta^2/3}}
\tag{3}
\]
holds. For odd \(q\), the exponent \(1/2\) in (2)--(3) is **optimal**, even when the field size is fixed: there exist admissible perturbations with total-variation distance proportional to the square root of the Fourier-bias excess.

## Assumptions and scope
Every measure is a real-valued nonnegative probability mass function. The permitted support \(K\) contains the origin and every point outside \(H\), but no other point of \(H\). The Fourier transform is unnormalized and the trivial Fourier coefficient equals one. Neither the group exponent nor its isomorphism type is restricted. The assertion is an upper bound for the distance to a specific optimal measure, **not** a claim that the displayed prefactor is itself the best possible for each finite group. Sharpness is claimed for the square-root **exponent**, and for the origin-mass slopes in (1), not for every constant in (2).

## Proof
Write \(S=H^\perp\subset\widehat G\) for the annihilator. Standard character orthogonality gives \(|S|=m\) and
\[
\frac1m\sum_{\eta\in S}\eta(x)={\bf1}_H(x).
\]
Put \(a=\mu(0)\) and \(d=D(\mu)\). For each character \(\chi\notin S\), the average of \(\widehat\mu\) over the coset \(\chi S\) equals \(a\), because the only mass in \(H\) is at zero. Since \(H\) is nontrivial, at least one such coset exists. Thus \(d\ge a\). On \(S\) itself,
\[
\sum_{\chi\in S\setminus\{1\}}\widehat\mu(\chi)=ma-1,
\]
so \(d\ge |ma-1|/(m-1)\). Their intersection gives \(d\ge r=1/(2m-1)\). Substituting \(d=r+\varepsilon\) in these inequalities proves (1). The corresponding lower bound on \(a\) follows from \(ma-1\ge-(m-1)d\).

The displayed \(\mu_*\) has Fourier coefficients
\[
\widehat\mu_*(1)=1,\qquad
\widehat\mu_*(\chi)=\begin{cases}
-r,&\chi\in S\setminus\{1\},\\
+r,&\chi\notin S.
\end{cases}
\tag{4}
\]
Indeed, character sums over \(G\setminus H\) equal \(-h\) for nontrivial \(\chi\in S\) and zero for \(\chi\notin S\). Hence \(D(\mu_*)=r\). The equality case for \(d=r\) forces \(a=r\); in each dual coset outside \(S\), \(m\) points of the closed disk of radius \(r\) average to the boundary point \(r\), so all are \(r\). Likewise, all values in \(S\setminus\{1\}\) must be \(-r\). Fourier inversion and (4) force \(\mu=\mu_*\), proving uniqueness.

For the quantitative estimate, Parseval and the bound on the \(N-1\) nontrivial coefficients give
\[
\sum_{\chi\ne1}|\widehat\mu(\chi)|^2\le(N-1)d^2.
\]
The two character sums above also yield the exact real identity
\[
\sum_{\chi\notin S}\widehat\mu(\chi)
-\sum_{\chi\in S\setminus\{1\}}\widehat\mu(\chi)
=(N-2m)a+1.
\]
Using the two signs in (4), expanding squares, and applying Parseval to \(\mu-\mu_*\), we therefore obtain
\[
\begin{aligned}
N\sum_{x\in G}|\mu(x)-\mu_*(x)|^2
&=\sum_{\chi\ne1}|\widehat\mu(\chi)-\widehat\mu_*(\chi)|^2\\
&\le(N-1)(d^2+r^2)-2r((N-2m)a+1)\\
&=(N-1)(d^2-r^2)-2r(N-2m)(a-r).
\end{aligned}
\]
Since \(N-2m=m(h-2)\ge0\), inserting the lower endpoint in (1) and \(d=r+\varepsilon\) simplifies **exactly** to
\[
N\|\mu-\mu_*\|_2^2\le2(h-1)\varepsilon+(N-1)\varepsilon^2.
\tag{5}
\]
Cauchy--Schwarz gives \(2\|\mu-\mu_*\|_{\mathrm{TV}}=\|\mu-\mu_*\|_1\le\sqrt N\|\mu-\mu_*\|_2\), proving (2).

For \(G=\mathbb F_q^2\) and a line \(H\), we have \(h=m=q\), \(N=q^2\). Given \(d\le(1+\eta)r\), replace \(\varepsilon\) in (2) by \(r\eta\) and use
\[
\frac{2(q-1)}{2q-1}\le1,
\qquad\frac{q^2-1}{(2q-1)^2}\le\frac13
\quad(q\ge2),
\]
where the second inequality reduces to \((q-2)^2\ge0\), to obtain (3). The set \(K\) contains each one-dimensional subspace other than \(H\), as well as every affine line parallel to \(H\) but disjoint from it; hence it is Kakeya.

For optimality of the exponent, take odd \(q\) and an element \(v\notin H\) with \(v\ne-v\). For all sufficiently small real \(t\),
\[
\mu_t=\mu_*+t(\delta_v-\delta_{-v})
\]
is nonnegative and supported on \(K\). Fourier coefficients change by a purely imaginary term
\[
\widehat\mu_t(\chi)=\widehat\mu_*(\chi)-2it\,\operatorname{Im}\chi(v).
\]
With \(s=\max_{\chi\ne1}|\operatorname{Im}\chi(v)|>0\), it follows that
\[
D(\mu_t)=\sqrt{r^2+4s^2t^2},\qquad
\|\mu_t-\mu_*\|_{\mathrm{TV}}=|t|.
\]
Consequently the deficit is quadratic in \(t\), whereas the distance is linear: no higher power than \(1/2\) of the bias deficit (or its relative version) can replace the exponent in the asserted local stability statement. Finally, the bounds in (1) are attained by measures \(a\delta_0+(1-a)\mathbf1_{G\setminus H}/|G\setminus H|\) as \(a\) varies on the two sides of \(r\); their exact bias is \(\max(a,|ma-1|/(m-1))\).

## Verification
The standalone `verify.py` constructs cyclic-group and finite-prime-plane test cases, computes all character sums, checks the two-level optimizer spectrum and the exact fixed-origin-mass profile, and tests inequalities (1)--(2) against 32,000 randomly generated admissible measures over eight group instances. In particular it checks characteristic-three and five Kakeya examples. All calculations are numerical consistency tests; the proof for all finite abelian groups is the character-orthogonality/Parseval argument above. The derivation does not rely on the sampled tests.

## Relationship to prior work
Fraser's 2025 preprint, published in 2026, proves that every finite-field Kakeya set carries a probability measure with nontrivial Fourier coefficients at most \(q^{-1}\), and constructs Kakeya sets showing worst-case asymptotic sharpness; it does not state quantitative closeness of almost-optimal measures on the punctured-line Kakeya family.

The **baseline** optimal bias \(1/(2m-1)\) is not claimed as a newly discovered fast-mixing constant. The Cayley graph of \(G\) with allowed increments \(K\) is a complete \(m\)-partite graph on cosets of \(H\), with holding loops. Boyd--Diaconis--Xiao compute the fastest mixing Markov chain for complete bipartite graphs in Section 7.1 of their 2004 paper. Boyd--Diaconis--Parrilo--Xiao give an analytic edge-transitive graph theorem (Theorem 3.1) in 2009 which also yields the optimal multipartite value. These results cover the **unconstrained optimum** after the graph reduction; the point of the present result is the explicit \(\ell^1\) stability inequality (2), its relative dimension-uniform Kakeya form (3), and the sharpness of the exponent for every odd field size. The compared work gives optimal SLEM formulas and symmetry reductions, not these quantitative near-optimal concentration estimates.

Published Fourier-synthesis \(\Lambda(6)\) calculations for a missing frequency subgroup use a different objective (sixth moments of arbitrary coefficients) and do not imply the near-optimal probability-measure stability result. Likewise, small-bias constructions for unrestricted support do not supply a quantitative rigidity theorem for the prescribed punctured subgroup geometry.

## Limitations
The bounds require a nontrivial proper subgroup; they do not cover a missing singleton or the full group. The coefficient of the total-variation remainder is explicit and field-uniform in the near-pencil application, but its exact optimality is not asserted. The sharp exponent construction uses odd characteristic; no exponent-optimality assertion is made for exponent-two groups. Independent external verification has not been performed. A differently stated general stability theorem for symmetric Markov-chain optimization could potentially imply a similar square-root modulus, although no source explicitly covering (2)--(3) was located in the inspected literature.

## References
1. J. M. Fraser, *Fourier analytic properties of Kakeya sets in finite fields*, arXiv:2505.09464v1, 2025-05-14; *Bull. London Math. Soc.* 58 (2026), e70367, DOI:10.1112/blms.70367.
2. S. Boyd, P. Diaconis, L. Xiao, *Fastest Mixing Markov Chain on a Graph*, *SIAM Review* 46 (2004), 667--689, DOI:10.1137/S0036144503423264, especially Section 7.1.
3. S. Boyd, P. Diaconis, P. A. Parrilo, L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, *SIAM J. Optimization* 20 (2009), 792--819, DOI:10.1137/070689413, especially Theorem 3.1.
4. S. Chen, C. Moore, A. Russell, *Small-Bias Sets for Nonabelian Groups: Derandomizing the Alon--Roichman Theorem*, arXiv:1304.5010v4 (2013).

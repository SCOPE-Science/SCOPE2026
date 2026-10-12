# Fixed local splitting conditions preserve support \(<1\) for cubic Artin one-level density
## Finding
Fix a finite set of rational primes and prescribe one cubic splitting type at each of them. Assume that one prescribed prime is inert, of type \((3)\), and a distinct prescribed prime is partially split, of type \((21)\); thus every field in the family is non-Galois. For either sign of the discriminant, write
\[
\mathcal F_\Sigma^{\pm}(X)=\{K:[K:\mathbb Q]=3,\ 0<\pm\operatorname{Disc}(K)\le X,\ K\text{ satisfies }\Sigma\}.
\]
Let \(L(s,\rho_K)=\zeta_K(s)/\zeta(s)\) be the two-dimensional Artin \(L\)-function. Assume GRH for Dedekind zeta functions of quadratic and cubic fields. Then for every real even Schwartz function \(\phi\) with
\[
\operatorname{supp}\widehat\phi\subset(-1,1),
\]
one has
\[
\frac1{\#\mathcal F_\Sigma^{\pm}(X)}\sum_{K\in\mathcal F_\Sigma^{\pm}(X)}\sum_{\gamma_K}
\phi\!\left(\frac{\log X}{2\pi}\gamma_K\right)
=\widehat\phi(0)-\frac12\phi(0)+o(1),
\]
where the zeros are written \(1/2+i\gamma_K\), with multiplicity. In particular,
\[
\liminf_{X\to\infty}
\frac{\#\{K\in\mathcal F_\Sigma^{\pm}(X):L(1/2,\rho_K)\ne0\}}
{\#\mathcal F_\Sigma^{\pm}(X)}\ge\frac34.
\]
Thus Ahlquist's conditional support \(<1\) and \(75\%\) nonvanishing theorem persist after any fixed finite set of splitting-type conditions of this \(S_3\)-family form.

## Assumptions and scope
The local prescriptions are fixed as \(X\to\infty\), and each is one of the five cubic splitting types \((111),(21),(3),(1^{2}1),(1^{3})\). The inert and partially split prescriptions at two distinct primes are included only to stay exactly inside the \(S_3\)-families used by Shankar--Södergren--Templier; the proof below uses no averaging over the prescribed primes. The sign \(\pm\) is fixed. GRH is the same hypothesis as in Ahlquist's Theorems 1.10 and 1.11.

No claim is made for a set of local conditions whose support grows with \(X\). The result concerns sharp discriminant ordering, not only smoothed counts.

## Proof
Ahlquist's explicit formula for the unconditioned family is
\[
D_\phi(K)=\frac{\widehat\phi(0)}{\log X}\log|D_K|-
\frac{2}{\log X}\sum_p\sum_{e\ge1}\frac{\log p}{p^{e/2}}
\widehat\phi\!\left(\frac{e\log p}{\log X}\right)a_K(p^e)+o(1),
\]
with \(|a_K(p^e)|\le2\). Let \(S\) be the fixed set of primes occurring in \(\Sigma\). The total contribution of \(p\in S\) is
\[
O_{\Sigma,\phi}\!\left(\frac1{\log X}\right),
\]
because for each fixed \(p\) the sum \(\sum_{e\ge1}p^{-e/2}\) converges. Hence only primes \(p\notin S\) matter for the limiting density.

For such a prime \(p\), insert the fixed local indicator \(\chi_\Sigma\) into every binary-cubic-form sum in Ahlquist's Sections 3--5. Since \(p\) is coprime to the fixed modulus supporting \(\chi_\Sigma\), the relevant finite test function factors as a tensor product of the original \(p\)-local factor and \(\chi_\Sigma\). The Shintani functional equation and the local Fourier transform therefore factor prime by prime. Three consequences are decisive.

First, the residue at \(s=1\) acquires the same fixed \(\Sigma\)-local mass as the leading field-counting term. After division by \(\#\mathcal F_\Sigma^{\pm}(X)\sim c_\Sigma^{\pm}X\), this fixed mass cancels, so the normalized leading term at every varying prime \(p\notin S\) is exactly the same as in the unconditioned proof. The \(s=5/6\) residue may acquire a different fixed local factor, but Ahlquist already proves its contribution is \(o(1)\) for support \(\sigma<1\); multiplication by a fixed factor does not change that estimate.

Second, all Fourier-transform and geometry-of-numbers estimates in the small and intermediate ranges change only by a constant depending on \(\Sigma\): the extra local factors live at finitely many fixed primes. At primes in \(S\), the maximality sieve is modified by the local identities described in Ahlquist's Section 7.4; because \(S\) is fixed, this introduces no new power of \(X\) or of the varying prime \(p\).

Third, the difficult dual \(S_3\)-contribution in Ahlquist's Section 5.4 is stable under the same insertion. After switching to maximal overrings, the argument reduces to counting \(S_3\)-cubic fields that are totally ramified at the varying prime and satisfy splitting conditions at auxiliary primes. Ahlquist explicitly invokes Shankar--Thorne's theorem in a form allowing arbitrary splitting conditions. Adding the fixed conditions \(\Sigma\) therefore changes only the implied constant, not the exponents that control the support. Reducible and cyclic-cubic contributions are likewise multiplied by bounded fixed local factors.

Consequently every exponent inequality in Ahlquist's proof of Theorem 1.10 is unchanged. The same argument therefore gives support \(\sigma<1\) for \(\mathcal F_\Sigma^{\pm}(X)\), with the same symplectic limit
\[
\widehat\phi(0)-\frac12\phi(0).
\]
This also upgrades Shankar--Södergren--Templier's Theorem 5, which proves the same local-family density only for support \((-2/5,2/5)\).

For nonvanishing, take \(0<\sigma<1\) and
\[
\phi_\sigma(x)=\left(\frac{\sin(\pi\sigma x)}{\pi x}\right)^2.
\]
Then \(\phi_\sigma\ge0\), \(\phi_\sigma(0)=\sigma^2\), and
\[
\widehat\phi_\sigma(t)=\max(\sigma-|t|,0).
\]
Thus the density theorem gives
\[
\limsup_{X\to\infty}\frac1{\#\mathcal F_\Sigma^{\pm}(X)}
\sum_K \operatorname{ord}_{s=1/2}L(s,\rho_K)
\le \frac1\sigma-\frac12.
\]
The completed Dedekind zeta functions of \(K\) and \(\mathbb Q\) both have root number \(+1\), so the quotient \(L(s,\rho_K)\) has root number \(+1\); hence a central zero has even order, at least \(2\). Therefore the vanishing proportion is at most
\[
\frac1{2\sigma}-\frac14.
\]
Letting \(\sigma\to1^-\) gives a vanishing proportion at most \(1/4\), proving the stated \(3/4\) nonvanishing lower bound.

## Verification
The proof is analytic and all-parameter; no finite computation is used to replace any infinite estimate. The accompanying `verify.py` checks the algebra of the test-function optimization and the geometric-series bound for the finitely many prescribed Euler factors.

Replay command: `python verify.py`

Expected output:
`VERIFY_OK sigma_cases=4 limit_nonvanishing=0.750000 fixed_prime_geometric_bound=1`

The executable check does not verify the Shintani-zeta estimates. Those are supplied by the cited theorems and by the stability argument above.

## Relationship to prior work
Ahlquist, arXiv:2610.01837v1, proves under GRH that the unconditioned non-Galois cubic family has symplectic one-level density for support \(<1\), and deduces \(75\%\) central nonvanishing. The same paper separately proves sharp and smooth counting theorems with finitely many prescribed splitting conditions and, in the hard dual \(S_3\) step, explicitly uses a field-counting theorem allowing arbitrary splitting conditions. It does not state the one-level density or \(75\%\) theorem for the conditioned subfamilies.

Shankar--Södergren--Templier, arXiv:2107.10900v3 / Inventiones Mathematicae 243 (2026), Theorem 5, does treat finite local specifications in an \(S_3\)-family, but obtains only support \((-2/5,2/5)\). Their central-value method also gives many nonvanishing fields under local specifications, but not a \(75\%\) lower proportion. The present observation couples Ahlquist's new support-\(<1\) argument with the fixed local-factor formalism and therefore strictly strengthens the known local-family support range under the same GRH hypothesis.

## Limitations
The local set \(S\) must be fixed. Uniformity when the number or size of prescribed primes grows with \(X\) is not established. The statement is conditional on GRH exactly as Ahlquist's support-\(<1\) result is. The proof establishes the same leading one-level density; it does not claim that lower-order terms are unchanged by local conditioning.

## References
1. V. Ahlquist, *Averages of Artin characters and their relation to the Davenport--Heilbronn theorem*, arXiv:2610.01837v1 (2026), especially Theorems 1.6, 1.10, 1.11 and Sections 3, 5.4, 7.4.
2. A. Shankar, A. Södergren, N. Templier, *Central values of zeta functions of non-Galois cubic fields*, arXiv:2107.10900v3; Invent. Math. 243 (2026), 33--116, especially Theorem 5 and Sections 6--7.
3. P. J. Cho, D. Fiorilli, Y. Lee, A. Södergren, *Omega results for cubic field counts via lower-order terms in the one-level density*, Forum Math. Sigma 10 (2022).

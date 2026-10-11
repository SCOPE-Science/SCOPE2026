# Inverse-temperature pressure law for the digit potential on bounded-type Sturmian beta-shifts

## Finding

For an irrational \(\alpha\in(0,1)\), let \(Y_\alpha\) be the one-sided Sturmian beta-shift, with lexicographically maximal sequence \(a_j=\lceil(j+1)\alpha\rceil-\lceil j\alpha\rceil\), and let \(\Phi(x)=x_0\). Write \(X_\alpha\subset Y_\alpha\) for its Sturmian subshift and \(\mu_\alpha\) for the unique invariant measure on \(X_\alpha\). Define \(\mathcal N=\{n\ge1:a_{n-1}=1\}\) and \(\epsilon_n=\{n\alpha\}\).

For every irrational \(\alpha\) and every \(t>0\), the pressure is
\[P(t\Phi)=t\alpha+d_\alpha(t),\qquad \sum_{n\in\mathcal N}e^{-t\epsilon_n-nd_\alpha(t)}=1,\qquad d_\alpha(t)>0,\]
where the equation has exactly one positive root. The measure \(\mu_\alpha\) is the **unique** maximizing invariant probability for the locally constant potential \(\Phi\). Moreover \(t\Phi\) has a unique equilibrium measure \(\nu_t\).

If \(\alpha\) has bounded continued-fraction coefficients, there exist \(T,c_i,C_i>0\), depending only on \(\alpha\), such that, for every real \(t\ge T\),
\[\frac{c_1}{t}\le P(t\Phi)-t\alpha\le\frac{C_1}{t},\qquad
\frac{c_2}{t^2}\le\alpha-\int\Phi\,d\nu_t\le\frac{C_2}{t^2},\qquad
\frac{c_3}{t}\le h_{\nu_t}(\sigma)\le\frac{C_3}{t}.\]
Here entropy is measured in natural logarithmic units. Thus the ground state is nonperiodic, while the pressure excess and equilibrium entropy disappear at the inverse-temperature scale and the density defect at the inverse-square scale.

## Assumptions and scope

The sequences are one-sided, over the alphabet \(\{0,1\}\), with the ordinary left shift \(\sigma\). The beta-shift is \(Y_\alpha=\{x:\sigma^j x\le_{\mathrm{lex}}a\text{ for all }j\ge0\}\). The pressure is the topological pressure of \(t\Phi\): if \(\mathcal L_n\) denotes admissible words of length \(n\),
\[P(t\Phi)=\lim_{n\to\infty}\frac1n\log Z_n(t),\qquad Z_n(t)=\sum_{w\in\mathcal L_n}e^{t|w|_1}.\]
The limit exists because \(Z_{n+m}(t)\le Z_n(t)Z_m(t)\). Bounded type means the continued-fraction partial quotients of \(\alpha\) are uniformly bounded. The exact renewal equation and optimizer uniqueness do **not** need bounded type; only the two-sided temperature-rate estimates do.

## Proof

**1. An exact weighted renewal identity.** The standard right-resolving beta-shift graph has vertices \(0,1,\ldots\), an edge \(j\to j+1\) labelled \(a_j\), and a reset edge \(j\to0\) labelled \(0\) whenever \(a_j=1\). Every admissible finite word has exactly one path starting at vertex \(0\), and that path decomposes uniquely into completed first-return loops followed by an unfinished prefix of \(a\) (Huang--Jenkinson--Xu--Zhang, Lemma 4.3). The loop of length \(n\in\mathcal N\) is \(a_0\cdots a_{n-2}0\), containing \(\lfloor n\alpha\rfloor\) ones; the unfinished prefix of length \(m\) contains \(\lceil m\alpha\rceil\) ones (their Lemma 4.5). Consequently, as an identity of formal power series,
\[\sum_{n\ge0}Z_n(t)z^n=\frac{\sum_{m\ge0}e^{t\lceil m\alpha\rceil}z^m}{1-\sum_{n\in\mathcal N}e^{t\lfloor n\alpha\rfloor}z^n}.\tag{1}\]
Both numerator and first-return series have convergence radius \(e^{-t\alpha}\). The first-return sum evaluated at that radius equals \(\sum_{n\in\mathcal N}e^{-t\{n\alpha\}}=\infty\): the irrational orbit hits \(\{n\alpha\}\in(0,\alpha/2)\) infinitely often. Hence there is a unique positive \(r<e^{-t\alpha}\) where the first-return sum equals \(1\). Below \(r\) the right side of (1) converges, and as the positive real variable increases to \(r\) it diverges, because the numerator is finite and positive. Thus the power series on the left has radius exactly \(r\). Its exponential growth rate equals \(e^{P(t\Phi)}\), so setting \(r=e^{-t\alpha-d_\alpha(t)}\) gives the claimed equation and uniqueness.

**2. Uniqueness of the ground state, without a Diophantine assumption.** An arbitrary admissible \(x\) decomposes into complete loops of lengths \(\ell_1,\ldots,\ell_s\) before time \(N\), followed by an unfinished prefix of length \(m\). The exact digit discrepancy is
\[\alpha N-S_N\Phi(x)=\sum_{j=1}^{s}\{\ell_j\alpha\}+m\alpha-\lceil m\alpha\rceil,\]
and the last term lies in \([-1,0]\). The motivating paper proves \(\sup_{\nu\text{ invariant}}\int\Phi\,d\nu=\alpha\), attained by \(\mu_\alpha\) (Proposition 4.6). Let \(x\) be typical for an ergodic maximizing measure. Then the left side is \(o(N)\), hence \(\sum_j\{\ell_j\alpha\}=o(N)\). For each fixed \(L\), the finitely many allowed loop lengths \(\ell\le L\) have a strictly positive minimum defect, so the number of short completed loops is \(o(N)\). The number of completed loops of length \(>L\) is at most \(N/L\). First let \(N\to\infty\), then \(L\to\infty\): the total number of completed loops is \(o(N)\). Each loop differs from a prefix of the maximal Sturmian sequence only at its last symbol. Thus a length-\(k\) block not belonging to the Sturmian language can start only within \(k\) sites of a loop boundary. Such blocks have zero asymptotic frequency for every fixed \(k\). The typical measure is therefore supported on \(X_\alpha\), which is uniquely ergodic, forcing it to be \(\mu_\alpha\). Applying ergodic decomposition proves the same for nonergodic maximizing measures.

**3. Lower bound for the pressure excess.** Suppose the continued-fraction coefficients are at most \(B\). There is \(K=K_\alpha\) such that for every large real \(t\), each interval of \(\lceil Kt\rceil\) consecutive positive integers contains some \(n\) with \(0<\{n\alpha\}<1/t\). Indeed, choose consecutive convergent denominators \(q_{j-1}\le\lceil4t\rceil<q_j\). Bounded partial quotients give \(q_j\le(B+2)\lceil4t\rceil\). The orbit points \(\{m\alpha\}\) for \(m=0,\ldots,q_j-1\) are within \(1/q_{j+1}\) of a permutation of the \(q_j\)-grid, so their largest circular gap is at most \(1/q_j+2/q_{j+1}<3/q_j<1/t\). Translating this set shows the asserted bounded waiting time. For \(t>1/\alpha\), every such hit belongs to \(\mathcal N\). Choose one hit in each consecutive block of length \(b_t=\lceil Kt\rceil\); then the renewal series at \(d=c/t\) is at least
\[\sum_{j\ge1}e^{-1}e^{-cj(K+1)}=\frac{e^{-1}}{e^{c(K+1)}-1}.\]
Choose \(c>0\) small enough to make this greater than \(1\). Since the renewal series decreases strictly with \(d\), \(d_\alpha(t)>c/t\).

**4. Upper bound for the pressure excess.** Bounded type also gives a constant \(\kappa>0\) such that \(\|n\alpha\|\ge\kappa/n\) for every \(n\ge1\), where \(\|\cdot\|\) is distance to the nearest integer. Choose \(\eta>0\) so small that \((e^{\kappa/\eta}-1)^{-1}<1/4\). Among the first \(m=\lfloor\eta t\rfloor\) orbit points, every fractional part is at least \(\kappa/m\), and pairwise fractional parts are separated on the circle by at least \(\kappa/m\). Ordering the points from zero gives
\[\sum_{1\le n\le m}e^{-t\{n\alpha\}}\le (e^{t\kappa/m}-1)^{-1}<1/4.\]
Any block of \(\lceil t\rceil\) consecutive orbit points has pairwise separation at least \(\kappa/\lceil t\rceil\); consequently its unweighted exponential sum is at most \(H=(1-e^{-\kappa/2})^{-1}\), for \(t\ge1\). Partition the remaining indices into these blocks. When \(t\) is large enough that \(m/t\ge\eta/2\), their combined contribution to the renewal series at \(d=C/t\) is at most
\[H\sum_{j\ge0}e^{-C(\eta/2+j)}=H\frac{e^{-C\eta/2}}{1-e^{-C}}.\]
Choose \(C\) sufficiently large to make this less than \(1/4\). The entire renewal series at \(C/t\) is then less than \(1\), so \(d_\alpha(t)<C/t\).

**5. Entropy and density rates.** The Sturmian beta-shift has specification (Huang--Jenkinson--Xu--Zhang, Lemma 4.4). The one-symbol potential has zero variation of its length-\(n\) Birkhoff sum on each length-\(n\) cylinder; the standard specification/Bowen theorem therefore gives a unique equilibrium measure \(\nu_t\) for each finite \(t>0\). By the variational principle and uniqueness, \(P\) is differentiable and \(P'(t)=\int\Phi\,d\nu_t\). Put \(D(t)=P(t\Phi)-t\alpha\). This is convex and satisfies \(c/t\le D(t)\le C/t\) for large \(t\). For any fixed \(\lambda>2C/c\), convex secant inequalities give
\[\frac{c}{2(\lambda-1)t^2}\le -D'(t)\le\frac{4C}{t^2}\]
when \(t\) is sufficiently large: the lower bound compares \(D(t)\) with \(D(\lambda t)\), and the upper bound compares \(D(t/2)\) with \(D(t)\). Since \(-D'(t)=\alpha-\int\Phi\,d\nu_t\), this proves the density deficit. Finally the variational identity \(h_{\nu_t}=P(t\Phi)-t\int\Phi\,d\nu_t=D(t)+t(-D'(t))\) gives its entropy bounds.

## Verification

The accompanying standard-library program `verify.py` checks the weighted finite-word decomposition by **independent methods**: direct lexicographic admissibility of all \(16{,}383\) binary words up to length \(13\), and an integer-polynomial renewal recurrence. It uses an exact rational enclosure of the golden slope to verify the tested Sturmian prefix, then compares the two enumerations coefficient by coefficient. Numerical roots of the truncated renewal equation are additionally computed for \(t=20,60,200,500\), with geometric upper bounds on the omitted positive tail. The observed values of \(t(P-t\alpha)\) are approximately \(0.827685,0.828394,0.828498,0.828505\) respectively. These checks are finite consistency tests. The universal theorem, bounded-type estimates, and asymptotic orders are proved analytically above.

## Relationship to prior work

Huang, Jenkinson, Xu and Zhang (2026), Sections 3--4, identify the same beta-shift, its uniquely ergodic Sturmian subsystem, the first-return graph, the positive loop defects and the fact that the Sturmian measure **maximizes** the digit potential. They establish robust unique optimization for a different potential, the digit function *minus a distance to the Sturmian subsystem*. They do not state unique optimization of the digit function alone, the weighted renewal pressure identity, or the inverse-temperature pressure/density/entropy rates obtained here. The graph and defect identities are inputs, not claimed discoveries.

Chi and Kwon (2003/2004) classify Sturmian beta parameters and study their expansion dynamics, including typical digit frequencies of the absolutely continuous maximal-entropy state. This does not give the low-temperature equilibrium laws of the digit potential. Anagnostopoulou and Jenkinson (2009) characterize the more stringent existence of a **largest invariant measure** in stochastic order, which is different from maximizing this single observable. Classical beta-shift thermodynamic formalism, including Climenhaga and Thompson (2012), supplies general equilibrium theory; no source inspected contains this bounded-type three-rate law.

## Limitations

The inverse-temperature exponents are proved for bounded-type slopes only; no uniform constants or limit for the rescaled pressure are claimed for all irrational slopes. The result concerns the one-symbol digit potential, not arbitrary Lipschitz potentials. The pressure formula uses the particular Sturmian beta-shift, and the thermodynamic entropy uses natural logarithms. Existing general renewal, rotation and specification theory may imply portions of the result in another formulation; equivalence in all prior literature has not been exhaustively ruled out. Independent scientific verification has not been performed.

## References

1. W. Huang, O. Jenkinson, L. Xu, Y. Zhang, *Sturmian beta-shifts do not have typical periodic optimization*, arXiv:2610.03619v1 (first publicly posted 2026-10-02), especially Sections 3--4 and Lemmas 3.5, 4.3--4.5 and Proposition 4.6. https://arxiv.org/abs/2610.03619
2. D. P. Chi and D. Kwon, *Sturmian words, beta-shifts, and transcendence*, arXiv:math/0308140v1 (2003), Sections 4--5. https://arxiv.org/abs/math/0308140
3. V. Anagnostopoulou and O. Jenkinson, *Which beta-shifts have a largest invariant measure?*, J. London Math. Soc. 79 (2009), 445--464, doi:10.1112/jlms/jdn070.
4. V. Climenhaga and D. J. Thompson, *Equilibrium states beyond specification and the Bowen property*, J. London Math. Soc. 87 (2013), 401--427, arXiv:1106.3575; first posted 2011.

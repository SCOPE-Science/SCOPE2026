# Peripheral Fredholm-spectrum inheritance under positive domination on \(c_0\)
## Finding
Let \(c_0=c_0(\mathbb N;\mathbb C)\) with its coordinatewise order and supremum norm. For a bounded operator \(A\), write \(\pi(A)\) for its class in the Calkin algebra \(\mathcal Q(c_0)=\mathcal B(c_0)/\mathcal K(c_0)\), \(\sigma_F(A)=\sigma(\pi(A))\), and \(r_F(A)=r(\pi(A))\). If \(S,T\in\mathcal B(c_0)\) are positive, \(0\le S\le T\), and \(r_F(S)=r_F(T)=r\), then

\[
\sigma_F(S)\cap r\mathbb T\subseteq\sigma_F(T)\cap r\mathbb T,
\]

where \(\mathbb T=\{z\in\mathbb C:|z|=1\}\). Thus every boundary spectral value of the smaller operator that obstructs Fredholmness persists for the larger operator when their Fredholm essential radii agree.

## Assumptions and scope
All operators are bounded and complex-linear on \(c_0\); positivity and order are coordinatewise. The inequality \(0\le S\le T\) means that \(Sx\ge0\) and \((T-S)x\ge0\) for every \(x\ge0\). The Fredholm essential spectrum is defined by Atkinson's theorem as the spectrum in the Calkin algebra, equivalently the set of \(\lambda\) for which \(\lambda I-A\) is not Fredholm. The assertion concerns only the outer circle of this essential spectrum. It does not assert cyclicity of the essential spectrum, inclusion of the full essential spectra, or validity on arbitrary Banach lattices.

## Proof
For \(m\ge1\), let \(P_m\) project onto the first \(m\) coordinates and \(Q_m=I-P_m\) be the tail projection. We first establish the essential-norm formula

\[
\|A\|_e=\lim_{m\to\infty}\|AQ_m\|, \qquad A\in\mathcal B(c_0),
\]

where \(\|A\|_e=\inf_{K\in\mathcal K(c_0)}\|A-K\|\). Since \(AP_m\) has finite rank, \(\|A\|_e\le\|AQ_m\|\). Conversely, for each compact \(K\), \(\|AQ_m\|\le\|A-K\|+\|KQ_m\|\). The adjoint \(K^*:\ell_1\to\ell_1\) is compact, and the \(\ell_1\)-tail projections converge uniformly to zero on compact subsets of \(\ell_1\); hence \(\|KQ_m\|=\|Q_m^*K^*\|\to0\). Taking limits and then the infimum over \(K\) proves the formula.

If \(r=0\), both Calkin classes have spectral radius zero, so their nonempty compact spectra are both \(\{0\}\), and the inclusion is immediate. Suppose henceforth that \(r>0\). For \(z\in\mathbb D\), define \(F(z)=S+z(T-S)\). For all \(x\in c_0\), coordinatewise modulus and positivity give

\[
|F(z)x|\le (S+|z|(T-S))|x|\le T|x|.
\]

Induction yields \( |F(z)^n x|\le T^n|x|\) for every integer \(n\ge1\). Since \(Q_m\) is a positive coordinate projection, this implies \(\|F(z)^nQ_m\|\le\|T^nQ_m\|\). The essential-norm formula therefore gives \(\|F(z)^n\|_e\le\|T^n\|_e\). Taking \(n\)-th roots and using the spectral-radius formula in the Calkin algebra shows

\[
r_F(F(z))\le r_F(T)=r,\qquad z\in\mathbb D.
\]

Now \(G(z)=\pi(F(z))/r\) is a holomorphic map into the unital Banach algebra \(\mathcal Q(c_0)\), and \(\sigma(G(z))\subseteq\overline{\mathbb D}\) for every \(z\in\mathbb D\). Fix \(\lambda\in\sigma_F(S)\cap r\mathbb T\) and put \(\mu=\lambda/r\). Then \(\mu\in\sigma(G(0))\cap\mathbb T\). The holomorphic map \(H(z)=(I+\overline{\mu}G(z))/2\) has spectrum in \(\overline{\mathbb D}\), and \(1\in\sigma(H(0))\), so its spectral radius attains the upper bound \(1\) at the interior point \(z=0\). By Vesentini's theorem, \(z\mapsto\log r(H(z))\) is subharmonic; the maximum principle forces \(r(H(z))=1\) throughout \(\mathbb D\). Compactness of each spectrum then gives some \(\eta\in\sigma(G(z))\) with \(|1+\overline{\mu}\eta|=2\). As \(|\eta|\le1\), equality in the triangle inequality forces \(\eta=\mu\). Thus \(\lambda\in\sigma(\pi(F(z)))\) for every \(z\in\mathbb D\).

Finally, let real \(t\uparrow1\). Since \(F(t)\to T\) in operator norm, \(\pi(F(t))\to\pi(T)\) in the Calkin algebra. If \(\lambda\notin\sigma_F(T)\), then \(\lambda I-\pi(T)\) is invertible; openness of the invertible group would make \(\lambda I-\pi(F(t))\) invertible for all sufficiently large \(t<1\), a contradiction. Hence \(\lambda\in\sigma_F(T)\), proving the inclusion.

## Verification
The proof is analytic and exact; it does not use numerical experiments. The key infinite-dimensional step is \(\|KQ_m\|\to0\) for compact \(K\) on \(c_0\), proved through compactness of the adjoint on \(\ell_1\). The spectral-radius comparison is derived for each complex interpolation parameter \(z\), not inferred from positivity of \(F(z)\), which need not be positive. The endpoint \(r=0\) is treated separately. No claim is made about essential-spectrum cyclicity or about replacing \(c_0\) by an arbitrary Banach lattice.

## Relationship to prior work
Dobrick's 2026 preprint proves cyclicity of the ordinary peripheral spectrum of positive operators and describes a spectral-domination theorem for equal ordinary spectral radii, based on Vesentini's theorem. The full text was not accessible through the available public routes. Räbiger and Wolff's 1997 paper proves ordinary peripheral-spectrum inclusion under a growth condition and treats essential-spectrum consequences when the ordinary spectral radius is a Riesz point. Martínez's 1993 paper addresses essential spectral radii of dominated positive operators. The present statement is different in its spectral object and hypothesis: it concerns Fredholm essential spectra, assumes equality of essential radii rather than ordinary radii, and is proved on \(c_0\) by an exact tail formula for the essential norm. The inspected Räbiger–Wolff statements do not give this boundary-spectrum inclusion under the present hypotheses. Because the full Dobrick and Martínez texts were unavailable, their additional essential-spectrum content remains a stated residual risk.

## Limitations
The result is restricted to \(c_0\) and to the Fredholm essential spectrum. The essential-norm tail formula used here is specific to the coordinate-tail approximation structure. The full texts of Dobrick (2026) and Martínez (1993) were not accessible through the available public routes. Dobrick's accessible abstract describes ordinary peripheral-spectrum results, while Martínez's available metadata concerns essential spectral radii of dominated positive operators; both remain explicit residual risks for any additional essential-spectrum statements not visible in the accessible material. Literature searches are not exhaustive. No independent audit has been performed.

## References
1. A. Dobrick, “On the Cyclicity Conjecture,” arXiv:2610.10093v1, submitted 7 October 2026. https://arxiv.org/abs/2610.10093
2. F. Räbiger and M. P. H. Wolff, “Spectral and asymptotic properties of dominated operators,” *J. Austral. Math. Soc. Ser. A* 63 (1997), 16–31. https://doi.org/10.1017/S144678870000029X
3. J. Martínez, “The Essential Spectral Radius of Dominated Positive Operators,” *Proc. Amer. Math. Soc.* 118 (1993), 419–426. https://doi.org/10.2307/2160318
4. E. Vesentini, “On the subharmonicity of the spectral radius,” *Boll. Un. Mat. Ital.* (4) 1 (1968), 427–429.
5. F. V. Atkinson, “The normal solvability of linear equations in normed spaces,” *Mat. Sb.* 28 (1951), 3–14.
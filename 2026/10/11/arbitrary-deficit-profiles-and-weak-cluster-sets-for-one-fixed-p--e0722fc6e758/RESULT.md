# Arbitrary deficit profiles and weak cluster sets for one fixed positive maximizing witness
## Finding
In the fixed counterexample of Costa--Miranda--Ribeiro, write \(D e_n=n^{-1}e_n\), let \(q^*:\ell_2\to Y^*\) be the positive lattice embedding used there, and put
\[
\rho(q^*u)=\|u\|_2+\|Du\|_2,
\qquad
X_1=(q^*(\ell_2),\rho)\oplus_\infty\mathbb R.
\]
For the fixed positive operator
\[
T(q^*u,t)=u,
\]
the source proves \(\|T\|=1\) and that \(T\) does not attain its norm.

For every sequence \((\varepsilon_k)\subset(0,1)\) with \(\varepsilon_k\to0\) and every nonempty compact set \(K\subset[0,1]\), there is a positive sequence \((z_k)\subset S_{X_1}\) satisfying
\[
\|Tz_k\|_2=1-\varepsilon_k
\quad\text{for every }k,
\]
whose weak cluster set is exactly \(\{0\}\times K\). Thus one fixed non-norm-attaining positive operator realizes every prescribed positive null norm-deficit profile and, independently, every compact scalar weak-cluster pattern. If \(K\) contains a nonzero point, the resulting maximizing sequence is not weakly null and therefore witnesses the positive weak-maximizing failure in the source construction.

## Assumptions and scope
The argument uses the real Banach-lattice construction and notation of arXiv:2609.38410v1. The source supplies a separable reflexive Banach lattice \(Y\), a positive surjection \(q:Y\to\ell_2\) for which \(q^*\) is a lattice embedding, the diagonal operator \(D e_n=n^{-1}e_n\), the norm \(\rho\) displayed above on \(q^*(\ell_2)\), and the lattice \(X_1\). It also supplies an ambient lattice \(X\supset X_1\) such that every bounded operator \(X\to\ell_2\) is compact.

The prescribed deficits are arbitrary positive numbers tending to zero. The compact set \(K\) may be any nonempty compact subset of \([0,1]\). Positivity is retained throughout. No claim is made about arbitrary weak-cluster geometry outside the one-dimensional scalar factor of this particular construction.

## Proof
Fix \((\varepsilon_k)\subset(0,1)\) with \(\varepsilon_k\to0\) and nonempty compact \(K\subset[0,1]\). Choose a sequence \((t_k)\subset[0,1]\) whose cluster set is exactly \(K\); such a sequence exists because every compact metric space admits finite nets of mesh tending to zero. Altering finitely many \(t_k\) does not change its cluster set.

Choose \(k_0\) so that \(0<\varepsilon_k\le 1/2\) for \(k\ge k_0\). For those indices define
\[
\delta_k=\frac{\varepsilon_k}{1-\varepsilon_k}\in(0,1].
\]
Select an integer \(m_k\) with
\[
\frac1{m_k+1}\le\delta_k\le\frac1{m_k}.
\]
Because \(\delta_k\to0\), these indices can be chosen so that \(m_k\to\infty\). Define
\[
\alpha_k=
\frac{\delta_k^2-(m_k+1)^{-2}}{m_k^{-2}-(m_k+1)^{-2}}
\in[0,1],
\]
and
\[
v_k=\sqrt{\alpha_k}e_{m_k}+\sqrt{1-\alpha_k}e_{m_k+1}.
\]
Then \(v_k\ge0\), \(\|v_k\|_2=1\), and direct substitution gives \(\|Dv_k\|_2=\delta_k\). Hence, with
\[
y_k=(1-\varepsilon_k)q^*v_k,
\]
we have
\[
\rho(y_k)
=(1-\varepsilon_k)(1+\delta_k)=1.
\]
Therefore
\[
z_k=(y_k,t_k)
\]
is positive and lies in \(S_{X_1}\), while
\[
\|Tz_k\|_2=(1-\varepsilon_k)\|v_k\|_2=1-\varepsilon_k.
\]

For each of the finitely many indices \(k<k_0\), use the same two-coordinate construction whenever \(\varepsilon_k\le1/2\). If instead \(\varepsilon_k>1/2\), replace \(t_k\) by \(1\), set \(v_k=e_1\), and set \(y_k=(1-\varepsilon_k)q^*e_1\). Since \(\rho(q^*e_1)=2\), in this latter case \(\rho(y_k)=2(1-\varepsilon_k)<1\); the scalar coordinate \(1\) forces \(z_k=(y_k,1)\in S_{X_1}\), and again \(\|Tz_k\|_2=1-\varepsilon_k\). These finite choices do not affect cluster sets.

It remains to identify the weak cluster set. For \(k\ge k_0\), the support of \(v_k\) escapes to infinity, so \(v_k\rightharpoonup0\) in \(\ell_2\). The bounded map \(q^*\) is weak-to-weak continuous, and multiplication by \(1-\varepsilon_k\) preserves this convergence. Thus \(y_k\rightharpoonup0\) in \((q^*(\ell_2),\rho)\); equivalent norms have the same continuous linear functionals. Consequently the weak cluster points of \(z_k=(y_k,t_k)\) are exactly the points \((0,t)\) with \(t\) a cluster point of \((t_k)\), namely \(\{0\}\times K\).

## Verification
The critical equalities are exact:
\[
\|Dv_k\|_2^2
=\frac{\alpha_k}{m_k^2}+\frac{1-\alpha_k}{(m_k+1)^2}
=\delta_k^2,
\]
\[
\rho((1-\varepsilon_k)q^*v_k)
=(1-\varepsilon_k)\left(1+\frac{\varepsilon_k}{1-\varepsilon_k}\right)=1,
\]
and
\[
\|Tz_k\|_2=1-\varepsilon_k.
\]
No numerical experiment or finite enumeration is used. The only asymptotic step is \(m_k\to\infty\), which follows from \(\delta_k\to0\), and this yields weak convergence of the two-coordinate vectors because every fixed coordinate is eventually zero.

## Relationship to prior work
Costa--Miranda--Ribeiro construct the fixed spaces and operator above and exhibit the particular positive maximizing sequence
\[
\left(\frac{q^*e_n}{1+n^{-1}},1\right),
\]
whose image norms are \(1/(1+n^{-1})\) and which converges weakly to \((0,1)\). Their stated result establishes failure of inheritance of the positive weak maximizing property; it does not state arbitrary exact deficit profiles or arbitrary compact scalar weak-cluster sets for the same fixed operator.

Earlier work on the weak maximizing property studies structural inheritance, compact perturbations, and maximizing sequences, but the comparisons checked here did not yield a theorem that jointly prescribes exact norm deficits and weak-cluster geometry for one fixed positive non-norm-attaining operator. A separate recent diagonal-witness result gives a full ball of weak limits for a different weak-maximizing counterexample; that statement does not imply the joint rate-and-cluster realization above.

## Limitations
The cluster-set classification exploits the explicit \(\ell_\infty\)-summed scalar factor in this construction and is not asserted for arbitrary failures of the weak maximizing property. The proof is real; the source discusses complexification, but no separate complex cluster-set theorem is claimed here. The literature search cannot exclude an unindexed equivalent result under different terminology.

## References
1. Alessandro Costa, Vinícius Miranda, and Geivison Ribeiro, *The weak maximizing property is not inherited by subspaces of the domain*, arXiv:2609.38410v1, 2026.
2. Sheldon Dantas, Mingu Jung, and Gonzalo Martínez-Cervantes, *Some remarks on the weak maximizing property*, Journal of Mathematical Analysis and Applications 503 (2021), 125433, DOI: 10.1016/j.jmaa.2021.125433.
3. Domingo García, Manuel Maestre, Damián Pinasco, and Ignacio Zalduendo, *The weak maximizing property, compact perturbations and duality*, arXiv:2609.23198, 2026.

# Periodic-set small-time control suffices for the noncompact Bowen–Walters bound
## Finding
Let \(\phi=(\phi_t)_{t\in\mathbb R}\) be a flow on a metric space \(X\). Write \(\operatorname{Per}(\phi)\) for the set of periodic points and define the periodic small-time displacement modulus
\[
\omega_{\mathrm{per}}(r)=\sup\left\{d(z,\phi_u(z)):z\in\operatorname{Per}(\phi),\ |u|\le r}\right\}.
\]
Assume that \(\phi\) is geometrically separating, dynamically isolated at infinity, and
\[
\omega_{\mathrm{per}}(r)\longrightarrow0\qquad(r\downarrow0).
\]
Then
\[
\limsup_{T\to\infty}\frac1T\log\nu(T)\le e^{\mathrm{uc}}_{\mathrm{top}}(\phi),
\]
where \(\nu(T)\) is the number of distinct periodic orbits with least period at most \(T\), and \(e^{\mathrm{uc}}_{\mathrm{top}}(\phi)\) is the supremum of the continuous-time upper-capacity entropies over compact subsets of \(X\).

The periodic-set hypothesis is genuinely weaker than uniform \(C_0\) continuity on all of \(X\). For every compact geometrically separating flow \((Y,\psi)\), one can adjoin a single nonperiodic translation orbit whose small-time displacement is nonuniform while preserving both the periodic-orbit collection and the upper-capacity entropy.

## Assumptions and scope
A geometrically separating constant is a number \(\delta>0\) such that, whenever \(x,y\in X\) and an increasing homeomorphism \(s:\mathbb R\to\mathbb R\) with \(s(0)=0\) satisfy
\[
d(\phi_t(x),\phi_{s(t)}(y))<\delta\quad\text{for all }t\in\mathbb R,
\]
then \(x\) and \(y\) lie on the same flow orbit. Dynamic isolation at infinity means that some compact set \(K\subset X\) meets every regular orbit. No compactness of \(X\) is assumed.

The conclusion concerns only the exponential upper growth rate of periodic orbits. It does not claim asymptotics, lower bounds, equidistribution, or that periodic-set small-time control is necessary.

## Proof
Fix a geometrically separating constant \(\delta>0\). Choose \(\eta>0\) so that
\[
\omega_{\mathrm{per}}(\eta)<\delta/2,
\]
and set \(\varepsilon=\delta/4\). Let \(\Gamma\) be a collection of distinct periodic orbits whose least periods lie in one interval \(I\subset(0,T]\) of length at most \(\eta\). Choose one point \(x_\gamma\) on each \(\gamma\in\Gamma\).

Suppose two chosen points \(x\) and \(y\), of least periods \(p\) and \(q\), were not \((T,\varepsilon)\)-separated. Thus
\[
d(\phi_u(x),\phi_u(y))<\varepsilon\qquad(0\le u\le T).
\]
Map each interval \([np,(n+1)p]\) linearly to \([nq,(n+1)q]\). Explicitly, for \(n\in\mathbb Z\) and \(0\le u\le p\), set
\[
s(np+u)=nq+\frac{q}{p}u.
\]
Then
\[
\left|\frac{q}{p}u-u\right|\le |q-p|\le\eta.
\]
Periodicity gives
\[
\phi_{np+u}(x)=\phi_u(x),\qquad
\phi_{s(np+u)}(y)=\phi_{(q/p)u}(y).
\]
The point \(\phi_u(y)\) is itself periodic, so the only small-time displacement needed in the comparison lies on \(\operatorname{Per}(\phi)\). Hence
\[
\begin{aligned}
d(\phi_{np+u}(x),\phi_{s(np+u)}(y))
&\le d(\phi_u(x),\phi_u(y))
   +d(\phi_u(y),\phi_{(q/p)u}(y))\\
&<\varepsilon+\omega_{\mathrm{per}}(\eta)
<\delta.
\end{aligned}
\]
This holds for all real times. Geometric separation would therefore put \(x\) and \(y\) on the same orbit, contrary to the choice of distinct periodic orbits. Thus the selected representatives from every period interval of width at most \(\eta\) form a \((T,\varepsilon)\)-separated set.

Let \(K\) be a compact set meeting every regular orbit. Partition \((0,T]\) into at most \(\lceil T/\eta\rceil\) intervals of length at most \(\eta\). Choose the representative of every periodic orbit inside \(K\). For each period interval there are at most \(s_T^\phi(K,\varepsilon)\) such representatives. Therefore
\[
\nu(T)\le \left\lceil\frac{T}{\eta}\right\rceil s_T^\phi(K,\varepsilon).
\]
After taking logarithms, dividing by \(T\), and passing to the upper limit, the polynomial prefactor disappears and gives
\[
\limsup_{T\to\infty}\frac1T\log\nu(T)
\le e^{\mathrm{uc}}_{\mathrm{top}}(\phi,K)
\le e^{\mathrm{uc}}_{\mathrm{top}}(\phi).
\]

To show strictness of the hypothesis, first replace its metric \(d_Y\) by \(d_Y'=\min\{1,d_Y\}\); this is compatible, bounded by \(1\), and preserves geometric separation after shrinking the separating constant if necessary. Form the disjoint union \(X=Y\sqcup\mathbb R\), set cross-component distances equal to \(2\), and on the real component put
\[
d_R(s,t)=\min\{1,|s^3-t^3|\},\qquad \tau_u(t)=t+u.
\]
The two components are clopen. The flow \(\phi=\psi\sqcup\tau\) is geometrically separating: use a separating constant smaller than both \(1\) and a separating constant for \(Y\); two points in the real component are automatically on the same full translation orbit, and points in distinct components stay distance \(2\) apart. The compact set \(Y\cup\{0\}\) meets every regular orbit, so dynamic isolation at infinity holds.

There are no periodic points on the translation component. Since \(Y\) is compact, small-time displacement is uniform on \(Y\), and therefore \(\omega_{\mathrm{per}}(r)\to0\). Global uniform \(C_0\) continuity nevertheless fails: for every \(r>0\), choose \(0<|u|\le r\) and then \(|t|\) large enough that
\[
|(t+u)^3-t^3|\ge1.
\]
Thus \(\sup_t d_R(t,t+u)=1\).

Finally, the added translation orbit contributes zero upper-capacity entropy. If \(C\subset\mathbb R\) is compact, choose \(M\) with \(C\subset[-M,M]\). For \(s,t\in C\) and \(0\le u\le T\), the mean-value theorem gives
\[
|(s+u)^3-(t+u)^3|\le3(M+T+1)^2|s-t|.
\]
Hence every \((T,\varepsilon)\)-separated subset of \(C\), with \(0<\varepsilon<1\), has cardinality \(O_{C,\varepsilon}((T+1)^2)\), so its exponential growth rate is zero. A compact subset of the disjoint union splits into compact pieces in \(Y\) and \(\mathbb R\); separated-set cardinalities add across the two components. Consequently
\[
e^{\mathrm{uc}}_{\mathrm{top}}(\phi)=e^{\mathrm{uc}}_{\mathrm{top}}(\psi).
\]
Thus the new hypothesis can hold while the global uniform \(C_0\) condition fails, even without changing the periodic-orbit growth problem or its ordinary upper-capacity entropy.

## Verification
The proof uses only the periodic-orbit separation argument and elementary entropy estimates. The critical localization step is explicit: the time-shifted point whose displacement must be controlled remains on the periodic orbit of \(y\), so no small-time estimate away from the periodic-point set enters. The strictness example was checked directly for metric compatibility, flow continuity, geometric separation, dynamic isolation, failure of global uniform \(C_0\), absence of new periodic points, and polynomial separated-set growth on the added component.

## Relationship to prior work
Morales, arXiv:2609.00626v1, proves the same Bowen–Walters upper bound under global uniform \(C_0\) control and explicitly states that it is unknown whether the conclusion remains valid without that hypothesis. Its Lemma 2.3 and proof of Theorem 1.2 use the global modulus precisely in the periodic-orbit comparison localized above. The present statement replaces that global hypothesis by uniform small-time control only on periodic points and supplies an example showing that the replacement is strict.

Yang and Morales, arXiv:2510.13224v1, prove a noncompact periodic-orbit bound for topologically expansive flows using a different conjugacy-invariant entropy-like quantity \(e^*\). That result does not subsume the present statement: topological expansivity is a different, stronger structural hypothesis than geometric separation, and its right-hand side is not the ordinary upper-capacity entropy used here.

The classical compact Bowen–Walters theorem is recovered when \(X\) is compact, since compactness makes small-time displacement uniform on all of \(X\).

## Limitations
This does not settle whether geometric separation and dynamic isolation at infinity alone imply the Bowen–Walters inequality. A 2026 preprint cited by Morales under the title “A noncompact Bowen-Walters inequality” was not available with enough public bibliographic detail for a full-text statement comparison, so possible overlap with that unpublished source remains a specific literature risk. The strictness example is deliberately modular: the added nonperiodic component shows that global uniform \(C_0\) is unnecessary, but it does not exhibit failure of periodic-set small-time control.

## References
1. C. A. Morales, “Entropy on regular sets and periodic-orbit growth for singular flows,” arXiv:2609.00626v1, 2026.
2. Y. Yang and C. A. Morales, “Expansiveness for flows on noncompact spaces,” arXiv:2510.13224v1, 2025.
3. R. Bowen and P. Walters, “Expansive one-parameter flows,” Journal of Differential Equations 12 (1972), 180–193.

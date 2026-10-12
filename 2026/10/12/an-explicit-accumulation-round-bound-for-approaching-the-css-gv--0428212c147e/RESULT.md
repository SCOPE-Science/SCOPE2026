# An explicit accumulation-round bound for approaching the CSS GV threshold
## Finding
Fix an even integer \(s\ge 4\). Let \(h_2\) be binary entropy in bits and let \(\delta_*=h_2^{-1}(1/s)\), the CSS Gilbert--Varshamov distance appearing in the construction of Zhang. For the source's spectral-threshold sequence \(\delta^{(m)}\), define
\[
d_s=\frac{1-\sqrt{1-(2s-1)^{-2}}}{2}.
\]
The source proves \(\delta^{(2)}\ge d_s\) and proves only qualitatively that \(\delta^{(m)}\to\delta_*\). The qualitative compactness step can be made explicit as follows. For \(d_s<\gamma<\delta_*\), put
\[
\varepsilon_s(\gamma)=\frac1s-h_2(\gamma),\qquad
q_s(\gamma)=\left(2^{s\varepsilon_s(\gamma)}-1\right)^{1/s},
\]
\[
\eta_s(\gamma)=-\frac{d_s}2\log_2\left(1-q_s(\gamma)^2\right),
\qquad
M_s(\gamma)=4+\left\lfloor\eta_s(\gamma)^{-1}\right\rfloor.
\]
Then
\[
\delta^{(m)}\ge\gamma\qquad\text{for every }m\ge M_s(\gamma).
\]
For \(0\le\gamma\le d_s\), the source's two-round estimate already gives \(\delta^{(2)}\ge\gamma\).

If \(\Delta=\delta_* -\gamma\downarrow0\), the explicit sufficient round count satisfies
\[
M_s(\delta_* -\Delta)
=K_s\Delta^{-2/s}(1+o(1)),
\]
where
\[
K_s=\frac{2\ln2}{d_s}
\left[s\ln\left(\frac{1-\delta_*}{\delta_*}\right)\right]^{-2/s}.
\]
Thus the spectral threshold is certified to lie within \(\Delta\) of the CSS GV distance after \(O_s(\Delta^{-2/s})\) accumulation rounds.

Combining this with the source's finite-round distance theorem gives a code-level corollary. To guarantee a target distance gap \(\Delta\), choose \(\gamma=\delta_* -\Delta/2\), take \(m\ge M_s(\gamma)\), and use the source theorem with its separate margin equal to \(\Delta/2\). For all sufficiently large blocklengths there then exist rate \(1-2/s\) CSS codes with both relative \(X\)- and \(Z\)-distance exceeding \(\delta_* -\Delta\). The encoder has depth
\[
2s-3+4m\lceil\log_2 n\rceil
\]
and CNOT count
\[
\left(4m+\frac{2s-3}s\right)n,
\]
so this explicit sufficient choice gives depth \(O_s(\Delta^{-2/s}\log n)\) and CNOT count \(O_s(\Delta^{-2/s}n)\).

## Assumptions and scope
The statement uses exactly the spectral recursion \(r_A^{(m)}\), the threshold \(\delta^{(m)}\), and the even repetition parameter \(s\ge4\) defined in arXiv:2610.01277v1. The limit is taken with fixed \(s\). The code-level corollary first fixes the target gap \(\Delta\), hence fixes \(m\), and then lets the blocklength grow. The bound is sufficient and may be very loose numerically. It does not claim that \(\Delta^{-2/s}\) is the true or optimal convergence rate.

## Proof
Suppose \(d_s<\gamma<\delta_*\) and, for some \(m\ge4\), assume for contradiction that \(r_A^{(m)}(\gamma)>0\). The maximizing-chain construction in Proposition 4.5 of the source gives \(\alpha_0,\ldots,\alpha_m=\gamma\) with \(\alpha_i\le1/2\). Its monotonicity argument also gives
\[
\alpha_i>\delta^{(i)}\ge\delta^{(2)}\ge d_s
\qquad (i=2,\ldots,m).
\]
For every \(i=0,\ldots,m-1\), the same proof bounds
\[
r_A^{(m)}(\gamma)
\le -\varepsilon_s(\gamma)
+\frac1s\log_2\left(1+(1-2\alpha_i)^s\right).
\]
Positivity therefore forces
\[
(1-2\alpha_i)^s>2^{s\varepsilon_s(\gamma)}-1=q_s(\gamma)^s,
\]
so, because \(\alpha_i\le1/2\),
\[
\alpha_i<u_s(\gamma):=\frac{1-q_s(\gamma)}2
\qquad (i=0,\ldots,m-1).
\]

Equation 14 of Fagnani--Ravazzi, used explicitly in the source, states
\[
f_A(\alpha,\beta)\le
\alpha\log_2\left(2\sqrt{\beta(1-\beta)}\right).
\]
For every intermediate transition ending at \(\alpha_{i+1}\) with \(i=2,\ldots,m-2\), the first argument is at least \(d_s\) and the second is below \(u_s(\gamma)\). Since \(x\mapsto2\sqrt{x(1-x)}\) is increasing on \([0,1/2]\),
\[
f_A(\alpha_i,\alpha_{i+1})
\le \frac{d_s}2\log_2\left(1-q_s(\gamma)^2\right)
=-\eta_s(\gamma).
\]
The final transition into \(\gamma\) is merely nonpositive, which is sufficient. The same source proof uses \(r_A^{(2)}\le1\), hence
\[
r_A^{(m)}(\gamma)
\le 1-(m-3)\eta_s(\gamma).
\]
If \(m=M_s(\gamma)=4+\lfloor1/\eta_s(\gamma)\rfloor\), then \((m-3)\eta_s(\gamma)>1\), contradicting nonnegativity of \(r_A^{(m)}\). Therefore \(r_A^{(m)}(\gamma)=0\), so \(\delta^{(m)}\ge\gamma\). Monotonicity of \(\delta^{(m)}\) in \(m\) gives the statement for all larger rounds.

For the asymptotic rate, write \(\gamma=\delta_* -\Delta\). Since
\[
h_2'(\delta_*)=\log_2\left(\frac{1-\delta_*}{\delta_*}\right),
\]
we have
\[
\varepsilon_s(\delta_* -\Delta)
=h_2'(\delta_*)\Delta+O(\Delta^2).
\]
Consequently
\[
q_s(\delta_* -\Delta)^2
=\left[s\ln\left(\frac{1-\delta_*}{\delta_*}\right)\Delta\right]^{2/s}(1+o(1)),
\]
and \(-\log_2(1-x)=x/\ln2+O(x^2)\) gives
\[
\eta_s(\delta_* -\Delta)
=\frac{d_s}{2\ln2}
\left[s\ln\left(\frac{1-\delta_*}{\delta_*}\right)\Delta\right]^{2/s}(1+o(1)).
\]
Inverting this expression proves the displayed formula for \(M_s\).

## Verification
The proof uses only inequalities already stated in the primary source plus elementary monotonicity and Taylor expansion. No finite experiment is used as an infinite proof. The accompanying checker recomputes \(\delta_*\), \(d_s\), \(q_s\), \(\eta_s\), and the predicted leading constant for several values of \(s\), and checks the algebraic identity \(4u_s(1-u_s)=1-q_s^2\). These computations are corroborative; the theorem is proved by the displayed inequalities.

## Relationship to prior work
The primary source proves \(\delta^{(m)}\to\delta_*\) and explicitly says that it does not give an explicit characterization of the rate of convergence. Its Proposition 4.5 obtains convergence by placing the maximizing chain in a compact interval and then invoking a uniform negative bound on \(f_A\). The present result makes both ends of that compact interval quantitative and substitutes the explicit Fagnani--Ravazzi inequality already used by the source, producing a closed sufficient round bound and a near-GV power law.

Ravazzi and Fagnani proved qualitative uniform convergence of the classical repeat-multiple-accumulate spectral shapes to the random-linear-code limit. Brehm and Resch later constructed fast codes with fast duals approaching the classical GV bound; their published discussion states that they do not know how to bound the encoding-time constant more precisely as a function of the target GV gap. Neither inspected statement supplies the quantum parity-outer-code bound above.

## Limitations
The explicit \(M_s\) is a certificate, not an estimate of the minimum number of rounds. It is numerically conservative because it uses a global lower bound \(d_s\) for every intermediate first argument and discards the negative contribution of the final transition. The result controls the spectral threshold used in the source and then invokes the source's finite-round distance theorem; it does not provide a finite-blocklength threshold in \(n\), an efficient decoder, or a converse on encoder complexity.

## References
Rachel Yun Zhang, “Linear-Time Encodable Quantum Codes near the CSS GV Bound,” arXiv:2610.01277v1, 2026.

Fabio Fagnani and Chiara Ravazzi, “Spectra and minimum distances of repeat multiple accumulate codes,” Information Theory and Applications Workshop, 2008, DOI 10.1109/ITA.2008.4601028.

Chiara Ravazzi and Fabio Fagnani, “Spectra and Minimum Distances of Repeat Multiple-Accumulate Codes,” IEEE Transactions on Information Theory 55(11), 2009, DOI 10.1109/TIT.2009.2030459.

Martijn Brehm and Nicolas Resch, “Linear Time Encodable Binary Code Achieving GV Bound with Linear Time Encodable Dual Achieving GV Bound,” ITCS 2026, DOI 10.4230/LIPIcs.ITCS.2026.28.

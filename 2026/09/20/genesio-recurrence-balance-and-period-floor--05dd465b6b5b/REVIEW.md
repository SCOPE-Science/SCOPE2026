# Review: Genesio recurrence balances and period floor

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** Direct differentiation of
\[
\mathcal J=yz+\frac a2y^2+\frac c2x^2-\frac13x^3
\]
along the Genesio vector field gives exactly
\[
\dot{\mathcal J}=z^2-by^2.
\]
The symbolic artifact verifies this with zero residual. The bounded-orbit Cesaro identity follows by integration because \(\mathcal J\) is bounded on a bounded orbit. The invariant-measure identity follows from integrating the generator against a compactly supported invariant probability measure. The additional generator identities \(Lx=y\), \(Ly=z\), and \(Lz=-cx-by-az+x^2\) give zero means for \(y,z\) and \(\int x^2=c\int x\). For \(b<0\), the balance forces \(y=z=0\) on the support; for \(b=0\), it forces \(z=0\), and compact invariance then forces the constant velocity \(y\) to vanish. Hence a compact invariant measure with support beyond the equilibria requires \(b>0\).

For \(b\le0\), \(W=-\mathcal J\) is nonincreasing. On a bounded forward orbit, LaSalle's invariance principle places the omega-limit set in the equilibrium set: for \(b<0\), zero dissipation requires \(y=z=0\); for \(b=0\), invariance inside \(z=0\) plus boundedness forces \(y=0\). In both cases invariance then forces \(x(x-c)=0\). Connectedness of the omega-limit set yields convergence to one equilibrium.

For a periodic orbit, integrating the balance gives \(\int z^2=b\int y^2\). Applying sharp Wirtinger to the zero-mean periodic function \(y=x'\) yields \(P\ge2\pi/\sqrt b\). Equality would make \(y\) a pure first harmonic and hence \(x=m+R\cos(\sqrt b t-\phi)\). Substitution leaves \(a x''+cx-x^2=0\), whose second harmonic has coefficient \(-R^2/2\); therefore a nonconstant orbit cannot attain equality. The artifact verifies this Fourier coefficient symbolically.

## Originality

**PASS, to the best of our knowledge.** Close sources were checked for equivalent and stronger coverage.

- Genesio and Tesi (1992) introduced the system in a harmonic-balance study of chaotic motion. The accessible description is heuristic and does not state the exact recurrence identities or period floor.
- Umut and Yasar (2013) gives a detailed numerical and qualitative study of a normalized Genesio jerk equation, including local stability, Hopf onset, period doubling and chaos. It reports that negative-parameter regions produced no bounded attracting dynamics in the computations, but does not provide the global bounded-orbit theorem or the exact recurrent-statistics balance found here.
- Umut's stability paper derives Lyapunov functions and regions of attraction. The accessible article description does not state the compact invariant-measure identities or the strict universal period bound. Its full theorem text was not inspected and remains a prior-coverage risk for the auxiliary-function aspect.
- Cardin and Llibre (2017) treats transcritical and zero-Hopf bifurcations. Diab, Guirao and Vera (2021) treats periodic trajectories near a zero-Hopf point in a generalized Genesio equation. The located statements do not give the present global recurrence restrictions.
- Valls (2025) was inspected in searchable full text. It establishes the Hopf loci and linear Hopf frequency, the global phase portrait at infinity, and nonexistence/classification results for algebraic and analytic integrability. Searches within the full text did not locate invariant-measure balances, a LaSalle recurrence barrier, or a minimum-period theorem. Its Hopf frequency supplies the limiting constant that shows the present strict period floor is locally sharp.
- Classical third-order stability literature descending from Barbasin (1952) studies equations broad enough to include related scalar jerk equations. The original 1952 full text was not inspected. An equivalent auxiliary function may therefore be classical; the originality claim is focused on the Genesio-specific global recurrence consequences, invariant-measure constraints, and strict sharp period floor.
- Searches through current literature for Genesio minimum-period bounds, invariant measures, exact \(L^2\) velocity/acceleration balances, and synonymous third-order jerk formulations did not locate an equivalent theorem.

The direction of improvement is exact and global: local Hopf calculations identify where cycles emerge, whereas the present theorem constrains every periodic orbit and every compact invariant statistical state, and gives a complete bounded-orbit recurrence obstruction throughout the half-space \(b\le0\).

## Value

**PASS.** The result turns one exact differential identity into three reusable diagnostics: an RMS relation for recurrent statistics, a rigorous sign boundary excluding bounded non-equilibrium recurrence, and an optimal universal period floor. The strict inequality distinguishes the nonlinear periodic orbit from the linear Hopf timescale while proving that the Hopf value is the limiting lower edge rather than an attainable nonlinear period. The parameter restrictions are independent of numerical orbit searches and apply across the full real parameter family.

## Scientific limitations

The bounded-orbit convergence theorem assumes the trajectory remains bounded; it does not establish ultimate boundedness or exclude escape to infinity. Compact invariant sets consisting of equilibria and connecting orbits are not ruled out merely by the recurrence statement. The invariant-measure claims require compact support.

Originality is a literature-search judgment. The 1952 Barbasin source was not inspected in full and could contain an equivalent auxiliary identity for a broader third-order scalar equation. The full theorem text of Umut's Genesio stability article was also not inspected. These are the principal identified prior-coverage risks. By contrast, the searchable full text of Valls (2025) was inspected and does not state the present invariant-measure, bounded-orbit, or minimum-period conclusions.

## Checked sources

- https://doi.org/10.1016/0005-1098(92)90177-H
- https://doi.org/10.4236/ijmnta.2013.21007
- https://doi.org/10.17654/0972111813014
- https://doi.org/10.1007/s11071-016-3259-2
- https://doi.org/10.3390/math9040354
- https://doi.org/10.3934/dcdsb.2025016
- Barbasin, Priklad. Mat. Mekh. 16 (1952), 629--632

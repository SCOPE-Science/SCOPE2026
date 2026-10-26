# A sharp group-size crossover in networked contribution decay
## Finding

Consider the distance-decay contribution model in which agents infer distant contributions from the average contributions of neighbors lying on shortest paths. Let \(M_G(\delta)\) be its linear update matrix on a connected, simple, undirected graph \(G\) with \(n\) vertices and \(0<\delta<1\). Write \(S_n=K_{1,n-1}\) for the star and \(C_n\) for the cycle. If \(\rho_S(n,\delta)=\rho(M_{S_n}(\delta))\) and \(\rho_C(n,\delta)=\rho(M_{C_n}(\delta))\), then
\[
\rho_C(n,\delta)>\rho_S(n,\delta)\quad(n=3,4),
\]
whereas
\[
\rho_S(n,\delta)>\rho_C(n,\delta)\quad(n\ge5).
\]
Thus the exact ordering of asymptotic persistence reverses at the sharp group size \(n=5\), for every admissible \(\delta\). “Persistence” here means the spectral-radius factor of the linear recurrence, not an ordering of finite-time averages for every initial condition.

The exact formulas are
\[
\rho_S(n,\delta)=\delta\sqrt{\frac{1+(n-2)\delta}{n-1}},
\]
and
\[
\rho_C(n,\delta)=\frac{1}{n-1}\left(2\sum_{r=1}^{\lfloor(n-1)/2\rfloor}\delta^r+\mathbf 1_{2\mid n}\delta^{n/2}\right).
\]

## Assumptions and scope

The recurrence is the model specified by Fatas et al. (first published online 27 July 2014): the graph is finite, connected, simple, unweighted, and undirected; agents directly observe neighbors; and a contribution at graph distance \(r\) is inferred with factor \(\delta^{r-1}\), averaged over neighbors one step closer to the target. The updating rule multiplies the sum of inferred contributions by \(\delta/(n-1)\).

For \(i\ne j\), let \(d_G(i,j)\) be graph distance and \(N_{i,j}\) the nonempty set of neighbors \(k\) of \(i\) satisfying \(d_G(k,j)=d_G(i,j)-1\). Then
\[
c_i(t)=\frac{1}{n-1}\sum_{j\ne i}\frac{\delta^{d_G(i,j)}}{|N_{i,j}|}\sum_{k\in N_{i,j}}c_k(t-1).
\]
The result compares only \(S_n\) and \(C_n\). It does not assert a general ordering for arbitrary graphs, nor does it imply that finite-time averages or welfare are ordered in the same way.

## Proof

Let \(M_G(\delta)\) be the matrix in the recurrence. Summing row \(i\), the average over \(N_{i,j}\) contributes total weight one for each target \(j\), so
\[
\sum_k(M_G)_{ik}=\frac{1}{n-1}\sum_{j\ne i}\delta^{d_G(i,j)}.
\]
For a cycle this row sum is independent of \(i\). The all-ones vector is therefore an eigenvector with that eigenvalue, and the nonnegative-matrix row-sum bound shows it is the spectral radius. Counting vertices at each cycle distance gives the formula for \(\rho_C\).

For the star, the center's update row has coefficient \(\delta/(n-1)\) at each leaf. A leaf's row has only one nonzero entry, at the center, with coefficient
\[
\frac{\delta+(n-2)\delta^2}{n-1}.
\]
The two nonzero eigenvalues are
\[
\pm\sqrt{(n-1)\frac{\delta}{n-1}\frac{\delta+(n-2)\delta^2}{n-1}},
\]
which gives the formula for \(\rho_S\).

Set
\[
F_n(\delta)=\frac{(n-1)\rho_C(n,\delta)}{\delta},\qquad
P_n(\delta)=(n-1)(1+(n-2)\delta)-F_n(\delta)^2.
\]
The sign of \(P_n\) is the sign of \(\rho_S^2-\rho_C^2\). Direct expansion gives \(P_3=2\delta-2<0\), \(P_4=-(1-\delta)^2<0\), and \(P_5=4\delta(1-\delta)>0\).

For \(n=2m+1\ge7\), \(F_n=2\sum_{j=0}^{m-1}\delta^j\); for \(n=2m\ge6\), \(F_n=2\sum_{j=0}^{m-2}\delta^j+\delta^{m-1}\). In either parity, the polynomial \(P_n\) has positive constant and linear coefficients and strictly negative coefficients at every power \(\delta^k\) for \(k\ge2\). Also \(P_n(1)=0\), since \(F_n(1)=n-1\). Write \(P_n=(1-\delta)Q_n\). The coefficients of \(Q_n\) are the successive partial sums of the coefficients of \(P_n\): they start positive and then strictly decrease, while the final coefficient is the negative of the leading coefficient of \(P_n\), hence positive. Thus every coefficient of \(Q_n\) is positive and \(P_n(\delta)>0\) on \(0<\delta<1\). This proves \(\rho_S>\rho_C\) for all \(n\ge5\) and completes the classification.

## Verification

The formulas follow from the recurrence and exact graph-distance counts. The comparison uses polynomial identities and a coefficient-sign argument valid for every integer \(n\), not a finite graph census or numerical spectral estimates. The inequalities are strict for \(0<\delta<1\); the two rates meet only at the continuous boundary limits \(\delta=0\) and \(\delta=1\), outside the strict parameter range.

## Relationship to prior work

Fatas, Meléndez-Jiménez, Morales, and Solaz introduce the distance-decay recurrence and give an explicit solution for the four-agent star. Their article compares the complete network, circle, line, and star in a four-agent experimental setting, including simulations. The result here gives exact spectral-radius formulas for arbitrary group size and proves the sharp all-parameter crossover between the star and cycle. The earlier recurrence is the model source, not a statement of the arbitrary-\(n\) comparison.

## Limitations

The spectral radius describes the asymptotic linear persistence factor. In even cycles and stars, a negative eigenvalue can produce alternating components, and the theorem does not claim componentwise monotonicity at each time. The comparison is restricted to a star and a cycle under the stated inference rule; changing the information rule, allowing weighted edges, or using other graph families may change the ordering. No empirical claim is made about actual cooperation or welfare.

## References

1. E. Fatas, M. A. Meléndez-Jiménez, A. J. Morales, and H. Solaz, “Public goods and decay in networks,” *SERIEs* 6 (2015), 73–90; first published online 27 July 2014. DOI: \(10.1007/s13209-014-0114-x\). Open-access full text: https://link.springer.com/article/10.1007/s13209-014-0114-x.

# Exact discord–teleportation region for Bell-diagonal two-qubit states
## Finding
For a two-qubit Bell-diagonal state
\[
\rho=\frac14\left(I\otimes I+\sum_{j=1}^{3}c_j\,\sigma_j\otimes\sigma_j\right),
\]
write \(s_1\ge s_2\ge s_3\ge0\) for the ordered magnitudes of \((c_1,c_2,c_3)\). Use the normalized Hilbert–Schmidt geometric discord convention
\[
D_G=\frac13\left(s_2^2+s_3^2\right)
\]
and the standard optimal average teleportation fidelity
\[
F=\frac12\left(1+\frac{s_1+s_2+s_3}{3}\right).
\]
For the useful-teleportation range \(2/3\le F\le1\), the exact set of attainable normalized geometric discord values is the interval
\[
\frac23(3F-2)^2\le D_G\le U(F),
\]
where
\[
U(F)=
\begin{cases}
\dfrac{45F^2-54F+17}{12},&\dfrac23\le F\le\dfrac9{13},\\[4pt]
\dfrac23(2F-1)^2,&\dfrac9{13}\le F\le1.
\end{cases}
\]
Both bounds are sharp for every admissible \(F\), every intermediate value is attained, and the upper extremizer changes family exactly at \(F=9/13\).

## Assumptions and scope
The state is Bell diagonal and the discord normalization is the one in which the two-qubit formula is \(D_G=(\|x\|^2+\|T\|^2-\lambda_{\max})/3\); Bell-diagonal states have \(x=0\). The fidelity is the standard optimized average fidelity of the usual qubit teleportation protocol, for which Bell-diagonal states satisfy \(F=(1+q/3)/2\) with \(q=s_1+s_2+s_3\). The theorem is restricted to \(q\in[1,3]\), equivalently \(F\in[2/3,1]\). It makes no claim that Hilbert–Schmidt geometric discord is monotone under arbitrary local channels.

## Proof
Fix \(q=s_1+s_2+s_3\in[1,3]\). For \(q>1\), every physical Bell-diagonal correlation vector is, up to Bell-state symmetries, represented by
\[
(c_1,c_2,c_3)=(s_1,-s_2,s_3).
\]
Its Bell-basis eigenvalues are
\[
\frac{1+s_1+s_2+s_3}{4},\quad
\frac{1-s_1-s_2+s_3}{4},\quad
\frac{1+s_1-s_2-s_3}{4},\quad
\frac{1-s_1+s_2-s_3}{4}.
\]
Because \(s_1\ge s_2\ge s_3\), the second eigenvalue is the smallest. Positivity is therefore equivalent to
\[
s_1+s_2-s_3\le1.
\]
The same description extends to \(q=1\) by closure.

Put \(y=s_2\), \(z=s_3\), and \(s_1=q-y-z\). Ordering and positivity become exactly
\[
\frac{q-1}{2}\le z\le\frac q3,
\qquad
z\le y\le\frac{q-z}{2}.
\]
On this compact connected feasible set,
\[
D_G=\frac{y^2+z^2}{3}.
\]
For fixed \(z\), the minimum occurs at \(y=z\), and then increases with \(z\). Hence
\[
D_{G,\min}(q)=\frac{(q-1)^2}{6},
\]
attained at
\[
(s_1,s_2,s_3)=\left(1,\frac{q-1}{2},\frac{q-1}{2}\right).
\]

For fixed \(z\), the maximum occurs at \(y=(q-z)/2\). Thus it remains to maximize the convex quadratic
\[
g(z)=\frac13\left(\frac{(q-z)^2}{4}+z^2\right)
\]
over \([(q-1)/2,q/3]\), so an endpoint is optimal. At the lower endpoint,
\[
D_L(q)=\frac{5q^2-6q+5}{48},
\qquad
(s_1,s_2,s_3)=\left(\frac{q+1}{4},\frac{q+1}{4},\frac{q-1}{2}\right),
\]
while at the upper endpoint,
\[
D_U(q)=\frac{2q^2}{27},
\qquad
(s_1,s_2,s_3)=\left(\frac q3,\frac q3,\frac q3\right).
\]
Their difference factors as
\[
D_L(q)-D_U(q)=\frac{13(q-3)(q-15/13)}{432}.
\]
Thus the upper extremizer changes at \(q=15/13\), equivalently \(F=9/13\). Substituting \(q=6F-3\) gives the displayed formulas. Since the feasible set at fixed \(q\) is connected and \(D_G\) is continuous, its image is the full interval between the sharp minimum and maximum, proving attainability of every intermediate value.

## Verification
A standalone exact-rational checker enumerates a denominator-30 grid of Bell-state probability vectors, reconstructs the correlation singular values, and verifies the two sharp inequalities for every grid state with \(q\ge1\). It separately checks both analytic extremal families on a rational grid and verifies the crossover \(q=15/13\), \(F=9/13\). These finite checks are supplementary: the theorem for all states follows from the analytic positivity reduction and one-dimensional extremization above.

## Relationship to prior work
Yao et al. give the Bell-diagonal tetrahedron geometry and the Hilbert–Schmidt geometric-discord formula from which the normalized expression used here follows after the stated normalization. Adhikari and Banerjee derive broad inequalities connecting geometric-discord quantities to teleportation fidelity and discuss the Werner family, but their results do not give the exact fixed-fidelity attainable interval of the actual normalized Bell-diagonal discord. The isotropic Werner-type line is precisely the upper extremizer only on the branch \(F\ge9/13\); below that crossover a different boundary family is optimal. Horodecki et al. provide the standard teleportation-fidelity criterion underlying the fidelity parameter. Roszak and Cywiński study Bell-diagonal teleportation using best- and worst-case input-state fidelities, a different performance functional from the standard optimal average fidelity fixed here.

## Limitations
The result is confined to two-qubit Bell-diagonal states and the normalized Hilbert–Schmidt geometric discord. It does not extend automatically to entropic discord, trace-distance discord, non-Bell-diagonal states, or channel-monotone resource measures. A highly relevant Bell-diagonal teleportation paper by Roszak and Cywiński was compared at the abstract/available-preview level because a full primary-text copy was not accessible in this run; its stated best/worst-case fidelity functional differs from the average-fidelity slice proved here, but this remains a residual literature-access risk rather than evidence of coverage.

## References
1. Y. Yao, H.-W. Li, Z.-Q. Yin, and Z.-F. Han, “Geometric interpretation of the geometric discord,” arXiv:1303.4827 (first public 2013-03-20).
2. S. Adhikari and S. Banerjee, “An Operational Meaning of Discord in terms of Teleportation Fidelity,” arXiv:1207.7226 (first public 2012-07-31).
3. R. Horodecki, M. Horodecki, and P. Horodecki, “Teleportation, Bell's Inequalities and Inseparability,” arXiv:quant-ph/9606027 (first public 1996-06-25).
4. K. Roszak and Ł. Cywiński, “The relation between the quantum discord and quantum teleportation: the physical interpretation of the transition between classical and quantum decoherence,” arXiv:1505.05741 (first public 2015-05-21).

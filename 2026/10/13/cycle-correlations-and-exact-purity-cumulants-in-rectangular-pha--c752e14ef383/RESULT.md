# Cycle correlations and exact purity cumulants in rectangular phase-random states

## Finding
Fix integers \(d,m\ge2\). Draw \(dm\) independent Haar-uniform unit-modulus complex variables \(z_{aj}\), indexed by \(1\le a\le d\), \(1\le j\le m\). In \(\mathbb C^d\otimes\mathbb C^m\), define the pure state
\[
|\Psi\rangle=\frac1{\sqrt{dm}}\sum_{a=1}^d\sum_{j=1}^m z_{aj}|a\rangle\otimes|j\rangle,
\qquad \rho=\operatorname{Tr}_{\mathbb C^m}|\Psi\rangle\langle\Psi|,
\qquad P=\operatorname{Tr}\rho^2.
\]
Then the exact finite-dimensional mean, variance, and third centered moment are
\[
\boxed{\mathbb EP=\frac{d+m-1}{dm}},\qquad
\boxed{\operatorname{Var}(P)=\frac{2(d-1)(m-1)}{d^3m^3}},
\]
\[
\boxed{\mathbb E(P-\mathbb EP)^3=\frac{8(d-1)(m-1)(d+m-4)}{d^5m^5}}.
\]
The standardized skewness is
\[
\gamma_1(P)=\frac{2\sqrt2(d+m-4)}{\sqrt{dm(d-1)(m-1)}}.
\]
For distinct row labels \(a,b\), set
\[
Y_{ab}=\Big|\sum_{j=1}^m z_{aj}\overline{z_{bj}}\Big|^2.
\]
For any simple graph \(G\) on row vertices \(\{1,\ldots,d\}\), the family \(\{Y_{ab}:\{a,b\}\in E(G)\}\) is mutually independent **if and only if** \(G\) is a forest. Every simple cycle \(C\) has the exact nonvanishing centered mixed moment
\[
\mathbb E\prod_{\{a,b\}\in E(C)}(Y_{ab}-m)=m(m-1).
\]
Thus individual edge overlaps are pairwise independent but cycles detect their higher-order dependence. Triangles supply the extra positive term in the purity's third centered moment.

## Assumptions and scope
The phases are independent and Haar-uniform on the unit circle, not Gaussian or Haar-uniform bipartite states. The Schmidt dimensions \(d\) and \(m\) are arbitrary integers at least two, and the reduced state is normalized as \(\rho=ZZ^\dagger/(dm)\), where \(Z=(z_{aj})\). The graph is simple: no loops or duplicated edges. All expectations refer to these independent phases. The statements are exact at finite dimensions; no limiting regime or unverified ensemble equivalence is used. If either Schmidt dimension is one, the purity is identically one; the nondegenerate variance and skewness statements are formulated for dimensions at least two.

## Proof
**1. Reduction to edge overlaps.** Since \(\rho_{ab}= (dm)^{-1}\sum_jz_{aj}\overline{z_{bj}}\), its diagonal entries are \(1/d\), and therefore
\[
P=\frac1d+\frac2{d^2m^2}\sum_{1\le a<b\le d}Y_{ab}.
\tag{1}
\]
For each edge \(\{a,b\}\), the variables \(w_j=z_{aj}\overline{z_{bj}}\) are independent uniform unit phases. Expanding \(Y_{ab}=|\sum_jw_j|^2\) and using \(\mathbb Ew^r=0\) for every nonzero integer \(r\) gives
\[
\mathbb EY_{ab}=m,\quad
\mathbb EY_{ab}^2=2m^2-m,\quad
\mathbb EY_{ab}^3=6m^3-9m^2+4m.
\tag{2}
\]
For the cubic identity, balanced index multisets have types \((3)\), \((2,1)\), and \((1,1,1)\), contributing \(m\), \(9m(m-1)\), and \(6m(m-1)(m-2)\), respectively. Consequently,
\[
\operatorname{Var}(Y_{ab})=m(m-1),\qquad
\mathbb E(Y_{ab}-m)^3=2m(m-1)(m-2).
\tag{3}
\]

**2. Forest independence.** For an oriented edge \(a\to b\) and column \(j\), let \(w_{ab,j}=z_{aj}\overline{z_{bj}}\). If \(G\) is a forest, choose a root in each component. For each fixed column, the change of variables from all vertex phases to component-root phases and oriented edge ratios is an invertible Haar-preserving transformation of the phase torus: solve vertex phases successively away from the roots. Thus all edge ratios \(w_{ab,j}\) are independent uniform phases. Different columns are independent as well, and every \(Y_{ab}=|\sum_jw_{ab,j}|^2\) depends only on its own independent edge-ratio vector. This proves mutual independence over any forest, including every pair of distinct edges.

**3. Cycles obstruct independence.** Orient the edges of a simple cycle coherently, with consecutive vertices \(v_1,\ldots,v_\ell\) and \(v_{\ell+1}=v_1\). For each oriented edge \(a\to b\),
\[
Y_{ab}-m=\sum_{j\ne k}w_{ab,j}\overline{w_{ab,k}}
=\sum_{j\ne k} z_{aj}\overline{z_{ak}}\overline{z_{bj}}z_{bk}.
\tag{4}
\]
In the expectation of the product of these sums around the cycle, each phase at each vertex must have net exponent zero. At a vertex incident to the preceding and following oriented edges, this forces the ordered pair \((j,k)\) to coincide on those two edges. Connectivity forces one common ordered pair all the way around the cycle. Exactly \(m(m-1)\) pairs satisfy \(j\ne k\), and each contributing monomial has expectation one; all other monomials have expectation zero. Hence
\[
\mathbb E\prod_{e\in E(C)}(Y_e-m)=m(m-1)>0.
\tag{5}
\]
If a graph contains a cycle, these centered variables therefore cannot be mutually independent; combined with step 2, this proves the if-and-only-if statement.

**4. Purity moments.** Put \(X=\sum_{a<b}(Y_{ab}-m)\). By forest independence for any two distinct edges,
\[
\mathbb EX=0,\quad
\mathbb EX^2={d\choose2}m(m-1).
\tag{6}
\]
In \(\mathbb EX^3\), terms containing exactly two distinct edges vanish by pairwise independence. For three distinct edges, the edge subgraph is a forest unless it is a triangle; the only surviving mixed terms therefore come from the \({d\choose3}\) triangles and have the value in (5). Using (3),
\[
\begin{aligned}
\mathbb EX^3
&={d\choose2}\,2m(m-1)(m-2)
+6{d\choose3}\,m(m-1)\\
&=d(d-1)m(m-1)(d+m-4).
\end{aligned}
\tag{7}
\]
Equation (1) gives \(P-\mathbb EP=2X/(d^2m^2)\); inserting (6) and (7) proves the stated exact mean, variance, third centered moment, and standardized skewness. Positivity and vanishing at \(d=m=2\) follow directly from these exact formulas.

## Verification
The standalone standard-library script `artifacts/verify.py` expands the centered purity as a Laurent polynomial in the independent phases and extracts exact zero Fourier coefficients of its second and third powers for dimensions \((2,2)\), \((2,3)\), \((3,2)\), \((3,3)\), \((3,4)\), and \((4,3)\). It also checks exact centered edge-product coefficients for triangles and four-cycles at column counts two and three. Run `python3 artifacts/verify.py` in an extracted package directory. These finite tests corroborate, but do not replace, the all-dimensional proof above.

## Relationship to prior work
Lakshminarayan, Puchała and Życzkowski (arXiv:1407.1169v1, Section III, especially Eqs. (7)–(10)) introduce and analyze the square unimodular phase ensemble and determine \(\mathbb E\operatorname{Tr}\rho^2\) and higher **single-trace spectral moments**. Their quantum-gate interpretation motivates this exact ensemble. Nakata, Turner and Murao (arXiv:1111.2747, Section III and Appendix A) study phase-random-state average linear entropy and concentration, including a standard-deviation estimate. Garza Vargas (arXiv:1709.01498, Sections 2–3) develops broad combinatorial traffic-moment tools for the **square** unimodular ensemble, which may in principle assist in computing many correlations. Those are prior contributions. The present claim specifies the rectangular finite-dimensional third **centered purity moment**, an exact graph-cycle mixed-moment identity, and the forest-versus-cycle joint-independence classification; it is not a claim that prior mean-purity formulas or general phase orthogonality are new.

## Limitations
This treats the equal-amplitude independent-phase ensemble only, not Haar-distributed states, correlated phases, random amplitudes, or arbitrary mixed-state ensembles. The formulas do not establish a central limit theorem, a full probability density, or general cumulants beyond order three. Pairwise independence does not imply mutual independence on cycles. The published traffic formalism gives a powerful broader approach to graph-moment enumeration; an equivalent specialization under different language is a literature risk. No independent audit has been performed.

## References
1. A. Lakshminarayan, Z. Puchała and K. Życzkowski, *Diagonal unitary entangling gates and contradiagonal quantum states*, arXiv:1407.1169v1 (public 2014-07-04), especially Section III and Eqs. (7)–(10); *Phys. Rev. A* **90**, 032303 (2014).
2. Y. Nakata, P. S. Turner and M. Murao, *Phase-random states: Ensembles of states with fixed amplitudes and uniformly distributed phases in a fixed basis*, arXiv:1111.2747, especially Section III and Appendix A; *Phys. Rev. A* **86**, 012301 (2012).
3. J. Garza Vargas, *The traffic distribution of the squared unimodular random matrix and a formula for the moments of its ESD*, arXiv:1709.01498, especially Sections 2–3; *Reports on Mathematical Physics* **81**, 273–282 (2018).

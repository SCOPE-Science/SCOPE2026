# Exact finite-width frozen-state entropy and occupancy in the spiral kinetic model

## Finding
For every integer \(n\ge4\), let \(Z_n(z)\) be the occupancy-counting polynomial of fixed points of the **monotone spiral culling cellular automaton** on the periodic \(n\)-by-\(3\) lattice. An exact \(64\)-state transfer matrix \(T(z)\), specified below, satisfies \(Z_n(z)=\operatorname{tr}T(z)^n\). At unit weight,
\[
\det(\lambda I-T(1))=\lambda^{44}P(\lambda)Q(\lambda),
\]
with
\[
\begin{aligned}
P(\lambda)&=\lambda^8-8\lambda^7+11\lambda^6-11\lambda^5+29\lambda^4-7\lambda^3-24\lambda^2+\lambda+3,\\
Q(\lambda)&=\lambda^{12}+4\lambda^{10}+\lambda^9+13\lambda^8-9\lambda^7+6\lambda^6+17\lambda^5+15\lambda^4-2\lambda^3+4\lambda^2+\lambda+1.
\end{aligned}
\]
The Perron root \(\alpha=6.459175219768575\ldots\) is the unique positive root of \(P\) in \((6,7)\). Consequently, the entropy per site of these fixed points is
\[
\lim_{n\to\infty}\frac{\log Z_n(1)}{3n}=\frac{\log\alpha}{3}=0.6218338782283147\ldots.
\]
If one samples uniformly from the fixed points and lets \(N_n\) be the number of occupied sites, then
\[
\frac{N_n}{3n}\xrightarrow{\mathbb P}\rho_*=0.6089266973105203\ldots,
\qquad
\rho_*=-\frac{R(\alpha)}{3\alpha P'(\alpha)},
\]
where \(R(\lambda)=-12\lambda^7+22\lambda^6-46\lambda^5+165\lambda^4-14\lambda^3-208\lambda^2+6\lambda+36\). Exact unweighted counts are \(Z_4(1)=1738\), \(Z_5(1)=11303\), and \(Z_6(1)=72790\).

## Assumptions and scope
Lattice sites are \((x,y)\in(\mathbb Z/n\mathbb Z)\times(\mathbb Z/3\mathbb Z)\), with occupation \(\eta(x,y)\in\{0,1\}\). Each occupied site is culled in one synchronous step precisely when at least one of its north-east/south-west neighbor pairs and at least one of its north-west/south-east neighbor pairs are simultaneously empty. Relative to \((x,y)\), the four two-site pairs are
\[
\begin{array}{ll}
NE=\{(0,1),(1,1)\},&SW=\{(0,-1),(-1,-1)\},\\
NW=\{(-1,0),(-1,1)\},&SE=\{(1,0),(1,-1)\}.
\end{array}
\]
All coordinates are periodic, and vacancies stay vacant. A **fixed point** is a configuration in which no currently occupied site is culled. This is not a count of configurations in which both occupied and unoccupied sites are unflippable under the separate reversible-temperature spin model. No statement is made about probabilities of dynamically reaching particular fixed points. The 3-site circumference is part of the model and is not sent to infinity.

## Proof
Identify the occupation of each column \(x\) with an integer \(b\in\{0,\ldots,7\}\); write \(b_y\in\{0,1\}\) for its bit indexed by \(y\) modulo \(3\). The middle column \(b\) is locally unchanged between left column \(a\) and right column \(c\) exactly when, for every \(y\) satisfying \(b_y=1\),
\[
\big((b_{y+1}\lor c_{y+1})\land(b_{y-1}\lor a_{y-1})\big)
\lor
\big((a_y\lor a_{y+1})\land(c_y\lor c_{y-1})\big)
\]
is true (Boolean operations). Indeed, the first conjunction negates the event that NE or SW is wholly empty, while the second negates the event that NW or SE is wholly empty; their disjunction is the negation of the conjunction required for culling.

Index the \(64\) rows and columns of \(T(z)\) by ordered pairs \((a,b)\). Put \(T(z)_{(a,b),(b,c)}=z^{|b|}\) if the local test holds, and zero otherwise, where \(|b|\) is the number of occupied bits. Every cyclic length-\(n\) closed walk corresponds bijectively to an \(n\)-tuple of column masks satisfying all local tests, with multiplicative weight \(z\) for each occupied site. This proves \(Z_n(z)=\operatorname{tr}T(z)^n\).

Exact polynomial elimination of this explicit integer-polynomial matrix, independently replayable in the accompanying program, establishes the characteristic factorization at \(z=1\) above. For the factor carrying the Perron eigenvalue, the full weighted polynomial is
\[
\begin{aligned}
P(\lambda,z)={}&\lambda^8-(z+1)^3\lambda^7+z(3z^2+5z+3)\lambda^6\\
&-z^2(3z^4+3z^3+3z+2)\lambda^5\\
&+z^4(z^4+5z^3+10z^2+10z+3)\lambda^4\\
&+z^5(z^5+2z^4+6z^3-10z-6)\lambda^3\\
&-z^7(5z^3+8z^2+9z+2)\lambda^2-z^9(z^3-2)\lambda+3z^{12}.
\end{aligned}
\]
The same exact matrix computation verifies that \(P(\lambda,z)\) divides the full characteristic polynomial for indeterminate \(z\), and that \(\partial_zP(\lambda,z)|_{z=1}=R(\lambda)\).

The directed graph of nonzero matrix entries has one strongly connected component of \(52\) states and \(12\) singleton acyclic components. The large component contains the all-occupied self-loop \((7,7)\to(7,7)\); it is therefore primitive, and its Perron eigenvalue is simple, positive, strictly dominant in modulus, and differentiable analytically with respect to positive \(z\) near \(1\). The displayed factorization shows \(\alpha\in(6,7)\): the values \(P(6)=-96975\) and \(P(7)=351781\) have opposite signs; \(P(6+t)\) has exactly one sign change in descending coefficient order, giving uniqueness above \(6\) by Descartes' rule. Also \(Q(\lambda)>0\) for all real \(\lambda\ge6\): group \(\lambda^{12}-9\lambda^7>0\), \(15\lambda^4-2\lambda^3>0\), and the remaining strictly positive terms. Therefore no other positive eigenvalue exceeds \(6\), so the Perron root equals \(\alpha\). The \(12\) acyclic states contribute no trace of positive powers, so \(Z_n(1)\) has exponential rate \(\alpha^n\).

Implicit differentiation of \(P(\alpha(z),z)=0\) yields \(\alpha'(1)=-R(\alpha)/P'(\alpha)\). Under uniform sampling of fixed points,
\[
\mathbb E e^{tN_n}=\frac{Z_n(e^t)}{Z_n(1)},\quad
\lim_{n\to\infty}\frac1n\log\mathbb E e^{tN_n}
=\log\alpha(e^t)-\log\alpha(1)
\]
for real \(t\) sufficiently close to zero. Differentiating at zero gives \(\alpha'(1)/\alpha\). Chernoff estimates for small positive and negative \(t\) then yield \(N_n/n\to\alpha'(1)/\alpha\) in probability, establishing the occupied-site density after division by \(3\).

## Verification
Run `python3 artifacts/verify.py` (Python 3.10+, SymPy 1.12+). The script constructs \(T(z)\) from the printed physical neighborhood rule, computes its exact characteristic polynomial and its factorization, checks graph strong components, and compares transfer-weight histograms with a second direct coordinate-level implementation for all \(2^{12}+2^{15}+2^{18}=299008\) configurations of lengths \(4,5,6\). It verifies the three displayed exact totals, the weighted factor and derivative, and the quoted root/density to high precision. The finite enumeration checks examples, not the infinite-size conclusions; those use the transfer representation and Perron–Frobenius/Chernoff argument.

## Relationship to prior work
Toninelli and Biroli (arXiv:0709.0378v1, 2007, particularly Secs. 2–3 and 6) introduced and analyzed the monotone spiral culling rule and the two-dimensional jamming-percolation transition; Biroli and Toninelli (arXiv:0709.0583v1, 2007) discuss its physical interpretation. Their infinite-lattice threshold and finite-size emptying estimates do not imply the exact stationary microstate count, entropy, or density on the periodic three-row system. The latter are a different finite-width ensemble, not a consequence of the limiting two-dimensional blocked fraction. Standard transfer-matrix methods motivate the counting approach, but the specific characteristic factor and occupancy limit are additional model-specific computations.

## Limitations
The width is exactly three and the longitudinal circumference is at least four; no claim is made for larger widths, the full two-dimensional lattice, reachability statistics, correlations, mixing, or reversible spin-model frozen configurations. The fixed-point ensemble is uniform over all fixed points, rather than the distribution induced by a given random initial state. Complete novelty cannot be guaranteed against unindexed literature. The exact symbolic certificate requires SymPy and its computations are reproduced from scratch, not an independent formal proof assistant.

## References
1. C. Toninelli and G. Biroli, *Spiral Model: a cellular automaton with a discontinuous glass transition*, arXiv:0709.0378v1 (first submitted 2007-09-04), especially Secs. 2, 3, 6, 7.
2. G. Biroli and C. Toninelli, *Spiral model, jamming percolation and glass-jamming transitions*, arXiv:0709.0583v1 (first submitted 2007-09-05).
3. C. Toninelli, G. Biroli, and D. S. Fisher, *Jamming percolation and glass transitions in lattice models*, arXiv:cond-mat/0509661 (2005), for the related physical framework.

# Orthogonal four-cycle residuals in uniform random tournaments

## Finding

Fix an integer \(n\ge4\). Give each edge of the complete graph on \([n]\) one of its two directions independently with equal probability. Let \(T_n\) count cyclic triangles and let \(Q_n\) count simple directed four-cycles up to cyclic rotation (in a tournament, each four-set supports at most one such cycle). Set
\[
Z_n=Q_n-\frac38\binom n4-\frac{n-3}{2}\left(T_n-\frac14\binom n3\right).
\]
The residual \(Z_n\) is a homogeneous Walsh polynomial of degree four in the independent edge-direction signs, with exactly \(3\binom n4\) distinct monomials, each having coefficient \(\pm1/8\). It is therefore orthogonal in \(L^2\) to **every** polynomial of degree at most three in these signs; moreover
\[
\mathbb EZ_n=0,\qquad \operatorname{Var}(Z_n)=\frac3{64}\binom n4.
\]
The orthogonal projection of \(Q_n\) onto the entire vector space of edge-sign polynomials of degree at most three is precisely
\[
\widehat Q_n=\frac38\binom n4+\frac{n-3}{2}\left(T_n-\frac14\binom n3\right).
\]
In particular this is also the best affine least-squares predictor from \(T_n\). The complete finite-size moments are
\[
\begin{aligned}
\mathbb ET_n&=\tfrac14\binom n3,&\operatorname{Var}(T_n)&=\tfrac3{16}\binom n3,\\
\mathbb EQ_n&=\tfrac38\binom n4,&\operatorname{Var}(Q_n)&=\tfrac{3(4n-11)}{64}\binom n4,\\
\operatorname{Cov}(T_n,Q_n)&=\tfrac38\binom n4.
\end{aligned}
\]
Hence
\[
\operatorname{Corr}(T_n,Q_n)=\sqrt{\frac{4(n-3)}{4n-11}},\qquad
\frac{\mathbb E[(Q_n-\widehat Q_n)^2]}{\operatorname{Var}(Q_n)}=\frac1{4n-11}.
\]
The correlation tends to one; these two counts exhibit asymptotically perfect *linear correlation*, though no assertion is made about a joint limit law or conditional expectation given \(T_n\).

## Assumptions and scope

Only uniform, independent orientations are assumed; statements concern every integer \(n\ge4\). For unordered \(\{a,b\}\), \(a<b\), let \(X_{ab}=+1\) if \(a\to b\) and \(-1\) otherwise, and extend antisymmetrically by \(X_{ba}=-X_{ab}\). The \(\binom n2\) variables indexed by increasing pairs are independent symmetric signs. A directed four-cycle is counted once modulo cyclic rotation, irrespective of the starting vertex. All expectations, orthogonality statements and variances are under the uniform random tournament law.

## Proof

For a four-set \(S\), denote by \(t(S)\) its number of cyclic triples and by \(q(S)\) its number of directed four-cycles. The four possible isomorphism types have respectively \((t,q)=(0,0),(1,0),(1,0),(2,1)\). The familiar local profile-counting identity, which is **not** claimed as new, is
\[
q(S)=\frac12 t(S)-\frac12\mathbf1_{\{t(S)=1\}}.
\]
A finer edge-sign expansion supplies the stochastic orthogonality result. For each of the three undirected Hamiltonian cycles \(\gamma=(v_1,v_2,v_3,v_4)\) on \(S\), modulo reversal and rotation, put
\[
U_\gamma=\prod_{i=1}^4X_{v_i v_{i+1}},\quad v_5=v_1.
\]
This is independent of reversing or rotating \(\gamma\). The indicator that either direction of \(\gamma\) is consistently oriented is
\[
\frac18\left(1+\sum_{1\le i<j\le4}
X_{v_i v_{i+1}}X_{v_j v_{j+1}}+U_\gamma\right).
\]
Summing this identity over the three Hamiltonian cycles, all products from opposite disjoint cycle edges cancel. The remaining quadratic terms are precisely the nonconstant part of four times the cyclic-triangle count. Thus the exact *local Walsh decomposition* is
\[
q(S)=\frac12t(S)-\frac18+\frac18\sum_{\gamma\subset S}U_\gamma.
\]
The coefficient comparison is also certified exhaustively for all \(2^6\) orientations on four vertices in the accompanying verifier; the displayed product expansion itself proves the identity for every tournament. Summing over all four-sets, each triangle lies in \(n-3\) four-sets, so
\[
Q_n=\frac{n-3}{2}T_n-\frac18\binom n4+
\frac18\sum_{|S|=4}\sum_{\gamma\subset S}U_\gamma.
\]
The last double sum is \(8Z_n\). Distinct terms have distinct sets of four undirected edges (each set is a four-cycle on its own vertex set). Orthogonality of different Walsh characters gives \(\mathbb E Z_n=0\), \(\operatorname{Var}(Z_n)=3\binom n4/64\), and orthogonality to every polynomial of edge-sign degree at most three.

Each cyclic-triangle indicator has mean \(1/4\), variance \(3/16\), and is a pure constant-plus-quadratic Walsh polynomial. Distinct cyclic-triangle indicators are uncorrelated: disjoint edge sets give independence, and when they share one edge their conditional probabilities given that edge are both \(1/4\), with independent remaining edges. Therefore \(\operatorname{Var}(T_n)=3\binom n3/16\). The remaining formulas follow by orthogonality and \(\binom n3=4\binom n4/(n-3)\). Since the coefficient \((n-3)/2\) is positive and \(Z_n\) has positive variance, the least-squares and correlation statements hold without boundary exceptions for \(n\ge4\).

## Verification

Run `python3 verify_tournament.py` with Python 3. The script checks the local Walsh identity, exhaustively enumerates the \(64\) tournaments on four vertices and the \(1024\) tournaments on five vertices for their exact rational means, variances and covariances, and tests the deterministic decomposition on a further \(1000\) six-vertex orientations. These are finite checks; orthogonality and all-\(n\) identities are established by the displayed symbolic expansion and independence argument, not by enumeration.

## Relationship to prior work

Linial and Morgenstern, *On the number of 4-cycles in a tournament* (arXiv:1405.1576, originally posted 7 May 2014), Observation 1.2, already count cyclic triangles across four-vertex types and derive the corresponding deterministic relation. That relation is background, not the originality claim. Chan, Grzesik, Král' and Noel (arXiv:1902.00572) analyze extremal three-cycle/four-cycle densities, not this finite-sample orthogonal regression. Andersson's *On the asymptotic distributions of subgraph counts in a random tournament* (1998) concerns general subgraph-count asymptotics, while *Small variance of subgraph counts in a random tournament* (2000) identifies exceptional variance orders. The novel aspect assessed here is the explicit degree-four Walsh remainder and its universal low-degree orthogonality, sharp finite-size optimal linear predictor and unexplained-variance fraction. These results may nevertheless be implicit in general orthogonal-decomposition frameworks; historical priority has not been independently established.

## Limitations

The result does not determine \(\mathbb E[Q_n\mid T_n]\), show independence of the residual from triangle counts, or prove any limit theorem. The general stochastic decomposition applies only to uniformly and independently oriented tournaments. Complete full texts of Andersson's 1998 and 2000 papers were unavailable during literature comparison; their potential implicit or explicit coverage remains a substantive originality risk. An independent scientific review has not been performed.

## References

1. N. Linial and A. Morgenstern, *On the number of 4-cycles in a tournament*, arXiv:1405.1576 (first public preprint 7 May 2014), Observation 1.2.
2. T. F. N. Chan, A. Grzesik, D. Král' and J. A. Noel, *Cycles of length three and four in tournaments*, arXiv:1902.00572 (2019).
3. P. Andersson, *On the asymptotic distributions of subgraph counts in a random tournament*, Random Structures & Algorithms 13 (1998), 249–260, DOI: 10.1002/(SICI)1098-2418(199810/12)13:3/4<249::AID-RSA4>3.0.CO;2-V.
4. P. Andersson, *Small variance of subgraph counts in a random tournament*, Statistics & Probability Letters 49 (2000), 135–138, DOI: 10.1016/S0167-7152(00)00041-9.

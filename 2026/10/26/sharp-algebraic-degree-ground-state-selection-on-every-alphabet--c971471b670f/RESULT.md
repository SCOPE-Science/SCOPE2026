# Sharp algebraic-degree ground-state selection on every alphabet of size at least three

## Finding

**Theorem.** For every integer \(N\ge3\), there is an explicit topologically mixing \(N\)-symbol one-sided shift of finite type and a nearest-neighbor potential taking only the values \(0\) and \(-1\) with precisely \(N\) fixed-point maximizing measures, such that the zero-temperature equilibrium measure gives a one-symbol cylinder an algebraic probability of **degree exactly \(N\)** over \(\mathbb Q\). This realizes the full upper bound for one-symbol cylinders in the degree theorem of Jenkinson and Pollicott (2026), even within the fixed-ground-state, two-energy class.

Write \(\rho=\rho_N\) for the unique positive root of \(t^N-t-1=0\). The limiting fixed-state masses are
\[
 p_i=\begin{cases}
 \dfrac{\rho+1}{(N-1)\rho+N},&0\le i\le N-2,\\[4pt]
 \dfrac{1}{(N-1)\rho+N},&i=N-1.
 \end{cases}
\]
In fact these are the stationary single-site masses at **every finite inverse temperature**, not only in the zero-temperature limit. The temperature-dependent chain is an exact lazy version of a fixed non-lazy Markov chain; its rare-jump scaling limit is an explicit stationary continuous-time Markov process.

## Assumptions and scope

Fix \(N\ge3\). Let \(K\) be the \(N\times N\) zero-one matrix whose directed edges are
\[
 i\to i+1\quad(0\le i\le N-2),\qquad N-1\to0,\qquad N-2\to0.
\]
The final edge is a distinct shortcut because \(N\ge3\). Put \(A=I+K\), and let \(X_A\) be the one-sided edge-admissible vertex shift on \(\{0,\ldots,N-1\}^{\mathbb N_0}\). Define \(f(x)=0\) when \(x_0=x_1\), and \(f(x)=-1\) otherwise. All allowed self-edges and only those self-edges have potential zero. For \(\beta\ge0\), let \(\mu_\beta\) be the unique equilibrium measure for \(\beta f\), with no normalization ambiguity: \(\mu_\beta\) is a probability measure and the pressure is \(\log\lambda_\beta\).

The matrix \(A\) is primitive: \(K\) is strongly connected and all vertices of \(A\) possess loops. All maximizing measures of \(f\) are exactly the mixtures of the \(N\) fixed-point Dirac measures \(\delta_{i^\infty}\). In particular this is a singular zero-temperature selection problem, not a constant-potential example.

## Proof

**1. Exact Perron polynomial.** The graph of \(K\) has exactly two simple directed cycles: one of length \(N\) and one of length \(N-1\); they overlap and therefore cannot occur simultaneously in any vertex-disjoint cycle cover. The determinant expansion gives
\[
 \det(I-zK)=1-z^{N-1}-z^N,
 \qquad \det(tI-K)=t^N-t-1.
\]
The graph has cycles of coprime lengths and is strongly connected, hence \(K\) is primitive. Its Perron root is the unique real root \(\rho>1\) of \(\rho^N=\rho+1\). Explicit positive right and left eigenvectors are
\[
 r=(1,\rho,\ldots,\rho^{N-2},\rho^{-1})^{\mathsf T},
 \qquad \ell=(1,\rho^{-1},\ldots,\rho^{-(N-1)})^{\mathsf T}.
\]
Indeed, each row and column eigenvalue equation follows from the chain edges, except at the shortcut and at vertex zero, where the remaining identity is exactly \(\rho^N=\rho+1\).

**2. The entire equilibrium family.** The weighted transfer matrix of \(\beta f\) is
\[
 B_\beta=I+qK,\qquad q=e^{-\beta},\qquad
 \lambda_\beta=1+q\rho.
\]
Its positive Perron eigenvectors are the above \(r,\ell\), independent of \(\beta\). The standard Perron–Frobenius equilibrium construction therefore gives the stationary vertex masses \(p_i=\ell_i r_i/(\ell^{\mathsf T}r)\). Since \(\ell_i r_i=1\) for \(i\le N-2\), and \(\ell_{N-1}r_{N-1}=\rho^{-N}=1/(\rho+1)\), the advertised formulas follow. These masses sum to one. The Markov transition law is
\[
 P_\beta(i,j)=\frac{B_\beta(i,j)r_j}{\lambda_\beta r_i}
 =(1-a_\beta)I(i,j)+a_\beta Q(i,j),
\]
where
\[
 a_\beta=\frac{q\rho}{1+q\rho},\qquad
 Q(i,j)=\frac{K(i,j)r_j}{\rho r_i}.
\]
The matrix \(Q\) is stochastic, with zero diagonal and stationary vector \(p\); hence \(\mu_\beta\) has the stationary distribution \(p\) for every \(\beta\).

**3. Zero-temperature limit and degree.** For every fixed positive word length, any cylinder containing a nonself transition has \(\mu_\beta\)-mass at most its number of transitions times \(a_\beta\), tending to zero. A constant-word cylinder \([i^k]\) has mass \(p_i(1-a_\beta)^{k-1}\to p_i\). Cylinders determine weak convergence, so
\[
 \mu_\beta\xrightarrow[\beta\to\infty]{w^*}
 \sum_{i=0}^{N-1}p_i\delta_{i^\infty}.
\]
Write \(u=p_{N-1}=1/((N-1)\rho+N)\). The rational inverse \(\rho=(u^{-1}-N)/(N-1)\) implies \(\mathbb Q(u)=\mathbb Q(\rho)\). By Selmer's irreducibility theorem, \(t^N-t-1\) is irreducible over \(\mathbb Q\) for **every** \(N\ge2\), hence \([\mathbb Q(u):\mathbb Q]=N\). In the cited degree bound, nearest-neighbor \(f\) has range \(2\), the length-one cylinders are exactly the \(N\) one-symbol cylinders, and therefore this attains the bound at its stated alphabet-size parameter.

**4. Exact rare-jump scaling.** Let \(X^{(\beta)}\) be the stationary finite-state Markov chain with transition matrix \(P_\beta\). Then
\[
 e^\beta(P_\beta-I)\longrightarrow G=\rho(Q-I)
 \qquad (\beta\to\infty).
\]
Consequently, for every real \(s\ge0\),
\[
 P_\beta^{\lfloor s e^\beta\rfloor}
 \longrightarrow e^{sG}
\]
by the finite-dimensional matrix exponential limit. Joint finite-dimensional distributions at finitely many rescaled times therefore converge to those of the continuous-time chain generated by \(G\), started in the same stationary vector \(p\). At finite \(\beta\), each jump-clock success probability is exactly \(a_\beta\). The limit generator has exit rate \(\rho\) from every vertex and post-jump transition law \(Q\).

## Verification

The supplied standalone Python checker `verify.py` computes \(K\), its eigenvectors, and finite-temperature Markov laws without additional packages. It performed exact Bareiss-determinant samples for \(3\le N\le11\) and numerical Perron, normalization, stationarity and jump checks for \(3\le N\le60\), reporting `VERIFY_OK`. The infinite family, degree, and weak-limit claims are established by the argument above, not by finite samples. In particular, the only non-elementary number-theoretic input is Selmer's established irreducibility theorem, cited below.

## Relationship to prior work

Jenkinson–Pollicott (2026, Corollary in Section 3) prove the algebraic-degree upper bound \(N\) for length-at-most-two cylinders in an \(N\)-symbol mixing subshift under a two-symbol potential; that bound is not asserted there to be attained with all ground states fixed. Chazottes–Gambaudo–Ugalde (2011, Section 6.2) produce an explicit irrational four-state zero-temperature barycenter via a different weighted graph and a general renormalization procedure. Garibaldi–Thieullen (2012, Sections 6.1–6.3) work out detailed low-dimensional Puiseux selection patterns. These methods explain the mechanism for algebraic selection but do not supply the explicit uniform all-\(N\) fixed-ground-state family or the exact rare-jump law exhibited above. Selmer's classical theorem supplies the degree obstruction.

## Limitations

The construction uses an explicitly restricted adjacency graph, not the full \(N\)-shift, and covers only \(N\ge3\). The polynomial-degree equality concerns one-symbol cylinders under a nearest-neighbor potential; it is not a lower bound for higher-range presentations on fewer symbols. No claim is made that every algebraic number of degree \(N\) is realizable, nor that this construction is unique. The Markov-process limit is finite-dimensional (not an asserted path-space topology theorem). General earlier renormalization frameworks subsume the Perron-selection calculation in principle, so historical priority for an equivalent explicit all-size family remains an open bibliographic risk.

## References

- O. Jenkinson and M. Pollicott, *An elementary proof of Brémont's theorem on the convergence of equilibrium measures at temperature zero*, arXiv:2610.19990v1 (first publicly posted 2026-10-14), especially Corollary in Section 3. https://arxiv.org/html/2610.19990v1
- J.-R. Chazottes, J.-M. Gambaudo and E. Ugalde, *Zero-temperature limit of one-dimensional Gibbs states via renormalization: the case of locally constant potentials*, *Ergodic Theory Dynam. Systems* **31** (2011), 1109–1161, Section 6.2; https://arxiv.org/pdf/0903.1212
- E. Garibaldi and P. Thieullen, *Description of Some Ground States by Puiseux Techniques*, *Journal of Statistical Physics* **146** (2012), 125–180, Sections 6.1–6.3; https://www.math.u-bordeaux.fr/~pthieull/Recherche/Publications/Garibaldi_Thieullen2012_01.pdf
- E. S. Selmer, *On the irreducibility of certain trinomials*, *Mathematica Scandinavica* **4** (1956), 287–302. An accessible standalone proof is K. Conrad, *Irreducibility of \(t^N-t-1\)*; https://kconrad.math.uconn.edu/blurbs/ringtheory/irredselmerpoly.pdf

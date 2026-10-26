# Poisson bridge adsorption and parity-dependent jamming in two coupled cliques

## Finding
Let \(n\ge2\) and let \(G_n\) consist of two copies \(A=\{A_1,\ldots,A_n\}\) and \(B=\{B_1,\ldots,B_n\}\) of the complete graph \(K_n\), together with the \(n\) paired edges \(A_iB_i\). Each internal edge attempts irreversible hard-core dimer deposition as a rate-one Poisson process; each paired edge attempts at a fixed rate \(\lambda\ge0\). A deposition succeeds exactly when both endpoints are vacant. Let \(M_{n,\lambda}\) count successful depositions across the paired edges, and \(U_{n,\lambda}\) count vacant vertices at jamming.

For every fixed \(\lambda\ge0\), as \(n\to\infty\),
\[
 M_{n,\lambda}\ \Longrightarrow\ \operatorname{Poisson}(\lambda).
\]
For **every finite** \(n\) and \(\lambda\ge0\), the terminal defect is exactly
\[
 U_{n,\lambda}=2\,\mathbf1_{\{M_{n,\lambda}\not\equiv n\pmod2\}}.
\]
In particular, along either fixed parity of \(n\),
\[
 \Pr(U_{n,\lambda}=2)
 =\frac{1-(-1)^n e^{-2\lambda}}2+o(1),\qquad
 \mathbb E U_{n,\lambda}=1-(-1)^n e^{-2\lambda}+o(1).
\]
The two limiting defect probabilities differ by \(e^{-2\lambda}\). This is an order-one jamming effect although the paired edges are only a vanishing fraction of the possible bonds. When \(\lambda=0\), the statements hold with a degenerate zero Poisson variable.

## Assumptions and scope
The graph is fixed for each \(n\) and has unit-rate attempts on all \(n(n-1)\) intra-clique edges and rate \(\lambda\) on the \(n\) paired cross-edges. Attempts on distinct edges are independent. Successful dimers persist forever and block their endpoints; rejected attempts change nothing. The parameter \(\lambda\) stays fixed with \(n\); no assertion is made for \(\lambda=\lambda_n\) diverging with \(n\). A Poisson-process construction is equivalent to uniform exponential first-priority clocks on edges, because an edge cannot become newly available after either endpoint has been occupied.

## Proof
**1. Exact Markov state and parity.** Write \(a\) and \(b\) for the numbers of vacant sites in the respective cliques, and \(c\) for the number of labels \(i\) for which both \(A_i\) and \(B_i\) are vacant. Initially \((a,b,c)=(n,n,n)\). The rates of successful internal depositions in the two classes are respectively \(\binom a2\) and \(\binom b2\), while the rate of cross-depositions is \(\lambda c\). Under an internal deposition in the first class, \(a\) decreases by two and \(c\) decreases by a hypergeometric random variable \(X\) with \(\mathbb EX=2c/a\); the second class has the symmetric transition. Each cross-deposition changes \((a,b,c)\) to \((a-1,b-1,c-1)\).

Because a complete graph can never finish with more than one vacant vertex, at jamming \(a,b\in\{0,1\}\). Both parities equal the parity of \(n-M_{n,\lambda}\): internal dimers remove two sites on one side and cross-dimers remove one site on each side. Therefore the only terminal possibilities are \((a,b)=(0,0)\) and \((1,1)\). In the first case \(U=0\), in the second \(U=2\); this proves the finite identity, including \(\lambda=0\).

**2. Finite scaled-time fluid law.** Let \(t\) denote physical time and \(u=nt\). Let \(x_n(u)=a(u/n)/n\), \(y_n(u)=b(u/n)/n\), and \(z_n(u)=c(u/n)/n\). Their predictable drifts per unit \(u\) are exactly
\[
 \dot x_n=-x_n^2+\frac{x_n-\lambda z_n}{n},\qquad
 \dot y_n=-y_n^2+\frac{y_n-\lambda z_n}{n},\qquad
 \dot z_n=-z_n(x_n+y_n)+\frac{(2-\lambda)z_n}{n},
\]
where the displayed dots describe compensator densities, not pathwise derivatives of the jump processes. Each jump has size at most \(2/n\); on every bounded \(u\)-interval the predictable quadratic variations of the martingale parts are \(O_{\lambda}(1/n)\). The martingale maximal inequality and Gronwall's inequality therefore give uniform-in-probability convergence on every \([0,T]\) to the solution of
\[
 x'=-x^2,\quad y'=-y^2,\quad z'=-(x+y)z,
 \quad x(0)=y(0)=z(0)=1.
\]
The unique solution is
\[
 x(u)=y(u)=(1+u)^{-1},\qquad z(u)=(1+u)^{-2}.
\]

**3. Cross-count Poisson law on bounded time intervals.** In scaled time the cross-counting process has predictable intensity \(\lambda z_n(u)\). By the standard independent-channel Poisson time-change construction one can write its count through time \(T\) as \(Y(\Lambda_n(T))\), where \(Y\) is a unit-rate Poisson process and
\[
 \Lambda_n(T)=\lambda\int_0^T z_n(u)\,du
 \xrightarrow{\Pr}\lambda\int_0^T(1+u)^{-2}\,du
 =\frac{\lambda T}{1+T}.
\]
Since a Poisson process has no jump at a prespecified deterministic time almost surely, the continuous-mapping argument yields \(M_{n,\lambda}(T/n)\Rightarrow\operatorname{Poisson}(\lambda T/(1+T))\) for each fixed \(T\).

**4. Uniform late-event control.** Define the nonnegative function
\[
 \Phi(a,b,c)=\begin{cases}c/a+c/b,&a,b\ge1,\\0,&c=0.\end{cases}
\]
States with \(c>0\) necessarily have \(a,b\ge1\). Under an internal deposition in the first class with \(a>2\), the expected new value of \(c/a\) equals its previous value, whereas \(c/b\) decreases in expectation by \(2c/(ab)\). For \(a=2\), the new \(c\) is zero and the change is more negative. Thus the first-class internal contribution to the generator is at most \(-c(a-1)/b\), and similarly the second-class contribution is at most \(-c(b-1)/a\), provided \(a,b\ge2\). Their sum is at most \(-c\), since
\[
 \frac{a-1}{b}+\frac{b-1}{a}\ge1\quad(a,b\ge2).
\]
For \(a=1<b\), the remaining internal-class contribution is at most \(-c\) (including \(b=2\)), with the symmetric statement when \(b=1<a\). A cross-deposition never increases \(\Phi\), because \((c-1)/(a-1)\le c/a\) whenever the denominators exist, and similarly for \(b\). If \(a=b=1,c=1\), only a cross-deposition is possible and the generator satisfies \(\mathcal L\Phi=-2\lambda\).

Consequently, setting \(K_\lambda=\max\{1,\lambda\}\), the exact finite-state generator inequality holds in every state:
\[
 \mathcal L(K_\lambda\Phi)\le-\lambda c.
\]
Dynkin's formula up to jamming (or its monotone bounded stopping-time approximation) gives for every state
\[
 \mathbb E(\text{number of future successful cross-depositions}\mid a,b,c)
 \le K_\lambda\Phi(a,b,c).
\]
For any fixed \(T\), the fluid law and boundedness \(0\le\Phi\le2\) imply
\[
 \limsup_{n\to\infty}\Pr\{\text{a cross-deposition occurs after time }T/n\}
 \le\frac{2K_\lambda}{1+T}.
\]
Letting \(T\to\infty\) proves that the full terminal cross-count converges to \(\operatorname{Poisson}(\lambda)\); in the case \(\lambda=0\) this is immediate without the inequality.

**5. Jammed-state law.** The exact parity identity in Step 1 and convergence of the terminal cross-count give \(\mathbb E[(-1)^{M_{n,\lambda}}]\to\exp(-2\lambda)\), since parity is a bounded function on the discrete nonnegative integers. Substituting into \(\Pr(U_{n,\lambda}=2)=[1-(-1)^n\mathbb E(-1)^{M_{n,\lambda}}]/2\) completes the proof.

## Verification
Run `python verify.py` using Python 3.9 or later; no third-party dependencies are needed. The script computes the exact cross-count probability polynomial in two independent ways: a hypergeometric three-count Markov recurrence and a direct enumeration of the original labeled vacant subsets. It compares both constructions for \(n=2,3,4,5\) and \(\lambda\in\{1/3,1,3\}\), checks the generator inequality exhaustively on all count triples with \(1\le a,b\le11\), and computes larger finite examples. Its execution returned `PASS 1923 exact transition, full-graph comparison, and Lyapunov assertions`. This is corroboration only; the proof above handles all sizes and every fixed \(\lambda\ge0\).

## Relationship to prior work
Irreversible dimer parking and random greedy matchings are classical. Dyer and Frieze analyze randomized greedy matching on general fixed graphs, with their abstract emphasizing forests; that accessible material does not state the present two-clique Poisson bridge limit. The full article was not accessible for a decisive exhaustive comparison. Gerin's Page–Rényi parking study is an accessible full-text treatment of pair adsorption on a path, with a limiting *coverage density* rather than the order-one parity defect of two coupled cliques. Dhara, van Leeuwaarden and Mukherjee analyze greedy *vertex*-occupancy processes on Erdős–Rényi graphs, not edge-dimer adsorption on this deterministic dense two-community geometry. Prior adsorption on narrow ladders refers to a fixed-width lattice geometry, not the increasing clique degree here. These distinctions concern theorem implications, not merely titles. A general random-greedy-matching theorem with stronger hypotheses could subsume the claim; no exhaustive priority assertion is made.

## Limitations
The result fixes the inter-clique rate \(\lambda\) while \(n\to\infty\) and assumes two equally sized complete communities, exactly one paired bridge at each label, and irreversible independent Poisson attempts. It does not give a quantitative convergence rate, a time-to-jamming law, a limit when \(\lambda\) grows with \(n\), or a claim for arbitrary inter-community graphs. The random matching in the theorem is the edge-priority greedy matching, not a procedure selecting a random unmatched vertex first. Mathematical correctness does not establish exhaustive historical originality; the relevant inaccessible source remains a priority risk.

## References
1. M. E. Dyer and A. M. Frieze, *Randomized greedy matching*, Random Structures & Algorithms 2 (1991), 29–46. DOI: 10.1002/rsa.3240020104. Abstract and bibliographic record inspected; full text was not available.
2. L. Gerin, *The Page–Rényi parking process*, Electronic Journal of Combinatorics 22(4) (2015), P4.4. arXiv:1411.8002 (first version November 28, 2014); DOI: 10.37236/5150. Full open-access journal PDF inspected.
3. S. Dhara, J. S. H. van Leeuwaarden and D. Mukherjee, *Generalized random sequential adsorption on Erdős–Rényi random graphs*, Journal of Statistical Physics 164 (2016), 1217–1232. DOI: 10.1007/s10955-016-1583-z. Open-access HTML text inspected.
4. J. W. Evans and R. S. Nord, *Random and cooperative sequential adsorption on infinite ladders and strips*, Journal of Statistical Physics 69 (1992), 151–162. DOI: 10.1007/BF01053787. Abstract record inspected; full text not available.

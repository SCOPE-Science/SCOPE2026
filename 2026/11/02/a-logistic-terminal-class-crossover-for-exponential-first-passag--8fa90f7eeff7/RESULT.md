# A logistic terminal-class crossover for exponential first-passage infection on near-balanced bicliques

## Finding
Let \(G_n=K_{a_n,n}\) where
\[
a_n=n+\left\lfloor\frac{\lambda n}{\log n}\right\rfloor,
\qquad \lambda\in\mathbb R\text{ is fixed},
\]
and \(n\to\infty\) through integers for which \(a_n\ge2\). Give every edge an independent rate-one exponential passage time and explore shortest-weight paths outward from one fixed root in the part \(A_n\) of size \(a_n\). Equivalently, infect the root and let each edge with one infected and one susceptible endpoint transmit independently at rate one, with no recovery.

Write \(L_n\in\{A,B\}\) for the class of the **last newly infected vertex**. Then
\[
\boxed{\lim_{n\to\infty}\Pr(L_n=A)=\frac{e^\lambda}{1+e^\lambda}.}
\]
Thus the competition between terminal classes has a nondegenerate window of part-size imbalance \(n/\log n\). Moreover, for every integer \(n\ge2\), the exactly balanced graph has the **finite-sample identity**
\[
\boxed{\Pr(L_n=A\mid G_n=K_{n,n})=\tfrac12.}
\]
This theorem concerns the class of the last infection, not the law of the entire flooding time.

## Assumptions and scope
A graph \(K_{a,b}\) has two parts of sizes \(a,b\) and every cross-edge present, no within-part edges. Each edge independently carries an \(\operatorname{Exp}(1)\) passage time; shortest-weight paths from the prescribed root give infection times. By the exponential memoryless property, the exploration process has transitions from \(i\) infected vertices in \(A\) and \(j\) in \(B\) at rates
\[
r_A(i,j)=(a-i)j,\qquad r_B(i,j)=(b-j)i.
\]
There are no ties almost surely. All probability statements include both random edge weights and the induced exploration. The root is in \(A\), so the initial state is \((1,0)\). The result allows positive or negative fixed \(\lambda\), and specifies no claim uniform in \(\lambda\).

## Proof
**1. Independent exposure thresholds.** Independently sample \(a-1\) rate-one exponential random variables \(E_{A,v}\) for the nonroot vertices of \(A\), and \(b\) such variables \(E_{B,w}\) for vertices of \(B\). Let \(I_A(t),I_B(t)\) be the infected counts and put
\[
H_A(t)=\int_0^t I_B(s)\,ds,\qquad H_B(t)=\int_0^t I_A(s)\,ds.
\]
The infection status of a nonroot \(A\)-vertex at \(t\) is \(\mathbf1\{E_{A,v}\le H_A(t)\}\), and similarly the status of a \(B\)-vertex is \(\mathbf1\{E_{B,w}\le H_B(t)\}\). This is the standard random-time-change realization: conditional on current states, each uninfected vertex in \(A\) has hazard \(I_B\) and each in \(B\) hazard \(I_A\). These hazards give exactly the transition rates displayed above, so the representation has the required law.

Denote the two independent threshold maxima by \(M_A\) and \(M_B\), and the class completion times by \(t_A,t_B\). Then \(H_A(t_A)=M_A\) and \(H_B(t_B)=M_B\). The classical exponential extreme-value identity gives jointly
\[
(M_A-\log n,M_B-\log n)\ \Longrightarrow\ (G_A,G_B),
\]
where \(G_A,G_B\) are independent standard Gumbel variables with distribution function \(\exp(-e^{-x})\). Here \(a_n/n\to1\), so both maximum sample sizes are asymptotic to \(n\).

**2. A uniform finite-population bound.** Define \(a=a_n,b=n\), \(N=a+n\), and let \(T_n=\max(t_A,t_B)\). At state \((i,j)\), total infection rate is
\[
R(i,j)=i(n-j)+j(a-i)=ni+aj-2ij.
\]
If \(k=i+j\le N/2\), the inequality \(2ij\le k^2/2\), together with \(a/n\to1\), yields \(R(i,j)\ge(n/4)k\) for all sufficiently large \(n\). If \(k\ge N/2\), the same reasoning applies to the \(N-k\) susceptible vertices by interchanging infected and susceptible counts. Thus
\[
R(i,j)\ge\frac n4\min(k,N-k)
\]
uniformly over nonabsorbing states, for all sufficiently large \(n\). Summing conditional mean holding times over successive total infected counts gives
\[
\mathbb ET_n\le\frac4n\sum_{k=1}^{N-1}\frac1{\min(k,N-k)}=O\left(\frac{\log n}{n}\right).
\]
Consequently \(T_n=O_{\mathbb P}(\log n/n)\).

For the threshold samples, let \(F_A(h)\) and \(F_B(h)\) count sample values not exceeding \(h\). The uniform empirical-distribution inequality for independent exponential samples gives
\[
\sup_{h\ge0}|F_A(h)-(a-1)(1-e^{-h})|
+\sup_{h\ge0}|F_B(h)-n(1-e^{-h})|
=O_{\mathbb P}(\sqrt{n\log n})=:\eta_n.
\]
It follows, *simultaneously for all random times* \(t\), that
\[
I_A(t)=a(1-e^{-H_A(t)})+O_{\mathbb P}(\eta_n+1),\qquad
I_B(t)=n(1-e^{-H_B(t)})+O_{\mathbb P}(\eta_n).
\]
The \(O_{\mathbb P}\) terms here are uniform absolute error bounds, not timewise independent errors.

**3. Early exposure equality.** Set \(\delta(t)=H_B(t)-H_A(t)\). The previous estimates imply
\[
\delta'(t)=(a-n)(1-e^{-H_A(t)})
+n(e^{-H_B(t)}-e^{-H_A(t)})+e_n(t),\quad
\sup_t|e_n(t)|=O_{\mathbb P}(\eta_n+1).
\]
The second term has sign opposite to \(\delta\). Taking the upper Dini derivative of \(|\delta|\) and using \(H_B'=I_A\) therefore gives, uniformly for \(0\le t\le T_n\),
\[
|\delta(t)|\le\frac{|a-n|}{a}H_B(t)
+O_{\mathbb P}((\eta_n+1)t).
\]
Let \(h_n=\log\log n\) and \(\tau_n=\inf\{t:H_B(t)=h_n\}\). Since \(M_B=\log n+O_{\mathbb P}(1)\), this time occurs before \(t_B\) with probability tending to one. Also \(\tau_n\le T_n=O_{\mathbb P}(\log n/n)\). Since \(|a-n|/a=O(1/\log n)\), the bound proves
\[
\delta(\tau_n)=o_{\mathbb P}(1),\qquad
H_A(\tau_n)=h_n+o_{\mathbb P}(1).
\]
Hence both part populations have \((1+o_{\mathbb P}(1))n/\log n\) susceptible vertices at \(\tau_n\), by the uniform empirical estimate. In particular, throughout \([\tau_n,T_n]\), the infected counts satisfy \(I_A(t)/a=1-o_{\mathbb P}(1)\) and \(I_B(t)/n=1-o_{\mathbb P}(1)\) uniformly.

**4. The terminal exposure difference.** By definition \(H_B(t_B)=M_B=\log n+O_{\mathbb P}(1)\). Integrating \(H_B'=I_A\) over \([\tau_n,t_B]\) yields
\[
t_B-\tau_n=\frac{\log n}{n}(1+o_{\mathbb P}(1)).
\]
Write \(S_A=a-I_A\), \(S_B=n-I_B\). Because after \(\tau_n\) the two exposure rates are bounded below by \(n(1-o_{\mathbb P}(1))\), the uniform exponential empirical envelopes from step 2 give
\[
\int_{\tau_n}^{t_B}(S_A(t)+S_B(t))\,dt
=O_{\mathbb P}(1/\log n)+O_{\mathbb P}(\eta_nT_n)=o_{\mathbb P}(1).
\]
The exact identity \(\delta'=I_A-I_B=(a-n)-S_A+S_B\) now gives
\[
\delta(t_B)=\delta(\tau_n)+(a-n)(t_B-\tau_n)+o_{\mathbb P}(1)
\xrightarrow{\mathbb P}\lambda.
\]
This exposure-difference limit is the structural ingredient determining the transition window.

**5. Identify the last class.** At the instant \(t_B\) when the last \(B\)-vertex is infected, the \(A\)-class remains incomplete exactly when \(M_A>H_A(t_B)=M_B-\delta(t_B)\). Thus
\[
\Pr(L_n=A)=\Pr\{M_A-M_B+\delta(t_B)>0\}
\longrightarrow\Pr\{G_A-G_B+\lambda>0\}
=\frac{e^\lambda}{1+e^\lambda}.
\]
The final equality is the standard logistic difference-of-independent-Gumbels calculation; continuity avoids any boundary mass issue.

**6. Exact balance.** If \(a=b=n\ge2\), the first infection must be in \(B\), producing the state \((1,1)\). Thereafter the transition rates \((n-i)j\) and \((n-j)i\) are exchanged by swapping the parts, while the state \((1,1)\) is invariant. Therefore the probabilities that the final infection lies in either class are exactly equal, proving the finite identity.

## Verification
The standalone `checker.py` performs exact-rational forward propagation and independent backward recursion on the infected-count state grid for \(2\le a,b\le9\), checks the balanced finite identity through \(n=20\), and checks positivity of all reachable nonterminal total rates through sizes ten. It passed 3,468 exact assertions. A separately seeded stochastic diagnostic is provided but is **not** used as proof of any asymptotic statement. Run `python3 checker.py` in a directory containing the standalone file. The analytic argument above establishes the infinite limit; small graph enumeration does not.

## Relationship to prior work
Van der Hofstad and Lodewijks (first public preprint November 27, 2023) give leading typical-distance, flooding-time and diameter scales for long-range exponential first-passage percolation on complete graphs. Their stated main theorem treats a torus-embedded complete graph, rather than the marked last-infection class on near-balanced complete bipartite graphs. Ottino-Löffler, Scott and Strogatz (2017) analyze takeover times for a different discrete-time vertex-selection infection mechanism and derive limiting time distributions for several families, but not this class-marked exponential-edge transition. Kolossváry and Komjáthy (2012/2015) treat typical weighted paths and hopcounts of inhomogeneous random graphs. Leskelä and Ngo (2018/2019) obtain sparse-random-graph flooding estimates, not the deterministic dense two-class terminal competition. These differences are in the stochastic law and statement, not merely nomenclature. Historical-priority research cannot exclude all older dense-network epidemic and extreme-value literature.

## Limitations
Only the final infected **part** is described. The theorem does not identify the centered total infection time, joint independent time fluctuations, or uniform behavior for drifting \(\lambda\). The exponential memoryless property, complete bipartite structure, one infected root and fixed \(\lambda\) are essential to the proof. The finite exact identity holds for balanced classes with \(n\ge2\), not for a single edge. The asymptotic theorem has undergone only the documented mathematical and computational checks, not independent validation.

## References
- R. van der Hofstad and B. Lodewijks, *Long-range first-passage percolation on the complete graph*, arXiv:2311.16088, first posted 2023-11-27, https://arxiv.org/abs/2311.16088.
- B. Ottino-Löffler, J. G. Scott and S. H. Strogatz, *Takeover times for a simple model of network infection*, arXiv:1702.00881, first posted 2017-02-03, https://arxiv.org/abs/1702.00881.
- I. Kolossváry and J. Komjáthy, *First Passage Percolation on Inhomogeneous Random Graphs*, arXiv:1201.3137, first posted 2012-01-15, https://arxiv.org/abs/1201.3137.
- L. Leskelä and H. Ngo, *First passage percolation in sparse random graphs with boundary weights*, arXiv:1806.09568, first posted 2018-06-25, https://arxiv.org/abs/1806.09568.
- M. J. Lee and D.-S. Lee, *Understanding the temporal pattern of spreading in heterogeneous networks: Theory of the mean infection time*, Phys. Rev. E 99, 032309 (2019), https://doi.org/10.1103/PhysRevE.99.032309.

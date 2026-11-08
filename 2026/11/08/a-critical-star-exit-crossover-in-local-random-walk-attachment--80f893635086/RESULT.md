# A critical star-exit crossover in local random-walk attachment

## Finding
Consider the one-edge-per-arrival random-walk attachment process specified below, initially a star with \(s\ge2\) leaves. At each arrival let a walk have length zero with probability \(q\in[0,1]\) and length one with probability \(1-q\), independently. Write \(\tau_{s,q}\) for the first arrival that destroys the star. Its **entire survival distribution**, for integers \(t\ge0\), is
\[
\Pr(\tau_{s,q}>t)=\prod_{j=s}^{s+t-1}\frac{(1-q)j+q}{j+1},
\]
where an empty product is one. In particular,
\[
\Pr(\tau_{s,0}>t)=\frac{s}{s+t},\qquad
\Pr(\tau_{s,1}>t)=\frac{s!}{(s+t)!}.
\]
Thus \(\tau_{s,q}<\infty\) almost surely for every \(q\in[0,1]\), but \(\mathbb E\tau_{s,0}=\infty\) whereas \(\mathbb E\tau_{s,q}<\infty\) for every \(q>0\). For each fixed \(s\ge2\),
\[
\lim_{q\downarrow0}\frac{\mathbb E\tau_{s,q}}{\log(1/q)}=s.
\]
For \(0<q<1\), setting \(\alpha=q/(1-q)\) gives the exact gamma-ratio formula
\[
\Pr(\tau_{s,q}>t)=(1-q)^t\frac{\Gamma(s+1)\Gamma(s+t+\alpha)}{\Gamma(s+\alpha)\Gamma(s+t+1)}.
\]
Consequently the fixed-\(s\), fixed-\(q\) tail has an exponential factor multiplied by a power of order \(t^{\alpha-1}\).

There is a sharp large-initial-star crossover: if \(s\to\infty\) along integers and \(s q_s\to\lambda\in[0,\infty)\), then
\[
\frac{\tau_{s,q_s}}s\ \xrightarrow{d}\ Z_\lambda,
\qquad \Pr(Z_\lambda>x)=\frac{e^{-\lambda x}}{1+x}\quad(x\ge0).
\]
If instead \(q_s\to0\) and \(s q_s\to\infty\), then \(q_s\tau_{s,q_s}\xrightarrow{d}\operatorname{Exp}(1)\). The family interpolates between a heavy-tailed law and exponentially tilted lifetimes at the precise perturbation scale \(q_s\asymp1/s\).

## Assumptions and scope
Let the initial simple undirected tree be the star \(K_{1,s}\) with \(s\ge2\). For each successive arrival, independently choose a starting vertex uniformly among the vertices currently present. Independently choose walk length zero with probability \(q\), one with probability \(1-q\); for length one, move from the chosen vertex to a uniformly selected neighbor. Connect exactly one new vertex to the walk endpoint, retaining all prior edges. There are no self-loops, vertex deletions, or multiple connections per arrival. The first-exit variable is \(\tau_{s,q}=\min\{t\ge1:G_t\text{ is not a star}\}\), where \(G_t\) is the graph after \(t\) arrivals. Independence and uniform-start sampling are essential. The limiting results hold under the stated parameters, with no uniformity claim beyond those regimes.

## Proof
**Step 1 (one-step survival).** While the graph remains a star with \(j\ge s\) leaves, it has \(j+1\) vertices. For a length-one walk, the endpoint is the center exactly when the starting vertex was one of its \(j\) leaves, an event of probability \(j/(j+1)\). For a zero-length walk, the endpoint is the center exactly when the start was the center, an event of probability \(1/(j+1)\). Adding the new vertex preserves the star if and only if the endpoint is its center. Thus the conditional survival probability is \(((1-q)j+q)/(j+1)\). A nonstar tree contains a path on four vertices, which remains present under all subsequent leaf attachments; hence a nonstar can never become a star. Multiplying the conditional probabilities for \(j=s,\ldots,s+t-1\) gives the exact product.

**Step 2 (moments and fixed-parameter tail).** For \(q=0\) the product telescopes to \(s/(s+t)\); for \(q=1\) it is \(s!/(s+t)!\). The tail-sum formula \(\mathbb E\tau=\sum_{t\ge0}\Pr(\tau>t)\) yields infinite mean at \(q=0\). More generally factor
\[
\Pr(\tau_{s,q}>t)=\frac{s}{s+t}\prod_{j=s}^{s+t-1}\left(1-q\left(1-\frac1j\right)\right).
\]
For \(0<q<1\), the product equals the stated gamma ratio by multiplying \((1-q)(j+\alpha)/(j+1)\). Standard gamma ratios give the fixed-parameter tail exponent. For \(0<q\le1\), since \(j\ge s\),
\[
\frac{s}{s+t}(1-q)^t\le\Pr(\tau_{s,q}>t)
\le\frac{s}{s+t}\left(1-q(1-1/s)\right)^t.
\]
(The left bound is zero for \(t>0\) if \(q=1\), which is harmless.) The upper bound is summable for \(q>0\). For fixed \(s\), the identity
\[
\sum_{t\ge0}\frac{a^t}{s+t}=a^{-s}\left[-\log(1-a)-\sum_{j=1}^{s-1}\frac{a^j}{j}\right],\quad 0<a<1,
\]
and the two bounds with \(a=1-q\) and \(a=1-q(1-1/s)\) prove \(\mathbb E\tau_{s,q}\sim s\log(1/q)\) as \(q\downarrow0\).

**Step 3 (critical scale).** Let \(t_s=\lfloor sx\rfloor\) for fixed \(x\ge0\) and suppose \(s q_s\to\lambda<\infty\). In the product factored above, \(s/(s+t_s)\to(1+x)^{-1}\). Since \(q_s=O(1/s)\), the logarithm of the second factor equals
\[
-q_s\sum_{j=s}^{s+t_s-1}(1-1/j)+O(t_s q_s^2)\longrightarrow-\lambda x.
\]
This gives the continuous survival function of \(Z_\lambda\) and weak convergence. When instead \(q_s\to0\) and \(s q_s\to\infty\), set \(t_s=\lfloor x/q_s\rfloor\). Now \(t_s/s\to0\), \(q_s t_s\to x\), \(t_s q_s^2\to0\), and \(q_s\sum_{j=s}^{s+t_s-1}1/j\le q_s t_s/s\to0\). The product therefore tends to \(e^{-x}\), proving the exponential limit. These steps cover all fixed \(x\ge0\); no asymptotic moment interchange is used.

## Verification
Run `python3 verify.py` using Python's standard library. The checker directly expands the two-stage attachment transitions for small labeled stars, retaining only graph-theoretically star-shaped outcomes, and compares the resulting exact rational survival probabilities with the product. It also checks rational survival bounds, telescoping boundary cases, and integral-alpha gamma-product identities. At the packaged run it passed 4694 exact assertions. Finite checking is supporting evidence; the unbounded statements follow from the proof above.

## Relationship to prior work
Saramäki and Kaski's 2004 random-walk network-growth model supplies the local attachment mechanism. Evans and Saramäki's 2004 preprint discusses random and walk-mediated attachment mixtures. Cannings and Jordan (2013), Theorem 2.1, prove that the leaf proportion tends to one for deterministic one-step walks; their proof explicitly excludes initial stars by observing that such an initial condition eventually exits the star class almost surely. Their subsequent section discusses mixtures of zero- and one-step walks. The present finding isolates the neglected *time to that first exit*, distinguishes almost-sure exit from finite mean exit, and proves its critical initial-size/noise crossover. It does not reassert their limiting leaf-proportion theorem. A general inhomogeneous-geometric hazard computation makes the exact product elementary once the star transition kernel is identified, and older implicit coverage cannot be fully excluded.

## Limitations
The result concerns only the first departure from a star, not the subsequent graph law, rates of eventual leaf-proportion convergence, arbitrary initial seeds, multiple attachments, or longer walks. Its sharp waiting-time behavior should not be extrapolated to those settings. Large-star weak limits do not assert convergence of expectations; the limiting heavy-tailed distribution itself has infinite mean at \(\lambda=0\). The literature comparison is not a proof of universal uniqueness or independent validation.

## References
1. J. Saramäki and K. Kaski, *Scale-Free Networks Generated By Random Walkers*, arXiv:cond-mat/0404088, first submitted 2004-04-05; https://arxiv.org/abs/cond-mat/0404088.
2. T. S. Evans and J. P. Saramäki, *Scale Free Networks from Self-Organisation*, arXiv:cond-mat/0411390, first submitted 2004-11-15; https://arxiv.org/abs/cond-mat/0411390.
3. C. Cannings and J. Jordan, *Random walk attachment graphs*, Electronic Communications in Probability 18 (2013), no. 77, DOI:10.1214/ECP.v18-2518; https://eprints.whiterose.ac.uk/id/eprint/116490/.

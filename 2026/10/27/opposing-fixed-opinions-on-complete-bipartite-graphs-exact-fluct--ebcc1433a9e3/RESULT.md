# Opposing fixed opinions on complete bipartite graphs: exact fluctuations and a beta-law limit

## Finding

Consider the linear continuous-time voter model on \(K_{m,n}\), with one permanently positive vertex in the part of size \(m\) and one permanently negative vertex in the part of size \(n\). Every other vertex independently copies a uniformly selected neighbor at rate one. In its unique stationary law let \(Y\) be the total number of positive vertices, including the fixed positive vertex. For all integers \(m,n\ge1\), writing \(N=m+n\),
\[
\mathbb EY=n,\qquad
\operatorname{Var}(Y)=\frac{(m-1)(n-1)N^2}{(N-1)(3N-4)}.
\]
At fixed \(N\ge4\), this fluctuation is maximized exactly by the most balanced unordered bipartition and minimized at the stars (where it vanishes). In particular, the stationary mean counts the *size of the part containing the negative zealot*, not the size of the positive-zealot part.

More strongly, for any sequence with \(m,n\to\infty\) and \(n/(m+n)\to\theta\in(0,1)\), the stationary proportions of positive *non-zealot* vertices in the two parts converge jointly in distribution to \((Z,Z)\), where
\[
Z\sim\operatorname{Beta}(2\theta,2(1-\theta)).
\]
Hence \(Y/N\Rightarrow Z\). At balanced growth \(\theta=1/2\), the macroscopic stationary positive proportion converges to the continuous uniform law on \([0,1]\), despite each opposing fixed opinion being represented by only one vertex. The limiting variance of \(Y/N\) is \(\theta(1-\theta)/3\); it does not vanish.

## Assumptions and scope

Both vertex classes are nonempty, all cross-edges are present, and no edges are present within either class. Opinions are binary, here coded \(0\) and \(1\). The two permanent opinions never change. Independently at each free vertex, a rate-one Poisson clock triggers replacement of its current opinion by that of a uniformly selected neighbor. All statements concern the stationary distribution; they do not impose an initial-state distribution. For the joint limit, both part sizes diverge and their ratio has the stated nondegenerate limit.

For finite parameters write \(i\in\{0,\ldots,m-1\}\) for the number of positive free vertices in the first part, \(j\in\{0,\ldots,n-1\}\) for the number in the second. The observable is \(Y=1+i+j\). If one part has only its zealot, the process has a unique absorbing configuration and the displayed formulas remain valid.

## Proof

**1. Exact lumped generator and stationarity.** For \(m,n\ge2\), the pair \((i,j)\) is a finite Markov chain with respective upward and downward transition rates
\[
\begin{aligned}
q_{(i,j),(i+1,j)}&=(m-1-i)j/n, & q_{(i,j),(i-1,j)}&=i(n-j)/n,\\
q_{(i,j),(i,j+1)}&=(n-1-j)(i+1)/m, & q_{(i,j),(i,j-1)}&=j(m-1-i)/m.
\end{aligned}
\]
Out-of-range moves have rate zero. This chain is irreducible: the permanent positive neighbor can produce positive free vertices in the second part, which can seed positives in the first; the permanent negative neighbor can produce negatives in the first, which can seed negatives in the second. Thus every configuration communicates with every other through a sequence of moves with positive rates. It has a unique invariant probability, independent of the initial state. For \(m=1\) or \(n=1\) all free voters eventually copy the sole opposite-class fixed vertex and stationarity is uniquely absorbing.

**2. First moments.** By permutations of free vertices within each class, a generic free vertex has stationary positivity probabilities \(p_A\) and \(p_B\). Its conditional drift yields
\[
p_A=\frac{n-1}{n}p_B,\qquad p_B=\frac{1+(m-1)p_A}{m}.
\]
Consequently
\[
p_A=\frac{n-1}{N-1},\quad p_B=\frac n{N-1},\qquad
\mathbb EY=1+(m-1)p_A+(n-1)p_B=n.
\]

**3. Pair correlations and the exact variance.** For \(m\ge3\), let \(a\) be the stationary product of two distinct free first-class binary opinions; for \(n\ge3\), let \(b\) be the analogous second-class product. For all \(m,n\ge2\), let \(c\) be the product of a free cross-class pair. Applying the generator gives the following relations, with equations defining \(a\) or \(b\) and terms involving them omitted when the corresponding free class has size one:
\[
a=\frac{n-1}{n}c,\qquad
b=\frac{p_B+(m-1)c}{m},\qquad
2c=\frac{p_B+(n-2)b}{n}+\frac{2p_A+(m-2)a}{m}.
\]
Solving the available equations yields, with \(Q=(N-1)(3N-4)\), the following formulas for each pair moment that exists:
\[
a=\frac{(n-1)(m+3n-4)}Q,\quad
b=\frac{n(m+3n-2)}Q,\quad
c=\frac{n(m+3n-4)}Q.
\]
Writing \(Y=1+\sum X_A+\sum X_B\) and expanding its second moment with the single-site and pair expectations yields
\[
\operatorname{Var}(Y)=\frac{(m-1)(n-1)N^2}{(N-1)(3N-4)}.
\]
The cases \(m=1\) or \(n=1\) give zero directly. At fixed \(N\), only the factor \((m-1)(n-1)\) varies with the bipartition, establishing the exact extremizers.

**4. Synchronization of the two proportions.** For \(m,n\ge2\), set \(x=i/(m-1)\), \(y=j/(n-1)\), \(D=x-y\), \(z=(x+y)/2\). The generator \(L\) obeys the exact drift identities
\[
Lx=-D-y/n,\qquad Ly=D+(1-x)/m,
\]
\[
LD=-2D-(1-x)/m-y/n,\qquad
Lz=\tfrac12((1-x)/m-y/n).
\]
The predictable quadratic-variation rate \(Q_D\) of \(D\) is at most \(1/(m-1)+1/(n-1)\) because each of the \(m-1\) or \(n-1\) free update clocks changes its class fraction by at most the reciprocal class size. Applying stationarity to \(L(D^2)=2D LD+Q_D\), using \(|D|\le1\), proves
\[
4\mathbb E[D^2]\le 2/m+2/n+1/(m-1)+1/(n-1).
\]
In the joint-size limit, \(x-y\to0\) in stationary mean square.

**5. Limiting stationary distribution.** Put \(N=m+n\) and assume \(n/N\to\theta\in(0,1)\). For each fixed polynomial \(f\), Taylor expansion of the four jumps of \(z\), their exact rates from Step 1, and the mean-square bound from Step 4 give, in stationary \(L^1\),
\[
NLf(z)=\frac{2(\theta-z)f'(z)+z(1-z)f''(z)}{4\theta(1-\theta)}+o(1).
\]
Indeed, the first-order coefficient is obtained from \(Lz\), the second-order jump coefficient tends to \(z(1-z)/(4\theta(1-\theta))\), and the remaining third-order jump terms are uniformly \(O(1/N)\) after multiplication by \(N\). In expectation, terms involving \(D\) vanish by Cauchy–Schwarz.

Let \(M_r\) be the \(r\)-th moment of a weak subsequential limit of stationary \(z\), which exists because \(z\in[0,1]\). Stationarity and the last equation with \(f(z)=z^r\) imply for every integer \(r\ge1\)
\[
M_0=1,\qquad M_r=\frac{2\theta+r-1}{r+1}M_{r-1}.
\]
Thus \(M_r=(2\theta)_r/(2)_r\), the moments of \(\operatorname{Beta}(2\theta,2(1-\theta))\). Compact-support moment determinacy makes every subsequential limit equal to this beta law. As \(x-y\to0\) in probability, the joint law tends to \((Z,Z)\). Finally,
\[
\frac YN=\frac{1+(m-1)x+(n-1)y}{N}=z+o_{\mathbb P}(1),
\]
which gives the same limiting law for the overall positive fraction. Its variance is \(\theta(1-\theta)/3\), agreeing with the finite exact variance asymptotics.

## Verification

Run the accompanying standard-library program `verify_voter.py` with Python 3. It independently solves the full lumped finite-state stationary linear system using exact rational Gaussian elimination for all \(1\le m,n\le5\), comparing mean and variance to the displayed formulas. It also checks the beta-moment recursion for five rational limiting partition ratios and eleven successive moment orders. The recorded successful run found 25 finite-model comparisons and 55 moment checks. These are corroborative finite computations, not a replacement for the general symbolic and limit proofs above.

## Relationship to prior work

Mobilia and Georgiev's 2004 voter model with competing *rate-biased* inhomogeneities concerns hypercubic lattices and soft zealotry, not the present fixed-opinion bipartite geometry. Mobilia, Petersen and Redner's 2007 article treats the influence of hard zealots on complete graphs and lower-dimensional lattices. Yildiz and coauthors' 2011 preprint develops general dual-walk descriptions of stationary first and second moments for arbitrary finite networks with stubborn agents, and supplies complete-graph evaluations. Their general first-two-moment equations are relevant prior methods; in particular, evaluating pair correlations for a specific graph is not claimed to be a new general principle. The inspected full text does not provide the present all-size opposite-class bipartite evaluation or the limiting beta law. Ben-Ari and coauthors' 2020 complete-bipartite voter article studies quasi-stationarity *without* zealots, a different conditioning regime. The nonlinear well-mixed \(q\)-voter study of Mobilia (2015) is also a different transition rule. The stated contribution is the **evaluated bipartite fluctuation classification together with the stationary macroscopic beta limit and balanced uniform-law specialization**. General existing methods could possibly be adapted to derive some of these expressions; priority is asserted only relative to the sources inspected, not absolutely.

## Limitations

The exact formulas require one positive fixed opinion in the first part, one negative fixed opinion in the second, and unit-rate linear copying. The beta law requires both class sizes to diverge with a nonzero limiting proportion. No assertion is made for arbitrary graphs, zealot placement in one class, nonlinear voting rules, nonstationary transient distributions, or independent external opinion noise. The finite-graph stationary second moments can in principle be recovered using general coalescing-walk methods from the earlier literature. Independent scientific validation and a fully exhaustive priority search have not been performed.

## References

1. M. Mobilia and I. T. Georgiev, *Voting and Catalytic Processes with Inhomogeneities*, arXiv:cond-mat/0412306, first posted 13 December 2004, https://arxiv.org/abs/cond-mat/0412306.
2. M. Mobilia, A. Petersen, and S. Redner, *On the Role of Zealotry in the Voter Model*, arXiv:0706.2892 (2007), https://arxiv.org/abs/0706.2892.
3. E. Yildiz, A. Acemoglu, A. Ozdaglar, A. Saberi, and A. Scaglione, *Discrete Opinion Dynamics with Stubborn Agents*, 2011 submitted manuscript, https://web.mit.edu/Asuman/Desktop/asuman/www/documents/voter-submit.pdf; related journal version *Binary Opinion Dynamics with Stubborn Agents* (2013), DOI:10.1145/2538508.
4. M. Mobilia, *Nonlinear \(q\)-voter model with inflexible zealots*, arXiv:1506.04911 (2015), https://arxiv.org/abs/1506.04911.
5. I. Ben-Ari, M. Panzo, R. Speegle, and J. VandenBerg, *Quasi-Stationary Distributions for the Voter Model on Complete Bipartite Graphs*, arXiv:2004.10187 (2020), https://arxiv.org/abs/2004.10187.

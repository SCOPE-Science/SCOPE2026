# A sharp topology-dependent reversal of finite outbreak-tail risk

## Finding

**Theorem (single-crossover phase diagram).** Fix an integer \(n\ge4\). In either the \(n\)-vertex star \(S_n\) or the \(n\)-vertex path \(P_n\), independently retain each edge with probability \(p\in(0,1)\). Select an initial infected vertex uniformly from all \(n\) vertices and let \(X_G\) be the size of its retained-edge component. For an integer outbreak threshold \(2\le t\le n\), put \(R_G(n,t,p)=\Pr(X_G\ge t)\).

1. At threshold \(t=2\), \(R_{S_n}<R_{P_n}\) for every \(p\in(0,1)\).
2. At threshold \(t=n\), both risks equal \(p^{n-1}\).
3. For \(3\le t\le n-1\), if \(n\le t(t-1)+1\), then \(R_{S_n}>R_{P_n}\) at every \(p\in(0,1)\). If \(n\ge t(t-1)+2\), there is exactly one \(p_*(n,t)\in(0,1)\) such that \(R_{S_n}>R_{P_n}\) for \(0<p<p_*\), equality at \(p=p_*\), and \(R_{S_n}<R_{P_n}\) for \(p_*<p<1\). This crossing is transverse: the derivative of \(R_{S_n}-R_{P_n}\) is strictly negative at \(p_*\).
4. Nevertheless, \(\mathbb E X_{S_n}>\mathbb E X_{P_n}\) for every \(n\ge4\) and \(p\in(0,1)\).

For \(n=3\), star and path are isomorphic and all risks agree. The first crossover among thresholds \(t\ge3\) occurs at \((n,t)=(8,3)\); there its probability is the unique root in \((0,1)\) of
\[
13p^4-64p^3+125p^2-120p+45=0,
\]
namely \(p_*\approx0.909894479585254\). These statements concern final *component size* and not the peak number simultaneously infectious.

## Assumptions and scope

All graphs are simple and undirected. The \(n\)-vertex star has one hub and \(n-1\) leaves. The \(n\)-vertex path has \(n-1\) edges in a chain. Every edge is independently open with the *same* probability \(p\). The initial vertex is independent of the edge states and uniformly distributed. It infects precisely the vertices in its open-edge component. No infection time, reinfection, recovery-time randomness, directed edge dependence or adaptive intervention is part of the model. The risk threshold \(t\) is a fixed integer number of distinct ultimately infected vertices.

Here and below \(\binom ab=0\) when \(b<0\) or \(b>a\). All displayed inequalities are strict for the specified open parameter ranges.

## Proof

**Exact tails.** Write \(q=1-p\). On the star, if exactly \(j\) of its \(n-1\) edges are open, the only nontrivial component has size \(j+1\). A uniform initial vertex selects that component with probability \((j+1)/n\). Hence for \(2\le t\le n\),
\[
R_{S_n}(n,t,p)=\frac1n\sum_{j=t-1}^{n-1}(j+1)\binom{n-1}{j}p^jq^{n-1-j}.\tag{1}
\]
For the path, the expected number of open components of size \(m<n\) is
\[
p^{m-1}\bigl(2q+(n-m-1)q^2\bigr),
\]
because a run of \(m\) vertices can lie at either endpoint (one closed boundary) or in one of \(n-m-1\) interior positions (two closed boundaries). The full-size component occurs with probability \(p^{n-1}\). Size-bias by \(m/n\) to account for the uniform source, sum over \(m\ge t\), and telescope the finite geometric sums. This gives
\[
R_{P_n}(n,t,p)=\frac{p^{t-1}}n\bigl[t(n-t+1)-(t-1)(n-t)p\bigr].\tag{2}
\]
In particular, when \(t=n\) both expressions are \(p^{n-1}\).

**Conditional edge-count comparison.** Set \(N=n-1\) and use the strictly positive Bernstein basis
\[
B_j(p)=\binom Nj p^j(1-p)^{N-j}\quad(0\le j\le N).
\]
The identity
\[
p^k=\sum_{j=k}^{N}\frac{\binom jk}{\binom Nk}B_j(p)
\]
shows that \(R_{S_n}-R_{P_n}=\sum_{j=0}^{N}B_j(p)\delta_j\), where \(\delta_j=0\) for \(j<t-1\) and, for \(t-1\le j\le n-1\),
\[
\delta_j=\frac{j+1}{n}-\frac1n\frac{\binom j{t-1}}{\binom{n-1}{t-1}}
\bigl[t(n-1)+1-(t-1)j\bigr].\tag{3}
\]
The first term is the star risk conditional on \(j\) open edges, and the second is the corresponding conditional path risk. The last coefficient \(\delta_{n-1}=0\).

For \(t=2\), direct simplification gives \(\delta_j=(j-1)(j-n+1)/(n(n-1))\) for \(1\le j\le n-1\). It is negative at every \(2\le j\le n-2\) and zero elsewhere. Because all \(B_j(p)>0\) for \(p\in(0,1)\), this proves assertion 1.

Now suppose \(3\le t\le n-1\). Define the strictly positive ratio of conditional risks
\[
H_j=\frac{\binom j{t-1}}{\binom{n-1}{t-1}}
\frac{t(n-1)+1-(t-1)j}{j+1},\qquad t-1\le j\le n-1.
\]
One has \(H_{t-1}<1\), because \(\binom{n-1}{t-1}>n-t+1\), and \(H_{n-1}=1\). Furthermore,
\[
\frac{H_{j+1}}{H_j}=
\frac{(j+1)^2}{(j-t+2)(j+2)}
\frac{t(n-1)+1-(t-1)(j+1)}{t(n-1)+1-(t-1)j}.\tag{4}
\]
Both positive factors in (4) decrease strictly with \(j\) on \(j\ge t-1\): for the first factor, its continuous derivative has numerator
\[
-(j+1)\bigl((t-2)j+3t-4\bigr)<0,
\]
and the second is \(1-(t-1)/(t(n-1)+1-(t-1)j)\). Thus \((H_j)\) is strictly log-concave, with consecutive ratios strictly decreasing. It first rises to a possible maximum and then falls. Since it begins below one and ends at one, the \(\delta_j\), which have the sign of \(1-H_j\), can change sign at most once, and only from positive to negative as \(j\) increases. If \(H_{n-2}\le1\), the final ratio \(H_{n-1}/H_{n-2}\ge1\), so all earlier ratios exceed or equal one; hence every \(\delta_j\ge0\), with a strictly positive initial coefficient.

A direct calculation from (3) yields
\[
\delta_{n-2}=\frac{t(t-1)-(n-1)}{n(n-1)}.\tag{5}
\]
Therefore, if \(n\le t(t-1)+1\), every coefficient is nonnegative and at least one is positive; assertion 3's first case follows. If \(n\ge t(t-1)+2\), there is a nonempty positive coefficient block followed by a nonempty negative coefficient block, with any zeros at their boundary. The low-\(p\) leading term is positive, as \(\delta_{t-1}>0\); by (5) the high-\(p\) leading term is negative:
\[
R_{S_n}-R_{P_n}=\frac{t(t-1)-(n-1)}n(1-p)+O((1-p)^2).
\]
To prove there is *exactly one* zero, let \(a\) be the first index with \(\delta_a<0\). Divide the Bernstein expansion by \(B_a(p)>0\). Every positive term with index \(j<a\) becomes a positive constant times \(((1-p)/p)^{a-j}\), strictly decreasing in \(p\); every negative term with index \(j>a\) becomes a negative constant times \((p/(1-p))^{j-a}\), again nonincreasing in \(p\). The \(j=a\) term is a negative constant. The quotient is strictly decreasing, and it runs from positive to negative. It therefore has precisely one zero, with negative derivative there. Multiplication back by \(B_a\) establishes the claimed transverse crossing.

**Strict mean comparison.** In any tree, independence of edge retention gives
\[
\mathbb E X_G=\frac1n\sum_{u,v\in V(G)}p^{\operatorname{dist}_G(u,v)}.
\]
Both graphs have the same number of ordered adjacent vertex pairs, namely \(2(n-1)\). Every nonadjacent pair in the star is at distance two, whereas every nonadjacent pair in the path is at distance at least two and, for \(n\ge4\), some are at distance strictly greater than two. Since \(0<p<1\), the star has strictly larger mean, proving assertion 4.

Finally, the crossover condition requires \(n\ge t(t-1)+2\), minimized over \(t\ge3\) at \(t=3,n=8\). Substitution of \((n,t)=(8,3)\) into (1)-(2) gives
\[
R_{S_8}-R_{P_8}=\frac{p^2(1-p)}8
\bigl(13p^4-64p^3+125p^2-120p+45\bigr),
\]
so uniqueness above gives the claimed algebraic root and its precise location.

## Verification

The accompanying standalone `verify.py` uses only Python's standard library and exact rational arithmetic. It independently enumerates all subsets of retained edges and reconstructs connected components on both graphs for sizes three through nine, all thresholds, and three rational probabilities. It also checks the path Bernstein coefficient identity, finite coefficient sign patterns and log-concavity ratios for graph sizes four through sixty, and the strict mean inequality for sizes four through thirty. Outputs and case counts are recorded in `certificate.json`. These finite tests check formula normalization and boundary cases; the proof above, not the enumeration, establishes the assertions for arbitrary \(n,t,p\).

To reproduce, run `python3 verify.py` and compare its JSON output with `certificate.json`.

## Relationship to prior work

The component-size interpretation of independent bond percolation for certain epidemic models and its generating-function approach are classical. Newman, Jensen and Ziff (2001/2002) treat outbreak-cluster sizes and thresholds on two-dimensional small-world networks; their object is a random spatial lattice with shortcuts, not an exact fixed-star-versus-fixed-path tail-risk comparison. Hartfield and Alizon (2013) motivate outbreak-size thresholds and host heterogeneity, but their large-population threshold framework does not imply this finite-tree phase diagram. Kenah and Robins (2006/2007) show why independent bond percolation cannot be identified with *every* stochastic SIR model; this finding deliberately works with independent open edges, not general random infectious periods.

Jevtić, Lanchier and La Salle (2020) study precisely the same uniformly rooted bond-percolation clusters on paths and stars, but the accessible abstract states first- and second-moment formulas as the objective, rather than a complete tail-risk crossing theorem. Their full article could not be inspected, so any distributions or additional results in it remain unresolved prior-art risk; its moment-level subject matter is expressly acknowledged and is not claimed as new here. Known single-path run enumeration and polynomial moment methods alone do not establish that the two topologies have exactly one tail-risk crossover, nor the sharp boundary \(n=t(t-1)+1\). A potential equivalent result in extremal tree reliability or epidemic-percolation literature remains a bibliographic risk; the result is not represented as independently certified.

## Limitations

The theorem compares two specified tree topologies, not all trees on \(n\) vertices. It addresses one uniformly random seed and independent, homogeneous, undirected edge transmission. A finite percolation cluster is an exact mathematical infection set only under this specified mechanism; correlated infectious periods, directed transmission, reinfection, multiple seeds, temporal infection peaks and heterogeneous transmission can change the conclusions. The crossover \(p_*\) is characterized implicitly rather than by an elementary expression for all \(n,t\). This is a structural theorem, not a fitted clinical outbreak threshold.

## References

1. M. E. J. Newman, I. Jensen and R. M. Ziff, *Percolation and epidemics in a two-dimensional small world*, arXiv:cond-mat/0108542, publicly posted 2001-08-31; Physical Review E **65** (2002), 021904. DOI: 10.1103/PhysRevE.65.021904.
2. P. Jevtić, N. Lanchier and A. La Salle, *First and second moments of the size distribution of bond percolation clusters on rings, paths and stars*, Statistics & Probability Letters **161** (2020), 108714. DOI: 10.1016/j.spl.2020.108714.
3. E. Kenah and J. M. Robins, *Second look at the spread of epidemics on networks*, arXiv:q-bio/0610057, publicly posted 2006-10-30; Physical Review E **76** (2007), 036113. DOI: 10.1103/PhysRevE.76.036113.
4. M. Hartfield and S. Alizon, *Introducing the outbreak threshold in epidemiology*, PLOS Pathogens **9** (2013), e1003277, publicly posted 2013-06-06. DOI: 10.1371/journal.ppat.1003277.

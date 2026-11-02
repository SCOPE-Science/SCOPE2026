# Exact stability probabilities with sparse reciprocal top ties

## Finding

Let a balanced two-sided matching market have complete weak preference lists and a fixed perfect matching \(\mu\). Assume that every participant places their assigned partner in their (possibly singleton) highest indifference class, and that agents independently refine every tie uniformly at random. Define the **reciprocal top-tie graph** \(H\): its vertices are the participants, and it has an edge between any unmatched man and woman if and only if each places the other in their respective highest indifference class. Let \(P_\mu\) be the probability that \(\mu\) is stable after refinement.

**Exact graph identity.** For every such instance, including graphs with cycles,
\[
 P_\mu=\int_{[0,1]^{V(H)}}\prod_{\{u,v\}\in E(H)}(1-x_ux_v)\,d\mathbf{x}
 =\sum_{F\subseteq E(H)}(-1)^{|F|}\prod_{v\in V(H)}\frac{1}{\deg_F(v)+1}.
\]
In particular, the probability depends only on \(H\), not on additional candidates in the top indifference classes who do not form reciprocal top ties.

**Sparse exact computation.** If \(H\) is a forest, \(P_\mu\) is computable exactly in \(O(s^2)\) rational-arithmetic operations and polynomial bit complexity, where \(s=|V(H)|\). If every component is a path or a cycle, an explicit closed expression applies. For a path on \(j\ge1\) vertices let \(p_j\) be its factor, with
\[
 p_1=1,\qquad p_2=\frac34,\qquad p_j=\frac23p_{j-1}+\frac1{12}p_{j-2}\quad(j\ge3).
\]
For a cycle on \(j\ge4\) vertices (necessarily even for a matching market), its factor is
\[
 c_j=\left(\frac{2+\sqrt7}{6}\right)^j+
      \left(\frac{2-\sqrt7}{6}\right)^j.
\]
The factors of different components multiply. Both long paths and long cycles have exponential decay base \((2+\sqrt7)/6\).

## Assumptions and scope

The two sides each have the same positive finite number of agents, the fixed matching pairs every participant, and every listed candidate is acceptable. Each participant's matched partner is in their highest tied class. Every weak preference list is independently refined by a uniform permutation within each tied class. The reciprocal top-tie graph is simple and bipartite, with no edge corresponding to a matched pair. The graph may have isolated vertices. No assumption is made about ties below the top class, because no such candidate can form a blocking pair. The polynomial-time assertion is for the input class whose reciprocal top-tie graph is a forest; the closed forms hold for graph components of maximum degree at most two.

## Proof

**1. Reduction to independent latent thresholds.** Fix a participant \(u\). Generate the uniform permutation of their top indifference class by independently sampling continuous priorities uniformly on \([0,1]\), with smaller priority preferred. Write \(x_u\) for the priority of their matched partner. Conditional on \(x_u\), every other top-tied candidate is preferred to the partner with probability \(x_u\), independently for the candidates of that participant. The thresholds \(x_u\) are independent across participants. An unmatched pair can block only if it is an edge of \(H\). Conditional on all thresholds, an edge \(\{u,v\}\) blocks with probability \(x_ux_v\), and the blocking events for distinct edges are independent because each is determined by distinct candidate-priority variables. Multiplying their complementary probabilities and then integrating gives the first identity. Expanding the finite product by subsets \(F\) and using \(\int_0^1 x^d\,dx=1/(d+1)\) gives the second identity. This step proves the stated independence of any nonreciprocal top ties.

**2. Forest algorithm.** Root each tree of \(H\). For a nonroot vertex \(u\) whose children \(w\) have already supplied pairs \((A_w,B_w)\), form
\[
 Q_u(t)=\prod_{w\text{ child of }u}(A_w-B_wt),\quad
 A_u=\int_0^1Q_u(t)\,dt,\quad B_u=\int_0^1tQ_u(t)\,dt.
\]
For a leaf these values are \((1,1/2)\). The conditional contribution of the subtree below \(u\), when the priority of its parent is \(x\), is
\[
 \int_0^1(1-xt)Q_u(t)\,dt=A_u-xB_u.
\]
This proves the recursion inductively. For the root \(r\), the tree probability is \(\int_0^1 Q_r(t)\,dt\), and independent trees multiply. Multiplying the affine factors into the polynomial \(Q_u\) and integrating its coefficients costs \(O(d_u^2)\) rational operations per vertex. As \(\sum_u d_u=2|E(H)|\) for a forest, \(\sum_u d_u^2=O(s^2)\). All generated numbers have polynomial bit length: each partial coefficient comes from finitely many integrations of polynomials whose local degree is bounded by the vertex degree; denominators divide products of local factorials of size at most \((d_u+2)!\), so their logarithmic sizes are \(O(\sum_u(d_u+2)\log(s+2))\). Hence exact rational arithmetic is polynomial-time in the ordinary bit model as well.

**3. Path and cycle formulas.** Let \(K\) be the integral operator on functions of one variable defined by
\[
 (Kf)(x)=\int_0^1(1-xy)f(y)\,dy.
\]
Its image is contained in the span of \(1\) and \(x\), where its representing matrix is
\[
 \begin{pmatrix}1&1/2\\-1/2&-1/3\end{pmatrix}.
\]
Its two nonzero eigenvalues are \(\lambda_\pm=(2\pm\sqrt7)/6\), the roots of \(\lambda^2-(2/3)\lambda-1/12=0\). For a path on \(j\) vertices, the integral identity is \(\langle1,K^{j-1}1\rangle\). Its first two values are \(1\) and \(3/4\), and Cayley--Hamilton gives the recurrence. For a cycle on \(j\) vertices, the integral is the trace of \(K^j\) (the kernel is finite rank), equal to \(\lambda_+^j+\lambda_-^j\). Because \(\lambda_+>|\lambda_-|\), the claimed exponential base is exact. Independent component factors multiply by Fubini's theorem.

## Verification

Run `python3 verify_stability.py` using Python's standard library. The checker independently enumerates the preceding-partner subsets at each vertex rather than evaluating the integral directly. It tests 9,016 finite graph instances against the subset-expansion identity, of which 3,110 forests are checked against the polynomial-message algorithm. It also tests 21 path lengths and 19 cycle lengths (using exact edge expansions for lengths up to nine). For a realizable six-cycle on three matched pairs with every top tie containing all three opposite-side candidates, exhaustive enumeration of all \(6^6=46656\) strict preference refinements yields 10,054 stable profiles, exactly \(c_6=5027/23328\).

## Relationship to prior work

Knuth’s classical uniform-preference stability integral (as used by Pittel) anticipates the product-kernel method for complete reciprocal competition graphs; no originality is claimed for that classical integral technique. Aziz, Biró, Gaspers, de Haan, Mattei and Rastegari study compact-indifference stability probabilities and prove an exact polynomial-time procedure when one side's preferences are certain (Theorem 8 in the 2019 open-access article). Chen's October 2026 preprint proves general exact counting is #P-complete, even with only one non-singleton top tie containing the partner for each participant. The contribution assessed here is exact graph-structured tractability for reciprocal top-tie forests and the closed path/cycle spectra, not the definition of the compact-indifference model or the general hardness theorem. The full text of Chen's primary preprint was inaccessible during this comparison, so possible overlap in an uninspected section remains a publication-priority limitation.

## Limitations

The reduction does not apply without modification when participants can strictly prefer a candidate to their matched partner before ties are refined. The forest algorithm does not establish polynomial-time exact counting for arbitrary reciprocal top-tie graphs. The formulas count stability of a given matching, not the probability that some stable matching exists nor the optimal choice of a matching. The finite verifier is corroboration; universal claims follow from the analytical argument. Publication priority is not independently certified.

## References

1. L. Chen, *The complexity of stability probability under compact indifference*, Zenodo preprint, first public 2026-10-12, https://doi.org/10.5281/zenodo.23308285.
2. H. Aziz, P. Biró, S. Gaspers, R. de Haan, N. Mattei, B. Rastegari, *Stable Matching with Uncertain Linear Preferences*, arXiv:1607.02917 (2016), open-access journal article https://pmc.ncbi.nlm.nih.gov/articles/PMC7066306/ (2019).
3. B. Pittel, *The Average Number of Stable Matchings*, SIAM J. Discrete Math. 2 (1989), https://doi.org/10.1137/0402048; the underlying uniform-preference integral is attributed to Knuth in subsequent literature, for example https://doi.org/10.1002/rsa.70036.

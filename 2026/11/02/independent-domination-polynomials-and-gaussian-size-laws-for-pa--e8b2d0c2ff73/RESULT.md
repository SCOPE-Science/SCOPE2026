# Independent-domination polynomials and Gaussian size laws for path–clique tensor products

## Finding

Let \(q\ge3\) and \(\ell\ge1\) be integers. The *direct*, *tensor*, or *categorical* graph product \(G_{\ell,q}=P_\ell\times K_q\) has vertex set \([\ell]\times[q]\); distinct vertices \((i,c)\) and \((j,d)\) are adjacent precisely when \(|i-j|=1\) and \(c\ne d\). An **independent dominating set** is an independent vertex set whose closed neighborhoods cover the graph, equivalently an inclusion-maximal independent set. Let
\[D_{\ell,q}(z)=\sum_{S\text{ independent dominating in }G_{\ell,q}}z^{|S|}.\]

Define \(A=t z^q\), \(B=t^2z^2/(1-tz)\), and
\[
R_q(t,z)=\begin{pmatrix}
(t+t^2)A & qtB\\
tA & (q-1)tB
\end{pmatrix}.
\]
**Complete cardinality law.** The following rational matrix identity holds as a formal series for every \(q\ge3\):
\[
\boxed{\sum_{\ell\ge1}D_{\ell,q}(z)t^\ell
=\big((1+t)A,qB\big)(I-R_q(t,z))^{-1}
\begin{pmatrix}1+t\\1\end{pmatrix}.}
\]
Thus it determines the exact number of independent dominating sets of every size, for every path length and color-clique order.

**Multiplicity of optimum sets.** For \(\ell\ge2\), the known minimum independent-domination cardinality is
\[s_{\min}(\ell,q)=\left\lceil\frac{2(\ell+1)}3\right\rceil.\]
Writing \(N_{\ell,q}=[z^{s_{\min}(\ell,q)}]D_{\ell,q}(z)\), its *newly evaluated multiplicity* is, for every \(k\ge1\),
\[
\boxed{\begin{aligned}
N_{3k-1,q}&=q(q-1)^{k-1},\\
N_{3k,q}&=kq(q-1)^{k-1}+\mathbf1_{\{k=1,\,q=3\}},\\
N_{3k+1,q}&=\binom{k+1}{2}q(q-1)^{k-1}.
\end{aligned}}
\]
Here \(\mathbf1\) denotes the indicator. For \(\ell=1\), there is one independent dominating set, of size \(q\).

**Size limit law.** Fix \(q\ge3\) and draw an independent dominating set uniformly. Write \(X_{\ell,q}\) for its size. For positive real \(z\) sufficiently near \(1\), there is a unique smallest positive \(t=r_q(z)<1/z\) such that the positive matrix \(R_q(t,z)\) has Perron eigenvalue \(1\). Let
\[
\psi_q(s)=\log\frac{r_q(1)}{r_q(e^s)},\qquad
\mu_q=\psi_q'(0),\qquad\sigma_q^2=\psi_q''(0).
\]
These constants are strictly positive. More precisely,
\[
\mathbb E X_{\ell,q}=\mu_q\ell+O_q(1),\qquad
\operatorname{Var}X_{\ell,q}=\sigma_q^2\ell+O_q(1),\qquad
\frac{X_{\ell,q}-\mu_q\ell}{\sigma_q\sqrt\ell}
\Longrightarrow N(0,1).
\]
For \(q=3\), the values are \(r_3(1)\approx0.5210033076\), \(\mu_3\approx0.9281206562\), and \(\sigma_3^2\approx0.20088577\). Furthermore, the fraction of all independent dominating sets that have minimum cardinality is exponentially small as \(\ell\to\infty\) for every fixed \(q\ge3\).

## Assumptions and scope

All graphs are finite, labeled, simple and undirected. The complete-graph factor has \(q\ge3\) vertices. The generating function includes \(\ell=1\), while the three-case optimum count concerns \(\ell\ge2\). The asymptotic statements hold at each *fixed* \(q\) as \(\ell\to\infty\); no simultaneous limit with growing \(q\) is asserted. A negative or zero coefficient is not treated as evidence about a graph outside this parameter range.

## Proof

**1. Fiber restriction.** For an independent dominating set \(S\), let \(S_i=\{c:(i,c)\in S\}\). Suppose \(2\le |S_i|<q\). Independence forces both neighboring fibers to be empty, because every color in a neighboring fiber is adjacent to at least one of two distinct selected colors. An omitted color in fiber \(i\) then has no selected neighbor, contradiction. Hence each fiber is either empty (symbol \(0\)), a singleton of one color \(c\), or full (symbol \(F\)). This is consistent with the general weak-partition lemma of Kuenzel and Rall, which is not claimed as new.

**2. Exact words.** A full fiber has empty neighboring fibers. Whenever a singleton fiber carries color \(c\), every nonempty neighboring fiber must be another singleton of color \(c\). At least one such neighbor is necessary, because otherwise the omitted colors in that fiber are undominated. Thus singleton fibers form monochromatic runs of length at least two. An empty interior fiber is dominated if and only if it has a neighboring full fiber or it lies between singleton runs of *different* colors. A leading or trailing empty fiber is dominated if and only if its sole neighbor is full. It follows that every independent dominating set is represented *uniquely* by a nonempty sequence of nodes of type \(F\) (one full fiber) or \(C\) (a monochromatic run of length at least two): consecutive nodes are separated by one empty fiber, except two \(F\)-nodes may also be separated by two empty fibers; consecutive \(C\)-nodes have distinct colors. An optional leading or trailing empty fiber is allowed precisely when the adjacent end node is \(F\). The converse follows from the same domination and independence checks. No words are double counted because node boundaries are the maximal singleton runs or isolated full fibers.

**3. Enumerating nodes.** A full node has length–cardinality weight \(A=t z^q\). A singleton-run node of a fixed color has weight \(B=\sum_{j\ge2}(tz)^j=t^2z^2/(1-tz)\). A first \(F\)-node allows an optional leading empty fiber and has weight \((1+t)A\); a first \(C\)-node has one of \(q\) colors and weight \(qB\). Appending \(F\) after \(F\) allows one or two empty fibers, giving \((t+t^2)A\); appending \(C\) after \(F\) gives \(qtB\); appending \(F\) after \(C\) gives \(tA\); appending \(C\) after \(C\) gives \((q-1)tB\) because its color must change. An end \(F\) permits a trailing empty fiber, whereas an end \(C\) does not. Summing all node counts gives the stated matrix inverse.

**4. Optimum multiplicities.** Let a word contain \(a\) full nodes, \(b\) colored nodes, \(s\) selected singleton fibers, \(d\) double-zero separators, and \(e\) end zeros. Then \(s\ge2b\), \(d\le a-1\) if \(a>0\), \(e\le2\), and
\[\ell=s+2a+b-1+d+e,\qquad |S|=s+qa.\]
Therefore
\[3|S|-2(\ell+1)=(s-2b)+(3q-4)a-2(d+e).\]
When \(a=0\), this is nonnegative, and the least size occurs for the largest possible number of colored runs \(b=k=\lfloor(\ell+1)/3\rfloor\). Such runs have a total excess length \(u=\ell-3k+1\in\{0,1,2\}\) beyond their minimum length two. They admit \(\binom{k+u-1}{u}\) ordered length compositions and \(q(q-1)^{k-1}\) legal colorings. This proves the three stated multiplicities without full nodes. When \(a\ge1\), using \(d\le a-1\), \(e\le2\), and \(q\ge3\) gives \(3|S|-2(\ell+1)\ge(3q-6)a-2\). Except for the case \(a=1,q=3,e=2,s=0\) (the word \(0F0\) of length three), a full-node word exceeds the minimum size. For \(a=1,q=3\), equality in the potentially exceptional lower bound requires \(e=2\), which forces that sole full node to be both end nodes and hence forces \(b=0\). The one exception gives the stated additional set. This also reproves the known minimum-cardinality formula by a direct count.

**5. Dominant root and Gaussian limit.** Specializing to \(z>0\), the entries of \(R_q(t,z)\) are strictly positive for \(0<t<1/z\) and strictly increasing in \(t\). Its spectral radius moves strictly from zero to infinity, so the equation \(\rho(R_q(r,z))=1\) has a unique solution \(0<r=r_q(z)<1/z\). The Perron eigenvalue is simple and crosses one transversely. At \(z=1\), a hypothetical other singularity \(t\) with \(|t|=r\) would force equality in entrywise triangle bounds. In particular, the \(F\)-to-\(F\) entry has positive terms of lengths two and three, forcing \(\arg t=0\). Thus the positive pole is the unique singularity of minimum modulus. The entries are rational, so the same simple-pole dominance persists analytically for \(z\) near one. The numerator and boundary weights are strictly positive at the pole, with no cancellation. Consequently there are an analytic nonzero prefactor \(c_q(z)\) and \(\eta_q<1\) such that, uniformly near \(z=1\),
\[D_{\ell,q}(z)=c_q(z)r_q(z)^{-\ell}(1+O_q(\eta_q^\ell)).\]
Setting \(z=e^s\) and normalizing by \(D_{\ell,q}(1)\) gives the analytic moment generating function form \(\mathbb Ee^{sX_{\ell,q}}=c_q(e^s)c_q(1)^{-1}e^{\ell\psi_q(s)}(1+O(\eta_q^\ell))\). Taylor expansion at \(s=0\), followed by the characteristic-function convergence criterion, establishes the asserted mean, variance and Gaussian limit provided \(\sigma_q^2>0\).

For strict variance positivity, the standard nondegeneracy criterion for additive weights on a positive, irreducible finite-state transfer system says that zero limiting variance is possible only if every directed closed walk has selected-cardinality increment proportional to its length. The above run system has a finite-state per-fiber realization (record whether a singleton run has begun, whether it is long enough, and the previous fiber symbol), and is irreducible on its recurrent component. It contains the two closed \(F\)-to-\(F\) transitions of weights \(t^2z^q\) and \(t^3z^q\). These have the same selected-cardinality increment \(q\) but lengths two and three. They cannot have a common cardinality-per-length ratio, proving \(\sigma_q^2>0\). Positivity of \(\mu_q\) follows because every admissible word has a positive fraction of selected fibers, at least the proved lower bound \(2(\ell+1)/3\).

Finally, \(D_{\ell,q}(1)\asymp_q r_q(1)^{-\ell}\). At \(t_0=(q-1)^{-1/3}\), the \(C\)-to-\(C\) matrix entry alone is \((q-1)t_0^3/(1-t_0)=1/(1-t_0)>1\), so \(r_q(1)<t_0\). Since \(N_{\ell,q}=O_q(\ell^2(q-1)^{\ell/3})\), dividing by \(D_{\ell,q}(1)\) proves exponential rarity of minimum independent dominating sets.

## Verification

The accompanying standalone Python 3 program `verify_path_clique.py` uses three separately expressed finite procedures: original graph-adjacency bitmask search, fiber-local predicate enumeration, and run-node transition counting. It checks 13 parameter pairs, including all original graph subsets for the cases with at most 18 vertices (403,264 bitmasks in aggregate), and confirms all independent domination polynomials and optimum multiplicities. Numerical Perron-root differentiation independently checks \(r_q(1)\), \(\mu_q\) and \(\sigma_q^2\) for \(q=3,4,5\). The finite calculations validate examples and implementation but are not the proof of the all-parameter identities or the central limit theorem.

## Relationship to prior work

Jahari and Alikhani (2018) define and study independent domination polynomials and derive formulas for ordinary paths and several compound graph families. Those results are not formulas for the direct product \(P_\ell\times K_q\). Kuenzel and Rall (2019) give a weak-partition characterization of all maximal independent sets of \(G\times K_q\). Their 2022 preprint (subsequently published 2023) determines the independent domination number of \(P_\ell\times K_q\) and describes constructions attaining it. The fiber restriction used here is expressly credited to them. The results here evaluate the full bivariate enumerator for paths, the precise count of all optimal sets including its single exception, and the Gaussian law and exponential rarity for a uniform maximal independent set. Those quantitative results are not stated in the inspected portions of the primary papers, though the general weak-partition criterion is a substantive mathematical precursor.

## Limitations

No statement is made about the case \(q=2\), which has a different disconnected-product structure. The Gaussian theorem is for fixed \(q\) only, with implicit constants depending on \(q\). The count pertains to labeled vertex subsets, not automorphism classes. The preexisting weak-partition characterization substantially narrows priority claims: it implies a general enumeration procedure in principle, even though the evaluated rational formula and limit laws were not located. Publication priority against unindexed or differently phrased results is not fully settled. No independent mathematical audit has been performed.

## References

1. S. Jahari and S. Alikhani, *On the independent domination polynomial of a graph*, arXiv:1808.07369, first public 2018-08-21, https://arxiv.org/abs/1808.07369.
2. K. Kuenzel and D. F. Rall, *On well-covered direct products*, arXiv:1901.03218, first public 2019-01-10, https://arxiv.org/abs/1901.03218.
3. K. Kuenzel and D. F. Rall, *On independent domination in direct products*, arXiv:2203.12397, first public 2022-03-23, https://arxiv.org/abs/2203.12397; *Graphs and Combinatorics* 39, article 7 (2023), DOI:10.1007/s00373-022-02600-0.
4. P. Flajolet and R. Sedgewick, *Analytic Combinatorics*, Cambridge University Press, 2009, Chapter IX (quasi-powers and normal limit laws). Used for standard analytic tools, not for the graph-product enumeration.

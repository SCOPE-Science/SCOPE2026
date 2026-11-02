# A sorted-cut criterion for weighted-variation contraction of normalized heat on \(K_{2,q}\)

## Finding

**Theorem.** Fix an integer \(q\ge3\). Let \(K_{2,q}\) have left vertices \(u,v\), right vertices \(y_1,\ldots,y_q\), and independently chosen strictly positive edge-variation weights \(a_j\) on \(uy_j\) and \(b_j\) on \(vy_j\). The **heat rates** are unweighted and degree-normalized: \(Q=P-I\), where \(P\) averages a vertex's neighbors, and \(H_t=e^{tQ}\). Set
\[
J(f)=\sum_{j=1}^q\bigl(a_j|f(u)-f(y_j)|+b_j|f(v)-f(y_j)|\bigr),\qquad A=\sum_j a_j,\quad B=\sum_jb_j,\quad W=A+B.
\]
For every \(s\in\{0,\ldots,q\}\), put
\[
d_s=\tfrac12-\tfrac{s}{q},\qquad
\tau_j(s)=(1+d_s+|d_s|)a_j-(1-d_s+|d_s|)b_j,
\]
and let \(T_s\) be the sum of the largest \(s\) values among \(\tau_1(s),\ldots,\tau_q(s)\), with \(T_0=0\).

The following assertions are equivalent:

1. \(J(H_tf)\le J(f)\) for **every** real vertex signal \(f\) and **every** \(t\ge0\).
2. The \(q\) column inequalities
   \[
   (q+2)(a_j+b_j)\ge W\qquad(1\le j\le q)
   \]
   and the \(q+1\) sorted-cut inequalities
   \[
   T_s\le (1+d_s)A-|d_s|B\qquad(0\le s\le q)
   \]
   all hold.

The test can be evaluated in \(O(q^2\log q)\) arithmetic comparisons and operations. Whenever one condition fails, its violating column or maximizing sorted subset constructs an indicator function with \(J(H_t f)>J(f)\) for all sufficiently small positive \(t\).

The distinction between singleton-cut tests and mixed cuts first occurs at \(q=3\) (five vertices). On \(K_{2,3}\), take
\[
(a_1,a_2,a_3)=(4,1,1),\qquad(b_1,b_2,b_3)=(1,8,8).
\]
Every singleton-cut test is strictly contractive at first order, but the indicator of \(\{u,y_1\}\) has \(J(f)=3\) and \(\left.\frac{d}{dt}\right|_{0+}J(H_tf)=1/6>0\). For \(q=1,2\), singleton-cut tests suffice; these are included as boundary comparisons, not as a separate new classification.

## Assumptions and scope

The vertex set has exactly \(q+2\) vertices. Both vertex classes are labelled; all \(a_j,b_j\) are finite, real and strictly positive. They weight only the total-variation functional, not the heat-transition probabilities. The normalized generator is
\[
(Qf)(u)=q^{-1}\sum_j f(y_j)-f(u),\quad
(Qf)(v)=q^{-1}\sum_j f(y_j)-f(v),\quad
(Qf)(y_j)=\tfrac12(f(u)+f(v))-f(y_j).
\]
The theorem concerns a linear, continuous-time, constant-preserving Markov semigroup and a one-input variation seminorm. The inequality is over every real signal, not just binary signals, and over the entire nonnegative time axis. All comparisons are exact, including equality cases. Multiplying all variation weights by the same positive factor changes none of the criteria.

## Proof

**1. Reduction to binary cuts.** Define \(E_\varepsilon=I+\varepsilon Q\) for \(0<\varepsilon<1/2\). This map preserves constants. For an indicator \(\mathbf1_S\), all edges with unequal endpoint labels retain the sign of their difference under \(E_\varepsilon\), since values initially equal to one remain above \(1-\varepsilon\), whereas values initially equal to zero stay below \(\varepsilon\). The zero-difference edges contribute the absolute directional derivative. Therefore
\[
J(E_\varepsilon\mathbf1_S)=J(\mathbf1_S)+\varepsilon\Phi(S),\qquad
\Phi(S)=\left.\frac{d}{dt}\right|_{0+}J(H_t\mathbf1_S).
\]
If every nontrivial cut has \(\Phi(S)\le0\), then \(E_\varepsilon\) contracts \(J\) on every indicator. For any real \(f\), list its distinct values in increasing order and express it as a constant plus a nonnegative combination of nested superlevel indicators. The edgewise layer-cake identity gives the **exact** equality \(J(f)=\sum_k c_kJ(\mathbf1_{S_k})\) with \(c_k\ge0\). Linearity and the triangle inequality then yield
\[
J(E_\varepsilon f)\le\sum_kc_kJ(E_\varepsilon\mathbf1_{S_k})\le J(f).
\]
Applying this to every iterate \(E_{t/n}^{\,n}\), with \(n>2t\), and taking the finite-dimensional exponential limit proves \(J(H_tf)\le J(f)\) for all \(t\ge0\). Conversely, any cut with \(\Phi(S)>0\) strictly amplifies variation for sufficiently small positive \(t\) by the first-order expansion. Thus all-time contractivity is **equivalent** to the nonpositivity of all binary-cut derivatives.

**2. Cuts omitting both left vertices.** Let \(S=\{y_j:j\in Y\}\), with \(|Y|=s\) and \(C(Y)=\sum_{j\in Y}(a_j+b_j)\). The generator gives
\[
\Phi(S)=\tfrac{s}{q}W-\bigl(1+\tfrac{2s}{q}\bigr)C(Y).
\]
With \(s=1\), its nonpositivity is precisely \((q+2)(a_j+b_j)\ge W\) for each column. Conversely, these inequalities imply \(C(Y)\ge sW/(q+2)\), and hence
\[
\Phi(S)\le\frac{2s(1-s)}{q(q+2)}W\le0\quad(1\le s\le q).
\]
The empty cut has zero variation and zero derivative.

**3. Cuts containing exactly one left vertex.** Every such cut, up to taking complements, has the form \(S=\{u\}\cup\{y_j:j\in Y\}\). Put \(s=|Y|\) and \(d=1/2-s/q\). On edges from \(u\) to \(Y\), and from \(v\) to its complementary right set, both indicator values agree, so the absolute derivative contributes \(|d|\) times the edge weight. On the remaining crossing edges, the derivative contributes respectively \(-(1+d)\) and \(-(1-d)\) times the edge weight. Consequently
\[
\begin{aligned}
\Phi(S)&=|d|\sum_{j\in Y}a_j-(1+d)\sum_{j\notin Y}a_j\\
&\quad -(1-d)\sum_{j\in Y}b_j+|d|\sum_{j\notin Y}b_j\\
&=|d|B-(1+d)A+\sum_{j\in Y}\tau_j(s).
\end{aligned}
\]
For fixed \(s\), the maximum over every \(s\)-element set \(Y\) is obtained by taking the \(s\) largest values of \(\tau_j(s)\). Its nonpositivity is exactly the corresponding sorted-cut inequality. The complement of a cut containing \(v\) but not \(u\) contains \(u\) but not \(v\), and its variation derivative is identical because \(H_t\mathbf1_{S^c}=\mathbf1-H_t\mathbf1_S\). Cuts containing both left vertices are complements of cuts omitting both. Thus the preceding two families exhaust all binary cuts. This proves the equivalence and the constructive obstruction statement.

**4. Complexity and the first mixed-cut obstruction.** Evaluate the \(q\) column conditions directly. For every \(s=0,\ldots,q\), compute \(q\) values \(\tau_j(s)\), sort them, and sum the largest \(s\). Performing \(q+1\) ordinary sorts costs \(O(q^2\log q)\). If an inequality fails, the corresponding ordered subset directly specifies the amplifying cut.

For \(q=1\), there are no genuinely mixed cuts. For \(q=2\), a cut with exactly one selected left vertex and exactly one selected right vertex has \(d=0\), so its derivative is the negative of the sum of the two crossing edge weights. The remaining nontrivial cuts are singleton cuts or complements. Thus all mixed cuts are automatically contractive when \(q\le2\).

For the displayed \(q=3\) example, \(A=6\), \(B=17\), \(W=23\). The singleton left-vertex derivative for \(u\) is \((B-3A)/2=-1/2\), and for \(v\) it is \((A-3B)/2=-45/2\). The right-vertex derivatives are \(23/3-(5/3)c_j\), where \((c_1,c_2,c_3)=(5,9,9)\); all are negative. But for \(S=\{u,y_1\}\), \(d=1/6\), and the formula above gives \(\Phi(S)=1/6\) and \(J(\mathbf1_S)=a_2+a_3+b_1=3\). This establishes the five-vertex threshold.

## Verification

The standalone Python program `verify.py` uses only the standard library's exact rational arithmetic. It directly computes the generator's directional derivative on binary cuts and compares exhaustive cut tests against the sorted certificate. On deterministic samples it checked 276 positive weight profiles over \(q=1,\ldots,7\), covering 25,728 binary cuts, and 12,576 exact-rational Euler-step variation inequalities on certified contractive profiles. It also checks the rational five-vertex obstruction, including \(J(E_{1/16}\mathbf1_S)=3+1/96\). These finite checks corroborate arithmetic and boundary cases; the universal claim is proved above without relying on enumeration.

To reproduce: `python3 verify.py`. Use the version included beside this document, rather than an external or mutable script.

## Relationship to prior work

Bauer, Horn, Lin, Lippner, Mangoubi and Yau develop heat-gradient estimates under graph curvature conditions (arXiv:1306.2561). Their estimates involve positive solutions, curvature and quadratic gradient quantities rather than an exact anisotropic edge-\(\ell^1\) variation contraction cone. Van Gennip, Guillen, Osting and Bertozzi develop graph total variation, coarea, graph curvature and heat-threshold dynamics (arXiv:1307.0045, especially Sections 2–4); their coarea framework motivates the cut reduction, but the inspected results do not state the sorted two-row weighted semigroup criterion. Couprie, Grady, Najman, Pesquet and Talbot study dual-constrained graph total-variation regularization (DOI:10.1137/120895068), a different proximal/optimization problem rather than the degree-normalized heat semigroup considered here.

The standard cut/coarea principle alone leaves exponentially many vertex subsets. The specific reduction to \(q\) column conditions and \(q+1\) sorted tests, together with the five-vertex mixed-cut obstruction, is the assertion requiring the new argument.

## Limitations

The theorem applies to complete bipartite graphs with exactly two vertices on one side and \(q\ge3\) on the other, with unit jump rates after degree normalization. Variation weights are independent but strictly positive; the heat rates are not allowed to depend on those weights. No classification of general \(K_{p,q}\) with \(p\ge3\), general graphs, or independently weighted jump rates is asserted. The result establishes an all-time nonexpansivity criterion, not the sharp operator amplification factor at a prescribed positive time when the criterion fails. Prior-work coverage remains subject to indexing and historical-literature limitations.

## References

1. F. Bauer, P. Horn, Y. Lin, G. Lippner, D. Mangoubi, and S.-T. Yau, *Li-Yau inequality on graphs*, arXiv:1306.2561 (first public version June 11, 2013), https://arxiv.org/abs/1306.2561.
2. Y. van Gennip, N. Guillen, B. Osting, and A. L. Bertozzi, *Mean curvature, threshold dynamics, and phase field theory on finite graphs*, arXiv:1307.0045 (first public version June 28, 2013), https://arxiv.org/abs/1307.0045; *Milan Journal of Mathematics* 82 (2014), 3–65, DOI:10.1007/s00032-014-0216-8.
3. C. Couprie, L. Grady, L. Najman, J.-C. Pesquet, and H. Talbot, *Dual Constrained TV-based Regularization on Graphs*, *SIAM Journal on Imaging Sciences* 6 (2013), 1246–1273, DOI:10.1137/120895068.

# Sharp weighted variation of centered maximal averages on cycles of diameter at most two

## Finding
Let \(C_n\) be the simple cycle with \(n\in\{3,4,5\}\) vertices. Give its vertices arbitrary strictly positive masses \(w_0,\ldots,w_{n-1}\), and put \(W=\sum_iw_i\), \(w_*=\min_i w_i\). For the mass-weighted **centered** Hardy--Littlewood maximal function \(M_w\), whose balls are determined by ordinary graph distance, and the **unweighted edge** total variation \(\operatorname{Var}(f)=\sum_i|f_{i+1}-f_i|\) (indices modulo \(n\)), the exact, attained constant is
\[
\boxed{\sup_{\operatorname{Var}(f)>0}\frac{\operatorname{Var}(M_w f)}{\operatorname{Var}(f)}=1-\frac{w_*}{W}.}
\]
For each vertex with mass \(w_*\), its point-mass indicator is an extremizer. More strongly, every real input satisfies the sharp **additive coarea deficit**
\[
\operatorname{Var}(M_w f)\le \operatorname{Var}(|f|)-2\bigl(\overline{|f|}_w-\min_i|f_i|\bigr),
\qquad \overline{|f|}_w=\frac1W\sum_iw_i|f_i|.
\]
The coefficient \(2\) cannot be increased uniformly, as point-mass indicators attain equality. For fixed \(n\) and total mass \(W\), the unique minimizer over positive masses is uniform mass, with optimal constant \(1-1/n\). Along positive mass vectors with \(w_*/W\to0\), the sharp constants approach \(1\) without attaining it.

## Assumptions and scope
Vertices form an undirected, unweighted simple cycle of size \(3\), \(4\), or \(5\). Each vertex mass is strictly positive, and only *averaging* uses these masses. For an input \(f:V\to\mathbb R\), let
\[
(M_wf)(i)=\max_{r\ge0}\frac{\sum_{j\in B(i,r)}w_j|f_j|}{\sum_{j\in B(i,r)}w_j},\qquad
B(i,r)=\{j:\operatorname{dist}_{C_n}(i,j)\le r\}.
\]
The edge variation is neither vertex-mass-weighted nor conductance-weighted. A radius-zero ball consists of its center; when \(n=4,5\), the only other proper ball is the three-vertex radius-one ball, while radius-two balls contain all vertices. For \(n=3\), radius-one balls already contain all vertices. Constant inputs are excluded from the quotient but included in the additive estimate.

## Proof
Write \(h_i=|f_i|\), \(a=\min_i h_i\), \(b=\max_i h_i\), and \(q=W^{-1}\sum_iw_ih_i\). If \(h\) is constant, the assertions are immediate. Otherwise \(a<q<b\). The operator only depends on \(h\), and \(\operatorname{Var}(h)\le\operatorname{Var}(f)\).

**Level-set lemma.** For every \(t>q\), set \(E_t=\{i:h_i>t\}\) and \(F_t=\{i:(M_wh)_i>t\}\). The radius-zero average gives \(E_t\subseteq F_t\). If \(i\in F_t\setminus E_t\), neither its radius-zero value (at most \(t\)) nor the whole-cycle average \(q<t\) can certify membership. For \(n=3\) this cannot happen. For \(n=4,5\) only a radius-one average can exceed \(t\). That ball contains \(i\) and its two cycle neighbors; because \(h_i\le t\), at least one neighbor must belong to \(E_t\). Thus every newly added vertex is adjacent to an original high-level vertex. If \(E_t\) is empty, then all averages are at most \(t\), so \(F_t\) is empty as well. Otherwise every connected component of \(F_t\) contains one of \(E_t\), and the number of connected components cannot increase.

A nonempty proper subset of a simple cycle has edge boundary size twice its number of connected components; the whole set has boundary zero. Consequently \(|\partial F_t|\le|\partial E_t|\) for every \(t>q\). For \(t<q\), \(F_t\) is the entire cycle because every centered ball system contains the whole-cycle average \(q\). For \(a<t<q\), \(E_t\) is a nonempty proper subset, so \(|\partial E_t|\ge2\).

The finite graph coarea identity, obtained edgewise by integrating \(\mathbf1_{\{h_i>t\}}-\mathbf1_{\{h_{i+1}>t\}}\) in absolute value, gives
\[
\begin{aligned}
\operatorname{Var}(M_wh)
&=\int_{-\infty}^{\infty}|\partial F_t|\,dt
\le\int_q^b|\partial E_t|\,dt\\
&=\operatorname{Var}(h)-\int_a^q|\partial E_t|\,dt
\le\operatorname{Var}(h)-2(q-a).
\end{aligned}
\]
This is the asserted additive deficit, after observing \(M_wf=M_wh\).

Every vertex of a cycle has degree two. Using \(h_i\ge a\), positivity of the weights, and the triangle inequality,
\[
W(q-a)=\sum_iw_i(h_i-a)\ge w_*\sum_i(h_i-a)
\ge\frac{w_*}{2}\sum_i|h_i-h_{i+1}|=\frac{w_*}{2}\operatorname{Var}(h).
\]
Therefore \(\operatorname{Var}(M_wf)\le(1-w_*/W)\operatorname{Var}(h)\le(1-w_*/W)\operatorname{Var}(f)\).

**Sharpness.** Choose a minimum-mass vertex \(k\) and set \(h_k=1\), \(h_i=0\) otherwise. Then \(\operatorname{Var}(h)=2\) and \(q=w_*/W\). At \(k\), the maximal value is \(1\). On its two neighbors it is at least \(q\), and on every remaining vertex (if any) it equals \(q\), since no proper centered ball at such a vertex contains \(k\). The resulting maximal values decrease (weakly) along both arcs from \(k\) to the complementary lowest plateau, so their cycle variation is \(2(1-q)\). This attains both the multiplicative bound and the additive deficit. (For \(n=3\) the two neighbors are already the lowest plateau.)

Finally \(w_*/W\le1/n\), with equality if and only if all \(n\) masses are equal. This proves the unique minimax distribution. A sequence of positive masses with the smallest relative mass approaching zero gives the indicated supremal limit.

## Verification
The standalone file `verify_exact.py` evaluates all weighted centered graph-ball averages with exact Python rational arithmetic. It checked every integer mass vector with entries in \(\{1,2,3\}\), all test inputs with entries in \(\{0,1,2\}\), and every single-site delta input for \(n=3,4,5\). It passed 65,286 nonconstant input/mass combinations and 1,620 delta equalities. These finite checks test implementations and boundaries; they do not prove the universal statement, which follows from the coarea argument above. Run `python3 verify_exact.py` using the Python standard library.

## Relationship to prior work
Bober--Carneiro--Hughes--Pierce initiated discrete total-variation estimates for Hardy--Littlewood maximal operators on \(\mathbb Z\); Madrid sharpened the discrete \(\ell^1\)-to-variation bound. These concern infinite integer lattices with counting measure, not the arbitrary vertex-mass finite-cycle quotient. González-Riquelme--Madrid established counting-measure estimates on complete and star graphs. González-Riquelme--Kovač--Madrid proved the unweighted \(C_4\) constant \(3/4\) and computed uniform-measure constants for five-vertex graphs; their \(C_4\) argument uses finite linear programs. The present claim does not reassert those counting-measure values as individually new: it determines the whole positive mass simplex for every \(C_3,C_4,C_5\), proves the sharp additive coarea deficit, and identifies the minimizing mass configuration analytically.

## Limitations
The multiplicative theorem is restricted to cycles with at most five vertices. For longer cycles, proper balls of radius two can certify additional high-level vertices that are not adjacent to the original high-level set, so the key level-set argument does not directly apply; this is a limit of the proof, not a counterexample beyond five vertices. Edge variation is unweighted and the averaging balls are centered. No claim is made for other variation exponents, noncentered operators, arbitrary finite graphs, or signed linear averages without taking absolute values. Published/unindexed weighted finite-cycle treatments remain a priority risk; independent assessment has not been performed.

## References
- J. Bober, E. Carneiro, K. Hughes, L. B. Pierce, *On a discrete version of Tanaka's theorem for maximal functions*, arXiv:1005.3030v1, 2010-05-17, https://arxiv.org/abs/1005.3030 .
- J. Madrid, *Sharp inequalities for the variation of the discrete maximal function*, arXiv:1512.04112v1, 2015-12-13, https://arxiv.org/abs/1512.04112 .
- C. González-Riquelme, J. Madrid, *Sharp inequalities for maximal operators on finite graphs*, arXiv:2005.03146v1, 2020-05-06, https://arxiv.org/abs/2005.03146 .
- C. González-Riquelme, V. Kovač, J. Madrid, *Sharp variational inequalities for the Hardy--Littlewood maximal operator on finite undirected graphs*, arXiv:2603.12462v1, 2026-03-12, https://arxiv.org/abs/2603.12462 .

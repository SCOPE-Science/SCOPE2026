# Universal leaf/path-length anticorrelation in root-biased Hoppe trees

## Finding
Let \(T_n\) be the Hoppe recursive tree with fixed root weight \(\theta>0\), all nonroot weights one, and \(n\ge2\) vertices. Write \(L_n\) for its number of leaves (vertices with no children), and \(P_n\) for its internal path length (sum of depths of all vertices from the root). Their covariance \(C_n=\operatorname{Cov}(L_n,P_n)\) is \(C_2=0\) and, for every integer \(n\ge3\), satisfies
\[
C_n=-\frac{n+\theta-3}{4}+\frac{\theta(\theta-1)}{2(\theta+n-2)}\left(1+\sum_{j=2}^{n-2}\frac1{\theta+j}-\frac{\theta-1}{2(\theta+1)}\right).
\]
In particular, \(C_n<0\) for every \(n\ge3\) and every \(\theta>0\). The empty sum when \(n=3\) is zero.

For fixed \(\theta>0\),
\[
C_n=-\frac{n+\theta-3}{4}+O_\theta\!\left(\frac{\log n}{n}\right),\qquad \lim_{n\to\infty}\frac{C_n}{n}=-\frac14.
\]
The marginal variance asymptotics established by Leckey and Neininger are \(\operatorname{Var}(L_n)=n/12+O_\theta(1)\) and \(\operatorname{Var}(P_n)=v_\theta n^2+o_\theta(n^2)\), with \(v_\theta=2/(\theta+1)-\Psi_1(\theta+1)>0\). Therefore
\[
\lim_{n\to\infty}\sqrt n\,\operatorname{Corr}(L_n,P_n)=-\frac{\sqrt3}{2\sqrt{v_\theta}}.
\]
The \(\theta=1\) benchmark simplifies to \(C_n=-(n-2)/4\). Only the formula uniformly across root weights and its strict-sign/sharp-asymptotic consequences are assessed as the new contribution.

## Assumptions and scope
Start with root vertex labeled \(1\). Given a tree on \(m\ge1\) vertices, choose one existing vertex as parent of new vertex \(m+1\) with probability equal to its weight divided by \(\theta+m-1\); the root has weight \(\theta\), every other vertex weight one. Fix \(\theta>0\) independently of \(n\). All expectations and covariances are with respect to this attachment law. The root has depth zero. For \(n\ge2\), the root is never a leaf. There are no claims for growing \(\theta=\theta_n\), other weighted attachment rules, or other models of recursive trees. The trigamma function \(\Psi_1(x)=\sum_{k=0}^\infty(x+k)^{-2}\) for positive \(x\).

## Proof
Fix \(n\ge2\) and let \(\mathcal F_n\) denote the entire tree on \(n\) vertices. Set \(W_n=\theta+n-1\), and introduce the sum of leaf depths
\[
Q_n=\sum_{v:\,v\text{ is a leaf of }T_n}\operatorname{depth}(v).
\]
Let \(J\) indicate that the selected parent is currently a leaf and let \(d\) be that parent's depth. The deterministic update equations are
\[
L_{n+1}=L_n+1-J,\quad P_{n+1}=P_n+1+d,\quad Q_{n+1}=Q_n+1+(1-J)d.
\]
Because every leaf is nonroot, and the root's depth is zero, conditional expectations are \(\mathbb E[J\mid\mathcal F_n]=L_n/W_n\), \(\mathbb E[d\mid\mathcal F_n]=P_n/W_n\), and \(\mathbb E[Jd\mid\mathcal F_n]=Q_n/W_n\). Consequently
\[
\begin{aligned}
\mathbb E[L_{n+1}\mid\mathcal F_n]&=(1-W_n^{-1})L_n+1,\\
\mathbb E[P_{n+1}\mid\mathcal F_n]&=(1+W_n^{-1})P_n+1,\\
\mathbb E[Q_{n+1}\mid\mathcal F_n]&=(1-W_n^{-1})Q_n+1+P_n/W_n.
\end{aligned}
\]
Starting from \(L_2=P_2=Q_2=1\), the first recursion gives the exact mean
\[
\ell_n:=\mathbb E[L_n]=\frac{W_n}{2}+\frac{h}{2(W_n-1)},\qquad h:=\theta(1-\theta).
\]
The second gives \(p_n:=\mathbb E[P_n]=W_n\sum_{j=1}^{n-1}(\theta+j)^{-1}\). Let \(q_n:=\mathbb E[Q_n]\), define \(\delta_n:=q_n-\ell_np_n/W_n\), and let \(C_n:=\mathbb E[L_nP_n]-\ell_np_n\). Expanding the product update, taking conditional expectation, and subtracting \(\ell_{n+1}p_{n+1}\) yields the exact recurrence
\[
C_{n+1}=C_n+\frac{\ell_np_n}{W_n^2}-\frac{q_n}{W_n}=C_n-\frac{\delta_n}{W_n}.
\]
Using the three conditional means and the displayed expression for \(\ell_n\), direct substitution gives
\[
\delta_2=\frac{\theta}{\theta+1},\qquad
\delta_{n+1}=\frac{W_n-1}{W_n}\delta_n+\frac12-\frac{h}{2W_n(W_n+1)}.
\]
The last forcing term is positive for all \(\theta>0\): if \(\theta\ge1\), then \(h\le0\); if \(0<\theta<1\), then \(0<h\le1/4\) and \(W_n>1\). Thus induction gives \(\delta_n>0\) for \(n\ge2\), so \(C_{n+1}<C_n\). Since \(C_2=0\), the claimed strict negativity holds, including \(n=3\).

For the explicit value, solving the first-order affine recurrence gives
\[
\delta_n=\frac{W_n}{4}+\frac{\theta(\theta-1)}{2(W_n-1)}\left(\sum_{j=2}^{n-1}\frac1{\theta+j}-\frac{\theta-1}{2(\theta+1)}\right).
\]
This identity holds at \(n=2\) and substitution establishes the induction step. Sum \(C_{m+1}-C_m=-\delta_m/W_m\) over \(m=2,\ldots,n-1\). The first term sums to \(-(n-2)/4\); the remaining terms telescope after using \(\big(W_m(W_m-1)\big)^{-1}=(W_m-1)^{-1}-W_m^{-1}\) and exchanging the finite harmonic sums. The resulting expression is the formula under **Finding** (including its \(n=3\) empty-sum convention). For fixed \(\theta\), the harmonic sum grows as \(O_\theta(\log n)\), yielding the stated covariance asymptotic.

Leckey–Neininger's separate variance theorems give the displayed marginal scales. Positivity of \(v_\theta\) also follows from their nondegenerate second-order internal-path-length limit. Dividing the exact covariance asymptotic by the square root of those variances proves the correlation limit. No joint central limit theorem is claimed or required.

## Verification
The standalone `verify.py` uses exact fractions and enumerates every increasing recursive tree for \(n=2,\dots,9\), at each of the five root weights \(\theta\in\{1/3,1/2,1,2,5\}\). Each tree receives the product of the actual parent-selection probabilities, and its leaf count and depth sum are computed directly from the parent list. The script checked all 231165 weighted tree instances across 40 size-parameter pairs, with 208 exact assertions for the two means, mixed covariance, covariance sign and the \(\theta=1\) benchmark. It returns `VERIFY_OK`. Run `python3 verify.py` with no third-party Python dependencies. The finite verification supplements, but cannot replace, the above infinite analytical argument.

## Relationship to prior work
Leckey and Neininger, *Asymptotic analysis of Hoppe trees* (arXiv:1202.2439), introduce exactly the fixed-root-weight model and separately prove leaf and internal-path-length first and second moments and marginal limit laws (Theorems 2.5–2.7). They do not state the mixed leaf/path-length covariance, strict sign or the parameter-universal leading term.

Hiesmayr and Işlak (arXiv:1712.03572) analyze Hoppe trees and weighted variations, including leaf counts, but do not give this mixed path-length covariance. Lundblad and Wagner, *Path Length and External Path Length in Random Trees* (2026), give a **complete multivariate generating-function equation** that includes leaf count and internal path length for the **uniform** recursive-tree special case \(\theta=1\). That equation implicitly covers moments at \(\theta=1\), even without the simplified formula; this special case is acknowledged and not claimed as independently original. Their model with attachment depending on child count is distinct from a distinguished root having constant exceptional attachment weight, and their results do not imply the stated \(\theta\ne1\) formula or its all-parameter strict sign. Dobrow–Fill (1999) treat the total internal path length of uniform recursive trees; their original full text was not available in this review.

## Limitations
This is an exact two-variable mixed-moment theorem, not a characterization of the full joint law; absence of a nonzero normalized covariance does not establish independence, and no independent validation or historical-priority certification has been performed. Literature priority may be affected by less accessible earlier joint-moment results or general generating functions. Parameters \(\theta\) depending on \(n\) lie outside the theorem. The \(\theta=1\) consequence is covered implicitly by a previously published complete mixed generating function and is used only to check the more general expression.

## References
1. K. Leckey and R. Neininger, *Asymptotic analysis of Hoppe trees*, arXiv:1202.2439v1 (first public 2012-02-11), https://arxiv.org/abs/1202.2439 .
2. E. Hiesmayr and Ü. Işlak, *Asymptotic results on Hoppe trees and its variations*, arXiv:1712.03572v1, https://arxiv.org/abs/1712.03572 .
3. J. Lundblad and S. Wagner, *Path Length and External Path Length in Random Trees*, AofA 2026, DOI:10.4230/LIPIcs.AofA.2026.2, https://doi.org/10.4230/LIPIcs.AofA.2026.2 .
4. R. P. Dobrow and J. A. Fill, *Total Path Length for Random Recursive Trees*, Combinatorics, Probability and Computing 8 (1999), 317–333, DOI:10.1017/S0963548399003855 .

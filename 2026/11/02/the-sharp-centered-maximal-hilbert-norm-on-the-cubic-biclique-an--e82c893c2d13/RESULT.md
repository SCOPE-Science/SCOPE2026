# The sharp centered maximal Hilbert norm on the cubic biclique and a balanced-family lower law

## Finding

Let \(M_G\) be the centered Hardy–Littlewood maximal operator on a finite unweighted graph with counting measure, defined by
\[
(M_Gf)(v)=\max_{r\in\{0,1,\ldots,\operatorname{diam}G\}}\frac{1}{|B(v,r)|}\sum_{w\in B(v,r)}|f(w)|.
\]
For the complete bipartite graph \(K_{3,3}\), the exact strong Hilbert-space operator norm is
\[
\boxed{\|M_{K_{3,3}}\|_{\ell^2\to\ell^2}=\frac{\sqrt{13+3\sqrt{17}}}{4}=1.25919907274557\ldots.}
\]
Every nonzero real-valued extremizer has, up to a positive scalar, independent coordinatewise signs, and graph automorphisms, absolute-value vector
\[
\boxed{(\sqrt{17}-4,\sqrt{17}-4,\sqrt{17}-4,1,1,1).}
\]
There are precisely two labeled nonnegative extremizing rays, one with the smaller value on each of the two color classes.

For every integer \(r\ge2\), the related balanced biclique has the **attained lower bound**
\[
\boxed{\|M_{K_{r,r}}\|_{\ell^2\to\ell^2}\ge B_r:=\frac{\sqrt{r^2+r+1+r\sqrt{r^2+2r+2}}}{r+1}.}
\]
The numbers \(B_r\) increase strictly and converge to \(\sqrt2\). Equality with this lower bound is established here for \(r=3\) only; the \(r=2\) equality is the previously known four-cycle case. No full-norm assertion is made for \(r\ge4\).

## Assumptions and scope

All graph edges have unit length and the graph metric is shortest-path distance. Balls are centered at the evaluation vertex, with all vertices counted equally. The input is any nonzero real function on the six vertices, and the output is the maximal average of its absolute values. The norm is the usual unnormalized \(\ell^2\) norm; the same quotient results under normalized counting measure. The two classes of \(K_{3,3}\) are labeled \(\{0,1,2\}\) and \(\{3,4,5\}\). Other exponents, edge weights, and uncentered balls are not included.

## Proof

**1. Exact ball selection.** Every vertex of \(K_{3,3}\) has three centered balls: itself (radius zero), itself together with the opposite color class (radius one, four vertices), and the whole graph (radius two, six vertices). For each choice vector \(s\in\{0,1,2\}^{6}\), let \(A_s\) be the six-by-six matrix whose \(i\)-th row is the normalized indicator of the ball selected by \(s_i\) at vertex \(i\). Every \(A_s\) is nonnegative and row-stochastic. Thus for \(x=|f|\ge0\),
\[
\|M_Gf\|_2^2=\max_s\|A_sx\|_2^2,
\qquad
\|M_G\|_{2\to2}^2=\max_s\lambda_{\max}(A_s^{\mathsf T}A_s).
\]
The second identity follows because the Perron eigenvector of the entrywise nonnegative Gram matrix may be chosen nonnegative; maximization and the finite maximum commute. In particular, there are exactly \(3^6=729\) raw selections and no unexamined ball radius.

**2. Exhaustive exact upper bound.** Permuting the three vertices within either color class and exchanging the two classes conjugates selection matrices by graph automorphisms and leaves their singular values unchanged. A selection is therefore represented by two sorted triples in \(\{0,1,2\}\), considered as an unordered pair. There are exactly
\[
\binom{5}{3}=10\quad\text{sorted triples},\qquad \binom{10+1}{2}=55\quad\text{representatives}.
\]
For all but the representative \(((0,0,0),(1,1,1))\), the rational symmetric matrix
\[
H_s=\frac{39}{25}I_6-A_s^{\mathsf T}A_s
\]
is positive definite. An exact Sylvester-principal-minor computation over the 54 representatives gives the following **minimum leading principal minors**, ordered by their size from one to six:
\[
\frac{1141}{3600},\quad\frac{1631}{22500},\quad\frac{2989}{93750},\quad
\frac{12691}{390625},\quad\frac{357749}{9765625},\quad
\frac{7529536}{244140625}.
\]
All are strictly positive. The included standalone `verify_k33.py` constructs every rational ball row directly from the graph, enumerates every representative, recomputes these six exact minima, and independently checks all 729 raw choices. Its complete finite loop, rational determinant elimination, and hardcoded expected minima constitute a reproducible finite certificate, rather than a floating-point experiment. Hence all nonexceptional selections have squared operator norm **strictly less** than \(39/25\).

**3. Exceptional spectrum.** For the remaining selection, one color class uses the singleton ball at every vertex and the other uses the radius-one ball at every vertex. On the two class-constant coordinates, its averaging action, after ordering the small-value class first, is
\[
S=\begin{pmatrix}1/4&3/4\\0&1\end{pmatrix}.
\]
The two transverse mean-zero directions in the radius-one class have squared singular value \(1/16\), while the two transverse directions in the singleton class have squared singular value \(1\). The remaining squared singular values are the roots of
\[
16z^2-26z+1=0,
\]
namely \((13\pm3\sqrt{17})/16\). The larger root
\[
\lambda_*:=\frac{13+3\sqrt{17}}{16}
\]
is simple and exceeds \(39/25\), since \(\sqrt{17}>4\) implies \(\lambda_*>25/16>39/25\). The exchanged-class selection has the same spectrum. This proves the exact norm.

**4. Attainment and all equality cases.** Put \(t=\sqrt{17}-4\in(0,1)\). On the smaller-valued class, the radius-one average \((t+3)/4\) strictly exceeds both the singleton value \(t\) and the whole-graph average \((t+1)/2\). On the larger-valued class, the singleton value \(1\) strictly dominates both other averages. Moreover the positive vector \((t,1)\) is an eigenvector of \(S^{\mathsf T}S\) at eigenvalue \(\lambda_*\), because \(t=1/(4+\sqrt{17})\). Hence the displayed six-coordinate input realizes the norm. All other selections lie strictly below \(39/25<\lambda_*\), and the exceptional top singular value is simple. Thus every nonnegative norming input lies on one of the two stated rays. As \(M_Gf=M_G|f|\), independently changing input signs preserves and exhausts the real extremizers.

**5. The all-order balanced-biclique bound.** Fix \(r\ge2\) and an input constant \(a\) on one class and \(b\) on the other, with \(0<a<b\). The maximal values are \((a+rb)/(r+1)\) on the small class and \(b\) on the large class. Thus its squared norm quotient is exactly the Rayleigh quotient of
\[
S_r=\begin{pmatrix}1/(r+1)&r/(r+1)\\0&1\end{pmatrix}.
\]
The largest eigenvalue of \(S_r^{\mathsf T}S_r\) is
\[
\lambda_r=\frac{r^2+r+1+r\sqrt{r^2+2r+2}}{(r+1)^2}.
\]
Its positive top eigenvector has \(0<a<b\): the eigenvalue exceeds one (test \(a=0\)), whereas \(a\ge b\) would make the Rayleigh quotient at most one. This proves the **attained lower bound** \(B_r=\sqrt{\lambda_r}\). For that top vector, increasing \(r\) strictly raises \((a+rb)/(r+1)\) while leaving \(b\) and the input quotient denominator unchanged; hence \(B_r\) is strictly increasing. As \(S_r\to\begin{psmallmatrix}0&1\\0&1\end{psmallmatrix}\), one has \(B_r\to\sqrt2\). This last statement is a limit **of proved lower bounds**, not a claim about the limit of the full operator norms.

## Verification

Run `python3 verify_k33.py` with a standard Python 3 installation. It uses only the standard library and prints `CERTIFICATE_OK canonical=55 strict=54 raw=729 winning_raw=2` after exact rational checks. It also prints the six principal-minor minima. The proof is the fully enumerated finite rational certificate together with the analytic two-dimensional eigenvalue and ball-activity arguments, not numerical sampling.

## Relationship to prior work

Soria and Tradacete initiated sharp maximal inequalities on finite graphs and obtained sharp results for \(0<p\le1\) and bounds at larger exponents, but their inspected paper does not give the strong \(\ell^2\) constant of \(K_{3,3}\). González-Riquelme and Madrid established exact strong \(\ell^2\) norms for complete graphs and stars, not for this cubic complete bipartite graph. Their subsequent paper continues the complete-graph and star analysis. Earlier strong-\(\ell^2\) results for the four-cycle and five-cycle involve different graph geometries and do not imply the cubic-biclique constant; \(K_{2,2}\cong C_4\), so the lower bound's equality at \(r=2\) is explicitly treated as known, not as an additional original result. No stronger inspected primary result or equivalent indexed formula was identified. An earlier unindexed calculation remains possible.

## Limitations

Exact sharpness of \(B_r\) as the **full** strong \(\ell^2\) norm is **not** proved for any \(r\ge4\). No claim is made for unbalanced bicliques, weighted vertices, uncentered maximal averages, other exponents, or infinite graphs. The originality assessment is not a proof of publication priority; independent external mathematical review remains outstanding.

## References

1. J. Soria and P. Tradacete, *Best constants for the Hardy–Littlewood maximal operator on finite graphs*, first publicly posted October 22, 2014, arXiv:1410.6204, https://arxiv.org/abs/1410.6204 .
2. C. González-Riquelme and J. Madrid, *Sharp Inequalities for maximal operators on finite graphs*, first publicly posted May 6, 2020, arXiv:2005.03146, https://arxiv.org/abs/2005.03146 .
3. C. González-Riquelme and J. Madrid, *Sharp inequalities for maximal operators on finite graphs, II*, first publicly posted November 5, 2020, arXiv:2011.02630, https://arxiv.org/abs/2011.02630 .

# Exact endpoint Hodge norms and the rim–rung transition on circular ladders

## Finding

For every integer \(n\ge3\), consider the unweighted prism (circular-ladder) graph \(G_n=C_n\square K_2\). In its real edge-coordinate space let \(Q_n\) be the Euclidean-orthogonal projection onto the cut space and \(C_n=I-Q_n\) the projection onto the cycle space. The endpoint operator norms are exactly described below, and the same values hold on \(\ell_1\) and \(\ell_\infty\).

Put \(\rho=2-\sqrt3\), \(d_n(i)=\min(i,n-i)\) for \(0\le i<n\), and
\[
 h_{n,i}=\frac{\rho^{d_n(i)}+\rho^{n-d_n(i)}}{\sqrt3(1-\rho^n)},\qquad
 a_n=h_{n,0},\qquad b_n=h_{n,\lfloor n/2\rfloor},\qquad
 t_n=\sum_{i=1}^{n-1}\left(\frac1n-h_{n,i}\right)_+.
\]
Here \((x)_+=\max(x,0)\). The four absolute-column sums associated with the two edge orbits (rim edges \(R\), rungs \(V\)) are
\[
\begin{aligned}
 q_R(n)&=2-\frac1n-b_n+t_n,&q_V(n)&=1+2(a_n-b_n),\\
 c_R(n)&=1+a_n-b_n+t_n,&c_V(n)&=2-2b_n.
\end{aligned}
\]
In particular,
\[
 \|Q_n\|_{1\to1}=\|Q_n\|_{\infty\to\infty}
 =\begin{cases}\frac95,&n=3,\\q_R(n),&n\ge4,\end{cases}
 \qquad
 \|C_n\|_{1\to1}=\|C_n\|_{\infty\to\infty}=c_R(n).
\]
The cut norm is attained on rungs only when \(n=3\), both orbit types tie when \(n=4\), and the rim strictly wins when \(n\ge5\). The cycle norm is attained on rims only when \(n=3\) or \(n\ge5\), with both orbit types tying when \(n=4\). For every \(n\ge3\), \(\|Q_n\|_{1\to1}>\|C_n\|_{1\to1}\).

As \(n\to\infty\), with natural logarithms,
\[
 \|Q_n\|_{1\to1}=3-\frac{2\log n}{n\log(2+\sqrt3)}+O(n^{-1}),\qquad
 \|C_n\|_{1\to1}=2+\frac1{\sqrt3}-\frac{2\log n}{n\log(2+\sqrt3)}+O(n^{-1}).
\]
Thus the full finite-size endpoint norms and the sharp logarithmic corrections are determined by the same decaying cyclic Green kernel, while the maximizing edge orbit undergoes a genuine transition at the square prism.

## Assumptions and scope

The graph has vertices \((i,s)\) with \(i\in\mathbb Z/n\mathbb Z\), \(s\in\{0,1\}\), and edges \((i,s)(i+1,s)\) (rims) and \((i,0)(i,1)\) (rungs), each of conductance one. Arbitrarily orient its \(3n\) edges and write the incidence matrix as \(B\), with one \(+1\) and one \(-1\) per column. Then \(L=BB^{\mathsf T}\) and \(Q_n=B^{\mathsf T}L^+B\). Orientation changes conjugate the projections by coordinate signs and therefore do not affect their endpoint norms. No minimum-norm assertion over nonorthogonal projections is made.

## Proof

**Step 1: cyclic Green function.** Let \(L_n\) be the combinatorial Laplacian on \(C_n\). The unique vector \(h\) solving
\[
 (L_n+2I)h=2\delta_0
\]
is strictly positive, sums to one, and is explicitly \(h_i=h_{n,i}\) as displayed in the finding. Indeed, \(\rho+\rho^{-1}=4\) solves the homogeneous recurrence and the value at zero gives the required point source. For \(0\le d\le\lfloor n/2\rfloor\), the values \(h_d\) decrease with \(d\); the cyclic variation is
\[
 \sum_{i=0}^{n-1}|h_i-h_{i-1}|=2(a_n-b_n).
\]
The minimum is \(b_n\), including the adjacent two minimum sites when \(n\) is odd.

**Step 2: source at a rung.** Inject one unit at \((0,0)\) and extract one at \((0,1)\). Decomposing the two layers into their symmetric and antisymmetric components gives potentials \(h_i/2\) on the upper layer and \(-h_i/2\) on the lower layer. Thus rung currents are \(h_i\), and the absolute sum of currents in the two rim layers is \(\sum_i|h_i-h_{i+1}|\). As \(\sum_i h_i=1\), the absolute cut-projection column sum at a rung is \(q_V(n)=1+2(a_n-b_n)\). Its diagonal entry is \(a_n\).

**Step 3: source at a rim.** Inject at \((0,0)\) and extract at \((1,0)\). Split its potential into a layer-symmetric part \(u/2\) and a layer-antisymmetric part \(v/2\). The one-cycle gradients \(A_i=u_i-u_{i+1}\) are \(1-1/n\) for \(i=0\), and \(-1/n\) otherwise. The antisymmetric component is \(v_i=(h_i-h_{i-1})/2\), with gradient \(D_i=v_i-v_{i+1}=\mathbf1_{\{i=0\}}-h_i\). The two rim currents at position \(i\) are \((A_i+D_i)/2\) and \((A_i-D_i)/2\). Since
\[
 \frac{|A_i+D_i|+|A_i-D_i|}{2}=\max(|A_i|,|D_i|),
\]
the absolute rim-current contribution equals \(1-1/n+\sum_{i=1}^{n-1}\max(1/n,h_i)\); here \(a_n>1/n\) ensures the stated value at \(i=0\). The total absolute rung-current contribution is \(\frac12\sum_i|h_i-h_{i-1}|=a_n-b_n\). Using \(\sum_i h_i=1\) produces
\[
 q_R(n)=2-\frac1n-b_n+\sum_{i=1}^{n-1}\left(\frac1n-h_i\right)_+.
\]
Its diagonal entry is \(Q_{e,e}=1-(1/n+a_n)/2\).

**Step 4: complementary projection.** For every Euclidean orthogonal projection \(Q\), \(0\le Q_{e,e}\le1\) and
\[
 \|(I-Q)e\|_1=\|Qe\|_1+1-2Q_{e,e}.
\]
Apply this to the two edge orbits and the diagonal entries from Steps 2–3 to obtain \(c_R(n)\) and \(c_V(n)\). Since both \(Q_n\) and \(C_n\) are symmetric matrices, each one's maximum absolute row sum equals its maximum absolute column sum, proving the equality of the two endpoint operator norms.

**Step 5: exact orbit classification.** Direct subtraction gives
\[
 q_R-q_V=1-\frac1n+b_n-2a_n+t_n,
 \qquad c_R-c_V=-1+a_n+b_n+t_n.
\]
The first differences for \(n=3,4,5,6,7,8,9,10,11\) respectively are
\[
 -\frac1{15},\quad0,\quad\frac7{95},\quad\frac19,\quad\frac{87}{497},\quad\frac5{21},\quad\frac{139}{477},\quad\frac{1046}{3135},\quad\frac{4019}{10879},
\]
and the second differences are
\[
 \frac1{15},\quad0,\quad\frac1{95},\quad\frac1{90},\quad\frac{25}{497},\quad\frac2{21},\quad\frac{107}{795},\quad\frac{1039}{6270},\quad\frac{91}{473}.
\]
These fractions follow by solving the integer cyclic system in Step 1 (or by substituting the geometric formula). For all \(n\ge12\), there are \(n-5\) vertices at cyclic distance at least three from zero. Since \(0<\rho<268/1000\), \(\sqrt3>1732/1000\),
\[
 \sum_{d_n(i)\ge3} h_i
 \le\frac{4\rho^3}{\sqrt3(1-\rho)(1-\rho^{12})}
 <\frac{61}{1000},
\]
so \(t_n\ge1-5/n-61/1000\). Also \(1/\sqrt3\le a_n<29/50\). Therefore
\[
 c_R-c_V>\frac1{\sqrt3}-\frac5{12}-\frac{61}{1000}>0,
 \qquad q_R-q_V>2-\frac6{12}-\frac{58}{50}-\frac{61}{1000}>0.
\]
This completes the all-parameter orbit classification. Finally \(q_R-c_R=1-1/n-a_n\). For \(n\ge5\), monotonicity of \(a_n\) and \(a_5=11/19\) make this difference at least \(21/95>0\). For \(n=3\), the two norms are \(9/5\) and \(5/3\); for \(n=4\), they are \(2\) and \(11/6\). This proves strict cut dominance.

**Step 6: the logarithmic correction.** Since \(h_{n,i}\) decays geometrically in the cyclic distance \(d_n(i)\), its exceedance set \(S_n=\{1\le i<n:h_{n,i}\ge1/n\}\) satisfies
\[
 |S_n|=\frac{2\log n}{\log(2+\sqrt3)}+O(1).
\]
The total kernel mass outside \(S_n\cup\{0\}\) is \(O(1/n)\) by a geometric-series bound beginning at the threshold distance. Hence
\[
 t_n=1-\frac{1+|S_n|}{n}+O(n^{-1})
 =1-\frac{2\log n}{n\log(2+\sqrt3)}+O(n^{-1}).
\]
As \(a_n=1/\sqrt3+O(\rho^n)\) and \(b_n=O(\rho^{n/2})\), substitution into \(q_R\) and \(c_R\) yields the asymptotic statements.

## Verification

The standalone pure-standard-library program `verify_prism.py` builds each finite incidence matrix, inverts a grounded Laplacian using exact fractions, reconstructs every projection column, and compares both orbit columns with an independent inverse of \(L_n+2I\). Running `python3 verify_prism.py` gives `PASS: sizes 3..18; all 504 edge columns; exact rational identities, orbit comparisons, cut dominance`. This independently checks \(504\) edge columns across \(16\) graph sizes. The finite computation verifies those instances only; the proofs above establish all integers \(n\ge3\), the sharp transition, and the asymptotic law.

## Relationship to prior work

The cycle/cut projection framework follows Dilworth, Kutzarova, and Ostrovskii (2023), whose detailed explicit norm calculations concern discrete tori and Hamming graphs rather than the unequal-factor product \(C_n\square K_2\) in general. Their cube calculation includes the particular square prism \(C_4\square K_2\), whose values \(2\) and \(11/6\) are therefore a known special case, not a new claim. Cinkir (2017) gives effective resistances and the Kirchhoff index for prism graphs; these are important background electrical data, not claimed as new here. The added result is the absolute-current evaluation of two operator norms, the exact competing edge-orbit inequalities, and their logarithmic finite-size correction. A 2023 paper by Raza and collaborators treats spectra and other network indices of generalized prism graphs, without an explicit norm comparison in its available abstract. The complete text of Cinkir's article could not be checked, so a prior equivalent absolute-current formulation remains a bibliographic risk.

## Limitations

All graphs are finite, simple, unweighted circular ladders with \(n\ge3\); no arbitrary edge weights, general Cartesian products, or unrestricted minimum-norm projections are covered. The sum defining \(t_n\) is finite and exact, but involves a positive-part threshold rather than one rational expression without cases. The logarithmic statement has an \(O(n^{-1})\) remainder, without its oscillatory next-order term. Independent mathematical validation has not been performed. The inaccessible full text of the 2017 prism-resistance source leaves a residual originality risk.

## References

1. Stephen J. Dilworth, Denka Kutzarova, Mikhail I. Ostrovskii, *Cycle spaces: invariant projections and applications to transportation cost*, arXiv:2305.12582 (first public preprint 2023-05-21), especially Sections 1.1, 1.4 and 2.1–2.7.
2. Zubeyir Cinkir, *Effective Resistances and Kirchhoff index of Prism Graphs*, arXiv:1704.03429 (first public preprint 2017-04-11). Abstract verified; complete article not available for close comparison.
3. Ali Raza, Mobeen Munir, Tasawar Abbas, Sayed M. Eldin, Ilyas Khan, *Spectrum of prism graph and relation with network related quantities*, AIMS Mathematics 8 (2023), 2634–2647, DOI:10.3934/math.2023137. Article metadata and abstract consulted.

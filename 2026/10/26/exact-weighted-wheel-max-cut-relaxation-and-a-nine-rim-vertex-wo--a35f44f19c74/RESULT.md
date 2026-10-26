# Exact weighted-wheel Max-Cut relaxation and a nine-rim-vertex worst-gap switch

## Finding
For every weighted wheel with uniform spoke weight \(t\ge0\), the basic Max-Cut semidefinite relaxation and the integer maximum cut admit elementary closed forms. Their exactness sets and the unique worst multiplicative integrality-gap parameter are completely classified. Unexpectedly, among odd wheel rims, the worst spoke weight changes from \(t=0\) for lengths \(3,5,7\) to \(t=2\) for every length at least \(9\).

Let \(n\ge3\) be an integer, and put
\[
c_n=\begin{cases}1,&n\text{ even},\\\cos(\pi/n),&n\text{ odd},\end{cases}\qquad T_n=2(1+c_n).
\]
Then the optimal values are
\[
\boxed{\operatorname{SDP}_n(t)=\begin{cases}
\frac n2\left(1+t+c_n+\frac{t^2}{4(1+c_n)}\right),&0\le t\le T_n,\\
nt,&t\ge T_n,
\end{cases}}
\]
and
\[
\boxed{\operatorname{CUT}_n(t)=\begin{cases}
n+\frac{nt}{2},&n\text{ even},\quad 0\le t\le2,\\
n-1+\frac{(n+1)t}{2},&n\text{ odd},\quad0\le t\le2,\\
nt,&t\ge2.
\end{cases}}
\]
Every boundary value is consistent where the displayed branches meet. The SDP is exact precisely for \(t=0\) or \(t\ge4\) when \(n\) is even, for \(t\ge T_n\) when \(n\ge5\) is odd, and for \(t=1\) or \(t\ge3\) when \(n=3\).

The largest multiplicative ratio \(\operatorname{SDP}_n(t)/\operatorname{CUT}_n(t)\) over all \(t\ge0\), which is defined since \(\operatorname{CUT}_n(t)>0\), has a **unique** maximizing parameter:
\[
t_{\max}(n)=\begin{cases}
0,&n\in\{3,5,7\},\\
2,&n\text{ even or odd with }n\ge9.
\end{cases}
\]
At that parameter the exact peak is
\[
\max_{t\ge0}\frac{\operatorname{SDP}_n(t)}{\operatorname{CUT}_n(t)}=
\begin{cases}
\dfrac{n(1+\cos(\pi/n))}{2(n-1)},&n\in\{3,5,7\},\\
\dfrac98,&n\text{ even},\\
1+\dfrac{\cos^2(\pi/n)}{4(1+\cos(\pi/n))},&n\text{ odd},\ n\ge9.
\end{cases}
\]

## Assumptions and scope
The graph \(W_n(t)\) has a hub indexed by \(\star\), rim vertices indexed cyclically by \(i\in\{0,\ldots,n-1\}\), rim-edge weights exactly one, and hub-to-rim weights exactly \(t\). Zero spoke weight is allowed; it leaves the hub isolated but does not affect either optimum on the rim. A cut assigns signs \(x_\star,x_i\in\{-1,1\}\), and its weight is \(\frac12\sum_{ij\in E}w_{ij}(1-x_ix_j)\). The standard Goemans--Williamson relaxation replaces signs by unit vectors \(v_\star,v_i\) in an arbitrary finite-dimensional Euclidean space and maximizes \(\frac12\sum_{ij\in E}w_{ij}(1-\langle v_i,v_j\rangle)\). The claim is about this **basic SDP**, not a strengthened SDP with triangle or higher-order cut constraints. All graph orders and all stated spoke weights are covered; there is no asymptotic assumption.

## Proof
**1. Universal spectral inequality.** Put \(z=v_\star\) and \(m=n^{-1}\sum_i v_i\); write \(v_i=m+w_i\), where \(\sum_iw_i=0\). The smallest adjacency eigenvalue of \(C_n\) is \(-2c_n\), while its constant eigenvalue is \(2\). Applying the spectral minimum separately to every coordinate of the mean-zero vectors gives
\[
\sum_i\langle w_i,w_{i+1}\rangle\ge -c_n\sum_i\|w_i\|^2.
\]
Since every \(v_i\) is a unit vector, \(\sum_i\|w_i\|^2=n(1-\|m\|^2)\). Therefore
\[
\sum_i\langle v_i,v_{i+1}\rangle\ge n[(1+c_n)\|m\|^2-c_n].
\]
For \(a=\langle z,m\rangle\in[-1,1]\), Cauchy--Schwarz implies \(\|m\|^2\ge a^2\), so including the spokes yields the **unrestricted**, dimension-independent inequality
\[
\sum_i\langle v_i,v_{i+1}\rangle+t\sum_i\langle z,v_i\rangle\ge n[(1+c_n)a^2-c_n+ta].
\]
The right side is minimized over \([-1,1]\) at
\[
a_*=-\min\!\left\{\frac{t}{2(1+c_n)},1\right\}.
\]

**2. Attaining the spectral bound.** Choose orthonormal vectors \(e_0,e_1,e_2\), and let \(z=e_0\). Set \(\theta=\pi\) if \(n\) is even, and \(\theta=\pi-\pi/n\) if \(n\) is odd. Define
\[
v_i=a_*e_0+\sqrt{1-a_*^2}\,[\cos(i\theta)e_1+\sin(i\theta)e_2].
\]
In either parity \(e^{in\theta}=1\), \(\sum_i e^{ii\theta}=0\), and \(\cos\theta=-c_n\). Consequently \(m=a_*e_0\) and every inequality in step 1 is an equality. Subtracting its achieved minimum from the total edge weight \(n(1+t)\), and dividing by two, gives the stated two-branch SDP formula. This construction also proves an optimal Gram matrix exists of rank at most three; no symmetry hypothesis was imposed on competitors.

**3. The integer optimum.** Flip all signs if necessary so the hub has sign \(+1\). If exactly \(k\in\{0,\ldots,n\}\) rim signs are negative, then the cycle has at most \(2\min(k,n-k)\) cut edges, and this upper bound is realized by placing the minority sign in separated alternating positions. The best cut for fixed \(k\) consequently has weight
\[
2\min(k,n-k)+tk.
\]
For \(t<2\), this is maximized at \(k=n/2\) for even \(n\), and at \(k=(n+1)/2\) for odd \(n\); when \(t>2\), it is maximized at \(k=n\). At \(t=2\), the branches agree. This gives the integer formula.

**4. Exactness.** For even \(n\), the difference \(\operatorname{SDP}-\operatorname{CUT}\) is \(nt^2/16\) on \([0,2]\), \(n(t-4)^2/16\) on \([2,4]\), and zero after \(4\). For odd \(n\), on \([2,T_n]\) the difference is
\[
\frac{n(T_n-t)^2}{8(1+c_n)},
\]
and it vanishes for \(t\ge T_n\). On \([0,2]\), the difference is the quadratic
\[
\frac{n t^2}{8(1+c_n)}-\frac t2+\frac{2-n(1-c_n)}2.
\]
Its discriminant equals
\[
\frac{(n-1)[(n-1)-(n+1)c_n]}{4(1+c_n)}.
\]
For odd \(n\ge5\), the strict inequality \(\cos(\pi/n)>1-2/(n+1)\) follows from \(\cos x\ge1-x^2/2\) and \(\pi^2(n+1)<4n^2\) for \(n\ge5\). The discriminant is then negative, so the gap is everywhere positive in this branch. At \(n=3\), the quadratic is exactly \((t-1)^2/4\). These facts prove every claimed exactness set.

**5. Sharp worst-ratio switch.** On \([0,2]\) the ratio has the form \((A+Bt+Ct^2)/(D+Et)\), with \(C,D,E>0\). The numerator of its derivative is \(CEt^2+2CDt+(BD-EA)\), which is strictly increasing on \([0,2]\). Thus this ratio has no strict interior maximum: it attains its maximum only at \(t=0\) or \(t=2\) (unless both endpoints tie). On \([2,T_n]\) the ratio is
\[
1+\frac{(T_n-t)^2}{8(1+c_n)t},
\]
strictly decreasing until \(T_n\); after \(T_n\) the ratio is one. Write \(R_0,R_2\) for the endpoint ratios. For even \(n\), \(R_0=1\) and \(R_2=9/8\). For odd \(n\),
\[
R_0=\frac{n(1+c_n)}{2(n-1)},\qquad R_2=1+\frac{c_n^2}{4(1+c_n)},
\]
and exact subtraction yields
\[
R_0-R_2=\frac{(n+1)c_n^2+4c_n-2(n-2)}{4(1+c_n)(n-1)}.
\]
At every odd \(n\ge9\), the numerator is strictly smaller than its value at \(c_n=1\), namely \(9-n\le0\); hence \(R_2>R_0\). At \(n=3\), direct substitution of \(c_3=1/2\) yields \(R_0>R_2\). At \(n=5\), the exact value \(c_5=(1+\sqrt5)/4>4/5\) yields the same strict inequality. At \(n=7\), \(c_7=\cos(\pi/7)>9/10\) follows, for example, from the alternating Taylor lower bound \(\cos x\ge1-x^2/2+x^4/24-x^6/720\), \(\pi/7<22/49\), and the rational bound \(561126746141/622857924045>9/10\) for the corresponding polynomial at \(22/49\). Substituting \(c_7>9/10\) makes the numerator strictly exceed \(8(9/10)^2+4(9/10)-10=2/25>0\). All comparisons are strict, proving both uniqueness and the seven-to-nine transition.

## Verification
Run \(\texttt{python verification/verify\_wheel.py}\) with Python, NumPy and SymPy installed. The included output records 144 exact brute-force Max-Cut comparisons, 144 explicit-Gram PSD/objective checks, 6,480 independent random feasible-Gram upper comparisons, five exact-rational Gram/eigenvalue/objective comparisons, and discrete ratio checks through rim length 80. These **finite tests do not certify the infinite-family result**; the analytic steps above do. The verification script constructs every test matrix directly rather than reading cached matrices. Exact-rational cases are separately checked symbolically.

## Relationship to prior work
Goemans and Williamson (1995) introduce the canonical unit-vector relaxation, which is the precise baseline optimized here. Laurent and Varvitsiotis (2011), Sections 2–4, study graph Grothendieck constants, graph cycles, and stronger global worst-weight statements for \(K_5\)-minor-free graphs; those results do not give the spoke-weight-specific Max-Cut objective, exactness set, or endpoint maximizer switch for \(W_n(t)\). Ben-Ameur, Glorieux, and Neto (2016), Section 5 and Table 1, **numerically report unweighted wheel cases at \(t=1\)** and introduce a stronger lifted relaxation; that particular parameter slice is therefore not claimed as an undisclosed numerical observation. Their reported table and formulation do not imply the arbitrary-spoke-weight classification or the odd-rim switch for the basic relaxation. Rendl, Rinaldi, and Wiegele (2007) present general Max-Cut SDP/branch-and-bound methods, not this closed-form weighted-wheel theorem.

Delorme and Poljak's (1993) work on eigenvalue bounds for graph classes is an especially relevant earlier possible antecedent: public search text indicates it discusses wheels, but its complete text was not available for material comparison. The precise weighted-wheel equivalence thus carries a genuine residual literature-coverage risk. The theorem is **not** a general graph SDP theorem or a new definition of integrality gap.

## Limitations
The claim concerns nonnegative uniform spoke weights and unit rim weights only; it does not classify arbitrary inhomogeneous wheel weights, strengthened SDP relaxations, or optimization with signed weights. A full-text equivalence comparison with Delorme and Poljak (1993) remains outstanding. The proof is mathematical and the accompanying computation is supporting finite evidence, not an independent proof. No independent mathematical audit is asserted.

## References
1. M. X. Goemans and D. P. Williamson, “Improved Approximation Algorithms for Maximum Cut and Satisfiability Problems Using Semidefinite Programming,” *Journal of the ACM* 42 (1995), 1115–1145. Author-accessible full text: https://math.mit.edu/~goemans/PAPERS/maxcut-jacm.pdf.
2. M. Laurent and A. Varvitsiotis, “Computing the Grothendieck constant of some graph classes,” arXiv:1106.2735v1, publicly posted June 10, 2011. https://arxiv.org/abs/1106.2735; full text https://arxiv.org/html/1106.2735v1.
3. W. Ben-Ameur, A. Glorieux, and J. Neto, “From Graph Orientation to the Unweighted Maximum Cut,” *Computing and Combinatorics* (2016), 370–384, DOI 10.1007/978-3-319-42634-1_30. Author-uploaded complete text: https://www.researchgate.net/publication/305455943_From_Graph_Orientation_to_the_Unweighted_Maximum_Cut.
4. F. Rendl, G. Rinaldi, and A. Wiegele, “Solving Max-Cut to Optimality by Intersecting Semidefinite and Polyhedral Relaxations,” Optimization Online (2007). https://optimization-online.org/wp-content/uploads/2007/05/1659.pdf.
5. C. Delorme and S. Poljak, “The performance of an eigenvalue bound on the max-cut problem in some classes of graphs,” *Discrete Mathematics* 111 (1993), 145–156, DOI 10.1016/0012-365X(93)90151-I. Plausible predecessor; complete text not inspected.

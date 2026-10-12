# Sharp quadratic waiting-time law for quantum transfer across a missing edge

## Finding

Let \(n\ge4\) be an integer. Let \(G_n\) be the simple unweighted complete graph on \(n\) vertices with exactly one edge \(\{u,v\}\) deleted, and let \(A_n\) be its adjacency matrix. For continuous-time adjacency evolution \(U_n(t)=\exp(itA_n)\), define the optimal transfer probability by a deadline \(T\ge0\):
\[
F_n(T)=\max_{0\le t\le T}|\langle v,U_n(t)u\rangle|^2.
\]
Put \(s=n-3\), \(d=\sqrt{(n+1)^2-8}\), \(\alpha=d/s\), and \(w=(d-s)/(2d)>0\). Then the following **explicit lower bound on the optimal infidelity** holds for every \(T\ge0\):
\[
1-F_n(T)\ge \frac{2w}{s^2(1+\alpha^2)(dsT/\pi+d+s)^2}.
\]
There is also a finite, positive constant \(C_n\), depending only on \(n\), such that for every sufficiently large \(T\),
\[
1-F_n(T)\le\frac{C_n}{T^2}.
\]
In particular, for every integer \(n\ge4\), the optimal missed-edge transfer infidelity is \(\Theta_n(T^{-2})\), with a matching time-to-fidelity law \(\Theta_n(\varepsilon^{-1/2})\) as \(\varepsilon\downarrow0\). The existence of pretty good transfer and absence of perfect transfer on this graph family were already established in earlier work; the contribution here is the **sharp quantitative finite-wait exponent and the explicit global lower obstruction**.

## Assumptions and scope

The graph has unit edge weights except for the single absent edge. The Hamiltonian is **adjacency**, not the combinatorial, normalized, or signless Laplacian. Times are real and nonnegative, the source and target are the two endpoints of the missing edge, and \(n\) is fixed when \(T\to\infty\). All implicit constants may depend on \(n\). The theorem does not give an \(n\)-uniform bound, an optimal leading constant, or a bound for arbitrary perturbed edge weights. The case \(n=3\) is excluded, since the graph becomes a three-vertex path with perfect transfer.

## Proof

**1. Exact spectral reduction.** Set \(r=n-2\) and \(s=r-1\). Write the unit vectors
\[
a=(e_u-e_v)/\sqrt2,\qquad b=(e_u+e_v)/\sqrt2,\qquad c=r^{-1/2}\sum_{z\notin\{u,v\}}e_z.
\]
The vector \(a\) has adjacency eigenvalue zero, and \(\operatorname{span}\{b,c\}\) is invariant, with restriction
\[
B=\begin{pmatrix}0&\sqrt{2r}\\\sqrt{2r}&s\end{pmatrix}.
\]
The eigenvalues of \(B\) are \(\lambda_\pm=(s\pm d)/2\), where
\[
d^2=s^2+8r=(n+1)^2-8.
\]
The spectral weights of \(b\) are \(w_+=(d-s)/(2d)=w\) and \(w_-=(d+s)/(2d)=1-w\). Therefore, with
\[
f(t)=w e^{it(s+d)/2}+(1-w)e^{it(s-d)/2},
\]
the exact transfer amplitude is \(\langle v,U_n(t)u\rangle=(f(t)-1)/2\). Notice that \(n^2<d^2<(n+1)^2\) for \(n\ge4\); thus \(d\), and hence \(\alpha\), are irrational.

**2. Relating loss to simultaneous phase errors.** Define
\[
S(t)=w|e^{it(s+d)/2}+1|^2+(1-w)|e^{it(s-d)/2}+1|^2.
\]
Since \(|f(t)|\le1\), elementary expansion gives
\[
1-|\langle v,U_n(t)u\rangle|^2=\frac{S(t)+1-|f(t)|^2}{4},\qquad
0\le1-|f(t)|^2\le S(t).
\]
Consequently \(S(t)/4\le1-|\langle v,U_n(t)u\rangle|^2\le S(t)/2\).

Put \(x=st/(2\pi)\), \(y=dt/(2\pi)=\alpha x\). Choose odd integers \(h_+\) and \(h_-\) nearest to \(x+y\) and \(x-y\), respectively, and put \(k=(h_++h_-)/2\), \(\ell=(h_+-h_-)/2\). Then \(k,\ell\in\mathbb Z\) and \(k+\ell\) is odd. Moreover \(|k-x|\le1\), \(|\ell-y|\le1\). The elementary inequality
\[
|e^{i\pi z}+1|^2\ge4\operatorname{dist}(z,2\mathbb Z+1)^2
\]
yields, with \(D^2=(x-k)^2+(y-\ell)^2\),
\[
S(t)\ge8wD^2,\qquad 1-|\langle v,U_n(t)u\rangle|^2\ge2wD^2.
\]

**3. An arithmetic lower obstruction at every time.** Because \(d\) is irrational and \(k+\ell\) is odd, the nonzero integer \(d^2k^2-s^2\ell^2\) has absolute value at least one. Therefore
\[
1\le |dk-s\ell|\,|dk+s\ell|.
\]
For \(0\le t\le T\), the bounds on \(k\) and \(\ell\) imply
\[
|dk+s\ell|\le \frac{dsT}{\pi}+d+s.
\]
Also, \(\alpha k-\ell=\alpha(k-x)+(y-\ell)\), so Cauchy--Schwarz gives
\[
\sqrt{1+\alpha^2}\,D\ge|\alpha k-\ell|=\frac{|dk-s\ell|}{s}\ge\frac1{s(dsT/\pi+d+s)}.
\]
Combining this with the previous loss inequality proves the explicit lower bound, uniformly for all observation times in the whole interval \([0,T]\). In particular perfect transfer at a finite time is impossible.

**4. Matching upper bound via bounded-type rotations.** The number \(\beta=(\alpha-1)/2\) is a real quadratic irrational. By the classical periodicity theorem for continued fractions, its positive partial quotients are bounded by some finite integer \(B_n\). Let \(q_j\) be consecutive convergent denominators. For every sufficiently large integer \(N\), choose \(j\) so that \(q_j\le N<q_{j+1}\); then \(q_j\ge N/(B_n+1)\). For the convergent \(p_j/q_j\),
\[
\left|\beta-\frac{p_j}{q_j}\right|<\frac1{q_jq_{j+1}}.
\]
Since multiplication by the coprime numerator \(p_j\) permutes the residue classes modulo \(q_j\), one can choose \(1\le k\le q_j\le N\) (nonzero once \(q_j\ge3\)) so that
\[
\operatorname{dist}\bigl(k\beta,\tfrac12+\mathbb Z\bigr)
\le\frac1{2q_j}+\frac1{q_{j+1}}
\le\frac{3(B_n+1)}{2N}.
\]
Choose an integer \(m\) attaining this distance, set \(\ell=k+2m+1\), and observe at time \(t=2\pi k/s\). Then \(x=k\), \(y=\alpha k\), and \(y-\ell=2(k\beta-m-1/2)\). Both phases in the definition of \(S(t)\) are within \(\pi|y-\ell|\) of an odd multiple of \(\pi\). Hence
\[
1-|\langle v,U_n(t)u\rangle|^2
\le\frac{\pi^2}{2}|y-\ell|^2
\le 2\pi^2\operatorname{dist}(k\beta,\tfrac12+\mathbb Z)^2
\le\frac{9\pi^2(B_n+1)^2}{2N^2}.
\]
Taking \(N=\lfloor sT/(2\pi)\rfloor\), for sufficiently large \(T\) this has \(0<t\le T\) and \(N\ge sT/(4\pi)\). Thus one admissible choice is
\[
C_n=\frac{72\pi^4(B_n+1)^2}{s^2}.
\]
The two estimates prove the matching exponent. Finally, their inversion proves the stated optimal waiting-time exponent for any target infidelity \(0<\varepsilon\ll1\).

## Verification

The accompanying standard-library Python program `verify.py` constructs adjacency matrices directly, checks the three-vector invariant subspace exactly for several graph orders, independently compares the matrix-exponential power series with the closed transition amplitude, and tests the explicit lower bound on finite sample times. Its finite tests verify algebra and normalization, not the infinite Diophantine assertion, which is proved above using integer norms and continued fractions. Run `python3 verify.py` in the directory containing this document and the file.

## Relationship to prior work

Kirkland, Monterde and Plosker, *Quantum state transfer between twins in weighted graphs*, arXiv:2201.02720, Theorem 14(2a) and Example 3, **already prove** proper adjacency pretty good transfer (and nonexistence of perfect transfer) between the missing-edge vertices of \(K_n\setminus e\) for all \(n\ge4\). Those qualitative facts are not claimed as novel here. Their discussion does not give the uniform finite-window infidelity exponent proved above.

Coutinho, Baptista, Godsil, Spier and Werner, *Irrational quantum walks*, arXiv:2208.08971, give general exact methods to decide pretty good state transfer and evaluate supremal transfer probabilities. These do not state this fixed-deadline optimal-rate result. Kirkland and Monterde, *Quantum walks on join graphs*, arXiv:2312.06906, study join-graph cospectrality, periodicity and perfect transfer; their introductory missing-edge example refers to a different Laplacian Hamiltonian. The new law applies to the adjacency Hamiltonian. Classical continued-fraction approximation is a key tool, not asserted to be new.

## Limitations

The constants are graph-order dependent; no joint large-order/high-fidelity asymptotic is claimed. The exact leading coefficient and the finer oscillation structure of \(T^2(1-F_n(T))\) are not determined. The source graph's adjacency PGST classification is established prior work, not a new theorem. Although relevant explicit prior statements were compared at the claim level, more general quantitative recurrence theorems under other terminology might cover portions of the rate calculation; this remains a literature risk. No experimental observation or independently conducted review is claimed.

## References

1. S. Kirkland, H. Monterde and S. Plosker, *Quantum state transfer between twins in weighted graphs*, arXiv:2201.02720, Theorem 14 and Example 3, https://arxiv.org/pdf/2201.02720.
2. G. Coutinho, P. F. Baptista, C. Godsil, T. J. Spier and R. Werner, *Irrational quantum walks*, arXiv:2208.08971 (first posted 2022-08-18), https://arxiv.org/pdf/2208.08971.
3. S. Kirkland and H. Monterde, *Quantum walks on join graphs*, arXiv:2312.06906, https://arxiv.org/pdf/2312.06906.
4. The classical Lagrange theorem on periodic simple continued fractions of quadratic irrationals and the standard convergent-approximation inequalities.

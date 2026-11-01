# Binary gear-graph parity dynamics: short-ring Jordan fusion and an exact recurrence census

## Finding

Let \(n\ge3\) be an integer. The gear graph \(G_n\) has a hub \(c\), original rim vertices \(u_i\), and inserted rim vertices \(v_i\), with indices \(i\in\mathbb Z/n\mathbb Z\); its edges are \(cu_i\), \(u_iv_i\), and \(v_iu_{i+1}\). Thus it has \(2n+1\) labelled vertices. Define \(F_n\) on binary configurations by simultaneous open-neighborhood parity, so each vertex receives the XOR of its neighbors.

Put \(e=2^{\nu_2(n)}\). Over \(\mathbb F_2\), write
\[
 H_n(X)=\frac{X^n+1}{(X+1)^e},\qquad
 Q_s(X)=(X^2+1)^s+X^s,\qquad
 h_n(s)=\deg\gcd(H_n,Q_s),
\]
where the degree of the gcd with \(1\) is zero. The **nilpotent Jordan-block lengths** of \(F_n\) over \(\mathbb F_2\), including multiplicities, are precisely
\[
 \mathcal L_n=\begin{cases}
 (1),&n\text{ odd},\\
 (3,1,1),&n\equiv2\pmod4,\\
 (e,e,1),&4\mid n.
 \end{cases}
\]
In particular, the maximal first-entry time into a periodic orbit is \(1\), \(3\), or \(e\), respectively. The binary dimension of the periodic-state space is
\[
 p_n=\begin{cases}2n,&n\text{ odd},\\2n-2e,&n\text{ even}.\end{cases}
\]
The number of configurations whose first periodic entry occurs by time \(j\ge0\) is exactly
\[
 E_n(j)=2^{p_n+\sum_{\ell\in\mathcal L_n}\min(j,\ell)}.
\]
Consequently the number first entering at time \(j\ge1\) is \(E_n(j)-E_n(j-1)\), and exactly \(2^{p_n}\) states are periodic from time zero. If \(n\) is a power of two, the unique periodic configuration is zero and every configuration vanishes after at most \(n\) updates.

For each positive integer \(t\), the exact number of states returning after \(t\) updates is \(2^{f_n(t)}\), where
\[
 f_n(t)=\begin{cases}
 1+h_n(t),&n\text{ odd and }t\text{ odd},\\
 2+2h_n(t/2),&n\text{ odd and }t\text{ even},\\
 h_n(t),&n\text{ even and }t\text{ odd},\\
 2h_n(t/2),&n\text{ even and }t\text{ even}.
 \end{cases}
\]
Thus, for each \(t\ge1\), the exact number of primitive period-\(t\) cycles is
\[
 \frac1t\sum_{d\mid t}\mu(t/d)\,2^{f_n(d)}.
\]
These formulas apply to all integers \(n\ge3\), \(j\ge0\), and \(t\ge1\), with no asymptotic restriction.

For instance, \(G_3\) has \(64\) periodic configurations among \(128\) binary configurations, including \(8\) fixed points and \(28\) primitive two-cycles. On \(G_6\), exactly \(256\) of the \(8192\) configurations are periodic; successive first-entry populations are \(7\cdot256\), \(8\cdot256\), and \(16\cdot256\). On \(G_8\), every configuration reaches zero in at most eight updates.

## Assumptions and scope

Everything is over \(\mathbb F_2\). Graphs are simple and labelled, updates are simultaneous, and the center does not retain its previous state unless contributed by a neighbor (the hub has no loop). An eventual-periodic-entry time is the smallest \(j\ge0\) for which \(F_n^j(x)\) lies on some periodic orbit. For this finite-dimensional linear map, the periodic-state space is the invertible Fitting summand. Jordan blocks refer to the zero-primary part; no assertion is made here about the detailed Jordan decomposition for nonzero eigenvalues beyond the exact fixed-point formula.

## Proof

**1. Polynomial coordinates.** Put \(R=\mathbb F_2[X]/(X^n+1)\), in which \(X\) is invertible. Encode the rim states by \(U(X)=\sum_i u_iX^i\) and \(V(X)=\sum_i v_iX^i\), and let \(J(X)=1+X+\cdots+X^{n-1}\). The update is exactly
\[
 (c,U,V)\longmapsto\bigl(U(1),\ cJ+(1+X)V,\ (1+X^{-1})U\bigr). \tag{1}
\]
Indeed the coefficient at \(X^i\) in the second component is \(c+v_i+v_{i-1}\), while the coefficient in the third component is \(u_i+u_{i+1}\).

**2. A single exceptional local factor.** Write \(n=em\), with \(m\) odd. In characteristic two,
\(X^n+1=(X^m+1)^e=(X+1)^eH_n(X)\), and \(H_n(1)=1\). Chinese remaindering gives
\[
 R\cong R_0\oplus R_1,\quad R_0=\mathbb F_2[t]/(t^e),\quad t=X+1,\quad R_1=\mathbb F_2[X]/(H_n).
\]
As \(J=(X^n+1)/(X+1)\), its \(R_1\)-component is zero. Writing \(X^m+1=(X+1)q(X)\), one has \(q(1)=1\) and \(q(X)^e\equiv1\pmod{t^e}\). Therefore the \(R_0\)-component of \(J\) is exactly \(t^{e-1}\). Evaluation at \(1\) depends only on the \(R_0\) coordinate. Thus the hub couples only to \(R_0\).

**3. Invertible cyclic part.** On \(R_1^2\) the map is represented by
\[
 B=\begin{pmatrix}0&1+X\\1+X^{-1}&0\end{pmatrix},\qquad
 B^2=\phi I,\qquad\phi=(X+1)^2/X.
\]
Both \(X\) and \(X+1\) are units modulo \(H_n\), so \(B\) is invertible. This part has dimension \(2\deg H_n=2(n-e)\).

**4. Exact zero-primary Jordan blocks.** In coordinates \((c,U,V)\in\mathbb F_2\oplus R_0^2\), the remaining map is
\[
 T(c,U,V)=\bigl(U(0),\ tV+ct^{e-1},\ (t/X)U\bigr), \tag{2}
\]
where \(U(0)\) means the constant term in its \(t\)-expansion, equivalently evaluation at \(X=1\). For \(e=1\), this is \((c,U,V)\mapsto(U,c,0)\). The first two coordinates form an invertible swap and the last gives one zero-Jordan block of length one.

Suppose \(e\ge2\). Direct substitution yields
\[
 T^2(c,U,V)=\bigl(0,\ (t^2/X)U+U(0)t^{e-1},\ (t^2/X)V\bigr),\tag{3}
\]
\[
 T^3(c,U,V)=\bigl(0,\ (t^3/X)V,\ (t^3/X^2)U\bigr).\tag{4}
\]
For \(j\ge3\), further iterates have rank \(2\max(e-j,0)\), because they are multiplication by \(t^j\) times units on two copies of \(R_0\). The kernel of \(T\) has dimension three: necessarily \(U\in t^{e-1}R_0\), while \(V=ct^{e-2}+bt^{e-1}\) with arbitrary \(b,c\in\mathbb F_2\). If \(e=2\), equation (3) has rank one and equation (4) vanishes, so the zero-primary partition is \((3,1,1)\). If \(e\ge4\), the first summand of (3) maps onto \(t^2R_0\): the image of \(1\) begins with \(t^2\), while images of \(t,t^2,\ldots\) successively begin with \(t^3,t^4,\ldots\). The second summand also maps onto \(t^2R_0\). Thus \(\operatorname{rank}(T^2)=2(e-2)\). Combined with \(\operatorname{rank}(T)=2e-2\), (4), and \(\dim T=2e+1\), this uniquely yields two Jordan blocks of length \(e\) and one of length one. This proves all three cases; note that \(e\) is a power of two, so \(e\ge4\) is the only remaining even case.

**5. Entry times.** The invertible Fitting summand contributes \(2^{p_n}\) configurations, and each zero-primary block of length \(\ell\) contributes \(2^{\min(j,\ell)}\) vectors annihilated by the \(j\)-th iterate. Multiplying these independent counts proves \(E_n(j)\). The claimed maximal transient lengths follow because the largest blocks exist, not just as upper bounds.

**6. Exact return counts.** On \(R_1^2\), for \(t=2s\), the operator \(B^t+I=(\phi^s+1)I\); multiplying by the unit \(X^s\) shows that its kernel has binary dimension \(2h_n(s)\). For odd \(t=2s+1\), the matrix \(B^t+I\) has a unit off-diagonal entry, and elementary row-column operations over \(R_1\) reduce it to \(\operatorname{diag}(1,1+\phi^{2s+1})\). Its kernel has binary dimension \(h_n(t)\), because \(X^t(1+\phi^t)=Q_t(X)\) and the kernel of multiplication by a polynomial on \(\mathbb F_2[X]/(H_n)\) has dimension \(\deg\gcd(H_n,Q_t)\). The \(R_0\) part gives no periodic fixed vectors for even \(n\). For odd \(n\), its invertible swap has fixed dimension one at odd \(t\) and two at even \(t\). Combining the summands proves the formula for \(f_n(t)\). Standard Möbius inversion on exact primitive periods gives the final cycle count.

## Verification

The standalone script `gear_verify.py` uses only Python's standard library. Running `python3 gear_verify.py` reproduces `gear_verify_output.txt` and prints `VERIFY_OK`. It compares direct binary adjacency-matrix ranks with the predicted nilpotent block ranks for every \(3\le n\le64\), direct fixed-space kernel ranks with the polynomial-gcd formula for each \(1\le t\le32\), and independently enumerates all binary configurations for \(3\le n\le8\) to compare both return counts and first-entry populations. The run passed 2,326 rank checks, 1,984 return-time checks, and enumerated 174,720 configurations. These finite tests corroborate, but do not replace, the infinite-family proof above.

## Relationship to prior work

Martin, Odlyzko and Wolfram developed algebraic state-transition methods for finite one-dimensional cellular automata. Marr and Hütt studied the dependence of binary network automata on graph topology, but their two threshold-density flip rules are not the synchronous neighbor-parity rule here. Berman, Borer and Hungerbühler studied solvability and related linear algebra for Lights Out on arbitrary graphs, where the button-press model is not the autonomous iteration of the open-neighborhood adjacency matrix. Sutner’s earlier σ-game study relates graph games to cellular automata, but its accessible abstract treats graph-game rules and rectangular grids; the unavailable full text remains a specifically acknowledged comparison limit. Standard graph references identify the gear graph with the bipartite wheel and with the Jahangir graph \(J_{2,n}\). The present claim is the gear-specific, all-size zero-primary Jordan classification and exact repeated-return count; generic matrix-based methods do not themselves state these formulas. No claim of a universal novelty guarantee is made.

## Limitations

The result is restricted to the binary field, simple gear graphs, and synchronous open-neighborhood parity. It does not classify primitive-cycle lengths by a closed elementary formula independent of gcd computations, although every exact primitive-cycle count follows from the displayed polynomial formula. Its novelty comparison is limited to the inspected accessible sources and indexed research; differently phrased prior work remains a possibility. No independent external validation is asserted.

## References

- C. Marr and M.-T. Hütt, *Topology regulates pattern formation capacity of binary cellular automata on graphs*, arXiv:cond-mat/0502509v1 (first posted 2005-02-21), https://arxiv.org/abs/cond-mat/0502509.
- O. Martin, A. M. Odlyzko and S. Wolfram, *Algebraic properties of cellular automata*, Communications in Mathematical Physics **93** (1984), 219–258, https://doi.org/10.1007/BF01223745.
- A. Berman, F. Borer and N. Hungerbühler, *Lights Out on graphs*, Mathematische Semesterberichte **68** (2021), 237–255, https://doi.org/10.1007/s00591-021-00297-5.
- K. Sutner, *The σ-Game and Cellular Automata*, American Mathematical Monthly **97** (1990), 24–34, https://doi.org/10.1080/00029890.1990.11995540.
- E. W. Weisstein, *Gear Graph*, Wolfram MathWorld, https://mathworld.wolfram.com/GearGraph.html.

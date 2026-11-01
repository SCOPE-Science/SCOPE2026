# Triangle–pentagon windmills: a complete parity-orbit and entrance-time census

## Finding

Let \(p,q\) be nonnegative integers with \(p+q\ge1\). Construct the simple undirected graph \(G_{p,q}\) by identifying one vertex (the hub) in each of \(p\) separate triangles and \(q\) separate pentagons. Distinct petals have no other common vertices or edges. Thus \(G_{p,q}\) has \(n=1+2p+4q\) labelled vertices. Let \(F:\mathbb F_2^{V(G_{p,q})}\to\mathbb F_2^{V(G_{p,q})}\) be the synchronous **open-neighborhood parity** update, \(F(x)_v=\sum_{w\sim v}x_w\pmod2\), with no self-input.

Put \(\epsilon_r=r\bmod2\in\{0,1\}\), and define
\[
 d_1=p+\epsilon_p,\qquad d_2=2p,\qquad
 d_3=p+2q+\epsilon_p+2\epsilon_q,\qquad d_6=2p+4q.
\]
Then every configuration first enters a periodic orbit at time zero or one. Exactly \(2^{2p+4q}\) configurations are periodic from time zero, and exactly the same number first become periodic at time one. Periodic configurations have primitive periods in \(\{1,2,3,6\}\), with exactly \(2^{d_j}\) configurations fixed by \(F^j\) for \(j\in\{1,2,3,6\}\). Consequently the numbers of distinct primitive temporal orbits are
\[
 Q_1=2^{d_1},\qquad Q_2=\frac{2^{d_2}-2^{d_1}}2,\qquad
 Q_3=\frac{2^{d_3}-2^{d_1}}3,\qquad
 Q_6=\frac{2^{d_6}-2^{d_3}-2^{d_2}+2^{d_1}}6.
\]
All other primitive-orbit counts are zero. In particular, a primitive two-cycle exists exactly for \(p\ge2\), a primitive three-cycle exactly for \(q\ge1\), and a primitive six-cycle exactly when \(q\ge2\) or when \(q=1\) and \(p\ge2\). Thus a triangle–pentagon pair by itself does not support primitive six-cycles, but adding a second pentagon **or** two triangles does. Moreover, **each primitive orbit of length \(d\) has an attraction basin of exactly \(2d\) configurations**: its \(d\) periodic states and exactly one nonperiodic one-step predecessor per periodic state. The exact periodicity, basin, and entrance-time statements hold for **every** labelled state, not just typical states.

For illustration, \((p,q)=(1,1)\) has \((Q_1,Q_2,Q_3,Q_6)=(4,0,20,0)\), whereas \((2,1)\) has \((4,6,20,30)\), and \((0,2)\) has \((1,0,5,40)\).

## Assumptions and scope

All vector operations and sums in the proof are over \(\mathbb F_2\). At each integer time, every vertex updates **simultaneously** using its neighbors' *previous* states. Each triangle and pentagon has a distinct set of nonhub vertices. The hub has degree \(2(p+q)\), and all other vertices have degree two. Parameter values \(p=0\) or \(q=0\) are included, but \(p=q=0\) is excluded. A state has first-periodic-entry time \(T=\min\{t\ge0:F^t(x)\text{ is periodic}\}\); an orbit is counted once, not once per point.

## Proof

**1. Coordinates and invariant base.** Write the hub value as \(h\). The nonhub values in triangle \(i\) are \(u_i,v_i\) along the cycle \(h,u_i,v_i,h\), and put \(\sigma_i=u_i+v_i\). In pentagon \(j\), write \(h,a_j,b_j,c_j,d_j,h\) and set \(s_j=a_j+d_j\), \(t_j=b_j+c_j\). Define the aggregate parities \(U=\sum_i\sigma_i\), \(S=\sum_j s_j\), and \(T=\sum_j t_j\), with empty sums zero. Denote one update by a superscript \(+\). The graph's local rules give
\[
\begin{aligned}
 \sigma_i^+&=\sigma_i,&s_j^+&=t_j,&t_j^+&=s_j+t_j,&h^+&=U+S,\\
 u_i^+&=u_i+\sigma_i+h,&
 \binom{a_j^+}{b_j^+}&=
 \begin{pmatrix}0&1\\1&1\end{pmatrix}\binom{a_j}{b_j}
 +\binom{h}{t_j}.
\end{aligned}
\]
The other values are reconstructed from \(v_i=u_i+\sigma_i\), \(c_j=b_j+t_j\), and \(d_j=a_j+s_j\). The base \((\sigma_i,s_j,t_j)\) returns after three steps: each \(\sigma_i\) is invariant and each \((s_j,t_j)\) is acted on by an order-three matrix. The aggregate sequence is \((U,S,T)\), then \((U,T,S+T)\), then \((U,S+T,S)\), and then the initial triple.

**2. Exact periodic state space.** Let \(A\) be the binary adjacency matrix, so \(F(x)=Ax\). Since each degree is even, the all-ones vector \(\mathbf1\) is in \(\ker A\). In fact \(\ker A=\langle\mathbf1\rangle\): at a triangle, the two nonhub equations \(Ax=0\) force \(u_i=v_i=h\); at a pentagon, the four nonhub equations successively force \(b_j=h\), \(c_j=a_j\), \(d_j=b_j\), and \(c_j=h\), hence all four values equal \(h\). The hub equation then holds automatically. As \(A\) is symmetric,
\[
 \operatorname{im}A=(\ker A)^\perp
 =\{x:h+U+S+T=0\},
\]
the even-total-parity hyperplane, of dimension \(n-1=2p+4q\). In particular, \(F(x)\) lies in this hyperplane for every \(x\).

For a vector in this hyperplane, \(h=U+S+T\). The hub follows \(h^+=U+S\), \(h^{++}=U+T\), \(h^{+++}=U+S+T=h\). Thus every forcing term in the internal triangle and pentagon update equations is three-periodic. The homogeneous matrices acting on these internal variables are \(1\) (for a triangle) and \(B=\left(\begin{smallmatrix}0&1\\1&1\end{smallmatrix}\right)\) (for a pentagon), both of whose cubes are the identity. Over characteristic two, applying two consecutive identical three-step forced blocks cancels the accumulated translation. Hence \(F^6(x)=x\) on \(\operatorname{im}A\). Every point in that hyperplane is therefore periodic from time zero. A point outside the hyperplane is never periodic (any periodic point belongs to \(\operatorname{im}A\)), but its first update is periodic. Both parity classes have size \(2^{n-1}\), proving the entrance-time census. Because \(\ker A=\{0,\mathbf1\}\) and \(n\) is odd, every \(y\in\operatorname{im}A\) has exactly two predecessors, which differ by \(\mathbf1\) and hence have opposite parity. Exactly one predecessor is in the periodic hyperplane, because \(A\) restricts to a bijection there; the other is one-step transient. Each temporal orbit of length \(d\) therefore has exactly \(d\) distinct one-step feeders and an attraction basin of size \(2d\). Equivalently the global matrix identity is \(A^7=A\).

**3. Fixed spaces for the first and second iterates.** For \(F(x)=x\), a pentagon base \((s_j,t_j)\) must be \((0,0)\), because the order-three matrix \(B\) has no nonzero fixed vector. The hub condition on the periodic hyperplane is \(h=U\), and each triangle requires \(\sigma_i=h=U\). Consequently \(U=pU\): an additional binary choice for \(U\) exists exactly when \(p\) is odd. There is one free \(u_i\) per triangle. Each pentagon has its unique forced fixed coordinates \((a_j,b_j,c_j,d_j)=(0,h,h,0)\). Thus \(\dim\ker(F-I)=p+\epsilon_p=d_1\).

For \(F^2(x)=x\), the pentagon base again vanishes, and hence \(h=U\) is constant in time. Every triangle then returns after two updates without a constraint on its two values \((u_i,v_i)\); a pentagon is uniquely forced to \((0,h,h,0)\). This gives \(\dim\ker(F^2-I)=2p=d_2\).

**4. Fixed space for the third iterate.** For every \(x\in\operatorname{im}A\), the coordinate formulas in Step 1 yield the exact three-step differences
\[
 u_i^{+++}+u_i=U+\sigma_i,\qquad
 a_j^{+++}+a_j=S+s_j,\qquad
 b_j^{+++}+b_j=T+t_j.
\]
The base variables are already three-periodic, so these differences vanish exactly when \(\sigma_i=U\) for all triangles and \((s_j,t_j)=(S,T)\) for all pentagons. Summing the equalities imposes \(U=pU\), \(S=qS\), \(T=qT\). There are \(p+2q\) free internal coordinates, an additional \(\epsilon_p\) choice for \(U\), and two additional choices precisely when \(q\) is odd. Therefore \(\dim\ker(F^3-I)=p+2q+\epsilon_p+2\epsilon_q=d_3\). Step 2 gives \(\dim\ker(F^6-I)=n-1=d_6\).

**5. Primitive orbit counts and existence thresholds.** Every primitive period divides six, so Möbius inversion on divisors of six gives the displayed formulas for \(Q_1,Q_2,Q_3,Q_6\). Since \(d_2>d_1\) precisely when \(p\ge2\), two-cycles occur exactly then. Similarly \(d_3>d_1\) precisely when \(q\ge1\). For six-cycles, note that a point is six-periodic but not of period \(1,2,3\) exactly when it lies outside the union of the \(F^2\)- and \(F^3\)-fixed spaces. Their intersection is the \(F\)-fixed space. This union cannot fill the vector space \(\operatorname{im}A\) unless one of those two subspaces equals the whole space. Using the dimensions, \(d_6>d_2\) exactly when \(q\ge1\), and \(d_6>d_3\) exactly when \(q\ge2\) or \(q=1,p\ge2\). This yields the stated sharp six-cycle criterion and completes the proof.

## Verification

Two standalone standard-library implementations give separate finite checks of the theorem, without being used to infer the all-parameter proof. Compile the included `verify.cpp` with `g++ -O2 -std=c++17 -Wall -Wextra -pedantic verify.cpp -o verify` and run `./verify`; compare with `verification_output.txt`. Its direct local-update enumeration checked **827,208 labelled configurations** on **24 complete parameter pairs** with up to 17 vertices; it tested \(F^7(x)=F(x)\), parity of first-periodic entry, the four fixed-space sizes, and integer primitive-orbit counts. Independently run `python3 rank_check.py` and compare with `rank_output.txt`: bit-vector matrix calculations checked **168 parameter pairs** with up to 73 vertices, including the ranks of \(A\), \(A^j-I\) for \(j\in\{1,2,3,6\}\), and \(A^7=A\). These computations corroborate but do not replace the unrestricted algebraic proof.

## Relationship to prior work

Noual, Regnault and Sené (2012) investigate XOR **circulant** Boolean networks, including convergence-time results. The present gluing family is not generally circulant, and their circle results neither enumerate the mixed-petal periodic orbits nor establish its sharp six-cycle criterion. Alcolei, Perrot and Sené (2015) introduce XOR flowers and classify **asynchronous** state-transition graphs; the update order and, in their cycle conventions, the directed interactions differ from the simultaneous undirected neighbor-sum map analyzed here. Aledo, Martínez and Valverde (2015) survey parallel graph dynamical systems, but do not give these orbit counts. Li, Zhang and Wang (2026) derive characteristic-polynomial formulas for Dutch windmill graphs as real spectral objects. A characteristic polynomial does not determine characteristic-two Jordan-block sizes, and the reviewed abstract does not state the present discrete orbit census.

The contribution claimed here is the **two-parameter synchronous dynamical classification**, its mixed-petal orbit counts and exact first-entry law; general linearity, the definition of flower graphs, and characteristic-polynomial methods are established background. Searches cannot rule out equivalent statements in unindexed or inaccessible literature.

## Limitations

The theorem requires exactly triangular or pentagonal undirected petals glued at a single hub, the binary field, no vertex self-input, and fully synchronous updates. It does not assert the same period spectrum for other cycle lengths, directed/asynchronous rules, nonbinary fields, or graphs with additional intersections. The older XOR-flower literature primarily addresses different update conventions. A relevant 2026 spectral paper was inspected at the abstract/metadata level, not line by line in its entire full text; its full content is therefore a residual priority-comparison risk. No independent mathematical audit has been performed.

## References

1. M. Noual, D. Regnault, S. Sené, *Boolean networks synchronism sensitivity and XOR circulant networks convergence time*, public preprint 2012-08-14, arXiv:1208.2767, https://arxiv.org/abs/1208.2767.
2. A. Alcolei, K. Perrot, S. Sené, *On the flora of asynchronous locally non-monotonic Boolean automata networks*, public preprint 2015-10-19, arXiv:1510.05452, https://arxiv.org/abs/1510.05452.
3. J. A. Aledo, S. Martínez, J. C. Valverde, *Parallel Dynamical Systems over Graphs and Related Topics: A Survey*, *Journal of Applied Mathematics* (2015), DOI:10.1155/2015/594294, https://doi.org/10.1155/2015/594294.
4. W. Li, Y. Zhang, Y. Wang, *On the characteristic polynomials of Dutch windmill graphs and their applications*, *AIMS Mathematics* 11 (2026), 16697–16711, DOI:10.3934/math.2026685, https://doi.org/10.3934/math.2026685.

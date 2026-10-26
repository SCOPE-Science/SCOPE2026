# Sharp RK4 positivity on Hamming graphs: a twelve-to-thirteen alphabet transition

## Finding

Let \(H(d,q)=K_q\mathbin{\square}\cdots\mathbin{\square}K_q\) be the unweighted Hamming graph on \([q]^d\), where the number of factors \(d\ge3\) and alphabet size \(q\ge2\) are integers. Let \(L\) be its combinatorial Laplacian, and apply the completed classical four-stage fourth-order Runge–Kutta method to \(u'=-Lu\):
\[
R_4(-hL)=I-hL+\frac{h^2L^2}{2}-\frac{h^3L^3}{6}+\frac{h^4L^4}{24},\qquad h\ge0.
\]
Write \(\Theta=2d(q-1)-3(q-2)>0\) and \(H_3=2/\Theta\). Define the cubic \(F_{d,q}(h)=1-Bh+Ch^2-Eh^3\), with \(m=d-1\) and
\[
\begin{aligned}
B&=m(q-1)+q/2,\\
C&=q^2/6+mq(q-1)+\binom m2(q-1)^2,\\
E&=q^3/24+\frac{7mq^2(q-1)}{12}
  +\frac{3q}{2}\binom m2(q-1)^2
  +\binom m3(q-1)^3.
\end{aligned}
\]
Then the **complete entrywise-positivity interval** is \([0,H_{d,q}]\), where
\[
H_{d,q}=\begin{cases}
H_3,&d\ge4,\quad\text{or }d=3,\ 2\le q\le12,\\
\text{the unique }h\in(0,H_3)\text{ with }F_{3,q}(h)=0,
    &d=3,\ q\ge13.
\end{cases}
\]
At all larger steps at least one entry is negative, with no later return to entrywise nonnegativity. At the first boundary the vanishing entries lie at Hamming distance three in the first regime, and at Hamming distance one in the second regime. There is no integer-alphabet tie between these failure mechanisms. The sharp new alphabet transition is therefore \(q=13\) in dimension three.

For example, \(H_{3,12}=1/18=0.055555\ldots\), whereas \(H_{3,13}=0.0512396000478\ldots < 2/39\). Every \(H_{d,q}\) in this domain strictly exceeds the forward-Euler positivity horizon \(1/[d(q-1)]\). As \(q\to\infty\) with \(d=3\), \(qH_{3,q}\) tends to the unique positive root \(0.6326662515436\ldots\) of \(24-60z+76z^2-65z^3=0\).

## Assumptions and scope

Every edge of the undirected Hamming graph has unit conductance; the Laplacian is unnormalized and the timestep is an endpoint timestep. For \(x,y\in[q]^d\), write \(r=\#\{i:x_i\ne y_i\}\) for Hamming distance. The assertion is that \(R_4(-hL)_{xy}\ge0\) for **all** ordered vertex pairs if and only if the displayed restriction on \(h\) holds. Because \(L\mathbf1=0\), the completed update has row sums one for every \(h\); entrywise nonnegativity therefore means it is a stochastic kernel. Intermediate RK4 stages, nonuniform conductances, dimension one or two, and nonlinear dynamics are outside the theorem.

## Proof

**1. All entries reduce to five distance classes.** On a single clique the exact continuous-time heat-kernel entries are \(a(t)=[1+(q-1)e^{-qt}]/q\) on the diagonal and \(b(t)=[1-e^{-qt}]/q\) off the diagonal. The Cartesian product commutes coordinatewise, hence between vertices at distance \(r\) the exact heat kernel equals \(a(t)^{d-r}b(t)^r\). Its fourth-order Taylor polynomial in \(t\) is the corresponding entry of \(R_4(-tL)\). Write \(e=q-1\). The resulting entries for \(1\le r\le4\) are:
\[
\begin{array}{ll}
r=1:&hF_{d,q}(h),\\
r=2:&h^2G_{d,q}(h),\\
r=3:&h^3(1-h/H_3),\\
r=4:&h^4,
\end{array}
\]
where
\[
G_{d,q}(h)=1-[(d-2)e+q]h+
\left[\frac{7q^2}{12}+\frac{3(d-2)qe}{2}
+\binom{d-2}{2}e^2\right]h^2.
\]
For \(r\ge5\), every entry is identically zero because a polynomial in \(L\) of degree four cannot connect more than four coordinates. When the corresponding distance does not exist, omit that row. All diagonal entries are strictly positive for \(h\ge0\): the scalar polynomial \(R_4(-z)=1-z+z^2/2-z^3/6+z^4/24\) is strictly positive for \(z\ge0\), by the signed Taylor remainder for \(e^{-z}\); spectral resolution of the positive semidefinite \(L\) gives each diagonal as a strictly positive weighted average of such values.

**2. Distance two cannot fail before distance three.** Set \(x=h/H_3\), so \(0\le x\le1\). For a polynomial \(P(x)\) of degree at most \(r\), write its degree-\(r\) Bernstein representation as \(\sum_{j=0}^r\binom rj\beta_j x^j(1-x)^{r-j}\). Every Bernstein basis term is nonnegative on this interval. Set \(D=d-3\ge0\), \(Q=q-2\ge0\), and \(T=\Theta\). The three Bernstein coefficients of \(G_{d,q}(H_3x)\) are \(1\), \((DQ+D+Q+3)/T\), and
\[
\frac{2(3D^2Q^2+6D^2Q+3D^2+9DQ^2+30DQ+21D+8Q^2+32Q+32)}{3T^2},
\]
all strictly positive. Consequently every distance-two entry is positive when \(0<h\le H_3\).

**3. The exact distance-one sign and its transition.** The four Bernstein coefficients of \(F_{d,q}(H_3x)\) begin with
\[
\begin{split}
\beta_0&=1,\\
\beta_1&=\frac{4(DQ+D+Q+3)}{3T},\\
\beta_2&=\frac{18D^2Q^2+36D^2Q+18D^2+42DQ^2+156DQ+114D+29Q^2+140Q+176}{9T^2}.
\end{split}
\]
Thus the first three are strictly positive for every allowed parameter. The last coefficient \(\beta_3=F_{d,q}(H_3)\) is, for \(d=3\),
\[
\beta_3=\frac{64-5q}{81q}.
\]
It is positive exactly for integral \(2\le q\le12\), and negative exactly for integral \(q\ge13\). For \(d\ge4\), write \(E_0=d-4\ge0\) and \(Q=q-2\ge0\). A completely positive polynomial certificate for \(\beta_3\) is
\[
\beta_3=\frac{N(E_0,Q)}{3T^3},
\]
\[
\begin{aligned}
N(E_0,Q)={}&8E_0^3(Q+1)^3+48E_0^2(Q+1)^2(Q+2)\\
&+2E_0(Q+1)(5Q+12)(9Q+16)\\
&+(Q+2)(45Q^2+242Q+256)>0.
\end{aligned}
\]
Therefore the first regime has \(F_{d,q}(h)>0\) for \(0\le h\le H_3\). In the second regime (\(d=3,q\ge13\)), \(\beta_3<0\). Substituting \(x=y/(1+y)\) gives the polynomial \(\beta_0+3\beta_1y+3\beta_2y^2+\beta_3y^3\), whose coefficient signs have exactly one variation. Descartes' rule, together with its positive constant and negative leading coefficient, yields one and only one root \(y>0\), hence a unique first distance-one zero \(0<h<H_3\), with negative distance-one entries between this root and \(H_3\).

**4. Sharpness and no reentry.** The distance-three expression is nonnegative precisely until \(H_3\); for every \(h>H_3\) it is strictly negative. All other entries stay nonnegative up to the stated boundary by steps 1–3. If \(d=3,q\ge13\), the distance-one entry is already negative between its unique root and \(H_3\). This proves the complete if-and-only-if classification, endpoint inclusion, the active zero classes, and absence of later positivity reentry.

The forward-Euler horizon is \(1/[d(q-1)]\). Since \(H_3>1/[d(q-1)]\) and the distance-one entry at \(h=1/[d(q-1)]\) is strictly positive by the adjacency-polynomial expansion of \(R_4(-hL)\), the smaller distance-one root in the exceptional regime is also beyond the Euler horizon. To see the last assertion directly, with \(k=d(q-1)\), expand \(R_4(h(A-kI))\) in nonnegative powers of the adjacency matrix: the coefficients of \(A,A^2,A^3,A^4\) are respectively \(h(1-kh+(kh)^2/2-(kh)^3/6)\), \(h^2(1-kh+(kh)^2/2)/2\), \(h^3(1-kh)/6\), and \(h^4/24\), strictly positive for \(0<h\le1/k\). Thus the distance-one entry is strictly positive at Euler's boundary.

Finally, putting \(z=qh\) in the \(d=3\) cubic and taking coefficientwise limits as \(q\to\infty\) gives \(1-5z/2+19z^2/6-65z^3/24\), whose derivative has negative discriminant and is strictly negative. Its unique positive zero is the displayed asymptotic constant.

## Verification

The included `verify_hamming_rk4.py` needs Python and SymPy (`requirements.txt`). Run `python verify_hamming_rk4.py`. It checks the four nonzero off-diagonal Hamming-distance Taylor identities symbolically, verifies the Bernstein certificates and transition factorization exactly, and compares independent sparse-generator powers with the formulas for 32,118 off-diagonal rational transition entries on selected graphs and timesteps (including sizes on both sides of the transition). The checked range is finite; the universally quantified theorem is established by the preceding exact polynomial proof. The checker was executed successfully from its included source bytes.

## Relationship to prior work

Classical SSP Runge–Kutta theory studies uniform sufficient monotonicity restrictions across classes of semidiscrete operators and distinguishes endpoint and internal-stage behavior [1–3]. The 2001 and 2003 primary papers include forward-Euler-based constraints and higher-order stability criteria, not this complete exact Hamming-graph endpoint classification. The 2014 preprint develops other explicit SSP schemes with high linear order and does not derive the particular family-specific fourth-order Taylor endpoint's \(q=13\) switch. Previously studied path/cycle, weighted-star, and complete-multipartite RK4 endpoint classifications concern other graph families and do not imply the Hamming graph's distance-one versus distance-three transition. The tensor-product heat kernel itself is elementary and **not** asserted novel; the substantive claim is the sharp uniform sign classification for all dimensions and alphabets, including the exceptional cutoff.

## Limitations

The theorem does not describe intermediate RK4 stage positivity, all graph Laplacians, nonunit conductances, dimensions one or two, nonlinear diffusion, or temporal error tolerances. A specialized equivalent Hamming-network numerical-positivity theorem could have escaped the literature searches; independent historical review has not been carried out. The result is a self-reviewed mathematical statement rather than an independently certified publication.

## References

1. S. Gottlieb, C.-W. Shu and E. Tadmor, *Strong Stability-Preserving High-Order Time Discretization Methods*, SIAM Review 43 (2001), 89–112. First public electronically 2001-02-02. DOI: 10.1137/S003614450036757X. Author full text: https://www.math.umd.edu/~tadmor/pub/linear-stability/Gottlieb-Shu-Tadmor.SIREV-01.pdf.
2. S. Gottlieb and L.-A. J. Gottlieb, *Strong Stability Preserving Properties of Runge–Kutta Time Discretization Methods for Linear Constant Coefficient Operators*, Journal of Scientific Computing 18 (2003), 83–109. DOI: 10.1023/A:1020338228736. Author full text: https://www.cfm.brown.edu/people/sg/SGmcg1.pdf (article within compiled PDF, printed pp. 83–109).
3. S. Gottlieb, Z. Grant and D. Higgs, *Optimal Explicit Strong Stability Preserving Runge–Kutta Methods with High Linear Order and Optimal Nonlinear Order*, arXiv:1403.6519 (first posted 2014-03-25); subsequently Mathematics of Computation. https://arxiv.org/pdf/1403.6519.

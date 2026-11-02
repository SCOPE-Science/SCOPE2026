# Three disjoint positivity windows for two-stage Radau IIA on star networks

## Finding

Let \(m\ge 2\) be an integer. Let \(L_m\) be the combinatorial Laplacian of the unit-conductance star \(K_{1,m}\), with one hub and \(m\) leaves. The two-stage, order-three Radau IIA endpoint for diffusion \(u'=-L_mu\) is
\[
P_m(h)=R(hL_m),\qquad R(z)=\frac{6-2z}{z^2+4z+6},\qquad h\ge0.
\]
For every \(h\ge0\), \(P_m(h)\) has row sums one. For every \(h>0\), all its off-diagonal entries are strictly positive.

**Exact classification.** If \(2\le m\le10\), then \(P_m(h)\) is entrywise strictly positive for every \(h>0\). For every \(m\ge11\), define
\[
h_m^\pm=\frac{m-2\pm\sqrt{m^2-10m-2}}{m+1},
\]
and let \(\alpha_m<\beta_m\) be the two positive roots of the quartic
\[
F_m(h)=(m+1)h^4+(-2m^2+2m+10)h^3
 +(6m^2+4m+16)h^2+(24m+12)h+36.
\]
These quantities obey
\[
0<h_m^-<h_m^+<2<3<\alpha_m<8<\beta_m.
\]
The **complete** set of nonnegative end-step matrices is precisely
\[
\boxed{\{h\ge0:P_m(h)\ge0\}=[0,h_m^-]\cup[h_m^+,\alpha_m]\cup[\beta_m,\infty).}
\]
In the first excluded open interval \((h_m^-,h_m^+)\) only the hub diagonal is negative; in the second \((\alpha_m,\beta_m)\) only the leaf diagonals are negative. At their respective endpoints only those indicated diagonal entries vanish. Hence the smallest star exhibiting this phenomenon has \(12\) vertices and its positivity set has exactly three connected components.

For the first failing star \(K_{1,11}\), the hub-negative interval is exactly \((1/2,1)\), and the leaf-negative interval is approximately \((6.0684116042,11.7642575954)\).

The windows have distinct large-size scales:
\[
h_m^-=\frac3m+O(m^{-2}),\quad h_m^+=2-\frac9m+O(m^{-2}),\quad
\alpha_m=3+\frac{27}{2m}+O(m^{-2}),\quad \beta_m=2m-7+O(m^{-1}).
\]
Consequently the central safe window tends to the nontrivial finite interval \([2,3]\), while the last recovery step diverges linearly with leaf count.

## Assumptions and scope

The star is finite, simple, undirected and has **uniform unit** edge conductance; the hub is indexed by \(0\) and leaves by \(1,\ldots,m\). All quantifiers above range over integers \(m\ge2\) and real steps \(h\ge0\). Here \(P_m(h)\ge0\) means entrywise nonnegativity of the **endpoint** matrix, not positivity of intermediate Runge–Kutta stages. Row-sum-one does not by itself imply stochasticity when some entries are negative. A common edge conductance \(c>0\) replaces every threshold \(h\) by \(h/c\).

## Proof

**Spectral decomposition and entries.** The eigenvalues of \(L_m\) are \(0\) (simple), \(1\) (multiplicity \(m-1\)) and \(m+1\) (simple). Let
\[
a(h)=\frac{6-2h}{h^2+4h+6},\qquad b_m(h)=\frac{6-2(m+1)h}{(m+1)^2h^2+4(m+1)h+6}.
\]
Orthogonal spectral projectors on constants, leaf differences, and the hub-versus-leaves direction give four types of entries:
\[
\begin{aligned}
P_{00}&=\frac{1+mb_m}{m+1},
&P_{0i}=P_{i0}&=\frac{1-b_m}{m+1},\\
P_{ii}&=\frac{m+b_m+(m^2-1)a}{m(m+1)},
&P_{ij}&=\frac{m+b_m-(m+1)a}{m(m+1)}\quad(i\ne j,\ i,j\ge1).
\end{aligned}
\]
These identities also directly verify all row sums equal one. Write
\[
D_a=h^2+4h+6,\qquad D_b=(m+1)^2h^2+4(m+1)h+6.
\]
Clearing denominators yields
\[
\begin{aligned}
P_{00}&=\frac{(m+1)h^2+(4-2m)h+6}{D_b},\\
P_{0i}&=\frac{h((m+1)h+6)}{D_b},\\
P_{ii}&=\frac{F_m(h)}{D_aD_b},\\
P_{ij}&=\frac{h^2((m+1)h^2+(6m+12)h+18)}{D_aD_b},\quad i\ne j\ge1.
\end{aligned}
\]
Both denominators are strictly positive on \(h\ge0\). Thus all off-diagonal entries are strictly positive for \(h>0\), and the only sign obstructions are the two distinct diagonal types.

**Unconditional positivity through ten leaves.** On \(x\ge0\), elementary differentiation of \(r(x)=(6-2x)/(x^2+4x+6)\) shows
\[
r(x)\ge-\delta,\qquad \delta=\frac{3\sqrt3-5}{2}<\frac1{10}.
\]
Indeed its unique positive critical point is \(3+3\sqrt3\), a global minimum. Hence for \(m\le10\),
\[
1+mb_m\ge1-m\delta>0,
\qquad m+b_m+(m^2-1)a\ge m-m^2\delta>0.
\]
Together with the off-diagonal formulas, this proves strict positivity for every positive step.

**Hub obstruction.** Its numerator is the quadratic
\[
H_m(h)=(m+1)h^2+(4-2m)h+6.
\]
Its discriminant is \(4(m^2-10m-2)\), positive precisely at integer \(m\ge11\). Both roots are positive and equal \(h_m^\pm\). For such \(m\), the hub diagonal is negative exactly between those roots. Moreover \(h_m^+<2\), directly from \(\sqrt{m^2-10m-2}<m+4\).

**Leaf obstruction.** For \(m\ge11\), all coefficients of \(F_m\) except its cubic coefficient are positive, and its cubic coefficient is negative. Descartes' rule of signs bounds the number of positive roots, counted with multiplicity, by two. At \(h=0\), \(F_m>0\). Since \(a(h)\ge0\) for \(0\le h\le3\), and \(b_m(h)\ge-\delta\), the original expression for \(P_{ii}\) proves \(F_m(h)>0\) throughout \([0,3]\). However,
\[
F_m(8)=-4(160m^2-1392m-2593)<0\quad(m\ge11),
\]
where the quadratic in parentheses is positive at \(m=11\) and strictly increasing thereafter. The positive leading quartic coefficient gives \(F_m(h)>0\) for all sufficiently large \(h\). By continuity there is a root in \((3,8)\) and another in \((8,\infty)\). Descartes' rule forces these to be the only two positive roots, each simple. The leaf diagonals are therefore negative exactly on \((\alpha_m,\beta_m)\). Since \(h_m^+<2<3<\alpha_m\), the two negative intervals do not meet, proving the three-window formula.

**Scaling limits.** Expanding \(h_m^\pm\) with \(\sqrt{m^2-10m-2}=m-5-27/(2m)+O(m^{-2})\) gives the first two asymptotics. For the small positive quartic root, substitute \(h=3+u/m\) into \(F_m(h)\):
\[
\frac{F_m(3+u/m)}m=243-18u+O(m^{-1}),
\]
uniformly for bounded \(u\). The unique root in \((3,8)\) then satisfies \(\alpha_m=3+27/(2m)+O(m^{-2})\) by sign bracketing and the negative limiting slope. For the large root, substitute \(h=2m+v\):
\[
\frac{F_m(2m+v)}{m^4}=8(v+7)+O(m^{-1}),
\]
uniformly for bounded \(v\). Bracketing the sole root greater than eight shows \(\beta_m=2m-7+O(m^{-1})\). These calculations are asymptotic proofs from the exact quartic, not numerical extrapolations.

## Verification

Run `python verify.py` with SymPy installed. The code checks the rational entry identities, row sums, derivative and global-minimum identities, exact quartic evaluations, large-size coefficient limits, representative rational full-matrix inversions, both kinds of negative witnesses at \(m=11\), and exact Sturm-based positive-root counts for representative sizes. The package replay reported **3,951 exact symbolic/rational/root assertions passed**. Symbolic computations corroborate the paper proof; finitely many matrix instances alone do not establish the theorem for unbounded \(m\).

## Relationship to prior work

Zappavigna, Colaneri, Kirkland and Shorten (public repository deposit June 19, 2012) study failure of positivity in **diagonal Padé** discretizations and exhibit nilpotent-chain failures. Their section 4 treats a different rational method and neither the two-stage Radau IIA map nor the uniform star's two separate diagonal mechanisms. Lóczi and Ketcheson (arXiv v1 March 26, 2013) study absolute-monotonicity radii of rational stability functions, a uniform method property; this does not determine a graph-specific, nonmonotone all-step positivity set. The general literature also includes discussions of Radau methods as stiff solvers.

Relevant earlier computations establish a one-horizon Crank–Nicolson star result, a fourth-order Padé result on four-vertex weighted stars, a one-unsafe-interval Radau result on balanced complete multipartite graphs, and a six-state directed-cycle Radau phenomenon. None implies this star-specific **three-component** positivity set: the stability functions, graph structures, and controlling matrix entries differ. The present theorem makes no claim to be the first example of positivity loss or later recovery for numerical methods.

## Limitations

This is a theorem for uniform stars and one specified scalar endpoint rational map only. It does not cover heterogeneous spoke weights, arbitrary trees or graphs, internal-stage positivity, repeated timesteps as a nonlinear scheme, or graph-independent absolute monotonicity. Specialized or uncatalogued previous literature could still contain an equivalent classification; the similarity searches do not prove uniqueness in the literature. The only mathematical certificate here is the self-contained proof with reproducible algebraic checks; no independent mathematical audit has been performed.

## References

1. A. Zappavigna, P. Colaneri, S. Kirkland and R. Shorten, *Essentially Negative News About Positive Systems*, publicly deposited June 19, 2012, https://mural.maynoothuniversity.ie/id/eprint/3761/ ; lawfully accessible original PDF https://mural.maynoothuniversity.ie/id/eprint/3761/1/SK_Essentially_Negative.pdf .
2. L. Lóczi and D. I. Ketcheson, *Rational functions with maximal radius of absolute monotonicity*, arXiv:1303.6651v1, March 26, 2013, https://arxiv.org/html/1303.6651v1 .
3. E. Hairer and G. Wanner, *Stiff differential equations solved by Radau methods*, J. Comput. Appl. Math. 111 (1999), 93–111, https://doi.org/10.1016/S0377-0427(99)00134-X (abstract consulted; full text not inspected).

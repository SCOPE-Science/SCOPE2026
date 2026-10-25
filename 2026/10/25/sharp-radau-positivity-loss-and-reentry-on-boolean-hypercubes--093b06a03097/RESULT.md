# Sharp Radau positivity loss and reentry on Boolean hypercubes

## Finding
For the unit-weight binary hypercube \(Q_d\), with \(d\ge1\), let \(L_d\) be its combinatorial graph Laplacian. The completed two-stage third-order Radau IIA step for \(u'=-L_du\) is
\[
T_d(h)=(6I-2hL_d)(6I+4hL_d+h^2L_d^2)^{-1},\qquad h\ge0.
\]
Then \(T_d(h)\) is entrywise nonnegative for **every** \(h\ge0\) if and only if \(d\le3\). Indeed, every entry is strictly positive when \(h>0\) and \(d\le3\), while for **every** \(d\ge4\) all diagonal entries of \(T_d(3/2)\) are strictly negative. In dimension four, the full entrywise-nonnegativity set is exactly
\[
[0,\alpha]\cup[\beta,\infty),
\]
where \(\alpha=1.46546725520286\ldots\) and \(\beta=5.52994947048244\ldots\) are the only positive zeros of
\[
P(h)=192h^8-848h^7-1300h^6+168h^5+2242h^4+2216h^3+1050h^2+252h+27.
\]
For \(d=4\), every off-diagonal entry is strictly positive at every \(h>0\); the diagonal entries alone determine these two intervals. The matrix always has row and column sums one, independently of its entrywise signs.

## Assumptions and scope
The vertices of \(Q_d\) are \(\{0,1\}^d\), with an edge of unit conductance between binary strings differing in exactly one coordinate. Thus \(L_d=dI-A_d\), where \(A_d\) is the adjacency matrix. Time steps are nonnegative real numbers. Nonnegativity means every individual matrix entry is at least zero, not merely positive semidefiniteness. The claim concerns this particular completed Runge–Kutta endpoint map, not its internal stage vectors, arbitrary weighted cubes, nonreversible generators, or other Radau methods.

Write
\[
\rho_j(h)=\frac{6-4jh}{6+8jh+4j^2h^2},\qquad 0\le j\le d.
\]
All denominators are positive for \(h\ge0\). For vertices \(u,v\) at Hamming distance \(k\), put
\[
K_{d,k}(j)=\sum_{i=\max(0,j-d+k)}^{\min(k,j)}(-1)^i\binom{k}{i}\binom{d-k}{j-i}.
\]
The common entry for this distance is
\[
t_{d,k}(h)=2^{-d}\sum_{j=0}^{d}K_{d,k}(j)\rho_j(h).
\]
In particular \(t_{d,0}\) is the diagonal entry.

## Proof
**Walsh reduction.** The coordinate-flip matrices commute and the Walsh characters \(\chi_S(x)=(-1)^{\sum_{i\in S}x_i}\) diagonalize \(L_d\), with eigenvalue \(2|S|\). Substituting these eigenvalues into the stability function \(R(z)=(1+z/3)/(1-2z/3+z^2/6)\) yields the displayed Krawtchouk-type finite sum. Since \(R(0)=1\), the all-ones vector is fixed; symmetry gives both row and column sums one.

**Dimensions at most three.** Define the positive quadratics
\[
A=2h^2+4h+3,\quad B=6h^2+4h+1,\quad C=8h^2+8h+3.
\]
For \(d=3\), direct substitution in the Walsh sum gives, for Hamming distances \(k=0,1,2,3\), respectively,
\[
\begin{aligned}
t_{3,0}&=\frac{12h^6-14h^5+22h^4+83h^3+98h^2+45h+9}{ABC},\\
t_{3,1}&=\frac{h(12h^5+42h^4+92h^3+95h^2+45h+9)}{ABC},\\
t_{3,2}&=\frac{h^2(12h^4+58h^3+76h^2+45h+9)}{ABC},\\
t_{3,3}&=\frac{3h^3(4h^3+22h^2+18h+3)}{ABC}.
\end{aligned}
\]
The only numerator with a negative coefficient contains \(h^4(12h^2-14h+22)\), and \(12h^2-14h+22=12(h-7/12)^2+215/12>0\). Thus all four entries are strictly positive for \(h>0\). Marginalizing one coordinate of the \(Q_3\) step yields the \(Q_2\) step: the coordinate-independent subspace is invariant under \(L_3\), and its restriction is \(L_2\). The same reasoning yields \(Q_1\). Hence all dimensions \(d\le3\) are strictly positive at positive steps.

**Every higher dimension fails at one common step.** At \(h=3/2\) the spectral factors become
\[
\rho_j(3/2)=\frac{2(1-j)}{3j^2+4j+2},
\]
which equals \(1\) for \(j=0\), equals zero for \(j=1\), and is strictly negative for every \(j\ge2\). Therefore
\[
2^d t_{d,0}(3/2)=1+\sum_{j=2}^{d}\binom{d}{j}\rho_j(3/2).
\]
For \(d=4\) the right side equals
\[
1-\frac6{11}-\frac{16}{41}-\frac1{11}=-\frac{12}{451},
\qquad t_{4,0}(3/2)=-\frac3{1804}.
\]
For each \(d>4\), all the negative terms with \(2\le j\le4\) are at least as large in magnitude, since \(\binom dj\ge\binom4j\), and the extra terms are strictly negative. The diagonal is consequently negative for all \(d\ge4\), proving the sharp dimension frontier.

**Complete step classification in dimension four.** Put \(D=32h^2+16h+3>0\). The Walsh sum evaluates to
\[
\begin{aligned}
t_{4,0}&=P(h)/(ABCD),\\
t_{4,1}&=\frac{h(24h^5+50h^4+168h^3+163h^2+60h+9)}{ABD},\\
t_{4,2}&=\frac{h^2(16h^2+36h+9)}{CD},\\
t_{4,3}&=\frac{3h^3(8h^3+38h^2+24h+3)}{ABD},\\
t_{4,4}&=\frac{6h^4(32h^4+200h^3+210h^2+60h+3)}{ABCD}.
\end{aligned}
\]
The four off-diagonal classes are strictly positive for \(h>0\). In descending-degree order the coefficient signs of \(P\) are \(+,-,-,+,+,+,+,+,+\), with exactly two sign changes. Descartes' rule therefore permits at most two positive roots, counted with multiplicity. Since \(P(0)>0\), \(P(3/2)<0\), and the leading coefficient is positive, there must be one root in \((0,3/2)\) and one in \((3/2,\infty)\). Both are simple and there are no others. Thus the diagonal, and hence the entire matrix, is nonnegative precisely on the stated two closed intervals. Exact rational sign evaluations isolate the roots to \((1.465467,1.465468)\) and \((5.529949,5.529950)\), respectively. This finishes the proof.

## Verification
The standalone program `verify.py` uses exact rational and symbolic arithmetic (SymPy). It recomputes all nine displayed \(Q_3\) and \(Q_4\) Walsh identities, exact signs and positive-root counts for \(P\), and direct rational-matrix inversions on hypercubes of dimensions one through five at the stated sample steps. It also tests the fixed-step diagonal witness in a finite set of higher dimensions. Run `python verify.py` after installing SymPy as specified in `requirements.txt`.

Successful replay produced: `VERIFY_OK 9 symbolic kernel identities, 2 root isolations, 14 dimension checks, 124 direct rational matrix entries`. The proof for all dimensions does not rely on the finite dimension checks. The numerical root decimals are illustrations; the zeros of \(P\) define the exact boundaries.

## Relationship to prior work
Zappavigna, Colaneri, Kirkland and Shorten (2010, 2012) establish broader concerns and conditional positivity results for Padé discretizations of positive systems, especially diagonal \([p/p]\) Padé methods; their results and examples do not provide a Radau \([1/2]\) hypercube dimension frontier or these two exact step intervals. The standard Radau IIA method profile supplies the method's stability function and zero radius of absolute monotonicity; this does not determine the behavior of the specified family of symmetric Boolean-cube graph Laplacians. Related known results for Radau diffusion on unweighted cycles, stars, complete bipartite graphs and for Gauss diffusion on cubes concern different update maps or graph families and do not imply the present sharp cube-specific thresholds.

## Limitations
The exact positivity set is classified in every dimension up to four, but the full positivity-time sets for \(d\ge5\) are not determined here. The universal bad step \(3/2\) proves loss of unconditional positivity, not a complete description of every negative entry at other steps. The theorem is restricted to unit-rate unweighted binary cubes and to the completed third-order Radau IIA endpoint map. No claim is made for arbitrary weighted Cartesian products or intermediate Runge–Kutta stages.

## References
1. A. Zappavigna, P. Colaneri, S. Kirkland and R. Shorten, *On the preservation of co-positive Lyapunov functions under Padé discretization for positive systems*, MTNS 2010. Public repository record (deposited 15 October 2010): https://mural.maynoothuniversity.ie/id/eprint/2195/ ; full text: https://mural.maynoothuniversity.ie/id/eprint/2195/1/SK-pade_MTNS10_long.pdf .
2. A. Zappavigna, P. Colaneri, S. Kirkland and R. Shorten, *Essentially Negative News About Positive Systems*, publicly deposited working paper, 19 June 2012: https://mural.maynoothuniversity.ie/id/eprint/3761/ ; full text: https://mural.maynoothuniversity.ie/id/eprint/3761/1/SK_Essentially_Negative.pdf .
3. D. I. Ketcheson, *Numipedia: Radau IIA2*, method coefficients, stability function and absolute-monotonicity radius: https://ketch.github.io/numipedia/methods/RadauIIA2.html .

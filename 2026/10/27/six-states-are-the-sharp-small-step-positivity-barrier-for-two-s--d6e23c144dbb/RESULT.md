# Six states are the sharp small-step positivity barrier for two-stage Radau IIA on Markov generators

## Finding

Let \(Q\) be the row generator of a finite continuous-time Markov chain and let
\[
r(z)=\frac{6+2z}{6-4z+z^2},\qquad T_Q(h)=r(hQ).
\]
This is the exact end-step stability map of the two-stage, third-order Radau IIA Runge–Kutta method on the linear equation \(u'=Qu\). The following results hold.

1. **Minimal state count.** For every Markov generator on at most five states, there is a generator-dependent \(\varepsilon_Q>0\) such that \(T_Q(h)\) is entrywise nonnegative for every \(0\le h\le\varepsilon_Q\). Six states are sharp: an irreducible six-state generator violates entrywise nonnegativity for all sufficiently small positive steps.
2. **Complete sharp six-cycle classification.** Let \(P\) be the cyclic permutation matrix \(P_{i,i+1\bmod6}=1\) and \(Q_6=P-I\). Let \(\tau\) denote the unique positive zero of
\[
p(h)=h^5+15h^4+60h^3+90h^2+36h-12.
\]
Then \(\tau=0.208608859735000\ldots\) and
\[
\boxed{T_{Q_6}(h)\ge0\ \text{entrywise}\quad\Longleftrightarrow\quad h=0\ \text{or}\ h\ge\tau.}
\]
All rows sum to one for every \(h\ge0\); the violation for \(0<h<\tau\) occurs exactly in the entries at forward cyclic displacement five. At \(h=1/10\), one of these entries equals
\[
[T_{Q_6}(1/10)]_{0,5}=-\frac{743849}{19268401151106}<0.
\]
3. **Cycle dimension contrast.** On the analogous directed unit-rate cycles of lengths two through five, \(T_Q(h)\) is strictly positive for every \(h>0\). For every directed unit-rate cycle of length at least six, the forward-displacement-five entries are negative for all sufficiently small positive steps, while all entries are positive for every sufficiently large step. The latter is an eventual-positivity assertion, not an exact threshold classification beyond length six.

In particular, shrinking the timestep is not universally a remedy for a negative Markov end-step coefficient, even for a conservative, irreducible, unit-rate generator.

## Assumptions and scope

A real \(n\times n\) matrix \(Q\) is a **row Markov generator** when its off-diagonal entries are nonnegative and \(Q\mathbf1=0\). No irreducibility or reversibility is required for the five-state lower bound; rates may differ and transitions may be absent. When \(Q=P-I\) for the directed cycle of length \(n\), \(P\) has entries \(P_{i,(i+1)\bmod n}=1\) for \(i=0,\dots,n-1\). The step \(h\) is a nonnegative, dimensionless multiple of the unit edge rate; a common rate \(\gamma>0\) replaces \(h\) by \(\gamma h\).

The statement concerns entrywise nonnegativity of the **completed linear step** \(T_Q(h)\), not intermediate Runge–Kutta stages, nonlinear positivity, or floating-point behavior. The method has a well-defined rational end-step on every finite Markov generator for every \(h\ge0\): the denominator zeros of \(r\) are \(2\pm i\sqrt2\), whereas every eigenvalue of \(Q\) has nonpositive real part. As \(r(0)=1\) and \(Q\mathbf1=0\), \(T_Q(h)\mathbf1=\mathbf1\), regardless of entrywise signs.

## Proof

**1. Exact small-step coefficients.** Direct formal division at the origin gives
\[
r(z)=1+z+\frac{z^2}{2}+\frac{z^3}{6}+\frac{z^4}{36}-\frac{z^5}{108}+O(z^6).
\]
Fix different states \(i,j\). If \(j\) cannot be reached from \(i\) through positive-rate transitions, the rational resolvent and every polynomial in \(Q\) have zero entry at \((i,j)\), so \([T_Q(h)]_{ij}\equiv0\). Otherwise let \(d\) be their shortest directed path length. A shortest path is simple, so \(1\le d\le n-1\). Every contribution to \((Q^k)_{ij}\) with \(k<d\) vanishes. At length \(d\), only actual off-diagonal transitions can contribute, and at least one such path has a positive rate product; thus \((Q^d)_{ij}>0\). For \(n\le5\), \(d\le4\) and the coefficient of \(z^d\) in the displayed expansion is strictly positive. Consequently
\[
[T_Q(h)]_{ij}=a_d (Q^d)_{ij}h^d+O(h^{d+1})>0
\]
for sufficiently small positive \(h\), where \(a_1=1\), \(a_2=1/2\), \(a_3=1/6\), \(a_4=1/36\). Every diagonal entry is \(1+O(h)>0\). The finitely many entrywise neighborhoods admit a common \(\varepsilon_Q\), proving the five-state lower bound. This does **not** give a uniform positive timestep independent of the generator's rates.

**2. Six-state obstruction and all longer cycles.** For \(Q_n=P_n-I\) on any directed cycle with \(n\ge6\), the first path from vertex zero to vertex five uses five off-diagonal moves. Therefore
\[
[T_{Q_n}(h)]_{0,5}=-\frac{h^5}{108}+O(h^6)<0
\]
for all sufficiently small positive \(h\). For the irreducible cycle generator, the eigenvalues are \(e^{2\pi i k/n}-1\), and all but the zero eigenvalue have strictly negative real part. Since \(r(h\lambda)\to0\) for every nonzero eigenvalue as \(h\to\infty\), spectral decomposition of the cyclic shift gives
\[
T_{Q_n}(h)\longrightarrow\frac1n\mathbf1\mathbf1^{\mathsf T}
\quad\text{entrywise as }h\to\infty.
\]
Hence every such cycle eventually has all-positive coefficients. For the six-cycle the exact return boundary is determined next.

**3. Exact six-cycle rational reduction.** In the algebra \(P^6=I\), solve the polynomial congruence
\[
\bigl((6+4h+h^2)I-(4h+2h^2)P+h^2P^2\bigr)T
=(6-2h)I+2hP.
\]
The six resulting circulant transition classes have a common strictly positive denominator
\[
\begin{aligned}
D_6(h)={}&(2h^2+4h+3)
(h^4+4h^3+10h^2+24h+36)\\
&\hspace{8mm}\cdot(3h^4+12h^3+22h^2+24h+12).
\end{aligned}
\]
Write \([T_{Q_6}(h)]_{0,j}=N_j(h)/D_6(h)\). The exact numerator at forward displacement five is \(N_5(h)=h^5p(h)\). For the four other non-diagonal classes, each \(N_j(h)/h^j\) has **strictly positive coefficients**; the following table lists those coefficients in ascending degree order (each row defines its polynomial completely):

| \(j\) | Coefficients of \(N_j(h)/h^j\), ascending |
| --- | --- |
| 1 | 1296, 3888, 5400, 4512, 2472, 904, 214, 36, 7, 1 |
| 2 | 648, 1944, 2592, 2016, 996, 316, 63, 9, 1 |
| 3 | 216, 720, 960, 696, 300, 76, 11, 1 |
| 4 | 36, 204, 306, 210, 75, 13, 1 |

The diagonal numerator is
\[
\begin{aligned}
N_0(h)={}&h^{10}+5h^9-5h^8-50h^7+26h^6+664h^5\\
&+2280h^4+4440h^3+5400h^2+3888h+1296.
\end{aligned}
\]
Its positivity needs a certificate because it has two negative monomial coefficients. On \(0\le h\le1\), writing this degree-ten polynomial in the Bernstein basis \(\binom{10}{k}h^k(1-h)^{10-k}\) yields eleven **strictly positive** coefficients, in increasing \(k\):
\[
\left(1296,\frac{8424}{5},\frac{10968}{5},\frac{14297}{5},
\frac{130552}{35},\frac{306616}{63},\frac{666497}{105},
\frac{496103}{60},\frac{483569}{45},\frac{139181}{10},17945\right).
\]
On \(h\ge1\), setting \(h=1+t\) gives ascending monomial coefficients
\[
(17945,40269,38465,19230,4730,372,166,210,85,15,1),
\]
all strictly positive for \(t\ge0\). Thus the diagonal entry is positive for all \(h\ge0\). The denominator and remaining four numerators are strictly positive for \(h>0\). Finally
\[
p'(h)=5h^4+60h^3+180h^2+180h+36>0\quad(h\ge0),
\]
while \(p(0)=-12\) and \(p(h)\to+\infty\). This proves existence and uniqueness of \(\tau\), the exact six-cycle positivity set, and the identification of every negative transition. Exact substitution of \(h=1/10\) gives the stated rational counterexample.

**4. Short-cycle unconditional positivity.** Repeat the displayed polynomial congruence with \(P^n=I\) for \(n=2,3,4,5\). For each such \(n\), the common denominator has strictly positive monomial coefficients and every entry numerator has nonnegative monomial coefficients, with at least one strictly positive coefficient; all are therefore strictly positive for \(h>0\). These are four fixed finite rational identities, reconstructed and verified in exact symbolic arithmetic by the accompanying standalone script. No sampling or approximate eigenvalue argument is used to infer this conclusion.

## Verification

Run `python artifacts/verify_radau_directed_cycles.py` with SymPy from the package root. It constructs the actual rational matrix \((6I+2hQ)(6I-4hQ+h^2Q^2)^{-1}\), expands and checks every transition class for cycles of lengths two through six, verifies row sums, checks the Taylor coefficients and positive-root factor, verifies the six-cycle diagonal Bernstein/shift positivity certificates, and evaluates the exact negative witness. The successful output is embedded in `artifacts/verification_output.txt`. These exact finite algebra checks support the finite rational identities; the proof of the universal five-state bound and the general large-cycle assertions is analytical and not inferred by enumeration.

## Relationship to prior work

Gottlieb, Shu and Tadmor (2001) develop SSP theory, including the limitations of implicit high-order methods. Lóczi and Ketcheson (2014) analyze absolute-monotonicity radii of rational stability functions, which address method-wide positivity guarantees but do not determine a minimum conservative Markov state count or a particular irreducible cycle's complete return interval. Zappavigna, Colaneri, Kirkland and Shorten (2012) exhibit loss of positivity at arbitrarily small steps for a different, fourth-order diagonal Padé function and Metzler/Hurwitz systems; their nilpotent-shift example does not establish this six-state conservative third-order Radau classification. Blanes, Iserles and Macnamara (2022) motivate dedicated positivity-preserving integrators for graph-Laplacian systems but do not give the present threshold. A related published eight-state minimal small-step barrier for the fourth-order Gauss \([2/2]\) Padé map involves a different stability function and does not imply the third-order Radau result. Source/claim overlap comparisons are recorded separately in the accompanying review and audit materials.

## Limitations

No assertion is made that the Radau IIA method, including its intermediate stages, is positivity-preserving on nonlinear systems. The minimal-dimension statement concerns failure **for arbitrarily small positive steps**; it does not classify other generators' entire positivity intervals. The exact \(h\ge\tau\) condition applies to the unit-rate directed six-cycle only; for directed cycles longer than six, only small-step failure and eventual positivity are proved. The algebraic certificates do not establish novelty or replace independent proof inspection. No independent audit has been performed.

## References

1. S. Gottlieb, C.-W. Shu, E. Tadmor, “Strong Stability-Preserving High-Order Time Discretization Methods,” *SIAM Review* **43** (2001), 89–112, https://www.math.umd.edu/~tadmor/pub/linear-stability/Gottlieb-Shu-Tadmor.SIREV-01.pdf (electronically published 2001-02-02).
2. L. Lóczi, D. I. Ketcheson, “Rational functions with maximal radius of absolute monotonicity,” *LMS Journal of Computation and Mathematics* **17** (2014), 159–205, https://doi.org/10.1112/S1461157013000326 .
3. A. Zappavigna, P. Colaneri, S. Kirkland, R. Shorten, “Essentially negative news about positive systems,” *Linear Algebra and its Applications* **436** (2012), 3425–3442, https://doi.org/10.1016/j.laa.2011.12.021 .
4. S. Blanes, A. Iserles, S. Macnamara, “Positivity-preserving methods for ordinary differential equations,” *ESAIM: Mathematical Modelling and Numerical Analysis* **56** (2022), 1843–1870, https://personales.upv.es/serblaza/2022_M2AN.pdf .
5. D. I. Ketcheson, “Radau IIA (two-stage),” Numipedia, https://ketch.github.io/numipedia/methods/RadauIIA2.html (method stability-function reference).

# Sharp six-state recovery of Markov positivity for Radau IIA on directed cycles

## Finding

For the two-stage, order-three Radau IIA method, directed cycles exhibit an exact dimension barrier and a non-monotone dependence of endpoint positivity on step size. Let \(S_n\) be the \(n\times n\) cyclic shift, \((S_n)_{i,i+1\bmod n}=1\), and let \(Q_n=S_n-I_n\). The stability function and endpoint map are
\[
R(z)=\frac{6+2z}{6-4z+z^2},\qquad P_n(h)=R(hQ_n),\quad h\ge0.
\]
For all integers \(2\le n\le5\), the matrix \(P_n(h)\) is strictly entrywise positive for all \(h>0\). For \(n=6\), its *complete* entrywise-nonnegativity set is
\[
\{0\}\,\cup\,[\rho,\infty),\qquad
\rho=0.208608859735\ldots,
\]
where \(\rho\) is the unique positive root of
\[
q(h)=h^5+15h^4+60h^3+90h^2+36h-12.
\]
For **every** \(n\ge6\), all sufficiently small positive steps give a negative entry, but all sufficiently large steps give an entrywise positive matrix. Thus the six-state directed cycle is the smallest uniform directed cycle exhibiting small-step loss and later recovery of Markov positivity.

A separate, wider local statement holds: for every CTMC generator \(Q\) of order \(n\le5\), the matrix \(R(hQ)\) is entrywise nonnegative throughout some generator-dependent interval \(0\le h\le\varepsilon_Q\).

## Assumptions and scope

We work over real matrices, in the row-generator convention \(Q_{ij}\ge0\) for \(i\ne j\) and \(Q\mathbf 1=0\). The directed cycle uses a unit-rate clockwise jump from every state. A matrix is called endpoint-positive if it is entrywise nonnegative and row-stochastic, not merely stable. The independent time parameter is the dimensionless product of the jump rate and the physical timestep; a common rate \(\lambda>0\) changes each stated \(h\) to \(\lambda h\).

The Radau IIA Butcher matrix and weights are
\[
A=\begin{pmatrix}5/12&-1/12\\3/4&1/4\end{pmatrix},\qquad b=(3/4,1/4).
\]
They produce \(R(z)=1+z b(I-zA)^{-1}\mathbf1\). The method is L-stable, but this does not entail positivity.

## Proof

**Existence, mass conservation, and large-step limit.** The denominator \(6-4z+z^2\) has roots \(2\pm i\sqrt2\) in the strict right half-plane, while every CTMC generator has spectrum in the closed left half-plane. Thus \(R(hQ)\) is defined for all \(h\ge0\) and has row sums one because \(Q\mathbf1=0\) and \(R(0)=1\). For the directed cycle, \(Q_n\) is diagonalizable by the discrete Fourier transform, with simple zero eigenvalue and all other eigenvalues having negative real part. The rational function tends to zero at complex infinity, so
\[
\lim_{h\to\infty}P_n(h)=\frac1n\mathbf1\mathbf1^{\mathsf T}.
\]
This convergence is entrywise, giving eventual strict positivity for every fixed \(n\).

**Local lower bound and sharp failure.** Direct series division yields
\[
R(z)=1+z+\frac{z^2}2+\frac{z^3}6+\frac{z^4}{36}-\frac{z^5}{108}+O(z^6).
\]
For any CTMC generator, fix distinct states \(i,j\) with a directed path of minimal length \(\ell\). Then \((Q^k)_{ij}=0\) for \(k<\ell\), and \((Q^\ell)_{ij}>0\); these are sums of products of the positive rates along shortest paths. If \(n\le5\), every reachable \(j\) has \(\ell\le4\), for which the relevant coefficient of \(R\) is strictly positive. Nonreachable entries vanish identically (analytic functional calculus on the invariant reachability preorder), and diagonal entries tend to one. Finitely many entries give a common \(\varepsilon_Q>0\). On the uniform directed \(n\)-cycle with \(n\ge6\), the pair of states at clockwise distance five satisfies
\[
(P_n(h))_{i,i+5}=-\frac{h^5}{108}+O(h^6)<0
\]
for every sufficiently small \(h>0\); the minimal walk has exactly five jumps and unit rate product. This proves sharpness of the dimension barrier, independently of all finite checks below.

**Exact all-step classification through six states.** Write \(S=S_n\), \(S^n=I\). Algebra in \(\mathbb Q(h)[S]/(S^n-I)\) gives
\[
P_n(h)=\frac{\sum_{j=0}^{n-1}N_{n,j}(h)S^j}{D_n(h)}.
\]
To reconstruct the coefficients, reduce
\[
\bigl((h^2+4h+6)I-(2h^2+4h)S+h^2S^2\bigr)^{-1}
\bigl((6-2h)I+2hS\bigr)
\]
modulo \(S^n=I\). The complete integer polynomials \(D_n,N_{n,j}\) for \(2\le n\le6\) appear in `artifacts/COEFFICIENT_CERTIFICATES.md` and are independently recomputed and checked by `artifacts/verify_radau_cycle.py`. For every \(n\le5\), each denominator has strictly positive coefficients and each numerator has nonnegative coefficients and is strictly positive at \(h>0\). Therefore all entries are positive for every \(h>0\), a non-asymptotic conclusion.

For \(n=6\), each denominator factor has positive coefficients:
\[
D_6(h)=(2h^2+4h+3)(h^4+4h^3+10h^2+24h+36)
(3h^4+12h^3+22h^2+24h+12).
\]
The numerators \(N_{6,j}\) for \(j=1,2,3,4\) have nonnegative coefficients. The exceptional numerator is
\[
N_{6,5}(h)=h^5q(h).
\]
The diagonal numerator is
\[
\begin{aligned}
N_{6,0}(h)={}&h^{10}+5h^9-5h^8-50h^7+26h^6+664h^5\\
&+2280h^4+4440h^3+5400h^2+3888h+1296.
\end{aligned}
\]
For \(0\le h\le3\), the subset \(664h^5-5h^8-50h^7=h^5(664-5h^3-50h^2)\ge79h^5\). For \(h\ge3\), the subset \(h^{10}+5h^9-5h^8-50h^7=h^7(h^3+5h^2-5h-50)\) is positive: the cubic is positive at three and increasing thereafter. All remaining monomials are nonnegative. Thus the diagonal numerator is positive at every \(h\ge0\).

Finally, \(q(0)=-12\) and \(q'(h)>0\) for every \(h>0\), while \(q(h)\to\infty\), so \(q\) has precisely one positive root and \(N_{6,5}\) is the *only* possibly negative entry coefficient. Its root lies strictly between \(2086088597/10^{10}\) and \(2086088598/10^{10}\). This proves the claimed exact positivity set, including the boundary point.

## Verification

Run `python3 artifacts/verify_radau_cycle.py` with SymPy installed. The program reconstructs the Radau stability function from the Butcher tableau, checks the Taylor coefficients, proves all printed coefficient identities for \(2\le n\le6\) by symbolic modular polynomial inversion, compares them with exact six-by-six and smaller matrix inverses at four rational timesteps, verifies mass conservation, and checks the exact rational interval for \(\rho\). The deterministic replay recorded 158 successful assertions. The infinite-dimensional-range steps use the direct path-length and spectral arguments above, **not** finite enumeration or floating-point experiments.

## Relationship to prior work

Zappavigna, Colaneri, Kirkland, and Shorten (2012) give positivity failures for *diagonal* Padé maps on general Metzler systems and sufficient positivity criteria; they do not treat this subdiagonal \([1/2]\) Radau IIA rational map or the directed-cycle all-step classification. Lóczi and Ketcheson (2013/2014) establish an absolute-monotonicity framework, but their inspected theorem material does not state the exact directed-cycle threshold. A later published mathematical record gives an eight-state minimal dimension for the different *diagonal* \([2/2]\) Padé/Gauss map; its coefficients, threshold, and absorbing pure-birth witness are different. The present six-state rational positivity set is not an immediate corollary of those statements.

## Limitations

This theorem concerns the **endpoint** update under exact arithmetic, not nonnegativity of internal stages, variable or nonuniform cycle rates, nonlinear positivity, higher-dimensional graphs, or all-step positivity for arbitrary small CTMC generators. The local five-state extension has a generator-dependent step bound, not a universal positive step bound when rates are unbounded. The inspected literature does not prove global novelty against every specialized publication; independent mathematical validation has not been performed.

## References

1. A. Zappavigna, P. Colaneri, S. Kirkland, R. Shorten, “Essentially Negative News About Positive Systems,” preprint (2012), https://www.hamilton.ie/skirkland/pade_paper_final_end.pdf . Public repository deposit documented 2012-06-19: https://mural.maynoothuniversity.ie/id/eprint/3761/ .
2. L. Lóczi, D. I. Ketcheson, “Rational Functions with Maximal Radius of Absolute Monotonicity,” arXiv:1303.6651, first submitted 2013-03-26, https://arxiv.org/abs/1303.6651 .
3. “Eight-state barrier for Markov positivity of the \([2/2]\) Padé map,” published mathematical result (2026), https://github.com/Resultary/2026/tree/main/2026/9/20/SCOPE-eight-state-pade-markov-positivity-barrier--4aad2a3f58ab/RESULT.md .

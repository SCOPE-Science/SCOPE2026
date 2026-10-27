# Sharp mean–variance spectral phase boundaries in a locally resetting finite zero-range network

## Finding
For every finite complete network of \(K\ge2\) sites with positive fitness-dependent linear birth rates, positive death and migration rates, and independent positive-rate resets of individual sites to zero, the stationary **finite-first-moment** and **finite-second-moment** regimes have separate exact spectral tests. Let \(B\) be the \(K\)-by-\(K\) mean matrix and \(H\) the \(K(K+1)/2\)-by-\(K(K+1)/2\) factorial-second-moment matrix defined below. A stationary law with finite means exists exactly when the spectral abscissa \(s(B)<0\). Within that regime its entire second-moment matrix is finite exactly when \(s(H)<0\). Both matrices are explicit irreducible Metzler matrices, so the criteria have no moment-closure approximation.

An exact two-site witness has finite means \((56/5,6/5)\) but infinite variance at the fitter site: choose \((\ell_1,\ell_2)=(1,1/5)\), birth/death/migration rates as below with \(\delta=1/5\), \(\beta=1/10\), and independent local-reset rates \((r_1,r_2)=(4/5,1)\). This finite-mean/infinite-variance regime persists throughout an open parameter neighborhood.

## Assumptions and scope
The state is \(n=(n_1,\ldots,n_K)\in\mathbb N_0^K\). Assume \(K\ge2\), \(\ell_i>0\) (fitness), \(\delta>0\) (particle death), \(\beta>0\) (per-particle hopping), and \(r_i>0\) (local reset). All clocks are independent except for jumps acting on both the departure and arrival site. The transitions are:

* \(n\to n+e_i\) at rate \(\ell_i(n_i+1)\);
* \(n\to n-e_i\) at rate \(\delta n_i\);
* \(n\to n-e_i+e_j\), for each ordered \(i\ne j\), at rate \(\beta n_i/(K-1)\);
* \(n\to n-n_i e_i\) at rate \(r_i\).

A reset to zero leaves other sites unchanged; births can resume immediately. This is the finite-complete-network, uniform-destination version of the fitness-selection and local-site-resetting mechanisms, **not** an assertion about the infinite-network thermodynamic limit. The positive-rate continuous-time chain is nonexplosive and irreducible: the total birth intensity is at most linear in total population, and creation/death moves connect all finite configurations.

Put \(F_{ii}(n)=n_i(n_i-1)\) and \(F_{ij}(n)=n_i n_j\) for \(i<j\). Define \(B\) by
\[
 B_{ii}=\ell_i-\delta-\beta-r_i,\qquad
 B_{ij}=\frac{\beta}{K-1}\quad(i\ne j).
\]
Define the linear operator \(H\) on symmetric arrays \(z=(z_{ij})_{1\le i\le j\le K}\) by
\[
 (Hz)_{ii}=\bigl[2(\ell_i-\delta-\beta)-r_i\bigr]z_{ii}
 +\frac{2\beta}{K-1}\sum_{j\ne i}z_{\min(i,j),\max(i,j)},
\]
\[
\begin{split}
 (Hz)_{ij}={}&[\ell_i+\ell_j-2(\delta+\beta)-r_i-r_j]z_{ij}\\
 &+\frac{\beta}{K-1}\left[z_{ii}+z_{jj}+\sum_{k\notin\{i,j\}}(z_{\min(i,k),\max(i,k)}+z_{\min(j,k),\max(j,k)})\right]\quad(i<j).
\end{split}
\]
The spectral abscissa \(s(M)\) means the maximum real part among eigenvalues of \(M\). Irreducibility and positive off-diagonal edges imply that both spectral abscissae are real simple Perron eigenvalues with positive left/right eigenvectors.

## Proof
**1. Exact first-moment drift.** Apply the generator \(\mathcal L\) to each coordinate \(n_i\). The birth, death, outward jump, inward jump, and site-reset contributions give
\[
 \mathcal L n_i=\ell_i+\sum_j B_{ij}n_j.
\]
If \(s(B)<0\), the inverse of \(-B^\mathsf T\) is entrywise positive. Take \(h=(-B^\mathsf T)^{-1}\boldsymbol1>0\) and \(V(n)=1+h^\mathsf T n\). Then \(\mathcal LV=h^\mathsf T\ell-\sum_i n_i\). The standard countable-state Foster drift criterion gives positive recurrence, uniqueness of the invariant law \(\pi\), and finite stationary first moments. In particular
\[
 m:=\mathbb E_\pi n=-B^{-1}\ell>0.
\]
Conversely, any invariant law with finite means satisfies \(Bm+\ell=0\). A strictly positive left Perron vector \(u\) of \(B\) gives \(0=s(B)u^\mathsf Tm+u^\mathsf T\ell\), impossible when \(s(B)\ge0\). This proves the first criterion, without claiming the absence of invariant laws having infinite means.

**2. Exact quadratic drift.** A birth at site \(i\) increases \(F_{ii}\) by \(2n_i\); an outward jump decreases it by \(2(n_i-1)\); an inward jump increases it by \(2n_i\); and a reset annihilates it. For distinct \(i,j\), a hop \(i\to j\) changes \(F_{ij}\) by \(n_i-n_j-1\). Direct substitution gives, simultaneously for every configuration,
\[
 \mathcal L F_{ii}=(HF(n))_{ii}+4\ell_i n_i,
 \qquad
 \mathcal L F_{ij}=(HF(n))_{ij}+\ell_i n_j+\ell_j n_i.
\]
The linear source vector \(g(n)\) is coordinatewise nonnegative. Both \(H\) and \(B\) are Metzler and irreducible (migration connects all unordered two-particle index pairs).

**3. Necessity and sufficiency of quadratic stability.** Suppose \(s(B)<0\). If \(s(H)<0\), choose \(q=(-H^\mathsf T)^{-1}\boldsymbol1>0\) and the positive \(h\) from step 1. For sufficiently large \(c>0\), the nonnegative norm-like quadratic Lyapunov function
\[
 W(n)=1+q^\mathsf T F(n)+c h^\mathsf T n
\]
satisfies \(\mathcal LW\le C-\varepsilon W\) for constants \(C,\varepsilon>0\), since \(q^\mathsf T g(n)\) is only linear in \(n\). The invariant law therefore has all factorial second moments finite, hence all ordinary second moments finite. Conversely, if the stationary second moments were finite, stationary integration of the quadratic generator identities would yield \(Hz+g(m)=0\), where \(z=\mathbb E_\pi F(n)\). A positive left Perron vector \(v\) gives \(0=s(H)v^\mathsf Tz+v^\mathsf Tg(m)\). The last term is strictly positive because all fitnesses and stationary means are positive. Hence \(s(H)<0\). Both implications are exact.

**4. Rational two-site witness.** In the parameter example of the Finding, direct substitution gives
\[
 B=\begin{pmatrix}-1/10&1/10\\1/10&-11/10\end{pmatrix},\qquad
 H=\begin{pmatrix}3/5&1/5&0\\1/10&-6/5&1/10\\0&1/5&-6/5\end{pmatrix}
\]
with pair order \((11,12,22)\). The eigenvalues of \(B\) are \((-6\pm\sqrt{26})/10<0\), and the unique stationary mean is \(-B^{-1}\ell=(56/5,6/5)\). The first diagonal entry of \(H\) is \(3/5>0\). Since \(H\) is irreducible Metzler, \(s(H)>0\); thus some quadratic moment diverges.

To identify the divergent marginal, couple site 1 from below with a one-site population \(Y\) having births at rate \(Y+1\), deaths at rate \((3/10)Y\), and independent resets to zero at rate \(4/5\). Site 1 has these transitions plus nonnegative arrivals from site 2, so the usual shared-clock branching construction preserves \(N_1(t)\ge Y(t)\) when both start at zero. For the reset-free \(Y\) started at zero and evolved for age \(t\), writing \(\lambda=1-3/10=7/10\), direct birth-death moment equations give
\[
 u(t):=\mathbb EY(t)=\frac{e^{\lambda t}-1}{\lambda},\qquad
 \mathbb E[Y(t)(Y(t)-1)]=2u(t)^2.
\]
At stationarity, the time since the last reset has density \((4/5)e^{-4t/5}\), so the stationary mean of \(Y\) is \(1/(4/5-7/10)=10\), but its factorial second moment is \(\int_0^\infty (4/5)e^{-4t/5}2u(t)^2dt=+\infty\), as \(4/5<2(7/10)\). Stationary stochastic domination then forces \(\mathbb E_\pi[N_1(N_1-1)]=+\infty\) although \(\mathbb E_\pi N_1=56/5\). All inequalities that establish this example are strict, giving an open region of finite means with infinite first-site variance.

## Verification
The included standalone `check.py` uses Python's rational arithmetic and exhaustively compares the generator to both proposed polynomial drift identities at 1,841 deterministic state/index/parameter checks for \(K=2,3,4\), followed by rational mean and threshold assertions. It reproduces the saved `CHECK_OUTPUT.txt`; its finite checks validate algebraic coefficients but are **not** used as proof of universal spectral or moment claims. The proof is in the preceding section, using Perron–Frobenius, Foster drift criteria, exact generator identities, and a regenerative comparison.

To replay from the package: `python3 check.py` (Python standard library only).

## Relationship to prior work
Grange (2023, arXiv:2311.12414) studies fitness-dependent local resetting in a large complete-network nonconserving zero-range model, deriving site-level generating functions and average occupation and studying condensation under \(\beta+\delta>1\). Grange (2019, arXiv:1904.05604) develops the underlying fitness-dependent birth/migration/death mechanism, and Grange (2019/2020, arXiv:1910.05991) treats collective rather than sitewise resetting. These results motivate, but do not supply, the displayed **finite-network coupled second-moment spectral boundary** or the exact finite-mean/infinite-variance two-site regime outside the earlier \(\beta+\delta>1\) assumption.

Kapodistria, Phung-Duc and Resing (2015/2016) establish factorial-moment criteria for a **single** linear birth/immigration/death population with binomial or total catastrophes. In particular, the one-site exponent test used in step 4 is established general theory and is not represented as novel. What is assessed here is the joint finite-network classification involving independent local resets, particle migration, an interacting second-moment matrix, and its sharp gap from mean stability. A general multitype catastrophe theorem may encode similar matrices; independent priority validation remains outstanding.

## Limitations
The classification is for finite, fixed \(K\) and positive model rates, not a proof of a thermodynamic condensation transition. The first-moment test classifies **finite-mean stationary laws**, not the possible existence of invariant laws with infinite mean outside that regime. The second-moment test applies within the finite-first-moment regime. It does not characterize higher moments, critical decay at zero spectral abscissa, or finite-sample estimator performance. Independent scholarly audit has not been performed.

## References
1. Pascal Grange, *Local resetting in non-conserving zero-range processes with extensive rates*, arXiv:2311.12414 (first posted 2023-11-21), https://arxiv.org/abs/2311.12414.
2. Pascal Grange, *Steady states in a non-conserving zero-range process with extensive rates as a model for the balance of selection and mutation*, arXiv:1904.05604 (2019), https://arxiv.org/abs/1904.05604.
3. Pascal Grange, *Non-conserving zero-range processes with extensive rates under resetting*, arXiv:1910.05991 (2019), https://arxiv.org/abs/1910.05991.
4. Stella Kapodistria, Tuan Phung-Duc and Jacques Resing, *Linear birth/immigration-death process with binomial catastrophes*, Eurandom Report 2015-006; *Probability in the Engineering and Informational Sciences* 30 (2016), 79–111, https://www.eurandom.tue.nl/reports/2015/006-report.pdf.

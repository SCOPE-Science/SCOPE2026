# Six-state rate-tuning barrier for positivity of Alexander's two-stage SDIRK method on reversible stars

## Finding

Let \(K_{1,m}\) be a star with \(m\ge2\) leaves. Give each hub-to-leaf jump rate \(v>0\), and give each leaf-to-hub jump rate \(u>0\). Apply Alexander's second-order, two-stage, L-stable singly diagonally implicit Runge–Kutta method to the associated continuous-time Markov generator. Write \(P(h)\) for the resulting endpoint transition matrix at timestep \(h\ge0\).

**Sharp rate-tuning classification.** There exist positive rates \(u,v\) for which \(P(h)\) is entrywise nonnegative for **every** \(h\ge0\) if and only if \(m\le4\). Indeed, \(u=v\) suffices whenever \(2\le m\le4\). Conversely, for every \(m\ge5\) and every \(u,v>0\), at least one positive timestep gives a negative diagonal entry. All off-diagonal entries are strictly positive at every positive timestep. Every such negative episode is bounded away from sufficiently small timesteps and sufficiently large timesteps, where the matrix is entrywise nonnegative. Thus the six-state star is the smallest star on which *no choice of positive, homogeneous spoke rates* can make this method unconditionally endpoint-positive.

The negative diagonal is located constructively. Set
\[
\gamma=1-\frac1{\sqrt2},\quad
\eta=\frac{\sqrt2-1}{2},\quad
w_*=4+3\sqrt2,\quad
z=1+\frac{mv}{u},\quad z_*=3+2\sqrt2.
\]
For \(m\ge5\), if \(z>z_*\), then \(P_{00}(w_*/(uz))<0\). If \(1<z\le z_*\), then every leaf diagonal satisfies \(P_{jj}(w_*/u)<0\). At the second witness,
\[
 mP_{jj}(w_*/u)\le \frac{297-211\sqrt2}{98}<0.
\]
The statement is about endpoint positivity, not positivity of every intermediate Runge–Kutta stage.

## Assumptions and scope

The row-generator \(Q\) has state \(0\) at the hub and states \(1,\ldots,m\) at the leaves. Its nonzero entries are
\[
Q_{00}=-mv,\quad Q_{0j}=v,\quad Q_{j0}=u,\quad Q_{jj}=-u\qquad (1\le j\le m).
\]
The chain is irreducible and reversible for all \(u,v>0\). It is immaterial whether row distributions evolve by \(p'(t)=p(t)Q\) or column distributions evolve by \(y'(t)=Q^{\mathsf T}y(t)\): the endpoint matrices are transposes and have the same entrywise signs. Put
\[
\gamma=1-1/\sqrt2,\qquad
A=\begin{pmatrix}\gamma&0\\1-\gamma&\gamma\end{pmatrix},\qquad
b=(1-\gamma,\gamma).
\]
These are the two-stage, stiffly accurate, L-stable SDIRK coefficients; no modified method or positivity limiter is used. The scalar stability function on a negative real argument is
\[
r(x)=R(-x)=\frac{1-(1-2\gamma)x}{(1+\gamma x)^2},\qquad x\ge0.
\]
Thus \(P(h)=R(hQ)\), with the rational matrix expression well-defined at every \(h\ge0\). No condition on the ratio \(v/u\) is imposed in the impossibility half; the favorable half is an existence statement, not a statement about arbitrary rate choices.

## Proof

**1. Spectrum and exact entries.** Introduce \(z=1+mv/u>1\), \(w=uh\), and the stationary probabilities
\[
\pi_0=\frac1z,\qquad \pi_j=\frac{z-1}{mz}\quad(1\le j\le m).
\]
The generator has eigenvalues \(0\) (one-dimensional), \(-u\) (multiplicity \(m-1\), leaf differences), and \(-uz\) (one-dimensional, hub-versus-leaf mode). Resolving these invariant subspaces gives, for distinct leaves \(i,j\),
\[
\begin{aligned}
P_{00}(h)&=\frac{1+(z-1)r(zw)}z,\\
P_{0j}(h)&=\frac{z-1}{mz}\,[1-r(zw)],\\
P_{j0}(h)&=\frac1z[1-r(zw)],\\
P_{ij}(h)&=\frac{1}{m}\left[1-r(w)-\frac{1-r(zw)}z\right],\\
mP_{jj}(h)&=1+(m-1)r(w)+\frac{r(zw)-1}{z}.
\end{aligned}
\]
The formulas at \(h=0\) hold by continuity. Since \(R(0)=1\) and \(Q\mathbf1=0\), all rows of \(P(h)\) sum to one.

**2. Off-diagonal positivity.** A direct identity is
\[
F(x):=\frac{1-r(x)}x=\frac{1+\gamma^2x}{(1+\gamma x)^2}>0
\quad(x\ge0),\qquad
F'(x)=\frac{\gamma(\gamma-2-\gamma^2x)}{(1+\gamma x)^3}<0.
\]
The value at \(x=0\) is interpreted by continuity. Hence \(1-r(x)>0\) for every \(x>0\), and
\[
P_{ij}(h)=\frac{w}{m}[F(w)-F(zw)]>0
\qquad (i\ne j\text{ both leaves},\ h>0),
\]
while the two hub–leaf expressions above are also strictly positive. Therefore only diagonals can obstruct endpoint nonnegativity.

**3. Sharp scalar extremum.** Differentiating \(r\) yields
\[
r'(x)=\frac{-1+\gamma(1-2\gamma)x}{(1+\gamma x)^3}.
\]
Thus its unique global minimum on \([0,\infty)\) is reached at
\[
w_*=\frac1{\gamma(1-2\gamma)}=4+3\sqrt2,
\qquad r(w_*)=-\eta=-\frac{\sqrt2-1}{2}.
\]
In particular \(r(x)\ge-\eta\) for all \(x\ge0\).

**4. Safe rate choice for at most four leaves.** Let \(u=v\), so \(z=m+1\). The hub diagonal has the lower bound
\[
P_{00}(h)\ge\frac{1-m\eta}{m+1}.
\]
Likewise the leaf formula, using \(r(w),r(zw)\ge-\eta\), gives
\[
P_{jj}(h)\ge\frac{1-m\eta}{m+1}.
\]
Since \(4\eta=2(\sqrt2-1)<1\), both are strictly positive whenever \(2\le m\le4\), at every finite timestep. The off-diagonal result completes this half.

**5. Unavoidable failure from five leaves onward.** Put \(z_*=1+1/\eta=3+2\sqrt2\). If \(z>z_*\), evaluate the hub diagonal at \(h=w_*/(uz)\):
\[
P_{00}(h)=\frac{1-(z-1)\eta}{z}<0.
\]
If instead \(1<z\le z_*\), evaluate a leaf diagonal at \(h=w_*/u\). From \((r(zw_*)-1)/z=-w_*F(zw_*)\), strict decrease of \(F\) implies
\[
\begin{aligned}
mP_{jj}(h)
&=1-(m-1)\eta-w_*F(zw_*)\\
&\le1-4\eta-w_*F(z_*w_*)\\
&=\frac{297-211\sqrt2}{98}<0.
\end{aligned}
\]
The last sign is exact: \(2\cdot211^2=89042>88209=297^2\). These two cases exhaust all positive rate ratios and prove sharpness of the vertex threshold.

**6. Recovery.** The off-diagonal formulas and continuity imply entrywise nonnegativity near \(h=0\), with strictly positive diagonal entries. As \(h\to\infty\), both \(r(w)\) and \(r(zw)\) tend to zero, so \(P(h)\to\mathbf1\pi^{\mathsf T}\), whose entries are all strictly positive. Consequently every star with \(m\ge5\) has at least one bounded intermediate interval of nonpositive endpoint behavior, regardless of its positive rate ratio. No claim is made that there is exactly one forbidden interval.

## Verification

The accompanying standalone `verify.py` recomputes the stability function from the Butcher tableau, verifies the exact radicals and derivative identities symbolically, and compares the spectral-entry expressions with direct matrix Runge–Kutta stages on randomized stars. Running `python verify.py` with Python 3, SymPy and NumPy passed 2,827 assertions, including 420 full matrix cases. These finite checks are diagnostics; the all-dimension and all-rate quantifiers follow from the preceding inequalities rather than from sampling.

## Relationship to prior work

Alexander introduced the two-stage strongly stable diagonal-implicit method in 1977; an openly available implementation specification provides its tableau and stability function. Kocsis and Németh (arXiv:1409.8583, initially public September 30, 2014) analyze optimal SSP radii for classes of diagonally implicit Runge–Kutta methods, not graph-dependent rate-tuned star positivity. Horváth (1998) gives positivity radii and conditional guarantees for general problem classes but does not state the present reversible-star six-state existential/universal cutoff. Blanes, Iserles and Macnamara (arXiv:2102.08242) explain the general high-order positivity barrier and motivate alternative positivity-preserving methods, not this sharp restricted-family classification.

Known method-wide order barriers do not imply that a fixed graph family admits *some* unconditionally positive rate selection at small dimensions. The previous analyses of other rational integrators on stars or of SDIRK positivity on different Markov families do not entail the exact \(m=5\) transition for Alexander's rational function. The spectral calculations and explicit negative certificate here are required to distinguish the methods.

## Limitations

Only stars with identical outgoing rate on every spoke in each direction are addressed. Distinct spoke rates, other graphs, all individual internal stages, and the number of disconnected forbidden timestep intervals are not classified. The method's 1977 original full text was not accessible in the consulted copy; comparison relies on its available abstract and verified tableau. Possible specialized older sources not indexed by the searches remain an originality risk. This result has not received an independent mathematical audit.

## References

1. R. Alexander, “Diagonally Implicit Runge–Kutta Methods for Stiff O.D.E.'s,” *SIAM Journal on Numerical Analysis* **14** (1977), 1006–1021. DOI: https://doi.org/10.1137/0714068.
2. T. A. Kocsis and A. Németh, “Optimal second order diagonally implicit SSP Runge–Kutta methods,” arXiv:1409.8583 (first public September 30, 2014). https://arxiv.org/abs/1409.8583.
3. Z. Horváth, “Positivity of Runge–Kutta and diagonally split Runge–Kutta methods,” *Applied Numerical Mathematics* **28** (1998), 309–326. DOI: https://doi.org/10.1016/S0168-9274(98)00050-6.
4. S. Blanes, A. Iserles and S. Macnamara, “Positivity-preserving methods for ordinary differential equations,” arXiv:2102.08242 (2021). https://arxiv.org/abs/2102.08242.
5. Cardinal software documentation, “LStableDirk2,” https://cardinal.cels.anl.gov/source/timeintegrators/LStableDirk2.html (tableau and stability function).

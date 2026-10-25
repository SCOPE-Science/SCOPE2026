# Reentrant endpoint positivity of three-stage RKL2 on a minimal Markov chain

## Finding

For the three-stage, second-order Runge–Kutta–Legendre (RKL2) method, there is a conservative three-state continuous-time Markov generator for which the end-step matrix is nonnegative on **two disjoint closed intervals of positive step lengths**. In the normalization below, the exact positivity set is

\[
\mathcal P_3=[0,(5-\sqrt5)/2]\;\cup\;[(5+\sqrt5)/2,15/4].
\]

The phenomenon is minimal in **both** stage count and Markov state count: for the two-stage RKL2 method on every finite-state continuous-time Markov generator, the set of positive step sizes giving an entrywise-nonnegative end-step matrix is an initial interval; the same is true for the three-stage RKL2 method on every generator with at most two states. The loss–recovery–loss pattern persists under sufficiently small perturbations of the two positive birth rates of the three-state witness.

## Assumptions and scope

All matrices are real. A finite-state continuous-time Markov generator \(Q\) has nonnegative off-diagonal entries and row sums zero; row probability distributions evolve by multiplication on the right by \(e^{hQ}\). An **endpoint-positive** step satisfies \(R_s(hQ)\ge0\) entrywise and hence maps every row probability distribution to another. Nothing here asserts nonnegativity of the method's internal stages.

Write the three-stage RKL2 stability polynomial in its standard normalization,

\[
R_3(z)=\frac7{12}+\frac5{12}L_3(1+2z/5)
=1+z+\frac{z^2}{2}+\frac{z^3}{15},
\qquad L_3(x)=\frac{5x^3-3x}{2}.
\]

Its negative-real-axis stability interval includes \([-5,0]\). The two-stage, order-two RKL2 polynomial is \(R_2(z)=1+z+z^2/2\). The specific witness is the three-state pure-birth generator

\[
Q=\begin{pmatrix}-1&1&0\\0&-1&1\\0&0&0\end{pmatrix}.
\]

The assertions concern all \(h\ge0\). Positive semigroup evolution \(e^{hQ}\) holds for every \(h\ge0\), including step lengths at which the polynomial approximation is not positive.

## Proof

**1. Exact three-state calculation.** Matrix multiplication gives

\[
Q^2=\begin{pmatrix}1&-2&1\\0&1&-1\\0&0&0\end{pmatrix},\qquad
Q^3=\begin{pmatrix}-1&3&-2\\0&-1&1\\0&0&0\end{pmatrix}.
\]

Therefore, with \(r(h)=1-h+h^2/2-h^3/15\),

\[
R_3(hQ)=\begin{pmatrix}
r(h)&h(1-h+h^2/5)&h^2(1/2-2h/15)\\
0&r(h)&1-r(h)\\
0&0&1
\end{pmatrix}.
\]

Every row sums to one. For \(0\le h\le5\), the polynomial representation implies \(1/6\le r(h)\le1\), because \(|L_3(x)|\le1\) on \([-1,1]\): this last elementary bound follows by checking the endpoints and the critical points \(x=\pm1/\sqrt5\) of \(L_3\). Thus the diagonal and \((2,3)\) entries are nonnegative throughout the interval containing every candidate nonnegative step.

The \((1,2)\) entry factors as

\[
h(1-h+h^2/5)=\frac h5\left(h-\frac{5-\sqrt5}{2}\right)
\left(h-\frac{5+\sqrt5}{2}\right).
\]

It is nonnegative precisely on \([0,(5-\sqrt5)/2]\cup[(5+\sqrt5)/2,\infty)\). The \((1,3)\) entry equals \(h^2(15-4h)/30\) and is nonnegative precisely when \(0\le h\le15/4\). Since \((5+\sqrt5)/2<15/4<5\), their intersection gives exactly the claimed two-interval set. For \(h>15/4\) the \((1,3)\) entry is negative, so no further positivity is possible.

At \(h=3\) the \((1,2)\) entry is \(-3/5\), at \(h=37/10\) every entry is nonnegative, and at \(h=4\) the \((1,3)\) entry is \(-8/15\). All three steps lie within \([0,5]\), so the sign change is not explained by leaving the usual scalar stability interval.

**2. Two stages forbid a return on any finite Markov chain.** For any such \(Q\), since \((Q^2)_{ii}=q_{ii}^2+\sum_{k\ne i}q_{ik}q_{ki}\ge q_{ii}^2\),

\[
(R_2(hQ))_{ii}\ge1+hq_{ii}+\frac{h^2q_{ii}^2}{2}
=\frac{1+(1+hq_{ii})^2}{2}>0.
\]

For \(i\ne j\),

\[
(R_2(hQ))_{ij}=h\left(q_{ij}+\frac h2(Q^2)_{ij}\right).
\]

If \(q_{ij}=0\), then \((Q^2)_{ij}=\sum_{k\ne i,j}q_{ik}q_{kj}\ge0\), so this entry never becomes negative. If \(q_{ij}>0\), its nonnegativity for \(h\ge0\) describes an initial interval (possibly unbounded). Intersecting the finitely many entrywise conditions produces an initial interval. The one-stage forward-Euler polynomial has the same no-return property.

**3. Three stages forbid a return on at most two states.** Every nontrivial two-state generator can be written

\[
Q=\begin{pmatrix}-a&a\\b&-b\end{pmatrix},\qquad a,b\ge0,\quad \lambda=a+b>0.
\]

Because \(Q^2=-\lambda Q\),

\[
R_3(hQ)=I+\frac{1-r(\lambda h)}{\lambda}Q.
\]

Its off-diagonal entries are nonnegative for all \(h\ge0\), since

\[
1-r(z)=z(1-z/2+z^2/15)\ge0\quad (z\ge0),
\]

and the quadratic is strictly positive (negative discriminant). For \(0\le z\le5\), \(r(z)\ge1/6\) and both diagonal entries are positive. For \(z\ge5\), \(r'(z)=-1+z-z^2/5<0\), so each diagonal condition \((b+ar(z))/\lambda\ge0\), \((a+br(z))/\lambda\ge0\) can cross from positive to negative at most once and cannot recover. Hence the joint positivity set is an initial interval. The zero generator and one-state cases are immediate. Combined with step 2 and the three-state witness, this proves simultaneous minimality.

**4. Robustness.** Replace the witness by

\[
Q_{a,b}=\begin{pmatrix}-a&a&0\\0&-b&b\\0&0&0\end{pmatrix},\qquad a,b>0.
\]

At \((a,b)=(1,1)\), all entries not forced to be zero by the upper-triangular pattern are strictly positive at \(h=37/10\), while the \((1,2)\) entry is strictly negative at \(h=3\) and the \((1,3)\) entry strictly negative at \(h=4\). Polynomial dependence on \(a,b\) makes all these strict signs persist on a common open neighborhood of \((1,1)\). Every such nearby generator therefore exhibits a loss, restoration, and second loss of endpoint positivity as the step increases.

## Verification

The standalone standard-library Python file `verify.py` forms matrix polynomials with exact rational arithmetic. Its saved output `verification_output.txt` records 54,712 passed rational assertions checking the displayed matrix identity, representative positive/negative steps, stochastic row sums, the two-stage structural identities on random finite generators, the two-state reduction, and unequal-rate robustness. The assertions are regression checks, not substitutes for the all-dimension proofs above. Reproduce by running `python verify.py`.

## Relationship to prior work

Aggul, Francisquez, Reynolds, and Amihere (2026) examine RKL and other super-time-stepping methods for discontinuous-Galerkin and finite-difference diffusion discretizations; their stability and adaptivity results do not imply an entrywise positivity classification on directed three-state Markov generators. Tan, Aslam, and Bertozzi (2025/2026) establish RKL monotonicity under constant-coefficient heat-equation spatial structures on infinite and periodic domains. Those spatial hypotheses do not include the one-way pure-birth generator used here. The formula for the RKL stability polynomial is standard and is not claimed as new.

Earlier finite-Dirichlet-path results for the same RKL polynomial characterize a different symmetric boundary-discretization problem and do not imply the two separated positivity intervals or the all-generator low-stage/low-state impossibility results. Dawes (2021) discusses loss of positivity near Dirichlet boundaries, but only its abstract was accessible here; that incomplete comparison remains a priority risk. Work on SSP-SDIRK2(2) and the \([2/2]\) Padé map concerns distinct rational end-step maps and likewise does not entail the specific RKL2 classification.

## Limitations

The conclusion concerns **endpoint nonnegativity**, not positivity of each internal RKL stage, or nonlinear strong-stability preservation. The robust perturbation statement applies to the directed three-state rate family, not to arbitrary spatial discretizations. The RKL polynomial is applied to a generator with a zero eigenvalue, as required for Markov mass conservation. Nothing here establishes finite-precision stability, nonlinear order conditions beyond those already built into RKL2, or priority over inaccessible papers. The claimed originality is restricted to the combined exact phase diagram and minimal-stage/minimal-state statements.

## References

1. M. Aggul, M. Francisquez, D. R. Reynolds, and S. Amihere, *Super Time Stepping Methods for Diffusion using Discontinuous-Galerkin Spatial Discretizations*, arXiv:2601.14508v1, first public 2026-01-20, https://arxiv.org/abs/2601.14508.
2. Z. Tan, T. D. Aslam, and A. L. Bertozzi, *Explicit Monotone Stable Super-Time-Stepping Methods for Finite Time Singularities*, arXiv:2507.17062, first public 2025-07-22, https://arxiv.org/abs/2507.17062.
3. A. S. Dawes, *Some properties of the Runge-Kutta-Legendre super-time-stepping explicit methods*, Computers & Fluids 214 (2021), 104762, doi:10.1016/j.compfluid.2020.104762 (abstract inspected; complete text unavailable).
4. F. Le Floc'h, *Instabilities of Super-Time-Stepping Methods on the Heston Stochastic Volatility Model*, arXiv:2309.00540, https://arxiv.org/abs/2309.00540.
5. B. Vaidya et al., *Scalable explicit implementation of anisotropic diffusion with Runge–Kutta–Legendre super time stepping*, Monthly Notices of the Royal Astronomical Society 472 (2017), 3147–3160.

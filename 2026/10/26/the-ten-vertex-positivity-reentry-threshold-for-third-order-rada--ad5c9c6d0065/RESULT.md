# The ten-vertex positivity-reentry threshold for third-order Radau diffusion on cycles

## Finding

For every integer \(n\ge3\), let \(C_n\) be the unweighted undirected cycle, \(L_n=2I-A(C_n)\) its Laplacian, and consider the two-stage, third-order Radau IIA completed diffusion step
\[
T_n(h)=(6I-2hL_n)(6I+4hL_n+h^2L_n^2)^{-1},\qquad h\ge0.
\]
Then \(T_n(h)\) has row sums one and the following sharp positivity classification.

1. If \(3\le n\le9\), then \(T_n(h)\) has strictly positive entries for every \(h>0\).
2. If \(n=10\), then \(T_{10}(h)\) is entrywise nonnegative exactly for \(h=0\) and for \(h\ge\tau\), where \(\tau=0.108723395070995\ldots\) is the unique positive root of
\[
10h^5+255h^4+936h^3+954h^2+216h-36=0.
\]
At \(h=\tau\), exactly the ten opposite-vertex entries vanish; every other entry is strictly positive. For \(0<h<\tau\), those entries are strictly negative.
3. For every integer \(n\ge11\), the entries between vertices at distance five are strictly negative for all sufficiently small \(h>0\), although every entry is strictly positive for all sufficiently large \(h\).

Thus \(C_{10}\) is the smallest *unweighted cycle* whose two-stage Radau IIA completed-step matrix loses entrywise positivity, and its nonnegative timestep set has a separated isolated zero and positive half-line.

## Assumptions and scope

All cycle edges have unit conductance. The vertices are indexed by \(\mathbb Z/n\mathbb Z\); \(A(C_n)\) is the usual adjacency matrix (for \(C_3\) it is the triangle). The timestep \(h\) is real and nonnegative. Nonnegative means all completed-step matrix entries are at least zero, not positivity of the Runge–Kutta internal stages. There are no conditions on input vectors beyond nonnegativity for the implication \(T_n(h)x\ge0\). No claim is made about weighted cycles, arbitrary graphs, or complete timestep positivity sets when \(n\ge11\).

## Proof

The two-stage Radau IIA stability function is
\[
R(z)=\frac{1+z/3}{1-2z/3+z^2/6}=\frac{6+2z}{6-4z+z^2}.
\]
For the diffusion equation \(x'=-L_nx\), its completed-step matrix is \(R(-hL_n)=T_n(h)\). The denominator \(M_n(h)=6I+4hL_n+h^2L_n^2\) is symmetric positive definite for every \(h\ge0\), since each Laplacian eigenvalue \(\lambda\ge0\) contributes \(6+4h\lambda+h^2\lambda^2>0\). The constant vector is an eigenvector with eigenvalue one under \(T_n(h)\), giving row sums one.

**Finite positive region, \(3\le n\le9\).** Translation and reflection symmetries of the cycle reduce all entries to \(\lfloor n/2\rfloor+1\) rational functions \(t_{n,d}(h)=[T_n(h)]_{0,d}\). Exact inversion of \(M_n(h)\) over \(\mathbb Q(h)\) gives \(t_{n,d}=P_{n,d}/Q_{n,d}\), with numerator and denominator expressed as integer-coefficient polynomials. The complete normalized coefficient vectors are recorded in `coefficients.json`. For every \(3\le n\le9\) and \(0\le d\le\lfloor n/2\rfloor\), every coefficient of \(Q_{n,d}\) is strictly positive, every coefficient of \(P_{n,d}\) is nonnegative, and \(P_{n,d}\) is nonzero. These **finite exact polynomial inequalities**, independently recomputed from the explicitly defined matrices by `verify.py`, prove \(t_{n,d}(h)>0\) whenever \(h>0\). The certificate includes all \(32\) symmetry-distance expressions for \(3\le n\le10\); it is not a floating-point enumeration of timesteps.

**The first failure and exact reentry, \(n=10\).** Write
\[
D(h)=(8h^2+8h+3)(h^4+12h^3+58h^2+72h+36)
(25h^4+100h^3+170h^2+120h+36).
\]
Every factor of \(D(h)\) is strictly positive for \(h\ge0\). Exact rational inversion gives, for opposite vertices,
\[
t_{10,5}(h)=\frac{2h^5(10h^5+255h^4+936h^3+954h^2+216h-36)}{D(h)}.
\]
The other five distance classes \(t_{10,d}\), \(0\le d\le4\), have numerators with strictly nonnegative coefficients and a nonzero positive coefficient, and denominators with strictly positive coefficients; the full exact rational expressions are in `coefficients.json` and checked by `verify.py`. Thus each of those classes is positive for every \(h>0\). The displayed quintic has precisely one positive root by Descartes' rule of signs (its nonzero coefficients, in descending order, have one sign change); it is negative at zero and positive at infinity. Further, its values at \(1/10\) and \(1/9\) have opposite signs, isolating \(\tau\in(1/10,1/9)\). This gives the complete asserted positivity set, including endpoints. At exactly \(h=1/10\), the opposite-vertex entry equals \(-3544/384641341535<0\).

**All larger cycles.** The scalar Taylor expansion is
\[
R(-x)=1-x+\tfrac12x^2-\tfrac16x^3+\tfrac1{36}x^4+\tfrac1{108}x^5+O(x^6).
\]
For vertices \(u,v\) with graph distance five in \(C_n\), every \((L_n)^k_{uv}=0\) for \(0\le k<5\). At \(k=5\), every contributing walk is a shortest five-edge path, each with the sign \((-1)^5\). There are exactly two such paths for the antipodal pair when \(n=10\), and one such path for a distance-five pair whenever \(n\ge11\). Hence
\[
[T_n(h)]_{uv}=-\frac{m}{108}h^5+O_n(h^6),\quad
m=\begin{cases}2,&n=10,\\1,&n\ge11.\end{cases}
\]
This establishes strict negativity for all sufficiently small positive steps. Finally, because \(R(0)=1\) and \(R(-x)\to0\) as \(x\to+\infty\), the spectral decomposition of the connected graph Laplacian yields \(T_n(h)\to\mathbf1\mathbf1^{\mathsf T}/n\) as \(h\to\infty\). Each matrix entry therefore eventually becomes positive. This does not assert that the intervening positivity set is connected for \(n\ge11\).

## Verification

Run `python verify.py` with SymPy installed as specified in `requirements.txt`, in the directory containing `coefficients.json`. The script derives the transition entries from exact symbolic cycle Laplacians, checks equality with every independent integer-polynomial coefficient pair in the certificate, checks coefficient sign constraints for all \(3\le n\le9\) and all noncritical \(C_{10}\) distances, checks the explicit \(C_{10}\) quintic formula and its exact negative rational witness, and reconstructs the fifth-order Taylor coefficient. It does not enumerate infinitely many timesteps or graph sizes: those domains are handled by coefficient positivity, Descartes' rule, and the graph-distance argument.

## Relationship to prior work

Zappavigna, Colaneri, Kirkland and Shorten investigate positivity loss under Padé discretizations and supply general sufficient positivity criteria for diagonal Padé approximants [1]. In particular, their theorem about sufficiently short timesteps treats Hurwitz Metzler matrices and diagonal rational approximants; it neither concerns the present conservative graph Laplacians with a zero eigenvalue nor supplies a Radau IIA exact cycle-order threshold. The two-stage Radau IIA rational function and its third-order status are documented in [2]. The result here is a sharp graph-family boundary and a complete, reentrant positivity interval at the first failing cycle, neither a general assertion about all Markov generators nor a consequence of A-stability.

## Limitations

Only unit-rate undirected cycles and the *completed* third-order Radau IIA step are covered. The full timestep positivity sets beyond order ten are not classified. The exact finite certificate needs SymPy for convenient replay; its coefficients and all matrix definitions are included for mathematical inspection. Published specialized equivalences that are not discoverable in the inspected sources remain a literature risk. Independent review has not yet been performed.

## References

[1] A. Zappavigna, P. Colaneri, S. Kirkland and R. Shorten, *Essentially Negative News About Positive Systems*, preprint publicly deposited 2012-06-19, https://mural.maynoothuniversity.ie/id/eprint/3761/1/SK_Essentially_Negative.pdf .

[2] D. I. Ketcheson, *Numipedia: Radau IIA2*, method tableau and stability function, https://ketch.github.io/numipedia/methods/RadauIIA2.html .

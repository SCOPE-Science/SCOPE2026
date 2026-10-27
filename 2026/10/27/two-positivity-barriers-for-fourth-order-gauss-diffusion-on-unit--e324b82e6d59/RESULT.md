# Two positivity barriers for fourth-order Gauss diffusion on unit paths

## Finding
Let \(P_n\) be the unit-conductance path with vertices \(0,\ldots,n-1\), where \(n\ge2\). Let \(L_n\) be its combinatorial Laplacian and let
\[
T_n(h)=(I-\tfrac h2L_n+\tfrac{h^2}{12}L_n^2)
          (I+\tfrac h2L_n+\tfrac{h^2}{12}L_n^2)^{-1},\qquad h\ge0.
\]
This is the completed two-stage, fourth-order Gauss–Legendre heat step. The following is a single path-family classification of distinct sign obstructions and exact benchmark cases.

1. On the two- and three-vertex paths, \(T_n(h)\) is entrywise nonnegative for every \(h\ge0\).
2. On the four-vertex path, the positivity region is exactly
\[
 T_4(h)\ge0\ \text{entrywise}\quad\Longleftrightarrow\quad0\le h\le\rho_4,
\]
where \(\rho_4\approx11.8663785439266\) is the unique positive root of
\[
 q_4(h)=h^4-6h^3-60h^2-108h-72.
\]
3. Every path with \(n\ge4\) loses entrywise positivity at all sufficiently large steps, with the explicit asymptotic witness
\[
 (T_n(h))_{0,1}=-\frac{2(n-1)(2n-7)}{nh}+O(h^{-2})\quad(h\to\infty).
\]
4. Every path with \(n\ge8\) also loses entrywise positivity at all sufficiently small positive steps:
\[
 (T_n(h))_{0,7}=-\frac{h^7}{1728}+O(h^8)\quad(h\downarrow0).
\]
Nevertheless, \(T_8(4)\) is strictly positive entrywise: its minimum is exactly \(596772/61423369\). Consequently, even on a **symmetric, conservative, irreducible nearest-neighbor diffusion**, the fourth-order Gauss step can be nonpositive for all sufficiently small positive steps, strictly positive at an intermediate step, and nonpositive again for all sufficiently large steps.

## Assumptions and scope
The underlying ODE is \(\dot u=-L_nu\); all \(n-1\) edges have unit conductance, and time is measured in reciprocal-conductance units. The boundary vertices have degree one, the interior vertices degree two, and there are no Dirichlet sinks. The step is a rational matrix function; it is symmetric and row-stochastic whenever it is entrywise nonnegative. The denominator is nonsingular for every \(h\ge0\), since each Laplacian eigenvalue \(\lambda\ge0\) gives \(1+h\lambda/2+h^2\lambda^2/12>0\). No claim is made about internal Runge–Kutta stages or arbitrary weighted paths.

## Proof
**One- and two-step positivity benchmarks.** Write
\[
 r(-z)=\frac{1-z/2+z^2/12}{1+z/2+z^2/12}.
\]
For \(n=2\), the off-diagonal entry is \(3h/(h^2+3h+3)>0\) for \(h>0\), and the diagonal entry is \((h^2+3)/(h^2+3h+3)>0\). For \(n=3\), the distinct off-diagonal entries are
\[
(T_3)_{0,1}=\frac{4h}{3h^2+6h+4},\qquad
(T_3)_{0,2}=\frac{8h^2(2h+3)}{(h^2+6h+12)(3h^2+6h+4)},
\]
and the central diagonal entry is \((3h^2-2h+4)/(3h^2+6h+4)>0\). The endpoint diagonal numerator, over the same product denominator, is \(3h^4+4h^3+28h^2+48h+48>0\). Reflection supplies all remaining entries. The value at \(h=0\) is the identity.

**Four-node exact threshold.** Put
\[
D(h)=2(h^2+3h+3)(h^4+12h^3+54h^2+72h+36)>0.
\]
Direct rational matrix inversion gives
\[
\begin{aligned}
D(T_4)_{0,1}&=-3h q_4(h),\\
D(T_4)_{0,2}&=9h^2(h^3+6h^2+16h+12),\\
D(T_4)_{0,3}&=3h^3(5h^2+18h+12),\\
D(T_4)_{1,2}&=3h(h^4+6h^3+24h^2+72h+72).
\end{aligned}
\]
Reflection gives \((T_4)_{2,3}=(T_4)_{0,1}\) and \((T_4)_{1,3}=(T_4)_{0,2}\). The endpoint and interior diagonal numerators, respectively, are
\[
\begin{aligned}
&2h^6+9h^5+60h^4+180h^3+396h^2+432h+216,\\
&2h^6+21h^5+96h^4+144h^3+180h^2+216h+216,
\end{aligned}
\]
so they are positive. Hence the only possibly negative entries are the two outermost adjacent pairs, and their sign for \(h>0\) is opposite to \(q_4(h)\). This quartic has exactly one sign change in its descending coefficient list; by Descartes' rule it has at most one positive root. Because \(q_4(0)<0\) and \(q_4(h)\to+\infty\), it has exactly one, proving the iff statement.

**All-path large-step obstruction.** Spectral calculus yields
\[
T_n(h)=I-\frac{12}{h}L_n^++O(h^{-2})\qquad(h\to\infty),
\]
where \(L_n^+\) is the Moore–Penrose inverse; the constant mode contributes the identity because \(r(0)=1\). For the unit path, effective resistance between vertices \(i,j\) is \(|i-j|\). The standard resistance/pseudoinverse identity, also derived by imposing zero row sums on \(L_n^+\), gives
\[
(L_n^+)_{ij}=\frac{s_i+s_j}{2n}-\frac{|i-j|}{2}-\frac{n^2-1}{6n},
\qquad s_i=\sum_{k=0}^{n-1}|i-k|.
\]
For \(i=0,j=1\), \(s_0+s_1=(n-1)^2+1\), hence
\[
 (L_n^+)_{0,1}=\frac{(n-1)(2n-7)}{6n}>0\qquad(n\ge4).
\]
The asserted negative large-step asymptotic follows. This is an infinite-family argument, not a finite-size extrapolation.

**Eight-node small-step obstruction and exact return to positivity.** Taylor expansion gives
\[
r(z)=1+z+\frac{z^2}{2}+\frac{z^3}{6}+\frac{z^4}{24}+\frac{z^5}{144}
      +0\,z^6-\frac{z^7}{1728}+O(z^8).
\]
Let \(Q=-L_n\). For \(n\ge8\), the graph distance from node \(0\) to node \(7\) is seven. Thus \((Q^k)_{0,7}=0\) for \(k<7\), while \((Q^7)_{0,7}=1\): the only seven-step walk is the directed traverse of seven successive unit-rate edges. Substitution into \(r(hQ)\) gives the stated strictly negative leading term.

For \(n=8\), exact integer arithmetic yields \(T_8(4)=N/61423369\). The first four rows of \(N\) are
\[
\begin{pmatrix}
22767445&7237548&12586536&8978304&5124384&2634048&1318656&776448\\
7237548&28116433&3629316&8732616&6487968&3808992&2091840&1318656\\
12586536&3629316&24262513&1138980&7417224&5945760&3808992&2634048\\
8978304&8732616&1138980&22947121&596772&7417224&6487968&5124384
\end{pmatrix}.
\]
The remaining four rows are determined by \(N_{ij}=N_{7-i,7-j}\). All displayed entries are strictly positive, and their minimum, shared with the reflected rows, is \(596772\). The analytic small- and large-step obstructions therefore enclose an interval of strictly positive matrices around \(h=4\), by continuity.

## Verification
The accompanying `artifacts/verify_gauss_path.py` uses exact symbolic arithmetic to reconstruct the completed stability map, verify the Taylor coefficients, all four-node rational factorizations, the unique positive root bracket, the eight-node integer certificate, every row sum of that certificate, and finite instances of the pseudoinverse identity. It ran successfully in the delivered package. In particular, the eight-node witness is an exact rational equality, not a floating-point observation. The claims for arbitrarily many nodes follow from the walk-count and pseudoinverse proofs above, not from numerical enumeration.

## Relationship to prior work
Zappavigna, Colaneri, Kirkland and Shorten showed in 2012 that the \([2/2]\) Padé approximant need not preserve positivity, using an eight-dimensional nilpotent one-directional shift, and derived general sufficient conditions for positivity of higher diagonal Padé maps. Their Section 4 also explicitly identifies the negative seventh Taylor coefficient. The present theorem does **not** claim that coefficient or general arbitrarily-small-step positivity failure as new. Its additional content concerns a reversible, mass-conserving, undirected path; an exact four-node cutoff; and an exact intermediate positive eight-node step sandwiched between two failures. The 2012 proof neither specifies these path matrices nor its claimed interval.

Lóczi and Ketcheson's 2014 study of maximal absolute-monotonicity radii gives method-level restrictions, not exact matrix entries for unit paths. A published eight-state Markov-chain result uses an absorbing pure-birth generator and proves its nonmonotone stochasticity window and the general lower dimension bound. That directed generator is not similar to the symmetric path generator; its result does not imply the positive certificate or the four-node threshold here. The established small-step lower bound for general systems of at most seven states is background, not a new contribution here.

## Limitations
The step-size positivity set is classified completely only for the four-node path, not for every \(n\). For \(n\ge8\) the theorem proves small- and large-step failure, and provides an exact interior positive witness for \(n=8\); it does **not** assert that all larger paths regain positivity, nor claim exact transition times for those paths. The fourth-order Gauss method retains A-stability and mass conservation even where entrywise positivity fails. Literature comparisons cannot logically exclude every unindexed specialized prior result, particularly implicit applications of general matrix-function positivity theorems.

## References
1. A. Zappavigna, P. Colaneri, S. Kirkland, R. Shorten, *Essentially Negative News About Positive Systems*, 2012 preprint, deposited 19 June 2012. https://mural.maynoothuniversity.ie/id/eprint/3761/ (full text available at its repository link).
2. L. Lóczi, D. I. Ketcheson, *Rational functions with maximal radius of absolute monotonicity*, LMS Journal of Computation and Mathematics **17** (2014), 159–205; public arXiv version dated 26 March 2013, arXiv:1303.6651, doi:10.1112/S1461157013000326.
3. *Eight-state barrier for Markov positivity of the [2/2] Padé map*, publicly available 2026 result and proof, https://github.com/Resultary/2026/tree/main/2026/9/20/SCOPE-eight-state-pade-markov-positivity-barrier--4aad2a3f58ab .

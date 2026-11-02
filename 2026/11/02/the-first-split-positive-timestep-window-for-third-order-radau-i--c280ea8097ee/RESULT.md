# The first split positive-timestep window for third-order Radau IIA on directed cycles

## Finding

Let \(S_n\) be the forward cyclic permutation matrix on \(n\) states and let \(Q_n=S_n-I_n\), the generator of the unit-rate directed continuous-time Markov cycle. For every integer \(2\le n\le8\) and every real timestep \(h\ge0\), apply the unmodified two-stage, third-order Radau IIA endpoint map
\[
M_n(h)=R(hQ_n),\qquad R(z)=\frac{6+2z}{6-4z+z^2}.
\]
The matrix always has row sums one. Its exact entrywise-nonnegativity sets are
\[
\begin{array}{c|l}
 n&\{h\ge0:M_n(h)\ge0\text{ entrywise}\}\\ \hline
 2,3,4,5 &[0,\infty)\\
 6 &\{0\}\cup[\rho_6,\infty)\\
 7 &\{0\}\cup[\rho_7,\infty)\\
 8 &\{0\}\cup[\alpha,\beta]\cup[\gamma,\infty).
\end{array}
\]
Here \(\rho_6\) and \(\rho_7\) are the unique positive zeros of
\[
\begin{split}
 H_6(h)&=h^5+15h^4+60h^3+90h^2+36h-12,\\
 H_7(h)&=h^6+18h^5+90h^4+180h^3+108h^2-72h-72.
\end{split}
\]
The eight-state thresholds \(\alpha\), \(\beta\), and \(\gamma\) are characterized by the following two integer polynomials:
\[
\begin{aligned}
 T(h)&=h^7+21h^6+126h^5+315h^4+252h^3-252h^2-504h-198,\\
 U(h)&=h^{14}+7h^{13}-21h^{12}-343h^{11}-1351h^{10}-2142h^9+3094h^8\\
 &\quad+30286h^7+103278h^6+228564h^5+359100h^4+403704h^3\\
 &\quad+312984h^2+151632h+34992.
\end{aligned}
\]
Precisely, \(\alpha\) is the unique positive root of \(T\), while \(\beta<\gamma\) are the two positive roots of \(U\). Exact rational isolating intervals and useful decimal approximations are
\[
\begin{aligned}
&1.106<\alpha<1.107,&&\alpha\approx1.1068886282141903,\\
&3.297<\beta<3.298,&&\beta\approx3.2971342023798575,\\
&7.042<\gamma<7.043,&&\gamma\approx7.0423186961594336.
\end{aligned}
\]
In particular, among directed cycles of size \(2\) through \(8\), the eight-cycle is the **first whose strictly positive admissible timesteps have two disjoint components**. This is a statement about endpoint stochasticity, not internal-stage positivity or accuracy.

## Assumptions and scope

The directed cycle has equal unit forward jump rates, no other transitions, and finite dimension in the specified range. The shift convention is \((S_n)_{i,i+1\pmod n}=1\); reversing the direction only permutes columns. A matrix is stochastic when all its entries are nonnegative and every row sums to one. The proof covers every real \(h\ge0\), not only a sampled grid. The claimed first-occurrence statement concerns the set of **strictly positive** valid timesteps: the isolated always-valid timestep \(h=0\) does not count as a component there.

## Proof

**1. Exact circulant coefficients.** Put \(\eta=i\sqrt2\), \(p=h+2+\eta\), \(\bar p=h+2-\eta\), and \(a=1-5\eta/2\). The poles of \(R\) are \(2\pm\eta\), with residues \(a\) and \(\bar a\). Since \(|p|>h\) for every \(h\ge0\), partial fractions and a convergent geometric series reduced modulo \(S_n^n=I_n\) give
\[
M_n(h)=\sum_{j=0}^{n-1}c_{n,j}(h)S_n^j,
\qquad
c_{n,j}(h)=\frac{h^jF_{n,j}(h)}{D_n(h)},
\]
where
\[
\begin{aligned}
D_n(h)&=(p^n-h^n)(\bar p^n-h^n)=|p^n-h^n|^2>0,\\
F_{n,j}(h)&=-a p^{n-j-1}(\bar p^n-h^n)-\bar a\bar p^{n-j-1}(p^n-h^n).
\end{aligned}
\]
Every \(F_{n,j}\) is a real integer polynomial, obtained without numerical approximation by expanding in the quadratic ring \(\mathbb Z[\eta]\), where \(\eta^2=-2\). Continuity supplies \(M_n(0)=I_n\). Because \(Q_n\mathbf1=0\) and \(R(0)=1\), row sums are one. For \(h>0\), entrywise nonnegativity is therefore equivalent to \(F_{n,j}(h)\ge0\) for all \(j\).

**2. Dimensions below eight.** Exact coefficient expansion gives nonnegative coefficients with positive constant terms for every \(F_{n,j}\) when \(2\le n\le5\). For \(n=6,7\), all \(F_{n,j}\) with \(1\le j\le4\) likewise have strictly positive coefficients. The diagonal numerators \(F_{6,0}\) and \(F_{7,0}\) are positive at zero and have no positive real roots: the exact Sturm sign-variation pairs \((V(0^+),V(+\infty))\) are respectively \((4,4)\) and \((4,4)\). For \(n=6\), the only remaining obstruction is \(F_{6,5}=36H_6\), and Descartes' sign rule plus a sign change certifies one positive zero \(0.208<\rho_6<0.209\). For \(n=7\), \(F_{7,5}\) and \(F_{7,6}=42H_7\) each have exactly one positive zero, with the former in \((0.208,0.209)\) and the latter in \((0.663,0.664)\). These disjoint brackets order the obstructions and give the first three cases.

**3. Exact eight-state sign certificate.** For \(n=8\), the numerators have \(F_{8,j}=48P_j\). The polynomials \(P_1,P_2,P_3,P_4\) have strictly positive coefficients. The remaining relevant polynomials are
\[
\begin{aligned}
P_5(h)&=h^9+17h^8+154h^7+777h^6+2394h^5+4662h^4\\
&\quad+5544h^3+3474h^2+540h-324,\\
P_6(h)&=h^8+19h^7+147h^6+567h^5+1197h^4+1260h^3\\
&\quad+252h^2-630h-378,\\
P_7(h)&=T(h),\qquad P_0(h)=U(h).
\end{aligned}
\]
Each of \(P_5,P_6,P_7\) has exactly one positive real root by Descartes' rule and its sign at zero and infinity. Exact rational evaluations place the roots, respectively, in
\[
(0.208,0.209),\quad(0.663,0.664),\quad(1.106,1.107).
\]
Thus the off-diagonal entries are all nonnegative exactly when \(h\ge\alpha\) (for \(h>0\)). The exact Sturm variation counts for \(P_0=U\) are \(V(0^+)=6\) and \(V(+\infty)=4\), certifying exactly two positive zeros. Their rational sign brackets are \((3.297,3.298)\) and \((7.042,7.043)\). Since \(U(0)>0\) and its leading coefficient is positive, the diagonal entry is negative exactly for \(\beta<h<\gamma\). Combining the conditions proves the complete eight-state domain and the asserted first split.

**4. Exactness of the certificates.** The Sturm variations, polynomial coefficients, isolating interval signs, and direct rational-matrix comparisons are reproduced by the included `verify_cycle.py`. In particular, the argument uses a finite, exact root-count proof for the fixed dimensions and does not infer a global sign law from finite sampling.

## Verification

Run `python verify_cycle.py` with the dependencies in `requirements.txt`. The verifier reconstructs all \(F_{n,j}\) and \(D_n\) by exact polynomial-pair arithmetic, tests their stochastic row-sum identity, computes the required Sturm variations and isolating signs using exact rational arithmetic, and independently compares the formulas against exact inversions of the original matrices at four rational timesteps in each dimension. It reports `VERIFY_OK 188 exact assertions` with SymPy. The algebraic root isolations are exact; the printed decimal approximations are illustrative only.

## Relationship to prior work

Zappavigna, Colaneri, Kirkland and Shorten (2012) show that Padé discretizations can lose positivity even at arbitrarily small steps. Their full manuscript treats a cyclic-feedback family, but its explicit eight-dimensional counterexample is a nilpotent open chain using the diagonal \([2/2]\) Padé approximation, not the two-stage Radau IIA \([1/2]\) endpoint on a recurrent directed cycle. Lóczi and Ketcheson (2013) provide the fundamental absolute-monotonicity context for rational time steppers, but do not derive these fixed-cycle positivity windows. A published eight-state absorbing-chain \([2/2]\) result concerns a different rational map and generator. None of these inspected statements logically supplies the three algebraic endpoints or first-split claim above; equivalence in unlocated specialist literature remains a residual risk.

## Limitations

Only uniform directed cycles of sizes \(2\) through \(8\) are classified. The result does not claim a general all-size phase diagram, nonuniform jump rates, internal-stage nonnegativity, or any numerical-error guarantee. In particular, a large step with a nonnegative endpoint matrix can be a poor approximation of the true Markov semigroup. Independent mathematical validation and exhaustive historical-literature coverage are not established.

## References

- A. Zappavigna, P. Colaneri, S. Kirkland and R. Shorten, *Essentially Negative News About Positive Systems*, manuscript deposited June 19, 2012. https://mural.maynoothuniversity.ie/id/eprint/3761/ (full preprint).
- L. Lóczi and D. I. Ketcheson, *Rational functions with maximal radius of absolute monotonicity*, arXiv:1303.6651, first posted March 26, 2013. https://arxiv.org/abs/1303.6651.
- *Eight-state barrier for Markov positivity of the [2/2] Padé map*, published result describing an absorbing-chain model. https://github.com/Resultary/2026/tree/main/2026/9/20/SCOPE-eight-state-pade-markov-positivity-barrier--4aad2a3f58ab (comparison by recovered claim summary; linked full text not accessible during this check).

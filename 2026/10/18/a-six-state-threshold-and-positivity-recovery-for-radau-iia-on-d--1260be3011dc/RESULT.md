# A six-state threshold and positivity recovery for Radau IIA on directed cycles

## Finding
Let \(n\ge2\) be an integer and let \(P_n\) be the cyclic permutation matrix with \((P_n)_{i,i+1\pmod n}=1\). Set \(Q_n=P_n-I\). On the rate-one one-way continuous-time Markov cycle, the completed two-stage, third-order Radau IIA step is
\[
 T_n(h)=R(hQ_n),\qquad R(z)=\frac{1+z/3}{1-2z/3+z^2/6},\qquad h\ge0.
\]
All these matrices exist and have unit row and column sums. The following describes sharp cyclic positivity phenomena.

**(i)** For \(2\le n\le5\), \(T_n(h)\) has strictly positive entries for every \(h>0\).

**(ii)** Let \(\tau\) be the unique positive root of
\[
 f(h)=h^5+15h^4+60h^3+90h^2+36h-12.
\]
For \(n=6\), the exact entrywise-nonnegativity set is
\[
 \{h\ge0:T_6(h)\ge0\}=\{0\}\cup[\tau,\infty),\qquad
 \tau=0.208608859735000\ldots.
\]
For \(0<h<\tau\), precisely the six cyclic entries at displacement five are negative and every other entry is strictly positive. At \(h=\tau\), those entries are zero; all entries are positive for \(h>\tau\). An exact witness is
\[
 (T_6(1/10))_{i,i+5}=-\frac{743849}{19268401151106}<0.
\]

**(iii)** For every \(n\ge6\), the cyclic displacement-five entry is negative for all sufficiently small positive \(h\), with the universal expansion
\[
 (T_n(h))_{i,i+5}=-\frac{h^5}{108}+O(h^6).
\]
For each fixed \(n\ge6\), all entries are nevertheless strictly positive for every sufficiently large \(h\). No complete intermediate-step classification is asserted for \(n\ge7\).

## Assumptions and scope
The cycle is directed in one direction with common unit transition rate; the generator \(Q_n\) has nonnegative off-diagonal entries and zero row sums. An arbitrary common rate \(r>0\) is handled by replacing \(h\) with \(rh\). Entrywise nonnegativity means the complete endpoint matrix preserves every nonnegative state, not that all internal Runge--Kutta stages preserve positivity. The minimal-six-state assertion is **within the family of uniform one-way directed cycles**, not among all Markov generators. The theorem concerns exact real arithmetic and nonnegative timesteps.

## Proof
**Well-defined update and conservation.** Multiplying numerator and denominator by six, write
\[
 D(P,h)=6+4h+h^2-(4h+2h^2)P+h^2P^2,
 \quad N(P,h)=6-2h+2hP,
 \quad T_n(h)=N(P_n,h)D(P_n,h)^{-1}.
\]
The poles of the scalar denominator of \(R\) are \(2\pm i\sqrt2\), both in the open right half-plane. The eigenvalues of \(hQ_n\) lie in the closed left half-plane. Thus the inverse exists for all \(h\ge0\). Since \(Q_n\boldsymbol1=0\), \(R(0)=1\) gives unit row sums; the circulant property gives unit column sums.

**Exact finite-cycle sign certificates.** For each \(2\le n\le6\), there are explicit integer polynomials \(p_{n,j}(h)\) and a positive polynomial \(\Delta_n(h)\) such that
\[
 T_n(h)=\frac{1}{\Delta_n(h)}\sum_{j=0}^{n-1}p_{n,j}(h)P_n^j.
\]
Every coefficient of every \(p_{n,j}\) is nonnegative, with at least one positive nonconstant coefficient at every displacement \(j\), for \(2\le n\le5\). For \(n=6\), these coefficient-sign properties hold for \(j=1,2,3,4\); the remaining two polynomials are
\[
\begin{split}
 p_{6,0}(h)={}&1296+3888h+5400h^2+4440h^3+2280h^4+664h^5\\
  &+26h^6-50h^7-5h^8+5h^9+h^{10},\\
 p_{6,5}(h)={}&h^5\bigl(h^5+15h^4+60h^3+90h^2+36h-12\bigr),
\end{split}
\]
with common denominator
\[
 \Delta_6(h)=(2h^2+4h+3)(h^4+4h^3+10h^2+24h+36)
 (3h^4+12h^3+22h^2+24h+12)>0.
\]
Every one of the integer polynomials and denominators for \(2\le n\le6\) is included as a complete finite array of coefficients, ordered by increasing power, in `verify.py`. That program checks, by exact integer polynomial multiplication, **all** the identities
\[
 \left(\sum_{j=0}^{n-1}p_{n,j}(h)P^j\right)D(P,h)
 \equiv N(P,h)\Delta_n(h)\pmod{P^n-1}
\]
for each \(n=2,3,4,5,6\) and every coefficient of \(h\). This finite collection of polynomial identities is a complete algebraic certificate, not a finite-sample inference. The common denominators are manifestly positive on \(h\ge0\) (their arrays have positive constant terms and nonnegative coefficients; the six-state factorization appears above).

It remains to check \(p_{6,0}(h)>0\) despite its two negative coefficients. If \(0<h\le1\), then \(-50h^7-5h^8\ge-55h^5\), and the positive \(664h^5\) term dominates. If \(h\ge1\), substitute \(h=1+t\) with \(t\ge0\): every coefficient of \(p_{6,0}(1+t)\) is strictly positive, as checked by exact binomial expansion in `verify.py`. The remaining five six-state numerators have the stated signs. Finally, \(f(0)=-12\) and \(f'(h)=5h^4+60h^3+180h^2+180h+36>0\) for \(h\ge0\). Hence \(f\) has exactly one positive zero and determines the complete six-state positivity set. The stated negative rational witness follows by substitution.

**Arbitrary cycle sizes: small steps and eventual recovery.** Taylor expansion of the stability function at zero gives
\[
 R(z)=1+z+\frac{z^2}{2}+\frac{z^3}{6}+\frac{z^4}{36}-\frac{z^5}{108}+O(z^6).
\]
In \((P_n-I)^k\), for \(k\le5\), a term at displacement five first appears when \(k=5\), with coefficient one, provided \(n\ge6\). Thus the \(h^5\) coefficient of \((T_n(h))_{i,i+5}\) is exactly \(-1/108\), with no contribution from lower powers. Analyticity at zero proves strict negativity for sufficiently small positive steps for each such \(n\).

For large steps, \(P_n\) is diagonalized by the discrete Fourier matrix. The eigenvalues of \(Q_n\) are \(e^{2\pi i k/n}-1\), of which only the \(k=0\) value vanishes; the other values have strictly negative real parts. Since \(R(0)=1\) and \(R(z)\to0\) as \(|z|\to\infty\), Fourier inversion yields
\[
 \lim_{h\to\infty}T_n(h)=\frac1n\boldsymbol1\boldsymbol1^{\mathsf T}.
\]
Every entry of the limit is positive, so entrywise strict positivity holds for all sufficiently large \(h\). These arguments prove all three assertions.

## Verification
Run `python3 verify.py` using a standard-library Python interpreter. The checker verifies the complete polynomial identities for \(2\le n\le6\), the critical factorization and sign bounds, exact evaluations of the five-step coefficient and rational witness, plus independent rational-matrix inversion at seven positive timesteps for each of those five cycle orders. A successful replay prints `VERIFY_OK 930 exact polynomial/matrix assertions; cycles n=2..6`. The arbitrary-order small-step and large-step statements are proved symbolically above; they are not extrapolated from those finite checks.

## Relationship to prior work
Hairer and Wanner's study of Radau methods gives the third-order two-stage stability function and explains the method's stiff decay properties. Zappavigna, Colaneri, Kirkland and Shorten (2010) study positivity losses and sampling restrictions under Padé discretization; their related 2012 analysis documents positivity failures, prominently including a different eight-state counterexample for diagonal Padé. The Radau stability function is of subdiagonal Padé type \([1/2]\), not the Gauss--Legendre diagonal \([2/2]\) map. Existing undirected-star and complete-bipartite Radau positivity classifications concern symmetric graph Laplacians, not this directed cyclic family. The exact six-state recovery root and cyclic minimality are not implied by those statements; nevertheless, an equivalent specialized classification in less-indexed literature is possible.

## Limitations
The classification is restricted to equal-rate one-way cycles, with exact complete steps. It does not claim a universal minimal dimension over all continuous-time Markov generators, stage positivity, or the complete nonnegativity set for \(n\ge7\). The finite polynomial certificate covers exactly \(n=2,3,4,5,6\). The method's lack of absolute monotonicity does not on its own establish the claimed six-state recovery threshold.

## References
1. E. Hairer and G. Wanner, *Stiff differential equations solved by Radau methods*, Journal of Computational and Applied Mathematics **111** (1999), 93–111, DOI 10.1016/S0377-0427(99)00134-X. Author preprint: https://www.unige.ch/~hairer/preprints/coimbra.pdf.
2. A. Zappavigna, P. Colaneri, S. Kirkland and R. Shorten, *On the preservation of co-positive Lyapunov functions under Padé discretization for positive systems*, MTNS 2010. Public repository deposit: 15 October 2010, https://mural.maynoothuniversity.ie/id/eprint/2195/.
3. A. Zappavigna, P. Colaneri, S. Kirkland and R. Shorten, *Essentially negative news about positive systems*, Linear Algebra and its Applications (2012). Author open-access manuscript: https://www.hamilton.ie/skirkland/pade_paper_final_end.pdf.
4. D. I. Ketcheson, *Numipedia: Radau IIA2*, https://ketch.github.io/numipedia/methods/RadauIIA2.html.

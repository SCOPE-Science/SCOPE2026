# A reversible eight-vertex path with an intermediate positive Gauss heat step

## Finding
Let \(L_n\) be the combinatorial Laplacian of the unit-conductance path \(0,\ldots,n-1\), and let \(T_n(h)\) be its completed fourth-order, two-stage Gauss–Legendre heat step:
\[
T_n(h)=(I-hL_n/2+h^2L_n^2/12)(I+hL_n/2+h^2L_n^2/12)^{-1},\qquad h\ge0.
\]
For every fixed \(n\ge4\), the endpoint-adjacent entry satisfies
\[
(T_n(h))_{0,1}=-\frac{2(n-1)(2n-7)}{nh}+O(h^{-2})\qquad(h\to\infty).
\]
On the eight-vertex path the step has a negative entry for all sufficiently small positive \(h\), is strictly positive entrywise at \(h=4\) with minimum \(596772/61423369\), and has a negative entry again for all sufficiently large \(h\). Strict positivity extends to an open interval containing \(4\). Thus a nonmonotone stochasticity region is possible for a conservative, irreducible, reversible nearest-neighbor diffusion, even at the general minimum dimension for arbitrarily small-step failure.

## Assumptions and scope
The ODE is \(\dot u=-L_nu\); both endpoints have degree one, all conductances are one, and there are no boundary sinks. The scalar denominator is positive on the nonnegative spectrum of \(hL_n\). The step is symmetric and has row and column sums one, even where it has negative entries. This concerns the completed step and does not assert anything about internal stages.

## Proof
Write \(R(z)=(1+z/2+z^2/12)/(1-z/2+z^2/12)\), so \(T_n(h)=R(-hL_n)\). The identity \(R(-z)=1-z/(1+z/2+z^2/12)\) and spectral calculus give \(T_n(h)=I-12L_n^+/h+O(h^{-2})\) for fixed \(n\), where \(L_n^+\) is the Moore–Penrose inverse; the zero mode is unchanged. If \(s_i=\sum_j |i-j|\), then the unit path's effective resistance \(|i-j|\), together with the zero row sums of \(L_n^+\), gives
\[
(L_n^+)_{ij}=\frac{s_i+s_j}{2n}-\frac{|i-j|}{2}-\frac{n^2-1}{6n}.
\]
Indeed, summing \(|i-j|=(L_n^+)_{ii}+(L_n^+)_{jj}-2(L_n^+)_{ij}\) in \(j\) gives \(s_i=n(L_n^+)_{ii}+\operatorname{tr}(L_n^+)\); the sum of all resistances is \(n(n^2-1)/3\). Using \(s_0+s_1=(n-1)^2+1\) gives the claimed asymptotic and its strict negative sign for \(n\ge4\).

For small steps, the degree-seven Maclaurin coefficient of \(R\) is \(-1/1728\). For \(n\ge8\), the distance from 0 to 7 is seven, so \(((-L_n)^j)_{0,7}=0\) for \(j<7\) and \(((-L_n)^7)_{0,7}=1\). This gives \((T_n(h))_{0,7}=-h^7/1728+O(h^8)\) and is a direct application of the shortest-walk criterion for this coefficient.

At \(n=8\), put \(B=3I+6L_8+4L_8^2\) and \(A=3I-6L_8+4L_8^2\). The first four rows of the integer matrix \(N\) below, together with \(N_{ij}=N_{7-i,7-j}\), satisfy \(BN=61423369A\):
\[
\begin{pmatrix}
22767445&7237548&12586536&8978304&5124384&2634048&1318656&776448\\
7237548&28116433&3629316&8732616&6487968&3808992&2091840&1318656\\
12586536&3629316&24262513&1138980&7417224&5945760&3808992&2634048\\
8978304&8732616&1138980&22947121&596772&7417224&6487968&5124384
\end{pmatrix}.
\]
The denominator matrix \(B\) is invertible and commutes with \(A\); hence \(T_8(4)=N/61423369\). The minimum numerator is \(596772\) at \((3,4)\) and \((4,3)\) in zero-based indexing. Continuity gives strict positivity in an open neighborhood of \(4\).

## Verification
The displayed integer certificate can be checked by matrix multiplication without numerical tolerances. The standalone `artifacts/check_witness.py` checks this identity, the minimum, symmetry and row sums, using only Python 3. The small- and large-step conclusions above follow from analytic arguments, not finite checks.

## Relationship to prior work
Zappavigna, Colaneri, Kirkland and Shorten, *Essentially Negative News About Positive Systems*, §4, Example 3, give the negative seventh coefficient and an eight-dimensional one-way-shift example. *Eight-state barrier for Markov positivity of the [2/2] Padé map*, Theorems 1–2, gives the shortest-walk argument, establishes small-step nonnegativity in dimension at most seven, and obtains a nonmonotone stochasticity region in dimension eight using a directed pure-birth generator. The pure-birth witness is not reversible; its stochastic interval ends at \(2\sqrt3<4\). The contribution here is the reversible path witness with a strictly positive intermediate step and the explicit large-step path obstruction. Neither the coefficient nor the general small-step obstruction is claimed as new.

*Unconditional fourth-order Gauss–Padé positivity on complete multipartite graphs* covers all-step positivity for \(P_2=K_{1,1}\) and \(P_3=K_{1,2}\) and explicitly gives the exact four-vertex path cutoff with defining polynomial \(h^4-6h^3-60h^2-108h-72\). Those benchmarks are not part of the claim here.

## Limitations
This does not determine the endpoints or the number of connected components of the positive-step region on the eight-vertex path. The small- and large-step obstructions hold for every fixed \(n\ge8\), but recovery of positivity is asserted only for \(n=8\); there is no claim about arbitrary weighted paths or priority outside the works compared.

## References
1. A. Zappavigna, P. Colaneri, S. Kirkland and R. Shorten, *Essentially Negative News About Positive Systems*, §4, Example 3, https://mural.maynoothuniversity.ie/id/eprint/3761/ .
2. *Eight-state barrier for Markov positivity of the [2/2] Padé map*, Theorems 1–2, https://github.com/Resultary/2026/blob/main/2026/9/20/SCOPE-eight-state-pade-markov-positivity-barrier--4aad2a3f58ab/RESULT.md .
3. *Unconditional fourth-order Gauss–Padé positivity on complete multipartite graphs*, Finding and Proof (boundary of the graph class), https://github.com/Resultary/2026/blob/main/2026/10/25/SCOPE-unconditional-fourth-order-gauss-pad-positivity-on-complete-mult--3b12f25d4b2d/RESULT.md .

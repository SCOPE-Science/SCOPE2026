# Unique geometric test-vector optimizer for four-periodic weighted shifts

## Finding
For every \(0<q<1\) and every pair \(s,t>0\), define the four-periodic geometrically weighted unilateral shift \(T_{q,s,t}\) on complex \(\ell^2(\mathbb N_0)\) by
\[
T_{q,s,t}e_{4k+j}=q^{4k+j}\sigma_j e_{4k+j+1},\qquad
(\sigma_0,\sigma_1,\sigma_2,\sigma_3)=(1,s,1,t),\quad k\ge0.
\]
Its normalized geometric test vectors \(v(z)=\sqrt{1-z}(1,\sqrt z,z,z^{3/2},\ldots)\), for \(0<z<1\), give the exact test-vector lower-bound profile
\[
F_{q,s,t}(z)=\langle T_{q,s,t}v(z),v(z)\rangle
=\frac{\sqrt z(1-z)(1+sqz+q^2z^2+tq^3z^3)}{1-q^4z^4}.
\]
**Theorem.** The function \(F_{q,s,t}\) has exactly one critical point \(z_*=z_*(q,s,t)\) on \((0,1)\); it lies strictly in \((1/3,1)\), is a simple zero of its stationarity polynomial, and is its strict global maximum. Thus the degree-eight polynomial \(G_{q,s,t}\) defined in the proof has exactly one zero (counting multiplicity) in \((0,1)\) for **every** permissible parameter triple. The maximizing \(z_*\) depends real-analytically on \((q,s,t)\) in this open parameter region.

In particular this settles the full positive-parameter uniqueness question explicitly posed as Open Question 1 of Ghosh, Birbonshi and Ojha (2026). The theorem concerns the *geometric test-vector lower bound*, not a formula for the exact numerical radius of the weighted shift.

## Assumptions and scope
The Hilbert-space inner product is linear in its first argument; all vector coordinates and weights used in the Rayleigh quotient are positive, so this convention does not affect its value. The symbol \(w(T)\) denotes the numerical radius \(\sup_{\|h\|_2=1}|\langle Th,h\rangle|\), whence \(w(T_{q,s,t})\ge \max_{0<z<1}F_{q,s,t}(z)\). The scalar parameter domain is precisely \(0<q<1\), \(s,t>0\), with no relative restrictions on \(s\) and \(t\). No assertion is made for \(q=1\), nonpositive modulations, or the operator norm or exact numerical radius.

The eight-degree stationarity polynomial, explicitly displayed so that the claim is reproducible without another document, is
\[
\begin{aligned}
G_{q,s,t}(z)={}&1+3(sq-1)z+5q(q-s)z^2+7q^2(tq-1)z^3\\
&+q^3(7q-9t)z^4+5q^4(sq-1)z^5\\
&+3q^5(q-s)z^6+q^6(tq-1)z^7+tq^7z^8.
\end{aligned}
\]

## Proof
**1. Stationarity and boundary signs.** Put \(P(z)=1+sqz+q^2z^2+tq^3z^3\) and \(R(z)=1-q^4z^4\). On \(0<z<1\), differentiation yields
\[
F_{q,s,t}'(z)=\frac{G_{q,s,t}(z)}{2\sqrt z\,R(z)^2},
\quad
G_{q,s,t}(z)=\bigl[(1-3z)P(z)+2z(1-z)P'(z)\bigr]R(z)+2z(1-z)P(z)\,4q^4z^3.
\]
The expanded polynomial is the one displayed above. Because \(G_{q,s,t}(0)=1\) and \(G_{q,s,t}(1)=-2(1-q^4)P(1)<0\), a root lies in \((0,1)\).

**2. Every critical point lies past \(1/3\).** The positive-coefficient geometric expansion is
\[
F_{q,s,t}(z)=(1-z)\sum_{n=0}^{\infty}a_nz^{n+1/2},
\quad
(a_{4k},a_{4k+1},a_{4k+2},a_{4k+3})
=q^{4k}(1,sq,q^2,tq^3).
\]
Every summand has positive derivative for \(0<z<1/3\), because
\[
\frac{d}{dz}\bigl[(1-z)z^{n+1/2}\bigr]
=z^{n-1/2}\bigl(n+\tfrac12-(n+\tfrac32)z\bigr)>0.
\]
At \(z=1/3\), the summands with \(n\ge1\) still have positive derivatives. The series and its derivative converge locally uniformly on \((0,1)\); hence \(F'_{q,s,t}(z)>0\) on \((0,1/3]\).

**3. A positive half-line change of variable.** Let \(y=z/(1-z)\), so \(z=y/(1+y)\) bijects \((0,1)\) onto \((0,\infty)\). Set
\[
H(y)=(1+y)^8G_{q,s,t}\!\left(\frac y{1+y}\right)=\sum_{j=0}^8c_jy^j,
\quad x=qs>0,\quad u=q^2\in(0,1),\quad v=q^3t>0.
\]
Direct binomial expansion gives **all** coefficients:
\[
\begin{aligned}
c_0={}&1,\\
c_1={}&5+3x,\\
c_2={}&7+16x+5u,\\
c_3={}&-7+33x+23u+7v,\\
c_4={}&-35+30x+40u+26v+7u^2,\\
c_5={}&-49+(5+5u^2)x+30u+34v+23u^2,\\
c_6={}&-35+(12u^2-12)x+5u+16v+27u^2+3u^3,\\
c_7={}&-(1-u^2)(13+9x+5u+v),\\
c_8={}&-2(1-u^2)(1+x+u+v).
\end{aligned}
\]
In particular \(c_0,c_1,c_2>0\) and \(c_7,c_8<0\).

**4. A single sign change.** The key coefficient comparisons are the exact identities
\[
\begin{aligned}
c_4-5c_3={}&-135x-75u-9v+7u^2<0,\\
5c_5-7c_4={}&(-185+25u^2)x-130u-12v+66u^2<0,\\
7c_6-5c_5={}&(59u^2-109)x-115u-58v+74u^2+21u^3<0.
\end{aligned}
\]
The first is negative by \(u^2<u\). The second is negative because \(25u^2<25\) and \(66u^2<66u<130u\). For the third, \(59u^2-109<-50\) and \(74u^2+21u^3<95u<115u\). Therefore if \(c_3\le0\), then \(c_4<0\); if \(c_4\le0\), then \(c_5<0\); and if \(c_5\le0\), then \(c_6<0\). Together with the fixed signs of \(c_0,c_1,c_2,c_7,c_8\), the ascending list \((c_0,\ldots,c_8)\), with zeros discarded, has *exactly one* sign change for every \(x,v>0\) and \(0<u<1\).

Descartes' rule of signs now gives at most one positive real zero of \(H\), **counting multiplicity**. Step 1 gives at least one zero \(z\in(0,1)\), and the transformation takes it to a positive zero of \(H\). Hence that zero is unique and simple. Since \(F'\) has positive sign near zero and negative sign near one, it changes sign from positive to negative there and nowhere else. Step 2 places it beyond \(1/3\). The endpoint values of \(F\) are zero, proving strict global optimality.

**5. Parameter dependence.** The stationary root is simple, so the real-analytic implicit-function theorem applied to \(G_{q,s,t}(z)=0\) gives a locally real-analytic root for every parameter triple. Global uniqueness glues these local branches to the asserted real-analytic \(z_*(q,s,t)\).

## Verification
The standalone script `verify_polynomial.py` reconstructs \(G\) by differentiation, obtains all nine Cayley-substitution coefficients symbolically, checks the three exact comparison identities, and samples positive parameter triples to sanity-check their predicted sign variation. It is executable with Python and SymPy via `python verify_polynomial.py`. The algebraic inequalities and Descartes argument above—not finite numerical testing—prove the full uncountable parameter claim.

## Relationship to prior work
Ghosh, Birbonshi and Ojha (arXiv:2608.17486, Section 2) introduce exactly the lower-bound profile and degree-eight stationarity polynomial used here. Their Theorem 2.5 establishes uniqueness only for a restricted parameter regime; their Theorem 2.12 rules out roots below \(1/3\); and their Open Question 1 expressly asks for the unrestricted uniqueness assertion proved here. Their entire-function characterization in Section 3 determines the operator's exact numerical radius and does not imply uniqueness of the distinct test-vector lower-bound optimizer without additional reasoning.

Chakraborty and Ojha (2025) study the two-periodic specialization \(s=t\) of the weights and the resulting lower bound; their proof for that specialization is not the three-parameter result. Chien and Nakazato (2009) study the unmodulated specialization \(s=t=1\), including a geometric test-vector lower bound and exact determinant formulation; this does not cover independent modulations. Two further published research records on the exact same four-periodic shift determine, respectively, a constrained \(s+t\) numerical-radius allocation transition and an Airy asymptotic as \(q\uparrow1\). Those concern the *actual numerical radius*, not the degree-eight root of the geometric test-vector bound. The current claim neither asserts a new determinant formula nor recovers their budget or Airy results by implication.

## Limitations
This theorem proves uniqueness of the stationarity root for the **specified geometric test family**, not uniqueness of all vectors maximizing the numerical radius and not a closed-form evaluation of that radius. The degree-eight polynomial generally requires numerical root finding for a numerical maximizer. The earlier two-periodic 2025 article's full text was not available through the attempted authorized routes; its published scope and the explicit unresolved statement in the 2026 full primary paper limit, but do not eliminate, historical-priority risk. A mathematical database search cannot prove absolute uniqueness of this discovery, and no independent audit has occurred.

## References
1. A. Ghosh, R. Birbonshi and S. Ojha, *On the numerical radius of a class of weighted shift operators*, arXiv:2608.17486 (first submitted 2026-08-18), https://arxiv.org/abs/2608.17486. See Section 2, especially Theorems 2.5, 2.12 and Open Question 1.
2. B. Chakraborty and S. Ojha, *On the numerical radius of weighted shift operators with generalized geometric weights*, Journal of Mathematical Analysis and Applications 543 (2025), article 129021, DOI:10.1016/j.jmaa.2024.129021.
3. M.-T. Chien and H. Nakazato, *The numerical radius of a weighted shift operator with geometric weights*, Electronic Journal of Linear Algebra 18 (2009), 58–63, DOI:10.13001/1081-3810.1293.
4. *Exact allocation transition for a geometric four-periodic weighted shift*, published mathematical research record, identifier e1e34ea2e0ab (2026).
5. *A sharp Airy-edge law for four-periodic geometric weighted shifts*, published mathematical research record, identifier cffc9a187d0d (2026).

# Sharp three-regime Schatten blow-up for anisotropic Bergman companions

## Finding

On the unweighted holomorphic Bergman Hilbert space \(A^2(\mathbb B_2)\), let the generalized Volterra companion be
\[
T_\epsilon f(z)=\int_0^1 (t z_2)^k (Rf)(e^{-\epsilon}t z_1,e^{-\epsilon^a}t z_2)\,\frac{dt}{t},
\qquad Rf(z)=z_1\partial_1f(z)+z_2\partial_2f(z).
\]
Fix an integer \(k\ge1\), a real anisotropy exponent \(0<a<1\), and a Schatten exponent \(p>0\). Put \(q=kp/2\). For every \(\epsilon>0\), the operator is compact and belongs to every positive Schatten class. As \(\epsilon\downarrow0\), its Schatten power sum has the **sharp** three-regime law
\[
\boxed{
\|T_\epsilon\|_{\mathcal S_p}^{p}\sim
\begin{cases}
\dfrac{\Gamma(1-q)\Gamma(1+q)}{p^2}\,\epsilon^{-1-a+(1-a)q},&0<q<1,\\[6pt]
\dfrac{1-a}{p^2}\,\epsilon^{-2a}\log(1/\epsilon),&q=1,\\[6pt]
\dfrac{1}{p^2(q-1)}\,\epsilon^{-2a},&q>1.
\end{cases}}
\]
Here \(\sim\) means that the ratio tends to \(1\). In particular, the critical line \(kp=2\) creates a logarithmic enhancement, while on its two sides the power-law exponents and leading constants differ. No claims are made at \(a=0\) or \(a=1\).

## Assumptions and scope

The unit ball is \(\mathbb B_2=\{z\in\mathbb C^2:|z_1|^2+|z_2|^2<1\}\). Bergman norm means integration against normalized four-dimensional Lebesgue volume. The monomials are mutually orthogonal and
\[
\|z_1^u z_2^v\|_{A^2(\mathbb B_2)}^2
=\frac{2u!v!}{(u+v+2)!},\qquad u,v\in\mathbb Z_{\ge0}.
\]
The self-map is \(\varphi_\epsilon(z)=(e^{-\epsilon}z_1,e^{-\epsilon^a}z_2)\); it has relatively compact image for each fixed positive \(\epsilon\). The multiplier is precisely \(g(z)=z_2^k\). The operator integral is initially defined on polynomials and extends uniquely by the explicit singular-value formula below. The claim includes the quasi-Schatten range \(0<p<1\).

## Proof

**1. Exact singular values.** Set \(m=u+v\), and let \(e_{u,v}\) denote the normalized monomial. Since \(R(z_1^u z_2^v)=m z_1^u z_2^v\), direct radial integration gives, for \(m\ge1\),
\[
T_\epsilon e_{u,v}=
\exp(-\epsilon u-\epsilon^a v)\frac{m}{m+k}
\left(\frac{\prod_{j=1}^k(v+j)}{\prod_{j=1}^k(m+2+j)}\right)^{1/2}e_{u,v+k},
\qquad T_\epsilon e_{0,0}=0.
\]
The output monomials are pairwise different and orthogonal. Consequently the singular values, including multiplicity and a zero, are exactly the nonnegative displayed coefficients. They decay exponentially for every fixed positive \(\epsilon\), proving compactness and membership in every \(\mathcal S_p\).

**2. A uniform reduction.** Let \(\delta=\epsilon^a\), and denote the coefficient in the previous display without its exponential factor by \(w_{u,v}\). For \(v\ge1\), the finite products and \(m\ge v\) show, uniformly over \(u\ge0\),
\[
 w_{u,v}^{p}=\left(\frac{v}{u+v}\right)^q
 \left(1+O_{k,p}(v^{-1})\right).
\]
The \(v=0\) contribution is at most a constant multiple of
\[
\sum_{u\ge1}e^{-p\epsilon u}u^{-q}
=\begin{cases}
O(\epsilon^{q-1}),&q<1,\\
O(\log(1/\epsilon)),&q=1,\\
O(1),&q>1.
\end{cases}
\]
It is negligible against each final leading order. For any fixed positive integer \(V\), the sum over \(1\le v<V\) obeys the same type of bound (up to fixed factors); it too is negligible. Letting \(V\) grow shows that the entire Schatten power sum is asymptotic to
\[
G_\epsilon=
\sum_{v=1}^\infty e^{-p\delta v}
\sum_{u=0}^\infty e^{-p\epsilon u}
\left(\frac{v}{u+v}\right)^q.
\]
This argument uses positive summands; the uniform error at \(v\ge V\) is at most \(O_{k,p}(1/V)\) in relative value.

**3. Replace the inner sum by an integral.** For fixed \(v\), the function \(x\mapsto e^{-p\epsilon x}(v/(x+v))^q\) is positive and decreasing. Its sum over nonnegative integers differs from its integral over \([0,\infty)\) by a number in \([0,1]\). Consequently
\[
G_\epsilon=
\sum_{v=1}^\infty e^{-p\delta v}vH_q(p\epsilon v)
+O(\delta^{-1}),
\qquad H_q(t)=\int_0^\infty e^{-ts}(1+s)^{-q}\,ds.
\]
For small positive \(t\), elementary changes of variable and dominated convergence give
\[
H_q(t)\sim\Gamma(1-q)t^{q-1}\quad(0<q<1),
\qquad H_1(t)=\log(1/t)+O(1),
\qquad H_q(t)\longrightarrow\frac{1}{q-1}\quad(q>1).
\]
For \(q<1\) there is also the global bound \(H_q(t)\le\Gamma(1-q)t^{q-1}\). For \(q>1\) there is the global bound \(H_q(t)\le1/(q-1)\). These bounds justify the next weighted-sum limits by splitting the variable \(x=\delta v\) into a compact interval away from zero and exponentially small tails. At \(q=1\), the integrable weight \(xe^{-px}(1+|\log x|)\) gives the analogous domination.

**4. Evaluate the three regimes.** Since \(\epsilon/\delta=\epsilon^{1-a}\to0\), the dominant indices have \(v\asymp\delta^{-1}\) and hence \(p\epsilon v\to0\). The standard positive Riemann-sum limits are
\[
\delta^{q+1}\sum_{v\ge1}v^qe^{-p\delta v}\longrightarrow
\frac{\Gamma(q+1)}{p^{q+1}},
\qquad
\delta^2\sum_{v\ge1}ve^{-p\delta v}\longrightarrow\frac1{p^2}.
\]
For \(0<q<1\), substitute the first small-\(t\) law to obtain
\[
G_\epsilon\sim
\Gamma(1-q)(p\epsilon)^{q-1}
\frac{\Gamma(1+q)}{(p\delta)^{q+1}}
=\frac{\Gamma(1-q)\Gamma(1+q)}{p^2}
\epsilon^{-1-a+(1-a)q}.
\]
For \(q>1\), the finite integral \(H_q(0)=1/(q-1)\) gives
\[
G_\epsilon\sim\frac1{q-1}\frac1{(p\delta)^2}
=\frac1{p^2(q-1)}\epsilon^{-2a}.
\]
At \(q=1\), on the dominant scale
\(\log(1/(p\epsilon v))=(1-a)\log(1/\epsilon)-\log(p\delta v)\).
The term involving \(\log(p\delta v)\) contributes only \(O(\delta^{-2})\) after summation, whereas the first term contributes
\[
G_\epsilon\sim\frac{1-a}{p^2}\delta^{-2}\log(1/\epsilon).
\]
Finally \(\delta^{-1}\) is lower order than all three displayed expressions because \(a>0\). This proves the theorem with the exact leading constants. \(\square\)

## Verification

The standalone script `verify_companion.py` checks \(8{,}712\) exact rational instances of the Bergman monomial norm ratio and the weighted-shift coefficient formula, and evaluates illustrative finite Schatten partial sums in each regime. Run it using `python verify_companion.py` with only the standard library. The exact checks passed. The illustrative finite sums are consistent with the three regimes but do not prove the infinite limits; those follow from Steps 2–4.

## Relationship to prior work

Dong and Xu [1] define these radial generalized Volterra companion operators and prove qualitative Schatten membership and compact-range singular-value decay; their Sections 3.3 and 4.3 contain an ellipsoid example with a power-law Schatten threshold for the fixed noncompact map \(\varphi(z,w)=(z,0)\). That threshold is not a quantitative statement about the approach to the identity by two simultaneous, distinct damping scales. Our result instead computes exact norm blow-up constants, the logarithmic boundary, and the full quasi-Schatten range for a two-ball family in which every positive-parameter operator is compact. Almoka, Arroussi and Virtanen [2] treat generalized Volterra-type operators on rapidly weighted one-variable Bergman spaces, while Mengestie [3] studies corresponding Fock-space companions. Liu, Yuan and Zeng [4] consider the Volterra operator with the derivative placed on the inducing function. No listed theorem directly implies the present three-regime numerical constants; a prior equivalent result under different operator or lattice-sum terminology remains possible.

## Limitations

The theorem concerns an unweighted two-dimensional complex ball, an integer coordinate monomial multiplier, and fixed \(0<a<1\). It does not establish a uniform limit as \(a\) approaches either endpoint, nor describe arbitrary non-diagonal self-maps, general multipliers, higher dimensions, or operator-norm behavior. Mathematical priority has not been independently certified. The supporting finite tests are not substitutes for the analytic estimates.

## References

[1] J. Dong and C. Xu, *Generalized Volterra Companion Operators on Bergman Spaces over Convex Domains of Finite Type*, arXiv:2609.27584v1 (first public September 23, 2026), especially Sections 3.3 and 4.3. https://arxiv.org/abs/2609.27584

[2] M. Almoka, H. Arroussi, and J. Virtanen, *Composition and Volterra type operators on large Bergman spaces with rapidly decreasing weights*, arXiv:2507.16437v1 (2025). https://arxiv.org/abs/2507.16437

[3] T. Mengestie, *Schatten class generalized Volterra companion integral operators*, arXiv:1507.03536 (2015). https://arxiv.org/abs/1507.03536

[4] J. Liu, C. Yuan, and H. Zeng, *Schatten classes of Volterra operators on Bergman-type spaces in the unit ball*, Communications on Pure and Applied Analysis 21 (2022), 3425–3439, doi:10.3934/cpaa.2022108. https://doi.org/10.3934/cpaa.2022108

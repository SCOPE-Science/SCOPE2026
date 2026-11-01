# Uniform two-term period crossover in a cubic global-center family

## Finding
Consider the polynomial differential system in **original physical time**
\[
\dot x=y,\qquad \dot y=-x-\gamma x^3-\beta xy^2,
\qquad \beta>0,\quad\gamma>0.
\]
For every turning amplitude \(A>0\), there is exactly one nonconstant periodic orbit with maximum position \(x=A\). Let \(T_{\beta,\gamma}(A)\) denote its minimal original-time period. The period function is smooth, strictly decreasing, and is a bijection from \((0,\infty)\) to \((0,2\pi)\). More sharply, **uniformly over all choices of \(\gamma>0\)**, with \(\beta>0\) fixed and \(A\to\infty\),
\[
\boxed{\displaystyle
T_{\beta,\gamma}(A)
=\frac{2\pi}{A\sqrt{\beta(1+\gamma A^2)}}
\left[
1+\frac{2\log2+\dfrac{\gamma A^2}{1+\gamma A^2}(2\log2-1)}{2\beta A^2}
+O_{\beta}(A^{-4})
\right].}
\]
The relative remainder is bounded by a constant depending only on \(\beta\) times \(A^{-4}\) for every \(\gamma>0\), including sequences in which \(\gamma\) varies with \(A\). Consequently, the distinguished crossover variable is \(\gamma A^2\): if \(\gamma A^2\to\lambda\in[0,\infty)\), then \(A T_{\beta,\gamma}(A)\to 2\pi/\sqrt{\beta(1+\lambda)}\); for each fixed \(\gamma>0\), \(A^2 T_{\beta,\gamma}(A)\to2\pi/\sqrt{\beta\gamma}\). The coefficient of the first relative correction interpolates continuously between \(\log2/\beta\) and \((4\log2-1)/(2\beta)\).

The strict decrease also yields one and only one periodic orbit with each prescribed period in \((0,2\pi)\). Near the origin,
\[
T_{\beta,\gamma}(A)=2\pi\left[1-\frac{\beta+3\gamma}{8}A^2+O_{\beta,\gamma}(A^4)\right].
\]
The previously studied \(\gamma=0\) axis is *not* an originality claim: its leading and two-term period laws already occur in related published mathematical records. Here the contribution is the \(\gamma>0\) regime, its new correction coefficient, and the parameter-uniform crossover.

## Assumptions and scope
The parameter \(\beta>0\) is held fixed in the large-amplitude expansion. The restoring coefficient \(\gamma\) is an arbitrary *strictly positive* real number, potentially dependent on the amplitude in the uniform asymptotic assertion. The monotonicity statement refers to each fixed pair \((\beta,\gamma)\); it does not compare periods across different parameter values. Amplitude means the positive turning-point coordinate \(A\) (not canonical displacement, energy, or velocity magnitude). All times and periods are measured in the displayed polynomial vector field, without time reparametrization. The expansion asserts no uniformity as \(\beta\to0\), and no claim is made about the entire seven-parameter cubic family.

## Proof
**1. Exact global energy and one orbit per amplitude.** Put
\[
U(x)=\int_0^x e^{\beta s^2}(s+\gamma s^3)\,ds,\qquad
H(x,y)=\tfrac12e^{\beta x^2}y^2+U(x).
\]
Direct differentiation along the flow gives
\[
\dot H=e^{\beta x^2}y\,[\beta xy^2+x+\gamma x^3+\dot y]=0.
\]
The potential \(U\) is even, strictly increasing on \((0,\infty)\), tends to infinity at both ends, and has only one critical point. For each \(A>0\), the level \(H=U(A)\) is a compact smooth oval, with turning points \((\pm A,0)\). The vector field is nonzero on that level. Thus the level is one periodic orbit, and all other points except the equilibrium belong to exactly one such level. Its physical period is
\[
T(A)=4\int_0^A\frac{dx}{\sqrt{e^{-\beta x^2}\int_{x^2}^{A^2}e^{\beta v}(1+\gamma v)\,dv}}.
\tag{1}
\]
Both turning singularities are integrable.

**2. Strict period decrease.** Introduce the global odd coordinate
\[
q(x)=\int_0^x e^{\beta s^2/2}\,ds.
\]
Since \(\dot q=e^{\beta x^2/2}y\), the unchanged-time system becomes the mechanical oscillator
\[
\ddot q=-G(q),\qquad G(q(x))=e^{\beta x^2/2}x(1+\gamma x^2).
\]
For \(x>0\), write \(e=e^{\beta x^2/2}\). Differentiating \(G\) in its canonical argument yields
\[
G'(q(x))=1+(\beta+3\gamma)x^2+\beta\gamma x^4.
\]
The comparison function \(f(x)=xe/(1+\beta x^2)\) satisfies \(f(0)=q(0)=0\) and
\[
f'(x)=e\frac{1+\beta^2x^4}{(1+\beta x^2)^2}<e=q'(x)
\qquad (x>0).
\]
Thus \(q(x)>xe/(1+\beta x^2)\), and consequently
\[
\begin{aligned}
qG'(q)-G(q)
&>ex\left[\frac{1+(\beta+3\gamma)x^2+\beta\gamma x^4}{1+\beta x^2}-(1+\gamma x^2)\right]\\
&=\frac{2\gamma ex^3}{1+\beta x^2}>0.
\end{aligned}
\]
Therefore \(k(q)=G(q)/q\) strictly increases for \(q>0\). In terms of the canonical positive amplitude \(Q=q(A)\), symmetry of the oscillator gives the exact period representation
\[
T(Q)=4\int_0^1\left(2\int_s^1t\,k(Qt)\,dt\right)^{-1/2}\,ds.
\tag{2}
\]
For every \(0\le s<1\), the inner integral strictly increases with \(Q\), while the turning-point singularity remains integrable. Hence \(T\) strictly decreases with \(Q\), and therefore with \(A\). Since \(G'(0)=1\), \(T(A)\to2\pi\) as \(A\downarrow0\).

For the local coefficient, expand \(q=x+\beta x^3/6+O(x^5)\) and invert to get \(G(q)=q+(\gamma+\beta/3)q^3+O(q^5)\). Expanding (2) for a quartic potential gives \(T=2\pi[1-3(\gamma+\beta/3)Q^2/8+O(Q^4)]\); since \(Q=A+O(A^3)\), the stated small-amplitude formula follows.

**3. Exact boundary-layer quadrature.** Set \(u=A^2-x^2\), \(L=1+\gamma A^2\), and
\[
E_0(u)=\int_0^ue^{\beta w}\,dw=\frac{e^{\beta u}-1}{\beta},\qquad
E_1(u)=\int_0^u(u-w)e^{\beta w}\,dw=\frac{e^{\beta u}-1-\beta u}{\beta^2}.
\]
Equation (1) transforms **exactly**, without a change of time, into
\[
A\sqrt L\,T(A)
=2\int_0^{A^2}\frac{du}{\sqrt{1-u/A^2}\,\sqrt{E_0(u)-\frac{r}{A^2}E_1(u)}},
\qquad r=\frac{\gamma A^2}{1+\gamma A^2}\in(0,1).
\tag{3}
\]
For each fixed \(u>0\), the integrand approaches \(2E_0(u)^{-1/2}\), uniformly in \(0<r<1\). Its integral is finite because \(E_0(u)\asymp u\) near zero and \(E_0(u)\asymp e^{\beta u}\) at infinity.

**4. The uniform second-order expansion.** Write \(h=A^{-2}\). For \(0\le u\le A\), one has \(hu\le A^{-1}\), \(0\le E_1/E_0\le u\), and Taylor's theorem gives, with a remainder bounded independently of \(r\in[0,1]\),
\[
\frac{1}{\sqrt{1-hu}\sqrt{E_0-hrE_1}}
=\frac{1}{\sqrt{E_0}}
\left[1+\frac h2\left(u+r\frac{E_1}{E_0}\right)
+O\big(h^2u^2\big)\right].
\tag{4}
\]
The absolute contribution of the error is \(O_\beta(h^2)\), since \(\int_0^\infty u^2E_0(u)^{-1/2}\,du<\infty\). The expansion remains valid after extending the two displayed leading integrals to infinity: their discarded tails beyond \(u=A\) are exponentially small.

For completeness, the exact integral from \(A\) to \(A^2/2\) is exponentially small, because \(1-hu\ge1/2\) and \(E_0-hrE_1\ge E_0/2\) there. On \(A^2/2\le u\le A^2\), the identity
\[
E_0-hrE_1=\int_0^ue^{\beta w}\,[1-hr(u-w)]\,dw
\ge\tfrac12\int_{u/2}^{u}e^{\beta w}\,dw
\]
controls the denominator uniformly. Integrating the remaining \((1-u/A^2)^{-1/2}\) singularity gives an exponentially small remainder, even after multiplication by powers of \(A\). Hence, uniformly in \(r\in[0,1]\),
\[
A\sqrt L\,T(A)
=2I_0+h(I_u+rI_1^*)+O_\beta(h^2),
\]
where
\[
I_0=\int_0^\infty E_0^{-1/2}\,du,
\quad I_u=\int_0^\infty uE_0^{-1/2}\,du,
\quad I_1^*=\int_0^\infty\frac{E_1}{E_0^{3/2}}\,du.
\]
With the substitution \(z=e^{-\beta u}\), beta integrals and the classical logarithmic beta integral yield
\[
I_0=\frac\pi{\sqrt\beta},\qquad
I_u=\frac{2\pi\log2}{\beta^{3/2}},\qquad
I_1^*=\frac{\pi(2\log2-1)}{\beta^{3/2}}.
\]
To verify the last formula directly, note that \(E_1/E_0=\beta^{-1}-u/(e^{\beta u}-1)\); the remaining beta integral equals \(2\pi(1-\log2)/\beta^{3/2}\). Substitution proves the displayed **relative \(O_\beta(A^{-4})\) expansion**, uniformly over \(\gamma>0\). It also shows \(T(A)\to0\) as \(A\to\infty\), completing the period-bijection statement.

## Verification
Run `python tools/check_period.py` with Python 3, SymPy, and mpmath. The checker verifies the conserved-energy cancellation, the crucial comparison-function derivative, and the positive algebraic difference used for strict monotonicity. It then evaluates the exact physical-time period quadrature at 18 amplitude/parameter combinations (including both very weak and strong positive cubic restoration), checks representative strictly decreasing sequences, and checks the local period coefficient. In all 18 large-amplitude comparisons the scaled relative two-term residual \(A^4|T/T_{\mathrm{two\,term}}-1|\) was below \(17.634\). This finite evidence is a reproduction check, not a proof of the all-amplitude monotonicity or uniform remainder; those assertions follow from the analytical inequalities and dominated Taylor bounds above.

## Relationship to prior work
Appis and Llibre (2024), Theorem 4(a,d), classify the relevant cubic systems as global centers; the present family corresponds to \(a_4=-\gamma<0\), \(a_6=-\beta<0\), with all other cubic coefficients zero. Their openly accessible proof examines global phase portraits, not the original-time minimal period or any parameter-uniform two-term law. The existence of the global center is therefore acknowledged, not claimed as new.

Two earlier publicly available mathematical findings analyze the *distinct* cubic family \(\dot y=-x(1-\alpha y+\kappa y^2)\) and the restoring-free system \(\dot y=-x+(a-\kappa x)y^2\). At \(\alpha=a=0\) these **cover the \(\gamma=0\) axis**, including its one- and two-term high-amplitude period laws. That axis is excluded from the originality claim. The added \(-\gamma x^3\) term with \(\gamma>0\), the explicit \(r\)-dependent correction, and especially the bound uniform across the scale \(\gamma A^2=O(1)\) do not follow from those fixed-parameter axis results. A published result for a quintic global-center oscillator proves a related leading power-law boundary behavior with \(x^3y^2\) and \(x^5\) terms, but it concerns a different vector field and does not specify the present cubic second-order crossover. General period monotonicity criteria may provide alternative routes to the decreasing-period statement; the independent content here is the complete quantitative uniform law for this family.

## Limitations
The asserted new asymptotics require \(\gamma>0\) and fixed \(\beta>0\); the \(\gamma=0\) limit is included in the uniform estimate only as a mathematical boundary check, not a newly claimed theorem on that axis. The theorem does not establish uniformity as \(\beta\downarrow0\), any perturbative persistence of the center, or uniqueness of periodic orbits outside the stated cubic family. The literature survey is finite; unindexed equivalent statements or broader theorems could alter publication priority. Exact source records for related public findings were read where available; their existence is not evidence of independent validation of this theorem. Independent mathematical audit has not been performed.

## References
1. R. F. Appis and J. Llibre, *Global centers of a family of cubic systems*, **Aequationes Mathematicae** 98 (2024), 1373–1389; DOI `10.1007/s00010-024-01051-7`, first public online 2024-04-05. Open full text: `https://pmc.ncbi.nlm.nih.gov/articles/PMC11374847/`.
2. *Two-term boundary-period law and velocity skew for a cubic global center* (2026), publicly accessible result and proof: `https://github.com/Resultary/2026/blob/main/2026/10/11/SCOPE-two-term-boundary-period-law-and-velocity-skew-for-a-cubic-globa--c61200f602fe/RESULT.md`. The \(\alpha=0\) specialization covers the restoring-free axis.
3. *Universal logarithmic frequency and square-wave limit at a cubic global center* (2026), publicly accessible result and proof: `https://github.com/Resultary/2026/blob/main/2026/10/11/SCOPE-universal-logarithmic-frequency-and-square-wave-limit-at-a-cubic--5ef7d7af5678/RESULT.md`. The \(a=0\) specialization covers the leading period limit on that axis.
4. *Strict period decrease and sharp large-amplitude laws for quintic global centers* (2026), publicly accessible result and proof: `https://github.com/Resultary/2026/blob/main/2026/10/11/SCOPE-strict-period-decrease-and-sharp-large-amplitude-laws-for-quinti--ffe383da977f/RESULT.md`.
5. L.-J. Yang and X.-W. Zeng, *The period function of Liénard systems*, **Proceedings of the Royal Society of Edinburgh A** 143 (2013), 205–221; DOI `10.1017/S0308210511000096` (general period-function criteria; abstract inspected).

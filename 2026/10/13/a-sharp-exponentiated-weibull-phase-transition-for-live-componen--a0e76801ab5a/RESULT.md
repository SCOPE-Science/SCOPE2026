# A sharp exponentiated-Weibull phase transition for live-component cumulative residual extropy
## Finding
Let \(n\\ge 2\) and consider a coherent system with IID continuous component lifetimes and signature
\[
\\mathbf s=(s_1,\\ldots,s_i,0,\\ldots,0),\\qquad 1\\le i\\le n-1.
\]
Suppose each component has the exponentiated-Weibull distribution
\[
G(x)=\\left(1-e^{-(x/\\lambda)^\\beta}\\right)^\\alpha,\\qquad x>0,
\]
with \(\\alpha,\\beta,\\lambda>0\). Write \(Y_{n:n}\) for the largest component lifetime and use the live-component residual lifetime
\[
T_{{n,n}}(t)=Y_{{n:n}}-t\\mid T^{{(n)}}<t<Y_{{n:n}}.
\]
For cumulative residual extropy
\[
\\xi J(Z)=-\\frac12\\int_0^\\infty \\overline F_Z(y)^2\\,dy,
\]
one has the sharp asymptotic
\[
\\xi J(T_{{n,n}}(t))\\sim -\\frac{{\\lambda^\\beta}}{{4\\beta}}t^{{1-\\beta}},\\qquad t\\to\\infty.
\]
Equivalently, with \(a_t=\\lambda^\\beta/(\\beta t^{{\\beta-1}})\),
\[
\\frac{{\\xi J(T_{{n,n}}(t))}}{{a_t}}\\longrightarrow -\\frac14.
\]
Hence there is a sharp tail-shape phase transition:
\[
\\xi J(T_{{n,n}}(t))\\to
\\begin{{cases}}
0,&\\beta>1,\\\\
-\\lambda/4,&\\beta=1,\\\\
-\\infty,&0<\\beta<1.
\\end{{cases}}
\]
The leading term does not depend on \(\\alpha\), \(n\), or the signature within the stated class.

## Assumptions and scope
The result uses the standard IID continuous coherent-system signature model. The restriction \(s_{{i+1}}=\\cdots=s_n=0\) ensures that system failure occurs before the maximum component failure with positive conditional probability, exactly the live-component regime in which \(T_{{n,n}}(t)\) is defined. No increasing-hazard-rate hypothesis is needed.

The result is only asserted for the final live order statistic \(j=n\). It does not state corresponding first-order asymptotics for \(T_{{j,n}}(t)\) when \(j<n\), nor does it address non-IID components.

## Proof
Let \(S(x)=1-G(x)\) and put \(q_t=S(t)\). Let \(K\) be the random failure rank of the coherent system, so \(P(K=k)=s_k\), and let \(R_t\) be the number of component lifetimes exceeding \(t\). For IID continuous lifetimes, the failure-order permutation is independent of the ordered lifetime values; consequently \(K\) is independent of \(R_t\), and
\[
R_t\\sim\\operatorname{{Bin}}(n,q_t).
\]
The conditioning event \(E_t=\\{{T^{{(n)}}<t<Y_{{n:n}}\\}}\) is equivalent, given \(K=k\), to \(1\\le R_t\\le n-k\). Thus, for \(1\\le r\\le n-1\),
\[
P(R_t=r,E_t)=\\binom nr q_t^r(1-q_t)^{{n-r}}c_r,
\\qquad
c_r=\\sum_{{k=1}}^{{\\min(i,n-r)}}s_k.
\]
Because \(i\\le n-1\), \(c_1=1\). Since \(q_t\\to0\), division by \(P(E_t)\) gives
\[
P(R_t=1\\mid E_t)=1-O(q_t),
\\qquad
P(R_t\\ge2\\mid E_t)=O(q_t).
\]

Conditional on \(R_t=r\) and \(E_t\), the \(r\) surviving component excesses are IID with survival function
\[
Q_t(y)=\\frac{{S(t+y)}}{{S(t)}},\\qquad y\\ge0,
\]
and \(T_{{n,n}}(t)\) is their maximum. Hence its survival function conditional on \(R_t=r\) is
\[
H_{{r,t}}(y)=1-(1-Q_t(y))^r.
\]
For \(0\\le Q_t(y)\\le1\),
\[
Q_t(y)\\le H_{{r,t}}(y)\\le rQ_t(y).
\]
Averaging over \(R_t\\mid E_t\) therefore yields, uniformly in \(y\\ge0\),
\[
Q_t(y)\\le \\overline F_{{T_{{n,n}}(t)}}(y)
\\le (1+O(q_t))Q_t(y).
\]
Consequently
\[
\\int_0^\\infty \\overline F_{{T_{{n,n}}(t)}}(y)^2\\,dy
=(1+o(1))I_t,
\\qquad
I_t=\\int_0^\\infty Q_t(y)^2\\,dy.
\]

For the exponentiated-Weibull tail, uniformly for \(x\\ge t\),
\[
S(x)=\\alpha e^{-(x/\\lambda)^\\beta}
\\left(1+O\\left(e^{-(t/\\lambda)^\\beta}\\right)\\right).
\]
Thus, with \(u_t=(t/\\lambda)^\\beta\),
\[
I_t
=\\frac{{\\int_t^\\infty S(x)^2\\,dx}}{{S(t)^2}}
\\sim e^{{2u_t}}\\int_t^\\infty e^{{-2(x/\\lambda)^\\beta}}\\,dx.
\]
After the substitution \(u=(x/\\lambda)^\\beta\),
\[
I_t\\sim \\frac{{\\lambda}}{{\\beta}}e^{{2u_t}}
\\int_{{u_t}}^\\infty e^{{-2u}}u^{{1/\\beta-1}}\\,du.
\]
For any fixed real \(a\),
\[
\\int_v^\\infty e^{{-2u}}u^a\\,du
\\sim \\frac12e^{{-2v}}v^a,
\\qquad v\\to\\infty,
\]
which follows directly by l'Hopital's rule applied to the ratio of the two sides. Therefore
\[
I_t\\sim \\frac{{\\lambda}}{{2\\beta}}u_t^{{1/\\beta-1}}
=\\frac{{\\lambda^\\beta}}{{2\\beta}}t^{{1-\\beta}}.
\]
Multiplication by \(-1/2\) in the definition of CRJ gives the claimed asymptotic and all three limiting regimes.

## Verification
The proof is analytic. The key conditioning reduction is exact, not asymptotic: once the number of survivors at time \(t\) is fixed, the residual maximum is the maximum of IID component excesses, while the coherent-system architecture only changes the survivor-count mixing weights. Because the one-survivor weight tends to one at rate \(O(S(t))\), the architecture disappears from the leading term.

The exponentiated-Weibull tail approximation is uniform over \(x\\ge t\), so replacing \(S(x)^2\) by its Weibull-tail equivalent inside the tail integral does not rely on pointwise-only convergence. The incomplete-gamma endpoint estimate is valid for every \(\\beta>0\), including the critical case \(\\beta=1\) and the long-residual-scale regime \(0<\\beta<1\).

## Relationship to prior work
Pakdaman and Alizadeh Noughabi introduced the CRJ analysis of \(T_{{j,n}}(t)\) for live components in coherent systems and studied exponentiated-Weibull examples. Their 2026 paper derives a general fixed-\(y\) limiting function and, for its exponentiated-Weibull example with \(\\beta=1.5\), concludes that the CRJ of \(T_{{4,4}}(t)\) tends to zero. The result here is a first-order asymptotic for arbitrary \(\\beta>0\), identifies the critical value \(\\beta=1\), and covers the divergent \(0<\\beta<1\) regime without an increasing-hazard-rate assumption.

Earlier work on cumulative residual extropy of coherent and mixed systems treats system-level CRJ, while classical residual-lifetime mixture theory supplies structural representations for used coherent systems. Those results provide background but do not by themselves yield the stated exponentiated-Weibull live-component CRJ asymptotic or its independence from \(\\alpha\), \(n\), and the signature.

## Limitations
The result concerns a single asymptotic functional and the largest surviving order statistic. It does not establish second-order terms, uniformity over varying system size, or analogous constants for intermediate live order statistics. General extreme-value excess scaling is standard background; the new content assessed here is the CRJ asymptotic after conditioning on coherent-system failure and the resulting architecture-independent phase transition.

## References
Pakdaman, Z. and Alizadeh Noughabi, R., “Discovering the complexity of residual lifetimes of live components in the coherent system using cumulative residual extropy,” Probability in the Engineering and Informational Sciences 40 (2026), 440–470. DOI: 10.1017/S0269964826100205.

Chakraborty, S. and Pradhan, B., “On cumulative residual extropy of coherent and mixed systems,” Annals of Operations Research 340 (2024), 59–81. DOI: 10.1007/s10479-023-05727-2.

Navarro, J., Balakrishnan, N., and Samaniego, F. J., “Mixture representations of residual lifetimes of used systems,” Journal of Applied Probability 45 (2008), 1097–1112. DOI: 10.1239/jap/1231340236.

# Degeneracy-only splitting of Schottky peaks in an equally spaced three-level system

## Finding
For every integer \(M\ge256\), a canonical system with three equally spaced energies \(0,\Delta,2\Delta\), \(\Delta>0\), and respective degeneracies \(1,M^2,M^3\) has **at least two distinct strict local maxima** of heat capacity at positive temperature, separated by a local minimum. This is a uniform constructive result, not a claim that no further maxima occur.

Write \(L=\log M\) and \(x=\Delta/(k_{\mathrm B}T)\). There are peak branches \(x_{\mathrm h}(M)\) and \(x_{\mathrm c}(M)\) whose inverse-temperature positions and heights satisfy
\[
x_{\mathrm h}=L+\frac4L+O(L^{-2}),\qquad
x_{\mathrm c}=2L+\frac2L+O(L^{-2}),
\]
\[
\frac{C(x_{\mathrm h})}{k_{\mathrm B}}\sim\frac{L^2}{4},\qquad
\frac{C(x_{\mathrm c})}{k_{\mathrm B}}\sim L^2.
\]
Between the branches, at the explicit inverse temperature \(x=3L/2\),
\[
\frac{C(3L/2)}{k_{\mathrm B}}=\frac{9L^2}{2(\sqrt M+2)}\longrightarrow0.
\]
Thus a growing degeneracy hierarchy alone separates two calorimetric peaks even though both adjacent energy gaps equal \(\Delta\).

## Assumptions and scope
A noninteracting canonical single-unit spectrum consists of exactly three energy values with degeneracies as stated. The heat capacity is the equilibrium derivative at fixed energy levels and fixed degeneracies, with \(k_{\mathrm B}>0\). The integer \(M\) may be arbitrarily large. No thermodynamic-limit phase transition, many-body interaction, or restriction on the existence of further extrema is asserted.

Set \(b=M^2e^{-x}\), \(c=M^3e^{-2x}\), and \(Z=1+b+c\). The standard canonical variance identity yields
\[
\frac{C(x)}{k_{\mathrm B}}=x^2\operatorname{Var}_x(J)
=x^2\frac{P}{Z^2},\qquad P=b+4c+bc,
\]
where \(J\) takes values \(0,1,2\) with probabilities \((1,b,c)/Z\).

## Proof
**Derivative and third cumulant.** Let \(\kappa_3=\mathbb E[(J-\mathbb EJ)^3]\). Expanding the first three moments gives
\[
\kappa_3=\frac{Q}{Z^3},\quad
Q=(c-1)(b^2-bc-b-8c),\quad
\frac{d}{dx}\frac{C}{k_{\mathrm B}}=\frac{x(2PZ-xQ)}{Z^3}.
\]
Since \(P,Z,x>0\), this derivative has the sign of \(2-xR\), with \(R=Q/(PZ)\). These identities follow by differentiating the displayed partition sum; no approximation is used.

**Four exact derivative signs.** Let \(L=\log M\) and \(q=e^{-1}\), for which \(1/3<q<3/8\). The four points
\[
L<L+1<3L/2<2L+1
\]
are ordered when \(M\ge256\). At \(x=L\), the weights are \((1,M,M)\), and \(Q=-9M(M-1)<0\), so the derivative is positive. At \(x=3L/2\), the weights are \((1,\sqrt M,1)\), hence \(Q=0\) and the derivative is positive.

At \(x=L+1\), the weights are \((1,Mq,Mq^2)\), and direct factorization gives
\[
R=\frac{1-q}{1+q}\,
\frac{\left(1-\frac1{Mq^2}\right)
\left(1-\frac{q^{-1}+8}{M(1-q)}\right)}
{\left(1+\frac{q^{-1}+4}{Mq}\right)
\left(1+\frac1{Mq(1+q)}\right)}.
\]
The elementary bounds \(1/3<q<3/8\) and \(M\ge256\) imply
\[
R\ge\frac5{11}\frac{(1-9/256)(1-11/160)}{(1+21/256)(1+3/256)}
=\frac{294424}{789173}>\frac13.
\]
At \(x=2L+1\), the weights are \((1,q,q^2/M)\). Setting \(h=q^2/M\le9/16384\) gives
\[
R=\frac{(1-h)[q(1-q)+h(q+8)]}{[q+h(q+4)](1+q+h)}
\ge\frac5{11}\frac{1-9/16384}{(1+117/16384)(1+9/16384)}
=\frac{1341440000}{2975509823}>\frac13.
\]
Moreover \(L>5\) because \(e<3\) and \(e^5<243<256\le M\). At both of the latter two points \(x>6\), hence \(2-xR<0\). The derivative signs in order are therefore
\[
+\,,\quad -\,,\quad +\,,\quad -.
\]
Analyticity of the nonconstant heat-capacity function and the extreme-value theorem give a strict local maximum in each of the disjoint intervals \((L,L+1)\) and \((3L/2,2L+1)\), with an intervening local minimum in \((L+1,3L/2)\). The maxima remain maxima after changing from inverse temperature to temperature, since the change is a smooth bijection.

**Asymptotic peak positions.** Write \(x=L+s\), \(0\le s\le1\). Uniformly there, the normalized weights of levels 1 and 2 differ from a two-level distribution of relative weight \(e^{-s}\) by \(O(M^{-1})\), also after one differentiation in \(s\). Consequently
\[
R(L+s)=\tanh(s/2)+O(M^{-1}),\qquad
\frac{dR(L+s)}{ds}=\tfrac12\operatorname{sech}^2(s/2)+O(M^{-1}).
\]
The stationarity equation \((L+s)R(L+s)=2\) has a unique solution in \(0<s<1\) for all sufficiently large \(M\), with \(s=4/L+O(L^{-2})\). Indeed the left side is strictly increasing there for large \(M\), negative relative to 2 at \(s=0\), and positive relative to 2 at \(s=1\); Taylor expansion at \(s=0\) then gives the stated location. At \(x=2L+s\), the uppermost level instead has relative weight \(O(M^{-1})\). The same argument applies to the lower two levels and yields \(s=2/L+O(L^{-2})\). The derivative passes from positive to negative at each root.

Near each branch the variance converges to that of two equiprobable adjacent levels, \(1/4\), proving the two peak-height asymptotics. At \(x=3L/2\), the three exact weights \((1,\sqrt M,1)\) give variance \(2/(\sqrt M+2)\) and the stated exact trough test value. This completes the proof.

## Verification
The standalone file `verify.py` uses independent moment sums and independently expanded rational formulas. It checks all four derivative signs for six values of \(M\ge256\), three distinct stationary roots, exact midpoint heat capacities, central finite-difference derivatives, the rational lower bounds above, and both large-\(M\) asymptotic branches. Running `python verify.py` produces 256 successful checks. The numerical tests do not substitute for the uniform sign proof or asymptotic argument.

## Relationship to prior work
The 2015 multilevel Schottky analysis by de Souza, Paupitz, Seridonio and Lagos gives the general three-level heat-capacity partition-function formula and numerically studies double peaks with widely separated excitation gaps and varying degeneracies. Those formulas and the qualitative degeneracy effect are established prior work, not claimed here. The added mathematical statement is a uniform finite cutoff for **equal adjacent gaps** and an explicit logarithmic two-peak scaling regime with divergent peak heights and a vanishing inter-peak test value. The source's large gap-ratio heuristic is not a necessary condition in the unrestricted three-level canonical model. Related ferrimagnet work documents double heat-capacity peaks from different excitation channels but does not supply this equal-gap degeneracy theorem.

## Limitations
This result proves at least two strict local maxima, not exactly two. No optimal/minimal degeneracy cutoff is claimed; \(256\) is a sufficient bound. Extreme degeneracies may not be physically realizable as isolated low-energy multiplets, and peak multiplicity alone cannot uniquely reconstruct an experimental spectrum. Exact historical priority is unresolved: older three-level calorimetric studies cited in the 2015 source were not all accessible in full text. The result concerns a single finite canonical spectrum and makes no phase-transition claim.

## References
1. M. de Souza, R. Paupitz, A. Seridonio and R. E. Lagos, *Specific Heat Anomalies in Solids Described by a Multilevel Model*, first posted April 28, 2015, https://arxiv.org/abs/1504.07525. Primary full-text comparison: sections II–V, particularly equations (7)–(11), Figure 3 discussion, and conclusion.
2. T. Nakanishi and S. Yamamoto, *Intrinsic double-peak structure of the specific heat in low-dimensional quantum ferrimagnets*, first posted June 27, 2002, https://arxiv.org/abs/cond-mat/0206555. Abstract-level comparison only.
3. S. Mahdavifar and A. Akbari, *Heat capacity of Schottky type in low-dimensional spin system*, first posted March 31, 2008, https://arxiv.org/abs/0803.4495. Abstract-level comparison only.

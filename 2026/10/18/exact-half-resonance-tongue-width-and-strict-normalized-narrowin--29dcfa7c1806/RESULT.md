# Exact half-resonance tongue width and strict normalized narrowing in the sine circle map

## Finding
For the canonical lift of the Arnold sine circle diffeomorphism
\[
\widetilde F_{K,\Omega}(\theta)=\theta+2\pi\Omega-K\sin\theta,\qquad 0<K<1,
\]
whose induced circle map is obtained modulo \(2\pi\),
let \(\mathcal T_{1/2}(K)\) consist of all detunings \(\Omega\in[0,1]\) at which a lifted orbit obeys \(\widetilde F_{K,\Omega}^{2}(\theta)=\theta+2\pi\). Its width \(W(K)=|\mathcal T_{1/2}(K)|\) has an exact one-root representation. Let \(d_K\in(0,\pi/2)\) be the unique positive root of
\[
K^2=4d_K\sec^2(d_K)\bigl(d_K\sec^2(d_K)+\tan(d_K)\bigr).
\]
Then the tongue is the closed interval \([\tfrac12-\tfrac12W(K),\tfrac12+\tfrac12W(K)]\) and
\[
W(K)=\frac{\sin d_K}{\pi}\sqrt{K^2-4d_K^2\sec^2 d_K}.
\]
Moreover \(W(K)/K^2\) is strictly decreasing on \((0,1)\), so the global sharp quadratic envelope is
\[
0<W(K)<\frac{K^2}{4\pi},\qquad
\lim_{K\downarrow0}\frac{4\pi W(K)}{K^2}=1.
\]
The small-coupling expansion is
\[
W(K)=\frac{K^2}{4\pi}\left(1-\frac{K^2}{12}+\frac{23K^4}{1440}+O(K^6)\right).
\]

## Assumptions and scope
The parameter \(K\) is a coupling coefficient strictly between zero and one, ensuring an orientation-preserving circle diffeomorphism. The detuning \(\Omega\) is represented modulo one and restricted to the fundamental interval \([0,1]\). A \(1:2\) resonance means one positive full turn in exactly two iterates of the canonical lift. The total tongue width is the length in the detuning coordinate \(\Omega\), not in angular units \(2\pi\Omega\). The statements concern deterministic maps, not noisy forcing, and make no claim for \(K\ge1\).

## Proof
At a positively winding period-two orbit, strict monotonicity and \(\widetilde F^2(x)=x+2\pi\) imply \(x<\widetilde F(x)<x+2\pi\). Write the two lifted orbit points as \(x=m-\pi/2-d\) and \(y=m+\pi/2+d\), with \(y=\widetilde F_{K,\Omega}(x)\) and \(\widetilde F_{K,\Omega}(y)=x+2\pi\). Summing and subtracting the two orbit equations gives the exact, reversible relations
\[
2d=K\cos m\cos d,\qquad
\Omega-\tfrac12=-\frac{K}{2\pi}\sin m\sin d.
\]
Because \(0<K<1\), the canonical lift is strictly increasing. Every rotation-\(1/2\) two-orbit has \(|2d|\le K<1\), and for every \(m\), the first relation has exactly one \(d\in[-K/2,K/2]\): the function \(2d/\cos d\) is strictly increasing there. Conversely any such solution constructs an exact lifted two-orbit. Symmetries of \(m\) show that the attainable detunings form the interval centered at \(1/2\), with half-width \(D(K)=\frac{K}{2\pi}\max_{0\le m\le\pi/2}\sin m\sin d(m,K)\).

For \(0<m<\pi/2\), put \(d=d(m,K)>0\), so \(2d=K\cos m\cos d\). Eliminating \(m\) yields an exact width maximization:
\[
W(K)=\frac1\pi\max_{0<d<d_{\max}(K)}\sin d\sqrt{K^2-4d^2\sec^2 d},
\]
where \(d_{\max}\in(0,\pi/2)\) uniquely solves \(2d_{\max}\sec d_{\max}=K\). The objective vanishes at both endpoints and is positive inside. Differentiating its logarithm shows that an interior extremum obeys
\[
K^2=Q(d):=4d\sec^2d\bigl(d\sec^2d+\tan d\bigr).
\]
Every positive factor of \(Q\) is strictly increasing on \((0,\pi/2)\); hence \(Q\) is strictly increasing from zero to infinity. At \(d_{\max}\), \(Q(d_{\max})>4d_{\max}^2\sec^2d_{\max}=K^2\). Thus exactly one critical point occurs inside the feasible interval; it is the unique global maximizer \(d_K\). This proves the exact root formula.

For monotonicity use the reversible relation \(2d=K\cos m\cos d\) to rewrite the normalized width as
\[
R(K):=\frac{4\pi W(K)}{K^2}=\max_{0\le m\le\pi/2}\sin(2m)\,\frac{\sin(2d(m,K))}{2d(m,K)}.
\]
For any fixed interior \(m\), \(d(m,K)\) strictly increases with \(K\), whereas \(\sin v/v\) strictly decreases for \(0<v<1\). The maximizing \(m\) is interior because the boundary values are zero; comparing the maximizer at two coupling strengths therefore yields \(R(K_2)<R(K_1)\) whenever \(0<K_1<K_2<1\). Also \(0<R(K)<1\); as \(K\downarrow0\), the expression converges uniformly to \(\sin2m\), so \(R(K)\to1\).

Finally, let \(A=K\cos m/2\). The implicit relation \(d=A\cos d\) gives \(d=A-A^3/2+O(A^5)\), whence \(\sin(2d)/(2d)=1-\frac23A^2+\frac45A^4+O(A^6)\). Therefore
\[
R(K)=\max_m\sin(2m)\left(1-\frac{K^2\cos^2m}{6}+\frac{K^4\cos^4m}{20}+O(K^6)\right).
\]
The nondegenerate maximum lies at \(m=\pi/4+K^2/24+O(K^4)\). Substitution gives \(R(K)=1-K^2/12+23K^4/1440+O(K^6)\), completing the expansion.

## Verification
The accompanying \(check_half_tongue.py\) numerically implements the midpoint maximization and the independently derived unique-root formula, comparing them for seven coupling strengths; it also checks the strict normalized-width trend and the small-coupling expansion. Direct numerical roots of the *original* second-iterate equation locate four period-two points inside the tongue and none immediately outside at \(K=0.8\). All printed values are approximate corroboration; the preceding analytic argument proves the all-parameter assertion. To replay, install Python 3 and SciPy, then run `python check_half_tongue.py` in the directory containing the script.

## Relationship to prior work
The Arnold circle map and the qualitative half-resonance tongue are classical. Schilder and Peckham (2006), section 4.1 and figure 5, compute resonant tongues for this exact map through numerical continuation but do not formulate the present exact global half-tongue root equation or the strict normalized-width monotonicity. Davie (1996) studies the width of sine-map tongues and is a particularly relevant antecedent; accessible abstract material describes asymptotic widths for rotation number \(1/n\), not the exact all-coupling \(1/2\) formula. Its full article was not inspectable, so coverage risk is explicitly retained. Duchet and collaborators (2023), section 4.1, derive a second-order small-coupling approximation for \((2p-1):2\) tongues, consistent with the leading term here; it does not provide an exact finite-coupling monotonicity theorem.

## Limitations
There is no independent review, and historical priority is not established. In particular, complete coverage comparisons with the inaccessible Davie article remain a publication risk. The result does not address higher-denominator tongues, \(K\ge1\), noise, or the attraction rates of periodic orbits. Small-coupling asymptotics are proved only as \(K\downarrow0\), while the exact root formula and normalized monotonicity cover every \(0<K<1\).

## References
1. F. Schilder and B. B. Peckham, *Computing Arnol'd Tongue Scenarios*, working paper, 30 January 2006, section 4.1. https://www.d.umn.edu/~bpeckham/export/Papers/ComputingArnold_submit.pdf ; https://research-information.bris.ac.uk/en/publications/computing-arnold-tongue-scenarios/ .
2. A. M. Davie, *The width of Arnold tongues for the sine circle map*, Nonlinearity **9** (1996), 421–432. https://www.semanticscholar.org/paper/The-width-of-Arnold-tongues-for-the-sine-circle-map-Davie/1169411886e24dfa16d02b2036c1cdddc5825420 .
3. B. Duchet et al., *How to entrain a selected neuronal rhythm but not others: open-loop dithered brain stimulation for selective entrainment*, Journal of Neural Engineering **20** (2023), 026003, section 4.1. https://pmc.ncbi.nlm.nih.gov/articles/PMC7614323/ .

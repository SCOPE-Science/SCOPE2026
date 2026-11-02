# Rare phase errors reverse complete-swap persistence in a two-patch population

## Finding

Let \(a>1\), \(0<b<1/a\), and let a population reproduce in two patches, one favourable in each environmental state. After reproduction, a fraction \(m\in[0,1]\) of individuals swaps patches. For an environmental state \(e\in\{A,B\}\), put
\[
P_m=\begin{pmatrix}1-m&m\\m&1-m\end{pmatrix},\qquad
M_A=P_m\operatorname{diag}(a,b),\quad
M_B=P_m\operatorname{diag}(b,a),\quad x_{t+1}=M_{E_t}x_t.
\]
Here \(x_0\) has strictly positive coordinates. If the environmental state switches at each time step with probability \(q\), independently of previous switch decisions, the following hold.

**(I) Two exact deterministic thresholds.** Set
\[
C=a+b-2ab,\qquad
m_F=\frac{(a-1)(1-b)}{C},\qquad
m_P=\frac{1-ab}{C}.
\]
These numbers lie strictly between zero and one. Each fixed-state matrix \(M_A,M_B\) has spectral radius less than one exactly when \(m>m_F\); a perfectly alternating environment (\(q=1\)) has positive asymptotic growth exactly when \(m>m_P\). Hence every \(m\in(\max\{m_F,m_P\},1]\) produces growth under perfect alternation even though both frozen environmental systems are individually subcritical.

**(II) Singular failure of complete swapping.** For every \(0<q<1\), at either \(m=0\) or \(m=1\), the almost-sure population growth exponent exists and equals
\[
\gamma(0,q)=\gamma(1,q)=\tfrac12\log(ab)<0.
\]
At complete swapping and perfect alternation, however,
\[
\gamma(1,1)=\log a>0.
\]
Thus arbitrarily rare non-switches of the environment reverse the sign of complete-swapping growth; the limit in \(q\) at this deterministic boundary is discontinuous.

**(III) Robust recovery at strictly interior dispersal.** Fix \(m\in(\max\{m_F,m_P\},1)\) and let \(\lambda=\sqrt{\rho(M_BM_A)}>1\). Choose a positive left Perron vector \(u_A\) of \(M_BM_A\), and set \(u_B=u_AM_B/\lambda\). Define
\[
r=\min_{e\in\{A,B\},j\in\{1,2\}}
\frac{(u_eM_e)_j}{(u_e)_j},\qquad
R=\max_{e\in\{A,B\},j\in\{1,2\}}
\frac{(u_eM_e)_j}{(u_e)_j}.
\]
Both are finite and positive. With probability one, for every \(0<q<1\),
\[
q\log\lambda+(1-q)\log r\ \le\ 
\liminf_{t\to\infty}\frac{\log\|x_t\|_1}{t}
\ \le\ \limsup_{t\to\infty}\frac{\log\|x_t\|_1}{t}
\ \le\ q\log\lambda+(1-q)\log R.
\]
Consequently there is a nonempty interval of imperfect-switching probabilities \(q<1\), arbitrarily close to one, for which the partially swapping population increases exponentially almost surely, while both zero swapping and complete swapping decline exponentially.

**(IV) Exact rational witness away from perfect alternation.** Take \(a=3\), \(b=1/4\), \(m=9/10\), and \(q=3/4\). Both frozen systems are subcritical. Taking \(u_A=(99,1)\), \(u_B=(1,99)\) gives the one-step lower factors \(27/10\) on a switch and \(18/55\) on a non-switch. Hence
\[
\liminf_{t\to\infty}\frac{\log\|x_t\|_1}{t}
\ge\tfrac14\log\left(\frac{177147}{27500}\right)>0,
\]
whereas at \(m=0\) or \(m=1\) the exponent is \(\tfrac12\log(3/4)<0\) for the same stochastic environment.

## Assumptions and scope

Time is discrete and patches exchange fractions *after* local reproduction. Environmental state \(A\) gives patch multipliers \((a,b)\), and state \(B\) gives \((b,a)\). The environmental process does not depend on population size or distribution. For \(0<q<1\), take independent Bernoulli switch indicators of parameter \(q\), so \(\Pr(E_{t+1}\ne E_t\mid E_t)=q\); the initial state may be fixed. All assertions about asymptotic stochastic growth are almost sure over this environment sequence, for any strictly positive initial abundance vector. Population persistence here means exponential growth of the *linear rare-population model*, not demographic survival of a finite stochastic population or bounded nonlinear persistence.

## Proof

**Thresholds.** Because \(ab<1\) and \(a>1>b\), we have \(C>0\) and
\[
C-(a-1)(1-b)=1-ab>0,\qquad C-(1-ab)=(a-1)(1-b)>0.
\]
Therefore \(0<m_F,m_P<1\). Direct multiplication gives
\[
\det(I-M_A)=\det(I-M_B)=(1-a)(1-b)+Cm=C(m-m_F).
\]
The matrices are nonnegative and irreducible for \(m>0\), and their non-Perron eigenvalues are strictly less than one: their determinant has absolute value \(ab|1-2m|<1\) and the Perron eigenvalue is the larger positive eigenvalue in modulus. Thus the sign of \(\det(I-M_A)\) decides whether the Perron root is below or above one. The same conclusion holds at \(m=1\), with eigenvalues \(\pm\sqrt{ab}\), and at \(m=0\), with eigenvalues \(a,b\). This proves the frozen-state condition.

For the two-year map \(T=M_BM_A\), direct multiplication gives
\[
\det(I-T)=(1-ab-Cm)\,[1-ab+m(a+b+2ab)],
\quad \det T=(ab)^2(1-2m)^2<1.
\]
The second factor is positive. The two nonnegative real eigenvalues of \(T\) are its Perron root and a second eigenvalue in \([0,1)\), since \(T\) is a product of two matrices with positive determinant or their negative determinants and \(\det T<1\). Hence \(\rho(T)>1\) precisely when \(\det(I-T)<0\), namely \(m>m_P\). The assertion includes \(m=0\), where \(T=abI\), and \(m=1\), where \(T=\operatorname{diag}(a^2,b^2)\) after a suitable starting phase. The annual growth exponent for perfect alternation is \(\frac12\log\rho(T)\) for every strictly positive initial vector.

**Complete swapping with imperfect environmental alternation.** At \(m=0\), the two coordinates never move. Each coordinate experiences \(a\) in exactly half the years and \(b\) in the other half almost surely, by ergodicity of the symmetric two-state Markov environment for \(0<q<1\). Their individual exponents, and hence that of their sum, are \(\frac12\log(ab)\).

At \(m=1\), each lineage swaps patches in every year. Write \(L_t\) for its patch before reproduction and \(F_t\) for the favourable patch in year \(t\). The match indicator \(1_{\{L_t=F_t\}}\) changes exactly when the environment *fails* to switch. Because \(0<1-q<1\), this two-state match process is irreducible and aperiodic with stationary probabilities \((1/2,1/2)\). The ergodic theorem gives a half-and-half frequency of multipliers \(a,b\), so each positive initial lineage and their sum have exponent \(\frac12\log(ab)\). At \(q=1\), by contrast, matching status never changes. Since the initial vector is strictly positive, one lineage always matches and grows by \(a\) each year; the total has exponent \(\log a\).

**Persistence of interior dispersal under small phase noise.** Fix the stated \(m\in(0,1)\); then \(M_A,M_B\) are strictly positive. By Perron–Frobenius, \(T=M_BM_A\) has a positive left eigenvector \(u_A\) with eigenvalue \(\lambda^2\). Defining \(u_B=u_AM_B/\lambda\) gives the exact switch identities
\[
u_AM_B=\lambda u_B,\qquad u_BM_A=\lambda u_A.
\]
If \(E_{t+1}\ne E_t\), the weighted abundance \(W_t=u_{E_t}x_t\) therefore satisfies \(W_{t+1}=\lambda W_t\). If \(E_{t+1}=E_t\), positivity and the definitions of \(r,R\) give \(rW_t\le W_{t+1}\le RW_t\). Let \(N_t\) be the number of environmental switches in the first \(t\) steps. Multiplying the inequalities gives
\[
\lambda^{N_t}r^{t-N_t}W_0\le W_t\le\lambda^{N_t}R^{t-N_t}W_0.
\]
The strong law applied to the independent switch indicators gives \(N_t/t\to q\). As the finitely many positive coordinates of \(u_A,u_B\) uniformly bound \(W_t\) above and below by positive constant multiples of \(\|x_t\|_1\), taking logarithms proves (III). Because \(\lambda>1\) and \(r>0\), the lower bound is positive whenever \(q\) is sufficiently close to one. The same bounds imply convergence of upper and lower asymptotic growth estimates to \(\log\lambda\) as \(q\uparrow1\) for every fixed strictly interior \(m\).

**Rational witness.** With the parameters in (IV),
\[
M_A=\begin{pmatrix}3/10&9/40\\27/10&1/40\end{pmatrix},\qquad
M_B=\begin{pmatrix}1/40&27/10\\9/40&3/10\end{pmatrix}.
\]
Here \(m_F=6/7\), \(m_P=1/7\), so the frozen systems are subcritical. The stated rows satisfy exactly
\[
\begin{aligned}
u_AM_A&=(162/5,223/10)\ge(18/55)u_A,\\
u_BM_B&=(223/10,162/5)\ge(18/55)u_B,\\
u_AM_B&=(27/10,1338/5)\ge(27/10)u_B,\\
u_BM_A&=(1338/5,27/10)\ge(27/10)u_A.
\end{aligned}
\]
All inequalities are componentwise. Thus \(W_t\ge (27/10)^{N_t}(18/55)^{t-N_t}W_0\). For \(q=3/4\), the claimed lower bound follows from \((27/10)^3(18/55)=177147/27500>1\). The endpoint exponent follows from the preceding parity argument. No floating-point approximation is needed for any of these conclusions.

## Verification

The independent script `check.py` uses the Python standard library `fractions.Fraction` to recompute the rational witness, all four weighted-vector inequalities, the two determinant factorizations on selected rational parameter sets, and the strict growth certificate. Run with `python3 check.py`. These finite checks detect arithmetic or transcription errors in the example; the parameter-uniform and almost-sure conclusions follow from the analytical arguments above, not finite enumeration.

## Relationship to prior work

Schreiber (2010) studies stochastic spatially structured population growth under temporal correlations and derives perturbative formulas for partially mixed systems. Schreiber and Li (2011) prove evolutionary dispersal results for *period-two* environments, including a matrix spectral monotonicity theorem. Williams and Hastings (2011) review the ecological importance of switching between individually declining systems and its relation to Parrondo-like growth reversals. Thus the fact that temporal mixing can reverse decay is established prior knowledge, and the periodic two-matrix spectral calculation is not presented as a new general principle.

The contribution assessed here is the joint boundary phenomenon in this specific two-patch model: the exact complete-swap growth discontinuity at perfectly alternating versus arbitrarily imperfect Markov timing, its contrast with the strictly interior positive-dispersal regime, and the simultaneous frozen-system-extinction and exact rational noisy-persistence witness. General stochastic matrix theory and environmental-correlation theory provide conceptual context but do not, in the portions inspected, state or imply this particular endpoint classification without additional hypotheses and calculations.

## Limitations

The model is linear, spatially symmetric, and ignores density feedback, demographic noise, dispersal costs, and environmental switching driven by population state. The exact endpoint discontinuity relies on *exact* full swapping of individuals and a binary environmental process. For interior \(m\), only an explicit sufficient near-alternation criterion is provided, not an exact critical \(q\) for every parameter choice. At incomplete source access or under a stronger unpublished or uninspected result, historical priority could change. The theorem is a mathematical benchmark, not a recommendation about specific real habitats.

## References

1. S. J. Schreiber (2010), *Interactive effects of temporal correlations, spatial heterogeneity and dispersal on population persistence*, Proceedings of the Royal Society B **277**, 1907–1914. First online 17 February 2010. DOI: 10.1098/rspb.2009.2006. Author-hosted open text: https://schreiber.faculty.ucdavis.edu/wp-content/uploads/sites/568/2019/10/prsb-10.pdf.
2. S. J. Schreiber and C.-K. Li (2011), *Evolution of unconditional dispersal in periodic environments*, Journal of Biological Dynamics **5**, 120–134. First online 19 February 2011. DOI: 10.1080/17513758.2010.525667. Author-hosted open text: https://schreiber.faculty.ucdavis.edu/wp-content/uploads/sites/568/2021/04/Evolution-of-unconditional-dispersal-in-periodic-environments.pdf.
3. P. D. Williams and A. Hastings (2011), *Paradoxical persistence through mixed-system dynamics: towards a unified perspective of reversal behaviours in evolutionary ecology*, Proceedings of the Royal Society B **278**, 1281–1290. First online 26 January 2011. DOI: 10.1098/rspb.2010.2074. https://pmc.ncbi.nlm.nih.gov/articles/PMC3061147/.

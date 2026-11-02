# The first pure–mixed numerical-information gap: a sharp three-observable qutrit law

## Finding

A pair of density matrices need not be replaceable by a pair of pure states while preserving bounded differences of three observable expectations and the difference of a fourth expectation. The threshold is exact: there is no such relaxation gap for **any** family with at most two measured Hermitian observables, nor for **any** family on a complex Hilbert space of dimension at most two. A three-dimensional witness with three measurements has the full anisotropic error profile

\[
\Delta_{\mathrm{pure}}(\boldsymbol\varepsilon)=2\min\{1,\|\boldsymbol\varepsilon\|_2\},\qquad
\Delta_{\mathrm{mixed}}(\boldsymbol\varepsilon)=2,
\]

for every \(\boldsymbol\varepsilon\in[0,\infty)^3\). Both maxima are attained. This is simultaneously an exact robust-information law and a sharp minimality statement in the number of measurements and ambient dimension.

In the example the three measured expectations determine the fourth exactly on **pure** states through a non-affine radial map, but do not determine it on mixed states even with zero measurement error.

## Assumptions and scope

Throughout, \(H\) is a nonzero finite-dimensional complex Hilbert space, \(m\ge0\) is an integer, and \(A_1,\ldots,A_m,B\) are self-adjoint operators on \(H\). A density matrix \(\rho\) is positive semidefinite with trace one; it is *pure* when it has rank one. Given nonnegative error budgets \(\varepsilon_j\), set

\[
\begin{aligned}
\Delta_{\mathrm{mixed}}(B\mid\boldsymbol A;\boldsymbol\varepsilon)
&=\max_{\rho,\tau}\left|\operatorname{tr}B(\rho-\tau)\right|,\\
\Delta_{\mathrm{pure}}(B\mid\boldsymbol A;\boldsymbol\varepsilon)
&=\max_{\rho,\tau\ \mathrm{rank}\,1}\left|\operatorname{tr}B(\rho-\tau)\right|,
\end{aligned}
\]

where in both cases \(\rho,\tau\) are density matrices obeying \(\left|\operatorname{tr}A_j(\rho-\tau)\right|\le\varepsilon_j\) for every \(j\). The feasible pairs are nonempty, and all maxima exist by compactness.

The universal assertion is that \(\Delta_{\mathrm{pure}}=\Delta_{\mathrm{mixed}}\) whenever \(m\le2\) or \(\dim H\le2\), for **every** choice of observables and budgets. To show that both restrictions are sharp, work in \(\mathbb C^3=\mathbb C^2\oplus\mathbb C\), and define

\[
\sigma_1=\begin{pmatrix}0&1\\1&0\end{pmatrix},\quad
\sigma_2=\begin{pmatrix}0&-i\\i&0\end{pmatrix},\quad
\sigma_3=\begin{pmatrix}1&0\\0&-1\end{pmatrix},
\]

\[
A_j=\sigma_j\oplus0\quad(j=1,2,3),\qquad
B=I_2\oplus(-1).
\]

Additional zero observables and additional negative-one coordinates extend the counterexample to \(m\ge3\) and \(\dim H\ge3\), respectively, without changing its profile.

## Proof

**1. No gap for at most two measurements, in any finite dimension.** Consider the compact convex set \(K\) of all feasible pairs \((\rho,\tau)\). One of the two linear functionals \(\pm\operatorname{tr}B(\rho-\tau)\) attains the absolute maximum; a maximizing extreme point of \(K\) exists. Let its two state ranks be positive integers \(r,s\). Hermitian variations supported on their respective ranges form a real vector space of dimension \(r^2+s^2\). Requiring both traces to remain one gives two homogeneous linear conditions. Each active measurement inequality adds at most one further condition, including when its error budget is zero (then its upper and lower active inequalities are the same equality). There are at most \(m\) such conditions.

If \(r^2+s^2>m+2\), a nonzero supported Hermitian variation satisfies all these conditions. Both states are strictly positive on their supports, so sufficiently small positive and negative multiples preserve positivity; inactive inequalities remain feasible by strict slackness. This writes the alleged extreme pair as the midpoint of two distinct feasible pairs, a contradiction. Hence every extreme pair has \(r^2+s^2\le m+2\). When \(m\le2\), the only positive-integer possibility is \(r=s=1\), since the next possible sum of squares is \(1^2+2^2=5\). Thus the mixed maximum is achieved by pure states. The reverse inequality is automatic, proving equality of the maxima.

**2. No gap for qubits, regardless of measurement count.** For \(\dim H=2\), every density matrix is uniquely \(\rho=(I+u\cdot\boldsymbol\sigma)/2\), with \(u\in\mathbb R^3\) and \(\|u\|_2\le1\). Given two states with Bloch vectors \(u,v\), put \(d=u-v\). Then \(\|d\|_2\le2\). Choose \(w\perp d\) with \(\|w\|_2^2=1-\|d\|_2^2/4\); if \(d=0\), choose any unit \(w\). The vectors \(u'=w+d/2\) and \(v'=w-d/2\) both have unit length and satisfy \(u'-v'=d\). They define pure-state density matrices whose **operator difference** equals the original density-matrix difference. Therefore every constraint value and target difference are preserved for arbitrary \(m\), \(B\), and \(\boldsymbol\varepsilon\). Dimension one is immediate.

**3. Exact qutrit pure-state profile.** Let \(x=(a,b,c)\) be any unit vector in \(\mathbb C^3\). Define its measurement vector \(v(x)=(\langle A_jx,x\rangle)_{j=1}^3\in\mathbb R^3\), and let \(r=|a|^2+|b|^2\). Direct Pauli multiplication gives

\[
 v(x)=(2\operatorname{Re}(\overline a b),\ 2\operatorname{Im}(\overline a b),\ |a|^2-|b|^2),
 \quad \|v(x)\|_2^2=(|a|^2+|b|^2)^2=r^2.
\]

Since \(r\ge0\) and \(|c|^2=1-r\),

\[
 \langle Bx,x\rangle=2r-1=2\|v(x)\|_2-1.
\]

For any feasible pair of pure states \(x,y\), the reverse triangle inequality gives

\[
\left|\langle Bx,x\rangle-\langle By,y\rangle\right|
=2\left|\|v(x)\|_2-\|v(y)\|_2\right|
\le2\|v(x)-v(y)\|_2
\le 2\|\boldsymbol\varepsilon\|_2.
\]

The spectral spread of \(B\) is two, so the same difference is at most two. Write \(L=\|\boldsymbol\varepsilon\|_2\) and \(t=\min\{1,L\}\). If \(L>0\), take a normalized two-spinor \(\xi\in\mathbb C^2\) whose Pauli expectation triple is \(\boldsymbol\varepsilon/L\) (every unit Bloch vector arises this way). Put \(x=(\sqrt t\,\xi,\sqrt{1-t})\) and \(y=(0,0,1)\). Then \(v(x)=t\boldsymbol\varepsilon/L\), \(v(y)=0\), and all coordinate differences are at most their budgets. The target difference equals \(2t\), giving equality. For \(L=0\), take \(x=y=(0,0,1)\), obtaining equality at zero. Thus the displayed pure-state formula holds for all budgets, including the boundary \(L=1\).

The pure-state target connector is genuinely non-affine on the full measured-data ball: its restriction to opposite unit measurement vectors equals one, while its value at their midpoint zero is minus one. So this is exact but nonlinear pure-state numerical information.

**4. Exact mixed-state profile and minimality.** The two density matrices

\[
 \rho=\left(\frac12 I_2\right)\oplus0,\qquad
 \tau=0_2\oplus1
\]

have identical expectation zero for all three measured observables but satisfy \(\operatorname{tr}(B\rho)=1\) and \(\operatorname{tr}(B\tau)=-1\). They are feasible for *every* budget and achieve target difference two, which no state pair can exceed because the spectrum of \(B\) is \(\{-1,1\}\). Hence \(\Delta_{\mathrm{mixed}}=2\) for all budgets. Combining the formulas gives the exact relaxation gap

\[
 \Delta_{\mathrm{mixed}}-\Delta_{\mathrm{pure}}
 =2\left[1-\min\{1,\|\boldsymbol\varepsilon\|_2\}\right].
\]

It is positive precisely for \(\|\boldsymbol\varepsilon\|_2<1\), reaches two at zero error, and vanishes sharply at \(\|\boldsymbol\varepsilon\|_2=1\). Steps 1 and 2 rule out such a gap in any smaller measurement count or complex Hilbert dimension. Therefore three measurements in dimension three are simultaneously minimal.

## Verification

The proof is algebraic and finite-dimensional, with all quantifiers and equality constructions explicit. A supplementary standard-library Python script `verify_three_obs.py` checks the Pauli norm identity, qubit Bloch-difference replacement, the exact tolerance-budget witness, and endpoint cases. The reproducibility command is `python verify_three_obs.py`. These finite checks are supporting tests; the uniform statements follow from Steps 1–4 and not from random sampling.

## Relationship to prior work

D. M. Johnson, *Numerical Information of Hilbert Space Operators* (arXiv:2610.29826v1, 21 October 2026), proves affine-rigidity of a target expectation determined by a single complex numerical-range map (Theorem 5.2), corresponding to two Hermitian real coordinates. His work motivates asking what changes for three real measurements and for nonzero measurement error, but does not contain the present three-coordinate radial connector or the pure–mixed error profile.

K. Szymański, S. Weis, and K. Życzkowski, *Classification of joint numerical ranges of three hermitian matrices of size three* (arXiv:1603.06569, later Linear Algebra and its Applications 545), classify the **image** of three Hermitian qutrit measurements, including convex balls. That classification does not determine the values of a separately specified fourth observable along measurement fibers, and does not provide the present exact robust pure-versus-mixed comparison. In particular, the convexity of the *three-coordinate projection* is compatible with the mixed-state ambiguity established here. General Bloch-sphere and joint numerical-range facts used above are standard and are not presented as new.

## Limitations

The counterexample is finite-dimensional and uses a reducible qutrit observable triple; it is not a universal formula for arbitrary triples of three observables. The no-gap assertions apply to **pairs of states with componentwise absolute expectation-difference budgets** and do not address other loss functions, statistical sampling noise, or non-Hermitian measurement protocols. The exact law is an algebraic model rather than an experimental noise-calibration theorem. The two-measurement extreme-point argument is an elementary instance of convex rank reduction. The Bloch identity is classical; the possible existence of a prior paper giving the same combined minimality-and-error-profile theorem under different terminology is a residual originality risk. No independent mathematical validation or definitive publication-priority determination has occurred.

## References

1. Dylan M. Johnson, *Numerical Information of Hilbert Space Operators*, arXiv:2610.29826v1, first submitted 21 October 2026. https://arxiv.org/html/2610.29826v1
2. Konrad Szymański, Stephan Weis, and Karol Życzkowski, *Classification of joint numerical ranges of three hermitian matrices of size three*, arXiv:1603.06569, first submitted 20 March 2016; *Linear Algebra and its Applications* **545**, 148–173. https://arxiv.org/abs/1603.06569
3. Y.-H. Au-Yeung and Y.-T. Poon, *A remark on the convexity and positive definiteness concerning Hermitian matrices*, *Southeast Asian Bulletin of Mathematics* **3** (1979), 85–92 (background convexity theorem, cited by Reference 2).

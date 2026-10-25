# Exact quenched–annealed rotation-complexity spectra for a Bernoulli circle map

## Finding

Fix \(0<p<1\). Consider independent \(+\) and \(-\) choices with respective probabilities \(p\) and \(1-p\), and the degree-one real lifts \(F_\pm(x+1)=F_\pm(x)+1\) determined for \(0\le x<1\) by
\[
F_+(x)=\begin{cases}3x,&0\le x<2/3,\\4-3x,&2/3\le x<1,\end{cases}\qquad
F_-(x)=\begin{cases}-3x,&0\le x<1/3,\\3x-2,&1/3\le x<1.\end{cases}
\]
Each map has three full affine circle branches, indexed \(0,1,2\) according to the ternary intervals. The integer lift increment of a branch is
\[
(k(+,0),k(+,1),k(+,2))=(0,1,1),\qquad
(k(-,0),k(-,1),k(-,2))=(-1,-1,0).
\]
For an environment \(\omega\) and length-\(n\) word \(w\in\{0,1,2\}^n\), let \(K_\omega(w)=\sum_{j=1}^n k(\omega_j,w_j)\). Write \(C_{\omega,n}(r,\varepsilon)\) for the number of length-\(n\) branch cylinders with \(|K_\omega(w)/n-r|<\varepsilon\), and \(A_n(r,\varepsilon)=\mathbb E_\omega C_{\omega,n}(r,\varepsilon)\). Use natural logarithms and \(\log0=-\infty\). Define the microcanonical quenched and annealed rotation-complexity rates, respectively, by
\[
H_{\mathrm q}(r)=\lim_{\varepsilon\downarrow0}\lim_{n\to\infty}\frac1n\log C_{\omega,n}(r,\varepsilon),\qquad
H_{\mathrm a}(r)=\lim_{\varepsilon\downarrow0}\lim_{n\to\infty}\frac1n\log A_n(r,\varepsilon).
\]
The first formula is asserted for almost every environment, simultaneously for every real \(r\); the inner limits exist (possibly \(-\infty\)) for every \(\varepsilon>0\) except at immaterial interval-endpoint conventions, for which the outer limit gives the same rate. Equivalently one may use matching upper and lower exponential rates inside the outer limit.

**Theorem.** Both rates exist and are deterministic. On \(p-1\le r\le p\),
\[
H_{\mathrm q}(r)=\inf_{t\in\mathbb R}\{P_{\mathrm q}(t)-tr\},\qquad
P_{\mathrm q}(t)=p\log(1+2e^t)+(1-p)\log(1+2e^{-t});
\]
outside this interval \(H_{\mathrm q}(r)=-\infty\). On \(-1\le r\le1\),
\[
H_{\mathrm a}(r)=\inf_{t\in\mathbb R}\{P_{\mathrm a}(t)-tr\},\qquad
P_{\mathrm a}(t)=\log(1+2pe^t+2(1-p)e^{-t});
\]
outside this interval \(H_{\mathrm a}(r)=-\infty\). At the extreme accessible values,
\[
H_{\mathrm q}(p)=p\log2,\quad H_{\mathrm q}(p-1)=(1-p)\log2,\quad
H_{\mathrm a}(1)=\log(2p),\quad H_{\mathrm a}(-1)=\log(2(1-p)).
\]
Set \(r_*=(4p-2)/3\). Both spectra attain \(\log3\) precisely at \(r_*\). On the full quenched interval, the **annealed–quenched gap is strict** except at this common maximum:
\[
H_{\mathrm a}(r)>H_{\mathrm q}(r)\quad(r\in[p-1,p],\ r\ne r_*).
\]
Their local curvatures at the maximum differ explicitly:
\[
H_{\mathrm q}''(r_*)=-\frac92,\qquad
H_{\mathrm a}''(r_*)=-\frac{9}{6-(4p-2)^2}.
\]
In particular, quenched curvature is independent of environmental bias. The quenched extreme-rate boundary layers, as \(\delta\downarrow0\), are
\[
\begin{aligned}
H_{\mathrm q}(p-\delta)&=p\log2+\delta\Bigl[1+\log\frac{(4-3p)/2}{\delta}\Bigr]+O_p(\delta^2),\\
H_{\mathrm q}(p-1+\delta)&=(1-p)\log2+\delta\Bigl[1+\log\frac{(1+3p)/2}{\delta}\Bigr]+O_p(\delta^2).
\end{aligned}
\]

## Assumptions and scope

The environment is the one-sided independent Bernoulli process with \(0<p<1\). Branch cylinders are the nonempty ternary inverse-branch intervals, each of length \(3^{-n}\). They count finite orbit histories, not distinct invariant measures. If \(x\) lies in the interior of a cylinder labelled \(w\), the true lift displacement obeys \(F_\omega^{(n)}(x)-x=K_\omega(w)+y_n-y_0\), where \(y_0,y_n\in[0,1]\); consequently replacing the integer statistic by the actual displacement average changes each constraint by at most \(1/n\) and leaves the rates unchanged. No claim about upper-capacity entropy of infinite-time level sets is made: those notions can differ from these microcanonical rates.

The annealed quantity is a logarithmic growth rate **of expected cylinder counts**. It is not claimed to be a topological entropy of a typical realization; it can be negative at extremely rare rotation rates.

## Proof

**Full branches and the exact generating functions.** On each ternary cell, the induced circle map is an affine homeomorphism onto the circle with derivative of absolute value three. Inductive inverse branches therefore give exactly one interval for each length-\(n\) word. Writing \(F_{\omega_j}(y_{j-1})=k(\omega_j,w_j)+y_j\) in compatible unit representatives, degree-one equivariance gives the telescope in the preceding section. With \(N_+(n)=\#\{1\le j\le n:\omega_j=+\}\) and \(N_-(n)=n-N_+(n)\), the **finite-time identity** is
\[
\sum_{w\in\{0,1,2\}^n}z^{K_\omega(w)}
=(1+2z)^{N_+(n)}(1+2z^{-1})^{N_-(n)}.
\]
Taking the environment expectation independently at each index yields
\[
\mathbb E_\omega\sum_w z^{K_\omega(w)}
=(1+2pz+2(1-p)z^{-1})^n.
\]
Thus the two exponential partition functions converge at every real \(t\) to \(P_{\mathrm q}(t)\) and \(P_{\mathrm a}(t)\) respectively; in the first case use the strong law \(N_+(n)/n\to p\). This convergence holds on one environment set independent of \(t\).

**Matching exponential bounds.** Fix a finite real \(t\), and give each branch letter at time \(j\) probability proportional to \(\exp(tk(\omega_j,a))\). Its product law assigns to a word \(w\) the weight \(\exp(tK_\omega(w)-\log Z_{\omega,n}(t))\). The sum of the independent bounded increment variables has a mean divided by \(n\) converging to \(P_{\mathrm q}'(t)\) and variance \(O(n)\). Chebyshev's inequality gives probability tending to one for every fixed positive window about this mean. Converting this probability back to an unweighted word count gives the lower exponential bound \(P_{\mathrm q}(t)-tP_{\mathrm q}'(t)\), with an arbitrarily small window correction. The elementary Chernoff weighted-sum estimate gives the corresponding upper bound and then its infimum over \(t\). Since \(P_{\mathrm q}\) is strictly convex and \(P_{\mathrm q}'(\mathbb R)=(p-1,p)\), the bounds agree for each interior rate. For a fixed window, applying the same argument to its interior rates and taking the supremum of their Legendre values establishes the inner exponential limit; sending the window width down to zero gives the claimed spectrum. The proof for the annealed polynomial is identical: normalize the three positive coefficients at each time into an iid random variable with values \(-1,0,1\). Its pressure is \(P_{\mathrm a}\), and its derivative ranges over \((-1,1)\). Values outside the closed respective derivative ranges are eventually impossible in sufficiently narrow windows.

At the upper quenched endpoint every plus step allows exactly two maximizing branch choices and every minus step exactly one; the number of perfectly maximizing words is \(2^{N_+(n)}\). At the lower endpoint it is \(2^{N_-(n)}\). These counts, together with the limiting pressures, establish both endpoint values. For the annealed endpoints the expected counts of maximizing words are \((2p)^n\) and \((2(1-p))^n\). This also proves the endpoint formulas without making a hidden assumption about exact realization of the asymptotic environmental frequency.

**The strict gap and curvature.** The strict concavity of the logarithm gives \(P_{\mathrm a}(t)>P_{\mathrm q}(t)\) at every \(t\ne0\): the two one-step partition sums are unequal precisely for nonzero \(t\), and \(0<p<1\). Their derivatives at zero coincide, equal to \(r_*\), and both pressure values at zero equal \(\log3\). For any other \(r\in[p-1,p]\), the annealed Legendre optimizer is a finite nonzero \(t\); evaluating the quenched Legendre infimum at this point proves the stated strict inequality. Direct differentiation gives \(P_{\mathrm q}''(0)=2/9\) and \(P_{\mathrm a}''(0)=[6-(4p-2)^2]/9\). The inverse-function relation for strictly convex Legendre transforms gives the curvature identities. Finally expand \(P_{\mathrm q}(t)\) in \(e^{-t}\) as \(t\to+\infty\), and in \(e^t\) as \(t\to-\infty\). The first corrections have respective coefficients \((4-3p)/2\) and \((1+3p)/2\); solving for the optimizer and substituting gives the two \(\delta\log(1/\delta)\) boundary expansions with the indicated error terms.

## Verification

The standalone `checker.py` uses only Python's standard library and exact rational arithmetic for finite branch identities. It verifies actual lift displacement identities over 726 constructed inverse-branch cylinders, the annealed polynomial identity for six lengths by explicit enumeration over both environmental signs, and 12 numerical strict-gap samples with independently optimized Legendre transforms. Run `python3 checker.py`; the accompanying `checker_output.txt` records the result. These are finite diagnostics; the infinite claims follow from the proof above, not the finite tests.

## Relationship to prior work

Li, Lloyd and Romaña (2026, arXiv:2606.16498v1, Examples 3.1 and 4.1) establish the model and compute its rotation interval \([p-1,p]\) and **unrestricted** random topological entropy \(\log3\). The present result computes a different and finer invariant, the entire family of rotation-constrained finite-branch complexity exponents, and distinguishes annealed rare-environment contributions from typical-fiber behavior. A related published mathematical result on ordered invariant graphs gives one zero-entropy realized orbit per rotation value, not exponential cylinder counts or this quenched–annealed comparison. General conditional-multifractal and random thermodynamic-formalism principles underlie the proof method; the contribution claimed here is the explicit two-spectrum classification, sharp strictly positive quenched boundary entropy, strict gap and parameter-independent curvature for these particular random circle maps. No claim of inventing the Legendre-transform method is made.

## Limitations

The result concerns exactly this pair of three-full-branch degree-one lifts and independent Bernoulli driving. It computes finite-time rotation-constrained itinerary counts; it does not claim equality with Bowen or upper-capacity entropies of noncompact infinite-time level sets or calculate Hausdorff dimensions of those level sets. Environmental correlations, other lift normalizations, non-full-branch perturbations and independent literature-priority verification are outside its scope. General existing relative-entropy theorems may imply the Legendre-transform step after symbolic coding; the special two-pressure formulas and derived quantitative contrasts are the specific assertions under consideration.

## References

1. Z. Li, S. Lloyd and S. Romaña, *Rotation Sets and Topological Entropy for Random Circle Endomorphisms*, arXiv:2606.16498v1 (first submitted 15 June 2026), especially Examples 3.1 and 4.1. https://arxiv.org/abs/2606.16498
2. D.-J. Feng and L. Shu, *Multifractal analysis for disintegrations of Gibbs measures and conditional Birkhoff averages*, Ergodic Theory Dynam. Systems (2009), DOI:10.1017/S0143385708000655.
3. M. Denker, Y. Kifer and M. Stadlbauer, *Thermodynamic formalism for random countable Markov shifts*, Discrete Contin. Dyn. Syst. 22 (2008), 131–164, DOI:10.3934/dcds.2008.22.131.

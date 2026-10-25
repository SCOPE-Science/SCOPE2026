# Poisson width loss and macroscopic exposed roots of transitive-tournament polytopes

## Finding
For every integer \(n\ge3\), consider the standard intrinsic-Euclidean directed-edge polytope
\[
P_n=\operatorname{conv}\{e_i-e_j:1\le i<j\le n\}\subset H_n,
\qquad H_n=\{x\in\mathbb R^n:\sum_i x_i=0\}.
\]
Write \(S_n=\operatorname{conv}\{\pm(e_i-e_j):1\le i<j\le n\}\), its symmetrically oriented counterpart. For a uniform random unit vector \(U_n\) in \(H_n\), let \(w_n\) and \(w_n^{\mathrm{sym}}\) be the directional widths of \(P_n\) and \(S_n\). Define
\[
b_n=\sqrt{2\log n}-\frac{\log\log n+\log(4\pi)}{2\sqrt{2\log n}},
\qquad a_n=(2\log n)^{-1/2}.
\]
Let \(\Pi^+,\Pi^-\) be independent Poisson point processes on \((0,1)\times\mathbb R\), each with intensity \(dt\,e^{-x}dx\). Put
\[
H_+=\max\{x:(t,x)\in\Pi^+\},\quad H_-=\max\{y:(s,y)\in\Pi^-\},
\]
\[
D_\rightarrow=\sup_{\substack{(t,x)\in\Pi^+,(s,y)\in\Pi^-\\t<s}}(x+y),
\qquad D_\leftarrow=\sup_{\substack{(t,x)\in\Pi^+,(s,y)\in\Pi^-\\t>s}}(x+y),
\]
and the universal positive random variable
\[
L=2(H_++H_-)-D_\rightarrow-D_\leftarrow.
\]
All four extrema are finite and are attained almost surely. The maximizing ordered pair in \(D_\rightarrow\) is unique almost surely; call its times \((T_+,T_-)\), with \(0<T_+<T_-<1\), and put \(J=T_--T_+\).

For a generic \(U_n\), let \(e_{I_n}-e_{K_n}\), \(I_n<K_n\), be the unique vertex exposed by \(U_n\). **The joint width-loss and exposed-root-gap theorem** is
\[
\boxed{\left(\frac{\sqrt{n-1}}{a_n}(w_n^{\mathrm{sym}}-w_n),\frac{K_n-I_n}{n}\right)\ \Longrightarrow\ (L,J).}
\tag{1}
\]
The distribution of \(J\) is supported strictly in \((0,1)\), and \(L>0\) almost surely. Consequently, the aggregate spherical normal-cone weight of the \(n-1\) simple-root vertices tends to zero:
\[
\boxed{\Pr(K_n-I_n=1)\longrightarrow0,\qquad
\lim_{\varepsilon\downarrow0}\limsup_{n\to\infty}\Pr(K_n-I_n\le\varepsilon n)=0.}
\tag{2}
\]
Conversely, in every dimension, precisely one of the two vertices exposed by the opposite directions \(U_n\) and \(-U_n\) realizes the full coordinate range, and
\[
\boxed{\Pr\bigl(\langle U_n,e_{I_n}-e_{K_n}\rangle=\max_i(U_n)_i-\min_j(U_n)_j\bigr)=\tfrac12.}
\tag{3}
\]

The width loss also converges in the mean. With \(\gamma_{\mathrm E}\) denoting Euler's constant, set
\[
M(t)=\sup\{y:(s,y)\in\Pi^-,\ s>t\},\quad
A=\int_0^1e^{M(t)}\,dt
\]
(the supremum over an empty set is \(-\infty\)). Then \(0<A<\infty\) almost surely and \(\mathbb E|\log A|<\infty\). The constant
\[
\boxed{C_*=\mathbb EL=2\bigl(\gamma_{\mathrm E}-\mathbb E\log A\bigr)\in(0,\infty)}
\tag{4}
\]
is intrinsic to this Poisson law. In particular,
\[
\boxed{\lim_{n\to\infty}\frac{\sqrt{n-1}}{a_n}
\bigl(\mathbb Ew_n^{\mathrm{sym}}-\mathbb Ew_n\bigr)=C_*.}
\tag{5}
\]
Both means nevertheless share the first-order asymptotic \(4\sqrt{2\log n/n}\). Formulae (1)--(5), not the classical positive-root construction, are the finding.

## Assumptions and scope
The vertices \(e_i-e_j\) use the standard orthonormal coordinate basis, not an arbitrary affine realization. Distances, widths, and random directions are intrinsic to \(H_n\) with its inherited Euclidean inner product. Every edge root is a vertex, and \(P_n\) is full dimensional in \(H_n\) for \(n\ge3\). No assumption about independent directional coordinates is made: the direction is uniform on the intrinsic sphere.

The Poisson processes have infinite mass toward marks \(-\infty\), but finite numbers of marks above each finite threshold. The extrema and the maximizing pair are well defined as proved below; no finite cutoff is part of the statement. The variable \(J\) refers to the vertex exposed in the positive direction only, not to the oppositely exposed vertex.

## Proof
**1. Finite-dimensional reduction.** Take independent standard normal variables \(G_1,\ldots,G_n\), their mean \(\bar G\), and \(R_n=\|G-\bar G\mathbf1\|_2\). Then \(U_n=(G-\bar G\mathbf1)/R_n\) is uniform on the intrinsic sphere, \(R_n\sim\chi_{n-1}\), and \(U_n\) and \(R_n\) are independent. Differences of coordinates are unaffected by subtraction of \(\bar G\). The two Gaussian support values are exactly
\[
F_n=\max_{1\le i<j\le n}(G_i-G_j),\qquad
B_n=\max_{1\le i<j\le n}(G_j-G_i).
\tag{6}
\]
The Gaussian width of \(P_n\) is \(F_n+B_n\), and that of \(S_n\) is \(2(M_n-m_n)\), where \(M_n=\max_iG_i\), \(m_n=\min_iG_i\). Thus
\[
R_n(w_n^{\mathrm{sym}}-w_n)=\Delta_n
:=2(M_n-m_n)-F_n-B_n\ge0.
\tag{7}
\]
If the positions of the global maximum and minimum satisfy \(i_{\max}<i_{\min}\), then \(F_n=M_n-m_n\), whereas \(B_n<M_n-m_n\) almost surely. For the reverse ordering, interchange \(F_n\) and \(B_n\). The two orders each have probability one half. This proves (3) and the finite strictness underlying (7).

**2. Two-sided extremal processes.** Consider the marked point measures
\[
\Pi_n^+=\sum_{i=1}^n\delta_{(i/n,(G_i-b_n)/a_n)},\qquad
\Pi_n^-=\sum_{i=1}^n\delta_{(i/n,(-G_i-b_n)/a_n)}.
\]
The Gaussian Mills ratio gives, for each fixed \(x\),
\[
n\Pr\{G_1>b_n+a_nx\}\longrightarrow e^{-x}.
\tag{8}
\]
On any finite collection of disjoint compact time--mark rectangles bounded below in mark, counts converge jointly to independent Poisson counts with mean obtained by integrating \(dt\,e^{-x}dx\). The positive and negative high-threshold events for a single coordinate are mutually exclusive for large \(n\). The usual multinomial rare-event argument therefore proves joint vague convergence \((\Pi_n^+,\Pi_n^-)\Rightarrow(\Pi^+,\Pi^-)\) to **independent** Poisson processes, including the upper tails controlled by (8).

The continuous-mapping step needs truncation: on an event of probability arbitrarily close to one, the maxima of the two mark processes are bounded above by a fixed \(T\), and there is an ordered high--low pair, in both time orientations, with sum at least \(-T\). A pair containing a mark below \(-2T-1\) cannot maximize, since its other mark is at most \(T\). Therefore all relevant maximizing pairs lie in a finite compact mark strip. In this strip their time and mark coordinates converge jointly; ties and diagonal-time coincidences have probability zero. Letting the strip expand yields
\[
\left(\frac{F_n-2b_n}{a_n},\frac{B_n-2b_n}{a_n},
\frac{M_n-b_n}{a_n},\frac{-m_n-b_n}{a_n},\frac{K_n-I_n}{n}\right)
\Rightarrow(D_\rightarrow,D_\leftarrow,H_+,H_-,J).
\tag{9}
\]
To justify the high-probability ordered pairs, use two disjoint time intervals of positive length, in each of which the two independent limiting processes have high marks above some sufficiently low fixed threshold with probability approaching one. The same construction applies with their time order reversed. This also proves that the suprema in the limiting definition are finite and attained. Their almost-sure uniqueness follows from finitely many candidate pairs above any fixed near-maximum level and the continuous joint mark distributions.

**3. Width loss and exposure.** Combining (7) and (9) gives \(\Delta_n/a_n\Rightarrow L\). Since \(R_n/\sqrt{n-1}\to1\) in probability, (1) follows by Slutsky's theorem. In the limit the maximum marks of \(\Pi^+\) and \(\Pi^-\) occur at distinct times almost surely. Exactly one of \(D_\rightarrow,D_\leftarrow\) equals \(H_++H_-\); the other is strictly smaller because the respective second-highest marks are separated from the highest marks. Hence \(L>0\) almost surely. The unique maximizing ordered pair has two distinct continuous time coordinates, so \(J\in(0,1)\) and \(\Pr(J=\varepsilon)=0\) for every fixed \(\varepsilon\). Portmanteau applied to (1) proves (2), including the limiting double order of the small-gap statement.

**4. Uniform integrability and the mean.** Split the coordinates into two consecutive halves \(A_n,B_n\), of sizes tending to infinity at half the total rate, and write \(Q(E)=\max_{i\in E}G_i-\min_{i\in E}G_i\). For the ordered split, the two cross-half candidates imply
\[
F_n\ge\max_{i\in A_n}G_i-\min_{j\in B_n}G_j,\qquad
B_n\ge\max_{j\in B_n}G_j-\min_{i\in A_n}G_i.
\]
Therefore
\[
0\le\Delta_n\le2Q(\{1,\ldots,n\})-Q(A_n)-Q(B_n).
\tag{10}
\]
The centered and \(a_n\)-scaled maxima and minima of samples of size \(n\), \(\lfloor n/2\rfloor\), or \(\lceil n/2\rceil\) have uniformly bounded absolute moments of any fixed positive order. This follows by integrating the Gaussian Mills-ratio upper and lower tail bounds for their distribution functions. Also \((b_n-b_{\lfloor n/2\rfloor})/a_n\to\log2\), and similarly for the other half. Expanding (10) around these \(b\)-centers thus yields uniformly bounded second moments of \(\Delta_n/a_n\). Consequently \(\mathbb E(\Delta_n/a_n)\to\mathbb EL\). Since \(R_n\) and the spherical deficit are independent, \(\mathbb E\Delta_n=\mathbb ER_n\,\mathbb E(w_n^{\mathrm{sym}}-w_n)\), while \(\mathbb ER_n/\sqrt{n-1}\to1\). This proves (5).

For the constant representation, condition on \(\Pi^-\). No high-process point may have mark \(x>z-M(t)\) if \(D_\rightarrow\le z\). By the Poisson void probability,
\[
\Pr(D_\rightarrow\le z\mid\Pi^-)=\exp\{-e^{-z}A\}.
\tag{11}
\]
Therefore \(D_\rightarrow\) has the same marginal law as \(\log A+G\), where \(G\) is an independent standard Gumbel variable. Since \(\mathbb EH_+=\mathbb EH_-=\gamma_{\mathrm E}\) and \(D_\leftarrow\) and \(D_\rightarrow\) have identical marginals,
\[
\mathbb EL=4\gamma_{\mathrm E}-2(\gamma_{\mathrm E}+\mathbb E\log A),
\]
which proves (4). Integrability holds because \(A\le e^{H_-}\), while \(A\ge\tfrac12 e^{H_{-,[1/2,1]}}\); both bounding maxima have shifted Gumbel laws with finite absolute moments. Finally, Gaussian extreme-value asymptotics and (6) show that both means have the displayed first-order asymptotic.

## Verification
The independent deterministic implementation in `verify.py` checks exact support identities by exhaustive root enumeration in several dimensions, the exact one-of-two global-extrema property, equivalence of the positive-root directional widths under Gaussian centering and intrinsic spherical normalization, and the point-process maximization algorithm against quadratic brute force for truncated Poisson samples. Its simulation diagnostics compare the nonnegative scaled loss and macroscopic gap for large Gaussian samples against independent truncated-Poisson samples. The Monte Carlo diagnostics are not used to infer any infinite-dimensional theorem. The reader can execute `python3 verify.py` using the Python standard library alone.

## Relationship to prior work
Numata, Takahashi, and Tamaki define directed-edge polytopes and describe their dimensions, facets and faces (arXiv:2203.14521; first public version 2022-03-28). Setiabrata studies the complete positive-root and origin-adjoined root-polytope face structures (arXiv:2001.05191). Gutekunst, Mészáros, and Petersen analyze triangulations and resonance arrangements for type-\(A\) positive-root configurations (arXiv:1903.06595). These papers supply the canonical objects but do not state the spherical width-loss law, Poisson joint law or macroscopic angular exposure conclusion.

A public same-object result on the transitive-tournament directed-edge polytope identifies the minimum enclosing sphere and proves that its only contacts are the simple roots. The present result is different: (2) shows that these very contacts carry asymptotically negligible total spherical normal-cone measure, while typical exposed root endpoints remain macroscopically separated. The known Gaussian extreme-value point-process theorem supplies a probabilistic ingredient, not the ordered-pair geometric functional, its joint angular gap and mean-deficit law. A complete bibliographic search cannot rule out an equivalent maximum-drawdown formulation; this remains the principal residual risk.

## Limitations
All metric statements depend on the standard coordinate realization and uniform intrinsic spherical measure. Formula (1) gives a Poisson-functional limit rather than an elementary closed-form density for \(L\) or \(J\). Formula (4) is an exact stochastic representation of the mean-deficit coefficient, not a claimed closed elementary value. Other tournament orientations need not have the same directional law.

## References
1. Y. Numata, Y. Takahashi, and D. Tamaki, *Faces of Directed Edge Polytopes*, arXiv:2203.14521, initial version 2022-03-28, MSC2020 52B05.
2. L. Setiabrata, *Faces of Root Polytopes*, arXiv:2001.05191, initial version 2020-01, *SIAM Journal on Discrete Mathematics* 35 (2021), 2093--2114.
3. S. C. Gutekunst, K. Mészáros, and T. K. Petersen, *Root Cones and the Resonance Arrangement*, arXiv:1903.06595, initial version 2019-03, *Electronic Journal of Combinatorics* 28 (2021), P1.12.
4. S. Resnick, *Extreme Values, Regular Variation, and Point Processes*, Springer, 1987; standard Poisson convergence and Gaussian extreme-value theory.
5. *Simple roots control the minimum sphere of transitive-tournament directed edge polytopes*, publicly accessible mathematical result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-simple-roots-control-the-minimum-sphere-of-transitive-tournament--c8c64739a8f1.

# Sharp Gabor tomography conditioning for two-line windows over odd finite fields

## Finding
Let \(q=p^r\) be any odd prime power, and fix any nontrivial additive character \(\psi\) of \(\mathbb F_q\). On \(G=\mathbb F_q^2\), consider the one-complex-parameter family of two-line windows
\[
g_c(x,y)=\mathbf1_{\{x=0\}}+c\mathbf1_{\{y=0\}},\qquad c\in\mathbb C\setminus\{0\}.
\]
For the complete Weyl-Heisenberg orbit of normalized rank-one projectors, define the tomography condition number as the ratio of the largest to smallest singular value of the complex-linear measurement map on all \(q^2\times q^2\) matrices, with infinity assigned if the map is singular. Then the sharp value over this family is
\[
\boxed{\min_{c\ne0}\kappa(c)=\frac{q-1}{\sin(\pi/(2p))},}
\]
attained **uniquely** by \(c=-1\). This optimizer is supported on exactly \(2(q-1)\) points, yet all its \(q^4\) rank-one Gabor projectors form a complex operator basis. With \(N=q^2\), the smallest operator-frame eigenvalue at the optimum is \(N\sin^2(\pi/(2p))/(q-1)^2\); its multiplicity is \(2q^2(q^2-1)/p\) if \(q>3\), and \(64\) if \(q=3\). The largest eigenvalue is \(N\) and has multiplicity one.

## Assumptions and scope
Use counting measure and the complex Hilbert space \(\mathcal H=\ell^2(G)\), of dimension \(N=q^2\). For \(s=(a,b)\) and \(\xi=(u,v)\) in \(G\), put \((T_sf)(z)=f(z-s)\), \((M_\xi f)(x,y)=\psi(ux+vy)f(x,y)\), and \(W_{s,\xi}=M_\xi T_s\). Define \(h_c=g_c/\sqrt{Q_c}\), where
\[
Q_c=\|g_c\|_2^2=q(1+|c|^2)+2\operatorname{Re}(c)>0.
\]
For each \((s,\xi)\in G^2\) let \(P_{s,\xi}=(W_{s,\xi}h_c)(W_{s,\xi}h_c)^*\). The analysis map is \(\mathcal A_c:X\mapsto(\operatorname{tr}(XP_{s,\xi}))_{s,\xi}\), with domain endowed with the Hilbert--Schmidt norm and codomain with its usual Euclidean norm. The condition number is that of this **complex-linear** map, with both singular-value extremes understood in these norms. It is not the condition number of an inverse restricted to pure states.

Define the unnormalized ambiguity coefficient
\[
A_c(a,b;u,v)=\sum_{x,y\in\mathbb F_q}g_c(x,y)\overline{g_c(x-a,y-b)}\,\psi(ux+vy).
\]
Its magnitude agrees with that of the usual ambiguity coefficient up to a harmless relabeling of the Weyl parameters. Set \(\mu_q(c)=\min_{a,b,u,v}|A_c(a,b;u,v)|/Q_c\), and \(s_p=\sin(\pi/(2p))\).

## Proof
**1. Exact four-term character sum.** Expanding the four products of coordinate-line indicators, the vertical-vertical intersection contributes \(q\mathbf1_{a=0,v=0}\), and the horizontal-horizontal one contributes \(q|c|^2\mathbf1_{b=0,u=0}\). The two cross-intersections are singletons \((0,b)\) and \((a,0)\); hence, with no generic-position assumptions,
\[
\boxed{A_c(a,b;u,v)=q\mathbf1_{a=0,v=0}+q|c|^2\mathbf1_{b=0,u=0}+\overline c\,\psi(vb)+c\,\psi(ua).}
\tag{1}
\]
The case \((a,b;u,v)=(0,0;0,0)\) gives the displayed \(Q_c\).

**2. Universal upper bound with uniqueness.** Take any \(a,b\ne0\). The two Kronecker-delta terms in (1) vanish, so \(|A_c|=|\overline c\,\psi(vb)+c\,\psi(ua)|\). A nontrivial additive character on \(\mathbb F_q\) has exactly the \(p\)-th roots of unity as its image, and \((u,v)\) ranges independently; therefore
\[
\min_{u,v}|A_c(a,b;u,v)|\le 2|c|s_p.
\]
Indeed among the \(p\) equally spaced relative phases there is one within angular distance \(\pi/p\) of the negative of the fixed phase, giving the chord bound. On the other hand,
\[
Q_c\ge q(1+|c|^2)-2|c|\ge2|c|(q-1),
\]
where the last inequality follows from \(1+|c|^2\ge2|c|\). Consequently
\[
\mu_q(c)\le\frac{s_p}{q-1}.
\tag{2}
\]
Equality in (2) forces equality in both inequalities for \(Q_c\). Their joint equality conditions are \(|c|=1\) and \(\operatorname{Re}(c)=-|c|\), namely \(c=-1\). Thus the asserted optimizer, if attaining (2), is unique.

**3. Exact minimum for the optimizer, including all boundaries.** At \(c=-1\) formula (1) reduces to
\[
A_{-1}=q\mathbf1_{a=0,v=0}+q\mathbf1_{b=0,u=0}-\psi(vb)-\psi(ua),\qquad Q_{-1}=2(q-1).
\]
When \(a,b\ne0\), minimizing \(|\psi(vb)+\psi(ua)|\) over the two character values gives exactly \(2s_p\), because \(p\) is odd. When exactly one of \(a,b\) is zero, a nonvanishing Kronecker-delta term either disappears, leaving \(|1+\psi(t)|\ge2s_p\), or contributes the real number \(q-2\). When \(a=b=0\), the value is among \(2(q-1)\), \(q-2\), and \(-2\). Since \(q\ge3\) and \(2s_p\le1\), all these cases have absolute value at least \(2s_p\), attained already in the first case. Hence
\[
\boxed{\mu_q(-1)=\frac{2s_p}{2(q-1)}=\frac{s_p}{q-1}>0.}
\tag{3}
\]
Combined with (2), this establishes both sharpness and uniqueness and shows that no optimal ambiguity coefficient vanishes.

**4. Operator-frame singular values.** Weyl matrices form an orthogonal basis of \(M_N(\mathbb C)\) for the Hilbert--Schmidt product, with squared norm \(N\). Each projector \(P_{s,\xi}\) is the Weyl conjugate of \(h_ch_c^*\); conjugation acts diagonally by characters on this operator basis. Finite-group Fourier orthogonality of the \(N^2\) conjugations therefore gives the complete frame-operator eigenvalue multiset
\[
\left\{N\left|\frac{A_c(a,b;u,v)}{Q_c}\right|^2:(a,b,u,v)\in\mathbb F_q^4\right\}.
\tag{4}
\]
For completeness: writing \(P_{0,0}=\frac1N\sum_{\gamma}b_\gamma W_\gamma\), conjugation multiplies each \(W_\gamma\) by a character; the \(N^2\) character vectors are orthogonal, and their squared coefficient norms, summed across \(N^2\) conjugations, give \(N|b_\gamma|^2\) after the Hilbert--Schmidt normalization. Here \(|b_\gamma|=|A_c(\gamma)|/Q_c\) up to Weyl relabeling, so (4) follows. This is also the finite-abelian version of the Gabor projector Gram spectrum in Goldberger--Kang--Okoudjou. By Cauchy--Schwarz, \(|A_c|\le Q_c\), with equality only when the corresponding Weyl operator fixes the rank-one ray. At the optimizer, equality away from the identity is impossible: for nonzero translation, its support has \(2(q-1)\) points, not divisible by the odd characteristic \(p\), whereas every orbit of a nonzero translation has size \(p\), ruling out a translational period; for zero translation and nonzero modulation, constancy of the modulation phase on each punctured coordinate axis would force the additive character trivial in both coordinates, a contradiction. Thus the unique largest frame eigenvalue is \(N\). The smallest equals \(N\mu_q(c)^2\), so its singular-value condition number equals \(1/\mu_q(c)\) whenever the operator frame is invertible. Equation (3) proves the theorem.

**5. Multiplicity of the lowest eigenvalue.** For \(q>3\), equality \(|A_{-1}|=2s_p\) occurs only where \(a,b\ne0\), or where exactly one translation coordinate vanishes and the corresponding diagonal term is absent. For each fixed nonzero argument of the relative additive character, the map from frequency coordinates onto the cyclic image of \(\psi\) has uniform fibers. There are exactly two nearest-to-opposite relative phases among its \(p\)-th roots. Hence the off-axis contribution is \(2(q-1)^2q^2/p\), and the two single-axis contributions together are \(4(q-1)q^2/p\). Their sum is
\[
\boxed{K(q)=\frac{2q^2(q^2-1)}p\quad(q>3).}
\]
For \(q=3\), the additional equality \(q-2=2s_p=1\) contributes \(2q(q-1)=12\) axial frequencies and \(2(q-1)=4\) identity-translation frequencies. Thus \(K(3)=2\cdot3^2(3^2-1)/3+16=64\). These counts describe the equality Weyl eigenspaces as the span of precisely their indexed Weyl matrices.

## Verification
The standalone Python 3 program `artifacts/verify.py` independently reconstructs all ambiguity coefficients from both the closed formula (1) and direct finite sums; its extension-field case implements \(\mathbb F_9\) as \(\mathbb F_3[t]/(t^2+1)\). For \(q\in\{3,5,7,9,11\}\), it checks five representative complex weights, the sharp optimum and its multiplicities, and nearest-root geometry. Its replay reports `VERIFY_OK exhaustive_formulas=121545 direct_reconstructions=3856 optimal_examples=5 extension_field=F9`. The rigorous statements for all odd prime powers come from the character-sum, finite character-group orthogonality, and inequality proofs; finite replay is not an infinite proof.

## Relationship to prior work
Bojarovska and Flinth (2015, Theorems 2.2--2.3 and the following examples) gave nonvanishing-ambiguity conditions for Gabor phase retrieval and discussed lower stability bounds and finite difference sets. Their conditions motivate the study of quantitative ambiguity minima, but do not optimize this cross-supported weighted family or give its unique extremizer, exact minimum-eigenvalue multiplicity, and prime-characteristic dependence. Goldberger, Kang, and Okoudjou (2021) established the operator-projector Gram eigenvalue mechanism for finite cyclic Gabor systems; their general spectral formula is an input to the derivation, not a novelty claim. A later published calculation of operator-span capacity for **two-point cyclic** windows addresses varying numbers of windows, not a single cross-supported window on the noncyclic group \(\mathbb F_q^2\); a finite-field **orthonormal Gabor basis** construction with a restricted time-frequency lattice similarly addresses a different invariant. This work's claim is the sharp weighted-cross minimax and its equality characterization, not the standard Weyl diagonalization itself.

## Limitations
The minimax is only over the specified one-parameter family of two coordinate-line indicators with both coefficients nonzero; it does not assert optimality among arbitrary windows, arbitrary support patterns, or time-frequency sublattices. The result uses operator-frame conditioning, which is stronger than mere pure-state phase retrieval and distinct from its nonlinear noise conditioning. Equivalence with a historically unindexed formulation remains possible; an inaccessible recent full text on cyclic algebraic Gabor windows is an identified but apparently nondecisive priority risk. Independent mathematical audit has not been performed.

## References
1. I. Bojarovska and A. Flinth, *Phase Retrieval from Gabor Measurements*, arXiv:1503.05800v1 (first public posting 2015-03-19), Theorems 2.2--2.3 and related examples; primary MSC 42C15.
2. A. Goldberger, S. Kang and K. A. Okoudjou, *Towards a classification of incomplete Gabor POVMs in \(\mathbb C^d\)*, arXiv:2106.01509v1 (first public posting 2021-06-02), projector Gram spectrum; primary MSC 42C15.
3. D. Han, Q. Hu, R. Liu and H. Wang, *Quantum injectivity of multi-window Gabor frames in finite dimensions*, *Annals of Functional Analysis* 13 (2022), article 59, DOI 10.1007/s43034-022-00208-2; criterion for simultaneous ambiguity zeros of multiple windows, distinct from the present single-window minimax.

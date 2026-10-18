# Six-valued cubic Fourier energy for four-mode periodic Airy spectra

## Finding
Let \(S\subset\mathbb Z\) contain exactly four distinct integers. On the normalized two-dimensional torus, define the unit-coefficient Airy Fourier sum
\[
U_S(x,t)=\sum_{n\in S}e^{i(nx+n^3t)},\qquad
J_3(S)=\frac1{(2\pi)^2}\int_0^{2\pi}\!\int_0^{2\pi}|U_S(x,t)|^6\,dx\,dt.
\]
Then the ordered three-fold additive energy \(J_3(S)\) assumes **exactly six possible values**:
\[
\boxed{J_3(S)\in\{256,262,268,274,340,400\}.}
\]
The following table gives mutually exclusive and exhaustive arithmetic conditions. Different letters in one condition represent distinct elements of \(S\); the fourth element is unrestricted in the two three-point conditions.

| Value | Exact condition on the four-element set \(S\) |
| ---: | --- |
| \(400\) | \(S=\{-u,u,-v,v\}\), where \(uv\ne0\) and \(u\ne\pm v\). |
| \(340\) | \(\{-u,0,u\}\subset S\) for some \(u\ne0\). |
| \(274\) | \(S=\{a,b,c,d\}\), pairwise distinct, with \(2a+b=2c+d\) and \(2a^3+b^3=2c^3+d^3\). |
| \(268\) | \(S=\{a,b,c,d\}\), pairwise distinct, with \(a+b+c=3d\) and \(a^3+b^3+c^3=3d^3\). |
| \(262\) | \(\{-5u,u,4u\}\subset S\) for some \(u\ne0\). |
| \(256\) | None of the preceding conditions holds. |

Each possibility occurs. Witnesses in increasing order of energy are
\[
\begin{array}{c|c}
J_3(S)&S\\\hline
256&\{0,1,2,3\}\\
262&\{-5,1,4,6\}\\
268&\{-18,3,10,17\}\\
274&\{1,4,9,11\}\\
340&\{-1,0,1,2\}\\
400&\{-2,-1,1,2\}
\end{array}
\]
In particular, for every four distinct **strictly positive** frequencies,
\[
\boxed{J_3(S)\in\{256,274\},\qquad J_3(S)\le274,}
\]
and both values occur for strictly positive supports.

## Assumptions and scope
The variables \(x,t\) range independently over \(\mathbb R/2\pi\mathbb Z\); the normalization is probability Haar measure on their product. All four Fourier coefficients are exactly \(1\), not arbitrary amplitudes or phases. Frequencies are integers without any positivity assumption except in the last corollary. Equalities concern integer sums, not modular congruences. "Ordered energy" counts ordered sextuples, including permutations of the same three-element multisets.

## Proof
**Orthogonality and baseline.** Write \(\gamma(n)=(n,n^3)\in\mathbb Z^2\). Expanding the sixth power and integrating characters gives
\[
J_3(S)=\#\{(n_1,n_2,n_3,m_1,m_2,m_3)\in S^6:
\sum n_j=\sum m_j,\quad \sum n_j^3=\sum m_j^3\}.
\]
If distinct size-three multisets had distinct \(\gamma\)-sums, only permutations of the same multiset would survive. There are four constant triples with ordering multiplicity \(1\), twelve triples with pattern \(a,a,b\) and multiplicity \(3\), and four triples with three distinct elements and multiplicity \(6\). Their total contribution is
\[
4\cdot1^2+12\cdot3^2+4\cdot6^2=256.
\]

**One primitive collision direction.** Order the four frequencies as \(s_1<s_2<s_3<s_4\). The three vectors \((1,1,1,1)\), \((s_j)_{j=1}^4\), and \((s_j^3)_{j=1}^4\) have rank three: a polynomial of the form \(A+Bx+Cx^3\) cannot vanish at four distinct real arguments unless it is identically zero. Hence their integer kernel is one-dimensional. Let \(k\) be its primitive integer generator with relatively prime coordinates. A collision of two distinct size-three multisets has signed multiplicity vector \(qk\), and both its positive and negative masses are at most three. A primitive kernel vector has positive mass at least two, because mass one would force two distinct frequencies to coincide by the linear moment condition. Thus \(|q|=1\): all nontrivial collisions on one support are built from the same primitive signed relation.

**The five possible primitive types.** Cancel common atoms between two colliding triples. Positive and negative masses are equal and belong to \(\{2,3\}\). Their distinct frequency supports fit into four sites, so (up to swapping sides) the *only* multiplicity partitions are
\[
\begin{array}{c|c}
\text{positive side}&\text{negative side}\\\hline
(1,1)&(2)\\
(1,1)&(1,1)\\
(2,1)&(3)\\
(2,1)&(2,1)\\
(1,1,1)&(3).
\end{array}
\]
For the first type, \(a+c=2b\) and \(a^3+c^3=2b^3\) imply \(b=0\) and \(a=-c\), giving the symmetric three-point condition. For the second, equal pair sums \(s\) and equal cube sums imply \(s(ab-cd)=0\) from \(a^3+b^3=s^3-3abs\). Since distinct unordered pairs with the same sum cannot have the same product, \(s=0\), giving two opposite pairs. For the third, writing \(a=w+h\), \(b=w-2h\) in \(2a+b=3w\) gives
\[
2a^3+b^3-3w^3=6h^2(3w-h),
\]
and nontriviality forces \(h=3w\), yielding the three-point ratio \(\{-5w,w,4w\}\). The remaining two types are exactly the displayed four-point equations in the table; no parametrization is assumed.

**Exact multiplicity surplus.** Whenever two distinct size-three multisets collide, their respective ordering multiplicities \(r\) and \(s\) contribute an *extra* \(2rs\) beyond the baseline. The primitive rank-one argument rules out coexistence of different collision types. In the \((2,1)\) versus \((3)\) case the multiplicities are \(3\) and \(1\), giving \(6\). For \((1,1,1)\) versus \((3)\), they are \(6\) and \(1\), giving \(12\). For \((2,1)\) versus \((2,1)\), they are \(3\) and \(3\), giving \(18\). In the symmetric three-point case, the colliding multisets have the form \(\{-u,u,t\}\) and \(\{0,0,t\}\) as \(t\) ranges through the four points. The four products of ordering multiplicities are \(6,9,9,18\), giving surplus \(2(6+9+9+18)=84\). Finally, for the two-opposite-pairs case, the multisets \(\{-u,u,t\}\) and \(\{-v,v,t\}\), with \(t\in S\), yield four products equal to \(18\), giving surplus \(144\). This produces exactly the six stated energy values, proves their mutual exclusivity, and rules out additional levels.

**Attainability and positive-frequency dichotomy.** For each displayed witness, direct substitution verifies its indicated signed relation; the no-relation witness is ruled out by the five cases (and also checked independently). Strict positivity excludes both symmetric types, the \(\{-5u,u,4u\}\) type, and the three-distinct-versus-three-equal type: the latter contradicts strict convexity of \(x\mapsto x^3\) for positive inputs with equal arithmetic means. Thus only the generic value and the balanced four-site value remain. They occur at \(\{1,2,3,4\}\) and \(\{1,4,9,11\}\), respectively.

## Verification
Run `python3 verify_energy.py` with Python's standard library. The checker enumerates every four-element support in the integer interval from \(-15\) through \(15\), partitions the twenty unordered length-three multisets by their exact integer linear and cubic sums, and checks the predicted collision multiplicity type and resulting energy. It independently checks one witness for every level, including the rarer \(268\) case outside the finite enumeration range. It also checks the positive-support corollary inside its finite domain. Expected result begins with `VERIFY_OK six attainable levels`. The universal result follows from the proof above, not the finite checker.

## Relationship to prior work
Arthur, Greco, and Tsugawa (2026) analyze bilinear cubic-dispersion resonance factors in well-posedness of a coupled modulated KdV system; their formulas concern two-wave interactions and do not classify the six-fold moment of four integer Airy modes. Sutherland and Yim (2026) study continuum six-wave Hamiltonian scattering on deformed quadratic-dispersion resonance patches, including cubic corrections; their interacting coefficients and continuous resonance geometry are distinct from this discrete, unit-coefficient moment census. General single-balanced-defect trigonometric-moment formulas already account for the \(18\)-unit surplus when the collision type is \((2,1)\) against \((2,1)\); that individual surplus is used here, not presented as separately new. The contribution is the complete rank-one classification for the **integer cubic graph**, including four other distinct collision mechanisms, all attainable energy levels, and the positive-spectrum dichotomy.

## Limitations
The result is for precisely four frequencies, cubically dispersed periodic sums and equal unit coefficients. It does **not** determine sharp \(\ell^2\)-to-\(L^6\) restriction constants for arbitrary complex amplitudes or higher-cardinality supports; nor does it assert anything for incommensurate frequencies or other dispersion relations. The finite verifier is supplementary. Although relevant recent full manuscripts and closely related finite trigonometric-moment results were compared, an unindexed equivalent classification in older six-wave or thin-set literature remains a historical-priority risk. No independent scientific audit has been performed.

## References
- T. Arthur, D. Greco, K. Tsugawa, "Diophantine conditions in well-posedness theory for a coupled modulated Korteweg-de Vries system," arXiv:2607.12553, first public 2026-07-14, https://arxiv.org/abs/2607.12553.
- A. J. Sutherland, S. C. Yim, "Six-wave scattering in Hamiltonian Dysthe equations: Euler matching and integrability obstructions," arXiv:2609.23175, first public 2026-09-19, https://arxiv.org/abs/2609.23175.
- J. Maynard, "Sums of three positive cubes," *Journal of the London Mathematical Society* 113 (2026), article e70554, DOI 10.1112/jlms.70554. This survey supplies background on third-power Fourier moments, not the four-mode classification.

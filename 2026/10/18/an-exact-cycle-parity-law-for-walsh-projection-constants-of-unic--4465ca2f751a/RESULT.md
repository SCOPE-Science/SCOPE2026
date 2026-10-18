# An exact cycle-parity law for Walsh projection constants of unicyclic graphs

## Finding
Let \(G=(V,E)\) be a finite simple undirected graph with precisely one independent cycle, allowing attached trees, disjoint forest components, and isolated vertices. Write \(m=|E|\) and let \(k\) denote the number of edges in its unique cycle. Define the real Banach space
\[
X_G=\operatorname{span}_{\mathbb R}\{\chi_e:e=\{u,v\}\in E\}\subset C(\{-1,1\}^{V};\mathbb R),\qquad \chi_{\{u,v\}}(x)=x_ux_v,
\]
with the supremum norm. Its **absolute projection constant** is the infimum of the norms of projections onto an isometric copy of \(X_G\), with the supremum taken over all isometric embeddings into real Banach spaces.

Put
\[
 A_m=\frac{m}{2^{m-1}}\binom{m-1}{\lfloor(m-1)/2\rfloor},\qquad
 B_m=\frac{1}{2^{m-2}}\binom{m-2}{\lfloor(m-2)/2\rfloor}.
\]
Then the exact constant for every \(3\le k\le m\) is
\[
 \boxed{\lambda(X_G)=
 \begin{cases}
 A_m,&k\text{ odd},\\[3pt]
 A_m+(-1)^{s-1}B_m\displaystyle\frac{\binom{\lfloor(m-2)/2\rfloor}{s-1}}{\binom{m-2}{2s-2}},&k=2s\text{ even}.
 \end{cases}}
\tag{1}
\]
All terms in the even-cycle correction are strictly positive apart from its explicit sign, so its sign alternates according to \(k\pmod4\), and the odd-cycle correction is exactly zero. The value is invariant under any change to tree attachments or acyclic components that preserves \(m\) and \(k\). For fixed even \(k=2s\) and \(m\to\infty\),
\[
 \lambda(X_G)-A_m\sim (-1)^{s-1}(2s-3)!!\sqrt{\frac2\pi}\,m^{-s+1/2}.
\tag{2}
\]
For example, at \(m=6\) the unique cycle lengths \(4,5,6\) give respectively \(7/4,15/8,9/4\).

## Assumptions and scope
The underlying scalars and continuous functions are real, the vertex sign cube carries its usual discrete topology and the uniform probability measure when expectations occur, and graph edges are simple with no loops or repeated pairs. “Exactly one independent cycle” means the cycle-space dimension \(|E|-|V|+c(G)\) is one, where \(c(G)\) is the number of graph components. The unique simple cycle must consequently have \(k\ge3\) edges and \(m\ge k\). All supremum norms are unnormalized. Binomial coefficients in (1) have nonnegative integral lower arguments because \(2s\le m\). The odd double factorial in (2) has its standard meaning.

## Proof
**1. Optimality of the Fourier projection, including absolute optimality.** Write \(\Omega=\{-1,1\}^V\), viewed as a finite abelian group under coordinatewise multiplication. The natural Fourier/Walsh projection from \(C(\Omega;\mathbb R)\) onto \(X_G\) is
\[
 P_G f=\sum_{e\in E}\widehat f(e)\chi_e,
 \qquad \widehat f(e)=\mathbb E_{\Omega}[f(x)\chi_e(x)].
\]
If \(Q\) is any projection onto \(X_G\), average its conjugates by the \(\Omega\) translation action: \(\overline Q=|\Omega|^{-1}\sum_{g\in\Omega}\tau_gQ\tau_g^{-1}\). Each translation preserves \(X_G\); therefore \(\overline Q\) remains a projection onto \(X_G\), with \(\|\overline Q\|\le\|Q\|\). Its commutation with all translations forces it to be diagonal on the distinct one-dimensional Walsh character spaces. Because its range is \(X_G\) and it fixes \(X_G\), it acts as identity on precisely the edge characters and zero on every other Walsh character. Consequently \(\overline Q=P_G\), proving minimum norm in this ambient space.

For an arbitrary isometric copy \(J:X_G\hookrightarrow Y\), each point-evaluation of \(J^{-1}\) on \(J(X_G)\) has norm at most one; extend these finitely many functionals to all of \(Y\) by real Hahn–Banach. Their joint map \(S:Y\to C(\Omega;\mathbb R)\) has norm at most one and satisfies \(SJx=x\) for \(x\in X_G\). Then \(JP_GS\) is a projection of norm at most \(\|P_G\|\), while taking \(Y=C(\Omega)\) yields the opposite universal bound. Hence the absolute projection constant equals \(\|P_G\|\). Since \(P_G\) is convolution by \(\sum_{e\in E}\chi_e\), its norm is exactly
\[
 \lambda(X_G)=\mathbb E_{x\in\Omega}\left|\sum_{e\in E}\chi_e(x)\right|.
\tag{3}
\]
The upper bound is the triangle inequality; equality follows by using the sign of the kernel at the identity (translated appropriately).

**2. The single circuit is the only constraint.** Choose a spanning forest of \(G\) that contains every edge except one edge from the unique cycle. Assign independent uniform vertex signs. The edge-sign map \(x\mapsto(\chi_e(x))_{e\in E}\) is a homomorphism onto exactly those \(\eta\in\{-1,1\}^E\) satisfying
\[\prod_{e\in C}\eta_e=1,\tag{4}\]
where \(C\) is the unique cycle. Indeed the product around a cycle telescopes, while arbitrary signs on spanning-forest edges determine vertex signs up to one independent global sign per graph component. The missing cycle edge is then fixed by (4). Fibres of the homomorphism are equal in size, giving the uniform distribution on the indicated parity-constrained sign vectors. Tree edges and edges in separate forest components impose no further constraint.

**3. Independent baseline and parity correction.** Let \(\varepsilon_1,\ldots,\varepsilon_m\) be independent fair signs, label the \(k\) cycle edges first, and write \(S_m=\sum_{i=1}^m\varepsilon_i\). The conditional law in (4) has density \(1+\prod_{i=1}^k\varepsilon_i\) relative to the full independent-sign law. Therefore
\[
\lambda(X_G)=\mathbb E|S_m|+\Delta_{m,k},\qquad
\Delta_{m,k}=\mathbb E\left(|S_m|\prod_{i=1}^k\varepsilon_i\right).
\tag{5}
\]
By writing \(S_m=m-2j\) and telescoping using \((m-2j)\binom mj=m(\binom{m-1}{j}-\binom{m-1}{j-1})\), one obtains
\[\mathbb E|S_m|=2^{-m}\sum_{j=0}^m\binom mj|m-2j|=A_m.\]
If \(k\) is odd, simultaneously flipping all \(m\) independent signs preserves \(|S_m|\) but reverses \(\prod_{i=1}^k\varepsilon_i\), hence \(\Delta_{m,k}=0\).

**4. Closed evaluation of the even-cycle correction.** Write \(k=2s\) and \(R=\sum_{i=3}^m\varepsilon_i\). Direct averaging over the first two independent signs gives
\[
\mathbb E_{\varepsilon_1,\varepsilon_2}\bigl[|R+\varepsilon_1+\varepsilon_2|\varepsilon_1\varepsilon_2\bigr]
=\frac{|R+2|+|R-2|-2|R|}{4}
=\begin{cases}1,&R=0,\\1/2,&|R|=1,\\0,&\text{otherwise}.
\end{cases}
\tag{6}
\]
The sum \(R\) has the parity of \(n=m-2\). The probability weight in (6) is
\[
\begin{cases}\Pr(R=0),&n\text{ even},\\ \tfrac12\Pr(|R|=1),&n\text{ odd},\end{cases}
=2^{-n}\binom n{\lfloor n/2\rfloor}=B_m.
\tag{7}
\]
On the event \(R=0\) (even \(n\)), exactly \(n/2\) of its signs are positive and \(n/2\) are negative; on \(|R|=1\) (odd \(n\)), their two counts differ by one. In either case, conditional exchangeability and the generating polynomial for elementary symmetric sums yield
\[
\mathbb E\left[\prod_{i=3}^{2s}\varepsilon_i\ \middle|\ R=0\text{ or }|R|=1\right]
=(-1)^{s-1}\frac{\binom{\lfloor n/2\rfloor}{s-1}}{\binom n{2s-2}}.
\tag{8}
\]
For completeness, when \(n=2h\), the product generating polynomial equals \((1+t)^h(1-t)^h=(1-t^2)^h\), so its coefficient of \(t^{2s-2}\) is \((-1)^{s-1}\binom h{s-1}\). When \(n=2h+1\), it equals \((1\pm t)(1-t^2)^h\), and the same even coefficient results. Dividing by \(\binom n{2s-2}\) converts the elementary-symmetric coefficient into the mean product for a specified \((2s-2)\)-subset. Combining (5)–(8) proves (1), including exact sign and nonvanishing.

**5. Asymptotic correction.** For fixed \(s\ge2\) as \(m\to\infty\), Stirling's formula yields \(B_m\sim\sqrt{2/(\pi m)}\). Elementary fixed-degree binomial asymptotics give
\[
\frac{\binom{\lfloor(m-2)/2\rfloor}{s-1}}{\binom{m-2}{2s-2}}
\sim\frac{(2s-2)!}{2^{s-1}(s-1)!}\,m^{-(s-1)}
=(2s-3)!!\,m^{-(s-1)}.
\]
Multiplication proves (2).

## Verification
A standalone `verify.py` file is included. Running `python3 verify.py` from the directory containing the file returns the lines `UNICYCLE_WALSH_PROJECTION_EXACT_OK 292` and `SIX_EDGE_CYCLE_LENGTHS ['7/4', '15/8', '9/4']`. Its exact rational arithmetic independently enumerates the parity-constrained sign law for all \(3\le m\le13\) and \(3\le k\le m\); it also checks graph vertex-sign realizations with representative forest attachments and disconnected components and confirms the predicted parity-sign changes. These finite tests are corroboration; the proof for every graph and cycle length is the analytic argument above.

## Relationship to prior work
Defant, Galicer, Mansilla, Mastyło, and Muro prove the general formula (3) for arbitrary Walsh spectra, and its absolute-projection interpretation. That theorem is the starting point; **the general Walsh-kernel identity itself is not new**. Their theorem does not evaluate the edge spectra of all unicyclic graphs or identify the parity-dependent exact correction (1), its sign law, or the sharp decay order (2). Their earlier broad polynomial-space treatment gives the same general projection framework, rather than this explicit graph classification.

The graph-quadratic-chaos literature studies signed-edge sums via distribution and moments, often fourth moments or central-limit regimes. Published graph-supported Walsh fourth-moment inequalities and next-to-independent-sign endpoint \(L^n\) inequalities do not furnish the normalized absolute **first moment** required here. An unrestricted second Walsh-layer projection has a different spectrum and its general layer formula does not imply the unicyclic correction without isolating and evaluating the one-circuit constraint.

## Limitations
The theorem treats finite real spaces with exactly one independent cycle and unweighted Walsh **basis-character** coefficients in the canonical projection kernel. It does not provide the exact constant for graphs with multiple independent cycles, weighted Walsh sums, complex projections, or arbitrary graph-supported \(L^p\) moment extremizers. The quoted asymptotic holds with the even cycle length fixed. Related exact parity-slice formulas might exist under alternative combinatorial, Ising, or Krawtchouk terminology; bibliographic screening cannot exclude an unindexed equivalent. No independent scientific audit has been performed.

## References
1. A. Defant, D. Galicer, M. Mansilla, M. Mastyło, S. Muro, *Asymptotic insights for projection, Gordon–Lewis and Sidon constants in Boolean cube function spaces*, arXiv:2302.00233v1 (first public version 1 February 2023), https://arxiv.org/abs/2302.00233, especially the Walsh-projection constant theorem.
2. A. Defant, D. Galicer, M. Mansilla, M. Mastyło, S. Muro, *Projection constants for spaces of multivariate polynomials*, arXiv:2208.06467v1 (first public version 12 August 2022), https://arxiv.org/abs/2208.06467, Section 8.1.
3. B. B. Bhattacharya, S. Das, S. Mukherjee, S. Mukherjee, *Fluctuations of Quadratic Chaos*, arXiv:2203.02850v1 (6 March 2022), https://arxiv.org/abs/2203.02850.

# Random generation of radical-square-zero quiver algebras: exact probabilities and a density-corrected birthday law

## Finding

Let \(Q\) be a finite quiver with a nonempty vertex set \(V\), allowing oriented cycles, loops, and parallel arrows. Put \(v=|V|\), write \(a_{uw}\) for the number of arrows from \(u\) to \(w\), and let \(m=\sum_{u,w}a_{uw}\). Let \(q\) be any prime power. Choose \(k\ge1\) elements independently and uniformly from the finite-dimensional unital algebra
\[
A_Q=\mathbb F_q Q/\langle\text{all paths of length two}\rangle.
\]
The exact probability \(P_{Q,q}(k)\) that these elements generate \(A_Q\) as a unital \(\mathbb F_q\)-algebra is
\[
\boxed{P_{Q,q}(k)=
\prod_{i=0}^{v-1}(1-iq^{-k})\,
\prod_{u\ne w}\prod_{j=0}^{a_{uw}-1}(1-q^{j+1-k})\,
\prod_{u}\prod_{j=0}^{a_{uu}-1}(1-q^{j-k}).}
\tag{1}
\]
Empty products equal one. The exact number of generating ordered tuples is \(q^{k(v+m)}P_{Q,q}(k)\). Formula (1) is valid even when its probability is zero.

The minimum number \(d(A_Q)\) of nonunit algebra generators, with the identity automatically included, is
\[
\boxed{d(A_Q)=\max\left\{
\lceil\log_q v\rceil,\quad
\max_{u\in V}a_{uu},\quad
\max_{u\ne w\, :\,a_{uw}>0}(a_{uw}+1)
\right\}.}
\tag{2}
\]
The maximum over an empty set is defined to be zero. In particular, the single-vertex, no-arrow algebra is \(\mathbb F_q\) and has no required generators. The probability depends on the quiver only through its vertex count and the loop and off-diagonal arrow multiplicities, not through which ordered vertex pairs carry those multiplicities. For a loopless quiver with no parallel arrows, formula (1) becomes
\[
\boxed{P_{Q,q}(k)=\prod_{i=0}^{v-1}(1-iq^{-k})\,(1-q^{1-k})^m.}
\tag{3}
\]
Thus every orientation and placement of a fixed number of distinct directed arrows has the same random-generation probability.

For a sequence of loopless quivers \(Q_v\) on \(v\) vertices, with at most one arrow per ordered pair, suppose \(m_v/v^2\to\rho\in[0,1]\) and fix \(q\). For any integer sequence \(k_v\ge1\) such that \(q^{k_v}/v^2\to c\in(0,\infty)\), the sharp birthday-window limit is
\[
\boxed{P_{Q_v,q}(k_v)\longrightarrow\exp\left(-\frac{1/2+q\rho}{c}\right).}
\tag{4}
\]
If instead \(q^{k_v}/v^2\to0\), the probability tends to zero; if \(q^{k_v}/v^2\to\infty\), it tends to one. The density-dependent term is a genuinely additional obstruction beyond distinct vertex labels.

## Assumptions and scope

The quiver is finite, its vertex set is nonempty, and the coefficient field is any finite field \(\mathbb F_q\). All paths of length two or more are set to zero. The radical \(J\) is the span of the arrows and satisfies \(J^2=0\); the diagonal algebra is \(D=\bigoplus_{u\in V}\mathbb F_q e_u\), so \(A_Q=D\oplus J\) as vector spaces. Write \(J_{uw}=e_uJe_w\), a vector space of dimension \(a_{uw}\). Loops lie in \(J_{uu}\) and are retained. No acyclicity, connectedness, characteristic, or multiplicity assumption is imposed except in the separate asymptotic statement, where loops and parallel arrows are excluded. Generation is always unital and over the specified coefficient field.

## Proof

**Diagonal separation.** Write the chosen elements as \(x_i=d_i+b_i\), where \(d_i\in D\) and \(b_i\in J\). Define a label at each vertex by \(c(u)=(d_1(u),\ldots,d_k(u))\in\mathbb F_q^k\). The images \(d_i\) generate \(D\cong\mathbb F_q^v\) if and only if the labels \(c(u)\) are pairwise distinct. Necessity follows because equal labels cannot be separated by any polynomial in the generators. For sufficiency, distinct points in \(\mathbb F_q^k\) can be separated by coordinate polynomials, yielding every primitive diagonal idempotent. Thus a generating tuple must have distinct labels; their number is \(\prod_{i=0}^{v-1}(q^k-i)\).

**The radical criterion.** Assume the labels distinct. For each ordered pair \((u,w)\), define the linear map \(T_{uw}:\mathbb F_q^k\to J_{uw}\) by \(T_{uw}(\lambda)=\sum_i\lambda_i(b_i)_{uw}\), and write \(\delta_{uw}=c(u)-c(w)\). Put
\[
H_{uw}=\{\lambda\in\mathbb F_q^k:\lambda\cdot\delta_{uw}=0\}.
\]
If \(u\ne w\), then \(\delta_{uw}\ne0\) and \(\dim H_{uw}=k-1\). For a loop, \(\delta_{uu}=0\), so \(H_{uu}=\mathbb F_q^k\). The tuple generates \(A_Q\) precisely when
\[
T_{uw}(H_{uw})=J_{uw}\quad\text{for every ordered pair }(u,w).
\tag{5}
\]

To prove necessity, let \(B\) be the generated subalgebra and suppose that its image in \(A_Q/J\) is all of \(D\), which holds by label separation. Let \(I=B\cap J\). Since \(I^2=0\), the diagonal primitive idempotents lift to a complete family \(f_u\in B\) of pairwise orthogonal idempotents summing to the identity and reducing to \(e_u\). An explicit conjugator aligning them is \(g=\sum_u f_u e_u\in1+J\), because \(f_u g=g e_u\). Therefore \(g^{-1}Bg=D\oplus I'\), where \(I'\) is a \(D\)-bimodule and splits independently as \(\bigoplus_{u,w}I'_{uw}\). Writing \(g=1+z\) and using \(J^2=0\), the \((u,w)\) component of \(g^{-1}x_i g\) is \((b_i)_{uw}+(c_i(u)-c_i(w))z_{uw}\). Its linear combinations with coefficients in \(H_{uw}\) therefore have components exactly \(T_{uw}(H_{uw})\), which must lie in \(I'_{uw}\). If \(B=A_Q\), condition (5) follows.

Conversely, suppose condition (5) fails at some \((u,w)\). Choose a proper hyperplane \(M\subsetneq J_{uw}\) containing \(T_{uw}(H_{uw})\), and let \(I'\subsetneq J\) be the \(D\)-bimodule equal to \(M\) at this corner and to the entire corner elsewhere. In the one-dimensional quotient \(J_{uw}/M\), the map induced by \(T_{uw}\) annihilates \(H_{uw}=\ker(\lambda\mapsto\lambda\cdot\delta_{uw})\). Hence the induced map is a scalar multiple of this functional. If \(\delta_{uw}=0\), it is already zero; otherwise choose \(z_{uw}\in J_{uw}\) to cancel that scalar. With all other components of \(z\) zero, each conjugate \((1-z)x_i(1+z)\) belongs to the proper subalgebra \(D\oplus I'\). Thus the original tuple does not generate \(A_Q\). This establishes (5), including the loop case.

**Independent uniform ranks.** Conditional on the diagonal labels, every family \(((b_i)_{uw})_{i=1}^k\) is independent and uniform in \(J_{uw}^k\) across ordered pairs. Restriction to the fixed subspace \(H_{uw}\) is a uniform linear map. A uniform map from an \(s\)-dimensional vector space onto an \(a\)-dimensional vector space is surjective with probability \(\prod_{j=0}^{a-1}(1-q^{j-s})\) (zero when \(s<a\)). Taking \(s=k-1\) off the diagonal and \(s=k\) on it, multiplying these independent probabilities, and multiplying by the diagonal-separation probability proves (1).

**Minimal generators.** The diagonal-separation condition is possible exactly when \(q^k\ge v\). The restricted maps in (5) can be surjective exactly when \(k\ge a_{uu}\) for all loops and \(k-1\ge a_{uw}\) for all off-diagonal corners. Conversely, when these inequalities hold, each factor in (1) is strictly positive; therefore a generating tuple exists. This proves (2), including the zero-generator field boundary.

**Density-corrected birthday threshold.** For loopless simple directed quivers, take logarithms of (3) with \(N=q^{k_v}\). If \(N/v^2\to c\in(0,\infty)\), then
\[
\sum_{i=0}^{v-1}\log(1-i/N)
=-\frac{v(v-1)}{2N}+O(v^3/N^2)\longrightarrow-\frac1{2c},
\]
and
\[
m_v\log(1-q/N)=-\frac{qm_v}{N}+O(m_v/N^2)
\longrightarrow-\frac{q\rho}{c}.
\]
This gives (4). The upper bound \(\prod_i(1-i/N)\le\exp[-v(v-1)/(2N)]\), interpreted as zero when \(N<v\), proves the lower-window failure. For \(N/v^2\to\infty\), both logarithmic error terms and main terms vanish because \(m_v=O(v^2)\), proving convergence to one.

## Verification

The companion standalone script `verify.py` independently enumerates all algebra elements, forms every tested ordered tuple, builds the generated unital subalgebra by repeated left and right multiplication and exact finite-field Gaussian elimination, and compares its dimension to \(\dim A_Q\). It separately computes the count predicted by formula (1). It covers 19 fully exhaustive configurations over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_4\), including loops, parallel arrows, oriented two-cycles, a three-vertex path, and impossible cases. It returns `VERIFY_OK 19 exhaustive finite-field cases`. These finite tests corroborate the universally quantified proof but do not themselves establish it.

For example, for two vertices with one arrow, \(q=2\), and \(k=2\), exactly \(24\) of the \(64\) ordered pairs generate, giving probability \(3/8\). For the three-vertex two-arrow path with the same field and generator count, exactly \(96\) of the \(1024\) ordered pairs generate, giving probability \(3/32\). For a sequence with \(q=2\), \(v=2^r\), \(k=2r\), and approximately half of all possible distinct directed edges, the exact values approach \(\exp(-3/2)\).

To reproduce, run `python3 verify.py` with a standard Python installation; no packages or external data are required.

## Relationship to prior work

Sercombe and Shalev [1] study random generation of finite associative algebras and prove general probabilistic bounds and bounds on the number of generators. Their 2020 preprint is the motivating source. Their general high-dimensional hypotheses do not supply the present exact product for many one-dimensional semisimple factors, nor the fixed-field density-dependent birthday window. Iovanov and Sistko [2] classify maximal subalgebras of quiver algebras; their Proposition 4.2 provides relevant structural machinery, but not the all-\(k\) generation count, minimal-generator identity, or limiting density law. The present proof gives a specialized direct criterion and counts all tuple fibers. Kravchenko, Mazur, and Petrenko [3] develop generation probabilities for other algebras and, in their introduction, explicitly distinguish the unresolved nontrivial-radical calculation from their semisimple formulas. Mazorchuk and Zhang [4] supply context for radical-square-zero quiver algebras, not a generator census.

The orientation-insensitive generating probability should not be confused with centralizer or ideal enumerators for the same underlying algebras, which answer different counting questions. The classical distinct-label birthday probability is the first factor in (1); the other factors and the density correction quantify genuinely additional arrow-generation constraints.

## Limitations

The formula concerns unital associative generation of the truncated algebra with \(J^2=0\), not the full path algebra, representation generation, idempotent-only sampling, or nonunital generators. The asymptotic is restricted to loopless, at-most-one-arrow-per-ordered-pair sequences, with \(q\) fixed; it does not assert a universal critical constant for arbitrary multiquivers. At fixed \(q\), integer generator counts can make the ratio \(q^{k_v}/v^2\) oscillate, so the displayed critical limit is explicitly conditional on convergence of that ratio. Priority is assessed against inspected accessible sources and remains provisional; a wider uninspected generation formula might implicitly yield some part of the theorem. No independent mathematical audit has been performed.

## References

[1] D. Sercombe and A. Shalev, *Random generation of associative algebras*, arXiv:2009.01115 (first posted 2020-09-02); *J. London Math. Soc.* 109 (2024), e12827, DOI: 10.1112/jlms.12827. https://arxiv.org/abs/2009.01115

[2] M. Iovanov and A. Sistko, *Maximal Subalgebras of Finite-Dimensional Algebras*, arXiv:1705.00762 (2017); *Forum Math.* 31 (2019), Proposition 4.2. https://arxiv.org/abs/1705.00762

[3] R. V. Kravchenko, M. Mazur and B. V. Petrenko, *On the smallest number of generators and the probability of generating an algebra*, arXiv:1001.2873 (2010). https://arxiv.org/abs/1001.2873

[4] V. Mazorchuk and X. Zhang, *Bimodules over uniformly oriented A-type quivers with radical square zero*, arXiv:1703.08377 (2017). https://arxiv.org/abs/1703.08377

# Sharp adjacent parity modes for Poisson trinomial sums

## Finding
Let \(n\ge 1\) and let \(X_1,\ldots,X_n\) be independent random variables taking values in \(\{0,1/2,1\}\), with probabilities \(L_i,T_i,W_i\ge0\) summing to one. Set \(X=\sum_i X_i\). Assume both \(\Pr(X\in\mathbb Z)>0\) and \(\Pr(X\in\mathbb Z+1/2)>0\). Every mode \(m_E\) of the law of \(X\) conditional on integer values and every mode \(m_O\) of its law conditional on half-integer values satisfy the **sharp universal bound**

\[
|m_E-m_O|\le\frac32.
\]

If every \(L_i,T_i,W_i\) is **strictly positive**, then every such pair of modes is in fact *adjacent on the half-integer grid*:

\[
\boxed{|m_E-m_O|=\frac12.}
\]

The weaker universal constant \(3/2\) is attained at the boundary. For two independent variables with respective probabilities \((L_1,T_1,W_1)=(0,1/4,3/4)\) and \((L_2,T_2,W_2)=(1/2,0,1/2)\), the integer conditional modes are \(1,2\), while the half-integer conditional modes are \(1/2,3/2\). Choosing \(2\) and \(1/2\) attains separation \(3/2\). In particular, positivity is indispensable for the assertion that *all* pairs of modes have separation \(1/2\).

## Assumptions and scope
The sample size is any positive integer. Probabilities may be heterogeneous and may vanish, subject to both parity classes having positive probability. Modes mean **all** maximizing support points, including ties. The theorem compares conditional modes, not unconditional modes or means. The strict conclusion assumes all three outcome probabilities of every summand are positive; its conclusion makes no assertion about gaps between non-modal probabilities.

Set \(H=2X\) and form the probability generating polynomial

\[
F(w)=\mathbb E[w^H]=\prod_{i=1}^n(L_i+T_iw+W_iw^2)=P(w^2)+wQ(w^2),
\]

where \(P(z)=\sum_{k=0}^n p_kz^k\), \(Q(z)=\sum_{k=0}^{n-1}q_kz^k\), and \(p_k=\Pr(X=k)\), \(q_k=\Pr(X=k+1/2)\). Conditioning merely divides each coefficient sequence by its positive total mass and so preserves its modes.

## Proof
**Step 1 (strict stability and alternating zeros).** First suppose all \(L_i,T_i,W_i>0\). Every quadratic factor has its roots strictly in the left half-plane (their real part is negative, whether the roots are real or conjugate). Hence so does \(F\). Write \(F(w)=c\prod_{j=1}^{2n}(w+\zeta_j)\), where \(c>0\) and \(\Re\zeta_j>0\). For real \(y\ge0\), choose the continuous phase \(\phi(y)=\arg F(iy)\) with \(\phi(0)=0\). Since the factors occur in conjugate pairs,

\[
\phi'(y)=\sum_{j=1}^{2n}\frac{\Re\zeta_j}{|\zeta_j+iy|^2}>0,
\qquad
\phi(y)\mathrel{\longrightarrow}_{y\to\infty}n\pi.
\]

Moreover \(F(iy)=P(-y^2)+iyQ(-y^2)\), so zeros of \(P(-y^2)\) occur at the phases \(\pi/2,3\pi/2,\ldots,(n-1/2)\pi\), and the zeros of \(Q(-y^2)\) occur at \(\pi,2\pi,\ldots,(n-1)\pi\). The phase is strictly increasing, hence all these zeros are simple. Thus

\[
P(z)=c_P\prod_{j=1}^{n}(z+a_j),\qquad
Q(z)=c_Q\prod_{j=1}^{n-1}(z+b_j),
\quad
0<a_1<b_1<a_2<\cdots<b_{n-1}<a_n,
\]

with \(c_P,c_Q>0\). This argument supplies directly the interlacing property often called the Hermite--Biehler theorem. For \(n=1\), \(Q\) is constant; the conclusion follows immediately because the possible even modes are \(0\) and \(1\), while the odd mode is \(1/2\).

**Step 2 (positive partial fractions).** For \(n\ge2\), the interlacing makes every partial-fraction residue positive:

\[
\frac{Q(z)}{P(z)}=\sum_{j=1}^n\frac{c_j}{z+a_j},
\qquad c_j=\frac{Q(-a_j)}{P'(-a_j)}>0.
\]

Indeed, the numerator and denominator of the residue have the same sign, since exactly \(j-1\) of the factors in each product are negative at \(-a_j\). Define \(R_j(z)=P(z)/(z+a_j)=\sum_{k=0}^{n-1}r_{j,k}z^k\), so \(Q=\sum_jc_jR_j\). Each \(R_j\) has strictly positive coefficients and only negative real zeros. Newton's coefficient inequalities imply

\[
r_{j,k}^{2}>r_{j,k-1}r_{j,k+1}
\]

when \(r_{j,-1}=r_{j,n}=0\), for every \(0\le k\le n-1\), with the evident interpretation at the endpoints.

**Step 3 (strict coefficient-ratio sandwich).** Since \(P=(z+a_j)R_j\), the previous inequality gives, for every \(0\le k\le n-2\),

\[
\frac{p_{k+1}}{p_k}
>
\frac{r_{j,k+1}}{r_{j,k}}
>
\frac{p_{k+2}}{p_{k+1}}.
\]

For the first inequality, after clearing the positive denominators, the difference is \(r_{j,k}^{2}-r_{j,k-1}r_{j,k+1}>0\). For the second, the cleared difference is \(a_j(r_{j,k+1}^{2}-r_{j,k}r_{j,k+2})>0\). Since \(q_{k+1}/q_k\) is a positive weighted average of the ratios \(r_{j,k+1}/r_{j,k}\), it follows that

\[
\boxed{\frac{p_{k+1}}{p_k}>\frac{q_{k+1}}{q_k}>\frac{p_{k+2}}{p_{k+1}}}\qquad(0\le k\le n-2).
\]

This is stronger than separate log-concavity of the two conditional distributions.

**Step 4 (strictly positive probabilities).** Both \(P\) and \(Q\) have real negative zeros and thus strictly log-concave positive coefficient sequences; each modal set consists of one index or two adjacent indices. Let \(m\) be any modal coefficient index of \(P\). The strict ratio sandwich implies that \(Q\) is strictly increasing from index \(m-2\) to \(m-1\), when these indices exist, and strictly decreasing from index \(m\) to \(m+1\), when these indices exist. Its modes therefore lie in \(\{m-1,m\}\) (intersected with the valid support). If \(P\) has two modal indices, applying this conclusion to each forces the unique \(Q\) modal index between them. Consequently, for **every** pair of modal indices \(m,j\) of \(P,Q\), \(m-j\in\{0,1\}\), yielding \(|m-(j+1/2)|=1/2\).

**Step 5 (boundary probabilities).** Replace each triple of probabilities by its mixture with \((1/3,1/3,1/3)\) using any mixing weight \(\eta>0\). As \(\eta\downarrow0\), polynomial coefficients converge. Cross-multiplying the strict ratios in Step 3 and passing to the limit gives the two inequalities

\[
p_{k+1}q_k\ge p_kq_{k+1},\qquad
q_{k+1}p_{k+1}\ge p_{k+2}q_k,
\qquad 0\le k\le n-2.
\]

The polynomials \(P,Q\), if nonzero, remain real-rooted with nonpositive zeros: this follows from the coefficientwise limit of the strictly real-rooted polynomials after discarding vanishing leading coefficients. Their nonzero coefficient supports are consecutive intervals and Newton's strict inequality holds wherever three neighboring coefficients are positive. Hence each has at most two adjacent modal indices.

Because both conditional masses stay positive at the limit, every limiting modal coefficient has positive mass. There are only finitely many coefficient indices, so, for all sufficiently small mixing weights, **every** mode of the perturbed \(P\) and \(Q\) belongs to the corresponding limiting modal set. The interior result therefore guarantees that the two limiting modal sets contain *at least one adjacent pair* \(m,j\) with \(m-j\in\{0,1\}\).

Each limiting modal set has one or two consecutive indices. If some pair of limiting modes had separation strictly greater than \(3/2\), the parity lattice forces separation at least \(5/2\). Combined with the existence of an adjacent pair and the two-index maximum length, this would require precisely one of the following two configurations, for an integer \(h\):

- \(P\) has modal set \(\{h,h+1\}\) and \(Q\) has modal set \(\{h+1,h+2\}\);
- \(P\) has modal set \(\{h,h+1\}\) and \(Q\) has modal set \(\{h-2,h-1\}\).

The first configuration gives \(p_h=p_{h+1}>0\) and \(q_h<q_{h+1}\), contradicting the first weak coefficient inequality at \(k=h\), which forces \(q_h\ge q_{h+1}\). The second gives \(p_{h-1}<p_h\) and \(q_{h-2}=q_{h-1}>0\), contradicting the second weak inequality at \(k=h-2\), which forces \(p_{h-1}\ge p_h\). These configurations are therefore impossible; all pairs satisfy \(|m-(j+1/2)|\le3/2\).

**Step 6 (sharpness).** For the stated two-summand boundary example,

\[
F(w)=\frac{(w+3w^2)(2+2w^2)}{16}
=\frac{2w+6w^2+2w^3+6w^4}{16}.
\]

Thus \((p_0,p_1,p_2)=(0,6,6)/16\) and \((q_0,q_1)=(2,2)/16\). The mode sets are exactly those given in the finding, so separation \(3/2\) is attained. For strictly positive probabilities, separation is always exactly \(1/2\), and no smaller uniform separation is possible because the two lattices are disjoint.

## Verification
The standalone Python file `verify_modal.py` performs convolution and all coefficient comparisons using exact integer arithmetic. It exhaustively checks strictly positive integer-weight triples totaling five for up to six summands, with additional fixed-seed heterogeneous tests up to fourteen summands, and verifies both strict ratio inequalities and every cross-parity pair of modes. It also exhaustively checks boundary triples totaling four for up to four summands against the universal \(3/2\) bound and the weak cross inequalities. The designated two-summand extremizer is checked exactly. The successful program output was:

`PASS: 60986 strictly-positive exact coefficient tests, 52686 boundary exploratory mode tests (maximum observed distance 1.5); all exact integer arithmetic`

These finite checks test the formulas but do not prove the arbitrary-parameter or arbitrary-length theorem; Steps 1--6 provide that proof.

## Relationship to prior work
Broadie and Petkova (2026), Theorem 1 and Proposition 3, prove that the two parity-conditional laws are Poisson-binomial and that any pair of their modes differs by at most \(5/2\). Their full-text proof bounds each mode separately from the overall mean. The present result instead uses the *joint* interlacing of the two coefficient sequences to replace \(5/2\) by the optimal \(3/2\) on the full parameter simplex, and by exact adjacency \(1/2\) in its positive interior. It does not claim originality for the Hermite--Biehler interlacing theorem, the Newton inequalities, or classical Poisson-binomial mode facts. Earlier work on extended Bernoulli sums by Gnedin (2024) studies cross-modality and Darroch-type rules rather than this relation between two parity-conditioned summands of a trinomial law.

## Limitations
Both conditioning events must have positive probability; when one is impossible its conditional modes are undefined. The strengthened \(1/2\) assertion cannot be extended to all boundary distributions, as the explicit witness proves. The theorem does not claim a sharpening of the separate mode-to-mean bounds, of unconditional modal structure, or of match-ordering optimality thresholds. Earlier classical total-positivity results may provide alternative routes to the coefficient-ratio sandwich; no independence or priority claim for those tools is made.

## References
- Mark Broadie and Ina Petkova, *On the structure of the Poisson trinomial distribution*, arXiv:2603.09019v1, first submitted 2026-03-09, https://arxiv.org/html/2603.09019v1 (especially Sections 2--3 and Proposition 3).
- Alexander Gnedin, *Cross Modality of the Extended Binomial Sums*, arXiv:2408.06477v1, first submitted 2024-08-12, https://arxiv.org/html/2408.06477v1 (extended Bernoulli sums and Darroch-type modal properties).
- Classical Hermite--Biehler interlacing theorem and Newton's inequalities; both are invoked in the specific forms reconstructed in the proof above.

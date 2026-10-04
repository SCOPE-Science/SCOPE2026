# Exact rank-two optimum for DNA coverage depth
## Finding
For every prime power \(q\) and every integer \(n\ge 2\), write
\[
n=a(q+1)+r,\qquad 0\le r<q+1.
\]
For the uniform noiseless coverage-depth problem on \([n,2]_q\) linear codes,
\[
\mathbb E_{\mathrm{opt}}[n,2]_q
=1+(q+1-r)rac{a}{n-a}+rrac{a+1}{n-a-1}.
\]
The optimizers are exactly the codes whose generator matrices have no zero column and whose multiplicities among the \(q+1\) one-dimensional subspaces of \(\mathbb F_q^2\) differ by at most one. Thus exactly \(r\) projective classes occur \(a+1\) times and the remaining \(q+1-r\) classes occur \(a\) times.

## Assumptions and scope
The model is the full-recovery, uniform, noiseless DNA coverage-depth model: the \(n\) columns of a rank-two generator matrix are sampled independently and uniformly with replacement until the sampled columns span \(\mathbb F_q^2\). The field size \(q\) is any prime power and \(n\ge2\). The statement concerns linear \([n,2]_q\) codes only.

## Proof
Let \(G\) be a rank-two \(2	imes n\) generator matrix. An optimal \(G\) has no zero column. Indeed, if a column is zero, replace it by any existing nonzero column \(v\). For every sequence of sampled coordinate indices, the span produced after replacement contains the original span, so the stopping time cannot increase. Because \(G\) has rank two, there is another column \(w\) independent of \(v\); on the positive-probability event that the replaced coordinate is sampled first and the coordinate of \(w\) second, the new matrix has already reached rank two while the old matrix has not. Hence the expectation strictly decreases.

Assume therefore that every column is nonzero. The nonzero columns fall into the \(q+1\) projective classes, i.e. the one-dimensional subspaces of \(\mathbb F_q^2\). Let their multiplicities be
\[
m_1,\ldots,m_{q+1}\in\mathbb Z_{\ge0},\qquad \sum_{i=1}^{q+1}m_i=n.
\]
After the first draw, the sampled span has dimension one. Conditional on the first sampled projective class being \(i\), which occurs with probability \(m_i/n\), each subsequent draw leaves that line with probability \((n-m_i)/n\). Thus the additional waiting time is geometric with mean \(n/(n-m_i)\), and
\[
\mathbb E[G]=1+\sum_{i=1}^{q+1}rac{m_i}{n-m_i}.
\]
Set \(f(t)=t/(n-t)\) for \(0\le t<n\). Its discrete first difference is
\[
f(t+1)-f(t)=rac{n}{(n-t-1)(n-t)},
\]
which is strictly increasing in \(t\). Hence if two multiplicities satisfy \(x\ge y+2\), then
\[
f(x)+f(y)>f(x-1)+f(y+1).
\]
So any multiplicity vector with two entries differing by at least two can be strictly improved by moving one column from a larger projective class to a smaller one. Iterating this balancing operation shows that every minimizer has all multiplicities differing by at most one, and strictness shows that no other multiplicity multiset is optimal.

Writing \(n=a(q+1)+r\) with \(0\le r<q+1\), the balanced multiplicities are \(a+1\) in exactly \(r\) classes and \(a\) in the other \(q+1-r\) classes. Substitution into the expectation formula gives
\[
\mathbb E_{\mathrm{opt}}[n,2]_q
=1+(q+1-r)rac{a}{n-a}+rrac{a+1}{n-a-1},
\]
as claimed.

## Verification
The accompanying verifier exhaustively enumerates every composition of \(n\) into \(q+1\) projective multiplicities for \(2\le q\le6\) and \(2\le n\le10\), computes the exact rational expectation, and confirms both the displayed minimum and the equality characterization. It also checks the discrete-convexity exchange identity symbolically through exact rational arithmetic.

For \(n\le q+1\), the formula reduces to
\[
1+rac{n}{n-1},
\]
which is the known MDS value for dimension two. For \(n=q+1\), it becomes \(2+1/q\), the known simplex/MDS value. The genuinely non-MDS regime covered here is \(n>q+1\).

## Relationship to prior work
Bar-Lev, Sabary, Gabrys, and Yaakobi introduced the full-recovery coverage-depth optimization and proved MDS codes optimal whenever an \([n,k]_q\) MDS code exists. For dimension two this covers \(n\le q+1\), because at most \(q+1\) pairwise nonproportional columns exist.

Bertuzzo, Ravagnani, and Yaakobi later studied small-field coverage depth, derived the simplex expectation, and formulated the general optimal-coverage problem. Their 2025 preprint gives computational evidence for simplex optimality at \([7,3]_2\); their March 2026 extension still lists simplex optimality as an open conjectural direction and develops formulas for fixed code families rather than optimizing over all codes. The rank-two formula above instead solves the optimization problem for every length \(n\), including every non-MDS length \(n>q+1\), and characterizes all optimizers by balanced projective multiplicities.

## Limitations
The result is special to dimension two, where after the first nonzero draw only the projective class of that draw matters and the remaining stopping time is geometric. In higher dimension the state depends on the whole sampled subspace, so the same one-dimensional balancing reduction does not directly apply. The literature search found no matching rank-two optimization theorem, but database search cannot prove absolute novelty.

## References
1. M. Bertuzzo, A. Ravagnani, E. Yaakobi, “The Coverage Depth Problem in DNA Storage Over Small Alphabets,” arXiv:2507.20639v1, 28 July 2025.
2. M. Bertuzzo, A. Ravagnani, E. Yaakobi, “The DNA Coverage Depth Problem: Duality, Weight Distributions, and Applications,” arXiv:2603.06489v1, 6 March 2026.
3. D. Bar-Lev, O. Sabary, R. Gabrys, E. Yaakobi, “Cover Your Bases: How to Minimize the Sequencing Coverage in DNA Storage Systems,” arXiv:2305.05656v1, 9 May 2023; later IEEE Transactions on Information Theory 71(1), 192–218 (2025).

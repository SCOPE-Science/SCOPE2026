# Discrete-theta spectrum law for commuting triangular idempotents

## Finding
Let \(q\ge2\) be a prime power, \(k\ge1\) an integer, and \(m=2^k\). Let \(\mathcal T_n(q)\) denote the algebra of upper triangular \(n\times n\) matrices over \(\mathbb F_q\). Choose an ordered tuple \((E_1,\ldots,E_k)\) uniformly among all tuples of pairwise commuting idempotents in \(\mathcal T_n(q)\). For each binary character \(c\in\{0,1\}^k\), let \(N_c\) be the dimension of the joint eigenspace with eigenvalues \(c\). Let \(D_n=\dim_{\mathbb F_q}\mathbb F_q[E_1,\ldots,E_k]\).

The following *joint spectrum law* and *sharp proper-generation rate* hold for every fixed \(q,k\). Write \(n=mh+s\), \(0\le s<m\), and
\[
\Theta_{m,s}(q)=\sum_{\substack{\delta\in\mathbb Z^m\\\sum_c\delta_c=s}}q^{-\frac12\sum_c(\delta_c-s/m)^2}.
\]
This sum is positive and absolutely convergent. As \(n\to\infty\) through the residue class \(s\bmod m\),
\[
\Pr\bigl[(N_c-h)_c=\delta\bigr]\longrightarrow
\frac{q^{-\frac12\sum_c(\delta_c-s/m)^2}}{\Theta_{m,s}(q)}
\quad\text{for every fixed integral }\delta\text{ with }\sum_c\delta_c=s.
\]
The convergence is in total variation on the countable lattice \(\{\delta:\sum_c\delta_c=s\}\). In particular, the joint eigenspace multiplicities fluctuate on the bounded, discrete-Gaussian scale rather than a square-root scale.

For every \(1\le a<m\), the precise quadratic logarithmic rate for generating a split algebra of dimension \(a\) is
\[
\lim_{n\to\infty}\frac{1}{n^2}\log\Pr(D_n=a)
=-\frac{\log q}{2}\left(\frac1a-\frac1m\right).
\]
Consequently,
\[
\boxed{\lim_{n\to\infty}\frac1{n^2}\log\Pr(D_n<m)
=-\frac{\log q}{2m(m-1)}.}
\]
These statements include characteristic two and extension fields, with no splitting-field restriction.

For completeness, if \(Z_{n,k}(q)\) is the number of admissible tuples, the exact weighted identity is
\[
Z_{n,k}(q)=\sum_{\substack{(n_c)_{c\in\{0,1\}^k}\ge0\\\sum_c n_c=n}}
\frac{n!}{\prod_c n_c!}\,q^{\frac12(n^2-\sum_c n_c^2)},
\]
and the sharp count asymptotic for fixed \(q,k\) and \(n\equiv s\pmod m\) is
\[
Z_{n,k}(q)\sim
\frac{m^{n+m/2}}{(2\pi n)^{(m-1)/2}}
q^{\frac12(1-1/m)n^2}\Theta_{m,s}(q).
\]
The basic diagonal-color weighted count is closely related to a previously published scalar-root-potent matrix count and is **not** claimed to be a new counting polynomial. The assessed finding is the probabilistic spectral refinement, the discrete-theta limit, and the dimension-defect rate for commuting idempotent families.

## Assumptions and scope
All matrices are upper triangular over a finite field. An idempotent satisfies \(E^2=E\). A tuple is ordered, and the commuting condition is pairwise. Uniformity is over admissible tuples, not conjugacy classes. Joint eigenvalues belong to \(\{0,1\}^k\) over the ground field; no extension is necessary. The logarithm is natural. The asymptotics keep \(q,k\) fixed and take \(n\to\infty\). All \(m\) colors are labelled binary characters.

## Proof
**Step 1: diagonalization compatible with the fixed flag.** For every character \(c\in\{0,1\}^k\), form the joint spectral projection
\[
P_c=\prod_{j:c_j=1}E_j\prod_{j:c_j=0}(I-E_j).
\]
These are pairwise orthogonal idempotents, their sum is \(I\), and \(E_j=\sum_c c_jP_c\). If the \(i\)-th joint diagonal character is \(c(i)\), then \(v_i=P_{c(i)}e_i\) equals \(e_i\) plus a linear combination of preceding standard basis vectors. The matrix \(U\) with columns \(v_i\) is upper unitriangular and simultaneously conjugates the tuple to diagonal matrices with characters \(c(i)\). Thus the dimension of each joint eigenspace is the number of occurrences of that character on the diagonal, and \(D_n\) is the number of occurring characters.

**Step 2: orbit weights.** For a fixed word \((c(1),\ldots,c(n))\), the upper unitriangular group acts transitively on corresponding tuples by conjugation. The stabilizer consists exactly of upper unitriangular matrices whose \((i,j)\)-entry vanishes unless \(c(i)=c(j)\). Hence the orbit has cardinality
\[
q^{\#\{(i,j):i<j,\ c(i)\ne c(j)\}}
=q^{\frac12(n^2-\sum_c n_c^2)}.
\]
There are \(n!/\prod_c n_c!\) words with prescribed color multiplicities. This proves the weighted identity. Restricting to exactly \(a\) positive multiplicities gives the exact count for \(D_n=a\),
\[
\binom ma\sum_{\substack{b_1+\cdots+b_a=n\\b_j\ge1}}
\frac{n!}{\prod_{j=1}^a b_j!}\,q^{\frac12(n^2-\sum_{j=1}^a b_j^2)}.
\]

**Step 3: the discrete-theta limit.** Write \(n_c=h+\delta_c\), with \(\sum_c\delta_c=s\). The exponent has the exact decomposition
\[
\frac12(n^2-\sum_c n_c^2)
=\frac12(1-1/m)n^2-\frac12\sum_c(\delta_c-s/m)^2.
\]
For each fixed \(\delta\), Stirling's formula gives
\[
\frac{n!}{\prod_c(h+\delta_c)!}
\sim\frac{m^{n+m/2}}{(2\pi n)^{(m-1)/2}}.
\]
The multinomial coefficient is maximized at nearly equal multiplicities, so for fixed \(m\) it is uniformly at most a constant times the right-hand normalization. Since \(q^{-\frac12\sum_c(\delta_c-s/m)^2}\) is summable on the integral hyperplane, dominated convergence proves the count asymptotic. The same domination applied to normalized individual weights proves total-variation convergence to the stated lattice law.

**Step 4: sharp dimension-defect rates.** If exactly \(a\) characters occur, Cauchy--Schwarz gives \(\sum_j b_j^2\ge n^2/a\). Thus the count is at most \(m^n q^{\frac12(1-1/a)n^2}\). Conversely, choose \(a\) characters and a single nearly balanced word among them; it yields at least \(q^{\frac12(1-1/a)n^2-O_a(1)}\) tuples. Hence the logarithmic count divided by \(n^2\) tends to \(\frac12(1-1/a)\log q\). Subtract the corresponding total-count exponent \(\frac12(1-1/m)\log q\) to obtain the first rate. For \(D_n<m\), the largest exponent among \(a<m\) is at \(a=m-1\), proving the second rate.

## Verification
The standalone `CHECK.py` enumerates upper triangular matrices over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_4\), checks idempotency and pairwise commutation by multiplication, and compares every fixed-diagonal-word multiplicity against the orbit formula. It also compares the full distribution of generated-algebra dimensions against an independent multinomial calculation. All twelve exhaustive configurations passed, involving 57,836 ordered tuples before commutation filtering. For example, with \(q=2\), \(k=2\), \(n=4\), the dimension distribution for \(D_n=1,2,3,4\) is \((4,960,4608,1536)\), totaling \(7108\).

Run `python3 CHECK.py` with Python 3 and its standard library. Finite checks confirm the finite enumeration identities in tested cases; the general formulas and asymptotic limits are proved above and do not follow from enumeration.

## Relationship to prior work
Hou (2019) characterizes idempotents in triangular matrix rings, and Wright (2020) develops their construction and enumeration in general rings. Gargate and Gargate (2020), Theorems 1.1--1.2 and section 5, provide a color-multiplicity enumeration of single split-polynomial potent upper triangular matrices; Słowik (2014) proves a related root-of-unity count. Their finite weighted sums have the same functional shape as the counting identity above when the required scalar roots exist. They are credited as prior exact-enumeration results. A general Potts state-sum also shares this color-energy weighting, though it does not itself identify the commuting-idempotent eigenspaces.

The claim here is the specific fixed-field discrete-theta *joint-spectrum distribution* and the *sharp quadratic rate* of proper split-algebra generation in the commuting-idempotent model. The inspected full text of Gargate and Gargate treats finite enumeration but not these distributional limits; accessible abstracts of Hou and Wright do not resolve whether their longer texts imply an analogous asymptotic. Connections to classical complete-graph antiferromagnetic Potts statistics remain a possible route to an equivalent earlier limit theorem.

## Limitations
The work does not classify the tuples up to arbitrary invertible conjugation, and it does not apply unchanged when the number of idempotents \(k\) grows with \(n\) or when \(q\) varies with \(n\). The asymptotic theta law is a fixed-parameter result, not a central limit theorem. No claim of historical uniqueness is made; inaccessible relevant full texts and possible general lattice-theta theorems are genuine priority risks.

## References
1. X. Hou, *Idempotents in triangular matrix rings*, Linear and Multilinear Algebra, first published online 22 March 2019. DOI: 10.1080/03081087.2019.1596223.
2. S. E. Wright, *Triangular idempotent matrices over a general ring*, Linear and Multilinear Algebra, first published online 1 June 2020. DOI: 10.1080/03081087.2020.1773377.
3. I. Gargate and M. Gargate, *\((k+1)\)-potent Matrices in Triangular Matrix Groups and Incidence Algebras of Finite Posets*, arXiv:2009.04243 (2020), especially Theorems 1.1--1.2 and section 5.
4. R. Słowik, *How to construct a triangular matrix of a given order*, Linear and Multilinear Algebra 62 (2014), 28--38. DOI: 10.1080/03081087.2012.762712.
5. R. Shrock and Y. Xu, *Exact Results on Potts Model Partition Functions in a Generalized External Field and Weighted-Set Graph Colorings*, Journal of Statistical Physics 141 (2010), 909--939. DOI: 10.1007/s10955-010-0089-3.

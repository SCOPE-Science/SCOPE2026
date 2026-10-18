# A complete Poisson–binomial dichotomy for binary adjacent-pattern counts

## Finding

Let \(X_1,\dots,X_n\) be independent Bernoulli variables with a common parameter \(p\in(0,1)\). For any binary two-letter word \(w\in\{00,01,10,11\}\), let \(N_w\) count its overlapping occurrences among the consecutive pairs \((X_i,X_{i+1})\), where \(1\le i<n\).

**Theorem.** For every integer \(n\ge3\), the law of \(N_w\) is a sum of independent Bernoulli variables if and only if \(w\in\{01,10\}\). More strongly, for either oriented-change word,

\[
N_{01}\ \stackrel{d}{=}\ N_{10}\ \stackrel{d}{=}\ \sum_{j=1}^{\lfloor n/2\rfloor} B_j,
\qquad
\Pr(B_j=1)=4p(1-p)\cos^2\!\left(\frac{j\pi}{n+1}\right),
\]

with independent \(B_j\). For the two equal-letter words, the probability-generating polynomials are not real-rooted, and indeed violate the necessary Newton inequalities when \(n\ge4\); when \(n=3\) their discriminants are negative. For \(n=1\) the counts are identically zero, and for \(n=2\) all four counts are Bernoulli. These are the sharp length exceptions.

## Assumptions and scope

The letters are iid, take the values zero and one, and have strictly interior bias \(0<p<1\). Occurrences can overlap. A Poisson–binomial law means the distribution of a finite sum of mutually independent Bernoulli variables, allowing zero and one parameters where necessary. Equalities here are equalities in distribution, not couplings to the original dependent indicators. At boundary biases \(p=0\) or \(p=1\), each count is deterministic and the strict dichotomy does not apply.

## Proof

**Oriented patterns.** Put \(q=1-p\), \(u=pq(1-z)\), and \(G_n(z)=\mathbb E[z^{N_{10}}]\). With states recording the preceding letter, the weighted transition matrix is

\[
T(z)=\begin{pmatrix}q&p\\qz&p\end{pmatrix},\qquad
G_n(z)=(q,p)T(z)^{n-1}\begin{pmatrix}1\\1\end{pmatrix}.
\]

The trace of \(T(z)\) is one and its determinant is \(u\). Cayley–Hamilton therefore gives \(G_{n+2}=G_{n+1}-uG_n\). The initial values are \(G_1=1\) and \(G_2=1-u\). Solving this recurrence yields

\[
G_n(z)=R_n(u),\qquad
R_n(u)=\sum_{k=0}^{\lfloor n/2\rfloor}(-u)^k\binom{n-k}{k}.
\]

Let \(U_n\) denote the Chebyshev polynomial of the second kind. Its recurrence implies the polynomial identity \(R_n(u)=u^{n/2}U_n(1/(2\sqrt u))\), interpreted by polynomial cancellation at \(u=0\). The zeros of \(U_n\) are \(\cos(j\pi/(n+1))\), so, using \(R_n(0)=1\),

\[
R_n(u)=\prod_{j=1}^{\lfloor n/2\rfloor}
\left(1-4u\cos^2\!\left(\frac{j\pi}{n+1}\right)\right).
\]

Substitution of \(u=pq(1-z)\) gives the claimed product of Bernoulli generating functions. All parameters lie strictly between zero and one: \(0<4pq\le1\) and \(0<\cos^2(j\pi/(n+1))<1\) for the displayed index range. Reversing an iid word exchanges \(01\) and \(10\) while preserving its probability, hence \(N_{01}\stackrel d=N_{10}\).

**Equal-letter patterns.** It suffices to analyze \(11\), since replacing each letter by its complement exchanges \(11\) and \(00\) and replaces \(p\) by \(q\). Put \(d=n-1\), and write \(a_j=\Pr(N_{11}=j)\) for \(0\le j\le d\). When \(n\ge4\), direct classification of the words with at most two destroyed adjacent \(11\)-pairs gives

\[
a_d=p^n,\qquad
a_{d-1}=2p^{n-1}q,\qquad
 a_{d-2}=(n-2)p^{n-1}q+3p^{n-2}q^2.
\]

Indeed, the maximum needs all ones; one lost pair requires one zero at either endpoint. Exactly two lost pairs arise from a single interior zero (\(n-2\) choices) or from zeros in exactly one of the three unordered position pairs \(\{1,2\}\), \(\{1,n\}\), \(\{n-1,n\}\). There are no other possibilities: further zeros, or any other placement of two zeros, destroy at least three adjacent \(11\)-pairs.

Any Poisson–binomial distribution of degree \(d\) has a mass sequence obeying the Newton inequality

\[
a_{d-1}^2\ge\frac{2d}{d-1}a_da_{d-2}.
\]

But the explicit masses above give

\[
\frac{a_{d-1}^2}{a_da_{d-2}}
=\frac{4q}{(n-2)p+3q}<\frac43
<\frac{2(n-1)}{n-2}=\frac{2d}{d-1},
\]

which is a strict contradiction for every \(n\ge4\) and \(p\in(0,1)\). For \(n=3\), the masses are \(a_2=p^3\), \(a_1=2p^2q\), and \(a_0=1-2p^2+p^3\); the quadratic discriminant is

\[
a_1^2-4a_0a_2=-4p^3q<0.
\]

Thus its polynomial cannot be a product of real linear factors. The same proofs apply to \(00\) with \(p\) and \(q\) swapped. Finally, no two-letter word can occur when \(n=1\), while when \(n=2\) every word count is a single indicator. This proves all cases. \(\square\)

## Verification

The standalone standard-library file `verify.py` enumerates all binary sequences through length ten for four rational biases, computes all four exact count laws, checks the oriented-pattern polynomial against a separately derived binomial-coefficient expression, and checks the top coefficients, strict Newton failure and the exact three-letter discriminant. It also numerically checks the cosine factorization over these cases. Run `python verify.py` in a directory containing the file. This is a finite consistency check; the parameter-uniform, all-length theorem is established by the preceding identities and inequalities.

## Relationship to prior work

Kumar and Upadhye study Stein-type approximations for counts of delimited runs, rather than a Poisson–binomial decomposition of undelimited adjacent two-letter word counts [1]. Kong obtains general joint rise/fall/run enumerators [2], which contain the underlying counting data as specializations; those enumerators do not themselves state this sharp real-rootedness distinction or the explicit independent-Bernoulli parameters. Tang and Tang review the general real-zero characterization of Poisson–binomial laws and the Newton inequalities used above [3]. Martin develops exact overlapping-pattern probability computations [4]; only publisher-accessible summary material was examined for this comparison. The factorization is closely related to standard matching-polynomial/Chebyshev structure, which is not claimed as a new general polynomial theorem. The asserted contribution is the complete four-word probability-law classification and explicit sharp structural contrast.

## Limitations

The result assumes iid letters and a two-letter binary pattern. It does not assert an analogous classification for nonidentical success probabilities, larger alphabets, longer motifs, or joint distributions of several motif counts. The explicit Bernoulli decomposition is distributional and does not imply the original overlapping occurrence indicators are independent. The originality comparison is limited by incomplete access to [4] and potentially unindexed classical run-polynomial results; an independent literature audit remains outstanding.

## References

[1] A. N. Kumar and N. S. Upadhye, *On Discrete Gibbs Measure Approximation to Runs*, arXiv:1701.03294 (first posted 2017-01-12), https://arxiv.org/abs/1701.03294 .

[2] Y. Kong, *Joint distribution of rises, falls, and number of runs in random sequences*, arXiv:2405.01748, https://arxiv.org/abs/2405.01748 .

[3] W. Tang and F. Tang, *The Poisson binomial distribution—Old & New*, arXiv:1908.10024, https://arxiv.org/abs/1908.10024 .

[4] D. E. K. Martin, *Computation of exact probabilities associated with overlapping pattern occurrences*, WIREs Computational Statistics (2019), https://doi.org/10.1002/wics.1477 .

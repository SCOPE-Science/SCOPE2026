# Two-imbalance border rigidity for balanced forbidden binary words

## Finding

Let \(w\) be a balanced binary word of even length \(k\ge4\), and let \(\mathcal B(w)\) denote its nonempty borders, **including \(w\)**. Define \(\Delta(b)=2|b|_1-|b|\). Let \(\rho(w)\) be the limiting fraction of ones in a uniformly chosen binary word of length \(n\) avoiding \(w\) as a contiguous factor, with the limit taken as \(n\to\infty\).

**Theorem.** If at most two proper borders \(b\ne w\) satisfy \(\Delta(b)\ne0\), then
\[
\rho(w)=\frac12\quad\Longleftrightarrow\quad \Delta(b)=0\text{ for every }b\in\mathcal B(w).
\]
In particular, two proper borders with *opposite* imbalances cannot cancel to restore frequency \(1/2\). This is the mixed-sign case not resolved by the sign-uniform criterion in Bóna–Maga–Richey (2026).

**Infinite mixed-sign family.** For each integer \(m\ge0\), set
\[
w_m=10001\,0^m\,1^{m+2}\,10001.
\]
Every \(w_m\) is balanced and has exactly the proper borders \(1\) and \(10001\), of imbalances \(+1\) and \(-1\). In fact \(\rho(w_m)>1/2\) for every \(m\ge0\). In particular, \(w_0=100011110001\), the explicit mixed-sign example in the 2026 motivating paper.

## Assumptions and scope

A border is a positive-length word that is both a prefix and suffix; the whole word counts as a border. The finite avoidance language is \(\Omega_n(w)=\{u\in\{0,1\}^n:w\text{ is not a contiguous factor of }u\}\), and
\[
\rho(w)=\lim_{n\to\infty}\frac{\sum_{u\in\Omega_n(w)}|u|_1}{n|\Omega_n(w)|}.
\]
The limit exists for the present class by primitivity of the forbidden-word presentation. This theorem is for balanced forbidden words of length at least four with at most two imbalanced *proper* borders. It does not address the alternative stopped-process statistic \(q(w)\), unbalanced forbidden words, or three or more imbalanced proper borders.

## Proof

**1. A strict Perron property.** Let \(\lambda\) be the exponential growth rate of \(|\Omega_n(w)|\). The standard forbidden-word labeled adjacency graph \(L_w\) is irreducible except for the four binary patterns \(10^{k-1}\), \(1^{k-1}0\), \(01^{k-1}\), and \(0^{k-1}1\) (Chandgotia–Marcus–Richey–Wu, Proposition 3.5). Since \(w\) has equally many zeros and ones, with at least two of each, none of these exceptions occurs. The graph has a self-loop at the vertex for the symbol different from the first symbol of \(w\). Thus its nonnegative integer adjacency matrix is primitive. Its Perron eigenvalue \(\lambda\) is an algebraic integer, all other eigenvalues have modulus strictly less than \(\lambda\), and \(1<\lambda<2\). For completeness: the self-loop vertex also has an edge to a distinct vertex, so its positive Perron eigenvector gives \(\lambda>1\); forbidding a finite word from the full binary shift gives \(\lambda<2\).

For every integer \(r\ge1\), \(\lambda^r\) is irrational. Indeed, suppose \(\lambda^r\in\mathbb Q\). Since \(\lambda\) is an algebraic integer, \(\lambda^r\) would be a positive integer. Yet \(1<\lambda<2\) implies \(\lambda\) is not a rational algebraic integer, so it has another distinct algebraic conjugate \(\beta\). Such a conjugate is another eigenvalue of the integer adjacency matrix. Applying the embedding to \(\lambda^r\) gives \(\beta^r=\lambda^r\), hence \(|\beta|=\lambda\), contradicting primitivity.

**2. The exact border balance identity.** Set
\[
B(X,Y)=\sum_{b\in\mathcal B(w)}X^{|b|}Y^{|b|_1},\qquad
H(x,y)=1-x(1+y)+B(x^{-1},y^{-1})^{-1}.
\]
The exact weighted avoidance generating function is \(\sum_{n,j}|\Omega_{n,j}(w)|x^ny^j=1/H(x,y)\) (Bóna–Maga–Richey, Fact 2.9). Primitivity gives a simple positive dominant pole \(x_0=1/\lambda\) at \(y=1\), with \(H_x(x_0,1)<0\). Marking ones by \(y\), implicit differentiation of \(H(x(y),y)=0\) gives
\[
\rho(w)=\frac{\lambda'(1)}{\lambda(1)}
=\frac{H_y(x_0,1)}{x_0H_x(x_0,1)}.
\]
The weighted border polynomial satisfies the exact identity
\[
2H_y(x_0,1)-x_0H_x(x_0,1)
=\frac{\sum_{b\in\mathcal B(w)}\Delta(b)\lambda^{|b|}}{B(\lambda,1)^2}.
\]
Consequently
\[
\rho(w)-\frac12
=\frac{\sum_{b\in\mathcal B(w)}\Delta(b)\lambda^{|b|}}
{2x_0H_x(x_0,1)B(\lambda,1)^2}.
\]
All denominators are nonzero, and the denominator displayed here is negative. This also determines the *sign* of the frequency bias.

**3. At most two terms cannot cancel.** Because \(w\) is balanced, \(\Delta(w)=0\). Under the hypothesis, the numerator above contains at most two nonzero terms. No terms means frequency \(1/2\). Exactly one term cannot vanish because \(\lambda>0\). If there are two nonzero terms, they have distinct border lengths \(a\ne b\) and nonzero integer coefficients \(u,v\), so cancellation would imply \(\lambda^{|a-b|}\in\mathbb Q\), contrary to Step 1. This proves both directions of the theorem.

**4. The infinite family.** The word \(w_m=10001\,0^m\,1^{m+2}\,10001\) has length \(12+2m\) and \(6+m\) ones, hence is balanced. Proper borders of length at most five are exactly \(1\) and \(10001\). Any longer border must begin with \(10001\), and therefore its starting position inside the word would be a noninitial occurrence of this factor. Apart from the terminal occurrence, such a factor can only begin at the final \(1\) of the initial \(10001\), and only when \(m=3\); in that case its next symbol is \(1\), whereas the sixth symbol of the original word is \(0\). Thus there is no proper border longer than five. The only nonzero imbalances are \(+1\) at length one and \(-1\) at length five. The numerator in Step 2 is \(\lambda-\lambda^5<0\); its denominator is negative, so \(\rho(w_m)>1/2\).

## Verification

Run `python3 verification/check_border_density.py` with Python 3 and NumPy installed. The independent spectral calculation constructs a prefix-state automaton, computes the Perron right/left eigenvectors and the frequency of one-labeled transitions, and compares the sign with the exact border-derivative formula for 348 balanced words of lengths four, six, eight, and ten that satisfy the theorem's hypothesis. It additionally evaluates the explicitly mixed-sign length-twelve example. The recorded output is in `verification/checker_output.txt`. All tests passed. The infinite proof uses primitivity and algebraic conjugacy, not finite computation.

## Relationship to prior work

The motivating paper's Fact 2.9 supplies the bivariate correlation identity. Its Theorem 3.5 supplies a combinatorial injection when all borders have the same weak imbalance sign, and Conjecture 6.1 proposes that frequency \(1/2\) occurs exactly when all borders are balanced. The explicit length-twelve mixed-sign word is discussed immediately after Theorem 3.5; neither the sign-uniform theorem nor its bit-flipped version covers it. The present result proves the density (\(\rho\)) half of that conjecture whenever at most two proper borders are imbalanced, including the mixed-sign family. It does **not** prove the other stopped-process (\(q\)) half. The 2024 one-forbidden-word graph paper supplies the irreducibility criterion, but its entropy and correlation results do not assert this two-imbalance density criterion.

## Limitations

The proof does not handle cancellation among three or more imbalanced proper borders. It requires a balanced forbidden word and uses the Perron property of its primitive presentation. Calculations check finite examples only; they are not an exhaustive census of all balanced words. No statement is made about statistical quantities other than limiting one density, nor about uniqueness of this formulation in unindexed literature. The result has not undergone independent validation.

## References

1. M. Bóna, B. Maga, J. Richey, *Letter frequency in shifts of finite type with one forbidden word*, arXiv:2606.06655, first public version June 4, 2026; especially Definition 2.6, Fact 2.9, Theorem 3.5, Conjecture 6.1, and the mixed-sign example after Theorem 3.5. https://arxiv.org/abs/2606.06655
2. N. Chandgotia, B. Marcus, J. Richey, C. Wu, *Shifts of finite type obtained by forbidding a single pattern*, arXiv:2409.09024, first public version September 13, 2024; especially Proposition 3.5. https://arxiv.org/abs/2409.09024
3. L. J. Guibas and A. M. Odlyzko, *String overlaps, pattern matching, and nontransitive games*, Journal of Combinatorial Theory A 30 (1981), 183–208 (classical overlap framework; cited through the papers above).

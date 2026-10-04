# Closed-form law for binary subsequence universality
## Finding
Fix the ambient alphabet \(\Sigma=\{0,1\}\). For a binary word \(w\), let \(\iota(w)\) be the largest integer \(j\) such that every binary word of length \(j\) occurs as a subsequence of \(w\). Let
\[
N_{n,j}=\bigl|\{w\in\Sigma^n:\iota(w)=j\}\bigr|.
\]
Then the complete bivariate distribution has the rational generating function
\[
\sum_{n\ge 0}\sum_{j\ge 0}N_{n,j}u^jz^n=\frac{1+z}{1-z-2uz^2}.
\]
Equivalently, \(N_{0,0}=1\); for \(n\ge1\), \(N_{n,0}=2\); and, for \(1\le j\le\lfloor n/2\rfloor\),
\[
N_{n,j}=2^j\left(\binom{n-j-1}{j-1}+2\binom{n-j-1}{j}\right),
\]
where a binomial coefficient outside its natural range is zero.

If \(\mathcal U(n,k,2)\) denotes the length-\(n\) binary words that are \(k\)-subsequence universal, then for \(k\ge1\)
\[
|\mathcal U(n,k,2)|=
\begin{cases}
0,&n<2k,\\
2^k\displaystyle\sum_{r=0}^{n-2k}2^{n-2k-r}\binom{k+r-1}{k-1},&n\ge2k.
\end{cases}
\]
For \(k=0\), every word qualifies, so \(|\mathcal U(n,0,2)|=2^n\).

For a uniformly random \(W_n\in\Sigma^n\), write \(X_n=\iota(W_n)\). Then
\[
\mathbb E[X_n]=\frac n3-\frac29+\frac29\left(-\frac12\right)^n
\]
and
\[
\operatorname{Var}(X_n)=\frac{2\left(1+2r_n\right)\left(3n+1-r_n\right)}{81},
\qquad r_n=\left(-\frac12\right)^n.
\]

## Assumptions and scope
Universality is taken with respect to the fixed two-letter ambient alphabet \(\{0,1\}\), including for unary and empty source words. A subsequence need not be contiguous. The result concerns exact finite-length enumeration and the first two moments of the universality index; it does not claim an analogous closed form for larger alphabets.

## Proof
The arch factorization of a word is obtained greedily by repeatedly taking the shortest nonempty prefix containing the whole ambient alphabet, leaving a final rest that omits at least one alphabet symbol. Prior work establishes that the number of arches equals the universality index.

For the binary alphabet, every arch has the unique form \(a^r\bar a\), where \(a\in\{0,1\}\), \(r\ge1\), and \(\bar a\) is the opposite bit. Indeed, before the last letter of a shortest prefix containing both symbols, only one symbol can have appeared, and the last letter must be the other symbol. Hence the ordinary length generating function for one arch is
\[
A(z)=2(z^2+z^3+\cdots)=\frac{2z^2}{1-z}.
\]
The rest is either empty or a positive unary word, so its generating function is
\[
R(z)=1+2(z+z^2+\cdots)=\frac{1+z}{1-z}.
\]
Uniqueness of the greedy arch factorization gives, with \(u\) marking arches,
\[
F(z,u)=R(z)\sum_{j\ge0}(uA(z))^j
=\frac{1+z}{1-z-2uz^2}.
\]
Extracting the coefficient of \(u^jz^n\) yields the displayed formula for \(N_{n,j}\).

A word is \(k\)-subsequence universal exactly when it has at least \(k\) arches. Cutting immediately after its \(k\)-th arch gives a bijection between such words and a sequence of \(k\) binary arches followed by an arbitrary binary suffix. Thus
\[
\sum_{n\ge0}|\mathcal U(n,k,2)|z^n
=\frac{A(z)^k}{1-2z}
=\frac{2^kz^{2k}}{(1-z)^k(1-2z)},
\]
and coefficient extraction gives the stated finite sum.

Finally, differentiating \(F(z,u)\) with respect to \(u\), setting \(u=1\), and using
\[
F(z,1)=\frac1{1-2z}
\]
gives the first factorial moment generating function. A second derivative gives the second factorial moment. Dividing the coefficient of length \(n\) by the total number \(2^n\) of binary words and simplifying gives the displayed mean and variance formulas.

## Verification
The standalone verifier `verify.py` implements the universality index in two independent ways: greedy arch extraction and the defining test that every binary word of the next length occurs as a subsequence. It checks equality of those implementations for every binary word through length \(10\). It then exhaustively enumerates every binary word through length \(18\), compares the full histogram with the closed form, compares cumulative counts with the formula for \(|\mathcal U(n,k,2)|\), and checks the exact rational mean and variance. Separately, it checks the coefficient recurrence implied by \((1-z-2uz^2)F=1+z\) through length \(80\). A successful replay prints `VERIFY_OK definition_n<=10 exhaustive_n<=18 recurrence_n<=80`.

These computations corroborate the finite algebra but are not used as a substitute for the generating-function proof of the all-length statement.

## Relationship to prior work
Barker, Fleischmann, Harwardt, Manea, and Nowotka introduced scattered-factor universality and the arch-factorization approach; the arch count is the universality index. Adamson later gave an \(O(nk\sigma)\)-time dynamic-programming algorithm for counting \(\mathcal U(n,k,\sigma)\) and, in the conclusion of that work, explicitly asked whether there is a general formula for the number of length-\(n\), \(k\)-subsequence-universal words. The formulas above answer the binary-alphabet slice of that question and strengthen it to the complete exact distribution of the universality index and its first two moments.

Schnoebelen and Veron develop arch-factorization algorithms, including compressed-word and circular universality, but do not state a fixed-length binary enumeration formula. Fleischmann, Höfer, Huch, and Nowotka give a detailed binary treatment of Simon congruence and count congruence classes, a different object from counting words of a fixed length by universality index. Adamson, Fleischmann, Huch, Koß, Manea, and Nowotka later give automata-based counting algorithms for \(k\)-universal accepted words; this broader algorithmic computability does not state the rational generating function, coefficient formula, or moment identities proved here.

## Limitations
The proof is specific to a fixed binary ambient alphabet. For larger alphabets, an arch has internal structure not captured solely by its length, so the one-variable arch generating function used here no longer suffices. Literature searches and full-text comparisons did not locate the displayed binary formulas, but absence from the inspected literature is not a proof that no independently obtained or differently phrased formula exists.

## References
1. Laura Barker, Pamela Fleischmann, Katharina Harwardt, Florin Manea, Dirk Nowotka, *Scattered Factor-Universality of Words*, arXiv:2003.04629v1, 2020-03-10. https://arxiv.org/abs/2003.04629
2. Duncan Adamson, *Ranking and Unranking k-subsequence universal words*, arXiv:2304.04583v1, 2023-04-10. https://arxiv.org/abs/2304.04583
3. Philippe Schnoebelen, Julien Veron, *On arch factorization and subword universality for words and compressed words*, arXiv:2304.11932v1, 2023-04-24. https://arxiv.org/abs/2304.11932
4. Pamela Fleischmann, Jonas Höfer, Annika Huch, Dirk Nowotka, *α-β-Factorization and the Binary Case of Simon's Congruence*, arXiv:2306.14192v1, 2023-06-25. https://arxiv.org/abs/2306.14192
5. Duncan Adamson, Pamela Fleischmann, Annika Huch, Tore Koß, Florin Manea, Dirk Nowotka, *k-Universality of Regular Languages*, arXiv:2311.10658v1, 2023-11-17. https://arxiv.org/abs/2311.10658

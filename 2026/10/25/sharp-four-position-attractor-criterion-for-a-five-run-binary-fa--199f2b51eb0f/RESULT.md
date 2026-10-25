# Sharp four-position attractor criterion for a five-run binary family

## Finding

Let \(b,c,e\) range independently over all positive integers and define the binary word
\[
W_{b,c,e}=0\,1^b0^c1\,0^e.
\]
A **string attractor** for a finite word is a set of positions such that every distinct nonempty *contiguous* factor has at least one occurrence containing a selected position. Write \(\gamma(W)\) for the least cardinality of such a set. Then
\[
\boxed{\gamma(W_{b,c,e})=4\quad\Longleftrightarrow\quad
 b\ge4,\ c\ge3,\ e>c.}
\]
For every other positive triple, \(2\le\gamma(W_{b,c,e})\le3\). In the four-position regime, four explicit, mutually disjoint occurrences of distinct uniquely occurring factors force four positions; the proof also constructs an attractor of that size. Thus this is an exact criterion, not merely an upper bound.

Let \(Q_n\) count the words of length \(n\) in this family with attractor number four. Then
\[
Q_n=\begin{cases}0,&5\le n<13,\\
\left\lfloor (n-11)^2/4\right\rfloor,&n\ge13,
\end{cases}
\qquad
\sum_{n\ge5}Q_nz^n=\frac{z^{13}}{(1-z)^2(1-z^2)}.
\]
Among the \(\binom{n-3}{2}\) words of this family of length \(n\), the proportion with attractor number four tends to \(1/2\). The shortest such word has length \(13\) and is \(0111100010000\), with run lengths \((1,4,3,1,4)\).

## Assumptions and scope

All exponents are strictly positive and each displayed power means that many consecutive occurrences of its symbol. Both boundary runs \(0\) and the fourth run \(1\) have length one. The conclusion concerns contiguous factors of the **linear** word, not scattered subsequences or circular factors. No classification of all five-run binary words is asserted. Indices in the proof and accompanying checker start at zero; the total length is \(n=2+b+c+e\).

## Proof

**Gap criterion.** Fix a set \(S\) of selected positions in a finite word. An occurrence which misses \(S\) lies entirely inside a maximal interval of unselected positions (a *gap*). Hence \(S\) is an attractor if every factor occurring entirely in a gap has some occurrence meeting \(S\). In checking this condition, it suffices to describe the factors possible inside each gap and an alternative covering occurrence.

**Universal four-position upper bound.** Put \(z=b+c\) and \(t=b+c+2\). In the zero-based word, the positions \(0,b,z,t\) contain, respectively, the initial zero, the last one of the long one-run, the last zero of the middle zero-run, and the first zero of the final zero-run. Set \(S_4=\{0,b,z,t\}\). The unselected gaps comprise: a possibly empty run of ones before position \(b\); a possibly empty run of zeros before position \(z\); the singleton one at \(z+1\); and a run of zeros after position \(t\). Every one-only factor has an occurrence through \(b\), and every zero-only factor of length at most the length of its gap has one through \(z\) or \(t\). The singleton one has an occurrence at \(b\). By the gap criterion, \(S_4\) attracts all factors and \(\gamma\le4\).

**Three-position constructions.** Suppose at least one of the inequalities \(b\ge4,c\ge3,e>c\) fails. The cases below cover all possibilities.

* If \(e\le c\), take \(S=\{0,b,z\}\). Besides monochromatic gaps already covered by \(b,z\), the only gap with a transition lies after \(z\) and reads \(1\,0^e\). Each factor \(1\,0^k\), \(1\le k\le e\le c\), has an occurrence beginning at the last one of the long one-run (position \(b\)), so it meets the marker \(b\). Zero-only factors also meet \(z\) at another occurrence, and one-only factors meet \(b\).

* If \(e>c\) but \(b\le3\), put \(p=\min(b,2)\) and take \(S=\{p,z,t\}\). The initial gap contains at most the factor \(01\) together with its one-symbol subfactors: \(01\) occurs again at positions \(z,z+1\), meeting \(z\). The gap between \(p\) and \(z\) is either entirely zero or a single one followed by at most \(c-1\) zeros. The factors \(1\,0^k\) from this gap have a second occurrence in the final \(1\,0^e\), meeting \(t\), since \(k<c<e\). Monochromatic factors can be shifted through \(p,z,t\). The only gap between \(z\) and \(t\) is a single one, already covered at \(p\).

* If \(e>c\), \(b\ge4\), but \(c\le2\), take \(S=\{c-1,b+c-1,t\}\). When \(c=1\), these are positions \(0,b,t\); its only nonmonochromatic gap is \(01\) (the middle zero and the isolated second one), also occurring at the beginning and meeting position zero. When \(c=2\), these are positions \(1,b+1,t\); the corresponding gap \(01\) also occurs at the beginning and meets position one. The other gaps consist exclusively of zeros or ones that can be shifted to intersect the selected occurrences of their respective symbols. Thus both cases give three-position attractors.

This proves the claimed upper bound outside the three simultaneous inequalities. Since the word contains both zero and one, no one-position set can attract its single-letter factors, so \(\gamma\ge2\).

**Four disjoint unique-factor occurrences.** Suppose now \(b\ge4,c\ge3,e>c\). The factors \(011\), \(110\), \(001\), and \(0^e\) occur exactly once. Indeed, \(011\) and \(110\) can involve only the long one-run and meet its left and right boundary respectively, because the other one-run has length one; \(001\) must end at the isolated second one, as the initial zero-run has length one; and \(0^e\) occurs only in the final zero-run, because \(e>c\) and the initial zero-run has length one. Their respective inclusive position intervals are
\[
[0,2],\quad [b-1,b+1],\quad [b+c-1,b+c+1],\quad
[b+c+2,b+c+e+1].
\]
The first two are disjoint because \(b\ge4\); the next two because \(c\ge3\); the last two are automatically disjoint. Every attractor must contain at least one position in each of these four intervals. Hence \(\gamma\ge4\), and the upper construction gives \(\gamma=4\).

**Enumeration.** Write \(b=4+k\), \(c=3+i\), \(e=c+1+j\), where \(i,j,k\ge0\). Then \(n=13+2i+j+k\); this proves the rational generating function. The coefficient of \(z^{n-13}\), for \(n\ge13\), equals
\[
\sum_{i=0}^{\lfloor(n-13)/2\rfloor}(n-12-2i)
=\left\lfloor\frac{(n-11)^2}{4}\right\rfloor.
\]
The number of positive triples \((b,c,e)\) summing to \(n-2\) is \(\binom{n-3}{2}\). Its leading term is \(n^2/2\), whereas \(Q_n=n^2/4+O(n)\), proving the limiting proportion \(1/2\). All claims follow.

## Verification

The self-contained Python checker \(\texttt{verify.py}\) reconstructs every distinct contiguous factor and the union of position masks of all its occurrences, independently tests the displayed marker sets, tests the unique-factor lower-bound certificates in the four-position regime, and computes exact minima by exhaustive search for every triple with \(1\le b,c,e\le6\). It checks the factor constructions for every triple with \(1\le b,c,e\le12\), 160 additional deterministic larger triples with lengths through 60 per parameter, and every enumeration coefficient for \(5\le n\le100\). It returned:

`VERIFY_OK exact_minima=216 complete_factor_witnesses=1728 random_large=160 fixed_length_counts=5..100`

The infinite statements are proved by the gap argument and exact unique-occurrence intervals; the finite checker is corroboration, not a substitute for these proofs. Run `python3 verify.py` from the directory containing this result.

## Relationship to prior work

Mantaci, Restivo, Romana, Rosone and Sciortino study smallest string attractors of standard Sturmian words, de Bruijn words and other structured word families, giving the standard definition and general bounds, but do not give an exact criterion for this two-singleton, five-run family [1]. Bannai, Goto, Ishihata, Kanda, Köppl and Nishimoto give general MAX-SAT formulations for exact computation of string attractors, not a parameter-uniform three-inequality classification or its rational length count [2]. Gheeraert, Romana and Stipulanti analyze prefixes of fixed points of certain morphisms associated with Parry numeration; those hypotheses do not imply the present criterion for arbitrary positive \((b,c,e)\) [3].

The new contribution is **the explicit entire-family sharp criterion and distribution**, not the definition of attractors, the generic factor-cover formulation, or the elementary observation that several disjoint unique occurrences yield a lower bound.

## Limitations

The theorem leaves the precise distinction between attractor number two and three open outside the four-position regime, and does not classify general five-run words with arbitrary outer and fourth run lengths. The probabilistic statement is conditional on the specified three-parameter family, not uniformly over all five-run binary words. Finite verification covers only the stated finite ranges. Exhaustive global priority among unpublished and unindexed works has not been established; an equivalent specialization may exist. No independent audit has been performed.

## References

[1] S. Mantaci, A. Restivo, G. Romana, G. Rosone, M. Sciortino, *String Attractors and Combinatorics on Words* (first public arXiv version 2019-07-10), arXiv:1907.04660, https://arxiv.org/abs/1907.04660; later journal treatment *A combinatorial view on string attractors*, Theoretical Computer Science 850 (2021), 236–248.

[2] H. Bannai, K. Goto, M. Ishihata, S. Kanda, D. Köppl, T. Nishimoto, *Computing NP-hard Repetitiveness Measures via MAX-SAT*, arXiv:2207.02571 (2022), https://arxiv.org/abs/2207.02571.

[3] F. Gheeraert, G. Romana, M. Stipulanti, *String attractors of some simple-Parry automatic sequences*, arXiv:2302.13647 (first public version 2023-02-27; revised 2024), https://arxiv.org/abs/2302.13647. This study explicitly gives primary MSC2020 68R15 for its related combinatorics-on-words setting.
